#!/usr/bin/env python3
"""Small navigational table of literal item fields; archives remain authoritative."""
import json
import re
import zipfile
from pathlib import Path
import json5

ROOT = Path(__file__).resolve().parents[1]
VERSIONS = [
    ('1.6', 'SwordsAndMoreSwords.1.6.mcaddon', 'Sword_B'),
    ('2.8.8', 'swordsandmoreswords_2_8_8.mcaddon', 'Swords_B'),
    ('2.8.14', 'swordsandmoreswords-2-8-14.mcaddon', 'Swords_B'),
]

def slug(heading):
    return re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')

def read_items(filename, pack):
    items = {}
    with zipfile.ZipFile(ROOT / 'sources' / filename) as z:
        for name in z.namelist():
            if not (name.startswith(pack + '/items/') and name.endswith('.json')):
                continue
            item = json5.loads(z.read(name).decode('utf-8-sig'))['minecraft:item']
            ident = item['description']['identifier']
            if ident in items:
                raise ValueError('duplicate item identifier: '+ident)
            items[ident] = (name, item)
    return items

def literal(value):
    if value is None:
        return '—'
    return '`' + json.dumps(value, ensure_ascii=False, separators=(',', ':')) + '`'

def item_values(item):
    c = item.get('components', {})
    durability = c.get('minecraft:durability')
    cooldown = c.get('minecraft:cooldown')
    enchant = c.get('minecraft:enchantable')
    return [c.get('minecraft:damage'),
            durability.get('max_durability') if isinstance(durability, dict) else None,
            cooldown.get('duration') if isinstance(cooldown, dict) else None,
            c.get('minecraft:allow_off_hand'),
            enchant if enchant is not None else None]

def manual_links():
    coverage = (ROOT / 'docs/coverage-2.8.14.md').read_text(encoding='utf-8')
    return dict(re.findall(r'^\| `(effect:[^`]+)` \|[^\n]*\]\((manual-traces-2\.8\.14\.md#[^)]*)\)', coverage, re.M))

def legacy_manual_anchor(ident):
    special = {
        'coal_sword':'Coal Sword: 1.6 против 2.8.14',
        'cactus_sword':'Cactus Sword: 1.6 против 2.8.14',
        'emerald_sword':'Emerald Sword: 1.6 против 2.8.14',
        'sponge_sword':'Sponge Sword: 1.6 против 2.8.14',
        'ice_sword':'Ice Sword 1.6: подробная цепочка',
        'jungle_sword':'Jungle: сопоставление 1.6 и 2.8.14',
        'grass_sword':'Grass Sword: 1.6 и теги 2.x',
        'sea_sword':'Sea Sword: подробная цепочка 1.6 и группы 2.x',
        'fire_sword':'Fire, Magma и Spider 1.6: типы и мир',
        'magma_sword':'Fire, Magma и Spider 1.6: типы и мир',
        'spider_sword':'Fire, Magma и Spider 1.6: типы и мир',
        'lightning_sword':'Lightning Sword 1.6: подробная цепочка',
        'creeper_sword':'Creeper Sword и TNT Sword: 1.6',
        'tnt_sword':'Creeper Sword и TNT Sword: 1.6',
        'sword_of_time':'Sword of Time: 1.6',
        'blaze_sword':'Blaze и Bone: краткие различия и ошибки JSON 1.6',
        'bone_sword':'Blaze и Bone: краткие различия и ошибки JSON 1.6',
    }
    return slug(special.get(ident.split(':',1)[1], 'Остальные предметы 1.6: первичные прямые цепочки'))

def build():
    manual = manual_links()
    with zipfile.ZipFile(ROOT / 'sources/swordsandmoreswords-2-8-14.mcaddon') as z:
        ui = json5.loads(z.read('Swords_R/ui/how_to_play_screen.json').decode('utf-8-sig'))
    out = ['# Краткий указатель предметов', '',
           'Начните с нужной версии и ID, затем открывайте ручную цепочку и получение; полные исходные данные и ресурсы — по ссылкам. Таблица создана из item JSON, а не из игровых испытаний. Все 1.6 и 2.8.14 цепочки **частичные**; ссылки на 2.8.14 не являются ручным аудитом 2.8.8. Здесь нет всего поведения, вероятностей, рецептов, ремонта или косвенных связей.', '',
           '`—` = поле отсутствует в определении, не обязательно «ноль», «нельзя», «бесконечно» или движковое значение по умолчанию. Числа прочности и damage — буквально компоненты; cooldown — только duration в единицах исходного формата. `enchantable` показан целиком, не является гарантией работы на Bedrock 26.62.', '',
           '2.8.8 и 2.8.14 почти совпадают побайтово, однако Ice, добыча/торговля/генерация и другие файлы различаются; см. [отличия](manual-version-2.8.8.md) и [все изменённые пути](version-diff.md). Действительная версия определяется не именем архива.', '',
           '## Навигация по анализу', '',
           '- Статус и версии: [общий статус](analysis-status.md) · [покрытие 1.6](coverage-1.6.md) · [сравнение компонентов](item-version-matrix.md).',
           '- Предметы и использование: [ремонт и флаги](item-repair-index.md) · [значки и offsets](item-visual-index.md) · [weapon-хуки](weapon-event-index.md) · [on-use и cooldown](on-use-index.md) · [особенности рецептов](manual-acquisition-issues.md) · [модель loot-пулов](loot-selection-model.md).',
           '- Межигровые пересечения: [family и type игроков/сущностей](manual-family-cross-effects-2.8.md) — условные совпадения, не результаты игры.',
           '- Сущности: [сенсоры игрока](player-sensor-index.md) · группы [1.6](entity-groups-1.6.md) / [2.x](entity-groups-2.x.md) · event-поля [1.6](entity-event-fields-1.6.md) / [2.x](entity-event-fields-2.x.md) · spawn/shoot [1.6](spawn-shoot-index-1.6.md) / [2.x](spawn-shoot-index-2.x.md) · [projectile](projectile-component-index.md) · бой и уязвимости [1.6](entity-combat-index-1.6.md) / [2.x](entity-combat-index-2.x.md) · таймеры и сенсоры [1.6](entity-trigger-index-1.6.md) / [2.x](entity-trigger-index-2.x.md).',
           '- Эффекты и счётчики: команды/компоненты [1.6](effect-index-1.6.md) / [2.x](effect-index-2.x.md) · scoreboard [1.6](scoreboard-index-1.6.md) / [2.x](scoreboard-index-2.x.md).',
           '- Команды и геометрия: отдельные командные строки [1.6](command-risk-index-1.6.md) / [2.8.8](command-risk-index-2.8.8.md) / [2.8.14](command-risk-index-2.8.14.md) · командные summon/event [1.6](command-entity-calls-1.6.md) / [2.x](command-entity-calls-2.x.md) · все функции [1.6](function-ledger-1.6.md) / [2.x](function-ledger-2.x.md) · изменения мира [1.6](world-command-index-1.6.md) / [2.8.8](world-command-index-2.8.8.md) / [2.8.14](world-command-index-2.8.14.md) · [Ice: геометрия и селекторы](manual-ice-geometry-2.8.md).',
           '- Авторская справка: [прямые тексты UI](ui-localization-index.md) · [сверка чисел UI](ui-stat-comparison.md) · [все строки en_US](localization-source-index.md); это заявления автора, не доказательство исполнения.',
           '- Ресурсы: [визуальные и звуковые цепочки](manual-client-2.8.md) · [полные объекты анимаций](client-animation-index.md) · [модели и геометрия](client-geometry-index.md) · [контроллеры и частицы](client-effects-ledger.md); полные реестры и остальные тематические документы — в [общем статусе](analysis-status.md).', '']
    for version, filename, pack in VERSIONS:
        items = read_items(filename, pack)
        out += [f'## {version}', '', f'Архив `{filename}`, определений: {len(items)}. Названия файлов и ID в этой таблице — исходные, без исправления регистра.', '',
                '| ID | damage | max durability | cooldown duration | offhand | enchantable | Открыть |',
                '|---|---:|---:|---:|---|---|---|']
        for ident, (path, item) in sorted(items.items()):
            values = ' | '.join(literal(v) for v in item_values(item))
            target = slug(ident)
            links = [f'[исходные данные](items-{version}.md#{target})',
                     f'[получение](acquisition-index-{version}.md#{target})']
            if version == '1.6':
                links.insert(0, f'[цепочка](chain-index-1.6.md#{target})')
                links.insert(0, f'[ручной разбор](manual-traces-1.6.md#{legacy_manual_anchor(ident)})')
            else:
                if ident not in manual:
                    raise ValueError('missing manual trace: '+ident)
                label = 'ручная цепочка' if version == '2.8.14' else 'цепочка 2.8.14'
                links.insert(0, f'[{label}]({manual[ident]})')
                shared = {'effect:wet_sponge_sword':'sponge_sword', 'effect:bedrock_stick':'blocks_and_items', 'effect:quartz_diamond':'blocks_and_items', 'effect:quartz_diamond_stick':'blocks_and_items', 'effect:silver_ingot':'blocks_and_items'}
                section = shared.get(ident, ident.split(':', 1)[1]) + '_section@how_to_play_common.main_sections'
                if section in ui:
                    links.append(f'[текст справки](ui-localization-index.md#{slug(section)})')
            silver_wolf = {'effect:silver_ingot':'Руда, слиток и меч','effect:silver_sword':'Руда, слиток и меч','effect:wolf_sword':'Wolf Sword и конкурирующие контроллеры'}
            if ident in silver_wolf:
                links.insert(0, f'[цепочка Silver/Wolf](manual-silver-wolf-path.md#{slug(silver_wolf[ident])})')
            if ident in {'effect:ghost_sword','effect:nether_star_sword','effect:ultra_instinct_sword'}:
                heading = ident.split(':',1)[1].replace('_', ' ').title()
                links.insert(0, f'[подробная цепочка](manual-ghost-nether-ultra.md#{slug(heading)})')
            specialized = {
                'effect:bee_sword':'manual-bee-sword.md',
                'effect:creeper_sword':'manual-creeper-sword.md',
                'effect:grass_sword':'manual-grass-sword.md',
                'effect:ice_sword': 'manual-ice-1.6.md' if version == '1.6' else 'manual-ice-geometry-2.8.md',
                'effect:jungle_sword':'manual-jungle-vines.md',
                'effect:lightning_sword':'manual-lightning-1.6.md',
                'effect:sea_sword':'manual-sea-sword.md',
                'effect:wolf_sword':'manual-wolf-conditions-2.8.md',
                'effect:cursed_pumpkin_sword':'manual-pumpkin-script-2.8.md',
                'effect:silver_ingot':'manual-ore-and-loot-paths-2.8.md',
                'effect:silver_sword':'manual-ore-and-loot-paths-2.8.md',
            }
            if ident in specialized:
                links.insert(0, f'[детальный разбор]({specialized[ident]})')
            spectral_time = {'effect:spectral_sword':'Spectral Sword','effect:sword_of_time':'Sword of Time 1.6','effect:time_sword':'Clock Sword и Time Sword 2.x','effect:clock_sword':'Clock Sword и Time Sword 2.x'}
            if ident in spectral_time:
                links.insert(0, f'[подробное сравнение](manual-spectral-time-comparison.md#{slug(spectral_time[ident])})')
            fire_spider_sponge = {'effect:fire_sword':'Fire Sword', 'effect:spider_sword':'Spider Sword', 'effect:sponge_sword':'Sponge Sword и Wet Sponge Sword', 'effect:wet_sponge_sword':'Sponge Sword и Wet Sponge Sword'}
            if ident in fire_spider_sponge:
                links.insert(0, f'[подробно 1.6/2.x](manual-fire-spider-sponge.md#{slug(fire_spider_sponge[ident])})')
            progression = {'effect:quartz_sword':'Quartz Sword: одинаковый ID, разные рецепты и побочные эффекты', 'effect:quartz_diamond':'Граф крафта 2.x: Quartz Diamond', 'effect:quartz_diamond_stick':'Граф крафта 2.x: Quartz Diamond', 'effect:bedrock_sword':'Bedrock Stick и Bedrock Sword', 'effect:bedrock_stick':'Bedrock Stick и Bedrock Sword'}
            if ident in progression:
                links.insert(0, f'[цепочка материалов](manual-quartz-bedrock-progression.md#{slug(progression[ident])})')
            if ident in {'effect:ender_sword','effect:wither_sword','effect:tnt_sword','effect:slime_sword'}:
                heading = ident.split(':',1)[1].replace('_', ' ').title()
                links.insert(0, f'[подробно 1.6/2.x](manual-ender-wither-tnt-slime.md#{slug(heading)})')
            if ident in {'effect:blaze_sword','effect:bone_sword','effect:shulker_sword'}:
                heading = ident.split(':',1)[1].replace('_', ' ').title()
                links.insert(0, f'[подробно 1.6/2.x](manual-companion-projectile-swords.md#{slug(heading)})')
            if ident in {'effect:obsidian_sword','effect:magma_sword','effect:glowstone_sword','effect:wither_skeleton_sword'}:
                heading = ident.split(':',1)[1].replace('_', ' ').title()
                if ident == 'effect:wither_skeleton_sword': heading = 'Wither Skeleton Sword — только 2.x среди точных ID'
                links.insert(0, f'[подробно 1.6/2.x](manual-heat-light-swords.md#{slug(heading)})')
            if ident in {'effect:coal_sword','effect:cactus_sword','effect:emerald_sword','effect:lapis_sword','effect:glass_sword'}:
                heading = ident.split(':',1)[1].replace('_', ' ').title()
                if ident == 'effect:glass_sword': heading = 'Glass Sword — только 2.x среди точных ID'
                links.insert(0, f'[подробно 1.6/2.x](manual-basic-swords.md#{slug(heading)})')
            out.append(f'| `{ident}` | {values} | ' + ' · '.join(links) + ' |')
        out += ['', 'Путь к item в архиве указан в ссылке «исходные данные»; ссылки на получение описывают декларации и не гарантируют доступность или вероятность.', '']
    (ROOT / 'docs/quick-reference.md').write_text('\n'.join(out)+'\n', encoding='utf-8')
    print('Quick reference:', ', '.join(f'{version} {len(read_items(filename,pack))}' for version,filename,pack in VERSIONS))

if __name__ == '__main__':
    build()
