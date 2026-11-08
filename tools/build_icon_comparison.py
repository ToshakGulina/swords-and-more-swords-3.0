#!/usr/bin/env python3
"""Compare source item-icon PNGs by exact ID, bytes and decoded RGBA."""
from hashlib import sha256
from io import BytesIO
from pathlib import Path
from zipfile import ZipFile
import json5
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
VERSIONS=(('1.6','SwordsAndMoreSwords.1.6.mcaddon','Sword_R'),('2.8.8','swordsandmoreswords_2_8_8.mcaddon','Swords_R'),('2.8.14','swordsandmoreswords-2-8-14.mcaddon','Swords_R'))

def load(filename,pack):
    results={}
    with ZipFile(ROOT/'sources'/filename) as z:
        paths=set(z.namelist());atlas=json5.loads(z.read(pack+'/textures/item_texture.json').decode('utf-8-sig'))['texture_data']
        for p in sorted(paths):
            if '_B/items/' not in p or not p.endswith('.json'):continue
            item=json5.loads(z.read(p).decode('utf-8-sig'))['minecraft:item'];ident=item['description']['identifier'];icon=item['components'].get('minecraft:icon')
            key=icon.get('texture') if isinstance(icon,dict) else icon
            definition=atlas.get(key)
            if not isinstance(definition,dict) or not isinstance(definition.get('textures'),str):
                raise ValueError(f'Unsupported icon or atlas entry: {p}: {icon!r}: {definition!r}')
            path=pack+'/'+definition['textures']+'.png'
            if path not in paths:raise ValueError(f'Icon not found: {ident}: {path}')
            raw=z.read(path)
            with Image.open(BytesIO(raw)) as im:
                if getattr(im,'n_frames',1)!=1:raise ValueError(f'Animated icon needs explicit frame handling: {path}')
                rgba=im.convert('RGBA');size=rgba.size;pixels=rgba.tobytes()
            if ident in results:raise ValueError(f'Duplicate item ID: {ident}')
            results[ident]={'path':path,'icon':key,'bytes_sha256':sha256(raw).hexdigest(),'size':size,'pixels':pixels}
    return results

def compare(a,b):
    if a is None or b is None:return 'нет ID'
    if a['size']!=b['size']:return 'другой размер'
    if a['pixels']==b['pixels']:return 'RGBA совпадают'
    # Count full RGBA-pixel differences, including RGB of transparent pixels.
    diffs=sum(a['pixels'][i:i+4]!=b['pixels'][i:i+4] for i in range(0,len(a['pixels']),4))
    return f'различаются {diffs} пикс.'

def build():
    data={version:load(filename,pack) for version,filename,pack in VERSIONS}
    a,b,c=[data[v] for v,_,_ in VERSIONS];ids=sorted(set(a)|set(b)|set(c))
    matched=sorted(set(a)&set(c));diffs=[i for i in matched if compare(a[i],c[i])!='RGBA совпадают']
    out=['# Сопоставление исходных значков предметов', '',
         'Автоматическое разрешение `minecraft:icon` через локальный `textures/item_texture.json` и PNG. Сопоставление версий — **только по точному item ID**, без догадок о переименованиях. Размер указан в пикселях. PNG «байты одинаковы» сравниваются по SHA-256; «RGBA совпадают» — после декодирования Pillow, при совпадении размеров; многокадровый PNG вызывает ошибку генерации. Различия RGBA включают цвета полностью прозрачных пикселей и не являются визуальной оценкой. Рендер, материалы, анимации и масштаб в игре не проверены. Полные исходные пути и хэши каждого ассета: [1.6](assets-1.6.md), [2.8.8](assets-2.8.8.md), [2.8.14](assets-2.8.14.md).', '',
         f'Охват: 1.6 — {len(a)} ID; 2.8.8 — {len(b)}; 2.8.14 — {len(c)}; общих между 1.6 и 2.8.14 — {len(matched)}. Различаются размером или RGBA — {len(diffs)} из {len(matched)}; PNG обеих 2.x нужно оценивать по колонке ниже. Пробел в одной версии означает отсутствие именно этого ID, не обязательно отсутствие аналогичного предмета.', '',
         '| Точный ID | 1.6 размер | 2.8.14 размер | 1.6 ↔ 2.8.14 RGBA | 2.8.8 ↔ 2.8.14 PNG байты |','|---|---:|---:|---|---|']
    def size(v):return f"{v['size'][0]}×{v['size'][1]}" if v else '—'
    for ident in ids:
        x,y,z=a.get(ident),b.get(ident),c.get(ident)
        eq='да' if y and z and y['bytes_sha256']==z['bytes_sha256'] else 'нет' if y and z else 'нет ID'
        out.append(f'| `{ident}` | {size(x)} | {size(z)} | {compare(x,z)} | {eq} |')
    return '\n'.join(out)+'\n'

def main():
    (ROOT/'docs/icon-comparison.md').write_text(build(),encoding='utf-8')
    print('icon comparison written')

if __name__=='__main__':main()
