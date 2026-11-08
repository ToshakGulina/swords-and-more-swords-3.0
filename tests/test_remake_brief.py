"""Сверка рабочей памятки с уже сохранёнными выписками, без чтения архивов аддона."""
from pathlib import Path
import json
import re
import unittest
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'


def recorded_items():
    text = (DOCS / 'items-2.8.8.md').read_text(encoding='utf-8')
    parts = re.split(r'^## (effect:[^\n]+)\s*$', text, flags=re.M)
    result = {}
    for item_id, section in zip(parts[1::2], parts[2::2]):
        match = re.search(r'^```json\s*\n(.*?)\n```', section, re.M | re.S)
        if item_id.endswith('_sword'):
            result[item_id] = json.loads(match.group(1))['components']
    return result


def cards():
    text = (DOCS / 'remake-master-brief-ru.md').read_text(encoding='utf-8')
    section = text.split('## 38 карточек мечей\n', 1)[1].split('\n## Материалы и блоки', 1)[0]
    parts = re.split(r'^### \d+\. .*? — `(effect:[^`]+)`\s*$', section, flags=re.M)
    return dict(zip(parts[1::2], parts[2::2]))


def human_item(item_id, own_id):
    if item_id == own_id:
        if own_id == 'effect:wet_sponge_sword':
            return 'Wet Sponge Sword'
        return 'такой же меч'
    if item_id == 'effect:sponge_sword':
        return 'Sponge Sword'
    return item_id.replace('minecraft:', '').replace('effect:', '').replace('_', ' ')


class BriefAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = recorded_items()
        cls.cards = cards()

    def test_glowstone_and_blaze_decisions(self):
        glow = self.cards['effect:glowstone_sword']
        self.assertIn('при удержании в любой руке', glow)
        self.assertIn('уровень излучения — 15', glow)
        blaze = self.cards['effect:blaze_sword']
        self.assertIn('отменять ожидаемые выстрелы и снимать levitation и slow falling', blaze)
        self.assertIn('Уже созданные снаряды при смене не удалять', blaze)

    def test_living_flame_uses_loot_not_structure(self):
        brief = (DOCS / 'remake-master-brief-ru.md').read_text(encoding='utf-8')
        mob = brief.split('### Living Flame —', 1)[1].split('#### Записанные компоненты', 1)[0]
        self.assertIn('`loot spawn`', mob)
        self.assertIn('`entities/living_flame`', mob)
        self.assertNotIn('загружает структуру Fire Sword', mob)

    def test_red_enderman_has_explicit_loot_reference(self):
        brief = (DOCS / 'remake-master-brief-ru.md').read_text(encoding='utf-8')
        mob = brief.split('### Красноглазый Enderman', 1)[1].split('#### Записанные компоненты', 1)[0]
        self.assertIn('группа `red_enderman` прямо ссылается', mob)
        self.assertIn('loot_tables/entities/red_enderman.json', mob)
        self.assertIn('явно связать эту таблицу', self.cards['effect:ender_sword'])

    def test_vanilla_mob_loot_is_actionable(self):
        for sword in ('shulker_sword', 'sponge_sword', 'wither_skeleton_sword'):
            card = self.cards['effect:' + sword]
            self.assertIn('сохраняя обычную добычу', card)
            self.assertIn('2 процентных пункта за уровень Looting', card)
        self.assertIn('эффектом Wither I на 10 секунд', self.cards['effect:wither_skeleton_sword'])

    def test_quartz_area_and_slime_ownership(self):
        self.assertIn('эффект также распространяется на всех игроков в радиусе 1', self.cards['effect:quartz_sword'])
        self.assertIn('после спешивания он защищает именно его', self.cards['effect:slime_sword'])
        self.assertIn('снятие меча управляет только собственным слизнем', self.cards['effect:slime_sword'])

    def test_quartz_weapon_inputs_and_hostile_blaze_fireballs(self):
        quartz = self.cards['effect:quartz_sword']
        self.assertIn('попадание с уроном, удар без урона по сущности и удар по блоку', quartz)
        self.assertIn('затем выполнить эффект и частицу, даже если на первом шаге меч сломался', quartz)
        blaze = self.cards['effect:blaze_sword']
        self.assertIn('источник неизвестен или является враждебным мобом', blaze)
        self.assertIn('при включённом PvP добавляются снаряды других игроков', blaze)
        self.assertIn('собственные снаряды владельца не обрабатывать независимо от PvP', blaze)
        self.assertIn('без гарантии непроницаемого барьера', blaze)
        self.assertIn('power 0, inertia 0, gravity 0,06', blaze)
        self.assertIn('fake_fireball и большие fireball не включать', blaze)

    def test_bone_and_bedrock_intended_behavior(self):
        bone = self.cards['effect:bone_sword']
        self.assertIn('стрелы family arrow в радиусе 8', bone)
        self.assertIn('при включённом PvP добавляются стрелы других игроков', bone)
        self.assertIn('собственные стрелы владельца не обрабатывать независимо от PvP', bone)
        self.assertIn('без гарантии непроницаемого барьера', bone)
        self.assertIn('power 0, gravity 1, inertia 0, liquid inertia 0', bone)
        self.assertIn('дочерние помощники не запускают эту цепочку заново', bone)
        bedrock = self.cards['effect:bedrock_sword']
        self.assertIn('не должен ломать сам бедрок в выживании', bedrock)
        self.assertIn('приоритет у точного ID', bedrock)

    def test_slime_king_and_grass_witch_are_night_only(self):
        brief = (DOCS / 'remake-master-brief-ru.md').read_text(encoding='utf-8')
        king = brief.split('### Slime King', 1)[1].split('#### Записанные компоненты', 1)[0]
        witch = brief.split('### Grass Witch', 1)[1].split('#### Записанные компоненты', 1)[0]
        self.assertIn('по решению пользователя только ночью', king)
        self.assertIn('При событии появления ночью', witch)
        self.assertIn('Вне ночи этот выбор травяной формы не выполнять', witch)
        self.assertIn('контроль только с [0,16;0,4]', king)
        self.assertIn('в ремейке использовать задержку [0,16;0,4] секунды', king)

    def test_jungle_sword_fishing_is_jungle_only(self):
        card = self.cards['effect:jungle_sword']
        self.assertIn('рыбалка только в биоме джунглей', card)
        self.assertIn('сундук храма джунглей', card)
        self.assertIn('ограничение биома — выбранное требование ремейка', card)

    def test_spectral_ghast_requires_own_fatal_fireball(self):
        card = self.cards['effect:spectral_sword']
        self.assertIn('при гибели гаста от его собственного огненного шара — одна попытка 6%', card)
        self.assertIn('исходного гаста, выпустившего шар', card)
        self.assertIn('даже если игрок отразил его', card)
        self.assertIn('при его повреждении выполняется 2%-попытка', card)

    def test_coal_sword_fuel_duration(self):
        card = self.cards['effect:coal_sword']
        self.assertIn('36 плавок', card)
        self.assertIn('длительность топлива 360 секунд', card)
        self.assertIn('Контрольный уголь', card)

    def test_cursed_pumpkin_tag_death_persistence(self):
        card = self.cards['effect:cursed_pumpkin_sword']
        self.assertIn('после смерти игрока и после повторного входа сохранять тег', card)
        self.assertIn('проверялись общие теги игры', card.lower())

    def test_silver_wolf_damage_and_effect_order(self):
        silver = self.cards['effect:silver_sword']
        self.assertIn('Отдельный множитель урона Silver против волка не добавлять', silver)
        self.assertIn('после несмертельного попадания снять', silver)
        brief = (DOCS / 'remake-master-brief-ru.md').read_text(encoding='utf-8')
        wolf = brief.split('### Alpha Wolf —', 1)[1].split('#### Записанные компоненты', 1)[0]
        self.assertIn('допускать появление при фазе луны 0', wolf)
        self.assertIn('при смене фазы удалять волка', wolf)
        self.assertIn('при несмертельном ударе игрока с Silver после расчёта снять', wolf)
        self.assertIn('выполнить одну независимую попытку выдачи Wolf Sword с шансом 10%', wolf)

    def test_centella_lightning_does_not_chain_in_specification(self):
        brief = (DOCS / 'remake-master-brief-ru.md').read_text(encoding='utf-8')
        mob = brief.split('### Centella —', 1)[1].split('#### Записанные компоненты', 1)[0]
        self.assertIn('При фатальном уроне вызвать одну молнию', mob)
        self.assertIn('если источник — игрок', mob)
        self.assertIn('не запускать этот выбор', self.cards['effect:lightning_sword'])
        self.assertIn('один раз вызвать молнию в его позиции и уничтожить предмет', self.cards['effect:lightning_sword'])
        self.assertIn('дважды при попадании выброшенного меча', self.cards['effect:lightning_sword'])

    def test_exact_inventory(self):
        self.assertEqual(len(self.source), 38)
        self.assertEqual(set(self.source), set(self.cards))
        self.assertEqual(len(self.cards), 38)

    def test_damage_durability_and_cooldown(self):
        for item_id, c in self.source.items():
            with self.subTest(item=item_id):
                card = self.cards[item_id]
                damage = c.get('minecraft:damage', 'не указано')
                if item_id == 'effect:ghost_sword':
                    self.assertEqual(damage, -666)
                    self.assertIn('**Урон:** −666 в записанной настройке', card)
                else:
                    self.assertIn(f'**Урон:** {damage}.', card)
                if item_id == 'effect:bedrock_sword':
                    self.assertNotIn('minecraft:durability', c)
                    self.assertIn('**Прочность:** бесконечная по игровой задумке', card)
                else:
                    d = c.get('minecraft:durability', {}).get('max_durability', 'не указана')
                    self.assertIn(f'**Прочность:** {d}.', card)
                cooldown = c.get('minecraft:cooldown')
                expected = f"{cooldown['duration']} с" if cooldown else 'не указан'
                self.assertIn(f'**Кулдаун:** {expected}.', card)

    def test_repair_materials_and_amounts(self):
        for item_id, c in self.source.items():
            with self.subTest(item=item_id):
                repair = c.get('minecraft:repairable')
                if not repair:
                    expected = 'компонент не указан'
                else:
                    expected = '; '.join(
                        f"{human_item(material, item_id)}: {entry['repair_amount']}"
                        for entry in repair['repair_items']
                        for material in entry['items']
                    )
                self.assertIn(f'**Ремонт, единиц за материал:** {expected}.', self.cards[item_id])

    def test_enchant_components(self):
        for item_id, c in self.source.items():
            with self.subTest(item=item_id):
                ench = c.get('minecraft:enchantable')
                expected = f"есть: value {ench['value']}, слот {ench['slot']}" if ench else 'компонент не указан'
                self.assertIn(f'**Зачарование:** {expected}.', self.cards[item_id])

    def test_use_costs_match_saved_index(self):
        text = (DOCS / 'on-use-index.md').read_text(encoding='utf-8').split('## Без item', 1)[0]
        found = {}
        for line in text.splitlines():
            match = re.match(r'^\| \[`(effect:[^`]+)`\].*?\| `\{"type":"durability","amount":(\d+),"target":"self"\}`', line)
            if match:
                found[match.group(1)] = match.group(2)
        self.assertEqual(len(found), 14)
        for item_id, card in self.cards.items():
            expected = found.get(item_id, 'не указан')
            with self.subTest(item=item_id):
                self.assertIn(f'**Расход применения:** {expected}.', card)

    def test_crafting_and_smelting_against_saved_recipes(self):
        index = (DOCS / 'acquisition-index-2.8.8.md').read_text(encoding='utf-8')
        index = index.split('## Все рецепты и диагностика шаблонов', 1)[1].split('## Все записи', 1)[0]
        recipes = re.findall(r'^- Полное определение: `(\{.*\})`$', index, re.M)
        self.assertEqual(len(recipes), 14)
        brief = (DOCS / 'remake-master-brief-ru.md').read_text(encoding='utf-8')
        section = (DOCS / 'archive/remake-master-brief-before-item-restructure-ru.md').read_text(encoding='utf-8').split('## Рецепты из сохранённых записей', 1)[1].split('## Колодец', 1)[0]
        for raw in recipes:
            recipe = json.loads(raw)
            result = recipe.get('result', {}).get('item') or recipe.get('output')
            with self.subTest(result=result):
                row = next((line for line in section.splitlines() if line.startswith(f'- **{result}:**')), None)
                self.assertIsNotNone(row)
                if 'pattern' in recipe and result != 'effect:clock_sword':
                    self.assertIn(' / '.join(recipe['pattern']), row)
                    for symbol, ingredient in recipe['key'].items():
                        self.assertIn(f"{symbol}={ingredient['item']}", row)
                elif result == 'effect:clock_sword':
                    self.assertEqual(recipe['pattern'], ['X##', '#C#', 'I#X'])
                    self.assertIn('.GG / GCG / IG.', row)
                    self.assertIn('неопределённый символ `X`', section)
                elif 'ingredients' in recipe:
                    for ingredient in recipe['ingredients']:
                        self.assertIn(ingredient['item'], row)
                else:
                    self.assertIn(recipe['input'], row)
                    self.assertIn(recipe['output'], row)
                    self.assertIn('furnace, blast_furnace', row)
                if result in self.cards:
                    self.assertIn('**Рецепт:** ' + row.split(':** ', 1)[1], self.cards[result])
                else:
                    self.assertIn(row.split(':** ', 1)[1], brief)

    def test_chest_loot_weights_and_rolls(self):
        source = (DOCS / 'loot-selection-model.md').read_text(encoding='utf-8')
        cases = [
            ('chests/spawn_bonus_chest.json', 'coal_sword', '1', '1/5'),
            ('chests/igloo_chest.json', 'ice_sword', '{"min":2,"max":8}', '1/64'),
            ('chests/village/village_snowy_house.json', 'ice_sword', '{"min":3,"max":8}', '4/57'),
            ('chests/abandoned_mineshaft.json', 'spider_sword', '{"min":2,"max":4}', '3/86'),
            ('chests/buriedtreasure.json', 'sea_sword', '{"min":5,"max":12}', '15/219'),
            ('chests/desert_pyramid.json', 'tnt_sword', '{"min":2,"max":4}', '10/242'),
            ('chests/jungle_temple.json', 'jungle_sword', '{"min":2,"max":6}', '16/457'),
            ('chests/underwater_ruin_big.json', 'magma_sword', '1', '1/24'),
            ('chests/stronghold_corridor.json', 'emerald_sword', '{"min":2,"max":3}', '5/521'),
            ('chests/stronghold_corridor.json', 'lapis_sword', '{"min":2,"max":3}', '5/521'),
            ('chests/stronghold_library.json', 'lapis_sword', '{"min":2,"max":10}', '5/275'),
            ('chests/woodland_mansion.json', 'emerald_sword', '{"min":1,"max":3}', '25/670'),
            ('chests/pillager_outpost.json', 'emerald_sword', '{"min":2,"max":3}', '3/28'),
            ('chests/pillager_outpost.json', 'lapis_sword', '{"min":2,"max":3}', '3/28'),
            ('gameplay/fishing/treasure.json', 'jungle_sword', '1', '5/41'),
        ]
        for path, item, rolls, weight in cases:
            with self.subTest(path=path, item=item):
                rows = [line for line in source.splitlines()
                        if f'`{path}`' in line and f'`effect:{item}`' in line]
                self.assertEqual(len(rows), 1)
                cells = [cell.strip().strip('`') for cell in rows[0].split('|')[1:-1]]
                self.assertEqual(cells[3], rolls)
                self.assertEqual(cells[4], weight)

    def test_offhand_and_stack_summary(self):
        self.assertTrue(all(c.get('minecraft:max_stack_size') == 1 for c in self.source.values()))
        self.assertEqual([item for item, c in self.source.items()
                          if c.get('minecraft:allow_off_hand')], ['effect:glowstone_sword'])
        self.assertTrue(all(c.get('minecraft:allow_off_hand') is False
                            for item, c in self.source.items() if item != 'effect:glowstone_sword'))

    def test_projectile_weights_against_recorded_events(self):
        index = (DOCS / 'items-2.8.8.md').read_text(encoding='utf-8')
        parts = re.split(r'^## (effect:[^\n]+)\s*$', index, flags=re.M)
        recorded = {}
        for item, section in zip(parts[1::2], parts[2::2]):
            match = re.search(r'^```json\s*\n(.*?)\n```', section, re.M | re.S)
            recorded[item] = json.loads(match.group(1))
        expected = {
            'bee_sword': {'entity:bee_sword': 30},
            'blaze_sword': {'minecraft:small_fireball': 14, 'minecraft:fireball': 1},
            'bone_sword': {'minecraft:arrow': 20},
            'creeper_sword': {'minecraft:creeper': 20},
            'fire_sword': {'entity:fire': 85, 'entity:living_flame': 15},
            'ice_sword': {'minecraft:snowball': 30},
            'lightning_sword': {'entity:lightning_projectile': 85},
            'cursed_pumpkin_sword': {'entity:pumpkin_projectile': 80},
            'shulker_sword': {'minecraft:shulker_bullet': 10},
            'spider_sword': {'entity:web': 5},
            'tnt_sword': {'entity:tnt': 90},
            'wither_sword': {'minecraft:wither_skull': 10},
        }
        def walk(value):
            if isinstance(value, dict):
                if 'randomize' in value:
                    branches = value['randomize']
                    if any('shoot' in b for b in branches):
                        yield branches
                for v in value.values():
                    yield from walk(v)
            elif isinstance(value, list):
                for v in value:
                    yield from walk(v)
        for item, projectile_weights in expected.items():
            with self.subTest(item=item):
                branches, = list(walk(recorded['effect:' + item]['events']['weapon']))
                self.assertEqual(sum(b['weight'] for b in branches), 100)
                self.assertEqual({b['shoot']['projectile']: b['weight'] for b in branches if 'shoot' in b}, projectile_weights)
                for weight in set(projectile_weights.values()):
                    self.assertRegex(self.cards['effect:' + item], rf'(?<!\d){weight}(?:%| из 100|/100)')

    def test_item_navigation_has_all_38_distinct_cards(self):
        text = (DOCS / 'remake-master-brief-ru.md').read_text(encoding='utf-8')
        anchors = re.findall(r'<a id="sword-([\w]+)"></a>\n### \d+\. .*? — `effect:([\w]+)`', text)
        self.assertEqual(len(anchors), 38)
        self.assertEqual({a for a, b in anchors if a == b}, {item.removeprefix('effect:') for item in self.source})
        self.assertIn('## Материалы и блоки', text)
        self.assertIn('## Боссы, мобы и связанные сущности', text)
        self.assertNotIn('## Общие правила', text)
        self.assertNotIn('## Оставшиеся конкретные проверки', text)

    def test_structure_places_shared_details_with_each_object(self):
        text = (DOCS / 'remake-master-brief-ru.md').read_text(encoding='utf-8')
        for item, card in self.cards.items():
            with self.subTest(item=item):
                self.assertIn('**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.', card)
                self.assertIn('**Вход weapon-события:**', card)
        for item in ('quartz_diamond', 'quartz_diamond_stick', 'silver_ingot', 'bedrock_stick'):
            self.assertIn('### effect:' + item + '\n', text)
        for heading in ('Кварц-алмазная руда', 'Кварц-алмазный блок', 'Серебряная руда', 'Slime King', 'Alpha Wolf', 'Grass Witch', 'Centella', 'Living Flame'):
            self.assertIn('### ' + heading, text)
        for item in ('clock_sword', 'time_sword', 'ultra_instinct_sword'):
            self.assertIn('**Колодец:**', self.cards['effect:' + item])
            self.assertIn('2,5%', self.cards['effect:' + item])
        self.assertIn('0,8%', self.cards['effect:ultra_instinct_sword'])
        self.assertNotIn('указаны в таблице добычи', text)

    def test_per_object_references_and_exact_definitions(self):
        text = (DOCS / 'remake-master-brief-ru.md').read_text(encoding='utf-8')
        anchors = set(re.findall(r'<a id="([\w-]+)"></a>', text))
        links = re.findall(r'\]\(#([\w-]+)\)', text)
        self.assertTrue(links)
        self.assertFalse(set(links) - anchors, set(links) - anchors)
        bee = self.cards['effect:bee_sword']
        self.assertIn('(#mob-bee-sword)', bee)
        self.assertNotIn('health 10', bee.lower())
        self.assertIn('таймер 3–8 с', bee)
        for item, card in self.cards.items():
            icon = self.source[item]['minecraft:icon']['texture']
            self.assertIn('ключ атласа `' + icon + '`', card)
            self.assertTrue((ROOT / 'references/remake-assets-2.8.8/Swords_R/textures/items' / (icon + '.png')).is_file())
            components = self.source[item]
            if components.get('minecraft:weapon') or components.get('minecraft:on_use'):
                self.assertIn('#### Точные входы и события предмета 2.8.8', card)
        ice = self.cards['effect:ice_sword']
        rows = re.findall(r'^\| (\d+) \| `@e\[', ice, re.M)
        self.assertEqual([int(x) for x in rows], list(range(1, 41)))
        for actor in ('mob-bee-sword', 'mob-mountable-slime', 'mob-grass-witch',
                      'mob-grass-helper', 'mob-riding-spider', 'mob-centella',
                      'mob-living-flame', 'mob-ghost', 'mob-shulker-shield',
                      'mob-alpha-wolf', 'mob-slime-king', 'mob-creeper'):
            self.assertIn(actor, anchors)

    def test_fire_water_claim_against_recorded_chain(self):
        item_index = (DOCS / 'items-2.8.8.md').read_text(encoding='utf-8')
        section = item_index.split('## effect:fire_sword\n', 1)[1].split('\n## effect:', 1)[0]
        item = json.loads(re.search(r'^```json\s*\n(.*?)\n```', section, re.M | re.S).group(1))
        self.assertNotIn('in_water', json.dumps(item))
        sensors = (DOCS / 'player-sensor-index.md').read_text(encoding='utf-8')
        sensors = sensors.split('## 2.', 1)[1]
        fire_sensors = [line for line in sensors.splitlines() if line.startswith('| ') and
                        'effect:fire_sword' in line and 'on_environment' in line]
        self.assertEqual(len(fire_sensors), 2)
        for row in fire_sensors:
            self.assertIn('"domain":"hand"', row)
            self.assertNotIn('in_water', row)
        ledger = (DOCS / 'entity-ledger-2.8.8.md').read_text(encoding='utf-8')
        player = ledger.split('## `minecraft:player`', 1)[1].split('\n## `', 1)[0]
        event = player.split('**`minecraft:fire_sword`**', 1)[1].split('\n**`', 1)[0]
        stop = player.split('**`stop_fire_sword_event`**', 1)[1].split('\n**`', 1)[0]
        group = next(line for line in player.splitlines() if line.startswith('- `minecraft:fire_sword` ('))
        for text in (event, stop, group):
            self.assertNotIn('"test":"in_water', text)
            self.assertNotIn('replaceitem', text)
            self.assertNotIn('clear @s', text)
        dropped = (DOCS / 'manual-dropped-items-2.8.md').read_text(encoding='utf-8')
        self.assertIn('`fire_sword`, `in_water`', dropped)
        self.assertIn('загрузить `glass_sword`', dropped)
        card = self.cards['effect:fire_sword']
        self.assertIn('Пользователь проверил', card)
        self.assertIn('в ремейк не добавлять', card)
        self.assertIn('выброшенной item-сущности', card)
        audit = json.loads((ROOT / 'data/remake-audits/fire-water-original-2.8.8.json').read_text(encoding='utf-8'))
        self.assertEqual(audit['source_sha256'], 'ab8cbb75c930948f386bf0119bb0a4ee79c084db888c2e9b05deac61b799bb7f')
        self.assertEqual(audit['scanned_text_files'], 282)
        self.assertEqual(set(audit['player_fire_events']), {'minecraft:fire_sword', 'stop_fire_sword_event', 'fire_sword_sound'})
        self.assertEqual([(m['path'], m['line']) for m in audit['inventory_command_literal_matches']],
                         [('Swords_B/entities/player.json', 1595), ('Swords_B/entities/player.json', 1928), ('Swords_B/entities/player.json', 1932)])
        self.assertIn('structure load glass_sword', json.dumps(audit['dropped_item_water_event']))

    def test_recipe_and_loot_details_in_relevant_cards(self):
        text = (DOCS / 'remake-master-brief-ru.md').read_text(encoding='utf-8')
        recipes = (DOCS / 'archive/remake-master-brief-before-item-restructure-ru.md').read_text(encoding='utf-8').split('## Рецепты из сохранённых записей', 1)[1].split('## Колодец', 1)[0]
        entries = re.findall(r'^- \*\*(effect:\w+_sword):\*\* (.*)$', recipes, re.M)
        self.assertEqual(len(entries), 10)
        for item, recipe in entries:
            with self.subTest(recipe=item):
                self.assertIn('**Рецепт:** ' + recipe, self.cards[item])
        checks = {
            'coal_sword': ('1/5',), 'ice_sword': ('1/64', '4/57'),
            'spider_sword': ('3/86',), 'sea_sword': ('15/219',),
            'jungle_sword': ('16/457', '5/41'), 'magma_sword': ('1/24',),
            'emerald_sword': ('5/521', '25/670', '3/28'),
            'lapis_sword': ('5/521', '5/275', '3/28'), 'tnt_sword': ('10/242',),
        }
        for name, values in checks.items():
            with self.subTest(loot=name):
                card = self.cards['effect:' + name]
                line = re.search(r'^\*\*Пулы добычи:\*\* (.*)$', card, re.M).group(1)
                for value in values:
                    self.assertIn(value, line)
                self.assertIn('не шанс всего сундука', line)

    def test_per_item_visual_and_digger_fields(self):
        for item, components in self.source.items():
            with self.subTest(item=item):
                card = self.cards[item]
                foil = 'да' if components['minecraft:foil'] else 'нет'
                off = 'да' if components['minecraft:allow_off_hand'] else 'нет'
                despawn = 'false' if components.get('minecraft:should_despawn') is False else 'не указан'
                self.assertIn(f'блеск foil: {foil}; левая рука: {off}; should_despawn: {despawn};', card)
                digger = components.get('minecraft:digger')
                if digger is None:
                    self.assertIn('digger: компонент не указан', card)
                elif item == 'effect:bedrock_sword':
                    self.assertIn('digger: 68 отдельных правил', card)
                else:
                    speeds = {x['block'].removeprefix('minecraft:'): x['speed'] for x in digger['destroy_speeds']}
                    self.assertIn(f"digger: web {speeds['web']}, bamboo {speeds['bamboo']}", card)
                    if item == 'effect:glass_sword':
                        self.assertTrue(all(r['on_dig']['event'] == 'weapon' for r in digger['destroy_speeds']))
                        self.assertIn('on_dig вызывает weapon', card)

    def test_five_detailed_entity_cards_against_saved_ledger(self):
        ledger = (DOCS / 'entity-ledger-2.8.8.md').read_text(encoding='utf-8')
        def entity(name):
            return ledger.split('## `' + name + '`\n', 1)[1].split('\n## `', 1)[0]
        def component(section, name):
            match = re.search(r'^- `' + re.escape(name) + r'` \(строки [^)]*\): `(.*?)`$', section, re.M)
            self.assertIsNotNone(match, name)
            return json.loads(match.group(1))
        slime = entity('entity:mountable_slime')
        default = component(slime, 'default_slime')
        defense = component(slime, 'defense_mode_slime')
        self.assertEqual(default['minecraft:health']['value'], 1)
        self.assertEqual(default['minecraft:movement']['value'], .25)
        self.assertEqual(defense['minecraft:movement']['value'], .45)
        self.assertEqual(defense['minecraft:attack']['damage'], 1)
        self.assertIn('Повторяющиеся ключи', slime)
        king = entity('entity:slime_king')
        self.assertEqual(component(king, 'minecraft:health')['value'], 300)
        self.assertEqual(component(king, 'minecraft:attack')['damage'], 9)
        self.assertIn('minecraft:movement.jump', king)
        spider = entity('minecraft:spider')
        jockey = component(spider, 'minecraft:spider_player_jockey')
        self.assertEqual(jockey['minecraft:health']['value'], 20)
        self.assertEqual(jockey['minecraft:rideable']['seat_count'], 1)
        self.assertEqual(jockey['minecraft:loot']['table'], 'loot_tables/entities/empty.json')
        web = component(entity('entity:web'), 'minecraft:projectile')
        self.assertEqual((web['power'], web['gravity'], web['on_hit']['impact_damage']['damage']), (1.5, .03, 1))
        fireball = component(entity('entity:fake_fireball'), 'minecraft:projectile')
        self.assertEqual((fireball['power'], fireball['gravity'], fireball['on_hit']['impact_damage']['damage']), (1.3, .02, 5))
        witch = entity('minecraft:witch')
        special = component(witch, 'grass_witch')
        self.assertEqual((special['minecraft:health']['value'], special['minecraft:follow_range']['value']), (32, 80))
        self.assertEqual(component(witch, 'minecraft:behavior.nearest_attackable_target')['entity_types'][0]['max_dist'], 10)
        centella = entity('entity:centella')
        self.assertEqual(component(centella, 'minecraft:health')['value'], 200)
        self.assertEqual(component(centella, 'minecraft:timer')['time'], [10, 60])
        projectile = component(entity('entity:lightning_projectile'), 'minecraft:projectile')
        self.assertEqual((projectile['power'], projectile['gravity']), (2, 0.0))
        text = (DOCS / 'remake-master-brief-ru.md').read_text(encoding='utf-8')
        def mob(anchor):
            return text.split('<a id="' + anchor + '"></a>', 1)[1].split('\n<a id="mob-', 1)[0].lower()
        checks = {
            'mob-slime-king': ('health 300', 'r=1,8', 'повторяются'),
            'mob-mountable-slime': ('health 1', 'movement 0,25', 'повторяющийся ключ'),
            'mob-riding-spider': ('empty.json', 'amplifier 3'),
            'mob-grass-witch': ('follow_range 80', 'max_dist 10', '4%'),
            'mob-centella': ('[10,60]', 'при любом fatal'),
            'mob-bee-sword': ('health 10', 'movement 0,3', '−103'),
        }
        for anchor, fragments in checks.items():
            with self.subTest(anchor=anchor):
                for fragment in fragments:
                    self.assertIn(fragment.lower(), mob(anchor))
        for item, anchor in {'bee_sword':'mob-bee-sword', 'slime_sword':'mob-mountable-slime',
                             'spider_sword':'mob-riding-spider', 'grass_sword':'mob-grass-helper',
                             'lightning_sword':'mob-centella'}.items():
            self.assertIn('(#' + anchor + ')', self.cards['effect:' + item])
        self.assertIn('power 1,3', self.cards['effect:blaze_sword'])
        self.assertIn('0,25×0,25', self.cards['effect:spider_sword'])

    def test_block_records_stay_in_their_own_cards(self):
        text = (DOCS / 'remake-master-brief-ru.md').read_text(encoding='utf-8')
        for identifier, next_header in [
            ('quartz_diamond_ore', '### Кварц-алмазный блок'),
            ('quartz_diamond_block', '### Серебряная руда'),
            ('silver_ore', '## Колодец желаний'),
        ]:
            start = text.index(f'— `effect99:{identifier}`')
            section = text[start:text.index(next_header, start)]
            self.assertIn(f'"identifier": "effect99:{identifier}"', section)
        self.assertRegex(text, r'<a id="mob-slime-king"></a>\n+### Slime King')

    def test_creative_and_visual_properties(self):
        text = (DOCS / 'remake-master-brief-ru.md').read_text(encoding='utf-8')
        self.assertTrue(all(c['minecraft:hand_equipped'] is True and
                            c['minecraft:can_destroy_in_creative'] is False
                            for c in self.source.values()))
        foil_true = {name.removeprefix('effect:') for name, c in self.source.items()
                     if c.get('minecraft:foil') is True}
        self.assertEqual(len(foil_true), 14)
        for item, components in self.source.items():
            hand = components.get('minecraft:render_offsets', {}).get('main_hand')
            if hand:
                card = self.cards[item]
                match = re.search(r'\*\*Положение в основной руке:\*\* первое лицо `({[^`]+})`; третье лицо `({[^`]+})`', card)
                self.assertIsNotNone(match, item)
                self.assertEqual(json.loads(match.group(1)), hand['first_person'])
                self.assertEqual(json.loads(match.group(2)), hand['third_person'])
            else:
                self.assertNotIn('**Положение в основной руке:**', self.cards[item])

    def test_bedrock_digger_rules_exactly_as_saved(self):
        index = (DOCS / 'digger-index.md').read_text(encoding='utf-8')
        source = index.split('## P06\n', 1)[1].split('\n## ', 1)[0]
        source_rows = re.findall(r'^\| \d+ \|.*$', source, re.M)
        brief = (DOCS / 'remake-master-brief-ru.md').read_text(encoding='utf-8')
        section = self.cards['effect:bedrock_sword'].split('#### Все 68 правил добычи', 1)[1]
        copied = re.findall(r'^\| \d+ \|.*$', section, re.M)
        self.assertEqual(len(source_rows), 68)
        self.assertEqual(copied, source_rows)
        self.assertEqual(len(self.source['effect:bedrock_sword']['minecraft:digger']['destroy_speeds']), 68)
        rules = []
        for line in copied:
            row = re.match(r'^\| (\d+) \| `(.*?)` \| `(.*?)` \|$', line)
            self.assertIsNotNone(row)
            self.assertEqual(int(row.group(1)), len(rules) + 1)
            rules.append({'block': json.loads(row.group(2)), **json.loads(row.group(3))})
        self.assertEqual(rules, self.source['effect:bedrock_sword']['minecraft:digger']['destroy_speeds'])

    def test_weapon_event_models_against_saved_index(self):
        text = (DOCS / 'weapon-event-index.md').read_text(encoding='utf-8').split('## Полные event', 1)[0]
        models = {}
        for line in text.splitlines():
            m = re.match(r'^\| \[`(effect:[^`]+)`\].*\| ([^|]+) \|$', line)
            if m:
                models[m.group(1)] = m.group(2).strip().strip('`')
        for item_id, card in self.cards.items():
            with self.subTest(item=item_id):
                if item_id == 'effect:bedrock_sword':
                    self.assertEqual(models[item_id], 'пустой `minecraft:weapon')
                    self.assertIn('компонент weapon пуст; явного события износа не записано', card)
                else:
                    self.assertIn(f'**Условная модель износа weapon-события:** {models[item_id]}.', card)

    def test_documented_fuel_cooldown_and_entity_timer_units(self):
        with ZipFile(ROOT / 'references' / 'bedrock' / 'creator-docs-markdown.zip') as z:
            def doc(suffix):
                names = [n for n in z.namelist() if n.endswith(suffix)]
                self.assertEqual(len(names), 1)
                return z.read(names[0]).decode('utf-8')
            fuel = doc('/ItemComponents/minecraft_fuel.md')
            cooldown = doc('/ItemComponents/minecraft_cooldown.md')
            timer = doc('/EntityComponents/minecraftComponent_timer.md')
            self.assertRegex(fuel, r'(?i)duration[^\n]*seconds')
            self.assertRegex(cooldown, r'(?i)duration[^\n]*seconds')
            self.assertRegex(timer, r'(?i)time \(Legacy FloatRange\)[^\n]*seconds')
        self.assertIn('fuel duration 360', self.cards['effect:coal_sword'])
        self.assertIn('6 минут', self.cards['effect:coal_sword'])

    def test_shulker_levitation_amplifier(self):
        # В записи команда effect ... levitation 1 18; усилитель нумеруется с нуля.
        self.assertIn('левитацию XIX на 1 секунду', self.cards['effect:shulker_sword'])

    def test_bone_acquisition_keeps_brightness_without_separate_night(self):
        card = self.cards['effect:bone_sword']
        self.assertIn('brightness < 0,49', card)
        self.assertIn('без отдельной проверки ночи', card)
        self.assertIn('7 из 1000', card)

    def test_ghost_spawn_uses_light_not_separate_time_limit(self):
        text = (DOCS / 'remake-master-brief-ru.md').read_text(encoding='utf-8')
        ghost = text.split('### Призрак — `entity:ghost`', 1)[1].split('#### Записанные компоненты', 1)[0]
        self.assertIn('не добавлять отдельный запрет дня ни для одной ветви', ghost)
        self.assertIn('При brightness >0,1 указан despawn', ghost)

    def test_quartz_ore_and_block_damage_targets_nearest_player(self):
        text = (DOCS / 'remake-master-brief-ru.md').read_text(encoding='utf-8')
        self.assertIn('для руды и блока сохранить выбор ближайшего игрока в радиусе 6', text)
        self.assertIn('сохранить выбор ближайшего игрока, даже если это не добывающий игрок', text)

    def test_ender_damage_and_wet_projectile_decision(self):
        card = self.cards['effect:ender_sword']
        for text in ('при любом неснарядном уроне', 'вероятностью 50%',
                     'как у обычного эндермена целевой версии', 'при приёмке',
                     'не более одной телепортации на одно событие урона'):
            self.assertIn(text, card)

    def test_shulker_give_and_bee_block_decisions(self):
        text = (DOCS / 'remake-master-brief-ru.md').read_text(encoding='utf-8')
        for required in ('в двух заполненных шалкерах по 19', 'две свободные ячейки',
                         'ничего не выдавать', 'шалкеры не выбрасывать',
                         'при запуске командным блоком — ближайший к блоку игрок'):
            self.assertIn(required, text)
        bee = self.cards['effect:bee_sword']
        self.assertIn('постановка цветка может заменить уже находящийся там блок', bee)
        self.assertIn('попытка действует при атаке обычной пчелой игрока или другого моба', bee)

    def test_internal_navigation_has_no_broken_or_duplicate_targets(self):
        text = (DOCS / 'remake-master-brief-ru.md').read_text(encoding='utf-8')
        anchors = re.findall(r'<a id="([^"]+)"></a>', text)
        links = re.findall(r'\]\(#([^)]+)\)', text)
        self.assertEqual(len(anchors), len(set(anchors)))
        self.assertEqual(len(anchors), 51)
        self.assertTrue(links)
        self.assertEqual(set(links) - set(anchors), set())

    def test_handbook_preserves_user_decisions(self):
        text = (DOCS / 'remake-master-brief-ru.md').read_text(encoding='utf-8')
        for required in ('независимая попытка', '0,8%', '2,5%',
                         'сохранять и точно возвращать', 'не удалять выброшенные предметы'):
            self.assertIn(required, text.lower())
        basis = (DOCS / 'remake-working-basis-ru.md').read_text(encoding='utf-8')
        self.assertIn('только после отдельного разрешения пользователя', basis.lower())


if __name__ == '__main__':
    unittest.main()
