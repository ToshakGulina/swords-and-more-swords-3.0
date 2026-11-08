# Буквальные поля event в behavior-сущностях — 1.6

Поиск значений свойства `event`, являющихся строкой, во всём объекте `minecraft:entity`: разобранных файлов 28, вхождений 30. Это **не полный граф вызовов**: `spawn_event`, строковые команды `event entity`, анимационные контроллеры, внешние вызовы, ванильные правила и динамическое разрешение не входят в этот поиск.

Колонка локального объявления только проверяет наличие имени среди `events` **того же файла**, независимо от `target`. Она не определяет объект-адресат, фактическое исполнение или отсутствие события в игре: в частности, target `block` и `baby` не следует автоматически проверять как self. Если target не задан, его дефолт здесь не предположен. Само имя `self` не гарантирует, какой объект движок выберет в каждом контексте. Повторные ключи JSON5 сводит к последнему значению; неразобранные файлы исключены.

Вхождения по буквально записанному target: не указан — 28, `self` — 2.
Из них вхождений с именем, отсутствующим в локальном `events`: нет. Эти числа не являются количеством ошибок.

- Неразобранные файлы: `Sword_B/entities/blaze2.json` (<string>:78 Unexpected "}" at column 1); `Sword_B/entities/bone2.json` (<string>:75 Unexpected "}" at column 1); `Sword_B/entities/shulker2.json` (<string>:75 Unexpected "}" at column 1).
- Повторные ключи: нет.

| Файл / ID | Значение event | target | Локально объявлено имя | Буквальные пути |
|---|---|---|---|---|
| `Sword_B/entities/player.json`<br>`minecraft:player` | `minecraft:blaze_sword` | не указан | да | `$.components.minecraft:environment_sensor[3].on_environment.event` |
| `Sword_B/entities/player.json`<br>`minecraft:player` | `minecraft:bone_sword` | не указан | да | `$.components.minecraft:environment_sensor[26].on_environment.event` |
| `Sword_B/entities/player.json`<br>`minecraft:player` | `minecraft:cactus_sword` | не указан | да | `$.components.minecraft:environment_sensor[4].on_environment.event` |
| `Sword_B/entities/player.json`<br>`minecraft:player` | `minecraft:clear_add_bad_omen` | `self` | да | `$.component_groups.minecraft:add_bad_omen.minecraft:timer.time_down_event.event` |
| `Sword_B/entities/player.json`<br>`minecraft:player` | `minecraft:coal_sword` | не указан | да | `$.components.minecraft:environment_sensor[5].on_environment.event` |
| `Sword_B/entities/player.json`<br>`minecraft:player` | `minecraft:creeper_sword` | не указан | да | `$.components.minecraft:environment_sensor[6].on_environment.event` |
| `Sword_B/entities/player.json`<br>`minecraft:player` | `minecraft:emerald_sword` | не указан | да | `$.components.minecraft:environment_sensor[7].on_environment.event` |
| `Sword_B/entities/player.json`<br>`minecraft:player` | `minecraft:ender_sword` | не указан | да | `$.components.minecraft:environment_sensor[8].on_environment.event` |
| `Sword_B/entities/player.json`<br>`minecraft:player` | `minecraft:event_normal_player` | не указан | да | `$.components.minecraft:environment_sensor[1].on_environment.event` |
| `Sword_B/entities/player.json`<br>`minecraft:player` | `minecraft:fire_sword` | не указан | да | `$.components.minecraft:environment_sensor[9].on_environment.event` |
| `Sword_B/entities/player.json`<br>`minecraft:player` | `minecraft:glowstone_sword` | не указан | да | `$.components.minecraft:environment_sensor[10].on_environment.event` |
| `Sword_B/entities/player.json`<br>`minecraft:player` | `minecraft:grass_sword` | не указан | да | `$.components.minecraft:environment_sensor[11].on_environment.event` |
| `Sword_B/entities/player.json`<br>`minecraft:player` | `minecraft:ice_sword` | не указан | да | `$.components.minecraft:environment_sensor[12].on_environment.event` |
| `Sword_B/entities/player.json`<br>`minecraft:player` | `minecraft:jungle_sword` | не указан | да | `$.components.minecraft:environment_sensor[13].on_environment.event` |
| `Sword_B/entities/player.json`<br>`minecraft:player` | `minecraft:lapis_sword` | не указан | да | `$.components.minecraft:environment_sensor[14].on_environment.event` |
| `Sword_B/entities/player.json`<br>`minecraft:player` | `minecraft:lightning_sword` | не указан | да | `$.components.minecraft:environment_sensor[15].on_environment.event` |
| `Sword_B/entities/player.json`<br>`minecraft:player` | `minecraft:magma_sword` | не указан | да | `$.components.minecraft:environment_sensor[16].on_environment.event` |
| `Sword_B/entities/player.json`<br>`minecraft:player` | `minecraft:obsidian_sword` | не указан | да | `$.components.minecraft:environment_sensor[17].on_environment.event` |
| `Sword_B/entities/player.json`<br>`minecraft:player` | `minecraft:quartz_sword` | не указан | да | `$.components.minecraft:environment_sensor[27].on_environment.event` |
| `Sword_B/entities/player.json`<br>`minecraft:player` | `minecraft:remove_raid_trigger` | `self` | да | `$.component_groups.minecraft:raid_trigger.minecraft:raid_trigger.triggered_event.event` |
| `Sword_B/entities/player.json`<br>`minecraft:player` | `minecraft:sea_sword` | не указан | да | `$.components.minecraft:environment_sensor[18].on_environment.event` |
| `Sword_B/entities/player.json`<br>`minecraft:player` | `minecraft:shulker_sword` | не указан | да | `$.components.minecraft:environment_sensor[19].on_environment.event` |
| `Sword_B/entities/player.json`<br>`minecraft:player` | `minecraft:slime_sword` | не указан | да | `$.components.minecraft:environment_sensor[20].on_environment.event` |
| `Sword_B/entities/player.json`<br>`minecraft:player` | `minecraft:spectral_sword` | не указан | да | `$.components.minecraft:environment_sensor[2].on_environment.event` |
| `Sword_B/entities/player.json`<br>`minecraft:player` | `minecraft:spider_sword` | не указан | да | `$.components.minecraft:environment_sensor[21].on_environment.event` |
| `Sword_B/entities/player.json`<br>`minecraft:player` | `minecraft:sponge_sword` | не указан | да | `$.components.minecraft:environment_sensor[22].on_environment.event` |
| `Sword_B/entities/player.json`<br>`minecraft:player` | `minecraft:sword_of_time` | не указан | да | `$.components.minecraft:environment_sensor[23].on_environment.event` |
| `Sword_B/entities/player.json`<br>`minecraft:player` | `minecraft:tnt_sword` | не указан | да | `$.components.minecraft:environment_sensor[24].on_environment.event` |
| `Sword_B/entities/player.json`<br>`minecraft:player` | `minecraft:trigger_raid` | не указан | да | `$.components.minecraft:environment_sensor[0].on_environment.event` |
| `Sword_B/entities/player.json`<br>`minecraft:player` | `minecraft:wither_sword` | не указан | да | `$.components.minecraft:environment_sensor[25].on_environment.event` |

Полные объявления и условия: [реестр сущностей 1.6](entity-ledger-1.6.md); отдельный [индекс групп](entity-groups-1.6.md).
