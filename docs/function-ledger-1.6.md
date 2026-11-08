# Функции: все исходные строки и буквальные вызовы — 1.6

Все **3** `.mcfunction` behavior pack, всего **50 строк** с пустыми строками, по порядку. Строки представлены JSON-строками: кавычки, пробелы и специальные символы внутри значения не теряются; архив остаётся эталоном исходных байтов, в том числе окончаний строк. SHA-256 вычислен по исходным байтам. Путь function — относительный путь после `functions/` без `.mcfunction`.

Найдено 3 буквальных вхождений `function <путь>` при поиске во всех `.json`, `.mcfunction`, `.js` behavior pack, включая возможные комментарии или неразобранные JSON. Это только лексические кандидаты вызова, не парсер, доказательство запуска или исчерпывающий граф. Неточные или динамические пути, внешние пакеты и вызов игроком/консолью не интерпретируются. Нулевое число локальных вхождений не означает недоступность функции.

- Точные пути вызова без одноимённого локального файла: нет в области поиска.
- Вхождения не соответствующие шаблону: нет.

## Буквальные источники вызовов

| Файл:строка | Путь function | Локальный файл по точному пути | Полная строка |
|---|---|---|---|
| `Sword_B/animation_controllers/normal.json:13` | `"normalft"` | `Sword_B/functions/normalft.mcfunction` | `"            \"/function normalft\""` |
| `Sword_B/animation_controllers/normal.json:24` | `"normalft"` | `Sword_B/functions/normalft.mcfunction` | `"            \"/function normalft\""` |
| `Sword_B/functions/normalft.mcfunction:4` | `"normal"` | `Sword_B/functions/normal.mcfunction` | `"execute @a[scores={swords=0}] ~ ~ ~ function normal"` |

## Полные файлы

### give

Архивный путь: `Sword_B/functions/give.mcfunction`; SHA-256 `0dcf0acb17c76d9037cd0548da421033160f88bc897110e7b7fd5b4c2f743611`; буквальных кандидатов вызова: 0.

| № | Исходная строка |
|---:|---|
| 1 | `"give @p effect:blaze_sword"` |
| 2 | `"give @p effect:bone_sword"` |
| 3 | `"give @p effect:cactus_sword"` |
| 4 | `"give @p effect:coal_sword"` |
| 5 | `"give @p effect:creeper_sword"` |
| 6 | `"give @p effect:emerald_sword"` |
| 7 | `"give @p effect:ender_sword"` |
| 8 | `"give @p effect:fire_sword"` |
| 9 | `"give @p effect:glowstone_sword"` |
| 10 | `"give @p effect:grass_sword"` |
| 11 | `"give @p effect:ice_sword"` |
| 12 | `"give @p effect:jungle_sword"` |
| 13 | `"give @p effect:lapis_sword"` |
| 14 | `"give @p effect:lightning_sword"` |
| 15 | `"give @p effect:magma_sword"` |
| 16 | `"give @p effect:obsidian_sword"` |
| 17 | `"give @p effect:quartz_sword"` |
| 18 | `"give @p effect:sea_sword"` |
| 19 | `"give @p effect:shulker_sword"` |
| 20 | `"give @p effect:slime_sword"` |
| 21 | `"give @p effect:spectral_sword"` |
| 22 | `"give @p effect:spider_sword"` |
| 23 | `"give @p effect:sponge_sword"` |
| 24 | `"give @p effect:sword_of_time"` |
| 25 | `"give @p effect:tnt_sword"` |
| 26 | `"give @p effect:wither_sword"` |

### normal

Архивный путь: `Sword_B/functions/normal.mcfunction`; SHA-256 `b3b3889f0854cca24e1636087ca6ed6e865fa9a10263398f5a45a8cf3372ab8f`; буквальных кандидатов вызова: 1.

| № | Исходная строка |
|---:|---|
| 1 | `""` |
| 2 | `"gamerule commandblockoutput false"` |
| 3 | `"gamerule sendcommandfeedback false"` |
| 4 | `""` |
| 5 | `"tp @e[r=4,type=entity:blaze2] ~ 0 ~"` |
| 6 | `"tp @e[r=4,type=entity:bone2] ~ 0 ~"` |
| 7 | `"execute @p[r=2] ~ ~ ~ scoreboard objectives remove b"` |
| 8 | `"execute @p[r=2] ~ ~ ~ scoreboard objectives remove bn"` |
| 9 | `"execute @p[r=2] ~ ~ ~ scoreboard objectives remove sh"` |
| 10 | `"fill ~7 ~8 ~8 ~8 ~-8 ~-8 stone 0 replace barrier"` |
| 11 | `"fill ~-7 ~-8 ~-8 ~-8 ~8 ~8 stone 0 replace barrier"` |
| 12 | `"fill ~-6 ~8 ~7 ~6 ~-8 ~8 stone 0 replace barrier"` |
| 13 | `"fill ~6 ~-8 ~-7 ~-6 ~8 ~-8 stone 0 replace barrier"` |
| 14 | `"fill ~8 ~-8 ~8 ~-8 ~-7 ~-8 stone 0 replace barrier"` |
| 15 | `"fill ~8 ~8 ~8 ~-8 ~7 ~-8 stone 0 replace barrier"` |
| 16 | `"fill ~6 ~6 ~6 ~-6 ~-6 ~-6 stone 0 replace barrier"` |
| 17 | `"tp @e[r=4,type=entity:shulker2] ~ 0 ~"` |
| 18 | `"execute @p[r=2] ~ ~ ~ scoreboard objectives remove s"` |
| 19 | `"gamerule randomtickspeed 1"` |
| 20 | `"execute @p ~~~ fill ~5 ~5 ~5 ~-5 ~-5 ~-5 air 0 replace light_block 15"` |

### normalft

Архивный путь: `Sword_B/functions/normalft.mcfunction`; SHA-256 `5463f2e761b48231421cecf265949bc22f15487d778bccfdcd4585a1504b9d52`; буквальных кандидатов вызова: 2.

| № | Исходная строка |
|---:|---|
| 1 | `"scoreboard objectives add swords dummy"` |
| 2 | `"scoreboard players remove @a[scores={swords=1}] swords 1"` |
| 3 | `"scoreboard players remove @a[scores={swords=2}] swords 1"` |
| 4 | `"execute @a[scores={swords=0}] ~ ~ ~ function normal"` |

См. также [назначение тегов и проблемы получения](manual-acquisition-issues.md), [лианы Jungle](jungle-vine-index.md), [ручной разбор Wolf](manual-wolf-conditions-2.8.md) и [общий scoreboard 1.6](manual-global-state-1.6.md).
