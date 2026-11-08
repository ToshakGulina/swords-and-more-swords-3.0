#!/usr/bin/env python3
"""Fingerprint all resource-pack paths shared with official samples and inspect key maps."""
import argparse
from collections import defaultdict
from functools import lru_cache
import json
import struct
from pathlib import Path
from zipfile import ZipFile
import json5
from build_vanilla_reference_facts import REFERENCE
from build_vanilla_detail_diff import ROOT, sha256, changed_values

ADDONS={'1.6':('SwordsAndMoreSwords.1.6.mcaddon','Sword_R/'),'2.8.8':('swordsandmoreswords_2_8_8.mcaddon','Swords_R/'),'2.8.14':('swordsandmoreswords-2-8-14.mcaddon','Swords_R/')}
MAPS={
    'blocks.json': (),
    'textures/item_texture.json':('texture_data',),
    'textures/terrain_texture.json':('texture_data',),
    'sounds/sound_definitions.json':('sound_definitions',),
    'sounds.json':('entity_sounds','entities'),
    'ui/how_to_play_screen.json':(),
}
CLIENTS=('entity/enderman.entity.json','entity/player.entity.json','entity/witch.entity.json','entity/witch.v1.0.entity.json')
RENDERS=('render_controllers/default.render_controllers.json','render_controllers/enderman.render_controllers.json','render_controllers/witch.render_controllers.json')

def png_size(raw):
    if len(raw) >= 24 and raw[:8] == b'\x89PNG\r\n\x1a\n' and raw[12:16] == b'IHDR':
        return list(struct.unpack('>II',raw[16:24]))
    return None

@lru_cache(maxsize=50)
def parse_json(raw):
    return json5.loads(raw.decode('utf-8-sig'),allow_duplicate_keys=False)

def parse_lang(raw):
    records=defaultdict(list)
    for line in raw.decode('utf-8-sig').splitlines():
        if not line.strip() or line.lstrip().startswith('#'):continue
        if '=' not in line:raise ValueError('Unexpected language line: '+line[:120])
        key,value=line.split('=',1);records[key].append(value)
    return dict(records)

def map_diff(ref,addon):
    if not isinstance(ref,dict) or not isinstance(addon,dict):raise ValueError('Expected key map')
    a,b=set(ref),set(addon)
    return {'reference_count':len(a),'addon_count':len(b),'only_reference_count':len(a-b),
            'only_addon':sorted(b-a),'different_common':{k:{'reference':ref[k],'addon':addon[k]} for k in sorted(a&b) if ref[k]!=addon[k]},
            'equal_common_count':sum(ref[k]==addon[k] for k in a&b)}

def nested(obj,path):
    for part in path: obj=obj[part]
    return obj

def describe(path,raw_ref,raw_addon):
    if path in MAPS:
        return {'kind':'key_map','path':list(MAPS[path]),'diff':map_diff(nested(parse_json(raw_ref),MAPS[path]),nested(parse_json(raw_addon),MAPS[path]))}
    if path in CLIENTS:
        ref=parse_json(raw_ref)['minecraft:client_entity']['description'];new=parse_json(raw_addon)['minecraft:client_entity']['description']
        return {'kind':'client_description','changed_values':changed_values(ref,new)}
    if path in RENDERS:
        ref=parse_json(raw_ref)['render_controllers'];new=parse_json(raw_addon)['render_controllers']
        return {'kind':'render_controller','changed_values':changed_values(ref,new)}
    if path=='textures/flipbook_textures.json':
        ref=parse_json(raw_ref);new=parse_json(raw_addon)
        return {'kind':'array','reference_length':len(ref),'addon_length':len(new),'addon_values':new,'equal':ref==new}
    if path=='texts/en_US.lang':
        ref=parse_lang(raw_ref);new=parse_lang(raw_addon)
        return {'kind':'language','diff':map_diff(ref,new),'addon_duplicate_keys':{k:v for k,v in new.items() if len(v)>1},'reference_duplicate_key_count':sum(len(v)>1 for v in ref.values())}
    return None

def build(paths):
    data={'method':'shared relative RP paths; byte hashes, selected strict JSON5 key maps and client descriptions; no resource-pack loading assumed','addons':{},'references':{}}
    addon_data={}
    for ver,(filename,prefix) in ADDONS.items():
        with ZipFile(ROOT/'sources'/filename) as z:
            addon_data[ver]={n[len(prefix):]:z.read(n) for n in z.namelist() if n.startswith(prefix) and not n.endswith('/')}
        data['addons'][ver]={'file_count':len(addon_data[ver]),'files':{n:{'sha256':sha256(raw),'bytes':len(raw),'png_size':png_size(raw)} for n,raw in addon_data[ver].items()}}
    for ver,(commit,expected) in REFERENCE.items():
        if sha256(paths[ver].read_bytes())!=expected:raise ValueError('Reference ZIP SHA-256 mismatch: '+ver)
        prefix=f'bedrock-samples-{ver}/resource_pack/'
        with ZipFile(paths[ver]) as z:
            refnames={n[len(prefix):] for n in z.namelist() if n.startswith(prefix) and not n.endswith('/')}
            shared=set().union(*(set(v)&refnames for v in addon_data.values()))
            refs={n:z.read(prefix+n) for n in shared}
        compared={}
        for addon_ver,files in addon_data.items():
            compared[addon_ver]={}
            for name in sorted(set(files)&refnames):
                raw,ref=files[name],refs[name]
                item={'reference_sha256':sha256(ref),'reference_bytes':len(ref),'reference_png_size':png_size(ref),'byte_equal':raw==ref}
                details=describe(name,ref,raw)
                if details is not None:item['details']=details
                compared[addon_ver][name]=item
        data['references'][ver]={'commit':commit,'zip_sha256':expected,'reference_file_count':len(refnames),'comparisons':compared}
    return data

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--reference-119',type=Path,required=True);p.add_argument('--reference-120',type=Path,required=True);p.add_argument('--output',type=Path,default=ROOT/'data/vanilla-resource-diff.json');args=p.parse_args()
    data=build({'1.19.40.2':args.reference_119,'1.20.30.1':args.reference_120});args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(data,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n',encoding='utf-8');print('Resource comparisons:',args.output)

if __name__=='__main__':main()
