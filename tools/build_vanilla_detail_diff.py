#!/usr/bin/env python3
"""Preserve complete differing top-level entity values for sixteen vanilla IDs.

The input archives are never modified and external sample archives are not downloaded.
See docs/manual-vanilla-entities-2.8.md for the method and reproducibility instructions.
"""
import argparse
import hashlib
import json
from pathlib import Path
from zipfile import ZipFile

import json5
from build_vanilla_reference_facts import REFERENCE, VANILLA_NAMES

ROOT = Path(__file__).resolve().parents[1]
NAMES = tuple(x for x in VANILLA_NAMES if x not in {
    'creeper', 'item', 'player', 'blaze', 'cat', 'parrot', 'wolf', 'skeleton'
})


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def read_json(z, path, name):
    data = z.read(path)
    obj = json5.loads(data.decode('utf-8-sig'), allow_duplicate_keys=False)
    if obj['minecraft:entity']['description']['identifier'] != 'minecraft:' + name:
        raise ValueError('Unexpected identifier: ' + path)
    return data, obj


def changed_values(reference, addon):
    """Use exact key existence; objects unordered, arrays ordered, numbers by Python equality."""
    result = {}
    for key in sorted(reference.keys() | addon.keys()):
        left = {'present': True, 'value': reference[key]} if key in reference else {'present': False}
        right = {'present': True, 'value': addon[key]} if key in addon else {'present': False}
        if left != right:
            result[key] = {'reference': left, 'addon': right}
    return result


def compare(reference, addon):
    old, new = reference['minecraft:entity'], addon['minecraft:entity']
    result = {'root': changed_values({k: reference[k] for k in ('format_version',) if k in reference}, {k: addon[k] for k in ('format_version',) if k in addon})}
    for section in ('description', 'components', 'component_groups', 'events'):
        a, b = old.get(section, {}), new.get(section, {})
        if not isinstance(a, dict) or not isinstance(b, dict):
            raise ValueError('Expected object for ' + section)
        result[section] = changed_values(a, b)
    return result


def build(paths):
    result = {
        'method': 'complete differing top-level values, JSON5 without duplicate keys; arrays ordered, object keys unordered, numeric values use Python equality; not engine execution',
        'entity_names': list(NAMES), 'entities': {}
    }
    addons = {}
    with ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as main, ZipFile(ROOT/'sources/swordsandmoreswords_2_8_8.mcaddon') as old:
        for name in NAMES:
            path = f'Swords_B/entities/{name}.json'
            data, obj = read_json(main, path, name)
            if old.read(path) != data:
                raise ValueError(f'Addon entity differs between 2.8.8 and 2.8.14: {name}')
            addons[name] = (sha256(data), obj)
            result['entities'][name] = {'addon_sha256': sha256(data), 'comparisons': {}}
    for version, (commit, expected) in REFERENCE.items():
        path = paths[version]
        if sha256(path.read_bytes()) != expected:
            raise ValueError(f'Reference ZIP SHA-256 mismatch: {version}')
        with ZipFile(path) as z:
            for name in NAMES:
                reference_data, reference = read_json(z, f'bedrock-samples-{version}/behavior_pack/entities/{name}.json', name)
                result['entities'][name]['comparisons'][version] = {
                    'reference_commit': commit, 'reference_zip_sha256': expected,
                    'reference_file_sha256': sha256(reference_data),
                    'sections': compare(reference, addons[name][1]),
                }
    return result


def render_markdown(data):
    lines = [
        '# Полные значения отличающихся ключей 16 ванильных определений', '',
        'Машинная структурная выписка; интерпретация, ограничения и источники — [ручной разбор](manual-vanilla-entities-2.8.md).',
        'Полные значения каждого изменённого ключа сравниваются отдельно, массивы сохраняют порядок; числа 1 и 1.0 считаются равными.',
        '`present: false` означает отсутствие ключа в выбранном объекте, а не поведение движка. Одинаковые значения не выводятся.',
        'Файлы этих 16 определений в 2.8.8 и 2.8.14 побайтово совпадают; здесь называем их общим обозначением 2.x.', '',
    ]
    for name, entity in sorted(data['entities'].items()):
        lines.extend([f'## `minecraft:{name}`', '', f'Аддон SHA-256: `{entity["addon_sha256"]}`.', ''])
        for ver, diff in sorted(entity['comparisons'].items()):
            lines.extend([f'### Образец `{ver}`', '', f'Файл образца SHA-256: `{diff["reference_file_sha256"]}`.', ''])
            for section, keys in sorted(diff['sections'].items()):
                if not keys:
                    continue
                lines.extend([f'#### `{section}`', ''])
                for key, values in keys.items():
                    lines.extend([f'**`{key}`**', '', '```json', json.dumps(values, ensure_ascii=False, indent=2, sort_keys=True), '```', ''])
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--reference-119', type=Path, required=True)
    parser.add_argument('--reference-120', type=Path, required=True)
    parser.add_argument('--output', type=Path, default=ROOT/'data/vanilla-entity-detail-diff.json')
    parser.add_argument('--markdown-output', type=Path, default=ROOT/'docs/vanilla-entity-detail-ledger.md')
    args = parser.parse_args()
    data = build({'1.19.40.2': args.reference_119, '1.20.30.1': args.reference_120})
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(',', ':')) + '\n', encoding='utf-8')
    args.markdown_output.parent.mkdir(parents=True, exist_ok=True)
    args.markdown_output.write_text(render_markdown(data), encoding='utf-8')
    print('Detailed reference differences:', args.output, args.markdown_output)


if __name__ == '__main__':
    main()
