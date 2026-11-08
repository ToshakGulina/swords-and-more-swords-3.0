"""Audit matrix coverage and the recorded evidence, not game behavior."""
import re
import tarfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'


class ReadinessMatrixTests(unittest.TestCase):
    def test_all_swords_covered_once(self):
        brief = (DOCS / 'remake-master-brief-ru.md').read_text(encoding='utf8')
        matrix = (DOCS / 'remake-readiness-matrix-ru.md').read_text(encoding='utf8')
        ids = re.findall(r'^### \d\d\. .*?`([^`]+)`', brief, re.M)
        rows = re.findall(r'^\| \d\d `(effect:[^`]+)`', matrix, re.M)
        self.assertEqual(len(ids), 38)
        self.assertEqual(len(rows), 38)
        self.assertEqual(set(rows), set(ids))
        self.assertEqual(len(set(rows)), 38)

    def test_all_entities_materials_and_blocks_covered(self):
        brief = (DOCS / 'remake-master-brief-ru.md').read_text(encoding='utf8')
        matrix = (DOCS / 'remake-readiness-matrix-ru.md').read_text(encoding='utf8')
        tail = brief.split('## Боссы, мобы и связанные сущности', 1)[1]
        names = re.findall(r'^### (.+?) — `[^`]+`', tail, re.M)
        self.assertEqual(len(names), 13)
        for name in names:
            with self.subTest(entity=name):
                self.assertIn('| ' + name + ' |', matrix)
        for name in ('quartz_diamond', 'quartz_diamond_stick', 'silver_ingot', 'bedrock_stick',
                     'Quartz Diamond Ore', 'Quartz Diamond Block', 'Silver Ore', 'Колодец', '/function give'):
            with self.subTest(name=name):
                self.assertIn(name, matrix)

    def test_stable_declarations_and_runtime_observations_are_separated(self):
        pkg = ROOT / 'references/bedrock/npm/minecraft-server-2.11.0.tgz'
        with tarfile.open(pkg, 'r:gz') as archive:
            api = archive.extractfile('package/index.d.ts').read().decode('utf8')
        for name in ('class EntityHurtBeforeEvent', 'class EntityHitBlockAfterEvent',
                     'class ItemInventoryComponent', 'class ExplosionBeforeEvent',
                     'class EntityProjectileComponent', 'getMoonPhase()'):
            with self.subTest(api=name):
                self.assertIn(name, api)
        log = (ROOT / 'data/bedrock-preparation/capability-check-1.26.63.1.txt').read_text(encoding='utf8')
        for observation in ('DIAG_BEFORE_HURT 4 magic', 'DIAG_HEALTH_END 10 6',
                            'DIAG_FRACTION_HEALTH 10->8.75 10->6.5',
                            'DIAG_CONTAINER minecraft:shulker_box component=false',
                            'DIAG_LOOT_GENERATED 1 type=minecraft:white_shulker_box inv=false',
                            'DIAG_EXP_FORCED type=minecraft:air',
                            'DIAG_PROJECTILE_ERROR minecraft:small_fireball'):
            with self.subTest(observation=observation):
                self.assertIn(observation, log)
        matrix = (DOCS / 'remake-readiness-matrix-ru.md').read_text(encoding='utf8')
        self.assertIn('не доказывает выпадение блока', matrix)
        self.assertIn('её реальное содержимое и сохранение **не проверены**', matrix)
        self.assertIn('Для обещания готового и полностью совместимого аддона — нет', matrix)


if __name__ == '__main__':
    unittest.main()
