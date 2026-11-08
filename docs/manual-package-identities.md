# Идентификаторы пакетов и две клиентские ведьмы

[Машинная проверка объявлений](definition-audit.md) ищет `description.identifier` в разбираемых JSON каждого пакета отдельно, а также выписывает UUID/версии манифестов. Это не проверка регистрации и не все пространства имён: она не заменяет [граф ресурсов](resource-graph-2.8.14.md), учёт ванильных пакетов или работу движка. В 1.6 три повреждённых entity JSON, а в каждой 2.x `creeper.json` исключены из автоматической проверки и перечислены отдельно; повторные ключи также указаны в индексе.

## UUID и версия — не то же самое, что название файла

У `.mcaddon` **2.8.8** и **2.8.14** в манифестах одинаковы header UUID и `[1,0,0]` у каждого соответствующего пакета:

| Пакет | Header UUID | Версия | min_engine_version |
|---|---|---|---|
| Behavior | `1acf4d4b-3a3c-1be3-bc21-9512946109b1` | `[1,0,0]` | `[1,19,40]` |
| Resource | `3f15ae41-a1c1-4111-aa1e-855a98a06316` | `[1,0,0]` | `[1,19,40]` |

У них одинаковы и UUID/version соответствующих modules data, script и resources. Behavior и resource манифесты ссылаются друг на друга как dependencies. При этом название в 2.8.14 содержит `V2.8.9.5`, а требования `@minecraft/server` отличаются: `1.8.0-beta` против `1.12.0-beta` (подробности — в [анализе скрипта](manual-pumpkin-script-2.8.md)). Совпадение UUID/version при различающемся содержимом означает, что нельзя идентифицировать конкретный исходный архив только по этим двум полям. Как Bedrock разрешает импорт, обновление, кеш, одновременное подключение и зависимости, ещё не проверено; не утверждать, что оба варианта обязательно установятся рядом или что один обязательно заменит другой. Для чистого сравнения нужны раздельные профили/копии мира и проверка активного содержимого.

В **1.6** у header behavior UUID `1ecf4d4b-3a3c-1be3-bc21-9512946109b6`, у resource `2f15ae41-a1c1-4117-aa1e-855a98a06318`, версии `[1,0,0]`; `min_engine_version` в этих header **не указан**, а не задан нулём. Там тоже имеются взаимные dependencies. 26 одинаковых item ID обнаруживаются и в `Sword_B/items`, и в `Sword_R/items`, но это **разные пакеты и виды представления**, а не 26 повторов внутри одного пакета. Отсутствие таких повторов в узкой автоматической проверке не доказывает отсутствия других коллизий или корректной загрузки.

## Два `minecraft:witch` в одном resource pack 2.x

Оба 2.x содержат два **разных** `minecraft:client_entity` с одним identifier:

| Поле | `witch.entity.json` | `witch.v1.0.entity.json` |
|---|---|---|
| `description.min_engine_version` | строка `1.8.0` | не указан |
| geometry alias `default` | `geometry.villager.witch.v1.8` | `geometry.villager.witch` |
| animation `villager_general` | `animation.villager.general` | `animation.villager.general.v1.0` |
| render controller | `controller.render.witch` | `controller.render.witch.v1.0` |

Общие поля: format_version `1.8.0`, material `witch`, textures aliases `default: textures/entity/witch` и `grass_witch: textures/entity/grass_witch`, scripts.scale `0.9375`, spawn egg `spawn_egg` index 17. Оба render controller существуют в `render_controllers/witch.render_controllers.json`, используют `Geometry.default`, `Material.default` и `Array.variants[query.variant]`, массив `[Texture.default, Texture.grass_witch]`. Отличие: у `.v1.0` дополнительно `part_visibility`: `*` false, отдельно true для `head`, `nose`, `body`, `arms`, `leg0`, `leg1`, `hat`, `hat2`, `hat3`, `hat4`. Значение по умолчанию и точный результат видимости в реальном клиенте зависят от модели и движка.

Behavior `entities/witch.json` в группе `minecraft:default_witch` задаёт variant 0, в группе `minecraft:grass_witch` variant 1; оба клиентских контроллера буквально индексируют массив `query.variant`. В аддоне имеется `Swords_R/textures/entity/grass_witch.png`; `textures/entity/witch` и указанные geometry не обнаружены как соответствующие локальные файлы/определения в графе, что **не** доказывает отсутствия: они могут быть ванильными или поступать из другого resource pack. Загрузка/значение variant, разрешение двух client entity и выбор актуального renderer при разных версиях, а также texture pack priority требуют визуального теста.

Важно: один `description.min_engine_version` может быть способом выбора совместимого определения; сам повтор ID не даёт права объявлять файлы ошибкой, смешивать их поля или выбирать «последний» по порядку ZIP. Соответственно для ремейка прежде нужно выяснить, какой вариант действительно виден на нужной версии, а не удалять один автоматически.

## Оригинальные значки предметов разных версий

[Попиксельное сопоставление оригинальных PNG](icon-comparison.md) сопоставляет **только точные item ID**. У 25 общих ID между 1.6 и 2.8.14 размер либо RGBA отличаются у восьми: `bone_sword`, `cactus_sword`, `ender_sword`, `grass_sword`, `lightning_sword`, `quartz_sword`, `spectral_sword`, `wither_sword`. Например, 1.6 Wither — 16×16, 2.8.14 — 128×128; Bone в обеих 16×16, но отличаются данные 240 RGBA-пикселей, включая потенциально полностью прозрачные. Это не оценка визуального сходства или доказательство работы в игре.

У всех **42** одинаковых по ID предметов 2.8.8 и 2.8.14 разрешённые через item atlas PNG имеют одинаковый SHA-256 исходных файлов. `effect:sword_of_time` 1.6 и `effect:time_sword` 2.x в автоматическом сравнении идут отдельно: сходство названия ещё не доказывает тождества ID или поведения. Точный source path и SHA каждого изображения сохранены в отдельных [реестрах 1.6](assets-1.6.md) и [2.8.14](assets-2.8.14.md). При выборе эталона для ремейка потребуется согласовать версию, а не автоматически использовать последний файл для всех предметов.
