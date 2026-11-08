#!/usr/bin/env python3
"""Build a compact source-grounded index of custom loot and local parent pools."""
import json
import zipfile
from pathlib import Path
import json5
from build_acquisition_index import table_target

ROOT = Path(__file__).resolve().parents[1]
VERSIONS = [('1.6', 'SwordsAndMoreSwords.1.6.mcaddon', 'Sword_B'),
            ('2.8.8', 'swordsandmoreswords_2_8_8.mcaddon', 'Swords_B'),
            ('2.8.14', 'swordsandmoreswords-2-8-14.mcaddon', 'Swords_B')]

def compact(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':'))

def read_tables(filename, pack):
    tables, errors, duplicates = {}, [], []
    with zipfile.ZipFile(ROOT / 'sources' / filename) as z:
        for name in sorted(z.namelist()):
            if not name.startswith(pack + '/loot_tables/') or not name.endswith('.json'):
                continue
            repeated = []
            def pairs(items):
                result = {}
                for key, value in items:
                    if key in result:
                        repeated.append(key)
                    result[key] = value
                return result
            try:
                tables[name] = json5.loads(z.read(name).decode('utf-8-sig'), object_pairs_hook=pairs)
            except (ValueError, UnicodeDecodeError) as exc:
                errors.append((name, str(exc).splitlines()[0]))
            if repeated:
                duplicates.append((name, repeated))
    return tables, errors, duplicates

def indexes(tables, pack):
    # Restrict to top-level pools and direct entry lists: nested entry structures
    # or nonstandard schemas require separate manual review.
    direct = set()
    edges = []
    for name, obj in tables.items():
        if not isinstance(obj, dict) or not isinstance(obj.get('pools', []), list):
            continue
        for i, pool in enumerate(obj.get('pools', [])):
            if not isinstance(pool, dict) or not isinstance(pool.get('entries', []), list):
                continue
            for j, entry in enumerate(pool.get('entries', [])):
                if not isinstance(entry, dict):
                    continue
                ident = entry.get('name')
                if entry.get('type') == 'item' and isinstance(ident, str) and ident.startswith(('effect:', 'effect99:')):
                    direct.add((name, i, j))
                elif entry.get('type') == 'loot_table' and isinstance(ident, str):
                    edges.append((name, i, j, table_target(pack, ident)))
    reachable = {name for name, _, _ in direct}
    while True:
        previous = len(reachable)
        reachable.update(name for name, _, _, target in edges if target in reachable)
        if len(reachable) == previous:
            break
    parent = {(name, i, j) for name, i, j, target in edges if target in reachable}
    return direct, parent

def render_section(out, label, pack, tables, direct, parent):
    out += [f'## {label}', '', f'Таблиц: {len(tables)}; прямых записей: {len(direct)}; родительских записей: {len(parent)}.', '']
    selected = direct | parent
    for name, index in sorted({(name, i) for name, i, _ in selected}):
        obj = tables[name]; pool = obj['pools'][index]; entries = pool['entries']
        table_fields = {k:v for k,v in obj.items() if k != 'pools'}
        pool_fields = {k:v for k,v in pool.items() if k != 'entries'}
        # Preserve relevant selection properties of every sibling, including missing weights.
        siblings = [{k:v for k,v in e.items() if k in ('type', 'name', 'weight', 'quality', 'conditions')} if isinstance(e,dict) else e for e in entries]
        out += [f'### `{name}` — `$.pools[{index}]`', '',
                f'- Поля таблицы, кроме pools: `{compact(table_fields)}`',
                f'- Поля пула, кроме entries: `{compact(pool_fields)}`',
                f'- Все записи в исходном порядке (type/name/weight/quality/conditions): `{compact(siblings)}`']
        for j, entry in enumerate(entries):
            if (name,index,j) in selected:
                kinds=[]
                if (name,index,j) in direct: kinds.append('локальный ID')
                if (name,index,j) in parent: kinds.append('родительская таблица')
                out.append(f'- `entries[{j}]`, {"; ".join(kinds)} — полный объект: `{compact(entry)}`')
        out.append('')

def build():
    data={version:(read_tables(filename,pack),pack) for version,filename,pack in VERSIONS}
    out=['# Контекст loot-пулов для предметов и блоков аддона', '',
         'Указаны все прямые записи `type=item` с именами `effect:` и `effect99:` внутри обычных `pools[].entries[]`, а также родительские `type=loot_table` с точным локальным путём к таким таблицам (транзитивно, с добавлением `.json`). Это декларации, не подтверждение вызова или регистрации; внешние таблицы, команды, события, структуры, торговля и другие способы получения не заменяются этим указателем.', '',
         'Для каждого пула сохранены все поля пула и таблицы вне списков, соседние записи с весами, quality и conditions, а интересующие записи — целиком, включая функции. Отсутствующее поле не заполняется предполагаемым значением. Для полных исходных данных соседних записей см. [реестр мира 2.8.14](world-ledger-2.8.14.md) и [2.8.8](world-ledger-2.8.8.md). Иные и нестандартные вложенные схемы не индексируются. Значения rolls, count и веса — сырой формат: они не доказывают вероятность успешного получения, а пустые результаты, условия, удача и механика движка могут иметь значение.', '', '[Условная модель выбора записей](loot-selection-model.md) показывает арифметику внутри уже активированного пула и явно не является вероятностью выпадения.', '', '## Диагностика', '']
    for version, ((tables,errors,duplicates),pack) in data.items():
        out.append(f'- {version}: {len(tables)} таблиц, ошибки: '+(compact(errors) if errors else 'нет')+'; повторные ключи: '+(compact(duplicates) if duplicates else 'нет')+'.')
    same=data['2.8.8'][0][0]==data['2.8.14'][0][0]
    out += ['', 'Сравнение JSON таблиц 2.8.8/2.8.14: '+('структурно равны; условия вызова таблиц за их пределами могут отличаться.' if same else 'имеются различия, показаны обе версии.'), '']
    for version in (['1.6','2.8.14'] if same else ['1.6','2.8.8','2.8.14']):
        ((tables,_,_),pack)=data[version]
        direct,parent=indexes(tables,pack)
        render_section(out,'2.8.8 и 2.8.14' if same and version=='2.8.14' else version,pack,tables,direct,parent)
    (ROOT/'docs/loot-context.md').write_text('\n'.join(out)+'\n',encoding='utf-8')
    for version, ((tables,errors,duplicates),pack) in data.items():
        direct,parent=indexes(tables,pack)
        print(f'{version}: {len(tables)} tables, {len(direct)} direct, {len(parent)} parent, {len(errors)} errors')

if __name__=='__main__': build()
