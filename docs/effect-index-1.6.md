# Эффекты: команды и выбранные компоненты — 1.6

Лексический поиск во всех текстовых `.json`, `.mcfunction`, `.js` behavior pack: 49 исходных строк с буквальным `effect` и selector `@…`, 49 распознанных вхождений. Исходные строки сохранены целиком с номерами, даже если один JSON-ряд содержит несколько команд; сохраняются повторы разных состояний. Строка может быть комментарием или недостижимой ветвью. Это не парсер команд и не подтверждение исполнения. Выборка не включает команды с другим синтаксисом, динамически составленные строки, ресурсы извне, ванильные функции или эффекты, приходящие по косвенным цепям.

Селекторы, фильтры, нули, порядок и числовые аргументы приведены буквально. Не переводить duration/amplifier в секунды или уровни без учёта конкретной формы и версии; `0` не приравнивается автоматически к одному и тому же действию во всех контекстах. Необъявленный target не следует считать self. Имена ниже — лишь разбор подстроки, не гарантированный effect ID или цель.

Вхождения имён после selector: `conduit_power` — 2, `fatal_poison` — 4, `fire_resistance` — 24, `jump_boost` — 2, `levitation` — 2, `poison` — 7, `slowness` — 4, `speed` — 2, `village_hero` — 2.

Отдельно среди разобранных JSON извлечены **4** структурных объектов: `minecraft:spell_effects` — 4. Включены `minecraft:spell_effects`, `minecraft:attack` с `effect_name`/`effect_duration`, `minecraft:healable` с `items[].effects`, а также `mob_effect` и `arrow_effect`. Пустой `arrow_effect` не означает отсутствие стрелочных эффектов: обработка остаётся за движком. Списки, значения и вложенные фильтры сохранены целиком.

- Неразобранные JSON: `Sword_B/entities/blaze2.json` (<string>:78 Unexpected "}" at column 1); `Sword_B/entities/bone2.json` (<string>:75 Unexpected "}" at column 1); `Sword_B/entities/shulker2.json` (<string>:75 Unexpected "}" at column 1). Исходные строки с командами ищутся и в них, но структурные объекты этих файлов исключены.
- Повторные ключи в разобранных файлах: нет. JSON5 сохраняет последнее значение; подлинник остаётся эталоном.
- Вхождения не соответствующие ограниченному шаблону извлечения имени: нет.

## Исходные строки с командами

| Файл и строка | Распознанные имена | Исходная строка целиком |
|---|---|---|
| `Sword_B/animation_controllers/cactus_sword.json:16` | `poison` | `"            \"/execute @p[scores={ct=1}] ~ ~ ~ effect @s poison 1 1 true\","` |
| `Sword_B/animation_controllers/cactus_sword.json:17` | `poison` | `"            \"/execute @e[scores={ct=1},r=2] ~ ~ ~ effect @s poison 1 1 true\","` |
| `Sword_B/animation_controllers/cactus_sword.json:32` | `poison` | `"            \"/execute @p[scores={ct=1}] ~ ~ ~ effect @s poison 1 1 true\","` |
| `Sword_B/animation_controllers/cactus_sword.json:33` | `poison` | `"            \"/execute @e[scores={ct=1},r=2] ~ ~ ~ effect @s poison 1 1 true\","` |
| `Sword_B/animation_controllers/emerald_sword.json:13` | `village_hero` | `"          \t\"/effect @p village_hero 16 0 true\","` |
| `Sword_B/animation_controllers/emerald_sword.json:24` | `village_hero` | `"          \t\"/effect @p village_hero 16 0 true\","` |
| `Sword_B/animation_controllers/fire_sword.json:13` | `fire_resistance` | `"          \t\"/effect @p fire_resistance 10 0 true\","` |
| `Sword_B/animation_controllers/fire_sword.json:64` | `fire_resistance` | `"          \t\"/effect @p fire_resistance 10 0 true\","` |
| `Sword_B/animation_controllers/magma_sword.json:13` | `fire_resistance` | `"          \t\"/effect @p fire_resistance 10 0 true\","` |
| `Sword_B/animation_controllers/magma_sword.json:46` | `fire_resistance` | `"          \t\"/effect @p fire_resistance 10 0 true\","` |
| `Sword_B/animation_controllers/obsidian_sword.json:15` | `fire_resistance` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ lava 0 effect @s fire_resistance 10 0 true\","` |
| `Sword_B/animation_controllers/obsidian_sword.json:16` | `fire_resistance` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ lava 1 effect @s fire_resistance 10 0 true\","` |
| `Sword_B/animation_controllers/obsidian_sword.json:17` | `fire_resistance` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ lava 2 effect @s fire_resistance 10 0 true\","` |
| `Sword_B/animation_controllers/obsidian_sword.json:18` | `fire_resistance` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ lava 3 effect @s fire_resistance 10 0 true\","` |
| `Sword_B/animation_controllers/obsidian_sword.json:19` | `fire_resistance` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ lava 4 effect @s fire_resistance 10 0 true\","` |
| `Sword_B/animation_controllers/obsidian_sword.json:20` | `fire_resistance` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ lava 5 effect @s fire_resistance 10 0 true\","` |
| `Sword_B/animation_controllers/obsidian_sword.json:21` | `fire_resistance` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ lava 6 effect @s fire_resistance 10 0 true\","` |
| `Sword_B/animation_controllers/obsidian_sword.json:22` | `fire_resistance` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ lava 7 effect @s fire_resistance 10 0 true\","` |
| `Sword_B/animation_controllers/obsidian_sword.json:23` | `fire_resistance` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ lava 8 effect @s fire_resistance 10 0 true\","` |
| `Sword_B/animation_controllers/obsidian_sword.json:24` | `fire_resistance` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ flowing_lava 0 effect @s fire_resistance 10 0 true\","` |
| `Sword_B/animation_controllers/obsidian_sword.json:37` | `fire_resistance` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ lava 0 effect @s fire_resistance 10 0 true\","` |
| `Sword_B/animation_controllers/obsidian_sword.json:38` | `fire_resistance` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ lava 1 effect @s fire_resistance 10 0 true\","` |
| `Sword_B/animation_controllers/obsidian_sword.json:39` | `fire_resistance` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ lava 2 effect @s fire_resistance 10 0 true\","` |
| `Sword_B/animation_controllers/obsidian_sword.json:40` | `fire_resistance` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ lava 3 effect @s fire_resistance 10 0 true\","` |
| `Sword_B/animation_controllers/obsidian_sword.json:41` | `fire_resistance` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ lava 4 effect @s fire_resistance 10 0 true\","` |
| `Sword_B/animation_controllers/obsidian_sword.json:42` | `fire_resistance` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ lava 5 effect @s fire_resistance 10 0 true\","` |
| `Sword_B/animation_controllers/obsidian_sword.json:43` | `fire_resistance` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ lava 6 effect @s fire_resistance 10 0 true\","` |
| `Sword_B/animation_controllers/obsidian_sword.json:44` | `fire_resistance` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ lava 7 effect @s fire_resistance 10 0 true\","` |
| `Sword_B/animation_controllers/obsidian_sword.json:45` | `fire_resistance` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ lava 8 effect @s fire_resistance 10 0 true\",            "` |
| `Sword_B/animation_controllers/obsidian_sword.json:46` | `fire_resistance` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ flowing_lava 0 effect @s fire_resistance 10 0 true\","` |
| `Sword_B/animation_controllers/sea_sword.json:13` | `fatal_poison` | `"            \"/effect @e[type=guardian,r=6] fatal_poison 5 0 true\","` |
| `Sword_B/animation_controllers/sea_sword.json:14` | `fatal_poison` | `"            \"/effect @e[type=drowned,r=6] fatal_poison 5 0 true\","` |
| `Sword_B/animation_controllers/sea_sword.json:15` | `conduit_power` | `"            \"/effect @p conduit_power 16 0 true\","` |
| `Sword_B/animation_controllers/sea_sword.json:27` | `fatal_poison` | `"            \"/effect @e[type=guardian,r=6] fatal_poison 5 0 true\","` |
| `Sword_B/animation_controllers/sea_sword.json:28` | `fatal_poison` | `"            \"/effect @e[type=drowned,r=6] fatal_poison 5 0 true\","` |
| `Sword_B/animation_controllers/sea_sword.json:29` | `conduit_power` | `"            \"/effect @p conduit_power 16 0 true\","` |
| `Sword_B/animation_controllers/shulker_sword.json:13` | `levitation` | `"          \t\"/effect @p levitation 0 0 true\","` |
| `Sword_B/animation_controllers/shulker_sword.json:30` | `levitation` | `"            \"/effect @p levitation 0 0 true\","` |
| `Sword_B/animation_controllers/slime_sword.json:16` | `jump_boost` | `"            \"/effect @p jump_boost 1 5 true\","` |
| `Sword_B/animation_controllers/slime_sword.json:35` | `jump_boost` | `"            \"/effect @p jump_boost 1 5 true\","` |
| `Sword_B/animation_controllers/spider_sword.json:13` | `poison` | `"          \t\"/effect @p poison 0 0 true\","` |
| `Sword_B/animation_controllers/spider_sword.json:16` | `slowness` | `"          \t\"/execute @p ~ ~ ~ effect @e[r=6,type=spider] slowness 1 128 true\","` |
| `Sword_B/animation_controllers/spider_sword.json:17` | `slowness` | `"          \t\"/execute @p ~ ~ ~ effect @e[r=6,type=cave_spider] slowness 1 128 true\","` |
| `Sword_B/animation_controllers/spider_sword.json:57` | `poison` | `"          \t\"/effect @p poison 0 0 true\","` |
| `Sword_B/animation_controllers/spider_sword.json:60` | `slowness` | `"          \t\"/execute @p ~ ~ ~ effect @e[r=6,type=spider] slowness 1 128 true\","` |
| `Sword_B/animation_controllers/spider_sword.json:61` | `slowness` | `"          \t\"/execute @p ~ ~ ~ effect @e[r=6,type=cave_spider] slowness 1 128 true\","` |
| `Sword_B/animation_controllers/sword of time.json:14` | `speed` | `"            \"/effect @e speed 1 15 true\","` |
| `Sword_B/animation_controllers/sword of time.json:27` | `speed` | `"            \"/effect @e speed 1 15 true\","` |
| `Sword_B/animation_controllers/wither_sword.json:23` | `poison` | `"            \"/effect @e[r=16,type=!player] poison 30 1 true\","` |

## Структурные поля (все выбранные разобранные объекты)

| Файл / путь | Поле | Полный разобранный объект |
|---|---|---|
| `Sword_B/entities/player.json`<br>`$.minecraft:entity.component_groups.minecraft:normal_player.minecraft:spell_effects` | `minecraft:spell_effects` | `{}` |
| `Sword_B/entities/player.json`<br>`$.minecraft:entity.component_groups.minecraft:add_bad_omen.minecraft:spell_effects` | `minecraft:spell_effects` | `{"add_effects":[{"effect":"bad_omen","duration":6000,"display_on_screen_animation":true}]}` |
| `Sword_B/entities/player.json`<br>`$.minecraft:entity.component_groups.minecraft:clear_bad_omen_spell_effect.minecraft:spell_effects` | `minecraft:spell_effects` | `{}` |
| `Sword_B/entities/player.json`<br>`$.minecraft:entity.component_groups.minecraft:raid_trigger.minecraft:spell_effects` | `minecraft:spell_effects` | `{"remove_effects":"bad_omen"}` |

Контекст событий, включение групп и полные списки команд: [реестр сущностей](entity-ledger-1.6.md), [projectile](projectile-component-index.md), [weapon-хуки](weapon-event-index.md), [команды](command-risk-index-1.6.md).
