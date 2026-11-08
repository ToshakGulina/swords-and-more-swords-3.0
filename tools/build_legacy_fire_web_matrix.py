#!/usr/bin/env python3
"""Index Fire/Magma/Spider helper target types without assuming selector semantics."""
from pathlib import Path
from zipfile import ZipFile
import re,json5
ROOT=Path(__file__).resolve().parents[1]

def collect():
    results={}
    with ZipFile(ROOT/'sources/SwordsAndMoreSwords.1.6.mcaddon') as z:
        for name in ('fire','magma','spider'):
            states=json5.loads(z.read(f'Sword_B/animation_controllers/{name}_sword.json').decode('utf-8-sig'))['animation_controllers'][f'controller.animation.{name}']['states']
            commands=states['default']['on_entry']
            if commands!=states[name]['on_entry']:raise ValueError('states differ: '+name)
            expression=(r'/execute @e\[r=5,type=([^,\]]+)\] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air' if name=='spider'
                        else r'/execute @e\[r=15,rm=2,type=([^,\]]+)\] ~ ~ ~ setblock ~ ~ ~ fire')
            targets={}
            for no,command in enumerate(commands,1):
                m=re.fullmatch(expression,command)
                if m:
                    if m[1] in targets:raise ValueError('duplicate type: '+m[1])
                    targets[m[1]]=no
            if len(targets)!={'fire':31,'magma':21,'spider':25}[name]:raise ValueError('unexpected target count: '+name)
            results[name]=(states,targets)
    return results

def build():
    data=collect();types=sorted(set().union(*(set(t) for _,t in data.values())))
    out=['# 1.6: цели Fire, Magma и Spider', '',
         'В каждом из трёх контроллеров `default` и одноимённое состояние содержат одинаковые `on_entry` в одном порядке. Таблица сравнивает **только** отдельные команды по явному `type`; отсутствующие в ней команды с `@p`, `@a`, scoreboard и условиями разбираются [отдельно](manual-fire-magma-spider-1.6.md). Не включены потенциальные family, aliases, vanilla или другие файлы. Совпадение типов не доказывает одновременного срабатывания.', '',
         'Fire и Magma: `@e[r=15,rm=2,type=...] ~ ~ ~ setblock ~ ~ ~ fire`. Spider: `@e[r=5,type=...] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air`. Номера — позиции в `on_entry`, применимые к обоим состояниям соответствующего контроллера. Центр выбора — контекст helper, не обязательно текущая позиция владельца. Результат команд в игре не проверен.', '',
         '| Точный type | Fire № | Magma № | Spider № |', '|---|---:|---:|---:|']
    for t in types:
        values=[str(data[n][1][t]) if t in data[n][1] else '—' for n in ('fire','magma','spider')]
        out.append(f'| `{t}` | '+' | '.join(values)+' |')
    out += ['', f'Итого: Fire {len(data["fire"][1])}, Magma {len(data["magma"][1])}, Spider {len(data["spider"][1])} типов; объединение {len(types)}. `—` означает только отсутствие соответствующей отдельной type-команды в этом списке.']
    return '\n'.join(out)+'\n'

def main():
    (ROOT/'docs/fire-web-targets-1.6.md').write_text(build(),encoding='utf-8');print('fire/web target matrix written')
if __name__=='__main__':main()
