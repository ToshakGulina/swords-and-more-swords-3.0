#!/usr/bin/env python3
"""Index animation controllers and trace literal 1.6 player sensor spawn chains."""
import json
import re
import zipfile
from pathlib import Path
import json5

ROOT=Path(__file__).resolve().parents[1]
VERSIONS=[('1.6','SwordsAndMoreSwords.1.6.mcaddon','Sword_B'),('2.8.8','swordsandmoreswords_2_8_8.mcaddon','Swords_B'),('2.8.14','swordsandmoreswords-2-8-14.mcaddon','Swords_B')]

def compact(x):return json.dumps(x,ensure_ascii=False,separators=(',',':'))
def walk(x):
    yield x
    if isinstance(x,dict):
        for y in x.values():yield from walk(y)
    elif isinstance(x,list):
        for y in x:yield from walk(y)
def read_json(raw):return json5.loads(raw.decode('utf-8-sig'))

def main():
 for version,filename,pack in VERSIONS:
    with zipfile.ZipFile(ROOT/'sources'/filename) as z:
        files={n:z.read(n) for n in z.namelist() if not n.endswith('/')}
    entities={}; errors=[]
    for path,raw in files.items():
        if path.startswith(pack+'/entities/') and path.endswith('.json'):
            try:
                entity=read_json(raw)['minecraft:entity'];ident=entity['description']['identifier']
                if ident in entities: raise ValueError(f'duplicate entity id {ident}')
                entities[ident]=(path,entity)
            except Exception as e: errors.append((path,str(e).splitlines()[0]))
    controllers={}; controller_errors=[]
    for path,raw in files.items():
        if path.startswith(pack+'/animation_controllers/') and path.endswith('.json'):
            try:
                obj=read_json(raw)
                for name in obj.get('animation_controllers',{}):
                    if name in controllers: raise ValueError(f'duplicate controller {name}')
                    controllers[name]=path
            except Exception as e: controller_errors.append((path,str(e).splitlines()[0]))
    out=[f'# Контроллеры поведения и прямые связи — {version}', '',
         'Автоматическая выписка из behavior pack: оригинальный текст каждого файла контроллеров и буквальные связи `description.animations` у разбираемых сущностей. Команды/условия, порядок состояний и пробелы сохранены в блоках ниже; ни фактический запуск контроллера, ни семантика команд не доказаны. Повторяющиеся JSON-ключи и неразобранные файлы требуют проверки оригинала. Не охвачены ресурсные контроллеры и вложенные/динамические вызовы. Списки ссылок не являются полным графом.', '']
    out+=['## Диагностика', '']
    for path,err in errors+controller_errors:out.append(f'- `{path}`: `{err}`')
    if not errors and not controller_errors:out.append('- Ошибок JSON5 при обработке файлов сущностей и контроллеров не обнаружено.')
    out+=['', '## Все файлы контроллеров', '']
    for path,raw in sorted(files.items()):
        if not (path.startswith(pack+'/animation_controllers/') and path.endswith('.json')):continue
        refs=[]
        names=[k for k,v in controllers.items() if v==path]
        for ident,(entitypath,entity) in sorted(entities.items()):
            anim=entity.get('description',{}).get('animations',{})
            if not isinstance(anim,dict):continue
            for alias, target in anim.items():
                if target in names:
                    refs.append(f'`{ident}` `{entitypath}`: alias `{alias}`, `scripts.animate` = `{compact(entity.get("description",{}).get("scripts",{}).get("animate"))}`')
        out += [f'### `{path}`','',f'Идентификаторы: `{compact(names)}`.', '', 'Буквальные ссылки description.animations: '+('; '.join(refs) if refs else 'не найдены среди разобранных сущностей; отсутствие не доказывает неиспользования.')+'.','', '```json',raw.decode('utf-8-sig').rstrip(), '```','']
    (ROOT/'docs'/f'animation-ledger-{version}.md').write_text('\n'.join(out)+'\n',encoding='utf-8')
    if version!='1.6':continue
    player=entities['minecraft:player'][1]
    sensors=player.get('components',{}).get('minecraft:environment_sensor',[])
    items={}
    for name,raw in files.items():
        if name.startswith(pack+'/items/') and name.endswith('.json'):
            item=read_json(raw)['minecraft:item'];items[item['description']['identifier']]=name
    out=['# Связи предметов 1.6: sensor → player group → spawn entity → controller','',
         'Автоматический обзор только по прямым буквальным связям в `Sword_B/entities/player.json`: sensor содержит точный item ID, затем event по имени, `add.component_groups`, компоненты `minecraft:spawn_entity` в этих группах, ID сущности и её `description.animations`. Непосредственные проверки других сущностей, косвенные события, команды, список animate, значения по умолчанию, ошибки парсинга и ресурсы могут менять или обрывать цепь. Отсутствие найденной ссылки не доказывает отсутствия механики. Оригинальные контроллеры полностью приведены в [реестре контроллеров](animation-ledger-1.6.md).', '']
    for ident,itempath in sorted(items.items()):
        matched=[s for s in sensors if any(isinstance(n,dict) and n.get('test')=='has_equipment' and n.get('value')==ident for n in walk(s))]
        out += [f'## `{ident}`', '',f'- Предмет: `{itempath}`.',f'- Совпадений sensor: {len(matched)}.','']
        for sensor in matched:
            event=sensor.get('on_environment',{}).get('event')
            value=player.get('events',{}).get(event)
            out += [f'- Sensor: `{compact(sensor)}`',f'- Event `{event}`: `{compact(value)}`']
            groups=[]
            for node in walk(value):
                if isinstance(node,dict) and isinstance(node.get('add'),dict):groups+=node['add'].get('component_groups',[])
            for group in dict.fromkeys(groups):
                group_data=player.get('component_groups',{}).get(group)
                out.append(f'- Группа `{group}`: `{compact(group_data)}`')
                spawns=[]
                for n in walk(group_data):
                    if isinstance(n,dict) and isinstance(n.get('spawn_entity'),str):spawns.append(n['spawn_entity'])
                for spawn in dict.fromkeys(spawns):
                    target=entities.get(spawn)
                    if target is None:
                        out.append(f'  - `{spawn}`: определение не найдено или не разобрано; проверить оригинал.')
                        continue
                    ep,ent=target;desc=ent.get('description',{});anims=desc.get('animations',{})
                    out.append(f'  - `{spawn}`: `{ep}`; scripts `{compact(desc.get("scripts",{}))}`, animations `{compact(anims)}`.')
                    if isinstance(anims,dict):
                        for alias,controller in anims.items():out.append(f'    - `{alias}` → `{controller}` → `{controllers.get(controller,"не найден в разобранных файлах")}`.')
            out.append('')
    (ROOT/'docs/chain-index-1.6.md').write_text('\n'.join(out)+'\n',encoding='utf-8')
    print(version,'items',len(items),'entities',len(entities),'controllers',len(controllers),'errors',len(errors))

if __name__=='__main__':main()
