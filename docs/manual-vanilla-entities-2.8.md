# Шестнадцать ванильных сущностей 2.x: вложенные отличия и цепочки

Это продолжение [сравнения 22 ванильных ID](manual-vanilla-override-review.md): здесь разобраны оставшиеся 16, помимо player, blaze, cat, parrot, skeleton и wolf. Два файла аддона для каждого из этих 16 имён **побайтово совпадают** между 2.8.8 и 2.8.14. Анализ — чтение данных, без Minecraft. Он не доказывает, что Bedrock загрузит именно эти определения, каким будет порядок событий, кто является `other`, что выполнится legacy-команда, или какое значение назначит движок при отсутствии поля. Числа весов ниже — только **условные доли при вызове конкретного randomize и принятой модели весов**; фильтры, нормализация, кратность вызовов и успех команд отдельно не установлены.

Сравнение сделано с обоими внешними официальными образцами Mojang `v1.19.40.2` и `v1.20.30.1`, не с установленной игрой и не с известной основой автора. Источники, commit, SHA-256 ZIP, выбор ориентиров, исключения `creeper` и `item` — в [первом документе](manual-vanilla-override-review.md). [Полная выписка различающихся значений](vanilla-entity-detail-ledger.md) содержит для обоих образцов **весь** объект каждого отличающегося top-level ключа, включая `format_version` и `description`; [машинные данные](../data/vanilla-entity-detail-diff.json) сохраняют `present` отдельно от значения.

Заново скачать два ZIP по ссылкам из первого документа; затем выполнить:

```sh
python tools/build_vanilla_detail_diff.py \
  --reference-119 /путь/bedrock-samples-v1.19.40.2.zip \
  --reference-120 /путь/bedrock-samples-v1.20.30.1.zip
```

Генератор проверяет SHA-256 обоих ZIP, ID сущностей, корректность JSON5 без повторных ключей и побайтовую идентичность 16 файлов аддона между версиями. Массивы сравниваются с порядком, порядок ключей объектов неважен, числа 1 и 1.0 считаются равными. `root` охватывает только `format_version`, не любые другие корневые ключи; в `minecraft:entity` сравнены `description`, `components`, `component_groups`, `events`. Это полная **структурная выписка указанных разделов**, не доказательство полноты связей с остальными файлами или семантики. Табличные ссылки и численные данные ниже проверяются тестами на локальных архивах и сохранённых выдержках; полное воспроизведение с оригинальными внешними ZIP проверяет также их хэши.

## Обычные существа: получение и фоновые отличия

### Пчела `minecraft:bee`

- `bee.json`: `angry_bee` вызывает при атаке `countdown_to_perish_event`; в аддоне первый шаг события имеет ветви **2/98**, причём ветвь 2 дополнительно фильтрует `self` family `!= bee_sword` и выполняет `loot spawn ~ ~ ~ loot bee_sword`. После этого отдельно удаляются перечисленные группы и добавляется `countdown_to_perish` с timer `[10,60]`, `looping:false`, `randomInterval:true`. Это не «2% при любой смерти» и не доказательство успешного loot. Вызывается именно код обычной пчелы, не определение отдельной `entity:bee_sword`: [подробная цепочка](manual-bee-sword.md).
- Важная межверсионная поправка: образец 1.19.40.2 содержит `minecraft:is_charged` в `has_nectar` и не объявляет `description.properties.minecraft:has_nectar`. У аддона вместо этого свойство bool `minecraft:has_nectar`, `client_sync:true`, default `query.had_component_group('has_nectar')`, а соответствующие условия/события используют `bool_property`/`set_property`. **Образец 1.20.30.1 тоже использует это свойство и выбранные nectar-события совпадают с аддоном**; нельзя приписать эту конкретную разницу исключительно модификации меча. Другие части пчелы, в том числе цветочные списки и countdown, в образце 1.20 отличаются — точные объекты в выписке.

### Эндермен `minecraft:enderman`

- В `minecraft:entity_spawned` аддон задаёт ветви weight **80** для default и **20** для red, у red есть `has_biome_tag == overworld`. При выборе red добавляются `minecraft:red_enderman`, `red_enderman`, `minecraft:enderman_calm`; группа red задаёт health **120/120**, attack **12**, scale **1.2**, follow_range **64/64**, loot `loot_tables/entities/red_enderman.json`. Loot-пул отдельно имеет `killed_by_player` и `random_chance_with_looting` **0.025**, multiplier **0.02**, одну запись `effect:ender_sword`. Нельзя перемножить веса в безусловный шанс: eligibility, перезапуск, убийство, looting и исполнение команды не установлены.
- В базовом `hurt_on_condition` сохранена лава `damage_per_tick:4`, а водный фильтр в аддоне `in_water_or_rain`, в обоих образцах `in_contact_with_water`, `damage_per_tick:1`, cause `drowning`. У аддона отсутствует базовый `minecraft:despawn`, заданный в обоих образцах; default и поведение не выводятся. В аддоне `format_version:1.13.0`, в обоих образцах `1.16.0`. Образец 1.20 задаёт базовый follow_range **64/64**, а 1.19 и аддон **32/32**; у red-группы аддона отдельно 64/64. Приоритет группы и базового компонента без движка не установлен.

### Гаст `minecraft:ghast`

- В обоих образцах `damage_sensor` запрещает fall damage. У аддона это массив из двух триггеров: первый с `on_damage` фильтром `is_family:ghast`, **без явно записанного subject**, вызывает `spectral_ghast`, `deals_damage:true`; второй запрещает fall. В `spectral_ghast` веса **94/6**, ветвь 6 содержит `structure load spectral_sword ~~~`. В этом первом фильтре нет явного `has_damage:fatal`; нельзя говорить, что запись гарантированно проверяет убийцу или только смерть. Цель фильтра, вызов и структура требуют проверки.
- Collision box у образцов `4.02×4`, у аддона `4×4`; `minecraft:fire_immune` в образцах `{}`, в аддоне `true`. Компонент `minecraft:despawn` отсутствует в базе аддона, но присутствует в образцах. Это различия формы и значений, а не подтверждение hitbox, неуязвимости или despawn.

### Паук `minecraft:spider`

- Базовый `minecraft:attack.damage` **2** в обоих образцах, **3** в аддоне. Четыре поведения `hurt_by_target`, `random_stroll`, `look_at_player`, `random_look_around` из базовых компонентов образцов в аддоне перенесены в группу `minecraft:default_spider`; первая запись `minecraft:entity_spawned.sequence` её добавляет, затем следует randomize jockey. Нельзя считать их просто удалёнными: действительность входа и порядок применения зависят от движка.
- Player event `minecraft:spider_sword` содержит `ride @s summon_ride minecraft:spider no_ride_change minecraft:spider_sword`; одноимённое событие паука удаляет три группы, включая default_spider, и добавляет `minecraft:spider_player_jockey`: health **20/20**, jump strength `[0.4,0.7]`, family включает `spider_sword`, rideable для `player`, `minecraft:loot` указывает `loot_tables/entities/empty.json`. У паука есть группа `despawn`, хотя компонента нет в базе; event `minecraft:despawn` фильтрует family `spider_sword`. Связанный `not_climb` содержит четыре legacy detect и снятие levitation. Подробнее: [Spider по версиям](manual-fire-spider-sponge.md).

### Ведьма `minecraft:witch`

- У аддона `minecraft:entity_spawned` содержит веса **80/20** для `minecraft:default_witch` и набора `minecraft:grass_witch`, `grass_witch`. Последний задаёт family `grass_witch`, health **32/32**, follow_range **80**, sensor `grass_witch_skill`, а `minecraft:on_death` вызывает `grass_sword`. В событии `grass_sword` веса **80/20**; ветвь 20 содержит `structure load grass_sword ~~~`, `setblock ~ ~ ~ double_plant 2` и звук. Это две разные стадии, не подтверждение безусловного 4%-го шанса получения: условия вызова, порядок, результат записи структуры и возможные иные пути не проверены. Подробнее: [Grass Sword](manual-grass-sword.md).
- В группе `minecraft:raid_configuration` `dweller.can_migrate` у обоих образцов `true`, у аддона `false`; `minecraft:raid_persistence` и `minecraft:raid_expired` заданы в образцах, отсутствуют в файле аддона; вызовы raid и celebrate тоже различаются. Это не доказательство изменения механики рейдов в игре. Образец 1.20.30.1 дополнительно объявляет в базе `minecraft:behavior.drink_potion`, `minecraft:shooter` и `minecraft:behavior.nearest_prioritized_attackable_target`, которых нет в базе аддона; образец 1.19.40.2 отличается иначе. `format_version` — аддон `1.13.0`, образцы `1.16.0` / `1.19.60`.

### Иссушитель `minecraft:wither`

- Образцы содержат damage_sensor для `other` family `undead` с `deals_damage:false`. У аддона дополнительно триггер `other` с `has_equipment` hand `effect:nether_star_sword`, family `player` и `has_damage:fatal`: событие `wither_sword`, `deals_damage:true`. Оно содержит веса **87/13**, ветвь 13 — `structure load wither_sword ~ ~ ~`. Число 13/100 — условная доля при отработке этого randomize, не частота убийств или получения.
- `minecraft:fire_immune` у аддона `true`, у обоих образцов `{}`; при этом `description.is_spawnable:false` у аддона и в образце 1.19, но `true` в образце 1.20. Различие boolean описания не доказывает фактическую доступность spawn. См. также [Nether Star](manual-ghost-nether-ultra.md) и [Wither Sword](manual-ender-wither-tnt-slime.md).

## Молния и Ender Crystal

### `minecraft:lightning_bolt` → `entity:centella`

- У аддона `minecraft:entity_spawned` добавляет группу `spawn_centella`, в которой timer `[0,0]`, `looping:false` вызывает событие `spawn_centella`. В нём веса **80/20**; ветвь 20 содержит `summon entity:centella ~ ~1 ~`. В обоих образцах этих группы и событий нет. В записи нет фильтра, ограничивающего её только молнией от меча, но загрузка/вызов spawn event и трактовка нулевого timer не доказаны.
- У `entity:centella` base health `value:200`, family `[effect99_entities,centella,spherical_lightning]`; looping timer `[10,60]` направлен на `minecraft:start_death`, добавляющий группу despawn. Sensor-событие `minecraft:centella` содержит в том числе `effect @e[family=!effect99_entities,r=2] instant_damage 1 0 true` и два `fill` lightblock. Это объявления без гарантии периодичности/успеха.
- Два отдельных damage_sensor триггера требуют `has_damage:fatal`; первый дополнительно требует `other` family `player` и вызывает `centella_death_by_player`, второй без этого условия вызывает `centella_death`. Оба события содержат `summon lightning_bolt ~~~ default_lightning_bolt`; первое ещё содержит randomize **98/2**, где ветвь 2 загружает `lightning_sword` на `~ ~10 ~`. Фильтры пересекаются: нельзя по статике доказать, вызовется один из них или оба. Возможна циклическая цепочка, **если** создание такой молнии также активирует `minecraft:entity_spawned`, но применение именованного события при summon и поведение движка не доказаны; не рассчитать вероятность бесконечного цикла.
- Компонент centella ссылается на `loot_tables/entity/centella.json`; такого пути в архиве 2.8.14 не найдено. Это не доказывает отсутствия таблицы извне. Буквальная структура `structures/lightning_sword.mcstructure` в архиве есть. Связанные данные — [Lightning 1.6](manual-lightning-1.6.md) и [2.x](manual-traces-2.8.14.md).

### `minecraft:ender_crystal`

- У обоих образцов базовый `minecraft:on_hurt` вызывает `minecraft:crystal_explode`; в аддоне базового компонента нет, но он существует в группе `on_hurt_crystal`. В `minecraft:entity_spawned` при `has_biome_tag != nether` добавляется эта группа, при `has_biome_tag nether` — `spectral_sword_drop`; у последней `on_hurt` вызывает `spectral_crystal_explode`. Это два фильтра с разными ветвями, не доказательство работы всех измерений.
- `spectral_crystal_explode`: randomize **98/2**, где ветвь 2 выполняет `structure load spectral_sword ~~~`; затем отдельный шаг добавляет `crystal_exploding`. Условие 2/100 только на вызов и модель выбора; структура находится в архиве. Другая цепочка `minecraft:detect_player` добавляет sensor, затем `ride_player` содержит `ride @s start_riding @p[family=spectral_sword,r=3] teleport_rider`. Player-файл содержит `summon ender_crystal ~ ~1.8 ~ minecraft:detect_player`. Контроллеры `despawn_crystal`/`mount_crystal` и события с теми же именами тоже записаны, но успешный ride не доказан.
- В образце 1.20.30.1 базовый collision box **2×2**, в образце 1.19 и аддоне **0.98×0.98**: ещё один пример того, почему выбранная ванильная точка отсчёта важна. [Spectral Sword и мир](manual-spectral-world-2.8.md).

## TNT и ванильные снаряды

### `minecraft:tnt`

- В образцах `minecraft:explode` находится в базовых компонентах: fuse **4**, power **4**, `causes_fire:false`. У аддона он перенесён в группу `default_tnt`, добавляемую `minecraft:entity_spawned`, с теми же значениями и дополнительным `destroy_affected_by_griefing:true`. Нельзя объявить, что TNT не взрывается только из-за отсутствия компонента в базе.
- Отдельное событие `giant_tnt` удаляет default и добавляет одноимённую группу: fuse **8**, power **16**, `causes_fire:true`, `destroy_affected_by_griefing:true`, scale **2**, timer **7.99** → `camerashake` (радиус 32). Item `effect:tnt_sword` содержит команду `summon minecraft:tnt ~~~ giant_tnt`. Действие griefing и порядок spawn event/явного события не доказаны. Кроме того, аддон определяет другие TNT-сущности; их нельзя сливать: [TNT по версиям](manual-ender-wither-tnt-slime.md).

### `minecraft:arrow`

- В изменённом spawn sequence `other` с hand `effect:bone_sword` добавляет группу `despawn_arrow`, а `other` family `skeleton` — `family:arrow`; сохранены и дополнительные исходные ветви. Группа `despawn_arrow` задаёт family `[bone_sword_arrow,effect99_entities]`, timer `[1,1]` → `start_despawn_arrow` и projectile с impact damage `[1,4]`, `remove_on_hit:{}`. Сама группа `start_despawn_arrow` содержит `minecraft:despawn:{}`. Группы hard/player/pillager также добавляют family `[arrow]`; совпадение/перезапись групп и `other` без игры не установлены.
- Player event `minecraft:bone_sword` содержит `event entity @e[family=arrow,r=8] minecraft:inertia_disable`; событие стрелы удаляет группы `minecraft:player_arrow`, `minecraft:pillager_arrow`, `minecraft:hard_arrow`, `family:arrow` и добавляет `minecraft:inertia_disable` с `power:0`, `gravity:1`, `inertia:0`, `liquid_inertia:0`. Это selector по family, не доказательство воздействия на все или только вражеские стрелы. [Bone Sword](manual-companion-projectile-swords.md).

### `minecraft:fireball` и `minecraft:small_fireball`

- У большого fireball оба образца в базовом `projectile.on_hit` имеют impact_damage **6** и definition_event `minecraft:explode`; в аддоне `impact_damage` отсутствует, но definition_event сохранён. Collision box у обоих образцов **1×1**, у аддона **0.31×0.31**. При spawn фильтр `other` family `player` добавляет группу projectile `gravity_enable`, `gravity:0.04`, и команду звука. Отсутствие прямого impact_damage не доказывает отсутствия всех источников урона: сохранённый event добавляет группу с `minecraft:explode` power **1**.
- У small_fireball базовый impact damage **5** в обоих образцах и аддоне, `knockback:true` в образцах и `false` в аддоне. Spawn фильтр `other` family `player` или `fire_sword_skill` добавляет `gravity_enable` (`gravity:0.02`); условие `other` family `blaze` добавляет family `[small_fireball,shot_by_the_blaze]`. Player event `minecraft:blaze_sword` посылает `minecraft:inertia_disable` по `@e[family=shot_by_the_blaze,r=7]`; событие снаряда удаляет соответствующую группу и добавляет projectile с power **0**, gravity **0.06**, inertia и liquid_inertia **0**. Селектор и динамику снаряда необходимо проверить, а не предполагать перехват всех снарядов.

### `minecraft:snowball`, `minecraft:shulker_bullet`

- В snowball аддона baseline projectile не содержит `anchor` и `offset`, указанные в обоих образцах; `format_version` аддона `1.12.0`, образцов `1.16.0`. Условие spawn `other` с `effect:ice_sword` добавляет группу `ice_sword`; её projectile на hit вызывает событие `ice_sword`, где записано `fill ~ ~ ~ ~ ~ ~ snow_layer 0 replace air`. Это не доказывает успешную установку снега или какие именно попадания вызовут событие. [Ice 2.x](manual-ice-geometry-2.8.md).
- В `minecraft:shulker_bullet` базовый projectile у образцов имеет levitation amplifier **0**, у аддона **1**; durationeasy/normal/hard **200** во всех. Отдельная группа `shulker_sword`, условно добавляемая при `other` hand `effect:shulker_sword`, имеет gravity **0.01**, `homing:false`, `destroyOnHurt:false`, при сохранённом amplifier **1**. `destroyOnHurt` сохранено с точным регистром; нельзя предполагать, как парсер обработает имя. [Shulker Sword](manual-companion-projectile-swords.md).

### `minecraft:wither_skull` и `minecraft:wither_skull_dangerous`

В обоих файлах spawn sequence проверяет `other` hand `effect:wither_sword` и добавляет группу `wither_sword`. Группа задаёт collision box **0×0** и projectile: для обычного power **1.2**, gravity **0.05**; для dangerous power **0.6**, gravity **0.005**, `is_dangerous:true`, `reflect_on_hurt:true`. В обоих `shoot_target:false`, wither effect amplifier **1**, durationeasy **0**, normal **200**, hard **800**. Это значения отдельной условной группы, не характеристики всех черепов. Наличие группы и применение нулевой collision box не доказывают физику или успешное попадание.
