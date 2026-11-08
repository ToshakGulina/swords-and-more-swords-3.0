#!/usr/bin/env python3
"""Inventory player base environment sensors and narrowly matched equipment filters."""
from collections import defaultdict
from pathlib import Path
from zipfile import ZipFile
import json,json5
from build_quick_reference import read_items
ROOT=Path(__file__).resolve().parents[1]
VERSIONS=(('1.6','SwordsAndMoreSwords.1.6.mcaddon','Sword_B'),('2.8.8','swordsandmoreswords_2_8_8.mcaddon','Swords_B'),('2.8.14','swordsandmoreswords-2-8-14.mcaddon','Swords_B'))
def compact(obj):return json.dumps(obj,ensure_ascii=False,separators=(',',':'))

def collect(filename,pack):
    items=read_items(filename,pack)
    with ZipFile(ROOT/'sources'/filename) as z:e=json5.loads(z.read(pack+'/entities/player.json').decode('utf-8-sig'))['minecraft:entity']
    sensors=e['components']['minecraft:environment_sensor'];events=e.get('events',{})
    if not isinstance(sensors,list):raise ValueError('unexpected base sensor type')
    if any(not isinstance(x,dict) or not isinstance(x.get('on_environment'),dict) for x in sensors):raise ValueError('unexpected base sensor entry')
    mapped=defaultdict(list)
    for index,row in enumerate(sensors):
        env=row['on_environment'];f=env.get('filters')
        if not isinstance(f,dict) or set(f)!={'all_of'} or not isinstance(f['all_of'],list) or len(f['all_of'])!=1:continue
        spec=f['all_of'][0]
        if not isinstance(spec,dict):continue
        if spec.get('test')!='has_equipment' or spec.get('subject')!='self' or spec.get('domain')!='hand':continue
        if set(spec)-{'test','subject','domain','value','operator'}:continue
        ident=spec.get('value');operator=spec.get('operator')
        if ident in items and (('operator' not in spec) or operator=='!='):mapped[ident].append((index,operator,env.get('event')))
    return items,sensors,events,dict(mapped)

def table(out,version,data):
    items,sensors,events,mapping=data
    out += [f'## {version}: sensor по исходному порядку', '', f'Найдено **{len(sensors)}** элементов базового списка, из них по ограниченному шаблону ниже сопоставлено item ID: **{len(mapping)}** из {len(items)}. Путь каждого элемента — `$.minecraft:entity.components.minecraft:environment_sensor[index]`.', '',
            '| index | Полный элемент sensor | Имя события в events player |','|---:|---|---|']
    for i,row in enumerate(sensors):
        event=row['on_environment'].get('event');flag='да' if event in events else 'нет / имя отсутствует'
        out.append(f'| {i} | `{compact(row)}` | {flag} |')
    out += ['',f'### {version}: буквальный hand-фильтр по item ID', '',
            'Сопоставляются только фильтры строго вида `all_of` с одним `has_equipment`, subject `self`, domain `hand`, value равным точному ID и без других полей кроме необязательного operator. Ниже отдельно показаны **отсутствующий operator** и буквально `!=`; это не автоматическое утверждение об их семантической взаимной исключительности, отдельных слотах или времени срабатывания.', '',
            '| Точный item ID | operator отсутствует: index → event | operator `!=`: index → event |','|---|---|---|']
    def desc(rows,operator):
        match=[f'`{i}` → `{event}`' for i,op,event in rows if op==operator]
        return '<br>'.join(match) if match else '—'
    for ident in sorted(items):
        rows=mapping.get(ident,[]);out.append(f'| `{ident}` | {desc(rows,None)} | {desc(rows,"!=")} |')
    out += ['', 'Прочерк здесь означает только отсутствие соответствующего *простого* фильтра в этом списке. Предмет может действовать через более сложный фильтр, item hook, другие компоненты/файлы или команды; совпадение события по имени также не устанавливает его выполнение.', '']

def build():
    data={v:collect(f,p) for v,f,p in VERSIONS}
    if data['2.8.8'][1]!=data['2.8.14'][1] or data['2.8.8'][3]!=data['2.8.14'][3] or set(data['2.8.8'][0])!=set(data['2.8.14'][0]):raise ValueError('2.x player base sensors differ')
    out=['# Базовые environment-сенсоры player: 1.6 и 2.x', '',
         'Полные элементы **базового** `minecraft:environment_sensor` в `entities/player.json`, в исходном порядке массива. Значения и фильтры приведены буквально, без интерпретации дефолтов движка. Сенсоры внутри component groups, другие компоненты, команды, анимации и внешние пакеты сюда не включены. Порядок строк массива не доказывает последовательности или частоты вызовов.', '',
         'Списки и сопоставления item-фильтров 2.8.8 и 2.8.14 структурно совпадают; сами тела вызываемых событий и другие поля `player.json` могут отличаться. [Группы player 1.6](player-groups-1.6.md) · [группы player 2.8.14](player-groups-2.8.14.md) · [все event-поля сущностей](entity-event-fields-2.x.md).', '']
    table(out,'1.6',data['1.6']);table(out,'2.8.8 и 2.8.14',data['2.8.14']);return '\n'.join(out)+'\n'

def main():
    (ROOT/'docs/player-sensor-index.md').write_text(build(),encoding='utf-8');print('player sensor index written')
if __name__=='__main__':main()
