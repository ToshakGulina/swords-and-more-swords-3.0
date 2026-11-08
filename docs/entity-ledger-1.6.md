# Реестр поведения сущностей — архив 1.6

Автоматический структурный разбор каждого JSON в `Sword_B/entities/`: описание, все компоненты и группы в исходных значениях, все события как деревья шагов/условных ветвей. Номера строк — все текстовые вхождения ключа; это ориентир, не точная граница блока. Набор не доказывает связи конкретного объекта с конкретным предметом и не является ручной верификацией.

Соседние поля одного объекта не упорядочены этим отчётом. Веса в randomize — только относительные доли данного выбора при всех явных неотрицательных целых весах; успех действия, фильтры, вложенные вероятности и запуск события отдельно. Для повторяющихся ключей и неразобранного JSON см. оригинал: информация JSON5-парсера может теряться.

## `entity:blaze`

- Путь `Sword_B/entities/blaze.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:blaze","is_spawnable":false,"is_summonable":true,"is_experimental":false,"scripts":{"animate":["blaze"]},"animations":{"blaze":"controller.animation.blaze"}}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 19): `{"family":["despawnear"]}`
- `minecraft:despawn` (строки 24): `{"filters":{"all_of":[{"test":"is_family","subject":"self","value":"despawnear"}]}}`
- `minecraft:health` (строки 35): `{"value":1}`
- `minecraft:collision_box` (строки 38): `{"width":0.0,"height":0.0}`
- `minecraft:fire_immune` (строки 42): `true`
- `minecraft:physics` (строки 43): `{}`

### Группы компонентов


### События

## `Sword_B/entities/blaze2.json`

**Не разобран JSON5:** `<string>:78 Unexpected "}" at column 1`. Исходник не изменять и изучать вручную.

## `entity:bone`

- Путь `Sword_B/entities/bone.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:bone","is_spawnable":false,"is_summonable":true,"is_experimental":false,"scripts":{"animate":["bone"]},"animations":{"bone":"controller.animation.bone"}}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 19): `{"family":["despawnear"]}`
- `minecraft:despawn` (строки 24): `{"filters":{"all_of":[{"test":"is_family","subject":"self","value":"despawnear"}]}}`
- `minecraft:health` (строки 35): `{"value":1}`
- `minecraft:collision_box` (строки 38): `{"width":0.0,"height":0.0}`
- `minecraft:fire_immune` (строки 42): `true`
- `minecraft:physics` (строки 43): `{}`

### Группы компонентов


### События

## `Sword_B/entities/bone2.json`

**Не разобран JSON5:** `<string>:75 Unexpected "}" at column 1`. Исходник не изменять и изучать вручную.

## `entity:cactus`

- Путь `Sword_B/entities/cactus.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:cactus","is_spawnable":false,"is_summonable":true,"is_experimental":false,"scripts":{"animate":["cactus"]},"animations":{"cactus":"controller.animation.cactus"}}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 19): `{"family":["despawnear"]}`
- `minecraft:despawn` (строки 24): `{"filters":{"all_of":[{"test":"is_family","subject":"self","value":"despawnear"}]}}`
- `minecraft:health` (строки 35): `{"value":1}`
- `minecraft:collision_box` (строки 38): `{"width":0.0,"height":0.0}`
- `minecraft:fire_immune` (строки 42): `true`
- `minecraft:physics` (строки 43): `{}`

### Группы компонентов


### События

## `entity:coal`

- Путь `Sword_B/entities/coal.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:coal","is_spawnable":false,"is_summonable":true,"is_experimental":false,"scripts":{"animate":["coal"]},"animations":{"coal":"controller.animation.coal"}}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 19): `{"family":["despawnear"]}`
- `minecraft:despawn` (строки 24): `{"filters":{"all_of":[{"test":"is_family","subject":"self","value":"despawnear"}]}}`
- `minecraft:health` (строки 35): `{"value":1}`
- `minecraft:collision_box` (строки 38): `{"width":0.0,"height":0.0}`
- `minecraft:fire_immune` (строки 42): `true`
- `minecraft:physics` (строки 43): `{}`

### Группы компонентов


### События

## `entity:creeper`

- Путь `Sword_B/entities/creeper.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:creeper","is_spawnable":false,"is_summonable":true,"is_experimental":false,"scripts":{"animate":["creeper"]},"animations":{"creeper":"controller.animation.creeper"}}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 19): `{"family":["despawnear"]}`
- `minecraft:despawn` (строки 24): `{"filters":{"all_of":[{"test":"is_family","subject":"self","value":"despawnear"}]}}`
- `minecraft:health` (строки 35): `{"value":1}`
- `minecraft:collision_box` (строки 38): `{"width":0.0,"height":0.0}`
- `minecraft:fire_immune` (строки 42): `true`
- `minecraft:physics` (строки 43): `{}`

### Группы компонентов


### События

## `entity:emerald`

- Путь `Sword_B/entities/emerald.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:emerald","is_spawnable":false,"is_summonable":true,"is_experimental":false,"scripts":{"animate":["emerald"]},"animations":{"emerald":"controller.animation.emerald"}}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 19): `{"family":["despawnear"]}`
- `minecraft:despawn` (строки 24): `{"filters":{"all_of":[{"test":"is_family","subject":"self","value":"despawnear"}]}}`
- `minecraft:health` (строки 35): `{"value":1}`
- `minecraft:collision_box` (строки 38): `{"width":0.0,"height":0.0}`
- `minecraft:fire_immune` (строки 42): `true`
- `minecraft:physics` (строки 43): `{}`

### Группы компонентов


### События

## `entity:ender`

- Путь `Sword_B/entities/ender.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:ender","is_spawnable":false,"is_summonable":true,"is_experimental":false,"scripts":{"animate":["ender"]},"animations":{"ender":"controller.animation.ender"}}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 19): `{"family":["despawnear"]}`
- `minecraft:despawn` (строки 24): `{"filters":{"all_of":[{"test":"is_family","subject":"self","value":"despawnear"}]}}`
- `minecraft:health` (строки 35): `{"value":1}`
- `minecraft:collision_box` (строки 38): `{"width":0.0,"height":0.0}`
- `minecraft:fire_immune` (строки 42): `true`
- `minecraft:physics` (строки 43): `{}`

### Группы компонентов


### События

## `entity:explode`

- Путь `Sword_B/entities/explode.json`; format_version `"1.8.0"`.
- description: `{"identifier":"entity:explode","is_spawnable":false,"is_summonable":true,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 27): `{"family":["tnt","inanimate"]}`
- `minecraft:collision_box` (строки 30): `{"width":0.98,"height":0.98}`
- `minecraft:explode` (строки 13,35): `{"fuseLength":0,"fuseLit":true,"power":4,"causesFire":false,"destroy_affected_by_griefing":true}`
- `minecraft:physics` (строки 42): `{}`

### Группы компонентов

- `from_explosion` (строки 12,47,50): `{"minecraft:explode":{"fuseLength":{"range_min":0,"range_max":0},"fuseLit":true,"power":4,"causesFire":false,"destroy_affected_by_griefing":true}}`

### События

**`from_explosion`** (строки 12,47,50):

- `$` — поля действия: `{"add":{"component_groups":["from_explosion"]}}`

## `entity:fire`

- Путь `Sword_B/entities/fire.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:fire","is_spawnable":false,"is_summonable":true,"is_experimental":false,"scripts":{"animate":["fire"]},"animations":{"fire":"controller.animation.fire"}}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 19): `{"family":["despawnear"]}`
- `minecraft:despawn` (строки 24): `{"filters":{"all_of":[{"test":"is_family","subject":"self","value":"despawnear"}]}}`
- `minecraft:health` (строки 35): `{"value":1}`
- `minecraft:collision_box` (строки 38): `{"width":0.0,"height":0.0}`
- `minecraft:fire_immune` (строки 42): `true`
- `minecraft:physics` (строки 43): `{}`

### Группы компонентов


### События

## `entity:glow`

- Путь `Sword_B/entities/glowstone_sword.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:glow","is_spawnable":false,"is_summonable":true,"is_experimental":false,"scripts":{"animate":["glow"]},"animations":{"glow":"controller.animation.glow"}}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 19): `{"family":["despawnear"]}`
- `minecraft:despawn` (строки 24): `{"filters":{"all_of":[{"test":"is_family","subject":"self","value":"despawnear"}]}}`
- `minecraft:health` (строки 35): `{"value":1}`
- `minecraft:collision_box` (строки 38): `{"width":0.0,"height":0.0}`
- `minecraft:fire_immune` (строки 42): `true`
- `minecraft:physics` (строки 43): `{}`

### Группы компонентов


### События

## `entity:grass`

- Путь `Sword_B/entities/grass.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:grass","is_spawnable":false,"is_summonable":true,"is_experimental":false,"scripts":{"animate":["grass"]},"animations":{"grass":"controller.animation.grass"}}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 19): `{"family":["despawnear"]}`
- `minecraft:despawn` (строки 24): `{"filters":{"all_of":[{"test":"is_family","subject":"self","value":"despawnear"}]}}`
- `minecraft:health` (строки 35): `{"value":1}`
- `minecraft:collision_box` (строки 38): `{"width":0.0,"height":0.0}`
- `minecraft:fire_immune` (строки 42): `true`
- `minecraft:physics` (строки 43): `{}`

### Группы компонентов


### События

## `entity:ice`

- Путь `Sword_B/entities/ice.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:ice","is_spawnable":false,"is_summonable":true,"is_experimental":false,"scripts":{"animate":["ice"]},"animations":{"ice":"controller.animation.ice"}}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 19): `{"family":["despawnear"]}`
- `minecraft:despawn` (строки 24): `{"filters":{"all_of":[{"test":"is_family","subject":"self","value":"despawnear"}]}}`
- `minecraft:health` (строки 35): `{"value":1}`
- `minecraft:collision_box` (строки 38): `{"width":0.0,"height":0.0}`
- `minecraft:fire_immune` (строки 42): `true`
- `minecraft:physics` (строки 43): `{}`

### Группы компонентов


### События

## `entity:jungle`

- Путь `Sword_B/entities/jungle.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:jungle","is_spawnable":false,"is_summonable":true,"is_experimental":false,"scripts":{"animate":["jungle"]},"animations":{"jungle":"controller.animation.jungle"}}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 19): `{"family":["despawnear"]}`
- `minecraft:despawn` (строки 24): `{"filters":{"all_of":[{"test":"is_family","subject":"self","value":"despawnear"}]}}`
- `minecraft:health` (строки 35): `{"value":1}`
- `minecraft:collision_box` (строки 38): `{"width":0.0,"height":0.0}`
- `minecraft:fire_immune` (строки 42): `true`
- `minecraft:physics` (строки 43): `{}`

### Группы компонентов


### События

## `entity:lapis`

- Путь `Sword_B/entities/lapis.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:lapis","is_spawnable":false,"is_summonable":true,"is_experimental":false,"scripts":{"animate":["lapis"]},"animations":{"lapis":"controller.animation.lapis"}}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 19): `{"family":["despawnear"]}`
- `minecraft:despawn` (строки 24): `{"filters":{"all_of":[{"test":"is_family","subject":"self","value":"despawnear"}]}}`
- `minecraft:health` (строки 35): `{"value":1}`
- `minecraft:collision_box` (строки 38): `{"width":0.0,"height":0.0}`
- `minecraft:fire_immune` (строки 42): `true`
- `minecraft:physics` (строки 43): `{}`

### Группы компонентов


### События

## `entity:lightning`

- Путь `Sword_B/entities/lightning.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:lightning","is_spawnable":false,"is_summonable":true,"is_experimental":false,"scripts":{"animate":["lightning"]},"animations":{"lightning":"controller.animation.lightning"}}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 19): `{"family":["despawnear"]}`
- `minecraft:despawn` (строки 24): `{"filters":{"all_of":[{"test":"is_family","subject":"self","value":"despawnear"}]}}`
- `minecraft:health` (строки 35): `{"value":1}`
- `minecraft:collision_box` (строки 38): `{"width":0.0,"height":0.0}`
- `minecraft:fire_immune` (строки 42): `true`
- `minecraft:physics` (строки 43): `{}`

### Группы компонентов


### События

## `entity:magma`

- Путь `Sword_B/entities/magma.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:magma","is_spawnable":false,"is_summonable":true,"is_experimental":false,"scripts":{"animate":["magma"]},"animations":{"magma":"controller.animation.magma"}}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 19): `{"family":["despawnear"]}`
- `minecraft:despawn` (строки 24): `{"filters":{"all_of":[{"test":"is_family","subject":"self","value":"despawnear"}]}}`
- `minecraft:health` (строки 35): `{"value":1}`
- `minecraft:collision_box` (строки 38): `{"width":0.0,"height":0.0}`
- `minecraft:fire_immune` (строки 42): `true`
- `minecraft:physics` (строки 43): `{}`

### Группы компонентов


### События

## `entity:normal`

- Путь `Sword_B/entities/normal.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:normal","is_spawnable":false,"is_summonable":true,"is_experimental":false,"scripts":{"animate":["normal"]},"animations":{"normal":"controller.animation.normal"}}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 19): `{"family":["despawnear"]}`
- `minecraft:despawn` (строки 24): `{"filters":{"all_of":[{"test":"is_family","subject":"self","value":"despawnear"}]}}`
- `minecraft:health` (строки 35): `{"value":1}`
- `minecraft:collision_box` (строки 38): `{"width":0.0,"height":0.0}`
- `minecraft:fire_immune` (строки 42): `true`
- `minecraft:physics` (строки 43): `{"has_gravity":false,"has_collision":false}`

### Группы компонентов


### События

## `entity:obsidian`

- Путь `Sword_B/entities/obsidian.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:obsidian","is_spawnable":false,"is_summonable":true,"is_experimental":false,"scripts":{"animate":["ob"]},"animations":{"ob":"controller.animation.ob"}}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 19): `{"family":["despawnear"]}`
- `minecraft:despawn` (строки 24): `{"filters":{"all_of":[{"test":"is_family","subject":"self","value":"despawnear"}]}}`
- `minecraft:health` (строки 35): `{"value":1}`
- `minecraft:collision_box` (строки 38): `{"width":0.0,"height":0.0}`
- `minecraft:fire_immune` (строки 42): `true`
- `minecraft:physics` (строки 43): `{}`

### Группы компонентов


### События

## `minecraft:player`

- Путь `Sword_B/entities/player.json`; format_version `"1.11.0"`.
- description: `{"identifier":"minecraft:player","is_spawnable":false,"is_summonable":false,"is_experimental":false,"scripts":{"animate":["normal"]},"animations":{"normal":"controller.animation.normal"}}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 364): `{"family":["player"]}`
- `minecraft:is_hidden_when_invisible` (строки 369): `{}`
- `minecraft:movement` (строки 370): `{"value":0.1}`
- `minecraft:loot` (строки 373): `{"table":"loot_tables/empty.json"}`
- `minecraft:collision_box` (строки 376): `{"width":0.6,"height":1.8}`
- `minecraft:can_climb` (строки 380): `{}`
- `minecraft:player.saturation` (строки 381): `{"value":20}`
- `minecraft:player.exhaustion` (строки 384): `{"value":0,"max":4}`
- `minecraft:player.level` (строки 388): `{"value":0,"max":24791}`
- `minecraft:player.experience` (строки 392): `{"value":0,"max":1}`
- `minecraft:breathable` (строки 396): `{"totalSupply":15,"suffocateTime":-1,"inhaleTime":3.75,"generatesBubbles":false}`
- `minecraft:nameable` (строки 402): `{"alwaysShow":true,"allowNameTagRenaming":false}`
- `minecraft:physics` (строки 406): `{}`
- `minecraft:insomnia` (строки 407): `{"days_until_insomnia":3}`
- `minecraft:rideable` (строки 410): `{"seat_count":2,"family_types":["parrot_tame"],"pull_in_entities":true,"seats":[{"position":[0.4,-0.15,0.04],"min_rider_count":0,"max_rider_count":0,"lock_rider_rotation":0},{"position":[-0.4,-0.15,0.04],"min_rider_count":1,"max_rider_count":2,"lock_rider_rotation":0}]}`
- `minecraft:scaffolding_climber` (строки 439): `{}`
- `minecraft:environment_sensor` (строки 440): `[{"on_environment":{"filters":{"all_of":[{"test":"has_mob_effect","subject":"self","value":"bad_omen"},{"test":"is_in_village","subject":"self","value":true}]},"event":"minecraft:trigger_raid"}},{"on_environment":{"filters":{"all_of":[{"test":"is_family","subject":"self","value":"player"}]},"event":"minecraft:event_normal_player"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:spectral_sword"}]},"event":"minecraft:spectral_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:blaze_sword"}]},"event":"minecraft:blaze_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:cactus_sword"}]},"event":"minecraft:cactus_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:coal_sword"}]},"event":"minecraft:coal_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:creeper_sword"}]},"event":"minecraft:creeper_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:emerald_sword"}]},"event":"minecraft:emerald_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:ender_sword"}]},"event":"minecraft:ender_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:fire_sword"}]},"event":"minecraft:fire_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:glowstone_sword"}]},"event":"minecraft:glowstone_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:grass_sword"}]},"event":"minecraft:grass_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:ice_sword"}]},"event":"minecraft:ice_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:jungle_sword"}]},"event":"minecraft:jungle_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:lapis_sword"}]},"event":"minecraft:lapis_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:lightning_sword"}]},"event":"minecraft:lightning_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:magma_sword"}]},"event":"minecraft:magma_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:obsidian_sword"}]},"event":"minecraft:obsidian_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:sea_sword"}]},"event":"minecraft:sea_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:shulker_sword"}]},"event":"minecraft:shulker_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:slime_sword"}]},"event":"minecraft:slime_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:spider_sword"}]},"event":"minecraft:spider_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:sponge_sword"}]},"event":"minecraft:sponge_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:sword_of_time"}]},"event":"minecraft:sword_of_time"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:tnt_sword"}]},"event":"minecraft:tnt_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:wither_sword"}]},"event":"minecraft:wither_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:bone_sword"}]},"event":"minecraft:bone_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:quartz_sword"}]},"event":"minecraft:quartz_sword"}}]`

### Группы компонентов

- `minecraft:normal_player` (строки 19,870): `{"minecraft:spell_effects":{},"minecraft:attack":{"damage":1}}`
- `minecraft:spectral_sword` (строки 25,486,875,904,907): `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:spectral","num_to_spawn":1,"single_use":true}]}`
- `minecraft:magma_sword` (строки 36,696,889,1002,1005): `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:magma","num_to_spawn":1,"single_use":true}]}`
- `minecraft:lightning_sword` (строки 47,681,888,995,998): `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:lightning","num_to_spawn":1,"single_use":true}]}`
- `minecraft:lapis_sword` (строки 58,666,887,988,991): `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:lapis","num_to_spawn":1,"single_use":true}]}`
- `minecraft:jungle_sword` (строки 69,651,886,981,984): `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:jungle","num_to_spawn":1,"single_use":true}]}`
- `minecraft:slime_sword` (строки 80,756,893,1030,1033): `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:slime","num_to_spawn":1,"single_use":true}]}`
- `minecraft:shulker_sword` (строки 91,741,892,1023,1026): `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:shulker","num_to_spawn":1,"single_use":true}]}`
- `minecraft:sea_sword` (строки 102,726,891,1016,1019): `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:sea","num_to_spawn":1,"single_use":true}]}`
- `minecraft:grass_sword` (строки 113,621,884,967,970): `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:grass","num_to_spawn":1,"single_use":true}]}`
- `minecraft:glowstone_sword` (строки 124,606,883,960,963): `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:glow","num_to_spawn":1,"single_use":true}]}`
- `minecraft:fire_sword` (строки 135,591,882,953,956): `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:fire","num_to_spawn":1,"single_use":true}]}`
- `minecraft:ender_sword` (строки 146,576,881,946,949): `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:ender","num_to_spawn":1,"single_use":true}],"minecraft:teleport":{"random_teleports":true,"max_random_teleport_time":30,"random_teleport_cube":[32,32,32],"target_distance":16,"target_teleport_chance":0.05,"light_teleport_chance":0.05},"minecraft:hurt_on_condition":{"damage_conditions":[{"filters":{"test":"in_water_or_rain","operator":"==","value":true},"cause":"drowning","damage_per_tick":1}]}}`
- `minecraft:emerald_sword` (строки 182,561,880,939,942): `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:emerald","num_to_spawn":1,"single_use":true}]}`
- `minecraft:creeper_sword` (строки 193,546,879,932,935): `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:creeper","num_to_spawn":1,"single_use":true}]}`
- `minecraft:coal_sword` (строки 204,531,878,925,928): `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:coal","num_to_spawn":1,"single_use":true}]}`
- `minecraft:cactus_sword` (строки 215,516,877,918,921): `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:cactus","num_to_spawn":1,"single_use":true}]}`
- `minecraft:blaze_sword` (строки 226,501,876,911,914): `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:blaze","num_to_spawn":1,"single_use":true}]}`
- `minecraft:wither_sword` (строки 237,831,898,1065,1068): `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:wither","num_to_spawn":1,"single_use":true}]}`
- `minecraft:tnt_sword` (строки 248,816,897,1058,1061): `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:tnt_sword","num_to_spawn":1,"single_use":true}]}`
- `minecraft:sword_of_time` (строки 259,801,896,1051,1054): `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:time","num_to_spawn":1,"single_use":true}]}`
- `minecraft:sponge_sword` (строки 270,786,895,1044,1047): `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:sponge","num_to_spawn":1,"single_use":true}]}`
- `minecraft:spider_sword` (строки 281,771,894,1037,1040): `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:spider","num_to_spawn":1,"single_use":true}]}`
- `minecraft:ice_sword` (строки 292,636,885,974,977): `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:ice","num_to_spawn":1,"single_use":true}]}`
- `minecraft:obsidian_sword` (строки 303,711,890,1009,1012): `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:obsidian","num_to_spawn":1,"single_use":true}]}`
- `minecraft:bone_sword` (строки 314,846,899,1072,1075): `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:bone","num_to_spawn":1,"single_use":true}]}`
- `minecraft:quartz_sword` (строки 325,861,900,1079,1082): `{}`
- `minecraft:add_bad_omen` (строки 326,1089,1096): `{"minecraft:spell_effects":{"add_effects":[{"effect":"bad_omen","duration":6000,"display_on_screen_animation":true}]},"minecraft:timer":{"time":[0,0],"looping":false,"time_down_event":{"event":"minecraft:clear_add_bad_omen","target":"self"}}}`
- `minecraft:clear_bad_omen_spell_effect` (строки 348,1101): `{"minecraft:spell_effects":{}}`
- `minecraft:raid_trigger` (строки 351,352,1108,1115): `{"minecraft:raid_trigger":{"triggered_event":{"event":"minecraft:remove_raid_trigger","target":"self"}},"minecraft:spell_effects":{"remove_effects":"bad_omen"}}`

### События

**`minecraft:event_normal_player`** (строки 471,867):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:normal_player"]},"remove":{"component_groups":["minecraft:spectral_sword","minecraft:blaze_sword","minecraft:cactus_sword","minecraft:coal_sword","minecraft:creeper_sword","minecraft:emerald_sword","minecraft:ender_sword","minecraft:fire_sword","minecraft:glowstone_sword","minecraft:grass_sword","minecraft:ice_sword","minecraft:jungle_sword","minecraft:lapis_sword","minecraft:lightning_sword","minecraft:magma_sword","minecraft:obsidian_sword","minecraft:sea_sword","minecraft:shulker_sword","minecraft:slime_sword","minecraft:spider_sword","minecraft:sponge_sword","minecraft:sword_of_time","minecraft:tnt_sword","minecraft:wither_sword","minecraft:bone_sword","minecraft:quartz_sword"]}}`

**`minecraft:spectral_sword`** (строки 25,486,875,904,907):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:spectral_sword"]}}`

**`minecraft:blaze_sword`** (строки 226,501,876,911,914):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:blaze_sword"]}}`

**`minecraft:cactus_sword`** (строки 215,516,877,918,921):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:cactus_sword"]}}`

**`minecraft:coal_sword`** (строки 204,531,878,925,928):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:coal_sword"]}}`

**`minecraft:creeper_sword`** (строки 193,546,879,932,935):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:creeper_sword"]}}`

**`minecraft:emerald_sword`** (строки 182,561,880,939,942):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:emerald_sword"]}}`

**`minecraft:ender_sword`** (строки 146,576,881,946,949):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:ender_sword"]}}`

**`minecraft:fire_sword`** (строки 135,591,882,953,956):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:fire_sword"]}}`

**`minecraft:glowstone_sword`** (строки 124,606,883,960,963):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:glowstone_sword"]}}`

**`minecraft:grass_sword`** (строки 113,621,884,967,970):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:grass_sword"]}}`

**`minecraft:ice_sword`** (строки 292,636,885,974,977):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:ice_sword"]}}`

**`minecraft:jungle_sword`** (строки 69,651,886,981,984):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:jungle_sword"]}}`

**`minecraft:lapis_sword`** (строки 58,666,887,988,991):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:lapis_sword"]}}`

**`minecraft:lightning_sword`** (строки 47,681,888,995,998):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:lightning_sword"]}}`

**`minecraft:magma_sword`** (строки 36,696,889,1002,1005):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:magma_sword"]}}`

**`minecraft:obsidian_sword`** (строки 303,711,890,1009,1012):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:obsidian_sword"]}}`

**`minecraft:sea_sword`** (строки 102,726,891,1016,1019):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:sea_sword"]}}`

**`minecraft:shulker_sword`** (строки 91,741,892,1023,1026):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:shulker_sword"]}}`

**`minecraft:slime_sword`** (строки 80,756,893,1030,1033):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:slime_sword"]}}`

**`minecraft:spider_sword`** (строки 281,771,894,1037,1040):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:spider_sword"]}}`

**`minecraft:sponge_sword`** (строки 270,786,895,1044,1047):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:sponge_sword"]}}`

**`minecraft:sword_of_time`** (строки 259,801,896,1051,1054):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:sword_of_time"]}}`

**`minecraft:tnt_sword`** (строки 248,816,897,1058,1061):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:tnt_sword"]}}`

**`minecraft:wither_sword`** (строки 237,831,898,1065,1068):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:wither_sword"]}}`

**`minecraft:bone_sword`** (строки 314,846,899,1072,1075):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:bone_sword"]}}`

**`minecraft:quartz_sword`** (строки 325,861,900,1079,1082):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:quartz_sword"]}}`

**`minecraft:gain_bad_omen`** (строки 1086):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:add_bad_omen"]}}`

**`minecraft:clear_add_bad_omen`** (строки 343,1093):

- `$` — поля действия: `{"remove":{"component_groups":["minecraft:add_bad_omen"]},"add":{"component_groups":["minecraft:clear_bad_omen_spell_effect"]}}`

**`minecraft:trigger_raid`** (строки 457,1105):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:raid_trigger"]}}`

**`minecraft:remove_raid_trigger`** (строки 354,1112):

- `$` — поля действия: `{"remove":{"component_groups":["minecraft:raid_trigger"]}}`

## `entity:sea`

- Путь `Sword_B/entities/sea.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:sea","is_spawnable":false,"is_summonable":true,"is_experimental":false,"scripts":{"animate":["sea"]},"animations":{"sea":"controller.animation.sea"}}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 19): `{"family":["despawnear"]}`
- `minecraft:despawn` (строки 24): `{"filters":{"all_of":[{"test":"is_family","subject":"self","value":"despawnear"}]}}`
- `minecraft:health` (строки 35): `{"value":1}`
- `minecraft:collision_box` (строки 38): `{"width":0.0,"height":0.0}`
- `minecraft:fire_immune` (строки 42): `true`
- `minecraft:physics` (строки 43): `{}`

### Группы компонентов


### События

## `entity:shulker`

- Путь `Sword_B/entities/shulker.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:shulker","is_spawnable":false,"is_summonable":true,"is_experimental":false,"scripts":{"animate":["shulker"]},"animations":{"shulker":"controller.animation.shulker"}}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 19): `{"family":["despawnear"]}`
- `minecraft:despawn` (строки 24): `{"filters":{"all_of":[{"test":"is_family","subject":"self","value":"despawnear"}]}}`
- `minecraft:health` (строки 35): `{"value":1}`
- `minecraft:collision_box` (строки 38): `{"width":0.0,"height":0.0}`
- `minecraft:fire_immune` (строки 42): `true`
- `minecraft:physics` (строки 43): `{}`

### Группы компонентов


### События

## `Sword_B/entities/shulker2.json`

**Не разобран JSON5:** `<string>:75 Unexpected "}" at column 1`. Исходник не изменять и изучать вручную.

## `entity:slime`

- Путь `Sword_B/entities/slime.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:slime","is_spawnable":false,"is_summonable":true,"is_experimental":false,"scripts":{"animate":["slime"]},"animations":{"slime":"controller.animation.slime"}}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 19): `{"family":["despawnear"]}`
- `minecraft:despawn` (строки 24): `{"filters":{"all_of":[{"test":"is_family","subject":"self","value":"despawnear"}]}}`
- `minecraft:health` (строки 35): `{"value":1}`
- `minecraft:collision_box` (строки 38): `{"width":0.0,"height":0.0}`
- `minecraft:fire_immune` (строки 42): `true`
- `minecraft:physics` (строки 43): `{}`

### Группы компонентов


### События

## `entity:spectral`

- Путь `Sword_B/entities/spectral.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:spectral","is_spawnable":false,"is_summonable":true,"is_experimental":false,"scripts":{"animate":["spectral"]},"animations":{"spectral":"controller.animation.spectral"}}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 19): `{"family":["despawnear"]}`
- `minecraft:despawn` (строки 24): `{"filters":{"all_of":[{"test":"is_family","subject":"self","value":"despawnear"}]}}`
- `minecraft:health` (строки 35): `{"value":1}`
- `minecraft:collision_box` (строки 38): `{"width":0.0,"height":0.0}`
- `minecraft:fire_immune` (строки 42): `true`
- `minecraft:physics` (строки 43): `{}`

### Группы компонентов


### События

## `entity:spider`

- Путь `Sword_B/entities/spider.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:spider","is_spawnable":false,"is_summonable":true,"is_experimental":false,"scripts":{"animate":["spider"]},"animations":{"spider":"controller.animation.spider"}}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 19): `{"family":["despawnear"]}`
- `minecraft:despawn` (строки 24): `{"filters":{"all_of":[{"test":"is_family","subject":"self","value":"despawnear"}]}}`
- `minecraft:health` (строки 35): `{"value":1}`
- `minecraft:collision_box` (строки 38): `{"width":0.0,"height":0.0}`
- `minecraft:fire_immune` (строки 42): `true`
- `minecraft:physics` (строки 43): `{}`

### Группы компонентов


### События

## `entity:sponge`

- Путь `Sword_B/entities/sponge.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:sponge","is_spawnable":false,"is_summonable":true,"is_experimental":false,"scripts":{"animate":["sponge"]},"animations":{"sponge":"controller.animation.sponge"}}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 19): `{"family":["despawnear"]}`
- `minecraft:despawn` (строки 24): `{"filters":{"all_of":[{"test":"is_family","subject":"self","value":"despawnear"}]}}`
- `minecraft:health` (строки 35): `{"value":1}`
- `minecraft:collision_box` (строки 38): `{"width":0.0,"height":0.0}`
- `minecraft:fire_immune` (строки 42): `true`
- `minecraft:physics` (строки 43): `{}`

### Группы компонентов


### События

## `entity:time`

- Путь `Sword_B/entities/time.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:time","is_spawnable":false,"is_summonable":true,"is_experimental":false,"scripts":{"animate":["time"]},"animations":{"time":"controller.animation.time"}}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 19): `{"family":["despawnear"]}`
- `minecraft:despawn` (строки 24): `{"filters":{"all_of":[{"test":"is_family","subject":"self","value":"despawnear"}]}}`
- `minecraft:health` (строки 35): `{"value":1}`
- `minecraft:collision_box` (строки 38): `{"width":0.0,"height":0.0}`
- `minecraft:fire_immune` (строки 42): `true`
- `minecraft:physics` (строки 43): `{}`

### Группы компонентов


### События

## `entity:tnt_sword`

- Путь `Sword_B/entities/tnt_sword.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:tnt_sword","is_spawnable":false,"is_summonable":true,"is_experimental":false,"scripts":{"animate":["tnt"]},"animations":{"tnt":"controller.animation.tnt"}}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 19): `{"family":["despawnear"]}`
- `minecraft:despawn` (строки 24): `{"filters":{"all_of":[{"test":"is_family","subject":"self","value":"despawnear"}]}}`
- `minecraft:health` (строки 35): `{"value":1}`
- `minecraft:collision_box` (строки 38): `{"width":0.0,"height":0.0}`
- `minecraft:fire_immune` (строки 42): `true`
- `minecraft:physics` (строки 43): `{}`

### Группы компонентов


### События

## `entity:wither`

- Путь `Sword_B/entities/wither_s.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:wither","is_spawnable":false,"is_summonable":true,"is_experimental":false,"scripts":{"animate":["wither"]},"animations":{"wither":"controller.animation.wither"}}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 19): `{"family":["despawnear"]}`
- `minecraft:despawn` (строки 24): `{"filters":{"all_of":[{"test":"is_family","subject":"self","value":"despawnear"}]}}`
- `minecraft:health` (строки 35): `{"value":1}`
- `minecraft:collision_box` (строки 38): `{"width":0.0,"height":0.0}`
- `minecraft:fire_immune` (строки 42): `true`
- `minecraft:physics` (строки 43): `{}`

### Группы компонентов


### События

