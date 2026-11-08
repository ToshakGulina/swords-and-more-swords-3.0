# Item on-use и cooldown: 1.6 и 2.x

В 26 item JSON 1.6 компоненты `minecraft:on_use` и `minecraft:cooldown` отсутствуют: это не означает, что движок или helper не выполняют какие-либо действия при использовании. У 42 item ID 2.x 14 таких hook и 14 cooldown; оба компонента структурно одинаковы в 2.8.8 и 2.8.14. `on_use` event совпадает у 13, а у Ice отличается только буквальная замена `effect99:fake_ice` → `frosted_ice`. Прочие файлы и поведение версий могут различаться.

Таблица — **объявления item**, не подтверждённые действия или фактический расход. `duration` сохранён в единицах оригинального компонента; не считать его автоматически тиками или секундами целевой версии. `damage` показан только для прямых действий event; стандартный износ, on-hit, зачарования, раннее разрушение и косвенные команды не учитываются.

`sequence` обозначает явно записанный массив в данном порядке, но исполнение и ошибки движка не испытаны. Несколько ключей одного объекта — **соседние поля, не доказанная последовательность и не утверждение об одновременности**. Для `run_command.target` различаются буквальный `holder` и отсутствие поля; не подставлять дефолт без проверки. Команды/стрельба могут сработать или не сработать независимо от ожидаемой прочности.

| Точный ID | cooldown целиком | Форма event | Прямой durability damage | run_command: число / target | shoot целиком |
|---|---|---|---|---|---|
| [`effect:blaze_sword`](items-2.8.14.md#effectblaze_sword) | `{"category":"blaze_sword","duration":20}` | один объект: damage + run_command | `{"type":"durability","amount":10,"target":"self"}` | 3 / не задан | не задано |
| [`effect:clock_sword`](items-2.8.14.md#effectclock_sword) | `{"category":"clock_sword","duration":30}` | один объект: damage + run_command | `{"type":"durability","amount":10,"target":"self"}` | 1 / не задан | не задано |
| [`effect:creeper_sword`](items-2.8.14.md#effectcreeper_sword) | `{"category":"creeper_sword","duration":3}` | sequence: run_command → damage | `{"type":"durability","amount":1,"target":"self"}` | 1 / `holder` | не задано |
| [`effect:ender_sword`](items-2.8.14.md#effectender_sword) | `{"category":"ender_sword","duration":2}` | один объект: run_command + damage | `{"type":"durability","amount":5,"target":"self"}` | 2 / не задан | не задано |
| [`effect:fire_sword`](items-2.8.14.md#effectfire_sword) | `{"category":"fire_sword","duration":25}` | sequence: run_command → damage | `{"type":"durability","amount":20,"target":"self"}` | 8 / `holder` | не задано |
| [`effect:ghost_sword`](items-2.8.14.md#effectghost_sword) | `{"category":"ghost_sword","duration":2}` | один объект: shoot + damage | `{"type":"durability","amount":6,"target":"self"}` | не задано | `{"projectile":"entity:ghost_projectile","launch_power":1}` |
| [`effect:ice_sword`](items-2.8.14.md#effectice_sword) | `{"category":"ice_sword","duration":5}` | sequence: run_command → damage | `{"type":"durability","amount":6,"target":"self"}` | 43 / `holder` | не задано |
| [`effect:lightning_sword`](items-2.8.14.md#effectlightning_sword) | `{"category":"lightning_sword","duration":12}` | один объект: run_command + damage | `{"type":"durability","amount":9,"target":"self"}` | 41 / не задан | не задано |
| [`effect:shulker_sword`](items-2.8.14.md#effectshulker_sword) | `{"category":"shulker_sword","duration":8}` | один объект: run_command + damage | `{"type":"durability","amount":8,"target":"self"}` | 9 / не задан | не задано |
| [`effect:spectral_sword`](items-2.8.14.md#effectspectral_sword) | `{"category":"spectral_sword","duration":18}` | один объект: damage + shoot + run_command | `{"type":"durability","amount":15,"target":"self"}` | 2 / не задан | `{"projectile":"entity:ender_crystal_projectile","launch_power":1}` |
| [`effect:spider_sword`](items-2.8.14.md#effectspider_sword) | `{"category":"spider_sword","duration":28}` | один объект: run_command + damage | `{"type":"durability","amount":8,"target":"self"}` | 1 / `holder` | не задано |
| [`effect:tnt_sword`](items-2.8.14.md#effecttnt_sword) | `{"category":"tnt_sword","duration":10}` | один объект: run_command + damage | `{"type":"durability","amount":18,"target":"self"}` | 3 / не задан | не задано |
| [`effect:ultra_instinct_sword`](items-2.8.14.md#effectultra_instinct_sword) | `{"category":"ultra_instinct_sword","duration":61}` | один объект: shoot + damage + run_command | `{"type":"durability","amount":48,"target":"self"}` | 1 / не задан | `{"projectile":"entity:ultra_instinct_projectile","launch_power":1}` |
| [`effect:wither_sword`](items-2.8.14.md#effectwither_sword) | `{"category":"wither_sword","duration":3}` | один объект: shoot + run_command + damage | `{"type":"durability","amount":3,"target":"self"}` | 1 / не задан | `{"projectile":"minecraft:wither_skull_dangerous","launch_power":1}` |

## Без item-компонента `minecraft:on_use` в обоих архивах 2.x

`effect:bedrock_stick`, `effect:bedrock_sword`, `effect:bee_sword`, `effect:bone_sword`, `effect:cactus_sword`, `effect:coal_sword`, `effect:cursed_pumpkin_sword`, `effect:emerald_sword`, `effect:glass_sword`, `effect:glowstone_sword`, `effect:grass_sword`, `effect:jungle_sword`, `effect:lapis_sword`, `effect:magma_sword`, `effect:nether_star_sword`, `effect:obsidian_sword`, `effect:quartz_diamond`, `effect:quartz_diamond_stick`, `effect:quartz_sword`, `effect:sea_sword`, `effect:silver_ingot`, `effect:silver_sword`, `effect:slime_sword`, `effect:sponge_sword`, `effect:time_sword`, `effect:wet_sponge_sword`, `effect:wither_skeleton_sword`, `effect:wolf_sword`.

Это отсутствие именно item hook; у предметов могут быть weapon/digger/block-placer и player/entity/animation-события. Полные команды и источники по ссылкам на карточки предметов; отдельно [геометрия Ice](ice-geometry-index.md) и [рисунок Lightning](lightning-patterns.md).
