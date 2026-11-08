# Сводка прямых механик предметов — архив 2.8.8

Машинный индекс непосредственно объявленных данных предметов. Это **не** полное описание поведения: эффекты игрока, сущности, скрытые цепочки и поведение движка разбираются отдельно. Путь исходника и номера строк относятся к архиву из `sources/`.

Доли randomize рассчитаны как weight / сумма явно заданных неотрицательных целых весов в том же массиве. Это условная доля при выборе ветви, не вероятность успешного результата; фильтры, вложенность и триггер влияют на итог. При отсутствующем весе доли не вычисляются. Соседние поля объекта показаны вместе без предположений об их порядке.

## Общая таблица

| ID | Урон | Прочность max | Cooldown (category, duration) | Крюки |
|---|---:|---:|---|---|
| `effect:bedrock_stick` | `6` | `"—"` | `"—"` | weapon |
| `effect:bedrock_sword` | `18` | `"—"` | `"—"` | weapon |
| `effect:bee_sword` | `5` | `1080` | `"—"` | weapon |
| `effect:blaze_sword` | `6` | `2300` | `{"category":"blaze_sword","duration":20}` | on_use, weapon |
| `effect:bone_sword` | `5` | `820` | `"—"` | weapon |
| `effect:cactus_sword` | `6` | `125` | `"—"` | weapon |
| `effect:clock_sword` | `7` | `4800` | `{"category":"clock_sword","duration":30}` | on_use, weapon |
| `effect:coal_sword` | `4` | `121` | `"—"` | weapon |
| `effect:creeper_sword` | `6` | `1500` | `{"category":"creeper_sword","duration":3}` | on_use, weapon |
| `effect:emerald_sword` | `7` | `2300` | `"—"` | weapon |
| `effect:ender_sword` | `9` | `1256` | `{"category":"ender_sword","duration":2}` | on_use, weapon |
| `effect:fire_sword` | `6` | `2000` | `{"category":"fire_sword","duration":25}` | on_use, weapon |
| `effect:ghost_sword` | `-666` | `3333` | `{"category":"ghost_sword","duration":2}` | on_use, weapon |
| `effect:glass_sword` | `33` | `1` | `"—"` | weapon |
| `effect:glowstone_sword` | `4` | `128` | `"—"` | weapon |
| `effect:grass_sword` | `8` | `250` | `"—"` | weapon |
| `effect:ice_sword` | `8.5` | `500` | `{"category":"ice_sword","duration":5}` | on_use, weapon |
| `effect:jungle_sword` | `4` | `128` | `"—"` | weapon |
| `effect:lapis_sword` | `5` | `528` | `"—"` | weapon |
| `effect:lightning_sword` | `8` | `2012` | `{"category":"lightning_sword","duration":12}` | on_use, weapon |
| `effect:magma_sword` | `7.2` | `1316` | `"—"` | weapon |
| `effect:nether_star_sword` | `7` | `3256` | `"—"` | weapon |
| `effect:obsidian_sword` | `8` | `3000` | `"—"` | weapon |
| `effect:cursed_pumpkin_sword` | `5` | `606` | `"—"` | weapon |
| `effect:quartz_diamond` | `"—"` | `"—"` | `"—"` | — |
| `effect:quartz_diamond_stick` | `24` | `20` | `"—"` | weapon |
| `effect:quartz_sword` | `600` | `1` | `"—"` | weapon |
| `effect:sea_sword` | `7` | `1356` | `"—"` | weapon |
| `effect:shulker_sword` | `6` | `2609` | `{"category":"shulker_sword","duration":8}` | on_use, weapon |
| `effect:silver_ingot` | `"—"` | `"—"` | `"—"` | — |
| `effect:silver_sword` | `6` | `1800` | `"—"` | weapon |
| `effect:slime_sword` | `6` | `675` | `"—"` | weapon |
| `effect:spectral_sword` | `9` | `3256` | `{"category":"spectral_sword","duration":18}` | on_use, weapon |
| `effect:spider_sword` | `5` | `628` | `{"category":"spider_sword","duration":28}` | on_use, weapon |
| `effect:sponge_sword` | `5` | `128` | `"—"` | weapon |
| `effect:time_sword` | `13` | `13770` | `"—"` | weapon |
| `effect:tnt_sword` | `4` | `64` | `{"category":"tnt_sword","duration":10}` | on_use, weapon |
| `effect:ultra_instinct_sword` | `16` | `9999` | `{"category":"ultra_instinct_sword","duration":61}` | on_use, weapon |
| `effect:wet_sponge_sword` | `3` | `64` | `"—"` | weapon |
| `effect:wither_skeleton_sword` | `4` | `128` | `"—"` | weapon |
| `effect:wither_sword` | `10` | `3856` | `{"category":"wither_sword","duration":3}` | on_use, weapon |
| `effect:wolf_sword` | `5` | `2800` | `"—"` | weapon |

## Карточки

### effect:bedrock_stick

- Файл `Swords_B/items/bedrock_stick.json`; format_version `"1.16.100"`.
- Урон `6`; прочность `"не задана"`; стак `1`; перезарядка `"не задана"`.
- Зачарование `"не задано"`; ремонт `"не задан"`.
- Оффхенд `false`; hand_equipped `true`; foil `false`; icon `{"texture":"bedrock_stick"}`.
- Скорости добычи `"не заданы"`.

**Привязки триггеров:** `{"minecraft:weapon":{}}`.

Прямых item events в файле нет; это не исключает пассивные и косвенные механики.

### effect:bedrock_sword

- Файл `Swords_B/items/bedrock_sword.json`; format_version `"1.16.100"`.
- Урон `18`; прочность `"не задана"`; стак `1`; перезарядка `"не задана"`.
- Зачарование `"не задано"`; ремонт `"не задан"`.
- Оффхенд `false`; hand_equipped `true`; foil `false`; icon `{"texture":"bedrock_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":{"tags":"q.any_tag('stone', 'metal', 'diamond_pick_diggable', 'wood', 'pumpkin', 'plant', 'dirt', 'sand', 'gravel', 'grass', 'snow')"},"speed":999},{"block":"effect99:quartz_diamond_block","speed":50},{"block":"effect99:quartz_diamond_ore","speed":100},{"block":"effect99:silver_ore","speed":999},{"block":"minecraft:warped_wart_block","speed":999},{"block":"minecraft:nether_wart_block","speed":999},{"block":"minecraft:leaves","speed":999},{"block":"minecraft:leaves2","speed":999},{"block":"minecraft:hay_block","speed":999},{"block":"minecraft:soul_soil","speed":999},{"block":"minecraft:soul_sand","speed":999},{"block":"minecraft:chest","speed":999},{"block":"minecraft:melon_block","speed":999},{"block":"minecraft:bookshelf","speed":999},{"block":"minecraft:lectern","speed":999},{"block":"minecraft:pumkin","speed":999},{"block":"minecraft:ice","speed":999},{"block":"minecraft:bone_block","speed":999},{"block":"minecraft:mob_spawner","speed":999},{"block":"minecraft:anvil","speed":999},{"block":"minecraft:netherite_block","speed":999},{"block":"minecraft:sandstone","speed":999},{"block":"minecraft:diamond_block","speed":999},{"block":"minecraft:lapis_block","speed":999},{"block":"minecraft:emerald_block","speed":999},{"block":"minecraft:ancient_debris","speed":999},{"block":"minecraft:cracked_polished_blackstone_bricks","speed":999},{"block":"minecraft:nether_brick","speed":999},{"block":"minecraft:cracked_nether_bricks","speed":999},{"block":"minecraft:quartz_ore","speed":999},{"block":"minecraft:netherrack","speed":999},{"block":"minecraft:basalt","speed":999},{"block":"minecraft:end_bricks","speed":999},{"block":"minecraft:purpur_block","speed":999},{"block":"minecraft:purpur_stairs","speed":999},{"block":"minecraft:end_brick_stairs","speed":999},{"block":"minecraft:stone_slab2","speed":999},{"block":"minecraft:stone_slab3","speed":999},{"block":"minecraft:polished_basalt","speed":999},{"block":"minecraft:warped_nylium","speed":999},{"block":"minecraft:crimson_nylium","speed":999},{"block":"minecraft:end_stone","speed":999},{"block":"minecraft:ender_chest","speed":999},{"block":"minecraft:quartz_block","speed":999},{"block":"minecraft:quartz_stairs","speed":999},{"block":"minecraft:quartz_bricks","speed":999},{"block":"minecraft:quartz_stairs","speed":999},{"block":"minecraft:nether_gold_ore","speed":999},{"block":"minecraft:blackstone","speed":999},{"block":"minecraft:furnace","speed":999},{"block":"minecraft:blast_furnace","speed":999},{"block":"minecraft:lit_furnace","speed":999},{"block":"minecraft:blast_furnace","speed":999},{"block":"minecraft:chain","speed":999},{"block":"minecraft:lantern","speed":999},{"block":"minecraft:soul_lantern","speed":999},{"block":"minecraft:grindstone","speed":999},{"block":"minecraft:brewing_stand","speed":999},{"block":"minecraft:smooth_stone","speed":999},{"block":"minecraft:stonebrick","speed":999},{"block":"minecraft:enchanting_table","speed":999},{"block":"minecraft:stone_brick_stairs","speed":999},{"block":"minecraft:mossy_stone_brick_stairs","speed":999},{"block":"minecraft:polished_blackstone_bricks","speed":999},{"block":"minecraft:polished_blackstone_stairs","speed":999},{"block":"minecraft:blackstone_wall","speed":999},{"block":"minecraft:blackstone_wall","speed":999},{"block":"minecraft:polished_blackstone_wall","speed":999}]}`.

**Привязки триггеров:** `{"minecraft:weapon":{}}`.

Прямых item events в файле нет; это не исключает пассивные и косвенные механики.

### effect:bee_sword

- Файл `Swords_B/items/bee_sword.json`; format_version `"1.16.100"`.
- Урон `5`; прочность `{"max_durability":1080}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:bee_sword"],"repair_amount":1080},{"items":["minecraft:honey_block"],"repair_amount":400},{"items":["minecraft:honeycomb"],"repair_amount":150}]}`.
- Оффхенд `false`; hand_equipped `true`; foil `false`; icon `{"texture":"bee_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"},"on_not_hurt_entity":{"event":"weapon"},"on_hit_block":{"event":"weapon"}}}`.

**Событие `weapon`** (упоминания в исходнике: строки 66, 69, 72, 77):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`
  - `$.sequence[1].randomize`: альтернативы, веса `[30,70]`, сумма 100:
    - ветвь 0, weight `30`; условная доля 3/10 (30%):
      - `$.sequence[1].randomize[0]` — поля действия: `{"shoot":{"projectile":"entity:bee_sword","launch_power":1}}`
    - ветвь 1, weight `70`; условная доля 7/10 (70%):
      - `$.sequence[1].randomize[1]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`

**Прямые ссылки на сущности из текстовых значений item** (распознавание идентификаторов; не все они обязательно вызываются):
- `entity:bee_sword` → `Swords_B/entities/bee_entity.json`

**Таблицы добычи с буквальным ID и прямые упоминания этих таблиц:**
- `Swords_B/loot_tables/bee_sword.json` → `Swords_B/entities/bee.json`:849

### effect:blaze_sword

- Файл `Swords_B/items/blaze_sword.json`; format_version `"1.16.100"`.
- Урон `6`; прочность `{"max_durability":2300}`; стак `1`; перезарядка `{"category":"blaze_sword","duration":20}`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:blaze_sword"],"repair_amount":2300}]}`.
- Оффхенд `false`; hand_equipped `true`; foil `false`; icon `{"texture":"blaze_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{"minecraft:on_use":{"on_use":{"event":"on_use"}},"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"},"on_not_hurt_entity":{"event":"weapon"},"on_hit_block":{"event":"weapon"}}}`.

**Событие `on_use`** (упоминания в исходнике: строки 56, 57, 74):

- `$` — поля действия: `{"damage":{"type":"durability","amount":10,"target":"self"},"run_command":{"command":["event entity @s[family=blaze_sword] blaze_sword_skill_event","effect @s levitation 7 0 true","effect @s slow_falling 10 3 true"]}}`

**Событие `weapon`** (упоминания в исходнике: строки 63, 66, 69, 88):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`
  - `$.sequence[1].randomize`: альтернативы, веса `[14,1,85]`, сумма 100:
    - ветвь 0, weight `14`; условная доля 7/50 (14%):
      - `$.sequence[1].randomize[0]` — поля действия: `{"run_command":{"command":["effect @s fire_resistance 1 0 true"]},"shoot":{"projectile":"minecraft:small_fireball","launch_power":1}}`
    - ветвь 1, weight `1`; условная доля 1/100 (1%):
      - `$.sequence[1].randomize[1]` — поля действия: `{"run_command":{"command":["effect @s fire_resistance 1 0 true"]},"shoot":{"projectile":"minecraft:fireball","launch_power":1}}`
    - ветвь 2, weight `85`; условная доля 17/20 (85%):
      - `$.sequence[1].randomize[2]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`

**Прямые ссылки на сущности из текстовых значений item** (распознавание идентификаторов; не все они обязательно вызываются):
- `minecraft:fireball` → `Swords_B/entities/fireball.json`
- `minecraft:small_fireball` → `Swords_B/entities/small_fireball.json`

**Таблицы добычи с буквальным ID и прямые упоминания этих таблиц:**
- `Swords_B/loot_tables/entities/blaze.json` → `Swords_B/entities/blaze.json`:15

### effect:bone_sword

- Файл `Swords_B/items/bone_sword.json`; format_version `"1.16.100"`.
- Урон `5`; прочность `{"max_durability":820}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:bone_sword"],"repair_amount":820},{"items":["minecraft:bone"],"repair_amount":70},{"items":["minecraft:bone_block"],"repair_amount":300},{"items":["minecraft:bone_meal"],"repair_amount":18}]}`.
- Оффхенд `false`; hand_equipped `true`; foil `false`; icon `{"texture":"bone_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"},"on_not_hurt_entity":{"event":"weapon"},"on_hit_block":{"event":"weapon"}}}`.

**Событие `weapon`** (упоминания в исходнике: строки 72, 75, 78, 83):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`
  - `$.sequence[1].randomize`: альтернативы, веса `[20,80]`, сумма 100:
    - ветвь 0, weight `20`; условная доля 1/5 (20%):
      - `$.sequence[1].randomize[0]` — поля действия: `{"shoot":{"projectile":"minecraft:arrow","launch_power":1}}`
    - ветвь 1, weight `80`; условная доля 4/5 (80%):
      - `$.sequence[1].randomize[1]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`

**Прямые ссылки на сущности из текстовых значений item** (распознавание идентификаторов; не все они обязательно вызываются):
- `minecraft:arrow` → `Swords_B/entities/arrow.json`

### effect:cactus_sword

- Файл `Swords_B/items/cactus_sword.json`; format_version `"1.16.100"`.
- Урон `6`; прочность `{"max_durability":125}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:cactus_sword"],"repair_amount":125}]}`.
- Оффхенд `false`; hand_equipped `true`; foil `false`; icon `{"texture":"cactus_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"}}}`.

**Событие `weapon`** (упоминания в исходнике: строки 72, 77):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`

### effect:clock_sword

- Файл `Swords_B/items/clock_sword.json`; format_version `"1.16.100"`.
- Урон `7`; прочность `{"max_durability":4800}`; стак `1`; перезарядка `{"category":"clock_sword","duration":30}`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:clock_sword"],"repair_amount":4800},{"items":["minecraft:clock"],"repair_amount":900},{"items":["minecraft:gold_block"],"repair_amount":780},{"items":["minecraft:gold_ingot"],"repair_amount":87}]}`.
- Оффхенд `false`; hand_equipped `true`; foil `true`; icon `{"texture":"clock_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{"minecraft:on_use":{"on_use":{"event":"on_use"}},"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"},"on_not_hurt_entity":{"event":"weapon"},"on_hit_block":{"event":"weapon"}}}`.

**Событие `weapon`** (упоминания в исходнике: строки 81, 84, 87, 92):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`

**Событие `on_use`** (упоминания в исходнике: строки 75, 76, 103):

- `$` — поля действия: `{"damage":{"type":"durability","amount":10,"target":"self"},"run_command":{"command":["event entity @s[family=clock_sword] clock_sword_skill_event"]}}`

### effect:coal_sword

- Файл `Swords_B/items/coal_sword.json`; format_version `"1.16.100"`.
- Урон `4`; прочность `{"max_durability":121}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:coal_sword"],"repair_amount":121},{"items":["minecraft:coal"],"repair_amount":58},{"items":["minecraft:stick"],"repair_amount":2}]}`.
- Оффхенд `false`; hand_equipped `true`; foil `false`; icon `{"texture":"coal_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"}}}`.

**Событие `weapon`** (упоминания в исходнике: строки 69, 74):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`

**Таблицы добычи с буквальным ID и прямые упоминания этих таблиц:**
- `Swords_B/loot_tables/chests/spawn_bonus_chest.json` → прямых текстовых ссылок не найдено; возможна регистрация движком/косвенная ссылка

### effect:creeper_sword

- Файл `Swords_B/items/creeper_sword.json`; format_version `"1.16.100"`.
- Урон `6`; прочность `{"max_durability":1500}`; стак `1`; перезарядка `{"category":"creeper_sword","duration":3}`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:creeper_sword"],"repair_amount":1500},{"items":["minecraft:gunpowder"],"repair_amount":256}]}`.
- Оффхенд `false`; hand_equipped `true`; foil `false`; icon `{"texture":"creeper_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{"minecraft:on_use":{"on_use":{"event":"on_use"}},"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"},"on_not_hurt_entity":{"event":"weapon"},"on_hit_block":{"event":"weapon"}}}`.

**Событие `on_use`** (упоминания в исходнике: строки 64, 65, 81):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"run_command":{"command":["event entity @s start_player_explode_event"],"target":"holder"}}`
  - `$.sequence[1]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`

**Событие `weapon`** (упоминания в исходнике: строки 70, 73, 76, 100):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`
  - `$.sequence[1].randomize`: альтернативы, веса `[20,80]`, сумма 100:
    - ветвь 0, weight `20`; условная доля 1/5 (20%):
      - `$.sequence[1].randomize[0]` — поля действия: `{"shoot":{"projectile":"minecraft:creeper","launch_power":1}}`
    - ветвь 1, weight `80`; условная доля 4/5 (80%):
      - `$.sequence[1].randomize[1]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`

### effect:emerald_sword

- Файл `Swords_B/items/emerald_sword.json`; format_version `"1.16.100"`.
- Урон `7`; прочность `{"max_durability":2300}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:emerald_sword"],"repair_amount":2300}]}`.
- Оффхенд `false`; hand_equipped `true`; foil `false`; icon `{"texture":"emerald_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"},"on_not_hurt_entity":{"event":"weapon"},"on_hit_block":{"event":"weapon"}}}`.

**Событие `weapon`** (упоминания в исходнике: строки 54, 57, 60, 65):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`

**Таблицы добычи с буквальным ID и прямые упоминания этих таблиц:**
- `Swords_B/loot_tables/chests/pillager_outpost.json` → прямых текстовых ссылок не найдено; возможна регистрация движком/косвенная ссылка
- `Swords_B/loot_tables/chests/stronghold_corridor.json` → прямых текстовых ссылок не найдено; возможна регистрация движком/косвенная ссылка
- `Swords_B/loot_tables/chests/woodland_mansion.json` → прямых текстовых ссылок не найдено; возможна регистрация движком/косвенная ссылка

### effect:ender_sword

- Файл `Swords_B/items/ender_sword.json`; format_version `"1.16.100"`.
- Урон `9`; прочность `{"max_durability":1256}`; стак `1`; перезарядка `{"category":"ender_sword","duration":2}`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:ender_sword"],"repair_amount":1256},{"items":["minecraft:ender_pearl"],"repair_amount":28},{"items":["minecraft:ender_eye"],"repair_amount":32}]}`.
- Оффхенд `false`; hand_equipped `true`; foil `true`; icon `{"texture":"ender_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{"minecraft:on_use":{"on_use":{"event":"on_use"}},"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"}}}`.

**Событие `on_use`** (упоминания в исходнике: строки 97, 98, 108):

- `$` — поля действия: `{"run_command":{"command":["spreadplayers ~ ~ 16 32 @s","playsound mob.endermen.portal @a[r=34]"]},"damage":{"type":"durability","amount":5,"target":"self"}}`

**Событие `weapon`** (упоминания в исходнике: строки 103, 112):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`

**Таблицы добычи с буквальным ID и прямые упоминания этих таблиц:**
- `Swords_B/loot_tables/entities/red_enderman.json` → `Swords_B/entities/enderman.json`:71

### effect:fire_sword

- Файл `Swords_B/items/fire_sword.json`; format_version `"1.16.100"`.
- Урон `6`; прочность `{"max_durability":2000}`; стак `1`; перезарядка `{"category":"fire_sword","duration":25}`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:fire_sword"],"repair_amount":2000},{"items":["minecraft:fire"],"repair_amount":1000}]}`.
- Оффхенд `false`; hand_equipped `true`; foil `true`; icon `{"texture":"fire_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{"minecraft:on_use":{"on_use":{"event":"on_use"}},"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"},"on_not_hurt_entity":{"event":"weapon"},"on_hit_block":{"event":"weapon"}}}`.

**Событие `on_use`** (упоминания в исходнике: строки 63, 64, 80):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"run_command":{"command":["summon entity:living_flame ~ ~14 ~ minecraft:target","summon entity:living_flame ~ ~4 ~ fire_sword_skill","summon entity:living_flame ~3 ~4 ~ fire_sword_skill","summon entity:living_flame ~ ~4 ~3 fire_sword_skill","summon entity:living_flame ~-3 ~4 ~ fire_sword_skill","summon entity:living_flame ~ ~4 ~-3 fire_sword_skill","particle minecraft:example_linearcurve ~ ~0.2 ~","title @s actionbar §l§6Fire rain"],"target":"holder"}}`
  - `$.sequence[1]` — поля действия: `{"damage":{"type":"durability","amount":20,"target":"self"}}`

**Событие `weapon`** (упоминания в исходнике: строки 69, 72, 75, 106):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`
  - `$.sequence[1].randomize`: альтернативы, веса `[85,15]`, сумма 100:
    - ветвь 0, weight `85`; условная доля 17/20 (85%):
      - `$.sequence[1].randomize[0]` — поля действия: `{"shoot":{"projectile":"entity:fire","launch_power":1}}`
    - ветвь 1, weight `15`; условная доля 3/20 (15%):
      - `$.sequence[1].randomize[1]` — поля действия: `{"shoot":{"projectile":"entity:living_flame","launch_power":1}}`

**Прямые ссылки на сущности из текстовых значений item** (распознавание идентификаторов; не все они обязательно вызываются):
- `entity:fire` → `Swords_B/entities/fire.json`
- `entity:living_flame` → `Swords_B/entities/living_flame.json`

**Таблицы добычи с буквальным ID и прямые упоминания этих таблиц:**
- `Swords_B/loot_tables/entities/living_flame.json` → прямых текстовых ссылок не найдено; возможна регистрация движком/косвенная ссылка

### effect:ghost_sword

- Файл `Swords_B/items/ghost_sword.json`; format_version `"1.16.100"`.
- Урон `-666`; прочность `{"max_durability":3333}`; стак `1`; перезарядка `{"category":"ghost_sword","duration":2}`.
- Зачарование `"не задано"`; ремонт `"не задан"`.
- Оффхенд `false`; hand_equipped `true`; foil `true`; icon `{"texture":"ghost_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{"minecraft:on_use":{"on_use":{"event":"on_use"}},"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"},"on_not_hurt_entity":{"event":"weapon"},"on_hit_block":{"event":"weapon"}}}`.

**Событие `on_use`** (упоминания в исходнике: строки 63, 64, 80):

- `$` — поля действия: `{"shoot":{"projectile":"entity:ghost_projectile","launch_power":1},"damage":{"type":"durability","amount":6,"target":"self"}}`

**Событие `weapon`** (упоминания в исходнике: строки 69, 72, 75, 91):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`

**Прямые ссылки на сущности из текстовых значений item** (распознавание идентификаторов; не все они обязательно вызываются):
- `entity:ghost_projectile` → `Swords_B/entities/ghost_projectile.json`

### effect:glass_sword

- Файл `Swords_B/items/glass_sword.json`; format_version `"1.16.100"`.
- Урон `33`; прочность `{"max_durability":1}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:glass_sword"],"repair_amount":1},{"items":["minecraft:glass"],"repair_amount":1}]}`.
- Оффхенд `false`; hand_equipped `true`; foil `false`; icon `{"texture":"glass_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":25,"on_dig":{"event":"weapon"}},{"block":"minecraft:bamboo","speed":15,"on_dig":{"event":"weapon"}}],"on_dig":{"event":"weapon"}}`.

**Привязки триггеров:** `{"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"},"on_not_hurt_entity":{"event":"weapon"},"on_hit_block":{"event":"weapon"}}}`.

**Событие `weapon`** (упоминания в исходнике: строки 50, 57, 62, 69, 72, 75, 80):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"damage":{"type":"durability","amount":10,"target":"self"},"run_command":{"command":["playsound random.glass @a[r=8,m=0]"]}}`

### effect:glowstone_sword

- Файл `Swords_B/items/glowstone_sword.json`; format_version `"1.16.100"`.
- Урон `4`; прочность `{"max_durability":128}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:glowstone_sword"],"repair_amount":128},{"items":["minecraft:glowstone"],"repair_amount":64},{"items":["minecraft:glowstone_dust"],"repair_amount":16}]}`.
- Оффхенд `true`; hand_equipped `true`; foil `true`; icon `{"texture":"glowstone_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"}}}`.

**Событие `weapon`** (упоминания в исходнике: строки 66, 71):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`

### effect:grass_sword

- Файл `Swords_B/items/grass_sword.json`; format_version `"1.16.100"`.
- Урон `8`; прочность `{"max_durability":250}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:grass_sword"],"repair_amount":250}]}`.
- Оффхенд `false`; hand_equipped `true`; foil `false`; icon `{"texture":"grass_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"}}}`.

**Событие `weapon`** (упоминания в исходнике: строки 72, 77):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`

### effect:ice_sword

- Файл `Swords_B/items/ice_sword.json`; format_version `"1.16.100"`.
- Урон `8.5`; прочность `{"max_durability":500}`; стак `1`; перезарядка `{"category":"ice_sword","duration":5}`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:ice_sword"],"repair_amount":500},{"items":["minecraft:ice"],"repair_amount":55}]}`.
- Оффхенд `false`; hand_equipped `true`; foil `true`; icon `{"texture":"ice_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{"minecraft:on_use":{"on_use":{"event":"on_use"}},"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"},"on_not_hurt_entity":{"event":"weapon"},"on_hit_block":{"event":"weapon"}}}`.

**Событие `on_use`** (упоминания в исходнике: строки 63, 64, 80):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"run_command":{"command":["execute @e[type=!enderman,type=!horse,type=!slime,type=!silverfish,type=!spider,type=!cave_spider,type=!tnt,type=!vex,type=!chicken,type=!pig,type=!wolf,type=!cat,type=!item,type=!xp_orb,type=!xp_bottle,type=!egg,type=!snowball,type=!fireball,type=!small_fireball,type=!eye_of_ender_signal,type=!ender_pearl,type=!fishing_hook,type=!falling_block,type=!lightning_bolt,type=!lingering_potion,type=!dragon_fireball,type=!ender_dragon,type=!endermite,type=!arrow,type=!thrown_trident,type=!leash_knot,type=!bat,type=!rabbit,type=!parrot,type=!ghast,type=!shulker,type=!elder_guardian,type=!guardian,type=!turtle,type=!fox,type=!squid,type=!ocelot,type=!phantom,type=!area_effect_cloud,family=!fish,family=!effect99_entities,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 effect99:fake_ice 0 replace air 0","execute @e[type=enderman,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~3 ~-1 effect99:fake_ice 0 replace air 0","execute @e[family=slime_large,rm=2,r=12] ~ ~ ~ fill ~2 ~-1 ~2 ~-2 ~3 ~-2 effect99:fake_ice 0 replace air 0","execute @e[family=slime_large,rm=2,r=12] ~ ~1 ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 air 0 replace effect99:fake_ice","execute @e[family=slime_medium,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0","execute @e[family=slime_medium,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ air 0 replace effect99:fake_ice","execute @e[family=slime_small,rm=2,r=12] ~ ~ ~ fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:fake_ice 0 replace air 0","execute @e[family=slime_small,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ air 0 replace effect99:fake_ice","execute @e[type=silverfish,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ effect99:fake_ice 0 replace air 0","execute @e[type=spider,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0","execute @e[type=cave_spider,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0","execute @e[type=tnt,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0","execute @e[type=vex,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0","execute @e[type=chicken,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0","execute @e[type=pig,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0","execute @e[type=wolf,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0","execute @e[type=cat,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0","execute @e[type=small_fireball,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ effect99:fake_ice 0 replace air 0","execute @e[type=fireball,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ effect99:fake_ice 0 replace air 0","execute @e[type=arrow,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ effect99:fake_ice 0 replace air 0","execute @e[type=lingering_potion,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ effect99:fake_ice 0 replace air 0","execute @e[type=dragon_fireball,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ effect99:fake_ice 0 replace air 0","execute @e[type=thrown_trident,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ effect99:fake_ice 0 replace air 0","execute @e[type=endermite,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0","execute @e[type=rabbit,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0","execute @e[type=parrot,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0","execute @e[type=phantom,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0","execute @e[type=shulker,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0","execute @e[type=guardian,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0","execute @e[type=ocelot,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0","execute @e[type=turtle,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0","execute @e[type=fox,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0","execute @e[type=squid,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0","execute @e[type=elder_guardian,rm=2,r=12] ~ ~ ~ fill ~2 ~-1 ~2 ~-2 ~3 ~-2 effect99:fake_ice 0 replace air 0","execute @e[type=bat,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0","execute @e[type=ghast,rm=2,r=12] ~ ~ ~ fill ~4 ~-3 ~4 ~-4 ~4 ~-4 effect99:fake_ice 0 replace air 0","execute @e[type=ghast,rm=2,r=12] ~ ~ ~ fill ~3 ~-2 ~3 ~-3 ~3 ~-3 air 0 replace effect99:fake_ice","execute @e[type=horse,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0","execute @e[type=horse,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ air 0 replace effect99:fake_ice 0","execute @e[type=player,rm=3,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 effect99:fake_ice 0 replace air 0","title @s actionbar §l§bIce Skill","playsound random.fizz @a[r=12] ~ ~ ~ 1 2.3","particle minecraft:knockback_roar_particle ~ ~1 ~"],"target":"holder"}}`
  - `$.sequence[1]` — поля действия: `{"damage":{"type":"durability","amount":6,"target":"self"}}`

**Событие `weapon`** (упоминания в исходнике: строки 69, 72, 75, 141):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`
  - `$.sequence[1].randomize`: альтернативы, веса `[70,30]`, сумма 100:
    - ветвь 0, weight `70`; условная доля 7/10 (70%):
      - пустое действие
    - ветвь 1, weight `30`; условная доля 3/10 (30%):
      - `$.sequence[1].randomize[1]` — поля действия: `{"shoot":{"projectile":"minecraft:snowball","launch_power":1},"run_command":{"command":["playsound random.bow @a[r=10] ~ ~ ~ 1 0.4"]}}`

**Прямые ссылки на сущности из текстовых значений item** (распознавание идентификаторов; не все они обязательно вызываются):
- `minecraft:snowball` → `Swords_B/entities/snowball.json`

**Таблицы добычи с буквальным ID и прямые упоминания этих таблиц:**
- `Swords_B/loot_tables/chests/igloo_chest.json` → прямых текстовых ссылок не найдено; возможна регистрация движком/косвенная ссылка
- `Swords_B/loot_tables/chests/village/village_snowy_house.json` → прямых текстовых ссылок не найдено; возможна регистрация движком/косвенная ссылка

### effect:jungle_sword

- Файл `Swords_B/items/jungle_sword.json`; format_version `"1.16.100"`.
- Урон `4`; прочность `{"max_durability":128}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:jungle_sword"],"repair_amount":128}]}`.
- Оффхенд `false`; hand_equipped `true`; foil `false`; icon `{"texture":"jungle_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"}}}`.

**Событие `weapon`** (упоминания в исходнике: строки 58, 63):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`

**Таблицы добычи с буквальным ID и прямые упоминания этих таблиц:**
- `Swords_B/loot_tables/chests/jungle_temple.json` → прямых текстовых ссылок не найдено; возможна регистрация движком/косвенная ссылка
- `Swords_B/loot_tables/gameplay/fishing/treasure.json` → `Swords_B/loot_tables/gameplay/fishing.json`:14; `Swords_B/loot_tables/gameplay/jungle_fishing.json`:14

### effect:lapis_sword

- Файл `Swords_B/items/lapis_sword.json`; format_version `"1.16.100"`.
- Урон `5`; прочность `{"max_durability":528}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:lapis_sword"],"repair_amount":528},{"items":["minecraft:lapis_lazuli"],"repair_amount":48}]}`.
- Оффхенд `false`; hand_equipped `true`; foil `false`; icon `{"texture":"lapis_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"}}}`.

**Событие `weapon`** (упоминания в исходнике: строки 60, 65):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`

**Таблицы добычи с буквальным ID и прямые упоминания этих таблиц:**
- `Swords_B/loot_tables/chests/pillager_outpost.json` → прямых текстовых ссылок не найдено; возможна регистрация движком/косвенная ссылка
- `Swords_B/loot_tables/chests/stronghold_corridor.json` → прямых текстовых ссылок не найдено; возможна регистрация движком/косвенная ссылка
- `Swords_B/loot_tables/chests/stronghold_library.json` → прямых текстовых ссылок не найдено; возможна регистрация движком/косвенная ссылка

### effect:lightning_sword

- Файл `Swords_B/items/lightning_sword.json`; format_version `"1.16.100"`.
- Урон `8`; прочность `{"max_durability":2012}`; стак `1`; перезарядка `{"category":"lightning_sword","duration":12}`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:lightning_sword"],"repair_amount":2012}]}`.
- Оффхенд `false`; hand_equipped `true`; foil `true`; icon `{"texture":"lightning_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{"minecraft:on_use":{"on_use":{"event":"on_use"}},"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"},"on_not_hurt_entity":{"event":"weapon"},"on_hit_block":{"event":"weapon"}}}`.

**Событие `on_use`** (упоминания в исходнике: строки 85, 86, 102):

- `$` — поля действия: `{"run_command":{"command":["summon lightning_bolt ~ ~2 ~ default_lightning_bolt","summon lightning_bolt ~7 ~ ~ default_lightning_bolt","summon lightning_bolt ~ ~ ~7 default_lightning_bolt","summon lightning_bolt ~-7 ~ ~ default_lightning_bolt","summon lightning_bolt ~ ~ ~-7 default_lightning_bolt","summon lightning_bolt ~6 ~ ~6 default_lightning_bolt","summon lightning_bolt ~-6 ~ ~-6 default_lightning_bolt","summon lightning_bolt ~-6 ~ ~6 default_lightning_bolt","summon lightning_bolt ~6 ~ ~-6 default_lightning_bolt","summon lightning_bolt ~14 ~ ~ default_lightning_bolt","summon lightning_bolt ~ ~ ~14 default_lightning_bolt","summon lightning_bolt ~-14 ~ ~ default_lightning_bolt","summon lightning_bolt ~ ~ ~-14 default_lightning_bolt","summon lightning_bolt ~12 ~ ~12 default_lightning_bolt","summon lightning_bolt ~-12 ~ ~-12 default_lightning_bolt","summon lightning_bolt ~-12 ~ ~12 default_lightning_bolt","summon lightning_bolt ~12 ~ ~-12 default_lightning_bolt","summon lightning_bolt ~28 ~ ~ default_lightning_bolt","summon lightning_bolt ~ ~ ~28 default_lightning_bolt","summon lightning_bolt ~-28 ~ ~ default_lightning_bolt","summon lightning_bolt ~ ~ ~-28 default_lightning_bolt","summon lightning_bolt ~24 ~ ~24 default_lightning_bolt","summon lightning_bolt ~-24 ~ ~-24 default_lightning_bolt","summon lightning_bolt ~-24 ~ ~24 default_lightning_bolt","summon lightning_bolt ~24 ~ ~-24 default_lightning_bolt","summon lightning_bolt ~34 ~ ~ default_lightning_bolt","summon lightning_bolt ~ ~ ~34 default_lightning_bolt","summon lightning_bolt ~-34 ~ ~ default_lightning_bolt","summon lightning_bolt ~ ~ ~-34 default_lightning_bolt","summon lightning_bolt ~30 ~ ~30 default_lightning_bolt","summon lightning_bolt ~-30 ~ ~-30 default_lightning_bolt","summon lightning_bolt ~-30 ~ ~30 default_lightning_bolt","summon lightning_bolt ~30 ~ ~-30 default_lightning_bolt","summon lightning_bolt ~42 ~ ~ default_lightning_bolt","summon lightning_bolt ~ ~ ~42 default_lightning_bolt","summon lightning_bolt ~-42 ~ ~ default_lightning_bolt","summon lightning_bolt ~ ~ ~-42 default_lightning_bolt","summon lightning_bolt ~38 ~ ~38 default_lightning_bolt","summon lightning_bolt ~-38 ~ ~-38 default_lightning_bolt","summon lightning_bolt ~-38 ~ ~38 default_lightning_bolt","summon lightning_bolt ~38 ~ ~-38 default_lightning_bolt"]},"damage":{"type":"durability","amount":9,"target":"self"}}`

**Событие `weapon`** (упоминания в исходнике: строки 91, 94, 97, 155):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`
  - `$.sequence[1].randomize`: альтернативы, веса `[15,85]`, сумма 100:
    - ветвь 0, weight `15`; условная доля 3/20 (15%):
      - пустое действие
    - ветвь 1, weight `85`; условная доля 17/20 (85%):
      - `$.sequence[1].randomize[1]` — поля действия: `{"shoot":{"projectile":"entity:lightning_projectile","launch_power":1}}`

**Прямые ссылки на сущности из текстовых значений item** (распознавание идентификаторов; не все они обязательно вызываются):
- `entity:lightning_projectile` → `Swords_B/entities/lightning_projectile.json`

### effect:magma_sword

- Файл `Swords_B/items/magma_sword.json`; format_version `"1.16.100"`.
- Урон `7.2`; прочность `{"max_durability":1316}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:magma_sword"],"repair_amount":1316},{"items":["minecraft:magma"],"repair_amount":100}]}`.
- Оффхенд `false`; hand_equipped `true`; foil `false`; icon `{"texture":"magma_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"}}}`.

**Событие `weapon`** (упоминания в исходнике: строки 60, 65):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`

**Таблицы добычи с буквальным ID и прямые упоминания этих таблиц:**
- `Swords_B/loot_tables/chests/underwater_ruin_big.json` → прямых текстовых ссылок не найдено; возможна регистрация движком/косвенная ссылка

### effect:nether_star_sword

- Файл `Swords_B/items/nether_star_sword.json`; format_version `"1.16.100"`.
- Урон `7`; прочность `{"max_durability":3256}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:nether_star_sword"],"repair_amount":3256},{"items":["minecraft:nether_star"],"repair_amount":3000}]}`.
- Оффхенд `false`; hand_equipped `true`; foil `true`; icon `{"texture":"nether_star_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"},"on_not_hurt_entity":{"event":"weapon"},"on_hit_block":{"event":"weapon"}}}`.

**Событие `weapon`** (упоминания в исходнике: строки 62, 65, 68, 73):

- `$.sequence`: 3 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"shoot":{"projectile":"entity:nether_star_projectile","launch_power":1}}`
  - `$.sequence[1].randomize`: альтернативы, веса `[80,20]`, сумма 100:
    - ветвь 0, weight `80`; условная доля 4/5 (80%):
      - `$.sequence[1].randomize[0]` — поля действия: `{"run_command":{"command":["summon entity:nether_star ^ ^20 ^-6"]}}`
    - ветвь 1, weight `20`; условная доля 1/5 (20%):
      - `$.sequence[1].randomize[1]` — поля действия: `{"run_command":{"command":["summon entity:nether_star ^ ^20 ^-6","summon entity:nether_star ^ ^18 ^-6"]}}`
  - `$.sequence[2].randomize`: альтернативы, веса `[9999,1]`, сумма 10000:
    - ветвь 0, weight `9999`; условная доля 9999/10000 (99.99%):
      - `$.sequence[2].randomize[0]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`
    - ветвь 1, weight `1`; условная доля 1/10000 (0.01%):
      - `$.sequence[2].randomize[1]` — поля действия: `{"run_command":{"command":["summon entity:ultra_instinct_explode"]}}`

**Прямые ссылки на сущности из текстовых значений item** (распознавание идентификаторов; не все они обязательно вызываются):
- `entity:nether_star` → `Swords_B/entities/entity_nether_star.json`
- `entity:nether_star_projectile` → `Swords_B/entities/nether_star_projectile.json`
- `entity:ultra_instinct_explode` → `Swords_B/entities/ultra_instinct_explode.json`

### effect:obsidian_sword

- Файл `Swords_B/items/obsidian_sword.json`; format_version `"1.16.100"`.
- Урон `8`; прочность `{"max_durability":3000}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:obsidian_sword"],"repair_amount":3000},{"items":["minecraft:obsidian"],"repair_amount":120}]}`.
- Оффхенд `false`; hand_equipped `true`; foil `false`; icon `{"texture":"obsidian_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"}}}`.

**Событие `weapon`** (упоминания в исходнике: строки 61, 66):

- `$.randomize`: альтернативы, веса `[55,30,15]`, сумма 100:
  - ветвь 0, weight `55`; условная доля 11/20 (55%):
    - `$.randomize[0]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`
  - ветвь 1, weight `30`; условная доля 3/10 (30%):
    - `$.randomize[1]` — поля действия: `{"damage":{"type":"durability","amount":2,"target":"self"}}`
  - ветвь 2, weight `15`; условная доля 3/20 (15%):
    - `$.randomize[2]` — поля действия: `{"damage":{"type":"durability","amount":3,"target":"self"}}`

### effect:cursed_pumpkin_sword

- Файл `Swords_B/items/pumpkin_sword.json`; format_version `"1.16.100"`.
- Урон `5`; прочность `{"max_durability":606}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:cursed_pumpkin_sword"],"repair_amount":606},{"items":["minecraft:honey_block"],"repair_amount":400},{"items":["minecraft:honeycomb"],"repair_amount":150}]}`.
- Оффхенд `false`; hand_equipped `true`; foil `false`; icon `{"texture":"cursed_pumpkin_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"},"on_not_hurt_entity":{"event":"weapon"},"on_hit_block":{"event":"weapon"}}}`.

**Событие `weapon`** (упоминания в исходнике: строки 66, 69, 72, 77):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`
  - `$.sequence[1].randomize`: альтернативы, веса `[80,20]`, сумма 100:
    - ветвь 0, weight `80`; условная доля 4/5 (80%):
      - `$.sequence[1].randomize[0]` — поля действия: `{"shoot":{"projectile":"entity:pumpkin_projectile","launch_power":1}}`
    - ветвь 1, weight `20`; условная доля 1/5 (20%):
      - пустое действие

**Прямые ссылки на сущности из текстовых значений item** (распознавание идентификаторов; не все они обязательно вызываются):
- `entity:pumpkin_projectile` → `Swords_B/entities/pumpkin_projectile.json`

**Таблицы добычи с буквальным ID и прямые упоминания этих таблиц:**
- `Swords_B/loot_tables/pumpkin_sword.json` → `Swords_B/scripts/javascript.js`:8

### effect:quartz_diamond

- Файл `Swords_B/items/quartz_diamond.json`; format_version `"1.16.100"`.
- Урон `"не задан"`; прочность `"не задана"`; стак `9`; перезарядка `"не задана"`.
- Зачарование `"не задано"`; ремонт `"не задан"`.
- Оффхенд `"не задан"`; hand_equipped `false`; foil `true`; icon `{"texture":"quartz_diamond"}`.
- Скорости добычи `"не заданы"`.

**Привязки триггеров:** `{}`.

Прямых item events в файле нет; это не исключает пассивные и косвенные механики.

**Таблицы добычи с буквальным ID и прямые упоминания этих таблиц:**
- `Swords_B/loot_tables/blocks/quartz_diamond_ore.json` → `Swords_B/blocks/quartz_diamond_ore.json`:22

### effect:quartz_diamond_stick

- Файл `Swords_B/items/quartz_diamond_stick.json`; format_version `"1.16.100"`.
- Урон `24`; прочность `{"max_durability":20}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `"не задано"`; ремонт `"не задан"`.
- Оффхенд `false`; hand_equipped `true`; foil `true`; icon `{"texture":"quartz_diamond_stick"}`.
- Скорости добычи `"не заданы"`.

**Привязки триггеров:** `{"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"},"on_not_hurt_entity":{"event":"weapon"},"on_hit_block":{"event":"weapon"}}}`.

**Событие `weapon`** (упоминания в исходнике: строки 25, 28, 31, 36):

- `$.randomize`: альтернативы, веса `[10,85,5]`, сумма 100:
  - ветвь 0, weight `10`; условная доля 1/10 (10%):
    - `$.randomize[0]` — поля действия: `{"run_command":{"command":["damage @s 1 magic"]}}`
  - ветвь 1, weight `85`; условная доля 17/20 (85%):
    - `$.randomize[1]` — поля действия: `{"run_command":{"command":["damage @s 3 magic"]}}`
  - ветвь 2, weight `5`; условная доля 1/20 (5%):
    - `$.randomize[2]` — поля действия: `{"run_command":{"command":["damage @s 6 magic"]}}`

### effect:quartz_sword

- Файл `Swords_B/items/quartz_sword.json`; format_version `"1.16.100"`.
- Урон `600`; прочность `{"max_durability":1}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `"не задано"`; ремонт `"не задан"`.
- Оффхенд `false`; hand_equipped `true`; foil `true`; icon `{"texture":"quartz_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"},"on_not_hurt_entity":{"event":"weapon"},"on_hit_block":{"event":"weapon"}}}`.

**Событие `weapon`** (упоминания в исходнике: строки 68, 71, 74, 79):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"damage":{"type":"durability","amount":10,"target":"self"}}`
  - `$.sequence[1]` — поля действия: `{"run_command":{"command":["effect @a[r=1] instant_damage 1 99 true","particle minecraft:knockback_roar_particle ~ ~1 ~"]}}`

### effect:sea_sword

- Файл `Swords_B/items/sea_sword.json`; format_version `"1.16.100"`.
- Урон `7`; прочность `{"max_durability":1356}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:sea_sword"],"repair_amount":1356},{"items":["minecraft:heart_of_the_sea"],"repair_amount":482}]}`.
- Оффхенд `false`; hand_equipped `true`; foil `true`; icon `{"texture":"sea_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"}}}`.

**Событие `weapon`** (упоминания в исходнике: строки 60, 65):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`

**Таблицы добычи с буквальным ID и прямые упоминания этих таблиц:**
- `Swords_B/loot_tables/chests/buriedtreasure.json` → прямых текстовых ссылок не найдено; возможна регистрация движком/косвенная ссылка

### effect:shulker_sword

- Файл `Swords_B/items/shulker_sword.json`; format_version `"1.16.100"`.
- Урон `6`; прочность `{"max_durability":2609}`; стак `1`; перезарядка `{"category":"shulker_sword","duration":8}`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:shulker_sword"],"repair_amount":2609}]}`.
- Оффхенд `false`; hand_equipped `true`; foil `false`; icon `{"texture":"shulker_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{"minecraft:on_use":{"on_use":{"event":"on_use"}},"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"},"on_not_hurt_entity":{"event":"weapon"},"on_hit_block":{"event":"weapon"}}}`.

**Событие `on_use`** (упоминания в исходнике: строки 57, 58, 74):

- `$` — поля действия: `{"run_command":{"command":["particle minecraft:cauldron_explosion_emitter ~3 ~ ~","particle minecraft:cauldron_explosion_emitter ~ ~ ~3","particle minecraft:cauldron_explosion_emitter ~-3 ~ ~","particle minecraft:cauldron_explosion_emitter ~ ~ ~-3","particle minecraft:cauldron_explosion_emitter ~-2.5 ~ ~2.5","particle minecraft:cauldron_explosion_emitter ~2.5 ~ ~-2.5","particle minecraft:cauldron_explosion_emitter ~2.5 ~ ~2.5","particle minecraft:cauldron_explosion_emitter ~-2.5 ~ ~-2.5","effect @e[r=6,family=!shulker_sword] levitation 1 18 false"]},"damage":{"type":"durability","amount":8,"target":"self"}}`

**Событие `weapon`** (упоминания в исходнике: строки 63, 66, 69, 94):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`
  - `$.sequence[1].randomize`: альтернативы, веса `[10,90]`, сумма 100:
    - ветвь 0, weight `10`; условная доля 1/10 (10%):
      - `$.sequence[1].randomize[0]` — поля действия: `{"shoot":{"projectile":"minecraft:shulker_bullet","launch_power":1},"run_command":{"command":["playsound random.bow @a[r=10] ~ ~ ~ 1 0.4"]}}`
    - ветвь 1, weight `90`; условная доля 9/10 (90%):
      - пустое действие

**Прямые ссылки на сущности из текстовых значений item** (распознавание идентификаторов; не все они обязательно вызываются):
- `minecraft:shulker_bullet` → `Swords_B/entities/shulker_bullet.json`

**Таблицы добычи с буквальным ID и прямые упоминания этих таблиц:**
- `Swords_B/loot_tables/entities/shulker.json` → прямых текстовых ссылок не найдено; возможна регистрация движком/косвенная ссылка

### effect:silver_ingot

- Файл `Swords_B/items/silver_ingot.json`; format_version `"1.16.100"`.
- Урон `"не задан"`; прочность `"не задана"`; стак `64`; перезарядка `"не задана"`.
- Зачарование `"не задано"`; ремонт `"не задан"`.
- Оффхенд `"не задан"`; hand_equipped `false`; foil `"не задан"`; icon `{"texture":"silver_ingot"}`.
- Скорости добычи `"не заданы"`.

**Привязки триггеров:** `{}`.

Прямых item events в файле нет; это не исключает пассивные и косвенные механики.

### effect:silver_sword

- Файл `Swords_B/items/silver_sword.json`; format_version `"1.16.100"`.
- Урон `6`; прочность `{"max_durability":1800}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:silver_sword"],"repair_amount":1800}]}`.
- Оффхенд `false`; hand_equipped `true`; foil `false`; icon `{"texture":"silver_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"}}}`.

**Событие `weapon`** (упоминания в исходнике: строки 72, 77):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`

### effect:slime_sword

- Файл `Swords_B/items/slime_sword.json`; format_version `"1.16.100"`.
- Урон `6`; прочность `{"max_durability":675}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:slime_sword"],"repair_amount":675},{"items":["minecraft:slime"],"repair_amount":48}]}`.
- Оффхенд `false`; hand_equipped `true`; foil `false`; icon `{"texture":"slime_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"}}}`.

**Событие `weapon`** (упоминания в исходнике: строки 60, 65):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`

**Таблицы добычи с буквальным ID и прямые упоминания этих таблиц:**
- `Swords_B/loot_tables/entities/slime_king.json` → прямых текстовых ссылок не найдено; возможна регистрация движком/косвенная ссылка

### effect:spectral_sword

- Файл `Swords_B/items/spectral_sword.json`; format_version `"1.16.100"`.
- Урон `9`; прочность `{"max_durability":3256}`; стак `1`; перезарядка `{"category":"spectral_sword","duration":18}`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:spectral_sword"],"repair_amount":3256},{"items":["minecraft:end_crystal"],"repair_amount":620},{"items":["minecraft:nether_star"],"repair_amount":2052}]}`.
- Оффхенд `false`; hand_equipped `true`; foil `true`; icon `{"texture":"spectral_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{"minecraft:on_use":{"on_use":{"event":"on_use"}},"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"},"on_not_hurt_entity":{"event":"weapon"},"on_hit_block":{"event":"weapon"}}}`.

**Событие `on_use`** (упоминания в исходнике: строки 89, 90, 106):

- `$` — поля действия: `{"damage":{"type":"durability","amount":15,"target":"self"},"shoot":{"projectile":"entity:ender_crystal_projectile","launch_power":1},"run_command":{"command":["playsound portal.travel @a[r=16] ~ ~ ~ 1 5","event entity @e[type=ender_crystal,family=!ender_crystal_default,family=!ender_crystal_scale,c=1,r=4] minecraft:ender_crystal_scale"]}}`

**Событие `weapon`** (упоминания в исходнике: строки 95, 98, 101, 123):

- `$.randomize`: альтернативы, веса `[99,1]`, сумма 100:
  - ветвь 0, weight `99`; условная доля 99/100 (99%):
    - `$.randomize[0]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`
  - ветвь 1, weight `1`; условная доля 1/100 (1%):
    - `$.randomize[1]` — поля действия: `{"run_command":{"command":["event entity @e[type=ender_crystal,family=!ender_crystal_default,family=!ender_crystal_scale,c=1] minecraft:crystal_explode"]}}`

**Прямые ссылки на сущности из текстовых значений item** (распознавание идентификаторов; не все они обязательно вызываются):
- `entity:ender_crystal_projectile` → `Swords_B/entities/ender_crystal_projectile.json`

### effect:spider_sword

- Файл `Swords_B/items/spider_sword.json`; format_version `"1.16.100"`.
- Урон `5`; прочность `{"max_durability":628}`; стак `1`; перезарядка `{"category":"spider_sword","duration":28}`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:spider_sword"],"repair_amount":628},{"items":["minecraft:web"],"repair_amount":128},{"items":["minecraft:spider_eye"],"repair_amount":48}]}`.
- Оффхенд `false`; hand_equipped `true`; foil `false`; icon `{"texture":"spider_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":100},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{"minecraft:on_use":{"on_use":{"event":"on_use"}},"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"},"on_not_hurt_entity":{"event":"weapon"},"on_hit_block":{"event":"weapon"}}}`.

**Событие `on_use`** (упоминания в исходнике: строки 69, 70, 86):

- `$` — поля действия: `{"run_command":{"command":["event entity @s spider_sword_skill"],"target":"holder"},"damage":{"type":"durability","amount":8,"target":"self"}}`

**Событие `weapon`** (упоминания в исходнике: строки 75, 78, 81, 98):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`
  - `$.sequence[1].randomize`: альтернативы, веса `[95,5]`, сумма 100:
    - ветвь 0, weight `95`; условная доля 19/20 (95%):
      - пустое действие
    - ветвь 1, weight `5`; условная доля 1/20 (5%):
      - `$.sequence[1].randomize[1]` — поля действия: `{"shoot":{"projectile":"entity:web","launch_power":1}}`

**Прямые ссылки на сущности из текстовых значений item** (распознавание идентификаторов; не все они обязательно вызываются):
- `entity:web` → `Swords_B/entities/web.json`

**Таблицы добычи с буквальным ID и прямые упоминания этих таблиц:**
- `Swords_B/loot_tables/chests/abandoned_mineshaft.json` → прямых текстовых ссылок не найдено; возможна регистрация движком/косвенная ссылка

### effect:sponge_sword

- Файл `Swords_B/items/sponge_sword.json`; format_version `"1.16.100"`.
- Урон `5`; прочность `{"max_durability":128}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `"не задано"`; ремонт `{"repair_items":[{"items":["effect:sponge_sword"],"repair_amount":128},{"items":["minecraft:sponge"],"repair_amount":62}]}`.
- Оффхенд `false`; hand_equipped `true`; foil `false`; icon `{"texture":"sponge_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"}}}`.

**Событие `weapon`** (упоминания в исходнике: строки 56, 61):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`

**Таблицы добычи с буквальным ID и прямые упоминания этих таблиц:**
- `Swords_B/loot_tables/entities/elder_guardian.json` → прямых текстовых ссылок не найдено; возможна регистрация движком/косвенная ссылка

### effect:time_sword

- Файл `Swords_B/items/time_sword.json`; format_version `"1.16.100"`.
- Урон `13`; прочность `{"max_durability":13770}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `"не задан"`.
- Оффхенд `false`; hand_equipped `true`; foil `true`; icon `{"texture":"time_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"},"on_not_hurt_entity":{"event":"weapon"},"on_hit_block":{"event":"weapon"}}}`.

**Событие `weapon`** (упоминания в исходнике: строки 72, 75, 78, 83):

- `$.randomize`: альтернативы, веса `[90,6,3,1]`, сумма 100:
  - ветвь 0, weight `90`; условная доля 9/10 (90%):
    - `$.randomize[0]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`
  - ветвь 1, weight `6`; условная доля 3/50 (6%):
    - `$.randomize[1]` — поля действия: `{"damage":{"type":"durability","amount":16,"target":"self"}}`
  - ветвь 2, weight `3`; условная доля 3/100 (3%):
    - `$.randomize[2]` — поля действия: `{"damage":{"type":"durability","amount":32,"target":"self"}}`
  - ветвь 3, weight `1`; условная доля 1/100 (1%):
    - `$.randomize[3]` — поля действия: `{"damage":{"type":"durability","amount":64,"target":"self"}}`

### effect:tnt_sword

- Файл `Swords_B/items/tnt_sword.json`; format_version `"1.16.100"`.
- Урон `4`; прочность `{"max_durability":64}`; стак `1`; перезарядка `{"category":"tnt_sword","duration":10}`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:tnt_sword"],"repair_amount":64},{"items":["minecraft:tnt"],"repair_amount":18}]}`.
- Оффхенд `false`; hand_equipped `true`; foil `false`; icon `{"texture":"tnt_sword"}`.
- Скорости добычи `"не заданы"`.

**Привязки триггеров:** `{"minecraft:on_use":{"on_use":{"event":"on_use"}},"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"},"on_not_hurt_entity":{"event":"weapon"},"on_hit_block":{"event":"weapon"}}}`.

**Событие `on_use`** (упоминания в исходнике: строки 50, 51, 67):

- `$` — поля действия: `{"run_command":{"command":["summon minecraft:tnt ~~~ giant_tnt","title @a[r=18] actionbar §fSuper§4TNT §f§lhas been activated.","playsound random.fuse @a ~~~"]},"damage":{"type":"durability","amount":18,"target":"self"}}`

**Событие `weapon`** (упоминания в исходнике: строки 56, 59, 62, 77):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`
  - `$.sequence[1].randomize`: альтернативы, веса `[10,90]`, сумма 100:
    - ветвь 0, weight `10`; условная доля 1/10 (10%):
      - пустое действие
    - ветвь 1, weight `90`; условная доля 9/10 (90%):
      - `$.sequence[1].randomize[1]` — поля действия: `{"shoot":{"projectile":"entity:tnt","launch_power":1}}`

**Прямые ссылки на сущности из текстовых значений item** (распознавание идентификаторов; не все они обязательно вызываются):
- `entity:tnt` → `Swords_B/entities/entity_tnt.json`
- `minecraft:tnt` → `Swords_B/entities/tnt.json`

**Таблицы добычи с буквальным ID и прямые упоминания этих таблиц:**
- `Swords_B/loot_tables/chests/desert_pyramid.json` → прямых текстовых ссылок не найдено; возможна регистрация движком/косвенная ссылка

### effect:ultra_instinct_sword

- Файл `Swords_B/items/ultra_instinct_sword.json`; format_version `"1.16.100"`.
- Урон `16`; прочность `{"max_durability":9999}`; стак `1`; перезарядка `{"category":"ultra_instinct_sword","duration":61}`.
- Зачарование `"не задано"`; ремонт `"не задан"`.
- Оффхенд `false`; hand_equipped `true`; foil `true`; icon `{"texture":"ultra_instinct_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":999},{"block":"minecraft:bamboo","speed":999}]}`.

**Привязки триггеров:** `{"minecraft:on_use":{"on_use":{"event":"on_use"}},"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"}}}`.

**Событие `on_use`** (упоминания в исходнике: строки 78, 79, 89):

- `$` — поля действия: `{"shoot":{"projectile":"entity:ultra_instinct_projectile","launch_power":1},"damage":{"type":"durability","amount":48,"target":"self"},"run_command":{"command":["playsound mob.wither.ambient @s ~ ~1 ~ 2 0.6"]}}`

**Событие `weapon`** (упоминания в исходнике: строки 84, 101):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`

**Прямые ссылки на сущности из текстовых значений item** (распознавание идентификаторов; не все они обязательно вызываются):
- `entity:ultra_instinct_projectile` → `Swords_B/entities/ultra_instinct_projectile.json`

### effect:wet_sponge_sword

- Файл `Swords_B/items/wet_sponge_sword.json`; format_version `"1.16.100"`.
- Урон `3`; прочность `{"max_durability":64}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `"не задано"`; ремонт `{"repair_items":[{"items":["effect:sponge_sword"],"repair_amount":64},{"items":["minecraft:sponge"],"repair_amount":32},{"items":["effect:wet_sponge_sword"],"repair_amount":64}]}`.
- Оффхенд `false`; hand_equipped `true`; foil `false`; icon `{"texture":"wet_sponge_sword"}`.
- Скорости добычи `"не заданы"`.

**Привязки триггеров:** `{"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"}}}`.

**Событие `weapon`** (упоминания в исходнике: строки 49, 54):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`

### effect:wither_skeleton_sword

- Файл `Swords_B/items/wither_skeleton_sword.json`; format_version `"1.16.100"`.
- Урон `4`; прочность `{"max_durability":128}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:wither_skeleton_sword"],"repair_amount":128},{"items":["minecraft:coal"],"repair_amount":58},{"items":["minecraft:stick"],"repair_amount":2}]}`.
- Оффхенд `false`; hand_equipped `true`; foil `false`; icon `{"texture":"wither_skeleton_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"}}}`.

**Событие `weapon`** (упоминания в исходнике: строки 66, 71):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"},"shoot":{"projectile":"entity:wither_effect","launch_power":1}}`

**Прямые ссылки на сущности из текстовых значений item** (распознавание идентификаторов; не все они обязательно вызываются):
- `entity:wither_effect` → `Swords_B/entities/wither_effect.json`

**Таблицы добычи с буквальным ID и прямые упоминания этих таблиц:**
- `Swords_B/loot_tables/entities/wither_skeleton.json` → прямых текстовых ссылок не найдено; возможна регистрация движком/косвенная ссылка

### effect:wither_sword

- Файл `Swords_B/items/wither_sword.json`; format_version `"1.16.100"`.
- Урон `10`; прочность `{"max_durability":3856}`; стак `1`; перезарядка `{"category":"wither_sword","duration":3}`.
- Зачарование `"не задано"`; ремонт `{"repair_items":[{"items":["effect:wither_sword"],"repair_amount":3856}]}`.
- Оффхенд `false`; hand_equipped `true`; foil `true`; icon `{"texture":"wither_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{"minecraft:on_use":{"on_use":{"event":"on_use"}},"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"},"on_not_hurt_entity":{"event":"weapon"},"on_hit_block":{"event":"weapon"}}}`.

**Событие `on_use`** (упоминания в исходнике: строки 83, 84, 100):

- `$` — поля действия: `{"shoot":{"projectile":"minecraft:wither_skull_dangerous","launch_power":1},"run_command":{"command":["playsound mob.wither.shoot @a[r=16] ~~~ 1 0.7"]},"damage":{"type":"durability","amount":3,"target":"self"}}`

**Событие `weapon`** (упоминания в исходнике: строки 89, 92, 95, 114):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`
  - `$.sequence[1].randomize`: альтернативы, веса `[90,10]`, сумма 100:
    - ветвь 0, weight `90`; условная доля 9/10 (90%):
      - пустое действие
    - ветвь 1, weight `10`; условная доля 1/10 (10%):
      - `$.sequence[1].randomize[1]` — поля действия: `{"shoot":{"projectile":"minecraft:wither_skull","launch_power":1},"run_command":{"command":["playsound mob.wither.shoot @a[r=16]"]}}`

**Прямые ссылки на сущности из текстовых значений item** (распознавание идентификаторов; не все они обязательно вызываются):
- `minecraft:wither_skull` → `Swords_B/entities/wither_skull.json`
- `minecraft:wither_skull_dangerous` → `Swords_B/entities/wither_skull_dangerous.json`

### effect:wolf_sword

- Файл `Swords_B/items/wolf_sword.json`; format_version `"1.16.100"`.
- Урон `5`; прочность `{"max_durability":2800}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `"не задано"`; ремонт `{"repair_items":[{"items":["effect:wolf_sword"],"repair_amount":2800}]}`.
- Оффхенд `false`; hand_equipped `true`; foil `false`; icon `{"texture":"wolf_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{"minecraft:weapon":{"on_hurt_entity":{"event":"weapon"}}}`.

**Событие `weapon`** (упоминания в исходнике: строки 68, 73):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"damage":{"type":"durability","amount":1,"target":"self"}}`

