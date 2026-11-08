#!/usr/bin/env python3
"""Compare all 2.x loot-table paths against two official sample archives, offline."""
import argparse
import json
from pathlib import Path
from zipfile import ZipFile
import json5
from build_vanilla_reference_facts import REFERENCE
from build_vanilla_detail_diff import ROOT, sha256, changed_values

PREFIX = 'Swords_B/loot_tables/'


def read_table(raw):
    table=json5.loads(raw.decode('utf-8-sig'),allow_duplicate_keys=False)
    if not isinstance(table,dict):raise ValueError('Loot table must be an object')
    if 'pools' in table and not isinstance(table['pools'],list):raise ValueError('pools must be an array')
    return table


def match_pools(ref,addon):
    """Deterministically pair equal objects; unmatched entries retain original indices."""
    used=set();pairs=[];unmatched_ref=[]
    for ri, old in enumerate(ref):
        match=next((ai for ai,new in enumerate(addon) if ai not in used and old==new),None)
        if match is None: unmatched_ref.append({'index':ri,'value':old})
        else: used.add(match); pairs.append([ri,match])
    unmatched_addon=[{'index':ai,'value':v} for ai,v in enumerate(addon) if ai not in used]
    return {'equal_pairs_reference_addon':pairs,'only_reference':unmatched_ref,'only_addon':unmatched_addon}


def build(paths):
    with ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as a, ZipFile(ROOT/'sources/swordsandmoreswords_2_8_8.mcaddon') as b:
        names=sorted(n[len(PREFIX):] for n in a.namelist() if n.startswith(PREFIX) and n.endswith('.json'))
        other=sorted(n[len(PREFIX):] for n in b.namelist() if n.startswith(PREFIX) and n.endswith('.json'))
        if names!=other:raise ValueError('Loot path sets differ between add-on versions')
        raw_addons={name:a.read(PREFIX+name) for name in names}
        for name,raw in raw_addons.items():
            if b.read(PREFIX+name)!=raw:raise ValueError('Loot files differ between add-on versions: '+name)
    addon={name:read_table(raw) for name,raw in raw_addons.items()}
    data={'method':'all 2.x loot paths; strict JSON5; ordered arrays; Python numeric equality; missing sample path is not a game claim',
          'addon_files':{name:sha256(raw) for name,raw in raw_addons.items()},'references':{}}
    for version,(commit,expected) in REFERENCE.items():
        if sha256(paths[version].read_bytes())!=expected:raise ValueError('Reference ZIP SHA-256 mismatch: '+version)
        prefix=f'bedrock-samples-{version}/behavior_pack/loot_tables/'
        with ZipFile(paths[version]) as z:
            ref_names={n[len(prefix):] for n in z.namelist() if n.startswith(prefix) and n.endswith('.json')}
            tables={}
            for name in names:
                if name not in ref_names:
                    tables[name]={'reference_present':False}
                    continue
                raw=z.read(prefix+name);ref=read_table(raw);new=addon[name]
                pools_old=ref.get('pools',[]);pools_new=new.get('pools',[])
                tables[name]={'reference_present':True,'reference_sha256':sha256(raw),'equal':ref==new,
                    'pools_present':{'reference':'pools' in ref,'addon':'pools' in new},
                    'pools_field':changed_values({'pools':ref['pools']} if 'pools' in ref else {}, {'pools':new['pools']} if 'pools' in new else {}).get('pools') if ('pools' not in ref or 'pools' not in new) else None,
                    'other_fields':changed_values({k:v for k,v in ref.items() if k!='pools'},{k:v for k,v in new.items() if k!='pools'}),
                    'pool_comparison':match_pools(pools_old,pools_new)}
        data['references'][version]={'commit':commit,'zip_sha256':expected,'reference_table_count':len(ref_names),'tables':tables}
    return data


def render_markdown(data):
    lines=['# Полная сравнительная выписка таблиц добычи 2.x и образцов Mojang','',
           '[Метод, результаты и ограничения](manual-vanilla-loot-2.8.md). Идентичные пул-объекты сопоставлены по равенству без учёта положения; пары индексов сохранены. Несовпадающие пулы приведены целиком с исходными индексами. Изменение индекса само по себе не доказывает изменения механики. Отсутствие файла образца — не отсутствие в игре.','']
    for version,ref in sorted(data['references'].items()):
        lines.extend([f'## Образец `{version}`',''])
        for name,t in sorted(ref['tables'].items()):
            if not t['reference_present'] or t['equal']:continue
            lines.extend([f'### `{name}`','',f'SHA-256 add-on `{data["addon_files"][name]}`; образца `{t["reference_sha256"]}`.','',
                          '```json',json.dumps({k:t[k] for k in ('pools_present','pools_field','other_fields','pool_comparison')},ensure_ascii=False,sort_keys=True,indent=2),'```',''])
    return '\n'.join(lines)


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--reference-119',type=Path,required=True);p.add_argument('--reference-120',type=Path,required=True)
    p.add_argument('--output',type=Path,default=ROOT/'data/vanilla-loot-diff.json');p.add_argument('--markdown-output',type=Path,default=ROOT/'docs/vanilla-loot-detail-ledger.md');args=p.parse_args()
    data=build({'1.19.40.2':args.reference_119,'1.20.30.1':args.reference_120});args.output.parent.mkdir(parents=True,exist_ok=True);args.markdown_output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(data,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n',encoding='utf-8');args.markdown_output.write_text(render_markdown(data),encoding='utf-8');print('Loot diff:',args.output,args.markdown_output)

if __name__=='__main__':main()
