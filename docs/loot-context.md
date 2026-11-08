# Контекст loot-пулов для предметов и блоков аддона

Указаны все прямые записи `type=item` с именами `effect:` и `effect99:` внутри обычных `pools[].entries[]`, а также родительские `type=loot_table` с точным локальным путём к таким таблицам (транзитивно, с добавлением `.json`). Это декларации, не подтверждение вызова или регистрации; внешние таблицы, команды, события, структуры, торговля и другие способы получения не заменяются этим указателем.

Для каждого пула сохранены все поля пула и таблицы вне списков, соседние записи с весами, quality и conditions, а интересующие записи — целиком, включая функции. Отсутствующее поле не заполняется предполагаемым значением. Для полных исходных данных соседних записей см. [реестр мира 2.8.14](world-ledger-2.8.14.md) и [2.8.8](world-ledger-2.8.8.md). Иные и нестандартные вложенные схемы не индексируются. Значения rolls, count и веса — сырой формат: они не доказывают вероятность успешного получения, а пустые результаты, условия, удача и механика движка могут иметь значение.

[Условная модель выбора записей](loot-selection-model.md) показывает арифметику внутри уже активированного пула и явно не является вероятностью выпадения.

## Диагностика

- 1.6: 0 таблиц, ошибки: нет; повторные ключи: нет.
- 2.8.8: 60 таблиц, ошибки: нет; повторные ключи: нет.
- 2.8.14: 60 таблиц, ошибки: нет; повторные ключи: нет.

Сравнение JSON таблиц 2.8.8/2.8.14: структурно равны; условия вызова таблиц за их пределами могут отличаться.

## 1.6

Таблиц: 0; прямых записей: 0; родительских записей: 0.

## 2.8.8 и 2.8.14

Таблиц: 60; прямых записей: 29; родительских записей: 2.

### `Swords_B/loot_tables/bee_sword.json` — `$.pools[0]`

- Поля таблицы, кроме pools: `{}`
- Поля пула, кроме entries: `{"rolls":1}`
- Все записи в исходном порядке (type/name/weight/quality/conditions): `[{"type":"item","name":"effect:bee_sword","weight":1}]`
- `entries[0]`, локальный ID — полный объект: `{"type":"item","name":"effect:bee_sword","weight":1}`

### `Swords_B/loot_tables/blocks/quartz_diamond_block.json` — `$.pools[0]`

- Поля таблицы, кроме pools: `{}`
- Поля пула, кроме entries: `{"rolls":1}`
- Все записи в исходном порядке (type/name/weight/quality/conditions): `[{"type":"item","name":"effect99:quartz_diamond_block","weight":1}]`
- `entries[0]`, локальный ID — полный объект: `{"type":"item","name":"effect99:quartz_diamond_block","weight":1,"functions":[{"function":"set_count","count":{"min":1,"max":1}}]}`

### `Swords_B/loot_tables/blocks/quartz_diamond_ore.json` — `$.pools[0]`

- Поля таблицы, кроме pools: `{}`
- Поля пула, кроме entries: `{"rolls":1}`
- Все записи в исходном порядке (type/name/weight/quality/conditions): `[{"type":"item","name":"effect:quartz_diamond","weight":89},{"type":"item","name":"effect:quartz_diamond","weight":10},{"type":"item","name":"effect:quartz_diamond","weight":1}]`
- `entries[0]`, локальный ID — полный объект: `{"type":"item","name":"effect:quartz_diamond","weight":89,"functions":[{"function":"set_count","count":{"min":1,"max":1}}]}`
- `entries[1]`, локальный ID — полный объект: `{"type":"item","name":"effect:quartz_diamond","weight":10,"functions":[{"function":"set_count","count":{"min":1,"max":2}}]}`
- `entries[2]`, локальный ID — полный объект: `{"type":"item","name":"effect:quartz_diamond","weight":1,"functions":[{"function":"set_count","count":{"min":2,"max":4}}]}`

### `Swords_B/loot_tables/blocks/silver_ore.json` — `$.pools[0]`

- Поля таблицы, кроме pools: `{}`
- Поля пула, кроме entries: `{"rolls":1}`
- Все записи в исходном порядке (type/name/weight/quality/conditions): `[{"type":"item","name":"effect99:silver_ore","weight":1}]`
- `entries[0]`, локальный ID — полный объект: `{"type":"item","name":"effect99:silver_ore","weight":1,"functions":[{"function":"set_count","count":{"min":1,"max":1}}]}`

### `Swords_B/loot_tables/chests/abandoned_mineshaft.json` — `$.pools[1]`

- Поля таблицы, кроме pools: `{}`
- Поля пула, кроме entries: `{"rolls":{"min":2,"max":4}}`
- Все записи в исходном порядке (type/name/weight/quality/conditions): `[{"type":"item","name":"minecraft:iron_ingot","weight":10},{"type":"item","name":"minecraft:gold_ingot","weight":5},{"type":"item","name":"minecraft:redstone","weight":5},{"type":"item","name":"minecraft:dye","weight":5},{"type":"item","name":"minecraft:diamond","weight":3},{"type":"item","name":"effect:spider_sword","weight":3},{"type":"item","name":"minecraft:coal","weight":10},{"type":"item","name":"minecraft:bread","weight":15},{"type":"item","name":"minecraft:melon_seeds","weight":10},{"type":"item","name":"minecraft:pumpkin_seeds","weight":10},{"type":"item","name":"minecraft:beetroot_seeds","weight":10}]`
- `entries[5]`, локальный ID — полный объект: `{"type":"item","name":"effect:spider_sword","functions":[{"function":"set_count","count":{"min":1,"max":1}}],"weight":3}`

### `Swords_B/loot_tables/chests/buriedtreasure.json` — `$.pools[1]`

- Поля таблицы, кроме pools: `{}`
- Поля пула, кроме entries: `{"rolls":{"min":5,"max":12}}`
- Все записи в исходном порядке (type/name/weight/quality/conditions): `[{"type":"item","name":"minecraft:prismarine_crystals","weight":5},{"type":"item","name":"minecraft:iron_ingot","weight":20},{"type":"item","name":"minecraft:gold_ingot","weight":10},{"type":"item","name":"minecraft:tnt","weight":10},{"type":"item","name":"minecraft:diamond","weight":15},{"type":"item","name":"minecraft:record_wait","weight":5},{"type":"item","name":"minecraft:record_mellohi","weight":5},{"type":"item","name":"minecraft:name_tag","weight":10},{"type":"item","name":"effect:sea_sword","weight":15},{"type":"item","name":"minecraft:chainmail_chestplate","weight":20},{"type":"item","name":"minecraft:chainmail_helmet","weight":20},{"type":"item","name":"minecraft:chainmail_leggings","weight":20},{"type":"item","name":"minecraft:chainmail_boots","weight":20},{"type":"item","name":"minecraft:writable_book","weight":5},{"type":"item","name":"minecraft:lead","weight":10},{"type":"item","name":"minecraft:experience_bottle","weight":3},{"type":"item","name":"minecraft:potion","weight":15},{"type":"item","name":"minecraft:potion","weight":10},{"type":"item","name":"minecraft:cake","weight":1}]`
- `entries[8]`, локальный ID — полный объект: `{"type":"item","name":"effect:sea_sword","weight":15}`

### `Swords_B/loot_tables/chests/desert_pyramid.json` — `$.pools[0]`

- Поля таблицы, кроме pools: `{}`
- Поля пула, кроме entries: `{"rolls":{"min":2,"max":4}}`
- Все записи в исходном порядке (type/name/weight/quality/conditions): `[{"type":"item","name":"minecraft:diamond","weight":5},{"type":"item","name":"minecraft:iron_ingot","weight":15},{"type":"item","name":"minecraft:gold_ingot","weight":15},{"type":"item","name":"minecraft:emerald","weight":15},{"type":"item","name":"minecraft:bone","weight":25},{"type":"item","name":"minecraft:spider_eye","weight":25},{"type":"item","name":"minecraft:rotten_flesh","weight":25},{"type":"item","name":"minecraft:saddle","weight":20},{"type":"item","name":"effect:tnt_sword","weight":10},{"type":"item","name":"minecraft:horsearmoriron","weight":15},{"type":"item","name":"minecraft:horsearmorgold","weight":10},{"type":"item","name":"minecraft:horsearmordiamond","weight":5},{"type":"item","name":"minecraft:book","weight":20},{"type":"item","name":"minecraft:golden_apple","weight":20},{"type":"item","name":"minecraft:appleEnchanted","weight":2},{"type":"empty","weight":15}]`
- `entries[8]`, локальный ID — полный объект: `{"type":"item","name":"effect:tnt_sword","weight":10}`

### `Swords_B/loot_tables/chests/igloo_chest.json` — `$.pools[0]`

- Поля таблицы, кроме pools: `{}`
- Поля пула, кроме entries: `{"rolls":{"min":2,"max":8}}`
- Все записи в исходном порядке (type/name/weight/quality/conditions): `[{"type":"item","name":"minecraft:apple","weight":15},{"type":"item","name":"minecraft:coal","weight":15},{"type":"item","name":"minecraft:gold_nugget","weight":10},{"type":"item","name":"minecraft:stone_axe","weight":2},{"type":"item","name":"minecraft:rotten_flesh","weight":10},{"type":"item","name":"minecraft:emerald","weight":1},{"type":"item","name":"effect:ice_sword","weight":1},{"type":"item","name":"minecraft:wheat","weight":10}]`
- `entries[6]`, локальный ID — полный объект: `{"type":"item","name":"effect:ice_sword","weight":1}`

### `Swords_B/loot_tables/chests/jungle_temple.json` — `$.pools[0]`

- Поля таблицы, кроме pools: `{}`
- Поля пула, кроме entries: `{"rolls":{"min":2,"max":6}}`
- Все записи в исходном порядке (type/name/weight/quality/conditions): `[{"type":"item","name":"minecraft:diamond","weight":15},{"type":"item","name":"minecraft:iron_ingot","weight":50},{"type":"item","name":"minecraft:gold_ingot","weight":75},{"type":"item","name":"minecraft:emerald","weight":10},{"type":"item","name":"minecraft:bone","weight":100},{"type":"item","name":"minecraft:rotten_flesh","weight":80},{"type":"item","name":"minecraft:bamboo","weight":75},{"type":"item","name":"minecraft:saddle","weight":15},{"type":"item","name":"effect:jungle_sword","weight":16},{"type":"item","name":"minecraft:horsearmoriron","weight":5},{"type":"item","name":"minecraft:horsearmorgold","weight":5},{"type":"item","name":"minecraft:horsearmordiamond","weight":5},{"type":"item","name":"minecraft:book","weight":6}]`
- `entries[8]`, локальный ID — полный объект: `{"type":"item","name":"effect:jungle_sword","weight":16}`

### `Swords_B/loot_tables/chests/pillager_outpost.json` — `$.pools[3]`

- Поля таблицы, кроме pools: `{}`
- Поля пула, кроме entries: `{"rolls":{"min":2,"max":3}}`
- Все записи в исходном порядке (type/name/weight/quality/conditions): `[{"type":"item","weight":7,"name":"minecraft:experience_bottle"},{"type":"item","weight":4,"name":"minecraft:string"},{"type":"item","weight":4,"name":"minecraft:arrow"},{"type":"item","weight":3,"name":"minecraft:tripwire_hook"},{"type":"item","weight":3,"name":"minecraft:iron_ingot"},{"type":"item","weight":3,"name":"effect:emerald_sword"},{"type":"item","weight":3,"name":"effect:lapis_sword"},{"type":"item","name":"minecraft:book"}]`
- `entries[5]`, локальный ID — полный объект: `{"type":"item","weight":3,"functions":[{"function":"set_count","count":{"min":0,"max":1}}],"name":"effect:emerald_sword"}`
- `entries[6]`, локальный ID — полный объект: `{"type":"item","weight":3,"functions":[{"function":"set_count","count":{"min":0,"max":1}}],"name":"effect:lapis_sword"}`

### `Swords_B/loot_tables/chests/spawn_bonus_chest.json` — `$.pools[0]`

- Поля таблицы, кроме pools: `{}`
- Поля пула, кроме entries: `{"rolls":1}`
- Все записи в исходном порядке (type/name/weight/quality/conditions): `[{"type":"item","name":"effect:coal_sword","weight":1},{"type":"item","name":"minecraft:stone_axe","weight":1},{"type":"item","name":"minecraft:wooden_axe","weight":3}]`
- `entries[0]`, локальный ID — полный объект: `{"type":"item","name":"effect:coal_sword","weight":1}`

### `Swords_B/loot_tables/chests/stronghold_corridor.json` — `$.pools[0]`

- Поля таблицы, кроме pools: `{}`
- Поля пула, кроме entries: `{"rolls":{"min":2,"max":3}}`
- Все записи в исходном порядке (type/name/weight/quality/conditions): `[{"type":"item","name":"minecraft:ender_pearl","weight":50},{"type":"item","name":"minecraft:emerald","weight":15},{"type":"item","name":"minecraft:diamond","weight":15},{"type":"item","name":"minecraft:iron_ingot","weight":50},{"type":"item","name":"minecraft:gold_ingot","weight":25},{"type":"item","name":"minecraft:redstone","weight":25},{"type":"item","name":"minecraft:bread","weight":75},{"type":"item","name":"minecraft:apple","weight":75},{"type":"item","name":"minecraft:iron_pickaxe","weight":25},{"type":"item","name":"minecraft:iron_sword","weight":25},{"type":"item","name":"minecraft:iron_chestplate","weight":25},{"type":"item","name":"minecraft:iron_helmet","weight":25},{"type":"item","name":"minecraft:iron_leggings","weight":25},{"type":"item","name":"minecraft:iron_boots","weight":25},{"type":"item","name":"minecraft:golden_apple","weight":5},{"type":"item","name":"minecraft:saddle","weight":5},{"type":"item","name":"effect:emerald_sword","weight":5},{"type":"item","name":"effect:lapis_sword","weight":5},{"type":"item","name":"minecraft:horsearmoriron","weight":5},{"type":"item","name":"minecraft:horsearmorgold","weight":5},{"type":"item","name":"minecraft:horsearmordiamond","weight":5},{"type":"item","name":"minecraft:book","weight":6}]`
- `entries[16]`, локальный ID — полный объект: `{"type":"item","name":"effect:emerald_sword","weight":5}`
- `entries[17]`, локальный ID — полный объект: `{"type":"item","name":"effect:lapis_sword","weight":5}`

### `Swords_B/loot_tables/chests/stronghold_library.json` — `$.pools[0]`

- Поля таблицы, кроме pools: `{}`
- Поля пула, кроме entries: `{"rolls":{"min":2,"max":10}}`
- Все записи в исходном порядке (type/name/weight/quality/conditions): `[{"type":"item","name":"minecraft:book","weight":100},{"type":"item","name":"minecraft:paper","weight":100},{"type":"item","name":"minecraft:map","weight":5},{"type":"item","name":"effect:lapis_sword","weight":5},{"type":"item","name":"minecraft:compass","weight":5},{"type":"item","name":"minecraft:book","weight":60}]`
- `entries[3]`, локальный ID — полный объект: `{"type":"item","name":"effect:lapis_sword","weight":5}`

### `Swords_B/loot_tables/chests/underwater_ruin_big.json` — `$.pools[1]`

- Поля таблицы, кроме pools: `{}`
- Поля пула, кроме entries: `{"rolls":1}`
- Все записи в исходном порядке (type/name/weight/quality/conditions): `[{"type":"item","name":"minecraft:golden_apple","weight":1},{"type":"item","name":"effect:magma_sword","weight":1},{"type":"item","name":"minecraft:book","weight":5},{"type":"item","name":"minecraft:leather_chestplate","weight":1},{"type":"item","name":"minecraft:golden_helmet","weight":1},{"type":"item","name":"minecraft:fishing_rod","weight":5},{"type":"item","name":"minecraft:map","weight":10}]`
- `entries[1]`, локальный ID — полный объект: `{"type":"item","name":"effect:magma_sword","weight":1}`

### `Swords_B/loot_tables/chests/village/village_snowy_house.json` — `$.pools[0]`

- Поля таблицы, кроме pools: `{"type":"minecraft:chest"}`
- Поля пула, кроме entries: `{"rolls":{"min":3,"max":8}}`
- Все записи в исходном порядке (type/name/weight/quality/conditions): `[{"type":"item","name":"minecraft:blue_ice"},{"type":"item","weight":4,"name":"minecraft:snow"},{"type":"item","weight":10,"name":"minecraft:potato"},{"type":"item","weight":10,"name":"minecraft:bread"},{"type":"item","weight":10,"name":"minecraft:beetroot_seeds"},{"type":"item","name":"minecraft:beetroot_soup"},{"type":"item","name":"minecraft:furnace"},{"type":"item","name":"minecraft:emerald"},{"type":"item","weight":10,"name":"minecraft:snowball"},{"type":"item","weight":4,"name":"effect:ice_sword"},{"type":"item","weight":5,"name":"minecraft:coal"}]`
- `entries[9]`, локальный ID — полный объект: `{"type":"item","weight":4,"functions":[{"function":"minecraft:set_count","count":{"min":1,"max":1}}],"name":"effect:ice_sword"}`

### `Swords_B/loot_tables/chests/woodland_mansion.json` — `$.pools[0]`

- Поля таблицы, кроме pools: `{}`
- Поля пула, кроме entries: `{"rolls":{"min":1,"max":3}}`
- Все записи в исходном порядке (type/name/weight/quality/conditions): `[{"type":"item","name":"minecraft:lead","weight":100},{"type":"item","name":"minecraft:golden_apple","weight":75},{"type":"item","name":"minecraft:appleEnchanted","weight":10},{"type":"item","name":"minecraft:record_13","weight":75},{"type":"item","name":"minecraft:record_cat","weight":75},{"type":"item","name":"minecraft:name_tag","weight":100},{"type":"item","name":"minecraft:chainmail_chestplate","weight":50},{"type":"item","name":"minecraft:diamond_hoe","weight":75},{"type":"item","name":"minecraft:diamond_chestplate","weight":25},{"type":"item","name":"effect:emerald_sword","weight":25},{"type":"item","name":"minecraft:book","weight":60}]`
- `entries[9]`, локальный ID — полный объект: `{"type":"item","name":"effect:emerald_sword","weight":25}`

### `Swords_B/loot_tables/entities/blaze.json` — `$.pools[1]`

- Поля таблицы, кроме pools: `{}`
- Поля пула, кроме entries: `{"conditions":[{"condition":"killed_by_entity","entity_type":"minecraft:snow_golem"},{"condition":"random_chance_with_looting","chance":0.025,"looting_multiplier":0.02}],"rolls":1}`
- Все записи в исходном порядке (type/name/weight/quality/conditions): `[{"type":"item","name":"effect:blaze_sword","weight":1}]`
- `entries[0]`, локальный ID — полный объект: `{"type":"item","name":"effect:blaze_sword","weight":1,"functions":[{"function":"set_data","data":0}]}`

### `Swords_B/loot_tables/entities/elder_guardian.json` — `$.pools[1]`

- Поля таблицы, кроме pools: `{}`
- Поля пула, кроме entries: `{"conditions":[{"condition":"killed_by_player"},{"condition":"random_chance_with_looting","chance":0.065,"looting_multiplier":0.02}],"rolls":1}`
- Все записи в исходном порядке (type/name/weight/quality/conditions): `[{"type":"item","name":"effect:sponge_sword","weight":1}]`
- `entries[0]`, локальный ID — полный объект: `{"type":"item","name":"effect:sponge_sword","weight":1,"functions":[{"function":"set_count","count":{"min":1,"max":1}},{"function":"set_data","data":0}]}`

### `Swords_B/loot_tables/entities/living_flame.json` — `$.pools[0]`

- Поля таблицы, кроме pools: `{}`
- Поля пула, кроме entries: `{"rolls":1}`
- Все записи в исходном порядке (type/name/weight/quality/conditions): `[{"type":"item","name":"effect:fire_sword","weight":1}]`
- `entries[0]`, локальный ID — полный объект: `{"type":"item","name":"effect:fire_sword","weight":1,"functions":[{"function":"set_data","data":0}]}`

### `Swords_B/loot_tables/entities/red_enderman.json` — `$.pools[0]`

- Поля таблицы, кроме pools: `{}`
- Поля пула, кроме entries: `{"conditions":[{"condition":"killed_by_player"},{"condition":"random_chance_with_looting","chance":0.025,"looting_multiplier":0.02}],"rolls":1}`
- Все записи в исходном порядке (type/name/weight/quality/conditions): `[{"type":"item","name":"effect:ender_sword","weight":1}]`
- `entries[0]`, локальный ID — полный объект: `{"type":"item","name":"effect:ender_sword","weight":1,"functions":[{"function":"set_data","data":0}]}`

### `Swords_B/loot_tables/entities/shulker.json` — `$.pools[1]`

- Поля таблицы, кроме pools: `{}`
- Поля пула, кроме entries: `{"conditions":[{"condition":"killed_by_player"},{"condition":"random_chance_with_looting","chance":0.045,"looting_multiplier":0.02}],"rolls":1}`
- Все записи в исходном порядке (type/name/weight/quality/conditions): `[{"type":"item","name":"effect:shulker_sword","weight":1}]`
- `entries[0]`, локальный ID — полный объект: `{"type":"item","name":"effect:shulker_sword","weight":1,"functions":[{"function":"set_count","count":{"min":1,"max":1}},{"function":"set_data","data":0}]}`

### `Swords_B/loot_tables/entities/slime_king.json` — `$.pools[0]`

- Поля таблицы, кроме pools: `{}`
- Поля пула, кроме entries: `{"conditions":[{"condition":"killed_by_player"},{"condition":"random_chance_with_looting","chance":0.04,"looting_multiplier":0.02}],"rolls":1}`
- Все записи в исходном порядке (type/name/weight/quality/conditions): `[{"type":"item","name":"effect:slime_sword","weight":1}]`
- `entries[0]`, локальный ID — полный объект: `{"type":"item","name":"effect:slime_sword","weight":1,"functions":[{"function":"set_data","data":0}]}`

### `Swords_B/loot_tables/entities/wither_skeleton.json` — `$.pools[3]`

- Поля таблицы, кроме pools: `{}`
- Поля пула, кроме entries: `{"conditions":[{"condition":"killed_by_player"},{"condition":"random_chance_with_looting","chance":0.025,"looting_multiplier":0.02}],"rolls":1}`
- Все записи в исходном порядке (type/name/weight/quality/conditions): `[{"type":"item","name":"effect:wither_skeleton_sword","weight":1}]`
- `entries[0]`, локальный ID — полный объект: `{"type":"item","name":"effect:wither_skeleton_sword","weight":1,"functions":[{"function":"set_data","data":0}]}`

### `Swords_B/loot_tables/gameplay/fishing.json` — `$.pools[0]`

- Поля таблицы, кроме pools: `{}`
- Поля пула, кроме entries: `{"rolls":1}`
- Все записи в исходном порядке (type/name/weight/quality/conditions): `[{"type":"loot_table","name":"loot_tables/gameplay/fishing/junk.json","weight":10,"quality":-2},{"type":"loot_table","name":"loot_tables/gameplay/fishing/treasure.json","weight":5,"quality":2},{"type":"loot_table","name":"loot_tables/gameplay/fishing/fish.json","weight":85,"quality":-1}]`
- `entries[1]`, родительская таблица — полный объект: `{"type":"loot_table","name":"loot_tables/gameplay/fishing/treasure.json","weight":5,"quality":2}`

### `Swords_B/loot_tables/gameplay/fishing/treasure.json` — `$.pools[0]`

- Поля таблицы, кроме pools: `{}`
- Поля пула, кроме entries: `{"rolls":1}`
- Все записи в исходном порядке (type/name/weight/quality/conditions): `[{"type":"item","name":"minecraft:nautilus_shell","weight":5},{"type":"item","name":"minecraft:waterlily","weight":5},{"type":"item","name":"minecraft:name_tag","weight":5},{"type":"item","name":"minecraft:saddle","weight":5},{"type":"item","name":"effect:jungle_sword","weight":5},{"type":"item","name":"minecraft:bow","weight":5},{"type":"item","name":"minecraft:fishing_rod","weight":5},{"type":"item","name":"minecraft:book","weight":6}]`
- `entries[4]`, локальный ID — полный объект: `{"type":"item","name":"effect:jungle_sword","weight":5}`

### `Swords_B/loot_tables/gameplay/jungle_fishing.json` — `$.pools[0]`

- Поля таблицы, кроме pools: `{}`
- Поля пула, кроме entries: `{"rolls":1}`
- Все записи в исходном порядке (type/name/weight/quality/conditions): `[{"type":"loot_table","name":"loot_tables/gameplay/fishing/jungle_junk.json","weight":10,"quality":-2},{"type":"loot_table","name":"loot_tables/gameplay/fishing/treasure.json","weight":5,"quality":2},{"type":"loot_table","name":"loot_tables/gameplay/fishing/jungle_fish.json","weight":85,"quality":-1}]`
- `entries[1]`, родительская таблица — полный объект: `{"type":"loot_table","name":"loot_tables/gameplay/fishing/treasure.json","weight":5,"quality":2}`

### `Swords_B/loot_tables/pumpkin_sword.json` — `$.pools[0]`

- Поля таблицы, кроме pools: `{}`
- Поля пула, кроме entries: `{"rolls":1}`
- Все записи в исходном порядке (type/name/weight/quality/conditions): `[{"type":"item","name":"effect:cursed_pumpkin_sword","weight":1}]`
- `entries[0]`, локальный ID — полный объект: `{"type":"item","name":"effect:cursed_pumpkin_sword","weight":1}`

