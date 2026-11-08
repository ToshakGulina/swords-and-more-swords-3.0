#!/usr/bin/env python3
"""Preserve detailed comparison values for player in 1.6/2.x and five vanilla mobs in 2.x."""
import argparse
import json
from pathlib import Path
from zipfile import ZipFile

from build_vanilla_reference_facts import REFERENCE
from build_vanilla_detail_diff import ROOT, sha256, read_json, compare

NAMES = ('player', 'blaze', 'cat', 'parrot', 'skeleton', 'wolf')
ADDON_FILES = {'1.6': ('SwordsAndMoreSwords.1.6.mcaddon', 'Sword_B'), '2.8.8': ('swordsandmoreswords_2_8_8.mcaddon', 'Swords_B'), '2.8.14': ('swordsandmoreswords-2-8-14.mcaddon', 'Swords_B')}


def build(paths):
    out = {'method': 'complete differing top-level values; strict JSON5; not engine execution', 'entities': {}}
    addons = {}
    for ver, (filename, pack) in ADDON_FILES.items():
        addons[ver] = {}
        with ZipFile(ROOT/'sources'/filename) as z:
            for name in (('player',) if ver == '1.6' else NAMES):
                data, obj = read_json(z, f'{pack}/entities/{name}.json', name)
                addons[ver][name] = (sha256(data), obj)
    for name in NAMES:
        out['entities'][name] = {'addons': {}}
        for addon_ver in ADDON_FILES:
            if name not in addons[addon_ver]: continue
            out['entities'][name]['addons'][addon_ver] = {'file_sha256': addons[addon_ver][name][0], 'comparisons': {}}
    for ref_ver, (commit, expected) in REFERENCE.items():
        if sha256(paths[ref_ver].read_bytes()) != expected:
            raise ValueError('Reference ZIP SHA-256 mismatch: ' + ref_ver)
        with ZipFile(paths[ref_ver]) as z:
            for name in NAMES:
                raw, reference = read_json(z, f'bedrock-samples-{ref_ver}/behavior_pack/entities/{name}.json', name)
                for addon_ver in ADDON_FILES:
                    if name not in addons[addon_ver]: continue
                    result = out['entities'][name]['addons'][addon_ver]['comparisons']
                    result[ref_ver] = {'reference_commit': commit, 'reference_zip_sha256': expected,
                                       'reference_file_sha256': sha256(raw),
                                       'sections': compare(reference, addons[addon_ver][name][1])}
    return out


def render_markdown(data):
    lines = [
        '# Полные значения отличающихся ключей player 1.6/2.x и пяти ванильных мобов 2.x', '',
        'Структурная машинная выписка без игры. [Источники, ограничения, воспроизведение и ручной разбор](manual-vanilla-override-review.md).',
        'Выводятся полные значения каждого отличающегося ключа в выбранных разделах; одинаковые не выводятся.',
        '`present:false` — ключ отсутствует, а не значение по умолчанию; массивы упорядочены, 1 и 1.0 равны.', '',
    ]
    for name, entity in sorted(data['entities'].items()):
        lines.extend([f'## `minecraft:{name}`', ''])
        for addon_ver, addon in sorted(entity['addons'].items()):
            lines.extend([f'### Аддон `{addon_ver}`', '', f'SHA-256 файла: `{addon["file_sha256"]}`.', ''])
            for ref_ver, diff in sorted(addon['comparisons'].items()):
                lines.extend([f'#### Образец `{ref_ver}`', '', f'SHA-256 файла образца: `{diff["reference_file_sha256"]}`.', ''])
                for section, keys in sorted(diff['sections'].items()):
                    if not keys: continue
                    lines.extend([f'##### `{section}`', ''])
                    for key, values in sorted(keys.items()):
                        lines.extend([f'**`{key}`**', '', '```json', json.dumps(values, ensure_ascii=False, indent=2, sort_keys=True), '```', ''])
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--reference-119', type=Path, required=True)
    parser.add_argument('--reference-120', type=Path, required=True)
    parser.add_argument('--output', type=Path, default=ROOT/'data/vanilla-six-detail-diff.json')
    parser.add_argument('--markdown-output', type=Path, default=ROOT/'docs/vanilla-six-detail-ledger.md')
    args = parser.parse_args()
    data = build({'1.19.40.2': args.reference_119, '1.20.30.1': args.reference_120})
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.markdown_output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(',', ':'))+'\n', encoding='utf-8')
    args.markdown_output.write_text(render_markdown(data), encoding='utf-8')
    print('Detailed differences:', args.output, args.markdown_output)


if __name__ == '__main__':
    main()
