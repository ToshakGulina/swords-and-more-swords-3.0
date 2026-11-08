#!/usr/bin/env python3
"""Sample source-pinned Wolf conditions under explicitly assumed Boolean semantics."""
from decimal import Decimal
from pathlib import Path
from zipfile import ZipFile
import json5

ROOT=Path(__file__).resolve().parents[1]
ARCHIVES=('swordsandmoreswords_2_8_8.mcaddon','swordsandmoreswords-2-8-14.mcaddon')
PATH='Swords_B/animation_controllers/wolf_sword.json'
EXPECTED=(
    "q.get_equipped_item_name('main_hand') == 'wolf_sword' && q.moon_phase == 0 && (q.time_of_day >= 0.77 && q.time_of_day <= 0.78)",
    "q.get_equipped_item_name('main_hand') == 'wolf_sword' && q.moon_phase == 0 && (q.time_of_day <= 0.20 || q.time_of_day >= 0.80)",
    "q.get_equipped_item_name('main_hand') == 'wolf_sword' || q.get_equipped_item_name('main_hand') != 'wolf_sword' && q.moon_phase == 0 && q.time_of_day == 0.20",
)

def source_conditions():
    sources=[]
    for archive in ARCHIVES:
        with ZipFile(ROOT/'sources'/archive) as z:sources.append(z.read(PATH))
    if sources[0]!=sources[1]:raise ValueError('Wolf controllers differ across versions')
    root=json5.loads(sources[0].decode('utf-8-sig'))['animation_controllers']
    conditions=(root['controller.animation.wolf_sword']['states']['wolf_transformation']['transitions'][0]['wolf_sword'],
                root['controller.animation.start_wolf_sword']['states']['start_wolf_transformation']['transitions'][0]['wolf_sword_start'],
                root['controller.animation.end_wolf_sword']['states']['end_wolf_transformation']['transitions'][0]['wolf_sword_end'])
    if conditions!=EXPECTED:raise ValueError('Source changed: review Boolean model before regenerating')
    return conditions

def model(item,phase,time):
    """Ordinary &&-before-|| precedence; no claim about actual Molang semantics."""
    t=Decimal(time); p=(phase==0)
    return (item and p and Decimal('0.77')<=t<=Decimal('0.78'),
            item and p and (t<=Decimal('0.20') or t>=Decimal('0.80')),
            item or ((not item) and p and t==Decimal('0.20')))

def build():
    conds=source_conditions()
    cases=[(True,0,t) for t in ('0.19','0.20','0.21','0.769','0.77','0.775','0.78','0.781','0.79','0.80','0.81')]
    cases += [(True,1,t) for t in ('0.20','0.77','0.80')]
    cases += [(False,0,t) for t in ('0.19','0.20','0.21','0.80')]+[(False,1,'0.20')]
    out=['# Wolf Sword: выборочные значения условий перехода 2.x','',
         'Это арифметическая модель **условий перехода**, не симуляция контроллеров. Предполагается обычный приоритет `&&` выше `||`, точное сравнение десятичных чисел и истинность `W` тогда, когда запрос имени главной руки равен `wolf_sword`. Фактические Molang, численная точность, доступные значения, состояние контроллера, порядок событий и исполнение в движке не подтверждены. Значение «да» не доказывает вход в состояние в этот момент. Строка источника сопоставлена с обоими архивами; см. [ручной разбор](manual-wolf-conditions-2.8.md).','',
         '- A: возможный переход на состояние с `wolf_sword_start_events`.',
         '- B: возможный переход на состояние с `wolf_transformation`; условие клиентской графики имеет ту же часть W/phase/time, но дополнительно зависит от камеры.',
         '- C: возможный переход на состояние с `stop_wolf_transformation`.','',
         'Исходные выражения:', '', *[f'{label}. `{expression}`' for label,expression in zip(('A','B','C'),conds)],'',
         '| W: меч в main hand | moon_phase | time_of_day | A | B | C |','|---|---:|---:|---|---|---|']
    for item,phase,t in cases:
        values=model(item,phase,t)
        out.append('| '+('да' if item else 'нет')+f' | {phase} | {t} | '+' | '.join('да' if x else 'нет' for x in values)+' |')
    return '\n'.join(out)+'\n'

def main():
    (ROOT/'docs/wolf-condition-samples-2.8.md').write_text(build(),encoding='utf-8')
    print('wolf condition table written')

if __name__=='__main__':main()
