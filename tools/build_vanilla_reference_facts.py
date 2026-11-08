#!/usr/bin/env python3
"""Extract narrowly selected official-sample and add-on facts; no engine execution.

Downloads are deliberately not automatic. See docs/manual-vanilla-override-review.md.
"""
import argparse
import hashlib
import json
from pathlib import Path
from zipfile import ZipFile

import json5

ROOT = Path(__file__).resolve().parents[1]
VANILLA_NAMES = ('arrow', 'bee', 'blaze', 'cat', 'creeper', 'enderman', 'ender_crystal', 'fireball', 'ghast', 'item', 'lightning_bolt', 'parrot', 'player', 'shulker_bullet', 'skeleton', 'small_fireball', 'snowball', 'spider', 'tnt', 'witch', 'wither', 'wither_skull', 'wither_skull_dangerous', 'wolf')
REFERENCE = {
    '1.19.40.2': ('16f15af95678d72bcd4b2af468b71f60140a6c06', 'd99671c6fa61d38dda2b87286e44ddc352ef6578253cbb1d8cfc032ff826c08d'),
    '1.20.30.1': ('c7755281ab8c69d7e61d35856ad5a05813e2b853', 'a667860cf7e9c495a29f05e4f9cfc81c79ca3fce1269aa7348de65f3e9811301'),
}
# Paths are exact keys, not dot-notation: component names themselves contain dots.
PATHS = {
    'player': [
        ('components', 'minecraft:player.exhaustion'), ('components', 'minecraft:player.saturation'),
        ('components', 'minecraft:exhaustion_values'), ('components', 'minecraft:block_climber'),
        ('components', 'minecraft:scaffolding_climber'), ('components', 'minecraft:type_family'),
    ],
    'cat': [
        ('components', 'minecraft:despawn'), ('components', 'minecraft:leashable'),
        ('component_groups', 'minecraft:cat_tame', 'minecraft:type_family'),
        ('component_groups', 'minecraft:cat_tame', 'minecraft:leashable'),
        ('component_groups', 'minecraft:cat_gift_for_owner', 'minecraft:behavior.drop_item_for'),
    ],
    'parrot': [
        ('components', 'minecraft:despawn'), ('components', 'minecraft:behavior.tempt'),
        ('components', 'minecraft:game_event_movement_tracking'),
        ('component_groups', 'minecraft:parrot_riding_player', 'minecraft:entity_sensor'),
        ('component_groups', 'minecraft:parrot_not_riding_player', 'minecraft:entity_sensor'),
    ],
    'wolf': [
        ('components', 'minecraft:despawn'), ('components', 'minecraft:leashable'),
        ('component_groups', 'minecraft:wolf_tame', 'minecraft:type_family'),
        ('component_groups', 'minecraft:wolf_tame', 'minecraft:leashable'),
        ('component_groups', 'minecraft:wolf_tame', 'minecraft:behavior.breed'),
    ],
    'skeleton': [
        ('components', 'minecraft:despawn'), ('components', 'minecraft:environment_sensor'),
        ('components', 'minecraft:behavior.pickup_items'),
        ('component_groups', 'in_powder_snow', 'minecraft:timer'),
        ('component_groups', 'become_stray', 'minecraft:transformation'),
        ('component_groups', 'minecraft:melee_attack', 'minecraft:attack'),
    ],
    'blaze': [
        ('components', 'minecraft:despawn'), ('components', 'minecraft:hurt_on_condition'),
        ('components', 'minecraft:behavior.melee_attack'), ('components', 'minecraft:behavior.ranged_attack'),
        ('component_groups', 'mode_switcher', 'minecraft:target_nearby_sensor'),
    ],
}

def digest(data):
    return hashlib.sha256(data).hexdigest()

def extract(data, name):
    entity = json5.loads(data.decode('utf-8-sig'), allow_duplicate_keys=False)['minecraft:entity']
    if entity['description']['identifier'] != 'minecraft:' + name:
        raise ValueError('unexpected identifier: ' + name)
    result = {}
    for parts in PATHS[name]:
        node = entity
        present = True
        for part in parts:
            if not isinstance(node, dict) or part not in node:
                present = False
                break
            node = node[part]
        result['/'.join(parts)] = {'present': True, 'value': node} if present else {'present': False}
    return {'sha256': digest(data), 'selected': result}

def top_level_diff(ref, addon):
    result = {}
    for section in ('components', 'component_groups', 'events'):
        old, new = ref.get(section, {}), addon.get(section, {})
        if not isinstance(old, dict) or not isinstance(new, dict):
            raise ValueError('expected entity section object: ' + section)
        old_keys, new_keys = set(old), set(new)
        result[section] = {
            'only_reference': sorted(old_keys - new_keys),
            'only_addon': sorted(new_keys - old_keys),
            'different_both': sorted(k for k in old_keys & new_keys if old[k] != new[k]),
        }
    return result

def parse_entity(data, name):
    entity = json5.loads(data.decode('utf-8-sig'), allow_duplicate_keys=False)['minecraft:entity']
    if entity['description']['identifier'] != 'minecraft:' + name:
        raise ValueError('unexpected identifier: ' + name)
    return entity

def build(ref_paths):
    result = {'method': 'literal JSON5 extraction; present tracks key existence; not Bedrock execution', 'references': {}, 'addons': {}}
    refs_full = {}
    for version, (commit, expected_hash) in REFERENCE.items():
        file = ref_paths[version]
        actual_hash = digest(file.read_bytes())
        if actual_hash != expected_hash:
            raise ValueError(f'{version}: ZIP SHA-256 mismatch: {actual_hash}')
        with ZipFile(file) as z:
            entities = {name: extract(z.read(f'bedrock-samples-{version}/behavior_pack/entities/{name}.json'), name) for name in PATHS}
            raw_refs = {name: z.read(f'bedrock-samples-{version}/behavior_pack/entities/{name}.json') for name in VANILLA_NAMES if name not in ('creeper', 'item')}
            refs_full[version] = {name: parse_entity(data, name) for name, data in raw_refs.items()}
        result['references'][version] = {'commit': commit, 'zip_sha256': actual_hash, 'file_sha256': {name: digest(data) for name, data in raw_refs.items()}, 'entities': entities}
    result['comparisons'] = {}
    for version, filename, pack in [('1.6', 'SwordsAndMoreSwords.1.6.mcaddon', 'Sword_B'), ('2.8.8', 'swordsandmoreswords_2_8_8.mcaddon', 'Swords_B'), ('2.8.14', 'swordsandmoreswords-2-8-14.mcaddon', 'Swords_B')]:
        with ZipFile(ROOT / 'sources' / filename) as z:
            names = ('player',) if version == '1.6' else tuple(PATHS)
            result['addons'][version] = {name: extract(z.read(f'{pack}/entities/{name}.json'), name) for name in names}
            if version != '1.6':
                raw_addons = {name: z.read(f'{pack}/entities/{name}.json') for name in VANILLA_NAMES if name not in ('creeper', 'item')}
                addon_full = {name: parse_entity(data, name) for name, data in raw_addons.items()}
                result['addons'][version + '_file_sha256'] = {name: digest(data) for name, data in raw_addons.items()}
                result['comparisons'][version] = {ref_version: {name: top_level_diff(refs_full[ref_version][name], addon_full[name]) for name in addon_full} for ref_version in REFERENCE}
    return result

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--reference-119', type=Path, required=True)
    parser.add_argument('--reference-120', type=Path, required=True)
    parser.add_argument('--output', type=Path, default=ROOT / 'data/vanilla-reference-facts.json')
    args = parser.parse_args()
    data = build({'1.19.40.2': args.reference_119, '1.20.30.1': args.reference_120})
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True) + '\n', encoding='utf-8')
    print('Selected reference facts:', args.output)

if __name__ == '__main__':
    main()
