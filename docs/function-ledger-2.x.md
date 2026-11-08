# Функции: все исходные строки и буквальные вызовы — 2.8.8 и 2.8.14

Все **4** `.mcfunction` behavior pack, всего **197 строк** с пустыми строками, по порядку. Строки представлены JSON-строками: кавычки, пробелы и специальные символы внутри значения не теряются; архив остаётся эталоном исходных байтов, в том числе окончаний строк. SHA-256 вычислен по исходным байтам. Путь function — относительный путь после `functions/` без `.mcfunction`.

Найдено 3 буквальных вхождений `function <путь>` при поиске во всех `.json`, `.mcfunction`, `.js` behavior pack, включая возможные комментарии или неразобранные JSON. Это только лексические кандидаты вызова, не парсер, доказательство запуска или исчерпывающий граф. Неточные или динамические пути, внешние пакеты и вызов игроком/консолью не интерпретируются. Нулевое число локальных вхождений не означает недоступность функции.

- Точные пути вызова без одноимённого локального файла: нет в области поиска.
- Вхождения не соответствующие шаблону: нет.

Все четыре `.mcfunction` и выбранные строки вызова в двух архивах 2.x совпадают побайтово/буквально соответственно; это не равенство всех других файлов или фактической работы функций.

## Буквальные источники вызовов

| Файл:строка | Путь function | Локальный файл по точному пути | Полная строка |
|---|---|---|---|
| `Swords_B/entities/player.json:1060` | `"commands/swords_and_more_swords/swords_and_more_swords/tag_swords"` | `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/tag_swords.mcfunction` | `"              \"function commands/swords_and_more_swords/swords_and_more_swords/tag_swords\","` |
| `Swords_B/entities/player.json:1313` | `"commands/swords_and_more_swords/swords_and_more_swords/tellraw1"` | `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/tellraw1.mcfunction` | `"           \"run_command\": { \"command\": [ \"function commands/swords_and_more_swords/swords_and_more_swords/tellraw1\" ] }"` |
| `Swords_B/entities/player.json:2008` | `"commands/swords_and_more_swords/swords_and_more_swords/jungle_sword"` | `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction` | `"            \"run_command\": { \"command\": [ \"effect @s absorption 1 2 true\", \"function commands/swords_and_more_swords/swords_and_more_swords/jungle_sword\" ] }"` |

## Полные файлы

### commands/swords_and_more_swords/swords_and_more_swords/jungle_sword

Архивный путь: `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction`; SHA-256 `71fe36e10d77c5b8a55da101b36c9b06b9c7cca0e0e39fedbe030994a40d37d4`; буквальных кандидатов вызова: 1.

| № | Исходная строка |
|---:|---|
| 1 | `"execute @p ~~~ detect ~1 ~1 ~ log 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| 2 | `"execute @p ~~~ detect ~-1 ~1 ~ log 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| 3 | `"execute @p ~~~ detect ~ ~1 ~1 log 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| 4 | `"execute @p ~~~ detect ~ ~1 ~-1 log 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| 5 | `"execute @p ~~~ detect ~1 ~1 ~ log 1 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| 6 | `"execute @p ~~~ detect ~-1 ~1 ~ log 1 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| 7 | `"execute @p ~~~ detect ~ ~1 ~1 log 1 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| 8 | `"execute @p ~~~ detect ~ ~1 ~-1 log 1 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| 9 | `"execute @p ~~~ detect ~1 ~1 ~ log 2 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| 10 | `"execute @p ~~~ detect ~-1 ~1 ~ log 2 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| 11 | `"execute @p ~~~ detect ~ ~1 ~1 log 2 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| 12 | `"execute @p ~~~ detect ~ ~1 ~-1 log 2 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| 13 | `"execute @p ~~~ detect ~1 ~1 ~ log 3 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| 14 | `"execute @p ~~~ detect ~-1 ~1 ~ log 3 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| 15 | `"execute @p ~~~ detect ~ ~1 ~1 log 3 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| 16 | `"execute @p ~~~ detect ~ ~1 ~-1 log 3 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| 17 | `"execute @p ~~~ detect ~1 ~1 ~ log2 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| 18 | `"execute @p ~~~ detect ~-1 ~1 ~ log2 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| 19 | `"execute @p ~~~ detect ~ ~1 ~1 log2 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| 20 | `"execute @p ~~~ detect ~ ~1 ~-1 log2 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| 21 | `"execute @p ~~~ detect ~1 ~1 ~ log2 1 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| 22 | `"execute @p ~~~ detect ~-1 ~1 ~ log2 1 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| 23 | `"execute @p ~~~ detect ~ ~1 ~1 log2 1 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| 24 | `"execute @p ~~~ detect ~ ~1 ~-1 log2 1 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| 25 | `"execute @p ~~~ detect ~1 ~1 ~ stone 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| 26 | `"execute @p ~~~ detect ~-1 ~1 ~ stone 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| 27 | `"execute @p ~~~ detect ~ ~1 ~1 stone 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| 28 | `"execute @p ~~~ detect ~ ~1 ~-1 stone 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| 29 | `"execute @p ~~~ detect ~1 ~1 ~ cobblestone 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| 30 | `"execute @p ~~~ detect ~-1 ~1 ~ cobblestone 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| 31 | `"execute @p ~~~ detect ~ ~1 ~1 cobblestone 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| 32 | `"execute @p ~~~ detect ~ ~1 ~-1 cobblestone 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| 33 | `"execute @p ~~~ detect ~1 ~1 ~ dirt 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| 34 | `"execute @p ~~~ detect ~-1 ~1 ~ dirt 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| 35 | `"execute @p ~~~ detect ~ ~1 ~1 dirt 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| 36 | `"execute @p ~~~ detect ~ ~1 ~-1 dirt 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| 37 | `"execute @p ~~~ detect ~1 ~1 ~ leaves 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| 38 | `"execute @p ~~~ detect ~-1 ~1 ~ leaves 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| 39 | `"execute @p ~~~ detect ~ ~1 ~1 leaves 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| 40 | `"execute @p ~~~ detect ~ ~1 ~-1 leaves 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| 41 | `"execute @p ~~~ detect ~1 ~1 ~ leaves 1 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| 42 | `"execute @p ~~~ detect ~-1 ~1 ~ leaves 1 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| 43 | `"execute @p ~~~ detect ~ ~1 ~1 leaves 1 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| 44 | `"execute @p ~~~ detect ~ ~1 ~-1 leaves 1 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| 45 | `"execute @p ~~~ detect ~1 ~1 ~ leaves 2 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| 46 | `"execute @p ~~~ detect ~-1 ~1 ~ leaves 2 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| 47 | `"execute @p ~~~ detect ~ ~1 ~1 leaves 2 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| 48 | `"execute @p ~~~ detect ~ ~1 ~-1 leaves 2 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| 49 | `"execute @p ~~~ detect ~1 ~1 ~ leaves 3 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| 50 | `"execute @p ~~~ detect ~-1 ~1 ~ leaves 3 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| 51 | `"execute @p ~~~ detect ~ ~1 ~1 leaves 3 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| 52 | `"execute @p ~~~ detect ~ ~1 ~-1 leaves 3 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| 53 | `"execute @p ~~~ detect ~1 ~1 ~ leaves 11 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| 54 | `"execute @p ~~~ detect ~-1 ~1 ~ leaves 11 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| 55 | `"execute @p ~~~ detect ~ ~1 ~1 leaves 11 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| 56 | `"execute @p ~~~ detect ~ ~1 ~-1 leaves 11 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| 57 | `"execute @p ~~~ detect ~1 ~1 ~ leaves2 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| 58 | `"execute @p ~~~ detect ~-1 ~1 ~ leaves2 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| 59 | `"execute @p ~~~ detect ~ ~1 ~1 leaves2 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| 60 | `"execute @p ~~~ detect ~ ~1 ~-1 leaves2 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| 61 | `"execute @p ~~~ detect ~1 ~1 ~ leaves2 1 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| 62 | `"execute @p ~~~ detect ~-1 ~1 ~ leaves2 1 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| 63 | `"execute @p ~~~ detect ~ ~1 ~1 leaves2 1 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| 64 | `"execute @p ~~~ detect ~ ~1 ~-1 leaves2 1 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| 65 | `"execute @p ~~~ detect ~1 ~1 ~ planks 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| 66 | `"execute @p ~~~ detect ~-1 ~1 ~ planks 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| 67 | `"execute @p ~~~ detect ~ ~1 ~1 planks 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| 68 | `"execute @p ~~~ detect ~ ~1 ~-1 planks 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| 69 | `"execute @p ~~~ detect ~1 ~1 ~ planks 1 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| 70 | `"execute @p ~~~ detect ~-1 ~1 ~ planks 1 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| 71 | `"execute @p ~~~ detect ~ ~1 ~1 planks 1 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| 72 | `"execute @p ~~~ detect ~ ~1 ~-1 planks 1 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| 73 | `"execute @p ~~~ detect ~1 ~1 ~ planks 2 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| 74 | `"execute @p ~~~ detect ~-1 ~1 ~ planks 2 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| 75 | `"execute @p ~~~ detect ~ ~1 ~1 planks 2 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| 76 | `"execute @p ~~~ detect ~ ~1 ~-1 planks 2 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| 77 | `"execute @p ~~~ detect ~1 ~1 ~ planks 3 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| 78 | `"execute @p ~~~ detect ~-1 ~1 ~ planks 3 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| 79 | `"execute @p ~~~ detect ~ ~1 ~1 planks 3 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| 80 | `"execute @p ~~~ detect ~ ~1 ~-1 planks 3 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| 81 | `"execute @p ~~~ detect ~1 ~1 ~ planks 4 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| 82 | `"execute @p ~~~ detect ~-1 ~1 ~ planks 4 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| 83 | `"execute @p ~~~ detect ~ ~1 ~1 planks 4 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| 84 | `"execute @p ~~~ detect ~ ~1 ~-1 planks 4 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| 85 | `"execute @p ~~~ detect ~1 ~1 ~ planks 5 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| 86 | `"execute @p ~~~ detect ~-1 ~1 ~ planks 5 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| 87 | `"execute @p ~~~ detect ~ ~1 ~1 planks 5 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| 88 | `"execute @p ~~~ detect ~ ~1 ~-1 planks 5 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| 89 | `"execute @p ~~~ detect ~1 ~1 ~ grass 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| 90 | `"execute @p ~~~ detect ~-1 ~1 ~ grass 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| 91 | `"execute @p ~~~ detect ~ ~1 ~1 grass 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| 92 | `"execute @p ~~~ detect ~ ~1 ~-1 grass 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| 93 | `"execute @p ~~~ detect ~1 ~1 ~ netherrack 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| 94 | `"execute @p ~~~ detect ~-1 ~1 ~ netherrack 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| 95 | `"execute @p ~~~ detect ~ ~1 ~1 netherrack 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| 96 | `"execute @p ~~~ detect ~ ~1 ~-1 netherrack 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| 97 | `"execute @p ~~~ detect ~1 ~1 ~ nether_brick 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| 98 | `"execute @p ~~~ detect ~-1 ~1 ~ nether_brick 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| 99 | `"execute @p ~~~ detect ~ ~1 ~1 nether_brick 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| 100 | `"execute @p ~~~ detect ~ ~1 ~-1 nether_brick 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| 101 | `"execute @p ~~~ detect ~1 ~1 ~ sand 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| 102 | `"execute @p ~~~ detect ~-1 ~1 ~ sand 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| 103 | `"execute @p ~~~ detect ~ ~1 ~1 sand 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| 104 | `"execute @p ~~~ detect ~ ~1 ~-1 sand 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| 105 | `"execute @p ~~~ detect ~1 ~1 ~ glass 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| 106 | `"execute @p ~~~ detect ~-1 ~1 ~ glass 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| 107 | `"execute @p ~~~ detect ~ ~1 ~1 glass 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| 108 | `"execute @p ~~~ detect ~ ~1 ~-1 glass 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| 109 | `"execute @p ~~~ detect ~1 ~1 ~ obsidian 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| 110 | `"execute @p ~~~ detect ~-1 ~1 ~ obsidian 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| 111 | `"execute @p ~~~ detect ~ ~1 ~1 obsidian 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| 112 | `"execute @p ~~~ detect ~ ~1 ~-1 obsidian 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| 113 | `"execute @p ~~~ detect ~1 ~1 ~ end_stone 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| 114 | `"execute @p ~~~ detect ~-1 ~1 ~ end_stone 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| 115 | `"execute @p ~~~ detect ~ ~1 ~1 end_stone 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| 116 | `"execute @p ~~~ detect ~ ~1 ~-1 end_stone 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| 117 | `"execute @p ~~~ detect ~1 ~1 ~ sandstone 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| 118 | `"execute @p ~~~ detect ~-1 ~1 ~ sandstone 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| 119 | `"execute @p ~~~ detect ~ ~1 ~1 sandstone 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| 120 | `"execute @p ~~~ detect ~ ~1 ~-1 sandstone 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| 121 | `"execute @p ~~~ detect ~1 ~1 ~ gravel 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| 122 | `"execute @p ~~~ detect ~-1 ~1 ~ gravel 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| 123 | `"execute @p ~~~ detect ~ ~1 ~1 gravel 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| 124 | `"execute @p ~~~ detect ~ ~1 ~-1 gravel 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| 125 | `"execute @p ~~~ detect ~1 ~1 ~ stone 1 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| 126 | `"execute @p ~~~ detect ~-1 ~1 ~ stone 1 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| 127 | `"execute @p ~~~ detect ~ ~1 ~1 stone 1 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| 128 | `"execute @p ~~~ detect ~ ~1 ~-1 stone 1 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| 129 | `"execute @p ~~~ detect ~1 ~1 ~ stone 3 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| 130 | `"execute @p ~~~ detect ~-1 ~1 ~ stone 3 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| 131 | `"execute @p ~~~ detect ~ ~1 ~1 stone 3 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| 132 | `"execute @p ~~~ detect ~ ~1 ~-1 stone 3 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| 133 | `"execute @p ~~~ detect ~1 ~1 ~ stone 5 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| 134 | `"execute @p ~~~ detect ~-1 ~1 ~ stone 5 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| 135 | `"execute @p ~~~ detect ~ ~1 ~1 stone 5 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| 136 | `"execute @p ~~~ detect ~ ~1 ~-1 stone 5 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| 137 | `"execute @p ~~~ detect ~1 ~1 ~ snow 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| 138 | `"execute @p ~~~ detect ~-1 ~1 ~ snow 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| 139 | `"execute @p ~~~ detect ~ ~1 ~1 snow 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| 140 | `"execute @p ~~~ detect ~ ~1 ~-1 snow 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| 141 | `"execute @p ~~~ detect ~1 ~1 ~ packed_ice 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| 142 | `"execute @p ~~~ detect ~-1 ~1 ~ packed_ice 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| 143 | `"execute @p ~~~ detect ~ ~1 ~1 packed_ice 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| 144 | `"execute @p ~~~ detect ~ ~1 ~-1 packed_ice 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| 145 | `"execute @p ~~~ detect ~1 ~1 ~ ice 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| 146 | `"execute @p ~~~ detect ~-1 ~1 ~ ice 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| 147 | `"execute @p ~~~ detect ~ ~1 ~1 ice 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| 148 | `"execute @p ~~~ detect ~ ~1 ~-1 ice 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |

### commands/swords_and_more_swords/swords_and_more_swords/tag_swords

Архивный путь: `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/tag_swords.mcfunction`; SHA-256 `4a03e64a5bbe2feb1038c3b2d8098d135abb37d70a6abe96046897da190e01d9`; буквальных кандидатов вызова: 1.

| № | Исходная строка |
|---:|---|
| 1 | `"tag @e[type=item,name=\"§l§6Fire Sword\",tag=!fire_sword] add fire_sword"` |
| 2 | `"tag @e[type=item,name=\"§4TNT§f Sword\",tag=!tnt_sword] add tnt_sword"` |
| 3 | `"tag @e[type=item,name=\"§l§bIce Sword\",tag=!ice_sword] add ice_sword"` |
| 4 | `"tag @e[type=item,name=\"§l§7Wither Sword\",tag=!wither_sword] add wither_sword"` |
| 5 | `"tag @e[type=item,name=\"§l§5Ender Sword\",tag=!ender_sword] add ender_sword"` |
| 6 | `"tag @e[type=item,name=\"§g§lLightning Sword\",tag=!lightning_sword] add lightning_sword"` |
| 7 | `"tag @e[type=item,name=\"§l§eSponge Sword\",tag=!sponge_sword] add sponge_sword"` |
| 8 | `"tag @e[type=item,name=\"§l§fNether Star Sword\",tag=!nether_star_sword] add nether_star_sword"` |
| 9 | `"tag @e[type=item,name=\"§l§7Bedrock Sword\",tag=!bedrock_sword] add bedrock_sword"` |
| 10 | `"tag @e[type=item,name=\"§l§8Obsidian Sword\",tag=!obsidian_sword] add obsidian_sword"` |
| 11 | `"tag @e[type=item,name=\"Quartz Diamond\",tag=!wish_1] add wish_1"` |
| 12 | `"tag @e[type=item,name=\"Quartz Diamond block\",tag=!wish_2] add wish_2"` |
| 13 | `"tag @e[type=item,name=\"§l§gClock Sword\",tag=!wish_3] add wish_3"` |

### commands/swords_and_more_swords/swords_and_more_swords/tellraw1

Архивный путь: `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/tellraw1.mcfunction`; SHA-256 `0ee5960d0d6e4abbe2c460a74178b6309ef722d5f0a4261b4f7fa57c93ce63e4`; буквальных кандидатов вызова: 1.

| № | Исходная строка |
|---:|---|
| 1 | `"tellraw @s {\"rawtext\":[{\"text\":\"§fFor some reason you feel nauseous...\"}]}"` |

### give

Архивный путь: `Swords_B/functions/give.mcfunction`; SHA-256 `96b986ada305296f48142331386b6bbcd4e81bc3443521ba69fa81d490378de2`; буквальных кандидатов вызова: 0.

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
| 14 | `"give @s effect:lightning_sword"` |
| 15 | `"give @p effect:magma_sword"` |
| 16 | `"give @p effect:obsidian_sword"` |
| 17 | `"give @p effect:quartz_sword"` |
| 18 | `"give @p effect:sea_sword"` |
| 19 | `"give @p effect:shulker_sword"` |
| 20 | `"give @p effect:slime_sword"` |
| 21 | `"give @p effect:spectral_sword"` |
| 22 | `"give @p effect:spider_sword"` |
| 23 | `"give @p effect:sponge_sword"` |
| 24 | `"give @p effect:time_sword"` |
| 25 | `"give @p effect:tnt_sword"` |
| 26 | `"give @p effect:wither_sword"` |
| 27 | `"give @p effect:wolf_sword"` |
| 28 | `"give @p effect:ultra_instinct_sword"` |
| 29 | `"give @p effect:wither_skeleton_sword"` |
| 30 | `"give @p effect:glass_sword"` |
| 31 | `"give @p effect:clock_sword"` |
| 32 | `"give @p effect:ghost_sword"` |
| 33 | `"give @p effect:bedrock_sword"` |
| 34 | `"give @p effect:nether_star_sword"` |
| 35 | `"give @p effect:silver_sword"` |

См. также [назначение тегов и проблемы получения](manual-acquisition-issues.md), [лианы Jungle](jungle-vine-index.md), [ручной разбор Wolf](manual-wolf-conditions-2.8.md) и [общий scoreboard 1.6](manual-global-state-1.6.md).
