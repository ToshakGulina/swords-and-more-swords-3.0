# Предметы: прочность, ремонт и флаги по версиям

Полные буквальные компоненты `minecraft:durability` и `minecraft:repairable` из всех item JSON, а также заданные значения `foil`, `hand_equipped`, `allow_off_hand`, `max_stack_size`. Значения материалов и `repair_amount` не нормализуются и не исправляются; `—` означает **нет поля**, а не false, нулевую прочность, бесконечность или невозможность иных способов ремонта. Таблица не включает вызовы weapon/on-use и фактический расход прочности.

В 2.8.8 и 2.8.14 все разобранные **компоненты** одноимённых 42 item структурно совпадают. Это не означает равенства файлов целиком: события Ice различаются. Для урона и зачарования см. [сводную таблицу предметов](quick-reference.md), для различий 25 общих ID — [матрицу](item-version-matrix.md), для событий — [weapon](weapon-event-index.md) и [on-use](on-use-index.md).

Обратите внимание на буквальные ID: `minecraft:fire`, `minecraft:slime`, `minecraft:magma` и `minecraft:bone_meal` не заменяются похожими именами. У `effect:wet_sponge_sword` наряду с самим предметом указан `effect:sponge_sword`; у Cursed Pumpkin как материалы присутствуют `minecraft:honey_block` и `minecraft:honeycomb`. Это зафиксированное содержимое архива, а не вывод о доступности материала.

## 1.6

Всего item ID: 26; с явно заданным `minecraft:repairable`: 26; без этого компонента: 0.

| ID | durability | repairable целиком | foil | hand_equipped | allow_off_hand | max_stack_size |
|---|---|---|---|---|---|---|
| [`effect:blaze_sword`](items-1.6.md#effectblaze_sword) | `{"max_durability":2300}` | `{"repair_items":[{"items":["effect:blaze_sword"],"repair_amount":2300}]}` | — | `true` | `true` | `1` |
| [`effect:bone_sword`](items-1.6.md#effectbone_sword) | `{"max_durability":820}` | `{"repair_items":[{"items":["effect:bone_sword"],"repair_amount":820}]}` | — | `true` | `true` | `1` |
| [`effect:cactus_sword`](items-1.6.md#effectcactus_sword) | `{"max_durability":125}` | `{"repair_items":[{"items":["effect:cactus_sword"],"repair_amount":125}]}` | — | `true` | `true` | `1` |
| [`effect:coal_sword`](items-1.6.md#effectcoal_sword) | `{"max_durability":121}` | `{"repair_items":[{"items":["effect:coal_sword"],"repair_amount":121}]}` | — | `true` | `true` | `1` |
| [`effect:creeper_sword`](items-1.6.md#effectcreeper_sword) | `{"max_durability":1500}` | `{"repair_items":[{"items":["effect:creeper_sword"],"repair_amount":1500}]}` | — | `true` | `true` | `1` |
| [`effect:emerald_sword`](items-1.6.md#effectemerald_sword) | `{"max_durability":2300}` | `{"repair_items":[{"items":["effect:emerald_sword"],"repair_amount":2300}]}` | — | `true` | `true` | `1` |
| [`effect:ender_sword`](items-1.6.md#effectender_sword) | `{"max_durability":1256}` | `{"repair_items":[{"items":["effect:ender_sword"],"repair_amount":1256}]}` | — | `true` | `true` | `1` |
| [`effect:fire_sword`](items-1.6.md#effectfire_sword) | `{"max_durability":2000}` | `{"repair_items":[{"items":["effect:fire_sword"],"repair_amount":2000}]}` | — | `true` | `true` | `1` |
| [`effect:glowstone_sword`](items-1.6.md#effectglowstone_sword) | `{"max_durability":128}` | `{"repair_items":[{"items":["effect:glowstone_sword"],"repair_amount":128}]}` | — | `true` | `true` | `1` |
| [`effect:grass_sword`](items-1.6.md#effectgrass_sword) | `{"max_durability":250}` | `{"repair_items":[{"items":["effect:grass_sword"],"repair_amount":250}]}` | — | `true` | `true` | `1` |
| [`effect:ice_sword`](items-1.6.md#effectice_sword) | `{"max_durability":500}` | `{"repair_items":[{"items":["effect:ice_sword"],"repair_amount":500}]}` | — | `true` | `true` | `1` |
| [`effect:jungle_sword`](items-1.6.md#effectjungle_sword) | `{"max_durability":128}` | `{"repair_items":[{"items":["effect:jungle_sword"],"repair_amount":128}]}` | — | `true` | `true` | `1` |
| [`effect:lapis_sword`](items-1.6.md#effectlapis_sword) | `{"max_durability":528}` | `{"repair_items":[{"items":["effect:lapis_sword"],"repair_amount":528}]}` | — | `true` | `true` | `1` |
| [`effect:lightning_sword`](items-1.6.md#effectlightning_sword) | `{"max_durability":2000}` | `{"repair_items":[{"items":["effect:lightning_sword"],"repair_amount":2000}]}` | — | `true` | `true` | `1` |
| [`effect:magma_sword`](items-1.6.md#effectmagma_sword) | `{"max_durability":1000}` | `{"repair_items":[{"items":["effect:magma_sword"],"repair_amount":1000}]}` | — | `true` | `true` | `1` |
| [`effect:obsidian_sword`](items-1.6.md#effectobsidian_sword) | `{"max_durability":3000}` | `{"repair_items":[{"items":["effect:obsidian_sword"],"repair_amount":3000}]}` | — | `true` | `true` | `1` |
| [`effect:quartz_sword`](items-1.6.md#effectquartz_sword) | `{"max_durability":1}` | `{"repair_items":[{"items":["effect:quartz_sword"],"repair_amount":1}]}` | — | `true` | `true` | `1` |
| [`effect:sea_sword`](items-1.6.md#effectsea_sword) | `{"max_durability":1000}` | `{"repair_items":[{"items":["effect:sea_sword"],"repair_amount":1000}]}` | — | `true` | `true` | `1` |
| [`effect:shulker_sword`](items-1.6.md#effectshulker_sword) | `{"max_durability":1000}` | `{"repair_items":[{"items":["effect:shulker_sword"],"repair_amount":1000}]}` | — | `true` | `true` | `1` |
| [`effect:slime_sword`](items-1.6.md#effectslime_sword) | `{"max_durability":675}` | `{"repair_items":[{"items":["effect:slime_sword"],"repair_amount":675}]}` | — | `true` | `true` | `1` |
| [`effect:spectral_sword`](items-1.6.md#effectspectral_sword) | `{"max_durability":3256}` | `{"repair_items":[{"items":["effect:spectral_sword"],"repair_amount":3256}]}` | — | `true` | `true` | `1` |
| [`effect:spider_sword`](items-1.6.md#effectspider_sword) | `{"max_durability":628}` | `{"repair_items":[{"items":["effect:spider_sword"],"repair_amount":628}]}` | — | `true` | `true` | `1` |
| [`effect:sponge_sword`](items-1.6.md#effectsponge_sword) | `{"max_durability":128}` | `{"repair_items":[{"items":["effect:sponge_sword"],"repair_amount":128}]}` | — | `true` | `true` | `1` |
| [`effect:sword_of_time`](items-1.6.md#effectsword_of_time) | `{"max_durability":128}` | `{"repair_items":[{"items":["effect:sword_of_time"],"repair_amount":128}]}` | — | `true` | `true` | `1` |
| [`effect:tnt_sword`](items-1.6.md#effecttnt_sword) | `{"max_durability":1}` | `{"repair_items":[{"items":["effect:tnt_sword"],"repair_amount":1}]}` | — | `true` | `true` | `1` |
| [`effect:wither_sword`](items-1.6.md#effectwither_sword) | `{"max_durability":1256}` | `{"repair_items":[{"items":["effect:wither_sword"],"repair_amount":1256}]}` | — | `true` | `true` | `1` |

## 2.8.8 и 2.8.14

Всего item ID: 42; с явно заданным `minecraft:repairable`: 33; без этого компонента: 9.

| ID | durability | repairable целиком | foil | hand_equipped | allow_off_hand | max_stack_size |
|---|---|---|---|---|---|---|
| [`effect:bedrock_stick`](items-2.8.14.md#effectbedrock_stick) | — | — | `false` | `true` | `false` | `1` |
| [`effect:bedrock_sword`](items-2.8.14.md#effectbedrock_sword) | — | — | `false` | `true` | `false` | `1` |
| [`effect:bee_sword`](items-2.8.14.md#effectbee_sword) | `{"max_durability":1080}` | `{"repair_items":[{"items":["effect:bee_sword"],"repair_amount":1080},{"items":["minecraft:honey_block"],"repair_amount":400},{"items":["minecraft:honeycomb"],"repair_amount":150}]}` | `false` | `true` | `false` | `1` |
| [`effect:blaze_sword`](items-2.8.14.md#effectblaze_sword) | `{"max_durability":2300}` | `{"repair_items":[{"items":["effect:blaze_sword"],"repair_amount":2300}]}` | `false` | `true` | `false` | `1` |
| [`effect:bone_sword`](items-2.8.14.md#effectbone_sword) | `{"max_durability":820}` | `{"repair_items":[{"items":["effect:bone_sword"],"repair_amount":820},{"items":["minecraft:bone"],"repair_amount":70},{"items":["minecraft:bone_block"],"repair_amount":300},{"items":["minecraft:bone_meal"],"repair_amount":18}]}` | `false` | `true` | `false` | `1` |
| [`effect:cactus_sword`](items-2.8.14.md#effectcactus_sword) | `{"max_durability":125}` | `{"repair_items":[{"items":["effect:cactus_sword"],"repair_amount":125}]}` | `false` | `true` | `false` | `1` |
| [`effect:clock_sword`](items-2.8.14.md#effectclock_sword) | `{"max_durability":4800}` | `{"repair_items":[{"items":["effect:clock_sword"],"repair_amount":4800},{"items":["minecraft:clock"],"repair_amount":900},{"items":["minecraft:gold_block"],"repair_amount":780},{"items":["minecraft:gold_ingot"],"repair_amount":87}]}` | `true` | `true` | `false` | `1` |
| [`effect:coal_sword`](items-2.8.14.md#effectcoal_sword) | `{"max_durability":121}` | `{"repair_items":[{"items":["effect:coal_sword"],"repair_amount":121},{"items":["minecraft:coal"],"repair_amount":58},{"items":["minecraft:stick"],"repair_amount":2}]}` | `false` | `true` | `false` | `1` |
| [`effect:creeper_sword`](items-2.8.14.md#effectcreeper_sword) | `{"max_durability":1500}` | `{"repair_items":[{"items":["effect:creeper_sword"],"repair_amount":1500},{"items":["minecraft:gunpowder"],"repair_amount":256}]}` | `false` | `true` | `false` | `1` |
| [`effect:cursed_pumpkin_sword`](items-2.8.14.md#effectcursed_pumpkin_sword) | `{"max_durability":606}` | `{"repair_items":[{"items":["effect:cursed_pumpkin_sword"],"repair_amount":606},{"items":["minecraft:honey_block"],"repair_amount":400},{"items":["minecraft:honeycomb"],"repair_amount":150}]}` | `false` | `true` | `false` | `1` |
| [`effect:emerald_sword`](items-2.8.14.md#effectemerald_sword) | `{"max_durability":2300}` | `{"repair_items":[{"items":["effect:emerald_sword"],"repair_amount":2300}]}` | `false` | `true` | `false` | `1` |
| [`effect:ender_sword`](items-2.8.14.md#effectender_sword) | `{"max_durability":1256}` | `{"repair_items":[{"items":["effect:ender_sword"],"repair_amount":1256},{"items":["minecraft:ender_pearl"],"repair_amount":28},{"items":["minecraft:ender_eye"],"repair_amount":32}]}` | `true` | `true` | `false` | `1` |
| [`effect:fire_sword`](items-2.8.14.md#effectfire_sword) | `{"max_durability":2000}` | `{"repair_items":[{"items":["effect:fire_sword"],"repair_amount":2000},{"items":["minecraft:fire"],"repair_amount":1000}]}` | `true` | `true` | `false` | `1` |
| [`effect:ghost_sword`](items-2.8.14.md#effectghost_sword) | `{"max_durability":3333}` | — | `true` | `true` | `false` | `1` |
| [`effect:glass_sword`](items-2.8.14.md#effectglass_sword) | `{"max_durability":1}` | `{"repair_items":[{"items":["effect:glass_sword"],"repair_amount":1},{"items":["minecraft:glass"],"repair_amount":1}]}` | `false` | `true` | `false` | `1` |
| [`effect:glowstone_sword`](items-2.8.14.md#effectglowstone_sword) | `{"max_durability":128}` | `{"repair_items":[{"items":["effect:glowstone_sword"],"repair_amount":128},{"items":["minecraft:glowstone"],"repair_amount":64},{"items":["minecraft:glowstone_dust"],"repair_amount":16}]}` | `true` | `true` | `true` | `1` |
| [`effect:grass_sword`](items-2.8.14.md#effectgrass_sword) | `{"max_durability":250}` | `{"repair_items":[{"items":["effect:grass_sword"],"repair_amount":250}]}` | `false` | `true` | `false` | `1` |
| [`effect:ice_sword`](items-2.8.14.md#effectice_sword) | `{"max_durability":500}` | `{"repair_items":[{"items":["effect:ice_sword"],"repair_amount":500},{"items":["minecraft:ice"],"repair_amount":55}]}` | `true` | `true` | `false` | `1` |
| [`effect:jungle_sword`](items-2.8.14.md#effectjungle_sword) | `{"max_durability":128}` | `{"repair_items":[{"items":["effect:jungle_sword"],"repair_amount":128}]}` | `false` | `true` | `false` | `1` |
| [`effect:lapis_sword`](items-2.8.14.md#effectlapis_sword) | `{"max_durability":528}` | `{"repair_items":[{"items":["effect:lapis_sword"],"repair_amount":528},{"items":["minecraft:lapis_lazuli"],"repair_amount":48}]}` | `false` | `true` | `false` | `1` |
| [`effect:lightning_sword`](items-2.8.14.md#effectlightning_sword) | `{"max_durability":2012}` | `{"repair_items":[{"items":["effect:lightning_sword"],"repair_amount":2012}]}` | `true` | `true` | `false` | `1` |
| [`effect:magma_sword`](items-2.8.14.md#effectmagma_sword) | `{"max_durability":1316}` | `{"repair_items":[{"items":["effect:magma_sword"],"repair_amount":1316},{"items":["minecraft:magma"],"repair_amount":100}]}` | `false` | `true` | `false` | `1` |
| [`effect:nether_star_sword`](items-2.8.14.md#effectnether_star_sword) | `{"max_durability":3256}` | `{"repair_items":[{"items":["effect:nether_star_sword"],"repair_amount":3256},{"items":["minecraft:nether_star"],"repair_amount":3000}]}` | `true` | `true` | `false` | `1` |
| [`effect:obsidian_sword`](items-2.8.14.md#effectobsidian_sword) | `{"max_durability":3000}` | `{"repair_items":[{"items":["effect:obsidian_sword"],"repair_amount":3000},{"items":["minecraft:obsidian"],"repair_amount":120}]}` | `false` | `true` | `false` | `1` |
| [`effect:quartz_diamond`](items-2.8.14.md#effectquartz_diamond) | — | — | `true` | `false` | — | `9` |
| [`effect:quartz_diamond_stick`](items-2.8.14.md#effectquartz_diamond_stick) | `{"max_durability":20}` | — | `true` | `true` | `false` | `1` |
| [`effect:quartz_sword`](items-2.8.14.md#effectquartz_sword) | `{"max_durability":1}` | — | `true` | `true` | `false` | `1` |
| [`effect:sea_sword`](items-2.8.14.md#effectsea_sword) | `{"max_durability":1356}` | `{"repair_items":[{"items":["effect:sea_sword"],"repair_amount":1356},{"items":["minecraft:heart_of_the_sea"],"repair_amount":482}]}` | `true` | `true` | `false` | `1` |
| [`effect:shulker_sword`](items-2.8.14.md#effectshulker_sword) | `{"max_durability":2609}` | `{"repair_items":[{"items":["effect:shulker_sword"],"repair_amount":2609}]}` | `false` | `true` | `false` | `1` |
| [`effect:silver_ingot`](items-2.8.14.md#effectsilver_ingot) | — | — | — | `false` | — | `64` |
| [`effect:silver_sword`](items-2.8.14.md#effectsilver_sword) | `{"max_durability":1800}` | `{"repair_items":[{"items":["effect:silver_sword"],"repair_amount":1800}]}` | `false` | `true` | `false` | `1` |
| [`effect:slime_sword`](items-2.8.14.md#effectslime_sword) | `{"max_durability":675}` | `{"repair_items":[{"items":["effect:slime_sword"],"repair_amount":675},{"items":["minecraft:slime"],"repair_amount":48}]}` | `false` | `true` | `false` | `1` |
| [`effect:spectral_sword`](items-2.8.14.md#effectspectral_sword) | `{"max_durability":3256}` | `{"repair_items":[{"items":["effect:spectral_sword"],"repair_amount":3256},{"items":["minecraft:end_crystal"],"repair_amount":620},{"items":["minecraft:nether_star"],"repair_amount":2052}]}` | `true` | `true` | `false` | `1` |
| [`effect:spider_sword`](items-2.8.14.md#effectspider_sword) | `{"max_durability":628}` | `{"repair_items":[{"items":["effect:spider_sword"],"repair_amount":628},{"items":["minecraft:web"],"repair_amount":128},{"items":["minecraft:spider_eye"],"repair_amount":48}]}` | `false` | `true` | `false` | `1` |
| [`effect:sponge_sword`](items-2.8.14.md#effectsponge_sword) | `{"max_durability":128}` | `{"repair_items":[{"items":["effect:sponge_sword"],"repair_amount":128},{"items":["minecraft:sponge"],"repair_amount":62}]}` | `false` | `true` | `false` | `1` |
| [`effect:time_sword`](items-2.8.14.md#effecttime_sword) | `{"max_durability":13770}` | — | `true` | `true` | `false` | `1` |
| [`effect:tnt_sword`](items-2.8.14.md#effecttnt_sword) | `{"max_durability":64}` | `{"repair_items":[{"items":["effect:tnt_sword"],"repair_amount":64},{"items":["minecraft:tnt"],"repair_amount":18}]}` | `false` | `true` | `false` | `1` |
| [`effect:ultra_instinct_sword`](items-2.8.14.md#effectultra_instinct_sword) | `{"max_durability":9999}` | — | `true` | `true` | `false` | `1` |
| [`effect:wet_sponge_sword`](items-2.8.14.md#effectwet_sponge_sword) | `{"max_durability":64}` | `{"repair_items":[{"items":["effect:sponge_sword"],"repair_amount":64},{"items":["minecraft:sponge"],"repair_amount":32},{"items":["effect:wet_sponge_sword"],"repair_amount":64}]}` | `false` | `true` | `false` | `1` |
| [`effect:wither_skeleton_sword`](items-2.8.14.md#effectwither_skeleton_sword) | `{"max_durability":128}` | `{"repair_items":[{"items":["effect:wither_skeleton_sword"],"repair_amount":128},{"items":["minecraft:coal"],"repair_amount":58},{"items":["minecraft:stick"],"repair_amount":2}]}` | `false` | `true` | `false` | `1` |
| [`effect:wither_sword`](items-2.8.14.md#effectwither_sword) | `{"max_durability":3856}` | `{"repair_items":[{"items":["effect:wither_sword"],"repair_amount":3856}]}` | `true` | `true` | `false` | `1` |
| [`effect:wolf_sword`](items-2.8.14.md#effectwolf_sword) | `{"max_durability":2800}` | `{"repair_items":[{"items":["effect:wolf_sword"],"repair_amount":2800}]}` | `false` | `true` | `false` | `1` |

