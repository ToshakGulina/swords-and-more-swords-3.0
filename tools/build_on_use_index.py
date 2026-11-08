#!/usr/bin/env python3
"""Index literal item on-use events without interpreting Bedrock event execution."""
from pathlib import Path
import json
from build_quick_reference import read_items,slug
from build_weapon_event_index import distribution
ROOT=Path(__file__).resolve().parents[1]
MISSING=object()

def replace_ice(v):
    if isinstance(v,str):return v.replace('effect99:fake_ice','frosted_ice')
    if isinstance(v,list):return [replace_ice(x) for x in v]
    if isinstance(v,dict):return {k:replace_ice(x) for k,x in v.items()}
    return v

def collect():
    old=read_items('SwordsAndMoreSwords.1.6.mcaddon','Sword_B');a=read_items('swordsandmoreswords_2_8_8.mcaddon','Swords_B');b=read_items('swordsandmoreswords-2-8-14.mcaddon','Swords_B')
    if set(a)!=set(b):raise ValueError('2.x item sets differ')
    if any('minecraft:on_use' in i['components'] or 'minecraft:cooldown' in i['components'] for _,i in old.values()):raise ValueError('unexpected 1.6 item component')
    for ident in a:
        x=a[ident][1];y=b[ident][1]
        for key in ('minecraft:cooldown','minecraft:on_use'):
            if x['components'].get(key,MISSING)!=y['components'].get(key,MISSING):raise ValueError('2.x component differs '+ident)
        e=x.get('events',{}).get('on_use',MISSING);f=y.get('events',{}).get('on_use',MISSING)
        if ident=='effect:ice_sword':
            if e is MISSING or f is MISSING or replace_ice(e)!=f or e==f:raise ValueError('unexpected Ice difference')
        elif e!=f:raise ValueError('2.x on_use event differs '+ident)
    return old,a,b

def actions(node):
    if isinstance(node,list):
        for x in node:yield from actions(x)
    elif isinstance(node,dict):
        for key,v in node.items():
            if key in ('run_command','shoot','damage'):yield key,v
            else:yield from actions(v)

def shape(event):
    if 'sequence' in event:
        if set(event)!={'sequence'}:raise ValueError('unsupported sibling sequence')
        return 'sequence: '+' → '.join('+'.join(x.keys()) for x in event['sequence'])
    return 'один объект: '+' + '.join(event.keys())

def build():
    old,a,b=collect();out=['# Item on-use и cooldown: 1.6 и 2.x', '',
        'В 26 item JSON 1.6 компоненты `minecraft:on_use` и `minecraft:cooldown` отсутствуют: это не означает, что движок или helper не выполняют какие-либо действия при использовании. У 42 item ID 2.x 14 таких hook и 14 cooldown; оба компонента структурно одинаковы в 2.8.8 и 2.8.14. `on_use` event совпадает у 13, а у Ice отличается только буквальная замена `effect99:fake_ice` → `frosted_ice`. Прочие файлы и поведение версий могут различаться.', '',
        'Таблица — **объявления item**, не подтверждённые действия или фактический расход. `duration` сохранён в единицах оригинального компонента; не считать его автоматически тиками или секундами целевой версии. `damage` показан только для прямых действий event; стандартный износ, on-hit, зачарования, раннее разрушение и косвенные команды не учитываются.', '',
        '`sequence` обозначает явно записанный массив в данном порядке, но исполнение и ошибки движка не испытаны. Несколько ключей одного объекта — **соседние поля, не доказанная последовательность и не утверждение об одновременности**. Для `run_command.target` различаются буквальный `holder` и отсутствие поля; не подставлять дефолт без проверки. Команды/стрельба могут сработать или не сработать независимо от ожидаемой прочности.', '',
        '| Точный ID | cooldown целиком | Форма event | Прямой durability damage | run_command: число / target | shoot целиком |', '|---|---|---|---|---|---|']
    absent=[];count=0
    for ident,(_,item) in sorted(b.items()):
        comp=item['components'];hook=comp.get('minecraft:on_use',MISSING);cool=comp.get('minecraft:cooldown',MISSING)
        if hook is MISSING:
            if cool is not MISSING:raise ValueError('cooldown without hook '+ident)
            absent.append(ident);continue
        if hook!={'on_use':{'event':'on_use'}} or cool is MISSING:raise ValueError('unexpected on_use hook '+ident)
        event=item['events']['on_use'];acts=list(actions(event));runs=[v for k,v in acts if k=='run_command'];shoots=[v for k,v in acts if k=='shoot'];dmg=[v for k,v in acts if k=='damage'];outcomes=distribution(event)
        if len(dmg)!=1 or len(outcomes)!=1:raise ValueError('unsupported damage shape '+ident)
        d='`'+json.dumps(dmg[0],ensure_ascii=False,separators=(',',':'))+'`'
        r='; '.join(f'{len(v["command"])} / '+('`'+v['target']+'`' if 'target' in v else 'не задан') for v in runs) if runs else 'не задано'
        shoot='; '.join('`'+json.dumps(v,ensure_ascii=False,separators=(',',':'))+'`' for v in shoots) if shoots else 'не задано'
        cooldown='`'+json.dumps(cool,ensure_ascii=False,separators=(',',':'))+'`';count+=1
        out.append(f'| [`{ident}`](items-2.8.14.md#{slug(ident)}) | {cooldown} | {shape(event)} | {d} | {r} | {shoot} |')
    if count!=14 or len(absent)!=28:raise ValueError('unexpected hook count')
    out+=['', '## Без item-компонента `minecraft:on_use` в обоих архивах 2.x', '', ', '.join('`'+x+'`' for x in absent)+'.', '',
          'Это отсутствие именно item hook; у предметов могут быть weapon/digger/block-placer и player/entity/animation-события. Полные команды и источники по ссылкам на карточки предметов; отдельно [геометрия Ice](ice-geometry-index.md) и [рисунок Lightning](lightning-patterns.md).']
    return '\n'.join(out)+'\n'

def main():
    (ROOT/'docs/on-use-index.md').write_text(build(),encoding='utf-8');print('on-use index written')
if __name__=='__main__':main()
