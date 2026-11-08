#!/usr/bin/env python3
"""Compare a hypothetical in-memory Creeper parse to two official samples.

The source is never changed; this is not evidence Bedrock accepts the original.
"""
import argparse
import json
from pathlib import Path
from zipfile import ZipFile
import json5
from build_vanilla_detail_diff import ROOT, sha256, read_json, compare
from build_vanilla_reference_facts import REFERENCE


def parse_diagnostic(raw):
    text = raw.decode('utf-8-sig').rstrip()
    try:
        json5.loads(text, allow_duplicate_keys=False)
    except ValueError:
        pass
    else:
        raise ValueError('Original Creeper unexpectedly parsed; refuse diagnostic transformation')
    if not text.endswith('}'):
        raise ValueError('Original does not end in a closing brace')
    transformed = text[:-1]
    obj = json5.loads(transformed, allow_duplicate_keys=False)
    if obj['minecraft:entity']['description']['identifier'] != 'minecraft:creeper':
        raise ValueError('Unexpected diagnostic identifier')
    return transformed, obj


def build(paths):
    with ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as a, ZipFile(ROOT/'sources/swordsandmoreswords_2_8_8.mcaddon') as b:
        raw=a.read('Swords_B/entities/creeper.json')
        if raw != b.read('Swords_B/entities/creeper.json'):
            raise ValueError('Creeper source differs between add-on versions')
    modified, obj = parse_diagnostic(raw)
    data = {'method':'hypothetical parse after UTF-8 BOM decoding, trailing whitespace removal and deletion of last closing brace in memory; NOT a fix or engine validation',
            'addon_original_sha256':sha256(raw), 'transformed_utf8_sha256':sha256(modified.encode('utf-8')), 'comparisons':{}}
    for version,(commit,expected) in REFERENCE.items():
        if sha256(paths[version].read_bytes()) != expected: raise ValueError('Reference ZIP SHA-256 mismatch: '+version)
        with ZipFile(paths[version]) as z:
            refraw, reference=read_json(z,f'bedrock-samples-{version}/behavior_pack/entities/creeper.json','creeper')
            data['comparisons'][version]={'reference_commit':commit,'reference_zip_sha256':expected,'reference_file_sha256':sha256(refraw),'sections':compare(reference,obj)}
    return data


def render_markdown(data):
    lines=['# Диагностическое сравнение повреждённого creeper.json', '',
           '**Не исправление и не поведение игры:** исходный файл JSON5 не разбирается; для этих гипотетических данных в памяти удалена только последняя закрывающая скобка после удаления конечных пробелов. Авторская задумка и поведение Bedrock не установлены.', '',
           '[Интерпретация и источники](manual-creeper-sword.md) · [метод внешних сравнений](manual-vanilla-override-review.md).', '',
           f'Оригинальный SHA-256: `{data["addon_original_sha256"]}`; преобразованный UTF-8 SHA-256: `{data["transformed_utf8_sha256"]}`.', '']
    for ver,diff in sorted(data['comparisons'].items()):
        lines.extend([f'## Образец `{ver}`', '',f'SHA-256 файла образца: `{diff["reference_file_sha256"]}`.', ''])
        for section,keys in sorted(diff['sections'].items()):
            if not keys:continue
            lines.extend([f'### `{section}`',''])
            for key,pair in sorted(keys.items()):
                lines.extend([f'**`{key}`**','','```json',json.dumps(pair,ensure_ascii=False,indent=2,sort_keys=True),'```',''])
    return '\n'.join(lines)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--reference-119',type=Path,required=True)
    p.add_argument('--reference-120',type=Path,required=True)
    p.add_argument('--output',type=Path,default=ROOT/'data/vanilla-creeper-diagnostic.json')
    p.add_argument('--markdown-output',type=Path,default=ROOT/'docs/vanilla-creeper-diagnostic-ledger.md')
    args=p.parse_args();data=build({'1.19.40.2':args.reference_119,'1.20.30.1':args.reference_120})
    args.output.parent.mkdir(parents=True,exist_ok=True);args.markdown_output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(data,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n',encoding='utf-8')
    args.markdown_output.write_text(render_markdown(data),encoding='utf-8')
    print('Diagnostic diff:',args.output,args.markdown_output)

if __name__=='__main__':main()
