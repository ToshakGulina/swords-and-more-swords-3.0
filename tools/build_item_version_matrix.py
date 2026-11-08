#!/usr/bin/env python3
"""Compare exact item-component declarations across supplied versions."""
from pathlib import Path
from zipfile import ZipFile
import json
import json5

ROOT=Path(__file__).resolve().parents[1]
VERSIONS=(('1.6','SwordsAndMoreSwords.1.6.mcaddon','Sword_B'),('2.8.8','swordsandmoreswords_2_8_8.mcaddon','Swords_B'),('2.8.14','swordsandmoreswords-2-8-14.mcaddon','Swords_B'))
MISSING=object()
def compact(value):return json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':'))
def md(value):return 'не задано' if value is MISSING else '`'+compact(value).replace('|','\\|').replace('`','\\`')+'`'

def load(filename,pack):
    out={}
    with ZipFile(ROOT/'sources'/filename) as z:
        for path in sorted(z.namelist()):
            if not path.startswith(pack+'/items/') or not path.endswith('.json'):continue
            raw=z.read(path);data=json5.loads(raw.decode('utf-8-sig'));item=data['minecraft:item'];ident=item['description']['identifier']
            if ident in out:raise ValueError('duplicate item ID '+ident)
            out[ident]={'raw':raw,'data':data,'item':item,'path':path}
    return out

def maxdur(c):
    value=c.get('minecraft:durability',MISSING)
    return value.get('max_durability',MISSING) if isinstance(value,dict) else value

def build():
    a,b,c=[load(f,p) for _,f,p in VERSIONS]
    common=sorted(set(a)&set(c));oldonly=sorted(set(a)-set(c));newonly=sorted(set(c)-set(a))
    diff=[i for i in sorted(set(b)&set(c)) if b[i]['raw']!=c[i]['raw']]
    out=['# Компоненты предметов: 1.6 ↔ 2.8.x', '',
         'Автоматическое сопоставление только **точных item ID** в behavior pack. Приведены буквальные значения JSON, не игровой урон/скорость/длительность. «Не задано» означает отсутствие поля, не `null`, не `false` и не движковое значение по умолчанию; списки «только в версии» относятся к определениям предметов, а не ко всем упоминаниям в архиве. Равенство определений предмета не доказывает равенства player/entity, ресурсов или поведения; имена событий не раскрывают их цепочки. Разные ключи glint/foil и другие схемы не считаются автоматически эквивалентными.', '',
         f'Общих ID 1.6 и 2.8.14: {len(common)}; только в 1.6: {len(oldonly)}; только в 2.8.14: {len(newonly)}. Между 2.8.8 и 2.8.14 общих ID: {len(set(b)&set(c))}, из них побайтово изменённых item JSON: {len(diff)}: '+(', '.join('`'+i+'`' for i in diff) if diff else 'нет')+'.', '',
         '- Только 1.6: '+', '.join('`'+x+'`' for x in oldonly)+'.',
         '- Только 2.8.14: '+', '.join('`'+x+'`' for x in newonly)+'.',
         '- `effect:sword_of_time` и `effect:time_sword` здесь не объединяются автоматически.', '',
         '## Обзор числовых полей', '', '| Точный ID | damage 1.6 → 2.8.14 | max_durability 1.6 → 2.8.14 | allow_off_hand 1.6 → 2.8.14 |', '|---|---|---|---|']
    for ident in common:
        o=a[ident]['item'].get('components',{});n=c[ident]['item'].get('components',{})
        def pair(x,y):return md(x)+' → '+md(y)
        out.append(f'| `{ident}` | {pair(o.get("minecraft:damage",MISSING),n.get("minecraft:damage",MISSING))} | {pair(maxdur(o),maxdur(n))} | {pair(o.get("minecraft:allow_off_hand",MISSING),n.get("minecraft:allow_off_hand",MISSING))} |')
    out += ['', '## Все изменённые или отсутствующие компоненты общих ID', '',
            'Для каждого ключа выводится **полное значение компонента** с каждой стороны. Поля, одинаковые структурно, опущены; события показаны только именами. Полный исходный текст, рецепты и связи — в [карточках 1.6](items-1.6.md), [2.8.14](items-2.8.14.md), [ручном разборе 1.6](manual-traces-1.6.md) и [2.8.14](manual-traces-2.8.14.md).', '']
    for ident in common:
        old=a[ident];new=c[ident];o=old['item'].get('components',{});n=new['item'].get('components',{})
        changed=[k for k in sorted(set(o)|set(n)) if k not in o or k not in n or compact(o[k])!=compact(n[k])]
        oe=old['item'].get('events',MISSING);ne=new['item'].get('events',MISSING)
        out += [f'### `{ident}`', '', f'- Источники: `{old["path"]}` · `{new["path"]}`.',
                f'- `format_version`: {md(old["data"].get("format_version",MISSING))} → {md(new["data"].get("format_version",MISSING))}.',
                f'- Description: {md(old["item"].get("description",MISSING))} → {md(new["item"].get("description",MISSING))}.',
                f'- Event keys: {md(sorted(oe) if isinstance(oe,dict) else oe)} → {md(sorted(ne) if isinstance(ne,dict) else ne)}.', '',
                '| Компонент | 1.6 | 2.8.14 |','|---|---|---|']
        for key in changed:out.append(f'| `{key}` | {md(o.get(key,MISSING))} | {md(n.get(key,MISSING))} |')
        out.append('')
    return '\n'.join(out)+'\n'

def main():
    (ROOT/'docs/item-version-matrix.md').write_text(build(),encoding='utf-8')
    print('item version matrix written')
if __name__=='__main__':main()
