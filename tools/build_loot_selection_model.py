#!/usr/bin/env python3
"""Conditional selection arithmetic for direct custom entries; never infer game drops."""
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
import json
from build_loot_context import read_tables,indexes
ROOT=Path(__file__).resolve().parents[1]
MISSING=object()

def compact(v):return json.dumps(v,ensure_ascii=False,separators=(',',':'))
def weight(entry):
    w=entry.get('weight',1)
    if type(w) is not int or w<=0:raise ValueError('unsupported weight: '+str(w))
    return w

def roll_range(rolls):
    if type(rolls) is int and rolls>=0:return rolls,rolls
    if isinstance(rolls,dict) and set(rolls)=={'min','max'} and all(type(rolls[k]) is int for k in rolls) and 0<=rolls['min']<=rolls['max']<=100:return rolls['min'],rolls['max']
    raise ValueError('unsupported rolls: '+str(rolls))

def one_or_more(p,lo,hi):
    return sum((1-(1-p)**n for n in range(lo,hi+1)),Fraction())/(hi-lo+1)

def collect():
    a,ae,ad=read_tables('swordsandmoreswords_2_8_8.mcaddon','Swords_B');b,be,bd=read_tables('swordsandmoreswords-2-8-14.mcaddon','Swords_B')
    if ae or ad or be or bd or a!=b:raise ValueError('unexpected loot differences, errors or duplicate keys')
    direct,parents=indexes(b,'Swords_B');groups=defaultdict(list)
    for path,pool,entry in sorted(direct):groups[(path,pool,b[path]['pools'][pool]['entries'][entry]['name'])].append(entry)
    rows=[]
    for (path,poolidx,ident),indices in sorted(groups.items()):
        table=b[path];pool=table['pools'][poolidx];entries=pool['entries'];lo,hi=roll_range(pool.get('rolls'));total=sum(weight(x) for x in entries);target=sum(weight(entries[i]) for i in indices)
        if not 0<target<=total:raise ValueError('invalid weight total')
        rows.append({'path':path,'pool':poolidx,'id':ident,'indices':indices,'rolls':pool['rolls'],'lo':lo,'hi':hi,'target_weight':target,'total_weight':total,'prob':one_or_more(Fraction(target,total),lo,hi),'missing':sum('weight' not in x for x in entries),'quality':sum('quality' in x for x in entries),'conditions':pool.get('conditions',MISSING),'entry_conditions':sum('conditions' in x for x in entries),'functions':[entries[i].get('functions',MISSING) for i in indices], 'pool_other':{k:v for k,v in pool.items() if k not in ('conditions','entries','rolls')},'table_other':{k:v for k,v in table.items() if k!='pools'}})
    return b,direct,parents,rows

def build():
    _,direct,parents,rows=collect();pools={(r['path'],r['pool']) for r in rows}
    out=['# Условная модель выбора прямых loot-записей 2.x', '',
         f'Охват: {len(direct)} прямых entries с `type:item` и ID `effect:`/`effect99:` в {len(pools)} пулах; {len(rows)} строк после группировки одинакового ID в одном пуле. Обе версии 2.x имеют структурно одинаковые локальные loot JSON. Только обычные `pools[].entries[]`; это не все способы получения и не анализ динамических или внешних таблиц. Родительские таблицы в эту арифметику не включаются ([контекст и {len(parents)} локальных родительских ссылки](loot-context.md)).', '',
         '**Проценты показывают только модель выбора как минимум одной указанной записи при уже активированном пуле, а не шанс выпадения предмета, сундука, смерти или заброса.** Предполагается, что все перечисленные entries доступны, отсутствующий weight равен 1, quality и модификаторы не влияют, выборы независимы с возвращением, целое число rolls равномерно распределено по границам. Любые условия пула считаются уже выполненными, условия entries игнорируются, функции и фактическая выдача не эмулируются. Неизвестны регистрация таблицы, выбор источника, семантика движка, поведение count, loot и слотов.', '',
         'Числитель — сумма весов записей **одного и того же точного ID** внутри данного пула; знаменатель — сумма весов **всех** entries, включая другие типы и предполагаемые по 1. В последнем столбце показаны полные `functions` каждой целевой записи; `не задано` не означает гарантированный count 1. Если у разных записей одного ID разные функции, их веса агрегированы только для события «запись выбрана», не для числа предметов.', '',
         '| Таблица / pool | ID | Индексы entries | rolls | Вес ID / сумма | Выбор ≥1 записи, модель | Риски и условия |', '|---|---|---|---|---|---:|---|']
    for r in rows:
        risks=[]
        if r['missing']:risks.append(f'{r["missing"]} отсутствующих weight → 1 в модели')
        if r['quality']:risks.append(f'{r["quality"]} quality игнорируются')
        if r['entry_conditions']:risks.append(f'{r["entry_conditions"]} entries с conditions игнорируются')
        if r['conditions'] is not MISSING:risks.append('pool conditions: `'+compact(r['conditions']).replace('|','\\|')+'`')
        if r['pool_other']:risks.append('другие поля pool: `'+compact(r['pool_other']).replace('|','\\|')+'`')
        if r['table_other']:risks.append('другие поля таблицы: `'+compact(r['table_other']).replace('|','\\|')+'`')
        fn=[('не задано' if f is MISSING else '`'+compact(f).replace('|','\\|')+'`') for f in r['functions']]
        risks.append('functions: '+', '.join(fn))
        out.append(f'| `{r["path"].removeprefix("Swords_B/loot_tables/")}` / {r["pool"]} | `{r["id"]}` | '+', '.join(map(str,r['indices']))+f' | `{compact(r["rolls"])}` | {r["target_weight"]}/{r["total_weight"]} | {float(r["prob"])*100:.4f}% | '+'; '.join(risks)+' |')
    out+=['', '## Прочтение граничных примеров', '',
          '- `entities/blaze.json` и пять других одноэлементных условных entity-пулов могут показывать 100% в последнем столбце **при уже выполненных условиях пула**. Их chance/killed_by_* указаны рядом и не равны 100%; частота события, looting и выполнение таблицы отдельно не установлены.',
          '- `chests/pillager_outpost.json`: `set_count` 0…1 у Emerald и Lapis; выбор записи не доказывает ненулевую выдачу. В одном соседнем entry вес не задан, 1 — только явное предположение модели.',
          '- `blocks/quartz_diamond_ore.json`: три записи одного ID (веса 89/10/1) суммированы в событие выбора ID; count у них различается. 100% выбора не означает одного предмета, гарантированной выдачи или срабатывания добычи.',
          '- `gameplay/fishing/treasure.json`: только условный выбор внутри treasure, не шанс рыбалки. Два локальных родителя имеют собственные веса и quality; их условия и способ вызова не включены.',
          '- Расчёт не доказывает существование/генерацию нужного сундука, успешное размещение блока, выпадение с конкретного существа, отсутствие альтернативных пакетов или корректную работу на Bedrock 26.62.']
    return '\n'.join(out)+'\n'

def main():
    (ROOT/'docs/loot-selection-model.md').write_text(build(),encoding='utf-8');print('loot selection model written')
if __name__=='__main__':main()
