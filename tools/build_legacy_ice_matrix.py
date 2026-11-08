#!/usr/bin/env python3
"""Compare declared 1.6 ice-controller targets with possible 2.x item targets."""
import re
from pathlib import Path
from zipfile import ZipFile
import json5
from build_ice_geometry import collect,parse
ROOT=Path(__file__).resolve().parents[1]

def collect_legacy():
    with ZipFile(ROOT/'sources/SwordsAndMoreSwords.1.6.mcaddon') as z:
        x=json5.loads(z.read('Sword_B/animation_controllers/ice_sword.json').decode('utf-8-sig'))['animation_controllers']['controller.animation.ice']['states']
    commands=x['ice']['on_entry']
    if len(commands)!=26 or x['default']['on_entry']!=['/Effect99']:raise ValueError('Unexpected Ice controller structure')
    rows=[]
    for number,cmd in enumerate(commands,1):
        if cmd.startswith('/execute @e[') and ' fill ' in cmd:
            row=parse(cmd[1:]);m=re.search(r'(?:\[|,)type=([^,\]]+)',row['selector'])
            if m is None:raise ValueError('missing type '+cmd)
            row['type']=m[1];row['source_number']=number;rows.append(row)
    if len(rows)!=22:raise ValueError('Unexpected target count')
    return x,rows

def build():
    states,old=collect_legacy();_,new,_=collect()
    excluded=set(re.findall(r'type=!([^,\]]+)',new[0]['selector']))
    out=['# Ice Sword 1.6: цели и потенциальные пересечения с 2.x', '',
         'Источник: `Sword_B/animation_controllers/ice_sword.json`, state `ice`, `on_entry`; номера — позиции в исходном списке из 26 команд. Здесь только 22 команды fill по типам. Все они используют `rm=5,r=12` относительно контекста helper; рамка задаётся относительно цели, материал `ice 0 replace air 0`. Объёмы — включительные размеры рамки, **не** фактическое число новых блоков. [Другие команды и ограничения](manual-ice-1.6.md).', '',
         'Последний столбец — лишь буквальные потенциальные соответствия в [40 командах on-use 2.x](ice-geometry-index.md). №1 — общий selector с `family=!fish` и `family=!effect99_entities`, поэтому присутствие типа не доказывает его выбора. Отдельные family-фильтры slime не равнозначны типу slime. Центр, момент, синтаксис, материал, исходный мир и расстояние различаются; это не тест поведения.', '',
         '| № 1.6 | Тип | Полный селектор 1.6 | Углы fill 1.6 | Объём | Потенциальные команды 2.x |', '|---:|---|---|---|---:|---|']
    for row in old:
        t=row['type']
        explicit=[str(i+1) for i,r in enumerate(new) if re.search(r'(?:\[|,)type='+re.escape(t)+r'(?:,|\])',r['selector'])]
        matches=[]
        if t not in excluded:matches.append('№1 при дополнительных family-условиях')
        if explicit:matches.append('type: №'+', '.join(explicit))
        if t=='slime':matches.append('family slime_large/medium/small: №3–8, не проверено соответствие типу')
        if not matches:matches=['буквально type не найден; требуется отдельная проверка']
        out.append(f'| {row["source_number"]} | `{t}` | `{row["selector"]}` | `{ " ".join(row["from"]) }` → `{ " ".join(row["to"]) }` | {row["volume"]} | '+ '; '.join(matches)+' |')
    out += ['', 'Другие четыре записи того же списка: №1–2 — 5×5 water/flowing_water под всеми `@a` при detect air, №17 — `detect ice` и `tp` slime, №26 — `scoreboard players set @a swords 2`. Значения и порядок выписаны в [ручном разборе](manual-ice-1.6.md); срабатывание состояний и команда default `/Effect99` не подтверждены игрой.']
    return '\n'.join(out)+'\n'

def main():
    (ROOT/'docs/ice-target-matrix-1.6.md').write_text(build(),encoding='utf-8')
    print('legacy Ice target matrix written')
if __name__=='__main__':main()
