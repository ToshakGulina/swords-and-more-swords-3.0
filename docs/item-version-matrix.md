# Компоненты предметов: 1.6 ↔ 2.8.x

Автоматическое сопоставление только **точных item ID** в behavior pack. Приведены буквальные значения JSON, не игровой урон/скорость/длительность. «Не задано» означает отсутствие поля, не `null`, не `false` и не движковое значение по умолчанию; списки «только в версии» относятся к определениям предметов, а не ко всем упоминаниям в архиве. Равенство определений предмета не доказывает равенства player/entity, ресурсов или поведения; имена событий не раскрывают их цепочки. Разные ключи glint/foil и другие схемы не считаются автоматически эквивалентными.

Общих ID 1.6 и 2.8.14: 25; только в 1.6: 1; только в 2.8.14: 17. Между 2.8.8 и 2.8.14 общих ID: 42, из них побайтово изменённых item JSON: 1: `effect:ice_sword`.

- Только 1.6: `effect:sword_of_time`.
- Только 2.8.14: `effect:bedrock_stick`, `effect:bedrock_sword`, `effect:bee_sword`, `effect:clock_sword`, `effect:cursed_pumpkin_sword`, `effect:ghost_sword`, `effect:glass_sword`, `effect:nether_star_sword`, `effect:quartz_diamond`, `effect:quartz_diamond_stick`, `effect:silver_ingot`, `effect:silver_sword`, `effect:time_sword`, `effect:ultra_instinct_sword`, `effect:wet_sponge_sword`, `effect:wither_skeleton_sword`, `effect:wolf_sword`.
- `effect:sword_of_time` и `effect:time_sword` здесь не объединяются автоматически.

## Обзор числовых полей

| Точный ID | damage 1.6 → 2.8.14 | max_durability 1.6 → 2.8.14 | allow_off_hand 1.6 → 2.8.14 |
|---|---|---|---|
| `effect:blaze_sword` | `8` → `6` | `2300` → `2300` | `true` → `false` |
| `effect:bone_sword` | `7` → `5` | `820` → `820` | `true` → `false` |
| `effect:cactus_sword` | `6` → `6` | `125` → `125` | `true` → `false` |
| `effect:coal_sword` | `6` → `4` | `121` → `121` | `true` → `false` |
| `effect:creeper_sword` | `8` → `6` | `1500` → `1500` | `true` → `false` |
| `effect:emerald_sword` | `7` → `7` | `2300` → `2300` | `true` → `false` |
| `effect:ender_sword` | `9` → `9` | `1256` → `1256` | `true` → `false` |
| `effect:fire_sword` | `12` → `6` | `2000` → `2000` | `true` → `false` |
| `effect:glowstone_sword` | `6` → `4` | `128` → `128` | `true` → `true` |
| `effect:grass_sword` | `8` → `8` | `250` → `250` | `true` → `false` |
| `effect:ice_sword` | `11` → `8.5` | `500` → `500` | `true` → `false` |
| `effect:jungle_sword` | `4` → `4` | `128` → `128` | `true` → `false` |
| `effect:lapis_sword` | `6` → `5` | `528` → `528` | `true` → `false` |
| `effect:lightning_sword` | `8` → `8` | `2000` → `2012` | `true` → `false` |
| `effect:magma_sword` | `7` → `7.2` | `1000` → `1316` | `true` → `false` |
| `effect:obsidian_sword` | `12` → `8` | `3000` → `3000` | `true` → `false` |
| `effect:quartz_sword` | `600` → `600` | `1` → `1` | `true` → `false` |
| `effect:sea_sword` | `7` → `7` | `1000` → `1356` | `true` → `false` |
| `effect:shulker_sword` | `7` → `6` | `1000` → `2609` | `true` → `false` |
| `effect:slime_sword` | `6` → `6` | `675` → `675` | `true` → `false` |
| `effect:spectral_sword` | `9` → `9` | `3256` → `3256` | `true` → `false` |
| `effect:spider_sword` | `6` → `5` | `628` → `628` | `true` → `false` |
| `effect:sponge_sword` | `6` → `5` | `128` → `128` | `true` → `false` |
| `effect:tnt_sword` | `7` → `4` | `1` → `64` | `true` → `false` |
| `effect:wither_sword` | `10` → `10` | `1256` → `3856` | `true` → `false` |

## Все изменённые или отсутствующие компоненты общих ID

Для каждого ключа выводится **полное значение компонента** с каждой стороны. Поля, одинаковые структурно, опущены; события показаны только именами. Полный исходный текст, рецепты и связи — в [карточках 1.6](items-1.6.md), [2.8.14](items-2.8.14.md), [ручном разборе 1.6](manual-traces-1.6.md) и [2.8.14](manual-traces-2.8.14.md).

### `effect:blaze_sword`

- Источники: `Sword_B/items/blaze_sword.json` · `Swords_B/items/blaze_sword.json`.
- `format_version`: `"1.20.20"` → `"1.16.100"`.
- Description: `{"identifier":"effect:blaze_sword","menu_category":{"category":"equipment"}}` → `{"category":"equipment","identifier":"effect:blaze_sword"}`.
- Event keys: не задано → `["on_use","weapon"]`.

| Компонент | 1.6 | 2.8.14 |
|---|---|---|
| `minecraft:allow_off_hand` | `true` | `false` |
| `minecraft:cooldown` | не задано | `{"category":"blaze_sword","duration":20}` |
| `minecraft:creative_category` | не задано | `{"parent":"itemGroup.name.sword"}` |
| `minecraft:damage` | `8` | `6` |
| `minecraft:display_name` | не задано | `{}` |
| `minecraft:foil` | не задано | `false` |
| `minecraft:glint` | `false` | не задано |
| `minecraft:on_use` | не задано | `{"on_use":{"event":"on_use"}}` |
| `minecraft:weapon` | не задано | `{"on_hit_block":{"event":"weapon"},"on_hurt_entity":{"event":"weapon"},"on_not_hurt_entity":{"event":"weapon"}}` |
| `tag:minecraft:is_sword` | `{}` | не задано |

### `effect:bone_sword`

- Источники: `Sword_B/items/bone_sword.json` · `Swords_B/items/bone_sword.json`.
- `format_version`: `"1.20.20"` → `"1.16.100"`.
- Description: `{"identifier":"effect:bone_sword","menu_category":{"category":"equipment"}}` → `{"category":"equipment","identifier":"effect:bone_sword"}`.
- Event keys: не задано → `["weapon"]`.

| Компонент | 1.6 | 2.8.14 |
|---|---|---|
| `minecraft:allow_off_hand` | `true` | `false` |
| `minecraft:creative_category` | не задано | `{"parent":"itemGroup.name.sword"}` |
| `minecraft:damage` | `7` | `5` |
| `minecraft:display_name` | не задано | `{}` |
| `minecraft:foil` | не задано | `false` |
| `minecraft:glint` | `false` | не задано |
| `minecraft:repairable` | `{"repair_items":[{"items":["effect:bone_sword"],"repair_amount":820}]}` | `{"repair_items":[{"items":["effect:bone_sword"],"repair_amount":820},{"items":["minecraft:bone"],"repair_amount":70},{"items":["minecraft:bone_block"],"repair_amount":300},{"items":["minecraft:bone_meal"],"repair_amount":18}]}` |
| `minecraft:weapon` | не задано | `{"on_hit_block":{"event":"weapon"},"on_hurt_entity":{"event":"weapon"},"on_not_hurt_entity":{"event":"weapon"}}` |
| `tag:minecraft:is_sword` | `{}` | не задано |

### `effect:cactus_sword`

- Источники: `Sword_B/items/cactus_sword.json` · `Swords_B/items/cactus_sword.json`.
- `format_version`: `"1.20.20"` → `"1.16.100"`.
- Description: `{"identifier":"effect:cactus_sword","menu_category":{"category":"equipment"}}` → `{"category":"equipment","identifier":"effect:cactus_sword"}`.
- Event keys: не задано → `["weapon"]`.

| Компонент | 1.6 | 2.8.14 |
|---|---|---|
| `minecraft:allow_off_hand` | `true` | `false` |
| `minecraft:creative_category` | не задано | `{"parent":"itemGroup.name.sword"}` |
| `minecraft:display_name` | не задано | `{}` |
| `minecraft:foil` | не задано | `false` |
| `minecraft:glint` | `false` | не задано |
| `minecraft:render_offsets` | не задано | `{"main_hand":{"first_person":{"position":[0.67,0,-1.24]},"third_person":{"position":[0.36,1.5,-0.66]}}}` |
| `minecraft:weapon` | не задано | `{"on_hurt_entity":{"event":"weapon"}}` |
| `tag:minecraft:is_sword` | `{}` | не задано |

### `effect:coal_sword`

- Источники: `Sword_B/items/coal_sword.json` · `Swords_B/items/coal_sword.json`.
- `format_version`: `"1.20.20"` → `"1.16.100"`.
- Description: `{"identifier":"effect:coal_sword","menu_category":{"category":"equipment"}}` → `{"category":"equipment","identifier":"effect:coal_sword"}`.
- Event keys: не задано → `["weapon"]`.

| Компонент | 1.6 | 2.8.14 |
|---|---|---|
| `minecraft:allow_off_hand` | `true` | `false` |
| `minecraft:creative_category` | не задано | `{"parent":"itemGroup.name.sword"}` |
| `minecraft:damage` | `6` | `4` |
| `minecraft:display_name` | не задано | `{}` |
| `minecraft:foil` | не задано | `false` |
| `minecraft:fuel` | не задано | `{"duration":360.0}` |
| `minecraft:glint` | `false` | не задано |
| `minecraft:repairable` | `{"repair_items":[{"items":["effect:coal_sword"],"repair_amount":121}]}` | `{"repair_items":[{"items":["effect:coal_sword"],"repair_amount":121},{"items":["minecraft:coal"],"repair_amount":58},{"items":["minecraft:stick"],"repair_amount":2}]}` |
| `minecraft:weapon` | не задано | `{"on_hurt_entity":{"event":"weapon"}}` |
| `tag:minecraft:is_sword` | `{}` | не задано |

### `effect:creeper_sword`

- Источники: `Sword_B/items/creeper_sword.json` · `Swords_B/items/creeper_sword.json`.
- `format_version`: `"1.20.20"` → `"1.16.100"`.
- Description: `{"identifier":"effect:creeper_sword","menu_category":{"category":"equipment"}}` → `{"category":"equipment","identifier":"effect:creeper_sword"}`.
- Event keys: не задано → `["on_use","weapon"]`.

| Компонент | 1.6 | 2.8.14 |
|---|---|---|
| `minecraft:allow_off_hand` | `true` | `false` |
| `minecraft:cooldown` | не задано | `{"category":"creeper_sword","duration":3}` |
| `minecraft:creative_category` | не задано | `{"parent":"itemGroup.name.sword"}` |
| `minecraft:damage` | `8` | `6` |
| `minecraft:display_name` | не задано | `{}` |
| `minecraft:foil` | не задано | `false` |
| `minecraft:glint` | `false` | не задано |
| `minecraft:on_use` | не задано | `{"on_use":{"event":"on_use"}}` |
| `minecraft:repairable` | `{"repair_items":[{"items":["effect:creeper_sword"],"repair_amount":1500}]}` | `{"repair_items":[{"items":["effect:creeper_sword"],"repair_amount":1500},{"items":["minecraft:gunpowder"],"repair_amount":256}]}` |
| `minecraft:weapon` | не задано | `{"on_hit_block":{"event":"weapon"},"on_hurt_entity":{"event":"weapon"},"on_not_hurt_entity":{"event":"weapon"}}` |
| `tag:minecraft:is_sword` | `{}` | не задано |

### `effect:emerald_sword`

- Источники: `Sword_B/items/emerald_sword.json` · `Swords_B/items/emerald_sword.json`.
- `format_version`: `"1.20.20"` → `"1.16.100"`.
- Description: `{"identifier":"effect:emerald_sword","menu_category":{"category":"equipment"}}` → `{"category":"equipment","identifier":"effect:emerald_sword"}`.
- Event keys: не задано → `["weapon"]`.

| Компонент | 1.6 | 2.8.14 |
|---|---|---|
| `minecraft:allow_off_hand` | `true` | `false` |
| `minecraft:creative_category` | не задано | `{"parent":"itemGroup.name.sword"}` |
| `minecraft:display_name` | не задано | `{}` |
| `minecraft:foil` | не задано | `false` |
| `minecraft:glint` | `false` | не задано |
| `minecraft:weapon` | не задано | `{"on_hit_block":{"event":"weapon"},"on_hurt_entity":{"event":"weapon"},"on_not_hurt_entity":{"event":"weapon"}}` |
| `tag:minecraft:is_sword` | `{}` | не задано |

### `effect:ender_sword`

- Источники: `Sword_B/items/ender_sword.json` · `Swords_B/items/ender_sword.json`.
- `format_version`: `"1.20.20"` → `"1.16.100"`.
- Description: `{"identifier":"effect:ender_sword","menu_category":{"category":"equipment"}}` → `{"category":"equipment","identifier":"effect:ender_sword"}`.
- Event keys: не задано → `["on_use","weapon"]`.

| Компонент | 1.6 | 2.8.14 |
|---|---|---|
| `minecraft:allow_off_hand` | `true` | `false` |
| `minecraft:cooldown` | не задано | `{"category":"ender_sword","duration":2}` |
| `minecraft:creative_category` | не задано | `{"parent":"itemGroup.name.sword"}` |
| `minecraft:display_name` | не задано | `{}` |
| `minecraft:foil` | не задано | `true` |
| `minecraft:glint` | `true` | не задано |
| `minecraft:on_use` | не задано | `{"on_use":{"event":"on_use"}}` |
| `minecraft:render_offsets` | не задано | `{"main_hand":{"first_person":{"position":[1,0.4,-3],"scale":[0.04,0.04,0.04]},"third_person":{"position":[0.5,1.6,-0.8],"scale":[0.038,0.038,0.038]}}}` |
| `minecraft:repairable` | `{"repair_items":[{"items":["effect:ender_sword"],"repair_amount":1256}]}` | `{"repair_items":[{"items":["effect:ender_sword"],"repair_amount":1256},{"items":["minecraft:ender_pearl"],"repair_amount":28},{"items":["minecraft:ender_eye"],"repair_amount":32}]}` |
| `minecraft:weapon` | не задано | `{"on_hurt_entity":{"event":"weapon"}}` |
| `tag:minecraft:is_sword` | `{}` | не задано |

### `effect:fire_sword`

- Источники: `Sword_B/items/fire_sword.json` · `Swords_B/items/fire_sword.json`.
- `format_version`: `"1.20.20"` → `"1.16.100"`.
- Description: `{"identifier":"effect:fire_sword","menu_category":{"category":"equipment"}}` → `{"category":"equipment","identifier":"effect:fire_sword"}`.
- Event keys: не задано → `["on_use","weapon"]`.

| Компонент | 1.6 | 2.8.14 |
|---|---|---|
| `minecraft:allow_off_hand` | `true` | `false` |
| `minecraft:cooldown` | не задано | `{"category":"fire_sword","duration":25}` |
| `minecraft:creative_category` | не задано | `{"parent":"itemGroup.name.sword"}` |
| `minecraft:damage` | `12` | `6` |
| `minecraft:display_name` | не задано | `{}` |
| `minecraft:foil` | не задано | `true` |
| `minecraft:glint` | `false` | не задано |
| `minecraft:on_use` | не задано | `{"on_use":{"event":"on_use"}}` |
| `minecraft:repairable` | `{"repair_items":[{"items":["effect:fire_sword"],"repair_amount":2000}]}` | `{"repair_items":[{"items":["effect:fire_sword"],"repair_amount":2000},{"items":["minecraft:fire"],"repair_amount":1000}]}` |
| `minecraft:weapon` | не задано | `{"on_hit_block":{"event":"weapon"},"on_hurt_entity":{"event":"weapon"},"on_not_hurt_entity":{"event":"weapon"}}` |
| `tag:minecraft:is_sword` | `{}` | не задано |

### `effect:glowstone_sword`

- Источники: `Sword_B/items/glowstone_sword.json` · `Swords_B/items/glowstone_sword.json`.
- `format_version`: `"1.20.20"` → `"1.16.100"`.
- Description: `{"identifier":"effect:glowstone_sword","menu_category":{"category":"equipment"}}` → `{"category":"equipment","identifier":"effect:glowstone_sword"}`.
- Event keys: не задано → `["weapon"]`.

| Компонент | 1.6 | 2.8.14 |
|---|---|---|
| `minecraft:creative_category` | не задано | `{"parent":"itemGroup.name.sword"}` |
| `minecraft:damage` | `6` | `4` |
| `minecraft:display_name` | не задано | `{}` |
| `minecraft:foil` | не задано | `true` |
| `minecraft:glint` | `true` | не задано |
| `minecraft:repairable` | `{"repair_items":[{"items":["effect:glowstone_sword"],"repair_amount":128}]}` | `{"repair_items":[{"items":["effect:glowstone_sword"],"repair_amount":128},{"items":["minecraft:glowstone"],"repair_amount":64},{"items":["minecraft:glowstone_dust"],"repair_amount":16}]}` |
| `minecraft:weapon` | не задано | `{"on_hurt_entity":{"event":"weapon"}}` |
| `tag:minecraft:is_sword` | `{}` | не задано |

### `effect:grass_sword`

- Источники: `Sword_B/items/grass_sword.json` · `Swords_B/items/grass_sword.json`.
- `format_version`: `"1.20.20"` → `"1.16.100"`.
- Description: `{"identifier":"effect:grass_sword","menu_category":{"category":"equipment"}}` → `{"category":"equipment","identifier":"effect:grass_sword"}`.
- Event keys: не задано → `["weapon"]`.

| Компонент | 1.6 | 2.8.14 |
|---|---|---|
| `minecraft:allow_off_hand` | `true` | `false` |
| `minecraft:creative_category` | не задано | `{"parent":"itemGroup.name.sword"}` |
| `minecraft:display_name` | не задано | `{}` |
| `minecraft:foil` | не задано | `false` |
| `minecraft:glint` | `false` | не задано |
| `minecraft:render_offsets` | не задано | `{"main_hand":{"first_person":{"position":[0.8,0.15,-1.74]},"third_person":{"position":[0.69,2.5,-0.96]}}}` |
| `minecraft:weapon` | не задано | `{"on_hurt_entity":{"event":"weapon"}}` |
| `tag:minecraft:is_sword` | `{}` | не задано |

### `effect:ice_sword`

- Источники: `Sword_B/items/ice_sword.json` · `Swords_B/items/ice_sword.json`.
- `format_version`: `"1.20.20"` → `"1.16.100"`.
- Description: `{"identifier":"effect:ice_sword","menu_category":{"category":"equipment"}}` → `{"category":"equipment","identifier":"effect:ice_sword"}`.
- Event keys: не задано → `["on_use","weapon"]`.

| Компонент | 1.6 | 2.8.14 |
|---|---|---|
| `minecraft:allow_off_hand` | `true` | `false` |
| `minecraft:cooldown` | не задано | `{"category":"ice_sword","duration":5}` |
| `minecraft:creative_category` | не задано | `{"parent":"itemGroup.name.sword"}` |
| `minecraft:damage` | `11` | `8.5` |
| `minecraft:display_name` | не задано | `{}` |
| `minecraft:foil` | не задано | `true` |
| `minecraft:on_use` | не задано | `{"on_use":{"event":"on_use"}}` |
| `minecraft:repairable` | `{"repair_items":[{"items":["effect:ice_sword"],"repair_amount":500}]}` | `{"repair_items":[{"items":["effect:ice_sword"],"repair_amount":500},{"items":["minecraft:ice"],"repair_amount":55}]}` |
| `minecraft:weapon` | не задано | `{"on_hit_block":{"event":"weapon"},"on_hurt_entity":{"event":"weapon"},"on_not_hurt_entity":{"event":"weapon"}}` |
| `tag:minecraft:is_sword` | `{}` | не задано |

### `effect:jungle_sword`

- Источники: `Sword_B/items/jungle_sword.json` · `Swords_B/items/jungle_sword.json`.
- `format_version`: `"1.20.20"` → `"1.16.100"`.
- Description: `{"identifier":"effect:jungle_sword","menu_category":{"category":"equipment"}}` → `{"category":"equipment","identifier":"effect:jungle_sword"}`.
- Event keys: не задано → `["weapon"]`.

| Компонент | 1.6 | 2.8.14 |
|---|---|---|
| `minecraft:allow_off_hand` | `true` | `false` |
| `minecraft:block_placer` | не задано | `{"block":"effect99:sapling3","use_on":["dirt","grass"]}` |
| `minecraft:creative_category` | не задано | `{"parent":"itemGroup.name.sword"}` |
| `minecraft:display_name` | не задано | `{}` |
| `minecraft:foil` | не задано | `false` |
| `minecraft:glint` | `false` | не задано |
| `minecraft:weapon` | не задано | `{"on_hurt_entity":{"event":"weapon"}}` |
| `tag:minecraft:is_sword` | `{}` | не задано |

### `effect:lapis_sword`

- Источники: `Sword_B/items/lapis_sword.json` · `Swords_B/items/lapis_sword.json`.
- `format_version`: `"1.20.20"` → `"1.16.100"`.
- Description: `{"identifier":"effect:lapis_sword","menu_category":{"category":"equipment"}}` → `{"category":"equipment","identifier":"effect:lapis_sword"}`.
- Event keys: не задано → `["weapon"]`.

| Компонент | 1.6 | 2.8.14 |
|---|---|---|
| `minecraft:allow_off_hand` | `true` | `false` |
| `minecraft:creative_category` | не задано | `{"parent":"itemGroup.name.sword"}` |
| `minecraft:damage` | `6` | `5` |
| `minecraft:display_name` | не задано | `{}` |
| `minecraft:foil` | не задано | `false` |
| `minecraft:glint` | `false` | не задано |
| `minecraft:repairable` | `{"repair_items":[{"items":["effect:lapis_sword"],"repair_amount":528}]}` | `{"repair_items":[{"items":["effect:lapis_sword"],"repair_amount":528},{"items":["minecraft:lapis_lazuli"],"repair_amount":48}]}` |
| `minecraft:weapon` | не задано | `{"on_hurt_entity":{"event":"weapon"}}` |
| `tag:minecraft:is_sword` | `{}` | не задано |

### `effect:lightning_sword`

- Источники: `Sword_B/items/lightning_sword.json` · `Swords_B/items/lightning_sword.json`.
- `format_version`: `"1.20.20"` → `"1.16.100"`.
- Description: `{"identifier":"effect:lightning_sword","menu_category":{"category":"equipment"}}` → `{"category":"equipment","identifier":"effect:lightning_sword"}`.
- Event keys: не задано → `["on_use","weapon"]`.

| Компонент | 1.6 | 2.8.14 |
|---|---|---|
| `minecraft:allow_off_hand` | `true` | `false` |
| `minecraft:cooldown` | не задано | `{"category":"lightning_sword","duration":12}` |
| `minecraft:creative_category` | не задано | `{"parent":"itemGroup.name.sword"}` |
| `minecraft:display_name` | не задано | `{}` |
| `minecraft:durability` | `{"max_durability":2000}` | `{"max_durability":2012}` |
| `minecraft:foil` | не задано | `true` |
| `minecraft:glint` | `true` | не задано |
| `minecraft:on_use` | не задано | `{"on_use":{"event":"on_use"}}` |
| `minecraft:render_offsets` | не задано | `{"main_hand":{"first_person":{"position":[1,0.4,-3],"scale":[0.04,0.04,0.04]},"third_person":{"position":[0.7,2.2,-1],"scale":[0.05,0.05,0.05]}}}` |
| `minecraft:repairable` | `{"repair_items":[{"items":["effect:lightning_sword"],"repair_amount":2000}]}` | `{"repair_items":[{"items":["effect:lightning_sword"],"repair_amount":2012}]}` |
| `minecraft:weapon` | не задано | `{"on_hit_block":{"event":"weapon"},"on_hurt_entity":{"event":"weapon"},"on_not_hurt_entity":{"event":"weapon"}}` |
| `tag:minecraft:is_sword` | `{}` | не задано |

### `effect:magma_sword`

- Источники: `Sword_B/items/magma_sword.json` · `Swords_B/items/magma_sword.json`.
- `format_version`: `"1.20.20"` → `"1.16.100"`.
- Description: `{"identifier":"effect:magma_sword","menu_category":{"category":"equipment"}}` → `{"category":"equipment","identifier":"effect:magma_sword"}`.
- Event keys: не задано → `["weapon"]`.

| Компонент | 1.6 | 2.8.14 |
|---|---|---|
| `minecraft:allow_off_hand` | `true` | `false` |
| `minecraft:creative_category` | не задано | `{"parent":"itemGroup.name.sword"}` |
| `minecraft:damage` | `7` | `7.2` |
| `minecraft:display_name` | не задано | `{}` |
| `minecraft:durability` | `{"max_durability":1000}` | `{"max_durability":1316}` |
| `minecraft:foil` | не задано | `false` |
| `minecraft:glint` | `false` | не задано |
| `minecraft:repairable` | `{"repair_items":[{"items":["effect:magma_sword"],"repair_amount":1000}]}` | `{"repair_items":[{"items":["effect:magma_sword"],"repair_amount":1316},{"items":["minecraft:magma"],"repair_amount":100}]}` |
| `minecraft:weapon` | не задано | `{"on_hurt_entity":{"event":"weapon"}}` |
| `tag:minecraft:is_sword` | `{}` | не задано |

### `effect:obsidian_sword`

- Источники: `Sword_B/items/obsidian_sword.json` · `Swords_B/items/obsidian_sword.json`.
- `format_version`: `"1.20.20"` → `"1.16.100"`.
- Description: `{"identifier":"effect:obsidian_sword","menu_category":{"category":"equipment"}}` → `{"category":"equipment","identifier":"effect:obsidian_sword"}`.
- Event keys: не задано → `["weapon"]`.

| Компонент | 1.6 | 2.8.14 |
|---|---|---|
| `minecraft:allow_off_hand` | `true` | `false` |
| `minecraft:creative_category` | не задано | `{"parent":"itemGroup.name.sword"}` |
| `minecraft:damage` | `12` | `8` |
| `minecraft:display_name` | не задано | `{}` |
| `minecraft:foil` | не задано | `false` |
| `minecraft:glint` | `false` | не задано |
| `minecraft:repairable` | `{"repair_items":[{"items":["effect:obsidian_sword"],"repair_amount":3000}]}` | `{"repair_items":[{"items":["effect:obsidian_sword"],"repair_amount":3000},{"items":["minecraft:obsidian"],"repair_amount":120}]}` |
| `minecraft:weapon` | не задано | `{"on_hurt_entity":{"event":"weapon"}}` |
| `tag:minecraft:is_sword` | `{}` | не задано |

### `effect:quartz_sword`

- Источники: `Sword_B/items/quartz_sword.json` · `Swords_B/items/quartz_sword.json`.
- `format_version`: `"1.20.20"` → `"1.16.100"`.
- Description: `{"identifier":"effect:quartz_sword","menu_category":{"category":"equipment"}}` → `{"category":"equipment","identifier":"effect:quartz_sword"}`.
- Event keys: не задано → `["weapon"]`.

| Компонент | 1.6 | 2.8.14 |
|---|---|---|
| `minecraft:allow_off_hand` | `true` | `false` |
| `minecraft:creative_category` | не задано | `{"parent":"itemGroup.name.sword"}` |
| `minecraft:display_name` | не задано | `{}` |
| `minecraft:foil` | не задано | `true` |
| `minecraft:glint` | `true` | не задано |
| `minecraft:render_offsets` | не задано | `{"main_hand":{"first_person":{"position":[1.0,0,-2],"scale":[0.07,0.07,0.07]},"third_person":{"position":[0.2,1.1,-0.5],"scale":[0.08,0.08,0.08]}}}` |
| `minecraft:repairable` | `{"repair_items":[{"items":["effect:quartz_sword"],"repair_amount":1}]}` | не задано |
| `minecraft:weapon` | не задано | `{"on_hit_block":{"event":"weapon"},"on_hurt_entity":{"event":"weapon"},"on_not_hurt_entity":{"event":"weapon"}}` |
| `tag:minecraft:is_sword` | `{}` | не задано |

### `effect:sea_sword`

- Источники: `Sword_B/items/sea_sword.json` · `Swords_B/items/sea_sword.json`.
- `format_version`: `"1.20.20"` → `"1.16.100"`.
- Description: `{"identifier":"effect:sea_sword","menu_category":{"category":"equipment"}}` → `{"category":"equipment","identifier":"effect:sea_sword"}`.
- Event keys: не задано → `["weapon"]`.

| Компонент | 1.6 | 2.8.14 |
|---|---|---|
| `minecraft:allow_off_hand` | `true` | `false` |
| `minecraft:creative_category` | не задано | `{"parent":"itemGroup.name.sword"}` |
| `minecraft:display_name` | не задано | `{}` |
| `minecraft:durability` | `{"max_durability":1000}` | `{"max_durability":1356}` |
| `minecraft:foil` | не задано | `true` |
| `minecraft:glint` | `true` | не задано |
| `minecraft:repairable` | `{"repair_items":[{"items":["effect:sea_sword"],"repair_amount":1000}]}` | `{"repair_items":[{"items":["effect:sea_sword"],"repair_amount":1356},{"items":["minecraft:heart_of_the_sea"],"repair_amount":482}]}` |
| `minecraft:weapon` | не задано | `{"on_hurt_entity":{"event":"weapon"}}` |
| `tag:minecraft:is_sword` | `{}` | не задано |

### `effect:shulker_sword`

- Источники: `Sword_B/items/shulker_sword.json` · `Swords_B/items/shulker_sword.json`.
- `format_version`: `"1.20.20"` → `"1.16.100"`.
- Description: `{"identifier":"effect:shulker_sword","menu_category":{"category":"equipment"}}` → `{"category":"equipment","identifier":"effect:shulker_sword"}`.
- Event keys: не задано → `["on_use","weapon"]`.

| Компонент | 1.6 | 2.8.14 |
|---|---|---|
| `minecraft:allow_off_hand` | `true` | `false` |
| `minecraft:cooldown` | не задано | `{"category":"shulker_sword","duration":8}` |
| `minecraft:creative_category` | не задано | `{"parent":"itemGroup.name.sword"}` |
| `minecraft:damage` | `7` | `6` |
| `minecraft:display_name` | не задано | `{}` |
| `minecraft:durability` | `{"max_durability":1000}` | `{"max_durability":2609}` |
| `minecraft:foil` | не задано | `false` |
| `minecraft:glint` | `false` | не задано |
| `minecraft:on_use` | не задано | `{"on_use":{"event":"on_use"}}` |
| `minecraft:repairable` | `{"repair_items":[{"items":["effect:shulker_sword"],"repair_amount":1000}]}` | `{"repair_items":[{"items":["effect:shulker_sword"],"repair_amount":2609}]}` |
| `minecraft:weapon` | не задано | `{"on_hit_block":{"event":"weapon"},"on_hurt_entity":{"event":"weapon"},"on_not_hurt_entity":{"event":"weapon"}}` |
| `tag:minecraft:is_sword` | `{}` | не задано |

### `effect:slime_sword`

- Источники: `Sword_B/items/slime_sword.json` · `Swords_B/items/slime_sword.json`.
- `format_version`: `"1.20.20"` → `"1.16.100"`.
- Description: `{"identifier":"effect:slime_sword","menu_category":{"category":"equipment"}}` → `{"category":"equipment","identifier":"effect:slime_sword"}`.
- Event keys: не задано → `["weapon"]`.

| Компонент | 1.6 | 2.8.14 |
|---|---|---|
| `minecraft:allow_off_hand` | `true` | `false` |
| `minecraft:creative_category` | не задано | `{"parent":"itemGroup.name.sword"}` |
| `minecraft:display_name` | не задано | `{}` |
| `minecraft:foil` | не задано | `false` |
| `minecraft:glint` | `false` | не задано |
| `minecraft:repairable` | `{"repair_items":[{"items":["effect:slime_sword"],"repair_amount":675}]}` | `{"repair_items":[{"items":["effect:slime_sword"],"repair_amount":675},{"items":["minecraft:slime"],"repair_amount":48}]}` |
| `minecraft:weapon` | не задано | `{"on_hurt_entity":{"event":"weapon"}}` |
| `tag:minecraft:is_sword` | `{}` | не задано |

### `effect:spectral_sword`

- Источники: `Sword_B/items/spectral_sword.json` · `Swords_B/items/spectral_sword.json`.
- `format_version`: `"1.20.20"` → `"1.16.100"`.
- Description: `{"identifier":"effect:spectral_sword","menu_category":{"category":"equipment"}}` → `{"category":"equipment","identifier":"effect:spectral_sword"}`.
- Event keys: не задано → `["on_use","weapon"]`.

| Компонент | 1.6 | 2.8.14 |
|---|---|---|
| `minecraft:allow_off_hand` | `true` | `false` |
| `minecraft:cooldown` | не задано | `{"category":"spectral_sword","duration":18}` |
| `minecraft:creative_category` | не задано | `{"parent":"itemGroup.name.sword"}` |
| `minecraft:display_name` | не задано | `{}` |
| `minecraft:foil` | не задано | `true` |
| `minecraft:glint` | `true` | не задано |
| `minecraft:on_use` | не задано | `{"on_use":{"event":"on_use"}}` |
| `minecraft:render_offsets` | не задано | `{"main_hand":{"first_person":{"position":[0.57,0.1,-1.24]},"third_person":{"position":[0.41,1.7,-0.7]}}}` |
| `minecraft:repairable` | `{"repair_items":[{"items":["effect:spectral_sword"],"repair_amount":3256}]}` | `{"repair_items":[{"items":["effect:spectral_sword"],"repair_amount":3256},{"items":["minecraft:end_crystal"],"repair_amount":620},{"items":["minecraft:nether_star"],"repair_amount":2052}]}` |
| `minecraft:should_despawn` | не задано | `false` |
| `minecraft:weapon` | не задано | `{"on_hit_block":{"event":"weapon"},"on_hurt_entity":{"event":"weapon"},"on_not_hurt_entity":{"event":"weapon"}}` |
| `tag:minecraft:is_sword` | `{}` | не задано |

### `effect:spider_sword`

- Источники: `Sword_B/items/spider_sword.json` · `Swords_B/items/spider_sword.json`.
- `format_version`: `"1.20.20"` → `"1.16.100"`.
- Description: `{"identifier":"effect:spider_sword","menu_category":{"category":"equipment"}}` → `{"category":"equipment","identifier":"effect:spider_sword"}`.
- Event keys: не задано → `["on_use","weapon"]`.

| Компонент | 1.6 | 2.8.14 |
|---|---|---|
| `minecraft:allow_off_hand` | `true` | `false` |
| `minecraft:cooldown` | не задано | `{"category":"spider_sword","duration":28}` |
| `minecraft:creative_category` | не задано | `{"parent":"itemGroup.name.sword"}` |
| `minecraft:damage` | `6` | `5` |
| `minecraft:digger` | `{"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}],"use_efficiency":true}` | `{"destroy_speeds":[{"block":"minecraft:web","speed":100},{"block":"minecraft:bamboo","speed":10}],"use_efficiency":true}` |
| `minecraft:display_name` | не задано | `{}` |
| `minecraft:foil` | не задано | `false` |
| `minecraft:glint` | `false` | не задано |
| `minecraft:on_use` | не задано | `{"on_use":{"event":"on_use"}}` |
| `minecraft:repairable` | `{"repair_items":[{"items":["effect:spider_sword"],"repair_amount":628}]}` | `{"repair_items":[{"items":["effect:spider_sword"],"repair_amount":628},{"items":["minecraft:web"],"repair_amount":128},{"items":["minecraft:spider_eye"],"repair_amount":48}]}` |
| `minecraft:weapon` | не задано | `{"on_hit_block":{"event":"weapon"},"on_hurt_entity":{"event":"weapon"},"on_not_hurt_entity":{"event":"weapon"}}` |
| `tag:minecraft:is_sword` | `{}` | не задано |

### `effect:sponge_sword`

- Источники: `Sword_B/items/sponge_sword.json` · `Swords_B/items/sponge_sword.json`.
- `format_version`: `"1.20.20"` → `"1.16.100"`.
- Description: `{"identifier":"effect:sponge_sword","menu_category":{"category":"equipment"}}` → `{"category":"equipment","identifier":"effect:sponge_sword"}`.
- Event keys: не задано → `["weapon"]`.

| Компонент | 1.6 | 2.8.14 |
|---|---|---|
| `minecraft:allow_off_hand` | `true` | `false` |
| `minecraft:creative_category` | не задано | `{"parent":"itemGroup.name.sword"}` |
| `minecraft:damage` | `6` | `5` |
| `minecraft:display_name` | не задано | `{}` |
| `minecraft:enchantable` | `{"slot":"sword","value":9}` | не задано |
| `minecraft:foil` | не задано | `false` |
| `minecraft:glint` | `false` | не задано |
| `minecraft:repairable` | `{"repair_items":[{"items":["effect:sponge_sword"],"repair_amount":128}]}` | `{"repair_items":[{"items":["effect:sponge_sword"],"repair_amount":128},{"items":["minecraft:sponge"],"repair_amount":62}]}` |
| `minecraft:weapon` | не задано | `{"on_hurt_entity":{"event":"weapon"}}` |
| `tag:minecraft:is_sword` | `{}` | не задано |

### `effect:tnt_sword`

- Источники: `Sword_B/items/tnt_sword.json` · `Swords_B/items/tnt_sword.json`.
- `format_version`: `"1.20.20"` → `"1.16.100"`.
- Description: `{"identifier":"effect:tnt_sword","menu_category":{"category":"equipment"}}` → `{"category":"equipment","identifier":"effect:tnt_sword"}`.
- Event keys: не задано → `["on_use","weapon"]`.

| Компонент | 1.6 | 2.8.14 |
|---|---|---|
| `minecraft:allow_off_hand` | `true` | `false` |
| `minecraft:cooldown` | не задано | `{"category":"tnt_sword","duration":10}` |
| `minecraft:creative_category` | не задано | `{"parent":"itemGroup.name.sword"}` |
| `minecraft:damage` | `7` | `4` |
| `minecraft:digger` | `{"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}],"use_efficiency":true}` | не задано |
| `minecraft:display_name` | не задано | `{}` |
| `minecraft:durability` | `{"max_durability":1}` | `{"max_durability":64}` |
| `minecraft:enchantable` | не задано | `{"slot":"sword","value":9}` |
| `minecraft:foil` | не задано | `false` |
| `minecraft:glint` | `false` | не задано |
| `minecraft:on_use` | не задано | `{"on_use":{"event":"on_use"}}` |
| `minecraft:repairable` | `{"repair_items":[{"items":["effect:tnt_sword"],"repair_amount":1}]}` | `{"repair_items":[{"items":["effect:tnt_sword"],"repair_amount":64},{"items":["minecraft:tnt"],"repair_amount":18}]}` |
| `minecraft:weapon` | не задано | `{"on_hit_block":{"event":"weapon"},"on_hurt_entity":{"event":"weapon"},"on_not_hurt_entity":{"event":"weapon"}}` |
| `tag:minecraft:is_sword` | `{}` | не задано |

### `effect:wither_sword`

- Источники: `Sword_B/items/wither_sword.json` · `Swords_B/items/wither_sword.json`.
- `format_version`: `"1.20.20"` → `"1.16.100"`.
- Description: `{"identifier":"effect:wither_sword","menu_category":{"category":"equipment"}}` → `{"category":"equipment","identifier":"effect:wither_sword"}`.
- Event keys: не задано → `["on_use","weapon"]`.

| Компонент | 1.6 | 2.8.14 |
|---|---|---|
| `minecraft:allow_off_hand` | `true` | `false` |
| `minecraft:cooldown` | не задано | `{"category":"wither_sword","duration":3}` |
| `minecraft:creative_category` | не задано | `{"parent":"itemGroup.name.sword"}` |
| `minecraft:display_name` | не задано | `{}` |
| `minecraft:durability` | `{"max_durability":1256}` | `{"max_durability":3856}` |
| `minecraft:enchantable` | `{"slot":"sword","value":9}` | не задано |
| `minecraft:foil` | не задано | `true` |
| `minecraft:glint` | `true` | не задано |
| `minecraft:on_use` | не задано | `{"on_use":{"event":"on_use"}}` |
| `minecraft:render_offsets` | не задано | `{"main_hand":{"first_person":{"position":[0.8,0.1,-1.8],"scale":[0.01,0.01,0.01]},"third_person":{"position":[0.8,2.5,-1.2],"scale":[0.027,0.027,0.027]}}}` |
| `minecraft:repairable` | `{"repair_items":[{"items":["effect:wither_sword"],"repair_amount":1256}]}` | `{"repair_items":[{"items":["effect:wither_sword"],"repair_amount":3856}]}` |
| `minecraft:should_despawn` | не задано | `false` |
| `minecraft:weapon` | не задано | `{"on_hit_block":{"event":"weapon"},"on_hurt_entity":{"event":"weapon"},"on_not_hurt_entity":{"event":"weapon"}}` |
| `tag:minecraft:is_sword` | `{}` | не задано |

