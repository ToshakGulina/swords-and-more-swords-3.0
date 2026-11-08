# Объявленные пути получения — архив 2.8.14

Автоматический указатель буквальных результатов рецептов (включая furnace output), записей type=item таблиц добычи, родителей вложенных loot_table, сделок с предметом в gives и NBT-полей Name структур. Это перечень деклараций, а не доказательство получения предмета. Внешние/ванильные пути, генерация, команды, скрипты, другие таблицы обмена и события могут дать предмет другими способами. Запись в структуре может быть в стойке для брони или хранилище, а не дропом. Таблица может не вызываться. Семантика, регистрация, правильность синтаксиса и чувствительность ID к регистру требуют проверки движка.

Родительские цепочки строятся только по точным текстовым путям loot_table с добавлением `.json` при её отсутствии. Циклы обозначаются явно; внешняя таблица не анализируется. Показаны полные объекты записей, но для вычисления вероятностей дополнительно нужны полные пулы, rolls, условия, функции и quality — см. [реестр мира](world-ledger-2.8.14.md). Веса не объявляются шансами.

## Диагностика чтения

- Ошибок разбора в обработанных категориях не обнаружено.

## Все рецепты и диагностика шаблонов

### `Swords_B/recipes/bedrock_stick.json` — `minecraft:recipe_shaped`

- Полное определение: `{"description":{"identifier":"effect:bedrock_stick"},"tags":["crafting_table"],"pattern":["#","#"],"key":{"#":{"item":"minecraft:bedrock"}},"result":{"item":"effect:bedrock_stick"}}`
- Символы pattern без key: `[]`; ключи не использованы в pattern: `[]`. Интерпретация символов и валидность — на проверку движка.

### `Swords_B/recipes/bedrock_sword.json` — `minecraft:recipe_shaped`

- Полное определение: `{"description":{"identifier":"effect:bedrock_sword"},"tags":["crafting_table"],"pattern":["B","B","#"],"key":{"#":{"item":"effect:bedrock_stick"},"B":{"item":"minecraft:bedrock"}},"result":{"item":"effect:bedrock_sword"}}`
- Символы pattern без key: `[]`; ключи не использованы в pattern: `[]`. Интерпретация символов и валидность — на проверку движка.

### `Swords_B/recipes/cactus_sword.json` — `minecraft:recipe_shaped`

- Полное определение: `{"description":{"identifier":"effect:cactus_sword"},"tags":["crafting_table"],"pattern":["F","F","E"],"key":{"E":{"item":"minecraft:stick"},"F":{"item":"minecraft:cactus"}},"result":{"item":"effect:cactus_sword"}}`
- Символы pattern без key: `[]`; ключи не использованы в pattern: `[]`. Интерпретация символов и валидность — на проверку движка.

### `Swords_B/recipes/clock_sword.json` — `minecraft:recipe_shaped`

- Полное определение: `{"description":{"identifier":"effect:clock_sword"},"tags":["crafting_table"],"pattern":["X##","#C#","I#X"],"key":{"#":{"item":"minecraft:gold_block"},"C":{"item":"minecraft:clock"},"I":{"item":"minecraft:gold_ingot"}},"result":{"item":"effect:clock_sword"}}`
- Символы pattern без key: `["X"]`; ключи не использованы в pattern: `[]`. Интерпретация символов и валидность — на проверку движка.

### `Swords_B/recipes/coal_sword.json` — `minecraft:recipe_shaped`

- Полное определение: `{"description":{"identifier":"effect:coal_sword"},"tags":["crafting_table"],"pattern":["2","2","1"],"key":{"2":{"item":"minecraft:coal_block"},"1":{"item":"minecraft:stick"}},"result":{"item":"effect:coal_sword"}}`
- Символы pattern без key: `[]`; ключи не использованы в pattern: `[]`. Интерпретация символов и валидность — на проверку движка.

### `Swords_B/recipes/fire_sword.json` — `minecraft:recipe_shaped`

- Полное определение: `{"description":{"identifier":"effect:fire_sword"},"tags":["crafting_table"],"pattern":["F","F","#"],"key":{"#":{"item":"minecraft:blaze_rod"},"F":{"item":"minecraft:fire"}},"result":{"item":"effect:fire_sword"}}`
- Символы pattern без key: `[]`; ключи не использованы в pattern: `[]`. Интерпретация символов и валидность — на проверку движка.

### `Swords_B/recipes/glowstone_sword.json` — `minecraft:recipe_shaped`

- Полное определение: `{"description":{"identifier":"effect:glowstone_sword"},"tags":["crafting_table"],"pattern":["2","2","1"],"key":{"1":{"item":"minecraft:blaze_rod"},"2":{"item":"minecraft:glowstone"}},"result":{"item":"effect:glowstone_sword"}}`
- Символы pattern без key: `[]`; ключи не использованы в pattern: `[]`. Интерпретация символов и валидность — на проверку движка.

### `Swords_B/recipes/nether_star_sword.json` — `minecraft:recipe_shapeless`

- Полное определение: `{"description":{"identifier":"effect:nether_star_sword"},"tags":["crafting_table"],"ingredients":[{"item":"minecraft:nether_star","data":0},{"item":"minecraft:diamond_sword","data":0}],"result":{"item":"effect:nether_star_sword","count":1}}`

### `Swords_B/recipes/quartz_diamond_block.json` — `minecraft:recipe_shaped`

- Полное определение: `{"description":{"identifier":"effect99:quartz_diamond_block"},"tags":["crafting_table"],"pattern":["###","###","###"],"key":{"#":{"item":"effect:quartz_diamond"}},"result":{"item":"effect99:quartz_diamond_block"}}`
- Символы pattern без key: `[]`; ключи не использованы в pattern: `[]`. Интерпретация символов и валидность — на проверку движка.

### `Swords_B/recipes/quartz_diamond_stick.json` — `minecraft:recipe_shaped`

- Полное определение: `{"description":{"identifier":"effect:quartz_diamond_stick"},"tags":["crafting_table"],"pattern":["#","#"],"key":{"#":{"item":"effect:quartz_diamond"}},"result":{"item":"effect:quartz_diamond_stick"}}`
- Символы pattern без key: `[]`; ключи не использованы в pattern: `[]`. Интерпретация символов и валидность — на проверку движка.

### `Swords_B/recipes/quartz_diamond_sword.json` — `minecraft:recipe_shaped`

- Полное определение: `{"description":{"identifier":"effect:quartz_sword"},"tags":["crafting_table"],"pattern":["Q","Q","#"],"key":{"#":{"item":"effect:quartz_diamond_stick","data":0},"Q":{"item":"effect99:quartz_diamond_block"}},"result":{"item":"effect:quartz_sword"}}`
- Символы pattern без key: `[]`; ключи не использованы в pattern: `[]`. Интерпретация символов и валидность — на проверку движка.

### `Swords_B/recipes/silver_ingot.json` — `minecraft:recipe_furnace`

- Полное определение: `{"description":{"identifier":"effect:silver_ingot"},"tags":["furnace","blast_furnace"],"input":"effect99:silver_ore","output":"effect:silver_ingot"}`

### `Swords_B/recipes/silver_sword.json` — `minecraft:recipe_shaped`

- Полное определение: `{"description":{"identifier":"effect:silver_sword"},"tags":["crafting_table"],"pattern":["2","2","1"],"key":{"2":{"item":"effect:silver_ingot"},"1":{"item":"minecraft:stick"}},"result":{"item":"effect:silver_sword"}}`
- Символы pattern без key: `[]`; ключи не использованы в pattern: `[]`. Интерпретация символов и валидность — на проверку движка.

### `Swords_B/recipes/wet_sponge_sword.json` — `minecraft:recipe_furnace`

- Полное определение: `{"description":{"identifier":"effect:wet_sponge_sword"},"tags":["furnace","blast_furnace"],"input":"effect:wet_sponge_sword","output":"effect:sponge_sword"}`

## Все записи type=loot_table и локальное разрешение

- `Swords_B/loot_tables/entities/elder_guardian.json` $.pools[4].entries[0] → `Swords_B/loot_tables/gameplay/fishing/fish.json` (локальный файл найден): `{"type":"loot_table","name":"loot_tables/gameplay/fishing/fish","weight":1}`
- `Swords_B/loot_tables/gameplay/fishing.json` $.pools[0].entries[2] → `Swords_B/loot_tables/gameplay/fishing/fish.json` (локальный файл найден): `{"type":"loot_table","name":"loot_tables/gameplay/fishing/fish.json","weight":85,"quality":-1}`
- `Swords_B/loot_tables/gameplay/jungle_fishing.json` $.pools[0].entries[2] → `Swords_B/loot_tables/gameplay/fishing/jungle_fish.json` (локальный файл найден): `{"type":"loot_table","name":"loot_tables/gameplay/fishing/jungle_fish.json","weight":85,"quality":-1}`
- `Swords_B/loot_tables/gameplay/jungle_fishing.json` $.pools[0].entries[0] → `Swords_B/loot_tables/gameplay/fishing/jungle_junk.json` (локальный файл найден): `{"type":"loot_table","name":"loot_tables/gameplay/fishing/jungle_junk.json","weight":10,"quality":-2}`
- `Swords_B/loot_tables/gameplay/fishing.json` $.pools[0].entries[0] → `Swords_B/loot_tables/gameplay/fishing/junk.json` (локальный файл найден): `{"type":"loot_table","name":"loot_tables/gameplay/fishing/junk.json","weight":10,"quality":-2}`
- `Swords_B/loot_tables/gameplay/fishing.json` $.pools[0].entries[1] → `Swords_B/loot_tables/gameplay/fishing/treasure.json` (локальный файл найден): `{"type":"loot_table","name":"loot_tables/gameplay/fishing/treasure.json","weight":5,"quality":2}`
- `Swords_B/loot_tables/gameplay/jungle_fishing.json` $.pools[0].entries[1] → `Swords_B/loot_tables/gameplay/fishing/treasure.json` (локальный файл найден): `{"type":"loot_table","name":"loot_tables/gameplay/fishing/treasure.json","weight":5,"quality":2}`

## По предметам

### `effect:bedrock_stick`

- Определение: `Swords_B/items/bedrock_stick.json`.
- Результаты рецептов: `Swords_B/recipes/bedrock_stick.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

### `effect:bedrock_sword`

- Определение: `Swords_B/items/bedrock_sword.json`.
- Результаты рецептов: `Swords_B/recipes/bedrock_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[35].Mainhand[0].Name
  - `Swords_B/structures/bedrock_sword.mcstructure` $.entities[0].Item.Name

### `effect:bee_sword`

- Определение: `Swords_B/items/bee_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - `Swords_B/loot_tables/bee_sword.json` $.pools[0].entries[0]: `{"type":"item","name":"effect:bee_sword","weight":1}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

### `effect:blaze_sword`

- Определение: `Swords_B/items/blaze_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - `Swords_B/loot_tables/entities/blaze.json` $.pools[1].entries[0]: `{"type":"item","name":"effect:blaze_sword","weight":1,"functions":[{"function":"set_data","data":0}]}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[16].Mainhand[0].Name

### `effect:bone_sword`

- Определение: `Swords_B/items/bone_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[13].Mainhand[0].Name
  - `Swords_B/structures/bone_sword.mcstructure` $.entities[0].Item.Name

### `effect:cactus_sword`

- Определение: `Swords_B/items/cactus_sword.json`.
- Результаты рецептов: `Swords_B/recipes/cactus_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[24].Mainhand[0].Name

### `effect:clock_sword`

- Определение: `Swords_B/items/clock_sword.json`.
- Результаты рецептов: `Swords_B/recipes/clock_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[34].Mainhand[0].Name

### `effect:coal_sword`

- Определение: `Swords_B/items/coal_sword.json`.
- Результаты рецептов: `Swords_B/recipes/coal_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - `Swords_B/loot_tables/chests/spawn_bonus_chest.json` $.pools[0].entries[0]: `{"type":"item","name":"effect:coal_sword","weight":1}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[19].Mainhand[0].Name

### `effect:creeper_sword`

- Определение: `Swords_B/items/creeper_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[17].Mainhand[0].Name
  - `Swords_B/structures/creeper_sword.mcstructure` $.entities[0].Item.Name

### `effect:cursed_pumpkin_sword`

- Определение: `Swords_B/items/pumpkin_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - `Swords_B/loot_tables/pumpkin_sword.json` $.pools[0].entries[0]: `{"type":"item","name":"effect:cursed_pumpkin_sword","weight":1}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

### `effect:emerald_sword`

- Определение: `Swords_B/items/emerald_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - `Swords_B/loot_tables/chests/pillager_outpost.json` $.pools[3].entries[5]: `{"type":"item","weight":3,"functions":[{"function":"set_count","count":{"min":0,"max":1}}],"name":"effect:emerald_sword"}`
  - `Swords_B/loot_tables/chests/stronghold_corridor.json` $.pools[0].entries[16]: `{"type":"item","name":"effect:emerald_sword","weight":5}`
  - `Swords_B/loot_tables/chests/woodland_mansion.json` $.pools[0].entries[9]: `{"type":"item","name":"effect:emerald_sword","weight":25}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[14].Mainhand[0].Name

### `effect:ender_sword`

- Определение: `Swords_B/items/ender_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - `Swords_B/loot_tables/entities/red_enderman.json` $.pools[0].entries[0]: `{"type":"item","name":"effect:ender_sword","weight":1,"functions":[{"function":"set_data","data":0}]}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[7].Mainhand[0].Name

### `effect:fire_sword`

- Определение: `Swords_B/items/fire_sword.json`.
- Результаты рецептов: `Swords_B/recipes/fire_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - `Swords_B/loot_tables/entities/living_flame.json` $.pools[0].entries[0]: `{"type":"item","name":"effect:fire_sword","weight":1,"functions":[{"function":"set_data","data":0}]}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[15].Mainhand[0].Name
  - `Swords_B/structures/fire_sword.mcstructure` $.entities[0].Item.Name

### `effect:ghost_sword`

- Определение: `Swords_B/items/ghost_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[33].Mainhand[0].Name
  - `Swords_B/structures/ghost_sword.mcstructure` $.entities[0].Item.Name

### `effect:glass_sword`

- Определение: `Swords_B/items/glass_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[29].Mainhand[0].Name
  - `Swords_B/structures/glass_sword.mcstructure` $.entities[0].Item.Name

### `effect:glowstone_sword`

- Определение: `Swords_B/items/glowstone_sword.json`.
- Результаты рецептов: `Swords_B/recipes/glowstone_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[10].Mainhand[0].Name

### `effect:grass_sword`

- Определение: `Swords_B/items/grass_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[23].Mainhand[0].Name
  - `Swords_B/structures/grass_sword.mcstructure` $.entities[0].Item.Name

### `effect:ice_sword`

- Определение: `Swords_B/items/ice_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - `Swords_B/loot_tables/chests/igloo_chest.json` $.pools[0].entries[6]: `{"type":"item","name":"effect:ice_sword","weight":1}`
  - `Swords_B/loot_tables/chests/village/village_snowy_house.json` $.pools[0].entries[9]: `{"type":"item","weight":4,"functions":[{"function":"minecraft:set_count","count":{"min":1,"max":1}}],"name":"effect:ice_sword"}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[26].Mainhand[0].Name

### `effect:jungle_sword`

- Определение: `Swords_B/items/jungle_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - `Swords_B/loot_tables/chests/jungle_temple.json` $.pools[0].entries[8]: `{"type":"item","name":"effect:jungle_sword","weight":16}`
  - `Swords_B/loot_tables/gameplay/fishing/treasure.json` $.pools[0].entries[4]: `{"type":"item","name":"effect:jungle_sword","weight":5}`
    - Родитель: `Swords_B/loot_tables/gameplay/fishing.json` $.pools[0].entries[1] `{"type":"loot_table","name":"loot_tables/gameplay/fishing/treasure.json","weight":5,"quality":2}`
    - Родитель: `Swords_B/loot_tables/gameplay/jungle_fishing.json` $.pools[0].entries[1] `{"type":"loot_table","name":"loot_tables/gameplay/fishing/treasure.json","weight":5,"quality":2}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[25].Mainhand[0].Name

### `effect:lapis_sword`

- Определение: `Swords_B/items/lapis_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - `Swords_B/loot_tables/chests/pillager_outpost.json` $.pools[3].entries[6]: `{"type":"item","weight":3,"functions":[{"function":"set_count","count":{"min":0,"max":1}}],"name":"effect:lapis_sword"}`
  - `Swords_B/loot_tables/chests/stronghold_corridor.json` $.pools[0].entries[17]: `{"type":"item","name":"effect:lapis_sword","weight":5}`
  - `Swords_B/loot_tables/chests/stronghold_library.json` $.pools[0].entries[3]: `{"type":"item","name":"effect:lapis_sword","weight":5}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[12].Mainhand[0].Name

### `effect:lightning_sword`

- Определение: `Swords_B/items/lightning_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[9].Mainhand[0].Name
  - `Swords_B/structures/lightning_sword.mcstructure` $.entities[0].Item.Name

### `effect:magma_sword`

- Определение: `Swords_B/items/magma_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - `Swords_B/loot_tables/chests/underwater_ruin_big.json` $.pools[1].entries[1]: `{"type":"item","name":"effect:magma_sword","weight":1}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[27].Mainhand[0].Name

### `effect:nether_star_sword`

- Определение: `Swords_B/items/nether_star_sword.json`.
- Результаты рецептов: `Swords_B/recipes/nether_star_sword.json` (`minecraft:recipe_shapeless`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[32].Mainhand[0].Name

### `effect:obsidian_sword`

- Определение: `Swords_B/items/obsidian_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[22].Mainhand[0].Name
  - `Swords_B/structures/obsidian_sword.mcstructure` $.entities[0].Item.Name

### `effect:quartz_diamond`

- Определение: `Swords_B/items/quartz_diamond.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - `Swords_B/loot_tables/blocks/quartz_diamond_ore.json` $.pools[0].entries[0]: `{"type":"item","name":"effect:quartz_diamond","weight":89,"functions":[{"function":"set_count","count":{"min":1,"max":1}}]}`
  - `Swords_B/loot_tables/blocks/quartz_diamond_ore.json` $.pools[0].entries[1]: `{"type":"item","name":"effect:quartz_diamond","weight":10,"functions":[{"function":"set_count","count":{"min":1,"max":2}}]}`
  - `Swords_B/loot_tables/blocks/quartz_diamond_ore.json` $.pools[0].entries[2]: `{"type":"item","name":"effect:quartz_diamond","weight":1,"functions":[{"function":"set_count","count":{"min":2,"max":4}}]}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

### `effect:quartz_diamond_stick`

- Определение: `Swords_B/items/quartz_diamond_stick.json`.
- Результаты рецептов: `Swords_B/recipes/quartz_diamond_stick.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

### `effect:quartz_sword`

- Определение: `Swords_B/items/quartz_sword.json`.
- Результаты рецептов: `Swords_B/recipes/quartz_diamond_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[21].Mainhand[0].Name

### `effect:sea_sword`

- Определение: `Swords_B/items/sea_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - `Swords_B/loot_tables/chests/buriedtreasure.json` $.pools[1].entries[8]: `{"type":"item","name":"effect:sea_sword","weight":15}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[6].Mainhand[0].Name

### `effect:shulker_sword`

- Определение: `Swords_B/items/shulker_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - `Swords_B/loot_tables/entities/shulker.json` $.pools[1].entries[0]: `{"type":"item","name":"effect:shulker_sword","weight":1,"functions":[{"function":"set_count","count":{"min":1,"max":1}},{"function":"set_data","data":0}]}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[3].Mainhand[0].Name

### `effect:silver_ingot`

- Определение: `Swords_B/items/silver_ingot.json`.
- Результаты рецептов: `Swords_B/recipes/silver_ingot.json` (`minecraft:recipe_furnace`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

### `effect:silver_sword`

- Определение: `Swords_B/items/silver_sword.json`.
- Результаты рецептов: `Swords_B/recipes/silver_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[30].Mainhand[0].Name

### `effect:slime_sword`

- Определение: `Swords_B/items/slime_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - `Swords_B/loot_tables/entities/slime_king.json` $.pools[0].entries[0]: `{"type":"item","name":"effect:slime_sword","weight":1,"functions":[{"function":"set_data","data":0}]}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[4].Mainhand[0].Name

### `effect:spectral_sword`

- Определение: `Swords_B/items/spectral_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[5].Mainhand[0].Name
  - `Swords_B/structures/spectral_sword.mcstructure` $.entities[0].Item.Name

### `effect:spider_sword`

- Определение: `Swords_B/items/spider_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - `Swords_B/loot_tables/chests/abandoned_mineshaft.json` $.pools[1].entries[5]: `{"type":"item","name":"effect:spider_sword","functions":[{"function":"set_count","count":{"min":1,"max":1}}],"weight":3}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[2].Mainhand[0].Name

### `effect:sponge_sword`

- Определение: `Swords_B/items/sponge_sword.json`.
- Результаты рецептов: `Swords_B/recipes/wet_sponge_sword.json` (`minecraft:recipe_furnace`).
- Прямые записи loot:
  - `Swords_B/loot_tables/entities/elder_guardian.json` $.pools[1].entries[0]: `{"type":"item","name":"effect:sponge_sword","weight":1,"functions":[{"function":"set_count","count":{"min":1,"max":1}},{"function":"set_data","data":0}]}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[1].Mainhand[0].Name

### `effect:time_sword`

- Определение: `Swords_B/items/time_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[0].Mainhand[0].Name
  - `Swords_B/structures/time_sword.mcstructure` $.entities[0].Item.Name

### `effect:tnt_sword`

- Определение: `Swords_B/items/tnt_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - `Swords_B/loot_tables/chests/desert_pyramid.json` $.pools[0].entries[8]: `{"type":"item","name":"effect:tnt_sword","weight":10}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[11].Mainhand[0].Name

### `effect:ultra_instinct_sword`

- Определение: `Swords_B/items/ultra_instinct_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[20].Mainhand[0].Name
  - `Swords_B/structures/ultra_instinct_sword.mcstructure` $.entities[0].Item.Name

### `effect:wet_sponge_sword`

- Определение: `Swords_B/items/wet_sponge_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[18].Mainhand[0].Name
  - `Swords_B/structures/wet_sponge_sword.mcstructure` $.entities[0].Item.Name

### `effect:wither_skeleton_sword`

- Определение: `Swords_B/items/wither_skeleton_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - `Swords_B/loot_tables/entities/wither_skeleton.json` $.pools[3].entries[0]: `{"type":"item","name":"effect:wither_skeleton_sword","weight":1,"functions":[{"function":"set_data","data":0}]}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[28].Mainhand[0].Name

### `effect:wither_sword`

- Определение: `Swords_B/items/wither_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[8].Mainhand[0].Name
  - `Swords_B/structures/wither_sword.mcstructure` $.entities[0].Item.Name

### `effect:wolf_sword`

- Определение: `Swords_B/items/wolf_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[31].Mainhand[0].Name
  - `Swords_B/structures/wolf_sword.mcstructure` $.entities[0].Item.Name

