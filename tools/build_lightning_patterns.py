#!/usr/bin/env python3
"""Extract 1.6 lightning selectors and 2.x on-use coordinates."""
from pathlib import Path
from zipfile import ZipFile
import json5, math, re
ROOT=Path(__file__).resolve().parents[1]

def collect():
    with ZipFile(ROOT/'sources/SwordsAndMoreSwords.1.6.mcaddon') as z:
        states=json5.loads(z.read('Sword_B/animation_controllers/lightning sword.json').decode('utf-8-sig'))['animation_controllers']['controller.animation.lightning']['states']
    if states['default']['on_entry']!=states['lightning']['on_entry']:raise ValueError('controller state commands differ')
    old=states['default']['on_entry'];targets=[]
    for c in old[:-1]:
        m=re.fullmatch(r'/execute @e\[type=([^,\]]+),r=16,rm=10\] ~ ~ ~ summon lightning_bolt',c)
        if not m:raise ValueError('unexpected legacy command '+c)
        targets.append(m[1])
    if len(targets)!=26 or old[-1]!='/scoreboard players set @a swords 2':raise ValueError('unexpected legacy controller')
    with ZipFile(ROOT/'sources/swordsandmoreswords_2_8_8.mcaddon') as a,ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as b:
        p='Swords_B/items/lightning_sword.json';raw=a.read(p)
        if raw!=b.read(p):raise ValueError('2.x item differs')
    item=json5.loads(raw.decode('utf-8-sig'))['minecraft:item'];event=item['events']['on_use'];new=[]
    for command in event['run_command']['command']:
        tokens=command.split()
        if len(tokens)!=6 or tokens[:2]!=['summon','lightning_bolt'] or tokens[-1]!='default_lightning_bolt':raise ValueError('unexpected summon '+command)
        coords=[]
        for token in tokens[2:5]:
            if not token.startswith('~'):raise ValueError('nonrelative coordinate '+token)
            coords.append(int(token[1:] or '0'))
        new.append((command,tuple(coords)))
    if len(new)!=41:raise ValueError('unexpected summon count')
    return states,targets,item,new

def build():
    states,targets,item,points=collect()
    lines=['# Lightning Sword: цели 1.6 и координаты 2.x', '',
           'Автоматическая выписка из `Sword_B/animation_controllers/lightning sword.json` и `Swords_B/items/lightning_sword.json`. Обе 2.x версии имеют одинаковый item JSON. Список — статические команды, не оценка успешных призывов, поражённых целей или порядка исполнения; контекст относительных координат и обработка устаревшего синтаксиса нуждаются в проверке. [Ручной разбор](manual-lightning-1.6.md).', '',
           '## 1.6 — 26 type', '', 'В состояниях `default` и `lightning` одинаковые 27 строк `on_entry`: сначала 26 команд ниже, затем `/scoreboard players set @a swords 2`. В каждой команде указан `r=16,rm=10` относительно текущего контекста helper; `execute` позиционируется у каждой выбранной сущности. Номера соответствуют исходному порядку.', '', '| № | Тип | Исходная команда |', '|---:|---|---|']
    for i,t in enumerate(targets,1):lines.append(f'| {i} | `{t}` | `{states["default"]["on_entry"][i-1]}` |')
    lines+=['', '## 2.x — 41 относительная координата', '', 'Координаты приведены относительно контекста команды `run_command`; квадрат горизонтального расстояния вычислен как x²+z², для человека показан его корень. Это геометрия **точек призыва**, а не радиус урона или гарантированный охват. Для первой точки y=+2, остальные y=0.', '', '| № | x | y | z | x²+z² | Горизонтальное расстояние ≈ | Исходная команда |','|---:|---:|---:|---:|---:|---:|---|']
    for i,(command,(x,y,z)) in enumerate(points,1):
        d2=x*x+z*z;lines.append(f'| {i} | {x} | {y} | {z} | {d2} | {math.sqrt(d2):.3f} | `{command}` |')
    lines += ['', 'У события `on_use` вместе с `run_command` объявлен `damage` type durability amount 9 target self; порядок обработки этих полей движком не установлен.']
    return '\n'.join(lines)+'\n'

def main():
    (ROOT/'docs/lightning-patterns.md').write_text(build(),encoding='utf-8');print('lightning patterns written')
if __name__=='__main__':main()
