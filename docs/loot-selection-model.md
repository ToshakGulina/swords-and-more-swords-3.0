# Условная модель выбора прямых loot-записей 2.x

Охват: 29 прямых entries с `type:item` и ID `effect:`/`effect99:` в 25 пулах; 27 строк после группировки одинакового ID в одном пуле. Обе версии 2.x имеют структурно одинаковые локальные loot JSON. Только обычные `pools[].entries[]`; это не все способы получения и не анализ динамических или внешних таблиц. Родительские таблицы в эту арифметику не включаются ([контекст и 2 локальных родительских ссылки](loot-context.md)).

**Проценты показывают только модель выбора как минимум одной указанной записи при уже активированном пуле, а не шанс выпадения предмета, сундука, смерти или заброса.** Предполагается, что все перечисленные entries доступны, отсутствующий weight равен 1, quality и модификаторы не влияют, выборы независимы с возвращением, целое число rolls равномерно распределено по границам. Любые условия пула считаются уже выполненными, условия entries игнорируются, функции и фактическая выдача не эмулируются. Неизвестны регистрация таблицы, выбор источника, семантика движка, поведение count, loot и слотов.

Числитель — сумма весов записей **одного и того же точного ID** внутри данного пула; знаменатель — сумма весов **всех** entries, включая другие типы и предполагаемые по 1. В последнем столбце показаны полные `functions` каждой целевой записи; `не задано` не означает гарантированный count 1. Если у разных записей одного ID разные функции, их веса агрегированы только для события «запись выбрана», не для числа предметов.

| Таблица / pool | ID | Индексы entries | rolls | Вес ID / сумма | Выбор ≥1 записи, модель | Риски и условия |
|---|---|---|---|---|---:|---|
| `bee_sword.json` / 0 | `effect:bee_sword` | 0 | `1` | 1/1 | 100.0000% | functions: не задано |
| `blocks/quartz_diamond_block.json` / 0 | `effect99:quartz_diamond_block` | 0 | `1` | 1/1 | 100.0000% | functions: `[{"function":"set_count","count":{"min":1,"max":1}}]` |
| `blocks/quartz_diamond_ore.json` / 0 | `effect:quartz_diamond` | 0, 1, 2 | `1` | 100/100 | 100.0000% | functions: `[{"function":"set_count","count":{"min":1,"max":1}}]`, `[{"function":"set_count","count":{"min":1,"max":2}}]`, `[{"function":"set_count","count":{"min":2,"max":4}}]` |
| `blocks/silver_ore.json` / 0 | `effect99:silver_ore` | 0 | `1` | 1/1 | 100.0000% | functions: `[{"function":"set_count","count":{"min":1,"max":1}}]` |
| `chests/abandoned_mineshaft.json` / 1 | `effect:spider_sword` | 5 | `{"min":2,"max":4}` | 3/86 | 10.0665% | functions: `[{"function":"set_count","count":{"min":1,"max":1}}]` |
| `chests/buriedtreasure.json` / 1 | `effect:sea_sword` | 8 | `{"min":5,"max":12}` | 15/219 | 44.5623% | functions: не задано |
| `chests/desert_pyramid.json` / 0 | `effect:tnt_sword` | 8 | `{"min":2,"max":4}` | 10/242 | 11.8392% | functions: не задано |
| `chests/igloo_chest.json` / 0 | `effect:ice_sword` | 6 | `{"min":2,"max":8}` | 1/64 | 7.5263% | functions: не задано |
| `chests/jungle_temple.json` / 0 | `effect:jungle_sword` | 8 | `{"min":2,"max":6}` | 16/457 | 13.1758% | functions: не задано |
| `chests/pillager_outpost.json` / 3 | `effect:emerald_sword` | 5 | `{"min":2,"max":3}` | 3/28 | 24.5513% | 1 отсутствующих weight → 1 в модели; functions: `[{"function":"set_count","count":{"min":0,"max":1}}]` |
| `chests/pillager_outpost.json` / 3 | `effect:lapis_sword` | 6 | `{"min":2,"max":3}` | 3/28 | 24.5513% | 1 отсутствующих weight → 1 в модели; functions: `[{"function":"set_count","count":{"min":0,"max":1}}]` |
| `chests/spawn_bonus_chest.json` / 0 | `effect:coal_sword` | 0 | `1` | 1/5 | 20.0000% | functions: не задано |
| `chests/stronghold_corridor.json` / 0 | `effect:emerald_sword` | 16 | `{"min":2,"max":3}` | 5/521 | 2.3809% | functions: не задано |
| `chests/stronghold_corridor.json` / 0 | `effect:lapis_sword` | 17 | `{"min":2,"max":3}` | 5/521 | 2.3809% | functions: не задано |
| `chests/stronghold_library.json` / 0 | `effect:lapis_sword` | 3 | `{"min":2,"max":10}` | 5/275 | 10.3245% | functions: не задано |
| `chests/underwater_ruin_big.json` / 1 | `effect:magma_sword` | 1 | `1` | 1/24 | 4.1667% | functions: не задано |
| `chests/village/village_snowy_house.json` / 0 | `effect:ice_sword` | 9 | `{"min":3,"max":8}` | 4/57 | 32.4613% | 4 отсутствующих weight → 1 в модели; другие поля таблицы: `{"type":"minecraft:chest"}`; functions: `[{"function":"minecraft:set_count","count":{"min":1,"max":1}}]` |
| `chests/woodland_mansion.json` / 0 | `effect:emerald_sword` | 9 | `{"min":1,"max":3}` | 25/670 | 7.2788% | functions: не задано |
| `entities/blaze.json` / 1 | `effect:blaze_sword` | 0 | `1` | 1/1 | 100.0000% | pool conditions: `[{"condition":"killed_by_entity","entity_type":"minecraft:snow_golem"},{"condition":"random_chance_with_looting","chance":0.025,"looting_multiplier":0.02}]`; functions: `[{"function":"set_data","data":0}]` |
| `entities/elder_guardian.json` / 1 | `effect:sponge_sword` | 0 | `1` | 1/1 | 100.0000% | pool conditions: `[{"condition":"killed_by_player"},{"condition":"random_chance_with_looting","chance":0.065,"looting_multiplier":0.02}]`; functions: `[{"function":"set_count","count":{"min":1,"max":1}},{"function":"set_data","data":0}]` |
| `entities/living_flame.json` / 0 | `effect:fire_sword` | 0 | `1` | 1/1 | 100.0000% | functions: `[{"function":"set_data","data":0}]` |
| `entities/red_enderman.json` / 0 | `effect:ender_sword` | 0 | `1` | 1/1 | 100.0000% | pool conditions: `[{"condition":"killed_by_player"},{"condition":"random_chance_with_looting","chance":0.025,"looting_multiplier":0.02}]`; functions: `[{"function":"set_data","data":0}]` |
| `entities/shulker.json` / 1 | `effect:shulker_sword` | 0 | `1` | 1/1 | 100.0000% | pool conditions: `[{"condition":"killed_by_player"},{"condition":"random_chance_with_looting","chance":0.045,"looting_multiplier":0.02}]`; functions: `[{"function":"set_count","count":{"min":1,"max":1}},{"function":"set_data","data":0}]` |
| `entities/slime_king.json` / 0 | `effect:slime_sword` | 0 | `1` | 1/1 | 100.0000% | pool conditions: `[{"condition":"killed_by_player"},{"condition":"random_chance_with_looting","chance":0.04,"looting_multiplier":0.02}]`; functions: `[{"function":"set_data","data":0}]` |
| `entities/wither_skeleton.json` / 3 | `effect:wither_skeleton_sword` | 0 | `1` | 1/1 | 100.0000% | pool conditions: `[{"condition":"killed_by_player"},{"condition":"random_chance_with_looting","chance":0.025,"looting_multiplier":0.02}]`; functions: `[{"function":"set_data","data":0}]` |
| `gameplay/fishing/treasure.json` / 0 | `effect:jungle_sword` | 4 | `1` | 5/41 | 12.1951% | functions: не задано |
| `pumpkin_sword.json` / 0 | `effect:cursed_pumpkin_sword` | 0 | `1` | 1/1 | 100.0000% | functions: не задано |

## Прочтение граничных примеров

- `entities/blaze.json` и пять других одноэлементных условных entity-пулов могут показывать 100% в последнем столбце **при уже выполненных условиях пула**. Их chance/killed_by_* указаны рядом и не равны 100%; частота события, looting и выполнение таблицы отдельно не установлены.
- `chests/pillager_outpost.json`: `set_count` 0…1 у Emerald и Lapis; выбор записи не доказывает ненулевую выдачу. В одном соседнем entry вес не задан, 1 — только явное предположение модели.
- `blocks/quartz_diamond_ore.json`: три записи одного ID (веса 89/10/1) суммированы в событие выбора ID; count у них различается. 100% выбора не означает одного предмета, гарантированной выдачи или срабатывания добычи.
- `gameplay/fishing/treasure.json`: только условный выбор внутри treasure, не шанс рыбалки. Два локальных родителя имеют собственные веса и quality; их условия и способ вызова не включены.
- Расчёт не доказывает существование/генерацию нужного сундука, успешное размещение блока, выпадение с конкретного существа, отсутствие альтернативных пакетов или корректную работу на Bedrock 26.62.
