# Объявленные пути получения — архив 1.6

Автоматический указатель буквальных результатов рецептов (включая furnace output), записей type=item таблиц добычи, родителей вложенных loot_table, сделок с предметом в gives и NBT-полей Name структур. Это перечень деклараций, а не доказательство получения предмета. Внешние/ванильные пути, генерация, команды, скрипты, другие таблицы обмена и события могут дать предмет другими способами. Запись в структуре может быть в стойке для брони или хранилище, а не дропом. Таблица может не вызываться. Семантика, регистрация, правильность синтаксиса и чувствительность ID к регистру требуют проверки движка.

Родительские цепочки строятся только по точным текстовым путям loot_table с добавлением `.json` при её отсутствии. Циклы обозначаются явно; внешняя таблица не анализируется. Показаны полные объекты записей, но для вычисления вероятностей дополнительно нужны полные пулы, rolls, условия, функции и quality — см. [реестр мира](world-ledger-1.6.md). Веса не объявляются шансами.

## Диагностика чтения

- Ошибок разбора в обработанных категориях не обнаружено.

## Все рецепты и диагностика шаблонов

### `Sword_B/recipes/Sword_of_Time.json` — `minecraft:recipe_shaped`

- Полное определение: `{"description":{"identifier":"effect:Sword_of_Time"},"tags":["crafting_table"],"pattern":["#SS","SBS","NS#"],"key":{"N":{"item":"minecraft:golden_sword"},"S":{"item":"minecraft:gold_block"},"B":{"item":"minecraft:clock"}},"result":{"item":"effect:Sword_of_Time"}}`
- Символы pattern без key: `["#"]`; ключи не использованы в pattern: `[]`. Интерпретация символов и валидность — на проверку движка.
- Результат `effect:Sword_of_Time` не совпадает буквально ни с одним локальным ID предмета; совпадения без учёта регистра: `["effect:sword_of_time"]`. Совместимость не установлена.

### `Sword_B/recipes/blaze_sword.json` — `minecraft:recipe_shaped`

- Полное определение: `{"description":{"identifier":"effect:blaze_sword"},"tags":["crafting_table"],"pattern":["F","F","E"],"key":{"E":{"item":"minecraft:blaze_rod"},"F":{"item":"minecraft:blaze_powder"}},"result":{"item":"effect:blaze_sword"}}`
- Символы pattern без key: `[]`; ключи не использованы в pattern: `[]`. Интерпретация символов и валидность — на проверку движка.

### `Sword_B/recipes/bone_sword.json` — `minecraft:recipe_shaped`

- Полное определение: `{"description":{"identifier":"effect:bone_sword"},"tags":["crafting_table"],"pattern":["F","F","E"],"key":{"E":{"item":"minecraft:bone"},"F":{"item":"minecraft:bone_block"}},"result":{"item":"effect:bone_sword"}}`
- Символы pattern без key: `[]`; ключи не использованы в pattern: `[]`. Интерпретация символов и валидность — на проверку движка.

### `Sword_B/recipes/cactus_sword.json` — `minecraft:recipe_shaped`

- Полное определение: `{"description":{"identifier":"effect:cactus_sword"},"tags":["crafting_table"],"pattern":["F","F","E"],"key":{"E":{"item":"minecraft:stick"},"F":{"item":"minecraft:cactus"}},"result":{"item":"effect:cactus_sword"}}`
- Символы pattern без key: `[]`; ключи не использованы в pattern: `[]`. Интерпретация символов и валидность — на проверку движка.

### `Sword_B/recipes/coal_sword.json` — `minecraft:recipe_shaped`

- Полное определение: `{"description":{"identifier":"effect:coal_sword"},"tags":["crafting_table"],"pattern":["2","2","1"],"key":{"2":{"item":"minecraft:coal_block"},"1":{"item":"minecraft:stick"}},"result":{"item":"effect:coal_sword"}}`
- Символы pattern без key: `[]`; ключи не использованы в pattern: `[]`. Интерпретация символов и валидность — на проверку движка.

### `Sword_B/recipes/creeper_sword.json` — `minecraft:recipe_shaped`

- Полное определение: `{"description":{"identifier":"effect:creeper_sword"},"tags":["crafting_table"],"pattern":["F","F","E"],"key":{"E":{"item":"minecraft:stick"},"F":{"item":"minecraft:skull","data":4}},"result":{"item":"effect:creeper_sword"}}`
- Символы pattern без key: `[]`; ключи не использованы в pattern: `[]`. Интерпретация символов и валидность — на проверку движка.

### `Sword_B/recipes/emerald sword.json` — `minecraft:recipe_shaped`

- Полное определение: `{"description":{"identifier":"effect:emerald_sword"},"tags":["crafting_table"],"pattern":["F","F","E"],"key":{"E":{"item":"minecraft:stick"},"F":{"item":"minecraft:emerald_block"}},"result":{"item":"effect:emerald_sword"}}`
- Символы pattern без key: `[]`; ключи не использованы в pattern: `[]`. Интерпретация символов и валидность — на проверку движка.

### `Sword_B/recipes/ender_sword.json` — `minecraft:recipe_shaped`

- Полное определение: `{"description":{"identifier":"effect:ender_sword"},"tags":["crafting_table"],"pattern":["F","F","E"],"key":{"E":{"item":"minecraft:ender_pearl"},"F":{"item":"minecraft:ender_eye"}},"result":{"item":"effect:ender_sword"}}`
- Символы pattern без key: `[]`; ключи не использованы в pattern: `[]`. Интерпретация символов и валидность — на проверку движка.

### `Sword_B/recipes/fire_sword.json` — `minecraft:recipe_shaped`

- Полное определение: `{"description":{"identifier":"effect:fire_sword"},"tags":["crafting_table"],"pattern":["#SM","SBS","NS#"],"key":{"N":{"item":"minecraft:blaze_rod"},"S":{"item":"minecraft:blaze_powder"},"B":{"item":"minecraft:iron_sword"},"M":{"item":"minecraft:magma_cream"}},"result":{"item":"effect:fire_sword"}}`
- Символы pattern без key: `["#"]`; ключи не использованы в pattern: `[]`. Интерпретация символов и валидность — на проверку движка.

### `Sword_B/recipes/glowstone_sword.json` — `minecraft:recipe_shaped`

- Полное определение: `{"description":{"identifier":"effect:glowstone_sword"},"tags":["crafting_table"],"pattern":["020","020","010"],"key":{"1":{"item":"minecraft:blaze_rod"},"2":{"item":"minecraft:glowstone"}},"result":{"item":"effect:glowstone_sword"}}`
- Символы pattern без key: `["0"]`; ключи не использованы в pattern: `[]`. Интерпретация символов и валидность — на проверку движка.

### `Sword_B/recipes/grass_sword.json` — `minecraft:recipe_shaped`

- Полное определение: `{"description":{"identifier":"effect:grass_sword"},"tags":["crafting_table"],"pattern":["F","F","E"],"key":{"E":{"item":"minecraft:stick"},"F":{"item":"minecraft:grass"}},"result":{"item":"effect:grass_sword"}}`
- Символы pattern без key: `[]`; ключи не использованы в pattern: `[]`. Интерпретация символов и валидность — на проверку движка.

### `Sword_B/recipes/ice_sword.json` — `minecraft:recipe_shaped`

- Полное определение: `{"description":{"identifier":"effect:ice_sword"},"tags":["crafting_table"],"pattern":["F","F","E"],"key":{"E":{"item":"minecraft:stick"},"F":{"item":"minecraft:blue_ice"}},"result":{"item":"effect:ice_sword"}}`
- Символы pattern без key: `[]`; ключи не использованы в pattern: `[]`. Интерпретация символов и валидность — на проверку движка.

### `Sword_B/recipes/jungle_sword.json` — `minecraft:recipe_shaped`

- Полное определение: `{"description":{"identifier":"effect:jungle_sword"},"tags":["crafting_table"],"pattern":["F","F","E"],"key":{"E":{"item":"minecraft:sapling","data":3},"F":{"item":"minecraft:leaves","data":3}},"result":{"item":"effect:jungle_sword"}}`
- Символы pattern без key: `[]`; ключи не использованы в pattern: `[]`. Интерпретация символов и валидность — на проверку движка.

### `Sword_B/recipes/lapis_sword.json` — `minecraft:recipe_shaped`

- Полное определение: `{"description":{"identifier":"effect:lapis_sword"},"tags":["crafting_table"],"pattern":["F","F","E"],"key":{"E":{"item":"minecraft:stick"},"F":{"item":"minecraft:lapis_block"}},"result":{"item":"effect:lapis_sword"}}`
- Символы pattern без key: `[]`; ключи не использованы в pattern: `[]`. Интерпретация символов и валидность — на проверку движка.

### `Sword_B/recipes/lightning_sword.json` — `minecraft:recipe_shaped`

- Полное определение: `{"description":{"identifier":"effect:lightning_sword"},"tags":["crafting_table"],"pattern":["F","F","E"],"key":{"E":{"item":"minecraft:netherstar"},"F":{"item":"minecraft:gold_block"}},"result":{"item":"effect:lightning_sword"}}`
- Символы pattern без key: `[]`; ключи не использованы в pattern: `[]`. Интерпретация символов и валидность — на проверку движка.

### `Sword_B/recipes/magma_sword.json` — `minecraft:recipe_shaped`

- Полное определение: `{"description":{"identifier":"effect:magma_sword"},"tags":["crafting_table"],"pattern":["F","F","E"],"key":{"E":{"item":"minecraft:blaze_rod"},"F":{"item":"minecraft:magma"}},"result":{"item":"effect:magma_sword"}}`
- Символы pattern без key: `[]`; ключи не использованы в pattern: `[]`. Интерпретация символов и валидность — на проверку движка.

### `Sword_B/recipes/obsidian_sword.json` — `minecraft:recipe_shaped`

- Полное определение: `{"description":{"identifier":"effect:obsidian_sword"},"tags":["crafting_table"],"pattern":["F","F","E"],"key":{"E":{"item":"minecraft:blaze_rod"},"F":{"item":"minecraft:obsidian"}},"result":{"item":"effect:obsidian_sword"}}`
- Символы pattern без key: `[]`; ключи не использованы в pattern: `[]`. Интерпретация символов и валидность — на проверку движка.

### `Sword_B/recipes/quartz_sword.json` — `minecraft:recipe_shaped`

- Полное определение: `{"description":{"identifier":"effect:quartz_sword"},"tags":["crafting_table"],"pattern":["#","#","0"],"key":{"#":{"item":"minecraft:quartz_block","data":0},"0":{"item":"minecraft:stick","data":0}},"result":[{"item":"effect:quartz_sword","data":0,"count":1}]}`
- Символы pattern без key: `[]`; ключи не использованы в pattern: `[]`. Интерпретация символов и валидность — на проверку движка.

### `Sword_B/recipes/sea_sword.json` — `minecraft:recipe_shaped`

- Полное определение: `{"description":{"identifier":"effect:sea_sword"},"tags":["crafting_table"],"pattern":["F","F","E"],"key":{"E":{"item":"minecraft:prismarine_shard"},"F":{"item":"minecraft:heart_of_the_sea"}},"result":{"item":"effect:sea_sword"}}`
- Символы pattern без key: `[]`; ключи не использованы в pattern: `[]`. Интерпретация символов и валидность — на проверку движка.

### `Sword_B/recipes/shulker_sword.json` — `minecraft:recipe_shaped`

- Полное определение: `{"description":{"identifier":"effect:shulker_sword"},"tags":["crafting_table"],"pattern":["F","F","E"],"key":{"E":{"item":"minecraft:end_rod"},"F":{"item":"minecraft:shulker_shell"}},"result":{"item":"effect:shulker_sword"}}`
- Символы pattern без key: `[]`; ключи не использованы в pattern: `[]`. Интерпретация символов и валидность — на проверку движка.

### `Sword_B/recipes/slime_sword.json` — `minecraft:recipe_shaped`

- Полное определение: `{"description":{"identifier":"effect:slime_sword"},"tags":["crafting_table"],"pattern":["F","F","E"],"key":{"E":{"item":"minecraft:stick"},"F":{"item":"minecraft:slime"}},"result":{"item":"effect:slime_sword"}}`
- Символы pattern без key: `[]`; ключи не использованы в pattern: `[]`. Интерпретация символов и валидность — на проверку движка.

### `Sword_B/recipes/spectral_sword.json` — `minecraft:recipe_shaped`

- Полное определение: `{"description":{"identifier":"effect:spectral_sword"},"tags":["crafting_table"],"pattern":["#SS","SBS","NS#"],"key":{"N":{"item":"minecraft:end_rod"},"S":{"item":"minecraft:end_crystal"},"B":{"item":"minecraft:netherstar"}},"result":{"item":"effect:spectral_sword"}}`
- Символы pattern без key: `["#"]`; ключи не использованы в pattern: `[]`. Интерпретация символов и валидность — на проверку движка.

### `Sword_B/recipes/spider_sword.json` — `minecraft:recipe_shaped`

- Полное определение: `{"description":{"identifier":"effect:spider_sword"},"tags":["crafting_table"],"pattern":["#SS","SBS","NS#"],"key":{"N":{"item":"minecraft:stick"},"S":{"item":"minecraft:web"},"B":{"item":"minecraft:spider_eye"}},"result":{"item":"effect:spider_sword"}}`
- Символы pattern без key: `["#"]`; ключи не использованы в pattern: `[]`. Интерпретация символов и валидность — на проверку движка.

### `Sword_B/recipes/sponge_sword.json` — `minecraft:recipe_shaped`

- Полное определение: `{"description":{"identifier":"effect:sponge_sword"},"tags":["crafting_table"],"pattern":["F","F","E"],"key":{"E":{"item":"minecraft:stick"},"F":{"item":"minecraft:sponge"}},"result":{"item":"effect:sponge_sword"}}`
- Символы pattern без key: `[]`; ключи не использованы в pattern: `[]`. Интерпретация символов и валидность — на проверку движка.

### `Sword_B/recipes/tnt_sword.json` — `minecraft:recipe_shaped`

- Полное определение: `{"description":{"identifier":"effect:tnt_sword"},"tags":["crafting_table"],"pattern":["F","F","E"],"key":{"E":{"item":"minecraft:stick"},"F":{"item":"minecraft:tnt"}},"result":{"item":"effect:tnt_sword"}}`
- Символы pattern без key: `[]`; ключи не использованы в pattern: `[]`. Интерпретация символов и валидность — на проверку движка.

### `Sword_B/recipes/wither_sword.json` — `minecraft:recipe_shaped`

- Полное определение: `{"description":{"identifier":"effect:wither_sword"},"tags":["crafting_table"],"pattern":["#SS","SBS","NS#"],"key":{"N":{"item":"minecraft:blaze_rod"},"S":{"item":"minecraft:skull","data":1},"B":{"item":"minecraft:netherstar"}},"result":{"item":"effect:wither_sword"}}`
- Символы pattern без key: `["#"]`; ключи не использованы в pattern: `[]`. Интерпретация символов и валидность — на проверку движка.

## Все записи type=loot_table и локальное разрешение

- Буквальных записей type=loot_table нет.

## По предметам

### `effect:blaze_sword`

- Определение: `Sword_B/items/blaze_sword.json`.
- Результаты рецептов: `Sword_B/recipes/blaze_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

### `effect:bone_sword`

- Определение: `Sword_B/items/bone_sword.json`.
- Результаты рецептов: `Sword_B/recipes/bone_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

### `effect:cactus_sword`

- Определение: `Sword_B/items/cactus_sword.json`.
- Результаты рецептов: `Sword_B/recipes/cactus_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

### `effect:coal_sword`

- Определение: `Sword_B/items/coal_sword.json`.
- Результаты рецептов: `Sword_B/recipes/coal_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

### `effect:creeper_sword`

- Определение: `Sword_B/items/creeper_sword.json`.
- Результаты рецептов: `Sword_B/recipes/creeper_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

### `effect:emerald_sword`

- Определение: `Sword_B/items/emerald_sword.json`.
- Результаты рецептов: `Sword_B/recipes/emerald sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

### `effect:ender_sword`

- Определение: `Sword_B/items/ender_sword.json`.
- Результаты рецептов: `Sword_B/recipes/ender_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

### `effect:fire_sword`

- Определение: `Sword_B/items/fire_sword.json`.
- Результаты рецептов: `Sword_B/recipes/fire_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

### `effect:glowstone_sword`

- Определение: `Sword_B/items/glowstone_sword.json`.
- Результаты рецептов: `Sword_B/recipes/glowstone_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

### `effect:grass_sword`

- Определение: `Sword_B/items/grass_sword.json`.
- Результаты рецептов: `Sword_B/recipes/grass_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

### `effect:ice_sword`

- Определение: `Sword_B/items/ice_sword.json`.
- Результаты рецептов: `Sword_B/recipes/ice_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

### `effect:jungle_sword`

- Определение: `Sword_B/items/jungle_sword.json`.
- Результаты рецептов: `Sword_B/recipes/jungle_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

### `effect:lapis_sword`

- Определение: `Sword_B/items/lapis_sword.json`.
- Результаты рецептов: `Sword_B/recipes/lapis_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

### `effect:lightning_sword`

- Определение: `Sword_B/items/lightning_sword.json`.
- Результаты рецептов: `Sword_B/recipes/lightning_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

### `effect:magma_sword`

- Определение: `Sword_B/items/magma_sword.json`.
- Результаты рецептов: `Sword_B/recipes/magma_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

### `effect:obsidian_sword`

- Определение: `Sword_B/items/obsidian_sword.json`.
- Результаты рецептов: `Sword_B/recipes/obsidian_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

### `effect:quartz_sword`

- Определение: `Sword_B/items/quartz_sword.json`.
- Результаты рецептов: `Sword_B/recipes/quartz_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

### `effect:sea_sword`

- Определение: `Sword_B/items/sea_sword.json`.
- Результаты рецептов: `Sword_B/recipes/sea_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

### `effect:shulker_sword`

- Определение: `Sword_B/items/shulker_sword.json`.
- Результаты рецептов: `Sword_B/recipes/shulker_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

### `effect:slime_sword`

- Определение: `Sword_B/items/slime_sword.json`.
- Результаты рецептов: `Sword_B/recipes/slime_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

### `effect:spectral_sword`

- Определение: `Sword_B/items/spectral_sword.json`.
- Результаты рецептов: `Sword_B/recipes/spectral_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

### `effect:spider_sword`

- Определение: `Sword_B/items/spider_sword.json`.
- Результаты рецептов: `Sword_B/recipes/spider_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

### `effect:sponge_sword`

- Определение: `Sword_B/items/sponge_sword.json`.
- Результаты рецептов: `Sword_B/recipes/sponge_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

### `effect:sword_of_time`

- Определение: `Sword_B/items/Sword of Time.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

### `effect:tnt_sword`

- Определение: `Sword_B/items/tnt_sword.json`.
- Результаты рецептов: `Sword_B/recipes/tnt_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

### `effect:wither_sword`

- Определение: `Sword_B/items/wither_sword.json`.
- Результаты рецептов: `Sword_B/recipes/wither_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

