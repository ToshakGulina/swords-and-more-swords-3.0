# Отличия 2.8.8: природная генерация, торговля и лёд

Это ручное статическое чтение отличающихся файлов; подробное содержимое и ссылки — в [реестре 2.8.8](world-ledger-2.8.8.md), [структурах](structures-2.8.8.md) и [построчном сравнении](version-lines-2.8.8-to-2.8.14.md). Архивы названы по именам файлов, не по проверенной версии манифеста. Доступность, регистрация и итог генерации не подтверждены запуском.

## Silver ore и quartz-diamond ore

Только 2.8.8 содержит по два файла `features/*_ore.json` и `feature_rules/*_ore_feature.json`; в 2.8.14 эти четыре пути отсутствуют, хотя определения самих блоков и добычи есть в обоих. Буквальные исходные параметры:

| Поле | Silver | Quartz-diamond |
|---|---|---|
| Feature ID | `effect99:silver_ore` | `effect99:quartz_diamond_ore` |
| Structure name | `mystructure:silver_ore` | `mystructure:quartz_diamond_ore` |
| Биом, `any_of` | тег `overworld` | теги `overworld` или `the_end` |
| placement_pass | `underground_pass` | `underground_pass` |
| iterations | 5 | 5 |
| x, z | uniform, extent `[0,16]` | uniform, extent `[0,16]` |
| y | gaussian, extent `[10,35]` | gaussian, extent `[0,16]` |
| scatter_chance | numerator 160, denominator 200 | numerator 160, denominator 200 |
| adjustment_radius / facing | 1 / random | 1 / random |
| block_intersection allowlist | `minecraft:stone` | `minecraft:stone`, `minecraft:end_stone` |

В 2.8.8 оба соответствующих файла `Swords_B/structures/{silver_ore,quartz_diamond_ore}.mcstructure` содержат структуру 1×1×1 с одним блоком соответствующего `effect99:*_ore`, пустым states, без сущностей; второй слой индексов содержит −1. В 2.8.14 silver-структура остаётся, но quartz-структура отсутствует. Сопоставление файлов с `mystructure:` зависит от правил разрешения имён структуры в движке и пространстве мира; одно наличие файла не доказывает действительное размещение. 160/200 — записанная дробь scatter_chance, **не** безусловный шанс руды на блок, чанк или мир: влияют iterations, биомы, разрешение структуры, ограничения и обработка распределений.

## Emerald Sword: два объявления торговли только в 2.8.8

- `Swords_B/trading/economy_trades/weapon_smith_trades.json`: tier `total_exp_required:310`, группа `num_to_select:1` содержит сделку: хочет 32 `minecraft:emerald_block`, price_multiplier 0, выдаёт один `effect:emerald_sword` с функцией `enchant_with_levels` (`treasure:false`, уровни min 5/max 60), trader_exp 0, max_uses 2, reward_exp true.
- `Swords_B/trading/weapon_smith_trades.json`: tier с индексом 2 содержит сделку: хочет `minecraft:emerald_block` quantity min 24/max 32, выдаёт `effect:emerald_sword` с той же функцией уровней 5…60; quantity результата явно не указан. Другие сделки tier содержат алмазные инструменты и изумруды. Точный список, группы и все остальные настройки — в реестре мира.
- Ни один из этих двух файлов не содержится в 2.8.14. Это не доказывает, какую из таблиц выберет движок, что торговец зарегистрирует сделку или что меч гарантированно появится. Обе версии также содержат отдельные loot-записи меча, которые нельзя сводить к торговле.

## `effect99:fake_ice` и Ice Sword

Только 2.8.8 содержит `Swords_B/blocks/fake_ice.json`, где свойства `fake_ice:model` могут принимать 1, 2, 3, 4. Для 1, 2, 3 существуют отдельные permutations с `minecraft:ticking` `looping:false`, range `[2,2]`, события `set_model2`, `set_model3`, `set_model4` соответственно; события присваивают строковые выражения `"2"`, `"3"`, `"4"`. При модели 4 ticking `looping:true`, `[2,2]`, event `destroy_block` выполняет `setblock ~ ~ ~ air 0 destroy`. Геометрии `geometry.fake_ice`, `fake_ice2`, `fake_ice3`, `fake_ice4`; базово destroy_time 9999, explosion_resistance 10, loot `loot_tables/empty.json`. Настоящая длительность смены состояний, исходный property после команды fill, поведение destroy и замена ранее существовавшей воды не доказаны — проверить загрузку блока и мир в соответствующем движке.

В 2.8.14 те же участки команд `items/ice_sword.json` и `entities/player.json` используют `frosted_ice` вместо `effect99:fake_ice`, а файл блока fake_ice отсутствует. Это не доказательство идентичного таяния: даже если команды выполняются, меняется тип блока и логика его последующей обработки.

### Точное побайтовое ограничение различия Ice

Сопоставлены все 42 item ID этих двух архивов: у **41** соответствующие behavior-item JSON совпадают побайтово; единственный отличающийся — `Swords_B/items/ice_sword.json`. В нём замена всех **40** буквальных вхождений `effect99:fake_ice` на `frosted_ice` в копии данных **в памяти** делает файл побайтово равным версии 2.8.14. Аналогично в `Swords_B/entities/player.json` замена всех **11** вхождений даёт побайтовое совпадение. Это не исправление файлов и не утверждение, что блоки функционально эквивалентны; это точное описание различия именно этих двух файлов. Остальные отличия архивов — в [полном побайтовом сравнении](version-diff.md). Даже идентичные item JSON могут вести себя иначе из-за сущностей, ресурсов, генерации или внешнего контекста.
