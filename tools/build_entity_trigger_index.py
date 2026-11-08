#!/usr/bin/env python3
"""Complete literal timer, sensor and ageable declarations in parsed entities."""
from pathlib import Path
from collections import Counter
from build_entity_group_index import VERSIONS
from build_entity_combat_index import extract,code
ROOT=Path(__file__).resolve().parents[1]
KEYS=('minecraft:timer','minecraft:environment_sensor','minecraft:block_sensor','minecraft:ageable','minecraft:on_target_acquired','minecraft:on_wake_with_owner')

def render(title,ver,data):
    rows,errors,duplicates,files=data;counts=Counter(x[3] for x in rows);timers=[value for _,_,_,key,value in rows if key=='minecraft:timer'];empty=sum(v=={} for v in timers)
    missing={k:sum(isinstance(v,dict) and k not in v for v in timers) for k in ('time','looping','randomInterval','time_down_event')}
    out=[f'# Таймеры, сенсоры и возраст сущностей — {title}', '',
         f'Из {files} разобранных entity-файлов извлечено **{len(rows)}** компонентов с {len(KEYS)} выбранными точными ключами только из базового `components` и `component_groups`. Полные значения сохраняют вложенные события, target, фильтры и порядок списков. В 2.x базовый sensor player содержит множество отдельных элементов; [отдельная таблица player](player-sensor-index.md) показывает их по одному.', '',
         'Это буквальные объявления, а не доказанные активные таймеры или последовательность срабатываний. Группы могут быть неактивны, вытесняться другими или включаться по разным событиям; repeat/random, пропущенные поля, target и область исполнения не следует дополнять значениями по умолчанию. Числа `time`, `duration` и другие величины сохранены в единицах исходных полей; одинаковый формат значений в разных компонентах не доказывает одинаковую семантику. Неточности JSON и внешние/ванильные определения остаются вне структурного разбора.', '',
         'Количество выбранных компонентов: '+', '.join(f'`{key}` — {counts[key]}' for key in KEYS)+'.',
         f'У `{len(timers)}` записей timer: пустых объектов {empty}; отсутствуют поля '+', '.join(f'`{k}` — {v}' for k,v in missing.items())+'. Отсутствие поля отдельно от явного false, null, нуля или пустого списка.', '',
         '- Неразобранные JSON: '+('; '.join(f'`{p}` ({err})' for p,err in errors) if errors else 'нет')+'. Их компоненты здесь не учтены.',
         '- Повторные ключи: '+('; '.join(f'`{p}`: '+', '.join('`'+k+'`' for k in keys) for p,keys in duplicates) if duplicates else 'нет')+'. JSON5 оставляет последнее значение.', '']
    if ver=='2.x':out += ['Выбранные объекты, ID, пути и ошибки совпадают в двух версиях 2.x; другие поля и события могут различаться. `ageable` иногда ссылается на необъявленное локальное событие — само имя здесь не гарантирует реализацию.', '']
    out += ['| Файл / ID | Область и компонент | Полное значение |','|---|---|---|']
    for path,ident,loc,key,value in rows:out.append(f'| `{path}`<br>`{ident}` | `{loc}` | {code(value)} |')
    out += ['',f'См. [группы сущностей](entity-groups-{ver}.md), [поля событий](entity-event-fields-{ver}.md) и [полные определения](entity-ledger-{ver if ver!="2.x" else "2.8.14"}.md).','']
    return '\n'.join(out)

def build_all():
    d={v:extract(f,p,KEYS) for v,f,p in VERSIONS}
    if d['2.8.8']!=d['2.8.14']:raise ValueError('2.x timer/sensor declarations differ')
    return {'1.6':render('1.6','1.6',d['1.6']),'2.x':render('2.8.8 и 2.8.14','2.x',d['2.8.14'])}

def main():
    for ver,text in build_all().items():
        (ROOT/f'docs/entity-trigger-index-{ver}.md').write_text(text,encoding='utf8');print(ver,len(text.splitlines()),'lines')
if __name__=='__main__':main()
