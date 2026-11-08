#!/usr/bin/env python3
"""Index Jungle's ordered block/data and direction tests, across archives."""
from pathlib import Path
from zipfile import ZipFile
import re,json5
ROOT=Path(__file__).resolve().parents[1]
OLD='Sword_B/animation_controllers/jungle_sword.json'
NEW='Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction'
PATTERN=re.compile(r'execute @p ~~~ detect (\S+) (\S+) (\S+) (\S+) (\S+) fill ~ ~1 ~ ~ ~1 ~ vine (\S+) replace air')
DIRECTIONS=[('~1','~1','~','8'),('~-1','~1','~','2'),('~','~1','~1','1'),('~','~1','~-1','4')]

def parse(cmd):
    m=PATTERN.fullmatch(cmd.removeprefix('/'))
    if not m:raise ValueError('unexpected jungle command: '+cmd)
    x,y,z,block,data,vine=m.groups()
    return {'direction':(x,y,z,vine),'block':block,'data':data}

def blocks(commands):
    if len(commands)%4:raise ValueError('incomplete direction group')
    result=[]
    for pos in range(0,len(commands),4):
        lines=[parse(c) for c in commands[pos:pos+4]]
        if [x['direction'] for x in lines]!=DIRECTIONS or len({(x['block'],x['data']) for x in lines})!=1:raise ValueError('unexpected direction group')
        result.append({'block':lines[0]['block'],'data':lines[0]['data'],'start':pos+1})
    if len({(x['block'],x['data']) for x in result})!=len(result):raise ValueError('duplicate block/data groups')
    return result

def collect():
    with ZipFile(ROOT/'sources/SwordsAndMoreSwords.1.6.mcaddon') as z:
        states=json5.loads(z.read(OLD).decode('utf-8-sig'))['animation_controllers']['controller.animation.jungle']['states']
    old=states['jungle']['on_entry'];
    if states['default']['on_entry']!=['/commands'] or old[-1]!='/scoreboard players set @a swords 2' or len(old)!=145:raise ValueError('unexpected legacy controller')
    old=old[:-1]
    with ZipFile(ROOT/'sources/swordsandmoreswords_2_8_8.mcaddon') as a,ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as b:
        raw=a.read(NEW)
        if raw!=b.read(NEW):raise ValueError('jungle functions differ between 2.x')
    new=raw.decode('utf-8-sig').splitlines()
    oldgroups=blocks(old);newgroups=blocks(new)
    old_normal=[x.removeprefix('/') for x in old];new_without=[x for x in new if not (parse(x)['block']=='leaves' and parse(x)['data']=='11')]
    if len(oldgroups)!=36 or len(newgroups)!=37 or old_normal!=new_without:raise ValueError('unexpected source difference')
    return states,old,new,oldgroups,newgroups

def build():
    _,old,new,og,ng=collect();old_idx={(r['block'],r['data']):r['start'] for r in og}
    out=['# Jungle Sword: блоки, data и порядок лозы', '',
         'Статическая выписка `controller.animation.jungle` state `jungle` 1.6 и функции 2.x. В 1.6 144 vine-команды плюс глобальный scoreboard; в 2.x 148 vine-команд. Каждый диапазон из четырёх строк идёт в неизменном порядке: detect на x+1/y+1/z+0 → vine data 8; x−1/y+1/z+0 → 2; x+0/y+1/z+1 → 1; x+0/y+1/z−1 → 4. Все команды направлены в одну позицию `~ ~1 ~` относительно выбранного `@p` с `replace air`.', '',
         '2.x имеет дополнительную группу `leaves 11` на строках 53–56. Если исключить её и убрать начальную `/` у 1.6, **оставшиеся команды совпадают в том же порядке**, не только как мультимножество. Это не доказывает равный контекст вызова, соблюдение старого синтаксиса или частоту событий. [Разбор и условная модель приоритетов](manual-jungle-vines.md).', '',
         '| Порядок 2.x | detect block | data | Номера команд 1.6 | Номера строк 2.x |', '|---:|---|---:|---:|---:|']
    for i,r in enumerate(ng,1):
        previous=old_idx.get((r['block'],r['data']));a=f'{previous}–{previous+3}' if previous is not None else 'не задано';b=f'{r["start"]}–{r["start"]+3}'
        out.append(f'| {i} | `{r["block"]}` | {r["data"]} | {a} | {b} |')
    return '\n'.join(out)+'\n'

def main():
    (ROOT/'docs/jungle-vine-index.md').write_text(build(),encoding='utf-8');print('jungle vine index written')
if __name__=='__main__':main()
