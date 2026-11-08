#!/usr/bin/env python3
"""Weapon hooks and symbolic direct-durability distributions, not Bedrock emulation."""
from pathlib import Path
from fractions import Fraction
from collections import defaultdict
import json
from build_quick_reference import read_items,slug
ROOT=Path(__file__).resolve().parents[1]
MISSING=object()
HOOKS=('on_hurt_entity','on_not_hurt_entity','on_hit_block')

def convolve(left,right):
    out=defaultdict(Fraction)
    for a,pa in left.items():
        for b,pb in right.items():out[a+b]+=pa*pb
    return dict(out)

def distribution(node):
    if not isinstance(node,dict):raise ValueError('expected event object')
    if 'filters' in node:raise ValueError('conditional event not handled')
    result={0:Fraction(1)}
    if 'damage' in node:
        d=node['damage']
        if d.get('type')=='durability':
            if d.get('target')!='self' or type(d.get('amount')) is not int:raise ValueError('unsupported damage: '+str(d))
            result={d['amount']:Fraction(1)}
    if 'sequence' in node:
        for step in node['sequence']:result=convolve(result,distribution(step))
    if 'randomize' in node:
        branches=node['randomize'];weights=[x.get('weight') for x in branches]
        if any(type(x) is not int or x<=0 for x in weights):raise ValueError('unsupported weight')
        total=sum(weights);mix=defaultdict(Fraction)
        for branch,w in zip(branches,weights):
            for amount,p in distribution(branch).items():mix[amount]+=Fraction(w,total)*p
        result=convolve(result,dict(mix))
    return result

def compact(v):return json.dumps(v,ensure_ascii=False,separators=(',',':'))
def fraction(v):return str(v.numerator) if v.denominator==1 else f'{v.numerator}/{v.denominator}'
def dist_text(d):return ', '.join(f'{n}: {fraction(p)}' for n,p in sorted(d.items()))

def collect():
    a=read_items('swordsandmoreswords_2_8_8.mcaddon','Swords_B');b=read_items('swordsandmoreswords-2-8-14.mcaddon','Swords_B')
    if set(a)!=set(b):raise ValueError('item ID sets differ')
    for ident in a:
        for key in ('minecraft:weapon',):
            if a[ident][1].get('components',{}).get(key,MISSING)!=b[ident][1].get('components',{}).get(key,MISSING):raise ValueError('weapon components differ: '+ident)
        if a[ident][1].get('events',{}).get('weapon',MISSING)!=b[ident][1].get('events',{}).get('weapon',MISSING):raise ValueError('weapon events differ: '+ident)
    return b

def build():
    items=collect();out=['# Weapon-хуки и условная модель прочности предметов 2.x', '',
        'Сопоставлены все 42 ID, совпадающие между архивами 2.8.8 и 2.8.14: проверено структурное равенство `minecraft:weapon` и соответствующего event `weapon`, но **не** равенство всего поведения предмета/сущностей. `не задан` — отсутствующее поле, `{}` — явно пустой объект. [Как читать модель и её ограничения](manual-weapon-durability-model.md).', '',
        'Условная модель в последнем столбце учитывает только **явные** `damage {type:durability,target:self}` внутри event, при успешном выполнении всех sequence и независимых weighted randomize с указанными весами. Доли — точные дроби по этой модели, не наблюдаемые игровые вероятности. Команды, on-use, digger, обычный износ движка, раннее разрушение и косвенные эффекты не включены; `0` **не** доказывает нулевой износ или отсутствие урона игроку.', '',
        '| ID | on_hurt_entity | on_not_hurt_entity | on_hit_block | Условная сумма явных damage: доля |', '|---|---|---|---|---|']
    eventrows=[]
    for ident,(_,item) in sorted(items.items()):
        c=item.get('components',{});weapon=c.get('minecraft:weapon',MISSING);event=item.get('events',{}).get('weapon',MISSING)
        if weapon is MISSING:hooks=['не задан']*3;model='нет компонента'
        elif not isinstance(weapon,dict):raise ValueError('weapon is not an object: '+ident)
        elif not weapon:hooks=['не задан']*3;model='пустой `minecraft:weapon`'
        else:
            hooks=[]
            for h in HOOKS:
                value=weapon.get(h,MISSING)
                hooks.append('не задан' if value is MISSING else '`'+compact(value).replace('|','\\|')+'`')
            if event is MISSING:raise ValueError('hook references missing weapon event: '+ident)
            if any(weapon[h].get('event')!='weapon' for h in weapon):raise ValueError('unexpected weapon hook: '+ident)
            model='`'+dist_text(distribution(event))+'`'
            eventrows.append((ident,event))
        out.append(f'| [`{ident}`](items-2.8.14.md#{slug(ident)}) | '+' | '.join(hooks)+f' | {model} |')
    out += ['', '## Полные event `weapon`', '', 'Буквальные структуры после JSON5-разбора, сохранён порядок массивов; комментарии и форматирование оригинала не воспроизводятся. Компоненты с пустым объектом и отсутствующие объекты перечислены в таблице выше; ссылки на исходные файлы — в карточках.', '', '| ID | Значение event |', '|---|---|']
    for ident,event in eventrows:out.append(f'| `{ident}` | `'+compact(event).replace('|','\\|').replace('`','\\`')+'` |')
    return '\n'.join(out)+'\n'

def main():
    (ROOT/'docs/weapon-event-index.md').write_text(build(),encoding='utf-8');print('weapon event index written')
if __name__=='__main__':main()
