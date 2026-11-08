# Правила добычи предметов: три исходные версии

Группировка буквальных `minecraft:digger` предметов из behavior pack. Профили равны только при одинаковой разобранной структуре компонента, включая порядок массива `destroy_speeds`; остальные свойства предметов могут различаться. Список правил Bedrock Sword сохранён в исходном порядке с повторами. Отсутствие компонента **не** означает скорость 0, запрет добычи или отсутствие ванильных значений. Механика блоков, приоритет пересекающихся правил, чары и `on_dig` требуют испытаний.

Диагностика JSON5: ошибки и повторные ключи не обнаружены.

| Профиль | 1.6 предметов | 2.8.8 предметов | 2.8.14 предметов |
|---|---:|---:|---:|
| P01 | 26 | 32 | 32 |
| P02 | 0 | 6 | 6 |
| P03 | 0 | 1 | 1 |
| P04 | 0 | 1 | 1 |
| P05 | 0 | 1 | 1 |
| P06 | 0 | 1 | 1 |

## P01

- **1.6 (26)**: `effect:blaze_sword`, `effect:bone_sword`, `effect:cactus_sword`, `effect:coal_sword`, `effect:creeper_sword`, `effect:emerald_sword`, `effect:ender_sword`, `effect:fire_sword`, `effect:glowstone_sword`, `effect:grass_sword`, `effect:ice_sword`, `effect:jungle_sword`, `effect:lapis_sword`, `effect:lightning_sword`, `effect:magma_sword`, `effect:obsidian_sword`, `effect:quartz_sword`, `effect:sea_sword`, `effect:shulker_sword`, `effect:slime_sword`, `effect:spectral_sword`, `effect:spider_sword`, `effect:sponge_sword`, `effect:sword_of_time`, `effect:tnt_sword`, `effect:wither_sword`.
- **2.8.8 (32)**: `effect:bee_sword`, `effect:blaze_sword`, `effect:bone_sword`, `effect:cactus_sword`, `effect:clock_sword`, `effect:coal_sword`, `effect:creeper_sword`, `effect:cursed_pumpkin_sword`, `effect:emerald_sword`, `effect:ender_sword`, `effect:fire_sword`, `effect:ghost_sword`, `effect:glowstone_sword`, `effect:grass_sword`, `effect:ice_sword`, `effect:jungle_sword`, `effect:lapis_sword`, `effect:lightning_sword`, `effect:magma_sword`, `effect:nether_star_sword`, `effect:obsidian_sword`, `effect:quartz_sword`, `effect:sea_sword`, `effect:shulker_sword`, `effect:silver_sword`, `effect:slime_sword`, `effect:spectral_sword`, `effect:sponge_sword`, `effect:time_sword`, `effect:wither_skeleton_sword`, `effect:wither_sword`, `effect:wolf_sword`.
- **2.8.14 (32)**: `effect:bee_sword`, `effect:blaze_sword`, `effect:bone_sword`, `effect:cactus_sword`, `effect:clock_sword`, `effect:coal_sword`, `effect:creeper_sword`, `effect:cursed_pumpkin_sword`, `effect:emerald_sword`, `effect:ender_sword`, `effect:fire_sword`, `effect:ghost_sword`, `effect:glowstone_sword`, `effect:grass_sword`, `effect:ice_sword`, `effect:jungle_sword`, `effect:lapis_sword`, `effect:lightning_sword`, `effect:magma_sword`, `effect:nether_star_sword`, `effect:obsidian_sword`, `effect:quartz_sword`, `effect:sea_sword`, `effect:shulker_sword`, `effect:silver_sword`, `effect:slime_sword`, `effect:spectral_sword`, `effect:sponge_sword`, `effect:time_sword`, `effect:wither_skeleton_sword`, `effect:wither_sword`, `effect:wolf_sword`.

Другие поля компонента: `{"use_efficiency":true}`.

| № | Блок / условие | Остальные поля правила |
|---:|---|---|
| 1 | `"minecraft:web"` | `{"speed":15}` |
| 2 | `"minecraft:bamboo"` | `{"speed":10}` |

## P02

- **2.8.8 (6)**: `effect:bedrock_stick`, `effect:quartz_diamond`, `effect:quartz_diamond_stick`, `effect:silver_ingot`, `effect:tnt_sword`, `effect:wet_sponge_sword`.
- **2.8.14 (6)**: `effect:bedrock_stick`, `effect:quartz_diamond`, `effect:quartz_diamond_stick`, `effect:silver_ingot`, `effect:tnt_sword`, `effect:wet_sponge_sword`.

Компонент `minecraft:digger` не задан.

## P03

- **2.8.8 (1)**: `effect:glass_sword`.
- **2.8.14 (1)**: `effect:glass_sword`.

Другие поля компонента: `{"on_dig":{"event":"weapon"},"use_efficiency":true}`.

| № | Блок / условие | Остальные поля правила |
|---:|---|---|
| 1 | `"minecraft:web"` | `{"on_dig":{"event":"weapon"},"speed":25}` |
| 2 | `"minecraft:bamboo"` | `{"on_dig":{"event":"weapon"},"speed":15}` |

## P04

- **2.8.8 (1)**: `effect:spider_sword`.
- **2.8.14 (1)**: `effect:spider_sword`.

Другие поля компонента: `{"use_efficiency":true}`.

| № | Блок / условие | Остальные поля правила |
|---:|---|---|
| 1 | `"minecraft:web"` | `{"speed":100}` |
| 2 | `"minecraft:bamboo"` | `{"speed":10}` |

## P05

- **2.8.8 (1)**: `effect:ultra_instinct_sword`.
- **2.8.14 (1)**: `effect:ultra_instinct_sword`.

Другие поля компонента: `{"use_efficiency":true}`.

| № | Блок / условие | Остальные поля правила |
|---:|---|---|
| 1 | `"minecraft:web"` | `{"speed":999}` |
| 2 | `"minecraft:bamboo"` | `{"speed":999}` |

## P06

- **2.8.8 (1)**: `effect:bedrock_sword`.
- **2.8.14 (1)**: `effect:bedrock_sword`.

Другие поля компонента: `{"use_efficiency":true}`.

| № | Блок / условие | Остальные поля правила |
|---:|---|---|
| 1 | `{"tags":"q.any_tag('stone', 'metal', 'diamond_pick_diggable', 'wood', 'pumpkin', 'plant', 'dirt', 'sand', 'gravel', 'grass', 'snow')"}` | `{"speed":999}` |
| 2 | `"effect99:quartz_diamond_block"` | `{"speed":50}` |
| 3 | `"effect99:quartz_diamond_ore"` | `{"speed":100}` |
| 4 | `"effect99:silver_ore"` | `{"speed":999}` |
| 5 | `"minecraft:warped_wart_block"` | `{"speed":999}` |
| 6 | `"minecraft:nether_wart_block"` | `{"speed":999}` |
| 7 | `"minecraft:leaves"` | `{"speed":999}` |
| 8 | `"minecraft:leaves2"` | `{"speed":999}` |
| 9 | `"minecraft:hay_block"` | `{"speed":999}` |
| 10 | `"minecraft:soul_soil"` | `{"speed":999}` |
| 11 | `"minecraft:soul_sand"` | `{"speed":999}` |
| 12 | `"minecraft:chest"` | `{"speed":999}` |
| 13 | `"minecraft:melon_block"` | `{"speed":999}` |
| 14 | `"minecraft:bookshelf"` | `{"speed":999}` |
| 15 | `"minecraft:lectern"` | `{"speed":999}` |
| 16 | `"minecraft:pumkin"` | `{"speed":999}` |
| 17 | `"minecraft:ice"` | `{"speed":999}` |
| 18 | `"minecraft:bone_block"` | `{"speed":999}` |
| 19 | `"minecraft:mob_spawner"` | `{"speed":999}` |
| 20 | `"minecraft:anvil"` | `{"speed":999}` |
| 21 | `"minecraft:netherite_block"` | `{"speed":999}` |
| 22 | `"minecraft:sandstone"` | `{"speed":999}` |
| 23 | `"minecraft:diamond_block"` | `{"speed":999}` |
| 24 | `"minecraft:lapis_block"` | `{"speed":999}` |
| 25 | `"minecraft:emerald_block"` | `{"speed":999}` |
| 26 | `"minecraft:ancient_debris"` | `{"speed":999}` |
| 27 | `"minecraft:cracked_polished_blackstone_bricks"` | `{"speed":999}` |
| 28 | `"minecraft:nether_brick"` | `{"speed":999}` |
| 29 | `"minecraft:cracked_nether_bricks"` | `{"speed":999}` |
| 30 | `"minecraft:quartz_ore"` | `{"speed":999}` |
| 31 | `"minecraft:netherrack"` | `{"speed":999}` |
| 32 | `"minecraft:basalt"` | `{"speed":999}` |
| 33 | `"minecraft:end_bricks"` | `{"speed":999}` |
| 34 | `"minecraft:purpur_block"` | `{"speed":999}` |
| 35 | `"minecraft:purpur_stairs"` | `{"speed":999}` |
| 36 | `"minecraft:end_brick_stairs"` | `{"speed":999}` |
| 37 | `"minecraft:stone_slab2"` | `{"speed":999}` |
| 38 | `"minecraft:stone_slab3"` | `{"speed":999}` |
| 39 | `"minecraft:polished_basalt"` | `{"speed":999}` |
| 40 | `"minecraft:warped_nylium"` | `{"speed":999}` |
| 41 | `"minecraft:crimson_nylium"` | `{"speed":999}` |
| 42 | `"minecraft:end_stone"` | `{"speed":999}` |
| 43 | `"minecraft:ender_chest"` | `{"speed":999}` |
| 44 | `"minecraft:quartz_block"` | `{"speed":999}` |
| 45 | `"minecraft:quartz_stairs"` | `{"speed":999}` |
| 46 | `"minecraft:quartz_bricks"` | `{"speed":999}` |
| 47 | `"minecraft:quartz_stairs"` | `{"speed":999}` |
| 48 | `"minecraft:nether_gold_ore"` | `{"speed":999}` |
| 49 | `"minecraft:blackstone"` | `{"speed":999}` |
| 50 | `"minecraft:furnace"` | `{"speed":999}` |
| 51 | `"minecraft:blast_furnace"` | `{"speed":999}` |
| 52 | `"minecraft:lit_furnace"` | `{"speed":999}` |
| 53 | `"minecraft:blast_furnace"` | `{"speed":999}` |
| 54 | `"minecraft:chain"` | `{"speed":999}` |
| 55 | `"minecraft:lantern"` | `{"speed":999}` |
| 56 | `"minecraft:soul_lantern"` | `{"speed":999}` |
| 57 | `"minecraft:grindstone"` | `{"speed":999}` |
| 58 | `"minecraft:brewing_stand"` | `{"speed":999}` |
| 59 | `"minecraft:smooth_stone"` | `{"speed":999}` |
| 60 | `"minecraft:stonebrick"` | `{"speed":999}` |
| 61 | `"minecraft:enchanting_table"` | `{"speed":999}` |
| 62 | `"minecraft:stone_brick_stairs"` | `{"speed":999}` |
| 63 | `"minecraft:mossy_stone_brick_stairs"` | `{"speed":999}` |
| 64 | `"minecraft:polished_blackstone_bricks"` | `{"speed":999}` |
| 65 | `"minecraft:polished_blackstone_stairs"` | `{"speed":999}` |
| 66 | `"minecraft:blackstone_wall"` | `{"speed":999}` |
| 67 | `"minecraft:blackstone_wall"` | `{"speed":999}` |
| 68 | `"minecraft:polished_blackstone_wall"` | `{"speed":999}` |
