#!/usr/bin/env python3
"""Selector-only Grass examples; deliberately not an engine simulator."""
from pathlib import Path
from zipfile import ZipFile
import re,json5
ROOT=Path(__file__).resolve().parents[1]
CASES=[
 ('Обычный игрок','player',('player','default_player')),
 ('Игрок в полной Wolf-группе','player',('wolf','wolf_sword','complete_wolf_transformation','monster')),
 ('Shulker shield','entity:shulker_shield',('effect99_entities','player','shulker_sword')),
 ('Grass Witch','witch',('witch','monster','mob','grass_witch')),
 ('Зомби: пример без спецсемей','zombie',('monster',)),
 ('Предмет: пример без спецсемей','item',()),
 ('Стрела: пример без спецсемей','arrow',()),
 ('Grass helper','entity:grass',('effect99_entities',)),
]

def selector(cmd):
    m=re.search(r'@e\[([^\]]+)\]',cmd)
    if not m:raise ValueError('no selector: '+cmd)
    return m.group(1)

def accepts(expr,typ,families,tags):
    for term in expr.split(','):
        key,sep,val=term.partition('=')
        if not sep:raise ValueError('unexpected selector term '+term)
        if key in ('r','rm','c'):continue
        invert=val.startswith('!');value=val[1:] if invert else val
        if key=='type':condition=(typ==value)
        elif key=='family':condition=(value in families)
        elif key=='tag':condition=(value in tags)
        else:raise ValueError('unsupported selector term '+term)
        if condition==invert:return False
    return True

def collect():
    players=[];grass=[];witch=[]
    for archive in ['swordsandmoreswords_2_8_8.mcaddon','swordsandmoreswords-2-8-14.mcaddon']:
        with ZipFile(ROOT/'sources'/archive) as z:
            def rd(p):return json5.loads(z.read('Swords_B/entities/'+p+'.json').decode('utf-8-sig'))['minecraft:entity']
            players.append(rd('player'));grass.append(rd('grass'));witch.append(rd('witch'))
    pc=players[0]['events']['grass_sword_skills']['run_command']['command'];wc=witch[0]['events']['grass_witch_skill']['run_command']['command'];spawn=grass[0]['events']['minecraft:entity_spawned']['sequence'][0]['run_command']['command'];skill=grass[0]['events']['grass_sword_skill']['run_command']['command'];ring=players[0]['events']['minecraft:grass_sword']['sequence'][1]['run_command']['command'][0]
    if pc!=players[1]['events']['grass_sword_skills']['run_command']['command'] or wc!=witch[1]['events']['grass_witch_skill']['run_command']['command'] or grass[0]!=grass[1] or ring!=players[1]['events']['minecraft:grass_sword']['sequence'][1]['run_command']['command'][0]:raise ValueError('selected grass sources differ')
    if selector(pc[0])!=selector(pc[1]) or selector(wc[0])!=selector(wc[1]) or selector(skill[1])!=selector(skill[2]):raise ValueError('expected same selector per pair')
    stages=[('P: поиск игрока',selector(pc[0]),False),('W: поиск ведьмы',selector(wc[0]),False),('T: назначение тега',selector(spawn[2]),False),('S: slowness',selector(spawn[1]),False),('C: выбор с tag',selector(skill[1]),True),('R: снять r=2',selector(skill[3]),True),('Q: снять rm=9/r=10',selector(ring),True)]
    return stages

def build():
    stages=collect()
    out=['# Grass Sword: условное пересечение селекторов 2.x', '',
         'Это таблица **только текстовых type/family/tag-фильтров**, не эмуляция Bedrock и не доказательство действия на сущность. Для P/W/T предполагается отсутствие тега `grass`, для C/R/Q — его наличие; S от тега не зависит. Каждая колонка рассматривается отдельно при удовлетворении своего радиуса, а для P/W/C ещё и двух detect. `c=1` и выбор одной цели не моделируются: «да» означает возможность пройти только показанные тип/family/tag, не гарантию выбора, спавна, телепорта или эффекта. Имена type и соответствие runtime/vanilla нужно испытать в игре. Семейства строк ниже — гипотетические состояния; одновременное существование групп и смена состояний не установлены. [Пошаговый разбор](manual-grass-sword.md).', '', '| Стадия | Исходный selector | Проверяемый тег |', '|---|---|---|']
    for title,expr,tag in stages:out.append(f'| {title} | `@e[{expr}]` | '+('есть' if tag else ('без ограничения' if title.startswith('S:') else 'нет'))+' |')
    out += ['', '| Пример: type и предполагаемые families | P | W | T | S | C | R | Q |', '|---|---|---|---|---|---|---|---|']
    for title,typ,families in CASES:
        result=['да' if accepts(expr,typ,set(families),{'grass'} if tagged else set()) else 'нет' for _,expr,tagged in stages]
        out.append(f'| {title}: `{typ}`, '+('families `'+','.join(families)+'`' if families else 'без специальных families')+' | '+' | '.join(result)+' |')
    return '\n'.join(out)+'\n'

def main():
    (ROOT/'docs/grass-selector-samples.md').write_text(build(),encoding='utf-8');print('grass selector samples written')
if __name__=='__main__':main()
