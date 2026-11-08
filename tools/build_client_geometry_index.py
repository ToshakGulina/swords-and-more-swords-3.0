#!/usr/bin/env python3
"""Extract local resource-pack model files and literal client geometry aliases."""
from collections import defaultdict
from hashlib import sha256
from pathlib import Path
from zipfile import ZipFile
import json,json5
from build_quick_reference import slug
ROOT=Path(__file__).resolve().parents[1]
VERSIONS=(('1.6','SwordsAndMoreSwords.1.6.mcaddon','Sword_R'),('2.8.8','swordsandmoreswords_2_8_8.mcaddon','Swords_R'),('2.8.14','swordsandmoreswords-2-8-14.mcaddon','Swords_R'))

def collect(filename,pack):
    files=[];geometry=[];aliases=defaultdict(list);errors=[];duplicates=[]
    with ZipFile(ROOT/'sources'/filename) as z:
        paths=[p for p in sorted(z.namelist()) if (p.startswith(pack+'/models/') or p.startswith(pack+'/entity/')) and p.endswith('.json')]
        for path in paths:
            repeated=[]
            def pairs(seq):
                out={}
                for k,v in seq:
                    if k in out:repeated.append(k)
                    out[k]=v
                return out
            raw=z.read(path)
            try:obj=json5.loads(raw.decode('utf-8-sig'),object_pairs_hook=pairs)
            except (ValueError,UnicodeDecodeError) as ex:errors.append((path,str(ex).splitlines()[0]));continue
            if repeated:duplicates.append((path,repeated))
            if path.startswith(pack+'/models/'):
                files.append({'path':path,'sha256':sha256(raw).hexdigest(),'object':obj})
                if 'minecraft:geometry' in obj:
                    if not isinstance(obj['minecraft:geometry'],list):raise ValueError('non-array geometry '+path)
                    for i,g in enumerate(obj['minecraft:geometry']):
                        desc=g.get('description',{});ident=desc.get('identifier')
                        if not isinstance(ident,str):raise ValueError('geometry without id '+path)
                        geometry.append({'path':path,'id':ident,'where':f'minecraft:geometry[{i}]','format_version':obj.get('format_version'),'data':g,'description':desc,'modern':True})
                for ident,g in obj.items():
                    if ident.startswith('geometry.'):
                        if not isinstance(g,dict):raise ValueError('unexpected legacy geometry '+path)
                        geometry.append({'path':path,'id':ident,'where':ident,'format_version':obj.get('format_version'),'data':g,'description':g,'modern':False})
            else:
                desc=obj.get('minecraft:client_entity',{}).get('description',{});mapping=desc.get('geometry',{})
                if not isinstance(mapping,dict):raise ValueError('unexpected geometry aliases '+path)
                for name,target in mapping.items():
                    if isinstance(target,str):aliases[target].append((path,desc.get('identifier'),name))
    return files,geometry,dict(aliases),errors,duplicates

def declared(obj,key):return '`'+json.dumps(obj[key],ensure_ascii=False,separators=(',',':'))+'`' if key in obj else '—'

def build():
    data={v:collect(f,p) for v,f,p in VERSIONS};old=data['1.6'];a=data['2.8.8'];b=data['2.8.14']
    if a!=b:raise ValueError('2.x model source or geometry aliases differ')
    if old[0]:raise ValueError('unexpected 1.6 resource models')
    files,geometries,aliases,errors,dups=b
    out=['# Клиентская геометрия: модели, кости и полные определения', '',
         f'В `Sword_R/models/` 1.6 не обнаружено локальных JSON-моделей: это не исключает ванильную или внешнюю геометрию. В 2.x JSON-файлов: **{len(files)}**, объявлений geometry: **{len(geometries)}**. Сопоставлены оригинальные SHA-256 файлов и разобранные client aliases 2.8.8/2.8.14: эти данные совпадают; остальные файлы пакетов могут различаться.', '',
         'Таблица показывает исходный format_version, расположение, прямо записанные размеры текстуры, количество элементов массива `bones` и количество прямо записанных `cubes`. `—` означает отсутствие поля; число кубов не включает прочие возможные формы геометрии. Это размеры разметки модели, не проверка размера присоединяемой PNG. Столбец aliases ищет точные ID только в `description.geometry` разобранных client entities: отсутствие там не означает отсутствие ссылок из блоков, render controllers, иных файлов или ванильных ресурсов.', '',
         'Ниже полностью сохранён разобранный JSON каждого локального model-файла, включая имена/иерархию костей, pivot, origin, size, rotation, inflate, UV и все остальные поля как в исходной структуре. Оба синтаксиса `minecraft:geometry` и legacy-корня `geometry.*` сохраняются раздельно. Комментарии и форматирование JSON5 не сохраняются; исходные файлы архивов остаются эталоном.', '',
         '- Ошибки разбора: '+('; '.join(f'`{p}` ({err})' for p,err in errors) if errors else 'нет')+'.',
         '- Повторные ключи: '+('; '.join(f'`{p}`: '+', '.join('`'+x+'`' for x in ks) for p,ks in dups) if dups else 'нет')+'. JSON5 сохраняет последнее значение.', '',
         '| ID / файл | Расположение / format_version | Размеры текстуры | bones / объявленные cubes | Прямые client aliases |','|---|---|---|---|---|']
    for g in geometries:
        desc=g['description'];width='texture_width' if g['modern'] else 'texturewidth';height='texture_height' if g['modern'] else 'textureheight';bones=g['data'].get('bones')
        if 'bones' not in g['data']:counts='— / —'
        else:
            if not isinstance(bones,list) or any(not isinstance(x,dict) or ('cubes' in x and not isinstance(x['cubes'],list)) for x in bones):raise ValueError('unsupported bone shape '+g['id'])
            counts=f'{len(bones)} / {sum(len(x.get("cubes",[])) for x in bones)}'
        refs='<br>'.join(f'`{p}` · `{ident}` · `{name}`' for p,ident,name in aliases.get(g['id'],[])) or 'не найдено в client entity'
        out.append(f'| `{g["id"]}`<br>`{g["path"]}` | `{g["where"]}`<br>`{g["format_version"]}` | {declared(desc,width)} × {declared(desc,height)} | {counts} | {refs} |')
    out += ['', '## Полные файлы моделей', '']
    for f in files:
        out += [f'### `{f["path"]}`', '',f'- SHA-256 исходного файла: `{f["sha256"]}`.', '', '```json',json.dumps(f['object'],ensure_ascii=False,indent=2),'```','']
    out += ['Текстуры, ID и прочие связи: [граф ресурсов](resource-graph-2.8.14.md) · [медиа и хэши](assets-2.8.14.md) · [локальные анимации](client-animation-index.md).','']
    return '\n'.join(out)

def main():
    (ROOT/'docs/client-geometry-index.md').write_text(build(),encoding='utf-8');print('client geometry index written')
if __name__=='__main__':main()
