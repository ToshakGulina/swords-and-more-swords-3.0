# Повторная пофайловая проверка исходных архивов

Все записи файлов в трёх архивах перечитаны из ZIP с проверкой CRC, SHA-256 и ограниченной проверкой по типу. Это **не** подтверждение полного ручного понимания каждого файла, совместимости, воспроизведения игры или поведения Bedrock. Локальные исходники не изменялись. [Полный машиночитаемый список по каждому пути](../data/file-validation.json) · [сводка аудита](static-audit-summary.md).

JSON/material: JSON5 с проверкой дублирующихся ключей; при ошибке строгого разбора отдельно пробуется обычный JSON5 и сохраняется ошибка. Изображения: Pillow verify и полное декодирование пикселей, не оценка сходства. `.mcstructure`: little-endian NBT → SNBT → NBT, побайтовая обратная проверка. Ogg: только метаданные контейнера/кодека, **не** полное декодирование и прослушивание. JS, mcfunction и lang: UTF-8, а не полная семантика. Повторные ключи lang указаны отдельно. Отсутствие ошибки парсера не подтверждает валидность схемы или работу Bedrock.

Наличие точного пути в каком-либо другом Markdown-документе (без инвентаризаций и этого документа) отмечается только как **буквальное упоминание**. Оно не означает, что каждый байт или все косвенные связи вручную изучены.

| Архив | Файлы | JSON5 без дублей | JSON с повтором | JSON не разобран | Прочие ошибки/неподдержанные | Путь буквально встречается вне инвентаризации |
|---|---:|---:|---:|---:|---:|---:|
| 1.6 | 170 | 135 | 0 | 3 | 0 | 170 |
| 2.8.8 | 403 | 274 | 3 | 1 | 0 | 403 |
| 2.8.14 | 395 | 267 | 3 | 1 | 0 | 395 |

## Исключения и неоднозначности

- 1.6 `Sword_B/entities/blaze2.json` — `invalid`: `<string>:78 Unexpected "}" at column 1`.
- 1.6 `Sword_B/entities/bone2.json` — `invalid`: `<string>:75 Unexpected "}" at column 1`.
- 1.6 `Sword_B/entities/shulker2.json` — `invalid`: `<string>:75 Unexpected "}" at column 1`.
- 2.8.8 `Swords_B/entities/creeper.json` — `invalid`: `<string>:430 Unexpected "}" at column 3`.
- 2.8.8 `Swords_B/entities/living_flame.json` — `duplicate_keys`: `Duplicate key "minecraft:fire_immune" found in object`.
- 2.8.8 `Swords_B/entities/mountable_slime.json` — `duplicate_keys`: `Duplicate key "despawn" found in object`.
- 2.8.8 `Swords_B/entities/slime_king.json` — `duplicate_keys`: `Duplicate key "minecraft:movement.jump" found in object`.
- 2.8.8 `Swords_R/texts/en_US.lang` — повторный ключ lang `entity.entity:ghost.name`: 2 строк; приоритет не установлен.
- 2.8.14 `Swords_B/entities/creeper.json` — `invalid`: `<string>:430 Unexpected "}" at column 3`.
- 2.8.14 `Swords_B/entities/living_flame.json` — `duplicate_keys`: `Duplicate key "minecraft:fire_immune" found in object`.
- 2.8.14 `Swords_B/entities/mountable_slime.json` — `duplicate_keys`: `Duplicate key "despawn" found in object`.
- 2.8.14 `Swords_B/entities/slime_king.json` — `duplicate_keys`: `Duplicate key "minecraft:movement.jump" found in object`.
- 2.8.14 `Swords_R/texts/en_US.lang` — повторный ключ lang `entity.entity:ghost.name`: 2 строк; приоритет не установлен.

## Состав исходной папки и границы проверки

В повторном списке Google Диска 25 файлов: 3 исходных mcaddon, 21 JPEG, один серверный ZIP. Три mcaddon здесь перечитаны; MD5 сравнивались с метаданными Диска. Все 21 JPEG повторно загружены: MD5 совпал с метаданными Диска, SHA-256 — с прежним OCR-индексом, изображения успешно декодированы. Ранее 20 описаний и браузерный снимок просмотрены визуально; **полной вручную выверенной транскрипции 21 изображения нет** ([OCR](screenshot-ocr.md), [выборочная визуальная сверка](screenshot-visual-review.md)). Серверный ZIP повторно проверен по MD5/SHA-256, CRC и хэшам **3384** файлов, без запуска; в 658 `.brarchive` найдены 9543 записи, из которых 312 с сигнатурой MCB не декодированы; четыре других двоичных файла тоже не декодированы, а 1608 `.nbt` проверены только как gzip, не как полностью разобранные NBT. Это не полная семантическая проверка серверного бинарника и ванильных данных ([сервер](server-archive.md)).

Имеются неразобранные JSON, повторные ключи, а также неизвестные приоритеты, внешние зависимости, порядок событий и поведение движка. Поэтому ответ «каждый файл полностью понят и проверен» не подтверждён. Можно опираться на буквальные выписки и тематические цепочки, но перенос поведения без последующей отдельной проверки остаётся с риском.
