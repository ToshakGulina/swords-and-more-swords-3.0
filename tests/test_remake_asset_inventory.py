"""Проверка отдельно сохранённых ресурсов, без чтения архивов аддона."""
from pathlib import Path
import hashlib
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'references' / 'remake-assets-2.8.8'


class AssetInventoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inventory = json.loads((ASSETS / 'inventory.json').read_text(encoding='utf-8'))
        cls.entries = {entry['path']: entry for entry in cls.inventory['files']}

    def test_expected_file_set(self):
        actual = {str(p.relative_to(ASSETS)) for parent in ('Swords_R', 'Swords_B')
                  for p in (ASSETS / parent).rglob('*') if p.is_file()}
        self.assertEqual(len(self.entries), 203)
        self.assertEqual(self.inventory['file_count'], 203)
        self.assertEqual(actual, set(self.entries))
        self.assertEqual(sum(x['bytes'] for x in self.entries.values()), 2285824)
        self.assertEqual(len(list((ASSETS / 'Swords_R').rglob('*.ogg'))), 3)
        self.assertEqual(len(list((ASSETS / 'Swords_B' / 'structures').rglob('*.mcstructure'))), 18)

    def test_checksums_and_sizes(self):
        sums = {}
        for line in (ASSETS / 'SHA256SUMS').read_text().splitlines():
            digest, path = line.split('  ', 1)
            self.assertNotIn(path, sums)
            sums[path] = digest
        self.assertEqual(set(sums), set(self.entries))
        for name, entry in self.entries.items():
            with self.subTest(file=name):
                content = (ASSETS / name).read_bytes()
                digest = hashlib.sha256(content).hexdigest()
                self.assertEqual(len(content), entry['bytes'])
                self.assertEqual(digest, entry['sha256'])
                self.assertEqual(digest, sums[name])

    def test_official_external_reference_audits_match_recorded_graph(self):
        graph = (ROOT / 'docs' / 'resource-graph-2.8.8.md').read_text(encoding='utf-8')
        audit = ROOT / 'data' / 'remake-audits'
        textures = json.loads((audit / 'vanilla-reference-textures.json').read_text(encoding='utf-8'))
        expected = set(re.findall(r'^- texture `[^`]+` → `([^`]+)` → не найдено локально', graph, re.M))
        self.assertEqual({row['referenced_texture'] for row in textures['textures']}, expected)
        self.assertEqual(len(expected), 24)
        self.assertFalse(textures['tree_truncated'])
        self.assertTrue(all(row['official_files'] for row in textures['textures']))
        definitions = json.loads((audit / 'vanilla-reference-definitions.json').read_text(encoding='utf-8'))
        self.assertFalse(definitions['parse_failures'])
        for kind in ('geometry', 'animation'):
            names = set(re.findall(rf'^- {kind} `[^`]+` → `([^`]+)` → не найдено локально', graph, re.M))
            actual = {r['id'] for r in definitions['categories'][kind]}
            if kind == 'animation':
                actual |= {r['id'] for r in definitions['categories']['animation_controller']}
            self.assertEqual(actual, names)
        render = set(re.findall(r'^- render controller `([^`]+)` → не найдено локально', graph, re.M))
        self.assertEqual({r['id'] for r in definitions['categories']['render_controller']}, render)
        missing = {r['id'] for rows in definitions['categories'].values() for r in rows if not r['definition_files']}
        self.assertEqual(missing, {'controller.animation.player.base', 'controller.animation.player.hudplayer'})
        self.assertEqual(textures['tree_sha'], definitions['commit'])
        sounds = json.loads((audit / 'vanilla-reference-command-sounds.json').read_text(encoding='utf-8'))
        sound_index = (ROOT / 'docs' / 'sound-index-2.8.8.md').read_text(encoding='utf-8')
        names = set(re.findall(r'^### `(?:playsound|stopsound) ([^`]+)`', sound_index, re.M))
        self.assertEqual({r['id'] for r in sounds['sound_ids']}, names)
        self.assertEqual(len(names), 32)
        self.assertTrue(all(r['definition_files'] for r in sounds['sound_ids']))
        self.assertEqual(sounds['official_commit'], definitions['commit'])

    def test_recorded_official_loot_table_paths(self):
        audit = json.loads((ROOT / 'data' / 'remake-audits' / 'vanilla-entity-loot-paths.json').read_text(encoding='utf-8'))
        paths = {row['id']: row['base_loot']['table'] for row in audit['entities']}
        for name in ('shulker', 'elder_guardian', 'wither_skeleton'):
            with self.subTest(entity=name):
                self.assertEqual(paths['minecraft:' + name], f'loot_tables/entities/{name}.json')
        self.assertEqual(audit['commit'], '15701fa9c13923f12662984c32c124327e40e3d3')

    def test_alpha_wolf_vanilla_controller_alias_mismatch(self):
        comparison = json.loads((ROOT / 'data' / 'remake-audits' / 'vanilla-render-alias-comparison.json').read_text(encoding='utf-8'))
        rows = [r for r in comparison['entries'] if r['entity'] == 'entity:alpha_wolf' and r['controller'] == 'controller.render.wolf']
        self.assertEqual(len(rows), 1)
        mismatch = rows[0]['unmatched_aliases']['Texture']
        source = json.loads((ASSETS / rows[0]['client_file']).read_text(encoding='utf-8-sig'))['minecraft:client_entity']['description']
        self.assertEqual(set(source['textures']), {'default', 'angry', 'tame'})
        self.assertEqual(set(mismatch['declared']), set(source['textures']))
        self.assertEqual(len(mismatch['missing']), 27)
        self.assertEqual(set(mismatch['missing']), set(mismatch['requested']) - set(source['textures']))

    def test_all_recorded_item_icons_in_catalog(self):
        text = (ROOT / 'docs' / 'items-2.8.8.md').read_text(encoding='utf-8')
        parts = re.split(r'^## (effect:[^\n]+)\s*$', text, flags=re.M)
        expected = {}
        for item_id, section in zip(parts[1::2], parts[2::2]):
            raw = re.search(r'^```json\s*\n(.*?)\n```', section, re.M | re.S)
            icon = json.loads(raw.group(1))['components']['minecraft:icon']
            expected[item_id] = icon['texture'] if isinstance(icon, dict) else icon
        catalog = (ASSETS / 'README.md').read_text(encoding='utf-8')
        rows = re.findall(r'^\| `(effect:[^`]+)` \| `([^`]+)` \| `([^`]+)` \|$', catalog, re.M)
        self.assertEqual(len(rows), 42)
        self.assertEqual(len({item for item, _, _ in rows}), 42)
        self.assertEqual({item: key for item, key, _ in rows}, expected)
        for item, _, path in rows:
            with self.subTest(item=item):
                self.assertIn(path, self.entries)
                self.assertTrue((ASSETS / path).is_file())


if __name__ == '__main__':
    unittest.main()
