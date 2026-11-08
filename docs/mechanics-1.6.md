# Сводка прямых механик предметов — архив 1.6

Машинный индекс непосредственно объявленных данных предметов. Это **не** полное описание поведения: эффекты игрока, сущности, скрытые цепочки и поведение движка разбираются отдельно. Путь исходника и номера строк относятся к архиву из `sources/`.

Доли randomize рассчитаны как weight / сумма явно заданных неотрицательных целых весов в том же массиве. Это условная доля при выборе ветви, не вероятность успешного результата; фильтры, вложенность и триггер влияют на итог. При отсутствующем весе доли не вычисляются. Соседние поля объекта показаны вместе без предположений об их порядке.

## Общая таблица

| ID | Урон | Прочность max | Cooldown (category, duration) | Крюки |
|---|---:|---:|---|---|
| `effect:sword_of_time` | `7` | `128` | `"—"` | — |
| `effect:blaze_sword` | `8` | `2300` | `"—"` | — |
| `effect:bone_sword` | `7` | `820` | `"—"` | — |
| `effect:cactus_sword` | `6` | `125` | `"—"` | — |
| `effect:coal_sword` | `6` | `121` | `"—"` | — |
| `effect:creeper_sword` | `8` | `1500` | `"—"` | — |
| `effect:emerald_sword` | `7` | `2300` | `"—"` | — |
| `effect:ender_sword` | `9` | `1256` | `"—"` | — |
| `effect:fire_sword` | `12` | `2000` | `"—"` | — |
| `effect:glowstone_sword` | `6` | `128` | `"—"` | — |
| `effect:grass_sword` | `8` | `250` | `"—"` | — |
| `effect:ice_sword` | `11` | `500` | `"—"` | — |
| `effect:jungle_sword` | `4` | `128` | `"—"` | — |
| `effect:lapis_sword` | `6` | `528` | `"—"` | — |
| `effect:lightning_sword` | `8` | `2000` | `"—"` | — |
| `effect:magma_sword` | `7` | `1000` | `"—"` | — |
| `effect:obsidian_sword` | `12` | `3000` | `"—"` | — |
| `effect:quartz_sword` | `600` | `1` | `"—"` | — |
| `effect:sea_sword` | `7` | `1000` | `"—"` | — |
| `effect:shulker_sword` | `7` | `1000` | `"—"` | — |
| `effect:slime_sword` | `6` | `675` | `"—"` | — |
| `effect:spectral_sword` | `9` | `3256` | `"—"` | — |
| `effect:spider_sword` | `6` | `628` | `"—"` | — |
| `effect:sponge_sword` | `6` | `128` | `"—"` | — |
| `effect:tnt_sword` | `7` | `1` | `"—"` | — |
| `effect:wither_sword` | `10` | `1256` | `"—"` | — |

## Карточки

### effect:sword_of_time

- Файл `Sword_B/items/Sword of Time.json`; format_version `"1.20.20"`.
- Урон `7`; прочность `{"max_durability":128}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:sword_of_time"],"repair_amount":128}]}`.
- Оффхенд `true`; hand_equipped `true`; foil `"не задан"`; icon `{"texture":"sword_of_time"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{}`.

Прямых item events в файле нет; это не исключает пассивные и косвенные механики.

### effect:blaze_sword

- Файл `Sword_B/items/blaze_sword.json`; format_version `"1.20.20"`.
- Урон `8`; прочность `{"max_durability":2300}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:blaze_sword"],"repair_amount":2300}]}`.
- Оффхенд `true`; hand_equipped `true`; foil `"не задан"`; icon `{"texture":"blaze_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{}`.

Прямых item events в файле нет; это не исключает пассивные и косвенные механики.

### effect:bone_sword

- Файл `Sword_B/items/bone_sword.json`; format_version `"1.20.20"`.
- Урон `7`; прочность `{"max_durability":820}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:bone_sword"],"repair_amount":820}]}`.
- Оффхенд `true`; hand_equipped `true`; foil `"не задан"`; icon `{"texture":"bone_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{}`.

Прямых item events в файле нет; это не исключает пассивные и косвенные механики.

### effect:cactus_sword

- Файл `Sword_B/items/cactus_sword.json`; format_version `"1.20.20"`.
- Урон `6`; прочность `{"max_durability":125}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:cactus_sword"],"repair_amount":125}]}`.
- Оффхенд `true`; hand_equipped `true`; foil `"не задан"`; icon `{"texture":"cactus_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{}`.

Прямых item events в файле нет; это не исключает пассивные и косвенные механики.

### effect:coal_sword

- Файл `Sword_B/items/coal_sword.json`; format_version `"1.20.20"`.
- Урон `6`; прочность `{"max_durability":121}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:coal_sword"],"repair_amount":121}]}`.
- Оффхенд `true`; hand_equipped `true`; foil `"не задан"`; icon `{"texture":"coal_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{}`.

Прямых item events в файле нет; это не исключает пассивные и косвенные механики.

### effect:creeper_sword

- Файл `Sword_B/items/creeper_sword.json`; format_version `"1.20.20"`.
- Урон `8`; прочность `{"max_durability":1500}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:creeper_sword"],"repair_amount":1500}]}`.
- Оффхенд `true`; hand_equipped `true`; foil `"не задан"`; icon `{"texture":"creeper_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{}`.

Прямых item events в файле нет; это не исключает пассивные и косвенные механики.

### effect:emerald_sword

- Файл `Sword_B/items/emerald_sword.json`; format_version `"1.20.20"`.
- Урон `7`; прочность `{"max_durability":2300}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:emerald_sword"],"repair_amount":2300}]}`.
- Оффхенд `true`; hand_equipped `true`; foil `"не задан"`; icon `{"texture":"emerald_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{}`.

Прямых item events в файле нет; это не исключает пассивные и косвенные механики.

### effect:ender_sword

- Файл `Sword_B/items/ender_sword.json`; format_version `"1.20.20"`.
- Урон `9`; прочность `{"max_durability":1256}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:ender_sword"],"repair_amount":1256}]}`.
- Оффхенд `true`; hand_equipped `true`; foil `"не задан"`; icon `{"texture":"ender_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{}`.

Прямых item events в файле нет; это не исключает пассивные и косвенные механики.

### effect:fire_sword

- Файл `Sword_B/items/fire_sword.json`; format_version `"1.20.20"`.
- Урон `12`; прочность `{"max_durability":2000}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:fire_sword"],"repair_amount":2000}]}`.
- Оффхенд `true`; hand_equipped `true`; foil `"не задан"`; icon `{"texture":"fire_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{}`.

Прямых item events в файле нет; это не исключает пассивные и косвенные механики.

### effect:glowstone_sword

- Файл `Sword_B/items/glowstone_sword.json`; format_version `"1.20.20"`.
- Урон `6`; прочность `{"max_durability":128}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:glowstone_sword"],"repair_amount":128}]}`.
- Оффхенд `true`; hand_equipped `true`; foil `"не задан"`; icon `{"texture":"glowstone_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{}`.

Прямых item events в файле нет; это не исключает пассивные и косвенные механики.

### effect:grass_sword

- Файл `Sword_B/items/grass_sword.json`; format_version `"1.20.20"`.
- Урон `8`; прочность `{"max_durability":250}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:grass_sword"],"repair_amount":250}]}`.
- Оффхенд `true`; hand_equipped `true`; foil `"не задан"`; icon `{"texture":"grass_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{}`.

Прямых item events в файле нет; это не исключает пассивные и косвенные механики.

### effect:ice_sword

- Файл `Sword_B/items/ice_sword.json`; format_version `"1.20.20"`.
- Урон `11`; прочность `{"max_durability":500}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:ice_sword"],"repair_amount":500}]}`.
- Оффхенд `true`; hand_equipped `true`; foil `"не задан"`; icon `{"texture":"ice_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{}`.

Прямых item events в файле нет; это не исключает пассивные и косвенные механики.

### effect:jungle_sword

- Файл `Sword_B/items/jungle_sword.json`; format_version `"1.20.20"`.
- Урон `4`; прочность `{"max_durability":128}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:jungle_sword"],"repair_amount":128}]}`.
- Оффхенд `true`; hand_equipped `true`; foil `"не задан"`; icon `{"texture":"jungle_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{}`.

Прямых item events в файле нет; это не исключает пассивные и косвенные механики.

### effect:lapis_sword

- Файл `Sword_B/items/lapis_sword.json`; format_version `"1.20.20"`.
- Урон `6`; прочность `{"max_durability":528}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:lapis_sword"],"repair_amount":528}]}`.
- Оффхенд `true`; hand_equipped `true`; foil `"не задан"`; icon `{"texture":"lapis_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{}`.

Прямых item events в файле нет; это не исключает пассивные и косвенные механики.

### effect:lightning_sword

- Файл `Sword_B/items/lightning_sword.json`; format_version `"1.20.20"`.
- Урон `8`; прочность `{"max_durability":2000}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:lightning_sword"],"repair_amount":2000}]}`.
- Оффхенд `true`; hand_equipped `true`; foil `"не задан"`; icon `{"texture":"lightning_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{}`.

Прямых item events в файле нет; это не исключает пассивные и косвенные механики.

### effect:magma_sword

- Файл `Sword_B/items/magma_sword.json`; format_version `"1.20.20"`.
- Урон `7`; прочность `{"max_durability":1000}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:magma_sword"],"repair_amount":1000}]}`.
- Оффхенд `true`; hand_equipped `true`; foil `"не задан"`; icon `{"texture":"magma_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{}`.

Прямых item events в файле нет; это не исключает пассивные и косвенные механики.

### effect:obsidian_sword

- Файл `Sword_B/items/obsidian_sword.json`; format_version `"1.20.20"`.
- Урон `12`; прочность `{"max_durability":3000}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:obsidian_sword"],"repair_amount":3000}]}`.
- Оффхенд `true`; hand_equipped `true`; foil `"не задан"`; icon `{"texture":"obsidian_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{}`.

Прямых item events в файле нет; это не исключает пассивные и косвенные механики.

### effect:quartz_sword

- Файл `Sword_B/items/quartz_sword.json`; format_version `"1.20.20"`.
- Урон `600`; прочность `{"max_durability":1}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `"не задано"`; ремонт `{"repair_items":[{"items":["effect:quartz_sword"],"repair_amount":1}]}`.
- Оффхенд `true`; hand_equipped `true`; foil `"не задан"`; icon `{"texture":"quartz_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{}`.

Прямых item events в файле нет; это не исключает пассивные и косвенные механики.

### effect:sea_sword

- Файл `Sword_B/items/sea_sword.json`; format_version `"1.20.20"`.
- Урон `7`; прочность `{"max_durability":1000}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:sea_sword"],"repair_amount":1000}]}`.
- Оффхенд `true`; hand_equipped `true`; foil `"не задан"`; icon `{"texture":"sea_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{}`.

Прямых item events в файле нет; это не исключает пассивные и косвенные механики.

### effect:shulker_sword

- Файл `Sword_B/items/shulker_sword.json`; format_version `"1.20.20"`.
- Урон `7`; прочность `{"max_durability":1000}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:shulker_sword"],"repair_amount":1000}]}`.
- Оффхенд `true`; hand_equipped `true`; foil `"не задан"`; icon `{"texture":"shulker_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{}`.

Прямых item events в файле нет; это не исключает пассивные и косвенные механики.

### effect:slime_sword

- Файл `Sword_B/items/slime_sword.json`; format_version `"1.20.20"`.
- Урон `6`; прочность `{"max_durability":675}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:slime_sword"],"repair_amount":675}]}`.
- Оффхенд `true`; hand_equipped `true`; foil `"не задан"`; icon `{"texture":"slime_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{}`.

Прямых item events в файле нет; это не исключает пассивные и косвенные механики.

### effect:spectral_sword

- Файл `Sword_B/items/spectral_sword.json`; format_version `"1.20.20"`.
- Урон `9`; прочность `{"max_durability":3256}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:spectral_sword"],"repair_amount":3256}]}`.
- Оффхенд `true`; hand_equipped `true`; foil `"не задан"`; icon `{"texture":"spectral_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{}`.

Прямых item events в файле нет; это не исключает пассивные и косвенные механики.

### effect:spider_sword

- Файл `Sword_B/items/spider_sword.json`; format_version `"1.20.20"`.
- Урон `6`; прочность `{"max_durability":628}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:spider_sword"],"repair_amount":628}]}`.
- Оффхенд `true`; hand_equipped `true`; foil `"не задан"`; icon `{"texture":"spider_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{}`.

Прямых item events в файле нет; это не исключает пассивные и косвенные механики.

### effect:sponge_sword

- Файл `Sword_B/items/sponge_sword.json`; format_version `"1.20.20"`.
- Урон `6`; прочность `{"max_durability":128}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:sponge_sword"],"repair_amount":128}]}`.
- Оффхенд `true`; hand_equipped `true`; foil `"не задан"`; icon `{"texture":"sponge_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{}`.

Прямых item events в файле нет; это не исключает пассивные и косвенные механики.

### effect:tnt_sword

- Файл `Sword_B/items/tnt_sword.json`; format_version `"1.20.20"`.
- Урон `7`; прочность `{"max_durability":1}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `"не задано"`; ремонт `{"repair_items":[{"items":["effect:tnt_sword"],"repair_amount":1}]}`.
- Оффхенд `true`; hand_equipped `true`; foil `"не задан"`; icon `{"texture":"tnt_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{}`.

Прямых item events в файле нет; это не исключает пассивные и косвенные механики.

### effect:wither_sword

- Файл `Sword_B/items/wither_sword.json`; format_version `"1.20.20"`.
- Урон `10`; прочность `{"max_durability":1256}`; стак `1`; перезарядка `"не задана"`.
- Зачарование `{"value":9,"slot":"sword"}`; ремонт `{"repair_items":[{"items":["effect:wither_sword"],"repair_amount":1256}]}`.
- Оффхенд `true`; hand_equipped `true`; foil `"не задан"`; icon `{"texture":"wither_sword"}`.
- Скорости добычи `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**Привязки триггеров:** `{}`.

Прямых item events в файле нет; это не исключает пассивные и косвенные механики.

