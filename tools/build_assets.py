#!/usr/bin/env python3
"""Lossless metadata inventory of image and audio assets in supplied archives."""
from pathlib import Path
from io import BytesIO
import hashlib, json, zipfile
import json5
from PIL import Image
from mutagen import File

ROOT=Path(__file__).resolve().parents[1]
VERSIONS={'1.6':'SwordsAndMoreSwords.1.6.mcaddon','2.8.8':'swordsandmoreswords_2_8_8.mcaddon','2.8.14':'swordsandmoreswords-2-8-14.mcaddon'}


def main():
 for version,filename in VERSIONS.items():
  with zipfile.ZipFile(ROOT/'sources'/filename) as z:
   data={n:z.read(n) for n in z.namelist() if not n.endswith('/')}
  out=[f'# Ресурсы архива {version}', '', 'Машинная инвентаризация медиа и буквального сопоставления значков. Хэши — исходных файлов, размер картинок — пиксели; это не визуальная или слуховая проверка, а длительность звука — оценка декодера. Текстуры, модели, анимации и условия рендеринга могут связываться косвенно. При сопоставлении значков выводятся только существующие файлы в ресурсном пакете с явно указанным путём; массивы и составные определения приводятся буквально. Отсутствие совпадения не доказывает отсутствия ресурса.', '', '## Все изображения', '', '| Путь | Формат | Размер | Режим | SHA-256 |', '|---|---|---|---|---|']
  for name,raw in sorted(data.items()):
   if Path(name).suffix.lower() not in ('.png','.jpeg','.jpg','.tga'):continue
   try:
    with Image.open(BytesIO(raw)) as im:
     val=f'{im.format} | {im.width} × {im.height} | {im.mode}'
   except Exception as e: val=f'ошибка: {type(e).__name__} | — | —'
   out.append(f'| `{name}` | {val} | `{hashlib.sha256(raw).hexdigest()}` |')
  out += ['', '## Все звуковые файлы', '', '| Путь | Кодек | Длительность (с) | Частота (Гц) | Каналы | SHA-256 |', '|---|---|---:|---:|---:|---|']
  for name,raw in sorted(data.items()):
   if Path(name).suffix.lower() not in ('.ogg','.wav','.mp3','.flac'):continue
   try:
    a=File(BytesIO(raw));info=a.info;vals=f'{type(info).__name__} | {info.length:.6f} | {getattr(info,"sample_rate","—")} | {getattr(info,"channels","—")}'
   except Exception as e: vals=f'ошибка: {type(e).__name__} | — | — | —'
   out.append(f'| `{name}` | {vals} | `{hashlib.sha256(raw).hexdigest()}` |')
  out += ['', '## Значки предметов и item_texture', '', '| Предмет / файл | Ключ значка | Определение в item_texture | Существующие пути |', '|---|---|---|---|']
  atlases=[]
  for name,raw in data.items():
   if name.endswith('/textures/item_texture.json'):
    try: atlases.append((name,json5.loads(raw.decode('utf-8-sig')).get('texture_data',{})))
    except Exception as e: out.append(f'Ошибка `{name}`: `{type(e).__name__}`')
  def strings(v):
   if isinstance(v,str):return [v]
   if isinstance(v,dict):return sum((strings(x) for x in v.values()),[])
   if isinstance(v,list):return sum((strings(x) for x in v),[])
   return []
  for name,raw in sorted(data.items()):
   if '_B/items/' not in name or not name.endswith('.json'):continue
   try:
    item=json5.loads(raw.decode('utf-8-sig'))['minecraft:item'];icon=item.get('components',{}).get('minecraft:icon');key=icon.get('texture') if isinstance(icon,dict) else icon
   except Exception as e:
    out.append(f'| `{name}` | ошибка `{type(e).__name__}` | — | — |');continue
   matches=[];defs=[]
   for atlas,mapping in atlases:
    v=mapping.get(key) if isinstance(key,str) else None
    if v is None:continue
    defs.append(f'{atlas}: {json.dumps(v,ensure_ascii=False,separators=(",",":"))}')
    base=atlas.split('/textures/item_texture.json')[0]
    for s in strings(v):
     for suffix in ('','.png','.tga','.jpeg','.jpg'):
      p=base+'/'+s+suffix
      if p in data:matches.append(p)
   esc=lambda s: str(s).replace('|','\\|').replace('`','\\`')
   out.append(f'| `{esc(item.get("description",{}).get("identifier",name))}` | `{esc(key)}` | `{esc("; ".join(defs) or "—")}` | `{esc("; ".join(matches) or "—")}` |')
  (ROOT/'docs'/f'assets-{version}.md').write_text('\n'.join(out)+'\n',encoding='utf-8')
  print(version)

if __name__=='__main__': main()
