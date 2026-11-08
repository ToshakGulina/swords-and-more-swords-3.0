#!/usr/bin/env python3
"""Compare explicitly enumerated target types in four 1.6 controllers."""
from pathlib import Path
from zipfile import ZipFile
import re
import json5

ROOT=Path(__file__).resolve().parents[1]
ARCHIVE=ROOT/'sources/SwordsAndMoreSwords.1.6.mcaddon'
CONFIG=(
    ('Wither','wither','wither',r'/execute @e\[scores=\{w=100\},r=16,type=([^\]]+)\] ~ ~ ~ summon entity:explode','summon entity:explode'),
    ('Creeper','creeper','default',r'/execute @e\[scores=\{c=100\},r=16,type=([^\]]+)\] ~ ~ ~ summon entity:explode','summon entity:explode'),
    ('Ender','ender','default',r'/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e\[r=10,rm=5,type=([^\]]+)\]','spreadplayers ~ ~ 8 16 @e['),
    ('TNT','tnt','default',r'/execute @e\[r=15,rm=10,type=([^\]]+)\] ~ ~ ~ summon entity:explode','summon entity:explode'),
)

def collect():
    results={}
    with ZipFile(ARCHIVE) as z:
        for label,name,state,pattern,needle in CONFIG:
            path=f'Sword_B/animation_controllers/{name}_sword.json'
            obj=json5.loads(z.read(path).decode('utf-8-sig'))['animation_controllers'][f'controller.animation.{name}']['states'][state]
            pairs=[]
            for i,cmd in enumerate(obj['on_entry'],1):
                if needle not in cmd:continue
                match=re.fullmatch(pattern,cmd)
                if not match:raise ValueError(f'Unexpected {label} command at {path}:{state}[{i}]: {cmd}')
                pairs.append((match.group(1),i))
            if len({name for name,_ in pairs})!=len(pairs):raise ValueError(f'Duplicate target in {label}')
            results[label]=pairs
    return results

def build(results):
    order=list(dict.fromkeys(name for pairs in results.values() for name,_ in pairs))
    maps={label:dict(pairs) for label,pairs in results.items()}
    out=['# Целевые типы четырёх контроллеров 1.6','',
         'Воспроизводимое буквальное сравнение команд из Wither (`wither` state), Creeper (`default`), Ender (`default`) и TNT (`default`). Цифра — позиция команды в списке `on_entry`, начиная с 1; «—» означает отсутствие среди команд именно этого вида, а не полную неуязвимость типа или отсутствие других эффектов. Условия/radius/центры отличаются; таблица не доказывает работу селекторов, совместимость ID или фактическое исполнение.', '',
         '- Wither: `@e[scores={w=100},r=16,type=…]` → `summon entity:explode`; default содержит только `/Effect99`.',
         '- Creeper: `@e[scores={c=100},r=16,type=…]` → `summon entity:explode`.',
         '- Ender: `execute @p` → `spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=…]`; у этих 27 команд нет score-фильтра.',
         '- TNT: `@e[r=15,rm=10,type=…]` → `summon entity:explode`, без score-фильтра.', '',
         'Число отдельных команд/типов: '+', '.join(f'{label} {len(pairs)}' for label,pairs in results.items())+'. Позиции и порядок — по исходному JSON; полные команды и другие состояния: [реестр контроллеров](animation-ledger-1.6.md), [ручной разбор](manual-area-targets-1.6.md).', '',
         '| Буквальный type | Wither | Creeper | Ender | TNT |','|---|---:|---:|---:|---:|']
    for name in order:
        out.append('| `'+name+'` | '+' | '.join(str(maps[label].get(name,'—')) for label, *_ in CONFIG)+' |')
    return '\n'.join(out)+'\n'

def main():
    text=build(collect())
    (ROOT/'docs/target-matrix-1.6.md').write_text(text,encoding='utf-8')
    print('target matrix written')

if __name__=='__main__':main()
