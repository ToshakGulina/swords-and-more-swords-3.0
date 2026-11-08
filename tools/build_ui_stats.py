#!/usr/bin/env python3
"""Compare numeric author UI claims with literal item components, not gameplay."""
from decimal import Decimal
import re,json
from pathlib import Path
from build_ui_localization import load,textrefs
from build_quick_reference import read_items,slug
ROOT=Path(__file__).resolve().parents[1]
PAT=re.compile(r'^-(Damage|Durability):\s*(.*)$')
NUMBER=re.compile(r'^([+-]?\d+(?:\.\d+)?)\b')

def claims(version):
    data=load()[version];ui=data['ui'];items=read_items('swordsandmoreswords-2-8-14.mcaddon','Swords_B');found={}
    for section,obj in ui.items():
        if not section.endswith('_section@how_to_play_common.main_sections'):continue
        ident='effect:'+section.split('@')[0][:-8]
        if ident not in items:continue
        found.setdefault(ident,{})
        for path,key in textrefs(obj,'$'):
            vals=data['entries'].get(key,[])
            if len(vals)>1:raise ValueError('duplicate localization for '+key)
            if not vals:continue
            line,text=vals[0];match=PAT.match(text)
            if not match:continue
            kind,body=match.groups();subject=ident
            # The second header in this UI section is explicitly Wet Sponge Sword.
            if section.startswith('sponge_sword_section@') and key in ('effect.sponge_sword.text.9','effect.sponge_sword.text.10'):subject='effect:wet_sponge_sword'
            record=found.setdefault(subject,{})
            if kind in record:raise ValueError('multiple claims for '+subject+' '+kind)
            n=NUMBER.match(body);record[kind]={'key':key,'line':line,'text':text,'number':Decimal(n.group(1)) if n else None}
    return found

def comp(items,id,kind):
    c=items[id][1]['components']
    return c.get('minecraft:damage') if kind=='Damage' else c.get('minecraft:durability',{}).get('max_durability')

def cell(record,item_value):
    value='—' if item_value is None else '`'+json.dumps(item_value,ensure_ascii=False)+'`'
    if record is None:return 'нет прямой строки',value,'не сравнивается'
    text='`'+json.dumps(record['text'],ensure_ascii=False).replace('|','\\|').replace('`','\\u0060')+'`<br>`'+record['key']+'`'
    if record['number'] is None:return text,value,'нечисловое заявление'
    if item_value is None:return text,value,'компонент отсутствует'
    return text,value,('совпадает' if Decimal(str(item_value))==record['number'] else '**различается**')

def build():
    first,second=claims('2.8.8'),claims('2.8.14')
    if first!=second:raise ValueError('UI numeric claims or line numbers differ between 2.x archives')
    a=read_items('swordsandmoreswords_2_8_8.mcaddon','Swords_B');items=read_items('swordsandmoreswords-2-8-14.mcaddon','Swords_B')
    if set(a)!=set(items) or any(a[id][1]['components']!=items[id][1]['components'] for id in items):raise ValueError('2.x item components differ')
    stats={'Damage':{'совпадает':0,'различается':0,'компонент отсутствует':0,'не сравнивается':0,'нечисловое заявление':0},'Durability':{'совпадает':0,'различается':0,'компонент отсутствует':0,'не сравнивается':0,'нечисловое заявление':0}};rows=[]
    for id,record in sorted(second.items()):
        dc,di,dr=cell(record.get('Damage'),comp(items,id,'Damage'));uc,ui,ur=cell(record.get('Durability'),comp(items,id,'Durability'));stats['Damage'][dr.replace('**','')]+=1;stats['Durability'][ur.replace('**','')]+=1
        section=('sponge_sword' if id=='effect:wet_sponge_sword' else id.split(':',1)[1])+'_section@how_to_play_common.main_sections'
        rows.append(f'| [`{id}`](items-2.8.14.md#{slug(id)}) · [UI](ui-localization-index.md#{slug(section)}) | {dc} | {di} | {dr} | {uc} | {ui} | {ur} |')
    out=['# Числа damage и durability: UI 2.x против компонентов', '',
         'Сопоставляются только прямо подключённые `$text` секций предметов и буквальные `minecraft:damage` / `minecraft:durability.max_durability`; первая числовая величина после точного префикса `-Damage:` / `-Durability:` сравнивается как число. Совпадение не доказывает реальный урон, срок службы, действие чар, условия или работу Bedrock. Отсутствующий компонент не равен нулю или бесконечности. Декларации 2.8.8/2.8.14 проверены как одинаковые для этих строк и item-компонентов.', '',
         f'Представлено {len(second)} ID. Числовые строки damage совпадают у {stats["Damage"]["совпадает"]}, различные — {stats["Damage"]["различается"]}; числовые строки durability совпадают у {stats["Durability"]["совпадает"]}, различные — {stats["Durability"]["различается"]}. Нечисловые заявления и отсутствующие строки не включены в число совпадений. Секции общих материалов, скриншоты, остальные свойства и косвенные значения не подсчитываются.', '',
         'Wet Sponge расположен внутри секции Sponge после отдельного заголовка `Wet Sponge Sword`: строки `.9` и `.10` сопоставлены с `effect:wet_sponge_sword`, а не с обычным Sponge. У Nether Star строка прочности `.13` стоит перед строкой урона `.0`; сортировка суффиксов не отражает порядок UI. Bedrock `Infinite` — текст, а не числовой компонент; у Wolf в прямом разделе нет строки durability. [Все прямые тексты](ui-localization-index.md) · [сверка скриншотов](screenshot-stat-comparison.md).', '',
         '| ID | Текст damage и ключ | Компонент damage | Сверка | Текст durability и ключ | max_durability | Сверка |', '|---|---|---:|---|---|---:|---|']
    return '\n'.join(out+rows+[''])

def main():
    (ROOT/'docs/ui-stat-comparison.md').write_text(build(),encoding='utf8');print('UI stat comparison written')
if __name__=='__main__':main()
