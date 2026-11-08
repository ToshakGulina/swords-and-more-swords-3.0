# Компоненты боя и уязвимости сущностей — 1.6

Из **28** разобранных behavior entity файлов выбраны все значения 11 точных ключей только в базовом `components` и объявленных `component_groups`: **57 объектов/значений**, файлов с выбранным ключом — 28. Сохранены целые объекты, вложенные triggers и filters, списки и порядок. Близко называющиеся события `minecraft:explode` не принимаются за одноимённый компонент.

Это индекс **деклараций**, не итоговые характеристики: группа может быть неактивна, несколько групп могут задавать конфликтующие компоненты, события могут не вызываться, target и контекст определяются отдельно. `damage_sensor`, `hurt_on_condition` и `on_death` не дают полного графа последствий. Значения health относятся к сущностям, а не к прочности предмета. Отсутствующее поле не означает false, ноль, иммунитет либо непробиваемость. Источники ошибок/повторов ниже; поведение движка, vanilla/runtime и внешние пакеты не устанавливаются.

Число вхождений выбранных ключей: `minecraft:damage_sensor` — 0, `minecraft:health` — 26, `minecraft:attack` — 1, `minecraft:attack_damage` — 0, `minecraft:explode` — 2, `minecraft:fire_immune` — 26, `minecraft:breathable` — 1, `minecraft:knockback_resistance` — 0, `minecraft:hurt_on_condition` — 1, `minecraft:on_death` — 0, `minecraft:on_hurt` — 0.

- Исключены неразобранные файлы: `Sword_B/entities/blaze2.json` (<string>:78 Unexpected "}" at column 1); `Sword_B/entities/bone2.json` (<string>:75 Unexpected "}" at column 1); `Sword_B/entities/shulker2.json` (<string>:75 Unexpected "}" at column 1). Для трёх helper-файлов есть [отдельная диагностика](manual-traces-1.6.md#что-написано-в-повреждённых-helper-файлах).
- Дублирующиеся ключи: нет. JSON5 сохраняет последнее значение, поэтому оригинал обязателен для спорных мест.

| Файл / ID | Область и ключ | Полное разобранное значение |
|---|---|---|
| `Sword_B/entities/blaze.json`<br>`entity:blaze` | `$.minecraft:entity.components.minecraft:health` | `{"value":1}` |
| `Sword_B/entities/blaze.json`<br>`entity:blaze` | `$.minecraft:entity.components.minecraft:fire_immune` | `true` |
| `Sword_B/entities/bone.json`<br>`entity:bone` | `$.minecraft:entity.components.minecraft:health` | `{"value":1}` |
| `Sword_B/entities/bone.json`<br>`entity:bone` | `$.minecraft:entity.components.minecraft:fire_immune` | `true` |
| `Sword_B/entities/cactus.json`<br>`entity:cactus` | `$.minecraft:entity.components.minecraft:health` | `{"value":1}` |
| `Sword_B/entities/cactus.json`<br>`entity:cactus` | `$.minecraft:entity.components.minecraft:fire_immune` | `true` |
| `Sword_B/entities/coal.json`<br>`entity:coal` | `$.minecraft:entity.components.minecraft:health` | `{"value":1}` |
| `Sword_B/entities/coal.json`<br>`entity:coal` | `$.minecraft:entity.components.minecraft:fire_immune` | `true` |
| `Sword_B/entities/creeper.json`<br>`entity:creeper` | `$.minecraft:entity.components.minecraft:health` | `{"value":1}` |
| `Sword_B/entities/creeper.json`<br>`entity:creeper` | `$.minecraft:entity.components.minecraft:fire_immune` | `true` |
| `Sword_B/entities/emerald.json`<br>`entity:emerald` | `$.minecraft:entity.components.minecraft:health` | `{"value":1}` |
| `Sword_B/entities/emerald.json`<br>`entity:emerald` | `$.minecraft:entity.components.minecraft:fire_immune` | `true` |
| `Sword_B/entities/ender.json`<br>`entity:ender` | `$.minecraft:entity.components.minecraft:health` | `{"value":1}` |
| `Sword_B/entities/ender.json`<br>`entity:ender` | `$.minecraft:entity.components.minecraft:fire_immune` | `true` |
| `Sword_B/entities/explode.json`<br>`entity:explode` | `$.minecraft:entity.components.minecraft:explode` | `{"fuseLength":0,"fuseLit":true,"power":4,"causesFire":false,"destroy_affected_by_griefing":true}` |
| `Sword_B/entities/explode.json`<br>`entity:explode` | `$.minecraft:entity.component_groups.from_explosion.minecraft:explode` | `{"fuseLength":{"range_min":0,"range_max":0},"fuseLit":true,"power":4,"causesFire":false,"destroy_affected_by_griefing":true}` |
| `Sword_B/entities/fire.json`<br>`entity:fire` | `$.minecraft:entity.components.minecraft:health` | `{"value":1}` |
| `Sword_B/entities/fire.json`<br>`entity:fire` | `$.minecraft:entity.components.minecraft:fire_immune` | `true` |
| `Sword_B/entities/glowstone_sword.json`<br>`entity:glow` | `$.minecraft:entity.components.minecraft:health` | `{"value":1}` |
| `Sword_B/entities/glowstone_sword.json`<br>`entity:glow` | `$.minecraft:entity.components.minecraft:fire_immune` | `true` |
| `Sword_B/entities/grass.json`<br>`entity:grass` | `$.minecraft:entity.components.minecraft:health` | `{"value":1}` |
| `Sword_B/entities/grass.json`<br>`entity:grass` | `$.minecraft:entity.components.minecraft:fire_immune` | `true` |
| `Sword_B/entities/ice.json`<br>`entity:ice` | `$.minecraft:entity.components.minecraft:health` | `{"value":1}` |
| `Sword_B/entities/ice.json`<br>`entity:ice` | `$.minecraft:entity.components.minecraft:fire_immune` | `true` |
| `Sword_B/entities/jungle.json`<br>`entity:jungle` | `$.minecraft:entity.components.minecraft:health` | `{"value":1}` |
| `Sword_B/entities/jungle.json`<br>`entity:jungle` | `$.minecraft:entity.components.minecraft:fire_immune` | `true` |
| `Sword_B/entities/lapis.json`<br>`entity:lapis` | `$.minecraft:entity.components.minecraft:health` | `{"value":1}` |
| `Sword_B/entities/lapis.json`<br>`entity:lapis` | `$.minecraft:entity.components.minecraft:fire_immune` | `true` |
| `Sword_B/entities/lightning.json`<br>`entity:lightning` | `$.minecraft:entity.components.minecraft:health` | `{"value":1}` |
| `Sword_B/entities/lightning.json`<br>`entity:lightning` | `$.minecraft:entity.components.minecraft:fire_immune` | `true` |
| `Sword_B/entities/magma.json`<br>`entity:magma` | `$.minecraft:entity.components.minecraft:health` | `{"value":1}` |
| `Sword_B/entities/magma.json`<br>`entity:magma` | `$.minecraft:entity.components.minecraft:fire_immune` | `true` |
| `Sword_B/entities/normal.json`<br>`entity:normal` | `$.minecraft:entity.components.minecraft:health` | `{"value":1}` |
| `Sword_B/entities/normal.json`<br>`entity:normal` | `$.minecraft:entity.components.minecraft:fire_immune` | `true` |
| `Sword_B/entities/obsidian.json`<br>`entity:obsidian` | `$.minecraft:entity.components.minecraft:health` | `{"value":1}` |
| `Sword_B/entities/obsidian.json`<br>`entity:obsidian` | `$.minecraft:entity.components.minecraft:fire_immune` | `true` |
| `Sword_B/entities/player.json`<br>`minecraft:player` | `$.minecraft:entity.components.minecraft:breathable` | `{"totalSupply":15,"suffocateTime":-1,"inhaleTime":3.75,"generatesBubbles":false}` |
| `Sword_B/entities/player.json`<br>`minecraft:player` | `$.minecraft:entity.component_groups.minecraft:normal_player.minecraft:attack` | `{"damage":1}` |
| `Sword_B/entities/player.json`<br>`minecraft:player` | `$.minecraft:entity.component_groups.minecraft:ender_sword.minecraft:hurt_on_condition` | `{"damage_conditions":[{"filters":{"test":"in_water_or_rain","operator":"==","value":true},"cause":"drowning","damage_per_tick":1}]}` |
| `Sword_B/entities/sea.json`<br>`entity:sea` | `$.minecraft:entity.components.minecraft:health` | `{"value":1}` |
| `Sword_B/entities/sea.json`<br>`entity:sea` | `$.minecraft:entity.components.minecraft:fire_immune` | `true` |
| `Sword_B/entities/shulker.json`<br>`entity:shulker` | `$.minecraft:entity.components.minecraft:health` | `{"value":1}` |
| `Sword_B/entities/shulker.json`<br>`entity:shulker` | `$.minecraft:entity.components.minecraft:fire_immune` | `true` |
| `Sword_B/entities/slime.json`<br>`entity:slime` | `$.minecraft:entity.components.minecraft:health` | `{"value":1}` |
| `Sword_B/entities/slime.json`<br>`entity:slime` | `$.minecraft:entity.components.minecraft:fire_immune` | `true` |
| `Sword_B/entities/spectral.json`<br>`entity:spectral` | `$.minecraft:entity.components.minecraft:health` | `{"value":1}` |
| `Sword_B/entities/spectral.json`<br>`entity:spectral` | `$.minecraft:entity.components.minecraft:fire_immune` | `true` |
| `Sword_B/entities/spider.json`<br>`entity:spider` | `$.minecraft:entity.components.minecraft:health` | `{"value":1}` |
| `Sword_B/entities/spider.json`<br>`entity:spider` | `$.minecraft:entity.components.minecraft:fire_immune` | `true` |
| `Sword_B/entities/sponge.json`<br>`entity:sponge` | `$.minecraft:entity.components.minecraft:health` | `{"value":1}` |
| `Sword_B/entities/sponge.json`<br>`entity:sponge` | `$.minecraft:entity.components.minecraft:fire_immune` | `true` |
| `Sword_B/entities/time.json`<br>`entity:time` | `$.minecraft:entity.components.minecraft:health` | `{"value":1}` |
| `Sword_B/entities/time.json`<br>`entity:time` | `$.minecraft:entity.components.minecraft:fire_immune` | `true` |
| `Sword_B/entities/tnt_sword.json`<br>`entity:tnt_sword` | `$.minecraft:entity.components.minecraft:health` | `{"value":1}` |
| `Sword_B/entities/tnt_sword.json`<br>`entity:tnt_sword` | `$.minecraft:entity.components.minecraft:fire_immune` | `true` |
| `Sword_B/entities/wither_s.json`<br>`entity:wither` | `$.minecraft:entity.components.minecraft:health` | `{"value":1}` |
| `Sword_B/entities/wither_s.json`<br>`entity:wither` | `$.minecraft:entity.components.minecraft:fire_immune` | `true` |

Дополнительный контекст: [полные сущности](entity-ledger-1.6.md), [группы](entity-groups-1.6.md), [снаряды](projectile-component-index.md), [эффекты](effect-index-1.6.md), [события](entity-event-fields-1.6.md).
