#!/usr/bin/env python3
"""One-off 2.8.8 source audit explicitly requested by user; never opens 2.8.14."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'sources/swordsandmoreswords_2_8_8.mcaddon'
EXPECTED_SHA256 = 'ab8cbb75c930948f386bf0119bb0a4ee79c084db888c2e9b05deac61b799bb7f'
OUT = ROOT / 'data/remake-audits/fire-water-original-2.8.8.json'


def parse_unique(raw):
    def unique(pairs):
        dup = [key for key, count in Counter(k for k, _ in pairs).items() if count > 1]
        if dup:
            raise ValueError(f'duplicate JSON keys: {dup}')
        return dict(pairs)
    return json.loads(raw.decode('utf-8-sig'), object_pairs_hook=unique)


def main():
    digest = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    if digest != EXPECTED_SHA256:
        raise ValueError('Unexpected archive SHA-256: refusing to audit another source')
    with ZipFile(SOURCE) as archive:
        paths = ['Swords_B/entities/player.json', 'Swords_B/entities/item.json', 'Swords_B/items/fire_sword.json']
        player = parse_unique(archive.read(paths[0]))['minecraft:entity']
        item_entity = parse_unique(archive.read(paths[1]))['minecraft:entity']
        item = parse_unique(archive.read(paths[2]))['minecraft:item']
        sensors = player['components']['minecraft:environment_sensor']
        fire_sensors = [s['on_environment'] for s in sensors if s['on_environment'].get('event') in ('minecraft:fire_sword', 'stop_fire_sword_event')]
        assert len(fire_sensors) == 2
        group = player['component_groups']['minecraft:fire_sword']
        events = {key: player['events'][key] for key in ('minecraft:fire_sword', 'stop_fire_sword_event', 'fire_sword_sound')}
        dropped_sensors = [s['on_environment'] for s in item_entity['components']['minecraft:environment_sensor'] if s['on_environment'].get('event') in ('fading_fire_sword', 'fire_sword_event_2', 'stop_fire_sword')]
        text_paths = [n for n in archive.namelist() if n.startswith(('Swords_B/', 'Swords_R/')) and n.endswith(('.json', '.mcfunction', '.js'))]
        fire_refs, inventory_commands = [], []
        inv = re.compile(r'\breplaceitem\b|\bclear\s+@|\bsetslot\b|\bsetitem\b|slot\.weapon\.mainhand', re.I)
        for name in text_paths:
            for number, line in enumerate(archive.read(name).decode('utf-8-sig', 'replace').splitlines(), 1):
                if re.search(r'fire_sword|fire sword', line, re.I):
                    fire_refs.append({'path': name, 'line': number, 'text': line.strip()})
                if inv.search(line):
                    inventory_commands.append({'path': name, 'line': number, 'text': line.strip()})
        item_fragment = json.dumps(item, ensure_ascii=False)
        held_fragment = json.dumps({'sensors': fire_sensors, 'group': group, 'events': events}, ensure_ascii=False)
        assert 'in_water' not in item_fragment and 'in_water' not in held_fragment
        assert 'replaceitem' not in held_fragment.lower() and 'clear @' not in held_fragment.lower()
        assert 'in_water' in json.dumps(dropped_sensors)
        assert 'structure load glass_sword' in json.dumps(item_entity['events']['fire_sword_event_2'])
        assert [(x['path'], x['line']) for x in inventory_commands] == [
            ('Swords_B/entities/player.json', 1595), ('Swords_B/entities/player.json', 1928), ('Swords_B/entities/player.json', 1932)]
        report = {
            'source': str(SOURCE.relative_to(ROOT)), 'source_sha256': digest,
            'scope': 'All JSON, mcfunction and JS files under Swords_B and Swords_R were searched literally; specific player, item entity and item JSON parsed with duplicate-key rejection. Static analysis, not runtime; external packs excluded.',
            'scanned_text_files': len(text_paths),
            'direct_source_files': paths,
            'player_fire_sensors': fire_sensors,
            'player_fire_group': group,
            'player_fire_events': events,
            'fire_item_events': item['events'],
            'dropped_item_fire_sensors': dropped_sensors,
            'dropped_item_water_event': item_entity['events']['fire_sword_event_2'],
            'fire_text_references': fire_refs,
            'inventory_command_literal_matches': inventory_commands,
            'script_module': 'Swords_B/scripts/javascript.js: playerBreakBlock pumpkin loot only; no water or inventory handling',
        }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Scanned {len(text_paths)} text files, {len(fire_refs)} Fire references, {len(inventory_commands)} literal inventory commands. Saved {OUT.relative_to(ROOT)}')

if __name__ == '__main__':
    main()
