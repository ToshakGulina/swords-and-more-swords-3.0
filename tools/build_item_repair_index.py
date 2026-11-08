#!/usr/bin/env python3
"""Compare item durability, repair definitions, and presentation flags verbatim."""
from pathlib import Path
import json
from build_quick_reference import read_items,slug
ROOT=Path(__file__).resolve().parents[1]

def collect():
    old=read_items('SwordsAndMoreSwords.1.6.mcaddon','Sword_B');a=read_items('swordsandmoreswords_2_8_8.mcaddon','Swords_B');b=read_items('swordsandmoreswords-2-8-14.mcaddon','Swords_B')
    if set(a)!=set(b) or any(a[k][1]['components']!=b[k][1]['components'] for k in a):raise ValueError('2.x item components differ')
    return old,a,b

def literal(comp,key):
    if key not in comp:return '—'
    return '`'+json.dumps(comp[key],ensure_ascii=False,separators=(',',':')).replace('|','\\|').replace('`','\\`')+'`'

def table(out,version,items):
    n=sum('minecraft:repairable' in item['components'] for _,item in items.values())
    out += [f'## {version}', '', f'Всего item ID: {len(items)}; с явно заданным `minecraft:repairable`: {n}; без этого компонента: {len(items)-n}.', '',
            '| ID | durability | repairable целиком | foil | hand_equipped | allow_off_hand | max_stack_size |', '|---|---|---|---|---|---|---|']
    keys=('minecraft:durability','minecraft:repairable','minecraft:foil','minecraft:hand_equipped','minecraft:allow_off_hand','minecraft:max_stack_size')
    file='2.8.14' if version!='1.6' else '1.6'
    for ident,(_,item) in sorted(items.items()):
        c=item['components'];out.append('| [`'+ident+'`](items-'+file+'.md#'+slug(ident)+') | '+' | '.join(literal(c,k) for k in keys)+' |')
    out.append('')

def build():
    old,a,b=collect()
    out=['# Предметы: прочность, ремонт и флаги по версиям', '',
         'Полные буквальные компоненты `minecraft:durability` и `minecraft:repairable` из всех item JSON, а также заданные значения `foil`, `hand_equipped`, `allow_off_hand`, `max_stack_size`. Значения материалов и `repair_amount` не нормализуются и не исправляются; `—` означает **нет поля**, а не false, нулевую прочность, бесконечность или невозможность иных способов ремонта. Таблица не включает вызовы weapon/on-use и фактический расход прочности.', '',
         'В 2.8.8 и 2.8.14 все разобранные **компоненты** одноимённых 42 item структурно совпадают. Это не означает равенства файлов целиком: события Ice различаются. Для урона и зачарования см. [сводную таблицу предметов](quick-reference.md), для различий 25 общих ID — [матрицу](item-version-matrix.md), для событий — [weapon](weapon-event-index.md) и [on-use](on-use-index.md).', '',
         'Обратите внимание на буквальные ID: `minecraft:fire`, `minecraft:slime`, `minecraft:magma` и `minecraft:bone_meal` не заменяются похожими именами. У `effect:wet_sponge_sword` наряду с самим предметом указан `effect:sponge_sword`; у Cursed Pumpkin как материалы присутствуют `minecraft:honey_block` и `minecraft:honeycomb`. Это зафиксированное содержимое архива, а не вывод о доступности материала.', '']
    table(out,'1.6',old);table(out,'2.8.8 и 2.8.14',b)
    return '\n'.join(out)+'\n'

def main():
    (ROOT/'docs/item-repair-index.md').write_text(build(),encoding='utf-8');print('item repair index written')
if __name__=='__main__':main()
