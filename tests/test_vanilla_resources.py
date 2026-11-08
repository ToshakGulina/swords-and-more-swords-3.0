import hashlib
import json
import sys
import unittest
from pathlib import Path
from zipfile import ZipFile

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
from build_vanilla_resource_diff import ADDONS, CLIENTS, MAPS, RENDERS, nested, parse_json, parse_lang, png_size
from build_vanilla_reference_facts import REFERENCE


class VanillaResourceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=json.loads((ROOT/'data/vanilla-resource-diff.json').read_text())

    def test_source_files_and_shared_paths_offline(self):
        expected_counts={'1.6':(56,4,0),'2.8.8':(184,26,4),'2.8.14':(184,26,4)}
        self.assertEqual(set(ADDONS),set(self.data['addons']))
        for ver,(filename,prefix) in ADDONS.items():
            with ZipFile(ROOT/'sources'/filename) as z:
                names={n[len(prefix):] for n in z.namelist() if n.startswith(prefix) and not n.endswith('/')}
                rec=self.data['addons'][ver]
                self.assertEqual(expected_counts[ver][0],rec['file_count'])
                self.assertEqual(names,set(rec['files']))
                for name,metadata in rec['files'].items():
                    raw=z.read(prefix+name)
                    self.assertEqual({'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'png_size':png_size(raw)},metadata)
                for ref_ver,ref in self.data['references'].items():
                    self.assertEqual(REFERENCE[ref_ver],(ref['commit'],ref['zip_sha256']))
                    comp=ref['comparisons'][ver]
                    self.assertEqual(expected_counts[ver][1],len(comp))
                    self.assertEqual(expected_counts[ver][2],sum(i['byte_equal'] for i in comp.values()))
                    for name,item in comp.items():
                        self.assertIn(name,names)
                        self.assertRegex(item['reference_sha256'],r'^[0-9a-f]{64}$')
                        self.assertEqual(rec['files'][name]['sha256']==item['reference_sha256'],item['byte_equal'])
                        if 'details' not in item:continue
                        raw=z.read(prefix+name);details=item['details']
                        if details['kind'] in ('key_map','language'):
                            source=parse_lang(raw) if details['kind']=='language' else nested(parse_json(raw),tuple(details['path']))
                            diff=details['diff'];self.assertEqual(len(source),diff['addon_count'])
                            self.assertEqual(len(source),len(diff['only_addon'])+len(diff['different_common'])+diff['equal_common_count'])
                            self.assertTrue(set(diff['only_addon']).issubset(source))
                            for key,value in diff['different_common'].items():self.assertEqual(source[key],value['addon'])
                            self.assertEqual(diff['reference_count'],diff['only_reference_count']+len(diff['different_common'])+diff['equal_common_count'])
                            if details['kind']=='language':self.assertEqual({k:v for k,v in source.items() if len(v)>1},details['addon_duplicate_keys'])
                        elif details['kind'] in ('client_description','render_controller'):
                            parsed=parse_json(raw)
                            source=parsed['minecraft:client_entity']['description'] if name in CLIENTS else parsed['render_controllers']
                            for key,pair in details['changed_values'].items():
                                expected={'present':True,'value':source[key]} if key in source else {'present':False}
                                self.assertEqual(expected,pair['addon'],(ver,ref_ver,name,key))
                        elif details['kind']=='array':self.assertEqual(parse_json(raw),details['addon_values'])

    def test_selected_resource_interactions(self):
        for ref in ('1.19.40.2','1.20.30.1'):
            for ver in ('2.8.8','2.8.14'):
                c=self.data['references'][ref]['comparisons'][ver]
                identical={name for name,item in c.items() if item['byte_equal']}
                self.assertEqual({'render_controllers/default.render_controllers.json','textures/entity/enderman/enderman.tga','textures/entity/slime/magmacube.tga','textures/entity/slime/slime.png'},identical)
                item=c['textures/item_texture.json']['details']['diff']
                self.assertEqual((234,42,0,0),(item['reference_count'],item['addon_count'],len(item['different_common']),item['equal_common_count']))
                terrain=c['textures/terrain_texture.json']['details']['diff']
                self.assertEqual(7 if ver=='2.8.8' else 6,terrain['addon_count'])
                self.assertEqual(ver=='2.8.8','fake_ice' in terrain['only_addon'])
                lang=c['texts/en_US.lang']['details']
                self.assertEqual(627,lang['diff']['addon_count'])
                self.assertEqual(0,len(lang['diff']['different_common'])+lang['diff']['equal_common_count'])
                self.assertEqual(['§lGhost','§l§fGhost'],lang['addon_duplicate_keys']['entity.entity:ghost.name'])
                ui=c['ui/how_to_play_screen.json']['details']['diff']
                self.assertEqual((84,80,3,1),(ui['addon_count'],len(ui['only_addon']),len(ui['different_common']),ui['equal_common_count']))
                texture=c['entity/enderman.entity.json']['details']['changed_values']['textures']
                self.assertEqual('textures/entity/enderman/red_enderman',texture['addon']['value']['red_enderman'])
                self.assertNotIn('red_enderman',texture['reference']['value'])
                render=c['render_controllers/enderman.render_controllers.json']['details']['changed_values']['controller.render.enderman']['addon']['value']
                self.assertEqual(['Array.textures[query.variant]'],render['textures'])
                self.assertEqual(['Texture.default','Texture.red_enderman'],render['arrays']['textures']['Array.textures'])
                for name in ('entity/witch.entity.json','entity/witch.v1.0.entity.json'):
                    self.assertEqual('textures/entity/grass_witch',c[name]['details']['changed_values']['textures']['addon']['value']['grass_witch'])
            for name,item in self.data['references'][ref]['comparisons']['2.8.14'].items():
                if name.startswith('textures/ui/how_to_play_button_'):
                    self.assertEqual([16,16],self.data['addons']['2.8.14']['files'][name]['png_size'])
                    if ref=='1.19.40.2':self.assertEqual([15,15],item['reference_png_size'])
        self.assertEqual(['manifest.json','pack_icon.png','texts/en_US.lang','textures/item_texture.json'],sorted(self.data['references']['1.19.40.2']['comparisons']['1.6']))
        names=self.data['addons']['2.8.14']['files']
        self.assertIn('textures/entity/enderman/red_enderman.tga',names)
        self.assertIn('textures/entity/grass_witch.png',names)


if __name__=='__main__':unittest.main()
