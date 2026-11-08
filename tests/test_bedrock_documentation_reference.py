"""Check the offline reference inventory, not Bedrock gameplay."""

import hashlib
import json
import tarfile
import unittest
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
REF = ROOT / 'references' / 'bedrock'


class BedrockDocumentationReferenceTests(unittest.TestCase):
    def test_new_archives_are_intact(self):
        expected = {
            'creator-docs-markdown.zip': '2b2ee5ece5dd2185d2b60670ea49f3e3352eae1ad4c82edf0fd2d7888bb0a95e',
            'bedrock-1.26.60.5-reference.zip': 'f875d57e46cb4681650a0f6aea1c0b02b799ba974b341058281d7398aeb9e8d6',
            'microsoft-script-samples.zip': 'f84c42bd75872481d31f16c685b35c79ca1d51d4b4688b3445b7d3daafa13437',
            'bedrock-server-1.26.63.1-text-reference.zip': 'c065d9ae2aa0bd43fdc6bdf9d0ae858d59fc82c48261c3ad869229482c33a40d',
            'microsoft-addon-examples.zip': 'c16349f1c60fc5c2b9794a145f7938192d07e3d82036defb145e20015c0efab9',
            'bedrock-1.26.60.5-resource-reference.zip': 'b36391010e511fdec7a9e991085f266ad8753ab81730b8583b60b78cd5e3c9bf',
            'npm/minecraft-server-2.11.0.tgz': '0ba02700b94ac4acf3875a629d3a63fa9d4c737d5eb43c8b7929ab00fd4ea546',
            'npm/minecraft-server-ui-2.3.0.tgz': '5b13b8ccbb21220672f51ee4888e20cc93f3c8617538ffdf7945530ea90864c3',
        }
        for name, digest in expected.items():
            with self.subTest(name=name):
                self.assertEqual(hashlib.sha256((REF / name).read_bytes()).hexdigest(), digest)

    def test_server_text_reference_inventory_and_checksums(self):
        inventory = json.loads((REF / 'bedrock-server-1.26.63.1-text-reference-inventory.json').read_text(encoding='utf8'))
        self.assertEqual(inventory['source_sha256'], 'b40b04c8f5a7c42a19ee685c22fc593e66116b9c22741b8c75489306b252ff62')
        self.assertEqual(inventory['file_count'], 262)
        entries = {item['path']: item for item in inventory['files']}
        self.assertEqual(len(entries), 262)
        with ZipFile(REF / inventory['archive']) as archive:
            self.assertIsNone(archive.testzip())
            self.assertEqual(set(archive.namelist()), set(entries))
            for path, expected in entries.items():
                with self.subTest(path=path):
                    data = archive.read(path)
                    self.assertEqual(len(data), expected['bytes'])
                    self.assertEqual(hashlib.sha256(data).hexdigest(), expected['sha256'])
            for path in ('bedrock_server_how_to.html', 'server.properties', 'release-notes.txt',
                         'definitions/features/diamond_ore_feature.json',
                         'definitions/feature_rules/overworld_underground_coal_ore_feature.json'):
                self.assertIn(path, entries)

    def test_core_offline_documentation_and_vanilla_examples_exist(self):
        with ZipFile(REF / 'creator-docs-markdown.zip') as archive:
            names = set(archive.namelist())
            for path in [
                'creator/Documents/EntityEvents.md',
                'creator/Documents/FeaturesTaxonomy.md',
                'creator/Documents/Spawning/EntitySpawningDeepDive.md',
                'creator/Documents/Structures/IntroductionToStructureBlocks.md',
                'creator/Documents/scripting/versioning.md',
                'creator/Documents/scripting/system-run-guide.md',
                'creator/Documents/scripting/multiplayer-scripts.md',
                'creator/Reference/Content/ItemReference/Examples/ItemComponents/minecraft_damage.md',
                'creator/Reference/Content/ItemReference/Examples/ItemComponents/minecraft_durability.md',
                'creator/Reference/Content/EntityReference/Examples/Filters/in_water_or_rain.md',
                'creator/ScriptAPI/minecraft/server/EntityDamageSource.md',
                'creator/ScriptAPI/minecraft/server/ItemInventoryComponent.md',
                'creator/Commands/commands/spreadplayers.md',
            ]:
                with self.subTest(path=path):
                    self.assertIn(path, names)
        with ZipFile(REF / 'bedrock-1.26.60.5-resource-reference.zip') as archive:
            names = set(archive.namelist())
            for path in ['LICENSE.md', 'version.json', 'resource_pack/textures/item_texture.json',
                         'resource_pack/texts/en_US.lang', 'resource_pack/texts/ru_RU.lang',
                         'resource_pack/entity/wolf.entity.json']:
                with self.subTest(path=path):
                    self.assertIn(path, names)
        with ZipFile(REF / 'microsoft-addon-examples.zip') as archive:
            names = set(archive.namelist())
            self.assertIn('LICENSE', names)
            self.assertIn('custom_projectiles/behavior_pack/entities/custom_arrow.json', names)
            self.assertIn('shapeshifter/behavior_pack/shapeshifter/entities/shapeshifter.behavior.json', names)
        for name in ['minecraft-server-2.11.0.tgz', 'minecraft-server-ui-2.3.0.tgz']:
            with tarfile.open(REF / 'npm' / name, 'r:gz') as archive:
                self.assertIn('package/index.d.ts', archive.getnames())

    def test_scope_keeps_server_and_sample_versions_distinct(self):
        text = (ROOT / 'docs' / 'remake-bedrock-documentation-ru.md').read_text(encoding='utf8')
        for value in ('1.26.63.1', 'v1.26.60.5', '1Frpkz7dSquy71iOTbUnkLosx5C5K5jwQ',
                      'не реализация аддона', 'не все методы API', 'ещё необходимо исследовать'):
            with self.subTest(value=value):
                self.assertIn(value, text)


if __name__ == '__main__':
    unittest.main()
