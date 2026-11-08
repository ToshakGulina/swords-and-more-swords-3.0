#!/usr/bin/env python3
"""Inventory resource identifiers and literal references without assuming vanilla is absent."""
import collections,json,zipfile
from pathlib import Path
import json5

ROOT=Path(__file__).resolve().parents[1]
VERSIONS=[('1.6','SwordsAndMoreSwords.1.6.mcaddon','Sword_R'),('2.8.8','swordsandmoreswords_2_8_8.mcaddon','Swords_R'),('2.8.14','swordsandmoreswords-2-8-14.mcaddon','Swords_R')]
def compact(x):return json.dumps(x,ensure_ascii=False,separators=(',',':'))
def resolve(mapping,key): return ', '.join('`'+x+'`' for x in sorted(set(mapping.get(key,[])))) or 'не найдено локально (возможно ванильный ресурс)'
def main():
 for version,filename,pack in VERSIONS:
  with zipfile.ZipFile(ROOT/'sources'/filename) as z:files={n:z.read(n) for n in z.namelist() if not n.endswith('/')}
  parsed={}; errors=[]
  for path,data in sorted(files.items()):
   if not path.startswith(pack+'/') or not path.endswith(('.json','.material')):continue
   duplicates=[]
   def pairs(xs):
    d={}
    for k,v in xs:
     if k in d:duplicates.append(k)
     d[k]=v
    return d
   try:
    parsed[path]=json5.loads(data.decode('utf-8-sig'),object_pairs_hook=pairs)
    if duplicates:errors.append((path,'повторные ключи '+compact(duplicates)))
   except Exception as e:errors.append((path,'JSON5: '+str(e).splitlines()[0]))
  indices={x:collections.defaultdict(list) for x in ('geometry','animation','animation_controller','render_controller','particle','client_entity')}
  for path,obj in parsed.items():
   if not isinstance(obj,dict):continue
   for g in obj.get('minecraft:geometry',[]) if isinstance(obj.get('minecraft:geometry',[]),list) else []:
    ident=g.get('description',{}).get('identifier') if isinstance(g,dict) else None
    if isinstance(ident,str):indices['geometry'][ident].append(path)
   for ident in obj:
    if ident.startswith('geometry.'):indices['geometry'][ident].append(path)
   for section,key in [('animations','animation'),('animation_controllers','animation_controller'),('render_controllers','render_controller')]:
    if isinstance(obj.get(section),dict):
     for ident in obj[section]:indices[key][ident].append(path)
   part=obj.get('particle_effect',{});ident=part.get('description',{}).get('identifier') if isinstance(part,dict) else None
   if ident:indices['particle'][ident].append(path)
   ent=obj.get('minecraft:client_entity',{});ident=ent.get('description',{}).get('identifier') if isinstance(ent,dict) else None
   if ident:indices['client_entity'][ident].append(path)
  out=[f'# Клиентские ресурсы и буквальные связи — {version}', '',
       'Автоматическое сопоставление определённых в resource pack идентификаторов и путей. «Не найдено локально» не означает ошибки: многие модели, анимации, текстуры и контроллеры являются ванильными или могут поступать из других пакетов. Списки не доказывают работающий рендер, не интерпретируют условия Molang и не обрабатывают динамические ссылки. JSON5 сохраняет только последнее значение повторённого ключа: при диагностике сверять оригинал. Полные исходные файлы и имена компонентов остаются в архиве.', '', '## Ошибки и повторные ключи', '']
  out += [f'- `{p}`: `{e}`' for p,e in errors] or ['- Не обнаружены парсером JSON5.']
  out += ['', '## Локальные определения и совпадения ID', '']
  for category,mapping in indices.items():
   out += [f'### {category}', '', '| ID | Определения в пакете |', '|---|---|']
   out += [f'| `{ident}` | {resolve(mapping,ident)} |' for ident in sorted(mapping)] or ['| — | — |']
   out.append('')
  out += ['## Описания клиентских сущностей и ссылки', '']
  for ident,paths in sorted(indices['client_entity'].items()):
   for path in sorted(paths):
    desc=parsed[path]['minecraft:client_entity']['description']
    out += [f'### `{ident}` — `{path}`','',f'- Полный `description`: `{compact(desc)}`','']
    for alias,value in desc.get('textures',{}).items():
     if not isinstance(value,str):continue
     paths2=[pack+'/'+value+ext for ext in ('.png','.tga','.jpg','.jpeg') if pack+'/'+value+ext in files]
     out.append(f'- texture `{alias}` → `{value}` → '+(', '.join(f'`{p}`' for p in paths2) if paths2 else 'не найдено локально (возможно ванильный ресурс)'))
    for alias,value in desc.get('geometry',{}).items():
     if isinstance(value,str):out.append(f'- geometry `{alias}` → `{value}` → {resolve(indices["geometry"],value)}')
    for alias,value in desc.get('animations',{}).items():
     if not isinstance(value,str):continue
     kind='animation_controller' if value.startswith('controller.animation.') else 'animation'
     out.append(f'- animation `{alias}` → `{value}` → {resolve(indices[kind],value)}')
    for element in desc.get('render_controllers',[]) or []:
     for value in ([element] if isinstance(element,str) else element.keys() if isinstance(element,dict) else []):
      out.append(f'- render controller `{value}` → {resolve(indices["render_controller"],value)}')
    out.append('')
  out += ['## Объявления звуков и текстуры flipbook', '']
  for path,obj in parsed.items():
   if path.endswith('/sounds/sound_definitions.json') or path.endswith('/sounds.json') or path.endswith('/textures/flipbook_textures.json'):
    out += [f'### `{path}`','', '```json',json.dumps(obj,ensure_ascii=False,indent=2),'```','']
  (ROOT/'docs'/f'resource-graph-{version}.md').write_text('\n'.join(out)+'\n',encoding='utf-8')
  print(version,'parsed',len(parsed),'client_entities',sum(map(len,indices['client_entity'].values())),'errors/duplicates',len(errors))

if __name__=='__main__':main()
