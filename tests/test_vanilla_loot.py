import hashlib
import json
import sys
import unittest
from pathlib import Path
from zipfile import ZipFile

import json5

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
from build_vanilla_loot_diff import PREFIX, match_pools, read_table, render_markdown
from build_vanilla_reference_facts import REFERENCE


def reconstruct_reference(addon,entry):
    """Reconstruct parsed sample from matching addon pools and recorded differences."""
    ref={k:v for k,v in addon.items() if k!='pools'}
    for key,difference in entry['other_fields'].items():
        if difference['reference']['present']:ref[key]=difference['reference']['value']
        else:ref.pop(key,None)
    if not entry['pools_present']['reference']:
        return ref
    pools=addon.get('pools',[]);comparison=entry['pool_comparison']
    n=len(comparison['equal_pairs_reference_addon'])+len(comparison['only_reference'])
    reference=[None]*n
    for ri,ai in comparison['equal_pairs_reference_addon']:reference[ri]=pools[ai]
    for p in comparison['only_reference']:reference[p['index']]=p['value']
    if any(p is None for p in reference):raise AssertionError('Unfilled reference pool index')
    ref['pools']=reference
    return ref


class VanillaLootTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=json.loads((ROOT/'data/vanilla-loot-diff.json').read_text())
        with ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as z:
            cls.addon={name:read_table(z.read(PREFIX+name)) for name in cls.data['addon_files']}

    def reference(self,ver,path):
        return reconstruct_reference(self.addon[path],self.data['references'][ver]['tables'][path])

    def test_complete_path_hashes_and_self_consistency(self):
        data=self.data
        self.assertEqual(60,len(data['addon_files']))
        with ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as main, ZipFile(ROOT/'sources/swordsandmoreswords_2_8_8.mcaddon') as old:
            for z in (main,old):
                self.assertEqual(set(data['addon_files']),{n[len(PREFIX):] for n in z.namelist() if n.startswith(PREFIX) and n.endswith('.json')})
            for name,hash_ in data['addon_files'].items():
                raw=main.read(PREFIX+name)
                self.assertEqual(raw,old.read(PREFIX+name))
                self.assertEqual(hash_,hashlib.sha256(raw).hexdigest())
        with ZipFile(ROOT/'sources/SwordsAndMoreSwords.1.6.mcaddon') as old:
            self.assertFalse([n for n in old.namelist() if n.startswith('Sword_B/loot_tables/')])
        counts={'1.19.40.2':(52,33,19,8,153),'1.20.30.1':(52,28,24,8,161)}
        for ver,r in data['references'].items():
            self.assertEqual(REFERENCE[ver],(r['commit'],r['zip_sha256']))
            self.assertEqual(set(data['addon_files']),set(r['tables']))
            tables=r['tables'].values();actual=(sum(t['reference_present'] for t in tables),sum(t.get('equal') is True for t in tables),sum(t.get('equal') is False for t in tables),sum(not t['reference_present'] for t in tables),r['reference_table_count'])
            self.assertEqual(counts[ver],actual)
            for name,entry in r['tables'].items():
                if not entry['reference_present']:continue
                self.assertRegex(entry['reference_sha256'],r'^[0-9a-f]{64}$')
                reference=self.reference(ver,name);addon=self.addon[name]
                self.assertEqual(reference==addon,entry['equal'],(ver,name))
                self.assertEqual(match_pools(reference.get('pools',[]),addon.get('pools',[])),entry['pool_comparison'])
        self.assertEqual(render_markdown(data),(ROOT/'docs/vanilla-loot-detail-ledger.md').read_text())

    def test_pool_matching_duplicates_and_reordering(self):
        a={'entries':[{'name':'x'}]};b={'entries':[{'name':'y'}]};c={'entries':[{'name':'z'}]}
        result=match_pools([a,a,b],[a,b,c])
        self.assertEqual([[0,0],[2,1]],result['equal_pairs_reference_addon'])
        self.assertEqual([{'index':1,'value':a}],result['only_reference'])
        self.assertEqual([{'index':2,'value':c}],result['only_addon'])

    def test_lost_vanilla_entries_and_sword_weights(self):
        missing={
            'chests/abandoned_mineshaft.json':'minecraft:glow_berries',
            'chests/pillager_outpost.json':'minecraft:goat_horn',
            'chests/shipwrecksupply.json':'minecraft:moss_block',
            'chests/simple_dungeon.json':'minecraft:record_otherside',
            'chests/stronghold_corridor.json':'minecraft:record_otherside',
            'chests/spawn_bonus_chest.json':'minecraft:mangrove_log',
        }
        names=lambda table:[e.get('name') for p in table['pools'] for e in p.get('entries',[])]
        for path,item in missing.items():
            self.assertNotIn(item,names(self.addon[path]))
            for ver in REFERENCE:self.assertIn(item,names(self.reference(ver,path)),(ver,path,item))
        for path,item in [('chests/pillager_outpost.json','minecraft:sentry_armor_trim_smithing_template'),('chests/shipwrecksupply.json','minecraft:coast_armor_trim_smithing_template'),('chests/stronghold_corridor.json','minecraft:eye_armor_trim_smithing_template')]:
            self.assertNotIn(item,names(self.addon[path]));self.assertIn(item,names(self.reference('1.20.30.1',path)))
        path='chests/abandoned_mineshaft.json'
        old=self.reference('1.19.40.2',path)['pools'][1]['entries'];new=self.addon[path]['pools'][1]['entries']
        self.assertEqual((98,86),(sum(e['weight'] for e in old),sum(e['weight'] for e in new)))
        self.assertEqual(15,next(e['weight'] for e in old if e.get('name')=='minecraft:glow_berries'))
        self.assertEqual(3,next(e['weight'] for e in new if e.get('name')=='effect:spider_sword'))
        path='gameplay/fishing/treasure.json';old=self.reference('1.19.40.2',path)['pools'][0];new=self.addon[path]['pools'][0]
        self.assertEqual((1,1),(old['rolls'],new['rolls']))
        self.assertEqual((36,41),(sum(e['weight'] for e in old['entries']),sum(e['weight'] for e in new['entries'])))
        self.assertEqual(5,next(e['weight'] for e in new['entries'] if e.get('name')=='effect:jungle_sword'))

    def test_mob_pools_preserve_conditions_and_shifted_vanilla_pools(self):
        def loot(name):return self.addon['entities/'+name+'.json']['pools']
        blaze=loot('blaze')[1]
        self.assertEqual([{'condition':'killed_by_entity','entity_type':'minecraft:snow_golem'},{'condition':'random_chance_with_looting','chance':0.025,'looting_multiplier':0.02}],blaze['conditions'])
        self.assertEqual('effect:blaze_sword',blaze['entries'][0]['name'])
        elder=loot('elder_guardian');self.assertEqual(5,len(elder))
        self.assertEqual('effect:sponge_sword',elder[1]['entries'][0]['name'])
        self.assertEqual([{'condition':'killed_by_player'},{'condition':'random_chance_with_looting','chance':0.065,'looting_multiplier':0.02}],elder[1]['conditions'])
        self.assertEqual([[0,0],[1,2],[2,3],[3,4]],self.data['references']['1.19.40.2']['tables']['entities/elder_guardian.json']['pool_comparison']['equal_pairs_reference_addon'])
        for name,chance in [('shulker',0.045),('wither_skeleton',0.025)]:
            extra=loot(name)[-1]
            self.assertEqual([{'condition':'killed_by_player'},{'condition':'random_chance_with_looting','chance':chance,'looting_multiplier':0.02}],extra['conditions'])


if __name__=='__main__':unittest.main()
