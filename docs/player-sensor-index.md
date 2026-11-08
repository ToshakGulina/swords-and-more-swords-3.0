# Базовые environment-сенсоры player: 1.6 и 2.x

Полные элементы **базового** `minecraft:environment_sensor` в `entities/player.json`, в исходном порядке массива. Значения и фильтры приведены буквально, без интерпретации дефолтов движка. Сенсоры внутри component groups, другие компоненты, команды, анимации и внешние пакеты сюда не включены. Порядок строк массива не доказывает последовательности или частоты вызовов.

Списки и сопоставления item-фильтров 2.8.8 и 2.8.14 структурно совпадают; сами тела вызываемых событий и другие поля `player.json` могут отличаться. [Группы player 1.6](player-groups-1.6.md) · [группы player 2.8.14](player-groups-2.8.14.md) · [все event-поля сущностей](entity-event-fields-2.x.md).

## 1.6: sensor по исходному порядку

Найдено **28** элементов базового списка, из них по ограниченному шаблону ниже сопоставлено item ID: **26** из 26. Путь каждого элемента — `$.minecraft:entity.components.minecraft:environment_sensor[index]`.

| index | Полный элемент sensor | Имя события в events player |
|---:|---|---|
| 0 | `{"on_environment":{"filters":{"all_of":[{"test":"has_mob_effect","subject":"self","value":"bad_omen"},{"test":"is_in_village","subject":"self","value":true}]},"event":"minecraft:trigger_raid"}}` | да |
| 1 | `{"on_environment":{"filters":{"all_of":[{"test":"is_family","subject":"self","value":"player"}]},"event":"minecraft:event_normal_player"}}` | да |
| 2 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:spectral_sword"}]},"event":"minecraft:spectral_sword"}}` | да |
| 3 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:blaze_sword"}]},"event":"minecraft:blaze_sword"}}` | да |
| 4 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:cactus_sword"}]},"event":"minecraft:cactus_sword"}}` | да |
| 5 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:coal_sword"}]},"event":"minecraft:coal_sword"}}` | да |
| 6 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:creeper_sword"}]},"event":"minecraft:creeper_sword"}}` | да |
| 7 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:emerald_sword"}]},"event":"minecraft:emerald_sword"}}` | да |
| 8 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:ender_sword"}]},"event":"minecraft:ender_sword"}}` | да |
| 9 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:fire_sword"}]},"event":"minecraft:fire_sword"}}` | да |
| 10 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:glowstone_sword"}]},"event":"minecraft:glowstone_sword"}}` | да |
| 11 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:grass_sword"}]},"event":"minecraft:grass_sword"}}` | да |
| 12 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:ice_sword"}]},"event":"minecraft:ice_sword"}}` | да |
| 13 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:jungle_sword"}]},"event":"minecraft:jungle_sword"}}` | да |
| 14 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:lapis_sword"}]},"event":"minecraft:lapis_sword"}}` | да |
| 15 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:lightning_sword"}]},"event":"minecraft:lightning_sword"}}` | да |
| 16 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:magma_sword"}]},"event":"minecraft:magma_sword"}}` | да |
| 17 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:obsidian_sword"}]},"event":"minecraft:obsidian_sword"}}` | да |
| 18 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:sea_sword"}]},"event":"minecraft:sea_sword"}}` | да |
| 19 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:shulker_sword"}]},"event":"minecraft:shulker_sword"}}` | да |
| 20 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:slime_sword"}]},"event":"minecraft:slime_sword"}}` | да |
| 21 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:spider_sword"}]},"event":"minecraft:spider_sword"}}` | да |
| 22 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:sponge_sword"}]},"event":"minecraft:sponge_sword"}}` | да |
| 23 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:sword_of_time"}]},"event":"minecraft:sword_of_time"}}` | да |
| 24 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:tnt_sword"}]},"event":"minecraft:tnt_sword"}}` | да |
| 25 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:wither_sword"}]},"event":"minecraft:wither_sword"}}` | да |
| 26 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:bone_sword"}]},"event":"minecraft:bone_sword"}}` | да |
| 27 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:quartz_sword"}]},"event":"minecraft:quartz_sword"}}` | да |

### 1.6: буквальный hand-фильтр по item ID

Сопоставляются только фильтры строго вида `all_of` с одним `has_equipment`, subject `self`, domain `hand`, value равным точному ID и без других полей кроме необязательного operator. Ниже отдельно показаны **отсутствующий operator** и буквально `!=`; это не автоматическое утверждение об их семантической взаимной исключительности, отдельных слотах или времени срабатывания.

| Точный item ID | operator отсутствует: index → event | operator `!=`: index → event |
|---|---|---|
| `effect:blaze_sword` | `3` → `minecraft:blaze_sword` | — |
| `effect:bone_sword` | `26` → `minecraft:bone_sword` | — |
| `effect:cactus_sword` | `4` → `minecraft:cactus_sword` | — |
| `effect:coal_sword` | `5` → `minecraft:coal_sword` | — |
| `effect:creeper_sword` | `6` → `minecraft:creeper_sword` | — |
| `effect:emerald_sword` | `7` → `minecraft:emerald_sword` | — |
| `effect:ender_sword` | `8` → `minecraft:ender_sword` | — |
| `effect:fire_sword` | `9` → `minecraft:fire_sword` | — |
| `effect:glowstone_sword` | `10` → `minecraft:glowstone_sword` | — |
| `effect:grass_sword` | `11` → `minecraft:grass_sword` | — |
| `effect:ice_sword` | `12` → `minecraft:ice_sword` | — |
| `effect:jungle_sword` | `13` → `minecraft:jungle_sword` | — |
| `effect:lapis_sword` | `14` → `minecraft:lapis_sword` | — |
| `effect:lightning_sword` | `15` → `minecraft:lightning_sword` | — |
| `effect:magma_sword` | `16` → `minecraft:magma_sword` | — |
| `effect:obsidian_sword` | `17` → `minecraft:obsidian_sword` | — |
| `effect:quartz_sword` | `27` → `minecraft:quartz_sword` | — |
| `effect:sea_sword` | `18` → `minecraft:sea_sword` | — |
| `effect:shulker_sword` | `19` → `minecraft:shulker_sword` | — |
| `effect:slime_sword` | `20` → `minecraft:slime_sword` | — |
| `effect:spectral_sword` | `2` → `minecraft:spectral_sword` | — |
| `effect:spider_sword` | `21` → `minecraft:spider_sword` | — |
| `effect:sponge_sword` | `22` → `minecraft:sponge_sword` | — |
| `effect:sword_of_time` | `23` → `minecraft:sword_of_time` | — |
| `effect:tnt_sword` | `24` → `minecraft:tnt_sword` | — |
| `effect:wither_sword` | `25` → `minecraft:wither_sword` | — |

Прочерк здесь означает только отсутствие соответствующего *простого* фильтра в этом списке. Предмет может действовать через более сложный фильтр, item hook, другие компоненты/файлы или команды; совпадение события по имени также не устанавливает его выполнение.

## 2.8.8 и 2.8.14: sensor по исходному порядку

Найдено **62** элементов базового списка, из них по ограниченному шаблону ниже сопоставлено item ID: **29** из 42. Путь каждого элемента — `$.minecraft:entity.components.minecraft:environment_sensor[index]`.

| index | Полный элемент sensor | Имя события в events player |
|---:|---|---|
| 0 | `{"on_environment":{"filters":{"all_of":[{"test":"has_mob_effect","subject":"self","value":"bad_omen"},{"test":"is_in_village","subject":"self","value":true}]},"event":"minecraft:trigger_raid"}}` | да |
| 1 | `{"on_environment":{"filters":{"test":"is_family","operator":"!=","value":"null"},"event":"minecraft:constant_events"}}` | да |
| 2 | `{"on_environment":{"filters":{"any_of":[{"test":"is_family","subject":"self","value":"default_player"},{"test":"is_family","subject":"self","operator":"!=","value":"spectral_sword"}]},"event":"minecraft:stop_sword_events"}}` | да |
| 3 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:blaze_sword"}]},"event":"minecraft:blaze_sword"}}` | да |
| 4 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:blaze_sword"}]},"event":"stop_blaze_sword_event"}}` | да |
| 5 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:bone_sword"}]},"event":"minecraft:bone_sword"}}` | да |
| 6 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:bone_sword"}]},"event":"stop_bone_sword_event"}}` | да |
| 7 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:cactus_sword"}]},"event":"minecraft:cactus_sword"}}` | да |
| 8 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:cactus_sword"}]},"event":"stop_cactus_sword_event"}}` | да |
| 9 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:emerald_sword"}]},"event":"minecraft:emerald_sword"}}` | да |
| 10 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:emerald_sword"}]},"event":"stop_emerald_sword_event"}}` | да |
| 11 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:fire_sword"}]},"event":"minecraft:fire_sword"}}` | да |
| 12 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:fire_sword"}]},"event":"stop_fire_sword_event"}}` | да |
| 13 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:grass_sword"}]},"event":"minecraft:grass_sword"}}` | да |
| 14 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:grass_sword"}]},"event":"stop_grass_sword_event"}}` | да |
| 15 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:jungle_sword"}]},"event":"minecraft:jungle_sword"}}` | да |
| 16 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:jungle_sword"}]},"event":"stop_jungle_sword_event"}}` | да |
| 17 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:magma_sword"}]},"event":"minecraft:magma_sword"}}` | да |
| 18 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:magma_sword"}]},"event":"stop_magma_sword_event"}}` | да |
| 19 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:ice_sword"}]},"event":"minecraft:ice_sword"}}` | да |
| 20 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:ice_sword"}]},"event":"stop_ice_sword_event"}}` | да |
| 21 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:lapis_sword"}]},"event":"minecraft:lapis_sword"}}` | да |
| 22 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:lapis_sword"}]},"event":"stop_lapis_sword_event"}}` | да |
| 23 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:obsidian_sword"}]},"event":"minecraft:obsidian_sword"}}` | да |
| 24 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:obsidian_sword"}]},"event":"stop_obsidian_sword_event"}}` | да |
| 25 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:quartz_sword"}]},"event":"minecraft:quartz_sword"}}` | да |
| 26 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:quartz_sword"}]},"event":"stop_quartz_sword_event"}}` | да |
| 27 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:sea_sword"}]},"event":"minecraft:sea_sword"}}` | да |
| 28 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:sea_sword"}]},"event":"stop_sea_sword_event"}}` | да |
| 29 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:spectral_sword"}]},"event":"minecraft:spectral_sword"}}` | да |
| 30 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:spectral_sword"}]},"event":"stop_spectral_sword_event"}}` | да |
| 31 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:slime_sword"}]},"event":"minecraft:slime_sword"}}` | да |
| 32 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:slime_sword"}]},"event":"stop_slime_sword_event"}}` | да |
| 33 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:shulker_sword"}]},"event":"minecraft:shulker_sword"}}` | да |
| 34 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:shulker_sword"}]},"event":"stop_shulker_sword_event"}}` | да |
| 35 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:spider_sword"}]},"event":"minecraft:spider_sword"}}` | да |
| 36 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:spider_sword"}]},"event":"stop_spider_sword_event"}}` | да |
| 37 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:sponge_sword"}]},"event":"minecraft:sponge_sword"}}` | да |
| 38 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:sponge_sword"}]},"event":"stop_sponge_sword_event"}}` | да |
| 39 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:time_sword"}]},"event":"minecraft:time_sword"}}` | да |
| 40 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:time_sword"}]},"event":"stop_time_sword_event"}}` | да |
| 41 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:wither_sword"}]},"event":"minecraft:wither_sword"}}` | да |
| 42 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:wither_sword"}]},"event":"stop_wither_sword_event"}}` | да |
| 43 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:glowstone_sword"}]},"event":"minecraft:glowstone_sword"}}` | да |
| 44 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:lightning_sword"}]},"event":"minecraft:lightning_sword"}}` | да |
| 45 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:lightning_sword"}]},"event":"stop_lightning_sword_event"}}` | да |
| 46 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:ender_sword"}]},"event":"minecraft:ender_sword"}}` | да |
| 47 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:ender_sword"}]},"event":"stop_ender_sword_event"}}` | да |
| 48 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:ultra_instinct_sword"}]},"event":"minecraft:ultra_instinct_sword"}}` | да |
| 49 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:ultra_instinct_sword"}]},"event":"stop_ultra_instinct_sword_event"}}` | да |
| 50 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:wolf_sword"}]},"event":"minecraft:wolf_sword"}}` | да |
| 51 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:wolf_sword"}]},"event":"stop_wolf_sword_event"}}` | да |
| 52 | `{"on_environment":{"filters":{"all_of":[{"test":"is_family","value":"wolf_transformation"}]},"event":"starting_wolf_transformation"}}` | да |
| 53 | `{"on_environment":{"filters":{"all_of":[{"test":"is_family","value":"complete_wolf_transformation"}]},"event":"wolf_movement"}}` | да |
| 54 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:ghost_sword"}]},"event":"minecraft:ghost_sword"}}` | да |
| 55 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:ghost_sword"}]},"event":"stop_ghost_sword_event"}}` | да |
| 56 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:clock_sword"}]},"event":"minecraft:clock_sword"}}` | да |
| 57 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:clock_sword"}]},"event":"stop_clock_sword_event"}}` | да |
| 58 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:nether_star_sword"}]},"event":"minecraft:nether_star_sword"}}` | да |
| 59 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:nether_star_sword"}]},"event":"stop_nether_star_sword_event"}}` | да |
| 60 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:bee_sword"}]},"event":"minecraft:bee_sword"}}` | да |
| 61 | `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:bee_sword"}]},"event":"stop_bee_sword_event"}}` | да |

### 2.8.8 и 2.8.14: буквальный hand-фильтр по item ID

Сопоставляются только фильтры строго вида `all_of` с одним `has_equipment`, subject `self`, domain `hand`, value равным точному ID и без других полей кроме необязательного operator. Ниже отдельно показаны **отсутствующий operator** и буквально `!=`; это не автоматическое утверждение об их семантической взаимной исключительности, отдельных слотах или времени срабатывания.

| Точный item ID | operator отсутствует: index → event | operator `!=`: index → event |
|---|---|---|
| `effect:bedrock_stick` | — | — |
| `effect:bedrock_sword` | — | — |
| `effect:bee_sword` | `60` → `minecraft:bee_sword` | `61` → `stop_bee_sword_event` |
| `effect:blaze_sword` | `3` → `minecraft:blaze_sword` | `4` → `stop_blaze_sword_event` |
| `effect:bone_sword` | `5` → `minecraft:bone_sword` | `6` → `stop_bone_sword_event` |
| `effect:cactus_sword` | `7` → `minecraft:cactus_sword` | `8` → `stop_cactus_sword_event` |
| `effect:clock_sword` | `56` → `minecraft:clock_sword` | `57` → `stop_clock_sword_event` |
| `effect:coal_sword` | — | — |
| `effect:creeper_sword` | — | — |
| `effect:cursed_pumpkin_sword` | — | — |
| `effect:emerald_sword` | `9` → `minecraft:emerald_sword` | `10` → `stop_emerald_sword_event` |
| `effect:ender_sword` | `46` → `minecraft:ender_sword` | `47` → `stop_ender_sword_event` |
| `effect:fire_sword` | `11` → `minecraft:fire_sword` | `12` → `stop_fire_sword_event` |
| `effect:ghost_sword` | `54` → `minecraft:ghost_sword` | `55` → `stop_ghost_sword_event` |
| `effect:glass_sword` | — | — |
| `effect:glowstone_sword` | `43` → `minecraft:glowstone_sword` | — |
| `effect:grass_sword` | `13` → `minecraft:grass_sword` | `14` → `stop_grass_sword_event` |
| `effect:ice_sword` | `19` → `minecraft:ice_sword` | `20` → `stop_ice_sword_event` |
| `effect:jungle_sword` | `15` → `minecraft:jungle_sword` | `16` → `stop_jungle_sword_event` |
| `effect:lapis_sword` | `21` → `minecraft:lapis_sword` | `22` → `stop_lapis_sword_event` |
| `effect:lightning_sword` | `44` → `minecraft:lightning_sword` | `45` → `stop_lightning_sword_event` |
| `effect:magma_sword` | `17` → `minecraft:magma_sword` | `18` → `stop_magma_sword_event` |
| `effect:nether_star_sword` | `58` → `minecraft:nether_star_sword` | `59` → `stop_nether_star_sword_event` |
| `effect:obsidian_sword` | `23` → `minecraft:obsidian_sword` | `24` → `stop_obsidian_sword_event` |
| `effect:quartz_diamond` | — | — |
| `effect:quartz_diamond_stick` | — | — |
| `effect:quartz_sword` | `25` → `minecraft:quartz_sword` | `26` → `stop_quartz_sword_event` |
| `effect:sea_sword` | `27` → `minecraft:sea_sword` | `28` → `stop_sea_sword_event` |
| `effect:shulker_sword` | `33` → `minecraft:shulker_sword` | `34` → `stop_shulker_sword_event` |
| `effect:silver_ingot` | — | — |
| `effect:silver_sword` | — | — |
| `effect:slime_sword` | `31` → `minecraft:slime_sword` | `32` → `stop_slime_sword_event` |
| `effect:spectral_sword` | `29` → `minecraft:spectral_sword` | `30` → `stop_spectral_sword_event` |
| `effect:spider_sword` | `35` → `minecraft:spider_sword` | `36` → `stop_spider_sword_event` |
| `effect:sponge_sword` | `37` → `minecraft:sponge_sword` | `38` → `stop_sponge_sword_event` |
| `effect:time_sword` | `39` → `minecraft:time_sword` | `40` → `stop_time_sword_event` |
| `effect:tnt_sword` | — | — |
| `effect:ultra_instinct_sword` | `48` → `minecraft:ultra_instinct_sword` | `49` → `stop_ultra_instinct_sword_event` |
| `effect:wet_sponge_sword` | — | — |
| `effect:wither_skeleton_sword` | — | — |
| `effect:wither_sword` | `41` → `minecraft:wither_sword` | `42` → `stop_wither_sword_event` |
| `effect:wolf_sword` | `50` → `minecraft:wolf_sword` | `51` → `stop_wolf_sword_event` |

Прочерк здесь означает только отсутствие соответствующего *простого* фильтра в этом списке. Предмет может действовать через более сложный фильтр, item hook, другие компоненты/файлы или команды; совпадение события по имени также не устанавливает его выполнение.

