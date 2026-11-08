# Локальные объявления ID и манифесты трёх архивов

Механический поиск `description.identifier` в корневых объектах разбираемых JSON каждого пакета отдельно. Рецепты разных видов объединены для дополнительной проверки, но реальный namespace регистрации определяется движком. **Совпадающий ID не доказывает ошибку**, победителя или запуск: версии client entity могут быть намеренными вариантами. Behavior и resource пакеты не смешаны. Не охвачены ресурсы без `description.identifier`, наборы geometry/animation/controllers, ванильные пакеты, неизвестные форматы, динамические объявления и неразобранные файлы. Повторные ключи JSON5 сохраняют последнее значение. Таблица не является доказательством загрузки.

## 1.6

Разобрано объявлений: 106; отдельных групп pack/вид/ID: 106; групп с повтором: 0.

- Неразобранные JSON: `Sword_B/entities/blaze2.json`, `Sword_B/entities/bone2.json`, `Sword_B/entities/shulker2.json`.
- Повторные ключи JSON: нет.

### Пакеты и типы

| Пакет | Категория объявления | Количество |
|---|---|---:|
| `Sword_B` | `minecraft:entity` | 28 |
| `Sword_B` | `minecraft:item` | 26 |
| `Sword_B` | `minecraft:recipe_*` | 26 |
| `Sword_R` | `minecraft:item` | 26 |

### Повторённые ID внутри одного пакета

Не обнаружено в указанном ограниченном поиске.

### Манифесты

- `Sword_B/manifest.json`: header UUID `1ecf4d4b-3a3c-1be3-bc21-9512946109b6`, version `[1,0,0]`, min_engine_version `не задан`.
  - modules: `[{"type":"data","uuid":"bc00e35a-1b9c-3c0c-a9b9-fc4efa7309ac","version":[1,0,0]}]`.
  - dependencies: `[{"uuid":"2f15ae41-a1c1-4117-aa1e-855a98a06318","version":[1,0,0]}]`.
- `Sword_R/manifest.json`: header UUID `2f15ae41-a1c1-4117-aa1e-855a98a06318`, version `[1,0,0]`, min_engine_version `не задан`.
  - modules: `[{"type":"resources","uuid":"e5447658-01ef-11e8-a1a0-ba2c34b08f13","version":[1,0,0]}]`.
  - dependencies: `[{"uuid":"1ecf4d4b-3a3c-1be3-bc21-9512946109b6","version":[1,0,0]}]`.

## 2.8.8

Разобрано объявлений: 147; отдельных групп pack/вид/ID: 146; групп с повтором: 1.

- Неразобранные JSON: `Swords_B/entities/creeper.json`.
- Повторные ключи JSON: `Swords_B/entities/living_flame.json`: `["minecraft:fire_immune"]`, `Swords_B/entities/mountable_slime.json`: `["despawn"]`, `Swords_B/entities/slime_king.json`: `["minecraft:movement.jump"]`.

### Пакеты и типы

| Пакет | Категория объявления | Количество |
|---|---|---:|
| `Swords_B` | `minecraft:block` | 8 |
| `Swords_B` | `minecraft:entity` | 51 |
| `Swords_B` | `minecraft:feature_rules` | 2 |
| `Swords_B` | `minecraft:item` | 42 |
| `Swords_B` | `minecraft:recipe_*` | 14 |
| `Swords_B` | `minecraft:spawn_rules` | 4 |
| `Swords_B` | `minecraft:structure_template_feature` | 2 |
| `Swords_R` | `minecraft:client_entity` | 17 |
| `Swords_R` | `particle_effect` | 7 |

### Повторённые ID внутри одного пакета

- `Swords_R` · `minecraft:client_entity` · `minecraft:witch`: `Swords_R/entity/witch.entity.json` (minecraft:client_entity), `Swords_R/entity/witch.v1.0.entity.json` (minecraft:client_entity).

### Манифесты

- `Swords_B/manifest.json`: header UUID `1acf4d4b-3a3c-1be3-bc21-9512946109b1`, version `[1,0,0]`, min_engine_version `[1,19,40]`.
  - modules: `[{"type":"data","uuid":"ba10e35a-3b9c-3c0c-a9b9-fc4efa7309ea","version":[1,0,0]},{"entry":"scripts/javascript.js","type":"script","uuid":"76310e1c-d881-46e6-eb3b-4fabfae56941","version":[1,0,0]}]`.
  - dependencies: `[{"description":"@minecraft/server","uuid":"b26a4d4c-afdf-4690-88f8-931846312678","version":"1.8.0-beta"},{"uuid":"3f15ae41-a1c1-4111-aa1e-855a98a06316","version":[1,0,0]}]`.
- `Swords_R/manifest.json`: header UUID `3f15ae41-a1c1-4111-aa1e-855a98a06316`, version `[1,0,0]`, min_engine_version `[1,19,40]`.
  - modules: `[{"type":"resources","uuid":"a6437658-11af-11e8-a1a0-be2c34b08f12","version":[1,0,0]}]`.
  - dependencies: `[{"uuid":"1acf4d4b-3a3c-1be3-bc21-9512946109b1","version":[1,0,0]}]`.

## 2.8.14

Разобрано объявлений: 142; отдельных групп pack/вид/ID: 141; групп с повтором: 1.

- Неразобранные JSON: `Swords_B/entities/creeper.json`.
- Повторные ключи JSON: `Swords_B/entities/living_flame.json`: `["minecraft:fire_immune"]`, `Swords_B/entities/mountable_slime.json`: `["despawn"]`, `Swords_B/entities/slime_king.json`: `["minecraft:movement.jump"]`.

### Пакеты и типы

| Пакет | Категория объявления | Количество |
|---|---|---:|
| `Swords_B` | `minecraft:block` | 7 |
| `Swords_B` | `minecraft:entity` | 51 |
| `Swords_B` | `minecraft:item` | 42 |
| `Swords_B` | `minecraft:recipe_*` | 14 |
| `Swords_B` | `minecraft:spawn_rules` | 4 |
| `Swords_R` | `minecraft:client_entity` | 17 |
| `Swords_R` | `particle_effect` | 7 |

### Повторённые ID внутри одного пакета

- `Swords_R` · `minecraft:client_entity` · `minecraft:witch`: `Swords_R/entity/witch.entity.json` (minecraft:client_entity), `Swords_R/entity/witch.v1.0.entity.json` (minecraft:client_entity).

### Манифесты

- `Swords_B/manifest.json`: header UUID `1acf4d4b-3a3c-1be3-bc21-9512946109b1`, version `[1,0,0]`, min_engine_version `[1,19,40]`.
  - modules: `[{"type":"data","uuid":"ba10e35a-3b9c-3c0c-a9b9-fc4efa7309ea","version":[1,0,0]},{"entry":"scripts/javascript.js","type":"script","uuid":"76310e1c-d881-46e6-eb3b-4fabfae56941","version":[1,0,0]}]`.
  - dependencies: `[{"description":"@minecraft/server","uuid":"b26a4d4c-afdf-4690-88f8-931846312678","version":"1.12.0-beta"},{"uuid":"3f15ae41-a1c1-4111-aa1e-855a98a06316","version":[1,0,0]}]`.
- `Swords_R/manifest.json`: header UUID `3f15ae41-a1c1-4111-aa1e-855a98a06316`, version `[1,0,0]`, min_engine_version `[1,19,40]`.
  - modules: `[{"type":"resources","uuid":"a6437658-11af-11e8-a1a0-be2c34b08f12","version":[1,0,0]}]`.
  - dependencies: `[{"uuid":"1acf4d4b-3a3c-1be3-bc21-9512946109b1","version":[1,0,0]}]`.

