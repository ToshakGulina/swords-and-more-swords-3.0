#!/usr/bin/env python3
"""Index each Ice Sword on-use fill from source, with bounding-box volumes."""
from pathlib import Path
from zipfile import ZipFile
import json5

ROOT=Path(__file__).resolve().parents[1]

def axis(token):
    if not token.startswith('~'):raise ValueError('not relative: '+token)
    return int(token[1:] or '0')

def parse(command):
    parts=command.split()
    if len(parts)<16 or parts[0]!='execute' or not parts[1].startswith('@e[') or parts[5]!='fill':
        raise ValueError('unrecognised fill command: '+command)
    offset=tuple(axis(v) for v in parts[2:5]);ends=[axis(v) for v in parts[6:12]]
    bounds=[(min(a,b)+off,max(a,b)+off) for a,b,off in zip(ends[:3],ends[3:],offset)]
    volume=1
    for lo,hi in bounds:volume*=hi-lo+1
    return {'selector':parts[1],'offset':parts[2:5],'from':parts[6:9],'to':parts[9:12],'operation':' '.join(parts[12:]),'bounds':bounds,'volume':volume}

def collect():
    with ZipFile(ROOT/'sources/swordsandmoreswords_2_8_8.mcaddon') as a,ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as b:
        old=a.read('Swords_B/items/ice_sword.json');new=b.read('Swords_B/items/ice_sword.json')
    if old.replace(b'effect99:fake_ice',b'frosted_ice')!=new:raise ValueError('Unexpected change between item versions')
    item=json5.loads(new.decode('utf-8-sig'))['minecraft:item'];step=item['events']['on_use']['sequence'][0]['run_command'];commands=step['command']
    if len(commands)!=43 or step.get('target')!='holder':raise ValueError('Unexpected on_use command structure')
    fills=[parse(c) for c in commands[:40]]
    return item,fills,commands[40:]

def build():
    item,rows,tail=collect()
    out=['# Ice Sword 2.x: 40 последовательных fill on-use', '',
         'Списки из `Swords_B/items/ice_sword.json`, `events.on_use.sequence[0].run_command` с `target:holder`; команды перечислены в исходном порядке. В 2.8.8 вместо `frosted_ice` употреблено `effect99:fake_ice` во всех 40 позициях; исходные файлы побайтово совпадают после этой буквальной замены в памяти. Объём — включительный геометрический размер рамки, **не** число фактически изменённых блоков. Контекст старого execute, selectors, доступность блоков/чанков, состояния и приоритет изменений не проверены. Селекторы могут пересекаться. Нельзя считать `rm`/`r` доказанной геометрией в игре без эксперимента. [Ручное пояснение](manual-ice-geometry-2.8.md).','',
         '| № | Селектор | Execute-смещение | Fill от → до | Позиции рамки | Материал и фильтр |','|---:|---|---|---|---:|---|']
    for i,row in enumerate(rows,1):
        out.append(f'| {i} | `{row["selector"]}` | `{ " ".join(row["offset"]) }` | `{ " ".join(row["from"]) }` → `{ " ".join(row["to"]) }` | {row["volume"]} | `{row["operation"]}` |')
    out += ['', 'После этих команд в той же последовательности:', '']
    out.extend('- `'+command+'`' for command in tail)
    out += ['', 'Далее отдельным шагом sequence задан `damage` durability `6`, target `self`. Порядок команд и успешность не доказывают итоговый расход или выбор целей.']
    return '\n'.join(out)+'\n'

def main():
    (ROOT/'docs/ice-geometry-index.md').write_text(build(),encoding='utf-8')
    print('ice geometry index written')
if __name__=='__main__':main()
