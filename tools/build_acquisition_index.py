#!/usr/bin/env python3
"""Index literal acquisition declarations; deliberately not a Bedrock validator."""
import collections
import io
import json
import zipfile
from pathlib import Path

import json5
import nbtlib
from build_structures import item_paths

ROOT = Path(__file__).resolve().parents[1]
VERSIONS = [('1.6', 'SwordsAndMoreSwords.1.6.mcaddon', 'Sword_B'),
            ('2.8.8', 'swordsandmoreswords_2_8_8.mcaddon', 'Swords_B'),
            ('2.8.14', 'swordsandmoreswords-2-8-14.mcaddon', 'Swords_B')]

def compact(obj):
    return json.dumps(obj, ensure_ascii=False, separators=(',', ':'))

def output_items(value):
    if isinstance(value, list):
        return [item for x in value for item in output_items(x)]
    if isinstance(value, dict):
        return [value['item']] if isinstance(value.get('item'), str) else []
    return [value] if isinstance(value, str) else []

def loot_entries(node, path='$'):
    """Report every object explicitly typed item or loot_table, including nested objects."""
    if isinstance(node, dict):
        if node.get('type') in ('item', 'loot_table') and isinstance(node.get('name'), str):
            yield path, node
        for key, value in node.items():
            yield from loot_entries(value, f'{path}.{key}')
    elif isinstance(node, list):
        for i, value in enumerate(node):
            yield from loot_entries(value, f'{path}[{i}]')

def trades(node, path='$'):
    if isinstance(node, dict):
        if isinstance(node.get('gives'), list) and isinstance(node.get('wants'), list):
            yield path, node
        for key, value in node.items():
            yield from trades(value, f'{path}.{key}')
    elif isinstance(node, list):
        for i, value in enumerate(node):
            yield from trades(value, f'{path}[{i}]')

def table_target(pack, name):
    name = name if name.endswith('.json') else name + '.json'
    return pack + '/' + name

def build(version, filename, pack):
    with zipfile.ZipFile(ROOT / 'sources' / filename) as archive:
        files = {n: archive.read(n) for n in archive.namelist() if not n.endswith('/')}
    def parse(name):
        return json5.loads(files[name].decode('utf-8-sig'))
    items = {}
    for name in sorted(files):
        if name.startswith(pack + '/items/') and name.endswith('.json'):
            identifier = parse(name)['minecraft:item']['description']['identifier']
            if identifier in items:
                raise ValueError(f'duplicate item ID: {identifier}')
            items[identifier] = name
    recipes = {}
    loot = {}
    trading = {}
    structures = collections.defaultdict(list)
    errors = []
    for name in sorted(files):
        if name.startswith(pack + '/recipes/') and name.endswith('.json'):
            try:
                obj = parse(name)
                for kind, data in obj.items():
                    if kind.startswith('minecraft:recipe_') and isinstance(data, dict):
                        recipes[(name, kind)] = data
            except (ValueError, UnicodeDecodeError) as exc:
                errors.append((name, str(exc).splitlines()[0]))
        if name.startswith(pack + '/loot_tables/') and name.endswith('.json'):
            try:
                loot[name] = parse(name)
            except (ValueError, UnicodeDecodeError) as exc:
                errors.append((name, str(exc).splitlines()[0]))
        if name.startswith(pack + '/trading/') and name.endswith('.json'):
            try:
                trading[name] = parse(name)
            except (ValueError, UnicodeDecodeError) as exc:
                errors.append((name, str(exc).splitlines()[0]))
        if name.startswith(pack + '/structures/') and name.endswith('.mcstructure'):
            try:
                nbt = nbtlib.File.parse(io.BytesIO(files[name]), byteorder='little')
                for path, ident in item_paths(nbt['structure']):
                    structures[ident].append((name, path))
            except (ValueError, KeyError, OSError) as exc:
                errors.append((name, str(exc).splitlines()[0]))
    refs = collections.defaultdict(list)
    reverse_tables = collections.defaultdict(list)
    for source, obj in loot.items():
        for path, entry in loot_entries(obj):
            if entry['type'] == 'item':
                refs[entry['name']].append((source, path, entry))
            else:
                target = table_target(pack, entry['name'])
                reverse_tables[target].append((source, path, entry))
    trade_refs = collections.defaultdict(list)
    for source, obj in trading.items():
        for path, trade in trades(obj):
            for ident in output_items(trade['gives']):
                trade_refs[ident].append((source, path, trade))
    out = [f'# Объявленные пути получения — архив {version}', '',
           'Автоматический указатель буквальных результатов рецептов (включая furnace output), записей type=item таблиц добычи, родителей вложенных loot_table, сделок с предметом в gives и NBT-полей Name структур. Это перечень деклараций, а не доказательство получения предмета. Внешние/ванильные пути, генерация, команды, скрипты, другие таблицы обмена и события могут дать предмет другими способами. Запись в структуре может быть в стойке для брони или хранилище, а не дропом. Таблица может не вызываться. Семантика, регистрация, правильность синтаксиса и чувствительность ID к регистру требуют проверки движка.', '',
           'Родительские цепочки строятся только по точным текстовым путям loot_table с добавлением `.json` при её отсутствии. Циклы обозначаются явно; внешняя таблица не анализируется. Показаны полные объекты записей, но для вычисления вероятностей дополнительно нужны полные пулы, rolls, условия, функции и quality — см. [реестр мира](world-ledger-' + version + '.md). Веса не объявляются шансами.', '',
           '## Диагностика чтения', '']
    out += [f'- `{name}`: `{error}`' for name, error in errors] or ['- Ошибок разбора в обработанных категориях не обнаружено.']
    out += ['', '## Все рецепты и диагностика шаблонов', '']
    for (name, kind), recipe in recipes.items():
        out += [f'### `{name}` — `{kind}`', '', f'- Полное определение: `{compact(recipe)}`']
        pattern, key = recipe.get('pattern'), recipe.get('key')
        if isinstance(pattern, list) and all(isinstance(x, str) for x in pattern) and isinstance(key, dict):
            used = set(''.join(pattern)) - {' '}
            missing, unused = sorted(used - set(key)), sorted(set(key) - used)
            out.append(f'- Символы pattern без key: `{compact(missing)}`; ключи не использованы в pattern: `{compact(unused)}`. Интерпретация символов и валидность — на проверку движка.')
        output = recipe.get('result', recipe.get('output'))
        for ident in output_items(output):
            if ident.startswith('effect:') and ident not in items:
                folded = [i for i in items if i.casefold() == ident.casefold()]
                out.append(f'- Результат `{ident}` не совпадает буквально ни с одним локальным ID предмета; совпадения без учёта регистра: `{compact(folded)}`. Совместимость не установлена.')
        out.append('')
    out += ['## Все записи type=loot_table и локальное разрешение', '']
    for target, incoming in sorted(reverse_tables.items()):
        for source, path, entry in incoming:
            out.append(f'- `{source}` {path} → `{target}` ({"локальный файл найден" if target in files else "локальный файл не найден"}): `{compact(entry)}`')
    if not reverse_tables:
        out.append('- Буквальных записей type=loot_table нет.')
    def parents(target, visited):
        for source, path, entry in sorted(reverse_tables.get(target, []), key=lambda x:(x[0],x[1])):
            if source in visited:
                yield [(source, path, entry, True)]
            else:
                yield [(source, path, entry, False)]
                for upper in parents(source, visited | {source}):
                    yield [(source, path, entry, False)] + upper
    out += ['', '## По предметам', '']
    for ident, item_path in sorted(items.items()):
        out += [f'### `{ident}`', '', f'- Определение: `{item_path}`.']
        matches = [(p, k, d) for (p, k), d in recipes.items() if ident in output_items(d.get('result', d.get('output')))]
        out += ['- Результаты рецептов: ' + ('; '.join(f'`{p}` (`{k}`)' for p,k,_ in matches) if matches else 'буквально не найдены в локальных файлах recipes') + '.']
        out.append('- Прямые записи loot:')
        if not refs[ident]:
            out.append('  - Буквально не найдены в локальных таблицах.')
        for source, path, entry in refs[ident]:
            out.append(f'  - `{source}` {path}: `{compact(entry)}`')
            for chain in parents(source, {source}):
                steps = ' ← '.join(f'`{p}` {loc}' + (' [цикл]' if cycle else '') + f' `{compact(e)}`' for p,loc,e,cycle in chain)
                out.append(f'    - Родитель: {steps}')
        out.append('- Сделки локальных таблиц (поле `gives`):')
        out += [f'  - `{p}` {path}: `{compact(trade)}`' for p,path,trade in trade_refs[ident]] or ['  - Не обнаружено.']
        out.append('- В структурах (поля `Name`):')
        out += [f'  - `{p}` {path}' for p,path in structures[ident]] or ['  - Не обнаружено.']
        out.append('')
    path = ROOT / 'docs' / f'acquisition-index-{version}.md'
    path.write_text('\n'.join(out) + '\n', encoding='utf-8')
    print(version, 'items',len(items), 'recipes',len(recipes), 'loot files',len(loot), 'table links',sum(map(len,reverse_tables.values())), 'trade files',len(trading), 'structures with item names',sum(map(len,structures.values())), 'errors',len(errors))

if __name__ == '__main__':
    for args in VERSIONS:
        build(*args)
