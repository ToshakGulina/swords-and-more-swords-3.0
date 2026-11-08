# Связи предметов 1.6: sensor → player group → spawn entity → controller

Автоматический обзор только по прямым буквальным связям в `Sword_B/entities/player.json`: sensor содержит точный item ID, затем event по имени, `add.component_groups`, компоненты `minecraft:spawn_entity` в этих группах, ID сущности и её `description.animations`. Непосредственные проверки других сущностей, косвенные события, команды, список animate, значения по умолчанию, ошибки парсинга и ресурсы могут менять или обрывать цепь. Отсутствие найденной ссылки не доказывает отсутствия механики. Оригинальные контроллеры полностью приведены в [реестре контроллеров](animation-ledger-1.6.md).

## `effect:blaze_sword`

- Предмет: `Sword_B/items/blaze_sword.json`.
- Совпадений sensor: 1.

- Sensor: `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:blaze_sword"}]},"event":"minecraft:blaze_sword"}}`
- Event `minecraft:blaze_sword`: `{"add":{"component_groups":["minecraft:blaze_sword"]}}`
- Группа `minecraft:blaze_sword`: `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:blaze","num_to_spawn":1,"single_use":true}]}`
  - `entity:blaze`: `Sword_B/entities/blaze.json`; scripts `{"animate":["blaze"]}`, animations `{"blaze":"controller.animation.blaze"}`.
    - `blaze` → `controller.animation.blaze` → `Sword_B/animation_controllers/blaze_sword.json`.

## `effect:bone_sword`

- Предмет: `Sword_B/items/bone_sword.json`.
- Совпадений sensor: 1.

- Sensor: `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:bone_sword"}]},"event":"minecraft:bone_sword"}}`
- Event `minecraft:bone_sword`: `{"add":{"component_groups":["minecraft:bone_sword"]}}`
- Группа `minecraft:bone_sword`: `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:bone","num_to_spawn":1,"single_use":true}]}`
  - `entity:bone`: `Sword_B/entities/bone.json`; scripts `{"animate":["bone"]}`, animations `{"bone":"controller.animation.bone"}`.
    - `bone` → `controller.animation.bone` → `Sword_B/animation_controllers/bone_sword.json`.

## `effect:cactus_sword`

- Предмет: `Sword_B/items/cactus_sword.json`.
- Совпадений sensor: 1.

- Sensor: `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:cactus_sword"}]},"event":"minecraft:cactus_sword"}}`
- Event `minecraft:cactus_sword`: `{"add":{"component_groups":["minecraft:cactus_sword"]}}`
- Группа `minecraft:cactus_sword`: `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:cactus","num_to_spawn":1,"single_use":true}]}`
  - `entity:cactus`: `Sword_B/entities/cactus.json`; scripts `{"animate":["cactus"]}`, animations `{"cactus":"controller.animation.cactus"}`.
    - `cactus` → `controller.animation.cactus` → `Sword_B/animation_controllers/cactus_sword.json`.

## `effect:coal_sword`

- Предмет: `Sword_B/items/coal_sword.json`.
- Совпадений sensor: 1.

- Sensor: `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:coal_sword"}]},"event":"minecraft:coal_sword"}}`
- Event `minecraft:coal_sword`: `{"add":{"component_groups":["minecraft:coal_sword"]}}`
- Группа `minecraft:coal_sword`: `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:coal","num_to_spawn":1,"single_use":true}]}`
  - `entity:coal`: `Sword_B/entities/coal.json`; scripts `{"animate":["coal"]}`, animations `{"coal":"controller.animation.coal"}`.
    - `coal` → `controller.animation.coal` → `Sword_B/animation_controllers/coal_sword.json`.

## `effect:creeper_sword`

- Предмет: `Sword_B/items/creeper_sword.json`.
- Совпадений sensor: 1.

- Sensor: `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:creeper_sword"}]},"event":"minecraft:creeper_sword"}}`
- Event `minecraft:creeper_sword`: `{"add":{"component_groups":["minecraft:creeper_sword"]}}`
- Группа `minecraft:creeper_sword`: `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:creeper","num_to_spawn":1,"single_use":true}]}`
  - `entity:creeper`: `Sword_B/entities/creeper.json`; scripts `{"animate":["creeper"]}`, animations `{"creeper":"controller.animation.creeper"}`.
    - `creeper` → `controller.animation.creeper` → `Sword_B/animation_controllers/creeper_sword.json`.

## `effect:emerald_sword`

- Предмет: `Sword_B/items/emerald_sword.json`.
- Совпадений sensor: 1.

- Sensor: `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:emerald_sword"}]},"event":"minecraft:emerald_sword"}}`
- Event `minecraft:emerald_sword`: `{"add":{"component_groups":["minecraft:emerald_sword"]}}`
- Группа `minecraft:emerald_sword`: `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:emerald","num_to_spawn":1,"single_use":true}]}`
  - `entity:emerald`: `Sword_B/entities/emerald.json`; scripts `{"animate":["emerald"]}`, animations `{"emerald":"controller.animation.emerald"}`.
    - `emerald` → `controller.animation.emerald` → `Sword_B/animation_controllers/emerald_sword.json`.

## `effect:ender_sword`

- Предмет: `Sword_B/items/ender_sword.json`.
- Совпадений sensor: 1.

- Sensor: `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:ender_sword"}]},"event":"minecraft:ender_sword"}}`
- Event `minecraft:ender_sword`: `{"add":{"component_groups":["minecraft:ender_sword"]}}`
- Группа `minecraft:ender_sword`: `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:ender","num_to_spawn":1,"single_use":true}],"minecraft:teleport":{"random_teleports":true,"max_random_teleport_time":30,"random_teleport_cube":[32,32,32],"target_distance":16,"target_teleport_chance":0.05,"light_teleport_chance":0.05},"minecraft:hurt_on_condition":{"damage_conditions":[{"filters":{"test":"in_water_or_rain","operator":"==","value":true},"cause":"drowning","damage_per_tick":1}]}}`
  - `entity:ender`: `Sword_B/entities/ender.json`; scripts `{"animate":["ender"]}`, animations `{"ender":"controller.animation.ender"}`.
    - `ender` → `controller.animation.ender` → `Sword_B/animation_controllers/ender_sword.json`.

## `effect:fire_sword`

- Предмет: `Sword_B/items/fire_sword.json`.
- Совпадений sensor: 1.

- Sensor: `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:fire_sword"}]},"event":"minecraft:fire_sword"}}`
- Event `minecraft:fire_sword`: `{"add":{"component_groups":["minecraft:fire_sword"]}}`
- Группа `minecraft:fire_sword`: `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:fire","num_to_spawn":1,"single_use":true}]}`
  - `entity:fire`: `Sword_B/entities/fire.json`; scripts `{"animate":["fire"]}`, animations `{"fire":"controller.animation.fire"}`.
    - `fire` → `controller.animation.fire` → `Sword_B/animation_controllers/fire_sword.json`.

## `effect:glowstone_sword`

- Предмет: `Sword_B/items/glowstone_sword.json`.
- Совпадений sensor: 1.

- Sensor: `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:glowstone_sword"}]},"event":"minecraft:glowstone_sword"}}`
- Event `minecraft:glowstone_sword`: `{"add":{"component_groups":["minecraft:glowstone_sword"]}}`
- Группа `minecraft:glowstone_sword`: `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:glow","num_to_spawn":1,"single_use":true}]}`
  - `entity:glow`: `Sword_B/entities/glowstone_sword.json`; scripts `{"animate":["glow"]}`, animations `{"glow":"controller.animation.glow"}`.
    - `glow` → `controller.animation.glow` → `Sword_B/animation_controllers/glowstone_sword.json`.

## `effect:grass_sword`

- Предмет: `Sword_B/items/grass_sword.json`.
- Совпадений sensor: 1.

- Sensor: `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:grass_sword"}]},"event":"minecraft:grass_sword"}}`
- Event `minecraft:grass_sword`: `{"add":{"component_groups":["minecraft:grass_sword"]}}`
- Группа `minecraft:grass_sword`: `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:grass","num_to_spawn":1,"single_use":true}]}`
  - `entity:grass`: `Sword_B/entities/grass.json`; scripts `{"animate":["grass"]}`, animations `{"grass":"controller.animation.grass"}`.
    - `grass` → `controller.animation.grass` → `Sword_B/animation_controllers/grass_sword.json`.

## `effect:ice_sword`

- Предмет: `Sword_B/items/ice_sword.json`.
- Совпадений sensor: 1.

- Sensor: `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:ice_sword"}]},"event":"minecraft:ice_sword"}}`
- Event `minecraft:ice_sword`: `{"add":{"component_groups":["minecraft:ice_sword"]}}`
- Группа `minecraft:ice_sword`: `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:ice","num_to_spawn":1,"single_use":true}]}`
  - `entity:ice`: `Sword_B/entities/ice.json`; scripts `{"animate":["ice"]}`, animations `{"ice":"controller.animation.ice"}`.
    - `ice` → `controller.animation.ice` → `Sword_B/animation_controllers/ice_sword.json`.

## `effect:jungle_sword`

- Предмет: `Sword_B/items/jungle_sword.json`.
- Совпадений sensor: 1.

- Sensor: `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:jungle_sword"}]},"event":"minecraft:jungle_sword"}}`
- Event `minecraft:jungle_sword`: `{"add":{"component_groups":["minecraft:jungle_sword"]}}`
- Группа `minecraft:jungle_sword`: `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:jungle","num_to_spawn":1,"single_use":true}]}`
  - `entity:jungle`: `Sword_B/entities/jungle.json`; scripts `{"animate":["jungle"]}`, animations `{"jungle":"controller.animation.jungle"}`.
    - `jungle` → `controller.animation.jungle` → `Sword_B/animation_controllers/jungle_sword.json`.

## `effect:lapis_sword`

- Предмет: `Sword_B/items/lapis_sword.json`.
- Совпадений sensor: 1.

- Sensor: `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:lapis_sword"}]},"event":"minecraft:lapis_sword"}}`
- Event `minecraft:lapis_sword`: `{"add":{"component_groups":["minecraft:lapis_sword"]}}`
- Группа `minecraft:lapis_sword`: `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:lapis","num_to_spawn":1,"single_use":true}]}`
  - `entity:lapis`: `Sword_B/entities/lapis.json`; scripts `{"animate":["lapis"]}`, animations `{"lapis":"controller.animation.lapis"}`.
    - `lapis` → `controller.animation.lapis` → `Sword_B/animation_controllers/lapis_sword.json`.

## `effect:lightning_sword`

- Предмет: `Sword_B/items/lightning_sword.json`.
- Совпадений sensor: 1.

- Sensor: `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:lightning_sword"}]},"event":"minecraft:lightning_sword"}}`
- Event `minecraft:lightning_sword`: `{"add":{"component_groups":["minecraft:lightning_sword"]}}`
- Группа `minecraft:lightning_sword`: `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:lightning","num_to_spawn":1,"single_use":true}]}`
  - `entity:lightning`: `Sword_B/entities/lightning.json`; scripts `{"animate":["lightning"]}`, animations `{"lightning":"controller.animation.lightning"}`.
    - `lightning` → `controller.animation.lightning` → `Sword_B/animation_controllers/lightning sword.json`.

## `effect:magma_sword`

- Предмет: `Sword_B/items/magma_sword.json`.
- Совпадений sensor: 1.

- Sensor: `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:magma_sword"}]},"event":"minecraft:magma_sword"}}`
- Event `minecraft:magma_sword`: `{"add":{"component_groups":["minecraft:magma_sword"]}}`
- Группа `minecraft:magma_sword`: `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:magma","num_to_spawn":1,"single_use":true}]}`
  - `entity:magma`: `Sword_B/entities/magma.json`; scripts `{"animate":["magma"]}`, animations `{"magma":"controller.animation.magma"}`.
    - `magma` → `controller.animation.magma` → `Sword_B/animation_controllers/magma_sword.json`.

## `effect:obsidian_sword`

- Предмет: `Sword_B/items/obsidian_sword.json`.
- Совпадений sensor: 1.

- Sensor: `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:obsidian_sword"}]},"event":"minecraft:obsidian_sword"}}`
- Event `minecraft:obsidian_sword`: `{"add":{"component_groups":["minecraft:obsidian_sword"]}}`
- Группа `minecraft:obsidian_sword`: `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:obsidian","num_to_spawn":1,"single_use":true}]}`
  - `entity:obsidian`: `Sword_B/entities/obsidian.json`; scripts `{"animate":["ob"]}`, animations `{"ob":"controller.animation.ob"}`.
    - `ob` → `controller.animation.ob` → `Sword_B/animation_controllers/obsidian_sword.json`.

## `effect:quartz_sword`

- Предмет: `Sword_B/items/quartz_sword.json`.
- Совпадений sensor: 1.

- Sensor: `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:quartz_sword"}]},"event":"minecraft:quartz_sword"}}`
- Event `minecraft:quartz_sword`: `{"add":{"component_groups":["minecraft:quartz_sword"]}}`
- Группа `minecraft:quartz_sword`: `{}`

## `effect:sea_sword`

- Предмет: `Sword_B/items/sea_sword.json`.
- Совпадений sensor: 1.

- Sensor: `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:sea_sword"}]},"event":"minecraft:sea_sword"}}`
- Event `minecraft:sea_sword`: `{"add":{"component_groups":["minecraft:sea_sword"]}}`
- Группа `minecraft:sea_sword`: `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:sea","num_to_spawn":1,"single_use":true}]}`
  - `entity:sea`: `Sword_B/entities/sea.json`; scripts `{"animate":["sea"]}`, animations `{"sea":"controller.animation.sea"}`.
    - `sea` → `controller.animation.sea` → `Sword_B/animation_controllers/sea_sword.json`.

## `effect:shulker_sword`

- Предмет: `Sword_B/items/shulker_sword.json`.
- Совпадений sensor: 1.

- Sensor: `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:shulker_sword"}]},"event":"minecraft:shulker_sword"}}`
- Event `minecraft:shulker_sword`: `{"add":{"component_groups":["minecraft:shulker_sword"]}}`
- Группа `minecraft:shulker_sword`: `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:shulker","num_to_spawn":1,"single_use":true}]}`
  - `entity:shulker`: `Sword_B/entities/shulker.json`; scripts `{"animate":["shulker"]}`, animations `{"shulker":"controller.animation.shulker"}`.
    - `shulker` → `controller.animation.shulker` → `Sword_B/animation_controllers/shulker_sword.json`.

## `effect:slime_sword`

- Предмет: `Sword_B/items/slime_sword.json`.
- Совпадений sensor: 1.

- Sensor: `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:slime_sword"}]},"event":"minecraft:slime_sword"}}`
- Event `minecraft:slime_sword`: `{"add":{"component_groups":["minecraft:slime_sword"]}}`
- Группа `minecraft:slime_sword`: `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:slime","num_to_spawn":1,"single_use":true}]}`
  - `entity:slime`: `Sword_B/entities/slime.json`; scripts `{"animate":["slime"]}`, animations `{"slime":"controller.animation.slime"}`.
    - `slime` → `controller.animation.slime` → `Sword_B/animation_controllers/slime_sword.json`.

## `effect:spectral_sword`

- Предмет: `Sword_B/items/spectral_sword.json`.
- Совпадений sensor: 1.

- Sensor: `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:spectral_sword"}]},"event":"minecraft:spectral_sword"}}`
- Event `minecraft:spectral_sword`: `{"add":{"component_groups":["minecraft:spectral_sword"]}}`
- Группа `minecraft:spectral_sword`: `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:spectral","num_to_spawn":1,"single_use":true}]}`
  - `entity:spectral`: `Sword_B/entities/spectral.json`; scripts `{"animate":["spectral"]}`, animations `{"spectral":"controller.animation.spectral"}`.
    - `spectral` → `controller.animation.spectral` → `Sword_B/animation_controllers/spectral_sword.json`.

## `effect:spider_sword`

- Предмет: `Sword_B/items/spider_sword.json`.
- Совпадений sensor: 1.

- Sensor: `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:spider_sword"}]},"event":"minecraft:spider_sword"}}`
- Event `minecraft:spider_sword`: `{"add":{"component_groups":["minecraft:spider_sword"]}}`
- Группа `minecraft:spider_sword`: `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:spider","num_to_spawn":1,"single_use":true}]}`
  - `entity:spider`: `Sword_B/entities/spider.json`; scripts `{"animate":["spider"]}`, animations `{"spider":"controller.animation.spider"}`.
    - `spider` → `controller.animation.spider` → `Sword_B/animation_controllers/spider_sword.json`.

## `effect:sponge_sword`

- Предмет: `Sword_B/items/sponge_sword.json`.
- Совпадений sensor: 1.

- Sensor: `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:sponge_sword"}]},"event":"minecraft:sponge_sword"}}`
- Event `minecraft:sponge_sword`: `{"add":{"component_groups":["minecraft:sponge_sword"]}}`
- Группа `minecraft:sponge_sword`: `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:sponge","num_to_spawn":1,"single_use":true}]}`
  - `entity:sponge`: `Sword_B/entities/sponge.json`; scripts `{"animate":["sponge"]}`, animations `{"sponge":"controller.animation.sponge"}`.
    - `sponge` → `controller.animation.sponge` → `Sword_B/animation_controllers/sponge_sword.json`.

## `effect:sword_of_time`

- Предмет: `Sword_B/items/Sword of Time.json`.
- Совпадений sensor: 1.

- Sensor: `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:sword_of_time"}]},"event":"minecraft:sword_of_time"}}`
- Event `minecraft:sword_of_time`: `{"add":{"component_groups":["minecraft:sword_of_time"]}}`
- Группа `minecraft:sword_of_time`: `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:time","num_to_spawn":1,"single_use":true}]}`
  - `entity:time`: `Sword_B/entities/time.json`; scripts `{"animate":["time"]}`, animations `{"time":"controller.animation.time"}`.
    - `time` → `controller.animation.time` → `Sword_B/animation_controllers/sword of time.json`.

## `effect:tnt_sword`

- Предмет: `Sword_B/items/tnt_sword.json`.
- Совпадений sensor: 1.

- Sensor: `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:tnt_sword"}]},"event":"minecraft:tnt_sword"}}`
- Event `minecraft:tnt_sword`: `{"add":{"component_groups":["minecraft:tnt_sword"]}}`
- Группа `minecraft:tnt_sword`: `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:tnt_sword","num_to_spawn":1,"single_use":true}]}`
  - `entity:tnt_sword`: `Sword_B/entities/tnt_sword.json`; scripts `{"animate":["tnt"]}`, animations `{"tnt":"controller.animation.tnt"}`.
    - `tnt` → `controller.animation.tnt` → `Sword_B/animation_controllers/tnt_sword.json`.

## `effect:wither_sword`

- Предмет: `Sword_B/items/wither_sword.json`.
- Совпадений sensor: 1.

- Sensor: `{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:wither_sword"}]},"event":"minecraft:wither_sword"}}`
- Event `minecraft:wither_sword`: `{"add":{"component_groups":["minecraft:wither_sword"]}}`
- Группа `minecraft:wither_sword`: `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"spawn_entity":"entity:wither","num_to_spawn":1,"single_use":true}]}`
  - `entity:wither`: `Sword_B/entities/wither_s.json`; scripts `{"animate":["wither"]}`, animations `{"wither":"controller.animation.wither"}`.
    - `wither` → `controller.animation.wither` → `Sword_B/animation_controllers/wither_sword.json`.

