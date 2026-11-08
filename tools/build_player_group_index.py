#!/usr/bin/env python3
"""Map player component group add/remove operations to paths inside declared events."""
import collections
import json
import zipfile
from pathlib import Path
import json5

ROOT=Path(__file__).resolve().parents[1]
VERSIONS=[('1.6','SwordsAndMoreSwords.1.6.mcaddon','Sword_B'),('2.8.8','swordsandmoreswords_2_8_8.mcaddon','Swords_B'),('2.8.14','swordsandmoreswords-2-8-14.mcaddon','Swords_B')]

def gather(filename,pack):
    source=pack+'/entities/player.json'
    with zipfile.ZipFile(ROOT/'sources'/filename) as z:
        entity=json5.loads(z.read(source).decode('utf-8-sig'))['minecraft:entity']
    groups=entity.get('component_groups',{})
    refs=collections.defaultdict(lambda:{'add':[],'remove':[]})
    def walk(node,path):
        if isinstance(node,dict):
            for action in ('add','remove'):
                value=node.get(action)
                if isinstance(value,dict) and isinstance(value.get('component_groups'),list):
                    for group in value['component_groups']:
                        refs[group][action].append(path+'.'+action+'.component_groups')
            for key,value in node.items():walk(value,path+'.'+key)
        elif isinstance(node,list):
            for i,value in enumerate(node):walk(value,f'{path}[{i}]')
    for event,value in entity.get('events',{}).items():walk(value,'$.events.'+event)
    return source,groups,dict(refs)

def build(version,filename,pack):
    source,groups,refs=gather(filename,pack)
    names=sorted(set(groups)|set(refs))
    manual = '[прямых цепочках](chain-index-1.6.md) или [ручных цепочках 1.6](manual-traces-1.6.md)' if version=='1.6' else '[ручных цепочках 2.x](manual-traces-2.8.14.md) и [Clock/Time](manual-time-interactions-2.8.md)'
    lines=[f'# Добавление и удаление групп игрока — {version}', '',
           f'Автоматический индекс для `{source}`: все упоминания `add.component_groups` и `remove.component_groups` внутри событий этого файла, включая вложенные sequence/randomize. Ссылки — пути внутри разобранного объекта `minecraft:entity`; индекс показывает объявления, не вызовы и не последовательность исполнения.', '',
           '«Нет» значит только, что такой операции не найдено среди событий данного файла: другие события, команды, внешние пакеты, дефолты и правила разрешения наложенных компонентов могут влиять на результат. Не следует считать отсутствие remove доказательством постоянно действующего эффекта. Фильтры на ветвях и в вызывающих сенсорах смотреть в [реестре сущностей](entity-ledger-'+version+'.md), '+manual+'.', '',
           f'Объявлено групп: {len(groups)}. У групп с add без локального remove: {sum(bool(refs.get(g,{}).get("add")) and not refs.get(g,{}).get("remove") for g in groups)}. Ссылки на группы, не объявленные в player: {len(set(refs)-set(groups))}.', '',
           '| Группа | Есть определение | Добавление | Удаление |', '|---|---|---|---|']
    def format_paths(arr):return '<br>'.join('`'+x+'`' for x in arr) if arr else 'нет'
    for group in names:
        operations=refs.get(group,{'add':[],'remove':[]})
        lines.append(f'| `{group}` | {"да" if group in groups else "нет"} | {format_paths(operations["add"])} | {format_paths(operations["remove"])} |')
    lines.append('')
    return '\n'.join(lines)

def main():
    for version,filename,pack in VERSIONS:
        content=build(version,filename,pack)
        (ROOT/f'docs/player-groups-{version}.md').write_text(content,encoding='utf-8')
        print(version,len(content.splitlines()),'lines')

if __name__=='__main__':main()
