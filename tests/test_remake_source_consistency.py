"""Сверка карточек с предметами разрешённого оригинала 2.8.8, без запуска игры."""

import json
import re
import unittest
from fractions import Fraction
from pathlib import Path
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'sources' / 'swordsandmoreswords_2_8_8.mcaddon'
BRIEF = ROOT / 'docs' / 'remake-master-brief-ru.md'


def parse_json_with_comments(data):
    """Удалить комментарии вне строк и конечные запятые в исходном JSON."""
    text = data.decode('utf-8-sig')
    comment_or_string = r'("(?:\\.|[^"\\])*")|(//[^\n]*|/\*.*?\*/)'
    text = re.sub(comment_or_string, lambda m: m.group(1) or '', text, flags=re.S)
    return json.loads(re.sub(r',(?=\s*[}\]])', '', text))


def number_at_start(text):
    match = re.match(r'[-−\d.,]+', text.strip())
    return float(match.group().replace('−', '-').replace(',', '.')) if match else None


def flatten_event_for_audit(event):
    """Collect exact action fields, sequence lengths and ordered branch weights."""
    actions, sequences, alternatives = {}, {}, {}
    def walk(node, path='$'):
        if not isinstance(node, dict):
            raise AssertionError('Unexpected non-object event node')
        ordinary = {k:v for k,v in node.items() if k not in ('weight', 'sequence', 'randomize')}
        if ordinary:
            actions[path] = ordinary
        if 'sequence' in node:
            if not isinstance(node['sequence'], list):
                raise AssertionError('Unexpected sequence structure')
            sequences[path + '.sequence'] = len(node['sequence'])
            for i, child in enumerate(node['sequence']):
                walk(child, f'{path}.sequence[{i}]')
        if 'randomize' in node:
            if not isinstance(node['randomize'], list):
                raise AssertionError('Unexpected randomize structure')
            alternatives[path + '.randomize'] = [c.get('weight') for c in node['randomize']]
            for i, child in enumerate(node['randomize']):
                walk(child, f'{path}.randomize[{i}]')
    walk(event)
    return actions, sequences, alternatives


def recorded_event_tree(text):
    actions = {k:json.loads(v) for k,v in re.findall(r'- `([^`]+)` — поля действия: `([^\n]+?)`', text)}
    sequences = {k:int(v) for k,v in re.findall(r'- `([^`]+)`:\s*(\d+) шаг\(ов\), порядок', text)}
    alternatives = {k:json.loads(v) for k,v in re.findall(r'- `([^`]+)`:\s*альтернативы, веса `([^`]+)`', text)}
    return actions, sequences, alternatives


class OriginalItemConsistency(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        text = BRIEF.read_text(encoding='utf-8')
        cls.cards = dict(re.findall(
            r'### \d+\. .*?`(effect:[^`]+)`\n(.*?)(?=\n<a id="sword-|\n## |\Z)',
            text, re.S,
        ))
        cls.items = {}
        with ZipFile(SOURCE) as source:
            for name in source.namelist():
                if name.startswith('Swords_B/items/') and name.endswith('.json'):
                    item = parse_json_with_comments(source.read(name))['minecraft:item']
                    cls.items[item['description']['identifier']] = item

    def test_all_38_swords_have_source_items(self):
        self.assertEqual(len(self.cards), 38)
        self.assertFalse(set(self.cards) - set(self.items))

    def test_recorded_item_components_and_events_match_archive(self):
        recorded = (ROOT / 'docs' / 'items-2.8.8.md').read_text(encoding='utf-8')
        parts = re.split(r'^## (effect:[^\n]+)\s*$', recorded, flags=re.M)
        records = {}
        for identifier, section in zip(parts[1::2], parts[2::2]):
            match = re.search(r'^```json\s*\n(.*?)\n```', section, re.M | re.S)
            if identifier in self.cards and match:
                records[identifier] = json.loads(match.group(1))
        self.assertEqual(set(records), set(self.cards))
        for identifier, saved in records.items():
            with self.subTest(item=identifier):
                self.assertEqual(saved['components'], self.items[identifier]['components'])
                self.assertEqual(saved.get('events', {}), self.items[identifier].get('events', {}))

    def test_item_card_raw_event_excerpts_match_original(self):
        # Независимо от отдельного индекса items-2.8.8.md.
        for identifier, card in self.cards.items():
            with self.subTest(item=identifier):
                excerpt = card.split('#### Точные входы и события предмета 2.8.8', 1)[1]
                match = re.search(r'```json\s*(.*?)\s*```', excerpt, re.S)
                self.assertIsNotNone(match)
                recorded = json.loads(match.group(1))
                original = self.items[identifier]
                for key, value in recorded['components'].items():
                    self.assertEqual(value, original['components'][key])
                self.assertEqual(recorded.get('events', {}), original.get('events', {}))

    def test_recorded_player_group_and_event_excerpts_match_original(self):
        # Перенесённые выписки, не исчерпывающий граф вызовов и не итоговое поведение.
        with ZipFile(SOURCE) as source:
            player = parse_json_with_comments(source.read('Swords_B/entities/player.json'))['minecraft:entity']
        cards = groups_count = events_count = 0
        for identifier, card in self.cards.items():
            heading = '#### Записанные группы и события владельца 2.8.8'
            if heading not in card:
                continue
            cards += 1
            section = card.split(heading, 1)[1]
            groups = section.split('**Группы:**', 1)[-1].split('**События:**', 1)[0]
            for name, value in re.findall(r'^- `([^`]+)` \(строки [^\n]*?\): `([^\n]*)`$', groups, re.M):
                with self.subTest(item=identifier, group=name):
                    self.assertEqual(json.loads(value), player['component_groups'][name])
                    groups_count += 1
            if '**События:**' not in section:
                continue
            events = section.split('**События:**', 1)[1]
            parts = re.split(r'^\*\*`([^`]+)`\*\* \(строки [^\n]*\):\s*$', events, flags=re.M)
            for name, content in zip(parts[1::2], parts[2::2]):
                with self.subTest(item=identifier, event=name):
                    self.assertEqual(recorded_event_tree(content), flatten_event_for_audit(player['events'][name]))
                    events_count += 1
        self.assertEqual((cards, groups_count, events_count), (31, 42, 94))

    def test_nether_star_summon_is_weapon_step_not_projectile_hit(self):
        item = self.items['effect:nether_star_sword']
        steps = item['events']['weapon']['sequence']
        self.assertEqual(steps[0]['shoot']['projectile'], 'entity:nether_star_projectile')
        self.assertEqual([x['weight'] for x in steps[1]['randomize']], [80, 20])
        self.assertEqual([x['run_command']['command'] for x in steps[1]['randomize']], [
            ['summon entity:nether_star ^ ^20 ^-6'],
            ['summon entity:nether_star ^ ^20 ^-6', 'summon entity:nether_star ^ ^18 ^-6']])
        self.assertEqual([x['weight'] for x in steps[2]['randomize']], [9999, 1])
        with ZipFile(SOURCE) as source:
            def entity(name):
                return parse_json_with_comments(source.read('Swords_B/entities/' + name + '.json'))['minecraft:entity']
            projectile, star, objective, player = (entity(n) for n in ('nether_star_projectile', 'entity_nether_star', 'objective', 'player'))
        group = projectile['component_groups']['nether_star_sword']['minecraft:projectile']
        self.assertEqual(group['on_hit']['definition_event']['event_trigger']['event'], 'set_objective')
        self.assertEqual(projectile['events']['set_objective']['run_command']['command'], ['summon entity:objective'])
        self.assertEqual(star['components']['minecraft:shooter']['def'], 'entity:nether_star_projectile')
        self.assertEqual(star['components']['minecraft:timer']['time'], [.5, .5])
        self.assertEqual(objective['components']['minecraft:timer']['time'], [1, 1])
        sensor = player['component_groups']['minecraft:nether_star_sword']['minecraft:damage_sensor']['triggers']
        self.assertFalse(sensor['deals_damage'])
        self.assertEqual(sensor['on_damage']['filters']['all_of'][0]['value'], 'nether_star_projectile')
        card = self.cards['effect:nether_star_sword']
        self.assertIn('Вызов звёзд не поставлен в зависимость от попадания', card)
        self.assertNotIn('снаряд вызывает падающие звёзды', card)

    def test_ice_forty_source_operations_and_accepted_radius(self):
        card = self.cards['effect:ice_sword']
        section = card.split('#### Точные 40 операций исходной формы', 1)[1].split('#### Точные входы', 1)[0]
        rows = re.findall(r'^\|\s*(\d+)\s*\|\s*`([^`]+)`\s*\|\s*`([^`]+)`\s*\|\s*`([^`]+)` → `([^`]+)`\s*\|\s*(\d+)\s*\|\s*`([^`]+)`\s*\|$', section, re.M)
        item = self.items['effect:ice_sword']
        commands = item['events']['on_use']['sequence'][0]['run_command']['command']
        fills = [c for c in commands if c.startswith('execute @e[') and ' fill ' in c]
        self.assertEqual(len(rows), 40)
        self.assertEqual(len(fills), 40)
        for i, (row, original) in enumerate(zip(rows, fills), 1):
            number, selector, origin, first, last, volume, material = row
            self.assertEqual(int(number), i)
            self.assertEqual(f'execute {selector} {origin} fill {first} {last} {material}', original)
            self.assertIn('r=12', selector)
            def coordinates(point):
                return [float(x[1:] or 0) for x in point.split()]
            sizes = [abs(a-b)+1 for a,b in zip(coordinates(first), coordinates(last))]
            self.assertEqual(int(volume), sizes[0]*sizes[1]*sizes[2])
        self.assertIn('согласован максимальный радиус **8**', section)

    def test_selected_owner_activation_sensors_preserve_hand_and_stop_filters(self):
        with ZipFile(SOURCE) as source:
            player = parse_json_with_comments(source.read('Swords_B/entities/player.json'))['minecraft:entity']
        sensors = [x['on_environment'] for x in player['components']['minecraft:environment_sensor']]
        for sword in ('bee', 'ice', 'nether_star', 'blaze', 'slime', 'sea', 'cactus', 'jungle', 'spider', 'shulker', 'grass', 'fire', 'obsidian', 'magma'):
            identifier = 'effect:' + sword + '_sword'
            for event, operator in [('minecraft:' + sword + '_sword', None), ('stop_' + sword + '_sword_event', '!=')]:
                with self.subTest(item=identifier, event=event):
                    matches = [x for x in sensors if x['event'] == event]
                    self.assertEqual(len(matches), 1)
                    condition = matches[0]['filters']['all_of']
                    expected = {'test':'has_equipment', 'subject':'self', 'domain':'hand', 'value':identifier}
                    if operator:
                        expected['operator'] = operator
                    self.assertEqual(condition, [expected])

    def test_spreadplayers_arguments_are_not_minimum_displacements(self):
        ender = self.items['effect:ender_sword']
        self.assertIn('spreadplayers ~ ~ 16 32 @s', ender['events']['on_use']['run_command']['command'])
        with ZipFile(SOURCE) as source:
            player = parse_json_with_comments(source.read('Swords_B/entities/player.json'))['minecraft:entity']
        self.assertIn('spreadplayers ~ ~ 1 3 @s', player['events']['ultra_instinct_sword_skill']['run_command']['command'])
        self.assertIn('не доказывает минимальную дистанцию 16', self.cards['effect:ender_sword'])
        self.assertIn('не задаёт гарантированную минимальную дистанцию 1', self.cards['effect:ultra_instinct_sword'])
        with ZipFile(ROOT / 'references' / 'bedrock' / 'creator-docs-markdown.zip') as docs:
            text = docs.read('creator/Commands/commands/spreadplayers.md').decode('utf-8-sig')
        self.assertIn('The distance between players when they spawn.', text)

    def test_spectral_crystal_spawn_selection_and_scale_are_distinct(self):
        spectral = self.items['effect:spectral_sword']['events']
        explosion = spectral['weapon']['randomize'][1]
        self.assertEqual(explosion['weight'], 1)
        command = explosion['run_command']['command'][0]
        self.assertEqual(command, 'event entity @e[type=ender_crystal,family=!ender_crystal_default,family=!ender_crystal_scale,c=1] minecraft:crystal_explode')
        self.assertIn('family=!ender_crystal_scale,c=1,r=4', spectral['on_use']['run_command']['command'][1])
        with ZipFile(SOURCE) as source:
            player = parse_json_with_comments(source.read('Swords_B/entities/player.json'))['minecraft:entity']
            crystal = parse_json_with_comments(source.read('Swords_B/entities/ender_crystal.json'))['minecraft:entity']
            references = [name for name in source.namelist() if name.startswith(('Swords_B/', 'Swords_R/')) and name.endswith(('.json', '.mcfunction', '.js')) and b'spectral_sword_reload_skill' in source.read(name)]
        group = player['component_groups']['minecraft:spectral_sword']
        self.assertEqual(group['minecraft:timer']['time'], [.4, .4])
        self.assertFalse(group['minecraft:timer']['looping'])
        branch = player['events']['spectral_sword_skills']['sequence'][0]
        self.assertEqual(branch['filters'], {'test':'has_biome_tag','operator':'!=','value':'the_end'})
        scale = crystal['component_groups']['ender_crystal_scale']
        self.assertEqual(scale['minecraft:ageable']['duration'], 18)
        self.assertEqual(scale['minecraft:scale_by_age'], {'start_scale':.1,'end_scale':1})
        self.assertEqual(references, ['Swords_B/entities/player.json'])
        self.assertIn('не создавать кристалл в биоме с тегом `the_end`', self.cards['effect:spectral_sword'])
        self.assertIn('после повторного снятия и взятия меча', self.cards['effect:spectral_sword'])
        self.assertIn('не доказывает исчезновение существующего кристалла', self.cards['effect:spectral_sword'])
        self.assertIn('при выстреле уменьшать и растить только собственный подходящий кристалл владельца в r=4', self.cards['effect:spectral_sword'])
        self.assertIn('кристалл не менять, но выстрел выполнять', self.cards['effect:spectral_sword'])

    def test_base_damage_and_explicit_durability_match_288(self):
        for identifier, card in self.cards.items():
            with self.subTest(item=identifier):
                components = self.items[identifier]['components']
                fields = re.search(r'\*\*Урон:\*\*\s*(.*?)\. \*\*Прочность:\*\*\s*(.*?)\.', card)
                self.assertIsNotNone(fields)
                self.assertEqual(number_at_start(fields.group(1)), components['minecraft:damage'])
                durability = components.get('minecraft:durability', {}).get('max_durability')
                if durability is not None:
                    self.assertEqual(number_at_start(fields.group(2)), durability)

    def test_original_give_function_gaps_are_identified(self):
        with ZipFile(SOURCE) as source:
            function = source.read('Swords_B/functions/give.mcfunction').decode('utf-8-sig')
        commands = re.findall(r'^give\s+@(\w+)\s+(effect:[a-z_]+)', function, re.M)
        self.assertEqual(len(commands), 35)
        self.assertEqual(set(self.cards) - {item for _, item in commands},
                         {'effect:bee_sword', 'effect:wet_sponge_sword', 'effect:cursed_pumpkin_sword'})
        self.assertEqual([item for selector, item in commands if selector == 's'], ['effect:lightning_sword'])

    def test_direct_archive_chest_sword_entries_and_fishing_links(self):
        expected = {
            ('abandoned_mineshaft', 'spider_sword'): ({'min': 2, 'max': 4}, 3, 86),
            ('buriedtreasure', 'sea_sword'): ({'min': 5, 'max': 12}, 15, 219),
            ('desert_pyramid', 'tnt_sword'): ({'min': 2, 'max': 4}, 10, 242),
            ('igloo_chest', 'ice_sword'): ({'min': 2, 'max': 8}, 1, 64),
            ('jungle_temple', 'jungle_sword'): ({'min': 2, 'max': 6}, 16, 457),
            ('pillager_outpost', 'emerald_sword'): ({'min': 2, 'max': 3}, 3, 28),
            ('pillager_outpost', 'lapis_sword'): ({'min': 2, 'max': 3}, 3, 28),
            ('spawn_bonus_chest', 'coal_sword'): (1, 1, 5),
            ('stronghold_corridor', 'emerald_sword'): ({'min': 2, 'max': 3}, 5, 521),
            ('stronghold_corridor', 'lapis_sword'): ({'min': 2, 'max': 3}, 5, 521),
            ('stronghold_library', 'lapis_sword'): ({'min': 2, 'max': 10}, 5, 275),
            ('underwater_ruin_big', 'magma_sword'): (1, 1, 24),
            ('village/village_snowy_house', 'ice_sword'): ({'min': 3, 'max': 8}, 4, 57),
            ('woodland_mansion', 'emerald_sword'): ({'min': 1, 'max': 3}, 25, 670),
        }
        found = {}
        with ZipFile(SOURCE) as source:
            prefix = 'Swords_B/loot_tables/chests/'
            for path in source.namelist():
                if not path.startswith(prefix) or not path.endswith('.json'):
                    continue
                data = parse_json_with_comments(source.read(path))
                for pool in data.get('pools', []):
                    for entry in pool.get('entries', []):
                        identifier = entry.get('name', '')
                        if identifier not in self.cards:
                            continue
                        key = (path[len(prefix):-5], identifier.removeprefix('effect:'))
                        self.assertNotIn(key, found)
                        self.assertFalse(pool.get('conditions'))
                        self.assertFalse(entry.get('conditions'))
                        found[key] = (pool['rolls'], entry.get('weight', 1),
                                      sum(x.get('weight', 1) for x in pool['entries']))
                        self.assertIn(f"{entry.get('weight', 1)}/{found[key][2]}", self.cards[identifier])
                        if key[0] == 'pillager_outpost':
                            self.assertEqual(entry['functions'][0]['count'], {'min': 0, 'max': 1})
                            self.assertIn('count 0–1', self.cards[identifier])
            self.assertEqual(found, expected)
            treasure = parse_json_with_comments(source.read('Swords_B/loot_tables/gameplay/fishing/treasure.json'))['pools'][0]
            self.assertEqual(treasure['rolls'], 1)
            entry, = [x for x in treasure['entries'] if x.get('name') == 'effect:jungle_sword']
            self.assertEqual((entry['weight'], sum(x.get('weight', 1) for x in treasure['entries'])), (5, 41))
            for path in ('fishing', 'jungle_fishing'):
                main = parse_json_with_comments(source.read(f'Swords_B/loot_tables/gameplay/{path}.json'))['pools'][0]
                ref, = [x for x in main['entries'] if x['name'] == 'loot_tables/gameplay/fishing/treasure.json']
                self.assertEqual((main['rolls'], ref['weight'], ref['quality']), (1, 5, 2))
            self.assertIn('рыбалка только в биоме джунглей', self.cards['effect:jungle_sword'])
            self.assertIn('5/41', self.cards['effect:jungle_sword'])

    def test_dropped_item_source_event_routing(self):
        with ZipFile(SOURCE) as source:
            item = parse_json_with_comments(source.read('Swords_B/entities/item.json'))['minecraft:entity']
            controller = parse_json_with_comments(source.read('Swords_B/animation_controllers/item_events.json'))['animation_controllers']['controller.animation.item_events']
        states = controller['states']
        self.assertEqual(states['default']['transitions'], [{'on_fire_swords': 'q.is_on_fire'}])
        commands = states['on_fire_swords']['on_entry']
        expected = ['fire_sword_event_3', 'despawn_event_5', 'despawn_event_4', 'despawn_event_1', 'despawn_event_2', 'despawn_event_3', 'despawn_event_6', 'respawn_event_1', 'respawn_event_2']
        self.assertEqual([x.rsplit(' ', 1)[-1] for x in commands], expected)
        self.assertIn('tag=!fire_sword_respawn', commands[0])
        events = item['events']
        self.assertNotIn('kill @s', events['despawn_event_3']['run_command']['command'])
        for group, seconds, event in [('fire_sword', [5, 6], 'fire_sword_event_1'), ('sponge_sword', [0, 1], 'wet_sponge_sword')]:
            timer = item['component_groups'][group]['minecraft:timer']
            self.assertEqual(timer['time'], seconds)
            self.assertFalse(timer['looping'])
            self.assertEqual(timer['time_down_event']['event'], event)
        self.assertIn('structure load glass_sword ~ ~ ~', events['fire_sword_event_2']['run_command']['command'])
        self.assertIn('structure load obsidian_sword ~ ~ ~', events['fire_sword_event_1']['run_command']['command'])
        sponge_commands = events['sponge_sword_event']['sequence'][1]['run_command']['command']
        self.assertIn('fill ~2 ~2 ~2 ~-2 ~-2 ~-2 air 0 replace sponge', sponge_commands)
        self.assertIn('fill ~2 ~2 ~2 ~-2 ~-2 ~-2 air 0 replace seagrass', sponge_commands)
        self.assertIn('Выброшенный Sponge', self.cards['effect:sponge_sword'])
        self.assertIn('ранее существовавшие блоки губки сохранять', self.cards['effect:sponge_sword'])

    def test_direct_three_block_harvest_paths_and_enchant_limits(self):
        with ZipFile(SOURCE) as source:
            self.assertNotIn('Swords_B/loot_tables/blocks/null.json', source.namelist())
            for block in ('quartz_diamond_ore', 'quartz_diamond_block', 'silver_ore'):
                with self.subTest(block=block):
                    data = parse_json_with_comments(source.read(f'Swords_B/blocks/{block}.json'))['minecraft:block']
                    self.assertEqual(data['components']['minecraft:loot'], 'loot_tables/blocks/null.json')
                    destroy = data['components']['minecraft:on_player_destroyed']
                    self.assertEqual(destroy['event'], block)
                    self.assertEqual([t for t in ('iron_pickaxe','diamond_pickaxe','netherite_pickaxe','bedrock_sword') if t in destroy['condition']], ['iron_pickaxe','diamond_pickaxe','netherite_pickaxe','bedrock_sword'])
                    table_path = data['events'][block]['spawn_loot']['table']
                    self.assertEqual(table_path, f'loot_tables/blocks/{block}.json')
                    raw = source.read('Swords_B/'+table_path)
                    loot = parse_json_with_comments(raw)
                    self.assertEqual(loot['pools'][0]['rolls'], 1)
                    self.assertNotIn(b'silk_touch', raw)
                    self.assertNotIn(b'looting', raw)
                    self.assertNotIn(b'fortune', raw)
                    self.assertTrue(all(f['function'] == 'set_count' for e in loot['pools'][0]['entries'] for f in e.get('functions', [])))
        brief = BRIEF.read_text(encoding='utf-8')
        self.assertEqual(brief.count('неподходящим инструментом блок разрушается без выпадения, специального урона и сфер опыта'), 3)
        self.assertIn('Шёлковое касание подходящей кирки выдаёт сам блок руды', brief)
        self.assertIn('при Шёлковом касании и при Удаче сохранять шесть сфер опыта', brief)

    def test_direct_ore_generation_rule_and_feature_constraints(self):
        with ZipFile(SOURCE) as source:
            for ore, y, biomes, blocks in (
                ('quartz_diamond', [0,16], ['overworld','the_end'], ['minecraft:stone','minecraft:end_stone']),
                ('silver', [10,35], ['overworld'], ['minecraft:stone']),
            ):
                with self.subTest(ore=ore):
                    path = f'Swords_B/feature_rules/{ore}_ore_feature.json'
                    rule = parse_json_with_comments(source.read(path))['minecraft:feature_rules']
                    dist = rule['distribution']
                    self.assertEqual(rule['description']['places_feature'], f'effect99:{ore}_ore')
                    self.assertEqual([x['value'] for x in rule['conditions']['minecraft:biome_filter']['any_of']], biomes)
                    self.assertEqual(rule['conditions']['placement_pass'], 'underground_pass')
                    self.assertEqual((dist['iterations'], dist['y']['distribution'], dist['y']['extent']), (5,'gaussian',y))
                    self.assertEqual(dist['scatter_chance'], {'numerator':160,'denominator':200})
                    feat = parse_json_with_comments(source.read(f'Swords_B/features/{ore}_ore.json'))['minecraft:structure_template_feature']
                    self.assertEqual(feat['structure_name'], f'mystructure:{ore}_ore')
                    self.assertEqual(feat['adjustment_radius'], 1)
                    self.assertEqual([x['name'] for x in feat['constraints']['block_intersection']['block_allowlist']], blocks)

    def test_direct_material_and_wither_effect(self):
        stick = self.items['effect:quartz_diamond_stick']
        self.assertEqual(stick['components']['minecraft:damage'], 24)
        self.assertEqual(stick['components']['minecraft:durability']['max_durability'], 20)
        self.assertEqual(set(stick['components']['minecraft:weapon']), {'on_hurt_entity','on_not_hurt_entity','on_hit_block'})
        branches = stick['events']['weapon']['randomize']
        self.assertEqual([b['weight'] for b in branches], [10,85,5])
        self.assertEqual([b['run_command']['command'] for b in branches], [['damage @s 1 magic'], ['damage @s 3 magic'], ['damage @s 6 magic']])
        bedrock_stick = self.items['effect:bedrock_stick']
        self.assertEqual(bedrock_stick['components']['minecraft:damage'], 6)
        self.assertNotIn('minecraft:durability', bedrock_stick['components'])
        self.assertEqual(self.items['effect:quartz_diamond']['components']['minecraft:max_stack_size'], 9)
        with ZipFile(SOURCE) as source:
            effect = parse_json_with_comments(source.read('Swords_B/entities/wither_effect.json'))['minecraft:entity']
        projectile = effect['components']['minecraft:projectile']
        self.assertEqual(projectile['on_hit']['mob_effect'], {'effect':'wither','durationeasy':200,'durationnormal':200,'durationhard':200,'amplifier':0})
        self.assertEqual(projectile['on_hit']['impact_damage']['damage'], 0)
        self.assertIn('Wither I на 10 секунд', self.cards['effect:wither_skeleton_sword'])

    def test_direct_sponge_water_condition_and_per_player_counter(self):
        with ZipFile(SOURCE) as source:
            player = parse_json_with_comments(source.read('Swords_B/entities/player.json'))['minecraft:entity']
        steps = player['events']['minecraft:sponge_sword']['sequence']
        self.assertEqual(steps[1]['filters'], {'test': 'in_water_or_rain'})
        self.assertIn('fill ~2 ~2 ~2 ~-2 ~-2 ~-2 sponge 0 replace water', steps[1]['run_command']['command'])
        self.assertIn('scoreboard players add @s sponge_sword 1', steps[1]['run_command']['command'])
        self.assertNotIn('filters', steps[2])
        self.assertIn('fill ~2 ~2 ~2 ~-2 ~-2 ~-2 air 0 replace seagrass', steps[2]['run_command']['command'])
        self.assertEqual([n for n in (150,155,160) if any(f'sponge_sword={n}' in c for c in steps[2]['run_command']['command'])], [150,155,160])
        stop = json.dumps(player['events']['stop_sponge_sword_event'])
        self.assertNotIn('scoreboard', stop)
        wet = player['events']['wet_sponge_sword']['sequence'][0]['run_command']['command']
        self.assertIn('scoreboard players set @s sponge_sword 0', wet)
        self.assertIn('Исходный счёт относится к игроку', self.cards['effect:sponge_sword'])
        self.assertIn('только при `in_water_or_rain` владельца', self.cards['effect:sponge_sword'])
        self.assertIn('как в оригинале, вода поглощается только при нахождении владельца в воде или под дождём', self.cards['effect:sponge_sword'])

    def test_direct_clock_coal_glass_and_wet_sponge_chains(self):
        clock = self.items['effect:clock_sword']
        coal = self.items['effect:coal_sword']
        glass = self.items['effect:glass_sword']
        wet = self.items['effect:wet_sponge_sword']
        self.assertEqual(coal['components']['minecraft:fuel']['duration'], 360)
        self.assertEqual(clock['events']['on_use']['damage']['amount'], 10)
        self.assertIn('clock_sword_skill_event', clock['events']['on_use']['run_command']['command'][0])
        self.assertEqual(glass['components']['minecraft:durability']['max_durability'], 1)
        self.assertEqual(glass['events']['weapon']['sequence'][0]['damage']['amount'], 10)
        self.assertEqual(glass['events']['weapon']['sequence'][0]['run_command']['command'], ['playsound random.glass @a[r=8,m=0]'])
        self.assertIn('обычный удар без чар ломает меч', self.cards['effect:glass_sword'])
        self.assertEqual(wet['components']['minecraft:damage'], 3)
        self.assertEqual(list(wet['events']), ['weapon'])
        with ZipFile(SOURCE) as source:
            player = parse_json_with_comments(source.read('Swords_B/entities/player.json'))['minecraft:entity']
            skill = player['component_groups']['clock_sword_skill']['minecraft:timer']
            self.assertEqual(skill['time'], [5,5])
            self.assertEqual(skill['time_down_event']['event'], 'stop_clock_sword_event')
            action = player['events']['minecraft:clock_sword']['sequence'][1]
            self.assertEqual(action['filters']['value'], 'clock_sword_skill')
            self.assertEqual(action['run_command']['command'], ['gamerule randomtickspeed 100', 'effect @e[type=!player] speed 1 10 true', 'time add 10', 'event entity @a[family=default_player] clock_sword_movement'])

    def test_selected_intersections_fire_ice_and_transformed_player(self):
        with ZipFile(SOURCE) as source:
            player = parse_json_with_comments(source.read('Swords_B/entities/player.json'))['minecraft:entity']
            flame = parse_json_with_comments(source.read('Swords_B/entities/living_flame.json'))['minecraft:entity']
            bone = parse_json_with_comments(source.read('Swords_B/entities/skeleton.json'))['minecraft:entity']
            centella = parse_json_with_comments(source.read('Swords_B/entities/centella.json'))['minecraft:entity']
            ghost = parse_json_with_comments(source.read('Swords_B/entities/ghost.json'))['minecraft:entity']
        fire_commands = player['events']['minecraft:fire_sword']['sequence'][1]['run_command']['command']
        self.assertIn('execute @e[family=!player,type=!item,r=3] ~ ~ ~ summon entity:fire', fire_commands)
        targets = flame['component_groups']['passive_entity']['minecraft:behavior.nearest_attackable_target']['entity_types'][0]['filters']['any_of']
        self.assertEqual(targets[0]['value'], 'monster')
        for entity in (bone, centella, ghost):
            self.assertIn('player', json.dumps(entity['components']['minecraft:damage_sensor']))
        text = BRIEF.read_text(encoding='utf-8')
        self.assertIn('минимальные расстояния `rm=2` и `rm=3` не применять', text)
        self.assertIn('владельца не выбирать целью, прочие исключения типов и формы сохранять', text)
        self.assertIn('игроков независимо от их формы выбирать для ближнего поджога только при включённом PvP', text)
        self.assertIn('пассивное Living Flame, выпущенное мечом, не выбирает владельца и призванных помощников любых игроков', text)
        self.assertIn('при проверках получения наград и соответствующих реакций учитывать реального игрока', text)

    def test_magma_water_sound_filter_and_documented_default(self):
        with ZipFile(SOURCE) as source:
            player = parse_json_with_comments(source.read('Swords_B/entities/player.json'))['minecraft:entity']
        branch = player['events']['minecraft:magma_sword']['sequence'][2]
        self.assertEqual(branch['filters'], {'test':'in_water','operator':'=='})
        self.assertEqual([x['weight'] for x in branch['randomize']], [99,1])
        self.assertIn('playsound bubble.up @a ~ ~ ~ 1 0.9', branch['randomize'][1]['run_command']['command'])
        with ZipFile(Path('references/bedrock/creator-docs-markdown.zip')) as docs:
            reference = docs.read('creator/Reference/Content/EntityReference/Examples/Filters/in_water.md').decode('utf-8')
        self.assertIn('Does not require any parameters', reference)
        self.assertIn('| value | true |', reference)
        self.assertIn('условная попытка звука при нахождении владельца в воде', BRIEF.read_text(encoding='utf-8'))

    def test_ice_general_selector_also_includes_players(self):
        with ZipFile(SOURCE) as source:
            item = parse_json_with_comments(source.read('Swords_B/items/ice_sword.json'))['minecraft:item']
        cmds = item['events']['on_use']['sequence'][0]['run_command']['command']
        general, = [c for c in cmds if 'type=!enderman' in c]
        player, = [c for c in cmds if 'type=player,rm=3' in c]
        selector = general.split(']')[0]
        self.assertIn('rm=2,r=12', selector)
        self.assertNotIn('type=!player', selector)
        self.assertNotIn('family=!player', selector)
        self.assertIn('rm=3,r=12', player)
        self.assertIn('rm=3` не является общим минимальным расстоянием для игрока', BRIEF.read_text(encoding='utf-8'))

    def test_dropped_item_sensor_paths_and_independent_timers(self):
        with ZipFile(SOURCE) as source:
            item = parse_json_with_comments(source.read('Swords_B/entities/item.json'))['minecraft:entity']
        sensors = item['components']['minecraft:environment_sensor']
        by_event = {entry['on_environment']['event']: entry['on_environment']['filters'] for entry in sensors}
        self.assertEqual(set(by_event), {'fading_fire_sword','fire_sword_event_2','stop_fire_sword','sponge_sword_event','stop_sponge_sword','delete_fire_blocks','fountain_of_wishes_1','fountain_of_wishes_2','fountain_of_wishes_3'})
        rain = by_event['fading_fire_sword']['all_of']
        self.assertIn({'test':'in_water','operator':'!='}, rain)
        self.assertIn({'test':'in_water_or_rain'}, rain)
        self.assertIn({'test':'in_water'}, by_event['fire_sword_event_2']['all_of'])
        self.assertIn({'test':'in_water_or_rain'}, by_event['sponge_sword_event']['all_of'])
        self.assertEqual(item['component_groups']['fire_sword']['minecraft:timer']['time'], [5,6])
        self.assertEqual(item['component_groups']['sponge_sword']['minecraft:timer']['time'], [0,1])
        self.assertEqual(by_event['delete_fire_blocks'], {'test':'has_tag','value':'fire_immune'})
        self.assertEqual(item['events']['delete_fire_blocks']['run_command']['command'], ['fill ~2 ~2 ~2 ~-2 ~-2 ~-2 air 0 replace fire'])
        self.assertTrue(all('kill @s' in x['run_command']['command'] for x in item['events']['wish_1']['randomize']))

    def test_spectral_end_transition_decision(self):
        text = BRIEF.read_text(encoding='utf-8')
        self.assertIn('при переходе в биом с тегом `the_end` убрать кристалл без взрыва и без 2%-попытки', text)
        self.assertIn('автоматически вернуть кристалл, если меч всё ещё удерживается', text)
        self.assertIn('ранее взорванный кристалл автоматически не возвращать', text)
        self.assertIn('если снять меч до выхода, ожидаемый автоматический возврат отменяется', text)
        self.assertIn('даже если снова взять меч внутри биома `the_end`', text)

    def test_jungle_vine_function_exact_order_and_conditions(self):
        path = 'Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction'
        with ZipFile(SOURCE) as source:
            lines = source.read(path).decode('utf-8').splitlines()
        blocks = [('log',i) for i in range(4)] + [('log2',i) for i in range(2)]
        blocks += [('stone',0),('cobblestone',0),('dirt',0)]
        blocks += [('leaves',i) for i in [0,1,2,3,11]] + [('leaves2',i) for i in range(2)]
        blocks += [('planks',i) for i in range(6)]
        blocks += [(b,0) for b in ('grass','netherrack','nether_brick','sand','glass','obsidian','end_stone','sandstone','gravel')]
        blocks += [('stone',i) for i in [1,3,5]] + [(b,0) for b in ('snow','packed_ice','ice')]
        directions = [('~1 ~1 ~',8),('~-1 ~1 ~',2),('~ ~1 ~1',1),('~ ~1 ~-1',4)]
        expected = [f'execute @p ~~~ detect {coords} {block} {data} fill ~ ~1 ~ ~ ~1 ~ vine {vine} replace air' for block,data in blocks for coords,vine in directions]
        self.assertEqual(len(expected), 148)
        self.assertEqual(lines, expected)
        text = BRIEF.read_text(encoding='utf-8')
        self.assertIn('лиана ставится только в воздушную клетку над игроком', text)
        self.assertIn('leaves 0–3/11', text)

    def test_secondary_mob_trigger_paths(self):
        with ZipFile(SOURCE) as source:
            def entity(name):
                return parse_json_with_comments(source.read('Swords_B/entities/' + name + '.json'))['minecraft:entity']
            witch, flame, centella, ghost, spider, enderman = [entity(x) for x in ('witch','living_flame','centella','ghost','spider','enderman')]
        witch_group = witch['component_groups']['grass_witch']
        self.assertEqual(witch_group['minecraft:on_death']['event'], 'grass_sword')
        self.assertEqual(witch_group['minecraft:environment_sensor']['triggers'][0], {'filters':{},'event':'grass_witch_skill'})
        self.assertEqual([x['weight'] for x in witch['events']['grass_sword']['randomize']], [80,20])
        hostile = flame['component_groups']['hostile_entity']
        self.assertEqual(hostile['minecraft:on_death']['event'], 'start_death_hostile')
        self.assertEqual(hostile['minecraft:timer']['time_down_event']['event'], 'minecraft:start_death')
        self.assertFalse(hostile['minecraft:damage_sensor']['triggers']['deals_damage'])
        self.assertEqual([x['weight'] for x in flame['events']['start_death_hostile']['sequence'][1]['randomize']], [85,15])
        triggers = centella['components']['minecraft:damage_sensor']['triggers']
        self.assertEqual([x['on_damage']['event'] for x in triggers], ['centella_death_by_player','centella_death'])
        self.assertEqual(ghost['components']['minecraft:damage_sensor']['triggers'][0]['on_damage']['event'], 'disturbed_ghost')
        self.assertEqual(spider['component_groups']['minecraft:spider_player_jockey']['minecraft:health']['value'], 20)
        self.assertIn('monster', spider['component_groups']['minecraft:spider_player_jockey']['minecraft:type_family']['family'])
        self.assertEqual(enderman['component_groups']['red_enderman']['minecraft:loot']['table'], 'loot_tables/entities/red_enderman.json')

    def test_companion_owner_safety_decision_and_original_filters(self):
        with ZipFile(SOURCE) as source:
            bee = parse_json_with_comments(source.read('Swords_B/entities/bee_entity.json'))['minecraft:entity']
            slime = parse_json_with_comments(source.read('Swords_B/entities/mountable_slime.json'))['minecraft:entity']
            player = parse_json_with_comments(source.read('Swords_B/entities/player.json'))['minecraft:entity']
        targeting = bee['components']['minecraft:behavior.nearest_attackable_target']['entity_types'][0]['filters']
        self.assertEqual(targeting['value'], 'monster')
        wolf = player['component_groups']['complete_wolf_transformation']['minecraft:type_family']['family']
        self.assertIn('monster', wolf)
        self.assertNotIn('player', wolf)
        self.assertNotIn('player', player['component_groups']['minecraft:ghost_sword']['minecraft:type_family']['family'])
        fall = slime['events']['fall_damage']['run_command']['command']
        self.assertIn('effect @e[r=1,family=!slime_sword,family=!undead] instant_damage 1 1 true', fall)
        text = BRIEF.read_text(encoding='utf-8')
        self.assertIn('каждую призванную пчелу привязать к владельцу', text)
        self.assertIn('слизень не выбирает владельца целью и не задевает его своими эффектами', text)
        self.assertIn('для других игроков отдельного нового правила не добавлять', text.lower())
        self.assertIn('пчёлы не атакуют и не наносят урон призванным помощникам любых игроков', text)
        self.assertIn('защитный слизень не атакует и не наносит урон призванным помощникам любых игроков', text)

    def test_slime_king_environment_damage_is_separate_from_fall(self):
        with ZipFile(SOURCE) as source:
            king = parse_json_with_comments(source.read('Swords_B/entities/slime_king.json'))['minecraft:entity']
        triggers = king['components']['minecraft:damage_sensor']['triggers']
        falling, = [x for x in triggers if x['on_damage']['event'] == 'fall_damage']
        self.assertFalse(falling['deals_damage'])
        self.assertEqual(falling['on_damage']['filters']['all_of'][0]['value'], 'fall')
        env = king['components']['minecraft:environment_sensor']['triggers']
        self.assertEqual(env, [{'filters':{},'event':'slime_effects'}])
        fall = king['events']['fall_damage']['run_command']['command']
        ambient = king['events']['slime_effects']['run_command']['command']
        self.assertTrue(all('instant_damage' in c for c in fall))
        self.assertIn('damage @p[r=1.8] 4 magic', ambient)
        self.assertIn('damage @e[r=1.5,family=!slime_king] 2 magic', ambient)
        text = BRIEF.read_text(encoding='utf-8')
        self.assertIn('Эти команды не являются частью события падения', text)

    def test_remaining_ten_hand_sensors_and_wolf_controllers(self):
        with ZipFile(SOURCE) as source:
            player = parse_json_with_comments(source.read('Swords_B/entities/player.json'))['minecraft:entity']
            controllers = parse_json_with_comments(source.read('Swords_B/animation_controllers/wolf_sword.json'))['animation_controllers']
        sensors = player['components']['minecraft:environment_sensor']
        expected = {
            'clock_sword':['minecraft:clock_sword','stop_clock_sword_event'],
            'sponge_sword':['minecraft:sponge_sword','stop_sponge_sword_event'],
            'wolf_sword':['minecraft:wolf_sword','stop_wolf_sword_event'],
            'coal_sword':[], 'bedrock_sword':[], 'wither_skeleton_sword':[], 'glass_sword':[],
            'silver_sword':[], 'wet_sponge_sword':[], 'cursed_pumpkin_sword':[],
        }
        for item, events in expected.items():
            with self.subTest(item=item):
                matches = [t['on_environment'] for t in sensors if 'effect:'+item in json.dumps(t)]
                self.assertEqual([x['event'] for x in matches], events)
                if matches:
                    for m in matches:
                        condition = m['filters']['all_of'][0]
                        self.assertEqual((condition['test'], condition['domain'], condition['value']), ('has_equipment','hand','effect:'+item))
                    self.assertEqual(matches[1]['filters']['all_of'][0]['operator'], '!=')
        prep = controllers['controller.animation.wolf_sword']['states']['wolf_transformation']['transitions'][0]['wolf_sword']
        full = controllers['controller.animation.start_wolf_sword']['states']['start_wolf_transformation']['transitions'][0]['wolf_sword_start']
        end = controllers['controller.animation.end_wolf_sword']['states']['end_wolf_transformation']['transitions'][0]['wolf_sword_end']
        self.assertIn('q.moon_phase == 0', prep)
        self.assertIn('q.time_of_day >= 0.77 && q.time_of_day <= 0.78', prep)
        self.assertIn('q.moon_phase == 0', full)
        self.assertIn('q.time_of_day <= 0.20 || q.time_of_day >= 0.80', full)
        self.assertIn("q.get_equipped_item_name('main_hand') == 'wolf_sword' ||", end)
        self.assertIn('конкурирующее условие', self.cards['effect:wolf_sword'])

    def test_direct_silver_wolf_and_pumpkin_chains(self):
        with ZipFile(SOURCE) as source:
            wolf = parse_json_with_comments(source.read('Swords_B/entities/alpha_wolf.json'))['minecraft:entity']
            triggers = wolf['components']['minecraft:damage_sensor']['triggers']
            self.assertEqual([t['on_damage']['event'] for t in triggers], ['minecraft:wolf_sword','add_effects','clear_effects'])
            self.assertIn({'test': 'has_damage', 'value': 'fatal'}, triggers[0]['on_damage']['filters']['all_of'])
            self.assertEqual(wolf['events']['add_effects']['run_command']['command'], ['effect @s resistance 20 2 true','effect @s regeneration 20 2 true'])
            self.assertEqual(wolf['events']['clear_effects']['run_command']['command'], ['effect @s resistance 0','effect @s regeneration 0'])
            self.assertEqual([b['weight'] for b in wolf['events']['minecraft:wolf_sword']['sequence'][0]['randomize']], [90,10])
            self.assertEqual(wolf['components']['minecraft:experience_reward']['on_death'], 'query.last_hit_by_player ? Math.Random(1,3) : 30')
            script = source.read('Swords_B/scripts/javascript.js').decode('utf-8-sig')
            self.assertIn(".includes('pumpkin') && !f.brokenBlockPermutation.type.id.includes('stem')", script)
            self.assertIn('Math.floor(Math.random() * 1000 + 1) <= 5', script)
            self.assertLess(script.index("f.player.addTag('pumpkin_sword')"), script.index('loot spawn'))
            loot = parse_json_with_comments(source.read('Swords_B/loot_tables/pumpkin_sword.json'))['pools'][0]
            self.assertEqual(loot['rolls'], 1)
            self.assertEqual(loot['entries'], [{'type':'item','name':'effect:cursed_pumpkin_sword','weight':1}])
        branches = self.items['effect:cursed_pumpkin_sword']['events']['weapon']['sequence'][1]['randomize']
        self.assertEqual([b['weight'] for b in branches], [80,20])
        self.assertEqual(branches[0]['shoot']['projectile'], 'entity:pumpkin_projectile')

    def test_direct_bedrock_all_digger_rows(self):
        digger = self.items['effect:bedrock_sword']['components']['minecraft:digger']
        rows = re.findall(r'^\| (\d+) \| `(.*?)` \| `(.*?)` \|$', self.cards['effect:bedrock_sword'], re.M)
        self.assertEqual(len(rows), 68)
        reconstructed = []
        for index, block, rest in rows:
            fields = json.loads(rest)
            reconstructed.append({'block':json.loads(block), **fields})
            self.assertEqual(int(index), len(reconstructed))
        self.assertEqual(reconstructed, digger['destroy_speeds'])
        self.assertFalse(any(r['block'] == 'minecraft:bedrock' for r in reconstructed))
        self.assertEqual(reconstructed[1]['speed'], 50)
        self.assertEqual(reconstructed[2]['speed'], 100)
        self.assertIn('не должен ломать сам бедрок в выживании', self.cards['effect:bedrock_sword'])

    def test_direct_tnt_and_fire_projectile_chains(self):
        with ZipFile(SOURCE) as source:
            def entity(name):
                return parse_json_with_comments(source.read(f'Swords_B/entities/{name}.json'))['minecraft:entity']
            tnt = entity('entity_tnt')
            self.assertEqual(tnt['description']['identifier'], 'entity:tnt')
            self.assertEqual(tnt['components']['minecraft:timer']['time'], [.1, .1])
            self.assertEqual(tnt['components']['minecraft:projectile']['on_hit']['impact_damage']['damage'], 1)
            self.assertEqual(tnt['component_groups']['mini_explosion']['minecraft:explode']['power'], 1)
            self.assertFalse(tnt['component_groups']['mini_explosion']['minecraft:explode']['causes_fire'])
            self.assertIn('одно только срабатывание 90%-ветви не гарантирует попадание и взрыв', self.cards['effect:tnt_sword'])
            fire = entity('fire')
            self.assertEqual(fire['components']['minecraft:projectile']['power'], 1)
            self.assertEqual(fire['component_groups']['fire_sword']['minecraft:projectile']['power'], 10)
            flame = entity('living_flame')
            hit = flame['component_groups']['living_flame_projectile']['minecraft:projectile']['on_hit']
            self.assertEqual(hit['definition_event']['event_trigger']['event'], 'minecraft:stop_projectile')
            steps = flame['events']['minecraft:stop_projectile']['sequence']
            self.assertEqual(steps[0]['remove']['component_groups'], ['hostile_entity','living_flame_projectile'])
            self.assertEqual(steps[1]['add']['component_groups'], ['passive_entity'])
            self.assertIn('добавляет пассивную форму живого пламени', self.cards['effect:fire_sword'])

    def test_acquisition_damage_triggers_and_explicit_loot_links(self):
        with ZipFile(SOURCE) as source:
            def entity(name):
                return parse_json_with_comments(source.read(f'Swords_B/entities/{name}.json'))['minecraft:entity']
            ghost = entity('ghost')
            trigger = ghost['components']['minecraft:damage_sensor']['triggers'][0]
            self.assertEqual(trigger['on_damage']['event'], 'disturbed_ghost')
            self.assertEqual(trigger['on_damage']['filters'], {'test':'is_family','subject':'other','value':'player'})
            self.assertFalse(trigger['deals_damage'])
            self.assertEqual([b['weight'] for b in ghost['events']['disturbed_ghost']['randomize']], [987, 10, 3])
            self.assertIn('смерть призрака для попытки не требуется', self.cards['effect:ghost_sword'])
            wither = entity('wither')
            trigger = wither['components']['minecraft:damage_sensor']['triggers'][1]['on_damage']
            self.assertEqual(trigger['event'], 'wither_sword')
            self.assertIn({'test':'has_damage','value':'fatal'}, trigger['filters']['all_of'])
            self.assertIn({'test':'has_equipment','subject':'other','domain':'hand','value':'effect:nether_star_sword'}, trigger['filters']['all_of'])
            enderman = entity('enderman')
            self.assertEqual(enderman['component_groups']['red_enderman']['minecraft:loot']['table'], 'loot_tables/entities/red_enderman.json')
            slime_king = entity('slime_king')
            self.assertNotIn('minecraft:loot', slime_king['components'])
            self.assertTrue(all('minecraft:loot' not in g for g in slime_king['component_groups'].values()))
            self.assertEqual(entity('blaze')['components']['minecraft:loot']['table'], 'loot_tables/entities/blaze.json')

    def test_crystal_reward_is_spawn_condition_and_damage_event(self):
        with ZipFile(SOURCE) as source:
            crystal = parse_json_with_comments(source.read('Swords_B/entities/ender_crystal.json'))['minecraft:entity']
        event = crystal['events']['minecraft:entity_spawned']['sequence'][1]
        self.assertEqual(event['filters'], {'test': 'has_biome_tag', 'value': 'nether'})
        self.assertEqual(event['add']['component_groups'], ['spectral_sword_drop'])
        self.assertEqual(crystal['component_groups']['spectral_sword_drop']['minecraft:on_hurt']['event'], 'spectral_crystal_explode')
        self.assertEqual([x['weight'] for x in crystal['events']['spectral_crystal_explode']['sequence'][0]['randomize']], [98, 2])
        self.assertEqual(crystal['events']['minecraft:crystal_explode'], {'add': {'component_groups': ['crystal_exploding']}})
        self.assertIn('при появлении кристалла', self.cards['effect:spectral_sword'])
        self.assertIn('при его повреждении выполняется 2%-попытка', self.cards['effect:spectral_sword'])
        self.assertIn('сам по себе 2%-попытку не запускает', self.cards['effect:spectral_sword'])
        projectile = None
        with ZipFile(SOURCE) as source:
            projectile = parse_json_with_comments(source.read('Swords_B/entities/ender_crystal_projectile.json'))['minecraft:entity']
        blast = projectile['component_groups']['crystal_exploding']['minecraft:explode']
        crystal_blast = crystal['component_groups']['crystal_exploding']['minecraft:explode']
        self.assertEqual((blast['power'], blast['causes_fire']), (6, True))
        self.assertEqual((crystal_blast['power'], crystal_blast['causes_fire']), (6, False))
        self.assertIn('при попадании запускает взрыв power 6 с огнём', self.cards['effect:spectral_sword'])
        self.assertIn('power 6 без огня', self.cards['effect:spectral_sword'])

    def test_fourteen_original_recipes_and_documented_exceptions(self):
        # Рецепты — данные архива, а не подтверждение регистрации в игре.
        shaped = {
            'bedrock_stick': (['#', '#'], {'#':'minecraft:bedrock'}, 'effect:bedrock_stick'),
            'bedrock_sword': (['B', 'B', '#'], {'B':'minecraft:bedrock', '#':'effect:bedrock_stick'}, 'effect:bedrock_sword'),
            'cactus_sword': (['F', 'F', 'E'], {'F':'minecraft:cactus', 'E':'minecraft:stick'}, 'effect:cactus_sword'),
            'clock_sword': (['X##', '#C#', 'I#X'], {'#':'minecraft:gold_block', 'C':'minecraft:clock', 'I':'minecraft:gold_ingot'}, 'effect:clock_sword'),
            'coal_sword': (['2', '2', '1'], {'2':'minecraft:coal_block', '1':'minecraft:stick'}, 'effect:coal_sword'),
            'fire_sword': (['F', 'F', '#'], {'F':'minecraft:fire', '#':'minecraft:blaze_rod'}, 'effect:fire_sword'),
            'glowstone_sword': (['2', '2', '1'], {'2':'minecraft:glowstone', '1':'minecraft:blaze_rod'}, 'effect:glowstone_sword'),
            'quartz_diamond_block': (['###', '###', '###'], {'#':'effect:quartz_diamond'}, 'effect99:quartz_diamond_block'),
            'quartz_diamond_stick': (['#', '#'], {'#':'effect:quartz_diamond'}, 'effect:quartz_diamond_stick'),
            'quartz_diamond_sword': (['Q', 'Q', '#'], {'Q':'effect99:quartz_diamond_block', '#':'effect:quartz_diamond_stick'}, 'effect:quartz_sword'),
            'silver_sword': (['2', '2', '1'], {'2':'effect:silver_ingot', '1':'minecraft:stick'}, 'effect:silver_sword'),
        }
        furnace = {'silver_ingot': ('effect99:silver_ore','effect:silver_ingot'),
                   'wet_sponge_sword': ('effect:wet_sponge_sword','effect:sponge_sword')}
        with ZipFile(SOURCE) as source:
            names = {n.rsplit('/', 1)[-1][:-5] for n in source.namelist()
                     if n.startswith('Swords_B/recipes/') and n.endswith('.json')}
            self.assertEqual(names, set(shaped) | set(furnace) | {'nether_star_sword'})
            for name, (pattern, keys, result) in shaped.items():
                with self.subTest(recipe=name):
                    recipe = parse_json_with_comments(source.read('Swords_B/recipes/' + name + '.json'))['minecraft:recipe_shaped']
                    self.assertEqual(recipe['pattern'], pattern)
                    self.assertEqual({k:v['item'] for k,v in recipe['key'].items()}, keys)
                    self.assertEqual(recipe['result']['item'], result)
                    self.assertEqual(recipe['tags'], ['crafting_table'])
            for name, (input_id, output_id) in furnace.items():
                with self.subTest(recipe=name):
                    recipe = parse_json_with_comments(source.read('Swords_B/recipes/' + name + '.json'))['minecraft:recipe_furnace']
                    self.assertEqual((recipe['input'], recipe['output']), (input_id, output_id))
                    self.assertEqual(set(recipe['tags']), {'furnace', 'blast_furnace'})
            recipe = parse_json_with_comments(source.read('Swords_B/recipes/nether_star_sword.json'))['minecraft:recipe_shapeless']
            self.assertEqual({x['item'] for x in recipe['ingredients']}, {'minecraft:diamond_sword', 'minecraft:nether_star'})
            self.assertEqual(recipe['result'], {'item':'effect:nether_star_sword', 'count':1})
        technical = (ROOT / 'docs' / 'remake-technical-verification-ru.md').read_text(encoding='utf-8')
        self.assertIn('неопределённый символ `X`', technical)
        self.assertIn('.GG / GCG / IG.', technical)
        self.assertIn('F=minecraft:fire', technical)

    def test_known_duplicate_keys_are_not_silently_lost(self):
        # Порядок важен для Slime King; другие две пары одинаковы по значениям.
        found = {}
        with ZipFile(SOURCE) as source:
            for name in ('slime_king', 'living_flame', 'mountable_slime'):
                text = source.read('Swords_B/entities/' + name + '.json').decode('utf-8-sig')
                pattern = r'("(?:\\.|[^"\\])*")|(//[^\n]*|/\*.*?\*/)'
                text = re.sub(pattern, lambda m: m.group(1) or '', text, flags=re.S)
                text = re.sub(r',(?=\s*[}\]])', '', text)
                duplicates = []
                def hook(pairs):
                    result = {}
                    for key, value in pairs:
                        if key in result:
                            duplicates.append((key, result[key], value))
                        result[key] = value
                    return result
                json.loads(text, object_pairs_hook=hook)
                found[name] = duplicates
        self.assertEqual(found['slime_king'], [('minecraft:movement.jump', {'jump_delay':[.5,1.5]}, {'jump_delay':[.16,.4]})])
        self.assertEqual(found['living_flame'], [('minecraft:fire_immune', True, True)])
        self.assertEqual(found['mountable_slime'], [('despawn', {'minecraft:despawn':{}}, {'minecraft:despawn':{}})])

    def test_twelve_entity_event_trees_match_archive(self):
        # Проверка полей и ветвлений, не механизмов вызова и не исполнения.
        text = BRIEF.read_text(encoding='utf-8').split('## Боссы, мобы и связанные сущности', 1)[1]
        cards = re.findall(r'^### [^\n]+\n(.*?)(?=\n### |\n## |\Z)', text, re.M | re.S)
        checked, total = 0, 0

        with ZipFile(SOURCE) as source:
            for card in cards:
                path = re.search(r'- Путь `(Swords_B/entities/[^`]+)`', card)
                if not path or '##### События' not in card:
                    continue
                entity = parse_json_with_comments(source.read(path.group(1)))['minecraft:entity']
                section = card.split('##### События', 1)[1]
                parts = re.split(r'^\*\*`([^`]+)`\*\* \(строки [^\n]*\):\s*$', section, flags=re.M)
                entries = dict(zip(parts[1::2], parts[2::2]))
                self.assertEqual(set(entries), set(entity.get('events', {})))
                for name, event in entity.get('events', {}).items():
                    with self.subTest(entity=entity['description']['identifier'], event=name):
                        content = entries[name]
                        self.assertEqual(recorded_event_tree(content), flatten_event_for_audit(event))
                        total += 1
                checked += 1
        self.assertEqual((checked, total), (12, 66))

    def test_creeper_diagnostic_extraction_is_not_source_repair(self):
        with ZipFile(SOURCE) as source:
            raw = source.read('Swords_B/entities/creeper.json')
        with self.assertRaises(json.JSONDecodeError):
            parse_json_with_comments(raw)
        # Diagnostic only: remove the final excess brace in memory, never modify the archive.
        pos = raw.rfind(b'}')
        entity = parse_json_with_comments(raw[:pos] + raw[pos + 1:])['minecraft:entity']
        groups = entity['component_groups']
        mini = groups['minecraft:minicreeper']
        self.assertEqual(mini['minecraft:scale']['value'], .3)
        self.assertEqual(mini['minecraft:timer']['time'], [10, 10])
        self.assertEqual(mini['minecraft:target_nearby_sensor']['inside_range'], 2.5)
        self.assertEqual(groups['minecraft:minicreeper_exploding']['minecraft:explode']['power'], 1)
        charged = groups['minecraft:forced_charged_exploding']
        self.assertEqual(charged['minecraft:timer']['time'], [1.4, 1.4])
        self.assertEqual(charged['minecraft:explode']['fuse_length'], 1.5)
        self.assertEqual([x['weight'] for x in entity['events']['creeper_sword']['randomize']], [95, 5])

    def test_twelve_entity_component_and_group_transcriptions_match_archive(self):
        # Last-value JSON parsing cannot verify overwritten duplicate keys (e.g. Slime King).
        text = BRIEF.read_text(encoding='utf-8').split('## Боссы, мобы и связанные сущности', 1)[1]
        checked = set()
        with ZipFile(SOURCE) as source:
            cards = re.findall(r'^### ([^\n]+)\n(.*?)(?=\n### |\n## |\Z)', text, re.M | re.S)
            for title, card in cards:
                path = re.search(r'- Путь `(Swords_B/entities/[^`]+)`', card)
                if not path or '##### Постоянные компоненты' not in card:
                    continue
                with self.subTest(entity=title):
                    entity = parse_json_with_comments(source.read(path.group(1)))['minecraft:entity']
                    checked.add(entity['description']['identifier'])
                    for heading, field, following in [
                        ('##### Постоянные компоненты', 'components', '##### Группы компонентов'),
                        ('##### Группы компонентов', 'component_groups', '##### События'),
                    ]:
                        section = card.split(heading, 1)[1].split(following, 1)[0]
                        rows = re.findall(r'^- `([^`]+)` \(строки [^\n]*?\): `([^\n]*)`$', section, re.M)
                        recorded = {key:json.loads(value) for key, value in rows}
                        self.assertEqual(recorded, entity.get(field, {}))
        self.assertEqual(len(checked), 12)
        self.assertIn('entity:slime_king', checked)
        self.assertIn('minecraft:enderman', checked)
        self.assertIn('entity:ghost', checked)

    def test_bone_skeleton_source_checks_fatal_player_biome_and_brightness(self):
        with ZipFile(SOURCE) as source:
            skeleton = parse_json_with_comments(source.read('Swords_B/entities/skeleton.json'))['minecraft:entity']
        trigger = skeleton['components']['minecraft:damage_sensor']['triggers'][0]['on_damage']
        self.assertEqual(trigger['event'], 'bone_sword')
        self.assertEqual(trigger['filters']['all_of'], [
            {'test':'is_family', 'subject':'other', 'value':'player'}, {'test':'has_damage', 'value':'fatal'}])
        branch = skeleton['events']['bone_sword']['sequence'][0]
        self.assertEqual(branch['filters']['all_of'], [
            {'test':'has_biome_tag', 'value':'desert'},
            {'test':'is_brightness', 'operator':'<', 'value':0.49}])
        self.assertEqual([b['weight'] for b in branch['randomize']], [993, 7])

    def test_other_custom_spawn_rule_data_and_decision_boundaries(self):
        # В исходнике дополнительные ограничения ночи не указаны; решения ремейка отдельны.
        with ZipFile(SOURCE) as source:
            def rule(name):
                return parse_json_with_comments(source.read('Swords_B/spawn_rules/' + name + '.json'))['minecraft:spawn_rules']
            wolf = rule('alpha_wolf')['conditions'][0]
            boss = rule('slime_king')['conditions'][0]
            flame = rule('living_flame')['conditions'][0]
        self.assertIn('minecraft:spawns_on_surface', wolf)
        self.assertEqual(wolf['minecraft:spawns_on_block_filter'], 'minecraft:grass')
        self.assertEqual(wolf['minecraft:brightness_filter'], {'min':0, 'max':7, 'adjust_for_weather':True})
        self.assertEqual(wolf['minecraft:weight']['default'], 10)
        self.assertEqual([x['value'] for x in wolf['minecraft:biome_filter']['all_of']], ['taiga', 'mega'])
        self.assertEqual(wolf['minecraft:biome_filter']['all_of'][1]['operator'], '!=')
        self.assertIn('minecraft:spawns_on_surface', boss)
        self.assertEqual(boss['minecraft:biome_filter']['value'], 'swamp')
        self.assertEqual(boss['minecraft:weight']['default'], 10)
        self.assertIn('minecraft:spawns_underground', flame)
        self.assertEqual(flame['minecraft:biome_filter']['value'], 'nether')
        self.assertEqual(flame['minecraft:weight']['default'], 20)
        self.assertEqual(flame['minecraft:herd'], {'min_size':1, 'max_size':4})
        for branch in (wolf, boss, flame):
            self.assertEqual(branch['minecraft:difficulty_filter'], {'min':'easy', 'max':'hard'})
            self.assertFalse(any('time' in key for key in branch))

    def test_ghost_spawn_branches_have_light_but_no_time_filter(self):
        with ZipFile(SOURCE) as source:
            rule = parse_json_with_comments(source.read('Swords_B/spawn_rules/ghost.json'))['minecraft:spawn_rules']
        self.assertEqual(rule['description']['identifier'], 'entity:ghost')
        cave, surface = rule['conditions']
        self.assertIn('minecraft:spawns_underground', cave)
        self.assertIn('minecraft:spawns_on_surface', surface)
        self.assertEqual(cave['minecraft:spawns_on_block_filter'], 'minecraft:stone')
        self.assertEqual(surface['minecraft:spawns_on_block_filter'], 'minecraft:grass')
        for branch in (cave, surface):
            self.assertEqual(branch['minecraft:brightness_filter'], {'min':0, 'max':7, 'adjust_for_weather':True})
            self.assertFalse(any('time' in key for key in branch))
        self.assertEqual(surface['minecraft:density_limit'], {'surface':3})

    def test_quartz_ore_three_recorded_loot_branches(self):
        with ZipFile(SOURCE) as source:
            data = parse_json_with_comments(source.read('Swords_B/loot_tables/blocks/quartz_diamond_ore.json'))
        pools = data['pools']
        self.assertEqual(len(pools), 1)
        self.assertEqual(pools[0]['rolls'], 1)
        entries = pools[0]['entries']
        self.assertEqual([entry['name'] for entry in entries], ['effect:quartz_diamond'] * 3)
        self.assertEqual([entry['weight'] for entry in entries], [89, 10, 1])
        ranges = [entry['functions'][0]['count'] for entry in entries]
        self.assertEqual(ranges, [{'min':1,'max':1}, {'min':1,'max':2}, {'min':2,'max':4}])
        # Conditional model only: assumes uniform inclusive integer count selection.
        distribution = {}
        for entry, bounds in zip(entries, ranges):
            for count in range(bounds['min'], bounds['max'] + 1):
                distribution[count] = distribution.get(count, Fraction()) + Fraction(entry['weight'], 100 * (bounds['max'] - bounds['min'] + 1))
        self.assertEqual(distribution, {1:Fraction(94,100), 2:Fraction(4,75), 3:Fraction(1,300), 4:Fraction(1,300)})
        self.assertEqual(sum(count * probability for count, probability in distribution.items()), Fraction(107,100))

    def test_quartz_ore_and_block_event_use_nearest_player(self):
        with ZipFile(SOURCE) as source:
            for name in ('quartz_diamond_ore', 'quartz_diamond_block'):
                with self.subTest(block=name):
                    block = parse_json_with_comments(source.read('Swords_B/blocks/' + name + '.json'))['minecraft:block']
                    event = block['events'][name]
                    commands = event['run_command']['command']
                    self.assertIn('effect @p[r=6] instant_damage 1 0 true', commands)
                    condition = block['components']['minecraft:on_player_destroyed']['condition']
                    for tool in ('iron_pickaxe', 'diamond_pickaxe', 'netherite_pickaxe', 'bedrock_sword'):
                        self.assertIn(tool, condition)
                    self.assertEqual(event['spawn_loot']['table'], 'loot_tables/blocks/' + name + '.json')

    def test_six_mob_loot_pools_chances_and_sources(self):
        # Проверяет записи, а не то, что каждая таблица подключена и исполняется.
        expected = {
            'shulker': ('effect:shulker_sword', .045, 'killed_by_player'),
            'elder_guardian': ('effect:sponge_sword', .065, 'killed_by_player'),
            'wither_skeleton': ('effect:wither_skeleton_sword', .025, 'killed_by_player'),
            'slime_king': ('effect:slime_sword', .04, 'killed_by_player'),
            'red_enderman': ('effect:ender_sword', .025, 'killed_by_player'),
            'blaze': ('effect:blaze_sword', .025, 'killed_by_entity'),
        }
        with ZipFile(SOURCE) as source:
            for mob, (item, chance, killer_type) in expected.items():
                with self.subTest(mob=mob):
                    data = parse_json_with_comments(source.read('Swords_B/loot_tables/entities/' + mob + '.json'))
                    pools = [p for p in data['pools'] if any(e.get('name') == item for e in p['entries'])]
                    self.assertEqual(len(pools), 1)
                    pool = pools[0]
                    self.assertEqual(pool['rolls'], 1)
                    conditions = {c['condition']: c for c in pool['conditions']}
                    self.assertIn(killer_type, conditions)
                    self.assertEqual(conditions['random_chance_with_looting']['chance'], chance)
                    self.assertEqual(conditions['random_chance_with_looting']['looting_multiplier'], .02)
                    if mob == 'blaze':
                        self.assertEqual(conditions[killer_type]['entity_type'], 'minecraft:snow_golem')

    def test_original_explicit_mob_event_weights(self):
        # GHAST action is retained as source evidence, not the user's revised condition.
        expected = {'wither': ('wither_sword', [87, 13]),
                    'skeleton': ('bone_sword', [993, 7]),
                    'ender_crystal': ('spectral_crystal_explode', [98, 2]),
                    'ghost': ('disturbed_ghost', [987, 10, 3]),
                    'ghast': ('spectral_ghast', [94, 6])}
        with ZipFile(SOURCE) as source:
            for mob, (event, weights) in expected.items():
                with self.subTest(mob=mob):
                    entity = parse_json_with_comments(source.read('Swords_B/entities/' + mob + '.json'))['minecraft:entity']
                    action = entity['events'][event]
                    if 'sequence' in action:
                        action = action['sequence'][0]
                    self.assertEqual([branch['weight'] for branch in action['randomize']], weights)

    def test_bee_on_attack_does_not_specify_player_victim(self):
        with ZipFile(SOURCE) as source:
            bee = parse_json_with_comments(source.read('Swords_B/entities/bee.json'))['minecraft:entity']
        on_attack = bee['component_groups']['angry_bee']['minecraft:behavior.melee_attack']['on_attack']
        self.assertEqual(on_attack, {'event': 'countdown_to_perish_event', 'target': 'self'})
        branches = bee['events']['countdown_to_perish_event']['sequence'][0]['randomize']
        self.assertEqual([branch['weight'] for branch in branches], [2, 98])
        self.assertEqual(branches[0]['filters'], {'test': 'is_family', 'subject': 'self', 'operator': '!=', 'value': 'bee_sword'})

    def test_ender_damage_triggers_have_overlapping_wet_condition(self):
        with ZipFile(SOURCE) as source:
            player = parse_json_with_comments(source.read('Swords_B/entities/player.json'))['minecraft:entity']
        group = player['component_groups']['minecraft:ender_sword']
        first, projectile, wet = group['minecraft:damage_sensor']['triggers']
        self.assertEqual(first['on_damage']['filters']['all_of'],
                         [{'test': 'has_damage', 'subject': 'self', 'operator': '!=', 'value': 'projectile'}])
        self.assertEqual(projectile['on_damage']['filters']['all_of'][0]['value'], 'projectile')
        self.assertFalse(projectile['deals_damage'])
        self.assertEqual(wet['on_damage']['filters']['all_of'], [{'test': 'in_water_or_rain'}])
        self.assertTrue(wet['deals_damage'])
        self.assertEqual([e['weight'] for e in player['events']['ender_sword_skill']['sequence'][1]['randomize']], [50, 50])

    def test_weapon_hooks_match_288(self):
        hooks = ('on_hurt_entity', 'on_not_hurt_entity', 'on_hit_block')
        phrases = {
            hooks: 'при попадании с уроном, ударе без урона и ударе по блоку',
            hooks[:1]: 'только при попадании по сущности с уроном',
            (): 'weapon-компонент пуст; явный weapon-event не указан',
        }
        for identifier, card in self.cards.items():
            with self.subTest(item=identifier):
                weapon = self.items[identifier]['components'].get('minecraft:weapon', {})
                present = tuple(name for name in hooks if name in weapon)
                self.assertIn(present, phrases)
                self.assertIn('**Вход weapon-события:** ' + phrases[present], card)


if __name__ == '__main__':
    unittest.main()
