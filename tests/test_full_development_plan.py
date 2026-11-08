"""Completeness and traceability of the plan; not an execution test."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'


class FullDevelopmentPlanTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plan = (DOCS / 'remake-full-development-plan-ru.md').read_text(encoding='utf8')
        cls.brief = (DOCS / 'remake-master-brief-ru.md').read_text(encoding='utf8')

    def test_all_swords_appear_once_in_assigned_work_table(self):
        expected = re.findall(r'^### \d\d\. .*?`([^`]+)`', self.brief, re.M)
        table = self.plan.split('## 5. Реестр всех мечей:', 1)[1].split('## 6.', 1)[0]
        actual = re.findall(r'^\| \d\d \| `([^`]+)` \|', table, re.M)
        self.assertEqual(len(expected), 38)
        self.assertEqual(len(actual), 38)
        self.assertEqual(set(actual), set(expected))
        self.assertEqual(len(set(actual)), 38)
        for row in re.findall(r'^\| \d\d \| .+$', table, re.M):
            with self.subTest(row=row):
                self.assertRegex(row, r'P\d')

    def test_all_mobs_materials_blocks_and_global_features(self):
        tail = self.brief.split('## Боссы, мобы и связанные сущности', 1)[1]
        mobs = re.findall(r'^### (.+?) — `[^`]+`', tail, re.M)
        table = self.plan.split('## 6. Все существа', 1)[1].split('## 7.', 1)[0]
        self.assertEqual(len(mobs), 13)
        # Two compound labels expand their corresponding brief heading.
        aliases = {'Ездовой слизень': 'Ездовой/защитный слизень',
                   'Заряженный и мини-крипер': 'Заряженный и мини-крипер'}
        for name in mobs:
            with self.subTest(name=name):
                self.assertIn('| ' + aliases.get(name, name) + ' |', table)
        for name in ('effect:quartz_diamond', 'effect:quartz_diamond_stick', 'effect:silver_ingot',
                     'effect:bedrock_stick', 'effect99:quartz_diamond_ore',
                     'effect99:quartz_diamond_block', 'effect99:silver_ore',
                     'Колодец', '/function give'):
            with self.subTest(name=name):
                self.assertIn(name, self.plan)

    def test_phases_are_traced_and_plan_is_not_permission(self):
        phases = re.findall(r'^\| \*\*(P\d+)\.', self.plan, re.M)
        self.assertEqual(phases, [f'P{i}' for i in range(14)])
        for required in ('плана для согласования', 'без согласования с пользователем',
                         '1.26.63.1', 'Не использовать 2.8.14',
                         'не доказательство работоспособности', 'не доказывает',
                         'не создавать', 'клиент'):
            if required == 'не создавать':
                # Equivalent instruction is worded explicitly at the top of the plan.
                required = 'Разработку по нему пока не начинать'
            if required == 'без согласования с пользователем':
                required = 'только после согласования с пользователем'
            if required == 'не доказательство работоспособности':
                required = 'ни доказательство работоспособности, ни невозможности'
            with self.subTest(required=required):
                self.assertIn(required, self.plan)

    def test_key_user_decisions_preserved(self):
        for required in ('двух шалкерах по 19', 'две свободные ячейки',
                         'brightness <0,49', '150 и резервы 155/160',
                         '50/100 над 999', 'всем игрокам r=1',
                         'при совпадении водной и 50%-ветви не более одного',
                         'Травяная форма только ночью', 'без отдельного запрета дня',
                         'только в джунглях', 'постановку цветов поверх блока'):
            with self.subTest(required=required):
                self.assertIn(required, self.plan)


if __name__ == '__main__':
    unittest.main()
