import io
import collections
import json
import re
import sys
import shutil
import subprocess
import unittest
import zipfile
from pathlib import Path

import json5
import nbtlib

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from build_mechanics import event_tree
from build_acquisition_index import loot_entries, output_items, table_target, trades

class AuditTests(unittest.TestCase):
    def test_randomize_fractions_and_filters(self):
        lines = []
        event_tree({'sequence':[{'randomize':[{'weight':9999},{'weight':1,'filters':{'test':'in_water'},'shoot':{'projectile':'entity:x'}}]}]}, lines)
        s='\n'.join(lines)
        self.assertIn('1/10000 (0.01%)',s)
        self.assertIn('9999/10000 (99.99%)',s)
        self.assertIn('"filters":{"test":"in_water"}',s)
        self.assertIn('"projectile":"entity:x"',s)
        self.assertIn('пустое действие',s)

    def test_missing_weight_is_not_guessed(self):
        lines=[]
        event_tree({'randomize':[{'weight':1},{'shoot':{'projectile':'entity:x'}}]}, lines)
        self.assertIn('сумму/вероятности не вычисляем','\n'.join(lines))
        self.assertNotIn('условная доля','\n'.join(lines))

    def test_item_coverage_all_versions(self):
        versions=[('1.6','SwordsAndMoreSwords.1.6.mcaddon',26),('2.8.8','swordsandmoreswords_2_8_8.mcaddon',42),('2.8.14','swordsandmoreswords-2-8-14.mcaddon',42)]
        for ver,filename,count in versions:
            with self.subTest(ver=ver),zipfile.ZipFile(ROOT/'sources'/filename) as z:
                expected=[]
                for p in z.namelist():
                    if re.search(r'_B/items/[^/]+\.json$',p):
                        expected.append(json5.loads(z.read(p).decode('utf-8-sig'))['minecraft:item']['description']['identifier'])
                text=(ROOT/'docs'/f'mechanics-{ver}.md').read_text()
                actual=re.findall(r'^### (effect:[^\n]+)$',text,re.M)
                self.assertEqual(count,len(expected))
                self.assertCountEqual(expected,actual)

    def test_world_ledger_includes_every_file_and_exact_parsed_content(self):
        with zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as z:
            names=[n for n in z.namelist() if n.endswith('.json') and any(n.startswith('Swords_B/'+x+'/') for x in ('loot_tables','blocks','recipes','spawn_rules'))]
            text=(ROOT/'docs/world-ledger-2.8.14.md').read_text()
            chunks=re.split(r'^## `([^`]+)`\n',text,flags=re.M)
            sections=dict(zip(chunks[1::2],chunks[2::2]))
            self.assertEqual(85,len(names)); self.assertCountEqual(names,sections)
            for name in names:
                block=re.search(r'```json\n(.*?)\n```',sections[name],re.S)
                self.assertIsNotNone(block,name)
                self.assertEqual(json5.loads(z.read(name).decode('utf-8-sig')),json.loads(block.group(1)),name)

    def test_manual_trace_key_numbers_against_sources(self):
        with zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as z:
            def read(path): return json5.loads(z.read('Swords_B/'+path).decode('utf-8-sig'))
            pool=read('loot_tables/chests/abandoned_mineshaft.json')['pools'][1]
            self.assertEqual({'min':2,'max':4},pool['rolls'])
            self.assertEqual(86,sum(e['weight'] for e in pool['entries']))
            self.assertEqual(3,next(e['weight'] for e in pool['entries'] if e.get('name')=='effect:spider_sword'))
            pool=read('loot_tables/entities/blaze.json')['pools'][1]
            self.assertEqual((0.025,0.02),(pool['conditions'][1]['chance'],pool['conditions'][1]['looting_multiplier']))
            pool=read('loot_tables/entities/slime_king.json')['pools'][0]
            self.assertEqual((0.04,0.02),(pool['conditions'][1]['chance'],pool['conditions'][1]['looting_multiplier']))
            player=read('entities/player.json')['minecraft:entity']
            spawn=player['component_groups']['shoot_small_fireball']['minecraft:spawn_entity']
            self.assertEqual(4,len(spawn))
            self.assertTrue(all(e['spawn_entity']=='entity:fake_fireball' and e['single_use'] for e in spawn))
            randomize=player['events']['minecraft:blaze_sword']['sequence'][2]['randomize']
            self.assertEqual([5,5,5,5,5,5,95],[e['weight'] for e in randomize])
            objective=read('entities/objective.json')['minecraft:entity']
            self.assertIn('r=8,c=1',objective['events']['follow_entity']['run_command']['command'][0])

    def test_new_manual_trace_details(self):
        with zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as z:
            def read(path): return json5.loads(z.read('Swords_B/'+path).decode('utf-8-sig'))
            alpha=read('entities/alpha_wolf.json')['minecraft:entity']
            self.assertEqual(480,alpha['components']['minecraft:health']['value'])
            self.assertEqual([90,10],[r['weight'] for r in alpha['events']['minecraft:wolf_sword']['sequence'][0]['randomize']])
            player=read('entities/player.json')['minecraft:entity']
            self.assertEqual(15,player['component_groups']['complete_wolf_transformation']['minecraft:attack']['damage'])
            self.assertNotIn('player',player['component_groups']['complete_wolf_transformation']['minecraft:type_family']['family'])
            self.assertEqual([0.5,0.5],player['component_groups']['minecraft:cactus_sword']['minecraft:timer']['time'])
            cmds=player['events']['cactus_sword_skills']['run_command']['command']
            self.assertEqual(['damage @e[r=1.4,type=!player] 1 contact entity @s','damage @s 1 contact'],cmds)
            cmds=player['events']['minecraft:sponge_sword']['sequence'][2]['run_command']['command']
            self.assertIn('fill ~2 ~2 ~2 ~-2 ~-2 ~-2 air 0 replace sponge',cmds)
            self.assertTrue(all(any(f'sponge_sword={n}' in cmd for cmd in cmds) for n in (150,155,160)))
            for item in ('sponge_sword','wet_sponge_sword'):
                self.assertNotIn('minecraft:enchantable',read(f'items/{item}.json')['minecraft:item']['components'])
            magma=read('loot_tables/chests/underwater_ruin_big.json')['pools'][1]
            self.assertEqual(24,sum(x['weight'] for x in magma['entries']))
            self.assertEqual(1,next(x['weight'] for x in magma['entries'] if x.get('name')=='effect:magma_sword'))
            corridor=read('loot_tables/chests/stronghold_corridor.json')['pools'][0]
            self.assertEqual(521,sum(x['weight'] for x in corridor['entries']))

    def test_asset_coverage_and_screenshot_index(self):
        for version, filename in [('1.6','SwordsAndMoreSwords.1.6.mcaddon'),('2.8.8','swordsandmoreswords_2_8_8.mcaddon'),('2.8.14','swordsandmoreswords-2-8-14.mcaddon')]:
            text=(ROOT/'docs'/f'assets-{version}.md').read_text()
            with self.subTest(version=version), zipfile.ZipFile(ROOT/'sources'/filename) as z:
                names=[p for p in z.namelist() if Path(p).suffix.lower() in ('.png','.jpeg','.jpg','.tga','.ogg','.wav','.mp3','.flac')]
                for name in names: self.assertIn('`'+name+'`',text)
        self.assertEqual(21,len(re.findall(r'^## Screenshot_', (ROOT/'docs/screenshot-ocr.md').read_text(),re.M)))

    def test_manual_coverage_count(self):
        text=(ROOT/'docs/coverage-2.8.14.md').read_text()
        rows=[s for s in text.splitlines() if s.startswith('| `effect:')]
        self.assertEqual(42,len(rows))
        self.assertEqual(42,sum('начата, не завершена' in s for s in rows))
        self.assertEqual(0,sum('не начата' in s for s in rows))

    def test_traced_remaining_items_and_missing_references(self):
        with zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as z:
            def read(path): return json5.loads(z.read('Swords_B/'+path).decode('utf-8-sig'))
            item=lambda name: read('items/'+name+'.json')['minecraft:item']
            self.assertEqual(41,len(item('lightning_sword')['events']['on_use']['run_command']['command']))
            self.assertEqual(3,item('wither_sword')['events']['on_use']['damage']['amount'])
            self.assertEqual(80,item('pumpkin_sword')['events']['weapon']['sequence'][1]['randomize'][0]['weight'])
            self.assertEqual(0.3,read('entities/pumpkin_projectile.json')['minecraft:entity']['components']['minecraft:projectile']['power'])
            self.assertEqual(242,sum(e['weight'] for e in read('loot_tables/chests/desert_pyramid.json')['pools'][0]['entries']))
            self.assertEqual(457,sum(e['weight'] for e in read('loot_tables/chests/jungle_temple.json')['pools'][0]['entries']))
            self.assertEqual(219,sum(e['weight'] for e in read('loot_tables/chests/buriedtreasure.json')['pools'][1]['entries']))
            self.assertEqual(41,sum(e['weight'] for e in read('loot_tables/gameplay/fishing/treasure.json')['pools'][0]['entries']))
            player=read('entities/player.json')['minecraft:entity']
            self.assertIn('kill @e[type=item,r=24]',read('entities/ultra_instinct_projectile.json')['minecraft:entity']['events']['projectile_particle']['run_command']['command'])
            self.assertEqual(300,int(player['events']['minecraft:time_sword']['sequence'][1]['run_command']['command'][0].split()[-1]))
            self.assertEqual([0.2,0.2],read('blocks/lightblock.json')['minecraft:block']['components']['minecraft:ticking']['range'])
            self.assertNotIn('Swords_B/loot_tables/blocks/null.json',z.namelist())
            self.assertNotIn('Swords_B/structures/blaze_sword.mcstructure',z.namelist())
            self.assertEqual(148,len(z.read('Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction').decode().splitlines()))
        refs=(ROOT/'docs/literal-references-2.8.14.md').read_text()
        self.assertIn('`Swords_B/loot_tables/blocks/null.json`',refs)
        self.assertIn('`Swords_B/structures/blaze_sword.mcstructure`',refs)

    def test_all_version_entity_and_world_ledgers(self):
        versions=[('1.6','SwordsAndMoreSwords.1.6.mcaddon','Sword_B',31,26),('2.8.8','swordsandmoreswords_2_8_8.mcaddon','Swords_B',52,92),('2.8.14','swordsandmoreswords-2-8-14.mcaddon','Swords_B',52,85)]
        categories=('loot_tables','blocks','recipes','spawn_rules','features','feature_rules','trading')
        for version, filename, pack, entity_count, world_count in versions:
            with self.subTest(version=version),zipfile.ZipFile(ROOT/'sources'/filename) as z:
                entities=[n for n in z.namelist() if n.startswith(pack+'/entities/') and n.endswith('.json')]
                world=[n for n in z.namelist() if n.endswith('.json') and any(n.startswith(pack+'/'+c+'/') for c in categories)]
                etext=(ROOT/'docs'/f'entity-ledger-{version}.md').read_text();wtext=(ROOT/'docs'/f'world-ledger-{version}.md').read_text()
                self.assertEqual(entity_count,len(entities));self.assertEqual(world_count,len(world))
                for n in entities:self.assertIn('`'+n+'`',etext,n)
                sections=re.split(r'^## `([^`]+)`\n',wtext,flags=re.M);sections=dict(zip(sections[1::2],sections[2::2]))
                self.assertCountEqual(world,sections)
                for n in world:
                    block=re.search(r'```json\n(.*?)\n```',sections[n],re.S)
                    self.assertIsNotNone(block,n)
                    self.assertEqual(json5.loads(z.read(n).decode('utf-8-sig')),json.loads(block.group(1)),n)

    def test_version_16_coal_not_equivalent(self):
        with zipfile.ZipFile(ROOT/'sources/SwordsAndMoreSwords.1.6.mcaddon') as old, zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as new:
            def components(z,path): return json5.loads(z.read(path).decode('utf-8-sig'))['minecraft:item']['components']
            a=components(old,'Sword_B/items/coal_sword.json'); b=components(new,'Swords_B/items/coal_sword.json')
            self.assertEqual((6,4),(a['minecraft:damage'],b['minecraft:damage']))
            self.assertEqual((True,False),(a['minecraft:allow_off_hand'],b['minecraft:allow_off_hand']))
            self.assertNotIn('minecraft:fuel',a);self.assertEqual(360.0,b['minecraft:fuel']['duration'])

    def test_structure_snbt_rebuilds_exact_original_binary(self):
        versions=[('2.8.8','swordsandmoreswords_2_8_8.mcaddon',18),('2.8.14','swordsandmoreswords-2-8-14.mcaddon',17)]
        for version, archive, count in versions:
            with self.subTest(version=version), zipfile.ZipFile(ROOT/'sources'/archive) as z:
                names={p.split('/structures/',1)[1][:-len('.mcstructure')]:p for p in z.namelist() if '/structures/' in p and p.endswith('.mcstructure')}
                text=(ROOT/'docs'/f'structures-{version}.md').read_text()
                chunks=re.split(r'^## `([^`]+)`\n',text,flags=re.M)
                sections=dict(zip(chunks[1::2],chunks[2::2]))
                self.assertEqual(count,len(names)); self.assertCountEqual(names,sections)
                self.assertIn('`blaze_sword`',chunks[0])
                for name,path in names.items():
                    block=re.search(r'```snbt\n(.*?)\n```',sections[name],re.S)
                    self.assertIsNotNone(block,path)
                    raw=z.read(path)
                    original=nbtlib.File.parse(io.BytesIO(raw),byteorder='little')
                    result=nbtlib.File(nbtlib.parse_nbt(block.group(1)),root_name=original.root_name)
                    out=io.BytesIO(); result.write(out,byteorder='little')
                    self.assertEqual(raw,out.getvalue(),path)

    def test_entity_ledger_includes_all_files_and_invalid_file(self):
        with zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as z:
            names=[n for n in z.namelist() if n.startswith('Swords_B/entities/') and n.endswith('.json')]
        text=(ROOT/'docs/entity-ledger-2.8.14.md').read_text()
        self.assertEqual(52,len(names))
        for name in names: self.assertIn('`'+name+'`',text,name)
        self.assertIn('Не разобран JSON5',text)
        self.assertIn('Повторяющиеся ключи',text)

    def test_controller_ledgers_exact_and_chain_coverage(self):
        versions=[('1.6','SwordsAndMoreSwords.1.6.mcaddon','Sword_B'),('2.8.8','swordsandmoreswords_2_8_8.mcaddon','Swords_B'),('2.8.14','swordsandmoreswords-2-8-14.mcaddon','Swords_B')]
        for version,filename,pack in versions:
            with self.subTest(version=version),zipfile.ZipFile(ROOT/'sources'/filename) as z:
                names=[n for n in z.namelist() if n.startswith(pack+'/animation_controllers/') and n.endswith('.json')]
                text=(ROOT/'docs'/f'animation-ledger-{version}.md').read_text()
                sections=re.split(r'^### `([^`]+)`\n',text,flags=re.M);sections=dict(zip(sections[1::2],sections[2::2]))
                self.assertCountEqual(names,sections)
                for name in names:
                    block=re.search(r'```json\n(.*?)\n```',sections[name],re.S)
                    self.assertIsNotNone(block,name)
                    self.assertEqual(z.read(name).decode('utf-8-sig').rstrip().replace('\r\n','\n'),block.group(1),name)
                if version=='1.6':
                    items=[json5.loads(z.read(n).decode('utf-8-sig'))['minecraft:item']['description']['identifier'] for n in z.namelist() if n.startswith(pack+'/items/') and n.endswith('.json')]
                    chain=(ROOT/'docs/chain-index-1.6.md').read_text()
                    self.assertCountEqual(items,re.findall(r'^## `(effect:[^`]+)`$',chain,re.M))

    def test_resource_client_descriptions_and_duplicate_witch(self):
        versions=[('1.6','SwordsAndMoreSwords.1.6.mcaddon','Sword_R',0),('2.8.8','swordsandmoreswords_2_8_8.mcaddon','Swords_R',17),('2.8.14','swordsandmoreswords-2-8-14.mcaddon','Swords_R',17)]
        for version,filename,pack,count in versions:
            with self.subTest(version=version),zipfile.ZipFile(ROOT/'sources'/filename) as z:
                clients=[]
                for name in z.namelist():
                    if not (name.startswith(pack+'/') and name.endswith(('.json','.material'))): continue
                    obj=json5.loads(z.read(name).decode('utf-8-sig'))
                    if isinstance(obj,dict) and 'minecraft:client_entity' in obj:
                        clients.append((name,obj['minecraft:client_entity']['description']))
                text=(ROOT/'docs'/f'resource-graph-{version}.md').read_text()
                self.assertEqual(count,len(clients))
                for name,desc in clients:
                    self.assertIn('### `'+desc['identifier']+'` — `'+name+'`',text)
                    self.assertIn(json.dumps(desc,ensure_ascii=False,separators=(',',':')),text)
                if version!='1.6':
                    self.assertEqual(2,sum(desc['identifier']=='minecraft:witch' for _,desc in clients))
                    self.assertIn('`'+pack+'/entity/witch.entity.json`, `'+pack+'/entity/witch.v1.0.entity.json`',text)

    def test_version_16_selected_mechanics(self):
        with zipfile.ZipFile(ROOT/'sources/SwordsAndMoreSwords.1.6.mcaddon') as z:
            def read(n):return json5.loads(z.read('Sword_B/'+n).decode('utf-8-sig'))
            for name,damage,durability in [('cactus',6,125),('emerald',7,2300),('sponge',6,128),('creeper',8,1500),('tnt',7,1)]:
                c=read('items/'+name+'_sword.json')['minecraft:item']['components']
                self.assertEqual((damage,durability,True),(c['minecraft:damage'],c['minecraft:durability']['max_durability'],c['minecraft:allow_off_hand']))
            time=read('items/Sword of Time.json')['minecraft:item']
            self.assertEqual('effect:sword_of_time',time['description']['identifier'])
            self.assertEqual(7,time['components']['minecraft:damage'])
            explosion=read('entities/explode.json')['minecraft:entity']['components']['minecraft:explode']
            self.assertEqual((0,4,False,True),(explosion['fuseLength'],explosion['power'],explosion['causesFire'],explosion['destroy_affected_by_griefing']))

    def test_acquisition_indexes_cover_items_recipes_loot_and_structures(self):
        from build_structures import item_paths
        versions=[('1.6','SwordsAndMoreSwords.1.6.mcaddon','Sword_B',26,26),('2.8.8','swordsandmoreswords_2_8_8.mcaddon','Swords_B',42,14),('2.8.14','swordsandmoreswords-2-8-14.mcaddon','Swords_B',42,14)]
        for version, filename, pack, item_count, recipe_count in versions:
            with self.subTest(version=version),zipfile.ZipFile(ROOT/'sources'/filename) as z:
                text=(ROOT/'docs'/f'acquisition-index-{version}.md').read_text()
                items={}
                for n in z.namelist():
                    if n.startswith(pack+'/items/') and n.endswith('.json'):
                        item=json5.loads(z.read(n).decode('utf-8-sig'))['minecraft:item']['description']['identifier']
                        items[item]=n
                sections=re.split(r'^### `(effect:[^`]+)`\n',text,flags=re.M)
                item_sections=dict(zip(sections[1::2],sections[2::2]))
                self.assertEqual(item_count,len(items));self.assertCountEqual(items,item_sections)
                count=0
                for n in z.namelist():
                    if n.startswith(pack+'/recipes/') and n.endswith('.json'):
                        obj=json5.loads(z.read(n).decode('utf-8-sig'))
                        for kind, recipe in obj.items():
                            if kind.startswith('minecraft:recipe_') and isinstance(recipe,dict):
                                count+=1
                                self.assertIn('### `'+n+'` — `'+kind+'`',text)
                                self.assertIn(json.dumps(recipe,ensure_ascii=False,separators=(',',':')),text)
                                for ident in output_items(recipe.get('result',recipe.get('output'))):
                                    if ident in items:self.assertIn('`'+n+'`',item_sections[ident])
                    if n.startswith(pack+'/loot_tables/') and n.endswith('.json'):
                        obj=json5.loads(z.read(n).decode('utf-8-sig'))
                        for path,entry in loot_entries(obj):
                            if entry['type']=='item' and entry['name'] in items:
                                self.assertIn('`'+n+'` '+path+': `'+json.dumps(entry,ensure_ascii=False,separators=(',',':'))+'`',item_sections[entry['name']])
                            elif entry['type']=='loot_table':
                                self.assertIn('`'+n+'` '+path+' → `'+table_target(pack,entry['name'])+'`',text)
                    if n.startswith(pack+'/trading/') and n.endswith('.json'):
                        obj=json5.loads(z.read(n).decode('utf-8-sig'))
                        for path,trade in trades(obj):
                            for ident in output_items(trade['gives']):
                                if ident in items:self.assertIn('`'+n+'` '+path+': `'+json.dumps(trade,ensure_ascii=False,separators=(',',':'))+'`',item_sections[ident])
                    if n.startswith(pack+'/structures/') and n.endswith('.mcstructure'):
                        nbt=nbtlib.File.parse(io.BytesIO(z.read(n)),byteorder='little')
                        for path,ident in item_paths(nbt['structure']):
                            if ident in items:self.assertIn('`'+n+'` '+path,item_sections[ident])
                self.assertEqual(recipe_count,count)

    def test_recipe_anomalies_and_furnace_reverse_output(self):
        with zipfile.ZipFile(ROOT/'sources/SwordsAndMoreSwords.1.6.mcaddon') as old,zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as new:
            def read(z,p):return json5.loads(z.read(p).decode('utf-8-sig'))
            item=read(old,'Sword_B/items/Sword of Time.json')['minecraft:item']['description']['identifier']
            recipe=read(old,'Sword_B/recipes/Sword_of_Time.json')['minecraft:recipe_shaped']
            self.assertEqual(('effect:sword_of_time','effect:Sword_of_Time'),(item,recipe['result']['item']))
            self.assertEqual({'#'},set(''.join(recipe['pattern']))-set(recipe['key'])-{' '})
            for name in ('fire_sword','spectral_sword','spider_sword','wither_sword'):
                recipe=read(old,'Sword_B/recipes/'+name+'.json')['minecraft:recipe_shaped']
                self.assertEqual({'#'},set(''.join(recipe['pattern']))-set(recipe['key'])-{' '})
            recipe=read(old,'Sword_B/recipes/glowstone_sword.json')['minecraft:recipe_shaped']
            self.assertEqual({'0'},set(''.join(recipe['pattern']))-set(recipe['key'])-{' '})
            furnace=read(new,'Swords_B/recipes/wet_sponge_sword.json')['minecraft:recipe_furnace']
            self.assertEqual(('effect:wet_sponge_sword','effect:sponge_sword'),(furnace['input'],furnace['output']))
        text=(ROOT/'docs/acquisition-index-2.8.14.md').read_text()
        section=text.split('### `effect:sponge_sword`',1)[1].split('### ',1)[0]
        self.assertIn('`Swords_B/recipes/wet_sponge_sword.json`',section)
        jungle=text.split('### `effect:jungle_sword`',1)[1].split('### ',1)[0]
        self.assertIn('`Swords_B/loot_tables/gameplay/fishing.json`',jungle)
        self.assertIn('`Swords_B/loot_tables/gameplay/jungle_fishing.json`',jungle)

    def test_client_visual_sources_identical_and_conditions(self):
        names=['entity/player.entity.json','render_controllers/ultra_instinct_aura.render_controllers.json','render_controllers/wolf_vision.render_controllers.json','render_controllers/wolf_transformation.render_controllers.json','render_controllers/player_ghost.render_controllers.json','render_controllers/mermaid_player.render_controllers.json','render_controllers/blaze_rods.render_controllers.json','render_controllers/blaze_aura.render_controllers.json','sounds/sound_definitions.json','sounds.json','animations/mermaid_player.animation.json']
        with zipfile.ZipFile(ROOT/'sources/swordsandmoreswords_2_8_8.mcaddon') as a,zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as b:
            for n in names:self.assertEqual(a.read('Swords_R/'+n),b.read('Swords_R/'+n),n)
            d=json5.loads(b.read('Swords_R/entity/player.entity.json').decode('utf-8-sig'))['minecraft:client_entity']['description']
            pre=' '.join(d['scripts']['pre_animation'])
            self.assertIn('query.moon_phase == 0',pre)
            self.assertIn('query.time_of_day <= 0.20 || query.time_of_day >= 0.80',pre)
            sounds=json5.loads(b.read('Swords_R/sounds/sound_definitions.json').decode('utf-8-sig'))['sound_definitions']
            self.assertEqual([32,100,60],[sounds[k]['min_distance'] for k in ('wolf_sword.howl','wolf_sword.distant_howl','ghost_sword.wailing')])

    def test_old_ore_generation_trade_and_ice_values(self):
        with zipfile.ZipFile(ROOT/'sources/swordsandmoreswords_2_8_8.mcaddon') as old,zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as new:
            def read(path):return json5.loads(old.read('Swords_B/'+path).decode('utf-8-sig'))
            for ore,yrange in [('silver',[10,35]),('quartz_diamond',[0,16])]:
                rule=read('feature_rules/'+ore+'_ore_feature.json')['minecraft:feature_rules']
                self.assertEqual((5,[0,16],yrange,[0,16],160,200),(rule['distribution']['iterations'],rule['distribution']['x']['extent'],rule['distribution']['y']['extent'],rule['distribution']['z']['extent'],rule['distribution']['scatter_chance']['numerator'],rule['distribution']['scatter_chance']['denominator']))
                path='Swords_B/structures/'+ore+'_ore.mcstructure'
                nbt=nbtlib.File.parse(io.BytesIO(old.read(path)),byteorder='little')
                self.assertEqual([1,1,1],list(map(int,nbt['size'])))
                self.assertEqual('effect99:'+ore+'_ore',str(nbt['structure']['palette']['default']['block_palette'][0]['name']))
                self.assertNotIn('Swords_B/feature_rules/'+ore+'_ore_feature.json',new.namelist())
            self.assertNotIn('Swords_B/structures/quartz_diamond_ore.mcstructure',new.namelist())
            self.assertIn('Swords_B/structures/silver_ore.mcstructure',new.namelist())
            ice=read('blocks/fake_ice.json')['minecraft:block']
            self.assertEqual([1,2,3,4],ice['description']['properties']['fake_ice:model'])
            self.assertEqual([[2,2]]*4,[p['components']['minecraft:ticking']['range'] for p in ice['permutations']])
            trade=read('trading/economy_trades/weapon_smith_trades.json')['tiers'][4]['groups'][1]['trades'][0]
            self.assertEqual((32,'effect:emerald_sword',2),(trade['wants'][0]['quantity'],trade['gives'][0]['item'],trade['max_uses']))
            index=(ROOT/'docs/acquisition-index-2.8.8.md').read_text()
            emerald=index.split('### `effect:emerald_sword`',1)[1].split('### ',1)[0]
            self.assertIn('`Swords_B/trading/economy_trades/weapon_smith_trades.json`',emerald)
            self.assertIn('`Swords_B/trading/weapon_smith_trades.json`',emerald)

    def test_jungle_legacy_controller_vs_new_function(self):
        with zipfile.ZipFile(ROOT/'sources/SwordsAndMoreSwords.1.6.mcaddon') as old,zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as new:
            controller=json5.loads(old.read('Sword_B/animation_controllers/jungle_sword.json').decode('utf-8-sig'))['animation_controllers']['controller.animation.jungle']['states']
            before=[s.lstrip('/') for s in controller['jungle']['on_entry']]
            after=[s.strip().lstrip('/') for s in new.read('Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction').decode('utf-8-sig').splitlines() if s.strip() and not s.strip().startswith('#')]
            a,b=collections.Counter(before),collections.Counter(after)
            self.assertEqual((145,148,144),(len(before),len(after),sum((a&b).values())))
            self.assertEqual(collections.Counter({'scoreboard players set @a swords 2':1}),a-b)
            extra=list((b-a).elements());self.assertEqual(4,len(extra))
            self.assertTrue(all(' leaves 11 fill ' in s for s in extra))
            self.assertEqual(['/commands'],controller['default']['on_entry'])

    def test_missing_local_event_and_group_references_in_parseable_entities(self):
        # Conservative literal scan only: targets can be external/vanilla and commands are not interpreted.
        def walk(node, path=()):
            if isinstance(node,dict):
                yield path,node
                for key,value in node.items():yield from walk(value,path+(key,))
            elif isinstance(node,list):
                for i,value in enumerate(node):yield from walk(value,path+(i,))
        for version,filename,pack,expected in [
            ('1.6','SwordsAndMoreSwords.1.6.mcaddon','Sword_B',set()),
            ('2.8.8','swordsandmoreswords_2_8_8.mcaddon','Swords_B',{
                ('bee.json','group remove','collect_nectar'),('lightning_projectile.json','event','particle'),
                ('nether_star_projectile.json','group add','objective'),('ultra_instinct_projectile.json','event','minecraft:end_scale'),
                ('wither_effect.json','event','particle'),('wolf.json','event','minecraft:on_leash'),('wolf.json','event','minecraft:on_unleash')}),
            ('2.8.14','swordsandmoreswords-2-8-14.mcaddon','Swords_B',{
                ('bee.json','group remove','collect_nectar'),('lightning_projectile.json','event','particle'),
                ('nether_star_projectile.json','group add','objective'),('ultra_instinct_projectile.json','event','minecraft:end_scale'),
                ('wither_effect.json','event','particle'),('wolf.json','event','minecraft:on_leash'),('wolf.json','event','minecraft:on_unleash')})]:
            actual=set(); invalid=[]
            with self.subTest(version=version),zipfile.ZipFile(ROOT/'sources'/filename) as z:
                for name in z.namelist():
                    if not (name.startswith(pack+'/entities/') and name.endswith('.json')):continue
                    try:entity=json5.loads(z.read(name).decode('utf-8-sig'))['minecraft:entity']
                    except ValueError:invalid.append(Path(name).name);continue
                    events=entity.get('events',{}); groups=entity.get('component_groups',{})
                    for path,obj in walk(entity):
                        if 'events' in path:continue
                        event=obj.get('event');target=obj.get('target')
                        if isinstance(event,str) and target in (None,'self') and event not in events:
                            actual.add((Path(name).name,'event',event))
                    for _,obj in walk(events):
                        for action in ('add','remove'):
                            value=obj.get(action)
                            if isinstance(value,dict):
                                for group in value.get('component_groups',[]):
                                    if group not in groups:actual.add((Path(name).name,'group '+action,group))
                self.assertEqual(expected,actual)
                self.assertCountEqual(['blaze2.json','bone2.json','shulker2.json'] if version=='1.6' else ['creeper.json'],invalid)

    def test_give_function_coverage_and_target_difference(self):
        versions=[('1.6','SwordsAndMoreSwords.1.6.mcaddon','Sword_B'),('2.8.8','swordsandmoreswords_2_8_8.mcaddon','Swords_B'),('2.8.14','swordsandmoreswords-2-8-14.mcaddon','Swords_B')]
        old_function=None
        for version,filename,pack in versions:
            with self.subTest(version=version),zipfile.ZipFile(ROOT/'sources'/filename) as z:
                items={json5.loads(z.read(n).decode('utf-8-sig'))['minecraft:item']['description']['identifier'] for n in z.namelist() if n.startswith(pack+'/items/') and n.endswith('.json')}
                content=z.read(pack+'/functions/give.mcfunction')
                cmds=[line.split() for line in content.decode('utf-8-sig').splitlines() if line.strip()]
                self.assertTrue(all(c[0]=='give' and len(c)==3 for c in cmds))
                given=[c[2] for c in cmds]
                if version=='1.6':
                    self.assertEqual(26,len(cmds));self.assertEqual(items,set(given));self.assertTrue(all(c[1]=='@p' for c in cmds))
                else:
                    self.assertEqual(35,len(cmds));self.assertEqual(35,len(set(given)))
                    self.assertEqual({'effect:bedrock_stick','effect:bee_sword','effect:cursed_pumpkin_sword','effect:quartz_diamond','effect:quartz_diamond_stick','effect:silver_ingot','effect:wet_sponge_sword'},items-set(given))
                    self.assertEqual([['give','@s','effect:lightning_sword']],[c for c in cmds if c[1]!='@p'])
                    if old_function is None:old_function=content
                    else:self.assertEqual(old_function,content)

    def test_coverage_item_links_reach_the_correct_manual_sections(self):
        coverage=(ROOT/'docs/coverage-2.8.14.md').read_text()
        manual=(ROOT/'docs/manual-traces-2.8.14.md').read_text()
        headings=re.findall(r'^## (.*)$',manual,re.M)
        slugs={re.sub(r'[^\w\- ]','',h.lower()).replace(' ','-'):h for h in headings}
        rows=re.findall(r'^\| `(effect:[^`]+)` \|[^\n]*\]\(manual-traces-2\.8\.14\.md#([^)]*)\)',coverage,re.M)
        self.assertEqual(42,len(rows))
        for ident,slug in rows:
            self.assertIn(slug,slugs,ident)
            if ident!='effect:blaze_sword':self.assertIn('`'+ident+'`',slugs[slug])
            else:self.assertTrue(slugs[slug].startswith('Blaze Sword'))

    def test_constant_player_events_and_tag_names(self):
        path='Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/tag_swords.mcfunction'
        with zipfile.ZipFile(ROOT/'sources/swordsandmoreswords_2_8_8.mcaddon') as old,zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as z:
            self.assertEqual(old.read(path),z.read(path))
            e=json5.loads(z.read('Swords_B/entities/player.json').decode('utf-8-sig'))['minecraft:entity']
            commands=e['events']['minecraft:constant_events']['sequence'][0]['run_command']['command']
            self.assertEqual(['function commands/swords_and_more_swords/swords_and_more_swords/tag_swords','gamerule sendcommandfeedback false','gamerule commandblockoutput false','scoreboard objectives add Effect99 dummy','scoreboard players add @s Effect99 1','title @s[scores={Effect99=12000}] actionbar §l§fCreated by §7Effect99','scoreboard players set @s[scores={Effect99=36001}] Effect99 1'],commands)
            lang=z.read('Swords_R/texts/en_US.lang').decode('utf-8-sig').splitlines()
            names=[line.split('=',1)[1] for line in lang if '=' in line and line.startswith(('item.effect:','tile.effect99:'))]
            lines=z.read(path).decode('utf-8-sig').splitlines();self.assertEqual(13,len(lines))
            for line in lines:
                match=re.search(r'name="([^"]+)"',line)
                self.assertIsNotNone(match,line);self.assertIn(match.group(1),names)

    def test_invalid_entities_diagnostic_only_remove_last_brace(self):
        entries=[('SwordsAndMoreSwords.1.6.mcaddon','Sword_B/entities/blaze2.json','entity:blaze2',78),('SwordsAndMoreSwords.1.6.mcaddon','Sword_B/entities/bone2.json','entity:bone2',75),('SwordsAndMoreSwords.1.6.mcaddon','Sword_B/entities/shulker2.json','entity:shulker2',75),('swordsandmoreswords_2_8_8.mcaddon','Swords_B/entities/creeper.json','minecraft:creeper',430),('swordsandmoreswords-2-8-14.mcaddon','Swords_B/entities/creeper.json','minecraft:creeper',430)]
        for archive,path,ident,error_line in entries:
            with self.subTest(archive=archive,path=path),zipfile.ZipFile(ROOT/'sources'/archive) as z:
                raw=z.read(path).decode('utf-8-sig')
                with self.assertRaises(ValueError) as error:json5.loads(raw)
                self.assertIn(':'+str(error_line)+' ',str(error.exception))
                self.assertEqual('}',raw.rstrip()[-1])
                index=raw.rfind('}');diagnostic=raw[:index]+raw[index+1:]
                entity=json5.loads(diagnostic)['minecraft:entity']
                self.assertEqual(ident,entity['description']['identifier'])
                if ident=='entity:blaze2':self.assertEqual('minecraft:small_fireball',entity['components']['minecraft:shooter']['def'])
                if ident=='entity:bone2':self.assertEqual('minecraft:arrow',entity['components']['minecraft:shooter']['def'])
                if ident=='entity:shulker2':self.assertEqual('minecraft:shulker_bullet',entity['components']['minecraft:shooter']['def'])
                if ident=='minecraft:creeper':self.assertEqual(1,entity['component_groups']['minecraft:minicreeper_exploding']['minecraft:explode']['power'])

    def test_quick_reference_is_accurate_and_all_links_resolve(self):
        from build_quick_reference import read_items, item_values, literal, slug, VERSIONS
        text=(ROOT/'docs/quick-reference.md').read_text()
        sections=re.split(r'^## (1\.6|2\.8\.8|2\.8\.14)\n',text,flags=re.M)
        sections=dict(zip(sections[1::2],sections[2::2]))
        self.assertEqual({'1.6','2.8.8','2.8.14'},set(sections))
        for version,filename,pack in VERSIONS:
            items=read_items(filename,pack)
            rows=re.findall(r'^\| `(effect:[^`]+)` \| (.*)$',sections[version],re.M)
            self.assertEqual(len(items),len(rows))
            self.assertCountEqual(items,[ident for ident,_ in rows])
            for ident,row in rows:
                fields=row.split(' | ')
                self.assertEqual([literal(x) for x in item_values(items[ident][1])],fields[:5],ident)
        for target,fragment in re.findall(r'\]\(([^()#]+\.md)(?:#([^()]+))?\)',text):
            path=ROOT/'docs'/target
            self.assertTrue(path.is_file(),target)
            if fragment:
                headings=re.findall(r'^#{1,6} (.*)$',path.read_text(),re.M)
                self.assertIn(fragment,{slug(h) for h in headings},target+'#'+fragment)

    def test_ghost_acquisition_conditions_and_structure(self):
        with zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as z:
            def read(p):return json5.loads(z.read('Swords_B/'+p).decode('utf-8-sig'))
            ghost=read('entities/ghost.json')['minecraft:entity']
            self.assertEqual((666,666),(ghost['components']['minecraft:health']['value'],ghost['components']['minecraft:health']['max']))
            self.assertEqual([987,10,3],[branch['weight'] for branch in ghost['events']['disturbed_ghost']['randomize']])
            self.assertIn('structure load ghost_sword ~~~',ghost['events']['disturbed_ghost']['randomize'][2]['run_command']['command'])
            spawn=read('spawn_rules/ghost.json')['minecraft:spawn_rules']['conditions']
            self.assertEqual([100,50],[x['minecraft:weight']['default'] for x in spawn])
            self.assertEqual(['minecraft:stone','minecraft:grass'],[x['minecraft:spawns_on_block_filter'] for x in spawn])
            self.assertEqual('ghost_wailing',spawn[0]['minecraft:spawn_event']['event'])
            self.assertNotIn('minecraft:spawn_event',spawn[1])
            nbt=nbtlib.File.parse(io.BytesIO(z.read('Swords_B/structures/ghost_sword.mcstructure')),byteorder='little')
            obj=nbt['structure']['entities'][0]['Item']
            self.assertEqual(('effect:ghost_sword',1,0),(str(obj['Name']),int(obj['Count']),int(obj['Damage'])))

    def test_dropped_sword_tags_and_saved_nbt(self):
        with zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as z:
            def item_structure(name):return nbtlib.File.parse(io.BytesIO(z.read('Swords_B/structures/'+name+'.mcstructure')),byteorder='little')['structure']['entities'][0]
            obs=item_structure('obsidian_sword')['Item']
            self.assertEqual(('effect:obsidian_sword',0,1000),(str(obs['Name']),int(obs['Damage']),int(obs['tag']['Damage'])))
            fire=item_structure('fire_sword')
            self.assertCountEqual(['fire_sword','fire_sword_respawn'],[str(t) for t in fire['Tags']])
            self.assertEqual(0,int(fire['Item']['tag']['Damage']))
            self.assertIn('lightning_sword',[str(t) for t in item_structure('lightning_sword')['Tags']])
            self.assertIn('wither_sword',[str(t) for t in item_structure('wither_sword')['Tags']])
            entity=json5.loads(z.read('Swords_B/entities/item.json').decode('utf-8-sig'))['minecraft:entity']
            events=entity['events']
            self.assertEqual(['particle minecraft:example_linearcurve ~ ~ ~','summon lightning_bolt ~~~ default_lightning_bolt'],events['despawn_event_3']['run_command']['command'])
            self.assertEqual(['structure load fire_sword ~ ~1 ~','kill @s'],events['respawn_event_2']['run_command']['command'])
            for name in ('despawn_event_1','despawn_event_2'):
                self.assertIn('kill @s',events[name]['run_command']['command'])
            ctrl=json5.loads(z.read('Swords_B/animation_controllers/item_events.json').decode('utf-8-sig'))['animation_controllers']['controller.animation.item_events']['states']
            self.assertEqual([{'on_fire_swords':'q.is_on_fire'}],ctrl['default']['transitions'])
            self.assertEqual([{'default':'1.0'}],ctrl['on_fire_swords']['transitions'])

    def test_saved_item_structure_metadata_summary(self):
        expected={
            'bedrock_sword':(279,None,[]),'bone_sword':(321,0,[]),'creeper_sword':(159,None,[]),
            'fire_sword':(1612,0,['fire_sword','fire_sword_respawn']),'ghost_sword':(403,None,[]),
            'glass_sword':(277,None,[]),'grass_sword':(196,None,[]),'lightning_sword':(133,None,['lightning_sword']),
            'obsidian_sword':(763,1000,[]),'spectral_sword':(360,0,[]),'time_sword':(373,None,[]),
            'ultra_instinct_sword':(247,None,[]),'wet_sponge_sword':(340,None,[]),'wither_sword':(401,None,['wither_sword']),
            'wolf_sword':(295,None,[])}
        summary=(ROOT/'docs/manual-acquisition-issues.md').read_text()
        with zipfile.ZipFile(ROOT/'sources/swordsandmoreswords_2_8_8.mcaddon') as old,zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as new:
            for name,(age,inner,tags) in expected.items():
                path='Swords_B/structures/'+name+'.mcstructure'
                self.assertEqual(old.read(path),new.read(path))
                entities=nbtlib.File.parse(io.BytesIO(new.read(path)),byteorder='little')['structure']['entities']
                self.assertEqual(1,len(entities));e=entities[0];item=e['Item']
                self.assertEqual(('effect:'+name,1,0),(str(item['Name']),int(item['Count']),int(item['Damage'])))
                self.assertEqual(age,int(e['Age']))
                tag=item.get('tag',{});self.assertEqual(inner,int(tag['Damage']) if 'Damage' in tag else None)
                self.assertCountEqual(tags,[str(x) for x in e.get('Tags',[])])
                self.assertIn('| `'+name+'` | '+str(age)+' |',summary)

    def test_randomize_index_covers_valid_behavior_json(self):
        from build_randomize_index import extract, compact
        versions=[('1.6','SwordsAndMoreSwords.1.6.mcaddon','Sword_B',0),('2.8.8','swordsandmoreswords_2_8_8.mcaddon','Swords_B',60),('2.8.14','swordsandmoreswords-2-8-14.mcaddon','Swords_B',60)]
        all_found={};text=(ROOT/'docs/randomize-index.md').read_text()
        for version,filename,pack,count in versions:
            found,errors,duplicates=extract(filename,pack)
            self.assertEqual(count,len(found));all_found[version]=found
            self.assertCountEqual(['blaze2.json','bone2.json','shulker2.json'] if version=='1.6' else ['creeper.json'],[Path(p).name for p,_ in errors])
            if version!='1.6':
                self.assertCountEqual(['living_flame.json','mountable_slime.json','slime_king.json'],[Path(p).name for p,_ in duplicates])
                for (source,path),branches in found.items():
                    self.assertIn(f'| `{source}` | `{path}` | `{compact([x.get("weight") for x in branches])}`',text)
        self.assertEqual(all_found['2.8.8'],all_found['2.8.14'])
        self.assertEqual(180,sum(len(v) for v in all_found['2.8.14'].values()))
        self.assertEqual(3,sum(any(isinstance(b,dict) and 'filters' in b for b in v) for v in all_found['2.8.14'].values()))
        # The malformed creeper file is explicitly excluded, not silently counted as empty.
        self.assertIn('`Swords_B/entities/creeper.json`',text)

    def test_randomize_conditions_selected_source_values(self):
        from build_randomize_index import extract
        found,_,_=extract('swordsandmoreswords-2-8-14.mcaddon','Swords_B')
        def get(entity,path): return found[(f'Swords_B/entities/{entity}.json','$.minecraft:entity.events.'+path)]
        bee=get('bee','countdown_to_perish_event.sequence[0].randomize')
        self.assertEqual([2,98],[x['weight'] for x in bee]);self.assertEqual('bee_sword',bee[0]['filters']['value'])
        spider=get('spider','minecraft:entity_spawned.sequence[1].randomize')
        self.assertEqual([1,99],[x['weight'] for x in spider]);self.assertEqual([80,80,20],[x['weight'] for x in spider[0]['randomize']])
        self.assertEqual(['minecraft:spider_jockey','minecraft:spider_neutral'],spider[0]['randomize'][2]['add']['component_groups'])
        enderman=get('enderman','minecraft:entity_spawned.randomize')
        self.assertEqual('overworld',enderman[1]['filters']['value'])
        blaze=get('player','minecraft:blaze_sword.sequence[2].randomize')
        self.assertEqual([5,5,5,5,5,5,95],[x['weight'] for x in blaze]);self.assertEqual(125,sum(x['weight'] for x in blaze))

    def test_loot_context_covers_custom_and_parent_pools(self):
        from build_loot_context import read_tables, indexes, compact
        text=(ROOT/'docs/loot-context.md').read_text()
        all_tables=[]
        for version,filename,pack,expected in [('1.6','SwordsAndMoreSwords.1.6.mcaddon','Sword_B',0),('2.8.8','swordsandmoreswords_2_8_8.mcaddon','Swords_B',60),('2.8.14','swordsandmoreswords-2-8-14.mcaddon','Swords_B',60)]:
            tables,errors,duplicates=read_tables(filename,pack)
            self.assertEqual(expected,len(tables));self.assertEqual([],errors);self.assertEqual([],duplicates)
            direct,parent=indexes(tables,pack)
            expected_direct={(name,i,j) for name,obj in tables.items() for i,pool in enumerate(obj.get('pools',[])) for j,entry in enumerate(pool.get('entries',[])) if entry.get('type')=='item' and entry.get('name','').startswith(('effect:','effect99:'))}
            self.assertEqual(expected_direct,direct)
            if version!='1.6':
                self.assertEqual(29,len(direct));self.assertEqual(2,len(parent))
                for name,i in {(name,i) for name,i,_ in direct|parent}:
                    self.assertIn(f'### `{name}` — `$.pools[{i}]`',text)
                    pool=tables[name]['pools'][i]
                    self.assertIn(f'- Поля пула, кроме entries: `{compact({k:v for k,v in pool.items() if k!="entries"})}`',text)
                    for j,entry in enumerate(pool['entries']):
                        if (name,i,j) in direct|parent:self.assertIn(f'полный объект: `{compact(entry)}`',text)
                all_tables.append(tables)
        self.assertEqual(all_tables[0],all_tables[1])

    def test_loot_manual_pool_conditions_and_missing_weights(self):
        from build_loot_context import read_tables
        tables,_,_=read_tables('swordsandmoreswords-2-8-14.mcaddon','Swords_B')
        def pool(path,index):return tables['Swords_B/loot_tables/'+path+'.json']['pools'][index]
        blaze=pool('entities/blaze',1)
        self.assertEqual([{'condition':'killed_by_entity','entity_type':'minecraft:snow_golem'},{'condition':'random_chance_with_looting','chance':0.025,'looting_multiplier':0.02}],blaze['conditions'])
        for path,index,chance in [('entities/red_enderman',0,0.025),('entities/shulker',1,0.045),('entities/elder_guardian',1,0.065),('entities/wither_skeleton',3,0.025),('entities/slime_king',0,0.04)]:
            entry=pool(path,index)
            self.assertEqual(1,entry['rolls']);self.assertEqual(1,len(entry['entries']));self.assertEqual(1,entry['entries'][0]['weight'])
            self.assertEqual([{'condition':'killed_by_player'},{'condition':'random_chance_with_looting','chance':chance,'looting_multiplier':0.02}],entry['conditions'])
        outpost=pool('chests/pillager_outpost',3)['entries']
        self.assertNotIn('weight',outpost[-1])
        for entry in [e for e in outpost if e.get('name') in ('effect:emerald_sword','effect:lapis_sword')]:
            self.assertEqual(3,entry['weight']);self.assertEqual({'min':0,'max':1},entry['functions'][0]['count'])
        self.assertEqual(2,len([e for e in outpost if e.get('name') in ('effect:emerald_sword','effect:lapis_sword')]))
        ore=pool('blocks/quartz_diamond_ore',0)['entries']
        self.assertEqual([89,10,1],[e['weight'] for e in ore]);self.assertEqual([{'min':1,'max':1},{'min':1,'max':2},{'min':2,'max':4}],[e['functions'][0]['count'] for e in ore])

    def test_living_flame_hostile_drop_trigger_is_not_fatal_only(self):
        with zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as z:
            entity=json5.loads(z.read('Swords_B/entities/living_flame.json').decode('utf-8-sig'))['minecraft:entity']
        groups=entity['component_groups'];hostile=groups['hostile_entity'];passive=groups['passive_entity']
        sensor=hostile['minecraft:damage_sensor']['triggers']
        self.assertFalse(sensor['deals_damage'])
        self.assertEqual('start_death_hostile',sensor['on_damage']['event'])
        self.assertEqual([{'test':'is_family','subject':'other','value':'player'}],sensor['on_damage']['filters']['all_of'])
        self.assertEqual('start_death_hostile',hostile['minecraft:on_death']['event'])
        self.assertEqual('minecraft:start_death',hostile['minecraft:timer']['time_down_event']['event'])
        self.assertEqual('minecraft:start_death',passive['minecraft:damage_sensor']['triggers']['on_damage']['event'])
        event=entity['events']['start_death_hostile']['sequence']
        self.assertEqual([85,15],[e['weight'] for e in event[1]['randomize']])
        self.assertEqual(['loot spawn ~ ~ ~ loot "entities/living_flame"'],event[1]['randomize'][1]['run_command']['command'])

    def test_version_16_player_reset_overlaps_every_equipment_event(self):
        with zipfile.ZipFile(ROOT/'sources/SwordsAndMoreSwords.1.6.mcaddon') as z:
            player=json5.loads(z.read('Sword_B/entities/player.json').decode('utf-8-sig'))['minecraft:entity']
        self.assertEqual(['player'],player['components']['minecraft:type_family']['family'])
        sensors=[s['on_environment'] for s in player['components']['minecraft:environment_sensor']]
        reset=next(s for s in sensors if s['event']=='minecraft:event_normal_player')
        self.assertEqual([{'test':'is_family','subject':'self','value':'player'}],reset['filters']['all_of'])
        event=player['events']['minecraft:event_normal_player']
        self.assertEqual(['minecraft:normal_player'],event['add']['component_groups'])
        self.assertEqual({'minecraft:spell_effects':{},'minecraft:attack':{'damage':1}},player['component_groups']['minecraft:normal_player'])
        removed=event['remove']['component_groups']; self.assertEqual(26,len(removed))
        equip=[s for s in sensors if any(f.get('test')=='has_equipment' for f in s['filters'].get('all_of',[]))]
        self.assertEqual(26,len(equip))
        added=[g for s in equip for g in player['events'][s['event']]['add']['component_groups']]
        self.assertCountEqual(removed,added)
        for group in removed:
            obj=player['component_groups'][group]
            if group=='minecraft:quartz_sword':self.assertEqual({},obj);continue
            self.assertEqual(1,len(obj['minecraft:spawn_entity']))
            spawn=obj['minecraft:spawn_entity'][0]
            self.assertEqual((0,0,1,True),(spawn['min_wait_time'],spawn['max_wait_time'],spawn['num_to_spawn'],spawn['single_use']))

    def test_version_16_global_reset_command_order_and_writers(self):
        with zipfile.ZipFile(ROOT/'sources/SwordsAndMoreSwords.1.6.mcaddon') as z:
            def text(path):return z.read('Sword_B/'+path).decode('utf-8-sig')
            self.assertEqual(['scoreboard objectives add swords dummy','scoreboard players remove @a[scores={swords=1}] swords 1','scoreboard players remove @a[scores={swords=2}] swords 1','execute @a[scores={swords=0}] ~ ~ ~ function normal'],text('functions/normalft.mcfunction').splitlines())
            normal=[x for x in text('functions/normal.mcfunction').splitlines() if x]
            self.assertEqual(7,len([x for x in normal if x.startswith('fill ') and x.endswith('stone 0 replace barrier')]))
            self.assertEqual(['b','bn','sh','s'],[x.rsplit(' ',1)[-1] for x in normal if 'scoreboard objectives remove' in x])
            self.assertEqual(3,len([x for x in normal if x.startswith('tp @e[r=4,') and x.endswith('~ 0 ~')]))
            self.assertIn('gamerule randomtickspeed 1',normal)
            self.assertEqual('execute @p ~~~ fill ~5 ~5 ~5 ~-5 ~-5 ~-5 air 0 replace light_block 15',normal[-1])
            controllers={}
            for path in z.namelist():
                if path.startswith('Sword_B/animation_controllers/') and path.endswith('.json'):
                    data=json5.loads(z.read(path).decode('utf-8-sig'))['animation_controllers']
                    for name,controller in data.items():
                        hits={state for state,body in controller.get('states',{}).items() if '/scoreboard players set @a swords 2' in body.get('on_entry',[])}
                        if hits:controllers[name]=hits
            self.assertEqual(25,len(controllers))
            self.assertEqual({'controller.animation.ice':{'ice'},'controller.animation.jungle':{'jungle'},'controller.animation.wither':{'wither'}},{name:states for name,states in controllers.items() if len(states)==1})
            for name,states in controllers.items():
                if name not in ('controller.animation.ice','controller.animation.jungle','controller.animation.wither'):self.assertEqual(2,len(states))
            control=json5.loads(text('animation_controllers/normal.json'))['animation_controllers']['controller.animation.normal']['states']
            self.assertEqual(['/function normalft'],control['default']['on_entry']);self.assertEqual(['/function normalft'],control['normal']['on_entry'])
            self.assertEqual([{'normal':'(1.0)'}],control['default']['transitions']);self.assertEqual([{'default':'(1.0)'}],control['normal']['transitions'])

    def test_slime_score_reset_is_separate_from_family_filter(self):
        for filename in ('swordsandmoreswords_2_8_8.mcaddon','swordsandmoreswords-2-8-14.mcaddon'):
            with zipfile.ZipFile(ROOT/'sources'/filename) as z:
                player=json5.loads(z.read('Swords_B/entities/player.json').decode('utf-8-sig'))['minecraft:entity']
                slime=json5.loads(z.read('Swords_B/entities/mountable_slime.json').decode('utf-8-sig'))['minecraft:entity']
            steps=player['events']['minecraft:slime_sword']['sequence']
            self.assertEqual('slime_sword',steps[0]['filters']['value']);self.assertNotIn('filters',steps[1])
            self.assertEqual(['scoreboard players set @e[type=entity:mountable_slime,c=1,r=12] slime_despawn 0'],steps[1]['run_command']['command'])
            self.assertEqual(['ride @s summon_ride entity:mountable_slime no_ride_change','scoreboard objectives add slime_despawn dummy'],player['events']['slime_sword_skills']['run_command']['command'])
            commands=slime['events']['slime_events']['run_command']['command']
            self.assertEqual(['tp @s[scores={slime_despawn=0}] @e[type=player,family=slime_sword,c=1,rm=8,r=12]','scoreboard players add @s slime_despawn 1','execute @s[scores={slime_despawn=100}] ~~~ event entity @s despawn'],commands[2:])

    def test_time_clock_global_commands_and_unremoved_groups_both_versions(self):
        snapshots=[]
        for filename in ('swordsandmoreswords_2_8_8.mcaddon','swordsandmoreswords-2-8-14.mcaddon'):
            with zipfile.ZipFile(ROOT/'sources'/filename) as z:
                player=json5.loads(z.read('Swords_B/entities/player.json').decode('utf-8-sig'))['minecraft:entity']
                clock=json5.loads(z.read('Swords_B/items/clock_sword.json').decode('utf-8-sig'))['minecraft:item']
                time=json5.loads(z.read('Swords_B/items/time_sword.json').decode('utf-8-sig'))['minecraft:item']
            groups=player['component_groups'];events=player['events']
            self.assertEqual({'time':[5,5],'looping':True,'randomInterval':False,'time_down_event':{'event':'stop_clock_sword_event','target':'self'}},groups['clock_sword_skill']['minecraft:timer'])
            self.assertEqual({'value':1},groups['clock_sword_movement']['minecraft:movement'])
            self.assertEqual({'value':1},groups['time_sword_movement']['minecraft:movement'])
            self.assertEqual({'value':0.1},groups['minecraft:default_player']['minecraft:movement'])
            self.assertEqual({},groups['minecraft:default_player']['minecraft:timer'])
            self.assertEqual({'add':{'component_groups':['minecraft:default_player']}},events['default_player'])
            self.assertEqual({'test':'is_family','subject':'self','operator':'==','value':'clock_sword_skill'},events['minecraft:clock_sword']['sequence'][1]['filters'])
            self.assertEqual(['gamerule randomtickspeed 100','effect @e[type=!player] speed 1 10 true','time add 10','event entity @a[family=default_player] clock_sword_movement'],events['minecraft:clock_sword']['sequence'][1]['run_command']['command'])
            time_seq=events['minecraft:time_sword']['sequence']
            self.assertEqual({'add':{'component_groups':['minecraft:time_sword']}},time_seq[0])
            self.assertEqual(['gamerule randomtickspeed 300','effect @e[type=!player] speed 1 15 true','time add 30','event entity @a[family=default_player] time_sword_movement'],time_seq[1]['run_command']['command'][:4])
            for key,group in [('stop_clock_sword_event','minecraft:clock_sword'),('stop_time_sword_event','minecraft:time_sword')]:
                stop=events[key]['sequence'][0]
                self.assertEqual([group],stop['remove']['component_groups'])
                self.assertEqual(['gamerule randomtickspeed 1','effect @e[type=!player] speed 0 0','event entity @a[family=default_player] default_player'],stop['run_command']['command'])
            def removals(node):
                if isinstance(node,dict):
                    remove=node.get('remove')
                    if isinstance(remove,dict):yield from remove.get('component_groups',[])
                    for value in node.values():yield from removals(value)
                elif isinstance(node,list):
                    for value in node:yield from removals(value)
            self.assertTrue({'clock_sword_skill','clock_sword_movement','time_sword_movement'}.isdisjoint(set(removals(player))))
            self.assertEqual(30,clock['components']['minecraft:cooldown']['duration'])
            self.assertEqual(10,clock['events']['on_use']['damage']['amount'])
            self.assertEqual(['event entity @s[family=clock_sword] clock_sword_skill_event'],clock['events']['on_use']['run_command']['command'])
            keys=['minecraft:clock_sword','clock_sword_skill_event','clock_sword_movement','stop_clock_sword_event','minecraft:time_sword','time_sword_movement','stop_time_sword_event','default_player']
            sensors=[x['on_environment'] for x in player['components']['minecraft:environment_sensor'] if x['on_environment']['event'] in keys]
            snapshots.append(({k:events[k] for k in keys}, {k:groups[k] for k in ('minecraft:clock_sword','clock_sword_skill','clock_sword_movement','minecraft:time_sword','time_sword_movement','minecraft:default_player')},sensors,clock,time))
        self.assertEqual(snapshots[0],snapshots[1])

    def test_player_group_indexes_cover_event_operations(self):
        from build_player_group_index import gather,build
        versions=[('1.6','SwordsAndMoreSwords.1.6.mcaddon','Sword_B',30,2),('2.8.8','swordsandmoreswords_2_8_8.mcaddon','Swords_B',49,10),('2.8.14','swordsandmoreswords-2-8-14.mcaddon','Swords_B',49,10)]
        results=[]
        for version,filename,pack,count,no_remove in versions:
            source,groups,refs=gather(filename,pack)
            self.assertEqual(count,len(groups));self.assertEqual(set(groups),set(refs))
            self.assertEqual(no_remove,sum(bool(refs[g]['add']) and not refs[g]['remove'] for g in groups))
            with zipfile.ZipFile(ROOT/'sources'/filename) as z:
                entity=json5.loads(z.read(source).decode('utf-8-sig'))['minecraft:entity']
            independently=collections.Counter()
            def walk(node):
                if isinstance(node,dict):
                    for op in ('add','remove'):
                        if isinstance(node.get(op),dict):
                            for group in node[op].get('component_groups',[]):independently[(group,op)]+=1
                    for value in node.values():walk(value)
                elif isinstance(node,list):
                    for value in node:walk(value)
            walk(entity['events'])
            self.assertEqual(independently,collections.Counter({(group,op):len(paths) for group,operations in refs.items() for op,paths in operations.items() if paths}))
            self.assertEqual(build(version,filename,pack),(ROOT/'docs'/f'player-groups-{version}.md').read_text())
            if version!='1.6':results.append((groups,refs))
        self.assertEqual(results[0],results[1])
        groups,refs=results[0]
        expected={'clock_sword_skill','clock_sword_movement','ghost_movement','time_sword_movement','shulker_sword_skill','mermaid_movement_out_water','blaze_sword_skill','minecraft:default_player','despawn','minecraft:clear_bad_omen_spell_effect'}
        self.assertEqual(expected,{g for g in groups if refs[g]['add'] and not refs[g]['remove']})
        self.assertEqual(0.14,groups['ghost_movement']['minecraft:movement']['value'])
        self.assertEqual(0.06,groups['mermaid_movement_out_water']['minecraft:movement']['value'])
        self.assertEqual(0.7,groups['shulker_sword_skill']['minecraft:scale']['value'])
        self.assertEqual([6,6],groups['blaze_sword_skill']['minecraft:timer']['time'])

    def test_visual_screenshot_index_references_ocr_hashes(self):
        ocr=(ROOT/'docs/screenshot-ocr.md').read_text()
        visual=(ROOT/'docs/screenshot-visual-review.md').read_text()
        pattern=r'\[(Screenshot_20261104_\d+_com_kayenworks_mcpeaddons_AddonDetailActivity\.jpg)\]\(https://drive\.google\.com/file/d/([A-Za-z0-9_-]+)/view\)<br>`([0-9a-f]{64})`'
        entries=re.findall(pattern,visual)
        self.assertEqual(20,len(entries));self.assertEqual(20,len({name for name,_,_ in entries}))
        for name,file_id,digest in entries:
            self.assertIn('## '+name+'\n\nSHA-256: `'+digest+'`',ocr)
        self.assertIn('10o0',ocr);self.assertIn('1000 ticks',visual)
        self.assertIn('115915',visual);self.assertIn('115902',visual);self.assertIn('120007',visual)

    def test_screenshot_stat_comparison_is_reproducible_and_source_grounded(self):
        from build_screenshot_stats import evidence,items,generate
        rows=evidence();self.assertEqual(39,len(rows))
        old=items('swordsandmoreswords_2_8_8.mcaddon');new=items('swordsandmoreswords-2-8-14.mcaddon')
        self.assertEqual(42,len(new));self.assertEqual(old,new)
        self.assertEqual({'effect:cursed_pumpkin_sword','effect:quartz_diamond','effect:silver_ingot'},set(new)-{r['id'] for r in rows})
        numeric_damage=[r for r in rows if type(r['damage']) in (int,float)]
        numeric_durability=[r for r in rows if type(r['durability']) in (int,float)]
        self.assertEqual((39,37),(len(numeric_damage),len(numeric_durability)))
        for row in numeric_damage:self.assertEqual(row['damage'],new[row['id']]['damage'],row['id'])
        for row in numeric_durability:self.assertEqual(row['durability'],new[row['id']]['durability'],row['id'])
        index={r['id']:r for r in rows}
        self.assertFalse(index['effect:time_sword']['enchantable']);self.assertTrue(new['effect:time_sword']['enchantable'])
        self.assertFalse(index['effect:spectral_sword']['enchantable']);self.assertTrue(new['effect:spectral_sword']['enchantable'])
        self.assertFalse(index['effect:glass_sword']['repairable']);self.assertTrue(new['effect:glass_sword']['repairable'])
        self.assertTrue(index['effect:sponge_sword']['enchantable']);self.assertFalse(new['effect:sponge_sword']['enchantable'])
        text=(ROOT/'docs/screenshot-stat-comparison.md').read_text();self.assertEqual(generate(),text)
        reference=(ROOT/'docs/items-2.8.14.md').read_text()
        visual=(ROOT/'docs/screenshot-visual-review.md').read_text()
        for row in rows:
            self.assertIn('## '+row['id']+'\n',reference)
            self.assertIn('#'+row['id'].replace(':','')+')',text)
            for stamp in row['screenshots']:self.assertIn('Screenshot_20261104_'+stamp+'_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg',visual)

    def test_spectral_world_fill_geometry_and_version_agreement(self):
        snapshots=[]
        for filename in ('swordsandmoreswords_2_8_8.mcaddon','swordsandmoreswords-2-8-14.mcaddon'):
            with zipfile.ZipFile(ROOT/'sources'/filename) as z:
                player=json5.loads(z.read('Swords_B/entities/player.json').decode('utf-8-sig'))['minecraft:entity']
                block=json5.loads(z.read('Swords_B/blocks/spectral_block.json').decode('utf-8-sig'))['minecraft:block']
            events=player['events']; keys=('minecraft:spectral_sword','spectral_sword_function','spectral_sword_function_1','minecraft:stop_sword_events','stop_spectral_sword_event')
            snapshots.append(({k:events[k] for k in keys},block))
            calls=events['minecraft:spectral_sword']['sequence'][1]['run_command']['command']
            self.assertIn('execute @s[y=8,dy=247] ~~~ event entity @s spectral_sword_function',calls)
            self.assertIn('execute @s[y=0,dy=7] ~~~ event entity @s spectral_sword_function_1',calls)
            def positions(command):
                parts=command.split();self.assertEqual('fill',parts[0]);coords=[int(x[1:]) if x!='~' else 0 for x in parts[1:7]]
                ranges=[range(min(coords[i],coords[i+3]),max(coords[i],coords[i+3])+1) for i in range(3)]
                return {(x,y,z) for x in ranges[0] for y in ranges[1] for z in ranges[2]}
            central={(x,y,z) for x in range(-6,7) for y in range(-6,7) for z in range(-6,7)}
            large={(x,y,z) for x in range(-8,9) for y in range(-8,9) for z in range(-8,9)}
            for branch,material in zip(events['spectral_sword_function']['sequence'],('stone','netherrack','end_stone')):
                commands=branch['run_command']['command'];self.assertEqual(7,len(commands))
                self.assertEqual(central,positions(commands[0]));self.assertTrue(commands[0].endswith('effect99:spectral_block 0 replace '+material))
                shell=set().union(*(positions(command) for command in commands[1:]));self.assertEqual(2716,len(shell));self.assertEqual(large-central,shell)
                self.assertTrue(all(cmd.endswith(material+' 0 replace effect99:spectral_block') for cmd in commands[1:]))
            for branch,material in zip(events['spectral_sword_function_1']['sequence'],('stone','netherrack','end_stone')):
                commands=branch['run_command']['command'];self.assertEqual(1,len(commands));self.assertEqual(4335,len(positions(commands[0])))
                self.assertTrue(commands[0].endswith(material+' 0 replace effect99:spectral_block'))
            stop=events['minecraft:stop_sword_events']['sequence']
            self.assertEqual(5,len(stop));self.assertIn('execute @e[r=64,type=!player] ~ ~ ~ detect ~ ~ ~ ice 0 tp @s ~ ~ ~',stop[0]['run_command']['command'])
            self.assertIn('ride @e[type=entity:mountable_slime,r=1,y=~-1] evict_riders',stop[4]['run_command']['command'])
            sensor=next(x['on_environment'] for x in player['components']['minecraft:environment_sensor'] if x['on_environment']['event']=='minecraft:stop_sword_events')
            self.assertEqual([{'test':'is_family','subject':'self','value':'default_player'},{'test':'is_family','subject':'self','operator':'!=','value':'spectral_sword'}],sensor['filters']['any_of'])
        self.assertEqual(snapshots[0],snapshots[1])

    def test_sound_command_index_and_local_assets(self):
        from build_sound_audit import collect,build
        data={}
        for version,filename,pack,count,errors in [('1.6','SwordsAndMoreSwords.1.6.mcaddon','Sword_R',14,3),('2.8.8','swordsandmoreswords_2_8_8.mcaddon','Swords_R',107,1),('2.8.14','swordsandmoreswords-2-8-14.mcaddon','Swords_R',107,1)]:
            files,defs,records,broken,duplicates=collect(filename,pack)
            self.assertEqual(count,len(records));self.assertEqual(errors,len(broken))
            self.assertEqual(0 if version=='1.6' else 3,len(defs))
            self.assertEqual(0 if version=='1.6' else 3,len(duplicates))
            text=(ROOT/'docs'/f'sound-index-{version}.md').read_text()
            self.assertEqual(build(version,filename,pack),text)
            for source,loc,op,sound,command in records:
                self.assertIn(f'### `{op} {sound}`',text)
                self.assertIn(f'`{source}` · `{loc}`',text)
            if version!='1.6':data[version]=(defs,records)
        self.assertEqual(data['2.8.8'],data['2.8.14'])
        defs,records=data['2.8.14']
        self.assertEqual({'wolf_sword.howl','wolf_sword.distant_howl','ghost_sword.wailing'},set(defs))
        self.assertEqual([32.0,100.0,60.0],[defs[n]['min_distance'] for n in ('wolf_sword.howl','wolf_sword.distant_howl','ghost_sword.wailing')])
        calls=[(op,sound,text) for _,_,op,sound,text in records]
        self.assertIn(('stopsound','wolf_sword.howl','stopsound @a wolf_sword.howl'),calls)
        self.assertEqual(2,calls.count(('stopsound','wolf_sword.distant_howl','stopsound @a wolf_sword.distant_howl')))
        self.assertIn(('playsound','ghost_sword.wailing','playsound ghost_sword.wailing @a[rm=10,r=50] ~~~ 1 7'),calls)

    def test_ghost_wailing_randomize_and_explicit_underground_spawn_event(self):
        with zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as z:
            ghost=json5.loads(z.read('Swords_B/entities/ghost.json').decode('utf-8-sig'))['minecraft:entity']
            rules=json5.loads(z.read('Swords_B/spawn_rules/ghost.json').decode('utf-8-sig'))['minecraft:spawn_rules']
        branches=ghost['events']['ghost_wailing']['randomize']
        self.assertEqual([70,30],[b['weight'] for b in branches])
        self.assertEqual([50,50],[b['weight'] for b in branches[1]['randomize']])
        conditions=rules['conditions'];self.assertEqual(2,len(conditions))
        self.assertEqual('ghost_wailing',conditions[0]['minecraft:spawn_event']['event'])
        self.assertNotIn('minecraft:spawn_event',conditions[1])

    def test_wish_fountain_detects_weights_consumption_and_versions(self):
        snapshots=[]
        for filename in ('swordsandmoreswords_2_8_8.mcaddon','swordsandmoreswords-2-8-14.mcaddon'):
            with zipfile.ZipFile(ROOT/'sources'/filename) as z:
                item=json5.loads(z.read('Swords_B/entities/item.json').decode('utf-8-sig'))['minecraft:entity']
                quartz=json5.loads(z.read('Swords_B/items/quartz_diamond.json').decode('utf-8-sig'))['minecraft:item']
                clock=json5.loads(z.read('Swords_B/items/clock_sword.json').decode('utf-8-sig'))['minecraft:item']
                tags=z.read('Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/tag_swords.mcfunction').decode('utf-8-sig').splitlines()
            self.assertEqual(9,quartz['components']['minecraft:max_stack_size']);self.assertEqual(1,clock['components']['minecraft:max_stack_size'])
            self.assertEqual(['tag @e[type=item,name="Quartz Diamond",tag=!wish_1] add wish_1','tag @e[type=item,name="Quartz Diamond block",tag=!wish_2] add wish_2','tag @e[type=item,name="§l§gClock Sword",tag=!wish_3] add wish_3'],tags[-3:])
            events=item['events']; names=['fountain_of_wishes_1','fountain_of_wishes_2','fountain_of_wishes_3','wish_1','wish_2','wish_3'];snapshots.append(({n:events[n] for n in names},tags))
            expected=[('~','~','~','water'),('~1','~','~','water'),('~-1','~','~','water'),('~','~','~1','water'),('~','~','~-1','water'),('~','~-1','~','sandstone'),('~1','~-1','~','sandstone'),('~-1','~-1','~','sandstone'),('~','~-1','~1','sandstone'),('~','~-1','~-1','sandstone'),('~','~4','~','sandstone'),('~1','~2','~1','sandstone'),('~-1','~2','~-1','sandstone'),('~-1','~2','~1','sandstone'),('~1','~2','~-1','sandstone')]
            for i in range(1,4):
                cmd=events[f'fountain_of_wishes_{i}']['run_command']['command'][0]
                actual=re.findall(r'detect (\S+) (\S+) (\S+) (water|sandstone) 0',cmd)
                self.assertEqual(expected,actual);self.assertTrue(cmd.endswith(f'event entity @s wish_{i}'))
            for i,weights in [(1,[992,8]),(2,[975,25]),(3,[975,25])]:
                branches=events[f'wish_{i}']['randomize'];self.assertEqual(weights,[x['weight'] for x in branches])
                for branch in branches:self.assertEqual('kill @s',branch['run_command']['command'][-1])
                success=branches[1]['run_command']['command']
                self.assertTrue(success[0].startswith('structure load '+('time_sword' if i==3 else 'ultra_instinct_sword')+' ~ ~1 ~'))
                fill=next(c for c in success if c.startswith('fill '))
                self.assertEqual(f'fill ~15 ~10 ~15 ~-15 ~-15 ~-15 concretepowder {4 if i==3 else 0} replace sand',fill)
            self.assertIn('time add 1000',events['wish_3']['randomize'][0]['run_command']['command'])
            self.assertIn('time add 6000',events['wish_3']['randomize'][1]['run_command']['command'])
        self.assertEqual(snapshots[0],snapshots[1])
        self.assertEqual(24986,31*26*31)

    def test_legacy_world_helper_geometry_and_command_contexts(self):
        from itertools import product
        with zipfile.ZipFile(ROOT/'sources/SwordsAndMoreSwords.1.6.mcaddon') as z:
            def load(path):return json5.loads(z.read('Sword_B/'+path).decode('utf-8-sig'))
            player=load('entities/player.json')['minecraft:entity']
            pairs=[('spectral','entity:spectral','controller.animation.spectral','spectral_sword'),('glowstone','entity:glow','controller.animation.glow','glowstone_sword'),('sponge','entity:sponge','controller.animation.sponge','sponge_sword'),('obsidian','entity:obsidian','controller.animation.ob','obsidian_sword'),('coal','entity:coal','controller.animation.coal','coal_sword')]
            for name,helper,controller,filename in pairs:
                group=player['component_groups']['minecraft:'+filename]
                self.assertEqual({'min_wait_time':0,'max_wait_time':0,'spawn_entity':helper,'num_to_spawn':1,'single_use':True},group['minecraft:spawn_entity'][0])
                states=load('animation_controllers/'+filename+'.json')['animation_controllers'][controller]['states']
                self.assertEqual(2,len(states));first,second=states.values()
                self.assertEqual(first['on_entry'],second['on_entry'])
                self.assertEqual('/scoreboard players set @a swords 2',first['on_entry'][-1])
            spectral=load('animation_controllers/spectral_sword.json')['animation_controllers']['controller.animation.spectral']['states']['default']['on_entry']
            normal=z.read('Sword_B/functions/normal.mcfunction').decode('utf-8-sig').splitlines()
            glow=load('animation_controllers/glowstone_sword.json')['animation_controllers']['controller.animation.glow']['states']['default']['on_entry']
            sponge=load('animation_controllers/sponge_sword.json')['animation_controllers']['controller.animation.sponge']['states']['default']['on_entry']
            obsidian=load('animation_controllers/obsidian_sword.json')['animation_controllers']['controller.animation.ob']['states']['default']['on_entry']
            coal=load('animation_controllers/coal_sword.json')['animation_controllers']['controller.animation.coal']['states']['default']['on_entry']
        self.assertEqual('/execute @p ~~~ fill ~6 ~6 ~6 ~-6 ~-6 ~-6 barrier 0 replace stone 0',spectral[0])
        def positions(cmd):
            fields=cmd.lstrip('/').split();self.assertEqual('fill',fields[0]);coords=[int(v[1:] or 0) for v in fields[1:7]]
            return set(product(*(range(min(a,b),max(a,b)+1) for a,b in zip(coords[:3],coords[3:]))))
        slabs=[positions(cmd) for cmd in spectral[1:7]]
        shell=set().union(*slabs);center=set(product(range(-6,7),repeat=3));cube=set(product(range(-8,9),repeat=3))
        self.assertEqual(3196,sum(map(len,slabs)));self.assertEqual(2716,len(shell));self.assertEqual(cube-center,shell)
        self.assertEqual([c.lstrip('/') for c in spectral[1:7]],[c for c in normal if c.startswith('fill ')][:6])
        self.assertEqual(cube,shell|positions([c for c in normal if c.startswith('fill ')][6]))
        self.assertEqual(glow[0],glow[2]);self.assertIn('fill ~5 ~5 ~5 ~-5 ~-5 ~-5 air 0 replace light_block 15',glow[1])
        self.assertEqual(13,len(sponge));self.assertIn('replace water',sponge[0]);self.assertIn('replace sponge',sponge[1]);self.assertEqual(list(range(9)),[int(re.search(r'detect ~ ~ ~ water (\d+)',c).group(1)) for c in sponge[2:11]])
        self.assertIn('detect ~ ~1 ~ air 0',sponge[11]);self.assertEqual(13,len(obsidian))
        self.assertIn('replace lava 0',obsidian[0]);self.assertIn('replace flowing_lava 0',obsidian[1]);self.assertEqual(list(range(9)),[int(re.search(r'detect ~ ~ ~ lava (\d+)',c).group(1)) for c in obsidian[2:11]])
        self.assertIn('detect ~ ~ ~ flowing_lava 0',obsidian[11]);self.assertEqual(14,len(coal))
        coords=set()
        for cmd in coal[:-1]:
            m=re.fullmatch(r'/replaceitem block (~-?\d*) (~-?\d*) (~-?\d*) slot.container 1 coal',cmd);self.assertIsNotNone(m)
            coords.add(tuple(int(v[1:] or 0) for v in m.groups()))
        cross={(1,0),(-1,0),(0,1),(0,-1)}
        self.assertEqual({(x,y,z) for y in (-1,0,1) for x,z in cross}|{(0,-1,0)},coords)

    def test_legacy_counted_helpers_selectors_order_and_global_teleport(self):
        cases=[('blaze','b','blaze2','2',10,4990,5000),('bone','bn','bone2','2',10,4990,5000),('shulker','sh','shulker2','2.5',40,2390,2400)]
        with zipfile.ZipFile(ROOT/'sources/SwordsAndMoreSwords.1.6.mcaddon') as z:
            def commands(name):
                states=json5.loads(z.read(f'Sword_B/animation_controllers/{name}_sword.json').decode('utf-8-sig'))['animation_controllers'][f'controller.animation.{name}']['states']
                self.assertEqual(list(states.values())[0]['on_entry'],list(states.values())[1]['on_entry'])
                return states['default']['on_entry']
            for name,objective,entity,height,summon,kill,remove in cases:
                cmds=commands(name);offset=1 if name=='shulker' else 0
                self.assertEqual(f'/execute @p ~ ~ ~ tp @e[type=entity:{entity}] ~ ~{height} ~',cmds[offset])
                self.assertEqual(f'/scoreboard objectives add {objective} dummy',cmds[offset+1])
                self.assertEqual(f'/scoreboard players add @p {objective} 1',cmds[offset+2])
                self.assertEqual(f'/execute @p[scores={{{objective}={summon}}}] ~ ~ ~ summon entity:{entity}',cmds[offset+3])
                self.assertEqual(f'/execute @p[scores={{{objective}={remove}}}] ~ ~ ~ scoreboard objectives remove {objective}',cmds[offset+4])
                self.assertEqual(f'/execute @p[scores={{{objective}={kill}}}] ~ ~ ~ kill @e[type=entity:{entity},r=5] ~ 0 ~',cmds[offset+5])
                self.assertEqual('/scoreboard players set @a swords 2',cmds[-1])
            slime=commands('slime');lapis=commands('lapis')
            self.assertEqual('/execute @p[scores={s=1}] ~ ~ ~ summon slime',slime[2]);self.assertEqual('/effect @p jump_boost 1 5 true',slime[3])
            self.assertEqual('/execute @p[scores={s=600}] ~ ~ ~ scoreboard objectives remove s',slime[4])
            self.assertEqual('/execute @p[scores={l=10}] ~ ~ ~ xp 5 @s',lapis[2]);self.assertEqual('/execute @p[scores={l=30}] ~ ~ ~ scoreboard objectives remove l',lapis[3])
            normal=z.read('Sword_B/functions/normal.mcfunction').decode('utf-8-sig')
            self.assertIn('execute @p[r=2] ~ ~ ~ scoreboard objectives remove s',normal)
            self.assertNotIn('scoreboard objectives remove l\n',normal)

    def test_legacy_area_target_matrix_and_controller_order(self):
        from build_legacy_target_matrix import collect,build
        matrix=collect();self.assertEqual({'Wither':28,'Creeper':27,'Ender':27,'TNT':26},{k:len(v) for k,v in matrix.items()})
        sets={k:{x for x,_ in v} for k,v in matrix.items()}
        self.assertEqual({'creeper'},sets['Wither']-sets['Creeper'])
        self.assertEqual({'wither'},sets['Wither']-sets['Ender'])
        self.assertEqual({'wither','tnt'},sets['Wither']-sets['TNT'])
        self.assertTrue(all(sets[k] <= sets['Wither'] for k in ['Creeper','Ender','TNT']))
        self.assertEqual(build(matrix),(ROOT/'docs/target-matrix-1.6.md').read_text())
        with zipfile.ZipFile(ROOT/'sources/SwordsAndMoreSwords.1.6.mcaddon') as z:
            def states(name):return json5.loads(z.read(f'Sword_B/animation_controllers/{name}_sword.json').decode('utf-8-sig'))['animation_controllers'][f'controller.animation.{name}']['states']
            for name in ['ender','creeper','tnt']:
                ss=states(name);self.assertEqual(ss['default']['on_entry'],ss[name]['on_entry'])
            wither=states('wither');self.assertEqual(['/Effect99'],wither['default']['on_entry'])
            commands=wither['wither']['on_entry'];self.assertEqual(46,len(commands));self.assertEqual('/effect @e[r=16,type=!player] poison 30 1 true',commands[0])
            fills=[x for x in commands if x.startswith('/fill ')];self.assertEqual(10,len(fills))
            self.assertTrue(all('/fill ~5 ~5 ~5 ~-5 ~-5 ~-5 ' in c for c in fills))
            score=[x for x in commands if x.startswith('/scoreboard players add @e')][0]
            self.assertEqual(['cow','pig','sheep','horse','rabbit','villager','wolf','cat','fox','chicken'],re.findall(r'type=!([^,\]]+)',score));self.assertNotIn('type=!player',score)
            ender=states('ender')['default']['on_entry']
            self.assertEqual('/scoreboard players add @e[r=16] e 1',ender[3])
            self.assertIn('scores={e=700}',ender[9]);self.assertIn('scores={e=750}',ender[10]);self.assertIn('scores={e=85}',ender[11])
            explosion=json5.loads(z.read('Sword_B/entities/explode.json').decode('utf-8-sig'))['minecraft:entity']
            self.assertEqual(['tnt','inanimate'],explosion['components']['minecraft:type_family']['family'])
            exp=explosion['components']['minecraft:explode'];self.assertEqual((0,True,4,False,True),tuple(exp[k] for k in ('fuseLength','fuseLit','power','causesFire','destroy_affected_by_griefing')))
            self.assertEqual({'range_min':0,'range_max':0},explosion['component_groups']['from_explosion']['minecraft:explode']['fuseLength'])

    def test_ore_loot_paths_are_distinct_and_conditional_distribution(self):
        from fractions import Fraction
        paths=['Swords_B/blocks/quartz_diamond_block.json','Swords_B/blocks/quartz_diamond_ore.json','Swords_B/blocks/silver_ore.json','Swords_B/loot_tables/blocks/quartz_diamond_block.json','Swords_B/loot_tables/blocks/quartz_diamond_ore.json','Swords_B/loot_tables/blocks/silver_ore.json','Swords_B/entities/spider.json','Swords_B/loot_tables/empty.json']
        copies=[]
        for filename in ['swordsandmoreswords_2_8_8.mcaddon','swordsandmoreswords-2-8-14.mcaddon']:
            with zipfile.ZipFile(ROOT/'sources'/filename) as z:
                copies.append({p:z.read(p) for p in paths})
                self.assertNotIn('Swords_B/loot_tables/blocks/null.json',z.namelist())
                self.assertNotIn('Swords_B/loot_tables/entities/empty.json',z.namelist())
                self.assertNotIn('Swords_B/loot_tables/entity/centella.json',z.namelist())
                self.assertEqual({},json5.loads(z.read('Swords_B/loot_tables/empty.json').decode('utf-8-sig')))
                spider=json5.loads(z.read('Swords_B/entities/spider.json').decode('utf-8-sig'))['minecraft:entity']
                self.assertEqual('loot_tables/entities/empty.json',spider['component_groups']['minecraft:spider_player_jockey']['minecraft:loot']['table'])
                blocks=[json5.loads(z.read(p).decode('utf-8-sig'))['minecraft:block'] for p in paths[:3]]
                self.assertEqual(['loot_tables/blocks/null.json']*3,[b['components']['minecraft:loot'] for b in blocks])
                self.assertEqual(1,len({b['components']['minecraft:on_player_destroyed']['condition'] for b in blocks}))
                self.assertEqual([20,10,8],[b['components']['minecraft:destroy_time'] for b in blocks])
                self.assertEqual([999,999,1],[b['components']['minecraft:explosion_resistance'] for b in blocks])
                self.assertIn('minecraft:light_emission',blocks[1]['components']);self.assertIn('minecraft:block_light_emission',blocks[0]['components']);self.assertIn('minecraft:block_light_emission',blocks[2]['components'])
                ore=blocks[1]['events']['quartz_diamond_ore']['run_command']['command'];self.assertEqual(6,ore.count('summon xp_orb'));self.assertEqual('effect @p[r=6] instant_damage 1 0 true',ore[-1])
                entries=json5.loads(z.read(paths[4]).decode('utf-8-sig'))['pools'][0]['entries']
                self.assertEqual([89,10,1],[e['weight'] for e in entries]);self.assertEqual([(1,1),(1,2),(2,4)],[(e['functions'][0]['count']['min'],e['functions'][0]['count']['max']) for e in entries])
                self.assertEqual({'effect:quartz_diamond'},{e['name'] for e in entries})
        self.assertEqual(copies[0],copies[1])
        probs={i:sum((Fraction(e['weight'],100)*Fraction(1,e['functions'][0]['count']['max']-e['functions'][0]['count']['min']+1) for e in entries if e['functions'][0]['count']['min']<=i<=e['functions'][0]['count']['max']),Fraction()) for i in range(1,5)}
        self.assertEqual({1:Fraction(47,50),2:Fraction(4,75),3:Fraction(1,300),4:Fraction(1,300)},probs)
        self.assertEqual(Fraction(107,100),sum(i*p for i,p in probs.items()))

    def test_dropped_item_controller_order_sensors_and_structures(self):
        with zipfile.ZipFile(ROOT/'sources/swordsandmoreswords_2_8_8.mcaddon') as old,zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as new:
            paths=['Swords_B/entities/item.json','Swords_B/animation_controllers/item_events.json','Swords_B/entities/instant_giant_explode.json','Swords_B/entities/ultra_instinct_explode.json','Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/tag_swords.mcfunction']
            for path in paths:self.assertEqual(old.read(path),new.read(path))
            obj=json5.loads(new.read(paths[0]).decode('utf-8-sig'))['minecraft:entity'];events=obj['events'];groups=obj['component_groups']
            controller=json5.loads(new.read(paths[1]).decode('utf-8-sig'))['animation_controllers']['controller.animation.item_events']['states']
            expected=[('fire_sword,tag=!fire_sword_respawn','fire_sword_event_3'),('tnt_sword','despawn_event_5'),('ice_sword','despawn_event_4'),('ender_sword','despawn_event_1'),('wither_sword','despawn_event_2'),('lightning_sword','despawn_event_3'),('nether_star_sword','despawn_event_6'),('bedrock_sword','respawn_event_1'),('fire_sword_respawn','respawn_event_2')]
            self.assertEqual([f'/event entity @s[tag={tag}] {event}' for tag,event in expected],controller['on_fire_swords']['on_entry'])
            self.assertEqual({'on_fire_swords':'q.is_on_fire'},controller['default']['transitions'][0]);self.assertEqual({'default':'1.0'},controller['on_fire_swords']['transitions'][0])
            for group,times,event in [('fire_sword',[5,6],'fire_sword_event_1'),('sponge_sword',[0,1],'wet_sponge_sword')]:
                timer=groups[group]['minecraft:timer'];self.assertEqual(times,timer['time']);self.assertFalse(timer['looping']);self.assertTrue(timer['randomInterval']);self.assertEqual(event,timer['time_down_event']['event'])
            self.assertEqual(['structure load obsidian_sword ~ ~ ~','playsound random.fizz @a[r=12] ~ ~ ~','kill @s'],events['fire_sword_event_1']['run_command']['command'])
            self.assertEqual(['playsound random.fizz @a[r=12] ~ ~ ~ 0.6','particle minecraft:cauldron_explosion_emitter ~ ~ ~','structure load glass_sword ~ ~ ~','kill @s'],events['fire_sword_event_2']['run_command']['command'])
            self.assertEqual(['structure load wet_sponge_sword ~ ~ ~','kill @s'],events['wet_sponge_sword']['run_command']['command'])
            fire=events['fire_sword_event_3']['sequence'][0]['run_command']['command'];self.assertEqual(9,sum(c.startswith('particle ') for c in fire));self.assertEqual(5,fire.count('summon entity:living_flame ~~~ hostile_entity'));self.assertEqual('kill @s',fire[-1])
            ice=events['despawn_event_4']['sequence'];self.assertEqual(2,len(ice));self.assertEqual('!=',ice[0]['filters']['operator']);self.assertEqual('nether',ice[1]['filters']['value'])
            self.assertEqual(['fill ~~~ ~~~ flowing_water 0 replace air','fill ~~~ ~~~ flowing_water 0 replace fire','fill ~~~ ~~~ flowing_water 0 replace lava'],ice[0]['run_command']['command'][:3]);self.assertFalse(any(c.startswith('fill ') for c in ice[1]['run_command']['command']))
            self.assertNotIn('kill @s',events['despawn_event_3']['run_command']['command'])
            for name in ['fire_sword','bedrock_sword','glass_sword','obsidian_sword','wet_sponge_sword']:
                path=f'Swords_B/structures/{name}.mcstructure';self.assertEqual(old.read(path),new.read(path))
                items=nbtlib.File.parse(io.BytesIO(new.read(path)),byteorder='little')['structure']['entities'];self.assertEqual(1,len(items));self.assertEqual(1,int(items[0]['Item']['Count']))
            for z in (old,new):
                hits=[]
                for name in z.namelist():
                    if name.endswith(('.json','.mcfunction','.js')):
                        for line in z.read(name).decode('utf-8-sig').splitlines():
                            if 'fire_immune' in line and 'minecraft:fire_immune' not in line:hits.append((name,line.strip()))
                    elif name.endswith('.mcstructure'):self.assertNotIn(b'fire_immune',z.read(name))
                self.assertEqual([('Swords_B/entities/item.json','"filters": { "test": "has_tag", "value": "fire_immune" },')],hits)

    @unittest.skipUnless(shutil.which('node'), 'Node.js required for mocked original script control flow')
    def test_pumpkin_script_original_js_with_mocked_server_api(self):
        sources=[];manifests=[]
        with zipfile.ZipFile(ROOT/'sources/swordsandmoreswords_2_8_8.mcaddon') as old,zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as new:
            for z in (old,new):
                source=z.read('Swords_B/scripts/javascript.js');sources.append(source.decode('utf-8-sig'))
                result=subprocess.run(['node',str(ROOT/'tools/test_pumpkin_script.cjs')],input=source,capture_output=True,check=False,timeout=10)
                self.assertEqual(0,result.returncode,result.stderr.decode('utf-8',errors='replace'));self.assertIn('all control-flow cases passed',result.stdout.decode())
                manifest=json5.loads(z.read('Swords_B/manifest.json').decode('utf-8-sig'));manifests.append(manifest)
                self.assertEqual([1,19,40],manifest['header']['min_engine_version'])
                self.assertTrue(any(x.get('type')=='script' and x.get('entry')=='scripts/javascript.js' for x in manifest['modules']))
            for path in ['Swords_B/items/pumpkin_sword.json','Swords_B/entities/pumpkin_projectile.json','Swords_B/loot_tables/pumpkin_sword.json']:
                self.assertEqual(old.read(path),new.read(path))
        self.assertNotEqual(sources[0],sources[1]);self.assertEqual([x.rstrip() for x in sources[0].splitlines()],[x.rstrip() for x in sources[1].splitlines()])
        self.assertEqual(['1.8.0-beta','1.12.0-beta'],[next(d['version'] for d in m['dependencies'] if d.get('description')=='@minecraft/server') for m in manifests])
        from math import log,ceil
        self.assertEqual(139,ceil(log(0.5)/log(0.995)))
        self.assertAlmostEqual(4.8889869534,100*(1-0.995**10),places=6)
        self.assertAlmostEqual(39.42295635,100*(1-0.995**100),places=6)

    def test_wolf_conditions_source_model_and_cross_family_triggers(self):
        from build_wolf_conditions import build,model,source_conditions
        self.assertEqual(3,len(source_conditions()));self.assertEqual(build(),(ROOT/'docs/wolf-condition-samples-2.8.md').read_text())
        for t in ('0.77','0.775','0.78'):self.assertEqual((True,False,True),model(True,0,t))
        self.assertEqual((False,False,True),model(True,0,'0.79'))
        for t in ('0.20','0.80'):self.assertEqual((False,True,True),model(True,0,t))
        self.assertEqual((False,False,True),model(False,0,'0.20'));self.assertEqual((False,False,False),model(False,1,'0.20'))
        with zipfile.ZipFile(ROOT/'sources/swordsandmoreswords_2_8_8.mcaddon') as old,zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as new:
            for path in ['Swords_R/entity/player.entity.json','Swords_B/entities/mountable_slime.json','Swords_B/entities/living_flame.json']:
                self.assertEqual(old.read(path),new.read(path))
            self.assertNotEqual(old.read('Swords_B/entities/player.json'),new.read('Swords_B/entities/player.json'))
            p=json5.loads(new.read('Swords_B/entities/player.json').decode('utf-8-sig'))['minecraft:entity']
            oldp=json5.loads(old.read('Swords_B/entities/player.json').decode('utf-8-sig'))['minecraft:entity']
            for section in ('component_groups','events'):
                for key in p[section]:
                    if 'wolf' in key or key=='minecraft:fire_sword':self.assertEqual(oldp[section][key],p[section][key])
            self.assertEqual(oldp['description'],p['description'])
            for trigger in p['components']['minecraft:environment_sensor']:
                if 'wolf' in str(trigger):self.assertIn(trigger,oldp['components']['minecraft:environment_sensor'])
            self.assertEqual(['player','default_player'],p['components']['minecraft:type_family']['family'])
            g=p['component_groups']['complete_wolf_transformation'];self.assertEqual(['wolf','wolf_sword','complete_wolf_transformation','monster'],g['minecraft:type_family']['family']);self.assertEqual(15,g['minecraft:attack']['damage'])
            self.assertEqual([3,6],g['minecraft:timer']['time']);self.assertTrue(g['minecraft:timer']['looping'])
            stop=p['events']['stop_wolf_transformation']['sequence'];self.assertNotIn('filters',stop[0]);self.assertEqual(['wolf_transformation','complete_wolf_transformation','wolf_movement'],stop[1]['remove']['component_groups']);self.assertEqual(['minecraft:wolf_sword'],stop[1]['add']['component_groups'])
            self.assertIn('stopsound @a wolf_sword.distant_howl',stop[0]['run_command']['command'])
            fire=p['events']['minecraft:fire_sword']['sequence'][1]['run_command']['command'];self.assertIn('execute @e[family=!player,type=!item,r=3] ~ ~ ~ summon entity:fire',fire)
            slime=json5.loads(new.read('Swords_B/entities/mountable_slime.json').decode('utf-8-sig'))['minecraft:entity'];self.assertIn('execute @e[r=1,family=monster] ~~~ summon entity:slime_damage',slime['events']['slime_events']['run_command']['command'])
            flame=json5.loads(new.read('Swords_B/entities/living_flame.json').decode('utf-8-sig'))['minecraft:entity'];target=flame['component_groups']['passive_entity']['minecraft:behavior.nearest_attackable_target']['entity_types'][0];self.assertEqual('monster',target['filters']['any_of'][0]['value']);self.assertEqual(16,target['max_dist'])
            client=json5.loads(new.read('Swords_R/entity/player.entity.json').decode('utf-8-sig'))['minecraft:client_entity']['description'];animations=client['scripts']['pre_animation']
            self.assertTrue(any('variable.wolf_transformation' in x and '!variable.is_first_person' in x and 'query.moon_phase == 0' in x and 'query.time_of_day <= 0.20 || query.time_of_day >= 0.80' in x for x in animations))
            self.assertTrue(any('variable.wolf_vision' in x and 'variable.is_first_person' in x and 'query.time_of_day <= 0.20 || query.time_of_day >= 0.80' in x for x in animations))

    def test_digger_profiles_cover_all_items_and_ordered_bedrock_rules(self):
        from build_digger_index import collect,build,ABSENT
        profiles,members,diagnostics=collect();self.assertEqual([],diagnostics);self.assertEqual(6,len(profiles))
        self.assertEqual(build(),(ROOT/'docs/digger-index.md').read_text())
        for version,total in [('1.6',26),('2.8.8',42),('2.8.14',42)]:
            ids=[item for profile in members.values() for item in profile.get(version,[])]
            self.assertEqual(total,len(ids));self.assertEqual(total,len(set(ids)))
        for key in profiles:
            self.assertEqual(sorted(members[key].get('2.8.8',[])),sorted(members[key].get('2.8.14',[])))
        absent=next(key for key,val in profiles.items() if val==ABSENT)
        self.assertCountEqual(['effect:bedrock_stick','effect:quartz_diamond','effect:quartz_diamond_stick','effect:silver_ingot','effect:tnt_sword','effect:wet_sponge_sword'],members[absent]['2.8.14'])
        def digger_for(item):return profiles[next(k for k,m in members.items() if item in m.get('2.8.14',[]))]
        bedrock=digger_for('effect:bedrock_sword');rules=bedrock['destroy_speeds'];self.assertEqual(68,len(rules));self.assertEqual(True,bedrock['use_efficiency'])
        self.assertEqual([50,100,999],[r['speed'] for r in rules[1:4]])
        self.assertEqual(['effect99:quartz_diamond_block','effect99:quartz_diamond_ore','effect99:silver_ore'],[r['block'] for r in rules[1:4]])
        self.assertIn('diamond_pick_diggable',rules[0]['block']['tags']);self.assertEqual(999,rules[0]['speed'])
        self.assertEqual('minecraft:pumkin',rules[15]['block'])
        for name,positions in [('minecraft:quartz_stairs',[45,47]),('minecraft:blast_furnace',[51,53]),('minecraft:blackstone_wall',[66,67])]:
            self.assertEqual(positions,[i for i,r in enumerate(rules,1) if r['block']==name])
        glass=digger_for('effect:glass_sword');self.assertEqual({'event':'weapon'},glass['on_dig'])
        self.assertEqual([25,15],[r['speed'] for r in glass['destroy_speeds']]);self.assertTrue(all(r['on_dig']=={'event':'weapon'} for r in glass['destroy_speeds']))
        self.assertEqual([100,10],[r['speed'] for r in digger_for('effect:spider_sword')['destroy_speeds']])
        self.assertEqual([999,999],[r['speed'] for r in digger_for('effect:ultra_instinct_sword')['destroy_speeds']])
        with zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as z:
            glass_item=json5.loads(z.read('Swords_B/items/glass_sword.json').decode('utf-8-sig'))['minecraft:item']
            self.assertEqual({'event':'weapon'},glass_item['components']['minecraft:weapon']['on_hit_block'])
            self.assertEqual(10,glass_item['events']['weapon']['sequence'][0]['damage']['amount'])

    def test_definition_audit_and_witch_client_variants(self):
        from build_definition_audit import collect,build
        self.assertEqual(build(),(ROOT/'docs/definition-audit.md').read_text())
        manifest_by_version={}
        for ver,filename,n,err,dups in [('1.6','SwordsAndMoreSwords.1.6.mcaddon',106,3,0),('2.8.8','swordsandmoreswords_2_8_8.mcaddon',147,1,3),('2.8.14','swordsandmoreswords-2-8-14.mcaddon',142,1,3)]:
            records,errors,duplicates,manifests=collect(filename)
            self.assertEqual((n,err,dups),(len(records),len(errors),len(duplicates)))
            grouped=collections.defaultdict(list)
            for pack,kind,ident,root,path in records:grouped[(pack,kind,ident)].append(path)
            repeated={k:v for k,v in grouped.items() if len(v)>1}
            if ver=='1.6':self.assertEqual({},repeated)
            else:self.assertEqual({('Swords_R','minecraft:client_entity','minecraft:witch'):['Swords_R/entity/witch.entity.json','Swords_R/entity/witch.v1.0.entity.json']},repeated)
            manifest_by_version[ver]={p.split('/')[0][-1]:m for p,m in manifests}
        for pack in ['B','R']:
            a,b=[manifest_by_version[v][pack] for v in ('2.8.8','2.8.14')]
            self.assertEqual(a['header']['uuid'],b['header']['uuid']);self.assertEqual(a['header']['version'],b['header']['version']);self.assertEqual(a['header']['min_engine_version'],b['header']['min_engine_version'])
            self.assertEqual([(m['type'],m['uuid'],m['version']) for m in a['modules']],[(m['type'],m['uuid'],m['version']) for m in b['modules']])
        for pack in ['B','R']:self.assertNotIn('min_engine_version',manifest_by_version['1.6'][pack]['header'])
        with zipfile.ZipFile(ROOT/'sources/swordsandmoreswords_2_8_8.mcaddon') as old,zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as new:
            paths=['Swords_R/entity/witch.entity.json','Swords_R/entity/witch.v1.0.entity.json','Swords_R/render_controllers/witch.render_controllers.json','Swords_B/entities/witch.json']
            for path in paths:self.assertEqual(old.read(path),new.read(path))
            def load(path):return json5.loads(new.read(path).decode('utf-8-sig'))
            a,b=[load(path)['minecraft:client_entity']['description'] for path in paths[:2]]
            self.assertEqual('minecraft:witch',a['identifier']);self.assertEqual(a['identifier'],b['identifier'])
            self.assertEqual('1.8.0',a['min_engine_version']);self.assertNotIn('min_engine_version',b)
            self.assertEqual(('geometry.villager.witch.v1.8','geometry.villager.witch'),(a['geometry']['default'],b['geometry']['default']))
            self.assertEqual((['controller.render.witch'],['controller.render.witch.v1.0']),(a['render_controllers'],b['render_controllers']))
            self.assertEqual(a['textures'],b['textures']);self.assertEqual('textures/entity/grass_witch',a['textures']['grass_witch'])
            self.assertIn('Swords_R/textures/entity/grass_witch.png',new.namelist());self.assertNotIn('Swords_R/textures/entity/witch.png',new.namelist())
            controllers=load(paths[2])['render_controllers'];x,y=controllers['controller.render.witch'],controllers['controller.render.witch.v1.0']
            self.assertEqual(['Texture.default','Texture.grass_witch'],x['arrays']['textures']['Array.variants']);self.assertEqual(x['arrays'],y['arrays'])
            self.assertNotIn('part_visibility',x);self.assertEqual(False,y['part_visibility'][0]['*'])
            witch=load(paths[3])['minecraft:entity']['component_groups'];self.assertEqual(0,witch['minecraft:default_witch']['minecraft:variant']['value']);self.assertEqual(1,witch['minecraft:grass_witch']['minecraft:variant']['value'])

    def test_item_icons_all_sources_decoded_and_cross_version(self):
        from build_icon_comparison import load,compare,build
        versions=[('SwordsAndMoreSwords.1.6.mcaddon','Sword_R'),('swordsandmoreswords_2_8_8.mcaddon','Swords_R'),('swordsandmoreswords-2-8-14.mcaddon','Swords_R')]
        old,mid,new=[load(filename,pack) for filename,pack in versions]
        self.assertEqual((26,42,42),(len(old),len(mid),len(new)));self.assertEqual(set(mid),set(new))
        self.assertTrue(all(mid[i]['bytes_sha256']==new[i]['bytes_sha256'] for i in new))
        common=set(old)&set(new);self.assertEqual(25,len(common))
        changed={i for i in common if compare(old[i],new[i])!='RGBA совпадают'}
        self.assertEqual({'effect:bone_sword','effect:cactus_sword','effect:ender_sword','effect:grass_sword','effect:lightning_sword','effect:quartz_sword','effect:spectral_sword','effect:wither_sword'},changed)
        self.assertEqual('различаются 240 пикс.',compare(old['effect:bone_sword'],new['effect:bone_sword']))
        self.assertEqual((16,16),old['effect:wither_sword']['size']);self.assertEqual((128,128),new['effect:wither_sword']['size'])
        self.assertIn('effect:sword_of_time',old);self.assertNotIn('effect:sword_of_time',new);self.assertIn('effect:time_sword',new)
        self.assertEqual(build(),(ROOT/'docs/icon-comparison.md').read_text())

    def test_exact_cross_version_item_components_and_ice_substitution(self):
        from build_item_version_matrix import load,build
        old=load('SwordsAndMoreSwords.1.6.mcaddon','Sword_B');mid=load('swordsandmoreswords_2_8_8.mcaddon','Swords_B');new=load('swordsandmoreswords-2-8-14.mcaddon','Swords_B')
        self.assertEqual((26,42,42),(len(old),len(mid),len(new)));self.assertEqual(set(mid),set(new))
        common=set(old)&set(new);self.assertEqual(25,len(common));self.assertEqual({'effect:sword_of_time'},set(old)-set(new));self.assertEqual(17,len(set(new)-set(old)))
        changed_damage=[];changed_durability=[];changed_offhand=[]
        for ident in common:
            a=old[ident]['item']['components'];b=new[ident]['item']['components']
            if a.get('minecraft:damage')!=b.get('minecraft:damage'):changed_damage.append(ident)
            if a.get('minecraft:durability')!=b.get('minecraft:durability'):changed_durability.append(ident)
            if a.get('minecraft:allow_off_hand')!=b.get('minecraft:allow_off_hand'):changed_offhand.append(ident)
        self.assertEqual((14,6,24),(len(changed_damage),len(changed_durability),len(changed_offhand)))
        self.assertNotIn('effect:glowstone_sword',changed_offhand)
        self.assertEqual(['effect:ice_sword'],[i for i in sorted(mid) if mid[i]['raw']!=new[i]['raw']])
        a=mid['effect:ice_sword']['raw'];b=new['effect:ice_sword']['raw']
        self.assertEqual(40,a.count(b'effect99:fake_ice'));self.assertEqual(40,b.count(b'frosted_ice'));self.assertEqual(a.replace(b'effect99:fake_ice',b'frosted_ice'),b)
        with zipfile.ZipFile(ROOT/'sources/swordsandmoreswords_2_8_8.mcaddon') as x,zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as y:
            a=x.read('Swords_B/entities/player.json');b=y.read('Swords_B/entities/player.json')
            self.assertEqual(11,a.count(b'effect99:fake_ice'));self.assertEqual(11,b.count(b'frosted_ice'));self.assertEqual(a.replace(b'effect99:fake_ice',b'frosted_ice'),b)
        self.assertEqual(build(),(ROOT/'docs/item-version-matrix.md').read_text())

    def test_ice_on_use_selector_geometry_and_potential_player_overlap(self):
        from build_ice_geometry import collect,build
        from itertools import product
        item,rows,tail=collect();self.assertEqual(40,len(rows));self.assertEqual(3,len(tail))
        self.assertEqual(build(),(ROOT/'docs/ice-geometry-index.md').read_text())
        self.assertNotIn('type=!player',rows[0]['selector']);self.assertIn('family=!fish',rows[0]['selector']);self.assertIn('family=!effect99_entities',rows[0]['selector']);self.assertIn('rm=2,r=12',rows[0]['selector'])
        self.assertEqual('@e[type=player,rm=3,r=12]',rows[39]['selector']);self.assertEqual(rows[0]['bounds'],rows[39]['bounds']);self.assertEqual(36,rows[0]['volume'])
        self.assertEqual(45,rows[1]['volume']);self.assertEqual(125,rows[2]['volume']);self.assertEqual(27,rows[3]['volume']);self.assertEqual([27,1,27,1],[r['volume'] for r in rows[4:8]])
        self.assertEqual([648,294,27,1],[r['volume'] for r in rows[35:39]])
        def pts(row):return set(product(*(range(a,b+1) for a,b in row['bounds'])))
        for outer,inner,result in [(2,3,98),(4,5,26),(6,7,26),(35,36,354),(37,38,26)]:
            self.assertTrue(pts(rows[inner])<=pts(rows[outer]));self.assertEqual(result,len(pts(rows[outer])-pts(rows[inner])))
        self.assertEqual(125,rows[33]['volume'])
        self.assertEqual({'type':'durability','amount':6,'target':'self'},item['events']['on_use']['sequence'][1]['damage'])
        self.assertEqual('air 0 replace frosted_ice 0',rows[38]['operation']);self.assertEqual('air 0 replace frosted_ice',rows[36]['operation'])

    def test_legacy_ice_controller_geometry_and_cross_version_loot_model(self):
        from build_legacy_ice_matrix import collect_legacy,build
        from fractions import Fraction
        states,rows=collect_legacy();self.assertEqual(build(),(ROOT/'docs/ice-target-matrix-1.6.md').read_text())
        self.assertEqual({'ice':'(1.0)'},states['default']['transitions'][0]);self.assertEqual({'default':'(1.0)'},states['ice']['transitions'][0]);self.assertEqual(['/Effect99'],states['default']['on_entry'])
        cmds=states['ice']['on_entry'];self.assertEqual(26,len(cmds));self.assertTrue(cmds[0].endswith('ice 0 replace water 0'));self.assertTrue(cmds[1].endswith('ice 0 replace flowing_water 0'))
        self.assertIn('detect ~ ~ ~ ice 0 tp @s ~ ~ ~',cmds[16]);self.assertEqual('/scoreboard players set @a swords 2',cmds[25]);self.assertEqual(22,len(rows))
        target={r['type']:r for r in rows};self.assertEqual(22,len(target));self.assertEqual((45,100,27,36),tuple(target[t]['volume'] for t in ('enderman','ravager','silverfish','slime')))
        with zipfile.ZipFile(ROOT/'sources/SwordsAndMoreSwords.1.6.mcaddon') as z:
            def rd(p):return json5.loads(z.read('Sword_B/'+p).decode('utf-8-sig'))
            player=rd('entities/player.json')['minecraft:entity'];group=player['component_groups']['minecraft:ice_sword']['minecraft:spawn_entity'][0]
            self.assertEqual({'min_wait_time':0,'max_wait_time':0,'spawn_entity':'entity:ice','num_to_spawn':1,'single_use':True},group)
            self.assertIn('minecraft:ice_sword',player['events']['minecraft:event_normal_player']['remove']['component_groups'])
            helper=rd('entities/ice.json')['minecraft:entity'];self.assertEqual(['despawnear'],helper['components']['minecraft:type_family']['family']);self.assertEqual({'width':0.0,'height':0.0},helper['components']['minecraft:collision_box'])
            recipe=rd('recipes/ice_sword.json')['minecraft:recipe_shaped'];self.assertEqual(['F','F','E'],recipe['pattern']);self.assertEqual('minecraft:blue_ice',recipe['key']['F']['item']);self.assertEqual('effect:ice_sword',recipe['result']['item'])
        paths=['Swords_B/loot_tables/chests/igloo_chest.json','Swords_B/loot_tables/chests/village/village_snowy_house.json']
        with zipfile.ZipFile(ROOT/'sources/swordsandmoreswords_2_8_8.mcaddon') as a,zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as b:
            for path,total,weight,lo,hi,estimate in zip(paths,[64,57],[1,4],[2,3],[8,8],[7.52629152685,32.46125191034]):
                self.assertEqual(a.read(path),b.read(path));pool=json5.loads(b.read(path).decode('utf-8-sig'))['pools'][0]
                self.assertEqual({'min':lo,'max':hi},pool['rolls']);self.assertEqual(total,sum(e.get('weight',1) for e in pool['entries']))
                matches=[e for e in pool['entries'] if e.get('name')=='effect:ice_sword'];self.assertEqual(1,len(matches));self.assertEqual(weight,matches[0]['weight'])
                p=Fraction(weight,total);prob=sum((1-(1-p)**n for n in range(lo,hi+1)),Fraction())/(hi-lo+1)
                self.assertAlmostEqual(estimate,float(prob)*100,places=8)

    def test_lightning_legacy_targets_and_modern_coordinates(self):
        from build_lightning_patterns import collect,build
        from fractions import Fraction
        states,targets,item,points=collect();self.assertEqual(build(),(ROOT/'docs/lightning-patterns.md').read_text())
        self.assertEqual(26,len(targets));self.assertEqual(len(targets),len(set(targets)));self.assertIn('zombie_pigman',targets);self.assertIn('evocation_fang',targets);self.assertNotIn('player',targets)
        self.assertEqual(states['default']['on_entry'],states['lightning']['on_entry']);self.assertEqual({'lightning':'(1.0)'},states['default']['transitions'][0]);self.assertEqual({'default':'(1.0)'},states['lightning']['transitions'][0])
        coords={xyz for _,xyz in points};self.assertEqual(41,len(coords));expected={(0,2,0)}
        for n in (7,14,28,34,42):expected.update({(n,0,0),(-n,0,0),(0,0,n),(0,0,-n)})
        for n in (6,12,24,30,38):expected.update((sx*n,0,sz*n) for sx in (-1,1) for sz in (-1,1))
        self.assertEqual(expected,coords);self.assertEqual(2888,max(x*x+z*z for x,y,z in coords))
        ev=item['events']['on_use'];self.assertEqual({'type':'durability','amount':9,'target':'self'},ev['damage']);self.assertNotIn('sequence',ev)
        self.assertEqual([15,85],[r['weight'] for r in item['events']['weapon']['sequence'][1]['randomize']])
        with zipfile.ZipFile(ROOT/'sources/SwordsAndMoreSwords.1.6.mcaddon') as z:
            recipe=json5.loads(z.read('Sword_B/recipes/lightning_sword.json').decode('utf-8-sig'))['minecraft:recipe_shaped'];self.assertEqual(['F','F','E'],recipe['pattern']);self.assertEqual('minecraft:netherstar',recipe['key']['E']['item'])
            player=json5.loads(z.read('Sword_B/entities/player.json').decode('utf-8-sig'))['minecraft:entity'];g=player['component_groups']['minecraft:lightning_sword']['minecraft:spawn_entity'][0];self.assertEqual(('entity:lightning',0,0,1,True),(g['spawn_entity'],g['min_wait_time'],g['max_wait_time'],g['num_to_spawn'],g['single_use']))
        with zipfile.ZipFile(ROOT/'sources/swordsandmoreswords_2_8_8.mcaddon') as a,zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as b:
            p='Swords_B/entities/lightning_bolt.json';self.assertEqual(a.read(p),b.read(p));lightning=json5.loads(b.read(p).decode('utf-8-sig'))['minecraft:entity'];self.assertEqual([80,20],[r['weight'] for r in lightning['events']['spawn_centella']['randomize']])
            self.assertEqual([0,0],lightning['component_groups']['spawn_centella']['minecraft:timer']['time']);self.assertEqual('summon entity:centella ~ ~1 ~',lightning['events']['spawn_centella']['randomize'][1]['run_command']['command'][0])
        self.assertAlmostEqual(99.989366176,float(1-Fraction(4,5)**41)*100,places=8)

    def test_sea_legacy_controller_and_modern_group_cleanup(self):
        from fractions import Fraction
        with zipfile.ZipFile(ROOT/'sources/SwordsAndMoreSwords.1.6.mcaddon') as z:
            def rd(p):return json5.loads(z.read('Sword_B/'+p).decode('utf-8-sig'))
            states=rd('animation_controllers/sea_sword.json')['animation_controllers']['controller.animation.sea']['states'];self.assertEqual(states['default']['on_entry'],states['sea']['on_entry'])
            self.assertEqual(['/effect @e[type=guardian,r=6] fatal_poison 5 0 true','/effect @e[type=drowned,r=6] fatal_poison 5 0 true','/effect @p conduit_power 16 0 true','/scoreboard players set @a swords 2'],states['sea']['on_entry'])
            recipe=rd('recipes/sea_sword.json')['minecraft:recipe_shaped'];self.assertEqual(['F','F','E'],recipe['pattern']);self.assertEqual('minecraft:heart_of_the_sea',recipe['key']['F']['item']);self.assertEqual('minecraft:prismarine_shard',recipe['key']['E']['item'])
            group=rd('entities/player.json')['minecraft:entity']['component_groups']['minecraft:sea_sword']['minecraft:spawn_entity'][0];self.assertEqual(('entity:sea',0,0,1,True),(group['spawn_entity'],group['min_wait_time'],group['max_wait_time'],group['num_to_spawn'],group['single_use']))
        players=[]
        with zipfile.ZipFile(ROOT/'sources/swordsandmoreswords_2_8_8.mcaddon') as a,zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as b:
            loot='Swords_B/loot_tables/chests/buriedtreasure.json';self.assertEqual(a.read(loot),b.read(loot));pools=json5.loads(b.read(loot).decode('utf-8-sig'))['pools'];self.assertEqual(1,pools[0]['rolls']);self.assertEqual('minecraft:heart_of_the_sea',pools[0]['entries'][0]['name'])
            pool=pools[1];self.assertEqual({'min':5,'max':12},pool['rolls']);self.assertTrue(all('weight' in x for x in pool['entries']));self.assertEqual((19,219),(len(pool['entries']),sum(x['weight'] for x in pool['entries'])));self.assertEqual(15,[x for x in pool['entries'] if x.get('name')=='effect:sea_sword'][0]['weight'])
            p=Fraction(15,219);prob=sum((1-(1-p)**n for n in range(5,13)),Fraction())/8;self.assertAlmostEqual(44.5623359057,float(prob)*100,places=8)
            for z in (a,b):
                player=json5.loads(z.read('Swords_B/entities/player.json').decode('utf-8-sig'))['minecraft:entity'];players.append(player)
                names=[]
                for path in z.namelist():
                    if not path.endswith(('.json','.mcfunction','.js')):continue
                    try:raw=z.read(path).decode('utf-8-sig')
                    except UnicodeDecodeError:continue
                    if 'mermaid_movement_out_water' in raw:names.append((path,raw.count('mermaid_movement_out_water')))
                self.assertEqual([('Swords_B/entities/player.json',2)],names)
        for p in players:
            ev=p['events']['minecraft:sea_sword']['sequence'];self.assertEqual({'test':'in_water','operator':'!='},ev[0]['filters']);self.assertEqual({'test':'in_water'},ev[2]['filters'])
            self.assertEqual(['mermaid_movement_out_water'],ev[0]['add']['component_groups']);self.assertEqual(['mermaid_movement_in_water'],ev[2]['add']['component_groups'])
            stop=p['events']['stop_sea_sword_event']['sequence'][0];self.assertEqual(['minecraft:sea_sword','mermaid_movement_in_water'],stop['remove']['component_groups']);self.assertEqual(['minecraft:default_player'],stop['add']['component_groups'])
            self.assertEqual(0.06,p['component_groups']['mermaid_movement_out_water']['minecraft:movement']['value']);self.assertEqual(0.07,p['component_groups']['mermaid_movement_in_water']['minecraft:underwater_movement']['value'])
            default=p['component_groups']['minecraft:default_player'];self.assertEqual((0.1,0.02),(default['minecraft:movement']['value'],default['minecraft:underwater_movement']['value']))
        for key in ('minecraft:sea_sword','stop_sea_sword_event','sea_sword_sound'):self.assertEqual(players[0]['events'][key],players[1]['events'][key])
        for key in ('minecraft:sea_sword','mermaid_movement_out_water','mermaid_movement_in_water'):self.assertEqual(players[0]['component_groups'][key],players[1]['component_groups'][key])

    def test_legacy_fire_magma_spider_targets_and_world_changes(self):
        from build_legacy_fire_web_matrix import collect,build
        data=collect();self.assertEqual(build(),(ROOT/'docs/fire-web-targets-1.6.md').read_text())
        f=data['fire'][1];m=data['magma'][1];s=data['spider'][1]
        self.assertEqual((31,21,25,37),(len(f),len(m),len(s),len(set(f)|set(m)|set(s))));self.assertTrue(set(m)<=set(f))
        self.assertEqual({'cow','pig','chicken','horse','rabbit','sheep','fox','bat','polar_bear','villager'},set(f)-set(m))
        self.assertNotIn('spider',s);self.assertNotIn('cave_spider',s);self.assertIn('tnt',s);self.assertIn('evocation_fang',s)
        for name,length in [('fire',39),('magma',24),('spider',31)]:
            states=data[name][0];self.assertEqual(states['default']['on_entry'],states[name]['on_entry']);self.assertEqual(length,len(states['default']['on_entry']));self.assertEqual('/scoreboard players set @a swords 2',states['default']['on_entry'][-1])
        fire=data['fire'][0]['default']['on_entry'];self.assertEqual('/execute @p ~ ~ ~ detect ~ ~ ~ air 0 setblock ~ ~ ~ fire',fire[1])
        self.assertEqual(['snow_layer','ice','blue_ice','packed_ice','snow'],[c.split(' replace ')[1] for c in fire[2:7]])
        self.assertTrue(all('fill ~3 ~3 ~3 ~-3 ~-3 ~-3' in c for c in fire[2:7]));self.assertEqual(343,7**3)
        magma=data['magma'][0]['default']['on_entry'];self.assertEqual('/execute @p ~ ~ ~ fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 magma 0 replace lava',magma[1])
        spider=data['spider'][0]['default']['on_entry'];self.assertEqual('/effect @p poison 0 0 true',spider[0]);self.assertIn('@e[r=6,type=spider] slowness 1 128 true',spider[3]);self.assertIn('@e[r=6,type=cave_spider] slowness 1 128 true',spider[4])
        with zipfile.ZipFile(ROOT/'sources/SwordsAndMoreSwords.1.6.mcaddon') as z:
            def rd(path):return json5.loads(z.read('Sword_B/'+path).decode('utf-8-sig'))
            player=rd('entities/player.json')['minecraft:entity']
            for name in ('fire','magma','spider'):
                group=player['component_groups']['minecraft:'+name+'_sword']['minecraft:spawn_entity'][0];self.assertEqual(('entity:'+name,0,0,1,True),(group['spawn_entity'],group['min_wait_time'],group['max_wait_time'],group['num_to_spawn'],group['single_use']))
            for name in ('fire','spider'):
                recipe=rd('recipes/'+name+'_sword.json')['minecraft:recipe_shaped'];self.assertTrue(any('#' in row for row in recipe['pattern']));self.assertNotIn('#',recipe['key'])
            self.assertEqual('minecraft:magma',rd('recipes/magma_sword.json')['minecraft:recipe_shaped']['key']['F']['item'])

    def test_jungle_vine_order_block_groups_and_loot_assumptions(self):
        from build_jungle_vine_index import collect,build,parse
        from fractions import Fraction
        states,old,new,og,ng=collect();self.assertEqual(build(),(ROOT/'docs/jungle-vine-index.md').read_text());self.assertEqual((144,148,36,37),(len(old),len(new),len(og),len(ng)))
        self.assertEqual(['/commands'],states['default']['on_entry']);self.assertEqual({'jungle':'(1.0)'},states['default']['transitions'][0]);self.assertEqual({'default':'(1.0)'},states['jungle']['transitions'][0]);self.assertEqual('/scoreboard players set @a swords 2',states['jungle']['on_entry'][-1])
        self.assertEqual([x.removeprefix('/') for x in old],[x for x in new if (parse(x)['block'],parse(x)['data'])!=('leaves','11')]);self.assertEqual([53,54,55,56],[i for i,x in enumerate(new,1) if (parse(x)['block'],parse(x)['data'])==('leaves','11')])
        def first(commands,neighbors):
            for no,cmd in enumerate(commands,1):
                row=parse(cmd);direction=row['direction'];seen=neighbors.get(direction[:3])
                if seen==(row['block'],row['data']):return no,direction[3]
        example={('~1','~1','~'):('stone','0'),('~-1','~1','~'):('log','0')};self.assertEqual((2,'2'),first(old,example));self.assertEqual((2,'2'),first(new,example))
        example={('~1','~1','~'):('leaves','11'),('~-1','~1','~'):('leaves2','0')};self.assertEqual((54,'2'),first(old,example));self.assertEqual((53,'8'),first(new,example))
        with zipfile.ZipFile(ROOT/'sources/SwordsAndMoreSwords.1.6.mcaddon') as z:
            def rd(p):return json5.loads(z.read('Sword_B/'+p).decode('utf-8-sig'))
            recipe=rd('recipes/jungle_sword.json')['minecraft:recipe_shaped'];self.assertEqual(['F','F','E'],recipe['pattern']);self.assertEqual({'item':'minecraft:leaves','data':3},recipe['key']['F']);self.assertEqual({'item':'minecraft:sapling','data':3},recipe['key']['E'])
            group=rd('entities/player.json')['minecraft:entity']['component_groups']['minecraft:jungle_sword']['minecraft:spawn_entity'][0];self.assertEqual(('entity:jungle',0,0,1,True),(group['spawn_entity'],group['min_wait_time'],group['max_wait_time'],group['num_to_spawn'],group['single_use']))
        with zipfile.ZipFile(ROOT/'sources/swordsandmoreswords_2_8_8.mcaddon') as a,zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as b:
            paths=['Swords_B/loot_tables/chests/jungle_temple.json','Swords_B/loot_tables/gameplay/fishing.json','Swords_B/loot_tables/gameplay/jungle_fishing.json','Swords_B/loot_tables/gameplay/fishing/treasure.json','Swords_B/blocks/sapling3.json','Swords_B/entities/parrot.json']
            for path in paths:self.assertEqual(a.read(path),b.read(path))
            player1=json5.loads(a.read('Swords_B/entities/player.json').decode('utf-8-sig'))['minecraft:entity'];player2=json5.loads(b.read('Swords_B/entities/player.json').decode('utf-8-sig'))['minecraft:entity']
            for key in ('minecraft:jungle_sword','stop_jungle_sword_event'):self.assertEqual(player1['events'][key],player2['events'][key])
            group=player2['component_groups']['minecraft:jungle_sword'];self.assertEqual({'value':8,'max':8},group['minecraft:health']);self.assertEqual(group,player1['component_groups']['minecraft:jungle_sword'])
            sap=json5.loads(b.read(paths[4]).decode('utf-8-sig'))['minecraft:block'];self.assertEqual(['playsound dig.grass @a[r=12] ~ ~ ~','fill ~ ~ ~ ~ ~ ~ sapling 3'],sap['events']['on_placed']['sequence'][0]['run_command']['command'])
            parrot=json5.loads(b.read(paths[5]).decode('utf-8-sig'))['minecraft:entity'];self.assertEqual({'speed_multiplier':1.0,'items':['effect:jungle_sword']},parrot['components']['minecraft:behavior.tempt'])
            pool=json5.loads(b.read(paths[0]).decode('utf-8-sig'))['pools'][0];self.assertEqual({'min':2,'max':6},pool['rolls']);self.assertEqual((13,457),(len(pool['entries']),sum(x['weight'] for x in pool['entries'])));self.assertEqual(16,[e['weight'] for e in pool['entries'] if e.get('name')=='effect:jungle_sword'][0])
            prob=sum((1-(1-Fraction(16,457))**n for n in range(2,7)),Fraction())/5;self.assertAlmostEqual(13.1757571099,float(prob)*100,places=8)
            for path in paths[1:3]:
                entries=json5.loads(b.read(path).decode('utf-8-sig'))['pools'][0]['entries'];self.assertEqual([10,5,85],[e['weight'] for e in entries]);self.assertEqual([-2,2,-1],[e['quality'] for e in entries]);self.assertEqual('loot_tables/gameplay/fishing/treasure.json',entries[1]['name'])
            treasure=json5.loads(b.read(paths[3]).decode('utf-8-sig'))['pools'][0];self.assertEqual(41,sum(e['weight'] for e in treasure['entries']));self.assertEqual(5,[e['weight'] for e in treasure['entries'] if e.get('name')=='effect:jungle_sword'][0])

    def test_grass_selector_intersections_and_helper_sources(self):
        from build_grass_selector_samples import collect,build,accepts
        stages=collect();self.assertEqual(build(),(ROOT/'docs/grass-selector-samples.md').read_text());self.assertEqual(7,len(stages));names=[row[0].split(':')[0] for row in stages];self.assertEqual(['P','W','T','S','C','R','Q'],names)
        sel={name:row[1] for name,row in zip(names,stages)}
        def v(stage,typ,families=(),tagged=False):return accepts(sel[stage],typ,set(families),{'grass'} if tagged else set())
        self.assertFalse(v('P','player',['player']));self.assertTrue(v('W','player',['player']));self.assertTrue(v('T','player',['player']))
        self.assertTrue(v('P','entity:shulker_shield',['effect99_entities','player','shulker_sword']));self.assertFalse(v('W','entity:shulker_shield',['effect99_entities','player','shulker_sword']))
        self.assertTrue(v('P','witch',['witch','monster','mob','grass_witch']));self.assertFalse(v('W','witch',['witch','monster','mob','grass_witch']));self.assertFalse(v('T','witch',['witch','monster','mob','grass_witch']))
        self.assertFalse(v('P','item'));self.assertFalse(v('W','item'));self.assertTrue(v('T','item'));self.assertFalse(v('T','arrow'));self.assertTrue(v('C','arrow',tagged=True));self.assertFalse(v('C','arrow'))
        with zipfile.ZipFile(ROOT/'sources/SwordsAndMoreSwords.1.6.mcaddon') as z:
            def rd(path):return json5.loads(z.read('Sword_B/'+path).decode('utf-8-sig'))
            states=rd('animation_controllers/grass_sword.json')['animation_controllers']['controller.animation.grass']['states'];self.assertEqual(states['default']['on_entry'],states['grass']['on_entry']);self.assertEqual(4,len(states['grass']['on_entry']));self.assertIn('@a',states['grass']['on_entry'][0]);self.assertIn('@e[r=10]',states['grass']['on_entry'][2]);self.assertEqual('/scoreboard players set @a swords 2',states['grass']['on_entry'][3])
            recipe=rd('recipes/grass_sword.json')['minecraft:recipe_shaped'];self.assertEqual(['F','F','E'],recipe['pattern']);self.assertEqual('minecraft:grass',recipe['key']['F']['item'])
            p=rd('entities/player.json')['minecraft:entity'];group=p['component_groups']['minecraft:grass_sword']['minecraft:spawn_entity'][0];self.assertEqual(('entity:grass',0,0,1,True),(group['spawn_entity'],group['min_wait_time'],group['max_wait_time'],group['num_to_spawn'],group['single_use']))
        with zipfile.ZipFile(ROOT/'sources/swordsandmoreswords_2_8_8.mcaddon') as a,zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as b:
            paths=['Swords_B/entities/grass.json','Swords_B/entities/witch.json','Swords_B/structures/grass_sword.mcstructure','Swords_B/items/grass_sword.json']
            for path in paths:self.assertEqual(a.read(path),b.read(path))
            grass=json5.loads(b.read(paths[0]).decode('utf-8-sig'))['minecraft:entity'];self.assertEqual([1.08,1.08],grass['component_groups']['grass_sword']['minecraft:timer']['time']);self.assertEqual([0.52,0.52],grass['component_groups']['start_despawn']['minecraft:timer']['time'])
            skill=grass['events']['grass_sword_skill'];self.assertIn('run_command',skill);self.assertIn('add',skill);self.assertNotIn('sequence',skill);self.assertEqual([50,50],[x['weight'] for x in grass['events']['despawn']['sequence'][1]['randomize']])
            witch=json5.loads(b.read(paths[1]).decode('utf-8-sig'))['minecraft:entity'];self.assertEqual([80,20],[x['weight'] for x in witch['events']['minecraft:entity_spawned']['randomize']]);self.assertEqual([80,20],[x['weight'] for x in witch['events']['grass_sword']['randomize']]);self.assertEqual({'filters':{},'event':'grass_witch_skill'},witch['component_groups']['grass_witch']['minecraft:environment_sensor']['triggers'][0])
            obj=nbtlib.File.parse(io.BytesIO(b.read(paths[2])),byteorder='little')['structure']['entities'][0];self.assertEqual(('minecraft:item','effect:grass_sword',1,0,196),(str(obj['identifier']),str(obj['Item']['Name']),int(obj['Item']['Count']),int(obj['Item']['Damage']),int(obj['Age'])));self.assertEqual([],list(obj['Tags']))
            player=json5.loads(b.read('Swords_B/entities/player.json').decode('utf-8-sig'))['minecraft:entity'];self.assertEqual(['wolf','wolf_sword','complete_wolf_transformation','monster'],player['component_groups']['complete_wolf_transformation']['minecraft:type_family']['family']);self.assertEqual([0.2,0.2],player['component_groups']['minecraft:grass_sword']['minecraft:timer']['time'])
            shield=json5.loads(b.read('Swords_B/entities/shulker_shield.json').decode('utf-8-sig'))['minecraft:entity'];self.assertEqual('entity:shulker_shield',shield['description']['identifier']);self.assertEqual(['effect99_entities','player','shulker_sword'],shield['components']['minecraft:type_family']['family'])

    def test_weapon_event_distribution_model_and_hook_coverage(self):
        from build_weapon_event_index import collect,build,distribution
        from build_quick_reference import read_items
        from fractions import Fraction
        items=collect();self.assertEqual(42,len(items));self.assertEqual(build(),(ROOT/'docs/weapon-event-index.md').read_text())
        old=read_items('SwordsAndMoreSwords.1.6.mcaddon','Sword_B');self.assertEqual(26,len(old));self.assertTrue(all('minecraft:weapon' not in item['components'] for _,item in old.values()))
        empty=[];missing=[];hooks={};event_count=0
        for ident,(_,item) in items.items():
            c=item['components']
            if 'minecraft:weapon' not in c:missing.append(ident);continue
            if not c['minecraft:weapon']:empty.append(ident);continue
            weapon=c['minecraft:weapon'];hooks[ident]=set(weapon);event=item['events']['weapon'];event_count+=1
            self.assertNotIn('"filters"',json.dumps(event));self.assertTrue(all(v=={'event':'weapon'} for v in weapon.values()))
            self.assertEqual(Fraction(1),sum(distribution(event).values(),Fraction()))
        self.assertEqual({'effect:bedrock_stick','effect:bedrock_sword'},set(empty));self.assertEqual({'effect:quartz_diamond','effect:silver_ingot'},set(missing));self.assertEqual(38,event_count)
        three={'on_hurt_entity','on_not_hurt_entity','on_hit_block'};self.assertEqual((21,17),(sum(h==three for h in hooks.values()),sum(h=={'on_hurt_entity'} for h in hooks.values())))
        expected={
            'effect:bee_sword':{1:Fraction(3,10),2:Fraction(7,10)},
            'effect:blaze_sword':{1:Fraction(3,20),2:Fraction(17,20)},
            'effect:obsidian_sword':{1:Fraction(11,20),2:Fraction(3,10),3:Fraction(3,20)},
            'effect:time_sword':{1:Fraction(9,10),16:Fraction(3,50),32:Fraction(3,100),64:Fraction(1,100)},
            'effect:nether_star_sword':{1:Fraction(9999,10000),0:Fraction(1,10000)},
            'effect:spectral_sword':{1:Fraction(99,100),0:Fraction(1,100)},
            'effect:quartz_diamond_stick':{0:Fraction(1)},
            'effect:quartz_sword':{10:Fraction(1)},
        }
        for ident,result in expected.items():self.assertEqual(result,distribution(items[ident][1]['events']['weapon']))
        self.assertEqual(Fraction(173,50),sum(k*v for k,v in expected['effect:time_sword'].items()));self.assertIn('damage @s 3 magic',json.dumps(items['effect:quartz_diamond_stick'][1]['events']['weapon']))
        with self.assertRaises(ValueError):distribution({'filters':{},'damage':{'type':'durability','target':'self','amount':1}})
        with self.assertRaises(ValueError):distribution({'randomize':[{'shoot':{}}]})

    def test_bee_sword_flowers_summon_and_attack_event_are_distinct(self):
        from build_quick_reference import read_items
        self.assertNotIn('effect:bee_sword',read_items('SwordsAndMoreSwords.1.6.mcaddon','Sword_B'))
        with zipfile.ZipFile(ROOT/'sources/swordsandmoreswords_2_8_8.mcaddon') as a,zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as b:
            paths=['Swords_B/items/bee_sword.json','Swords_B/entities/bee_entity.json','Swords_B/entities/bee.json','Swords_B/loot_tables/bee_sword.json']
            for path in paths:self.assertEqual(a.read(path),b.read(path))
            item=json5.loads(b.read(paths[0]).decode('utf-8-sig'))['minecraft:item'];weapon=item['events']['weapon']['sequence'];self.assertEqual(1,weapon[0]['damage']['amount']);self.assertEqual([30,70],[x['weight'] for x in weapon[1]['randomize']]);self.assertEqual('entity:bee_sword',weapon[1]['randomize'][0]['shoot']['projectile'])
            summoned=json5.loads(b.read(paths[1]).decode('utf-8-sig'))['minecraft:entity'];c=summoned['components'];self.assertEqual('entity:bee_sword',summoned['description']['identifier']);self.assertEqual(['bee','mob','arthropod'],c['minecraft:type_family']['family']);self.assertNotIn('countdown_to_perish_event',summoned['events']);self.assertEqual(['despawn'],list(summoned['events']))
            self.assertEqual(['tp @s ~ -103 ~'],summoned['events']['despawn']['run_command']['command']);self.assertEqual([6,8],c['minecraft:timer']['time']);self.assertTrue(c['minecraft:timer']['looping']);self.assertTrue(c['minecraft:timer']['randomInterval'])
            self.assertEqual((1024,16,10,True),(c['minecraft:follow_range']['value'],c['minecraft:behavior.nearest_attackable_target']['within_radius'],c['minecraft:behavior.nearest_attackable_target']['entity_types'][0]['max_dist'],c['minecraft:behavior.nearest_attackable_target']['must_see']))
            self.assertEqual('monster',c['minecraft:behavior.nearest_attackable_target']['entity_types'][0]['filters']['value']);self.assertEqual('player',c['minecraft:damage_sensor']['triggers'][0]['on_damage']['filters']['value'])
            ordinary=json5.loads(b.read(paths[2]).decode('utf-8-sig'))['minecraft:entity'];attack=ordinary['component_groups']['angry_bee']['minecraft:behavior.melee_attack'];self.assertTrue(attack['attack_once']);self.assertEqual('countdown_to_perish_event',attack['on_attack']['event'])
            steps=ordinary['events']['countdown_to_perish_event']['sequence'];self.assertEqual([2,98],[x['weight'] for x in steps[0]['randomize']]);self.assertEqual('bee_sword',steps[0]['randomize'][0]['filters']['value']);self.assertIn('collect_nectar',steps[1]['remove']['component_groups']);self.assertNotIn('collect_nectar',ordinary['component_groups'])
            loot=json5.loads(b.read(paths[3]).decode('utf-8-sig'))['pools'][0];self.assertEqual(1,loot['rolls']);self.assertEqual([{'type':'item','name':'effect:bee_sword','weight':1}],loot['entries'])
            players=[json5.loads(z.read('Swords_B/entities/player.json').decode('utf-8-sig'))['minecraft:entity'] for z in (a,b)];self.assertEqual(players[0]['events']['bee_sword_flower'],players[1]['events']['bee_sword_flower'])
            player=players[1];timer=player['component_groups']['minecraft:bee_sword']['minecraft:timer'];self.assertEqual([3,8],timer['time']);self.assertTrue(timer['looping']);self.assertTrue(timer['randomInterval'])
            flower=player['events']['bee_sword_flower']['randomize'];self.assertEqual([1]*12,[x['weight'] for x in flower]);cmds=[x['run_command']['command'][0] for x in flower];self.assertEqual([f'execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower {n}' for n in range(11)]+['execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ yellow_flower 0'],cmds)
            wolf=player['component_groups']['complete_wolf_transformation']['minecraft:type_family']['family'];self.assertIn('monster',wolf);self.assertNotIn('player',wolf)

    def test_local_markdown_document_links_and_heading_fragments(self):
        from build_quick_reference import slug
        from urllib.parse import unquote
        docs=ROOT/'docs';files=sorted(docs.glob('*.md'));self.assertGreaterEqual(len(files),40)
        anchors={};checked=0
        for source in files:
            for target,fragment in re.findall(r'\]\(([^()#\s]+\.md)(?:#([^()\s]+))?\)',source.read_text(encoding='utf-8')):
                if target.startswith(('http:','https:','mailto:')):continue
                checked+=1;destination=source.parent/unquote(target)
                self.assertTrue(destination.is_file(),f'{source.name}: missing {target}')
                if fragment:
                    if destination not in anchors:
                        headings=re.findall(r'^#{1,6} (.*)$',destination.read_text(encoding='utf-8'),re.M)
                        anchors[destination]={slug(h) for h in headings}
                    self.assertIn(unquote(fragment),anchors[destination],f'{source.name}: missing {target}#{fragment}')
        self.assertGreaterEqual(checked,500)

    def test_direct_loot_selection_model_is_conditional_and_reproducible(self):
        from build_loot_selection_model import collect,build,one_or_more,roll_range,weight,MISSING
        from fractions import Fraction
        tables,direct,parents,rows=collect();self.assertEqual((60,29,2,27,25),(len(tables),len(direct),len(parents),len(rows),len({(r['path'],r['pool']) for r in rows})));self.assertEqual(build(),(ROOT/'docs/loot-selection-model.md').read_text())
        lookup={(r['path'].split('loot_tables/',1)[1],r['pool'],r['id']):r for r in rows}
        quartz=lookup['blocks/quartz_diamond_ore.json',0,'effect:quartz_diamond'];self.assertEqual([0,1,2],quartz['indices']);self.assertEqual((100,100,Fraction(1)),(quartz['target_weight'],quartz['total_weight'],quartz['prob']));self.assertEqual([1,2,4],[x[0]['count']['max'] for x in quartz['functions']])
        outpost=lookup['chests/pillager_outpost.json',3,'effect:emerald_sword'];self.assertEqual((3,28,1),(outpost['target_weight'],outpost['total_weight'],outpost['missing']));self.assertEqual({'min':0,'max':1},outpost['functions'][0][0]['count']);self.assertEqual(one_or_more(Fraction(3,28),2,3),outpost['prob'])
        snowy=lookup['chests/village/village_snowy_house.json',0,'effect:ice_sword'];self.assertEqual((4,57,4),(snowy['target_weight'],snowy['total_weight'],snowy['missing']));self.assertEqual({'type':'minecraft:chest'},snowy['table_other']);self.assertAlmostEqual(32.46125191,float(snowy['prob'])*100,places=7)
        sea=lookup['chests/buriedtreasure.json',1,'effect:sea_sword'];self.assertEqual((15,219,5,12),(sea['target_weight'],sea['total_weight'],sea['lo'],sea['hi']));self.assertAlmostEqual(44.56233591,float(sea['prob'])*100,places=7)
        blaze=lookup['entities/blaze.json',1,'effect:blaze_sword'];self.assertEqual(Fraction(1),blaze['prob']);self.assertEqual('minecraft:snow_golem',blaze['conditions'][0]['entity_type']);self.assertEqual(0.025,blaze['conditions'][1]['chance']);self.assertEqual(0.02,blaze['conditions'][1]['looting_multiplier']);self.assertEqual(6,sum(r['conditions'] is not MISSING for r in rows))
        fishing=lookup['gameplay/fishing/treasure.json',0,'effect:jungle_sword'];self.assertEqual(Fraction(5,41),fishing['prob']);self.assertEqual(2,len(parents))
        self.assertEqual(Fraction(1,2),one_or_more(Fraction(1,2),1,1));self.assertEqual(Fraction(5,8),one_or_more(Fraction(1,2),1,2));self.assertEqual((2,4),roll_range({'min':2,'max':4}));self.assertEqual(1,weight({}))
        with self.assertRaises(ValueError):roll_range({'min':4,'max':2})
        with self.assertRaises(ValueError):weight({'weight':0})

    def test_on_use_index_component_coverage_and_event_shapes(self):
        from build_on_use_index import collect,build,actions,shape,replace_ice
        old,mid,new=collect();self.assertEqual(build(),(ROOT/'docs/on-use-index.md').read_text());self.assertEqual((26,42,42),(len(old),len(mid),len(new)))
        self.assertFalse(any('minecraft:on_use' in item['components'] or 'minecraft:cooldown' in item['components'] for _,item in old.values()))
        equipped={ident:item for ident,(_,item) in new.items() if 'minecraft:on_use' in item['components']};self.assertEqual(14,len(equipped));self.assertEqual(14,sum('minecraft:cooldown' in item['components'] for _,item in new.values()))
        expected={'blaze_sword':(20,10),'clock_sword':(30,10),'creeper_sword':(3,1),'ender_sword':(2,5),'fire_sword':(25,20),'ghost_sword':(2,6),'ice_sword':(5,6),'lightning_sword':(12,9),'shulker_sword':(8,8),'spectral_sword':(18,15),'spider_sword':(28,8),'tnt_sword':(10,18),'ultra_instinct_sword':(61,48),'wither_sword':(3,3)}
        for ident,item in equipped.items():
            name=ident.split(':')[1];duration,damage=expected[name];self.assertEqual({'category':name,'duration':duration},item['components']['minecraft:cooldown']);self.assertEqual({'on_use':{'event':'on_use'}},item['components']['minecraft:on_use']);act=list(actions(item['events']['on_use']));self.assertEqual([{'type':'durability','amount':damage,'target':'self'}],[v for k,v in act if k=='damage'])
        self.assertEqual(3,sum('sequence' in item['events']['on_use'] for item in equipped.values()));self.assertEqual(4,sum(any(k=='shoot' for k,v in actions(item['events']['on_use'])) for item in equipped.values()))
        def run(id):return [v for k,v in actions(equipped[id]['events']['on_use']) if k=='run_command'][0]
        self.assertEqual((43,'holder'),(len(run('effect:ice_sword')['command']),run('effect:ice_sword')['target']));self.assertEqual(41,len(run('effect:lightning_sword')['command']));self.assertNotIn('target',run('effect:lightning_sword'));self.assertEqual(8,len(run('effect:fire_sword')['command']))
        self.assertEqual('sequence: run_command → damage',shape(equipped['effect:creeper_sword']['events']['on_use']));self.assertEqual('один объект: run_command + damage',shape(equipped['effect:spider_sword']['events']['on_use']))
        before=mid['effect:ice_sword'][1]['events']['on_use'];after=new['effect:ice_sword'][1]['events']['on_use'];self.assertNotEqual(before,after);self.assertEqual(replace_ice(before),after)
        for ident in set(equipped)-{'effect:ice_sword'}:self.assertEqual(mid[ident][1]['events']['on_use'],new[ident][1]['events']['on_use'])

    def test_legacy_coverage_navigation_lists_all_exact_ids(self):
        from build_coverage_legacy import build,EXTRAS
        from build_quick_reference import read_items,legacy_manual_anchor
        items=read_items('SwordsAndMoreSwords.1.6.mcaddon','Sword_B');text=(ROOT/'docs/coverage-1.6.md').read_text();self.assertEqual(build(),text)
        ids=re.findall(r'^\| `(effect:[^`]+)` \|',text,re.M);self.assertCountEqual(items,ids);self.assertEqual(26,len(ids));self.assertTrue(set(EXTRAS)<={ident.split(':')[1] for ident in items})
        for ident in items:self.assertIn('(manual-traces-1.6.md#'+legacy_manual_anchor(ident)+')',text)
        self.assertIn('ни один не считается завершённым',text)

    def test_all_entity_group_reference_inventory_and_gaps(self):
        from build_entity_group_index import extract,counts,build_all
        a=extract('SwordsAndMoreSwords.1.6.mcaddon','Sword_B');b=extract('swordsandmoreswords_2_8_8.mcaddon','Swords_B');c=extract('swordsandmoreswords-2-8-14.mcaddon','Swords_B');self.assertEqual(b,c)
        self.assertEqual({'entities':28,'events':32,'declared':31,'add_only':3,'remove_only':0,'neither':0,'unknown':0,'add_refs':31,'remove_refs':28},counts(a[0]))
        self.assertEqual({'entities':51,'events':303,'declared':198,'add_only':106,'remove_only':1,'neither':7,'unknown':2,'add_refs':302,'remove_refs':124},counts(c[0]))
        self.assertEqual({'Sword_B/entities/blaze2.json','Sword_B/entities/bone2.json','Sword_B/entities/shulker2.json'},{x[0] for x in a[1]});self.assertEqual(['Swords_B/entities/creeper.json'],[x[0] for x in c[1]])
        self.assertEqual({'Swords_B/entities/living_flame.json':['minecraft:fire_immune'],'Swords_B/entities/mountable_slime.json':['despawn'],'Swords_B/entities/slime_king.json':['minecraft:movement.jump']},dict(c[2]))
        bee=c[0]['Swords_B/entities/bee.json'];self.assertNotIn('collect_nectar',bee['groups']);self.assertEqual(2,len(bee['refs']['collect_nectar']['remove']));self.assertEqual([],bee['refs']['collect_nectar']['add'])
        star=c[0]['Swords_B/entities/nether_star_projectile.json'];self.assertNotIn('objective',star['groups']);self.assertEqual(['$.events.objective.add.component_groups[0]'],star['refs']['objective']['add'])
        mounted=c[0]['Swords_B/entities/mountable_slime.json'];self.assertEqual([],mounted['refs']['slime_random_direction']['add']);self.assertTrue(mounted['refs']['slime_random_direction']['remove'])
        for name in ('minecraft:slime_large','minecraft:slime_medium','minecraft:slime_small'):self.assertIn(name,mounted['groups']);self.assertNotIn(name,mounted['refs'])
        self.assertIn('despawn',c[0]['Swords_B/entities/bee_entity.json']['groups']);self.assertNotIn('despawn',c[0]['Swords_B/entities/bee_entity.json']['refs'])
        docs=build_all()
        for version,text in docs.items():self.assertEqual(text,(ROOT/f'docs/entity-groups-{version}.md').read_text())

    def test_creeper_diagnostic_parse_and_independent_explosion_paths(self):
        with zipfile.ZipFile(ROOT/'sources/swordsandmoreswords_2_8_8.mcaddon') as old,zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as z:
            paths=['Swords_B/entities/creeper.json','Swords_B/entities/instant_creeper_explode.json','Swords_B/loot_tables/entities/creeper.json','Swords_B/items/creeper_sword.json','Swords_B/structures/creeper_sword.mcstructure']
            for path in paths:self.assertEqual(old.read(path),z.read(path))
            text=z.read(paths[0]).decode('utf-8-sig')
            with self.assertRaises(ValueError):json5.loads(text)
            pos=text.rfind('}');fixed=json5.loads(text[:pos]+text[pos+1:]);ent=fixed['minecraft:entity'];groups=ent['component_groups'];events=ent['events']
            self.assertEqual('minecraft:creeper',ent['description']['identifier']);self.assertEqual('loot_tables/entities/creeper.json',ent['components']['minecraft:loot']['table']);self.assertEqual(['creeper','monster','mob'],ent['components']['minecraft:type_family']['family'])
            spawned=events['minecraft:entity_spawned']['sequence'][0];self.assertEqual({'test':'has_equipment','subject':'other','domain':'hand','value':'effect:creeper_sword'},spawned['filters']);self.assertEqual(['minecraft:minicreeper','minecraft:minicreeper_projectile'],spawned['add']['component_groups']);self.assertEqual(['minecraft:minicreeper'],events['minecraft:minicreeper']['add']['component_groups'])
            mini=groups['minecraft:minicreeper'];self.assertEqual(['creeper','player','mob','effect99_entities'],mini['minecraft:type_family']['family']);self.assertEqual([10,10],mini['minecraft:timer']['time']);self.assertTrue(mini['minecraft:timer']['looping']);self.assertEqual('start_minicreeper_exploding',mini['minecraft:timer']['time_down_event']['event']);self.assertEqual(2.5,mini['minecraft:target_nearby_sensor']['inside_range'])
            projectile=groups['minecraft:minicreeper_projectile']['minecraft:projectile'];self.assertEqual((1,0.02,1,1),(projectile['power'],projectile['gravity'],projectile['inertia'],projectile['liquid_inertia']));self.assertEqual({'damage':1,'knockback':True},projectile['on_hit']['impact_damage']);self.assertNotIn('remove_on_hit',projectile['on_hit']);self.assertEqual(['minecraft:minicreeper_projectile'],events['minecraft:stop_projectile']['remove']['component_groups'])
            for name,power in [('minecraft:minicreeper_exploding',1),('minecraft:exploding',3),('minecraft:charged_exploding',6),('minecraft:forced_exploding',3),('minecraft:forced_charged_exploding',6)]:
                explode=groups[name]['minecraft:explode'];self.assertEqual((1.5,power,False,True),(explode['fuse_length'],explode['power'],explode['causes_fire'],explode['destroy_affected_by_griefing']))
            self.assertEqual(['minecraft:exploding'],events['minecraft:stop_exploding']['remove']['component_groups']);self.assertEqual(['minecraft:exploding'],events['minecraft:become_charged']['remove']['component_groups']);self.assertEqual(['minecraft:charged_creeper'],events['minecraft:become_charged']['add']['component_groups'])
            def removes(node):
                if isinstance(node,dict):
                    if isinstance(node.get('remove'),dict):yield from node['remove'].get('component_groups',[])
                    for value in node.values():yield from removes(value)
                elif isinstance(node,list):
                    for value in node:yield from removes(value)
            self.assertTrue({'minecraft:charged_exploding','minecraft:forced_exploding','minecraft:forced_charged_exploding','minecraft:minicreeper_exploding'}.isdisjoint(set(removes(events))))
            timer=groups['minecraft:forced_charged_exploding']['minecraft:timer'];self.assertEqual([1.4,1.4],timer['time']);self.assertFalse(timer['looping']);self.assertEqual('creeper_sword',timer['time_down_event']['event']);branches=events['creeper_sword']['randomize'];self.assertEqual([95,5],[x['weight'] for x in branches]);self.assertEqual(['structure load creeper_sword ~ ~ ~'],branches[1]['run_command']['command'])
            item=json5.loads(z.read(paths[3]).decode('utf-8-sig'))['minecraft:item'];seq=item['events']['weapon']['sequence'];self.assertEqual(1,seq[0]['damage']['amount']);self.assertEqual([20,80],[x['weight'] for x in seq[1]['randomize']]);self.assertEqual('minecraft:creeper',seq[1]['randomize'][0]['shoot']['projectile']);self.assertEqual('holder',item['events']['on_use']['sequence'][0]['run_command']['target'])
            players=[json5.loads(q.read('Swords_B/entities/player.json').decode('utf-8-sig'))['minecraft:entity'] for q in (old,z)]
            for section,name in [('component_groups','start_player_explode_event'),('events','start_player_explode_event'),('events','start_player_explode')]:self.assertEqual(players[0][section][name],players[1][section][name])
            group=players[1]['component_groups']['start_player_explode_event'];self.assertEqual(0,group['minecraft:movement']['value']);self.assertEqual([1.5,1.5],group['minecraft:timer']['time']);self.assertTrue(group['minecraft:timer']['looping']);self.assertEqual(['summon entity:instant_creeper_explode ~ ~1 ~','kill @s'],players[1]['events']['start_player_explode']['run_command']['command'])
            inst=json5.loads(z.read(paths[1]).decode('utf-8-sig'))['minecraft:entity']['components'];self.assertEqual((0,4,False,True),(inst['minecraft:explode']['fuse_length'],inst['minecraft:explode']['power'],inst['minecraft:explode']['causes_fire'],inst['minecraft:explode']['destroy_affected_by_griefing']))
            loot=json5.loads(z.read(paths[2]).decode('utf-8-sig'))['pools'];self.assertEqual(3,len(loot));self.assertEqual(['minecraft:skeleton','minecraft:stray'],[x['conditions'][0]['entity_type'] for x in loot[1:]]);self.assertEqual([12,12],[len(x['entries']) for x in loot[1:]]);self.assertFalse(any(x.get('name')=='effect:creeper_sword' for p in loot for x in p['entries']))
            structure=nbtlib.File.parse(io.BytesIO(z.read(paths[4])),byteorder='little');self.assertEqual([1,1,1],list(structure['size']));entities=structure['structure']['entities'];self.assertEqual(1,len(entities));self.assertEqual('effect:creeper_sword',entities[0]['Item']['Name']);self.assertEqual((1,0,159),(int(entities[0]['Item']['Count']),int(entities[0]['Item']['Damage']),int(entities[0]['Age'])))

    def test_entity_literal_event_fields_targets_and_local_names(self):
        from build_entity_event_index import extract,summary,build_all
        a=extract('SwordsAndMoreSwords.1.6.mcaddon','Sword_B');b=extract('swordsandmoreswords_2_8_8.mcaddon','Swords_B');c=extract('swordsandmoreswords-2-8-14.mcaddon','Swords_B');self.assertEqual(b,c)
        self.assertEqual((30,collections.Counter({None:28,'self':2}),collections.Counter()),summary(a[0]));self.assertEqual((228,collections.Counter({None:123,'self':100,'baby':3,'block':2}),collections.Counter({None:2,'self':3,'block':2})),summary(c[0]))
        self.assertEqual(28,len(a[0]));self.assertEqual(51,len(c[0]));self.assertEqual(['Swords_B/entities/creeper.json'],[x[0] for x in c[1]]);self.assertEqual(3,len(a[1]));self.assertEqual(3,len(c[2]))
        bee=c[0]['Swords_B/entities/bee.json'];self.assertEqual(2,sum(event=='minecraft:bee_returned_to_hive' and target=='block' for _,event,target in bee['refs']));self.assertNotIn('minecraft:bee_returned_to_hive',bee['events'])
        for p in ('lightning_projectile','wither_effect'):
            ent=c[0]['Swords_B/entities/'+p+'.json'];self.assertIn(('$.components.minecraft:environment_sensor[0].on_environment.event','particle',None),ent['refs']);self.assertNotIn('particle',ent['events'])
        ultra=c[0]['Swords_B/entities/ultra_instinct_projectile.json'];self.assertIn(('$.components.minecraft:ageable.grow_up.event','minecraft:end_scale','self'),ultra['refs']);self.assertNotIn('minecraft:end_scale',ultra['events'])
        wolf=c[0]['Swords_B/entities/wolf.json']
        for e in ('minecraft:on_leash','minecraft:on_unleash'):self.assertTrue(any(event==e and target=='self' for _,event,target in wolf['refs']));self.assertNotIn(e,wolf['events'])
        for version,text in build_all().items():self.assertEqual(text,(ROOT/f'docs/entity-event-fields-{version}.md').read_text())

    def test_direct_spawn_shoot_targets_and_ambiguities(self):
        from build_spawn_shoot_index import extract,build_all
        old=extract('SwordsAndMoreSwords.1.6.mcaddon','Sword_B');a=extract('swordsandmoreswords_2_8_8.mcaddon','Swords_B');b=extract('swordsandmoreswords-2-8-14.mcaddon','Swords_B');self.assertEqual(a[1:],b[1:])
        self.assertEqual(collections.Counter({'spawn_entity':25}),collections.Counter(x['kind'] for x in old[1]));self.assertTrue(all(x['id'] in old[0] for x in old[1]));self.assertEqual(collections.Counter({'shoot':20,'spawn_entity':6}),collections.Counter(x['kind'] for x in b[1]));self.assertEqual({'minecraft:creeper'},set(x['id'] for x in b[1] if x['id'] not in b[0]));self.assertEqual(['Swords_B/entities/creeper.json'],[x[0] for x in b[2]])
        fake=[x for x in b[1] if x['id']=='entity:fake_fireball'];self.assertEqual(4,len(fake));self.assertEqual([f'$.minecraft:entity.component_groups.shoot_small_fireball.minecraft:spawn_entity[{i}]' for i in range(4)],[x['location'] for x in fake]);self.assertTrue(all(x['value']['spawn_event']=='set_sound' and x['value']['num_to_spawn']==1 for x in fake));self.assertIn('set_sound',b[0]['entity:fake_fireball'][0]['events']);self.assertFalse(b[0]['entity:fake_fireball'][0]['description']['is_summonable']);self.assertIn('components',b[0]['entity:fake_fireball'][0]['projectiles'])
        bee=next(x for x in b[1] if x['id']=='entity:bee_sword');self.assertEqual((30,1),(bee['weight'],bee['value']['launch_power']));self.assertEqual([],b[0]['entity:bee_sword'][0]['projectiles'])
        creeper=next(x for x in b[1] if x['id']=='minecraft:creeper');self.assertEqual(20,creeper['weight']);self.assertEqual('shoot',creeper['kind']);self.assertTrue(any(x['id']=='entity:web' and x['kind']=='shoot' for x in b[1]));self.assertTrue(any(x['id']=='entity:web' and x['kind']=='spawn_entity' for x in b[1]))
        for version,text in build_all().items():self.assertEqual(text,(ROOT/f'docs/spawn-shoot-index-{version}.md').read_text())

    def test_command_risk_index_candidates_and_version_difference(self):
        from build_command_risk_index import extract,build_all,marks
        old=extract('SwordsAndMoreSwords.1.6.mcaddon','Sword_B');a=extract('swordsandmoreswords_2_8_8.mcaddon','Swords_B');b=extract('swordsandmoreswords-2-8-14.mcaddon','Swords_B')
        self.assertEqual((922,158),(old[3],len(old[0])));self.assertEqual((946,69),(a[3],len(a[0])));self.assertEqual((945,69),(b[3],len(b[0])));self.assertEqual(3,len(old[1]));self.assertEqual(['Swords_B/entities/creeper.json'],[x[0] for x in b[1]])
        def counts(data):return collections.Counter(label for row in data[0] for label in row[5])
        self.assertEqual((5,109,6,26),(counts(old)['gamerule'],counts(old)['scoreboard'],counts(old)['kill'],counts(old)['replaceitem']));self.assertEqual((6,9,4,20,9,7,11,3),tuple(counts(b)[k] for k in ('gamerule','scoreboard','time','kill','damage','tp','ride','replaceitem')))
        self.assertEqual(('scoreboard','kill'),marks('/execute @p ~ ~ ~ scoreboard objectives remove b; kill @s'));self.assertEqual((),marks('say effect99:time_not_command'))
        diff_a=set(a[0])-set(b[0]);diff_b=set(b[0])-set(a[0]);self.assertEqual((1,1),(len(diff_a),len(diff_b)));x,y=next(iter(diff_a)),next(iter(diff_b));self.assertEqual(x[:4],y[:4]);self.assertIn('effect99:fake_ice',x[4]);self.assertEqual(x[4].replace('effect99:fake_ice','frosted_ice'),y[4]);self.assertEqual(('tp',),x[5])
        self.assertTrue(any('kill @e[type=entity:blaze2,r=5] ~ 0 ~' in row[4] for row in old[0]));self.assertTrue(any(row[4]=='gamerule sendcommandfeedback false' for row in b[0]));self.assertTrue(any(row[4]=='damage @s 14 magic' for row in b[0]))
        for version,text in build_all().items():self.assertEqual(text,(ROOT/f'docs/command-risk-index-{version}.md').read_text())

    def test_all_projectile_component_objects_and_groups(self):
        from build_projectile_component_index import extract,build_all
        a=extract('SwordsAndMoreSwords.1.6.mcaddon','Sword_B');b=extract('swordsandmoreswords_2_8_8.mcaddon','Swords_B');c=extract('swordsandmoreswords-2-8-14.mcaddon','Swords_B');self.assertEqual(b,c);self.assertEqual((0,28,3),(len(a[0]),a[3],len(a[1])));self.assertEqual((35,20,51,1,3),(len(c[0]),len({x[0] for x in c[0]}),c[3],len(c[1]),len(c[2])))
        self.assertEqual('Swords_B/entities/creeper.json',c[1][0][0]);self.assertEqual(build_all(),(ROOT/'docs/projectile-component-index.md').read_text());records={(id,where):value for _,id,where,value in c[0]}
        self.assertEqual(6,sum(ident=='minecraft:arrow' for _,ident,_,_ in c[0]));self.assertEqual([1,4],records['minecraft:arrow','components']['on_hit']['impact_damage']['damage']);self.assertEqual(5,records['minecraft:arrow','component_groups.minecraft:player_arrow']['power'])
        self.assertEqual((1,10),(records['entity:fire','components']['power'],records['entity:fire','component_groups.fire_sword']['power']));self.assertNotIn('teleport_owner',records['entity:ghost_projectile','components']['on_hit']);self.assertIn('teleport_owner',records['entity:ghost_projectile','component_groups.teleport_enable']['on_hit']);self.assertIn('remove_on_hit',records['entity:ghost_projectile','component_groups.teleport_enable']['on_hit'])
        self.assertEqual((0,0.005),(records['minecraft:wither_skull_dangerous','components']['gravity'],records['minecraft:wither_skull_dangerous','component_groups.wither_sword']['gravity']));self.assertNotIn(('minecraft:creeper','component_groups.minecraft:minicreeper_projectile'),records)
        with zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as z:
            for path,ident,where,value in c[0]:
                e=json5.loads(z.read(path).decode('utf-8-sig'))['minecraft:entity'];source=e['components'] if where=='components' else e['component_groups'][where.split('.',1)[1]];self.assertEqual(value,source['minecraft:projectile'])

    def test_player_base_sensor_order_and_equipment_mapping(self):
        from build_player_sensor_index import collect,build
        old=collect('SwordsAndMoreSwords.1.6.mcaddon','Sword_B');a=collect('swordsandmoreswords_2_8_8.mcaddon','Swords_B');b=collect('swordsandmoreswords-2-8-14.mcaddon','Swords_B');self.assertEqual(build(),(ROOT/'docs/player-sensor-index.md').read_text())
        self.assertEqual((26,28,26),(len(old[0]),len(old[1]),len(old[3])));self.assertEqual((42,62,29),(len(b[0]),len(b[1]),len(b[3])));self.assertEqual(a[1],b[1]);self.assertEqual(a[3],b[3]);self.assertTrue(all(row['on_environment']['event'] in old[2] for row in old[1]));self.assertTrue(all(row['on_environment']['event'] in b[2] for row in b[1]))
        self.assertTrue(all(len(v)==1 and v[0][1] is None for v in old[3].values()));self.assertEqual(28,sum(len(v)==2 for v in b[3].values()));self.assertEqual([(43,None,'minecraft:glowstone_sword')],b[3]['effect:glowstone_sword'])
        for ident,refs in b[3].items():
            if ident!='effect:glowstone_sword':self.assertEqual([None,'!='],[r[1] for r in refs])
        self.assertEqual({'effect:bedrock_stick','effect:bedrock_sword','effect:coal_sword','effect:creeper_sword','effect:cursed_pumpkin_sword','effect:glass_sword','effect:quartz_diamond','effect:quartz_diamond_stick','effect:silver_ingot','effect:silver_sword','effect:tnt_sword','effect:wet_sponge_sword','effect:wither_skeleton_sword'},set(b[0])-set(b[3]))
        self.assertEqual({'test':'is_family','operator':'!=','value':'null'},b[1][1]['on_environment']['filters']);self.assertEqual('minecraft:constant_events',b[1][1]['on_environment']['event']);self.assertEqual({'any_of':[{'test':'is_family','subject':'self','value':'default_player'},{'test':'is_family','subject':'self','operator':'!=','value':'spectral_sword'}]},b[1][2]['on_environment']['filters']);self.assertEqual('minecraft:event_normal_player',old[1][1]['on_environment']['event'])
        self.assertEqual([(29,None,'minecraft:spectral_sword'),(30,'!=','stop_spectral_sword_event')],b[3]['effect:spectral_sword'])

    def test_item_repair_index_all_versions_and_literal_flags(self):
        from build_item_repair_index import collect,build,literal
        old,a,b=collect();text=(ROOT/'docs/item-repair-index.md').read_text();self.assertEqual(build(),text);self.assertEqual((26,42,42),(len(old),len(a),len(b)))
        self.assertTrue(all(a[id][1]['components']==b[id][1]['components'] for id in a));self.assertEqual(26,sum('minecraft:repairable' in item['components'] for _,item in old.values()));self.assertEqual(33,sum('minecraft:repairable' in item['components'] for _,item in b.values()));self.assertEqual(16,sum(item['components'].get('minecraft:foil') is True for _,item in b.values()))
        absent={'effect:bedrock_stick','effect:bedrock_sword','effect:ghost_sword','effect:quartz_diamond','effect:quartz_diamond_stick','effect:quartz_sword','effect:silver_ingot','effect:time_sword','effect:ultra_instinct_sword'};self.assertEqual(absent,{ident for ident,(_,it) in b.items() if 'minecraft:repairable' not in it['components']})
        keys=('minecraft:durability','minecraft:repairable','minecraft:foil','minecraft:hand_equipped','minecraft:allow_off_hand','minecraft:max_stack_size')
        sections=re.split(r'^## (1\.6|2\.8\.8 и 2\.8\.14)\n',text,flags=re.M);sections=dict(zip(sections[1::2],sections[2::2]))
        for version,data in [('1.6',old),('2.8.8 и 2.8.14',b)]:
            rows=re.findall(r'^\| \[`(effect:[^`]+)`\]\([^)]*\) \| (.*) \|$',sections[version],re.M);self.assertEqual(len(data),len(rows));self.assertCountEqual(data,[id for id,_ in rows])
            for ident,row in rows:self.assertEqual([literal(data[ident][1]['components'],key) for key in keys],row.split(' | '),ident)
        for ident,(_,it) in old.items():
            c=it['components'];self.assertEqual([{'items':[ident],'repair_amount':c['minecraft:durability']['max_durability']}],c['minecraft:repairable']['repair_items']);self.assertNotIn('minecraft:foil',c)
        wet=b['effect:wet_sponge_sword'][1]['components']['minecraft:repairable']['repair_items'];self.assertEqual([(['effect:sponge_sword'],64),(['minecraft:sponge'],32),(['effect:wet_sponge_sword'],64)],[(x['items'],x['repair_amount']) for x in wet]);pumpkin=b['effect:cursed_pumpkin_sword'][1]['components']['minecraft:repairable']['repair_items'];self.assertEqual([['effect:cursed_pumpkin_sword'],['minecraft:honey_block'],['minecraft:honeycomb']],[x['items'] for x in pumpkin])
        self.assertEqual('—',literal({},'minecraft:foil'));self.assertEqual('`false`',literal({'minecraft:foil':False},'minecraft:foil'))

    def test_client_animation_full_objects_and_alias_coverage(self):
        from build_client_animation_index import collect,build
        from build_quick_reference import slug
        old=collect('SwordsAndMoreSwords.1.6.mcaddon','Sword_R');a=collect('swordsandmoreswords_2_8_8.mcaddon','Swords_R');b=collect('swordsandmoreswords-2-8-14.mcaddon','Swords_R');self.assertEqual(a,b);self.assertEqual([],old[0]);self.assertEqual((18,9,0,0),(len(b[0]),len({x['path'] for x in b[0]}),len(b[2]),len(b[3])));text=(ROOT/'docs/client-animation-index.md').read_text();self.assertEqual(build(),text)
        ids=[x['id'] for x in b[0]];sections=re.split(r'^### `([^`]+)`\n',text,flags=re.M);sections=dict(zip(sections[1::2],sections[2::2]));self.assertCountEqual(ids,sections)
        for x in b[0]:
            chunk=sections[x['id']];raw=re.search(r'```json\n(.*?)\n```',chunk,re.S);self.assertIsNotNone(raw,x['id']);self.assertEqual(x['definition'],json.loads(raw.group(1)));self.assertIn(x['sha256'],chunk);self.assertIn('](#'+slug(x['id'])+')',text)
        lookup={x['id']:x['definition'] for x in b[0]};self.assertEqual(1.52,lookup['animation.player.explode']['animation_length']);self.assertEqual(7,len(lookup['animation.player.explode']['bones']));self.assertNotIn('animation.player.explode',b[1]);self.assertEqual(10000,lookup['animation.shulker_shield.closed']['animation_length']);self.assertNotIn('bones',lookup['animation.baby_slime.wing']);self.assertEqual(0.01,lookup['animation.mermaid_player.tail']['animation_length']);self.assertTrue(lookup['animation.mermaid_player.tail']['override_previous_animation'])
        self.assertIn(('Swords_R/entity/player.entity.json','minecraft:player','blaze_rods.move'),b[1]['animation.blaze_rods']);self.assertIn(('Swords_R/entity/mountable_slime.v1.0.json','entity:mountable_slime','is_jump'),b[1]['animation.baby_slime.speed_wing'])
        with zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as z:
            player=json5.loads(z.read('Swords_B/entities/player.json').decode('utf-8-sig'))['minecraft:entity'];self.assertIn('playanimation @s animation.player.explode',player['events']['start_player_explode_event']['run_command']['command'])

    def test_client_geometry_all_models_and_legacy_schemas(self):
        from build_client_geometry_index import collect,build
        old=collect('SwordsAndMoreSwords.1.6.mcaddon','Sword_R');a=collect('swordsandmoreswords_2_8_8.mcaddon','Swords_R');b=collect('swordsandmoreswords-2-8-14.mcaddon','Swords_R');self.assertEqual(a,b);self.assertEqual([],old[0]);self.assertEqual((21,21,0,0),(len(b[0]),len(b[1]),len(b[3]),len(b[4])));text=(ROOT/'docs/client-geometry-index.md').read_text();self.assertEqual(build(),text)
        parts=re.split(r'^### `([^`]+)`\n',text,flags=re.M);sections=dict(zip(parts[1::2],parts[2::2]));self.assertCountEqual([x['path'] for x in b[0]],sections)
        with zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as z:
            for x in b[0]:
                raw=re.search(r'```json\n(.*?)\n```',sections[x['path']],re.S);self.assertIsNotNone(raw,x['path']);self.assertEqual(x['object'],json.loads(raw.group(1)));self.assertEqual(x['object'],json5.loads(z.read(x['path']).decode('utf-8-sig')));self.assertIn(x['sha256'],sections[x['path']])
        geometries={x['id']:x for x in b[1]};self.assertEqual(3,sum(not x['modern'] for x in b[1]));self.assertFalse(geometries['geometry.blaze_rods']['modern']);self.assertEqual((64,32,12),(geometries['geometry.blaze_rods']['description']['texturewidth'],geometries['geometry.blaze_rods']['description']['textureheight'],len(geometries['geometry.blaze_rods']['data']['bones'])));self.assertNotIn('bones',geometries['geometry.null']['data']);wolf=geometries['geometry.wolf_transformation']['data'];self.assertEqual((25,10),(len(wolf['bones']),sum(len(x.get('cubes',[])) for x in wolf['bones'])));self.assertEqual((64,64),(wolf['description']['texture_width'],wolf['description']['texture_height']))
        self.assertTrue(any(alias[1]=='minecraft:player' for alias in b[2]['geometry.mermaid_player.tail']));self.assertNotIn('geometry.null',b[2])

    def test_client_effects_all_controllers_particles_materials(self):
        from build_client_effects_ledger import collect,build
        old=collect('SwordsAndMoreSwords.1.6.mcaddon','Sword_R');a=collect('swordsandmoreswords_2_8_8.mcaddon','Swords_R');b=collect('swordsandmoreswords-2-8-14.mcaddon','Swords_R');self.assertEqual([],old[0]);self.assertEqual(a,b);self.assertEqual((28,0,0),(len(b[0]),len(b[1]),len(b[2])));self.assertEqual(collections.Counter({'animation_controllers':5,'render_controllers':15,'particles':7,'materials':1}),collections.Counter(x['folder'] for x in b[0]))
        text=(ROOT/'docs/client-effects-ledger.md').read_text();self.assertEqual(build(),text);parts=re.split(r'^### `([^`]+)`\n',text,flags=re.M);sections=dict(zip(parts[1::2],parts[2::2]));self.assertCountEqual([x['path'] for x in b[0]],sections)
        with zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as z:
            for x in b[0]:
                raw=re.search(r'```json\n(.*?)\n```',sections[x['path']],re.S);self.assertIsNotNone(raw,x['path']);self.assertEqual(x['object'],json.loads(raw.group(1)));self.assertEqual(x['object'],json5.loads(z.read(x['path']).decode('utf-8-sig')));self.assertIn(x['sha256'],sections[x['path']])
        lookup={x['path']:x for x in b[0]};particle=lookup['Swords_R/particles/examples/example_directional_sphere.json']['object']['particle_effect']['description'];self.assertEqual('minecraft:example_directional_sphere',particle['identifier']);self.assertEqual('textures/ui/RTX_Sparkle',particle['basic_render_parameters']['texture']);self.assertIn('controller.animation.baby_slime.move',lookup['Swords_R/animation_controllers/baby_slime.animation_controllers.json']['ids'])

    def test_item_visual_atlas_keys_and_render_offsets(self):
        from build_item_visual_index import collect,build,icon_key,atlas_entry,png_ref,val
        old=collect('SwordsAndMoreSwords.1.6.mcaddon','Sword_B','Sword_R');a=collect('swordsandmoreswords_2_8_8.mcaddon','Swords_B','Swords_R');b=collect('swordsandmoreswords-2-8-14.mcaddon','Swords_B','Swords_R');text=(ROOT/'docs/item-visual-index.md').read_text();self.assertEqual(build(),text)
        self.assertEqual((26,26,26),(len(old[0]),len(old[1]),len(old[2]['texture_data'])));self.assertEqual(set(old[0]),set(old[1]));self.assertEqual((42,0,42),(len(b[0]),len(b[1]),len(b[2]['texture_data'])));self.assertEqual(a[3],b[3]);self.assertEqual((0,12),(sum('minecraft:render_offsets' in it['components'] for _,it in old[0].values()),sum('minecraft:render_offsets' in it['components'] for _,it in b[0].values())))
        mismatch=[]
        for ident,(_,it) in old[0].items():
            bc=it['components'];rc=old[1][ident][1]['minecraft:item']['components'];self.assertEqual('miscellaneous',rc['minecraft:render_offsets']);self.assertIn(icon_key(bc),old[2]['texture_data']);self.assertIn('.png',png_ref(old,icon_key(bc),'Sword_R'))
            if icon_key(bc)!=icon_key(rc):mismatch.append(ident)
        self.assertEqual(['effect:sword_of_time'],mismatch);bc=old[0]['effect:sword_of_time'][1]['components'];rc=old[1]['effect:sword_of_time'][1]['minecraft:item']['components'];self.assertEqual(('sword_of_time','Sword_of_Time'),(icon_key(bc),icon_key(rc)));self.assertNotIn('Sword_of_Time',old[2]['texture_data']);self.assertEqual({'textures':'textures/items/Sword_of_Time'},old[2]['texture_data']['sword_of_time']);self.assertEqual('**ключ не найден точно**',atlas_entry(old[2],'Sword_of_Time'))
        for id,(_,item) in b[0].items():self.assertIn(icon_key(item['components']),b[2]['texture_data']);self.assertIn('.png',png_ref(b,icon_key(item['components']),'Swords_R'));self.assertEqual(item['components'],a[0][id][1]['components'])
        rows=re.findall(r'^\| \[`(effect:[^`]+)`\]\([^)]*\) \|',text,re.M);self.assertEqual(68,len(rows));self.assertCountEqual(list(old[0])+list(b[0]),rows);self.assertEqual('—',val({},'minecraft:render_offsets'))
        ultra=b[0]['effect:ultra_instinct_sword'][1]['components']['minecraft:render_offsets'];self.assertEqual([0,-5.0,95],ultra['main_hand']['first_person']['rotation']);self.assertEqual([1.8,-1.4,-5.5],ultra['main_hand']['first_person']['position'])

    def test_ui_localization_direct_references_and_all_lang_lines(self):
        from build_ui_localization import load,build_ui,build_lang,textrefs,code
        d=load();ui=(ROOT/'docs/ui-localization-index.md').read_text();lang=(ROOT/'docs/localization-source-index.md').read_text();self.assertEqual(build_ui(d),ui);self.assertEqual(build_lang(d),lang)
        self.assertEqual((26,674,674),tuple(len(d[v]['lines']) for v in ('1.6','2.8.8','2.8.14')));self.assertIsNone(d['1.6']['ui']);self.assertEqual(d['2.8.8']['ui_raw'],d['2.8.14']['ui_raw']);refs=list(textrefs(d['2.8.14']['ui'],'$'));self.assertEqual((490,490),(len(refs),len({k for p,k in refs})))
        missing=[k for p,k in refs if k not in d['2.8.14']['entries']];self.assertEqual(9,len(missing));self.assertEqual(missing,[k for p,k in refs if k not in d['2.8.8']['entries']]);self.assertIn('effect.ice_sword.text.8',missing);self.assertIn('effect.nether_star_sword.text.1',missing)
        for path,key in refs:self.assertIn(code(path)+' | '+code(key),ui)
        for version in ('1.6','2.8.8','2.8.14'):
            section=lang.split('## '+version+'\n',1)[1].split('\n## ',1)[0]
            for i,line in enumerate(d[version]['lines'],1):self.assertIn(f'| {i} | {code(line)} |',section)
        self.assertEqual([(52,'§lGhost'),(54,'§l§fGhost')],d['2.8.14']['entries']['entity.entity:ghost.name']);a=d['2.8.8']['entries'];b=d['2.8.14']['entries'];self.assertEqual({'updates_changelog.header.title','effect.updates_changelog.text_0','effect.updates_changelog.text_2'},{k for k in set(a)|set(b) if a.get(k)!=b.get(k)})
        section=ui.split('### nether_star_sword_section@how_to_play_common.main_sections',1)[1].split('\n### ',1)[0];self.assertLess(section.index('effect.nether_star_sword.text.13'),section.index('effect.nether_star_sword.text.0'));self.assertIn('-Durability: 3256',section)
        quick=(ROOT/'docs/quick-reference.md').read_text();self.assertEqual(82,quick.count('[текст справки](ui-localization-index.md#'));self.assertIn('[текст справки](ui-localization-index.md#sponge_sword_sectionhow_to_play_commonmain_sections)',next(x for x in quick.splitlines() if x.startswith('| `effect:wet_sponge_sword`') and 'items-2.8.14.md' in x));self.assertIn('effect.sponge_sword.text.14',b);self.assertIn('effect.sponge_sword.text.15',b);self.assertTrue({'effect.sponge_sword.text.14','effect.sponge_sword.text.15'}.isdisjoint({key for _,key in refs}))

    def test_ui_numeric_claims_match_literal_item_components(self):
        from collections import Counter
        from build_ui_stats import claims,build,cell,comp
        from build_ui_localization import load
        from build_quick_reference import read_items
        a,b=claims('2.8.8'),claims('2.8.14');self.assertEqual(a,b);self.assertEqual(37,len(b));text=(ROOT/'docs/ui-stat-comparison.md').read_text();self.assertEqual(build(),text);items=read_items('swordsandmoreswords-2-8-14.mcaddon','Swords_B')
        damage=[];durability=[]
        for ident,record in b.items():
            damage.append(cell(record.get('Damage'),comp(items,ident,'Damage'))[2]);durability.append(cell(record.get('Durability'),comp(items,ident,'Durability'))[2])
        self.assertEqual({'совпадает':37},dict(Counter(damage)));self.assertEqual({'совпадает':35,'нечисловое заявление':1,'не сравнивается':1},dict(Counter(durability)))
        self.assertEqual(('effect.sponge_sword.text.0','effect.sponge_sword.text.1'),(b['effect:sponge_sword']['Durability']['key'],b['effect:sponge_sword']['Damage']['key']));self.assertEqual(('effect.sponge_sword.text.9','effect.sponge_sword.text.10'),(b['effect:wet_sponge_sword']['Durability']['key'],b['effect:wet_sponge_sword']['Damage']['key']));self.assertIn('Wet Sponge Sword',load()['2.8.14']['entries']['sponge_sword.header.title.1'][0][1]);self.assertEqual('effect.nether_star_sword.text.13',b['effect:nether_star_sword']['Durability']['key']);self.assertNotIn('Durability',b['effect:wolf_sword']);self.assertIsNone(b['effect:bedrock_sword']['Durability']['number'])

    def test_effect_index_commands_and_structural_objects(self):
        from build_effect_index import extract,build_all,CANDIDATE,code
        from build_entity_group_index import VERSIONS
        data={v:extract(f,p) for v,f,p in VERSIONS};self.assertEqual(data['2.8.8'],data['2.8.14']);self.assertEqual((49,60),(len(data['1.6'][0]),len(data['2.8.14'][0])));self.assertEqual((49,69),tuple(sum(len(x[3]) for x in data[v][0]) for v in ('1.6','2.8.14')));self.assertEqual((4,20),(len(data['1.6'][1]),len(data['2.8.14'][1])));self.assertEqual((3,1),(len(data['1.6'][2]),len(data['2.8.14'][2])));self.assertFalse(data['1.6'][4]);self.assertFalse(data['2.8.14'][4])
        built=build_all()
        for ver,filename,pack in VERSIONS:
            d=data[ver];doc=(ROOT/'docs'/f'effect-index-{ver if ver=="1.6" else "2.x"}.md').read_text()
            with zipfile.ZipFile(ROOT/'sources'/filename) as z:
                raw=[(p,i,l) for p in sorted(z.namelist()) if p.startswith(pack+'/') and p.endswith(('.json','.mcfunction','.js')) for i,l in enumerate(z.read(p).decode('utf-8-sig').splitlines(),1) if CANDIDATE.search(l)]
            self.assertEqual(raw,[(p,i,l) for p,i,l,names in d[0]])
            for path,line,text,names in d[0]:self.assertIn(f'`{path}:{line}`',doc);self.assertIn(code(text),doc)
            for path,loc,key,value in d[1]:self.assertIn('`'+loc+'`',doc);self.assertIn(code(value),doc)
        for ver,text in built.items():self.assertEqual(text,(ROOT/'docs'/f'effect-index-{ver}.md').read_text())
        objs=data['2.8.14'][1];parrot=next(value for path,loc,key,value in objs if path.endswith('/parrot.json') and key=='minecraft:healable');self.assertEqual({'name':'fatal_poison','chance':1.0,'duration':1000,'amplifier':0},parrot['items'][0]['effects'][0]);self.assertEqual('cookie',parrot['items'][0]['item']);self.assertEqual(6,sum(key=='arrow_effect' for path,loc,key,value in objs));wither=next(value for path,loc,key,value in objs if path.endswith('/wither_skull.json') and key=='mob_effect');self.assertEqual((0,200,800,1),(wither['durationeasy'],wither['durationnormal'],wither['durationhard'],wither['amplifier']))

    def test_scoreboard_index_raw_lines_and_named_objectives(self):
        from build_scoreboard_index import extract,build_all,SCAN,fmt
        from build_entity_group_index import VERSIONS
        data={v:extract(f,p) for v,f,p in VERSIONS};self.assertEqual(data['2.8.8'],data['2.8.14']);self.assertEqual((228,15),(len(data['1.6'][0]),len(data['2.8.14'][0])));self.assertFalse(data['1.6'][1]);self.assertFalse(data['2.8.14'][1]);self.assertEqual({'b','bn','c','ct','e','l','s','sh','swords','w'},{name for _,_,_,refs in data['1.6'][0] for name,_ in refs});self.assertEqual({'Effect99','slime_despawn','sponge_sword'},{name for _,_,_,refs in data['2.8.14'][0] for name,_ in refs})
        for ver,filename,pack in VERSIONS:
            rows=data[ver][0];doc=(ROOT/'docs'/f'scoreboard-index-{ver if ver=="1.6" else "2.x"}.md').read_text()
            with zipfile.ZipFile(ROOT/'sources'/filename) as z:raw=[(p,i,l) for p in sorted(z.namelist()) if p.startswith(pack+'/') and p.endswith(('.json','.mcfunction','.js')) for i,l in enumerate(z.read(p).decode('utf-8-sig').splitlines(),1) if SCAN.search(l)]
            self.assertEqual(raw,[(p,i,l) for p,i,l,refs in rows])
            for path,line,text,refs in rows:self.assertTrue(refs);self.assertIn(f'`{path}:{line}`',doc);self.assertIn(fmt(text),doc)
        for ver,text in build_all().items():self.assertEqual(text,(ROOT/'docs'/f'scoreboard-index-{ver}.md').read_text())
        s='\n'.join(row[2] for row in data['2.8.14'][0]);self.assertIn('scores={sponge_sword=150}',s);self.assertIn('scores={sponge_sword=155}',s);self.assertIn('scores={sponge_sword=160}',s);self.assertIn('scores={slime_despawn=100}',s);self.assertIn('scoreboard players set @e[type=entity:mountable_slime,c=1,r=12] slime_despawn 0',s)
        old='\n'.join(row[2] for row in data['1.6'][0]);self.assertIn('scoreboard players set @a swords 2',old);self.assertIn('execute @p[r=2] ~ ~ ~ scoreboard objectives remove b',old)

    def test_entity_combat_index_preserves_components_and_groups(self):
        from build_entity_combat_index import extract,build_all,KEYS,code
        from build_entity_group_index import VERSIONS
        data={v:extract(f,p) for v,f,p in VERSIONS};self.assertEqual(data['2.8.8'],data['2.8.14']);self.assertEqual((57,156),(len(data['1.6'][0]),len(data['2.8.14'][0])));self.assertEqual((28,51),(data['1.6'][3],data['2.8.14'][3]));self.assertEqual((3,1),(len(data['1.6'][1]),len(data['2.8.14'][1])));self.assertEqual(40,sum(r[3]=='minecraft:damage_sensor' for r in data['2.8.14'][0]));self.assertEqual(12,sum(r[3]=='minecraft:explode' for r in data['2.8.14'][0]))
        for ver,filename,pack in VERSIONS:
            rows=data[ver][0];expected=[]
            with zipfile.ZipFile(ROOT/'sources'/filename) as z:
                for path in sorted(z.namelist()):
                    if not path.startswith(pack+'/entities/') or not path.endswith('.json'):continue
                    try:e=json5.loads(z.read(path).decode('utf-8-sig'))['minecraft:entity']
                    except (ValueError,KeyError):continue
                    groups=[('$.minecraft:entity.components',e.get('components',{}))]+[('$.minecraft:entity.component_groups.'+k,v) for k,v in e.get('component_groups',{}).items()]
                    for loc,obj in groups:
                        for key,value in obj.items():
                            if key in KEYS:expected.append((path,e['description']['identifier'],loc+'.'+key,key,value))
            self.assertEqual(expected,rows);doc=(ROOT/'docs'/f'entity-combat-index-{ver if ver=="1.6" else "2.x"}.md').read_text()
            for path,ident,loc,key,value in rows:self.assertIn('`'+loc+'`',doc);self.assertIn(code(value),doc)
        for version,text in build_all().items():self.assertEqual(text,(ROOT/'docs'/f'entity-combat-index-{version}.md').read_text())
        rows=data['2.8.14'][0];hostile=next(v for p,id,loc,k,v in rows if p.endswith('/living_flame.json') and loc.endswith('hostile_entity.minecraft:damage_sensor'));self.assertFalse(hostile['triggers']['deals_damage']);self.assertEqual('start_death_hostile',hostile['triggers']['on_damage']['event']);self.assertEqual('player',hostile['triggers']['on_damage']['filters']['all_of'][0]['value'])
        ender=next(v for p,id,loc,k,v in rows if p.endswith('/player.json') and loc.endswith('minecraft:ender_sword.minecraft:damage_sensor'));self.assertEqual(3,len(ender['triggers']));self.assertEqual([True,False,True],[x['deals_damage'] for x in ender['triggers']]);tnt=next(v for p,id,loc,k,v in rows if p.endswith('/tnt.json') and loc.endswith('giant_tnt.minecraft:explode'));self.assertEqual((8,16,True),(tnt['fuse_length'],tnt['power'],tnt['causes_fire']))

    def test_command_entity_calls_all_raw_summons_and_events(self):
        from build_command_entity_calls import extract,build_all,SUMSCAN,EVSCAN,code
        from build_entity_group_index import VERSIONS
        data={v:extract(f,p) for v,f,p in VERSIONS};self.assertEqual(data['2.8.8'],data['2.8.14']);self.assertEqual((194,125),(len(data['1.6'][0]),len(data['2.8.14'][0])));self.assertEqual((194,95),(sum(len(row[3]) for row in data['1.6'][0]),sum(len(row[3]) for row in data['2.8.14'][0])));self.assertEqual((0,35),(sum(len(row[4]) for row in data['1.6'][0]),sum(len(row[4]) for row in data['2.8.14'][0])));self.assertFalse(data['1.6'][5]);self.assertFalse(data['2.8.14'][5]);self.assertEqual((3,1),(len(data['1.6'][1]),len(data['2.8.14'][1])))
        for ver,filename,pack in VERSIONS:
            doc=(ROOT/'docs'/f'command-entity-calls-{ver if ver=="1.6" else "2.x"}.md').read_text();rows=data[ver][0]
            with zipfile.ZipFile(ROOT/'sources'/filename) as z:raw=[(p,n,l) for p in sorted(z.namelist()) if p.startswith(pack+'/') and p.endswith(('.json','.mcfunction','.js')) for n,l in enumerate(z.read(p).decode('utf-8-sig').splitlines(),1) if SUMSCAN.search(l) or EVSCAN.search(l)]
            self.assertEqual(raw,[(p,n,l) for p,n,l,s,e in rows])
            for path,n,line,summons,events in rows:self.assertIn(f'`{path}:{n}`',doc);self.assertIn(code(line),doc)
        for version,text in build_all().items():self.assertEqual(text,(ROOT/'docs'/f'command-entity-calls-{version}.md').read_text())
        calls,_,_,ids,events,_=data['2.8.14'];self.assertEqual(11,len(events['despawn']));self.assertIn(('minecraft:item','Swords_B/entities/item.json'),events['fire_sword_event_3']);self.assertNotIn('lightning_bolt',ids);self.assertIn('entity:living_flame',ids);six=next(row for row in calls if row[0].endswith('/quartz_diamond_ore.json'));self.assertEqual(('xp_orb',)*6,six[3]);self.assertIn(('@s','wet_sponge_sword'),[event for row in calls for event in row[4]])

    def test_function_ledger_covers_all_lines_and_literal_callers(self):
        from build_function_ledger import extract,build_all,SCAN,code
        from build_entity_group_index import VERSIONS
        data={v:extract(f,p) for v,f,p in VERSIONS};self.assertEqual(data['2.8.8'],data['2.8.14']);self.assertEqual((3,4),(len(data['1.6'][0]),len(data['2.8.14'][0])));self.assertEqual((50,197),tuple(sum(len(f['lines']) for f in data[v][0].values()) for v in ('1.6','2.8.14')));self.assertEqual((3,3),tuple(len(data[v][1]) for v in ('1.6','2.8.14')));self.assertFalse(data['1.6'][2]);self.assertFalse(data['2.8.14'][2])
        for version,filename,pack in VERSIONS:
            functions,calls,unknown=data[version];doc=(ROOT/'docs'/f'function-ledger-{version if version=="1.6" else "2.x"}.md').read_text()
            with zipfile.ZipFile(ROOT/'sources'/filename) as z:
                names=[p for p in z.namelist() if p.startswith(pack+'/functions/') and p.endswith('.mcfunction')];self.assertCountEqual(names,[f['path'] for f in functions.values()])
                for name,info in functions.items():
                    self.assertEqual(z.read(info['path']).decode('utf-8-sig').splitlines(),info['lines']);section=doc.split('### '+name+'\n',1)[1].split('\n### ',1)[0]
                    for i,line in enumerate(info['lines'],1):self.assertIn(f'| {i} | {code(line)} |',section)
                expected=[(p,i,l) for p in sorted(z.namelist()) if p.startswith(pack+'/') and p.endswith(('.json','.mcfunction','.js')) for i,l in enumerate(z.read(p).decode('utf-8-sig').splitlines(),1) if SCAN.search(l)];self.assertEqual(expected,[(p,i,l) for p,i,l,name in calls]);self.assertTrue(all(name in functions for _,_,_,name in calls))
        for version,text in build_all().items():self.assertEqual(text,(ROOT/'docs'/f'function-ledger-{version}.md').read_text())
        lines=data['2.8.14'][0]['give']['lines'];self.assertEqual(35,len(lines));self.assertEqual(34,sum(line.startswith('give @p ') for line in lines));self.assertIn('give @s effect:lightning_sword',lines);self.assertEqual(148,len(data['2.8.14'][0]['commands/swords_and_more_swords/swords_and_more_swords/jungle_sword']['lines']))

    def test_world_command_index_raw_lines_and_ice_version_diff(self):
        from build_world_command_index import extract,build_all,PATS,code
        from build_entity_group_index import VERSIONS
        data={v:extract(f,p) for v,f,p in VERSIONS};self.assertEqual((412,331,330),tuple(len(data[v]) for v in ('1.6','2.8.8','2.8.14')))
        for ver,filename,pack in VERSIONS:
            doc=(ROOT/'docs'/f'world-command-index-{ver}.md').read_text()
            with zipfile.ZipFile(ROOT/'sources'/filename) as z:raw=[(p,i,l) for p in sorted(z.namelist()) if p.startswith(pack+'/') and p.endswith(('.json','.mcfunction','.js')) for i,l in enumerate(z.read(p).decode('utf-8-sig').splitlines(),1) if any(pattern.search(l) for pattern in PATS.values())]
            self.assertEqual(raw,[(p,i,l) for p,i,l,labels in data[ver]])
            for path,line,text,labels in data[ver]:self.assertIn(f'`{path}:{line}`',doc);self.assertIn(code(text),doc);self.assertTrue(labels)
        a={(p,n):(t,labels) for p,n,t,labels in data['2.8.8']};b={(p,n):(t,labels) for p,n,t,labels in data['2.8.14']};self.assertEqual({('Swords_B/blocks/fake_ice.json',107)},set(a)-set(b));self.assertFalse(set(b)-set(a));changed=[k for k in a.keys()&b.keys() if a[k]!=b[k]];self.assertEqual({'Swords_B/items/ice_sword.json':40,'Swords_B/entities/player.json':10},dict(collections.Counter(k[0] for k in changed)));self.assertTrue(all(a[k][0].replace('effect99:fake_ice','frosted_ice')==b[k][0] for k in changed));self.assertTrue(any(p.endswith('entities/creeper.json') and 'structure load creeper_sword' in text for p,n,text,labels in data['2.8.14']));self.assertTrue(any(p.endswith('/scripts/javascript.js') and '${x}' in text and 'loot spawn' in labels for p,n,text,labels in data['2.8.14']))
        for ver,text in build_all().items():self.assertEqual(text,(ROOT/'docs'/f'world-command-index-{ver}.md').read_text())

    def test_entity_timer_sensor_components_and_missing_fields(self):
        from build_entity_combat_index import extract,code
        from build_entity_trigger_index import KEYS,build_all
        from build_entity_group_index import VERSIONS
        data={v:extract(f,p,KEYS) for v,f,p in VERSIONS};self.assertEqual(data['2.8.8'],data['2.8.14']);self.assertEqual((2,98),(len(data['1.6'][0]),len(data['2.8.14'][0])));self.assertEqual((3,1),(len(data['1.6'][1]),len(data['2.8.14'][1])))
        rows=data['2.8.14'][0];counts=collections.Counter(x[3] for x in rows);self.assertEqual({'minecraft:timer':54,'minecraft:environment_sensor':29,'minecraft:block_sensor':1,'minecraft:ageable':7,'minecraft:on_target_acquired':6,'minecraft:on_wake_with_owner':1},dict(counts));timers=[value for _,_,_,key,value in rows if key=='minecraft:timer'];self.assertEqual(2,sum(x=={} for x in timers));self.assertEqual(36,sum('randomInterval' not in x for x in timers));self.assertEqual(2,sum('time' not in x for x in timers));self.assertEqual(2,sum('looping' not in x for x in timers))
        expected_empty={(p,loc) for p,id,loc,k,v in rows if k=='minecraft:timer' and v=={}};self.assertEqual({('Swords_B/entities/ghost_projectile.json','$.minecraft:entity.component_groups.teleport_enable.minecraft:timer'),('Swords_B/entities/player.json','$.minecraft:entity.component_groups.minecraft:default_player.minecraft:timer')},expected_empty)
        for ver,filename,pack in VERSIONS:
            expected=[]
            with zipfile.ZipFile(ROOT/'sources'/filename) as z:
                for path in sorted(z.namelist()):
                    if not path.startswith(pack+'/entities/') or not path.endswith('.json'):continue
                    try:e=json5.loads(z.read(path).decode('utf-8-sig'))['minecraft:entity']
                    except (ValueError,KeyError):continue
                    groups=[('$.minecraft:entity.components',e.get('components',{}))]+[('$.minecraft:entity.component_groups.'+k,v) for k,v in e.get('component_groups',{}).items()]
                    for loc,obj in groups:
                        for key,value in obj.items():
                            if key in KEYS:expected.append((path,e['description']['identifier'],loc+'.'+key,key,value))
            self.assertEqual(expected,data[ver][0]);doc=(ROOT/'docs'/f'entity-trigger-index-{ver if ver=="1.6" else "2.x"}.md').read_text()
            for path,ident,loc,key,value in expected:self.assertIn('`'+loc+'`',doc);self.assertIn(code(value),doc)
        for version,text in build_all().items():self.assertEqual(text,(ROOT/'docs'/f'entity-trigger-index-{version}.md').read_text())

    def test_basic_sword_comparative_manual_sources(self):
        names=('coal','cactus','emerald','lapis','glass');doc=(ROOT/'docs/manual-basic-swords.md').read_text()
        with zipfile.ZipFile(ROOT/'sources/SwordsAndMoreSwords.1.6.mcaddon') as old, zipfile.ZipFile(ROOT/'sources/swordsandmoreswords_2_8_8.mcaddon') as v88, zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as new:
            load=lambda z,p:json5.loads(z.read(p).decode('utf-8-sig'))
            oldp=load(old,'Sword_B/entities/player.json')['minecraft:entity'];p88=load(v88,'Swords_B/entities/player.json')['minecraft:entity'];p=load(new,'Swords_B/entities/player.json')['minecraft:entity']
            olditems={name:load(old,'Sword_B/items/'+name+'_sword.json')['minecraft:item'] for name in names if name!='glass'};items={name:load(new,'Swords_B/items/'+name+'_sword.json')['minecraft:item'] for name in names}
            for name in names:self.assertEqual(v88.read('Swords_B/items/'+name+'_sword.json'),new.read('Swords_B/items/'+name+'_sword.json'));self.assertIn('## '+name.title()+' Sword',doc)
            self.assertEqual([(6,121),(6,125),(7,2300),(6,528)],[(olditems[k]['components']['minecraft:damage'],olditems[k]['components']['minecraft:durability']['max_durability']) for k in names[:-1]]);self.assertEqual([(4,121),(6,125),(7,2300),(5,528),(33,1)],[(items[k]['components']['minecraft:damage'],items[k]['components']['minecraft:durability']['max_durability']) for k in names]);self.assertNotIn('minecraft:fuel',olditems['coal']['components']);self.assertEqual(360,items['coal']['components']['minecraft:fuel']['duration'])
            for name in names[:-1]:
                self.assertTrue(olditems[name]['components']['minecraft:allow_off_hand']);self.assertFalse(items[name]['components']['minecraft:allow_off_hand']);self.assertNotIn('minecraft:weapon',olditems[name]['components']);grp=oldp['component_groups']['minecraft:'+name+'_sword']['minecraft:spawn_entity'][0];self.assertEqual({'min_wait_time':0,'max_wait_time':0,'spawn_entity':'entity:'+name,'num_to_spawn':1,'single_use':True},grp)
                ctrl=load(old,'Sword_B/animation_controllers/'+name+'_sword.json')['animation_controllers']['controller.animation.'+name]['states'];self.assertEqual(ctrl['default']['on_entry'],ctrl[name]['on_entry']);self.assertEqual('/scoreboard players set @a swords 2',ctrl['default']['on_entry'][-1])
            coal=load(old,'Sword_B/animation_controllers/coal_sword.json')['animation_controllers']['controller.animation.coal']['states']['default']['on_entry'];self.assertEqual(13,len(coal)-1);self.assertEqual(['/replaceitem block ~-1 ~ ~ slot.container 1 coal','/replaceitem block ~1 ~ ~ slot.container 1 coal','/replaceitem block ~ ~ ~-1 slot.container 1 coal','/replaceitem block ~ ~ ~1 slot.container 1 coal','/replaceitem block ~ ~-1 ~ slot.container 1 coal','/replaceitem block ~-1 ~1 ~ slot.container 1 coal','/replaceitem block ~1 ~1 ~ slot.container 1 coal','/replaceitem block ~ ~1 ~-1 slot.container 1 coal','/replaceitem block ~ ~1 ~1 slot.container 1 coal','/replaceitem block ~-1 ~-1 ~ slot.container 1 coal','/replaceitem block ~1 ~-1 ~ slot.container 1 coal','/replaceitem block ~ ~-1 ~-1 slot.container 1 coal','/replaceitem block ~ ~-1 ~1 slot.container 1 coal'],coal[:-1])
            cactus=load(old,'Sword_B/animation_controllers/cactus_sword.json')['animation_controllers']['controller.animation.cactus']['states']['default']['on_entry'];self.assertIn('/execute @e[scores={ct=1},r=2] ~ ~ ~ effect @s poison 1 1 true',cactus);self.assertIn('/scoreboard players add @e[r=3,type=!entity:cactus,type=!player] ct 1',cactus)
            for name in ('cactus','emerald','lapis'):
                self.assertEqual(p88['component_groups']['minecraft:'+name+'_sword'],p['component_groups']['minecraft:'+name+'_sword']);self.assertEqual(p88['events']['minecraft:'+name+'_sword'],p['events']['minecraft:'+name+'_sword']);self.assertEqual(p88['events']['stop_'+name+'_sword_event'],p['events']['stop_'+name+'_sword_event'])
            self.assertNotIn('coal_sword',new.read('Swords_B/entities/player.json').decode('utf-8-sig'));self.assertNotIn('glass_sword',new.read('Swords_B/entities/player.json').decode('utf-8-sig'));self.assertEqual([0.5,0.5],p['component_groups']['minecraft:cactus_sword']['minecraft:timer']['time']);self.assertEqual(['damage @e[r=1.4,type=!player] 1 contact entity @s','damage @s 1 contact'],p['events']['cactus_sword_skills']['run_command']['command']);self.assertEqual([2.5,6.0],p['component_groups']['minecraft:lapis_sword']['minecraft:timer']['time']);self.assertTrue(p['component_groups']['minecraft:lapis_sword']['minecraft:timer']['randomInterval']);self.assertEqual('is_in_village',p['events']['minecraft:emerald_sword']['sequence'][1]['filters']['all_of'][0]['test'])
            for name in ('coal','cactus'):
                recipe='recipes/'+name+'_sword.json';self.assertEqual(load(old,'Sword_B/'+recipe),load(new,'Swords_B/'+recipe));self.assertEqual(new.read('Swords_B/'+recipe),v88.read('Swords_B/'+recipe))
            self.assertIn('Sword_B/recipes/emerald sword.json',old.namelist());self.assertIn('Sword_B/recipes/lapis_sword.json',old.namelist());self.assertFalse(any(path.startswith('Swords_B/recipes/') and path.endswith('.json') and any('effect:'+n+'_sword' in json.dumps(load(new,path).get('minecraft:recipe_shaped',{}).get('result',{})) for n in ('emerald','lapis','glass')) for path in new.namelist()))
            glass=items['glass']['components'];self.assertEqual(25,glass['minecraft:digger']['destroy_speeds'][0]['speed']);self.assertEqual(15,glass['minecraft:digger']['destroy_speeds'][1]['speed']);self.assertIn('on_dig',glass['minecraft:digger']);self.assertEqual(10,items['glass']['events']['weapon']['sequence'][0]['damage']['amount']);self.assertEqual(['playsound random.glass @a[r=8,m=0]'],items['glass']['events']['weapon']['sequence'][0]['run_command']['command']);self.assertEqual({'effect:glass_sword','minecraft:glass'},set(x['items'][0] for x in glass['minecraft:repairable']['repair_items']));self.assertNotIn('Sword_B/items/glass_sword.json',old.namelist())
            for path,index,total in [('chests/spawn_bonus_chest',0,5),('chests/stronghold_corridor',0,521),('chests/stronghold_library',0,275),('chests/woodland_mansion',0,670)]:
                pool=load(new,'Swords_B/loot_tables/'+path+'.json')['pools'][index];self.assertTrue(all('weight' in e for e in pool['entries']));self.assertEqual(total,sum(e['weight'] for e in pool['entries']))
            pool=load(new,'Swords_B/loot_tables/chests/pillager_outpost.json')['pools'][3];self.assertTrue(any('weight' not in e for e in pool['entries']));self.assertEqual(3,next(e['weight'] for e in pool['entries'] if e.get('name')=='effect:lapis_sword'))
            self.assertIn('Swords_B/trading/weapon_smith_trades.json',v88.namelist());self.assertNotIn('Swords_B/trading/weapon_smith_trades.json',new.namelist());self.assertIn('effect.glass_sword.text.3=-Repairable: false',new.read('Swords_R/texts/en_US.lang').decode('utf-8-sig'))

    def test_heat_light_sword_cards_compare_literal_sources(self):
        doc=(ROOT/'docs/manual-heat-light-swords.md').read_text();names=('obsidian','magma','glowstone','wither_skeleton')
        with zipfile.ZipFile(ROOT/'sources/SwordsAndMoreSwords.1.6.mcaddon') as old,zipfile.ZipFile(ROOT/'sources/swordsandmoreswords_2_8_8.mcaddon') as v88,zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as new:
            load=lambda z,p:json5.loads(z.read(p).decode('utf-8-sig'))
            p=load(new,'Swords_B/entities/player.json')['minecraft:entity'];p88=load(v88,'Swords_B/entities/player.json')['minecraft:entity'];oldp=load(old,'Sword_B/entities/player.json')['minecraft:entity']
            for name in names:
                self.assertIn('## '+name.replace('_',' ').title()+' Sword',doc);path='Swords_B/items/'+name+'_sword.json';self.assertEqual(new.read(path),v88.read(path))
            for name in ('obsidian','magma','glowstone'):
                self.assertEqual(p['events']['minecraft:'+name+'_sword'],p88['events']['minecraft:'+name+'_sword']);self.assertEqual(oldp['component_groups']['minecraft:'+name+'_sword']['minecraft:spawn_entity'][0]['num_to_spawn'],1)
            self.assertEqual(p['component_groups']['minecraft:obsidian_sword'],p88['component_groups']['minecraft:obsidian_sword']);self.assertEqual(p['component_groups']['minecraft:magma_sword'],p88['component_groups']['minecraft:magma_sword'])
            def state(name,key):
                states=load(old,'Sword_B/animation_controllers/'+name+'_sword.json')['animation_controllers']['controller.animation.'+key]['states'];self.assertEqual(states['default']['on_entry'],states[key]['on_entry']);return states['default']['on_entry']
            obs=state('obsidian','ob');self.assertEqual(13,len(obs));self.assertEqual(2,sum(' fill ' in x for x in obs));self.assertEqual(10,sum(' fire_resistance ' in x for x in obs));self.assertTrue(all('@a' in x for x in obs));self.assertIn('replace flowing_lava 0',obs[1]);self.assertEqual('/scoreboard players set @a swords 2',obs[-1])
            magma=state('magma','magma');self.assertEqual(21,sum(' setblock ~ ~ ~ fire' in x for x in magma));self.assertIn('/execute @p ~ ~ ~ fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 magma 0 replace lava',magma);glow=state('glowstone','glow');self.assertEqual(4,len(glow));self.assertEqual(glow[0],glow[2]);self.assertIn('~5 ~5 ~5 ~-5 ~-5 ~-5 air 0 replace light_block 15',glow[1])
            rec=load(old,'Sword_B/recipes/glowstone_sword.json')['minecraft:recipe_shaped'];self.assertEqual(['020','020','010'],rec['pattern']);self.assertNotIn('0',rec['key']);self.assertEqual(['2','2','1'],load(new,'Swords_B/recipes/glowstone_sword.json')['minecraft:recipe_shaped']['pattern']);self.assertTrue(load(old,'Sword_B/items/glowstone_sword.json')['minecraft:item']['components']['minecraft:allow_off_hand']);self.assertTrue(load(new,'Swords_B/items/glowstone_sword.json')['minecraft:item']['components']['minecraft:allow_off_hand'])
            item=load(new,'Swords_B/items/obsidian_sword.json')['minecraft:item'];branches=item['events']['weapon']['randomize'];self.assertEqual([(55,1),(30,2),(15,3)],[(x['weight'],x['damage']['amount']) for x in branches]);self.assertEqual(160,sum(x['weight']*x['damage']['amount'] for x in branches));trig=p['component_groups']['minecraft:obsidian_sword']['minecraft:damage_sensor']['triggers'];self.assertFalse(trig['deals_damage']);self.assertEqual({'block_explosion','entity_explosion'},{x['value'] for x in trig['on_damage']['filters']['any_of']})
            seq=p['events']['minecraft:magma_sword']['sequence'];self.assertEqual([99,1],[x['weight'] for x in seq[2]['randomize']]);self.assertEqual({'test':'in_water','operator':'=='},seq[2]['filters']);commands=seq[1]['run_command']['command'];self.assertEqual(5,sum(x.startswith('fill ') for x in commands));expected=['fill ~ ~-1 ~ ~ ~-1 ~ magma 0 replace lava','fill ~1 ~-1 ~1 ~ ~-1 ~ magma 0 replace lava','fill ~ ~-1 ~1 ~ ~-1 ~1 magma 0 replace lava','fill ~-1 ~-1 ~ ~-1 ~-1 ~ magma 0 replace lava','fill ~ ~-1 ~-1 ~ ~-1 ~-1 magma 0 replace lava'];self.assertEqual(expected,commands[:5]);spots=[(0,0),(0,0),(0,1),(1,0),(1,1),(0,1),(-1,0),(0,-1)];self.assertEqual((8,6),(len(spots),len(set(spots))))
            light=load(new,'Swords_B/blocks/lightblock.json')['minecraft:block']['components'];self.assertEqual((1,999,[0.2,0.2]),(light['minecraft:block_light_emission'],light['minecraft:explosion_resistance'],light['minecraft:ticking']['range']));self.assertNotIn('minecraft:glowstone_sword',p['component_groups']);self.assertNotIn('stop_glowstone_sword_event',p['events'])
            self.assertNotIn('Sword_B/items/wither_skeleton_sword.json',old.namelist());we=load(new,'Swords_B/entities/wither_effect.json')['minecraft:entity'];mob=we['components']['minecraft:projectile']['on_hit']['mob_effect'];self.assertEqual((200,200,200,0),(mob['durationeasy'],mob['durationnormal'],mob['durationhard'],mob['amplifier']));self.assertEqual([0.1,0.1],we['components']['minecraft:timer']['time']);self.assertNotIn('particle',we['events']);pool=load(new,'Swords_B/loot_tables/entities/wither_skeleton.json')['pools'][3];self.assertEqual([{'condition':'killed_by_player'},{'condition':'random_chance_with_looting','chance':0.025,'looting_multiplier':0.02}],pool['conditions']);self.assertEqual('effect:wither_skeleton_sword',pool['entries'][0]['name'])
            pool=load(new,'Swords_B/loot_tables/chests/underwater_ruin_big.json')['pools'][1];self.assertEqual((1,24),(pool['rolls'],sum(x['weight'] for x in pool['entries'])));self.assertEqual(1,next(x['weight'] for x in pool['entries'] if x.get('name')=='effect:magma_sword'))

    def test_companion_projectile_cards_and_malformed_helpers(self):
        doc=(ROOT/'docs/manual-companion-projectile-swords.md').read_text();names=('blaze','bone','shulker')
        with zipfile.ZipFile(ROOT/'sources/SwordsAndMoreSwords.1.6.mcaddon') as old,zipfile.ZipFile(ROOT/'sources/swordsandmoreswords_2_8_8.mcaddon') as v88,zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as new:
            load=lambda z,p:json5.loads(z.read(p).decode('utf-8-sig'));oldp=load(old,'Sword_B/entities/player.json')['minecraft:entity'];p=load(new,'Swords_B/entities/player.json')['minecraft:entity'];p88=load(v88,'Swords_B/entities/player.json')['minecraft:entity']
            for name,damage,old_damage,dur,old_dur,projectile,objective,threshold in [('blaze',6,8,2300,2300,'minecraft:small_fireball','b',10),('bone',5,7,820,820,'minecraft:arrow','bn',10),('shulker',6,7,2609,1000,'minecraft:shulker_bullet','sh',40)]:
                self.assertIn('## '+name.title()+' Sword',doc);path='Swords_B/items/'+name+'_sword.json';self.assertEqual(new.read(path),v88.read(path));item=load(new,path)['minecraft:item'];previous=load(old,'Sword_B/items/'+name+'_sword.json')['minecraft:item'];self.assertEqual((damage,dur,False),(item['components']['minecraft:damage'],item['components']['minecraft:durability']['max_durability'],item['components']['minecraft:allow_off_hand']));self.assertEqual((old_damage,old_dur,True),(previous['components']['minecraft:damage'],previous['components']['minecraft:durability']['max_durability'],previous['components']['minecraft:allow_off_hand']));self.assertNotIn('minecraft:weapon',previous['components']);self.assertEqual({'on_hurt_entity','on_not_hurt_entity','on_hit_block'},set(item['components']['minecraft:weapon']));self.assertEqual(p['events']['minecraft:'+name+'_sword'],p88['events']['minecraft:'+name+'_sword']);self.assertEqual(p['component_groups']['minecraft:'+name+'_sword'],p88['component_groups']['minecraft:'+name+'_sword'])
                recipe=load(old,'Sword_B/recipes/'+name+'_sword.json')['minecraft:recipe_shaped'];self.assertEqual(['F','F','E'],recipe['pattern']);self.assertEqual('effect:'+name+'_sword',recipe['result']['item']);spawn=oldp['component_groups']['minecraft:'+name+'_sword']['minecraft:spawn_entity'][0];self.assertEqual(('entity:'+name,0,0,1,True),(spawn['spawn_entity'],spawn['min_wait_time'],spawn['max_wait_time'],spawn['num_to_spawn'],spawn['single_use']))
                ctr=load(old,'Sword_B/animation_controllers/'+name+'_sword.json')['animation_controllers']['controller.animation.'+name]['states'];lines=ctr['default']['on_entry'];self.assertEqual(lines,ctr[name]['on_entry']);self.assertTrue(any('scoreboard objectives add '+objective+' dummy' in x for x in lines));self.assertTrue(any('scores={'+objective+'='+str(threshold)+'}' in x and 'summon entity:'+name+'2' in x for x in lines));self.assertTrue(any('kill @e[type=entity:'+name+'2,r=5] ~ 0 ~' in x for x in lines))
                raw=old.read('Sword_B/entities/'+name+'2.json').decode('utf-8-sig');self.assertRaises(ValueError,json5.loads,raw);pos=raw.rfind('}');hypothesis=json5.loads(raw[:pos]+raw[pos+1:])['minecraft:entity'];self.assertEqual(projectile,hypothesis['components']['minecraft:shooter']['def'])
            blaze=load(new,'Swords_B/items/blaze_sword.json')['minecraft:item'];self.assertEqual([14,1,85],[x['weight'] for x in blaze['events']['weapon']['sequence'][1]['randomize']]);self.assertEqual(10,blaze['events']['on_use']['damage']['amount']);self.assertEqual([6,6],p['component_groups']['blaze_sword_skill']['minecraft:timer']['time']);fire=p['component_groups']['shoot_small_fireball'];self.assertEqual(4,len(fire['minecraft:spawn_entity']));self.assertEqual([2,2],fire['minecraft:timer']['time']);self.assertEqual(125,sum(x['weight'] for x in p['events']['minecraft:blaze_sword']['sequence'][2]['randomize']));self.assertNotIn('blaze_sword_skill',p['events']['stop_blaze_sword_event']['sequence'][0]['remove']['component_groups']);self.assertNotIn('Swords_B/structures/blaze_sword.mcstructure',new.namelist())
            bone=load(new,'Swords_B/items/bone_sword.json')['minecraft:item'];self.assertEqual([20,80],[x['weight'] for x in bone['events']['weapon']['sequence'][1]['randomize']]);sk=load(new,'Swords_B/entities/skeleton.json')['minecraft:entity']['events']['bone_sword'];self.assertEqual([993,7],[x['weight'] for x in sk['sequence'][0]['randomize']]);grow=load(new,'Swords_B/entities/grows_crop.json')['minecraft:entity'];self.assertEqual((0.5,10),(grow['components']['minecraft:grows_crop']['chance'],grow['components']['minecraft:grows_crop']['charges']));children=grow['events']['grows_crop']['run_command']['command'];self.assertEqual(13,len(children));self.assertTrue(all('grows_crop_event' not in x for x in children))
            sh=load(new,'Swords_B/items/shulker_sword.json')['minecraft:item'];self.assertEqual([10,90],[x['weight'] for x in sh['events']['weapon']['sequence'][1]['randomize']]);self.assertIn('effect @e[r=6,family=!shulker_sword] levitation 1 18 false',sh['events']['on_use']['run_command']['command']);self.assertEqual(8,sh['events']['on_use']['damage']['amount']);self.assertNotIn('shulker_sword_skill',p['events']['stop_shulker_sword_event']['sequence'][0]['remove']['component_groups']);shield=load(new,'Swords_B/entities/shulker_shield.json')['minecraft:entity'];self.assertIn('effect @p[r=1,family=shulker_sword] instant_damage 1 2 true',shield['events']['damage_player']['run_command']['command']);pool=load(new,'Swords_B/loot_tables/entities/shulker.json')['pools'][1];self.assertEqual(0.045,pool['conditions'][1]['chance']);self.assertEqual(0.02,pool['conditions'][1]['looting_multiplier'])

    def test_ender_wither_tnt_slime_manual_literal_comparison(self):
        with zipfile.ZipFile(ROOT/'sources/SwordsAndMoreSwords.1.6.mcaddon') as old, zipfile.ZipFile(ROOT/'sources/swordsandmoreswords_2_8_8.mcaddon') as v88, zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as new:
            load=lambda z,p:json5.loads(z.read(p).decode('utf-8-sig'));op=load(old,'Sword_B/entities/player.json')['minecraft:entity'];p=load(new,'Swords_B/entities/player.json')['minecraft:entity'];p88=load(v88,'Swords_B/entities/player.json')['minecraft:entity'];doc=(ROOT/'docs/manual-ender-wither-tnt-slime.md').read_text()
            for n in ('ender','wither','tnt','slime'):
                self.assertIn('## '+('TNT' if n=='tnt' else n.title())+' Sword',doc);self.assertEqual(v88.read('Swords_B/items/'+n+'_sword.json'),new.read('Swords_B/items/'+n+'_sword.json'));self.assertEqual(p['events'].get('minecraft:'+n+'_sword'),p88['events'].get('minecraft:'+n+'_sword'));self.assertEqual(op['component_groups']['minecraft:'+n+'_sword']['minecraft:spawn_entity'][0]['num_to_spawn'],1)
            self.assertNotIn('minecraft:tnt_sword',p['events']);oldender=op['component_groups']['minecraft:ender_sword'];self.assertEqual({'random_teleports':True,'max_random_teleport_time':30,'random_teleport_cube':[32,32,32],'target_distance':16,'target_teleport_chance':0.05,'light_teleport_chance':0.05},oldender['minecraft:teleport']);self.assertEqual({'test':'in_water_or_rain','operator':'==','value':True},oldender['minecraft:hurt_on_condition']['damage_conditions'][0]['filters']);self.assertNotIn('minecraft:teleport',p['component_groups']['minecraft:ender_sword']);triggers=p['component_groups']['minecraft:ender_sword']['minecraft:damage_sensor']['triggers'];self.assertEqual([True,False,True],[t['deals_damage'] for t in triggers]);self.assertEqual({'test':'in_water_or_rain'},p['component_groups']['minecraft:ender_sword']['minecraft:hurt_on_condition']['damage_conditions'][0]['filters']);self.assertEqual([50,50],[x['weight'] for x in p['events']['ender_sword_skill']['sequence'][1]['randomize']])
            for n,key in [('ender','ender'),('tnt','tnt'),('slime','slime')]:
                states=load(old,'Sword_B/animation_controllers/'+n+'_sword.json')['animation_controllers']['controller.animation.'+key]['states'];self.assertEqual(states['default']['on_entry'],states[key]['on_entry'])
            states=load(old,'Sword_B/animation_controllers/wither_sword.json')['animation_controllers']['controller.animation.wither']['states'];self.assertEqual(['/Effect99'],states['default']['on_entry']);self.assertEqual(46,len(states['wither']['on_entry']));self.assertEqual(10,sum(x.startswith('/fill ') for x in states['wither']['on_entry']));cmds=p['events']['minecraft:wither_sword']['sequence'][1]['run_command']['command'];self.assertEqual(13,sum(x.startswith('fill ') for x in cmds));self.assertEqual(11,sum(x.startswith('fill ~5 ') for x in cmds));self.assertTrue(any(x.endswith('replace vine') for x in cmds));self.assertIn('effect @s wither 39960 1 true',cmds)
            wr=load(old,'Sword_B/recipes/wither_sword.json')['minecraft:recipe_shaped'];self.assertEqual(['#SS','SBS','NS#'],wr['pattern']);self.assertNotIn('#',wr['key']);self.assertEqual('minecraft:netherstar',wr['key']['B']['item'])
            tnt=load(new,'Swords_B/items/tnt_sword.json')['minecraft:item'];self.assertNotIn('minecraft:digger',tnt['components']);self.assertEqual([10,90],[x['weight'] for x in tnt['events']['weapon']['sequence'][1]['randomize']]);self.assertEqual('entity:tnt',tnt['events']['weapon']['sequence'][1]['randomize'][1]['shoot']['projectile']);self.assertIn('summon minecraft:tnt ~~~ giant_tnt',tnt['events']['on_use']['run_command']['command']);pool=load(new,'Swords_B/loot_tables/chests/desert_pyramid.json')['pools'][0];self.assertEqual(242,sum(x['weight'] for x in pool['entries']));self.assertEqual(10,next(x['weight'] for x in pool['entries'] if x.get('name')=='effect:tnt_sword'))
            slime=p['events']['minecraft:slime_sword']['sequence'];self.assertNotIn('filters',slime[1]);commands=p['events']['slime_sword_skills']['run_command']['command'];self.assertTrue(commands[0].startswith('ride @s summon_ride'));self.assertEqual('scoreboard objectives add slime_despawn dummy',commands[1]);mount=load(new,'Swords_B/entities/mountable_slime.json')['minecraft:entity'];self.assertNotEqual(mount['events']['minecraft:despawn'],mount['events']['despawn']);self.assertNotIn('minecraft:loot',load(new,'Swords_B/entities/slime_king.json')['minecraft:entity']['components'])

    def test_quartz_bedrock_recipe_dependency_and_source_limits(self):
        with zipfile.ZipFile(ROOT/'sources/SwordsAndMoreSwords.1.6.mcaddon') as old, zipfile.ZipFile(ROOT/'sources/swordsandmoreswords_2_8_8.mcaddon') as v88, zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as new:
            load=lambda z,p:json5.loads(z.read(p).decode('utf-8-sig'));op=load(old,'Sword_B/entities/player.json')['minecraft:entity'];p=load(new,'Swords_B/entities/player.json')['minecraft:entity'];doc=(ROOT/'docs/manual-quartz-bedrock-progression.md').read_text()
            self.assertIn('20',doc);self.assertEqual({},op['component_groups']['minecraft:quartz_sword']);r=load(old,'Sword_B/recipes/quartz_sword.json')['minecraft:recipe_shaped'];self.assertEqual(['#','#','0'],r['pattern']);self.assertIsInstance(r['result'],list);self.assertEqual([{'item':'effect:quartz_sword','data':0,'count':1}],r['result'])
            recipes={name:load(new,'Swords_B/recipes/'+name+'.json')['minecraft:recipe_shaped'] for name in ('quartz_diamond_block','quartz_diamond_stick','quartz_diamond_sword','bedrock_stick','bedrock_sword')}
            for n,r in recipes.items():self.assertEqual(v88.read('Swords_B/recipes/'+n+'.json'),new.read('Swords_B/recipes/'+n+'.json'));self.assertNotIn('count',r['result'])
            self.assertEqual((['###','###','###'],'effect:quartz_diamond','effect99:quartz_diamond_block'),(recipes['quartz_diamond_block']['pattern'],recipes['quartz_diamond_block']['key']['#']['item'],recipes['quartz_diamond_block']['result']['item']));self.assertEqual((['#','#'],'effect:quartz_diamond'),(recipes['quartz_diamond_stick']['pattern'],recipes['quartz_diamond_stick']['key']['#']['item']));self.assertEqual('effect:quartz_diamond_stick',recipes['quartz_diamond_sword']['key']['#']['item']);self.assertEqual('effect99:quartz_diamond_block',recipes['quartz_diamond_sword']['key']['Q']['item']);self.assertEqual(20,2*sum(row.count('#') for row in recipes['quartz_diamond_block']['pattern'])+sum(row.count('#') for row in recipes['quartz_diamond_stick']['pattern']))
            self.assertEqual((['#','#'],'minecraft:bedrock'),(recipes['bedrock_stick']['pattern'],recipes['bedrock_stick']['key']['#']['item']));self.assertEqual((['B','B','#'],'minecraft:bedrock','effect:bedrock_stick'),(recipes['bedrock_sword']['pattern'],recipes['bedrock_sword']['key']['B']['item'],recipes['bedrock_sword']['key']['#']['item']))
            for name in ('quartz_diamond','quartz_diamond_stick','quartz_sword','bedrock_stick','bedrock_sword'):self.assertEqual(v88.read('Swords_B/items/'+name+'.json'),new.read('Swords_B/items/'+name+'.json'))
            stick=load(new,'Swords_B/items/quartz_diamond_stick.json')['minecraft:item'];branches=stick['events']['weapon']['randomize'];self.assertEqual([10,85,5],[b['weight'] for b in branches]);self.assertEqual(295,sum(b['weight']*int(b['run_command']['command'][0].split()[2]) for b in branches))
            for name in ('bedrock_stick','bedrock_sword'):
                c=load(new,'Swords_B/items/'+name+'.json')['minecraft:item']['components'];self.assertEqual({},c['minecraft:weapon']);self.assertNotIn('minecraft:durability',c);self.assertNotIn('minecraft:repairable',c);self.assertNotIn('minecraft:enchantable',c)
            rules=load(new,'Swords_B/items/bedrock_sword.json')['minecraft:item']['components']['minecraft:digger']['destroy_speeds'];self.assertEqual(68,len(rules));self.assertFalse(any(x.get('block')=='minecraft:bedrock' for x in rules));self.assertTrue(any(x.get('block')=='minecraft:pumkin' for x in rules))
            ore=load(new,'Swords_B/blocks/quartz_diamond_ore.json')['minecraft:block'];self.assertEqual('loot_tables/blocks/null.json',ore['components']['minecraft:loot']);self.assertNotIn('Swords_B/loot_tables/blocks/null.json',new.namelist());pool=load(new,'Swords_B/loot_tables/blocks/quartz_diamond_ore.json')['pools'][0];self.assertEqual([89,10,1],[e['weight'] for e in pool['entries']]);self.assertEqual(6,sum('summon xp_orb' in x for x in ore['events']['quartz_diamond_ore']['run_command']['command']))
            for path in ('Swords_B/features/quartz_diamond_ore.json','Swords_B/feature_rules/quartz_diamond_ore_feature.json','Swords_B/structures/quartz_diamond_ore.mcstructure'):self.assertIn(path,v88.namelist());self.assertNotIn(path,new.namelist())
            quartz=load(new,'Swords_B/items/quartz_sword.json')['minecraft:item'];self.assertEqual(10,quartz['events']['weapon']['sequence'][0]['damage']['amount']);self.assertIn('effect @a[r=1] instant_damage 1 99 true',quartz['events']['weapon']['sequence'][1]['run_command']['command']);self.assertIn('damage @s 14 magic',p['events']['minecraft:quartz_sword']['sequence'][0]['run_command']['command']);self.assertIn('damage @s 14 magic',p['events']['stop_quartz_sword_event']['sequence'][0]['run_command']['command'])

    def test_fire_spider_sponge_comparison_and_world_operations(self):
        with zipfile.ZipFile(ROOT/'sources/SwordsAndMoreSwords.1.6.mcaddon') as old,zipfile.ZipFile(ROOT/'sources/swordsandmoreswords_2_8_8.mcaddon') as v88,zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as new:
            load=lambda z,p:json5.loads(z.read(p).decode('utf-8-sig'));op=load(old,'Sword_B/entities/player.json')['minecraft:entity'];p=load(new,'Swords_B/entities/player.json')['minecraft:entity'];doc=(ROOT/'docs/manual-fire-spider-sponge.md').read_text()
            for n,count in [('fire',39),('spider',31),('sponge',13)]:
                states=load(old,'Sword_B/animation_controllers/'+n+'_sword.json')['animation_controllers']['controller.animation.'+n]['states'];self.assertEqual(states['default']['on_entry'],states[n]['on_entry']);self.assertEqual(count,len(states[n]['on_entry']));self.assertEqual('entity:'+n,op['component_groups']['minecraft:'+n+'_sword']['minecraft:spawn_entity'][0]['spawn_entity']);self.assertEqual(p['events']['minecraft:'+n+'_sword'],load(v88,'Swords_B/entities/player.json')['minecraft:entity']['events']['minecraft:'+n+'_sword'])
            for n in ('fire','spider','sponge','wet_sponge'):self.assertEqual(v88.read('Swords_B/items/'+n+'_sword.json'),new.read('Swords_B/items/'+n+'_sword.json'))
            fire=load(old,'Sword_B/animation_controllers/fire_sword.json')['animation_controllers']['controller.animation.fire']['states']['default']['on_entry'];self.assertEqual(31,sum(' setblock ~ ~ ~ fire' in c and '@e[' in c for c in fire));self.assertEqual(5,sum(' fill ' in c for c in fire));spider=load(old,'Sword_B/animation_controllers/spider_sword.json')['animation_controllers']['controller.animation.spider']['states']['default']['on_entry'];self.assertEqual(25,sum('web 0 replace air' in c for c in spider));sponge=load(old,'Sword_B/animation_controllers/sponge_sword.json')['animation_controllers']['controller.animation.sponge']['states']['default']['on_entry'];self.assertEqual(10,sum(' detect ' in c and 'replace seagrass' in c for c in sponge));self.assertIn('air 0 replace sponge',sponge[1])
            for n in ('fire','spider'):
                r=load(old,'Sword_B/recipes/'+n+'_sword.json')['minecraft:recipe_shaped'];self.assertTrue(any('#' in row for row in r['pattern']));self.assertNotIn('#',r['key'])
            f=load(new,'Swords_B/items/fire_sword.json')['minecraft:item'];self.assertEqual([85,15],[x['weight'] for x in f['events']['weapon']['sequence'][1]['randomize']]);self.assertEqual(6,sum(x.startswith('summon entity:living_flame ') for x in f['events']['on_use']['sequence'][0]['run_command']['command']));self.assertEqual(20,f['events']['on_use']['sequence'][1]['damage']['amount']);self.assertEqual('minecraft:fire',load(new,'Swords_B/recipes/fire_sword.json')['minecraft:recipe_shaped']['key']['F']['item'])
            item=load(new,'Swords_B/entities/item.json')['minecraft:entity'];water=item['events']['fire_sword_event_2']['run_command']['command'];rain=item['events']['fire_sword_event_1']['run_command']['command'];self.assertTrue(any('structure load glass_sword' in x for x in water));self.assertTrue(any('structure load obsidian_sword' in x for x in rain));self.assertIn('kill @s',water);self.assertIn('kill @s',rain)
            si=load(new,'Swords_B/items/spider_sword.json')['minecraft:item'];self.assertEqual(100,si['components']['minecraft:digger']['destroy_speeds'][0]['speed']);self.assertEqual([95,5],[x['weight'] for x in si['events']['weapon']['sequence'][1]['randomize']]);self.assertEqual(8,si['events']['on_use']['damage']['amount']);skill=p['component_groups']['spider_sword_skill'];self.assertFalse(skill['minecraft:spawn_entity'][0]['single_use']);self.assertEqual([2,2],skill['minecraft:timer']['time']);pool=load(new,'Swords_B/loot_tables/chests/abandoned_mineshaft.json')['pools'][1];self.assertEqual(86,sum(x['weight'] for x in pool['entries']));self.assertEqual(3,next(x['weight'] for x in pool['entries'] if x.get('name')=='effect:spider_sword'))
            seq=p['events']['minecraft:sponge_sword']['sequence'];self.assertEqual('in_water_or_rain',seq[1]['filters']['test']);self.assertNotIn('filters',seq[2]);self.assertTrue(any('replace sponge' in x for x in seq[2]['run_command']['command']));self.assertTrue(all(any('sponge_sword='+str(n) in x for x in seq[2]['run_command']['command']) for n in (150,155,160)));self.assertIn('slot.weapon.mainhand',p['events']['wet_sponge_sword']['sequence'][0]['run_command']['command'][0]);furnace=load(new,'Swords_B/recipes/wet_sponge_sword.json')['minecraft:recipe_furnace'];self.assertEqual(('effect:wet_sponge_sword','effect:sponge_sword'),(furnace['input'],furnace['output']));wet=load(new,'Swords_B/items/wet_sponge_sword.json')['minecraft:item']['components'];self.assertNotIn('minecraft:digger',wet);self.assertNotIn('minecraft:enchantable',wet);self.assertNotIn('Sword_B/items/wet_sponge_sword.json',old.namelist())

    def test_spectral_time_comparison_and_legacy_group_exception(self):
        with zipfile.ZipFile(ROOT/'sources/SwordsAndMoreSwords.1.6.mcaddon') as old,zipfile.ZipFile(ROOT/'sources/swordsandmoreswords_2_8_8.mcaddon') as v88,zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as new:
            load=lambda z,p:json5.loads(z.read(p).decode('utf-8-sig'));op=load(old,'Sword_B/entities/player.json')['minecraft:entity'];p=load(new,'Swords_B/entities/player.json')['minecraft:entity'];removed=op['events']['minecraft:event_normal_player']['remove']['component_groups'];self.assertEqual(26,len(removed));self.assertEqual({},op['component_groups']['minecraft:quartz_sword']);extra={key:set(op['component_groups'][key]) for key in removed if key!='minecraft:quartz_sword' and set(op['component_groups'][key])!={'minecraft:spawn_entity'}};self.assertEqual({'minecraft:ender_sword':{'minecraft:spawn_entity','minecraft:teleport','minecraft:hurt_on_condition'}},extra)
            for n in ('spectral','time','clock'):self.assertEqual(v88.read('Swords_B/items/'+n+'_sword.json'),new.read('Swords_B/items/'+n+'_sword.json'))
            oldtime=load(old,'Sword_B/items/Sword of Time.json')['minecraft:item'];self.assertEqual('effect:sword_of_time',oldtime['description']['identifier']);self.assertEqual((7,128),(oldtime['components']['minecraft:damage'],oldtime['components']['minecraft:durability']['max_durability']));self.assertEqual('entity:time',op['component_groups']['minecraft:sword_of_time']['minecraft:spawn_entity'][0]['spawn_entity']);time=load(old,'Sword_B/animation_controllers/sword of time.json');states=time['animation_controllers']['controller.animation.time']['states'];lines=states['default']['on_entry'];self.assertEqual(lines,states['time']['on_entry']);self.assertIn('/effect @e speed 1 15 true',lines);self.assertIn('/gamerule randomtickspeed 300',lines);self.assertIn('/time add 30',lines)
            timer_recipe=load(old,'Sword_B/recipes/Sword_of_Time.json')['minecraft:recipe_shaped'];self.assertEqual('effect:Sword_of_Time',timer_recipe['result']['item']);self.assertNotEqual(oldtime['description']['identifier'],timer_recipe['result']['item']);self.assertNotIn('#',timer_recipe['key']);recipe=load(old,'Sword_B/recipes/spectral_sword.json')['minecraft:recipe_shaped'];self.assertNotIn('#',recipe['key']);self.assertEqual('minecraft:netherstar',recipe['key']['B']['item']);sp=load(new,'Swords_B/items/spectral_sword.json')['minecraft:item'];self.assertEqual([99,1],[x['weight'] for x in sp['events']['weapon']['randomize']]);rare=sp['events']['weapon']['randomize'][1]['run_command']['command'][0];self.assertIn('c=1',rare);self.assertNotIn('r=',rare);self.assertEqual(15,sp['events']['on_use']['damage']['amount']);self.assertEqual([0.4,0.4],p['component_groups']['minecraft:spectral_sword']['minecraft:timer']['time'])
            clk=load(new,'Swords_B/recipes/clock_sword.json')['minecraft:recipe_shaped'];self.assertEqual(['X##','#C#','I#X'],clk['pattern']);self.assertNotIn('X',clk['key']);t=load(new,'Swords_B/items/time_sword.json')['minecraft:item'];b=t['events']['weapon']['randomize'];self.assertEqual([90,6,3,1],[x['weight'] for x in b]);self.assertEqual(346,sum(x['weight']*x['damage']['amount'] for x in b));self.assertNotIn('minecraft:repairable',t['components']);self.assertEqual([5,5],p['component_groups']['clock_sword_skill']['minecraft:timer']['time'])
            def find_removals(node):
                if isinstance(node,dict):
                    if 'remove' in node and isinstance(node['remove'],dict):yield from node['remove'].get('component_groups',[])
                    for value in node.values():yield from find_removals(value)
                elif isinstance(node,list):
                    for value in node:yield from find_removals(value)
            removed=set(find_removals(p['events']));self.assertFalse({'clock_sword_skill','clock_sword_movement','time_sword_movement'} & removed)

    def test_ghost_nether_ultra_literal_paths_and_independent_events(self):
        with zipfile.ZipFile(ROOT/'sources/SwordsAndMoreSwords.1.6.mcaddon') as old,zipfile.ZipFile(ROOT/'sources/swordsandmoreswords_2_8_8.mcaddon') as v88,zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as new:
            load=lambda z,p:json5.loads(z.read(p).decode('utf-8-sig'));p=load(new,'Swords_B/entities/player.json')['minecraft:entity'];p88=load(v88,'Swords_B/entities/player.json')['minecraft:entity'];oldids={load(old,path)['minecraft:item']['description']['identifier'] for path in old.namelist() if path.startswith('Sword_B/items/') and path.endswith('.json')}
            for n in ('ghost','nether_star','ultra_instinct'):
                self.assertNotIn('effect:'+n+'_sword',oldids);path='Swords_B/items/'+n+'_sword.json';self.assertEqual(v88.read(path),new.read(path))
            for event in ('minecraft:ghost_sword','stop_ghost_sword_event','minecraft:ultra_instinct_sword','stop_ultra_instinct_sword_event','shoot_ultra_instinct_projectile'):self.assertEqual(p88['events'][event],p['events'][event])
            ghost=load(new,'Swords_B/items/ghost_sword.json')['minecraft:item'];self.assertEqual(-666,ghost['components']['minecraft:damage']);self.assertEqual(6,ghost['events']['on_use']['damage']['amount']);group=p['component_groups']['minecraft:ghost_sword'];self.assertEqual(['ghost_sword'],group['minecraft:type_family']['family']);self.assertEqual({'cause':'all','deals_damage':False},group['minecraft:damage_sensor']['triggers']);self.assertNotIn('ghost_movement',p['events']['stop_ghost_sword_event']['sequence'][0]['remove']['component_groups'])
            recipe=load(new,'Swords_B/recipes/nether_star_sword.json')['minecraft:recipe_shapeless'];self.assertEqual([{'item':'minecraft:nether_star','data':0},{'item':'minecraft:diamond_sword','data':0}],recipe['ingredients']);self.assertEqual({'item':'effect:nether_star_sword','count':1},recipe['result']);nether=load(new,'Swords_B/items/nether_star_sword.json')['minecraft:item']['events']['weapon']['sequence'];self.assertEqual('entity:nether_star_projectile',nether[0]['shoot']['projectile']);self.assertEqual([80,20],[x['weight'] for x in nether[1]['randomize']]);self.assertEqual([9999,1],[x['weight'] for x in nether[2]['randomize']]);self.assertNotIn('damage',nether[2]['randomize'][1]);projectile=load(new,'Swords_B/entities/nether_star_projectile.json')['minecraft:entity'];self.assertNotIn('objective',projectile['component_groups']);self.assertIn('objective',projectile['events']);self.assertIn('set_objective',projectile['events'])
            ultra=load(new,'Swords_B/items/ultra_instinct_sword.json')['minecraft:item'];self.assertEqual('entity:ultra_instinct_projectile',ultra['events']['on_use']['shoot']['projectile']);self.assertEqual(48,ultra['events']['on_use']['damage']['amount']);obj=p['events']['shoot_ultra_instinct_projectile'];self.assertEqual(['ultra_instinct_projectile'],obj['add']['component_groups']);self.assertEqual(['ultra_instinct_projectile'],obj['remove']['component_groups']);self.assertEqual('entity:ultra_instinct_projectile',p['component_groups']['ultra_instinct_projectile']['minecraft:spawn_entity'][0]['spawn_entity'])
            for z in (v88,new):
                matches=[]
                for path in z.namelist():
                    if path.endswith(('.json','.mcfunction','.js')):
                        matches.extend((path,i) for i,line in enumerate(z.read(path).decode('utf-8-sig').splitlines(),1) if 'shoot_ultra_instinct_projectile' in line)
                self.assertEqual([('Swords_B/entities/player.json',2266)],matches)
            up=load(new,'Swords_B/entities/ultra_instinct_projectile.json')['minecraft:entity'];self.assertIn('kill @e[type=item,r=24]',up['events']['projectile_particle']['run_command']['command']);self.assertNotIn('minecraft:end_scale',up['events']);self.assertIn('ultra_instinct_sword_movement',p['events']['stop_ultra_instinct_sword_event']['sequence'][0]['remove']['component_groups'])

    def test_family_cross_effect_model_and_both_version_sources(self):
        expected_groups={'minecraft:ghost_sword':['ghost_sword'],'complete_wolf_transformation':['wolf','wolf_sword','complete_wolf_transformation','monster']};families={}
        for version in ('swordsandmoreswords_2_8_8.mcaddon','swordsandmoreswords-2-8-14.mcaddon'):
            with zipfile.ZipFile(ROOT/'sources'/version) as z:
                load=lambda path:json5.loads(z.read('Swords_B/'+path).decode('utf-8-sig'));p=load('entities/player.json')['minecraft:entity'];groups={k:v['minecraft:type_family']['family'] for k,v in p['component_groups'].items() if 'minecraft:type_family' in v};self.assertEqual(35,len(groups));self.assertEqual(expected_groups,{k:v for k,v in groups.items() if 'player' not in v});self.assertEqual(['player','default_player'],p['components']['minecraft:type_family']['family']);shield=load('entities/shulker_shield.json')['minecraft:entity'];mount=load('entities/mountable_slime.json')['minecraft:entity'];self.assertEqual('minecraft:shulker',shield['description']['runtime_identifier']);self.assertEqual('minecraft:slime',mount['description']['runtime_identifier']);families={'ordinary':set(p['components']['minecraft:type_family']['family']),'ghost':set(groups['minecraft:ghost_sword']),'wolf':set(groups['complete_wolf_transformation']),'shield':set(shield['components']['minecraft:type_family']['family']),'slime':set(mount['component_groups']['defense_mode_slime']['minecraft:type_family']['family'])};self.assertEqual({'effect99_entities','player','shulker_sword'},families['shield']);self.assertEqual({'effect99_entities','tamed_slime','player'},families['slime'])
                fire=p['events']['minecraft:fire_sword']['sequence'][1]['run_command']['command'];self.assertIn('execute @e[family=!player,type=!item,r=3] ~ ~ ~ summon entity:fire',fire);self.assertIn('damage @e[r=1.4,type=!player] 1 contact entity @s',p['events']['cactus_sword_skills']['run_command']['command']);self.assertIn('effect @e[type=!player] speed 1 15 true',p['events']['minecraft:time_sword']['sequence'][1]['run_command']['command']);sh=load('items/shulker_sword.json')['minecraft:item'];self.assertIn('effect @e[r=6,family=!shulker_sword] levitation 1 18 false',sh['events']['on_use']['run_command']['command']);self.assertTrue(any('family=monster' in x for x in mount['events']['slime_events']['run_command']['command']))
        self.assertEqual([False,True,True,False,False],['player' not in f for f in families.values()]);self.assertEqual([False,False,True,False,False],['monster' in f for f in families.values()]);self.assertEqual([True,True,True,False,True],['shulker_sword' not in f for f in families.values()]);self.assertEqual([True,False,False,False,False],['default_player' in f for f in families.values()])

    def test_silver_alpha_wolf_progression_and_conditions(self):
        with zipfile.ZipFile(ROOT/'sources/SwordsAndMoreSwords.1.6.mcaddon') as old,zipfile.ZipFile(ROOT/'sources/swordsandmoreswords_2_8_8.mcaddon') as v88,zipfile.ZipFile(ROOT/'sources/swordsandmoreswords-2-8-14.mcaddon') as new:
            load=lambda z,p:json5.loads(z.read(p).decode('utf-8-sig'));files=('items/silver_ingot.json','items/silver_sword.json','items/wolf_sword.json','blocks/silver_ore.json','loot_tables/blocks/silver_ore.json','entities/alpha_wolf.json','spawn_rules/alpha_wolf.json','recipes/silver_ingot.json','recipes/silver_sword.json')
            for path in files:self.assertEqual(v88.read('Swords_B/'+path),new.read('Swords_B/'+path))
            ids={load(old,path)['minecraft:item']['description']['identifier'] for path in old.namelist() if path.startswith('Sword_B/items/') and path.endswith('.json')};self.assertFalse({'effect:silver_ingot','effect:silver_sword','effect:wolf_sword'} & ids)
            ore=load(new,'Swords_B/blocks/silver_ore.json')['minecraft:block'];self.assertEqual('loot_tables/blocks/null.json',ore['components']['minecraft:loot']);pool=load(new,'Swords_B/loot_tables/blocks/silver_ore.json')['pools'][0];self.assertEqual('effect99:silver_ore',pool['entries'][0]['name']);self.assertEqual((1,1),(pool['entries'][0]['functions'][0]['count']['min'],pool['entries'][0]['functions'][0]['count']['max']));furnace=load(new,'Swords_B/recipes/silver_ingot.json')['minecraft:recipe_furnace'];self.assertEqual(('effect99:silver_ore','effect:silver_ingot'),(furnace['input'],furnace['output']));recipe=load(new,'Swords_B/recipes/silver_sword.json')['minecraft:recipe_shaped'];self.assertEqual(['2','2','1'],recipe['pattern']);self.assertEqual(('effect:silver_ingot','minecraft:stick'),(recipe['key']['2']['item'],recipe['key']['1']['item']))
            for path in ('Swords_B/features/silver_ore.json','Swords_B/feature_rules/silver_ore_feature.json'):self.assertIn(path,v88.namelist());self.assertNotIn(path,new.namelist())
            alpha=load(new,'Swords_B/entities/alpha_wolf.json')['minecraft:entity'];triggers=alpha['components']['minecraft:damage_sensor']['triggers'];self.assertEqual(3,len(triggers));self.assertTrue(all(t['deals_damage'] is True for t in triggers));self.assertEqual(['minecraft:wolf_sword','add_effects','clear_effects'],[t['on_damage']['event'] for t in triggers]);self.assertTrue(any(x.get('test')=='has_damage' and x.get('value')=='fatal' for x in triggers[0]['on_damage']['filters']['all_of']));self.assertEqual([90,10],[x['weight'] for x in alpha['events']['minecraft:wolf_sword']['sequence'][0]['randomize']]);self.assertIn('effect @s resistance 20 2 true',alpha['events']['add_effects']['run_command']['command']);self.assertIn('effect @s resistance 0',alpha['events']['clear_effects']['run_command']['command'])
            rules=load(new,'Swords_B/spawn_rules/alpha_wolf.json')['minecraft:spawn_rules']['conditions'][0];self.assertEqual({'default':10},rules['minecraft:weight']);self.assertEqual({'min_size':1,'max_size':1},rules['minecraft:herd']);wolf=load(new,'Swords_B/items/wolf_sword.json')['minecraft:item']['components'];self.assertEqual((5,2800),(wolf['minecraft:damage'],wolf['minecraft:durability']['max_durability']));self.assertNotIn('minecraft:enchantable',wolf);player=load(new,'Swords_B/entities/player.json')['minecraft:entity'];self.assertEqual(['wolf','wolf_sword','complete_wolf_transformation','monster'],player['component_groups']['complete_wolf_transformation']['minecraft:type_family']['family']);self.assertEqual(15,player['component_groups']['complete_wolf_transformation']['minecraft:attack']['damage'])

    def test_all_item_rows_have_specialized_manual_entry(self):
        text=(ROOT/'docs/quick-reference.md').read_text()
        for version,count in (('1.6',26),('2.8.8',42),('2.8.14',42)):
            section=text.split('## '+version+'\n',1)[1].split('\n## ',1)[0];rows=[line for line in section.splitlines() if line.startswith('| `effect:')];self.assertEqual(count,len(rows))
            for row in rows:
                links=re.findall(r'\[([^]]+)\]\(([^)]+)\)',row);self.assertTrue(links,row);self.assertTrue(links[0][1].startswith('manual-'),row);path=links[0][1].split('#',1)[0];self.assertTrue((ROOT/'docs'/path).is_file(),row);self.assertNotIn(path,('manual-traces-1.6.md','manual-traces-2.8.14.md'))

    def test_vanilla_reference_review_offline(self):
        import hashlib
        from build_vanilla_reference_facts import PATHS, VANILLA_NAMES, extract, top_level_diff
        facts=json.loads((ROOT/'data/vanilla-reference-facts.json').read_text())
        self.assertEqual(24,len(VANILLA_NAMES))
        expected_refs={
            '1.19.40.2':('16f15af95678d72bcd4b2af468b71f60140a6c06','d99671c6fa61d38dda2b87286e44ddc352ef6578253cbb1d8cfc032ff826c08d'),
            '1.20.30.1':('c7755281ab8c69d7e61d35856ad5a05813e2b853','a667860cf7e9c495a29f05e4f9cfc81c79ca3fce1269aa7348de65f3e9811301'),
        }
        for ver,(commit,sha) in expected_refs.items():
            ref=facts['references'][ver]
            self.assertEqual((commit,sha),(ref['commit'],ref['zip_sha256']))
            self.assertEqual(set(VANILLA_NAMES)-{'item','creeper'},set(ref['file_sha256']))
            for name,entity in ref['entities'].items(): self.assertEqual(ref['file_sha256'][name],entity['sha256'])
        for name in PATHS:
            self.assertEqual(facts['references']['1.19.40.2']['entities'][name]['selected'],facts['references']['1.20.30.1']['entities'][name]['selected'])
        for version,filename,pack in [('1.6','SwordsAndMoreSwords.1.6.mcaddon','Sword_B'),('2.8.8','swordsandmoreswords_2_8_8.mcaddon','Swords_B'),('2.8.14','swordsandmoreswords-2-8-14.mcaddon','Swords_B')]:
            with zipfile.ZipFile(ROOT/'sources'/filename) as z:
                for name,entry in facts['addons'][version].items():
                    self.assertEqual(entry,extract(z.read(f'{pack}/entities/{name}.json'),name))
                if version != '1.6':
                    for name,sha in facts['addons'][version+'_file_sha256'].items():
                        self.assertEqual(sha,hashlib.sha256(z.read(f'{pack}/entities/{name}.json')).hexdigest())
                    for ref in expected_refs:
                        self.assertEqual(set(VANILLA_NAMES)-{'item','creeper'},set(facts['comparisons'][version][ref]))
        reference=facts['references']['1.19.40.2']['entities']
        get=lambda e,k: e['selected'][k]
        for version in ('1.6','2.8.8','2.8.14'):
            player=facts['addons'][version]['player']
            self.assertEqual({'present':True,'value':{'value':0,'max':4}},get(player,'components/minecraft:player.exhaustion'))
            self.assertEqual({'present':True,'value':{'value':20}},get(player,'components/minecraft:player.saturation'))
            self.assertEqual({'present':False},get(player,'components/minecraft:exhaustion_values'))
        self.assertEqual({'present':True,'value':{'value':0,'max':20}},get(reference['player'],'components/minecraft:player.exhaustion'))
        self.assertEqual({'present':True,'value':{'value':5,'max':20}},get(reference['player'],'components/minecraft:player.saturation'))
        for name in ('cat','wolf','parrot','skeleton','blaze'):
            self.assertEqual({'present':False},get(facts['addons']['2.8.14'][name],'components/minecraft:despawn'))
            self.assertEqual({'present':True,'value':{'despawn_from_distance':{}}},get(reference[name],'components/minecraft:despawn'))
        addon=facts['addons']['2.8.14']
        self.assertEqual(['effect:jungle_sword'],get(addon['parrot'],'components/minecraft:behavior.tempt')['value']['items'])
        self.assertEqual(2,get(reference['skeleton'],'component_groups/minecraft:melee_attack/minecraft:attack')['value']['damage'])
        self.assertEqual(3,get(addon['skeleton'],'component_groups/minecraft:melee_attack/minecraft:attack')['value']['damage'])
        self.assertEqual('in_contact_with_water',get(reference['blaze'],'components/minecraft:hurt_on_condition')['value']['damage_conditions'][0]['filters']['test'])
        self.assertEqual('in_water_or_rain',get(addon['blaze'],'components/minecraft:hurt_on_condition')['value']['damage_conditions'][0]['filters']['test'])
        for version,filename in [('2.8.8','swordsandmoreswords_2_8_8.mcaddon'),('2.8.14','swordsandmoreswords-2-8-14.mcaddon')]:
            with zipfile.ZipFile(ROOT/'sources'/filename) as z:
                for name in ('cat','wolf','parrot','skeleton','blaze'):
                    e=json5.loads(z.read(f'Swords_B/entities/{name}.json').decode('utf-8-sig'),allow_duplicate_keys=False)['minecraft:entity']
                    self.assertNotIn('minecraft:despawn',e['components'])
                    self.assertFalse(any('minecraft:despawn' in g for g in e.get('component_groups',{}).values()))
                spider=json5.loads(z.read('Swords_B/entities/spider.json').decode('utf-8-sig'))['minecraft:entity']
                self.assertNotIn('minecraft:despawn',spider['components'])
                self.assertIn('minecraft:despawn',spider['component_groups']['despawn'])
                parrot=json5.loads(z.read('Swords_B/entities/parrot.json').decode('utf-8-sig'))['minecraft:entity']
                self.assertNotIn('minecraft:parrot_riding_player',parrot['component_groups'])
                self.assertNotIn('minecraft:parrot_not_riding_player',parrot['component_groups'])
                blaze=json5.loads(z.read('Swords_B/entities/blaze.json').decode('utf-8-sig'))['minecraft:entity']
                self.assertNotIn('mode_switcher',blaze.get('component_groups',{}))
                self.assertIn('minecraft:behavior.melee_attack',blaze['components'])
                self.assertIn('minecraft:behavior.ranged_attack',blaze['components'])
        for version in ('1.6','2.8.8','2.8.14'):
            p=facts['addons'][version]['player']
            self.assertEqual({'present':False},get(p,'components/minecraft:block_climber'))
            self.assertEqual({'present':True,'value':{}},get(p,'components/minecraft:scaffolding_climber'))
        self.assertEqual({'present':True,'value':{}},get(reference['player'],'components/minecraft:block_climber'))
        self.assertEqual({'present':False},get(reference['player'],'components/minecraft:scaffolding_climber'))
        self.assertEqual(['player','default_player'],get(addon['player'],'components/minecraft:type_family')['value']['family'])
        self.assertEqual(['player'],get(reference['player'],'components/minecraft:type_family')['value']['family'])
        self.assertEqual(['cat','mob','tamed'],get(addon['cat'],'component_groups/minecraft:cat_tame/minecraft:type_family')['value']['family'])
        self.assertEqual(['wolf','mob','tamed'],get(addon['wolf'],'component_groups/minecraft:wolf_tame/minecraft:type_family')['value']['family'])
        example=top_level_diff({'components':{'a':[1,2],'b':{},'same':1}}, {'components':{'a':[2,1],'c':{},'same':1.0}})['components']
        self.assertEqual({'only_reference':['b'],'only_addon':['c'],'different_both':['a']},example)
        doc=(ROOT/'docs/manual-vanilla-override-review.md').read_text()
        for name,sections in facts['comparisons']['2.8.14']['1.19.40.2'].items():
            vals=['/'.join(str(len(sections[s][k])) for k in ('only_reference','only_addon','different_both')) for s in ('components','component_groups','events')]
            self.assertIn('| `'+name+'` | '+' | '.join(vals)+' |',doc)

if __name__=='__main__': unittest.main()
