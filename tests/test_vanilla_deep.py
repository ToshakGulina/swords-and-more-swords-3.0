import hashlib
import json
import sys
import unittest
import zipfile
from pathlib import Path

import json5

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from build_vanilla_detail_diff import NAMES, changed_values, compare, render_markdown
from build_vanilla_reference_facts import REFERENCE


class VanillaDeepTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT/'data/vanilla-entity-detail-diff.json').read_text())
        cls.index = json.loads((ROOT/'data/vanilla-reference-facts.json').read_text())

    def test_all_diff_values_match_addons_and_previous_offline_index(self):
        self.assertEqual(16, len(NAMES))
        self.assertEqual(set(NAMES), set(self.data['entities']))
        with zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as main, zipfile.ZipFile(ROOT/'sources/swordsandmoreswords_2_8_8.mcaddon') as old:
            for name in NAMES:
                path=f'Swords_B/entities/{name}.json'
                raw=main.read(path)
                self.assertEqual(raw,old.read(path),name)
                self.assertEqual(hashlib.sha256(raw).hexdigest(),self.data['entities'][name]['addon_sha256'])
                raw_json=json5.loads(raw.decode('utf-8-sig'),allow_duplicate_keys=False)
                ent=raw_json['minecraft:entity']
                for version,(commit,zip_hash) in REFERENCE.items():
                    record=self.data['entities'][name]['comparisons'][version]
                    self.assertEqual((commit,zip_hash),(record['reference_commit'],record['reference_zip_sha256']))
                    self.assertEqual(self.index['references'][version]['file_sha256'][name],record['reference_file_sha256'])
                    for section, values in record['sections'].items():
                        current=raw_json if section=='root' else ent.get(section,{})
                        for key, pair in values.items():
                            expected={'present':True,'value':current[key]} if key in current else {'present':False}
                            self.assertEqual(expected,pair['addon'],(name,version,section,key))
                            self.assertNotEqual(pair['reference'],pair['addon'],(name,version,section,key))
                        if section in ('components','component_groups','events'):
                            previous=self.index['comparisons']['2.8.14'][version][name][section]
                            categories={
                                'only_reference':{k for k,v in values.items() if v['reference']['present'] and not v['addon']['present']},
                                'only_addon':{k for k,v in values.items() if not v['reference']['present'] and v['addon']['present']},
                                'different_both':{k for k,v in values.items() if v['reference']['present'] and v['addon']['present']},
                            }
                            for category,keys in categories.items(): self.assertEqual(set(previous[category]),keys,(name,version,section,category))

    def test_comparison_distinguishes_missing_null_and_order(self):
        ref={'a':None,'b':[1,2],'c':1,'d':{'x':1,'y':2}}
        addon={'b':[2,1],'c':1.0,'d':{'y':2,'x':1},'e':None}
        out=changed_values(ref,addon)
        self.assertEqual({'a','b','e'},set(out))
        self.assertEqual({'present':True,'value':None},out['a']['reference'])
        self.assertEqual({'present':False},out['a']['addon'])
        self.assertEqual({'present':False},out['e']['reference'])
        self.assertEqual({'present':True,'value':None},out['e']['addon'])
        obj=lambda d:{'minecraft:entity':{'description':{},'components':d}}
        self.assertEqual({'format_version':{'reference':{'present':False},'addon':{'present':True,'value':None}}},compare(obj({}),dict(obj({}),format_version=None))['root'])

    def test_reference_version_pitfalls_and_projectiles(self):
        entity=self.data['entities']
        section=lambda name,version,kind:entity[name]['comparisons'][version]['sections'][kind]
        self.assertIn('properties',section('bee','1.19.40.2','description'))
        self.assertNotIn('properties',section('bee','1.20.30.1','description'))
        self.assertIn('has_nectar',section('bee','1.19.40.2','component_groups'))
        self.assertNotIn('has_nectar',section('bee','1.20.30.1','component_groups'))
        self.assertNotIn('minecraft:collision_box',section('ender_crystal','1.19.40.2','components'))
        box=section('ender_crystal','1.20.30.1','components')['minecraft:collision_box']
        self.assertEqual({'width':2,'height':2},box['reference']['value'])
        self.assertEqual({'width':0.98,'height':0.98},box['addon']['value'])
        for ver in REFERENCE:
            projectile=section('fireball',ver,'components')['minecraft:projectile']
            self.assertEqual(6,projectile['reference']['value']['on_hit']['impact_damage']['damage'])
            self.assertNotIn('impact_damage',projectile['addon']['value']['on_hit'])
            self.assertIn('definition_event',projectile['addon']['value']['on_hit'])
            impact=section('small_fireball',ver,'components')['minecraft:projectile']
            self.assertTrue(impact['reference']['value']['on_hit']['impact_damage']['knockback'])
            self.assertFalse(impact['addon']['value']['on_hit']['impact_damage']['knockback'])
            bullet=section('shulker_bullet',ver,'components')['minecraft:projectile']
            self.assertEqual(0,bullet['reference']['value']['on_hit']['mob_effect']['amplifier'])
            self.assertEqual(1,bullet['addon']['value']['on_hit']['mob_effect']['amplifier'])
        self.assertNotIn('is_spawnable',section('wither','1.19.40.2','description'))
        self.assertEqual({'reference':{'present':True,'value':True},'addon':{'present':True,'value':False}},section('wither','1.20.30.1','description')['is_spawnable'])
        self.assertEqual(render_markdown(self.data),(ROOT/'docs/vanilla-entity-detail-ledger.md').read_text())

    def test_lightning_tnt_bee_and_entity_connections(self):
        with zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as z:
            def entity(name): return json5.loads(z.read(f'Swords_B/entities/{name}.json').decode('utf-8-sig'))['minecraft:entity']
            lightning=entity('lightning_bolt')
            self.assertEqual(['spawn_centella'],lightning['events']['minecraft:entity_spawned']['sequence'][0]['add']['component_groups'])
            timer=lightning['component_groups']['spawn_centella']['minecraft:timer']
            self.assertEqual(([0,0],False,'spawn_centella'),(timer['time'],timer['looping'],timer['time_down_event']['event']))
            random=lightning['events']['spawn_centella']['randomize']
            self.assertEqual([80,20],[v['weight'] for v in random])
            self.assertEqual(['summon entity:centella ~ ~1 ~'],random[1]['run_command']['command'])
            centella=entity('centella')
            triggers=centella['components']['minecraft:damage_sensor']['triggers']
            self.assertEqual(['centella_death_by_player','centella_death'],[v['on_damage']['event'] for v in triggers])
            for trigger in triggers:self.assertIn({'test':'has_damage','value':'fatal'},trigger['on_damage']['filters']['all_of'])
            self.assertIn({'test':'is_family','subject':'other','value':'player'},triggers[0]['on_damage']['filters']['all_of'])
            player_death=centella['events']['centella_death_by_player']['sequence']
            self.assertIn('summon lightning_bolt ~~~ default_lightning_bolt',player_death[0]['run_command']['command'])
            self.assertIn('summon lightning_bolt ~~~ default_lightning_bolt',centella['events']['centella_death']['run_command']['command'])
            self.assertEqual([98,2],[v['weight'] for v in player_death[1]['randomize']])
            self.assertNotIn('Swords_B/'+centella['components']['minecraft:loot']['table'],z.namelist())
            tnt=entity('tnt')
            self.assertNotIn('minecraft:explode',tnt['components'])
            self.assertEqual(['default_tnt'],tnt['events']['minecraft:entity_spawned']['add']['component_groups'])
            self.assertEqual((4,4,False),(tnt['component_groups']['default_tnt']['minecraft:explode']['fuse_length'],tnt['component_groups']['default_tnt']['minecraft:explode']['power'],tnt['component_groups']['default_tnt']['minecraft:explode']['causes_fire']))
            giant=tnt['component_groups']['giant_tnt']['minecraft:explode']
            self.assertEqual((8,16,True),(giant['fuse_length'],giant['power'],giant['causes_fire']))
            bee=entity('bee')
            self.assertEqual("query.had_component_group('has_nectar')",bee['description']['properties']['minecraft:has_nectar']['default'])
            self.assertEqual([2,98],[v['weight'] for v in bee['events']['countdown_to_perish_event']['sequence'][0]['randomize']])
            arrow=entity('arrow')
            self.assertEqual([1,1],arrow['component_groups']['despawn_arrow']['minecraft:timer']['time'])
            player=entity('player')
            self.assertIn('event entity @e[family=arrow,r=8] minecraft:inertia_disable',player['events']['minecraft:bone_sword']['sequence'][1]['run_command']['command'])
            self.assertIn('event entity @e[family=shot_by_the_blaze,r=7] minecraft:inertia_disable',player['events']['minecraft:blaze_sword']['sequence'][1]['run_command']['command'])
            crystal=entity('ender_crystal')
            self.assertNotIn('minecraft:on_hurt',crystal['components'])
            self.assertIn('minecraft:on_hurt',crystal['component_groups']['on_hurt_crystal'])
            self.assertEqual([98,2],[v['weight'] for v in crystal['events']['spectral_crystal_explode']['sequence'][0]['randomize']])

    def test_player_and_five_other_entities_full_differences(self):
        from build_vanilla_six_detail_diff import NAMES as SIX, ADDON_FILES, render_markdown as render_six
        data=json.loads((ROOT/'data/vanilla-six-detail-diff.json').read_text())
        self.assertEqual(set(SIX),set(data['entities']))
        self.assertEqual(render_six(data),(ROOT/'docs/vanilla-six-detail-ledger.md').read_text())
        for name in SIX:
            for ver, record in data['entities'][name]['addons'].items():
                filename,pack=ADDON_FILES[ver]
                with zipfile.ZipFile(ROOT/'sources'/filename) as z:
                    raw=z.read(f'{pack}/entities/{name}.json')
                self.assertEqual(hashlib.sha256(raw).hexdigest(),record['file_sha256'])
                parsed=json5.loads(raw.decode('utf-8-sig'),allow_duplicate_keys=False)
                for ref_ver,comparison in record['comparisons'].items():
                    self.assertEqual(REFERENCE[ref_ver],(comparison['reference_commit'],comparison['reference_zip_sha256']))
                    self.assertEqual(self.index['references'][ref_ver]['file_sha256'][name],comparison['reference_file_sha256'])
                    for section,values in comparison['sections'].items():
                        current=parsed if section=='root' else parsed['minecraft:entity'].get(section,{})
                        for key,pair in values.items():
                            expected={'present':True,'value':current[key]} if key in current else {'present':False}
                            self.assertEqual(expected,pair['addon'],(name,ver,ref_ver,section,key))
                            self.assertNotEqual(pair['reference'],pair['addon'])
                        if ver!='1.6' and section in ('components','component_groups','events'):
                            prev=self.index['comparisons'][ver][ref_ver][name][section]
                            only_ref={k for k,v in values.items() if v['reference']['present'] and not v['addon']['present']}
                            only_addon={k for k,v in values.items() if not v['reference']['present'] and v['addon']['present']}
                            changed={k for k,v in values.items() if v['reference']['present'] and v['addon']['present']}
                            self.assertEqual(set(prev['only_reference']),only_ref)
                            self.assertEqual(set(prev['only_addon']),only_addon)
                            self.assertEqual(set(prev['different_both']),changed)
        self.assertEqual({'1.6','2.8.8','2.8.14'},set(data['entities']['player']['addons']))
        for name in set(SIX)-{'player'}:
            self.assertEqual({'2.8.8','2.8.14'},set(data['entities'][name]['addons']))
            self.assertEqual(data['entities'][name]['addons']['2.8.8']['file_sha256'],data['entities'][name]['addons']['2.8.14']['file_sha256'])

    def test_five_vanilla_mob_detail_paths(self):
        import re
        for filename in ('swordsandmoreswords_2_8_8.mcaddon','swordsandmoreswords-2-8-14.mcaddon'):
            with zipfile.ZipFile(ROOT/'sources'/filename) as z:
                def entity(name): return json5.loads(z.read(f'Swords_B/entities/{name}.json').decode('utf-8-sig'))['minecraft:entity']
                blaze=entity('blaze')
                self.assertNotIn('minecraft:on_hurt',blaze['components'])
                self.assertNotIn('minecraft:on_hurt_by_player',blaze['components'])
                self.assertEqual([995,5],[x['weight'] for x in blaze['events']['blaze_sword']['randomize']])
                self.assertNotIn('Swords_B/structures/blaze_sword.mcstructure',z.namelist())
                hits=[]
                for path in z.namelist():
                    if path.startswith('Swords_B/') and path.endswith(('.json','.mcfunction','.js')):
                        for i,line in enumerate(z.read(path).decode('utf-8-sig').splitlines(),1):
                            if re.search(r'"event"\s*:\s*"blaze_sword"|\bevent\s+entity\s+\S+\s+blaze_sword(?=["\s,]|$)',line):hits.append((path,i))
                self.assertEqual([],hits)
                skeleton=entity('skeleton')
                trigger=skeleton['components']['minecraft:damage_sensor']['triggers'][0]
                self.assertEqual('bone_sword',trigger['on_damage']['event'])
                self.assertTrue(trigger['deals_damage'])
                self.assertIn({'test':'has_damage','value':'fatal'},trigger['on_damage']['filters']['all_of'])
                event=skeleton['events']['bone_sword']['sequence'][0]
                self.assertEqual([993,7],[v['weight'] for v in event['randomize']])
                self.assertIn({'test':'has_biome_tag','value':'desert'},event['filters']['all_of'])
                self.assertIn({'test':'is_brightness','operator':'<','value':0.49},event['filters']['all_of'])
                cat=entity('cat'); wolf=entity('wolf')
                self.assertNotIn('require_full_health',cat['component_groups']['minecraft:cat_adult']['minecraft:breedable'])
                self.assertNotIn('require_full_health',wolf['component_groups']['minecraft:wolf_adult']['minecraft:breedable'])
                self.assertEqual({'priority':7},wolf['component_groups']['minecraft:wolf_tame']['minecraft:behavior.breed'])
                self.assertNotIn('minecraft:rideable',wolf['component_groups']['minecraft:wolf_angry'])
                parrot=entity('parrot')
                branches=parrot['events']['minecraft:entity_spawned']['randomize']
                self.assertEqual([20]*5,[v['weight'] for v in branches])
                self.assertTrue(all('minecraft:parrot_not_riding_player' not in v['add']['component_groups'] for v in branches))

    def test_diagnostic_creeper_comparison_is_explicitly_hypothetical(self):
        from build_creeper_diagnostic_diff import parse_diagnostic, render_markdown as render_creeper
        data=json.loads((ROOT/'data/vanilla-creeper-diagnostic.json').read_text())
        self.assertEqual(render_creeper(data),(ROOT/'docs/vanilla-creeper-diagnostic-ledger.md').read_text())
        self.assertEqual('8c8f169be60ee52a224928d57575cb3b47f19bf41c03e8dd5326f8440d6c33c2',data['addon_original_sha256'])
        sections=[]
        for ver,comparison in data['comparisons'].items():
            self.assertEqual(REFERENCE[ver],(comparison['reference_commit'],comparison['reference_zip_sha256']))
            self.assertEqual('6f8a46400a440580a9f450404476c17132e448f010cc7c81c9dd9984ffab8bce',comparison['reference_file_sha256'])
            sections.append(comparison['sections'])
        self.assertEqual(sections[0],sections[1])
        with zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as newer, zipfile.ZipFile(ROOT/'sources/swordsandmoreswords_2_8_8.mcaddon') as older:
            raw=newer.read('Swords_B/entities/creeper.json')
            self.assertEqual(raw,older.read('Swords_B/entities/creeper.json'))
            with self.assertRaises(ValueError):json5.loads(raw.decode('utf-8-sig'),allow_duplicate_keys=False)
            modified,obj=parse_diagnostic(raw)
            self.assertEqual(hashlib.sha256(raw).hexdigest(),data['addon_original_sha256'])
            self.assertEqual(hashlib.sha256(modified.encode('utf-8')).hexdigest(),data['transformed_utf8_sha256'])
            for section,values in sections[0].items():
                current=obj if section=='root' else obj['minecraft:entity'].get(section,{})
                for key,pair in values.items():
                    expected={'present':True,'value':current[key]} if key in current else {'present':False}
                    self.assertEqual(expected,pair['addon'])
            changed=sections[0]['components']['minecraft:behavior.nearest_attackable_target']
            self.assertEqual((3.0,0.0),(changed['reference']['value']['must_see_forget_duration'],changed['addon']['value']['must_see_forget_duration']))
            group=sections[0]['component_groups']['minecraft:forced_charged_exploding']
            self.assertNotIn('minecraft:timer',group['reference']['value'])
            self.assertEqual([1.4,1.4],group['addon']['value']['minecraft:timer']['time'])
        with self.assertRaises(ValueError):parse_diagnostic(b'{"minecraft:entity":{"description":{"identifier":"minecraft:creeper"}}}')

    def test_detailed_mob_projectile_and_variants(self):
        with zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as z:
            def load(path): return json5.loads(z.read('Swords_B/'+path).decode('utf-8-sig'),allow_duplicate_keys=False)
            def e(name): return load('entities/'+name+'.json')['minecraft:entity']
            ender=e('enderman');spawn=ender['events']['minecraft:entity_spawned']['randomize']
            self.assertEqual([80,20],[v['weight'] for v in spawn])
            self.assertEqual({'test':'has_biome_tag','operator':'==','value':'overworld'},spawn[1]['filters'])
            group=ender['component_groups']['red_enderman']
            self.assertEqual((120,120,12,1.2,64,64),(group['minecraft:health']['value'],group['minecraft:health']['max'],group['minecraft:attack']['damage'],group['minecraft:scale']['value'],group['minecraft:follow_range']['value'],group['minecraft:follow_range']['max']))
            pool=load('loot_tables/entities/red_enderman.json')['pools'][0]
            self.assertEqual([{'condition':'killed_by_player'},{'condition':'random_chance_with_looting','chance':0.025,'looting_multiplier':0.02}],pool['conditions'])
            self.assertEqual('effect:ender_sword',pool['entries'][0]['name'])
            ghast=e('ghast');trigger=ghast['components']['minecraft:damage_sensor']['triggers'][0]
            self.assertEqual({'test':'is_family','value':'ghast'},trigger['on_damage']['filters'])
            self.assertTrue(trigger['deals_damage'])
            self.assertEqual([94,6],[v['weight'] for v in ghast['events']['spectral_ghast']['randomize']])
            self.assertIn('structure load spectral_sword ~~~',ghast['events']['spectral_ghast']['randomize'][1]['run_command']['command'])
            spider=e('spider');self.assertEqual(3,spider['components']['minecraft:attack']['damage'])
            self.assertEqual(['minecraft:default_spider'],spider['events']['minecraft:entity_spawned']['sequence'][0]['add']['component_groups'])
            self.assertEqual(['minecraft:spider_player_jockey'],spider['events']['minecraft:spider_sword']['add']['component_groups'])
            self.assertEqual({'range_min':0.4,'range_max':0.7},spider['component_groups']['minecraft:spider_player_jockey']['minecraft:horse.jump_strength']['value'])
            witch=e('witch');self.assertEqual([80,20],[v['weight'] for v in witch['events']['minecraft:entity_spawned']['randomize']])
            self.assertEqual([80,20],[v['weight'] for v in witch['events']['grass_sword']['randomize']])
            self.assertEqual('grass_sword',witch['component_groups']['grass_witch']['minecraft:on_death']['event'])
            self.assertFalse(witch['component_groups']['minecraft:raid_configuration']['minecraft:dweller']['can_migrate'])
            wither=e('wither');self.assertEqual([87,13],[v['weight'] for v in wither['events']['wither_sword']['sequence'][0]['randomize']])
            self.assertIn({'test':'has_equipment','subject':'other','domain':'hand','value':'effect:nether_star_sword'},wither['components']['minecraft:damage_sensor']['triggers'][1]['on_damage']['filters']['all_of'])
            fireball=e('fireball');self.assertNotIn('impact_damage',fireball['components']['minecraft:projectile']['on_hit'])
            self.assertEqual(1,fireball['component_groups']['minecraft:exploding']['minecraft:explode']['power'])
            self.assertEqual(0.04,fireball['component_groups']['gravity_enable']['minecraft:projectile']['gravity'])
            small=e('small_fireball');self.assertFalse(small['components']['minecraft:projectile']['on_hit']['impact_damage']['knockback'])
            self.assertEqual(0.02,small['component_groups']['gravity_enable']['minecraft:projectile']['gravity'])
            self.assertEqual((0,0.06,0,0),tuple(small['component_groups']['minecraft:inertia_disable']['minecraft:projectile'][k] for k in ('power','gravity','inertia','liquid_inertia')))
            snow=e('snowball');self.assertEqual(['fill ~ ~ ~ ~ ~ ~ snow_layer 0 replace air'],snow['events']['ice_sword']['run_command']['command'])
            bullet=e('shulker_bullet');self.assertEqual(1,bullet['components']['minecraft:projectile']['on_hit']['mob_effect']['amplifier'])
            bp=bullet['component_groups']['shulker_sword']['minecraft:projectile'];self.assertEqual((0.01,False,False),(bp['gravity'],bp['homing'],bp['destroyOnHurt']))
            for name,power,gravity in [('wither_skull',1.2,0.05),('wither_skull_dangerous',0.6,0.005)]:
                group=e(name)['component_groups']['wither_sword'];self.assertEqual({'width':0,'height':0},group['minecraft:collision_box'])
                p=group['minecraft:projectile'];self.assertEqual((power,gravity,False),(p['power'],p['gravity'],p['shoot_target']))
                effect=p['on_hit']['mob_effect'];self.assertEqual((1,0,200,800),(effect['amplifier'],effect['durationeasy'],effect['durationnormal'],effect['durationhard']))


if __name__=='__main__': unittest.main()
