# Реестр поведения сущностей — архив 2.8.8

Автоматический структурный разбор каждого JSON в `Swords_B/entities/`: описание, все компоненты и группы в исходных значениях, все события как деревья шагов/условных ветвей. Номера строк — все текстовые вхождения ключа; это ориентир, не точная граница блока. Набор не доказывает связи конкретного объекта с конкретным предметом и не является ручной верификацией.

Соседние поля одного объекта не упорядочены этим отчётом. Веса в randomize — только относительные доли данного выбора при всех явных неотрицательных целых весах; успех действия, фильтры, вложенные вероятности и запуск события отдельно. Для повторяющихся ключей и неразобранного JSON см. оригинал: информация JSON5-парсера может теряться.

## `entity:alpha_wolf`

- Путь `Swords_B/entities/alpha_wolf.json`; format_version `"1.13.0"`.
- description: `{"animations":{"despawn_wolf":"controller.animation.despawn_wolf"},"identifier":"entity:alpha_wolf","is_experimental":false,"is_spawnable":true,"is_summonable":true,"runtime_identifier":"minecraft:wolf","scripts":{"animate":["despawn_wolf"]}}`.

### Постоянные компоненты

- `minecraft:angry` (строки 32): `{"broadcast_anger":true,"broadcast_range":30,"calm_event":{},"duration":75}`
- `minecraft:attack` (строки 38): `{"damage":8}`
- `minecraft:behavior.float` (строки 41): `{"priority":0}`
- `minecraft:behavior.hurt_by_target` (строки 44): `{"priority":1}`
- `minecraft:behavior.melee_attack` (строки 47): `{"priority":1,"reach_multiplier":1,"target_dist":3,"track_target":true}`
- `minecraft:behavior.nearest_attackable_target` (строки 53): `{"entity_types":[{"filters":{"any_of":[{"subject":"other","test":"is_family","value":"player"},{"subject":"other","test":"is_family","value":"panda"},{"subject":"other","test":"is_family","value":"irongolem"},{"subject":"other","test":"is_family","value":"snowgolem"},{"subject":"other","test":"is_family","value":"dolphin"},{"subject":"other","test":"is_family","value":"fox"},{"subject":"other","test":"is_family","value":"llama"},{"subject":"other","test":"is_family","value":"mushroomcow"},{"subject":"other","test":"is_family","value":"mule"},{"subject":"other","test":"is_family","value":"panda"},{"subject":"other","test":"is_family","value":"pig"},{"subject":"other","test":"is_family","value":"polarbear"},{"subject":"other","test":"is_family","value":"rabbit"},{"subject":"other","test":"is_family","value":"villager"},{"subject":"other","test":"is_family","value":"wandering_trader"},{"subject":"other","test":"is_family","value":"sheep"},{"subject":"other","test":"is_family","value":"chicken"},{"subject":"other","test":"is_family","value":"cow"},{"subject":"other","test":"is_family","value":"horse"},{"subject":"other","test":"is_family","value":"donkey"}]},"max_dist":30}],"priority":1}`
- `minecraft:behavior.random_stroll` (строки 85): `{"priority":2,"speed_multiplier":1}`
- `minecraft:breathable` (строки 89): `{"suffocate_time":0,"total_supply":15}`
- `minecraft:can_climb` (строки 93): `{}`
- `minecraft:collision_box` (строки 94): `{"height":0.8,"width":0.6}`
- `minecraft:damage_sensor` (строки 98): `{"triggers":[{"deals_damage":true,"on_damage":{"event":"minecraft:wolf_sword","filters":{"all_of":[{"domain":"hand","subject":"other","test":"has_equipment","value":"effect:silver_sword"},{"subject":"other","test":"is_family","value":"player"},{"test":"has_damage","value":"fatal"}]}}},{"deals_damage":true,"on_damage":{"event":"add_effects","filters":{"all_of":[{"domain":"hand","operator":"!=","subject":"other","test":"has_equipment","value":"effect:silver_sword"},{"subject":"other","test":"is_family","value":"player"}]}}},{"deals_damage":true,"on_damage":{"event":"clear_effects","filters":{"all_of":[{"domain":"hand","subject":"other","test":"has_equipment","value":"effect:silver_sword"},{"subject":"other","test":"is_family","value":"player"}]}}}]}`
- `minecraft:experience_reward` (строки 170): `{"on_bred":"Math.Random(1,7)","on_death":"query.last_hit_by_player ? Math.Random(1,3) : 30"}`
- `minecraft:health` (строки 174): `{"max":480,"value":480}`
- `minecraft:hurt_on_condition` (строки 178): `{"damage_conditions":[{"cause":"lava","damage_per_tick":4,"filters":{"operator":"==","subject":"self","test":"in_lava","value":true}}]}`
- `minecraft:jump.static` (строки 192): `{}`
- `minecraft:knockback_resistance` (строки 193): `{"value":0.5}`
- `minecraft:movement` (строки 196): `{"value":0.4}`
- `minecraft:movement.basic` (строки 199): `{}`
- `minecraft:nameable` (строки 200): `{}`
- `minecraft:navigation.walk` (строки 201): `{"avoid_damage_blocks":true,"can_path_over_water":true}`
- `minecraft:physics` (строки 205): `{}`
- `minecraft:pushable` (строки 206): `{"is_pushable":true,"is_pushable_by_piston":true}`
- `minecraft:scale` (строки 210): `{"value":1.8}`
- `minecraft:type_family` (строки 213): `{"family":["wolf","mob","monster","alpha_wolf"]}`

### Группы компонентов

- `despawn` (строки 20,249,252): `{"minecraft:despawn":{}}`
- `health_bar` (строки 23,226,239): `{"minecraft:boss":{"hud_range":16,"name":"§l§7Alpha Wolf","should_darken_sky":false}}`

### События

**`add_effects`** (строки 128,223):

- `$` — поля действия: `{"add":{"component_groups":["health_bar"]},"run_command":{"command":["effect @s resistance 20 2 true","effect @s regeneration 20 2 true"]}}`

**`clear_effects`** (строки 150,236):

- `$` — поля действия: `{"add":{"component_groups":["health_bar"]},"run_command":{"command":["effect @s resistance 0","effect @s regeneration 0"]}}`

**`despawn`** (строки 20,249,252):

- `$` — поля действия: `{"add":{"component_groups":["despawn"]},"run_command":{"command":["stopsound @a wolf_sword.distant_howl"]}}`

**`minecraft:entity_spawned`** (строки 261):

- `$` — поля действия: `{"run_command":{"command":["playsound wolf_sword.distant_howl @a[rm=25,r=100]"]}}`

**`minecraft:wolf_sword`** (строки 103,268):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0].randomize`: альтернативы, веса `[90,10]`, сумма 100:
    - ветвь 0, weight `90`; условная доля 9/10 (90%):
      - пустое действие
    - ветвь 1, weight `10`; условная доля 1/10 (10%):
      - `$.sequence[0].randomize[1]` — поля действия: `{"run_command":{"command":["structure load wolf_sword ~ ~ ~"]}}`

## `minecraft:arrow`

- Путь `Swords_B/entities/arrow.json`; format_version `"1.13.0"`.
- description: `{"identifier":"minecraft:arrow","is_spawnable":false,"is_summonable":true,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:collision_box` (строки 159): `{"width":0.25,"height":0.25}`
- `minecraft:hurt_on_condition` (строки 163): `{"damage_conditions":[{"filters":{"test":"in_lava","subject":"self","operator":"==","value":true},"cause":"lava","damage_per_tick":4}]}`
- `minecraft:projectile` (строки 19,47,78,104,133,172): `{"on_hit":{"impact_damage":{"damage":[1,4],"knockback":true,"semi_random_diff_damage":false,"destroy_on_hit":true},"stick_in_ground":{"shake_time":0.35},"arrow_effect":{}},"hit_sound":"bow.hit","power":1.6,"gravity":0.05,"uncertainty_base":16,"uncertainty_multiplier":4,"anchor":1,"should_bounce":true,"offset":[0,-0.1,0]}`
- `minecraft:physics` (строки 195): `{}`
- `minecraft:pushable` (строки 197): `{"is_pushable":false,"is_pushable_by_piston":true}`

### Группы компонентов

- `start_despawn_arrow` (строки 11,17,237): `{"minecraft:despawn":{}}`
- `despawn_arrow` (строки 14,220): `{"minecraft:type_family":{"family":["bone_sword_arrow","effect99_entities"]},"minecraft:timer":{"time":[1,1],"looping":false,"time_down_event":{"event":"start_despawn_arrow","target":"self"}},"minecraft:projectile":{"on_hit":{"remove_on_hit":{},"impact_damage":{"damage":[1,4],"knockback":true,"semi_random_diff_damage":false,"destroy_on_hit":true},"stick_in_ground":{"shake_time":0.35},"arrow_effect":{}},"hit_sound":"bow.hit","power":1.6,"gravity":0.05,"uncertainty_base":16,"uncertainty_multiplier":4,"anchor":1,"should_bounce":true,"offset":[0,-0.1,0]}}`
- `family:arrow` (строки 44,232,240): `{"minecraft:type_family":{"family":["arrow"]}}`
- `minecraft:inertia_disable` (строки 46,239,241): `{"minecraft:projectile":{"on_hit":{"impact_damage":{"damage":1,"knockback":true,"semi_random_diff_damage":true,"destroy_on_hit":true,"max_critical_damage":10,"min_critical_damage":9,"power_multiplier":0.97},"stick_in_ground":{"shake_time":0.35},"arrow_effect":{}},"hit_sound":"bow.hit","power":0,"gravity":1,"inertia":0,"liquid_inertia":0,"uncertainty_base":1,"uncertainty_multiplier":0,"anchor":1,"should_bounce":true,"offset":[0,-0.1,0]}}`
- `minecraft:hard_arrow` (строки 76,208,240): `{"minecraft:type_family":{"family":["arrow"]},"minecraft:projectile":{"on_hit":{"impact_damage":{"damage":[1,5],"knockback":true,"semi_random_diff_damage":false,"destroy_on_hit":true},"stick_in_ground":{"shake_time":0.35},"arrow_effect":{}},"hit_sound":"bow.hit","power":1.6,"gravity":0.05,"uncertainty_base":16,"uncertainty_multiplier":4,"anchor":1,"should_bounce":true,"offset":[0,-0.1,0]}}`
- `minecraft:player_arrow` (строки 102,214,240): `{"minecraft:type_family":{"family":["arrow"]},"minecraft:projectile":{"on_hit":{"impact_damage":{"damage":1,"knockback":true,"semi_random_diff_damage":true,"destroy_on_hit":true,"max_critical_damage":10,"min_critical_damage":9,"power_multiplier":0.97},"stick_in_ground":{"shake_time":0.35},"arrow_effect":{}},"hit_sound":"bow.hit","power":5.0,"gravity":0.05,"uncertainty_base":1,"uncertainty_multiplier":0,"anchor":1,"should_bounce":true,"offset":[0,-0.1,0]}}`
- `minecraft:pillager_arrow` (строки 131,226,240): `{"minecraft:type_family":{"family":["arrow"]},"minecraft:projectile":{"on_hit":{"impact_damage":{"damage":[3,6],"knockback":true,"semi_random_diff_damage":false,"destroy_on_hit":true},"stick_in_ground":{"shake_time":0.35},"arrow_effect":{}},"hit_sound":"bow.hit","power":1.6,"gravity":0.05,"uncertainty_base":16,"uncertainty_multiplier":4,"anchor":1,"should_bounce":true,"offset":[0,-0.1,0]}}`

### События

**`minecraft:entity_spawned`** (строки 203):

- `$.sequence`: 5 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_difficulty","value":"hard"},"add":{"component_groups":["minecraft:hard_arrow"]}}`
  - `$.sequence[1]` — поля действия: `{"filters":{"test":"is_family","subject":"other","value":"player"},"add":{"component_groups":["minecraft:player_arrow"]}}`
  - `$.sequence[2]` — поля действия: `{"filters":{"test":"has_equipment","subject":"other","domain":"hand","value":"effect:bone_sword"},"add":{"component_groups":["despawn_arrow"]}}`
  - `$.sequence[3]` — поля действия: `{"filters":{"test":"is_family","subject":"other","value":"pillager"},"add":{"component_groups":["minecraft:pillager_arrow"]}}`
  - `$.sequence[4]` — поля действия: `{"filters":{"test":"is_family","subject":"other","value":"skeleton"},"add":{"component_groups":["family:arrow"]}}`

**`start_despawn_arrow`** (строки 11,17,237):

- `$` — поля действия: `{"add":{"component_groups":["start_despawn_arrow"]}}`

**`minecraft:inertia_disable`** (строки 46,239,241):

- `$` — поля действия: `{"remove":{"component_groups":["minecraft:player_arrow","minecraft:pillager_arrow","minecraft:hard_arrow","family:arrow"]},"add":{"component_groups":["minecraft:inertia_disable"]}}`

## `minecraft:bee`

- Путь `Swords_B/entities/bee.json`; format_version `"1.18.20"`.
- description: `{"identifier":"minecraft:bee","is_spawnable":true,"is_summonable":true,"is_experimental":false,"properties":{"minecraft:has_nectar":{"type":"bool","client_sync":true,"default":"query.had_component_group('has_nectar')"}}}`.

### Постоянные компоненты

- `minecraft:is_hidden_when_invisible` (строки 390): `{}`
- `minecraft:behavior.tempt` (строки 392): `{"priority":5,"speed_multiplier":1.25,"within_radius":8,"can_tempt_vertically":true,"items":["minecraft:red_flower","minecraft:yellow_flower","minecraft:wither_rose","minecraft:double_plant:0","minecraft:double_plant:1","minecraft:double_plant:4","minecraft:double_plant:5","minecraft:flowering_azalea","minecraft:azalea_leaves_flowered","minecraft:mangrove_propagule"]}`
- `minecraft:behavior.move_towards_home_restriction` (строки 410): `{"priority":9}`
- `minecraft:behavior.random_hover` (строки 413): `{"priority":12,"xz_dist":8,"y_dist":8,"y_offset":-1,"interval":1,"hover_height":[1,4]}`
- `minecraft:leashable` (строки 421): `{"soft_distance":4.0,"hard_distance":6.0,"max_distance":10.0}`
- `minecraft:balloonable` (строки 426): `{"mass":0.5}`
- `minecraft:behavior.float` (строки 429): `{"priority":19}`
- `minecraft:type_family` (строки 144,432): `{"family":["bee","mob","arthropod"]}`
- `minecraft:on_target_acquired` (строки 435): `{"event":"attacked","target":"self"}`
- `minecraft:breathable` (строки 439): `{"totalSupply":15,"suffocateTime":0}`
- `minecraft:collision_box` (строки 443): `{"width":0.55,"height":0.5}`
- `minecraft:conditional_bandwidth_optimization` (строки 447): `{}`
- `minecraft:game_event_movement_tracking` (строки 449): `{"emit_flap":true}`
- `minecraft:home` (строки 452): `{"restriction_radius":22,"home_block_list":["minecraft:bee_nest","minecraft:beehive"]}`
- `minecraft:follow_range` (строки 459): `{"value":1024}`
- `minecraft:damage_sensor` (строки 462): `{"triggers":{"cause":"fall","deals_damage":false}}`
- `minecraft:hurt_on_condition` (строки 149,468): `{"damage_conditions":[{"filters":{"test":"in_lava","subject":"self","operator":"==","value":true},"cause":"lava","damage_per_tick":4}]}`
- `minecraft:movement` (строки 482): `{"value":0.3}`
- `minecraft:flying_speed` (строки 485): `{"value":0.15}`
- `minecraft:navigation.hover` (строки 488): `{"can_path_over_water":true,"can_sink":false,"can_pass_doors":false,"can_path_from_air":true,"avoid_water":true,"avoid_damage_blocks":true,"avoid_sun":false}`
- `minecraft:movement.hover` (строки 497): `{}`
- `minecraft:jump.static` (строки 498): `{}`
- `minecraft:can_fly` (строки 499): `{}`
- `minecraft:health` (строки 500): `{"value":10,"max":10}`
- `minecraft:nameable` (строки 504): `{}`
- `minecraft:block_sensor` (строки 505): `{"sensor_radius":16,"sources":[{"test":"has_silk_touch","subject":"other","value":false}],"on_break":[{"block_list":["minecraft:beehive","minecraft:bee_nest"],"on_block_broken":"hive_destroyed"}]}`
- `minecraft:physics` (строки 523): `{}`
- `minecraft:pushable` (строки 524): `{"is_pushable":true,"is_pushable_by_piston":true}`

### Группы компонентов

- `bee_baby` (строки 18,546,566,576): `{"minecraft:is_baby":{},"minecraft:scale":{"value":0.5},"minecraft:ageable":{"duration":1200,"feed_items":["minecraft:red_flower","minecraft:yellow_flower","minecraft:wither_rose","minecraft:double_plant:0","minecraft:double_plant:1","minecraft:double_plant:4","minecraft:double_plant:5","minecraft:flowering_azalea","minecraft:azalea_leaves_flowered","minecraft:mangrove_propagule"],"grow_up":{"event":"minecraft:ageable_grow_up","target":"self"}},"minecraft:behavior.follow_parent":{"priority":11,"speed_multiplier":1.1}}`
- `bee_adult` (строки 47,538,581): `{"minecraft:experience_reward":{"on_bred":"Math.Random(1,7)","on_death":"query.last_hit_by_player ? Math.Random(1,3) : 0"},"minecraft:behavior.breed":{"priority":4,"speed_multiplier":1.0},"minecraft:breedable":{"require_tame":false,"breeds_with":{"mate_type":"minecraft:bee","baby_type":"minecraft:bee","breed_event":{"event":"minecraft:entity_born","target":"baby"}},"breed_items":["minecraft:red_flower","minecraft:yellow_flower","minecraft:wither_rose","minecraft:double_plant:0","minecraft:double_plant:1","minecraft:double_plant:4","minecraft:double_plant:5","minecraft:flowering_azalea","minecraft:azalea_leaves_flowered","minecraft:mangrove_propagule"]}}`
- `track_attacker` (строки 80,555,568,860): `{"minecraft:behavior.hurt_by_target":{"priority":1}}`
- `angry_bee` (строки 85,678,725,863): `{"minecraft:angry":{"duration":25,"broadcastAnger":true,"broadcastRange":20,"broadcast_filters":{"test":"is_family","operator":"!=","value":"pacified"},"calm_event":{"event":"calmed_down","target":"self"}},"minecraft:behavior.melee_attack":{"priority":2,"attack_once":true,"speed_multiplier":1.4,"on_attack":{"event":"countdown_to_perish_event","target":"self"}}}`
- `escape_fire` (строки 110,598,621,630,637,771,831,866): `{"minecraft:behavior.panic":{"priority":1,"speed_multiplier":1.25,"force":true},"minecraft:timer":{"looping":false,"time":[20,50],"randomInterval":true,"time_down_event":{"event":"stop_panicking_after_fire","target":"self"}}}`
- `countdown_to_perish` (строки 126,871): `{"minecraft:mark_variant":{"value":1},"minecraft:behavior.panic":{"priority":1,"speed_multiplier":1.25,"force":true},"minecraft:timer":{"looping":false,"time":[10,60],"randomInterval":true,"time_down_event":{"event":"perish_event","target":"self"}},"minecraft:type_family":{"family":["bee","mob","arthropod","pacified"]}}`
- `perish` (строки 148,880): `{"minecraft:hurt_on_condition":{"damage_conditions":[{"cause":"none","damage_per_tick":999}]}}`
- `take_nearest_target` (строки 158,588,616,683,726,861): `{"minecraft:behavior.nearest_attackable_target":{"priority":2,"entity_types":[{"filters":{"test":"is_family","subject":"other","value":"player"},"max_dist":10}]},"minecraft:timer":{"looping":true,"time":5,"time_down_event":{"event":"calmed_down","target":"self"}}}`
- `look_for_food` (строки 181,557,569,644,733,776,801,813,837,862): `{"minecraft:behavior.move_to_block":{"priority":10,"tick_interval":1,"start_chance":0.5,"search_range":6,"search_height":4,"goal_radius":1.0,"stay_duration":20.0,"target_selection_method":"random","target_offset":[0,0.25,0],"target_block_filters":{"test":"is_waterlogged","subject":"block","operator":"==","value":false},"target_blocks":["minecraft:red_flower","minecraft:yellow_flower","minecraft:wither_rose","minecraft:double_plant:8","minecraft:double_plant:9","minecraft:double_plant:12","minecraft:double_plant:13","minecraft:flowering_azalea","minecraft:azalea_leaves_flowered","minecraft:mangrove_propagule"],"on_stay_completed":[{"event":"collected_nectar","target":"self"}]},"minecraft:timer":{"looping":true,"time":180,"time_down_event":{"event":"find_flower_timeout"}},"minecraft:ambient_sound_interval":{"event_name":"ambient.pollinate","range":3.0,"value":2.0}}`
- `has_nectar` (строки 225,595,652,739): `{"minecraft:grows_crop":{"charges":10,"chance":0.03}}`
- `return_to_home` (строки 231,594,651,669,720,738,750,792,806,821,830): `{"minecraft:behavior.go_home":{"priority":4,"speed_multiplier":1.0,"interval":1,"goal_radius":1.2,"on_home":[{"filters":{"any_of":[{"test":"is_block","subject":"block","value":"minecraft:bee_nest"},{"test":"is_block","subject":"block","value":"minecraft:beehive"}]},"event":"minecraft:bee_returned_to_hive","target":"block"},{"filters":{"all_of":[{"test":"is_block","subject":"block","operator":"!=","value":"minecraft:bee_nest"},{"test":"is_block","subject":"block","operator":"!=","value":"minecraft:beehive"}]},"event":"find_hive_event","target":"self"}],"on_failed":[{"event":"find_hive_event","target":"self"}]}}`
- `find_hive` (строки 267,593,650,668,756,770,787,865): `{"minecraft:behavior.move_to_block":{"priority":10,"search_range":16,"search_height":10,"tick_interval":1,"goal_radius":0.633,"target_blocks":["bee_nest","beehive"],"on_reach":[{"event":"minecraft:bee_returned_to_hive","target":"block"}]},"minecraft:timer":{"looping":false,"time":180,"time_down_event":{"event":"find_hive_timeout","target":"self"}}}`
- `hive_full` (строки 294,663,751,864): `{"minecraft:timer":{"looping":false,"time":[5,20],"randomInterval":true,"time_down_event":{"event":"find_hive_event","target":"self"}}}`
- `shelter_detection` (строки 305,556,567,597,645,719,815,836): `{"minecraft:environment_sensor":{"triggers":[{"event":"seek_shelter","filters":{"all_of":[{"any_of":[{"test":"is_daytime","value":false},{"test":"weather","operator":"==","value":"precipitation"}]},{"test":"bool_property","domain":"minecraft:has_nectar","operator":"!="},{"test":"has_biome_tag","value":"overworld"}]}}]}}`
- `abort_shelter_detection` (строки 340,596,653,822,829): `{"minecraft:environment_sensor":{"triggers":[{"event":"abort_sheltering","filters":{"all_of":[{"test":"weather","operator":"==","value":"clear"},{"test":"is_daytime","value":true}]}}]}}`
- `easy_attack` (строки 362,693,699,708): `{"minecraft:attack":{"damage":2}}`
- `normal_attack` (строки 367,690,702,708): `{"minecraft:attack":{"damage":2,"effect_name":"poison","effect_duration":10}}`
- `hard_attack` (строки 374,690,699,711): `{"minecraft:attack":{"damage":2,"effect_name":"poison","effect_duration":18}}`
- `default_sound` (строки 381,740,820): `{"minecraft:ambient_sound_interval":{"event_name":"ambient","range":0.0,"value":0.0}}`

### События

**`minecraft:entity_spawned`** (строки 530):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0].randomize`: альтернативы, веса `[95,5]`, сумма 100:
    - ветвь 0, weight `95`; условная доля 19/20 (95%):
      - `$.sequence[0].randomize[0]` — поля действия: `{"add":{"component_groups":["bee_adult"]}}`
    - ветвь 1, weight `5`; условная доля 1/20 (5%):
      - `$.sequence[0].randomize[1]` — поля действия: `{"add":{"component_groups":["bee_baby"]}}`
  - `$.sequence[1]` — поля действия: `{"add":{"component_groups":["track_attacker","shelter_detection","look_for_food"]}}`

**`minecraft:entity_born`** (строки 62,563):

- `$` — поля действия: `{"add":{"component_groups":["bee_baby","shelter_detection","track_attacker","look_for_food"]}}`

**`minecraft:ageable_grow_up`** (строки 38,573):

- `$` — поля действия: `{"remove":{"component_groups":["bee_baby"]},"add":{"component_groups":["bee_adult"]}}`

**`minecraft:exited_disturbed_hive`** (строки 585):

- `$` — поля действия: `{"add":{"component_groups":["take_nearest_target"]},"remove":{"component_groups":["find_hive","return_to_home","has_nectar","abort_shelter_detection","shelter_detection","escape_fire"]},"set_property":{"minecraft:has_nectar":false}}`

**`hive_destroyed`** (строки 519,605):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"pacified"},"add":{"component_groups":["take_nearest_target"]},"remove":{"component_groups":["escape_fire"]}}`

**`stop_panicking_after_fire`** (строки 121,627):

- `$` — поля действия: `{"remove":{"component_groups":["escape_fire"]}}`

**`minecraft:exited_hive_on_fire`** (строки 634):

- `$` — поля действия: `{"add":{"component_groups":["escape_fire"]}}`

**`minecraft:exited_hive`** (строки 641):

- `$` — поля действия: `{"add":{"component_groups":["look_for_food","shelter_detection"]},"remove":{"component_groups":["find_hive","return_to_home","has_nectar","abort_shelter_detection"]},"set_property":{"minecraft:has_nectar":false}}`

**`minecraft:hive_full`** (строки 660):

- `$` — поля действия: `{"add":{"component_groups":["hive_full"]},"remove":{"component_groups":["find_hive","return_to_home"]}}`

**`attacked`** (строки 436,673):

- `$.sequence`: 4 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"add":{"component_groups":["angry_bee"]},"remove":{"component_groups":["take_nearest_target"]}}`
  - `$.sequence[1]` — поля действия: `{"filters":{"test":"is_difficulty","value":"easy"},"remove":{"component_groups":["normal_attack","hard_attack"]},"add":{"component_groups":["easy_attack"]}}`
  - `$.sequence[2]` — поля действия: `{"filters":{"test":"is_difficulty","value":"normal"},"remove":{"component_groups":["easy_attack","hard_attack"]},"add":{"component_groups":["normal_attack"]}}`
  - `$.sequence[3]` — поля действия: `{"filters":{"test":"is_difficulty","value":"hard"},"remove":{"component_groups":["easy_attack","normal_attack"]},"add":{"component_groups":["hard_attack"]}}`

**`calmed_down`** (строки 96,176,716):

- `$` — поля действия: `{"add":{"component_groups":["shelter_detection","return_to_home"]},"remove":{"component_groups":["angry_bee","take_nearest_target"]}}`

**`collected_nectar`** (строки 207,730):

- `$` — поля действия: `{"remove":{"component_groups":["look_for_food"]},"add":{"component_groups":["return_to_home","has_nectar","default_sound"]},"set_property":{"minecraft:has_nectar":true}}`

**`find_hive_event`** (строки 255,261,300,747):

- `$` — поля действия: `{"remove":{"component_groups":["return_to_home","hive_full"]},"add":{"component_groups":["find_hive"]}}`

**`find_hive_timeout`** (строки 289,760):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"bool_property","operator":"!=","domain":"minecraft:has_nectar"},"remove":{"component_groups":["find_hive","escape_fire"]},"add":{"component_groups":["look_for_food"]}}`
  - `$.sequence[1]` — поля действия: `{"filters":{"test":"bool_property","domain":"minecraft:has_nectar"},"remove":{"component_groups":["find_hive"]},"add":{"component_groups":["return_to_home"]}}`

**`find_flower_timeout`** (строки 216,798):

- `$` — поля действия: `{"remove":{"component_groups":["look_for_food"]},"add":{"component_groups":["return_to_home"]}}`

**`seek_shelter`** (строки 309,810):

- `$` — поля действия: `{"remove":{"component_groups":["look_for_food","collect_nectar","shelter_detection"]},"add":{"component_groups":["default_sound","return_to_home","abort_shelter_detection"]}}`

**`abort_sheltering`** (строки 344,826):

- `$` — поля действия: `{"remove":{"component_groups":["abort_shelter_detection","return_to_home","escape_fire"]},"add":{"component_groups":["shelter_detection","look_for_food"]}}`

**`countdown_to_perish_event`** (строки 105,842):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0].randomize`: альтернативы, веса `[2,98]`, сумма 100:
    - ветвь 0, weight `2`; условная доля 1/50 (2%):
      - `$.sequence[0].randomize[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"bee_sword"},"run_command":{"command":["loot spawn ~ ~ ~ loot bee_sword"]}}`
    - ветвь 1, weight `98`; условная доля 49/50 (98%):
      - пустое действие
  - `$.sequence[1]` — поля действия: `{"remove":{"component_groups":["collect_nectar","track_attacker","take_nearest_target","look_for_food","angry_bee","hive_full","find_hive","escape_fire"]},"add":{"component_groups":["countdown_to_perish"]}}`

**`perish_event`** (строки 140,877):

- `$` — поля действия: `{"add":{"component_groups":["perish"]}}`

## `entity:bee_sword`

- Путь `Swords_B/entities/bee_entity.json`; format_version `"1.16.100"`.
- description: `{"identifier":"entity:bee_sword","is_spawnable":false,"is_summonable":true,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:timer` (строки 16): `{"looping":true,"time":[6,8],"randomInterval":true,"time_down_event":{"event":"despawn","target":"self"}}`
- `minecraft:damage_sensor` (строки 25): `{"triggers":[{"deals_damage":false,"on_damage":{"filters":{"test":"is_family","subject":"other","value":"player"}}},{"cause":"fall","deals_damage":false}]}`
- `minecraft:scale` (строки 39): `{"value":0.5}`
- `minecraft:behavior.melee_attack` (строки 42): `{"priority":1,"speed_multiplier":1.4,"track_target":true}`
- `minecraft:type_family` (строки 47): `{"family":["bee","mob","arthropod"]}`
- `minecraft:angry` (строки 50): `{"duration":99999,"broadcastAnger":true,"broadcastRange":20,"broadcast_filters":{},"calm_event":{}}`
- `minecraft:behavior.nearest_attackable_target` (строки 57): `{"priority":1,"within_radius":16,"entity_types":[{"filters":{"test":"is_family","subject":"other","value":"monster"},"max_dist":10}],"must_see":true}`
- `minecraft:attack` (строки 72): `{"damage":1,"effect_name":"fatal_poison","effect_duration":3}`
- `minecraft:is_hidden_when_invisible` (строки 77): `{}`
- `minecraft:behavior.move_towards_home_restriction` (строки 78): `{"priority":9}`
- `minecraft:behavior.random_hover` (строки 81): `{"priority":12,"xz_dist":8,"y_dist":8,"y_offset":-1,"interval":1,"hover_height":[1,4]}`
- `minecraft:leashable` (строки 89): `{"soft_distance":4,"hard_distance":6,"max_distance":10}`
- `minecraft:behavior.float` (строки 94): `{"priority":19}`
- `minecraft:breathable` (строки 97): `{"totalSupply":15,"suffocateTime":0}`
- `minecraft:collision_box` (строки 101): `{"width":0.55,"height":0.5}`
- `minecraft:conditional_bandwidth_optimization` (строки 105): `{}`
- `minecraft:follow_range` (строки 106): `{"value":1024}`
- `minecraft:hurt_on_condition` (строки 109): `{"damage_conditions":[{"filters":{"test":"in_lava","subject":"self","operator":"==","value":true},"cause":"lava","damage_per_tick":4}]}`
- `minecraft:movement` (строки 123): `{"value":0.3}`
- `minecraft:flying_speed` (строки 126): `{"value":0.15}`
- `minecraft:navigation.hover` (строки 129): `{"can_path_over_water":true,"can_sink":false,"can_pass_doors":false,"can_path_from_air":true,"avoid_water":true,"avoid_damage_blocks":true,"avoid_sun":false}`
- `minecraft:movement.hover` (строки 138): `{}`
- `minecraft:jump.static` (строки 139): `{}`
- `minecraft:can_fly` (строки 140): `{}`
- `minecraft:health` (строки 141): `{"value":10,"max":10}`
- `minecraft:nameable` (строки 145): `{}`
- `minecraft:physics` (строки 146): `{}`
- `minecraft:pushable` (строки 147): `{"is_pushable":true,"is_pushable_by_piston":true}`

### Группы компонентов

- `despawn` (строки 11,21,153): `{"minecraft:despawn":{}}`

### События

**`despawn`** (строки 11,21,153):

- `$` — поля действия: `{"run_command":{"command":["tp @s ~ -103 ~"]}}`

## `minecraft:blaze`

- Путь `Swords_B/entities/blaze.json`; format_version `"1.13.0"`.
- description: `{"identifier":"minecraft:blaze","is_spawnable":true,"is_summonable":true,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:experience_reward` (строки 11): `{"on_death":"query.last_hit_by_player ? 10 : 0"}`
- `minecraft:loot` (строки 14): `{"table":"loot_tables/entities/blaze.json"}`
- `minecraft:collision_box` (строки 17): `{"width":0.5,"height":1.8}`
- `minecraft:attack` (строки 21): `{"damage":6}`
- `minecraft:damage_sensor` (строки 24): `{"triggers":[{"cause":"fall","deals_damage":false}]}`
- `minecraft:movement` (строки 32): `{"value":0.23}`
- `minecraft:navigation.walk` (строки 35): `{"can_path_over_water":true}`
- `minecraft:movement.basic` (строки 38): `{}`
- `minecraft:jump.static` (строки 41): `{}`
- `minecraft:can_climb` (строки 43): `{}`
- `minecraft:can_fly` (строки 45): `{}`
- `minecraft:health` (строки 47): `{"value":20,"max":20}`
- `minecraft:hurt_on_condition` (строки 51): `{"damage_conditions":[{"filters":{"test":"in_water_or_rain","operator":"==","value":true},"cause":"drowning","damage_per_tick":1}]}`
- `minecraft:follow_range` (строки 60): `{"value":48,"max":48}`
- `minecraft:fire_immune` (строки 64): `true`
- `minecraft:nameable` (строки 65): `{}`
- `minecraft:behavior.float` (строки 68): `{"priority":0}`
- `minecraft:behavior.hurt_by_target` (строки 71): `{"priority":1}`
- `minecraft:behavior.nearest_attackable_target` (строки 74): `{"priority":2,"entity_types":[{"filters":{"test":"is_family","subject":"other","value":"player"},"max_dist":48}],"must_see":true}`
- `minecraft:behavior.melee_attack` (строки 88): `{"priority":3,"max_dist":3,"speed_multiplier":1,"random_stop_interval":2.0,"track_target":true}`
- `minecraft:shooter` (строки 95): `{"type":"smallfireball","def":"minecraft:small_fireball"}`
- `minecraft:behavior.ranged_attack` (строки 99): `{"priority":4,"attack_interval_min":3,"attack_interval_max":5,"charge_charged_trigger":0.0,"charge_shoot_trigger":4.0,"attack_radius":16,"burst_shots":3,"burst_interval":0.3}`
- `minecraft:behavior.random_stroll` (строки 109): `{"priority":5,"speed_multiplier":1.0}`
- `minecraft:behavior.random_look_around` (строки 113): `{"priority":6}`
- `minecraft:type_family` (строки 116): `{"family":["blaze","monster","mob"]}`
- `minecraft:physics` (строки 119): `{}`
- `minecraft:pushable` (строки 121): `{"is_pushable":true,"is_pushable_by_piston":true}`

### Группы компонентов


### События

**`blaze_sword`** (строки 127):

- `$.randomize`: альтернативы, веса `[995,5]`, сумма 1000:
  - ветвь 0, weight `995`; условная доля 199/200 (99.5%):
    - пустое действие
  - ветвь 1, weight `5`; условная доля 1/200 (0.5%):
    - `$.randomize[1]` — поля действия: `{"run_command":{"command":["structure load blaze_sword ~ ~ ~"]}}`

## `minecraft:cat`

- Путь `Swords_B/entities/cat.json`; format_version `"1.13.0"`.
- description: `{"identifier":"minecraft:cat","is_spawnable":true,"is_summonable":true,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:attack_damage` (строки 281): `{"value":4}`
- `minecraft:nameable` (строки 284): `{}`
- `minecraft:type_family` (строки 142,286): `{"family":["cat","mob"]}`
- `minecraft:breathable` (строки 289): `{"total_supply":15,"suffocate_time":0}`
- `minecraft:collision_box` (строки 293): `{"width":0.6,"height":0.7}`
- `minecraft:healable` (строки 297): `{"items":[{"item":"fish","heal_amount":2},{"item":"salmon","heal_amount":2}]}`
- `minecraft:hurt_on_condition` (строки 309): `{"damage_conditions":[{"filters":{"test":"in_lava","subject":"self","operator":"==","value":true},"cause":"lava","damage_per_tick":4}]}`
- `minecraft:movement` (строки 318): `{"value":0.3}`
- `minecraft:navigation.walk` (строки 321): `{"can_float":true,"avoid_water":true,"avoid_damage_blocks":true}`
- `minecraft:movement.basic` (строки 326): `{}`
- `minecraft:jump.static` (строки 328): `{}`
- `minecraft:can_climb` (строки 330): `{}`
- `minecraft:damage_sensor` (строки 332): `{"triggers":{"cause":"fall","deals_damage":false}}`
- `minecraft:dweller` (строки 338): `{"dwelling_type":"village","dweller_role":"passive","update_interval_base":60,"update_interval_variant":40,"can_find_poi":false,"can_migrate":true,"first_founding_reward":0}`
- `minecraft:behavior.float` (строки 347): `{"priority":0}`
- `minecraft:behavior.panic` (строки 350): `{"priority":1,"speed_multiplier":1.25}`
- `minecraft:behavior.mount_pathing` (строки 354): `{"priority":1,"speed_multiplier":1.25,"target_dist":0,"track_target":true}`
- `minecraft:behavior.leap_at_target` (строки 360): `{"priority":3,"target_dist":0.3}`
- `minecraft:behavior.ocelotattack` (строки 364): `{"priority":4,"walk_speed_multiplier":0.8,"sprint_speed_multiplier":1.33,"sneak_speed_multiplier":0.6}`
- `minecraft:behavior.random_stroll` (строки 370): `{"priority":8,"speed_multiplier":0.8}`
- `minecraft:behavior.look_at_player` (строки 374): `{"priority":9}`
- `minecraft:physics` (строки 377): `{}`
- `minecraft:pushable` (строки 379): `{"is_pushable":true,"is_pushable_by_piston":true}`

### Группы компонентов

- `minecraft:cat_baby` (строки 11,407,530,650,661): `{"minecraft:is_baby":{},"minecraft:scale":{"value":0.4},"minecraft:ageable":{"duration":1200,"feed_items":["fish","salmon"],"grow_up":{"event":"minecraft:ageable_grow_up","target":"self"}}}`
- `minecraft:cat_adult` (строки 27,396,519,629,666): `{"minecraft:experience_reward":{"on_bred":"Math.Random(1,7)","on_death":"query.last_hit_by_player ? Math.Random(1,3) : 0"},"minecraft:loot":{"table":"loot_tables/entities/cat.json"},"minecraft:scale":{"value":0.8},"minecraft:behavior.breed":{"priority":3,"speed_multiplier":1.0},"minecraft:breedable":{"require_tame":true,"allow_sitting":true,"breeds_with":{"mate_type":"minecraft:cat","baby_type":"minecraft:cat","breed_event":{"event":"minecraft:entity_born","target":"baby"}},"breed_items":["fish","salmon"]}}`
- `minecraft:cat_wild` (строки 56,397,408,520,531,630,675): `{"minecraft:health":{"value":10,"max":10},"minecraft:tameable":{"probability":0.33,"tame_items":["fish","salmon"],"tame_event":{"event":"minecraft:on_tame","target":"self"}},"minecraft:rideable":{"seat_count":1,"family_types":["zombie"],"seats":{"position":[0.0,0.35,0.0]}},"minecraft:behavior.nearest_attackable_target":{"priority":1,"attack_interval":10,"reselect_targets":true,"within_radius":16.0,"entity_types":[{"filters":{"test":"is_family","subject":"other","value":"rabbit"},"max_dist":8},{"filters":{"all_of":[{"test":"is_family","subject":"other","value":"baby_turtle"},{"test":"in_water","subject":"other","operator":"!=","value":true}]},"max_dist":8}]},"minecraft:behavior.tempt":{"priority":5,"speed_multiplier":0.5,"within_radius":16,"can_get_scared":true,"items":["fish","salmon"]},"minecraft:behavior.avoid_mob_type":{"priority":6,"entity_types":[{"filters":{"test":"is_family","subject":"other","value":"player"},"max_dist":10,"walk_speed_multiplier":0.8,"sprint_speed_multiplier":1.33}]},"minecraft:behavior.move_towards_restriction":{"priority":7}}`
- `minecraft:cat_tame` (строки 141,651,682): `{"minecraft:type_family":{"family":["cat","mob","tamed"]},"minecraft:is_tamed":{},"minecraft:health":{"value":20,"max":20},"minecraft:color":{"value":14},"minecraft:sittable":{},"minecraft:behavior.tempt":{"priority":5,"speed_multiplier":0.5,"within_radius":16,"items":["fish","salmon"]},"minecraft:is_dyeable":{"interact_text":"action.interact.dye"},"minecraft:leashable":{"soft_distance":4.0,"hard_distance":6.0,"max_distance":10.0},"minecraft:behavior.follow_owner":{"priority":4,"speed_multiplier":1.0,"start_distance":10,"stop_distance":2},"minecraft:behavior.stay_while_sitting":{"priority":3},"minecraft:behavior.ocelot_sit_on_block":{"priority":7,"speed_multiplier":1.0},"minecraft:behavior.pet_sleep_with_owner":{"priority":2,"speed_multiplier":1.2,"search_radius":10,"search_height":10,"goal_radius":1.0},"minecraft:on_wake_with_owner":{"event":"minecraft:pet_slept_with_owner","target":"self"}}`
- `minecraft:cat_gift_for_owner` (строки 198,691,698): `{"minecraft:behavior.drop_item_for":{"priority":1,"speed_multiplier":1.0,"search_range":5,"search_height":2,"search_count":0,"goal_radius":1.0,"entity_types":[{"filters":{"test":"is_family","subject":"other","value":"player"},"max_dist":6}],"max_dist":5,"drop_item_chance":0.7,"offering_distance":5,"loot_table":"loot_tables/entities/cat_gift.json","time_of_day_range":[0.74999,0.8],"on_drop_attempt":{"event":"minecraft:cat_gifted_owner","target":"self"}}}`
- `minecraft:cat_white` (строки 223,420,567): `{"minecraft:variant":{"value":0}}`
- `minecraft:cat_tuxedo` (строки 228,428,543): `{"minecraft:variant":{"value":1}}`
- `minecraft:cat_red` (строки 233,436,551): `{"minecraft:variant":{"value":2}}`
- `minecraft:cat_siamese` (строки 238,444,559): `{"minecraft:variant":{"value":3}}`
- `minecraft:cat_british` (строки 243,452,575): `{"minecraft:variant":{"value":4}}`
- `minecraft:cat_calico` (строки 248,460,583): `{"minecraft:variant":{"value":5}}`
- `minecraft:cat_persian` (строки 253,468,591): `{"minecraft:variant":{"value":6}}`
- `minecraft:cat_ragdoll` (строки 258,476,599): `{"minecraft:variant":{"value":7}}`
- `minecraft:cat_tabby` (строки 263,484,607): `{"minecraft:variant":{"value":8}}`
- `minecraft:cat_black` (строки 268,492,631): `{"minecraft:variant":{"value":9}}`
- `minecraft:cat_jellie` (строки 273,500,615): `{"minecraft:variant":{"value":10}}`

### События

**`minecraft:entity_spawned`** (строки 386):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0].randomize`: альтернативы, веса `[3,1]`, сумма 4:
    - ветвь 0, weight `3`; условная доля 3/4 (75%):
      - `$.sequence[0].randomize[0]` — поля действия: `{"remove":{},"add":{"component_groups":["minecraft:cat_adult","minecraft:cat_wild"]}}`
    - ветвь 1, weight `1`; условная доля 1/4 (25%):
      - `$.sequence[0].randomize[1]` — поля действия: `{"remove":{},"add":{"component_groups":["minecraft:cat_baby","minecraft:cat_wild"]}}`
  - `$.sequence[1].randomize`: альтернативы, веса `[15,15,15,15,15,15,15,15,15,15,15]`, сумма 165:
    - ветвь 0, weight `15`; условная доля 1/11 (9.09091%):
      - `$.sequence[1].randomize[0]` — поля действия: `{"add":{"component_groups":["minecraft:cat_white"]}}`
    - ветвь 1, weight `15`; условная доля 1/11 (9.09091%):
      - `$.sequence[1].randomize[1]` — поля действия: `{"add":{"component_groups":["minecraft:cat_tuxedo"]}}`
    - ветвь 2, weight `15`; условная доля 1/11 (9.09091%):
      - `$.sequence[1].randomize[2]` — поля действия: `{"add":{"component_groups":["minecraft:cat_red"]}}`
    - ветвь 3, weight `15`; условная доля 1/11 (9.09091%):
      - `$.sequence[1].randomize[3]` — поля действия: `{"add":{"component_groups":["minecraft:cat_siamese"]}}`
    - ветвь 4, weight `15`; условная доля 1/11 (9.09091%):
      - `$.sequence[1].randomize[4]` — поля действия: `{"add":{"component_groups":["minecraft:cat_british"]}}`
    - ветвь 5, weight `15`; условная доля 1/11 (9.09091%):
      - `$.sequence[1].randomize[5]` — поля действия: `{"add":{"component_groups":["minecraft:cat_calico"]}}`
    - ветвь 6, weight `15`; условная доля 1/11 (9.09091%):
      - `$.sequence[1].randomize[6]` — поля действия: `{"add":{"component_groups":["minecraft:cat_persian"]}}`
    - ветвь 7, weight `15`; условная доля 1/11 (9.09091%):
      - `$.sequence[1].randomize[7]` — поля действия: `{"add":{"component_groups":["minecraft:cat_ragdoll"]}}`
    - ветвь 8, weight `15`; условная доля 1/11 (9.09091%):
      - `$.sequence[1].randomize[8]` — поля действия: `{"add":{"component_groups":["minecraft:cat_tabby"]}}`
    - ветвь 9, weight `15`; условная доля 1/11 (9.09091%):
      - `$.sequence[1].randomize[9]` — поля действия: `{"add":{"component_groups":["minecraft:cat_black"]}}`
    - ветвь 10, weight `15`; условная доля 1/11 (9.09091%):
      - `$.sequence[1].randomize[10]` — поля действия: `{"add":{"component_groups":["minecraft:cat_jellie"]}}`

**`minecraft:spawn_from_village`** (строки 509):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0].randomize`: альтернативы, веса `[3,1]`, сумма 4:
    - ветвь 0, weight `3`; условная доля 3/4 (75%):
      - `$.sequence[0].randomize[0]` — поля действия: `{"remove":{},"add":{"component_groups":["minecraft:cat_adult","minecraft:cat_wild"]}}`
    - ветвь 1, weight `1`; условная доля 1/4 (25%):
      - `$.sequence[0].randomize[1]` — поля действия: `{"remove":{},"add":{"component_groups":["minecraft:cat_baby","minecraft:cat_wild"]}}`
  - `$.sequence[1].randomize`: альтернативы, веса `[15,15,15,15,15,15,15,15,15,15]`, сумма 150:
    - ветвь 0, weight `15`; условная доля 1/10 (10%):
      - `$.sequence[1].randomize[0]` — поля действия: `{"add":{"component_groups":["minecraft:cat_tuxedo"]}}`
    - ветвь 1, weight `15`; условная доля 1/10 (10%):
      - `$.sequence[1].randomize[1]` — поля действия: `{"add":{"component_groups":["minecraft:cat_red"]}}`
    - ветвь 2, weight `15`; условная доля 1/10 (10%):
      - `$.sequence[1].randomize[2]` — поля действия: `{"add":{"component_groups":["minecraft:cat_siamese"]}}`
    - ветвь 3, weight `15`; условная доля 1/10 (10%):
      - `$.sequence[1].randomize[3]` — поля действия: `{"add":{"component_groups":["minecraft:cat_white"]}}`
    - ветвь 4, weight `15`; условная доля 1/10 (10%):
      - `$.sequence[1].randomize[4]` — поля действия: `{"add":{"component_groups":["minecraft:cat_british"]}}`
    - ветвь 5, weight `15`; условная доля 1/10 (10%):
      - `$.sequence[1].randomize[5]` — поля действия: `{"add":{"component_groups":["minecraft:cat_calico"]}}`
    - ветвь 6, weight `15`; условная доля 1/10 (10%):
      - `$.sequence[1].randomize[6]` — поля действия: `{"add":{"component_groups":["minecraft:cat_persian"]}}`
    - ветвь 7, weight `15`; условная доля 1/10 (10%):
      - `$.sequence[1].randomize[7]` — поля действия: `{"add":{"component_groups":["minecraft:cat_ragdoll"]}}`
    - ветвь 8, weight `15`; условная доля 1/10 (10%):
      - `$.sequence[1].randomize[8]` — поля действия: `{"add":{"component_groups":["minecraft:cat_tabby"]}}`
    - ветвь 9, weight `15`; условная доля 1/10 (10%):
      - `$.sequence[1].randomize[9]` — поля действия: `{"add":{"component_groups":["minecraft:cat_jellie"]}}`

**`minecraft:spawn_midnight_cat`** (строки 624):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"add":{"component_groups":["minecraft:cat_adult","minecraft:cat_wild","minecraft:cat_black"]}}`

**`minecraft:entity_born`** (строки 49,638):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"has_component","operator":"!=","value":"minecraft:is_baby"},"remove":{},"add":{"component_groups":["minecraft:cat_baby","minecraft:cat_tame"]}}`

**`minecraft:ageable_grow_up`** (строки 21,658):

- `$` — поля действия: `{"remove":{"component_groups":["minecraft:cat_baby"]},"add":{"component_groups":["minecraft:cat_adult"]}}`

**`minecraft:on_tame`** (строки 65,670):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"remove":{"component_groups":["minecraft:cat_wild"]}}`
  - `$.sequence[1]` — поля действия: `{"add":{"component_groups":["minecraft:cat_tame"]}}`

**`minecraft:pet_slept_with_owner`** (строки 194,688):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:cat_gift_for_owner"]}}`

**`minecraft:cat_gifted_owner`** (строки 218,695):

- `$` — поля действия: `{"remove":{"component_groups":["minecraft:cat_gift_for_owner"]}}`

## `entity:centella`

- Путь `Swords_B/entities/centella.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:centella","is_spawnable":false,"is_summonable":true,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 16): `{"family":["effect99_entities","centella","spherical_lightning"]}`
- `minecraft:on_death` (строки 18): `{"event":"minecraft:start_death","target":"self"}`
- `minecraft:damage_sensor` (строки 21): `{"triggers":[{"on_damage":{"filters":{"all_of":[{"test":"has_damage","value":"fatal"},{"test":"is_family","subject":"other","value":"player"}]},"event":"centella_death_by_player"},"deals_damage":true},{"on_damage":{"filters":{"all_of":[{"test":"has_damage","value":"fatal"}]},"event":"centella_death"},"deals_damage":true}]}`
- `minecraft:movement` (строки 39): `{"value":0.22}`
- `minecraft:loot` (строки 42): `{"table":"loot_tables/entity/centella.json"}`
- `minecraft:navigation.walk` (строки 45): `{"can_path_over_water":false,"can_path_over_lava":true,"can_walk_in_lava":true,"can_jump":false,"avoid_water":true,"avoid_damage_blocks":false}`
- `minecraft:movement.basic` (строки 53): `{}`
- `minecraft:jump.static` (строки 55): `{}`
- `minecraft:can_climb` (строки 57): `{}`
- `minecraft:behavior.random_stroll` (строки 59): `{"priority":1,"speed_multiplier":0.7}`
- `minecraft:behavior.float` (строки 63): `{"priority":1}`
- `minecraft:timer` (строки 66): `{"time":[10,60],"looping":true,"randomInterval":true,"time_down_event":{"event":"minecraft:start_death","target":"self"}}`
- `minecraft:health` (строки 68): `{"value":200}`
- `minecraft:collision_box` (строки 69): `{"width":0.8,"height":1.5}`
- `minecraft:fire_immune` (строки 70): `true`
- `minecraft:physics` (строки 71): `{}`
- `minecraft:environment_sensor` (строки 72): `[{"on_environment":{"filters":{"test":"is_family","value":"centella"},"event":"minecraft:centella"}}]`

### Группы компонентов

- `despawn` (строки 11,93): `{"minecraft:despawn":{}}`

### События

**`minecraft:entity_spawned`** (строки 75):


**`minecraft:centella`** (строки 72,77):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"run_command":{"command":["particle minecraft:example_directional_sphere ~ ~1.3 ~","effect @e[family=!effect99_entities,r=2] instant_damage 1 0 true","effect @s slow_falling 10 0 true","playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3","fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock 0 replace air","fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock 0 replace effect99:lightblock"]}}`

**`minecraft:start_death`** (строки 19,66,92):

- `$` — поля действия: `{"add":{"component_groups":["despawn"]}}`

**`centella_death_by_player`** (строки 27,95):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"run_command":{"command":["summon lightning_bolt ~~~ default_lightning_bolt","say 1"]}}`
  - `$.sequence[1].randomize`: альтернативы, веса `[98,2]`, сумма 100:
    - ветвь 0, weight `98`; условная доля 49/50 (98%):
      - пустое действие
    - ветвь 1, weight `2`; условная доля 1/50 (2%):
      - `$.sequence[1].randomize[1]` — поля действия: `{"run_command":{"command":["structure load lightning_sword ~ ~10 ~"]}}`

**`centella_death`** (строки 33,113):

- `$` — поля действия: `{"run_command":{"command":["summon lightning_bolt ~~~ default_lightning_bolt","say 2"]}}`

## `Swords_B/entities/creeper.json`

**Не разобран JSON5:** `<string>:430 Unexpected "}" at column 3`. Исходник не изменять и изучать вручную.

## `minecraft:ender_crystal`

- Путь `Swords_B/entities/ender_crystal.json`; format_version `"1.12.0"`.
- description: `{"identifier":"minecraft:ender_crystal","is_spawnable":false,"is_summonable":true,"is_experimental":false,"scripts":{"animate":["despawn_crystal","mount_crystal"]},"animations":{"despawn_crystal":"controller.animation.despawn_crystal","mount_crystal":"controller.animation.mount_crystal"}}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 21,35,64): `{"family":["ender_crystal","ender_crystal_default"]}`
- `minecraft:collision_box` (строки 65): `{"width":0.98,"height":0.98}`
- `minecraft:health` (строки 69): `{"value":1,"max":1}`
- `minecraft:fire_immune` (строки 73): `true`
- `minecraft:physics` (строки 74): `{}`
- `minecraft:pushable` (строки 75): `{"is_pushable":true,"is_pushable_by_piston":true}`

### Группы компонентов

- `despawn` (строки 18,143): `{"minecraft:despawn":{}}`
- `ender_crystal_scale` (строки 20,21,115,120): `{"minecraft:type_family":{"family":["ender_crystal","spectral_sword","ender_crystal_scale"]},"minecraft:ageable":{"duration":18,"grow_up":{"event":"minecraft:end_scale","target":"self"}},"minecraft:scale_by_age":{"start_scale":0.1,"end_scale":1}}`
- `on_hurt_crystal` (строки 28,85,134): `{"minecraft:on_hurt":{"event":"minecraft:crystal_explode","target":"self"}}`
- `spectral_sword` (строки 21,34,35,41,116,133,135,142): `{"minecraft:type_family":{"family":["ender_crystal","spectral_sword"]}}`
- `detect_player` (строки 37,123): `{"minecraft:environment_sensor":[{"on_environment":{"filters":{"all_of":[{"test":"is_family","subject":"self","operator":"!=","value":"spectral_sword"}]},"event":"ride_player"}}]}`
- `crystal_exploding` (строки 47,107,112): `{"minecraft:explode":{"fuse_length":0,"fuse_lit":true,"power":6,"causes_fire":false,"destroy_affected_by_griefing":true}}`
- `spectral_sword_drop` (строки 56,89): `{"minecraft:on_hurt":{"event":"spectral_crystal_explode","target":"self"}}`

### События

**`minecraft:entity_spawned`** (строки 81):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"has_biome_tag","operator":"!=","value":"nether"},"add":{"component_groups":["on_hurt_crystal"]}}`
  - `$.sequence[1]` — поля действия: `{"filters":{"test":"has_biome_tag","value":"nether"},"add":{"component_groups":["spectral_sword_drop"]}}`

**`spectral_crystal_explode`** (строки 58,93):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0].randomize`: альтернативы, веса `[98,2]`, сумма 100:
    - ветвь 0, weight `98`; условная доля 49/50 (98%):
      - пустое действие
    - ветвь 1, weight `2`; условная доля 1/50 (2%):
      - `$.sequence[0].randomize[1]` — поля действия: `{"run_command":{"command":["structure load spectral_sword ~~~"]}}`
  - `$.sequence[1]` — поля действия: `{"add":{"component_groups":["crystal_exploding"]}}`

**`minecraft:crystal_explode`** (строки 30,111):

- `$` — поля действия: `{"add":{"component_groups":["crystal_exploding"]}}`

**`minecraft:end_scale`** (строки 24,114):

- `$` — поля действия: `{"remove":{"component_groups":["ender_crystal_scale"]},"add":{"component_groups":["spectral_sword"]},"run_command":{"command":["playsound portal.travel @a[r=16] ~ ~ ~ 0.6 7","particle minecraft:example_flipbook ~ ~0.8 ~"]}}`

**`minecraft:ender_crystal_scale`** (строки 119):

- `$` — поля действия: `{"add":{"component_groups":["ender_crystal_scale"]}}`

**`minecraft:detect_player`** (строки 122):

- `$` — поля действия: `{"add":{"component_groups":["detect_player"]}}`

**`ride_player`** (строки 42,125):

- `$` — поля действия: `{"run_command":{"command":["ride @s start_riding @p[family=spectral_sword,r=3] teleport_rider"]}}`

**`minecraft:mount_crystal`** (строки 130):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"spectral_sword"},"remove":{"component_groups":["on_hurt_crystal"]},"add":{"component_groups":["spectral_sword"]}}`

**`minecraft:despawn`** (строки 18,139):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"spectral_sword"},"add":{"component_groups":["despawn"]},"run_command":{"command":["playsound portal.travel @a[r=12] ~ ~ ~ 0.5 8","particle minecraft:example_flipbook ~ ~0.5 ~"]}}`

## `entity:ender_crystal_projectile`

- Путь `Swords_B/entities/ender_crystal_projectile.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:ender_crystal_projectile","runtime_identifier":"minecraft:snowball","is_spawnable":false,"is_summonable":true,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:despawn` (строки 23): `{"despawn_from_simulation_edge":true}`
- `minecraft:type_family` (строки 26): `{"family":["ender_crystal"]}`
- `minecraft:collision_box` (строки 27): `{"width":0,"height":0}`
- `minecraft:projectile` (строки 31): `{"on_hit":{"definition_event":{"affect_projectile":true,"event_trigger":{"event":"minecraft:crystal_explode","target":"self"}}},"power":5,"gravity":0.001,"inertia":1,"liquid_inertia":1,"uncertainty_base":0,"uncertainty_multiplier":0,"anchor":1,"offset":[0,0,0],"reflect_on_hurt":true,"catch_fire":true}`
- `minecraft:fire_immune` (строки 52): `true`
- `minecraft:physics` (строки 53): `{}`
- `minecraft:environment_sensor` (строки 54): `[{"on_environment":{"filters":{"all_of":[{"test":"is_family","value":"ender_crystal"}]},"event":"projectile_particle"}}]`

### Группы компонентов

- `crystal_exploding` (строки 12,68): `{"minecraft:explode":{"fuse_length":0,"fuse_lit":true,"power":6,"causes_fire":true,"destroy_affected_by_griefing":true}}`

### События

**`minecraft:crystal_explode`** (строки 36,67):

- `$` — поля действия: `{"add":{"component_groups":["crystal_exploding"]}}`

**`projectile_particle`** (строки 61,70):

- `$` — поля действия: `{"run_command":{"command":["particle minecraft:example_flipbook ~ ~ ~"]}}`

## `minecraft:enderman`

- Путь `Swords_B/entities/enderman.json`; format_version `"1.13.0"`.
- description: `{"identifier":"minecraft:enderman","is_spawnable":true,"is_summonable":true,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:experience_reward` (строки 80): `{"on_death":"query.last_hit_by_player ? 5 : 0"}`
- `minecraft:type_family` (строки 83): `{"family":["enderman","monster","mob"]}`
- `minecraft:breathable` (строки 86): `{"total_supply":15,"suffocate_time":0}`
- `minecraft:nameable` (строки 90): `{}`
- `minecraft:loot` (строки 70,92): `{"table":"loot_tables/entities/enderman.json"}`
- `minecraft:health` (строки 66,95): `{"value":40,"max":40}`
- `minecraft:hurt_on_condition` (строки 99): `{"damage_conditions":[{"filters":{"test":"in_lava","subject":"self","operator":"==","value":true},"cause":"lava","damage_per_tick":4},{"filters":{"test":"in_water_or_rain","operator":"==","value":true},"cause":"drowning","damage_per_tick":1}]}`
- `minecraft:attack` (строки 63,113): `{"damage":7}`
- `minecraft:follow_range` (строки 59,116): `{"value":32,"max":32}`
- `minecraft:collision_box` (строки 120): `{"width":0.6,"height":2.9}`
- `minecraft:teleport` (строки 51,124): `{"random_teleports":true,"max_random_teleport_time":30,"random_teleport_cube":[32,32,32],"target_distance":16,"target_teleport_chance":0.05,"light_teleport_chance":0.05}`
- `minecraft:lookat` (строки 73,132): `{"search_radius":64.0,"set_target":true,"look_cooldown":5.0,"filters":{"all_of":[{"subject":"other","test":"is_family","value":"player"},{"test":"has_equipment","domain":"head","subject":"other","operator":"not","value":"carved_pumpkin"}]}}`
- `minecraft:behavior.nearest_attackable_target` (строки 153): `{"priority":5,"attack_interval":10,"entity_types":[{"filters":{"test":"is_family","subject":"other","value":"endermite"},"max_dist":64}],"must_see":true}`
- `minecraft:navigation.walk` (строки 168): `{"can_path_over_water":false,"avoid_water":true}`
- `minecraft:movement.basic` (строки 172): `{}`
- `minecraft:jump.static` (строки 175): `{}`
- `minecraft:can_climb` (строки 177): `{}`
- `minecraft:behavior.float` (строки 179): `{"priority":0}`
- `minecraft:behavior.random_stroll` (строки 182): `{"priority":7,"speed_multiplier":1.0}`
- `minecraft:behavior.look_at_player` (строки 186): `{"priority":8,"look_distance":8.0,"probability":8.0}`
- `minecraft:behavior.random_look_around` (строки 191): `{"priority":8}`
- `minecraft:behavior.hurt_by_target` (строки 194): `{"priority":3}`
- `minecraft:behavior.enderman_leave_block` (строки 197): `{"priority":10}`
- `minecraft:behavior.enderman_take_block` (строки 200): `{"priority":11}`
- `minecraft:physics` (строки 203): `{}`
- `minecraft:pushable` (строки 205): `{"is_pushable":true,"is_pushable_by_piston":true}`

### Группы компонентов

- `minecraft:default_enderman` (строки 11,215,249): `{"minecraft:variant":{"value":0}}`
- `minecraft:red_enderman` (строки 16,220,252): `{"minecraft:variant":{"value":1}}`
- `minecraft:enderman_calm` (строки 21,215,220,227,244,249,252): `{"minecraft:on_target_acquired":{"event":"minecraft:become_angry","target":"self"},"minecraft:movement":{"value":0.3}}`
- `minecraft:enderman_angry` (строки 30,232,239): `{"minecraft:angry":{"duration":25,"calm_event":{"event":"minecraft:on_calm","target":"self"}},"minecraft:movement":{"value":0.45},"minecraft:behavior.melee_attack":{"priority":2,"speed_multiplier":1.0,"track_target":false}}`
- `red_enderman` (строки 47,220,251,252): `{"minecraft:scale":{"value":1.2},"minecraft:teleport":{"random_teleports":true,"max_random_teleport_time":20,"random_teleport_cube":[32,32,32],"target_distance":32,"target_teleport_chance":0.04,"light_teleport_chance":0.04},"minecraft:follow_range":{"value":64,"max":64},"minecraft:attack":{"damage":12},"minecraft:health":{"value":120,"max":120},"minecraft:loot":{"table":"loot_tables/entities/red_enderman.json"},"minecraft:lookat":{"search_radius":64.0,"set_target":true,"look_cooldown":5.0,"filters":{"all_of":[{"subject":"other","test":"is_family","value":"player"}]}}}`

### События

**`minecraft:entity_spawned`** (строки 211):

- `$.randomize`: альтернативы, веса `[80,20]`, сумма 100:
  - ветвь 0, weight `80`; условная доля 4/5 (80%):
    - `$.randomize[0]` — поля действия: `{"add":{"component_groups":["minecraft:default_enderman","minecraft:enderman_calm"]}}`
  - ветвь 1, weight `20`; условная доля 1/5 (20%):
    - `$.randomize[1]` — поля действия: `{"filters":{"test":"has_biome_tag","operator":"==","value":"overworld"},"add":{"component_groups":["minecraft:red_enderman","red_enderman","minecraft:enderman_calm"]}}`

**`minecraft:become_angry`** (строки 23,224):

- `$` — поля действия: `{"remove":{"component_groups":["minecraft:enderman_calm"]},"add":{"component_groups":["minecraft:enderman_angry"]}}`

**`minecraft:on_calm`** (строки 34,236):

- `$` — поля действия: `{"remove":{"component_groups":["minecraft:enderman_angry"]},"add":{"component_groups":["minecraft:enderman_calm"]}}`

**`default_enderman`** (строки 248):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:default_enderman","minecraft:enderman_calm"]}}`

**`red_enderman`** (строки 47,220,251,252):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:red_enderman","red_enderman","minecraft:enderman_calm"]}}`

## `entity:name`

- Путь `Swords_B/entities/entity_name.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:name","is_spawnable":false,"is_summonable":true,"is_experimental":false,"scripts":{"animate":["despawn2"]},"animations":{"despawn2":"controller.animation.despawn2"}}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 28): `{"family":["effect99_entities","entity_name"]}`
- `minecraft:collision_box` (строки 29): `{"width":0.0,"height":0.0}`
- `minecraft:damage_sensor` (строки 30): `{"triggers":{"cause":"all","deals_damage":false}}`
- `minecraft:physics` (строки 31): `{}`
- `minecraft:health` (строки 32): `{"value":1}`
- `minecraft:despawn` (строки 17,33,36): `{"despawn_from_simulation_edge":true}`

### Группы компонентов

- `despawn` (строки 17,36): `{"minecraft:despawn":{}}`
- `wither_sword` (строки 19,38): `{"minecraft:boss":{"should_darken_sky":true,"name":"§l§4Wither Sword","hud_range":64}}`

### События

**`minecraft:despawn`** (строки 17,33,36):

- `$` — поля действия: `{"add":{"component_groups":["despawn"]}}`

**`minecraft:wither_sword`** (строки 38):

- `$` — поля действия: `{"add":{"component_groups":["wither_sword"]}}`

## `entity:nether_star`

- Путь `Swords_B/entities/entity_nether_star.json`; format_version `"1.13.0"`.
- description: `{"identifier":"entity:nether_star","is_spawnable":false,"is_summonable":true,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 16): `{"family":["effect99_entities"]}`
- `minecraft:timer` (строки 18): `{"time":[0.5,0.5],"looping":true,"time_down_event":{"event":"minecraft:despawn","target":"self"}}`
- `minecraft:nameable` (строки 21): `{}`
- `minecraft:collision_box` (строки 23): `{"width":0.25,"height":0.25}`
- `minecraft:health` (строки 27): `{"value":99,"max":99}`
- `minecraft:navigation.walk` (строки 31): `{}`
- `minecraft:damage_sensor` (строки 33): `{"triggers":{"cause":"all","deals_damage":false}}`
- `minecraft:balloonable` (строки 39): `{}`
- `minecraft:behavior.ranged_attack` (строки 41): `{"priority":1,"speed_multiplier":0,"attack_interval":0.1,"charge_shoot_trigger":0.1,"charge_charged_trigger":0.1,"attack_radius":28}`
- `minecraft:shooter` (строки 49): `{"def":"entity:nether_star_projectile"}`
- `minecraft:behavior.nearest_attackable_target` (строки 52): `{"priority":1,"reselect_targets":true,"scan_interval":1,"target_search_height":28,"entity_types":[{"filters":{"test":"is_family","subject":"other","value":"objective"},"max_dist":28}],"must_see":false}`
- `minecraft:persistent` (строки 66): `{}`
- `minecraft:physics` (строки 68): `{"has_gravity":false}`
- `minecraft:pushable` (строки 71): `{"is_pushable":true,"is_pushable_by_piston":true}`

### Группы компонентов

- `despawn` (строки 11,77): `{"minecraft:despawn":{}}`

### События

**`minecraft:despawn`** (строки 12,19,77):

- `$` — поля действия: `{"add":{"component_groups":["despawn"]}}`

## `entity:tnt`

- Путь `Swords_B/entities/entity_tnt.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:tnt","runtime_identifier":"minecraft:snowball","is_spawnable":false,"is_summonable":true,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:timer` (строки 25): `{"time":[0.1,0.1],"looping":true,"time_down_event":{"event":"despawn","target":"self"}}`
- `minecraft:projectile` (строки 28): `{"on_hit":{"definition_event":{"affect_projectile":true,"event_trigger":{"event":"mini_explosion","target":"self"}},"impact_damage":{"damage":1,"knockback":true,"destroy_on_hit":false},"particle_on_hit":{}},"hit_sound":"fuse","power":2,"gravity":0.0,"angle_offset":0.0}`
- `minecraft:type_family` (строки 49): `{"family":["effect99_entities"]}`
- `minecraft:collision_box` (строки 50): `{"width":0.0,"height":0.0}`
- `minecraft:physics` (строки 51): `{}`
- `minecraft:environment_sensor` (строки 52): `[{"on_environment":{"filters":{"all_of":[{"test":"is_family","value":"effect99_entities"}]},"event":"particle"}}]`

### Группы компонентов

- `despawn` (строки 12,26,62): `{"minecraft:despawn":{}}`
- `mini_explosion` (строки 14,33,60): `{"minecraft:explode":{"fuse_length":0,"fuse_lit":true,"power":1,"causes_fire":false,"destroy_affected_by_griefing":true}}`

### События

**`mini_explosion`** (строки 14,33,60):

- `$` — поля действия: `{"add":{"component_groups":["mini_explosion"]}}`

**`despawn`** (строки 12,26,62):

- `$` — поля действия: `{"add":{"component_groups":["despawn"]}}`

**`particle`** (строки 54,64):

- `$` — поля действия: `{"run_command":{"command":["particle minecraft:obsidian_glow_dust_particle ~ ~ ~"]}}`

## `entity:fake_fireball`

- Путь `Swords_B/entities/fake_fireball.json`; format_version `"1.12.0"`.
- description: `{"identifier":"entity:fake_fireball","runtime_identifier":"minecraft:snowball","is_spawnable":false,"is_summonable":false,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:collision_box` (строки 12): `{"width":0.31,"height":0.31}`
- `minecraft:projectile` (строки 16): `{"on_hit":{"impact_damage":{"damage":5,"knockback":false,"catch_fire":true,"semi_random_diff_damage":false},"catch_fire":{"fire_affected_by_griefing":true},"remove_on_hit":{}},"power":1.3,"gravity":0.02,"inertia":1,"liquid_inertia":1,"anchor":2,"offset":[0,0.5,0],"semi_random_diff_damage":true,"uncertainty_base":10.0,"reflect_on_hurt":true}`
- `minecraft:physics` (строки 39): `{}`
- `minecraft:pushable` (строки 41): `{"is_pushable":true,"is_pushable_by_piston":true}`

### Группы компонентов


### События

**`set_sound`** (строки 47):

- `$` — поля действия: `{"run_command":{"command":["playsound mob.ghast.fireball @a[r=16] ~ ~ ~"]}}`

## `entity:fire`

- Путь `Swords_B/entities/fire.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:fire","runtime_identifier":"minecraft:snowball","is_spawnable":false,"is_summonable":true,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 35): `{"family":["effect99_entities"]}`
- `minecraft:despawn` (строки 36): `{}`
- `minecraft:collision_box` (строки 37): `{"width":0.1,"height":0.1}`
- `minecraft:physics` (строки 38): `{}`
- `minecraft:projectile` (строки 13,39): `{"on_hit":{"impact_damage":{"damage":0,"catch_fire":true},"remove_on_hit":{}},"power":1,"gravity":0.01}`

### Группы компонентов

- `fire_sword` (строки 12,53): `{"minecraft:projectile":{"on_hit":{"impact_damage":{"damage":1,"knockback":false,"catch_fire":true,"semi_random_diff_damage":false},"catch_fire":{"fire_affected_by_griefing":true},"remove_on_hit":{}},"power":10,"gravity":0.1,"inertia":1,"liquid_inertia":1,"reflect_on_hurt":true}}`

### События

**`minecraft:entity_spawned`** (строки 48):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"has_equipment","subject":"other","domain":"hand","value":"effect:fire_sword"},"add":{"component_groups":["fire_sword"]}}`

## `minecraft:fireball`

- Путь `Swords_B/entities/fireball.json`; format_version `"1.12.0"`.
- description: `{"identifier":"minecraft:fireball","is_spawnable":false,"is_summonable":false,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 46): `{"family":["fireball"]}`
- `minecraft:collision_box` (строки 47): `{"width":0.31,"height":0.31}`
- `minecraft:projectile` (строки 22,51): `{"on_hit":{"definition_event":{"affect_projectile":true,"event_trigger":{"event":"minecraft:explode","target":"self"}}},"power":1.6,"gravity":0.0,"inertia":1,"liquid_inertia":1,"uncertainty_base":0,"uncertainty_multiplier":0,"anchor":1,"offset":[0,-0.1,0],"reflect_on_hurt":true,"catch_fire":true}`
- `minecraft:physics` (строки 72): `{}`
- `minecraft:pushable` (строки 74): `{"is_pushable":true,"is_pushable_by_piston":true}`

### Группы компонентов

- `minecraft:exploding` (строки 11,83): `{"minecraft:explode":{"fuse_length":0,"fuse_lit":true,"power":1,"causes_fire":true,"fire_affected_by_griefing":true,"destroy_affected_by_griefing":true}}`
- `gravity_enable` (строки 21,90,99): `{"minecraft:projectile":{"on_hit":{"definition_event":{"affect_projectile":true,"event_trigger":{"event":"minecraft:explode","target":"self"}}},"power":1.6,"gravity":0.04,"inertia":1,"liquid_inertia":1,"uncertainty_base":0,"uncertainty_multiplier":0,"anchor":1,"offset":[0,-0.1,0],"reflect_on_hurt":true,"catch_fire":true}}`

### События

**`minecraft:explode`** (строки 12,27,56,80):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:exploding"]}}`

**`minecraft:gravity_enable`** (строки 87):

- `$` — поля действия: `{"add":{"component_groups":["gravity_enable"]}}`

**`minecraft:entity_spawned`** (строки 94):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"other","value":"player"},"add":{"component_groups":["gravity_enable"]},"run_command":{"command":["playsound mob.ghast.fireball @a[r=12] ~ ~ ~"]}}`

## `minecraft:ghast`

- Путь `Swords_B/entities/ghast.json`; format_version `"1.13.0"`.
- description: `{"identifier":"minecraft:ghast","is_spawnable":true,"is_summonable":true,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:experience_reward` (строки 11): `{"on_death":"query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"}`
- `minecraft:breathable` (строки 14): `{"total_supply":15,"suffocate_time":0}`
- `minecraft:fire_immune` (строки 18): `true`
- `minecraft:nameable` (строки 19): `{}`
- `minecraft:health` (строки 21): `{"value":10,"max":10}`
- `minecraft:collision_box` (строки 25): `{"width":4,"height":4}`
- `minecraft:movement` (строки 29): `{"value":0.03}`
- `minecraft:navigation.float` (строки 32): `{"can_path_over_water":true}`
- `minecraft:behavior.float_wander` (строки 35): `{"priority":2,"must_reach":true}`
- `minecraft:can_fly` (строки 39): `{}`
- `minecraft:loot` (строки 41): `{"table":"loot_tables/entities/ghast.json"}`
- `minecraft:shooter` (строки 44): `{"type":"largefireball","def":"minecraft:fireball"}`
- `minecraft:type_family` (строки 48): `{"family":["ghast","monster","mob"]}`
- `minecraft:damage_sensor` (строки 51): `{"triggers":[{"on_damage":{"filters":{"test":"is_family","value":"ghast"},"event":"spectral_ghast"},"deals_damage":true},{"cause":"fall","deals_damage":false}]}`
- `minecraft:jump.static` (строки 65): `{}`
- `minecraft:behavior.float` (строки 67): `{"priority":0}`
- `minecraft:behavior.ranged_attack` (строки 70): `{"priority":1,"attack_radius":64,"charge_shoot_trigger":2,"charge_charged_trigger":1}`
- `minecraft:follow_range` (строки 76): `{"value":64,"max":64}`
- `minecraft:behavior.hurt_by_target` (строки 80): `{"priority":1}`
- `minecraft:behavior.nearest_attackable_target` (строки 83): `{"priority":2,"entity_types":[{"filters":{"test":"is_family","subject":"other","value":"player"},"max_dist":28}],"must_see":true}`
- `minecraft:physics` (строки 97): `{}`
- `minecraft:pushable` (строки 99): `{"is_pushable":true,"is_pushable_by_piston":true}`

### Группы компонентов


### События

**`spectral_ghast`** (строки 55,105):

- `$.randomize`: альтернативы, веса `[94,6]`, сумма 100:
  - ветвь 0, weight `94`; условная доля 47/50 (94%):
    - пустое действие
  - ветвь 1, weight `6`; условная доля 3/50 (6%):
    - `$.randomize[1]` — поля действия: `{"run_command":{"command":["structure load spectral_sword ~~~"]}}`

## `entity:ghost`

- Путь `Swords_B/entities/ghost.json`; format_version `"1.13.0"`.
- description: `{"identifier":"entity:ghost","runtime_identifier":"minecraft:chicken","is_spawnable":true,"is_summonable":true,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:damage_sensor` (строки 17): `{"triggers":[{"on_damage":{"filters":{"test":"is_family","subject":"other","value":"player"},"event":"disturbed_ghost"},"deals_damage":false},{"cause":"all","deals_damage":false}]}`
- `minecraft:behavior.look_at_entity` (строки 31): `{"priority":3,"look_distance":6.0,"probability":1.0,"angle_of_view_vertical":135,"angle_of_view_horizontal":170,"filters":{"any_of":[{"test":"is_family","subject":"other","value":"mob"},{"test":"is_family","subject":"other","value":"ghost_sword"}]}}`
- `minecraft:type_family` (строки 44): `{"family":["ghost","mob","monster"]}`
- `minecraft:collision_box` (строки 47): `{"width":0.6,"height":1.8}`
- `minecraft:health` (строки 51): `{"value":666,"max":666}`
- `minecraft:scale` (строки 55): `{"value":1.05}`
- `minecraft:movement` (строки 58): `{"value":0.3}`
- `minecraft:navigation.walk` (строки 61): `{"can_path_over_water":true,"avoid_damage_blocks":true}`
- `minecraft:movement.basic` (строки 65): `{}`
- `minecraft:jump.static` (строки 67): `{}`
- `minecraft:can_climb` (строки 69): `{}`
- `minecraft:behavior.float` (строки 71): `{"priority":0}`
- `minecraft:behavior.flee_sun` (строки 74): `{"priority":2,"speed_multiplier":1}`
- `minecraft:behavior.random_stroll` (строки 78): `{"priority":1,"speed_multiplier":1.0,"xz_dist":30}`
- `minecraft:knockback_resistance` (строки 83): `{"value":1.0}`
- `minecraft:fire_immune` (строки 86): `true`
- `minecraft:physics` (строки 87): `{}`
- `minecraft:pushable` (строки 89): `{"is_pushable":false,"is_pushable_by_piston":false}`
- `minecraft:environment_sensor` (строки 93): `{"triggers":[{"filters":{"test":"is_brightness","operator":">","value":0.1},"event":"despawn"},{"filters":{},"event":"ghost_effects"}]}`

### Группы компонентов

- `despawn` (строки 12,97,120,165,166): `{"minecraft:despawn":{}}`

### События

**`minecraft:entity_spawned`** (строки 107):


**`disturbed_ghost`** (строки 21,109):

- `$.randomize`: альтернативы, веса `[987,10,3]`, сумма 1000:
  - ветвь 0, weight `987`; условная доля 987/1000 (98.7%):
    - пустое действие
  - ветвь 1, weight `10`; условная доля 1/100 (1%):
    - `$.randomize[1]` — поля действия: `{"run_command":{"command":["playsound mob.endermen.portal @a[r=17] ~~~","spreadplayers ~ ~ 0 16 @s"]}}`
  - ветвь 2, weight `3`; условная доля 3/1000 (0.3%):
    - `$.randomize[2]` — поля действия: `{"add":{"component_groups":["despawn"]},"run_command":{"command":["structure load ghost_sword ~~~","particle minecraft:ghost_spiral ~~~","playsound mob.wither.ambient @a[r=16] ~ ~1 ~ 2 0.3","particle minecraft:egg_destroy_emitter ~ ~ ~","particle minecraft:egg_destroy_emitter ~ ~0.3 ~","particle minecraft:egg_destroy_emitter ~ ~0.6 ~","particle minecraft:egg_destroy_emitter ~ ~0.9 ~","particle minecraft:egg_destroy_emitter ~ ~1.2 ~","particle minecraft:egg_destroy_emitter ~ ~1.5 ~"]}}`

**`ghost_wailing`** (строки 136):

- `$.randomize`: альтернативы, веса `[70,30]`, сумма 100:
  - ветвь 0, weight `70`; условная доля 7/10 (70%):
    - пустое действие
  - ветвь 1, weight `30`; условная доля 3/10 (30%):
    - `$.randomize[1].randomize`: альтернативы, веса `[50,50]`, сумма 100:
      - ветвь 0, weight `50`; условная доля 1/2 (50%):
        - `$.randomize[1].randomize[0]` — поля действия: `{"run_command":{"command":["playsound ghost_sword.wailing @a[rm=10,r=50]"]}}`
      - ветвь 1, weight `50`; условная доля 1/2 (50%):
        - `$.randomize[1].randomize[1]` — поля действия: `{"run_command":{"command":["playsound ghost_sword.wailing @a[rm=10,r=50] ~~~ 1 7"]}}`

**`ghost_effects`** (строки 101,154):

- `$.randomize`: альтернативы, веса `[90,10]`, сумма 100:
  - ветвь 0, weight `90`; условная доля 9/10 (90%):
    - пустое действие
  - ветвь 1, weight `10`; условная доля 1/10 (10%):
    - `$.randomize[1]` — поля действия: `{"run_command":{"command":["playsound mob.wither.spawn @a[r=16] ~ ~ ~ 0.15 0.2"]}}`

**`despawn`** (строки 12,97,120,165,166):

- `$` — поля действия: `{"add":{"component_groups":["despawn"]},"run_command":{"command":["particle minecraft:ghost_spiral ~~~","playsound mob.wither.ambient @a[r=16] ~ ~1 ~ 2 0.3","particle minecraft:egg_destroy_emitter ~ ~ ~","particle minecraft:egg_destroy_emitter ~ ~0.3 ~","particle minecraft:egg_destroy_emitter ~ ~0.6 ~","particle minecraft:egg_destroy_emitter ~ ~0.9 ~","particle minecraft:egg_destroy_emitter ~ ~1.2 ~","particle minecraft:egg_destroy_emitter ~ ~1.5 ~"]}}`

## `entity:ghost_projectile`

- Путь `Swords_B/entities/ghost_projectile.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:ghost_projectile","runtime_identifier":"minecraft:snowball","is_spawnable":false,"is_summonable":true,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:timer` (строки 13,37): `{"time":[0,0],"looping":true,"time_down_event":{"event":"teleport_owner","target":"self"}}`
- `minecraft:type_family` (строки 40): `{"family":["effect99_entities"]}`
- `minecraft:collision_box` (строки 17,41): `{"width":0.0,"height":0.0}`
- `minecraft:projectile` (строки 20,44): `{"on_hit":{"impact_damage":{"damage":-1}},"power":2.5,"gravity":0.0,"liquid_inertia":2.8,"angle_offset":0.0}`
- `minecraft:pushable` (строки 55): `{"is_pushable":false,"is_pushable_by_piston":false}`
- `minecraft:physics` (строки 14,59): `{"has_collision":false}`

### Группы компонентов

- `teleport_enable` (строки 12,71,75): `{"minecraft:timer":{},"minecraft:physics":{"has_collision":true},"minecraft:collision_box":{"width":10,"height":10},"minecraft:projectile":{"on_hit":{"impact_damage":{"damage":-1,"knockback":false},"teleport_owner":{},"remove_on_hit":{}},"power":2.5,"gravity":0.0,"liquid_inertia":2.8,"angle_offset":0.0}}`

### События

**`teleport_owner`** (строки 26,38,64):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"run_command":{"command":["execute @s ~~~ detect ~~~ air 0 event entity @s teleport_enable"]}}`
  - `$.sequence[1]` — поля действия: `{"filters":{"test":"in_water"},"add":{"component_groups":["teleport_enable"]}}`

**`teleport_enable`** (строки 12,71,75):

- `$` — поля действия: `{"add":{"component_groups":["teleport_enable"]}}`

## `entity:grass`

- Путь `Swords_B/entities/grass.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:grass","is_spawnable":false,"is_summonable":true,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 25): `{"family":["effect99_entities"]}`
- `minecraft:collision_box` (строки 26): `{"width":0.0,"height":0.0}`
- `minecraft:damage_sensor` (строки 27): `{"triggers":{"cause":"all","deals_damage":false}}`
- `minecraft:physics` (строки 28): `{"has_gravity":false,"has_collision":false}`
- `minecraft:pushable` (строки 29): `{"is_pushable":false,"is_pushable_by_piston":false}`

### Группы компонентов

- `despawn` (строки 11,15,54,56): `{"minecraft:despawn":{}}`
- `start_despawn` (строки 13,52): `{"minecraft:timer":{"time":[0.52,0.52],"looping":false,"time_down_event":{"event":"despawn","target":"self"}}}`
- `grass_sword` (строки 18,34): `{"minecraft:timer":{"time":[1.08,1.08],"looping":false,"time_down_event":{"event":"grass_sword_skill","target":"self"}}}`

### События

**`minecraft:entity_spawned`** (строки 32):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"add":{"component_groups":["grass_sword"]},"run_command":{"command":["playsound dig.grass @a[r=12]","effect @e[type=!entity:grass,r=1] slowness 2 15 true","execute @e[family=!grass_witch,type=!entity:grass,type=!xp_orb,type=!arrow,r=1,tag=!grass] ~ ~ ~ tag @s add grass"]}}`

**`grass_sword_skill`** (строки 20,44):

- `$` — поля действия: `{"run_command":{"command":["playsound dig.grass @a[r=12] ~ ~ ~ 1 0.4","execute @e[type=!entity:grass,c=1,r=1,tag=grass] ~ ~ ~ detect ~ ~-1 ~ grass 0 execute @s ~ ~ ~ detect ~ ~ ~ air 0 tp @s ~ ~-1 ~","execute @e[type=!entity:grass,c=1,r=1,tag=grass] ~ ~ ~ detect ~ ~-1 ~ grass 0 execute @s ~ ~ ~ detect ~ ~ ~ tallgrass 0 tp @s ~ ~-1 ~","tag @e[tag=grass,r=2] remove grass"]},"add":{"component_groups":["start_despawn"]}}`

**`despawn`** (строки 11,15,54,56):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"add":{"component_groups":["despawn"]}}`
  - `$.sequence[1].randomize`: альтернативы, веса `[50,50]`, сумма 100:
    - ветвь 0, weight `50`; условная доля 1/2 (50%):
      - `$.sequence[1].randomize[0]` — поля действия: `{"run_command":{"command":["fill ~ ~ ~ ~ ~ ~ tallgrass 0 replace air"]}}`
    - ветвь 1, weight `50`; условная доля 1/2 (50%):
      - пустое действие

## `entity:grows_crop`

- Путь `Swords_B/entities/grows_crop.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:grows_crop","runtime_identifier":"minecraft:bee","is_spawnable":false,"is_summonable":true,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:damage_sensor` (строки 22): `{"triggers":{"cause":"all","deals_damage":false}}`
- `minecraft:type_family` (строки 23): `{"family":["effect99_entities"]}`
- `minecraft:ageable` (строки 24): `{"duration":1,"grow_up":{"event":"despawn","target":"self"}}`
- `minecraft:grows_crop` (строки 25): `{"chance":0.5,"charges":10}`
- `minecraft:collision_box` (строки 26): `{"width":0.0,"height":0.0}`
- `minecraft:physics` (строки 27): `{"has_gravity":false,"has_collision":false}`

### Группы компонентов

- `despawn` (строки 12,24,35): `{"minecraft:despawn":{}}`
- `grows_crop_event` (строки 15,33): `{"minecraft:timer":{"time":[0.3,0.3],"looping":true,"time_down_event":{"event":"grows_crop","target":"self"}}}`

### События

**`grows_crop_event`** (строки 15,33):

- `$` — поля действия: `{"add":{"component_groups":["grows_crop_event"]}}`

**`despawn`** (строки 12,24,35):

- `$` — поля действия: `{"add":{"component_groups":["despawn"]}}`

**`grows_crop`** (строки 17,37):

- `$` — поля действия: `{"run_command":{"command":["summon entity:grows_crop ~ ~0.1 ~","summon entity:grows_crop ~ ~0.1 ~1","summon entity:grows_crop ~1 ~0.1 ~","summon entity:grows_crop ~-1 ~0.1 ~","summon entity:grows_crop ~ ~0.1 ~-1","summon entity:grows_crop ~1 ~0.1 ~1","summon entity:grows_crop ~-1 ~0.1 ~-1","summon entity:grows_crop ~1 ~0.1 ~-1","summon entity:grows_crop ~-1 ~0.1 ~1","summon entity:grows_crop ~ ~0.1 ~2","summon entity:grows_crop ~2 ~0.1 ~","summon entity:grows_crop ~-2 ~0.1 ~","summon entity:grows_crop ~ ~0.1 ~-2"]}}`

## `entity:instant_creeper_explode`

- Путь `Swords_B/entities/instant_creeper_explode.json`; format_version `"1.12.0"`.
- description: `{"identifier":"entity:instant_creeper_explode","is_spawnable":false,"is_summonable":true,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 6): `{"family":["effect99_entities"]}`
- `minecraft:collision_box` (строки 7): `{"width":0.0,"height":0.0}`
- `minecraft:damage_sensor` (строки 8): `{"triggers":{"cause":"all","deals_damage":false}}`
- `minecraft:explode` (строки 9): `{"fuse_length":0,"fuse_lit":true,"power":4,"causes_fire":false,"destroy_affected_by_griefing":true}`
- `minecraft:physics` (строки 10): `{}`

### Группы компонентов


### События

## `entity:instant_giant_explode`

- Путь `Swords_B/entities/instant_giant_explode.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:instant_giant_explode","is_spawnable":false,"is_summonable":true,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:timer` (строки 12): `{"time":[0,0],"looping":false,"time_down_event":{"event":"explode_effects","target":"self"}}`
- `minecraft:scale` (строки 15): `{"value":0}`
- `minecraft:explode` (строки 16): `{"fuse_length":0.02,"fuse_lit":true,"power":16,"causes_fire":true,"destroy_affected_by_griefing":true}`
- `minecraft:type_family` (строки 23): `{"family":["tnt","inanimate","effect99_entities"]}`
- `minecraft:collision_box` (строки 26): `{"width":0.98,"height":0.98}`
- `minecraft:physics` (строки 30): `{}`
- `minecraft:pushable` (строки 32): `{"is_pushable":false,"is_pushable_by_piston":true}`

### Группы компонентов


### События

**`explode_effects`** (строки 13,38):

- `$` — поля действия: `{"run_command":{"command":["camerashake add @a[r=32] 0.2 0.8 positional","playsound random.explode @a[r=32] ~ ~ ~ 2 0.4 2"]}}`

## `minecraft:item`

- Путь `Swords_B/entities/item.json`; format_version `"1.11.0"`.
- description: `{"identifier":"minecraft:item","is_spawnable":false,"is_summonable":true,"is_experimental":false,"scripts":{"animate":["on_fire_swords"]},"animations":{"on_fire_swords":"controller.animation.item_events"}}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 23,29,33): `{"family":["item"]}`
- `minecraft:environment_sensor` (строки 34): `[{"on_environment":{"filters":{"all_of":[{"test":"has_tag","value":"fire_sword"},{"test":"in_water","operator":"!="},{"test":"in_water_or_rain"}]},"event":"fading_fire_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_tag","value":"fire_sword"},{"test":"in_water"}]},"event":"fire_sword_event_2"}},{"on_environment":{"filters":{"all_of":[{"test":"is_family","value":"fire_sword"},{"test":"in_water_or_rain","operator":"!="}]},"event":"stop_fire_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_tag","value":"sponge_sword"},{"test":"in_water_or_rain"}]},"event":"sponge_sword_event"}},{"on_environment":{"filters":{"all_of":[{"test":"is_family","value":"sponge_sword"},{"test":"in_water_or_rain","operator":"!="}]},"event":"stop_sponge_sword"}},{"on_environment":{"filters":{"test":"has_tag","value":"fire_immune"},"event":"delete_fire_blocks"}},{"on_environment":{"filters":{"all_of":[{"test":"has_tag","value":"wish_1"}]},"event":"fountain_of_wishes_1"}},{"on_environment":{"filters":{"all_of":[{"test":"has_tag","value":"wish_2"}]},"event":"fountain_of_wishes_2"}},{"on_environment":{"filters":{"all_of":[{"test":"has_tag","value":"wish_3"}]},"event":"fountain_of_wishes_3"}}]`
- `minecraft:physics` (строки 112): `{}`

### Группы компонентов

- `sponge_sword` (строки 19,23,66,75,118,119,136): `{"minecraft:timer":{"time":[0,1],"looping":false,"randomInterval":true,"time_down_event":{"event":"wet_sponge_sword","target":"self"}},"minecraft:type_family":{"family":["sponge_sword"]}}`
- `fire_sword` (строки 25,29,38,48,57,219,220,227,233): `{"minecraft:timer":{"time":[5,6],"looping":false,"randomInterval":true,"time_down_event":{"event":"fire_sword_event_1","target":"self"}},"minecraft:type_family":{"family":["fire_sword"]}}`

### События

**`sponge_sword_event`** (строки 69,115):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","operator":"!=","value":"sponge_sword"},"add":{"component_groups":["sponge_sword"]}}`
  - `$.sequence[1]` — поля действия: `{"run_command":{"command":["fill ~2 ~2 ~2 ~-2 ~-2 ~-2 sponge 0 replace water","playsound random.fizz @a[r=12] ~~~ 0.5","particle minecraft:cauldron_explosion_emitter ~ ~ ~","fill ~2 ~2 ~2 ~-2 ~-2 ~-2 air 0 replace sponge","fill ~2 ~2 ~2 ~-2 ~-2 ~-2 air 0 replace seagrass"]}}`

**`wet_sponge_sword`** (строки 21,134):

- `$` — поля действия: `{"run_command":{"command":["structure load wet_sponge_sword ~ ~ ~","kill @s"]}}`

**`stop_sponge_sword`** (строки 78,136):

- `$` — поля действия: `{"remove":{"component_groups":["sponge_sword"]}}`

**`fountain_of_wishes_1`** (строки 92,138):

- `$` — поля действия: `{"run_command":{"command":["execute @s ~ ~ ~ detect ~ ~ ~ water 0 execute @s ~ ~ ~ detect ~1 ~ ~ water 0 execute @s ~ ~ ~ detect ~-1 ~ ~ water 0 execute @s ~ ~ ~ detect ~ ~ ~1 water 0 execute @s ~ ~ ~ detect ~ ~ ~-1 water 0 execute @s ~ ~ ~ detect ~ ~-1 ~ sandstone 0 execute @s ~ ~ ~ detect ~1 ~-1 ~ sandstone 0 execute @s ~ ~ ~ detect ~-1 ~-1 ~ sandstone 0 execute @s ~ ~ ~ detect ~ ~-1 ~1 sandstone 0 execute @s ~ ~ ~ detect ~ ~-1 ~-1 sandstone 0 execute @s ~ ~ ~ detect ~ ~4 ~ sandstone 0 execute @s ~ ~ ~ detect ~1 ~2 ~1 sandstone 0 execute @s ~ ~ ~ detect ~-1 ~2 ~-1 sandstone 0 execute @s ~ ~ ~ detect ~-1 ~2 ~1 sandstone 0 execute @s ~ ~ ~ detect ~1 ~2 ~-1 sandstone 0 event entity @s wish_1"]}}`

**`fountain_of_wishes_2`** (строки 100,140):

- `$` — поля действия: `{"run_command":{"command":["execute @s ~ ~ ~ detect ~ ~ ~ water 0 execute @s ~ ~ ~ detect ~1 ~ ~ water 0 execute @s ~ ~ ~ detect ~-1 ~ ~ water 0 execute @s ~ ~ ~ detect ~ ~ ~1 water 0 execute @s ~ ~ ~ detect ~ ~ ~-1 water 0 execute @s ~ ~ ~ detect ~ ~-1 ~ sandstone 0 execute @s ~ ~ ~ detect ~1 ~-1 ~ sandstone 0 execute @s ~ ~ ~ detect ~-1 ~-1 ~ sandstone 0 execute @s ~ ~ ~ detect ~ ~-1 ~1 sandstone 0 execute @s ~ ~ ~ detect ~ ~-1 ~-1 sandstone 0 execute @s ~ ~ ~ detect ~ ~4 ~ sandstone 0 execute @s ~ ~ ~ detect ~1 ~2 ~1 sandstone 0 execute @s ~ ~ ~ detect ~-1 ~2 ~-1 sandstone 0 execute @s ~ ~ ~ detect ~-1 ~2 ~1 sandstone 0 execute @s ~ ~ ~ detect ~1 ~2 ~-1 sandstone 0 event entity @s wish_2"]}}`

**`fountain_of_wishes_3`** (строки 108,142):

- `$` — поля действия: `{"run_command":{"command":["execute @s ~ ~ ~ detect ~ ~ ~ water 0 execute @s ~ ~ ~ detect ~1 ~ ~ water 0 execute @s ~ ~ ~ detect ~-1 ~ ~ water 0 execute @s ~ ~ ~ detect ~ ~ ~1 water 0 execute @s ~ ~ ~ detect ~ ~ ~-1 water 0 execute @s ~ ~ ~ detect ~ ~-1 ~ sandstone 0 execute @s ~ ~ ~ detect ~1 ~-1 ~ sandstone 0 execute @s ~ ~ ~ detect ~-1 ~-1 ~ sandstone 0 execute @s ~ ~ ~ detect ~ ~-1 ~1 sandstone 0 execute @s ~ ~ ~ detect ~ ~-1 ~-1 sandstone 0 execute @s ~ ~ ~ detect ~ ~4 ~ sandstone 0 execute @s ~ ~ ~ detect ~1 ~2 ~1 sandstone 0 execute @s ~ ~ ~ detect ~-1 ~2 ~-1 sandstone 0 execute @s ~ ~ ~ detect ~-1 ~2 ~1 sandstone 0 execute @s ~ ~ ~ detect ~1 ~2 ~-1 sandstone 0 event entity @s wish_3"]}}`

**`wish_1`** (строки 90,144):

- `$.randomize`: альтернативы, веса `[992,8]`, сумма 1000:
  - ветвь 0, weight `992`; условная доля 124/125 (99.2%):
    - `$.randomize[0]` — поля действия: `{"run_command":{"command":["particle minecraft:example_flipbook ~ ~ ~","kill @s"]}}`
  - ветвь 1, weight `8`; условная доля 1/125 (0.8%):
    - `$.randomize[1]` — поля действия: `{"run_command":{"command":["structure load ultra_instinct_sword ~ ~1 ~","fill ~15 ~10 ~15 ~-15 ~-15 ~-15 concretepowder 0 replace sand","particle minecraft:example_flipbook ~ ~ ~","particle minecraft:example_flipbook ~ ~1.5 ~","playsound mob.wither.ambient @a[r=16] ~ ~1 ~ 2 0.6","kill @s"]}}`

**`wish_2`** (строки 98,156):

- `$.randomize`: альтернативы, веса `[975,25]`, сумма 1000:
  - ветвь 0, weight `975`; условная доля 39/40 (97.5%):
    - `$.randomize[0]` — поля действия: `{"run_command":{"command":["particle minecraft:example_flipbook ~ ~ ~","kill @s"]}}`
  - ветвь 1, weight `25`; условная доля 1/40 (2.5%):
    - `$.randomize[1]` — поля действия: `{"run_command":{"command":["structure load ultra_instinct_sword ~ ~1 ~","fill ~15 ~10 ~15 ~-15 ~-15 ~-15 concretepowder 0 replace sand","particle minecraft:example_flipbook ~ ~ ~","particle minecraft:example_flipbook ~ ~1.5 ~","playsound mob.wither.ambient @a[r=16] ~ ~1 ~ 2 0.6","kill @s"]}}`

**`wish_3`** (строки 106,168):

- `$.randomize`: альтернативы, веса `[975,25]`, сумма 1000:
  - ветвь 0, weight `975`; условная доля 39/40 (97.5%):
    - `$.randomize[0]` — поля действия: `{"run_command":{"command":["particle minecraft:knockback_roar_particle ~ ~0.3 ~","time add 1000","playsound random.orb @a[r=16] ~ ~ ~ 1 0.5","kill @s"]}}`
  - ветвь 1, weight `25`; условная доля 1/40 (2.5%):
    - `$.randomize[1]` — поля действия: `{"run_command":{"command":["structure load time_sword ~ ~1 ~","time add 6000","fill ~15 ~10 ~15 ~-15 ~-15 ~-15 concretepowder 4 replace sand","particle minecraft:knockback_roar_particle ~ ~0.3 ~","playsound random.levelup @a[r=16] ~ ~ ~ 1 0.5","kill @s"]}}`

**`respawn_event_1`** (строки 180):

- `$` — поля действия: `{"run_command":{"command":["structure load bedrock_sword ~ ~1 ~","kill @s"]}}`

**`respawn_event_2`** (строки 183):

- `$` — поля действия: `{"run_command":{"command":["structure load fire_sword ~ ~1 ~","kill @s"]}}`

**`despawn_event_1`** (строки 186):

- `$` — поля действия: `{"run_command":{"command":["particle minecraft:example_linearcurve ~ ~ ~","playsound mob.endermen.death @a[r=16] ~ ~ ~ 1 0.5","kill @s"]}}`

**`despawn_event_2`** (строки 189):

- `$` — поля действия: `{"run_command":{"command":["particle minecraft:example_linearcurve ~ ~ ~","playsound mob.wither.death @a[r=16] ~ ~ ~ 1 0.5","kill @s"]}}`

**`despawn_event_3`** (строки 192):

- `$` — поля действия: `{"run_command":{"command":["particle minecraft:example_linearcurve ~ ~ ~","summon lightning_bolt ~~~ default_lightning_bolt"]}}`

**`despawn_event_4`** (строки 195):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"has_biome_tag","operator":"!=","value":"nether"},"run_command":{"command":["fill ~~~ ~~~ flowing_water 0 replace air","fill ~~~ ~~~ flowing_water 0 replace fire","fill ~~~ ~~~ flowing_water 0 replace lava","playsound random.fizz @a[r=12] ~ ~ ~ 0.6","particle minecraft:cauldron_explosion_emitter ~ ~ ~","kill @s"]}}`
  - `$.sequence[1]` — поля действия: `{"filters":{"test":"has_biome_tag","value":"nether"},"run_command":{"command":["playsound random.fizz @a[r=12] ~ ~ ~ 0.6","particle minecraft:cauldron_explosion_emitter ~ ~ ~","kill @s"]}}`

**`despawn_event_5`** (строки 207):

- `$` — поля действия: `{"run_command":{"command":["summon entity:instant_giant_explode","kill @s"]}}`

**`despawn_event_6`** (строки 210):

- `$` — поля действия: `{"run_command":{"command":["summon entity:ultra_instinct_explode","kill @s"]}}`

**`delete_fire_blocks`** (строки 84,213):

- `$` — поля действия: `{"run_command":{"command":["fill ~2 ~2 ~2 ~-2 ~-2 ~-2 air 0 replace fire"]}}`

**`fading_fire_sword`** (строки 42,216):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","operator":"!=","value":"fire_sword"},"add":{"component_groups":["fire_sword"]}}`
  - `$.sequence[1]` — поля действия: `{"run_command":{"command":["playsound random.fizz @a[r=12] ~ ~ ~ 0.6","particle minecraft:cauldron_explosion_emitter ~ ~ ~"]}}`

**`stop_fire_sword`** (строки 60,227):

- `$` — поля действия: `{"remove":{"component_groups":["fire_sword"]}}`

**`fire_sword_event_1`** (строки 27,228):

- `$` — поля действия: `{"run_command":{"command":["structure load obsidian_sword ~ ~ ~","playsound random.fizz @a[r=12] ~ ~ ~","kill @s"]}}`

**`fire_sword_event_2`** (строки 51,229):

- `$` — поля действия: `{"run_command":{"command":["playsound random.fizz @a[r=12] ~ ~ ~ 0.6","particle minecraft:cauldron_explosion_emitter ~ ~ ~","structure load glass_sword ~ ~ ~","kill @s"]}}`

**`fire_sword_event_3`** (строки 230):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"has_tag","value":"fire_sword"},"run_command":{"command":["particle minecraft:mobflame_single ~ ~0.3 ~","particle minecraft:mobflame_single ~1 ~0.3 ~","particle minecraft:mobflame_single ~ ~0.3 ~1","particle minecraft:mobflame_single ~-1 ~0.3 ~","particle minecraft:mobflame_single ~ ~0.3 ~-1","particle minecraft:mobflame_single ~1 ~0.3 ~1","particle minecraft:mobflame_single ~-1 ~0.3 ~-1","particle minecraft:mobflame_single ~1 ~0.3 ~-1","particle minecraft:mobflame_single ~-1 ~0.3 ~1","summon entity:living_flame ~~~ hostile_entity","summon entity:living_flame ~~~ hostile_entity","summon entity:living_flame ~~~ hostile_entity","summon entity:living_flame ~~~ hostile_entity","summon entity:living_flame ~~~ hostile_entity","playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 2","kill @s"]}}`

## `minecraft:lightning_bolt`

- Путь `Swords_B/entities/lightning_bolt.json`; format_version `"1.8.0"`.
- description: `{"identifier":"minecraft:lightning_bolt","is_spawnable":false,"is_summonable":true,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 12,27): `{"family":["lightning"]}`

### Группы компонентов

- `default_lightning_bolt` (строки 11,49,50): `{"minecraft:type_family":{"family":["lightning"]}}`
- `spawn_centella` (строки 15,20,34,38): `{"minecraft:timer":{"time":[0,0],"looping":false,"time_down_event":{"event":"spawn_centella","target":"self"}}}`

### События

**`minecraft:entity_spawned`** (строки 31):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"add":{"component_groups":["spawn_centella"]}}`

**`spawn_centella`** (строки 15,20,34,38):

- `$.randomize`: альтернативы, веса `[80,20]`, сумма 100:
  - ветвь 0, weight `80`; условная доля 4/5 (80%):
    - пустое действие
  - ветвь 1, weight `20`; условная доля 1/5 (20%):
    - `$.randomize[1]` — поля действия: `{"run_command":{"command":["summon entity:centella ~ ~1 ~"]}}`

**`default_lightning_bolt`** (строки 11,49,50):

- `$` — поля действия: `{"add":{"component_groups":["default_lightning_bolt"]}}`

## `entity:lightning_projectile`

- Путь `Swords_B/entities/lightning_projectile.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:lightning_projectile","runtime_identifier":"minecraft:snowball","is_spawnable":false,"is_summonable":true,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:timer` (строки 16): `{"time":[0.1,0.1],"looping":true,"time_down_event":{"event":"despawn","target":"self"}}`
- `minecraft:projectile` (строки 19): `{"on_hit":{"definition_event":{"affect_projectile":true,"event_trigger":{"event":"lightning_bolt","target":"self"}},"impact_damage":{"damage":1,"knockback":true,"destroy_on_hit":true},"particle_on_hit":{}},"hit_sound":"explode","power":2,"gravity":0.0,"angle_offset":0.0}`
- `minecraft:type_family` (строки 40): `{"family":["effect99_entities"]}`
- `minecraft:collision_box` (строки 41): `{"width":0.0,"height":0.0}`
- `minecraft:physics` (строки 42): `{}`
- `minecraft:environment_sensor` (строки 43): `[{"on_environment":{"filters":{"all_of":[{"test":"is_family","value":"effect99_entities"}]},"event":"particle"}}]`

### Группы компонентов

- `despawn` (строки 12,17,51): `{"minecraft:despawn":{}}`

### События

**`despawn`** (строки 12,17,51):

- `$` — поля действия: `{"add":{"component_groups":["despawn"]}}`

**`lightning_bolt`** (строки 24,53):

- `$` — поля действия: `{"run_command":{"command":["summon lightning_bolt ~ ~ ~ default_lightning_bolt"]}}`

## `entity:living_flame`

- Путь `Swords_B/entities/living_flame.json`; format_version `"1.13.0"`.
- description: `{"identifier":"entity:living_flame","is_spawnable":false,"is_summonable":true,"is_experimental":false}`.
- **Повторяющиеся ключи: `["minecraft:fire_immune"]`; следующие выписки могут потерять ранее встреченные значения. Обязательно читать исходник.**

### Постоянные компоненты

- `minecraft:type_family` (строки 15,32,37,79,93,104): `{"family":["living_flame","effect99_entities"]}`
- `minecraft:on_death` (строки 72,84,105): `{"event":"minecraft:start_death","target":"self"}`
- `minecraft:movement` (строки 107): `{"value":0.25}`
- `minecraft:behavior.random_stroll` (строки 109): `{"interval":60,"xz_dist":16}`
- `minecraft:navigation.walk` (строки 113): `{"can_path_over_water":false,"can_path_over_lava":true,"can_walk_in_lava":true,"can_jump":false,"avoid_water":true,"avoid_damage_blocks":false}`
- `minecraft:movement.basic` (строки 121): `{}`
- `minecraft:fire_immune` (строки 123,170): `true`
- `minecraft:nameable` (строки 124): `{"allow_name_tag_renaming":false,"always_show":true}`
- `minecraft:ageable` (строки 126): `{"duration":1,"grow_up":{"event":"hostile_entity_detect","target":"self"}}`
- `minecraft:hurt_on_condition` (строки 133): `{"damage_conditions":[{"filters":{"test":"in_water_or_rain","operator":"==","value":true},"cause":"drowning","damage_per_tick":1}]}`
- `minecraft:jump.static` (строки 138): `{}`
- `minecraft:can_climb` (строки 140): `{}`
- `minecraft:behavior.float` (строки 142): `{"priority":1}`
- `minecraft:attack` (строки 145): `{"damage":3}`
- `minecraft:behavior.melee_attack` (строки 148): `{"priority":4,"target_dist":1.2,"speed_multiplier":1.0,"track_target":true}`
- `minecraft:timer` (строки 16,33,80,94,154): `{"time":[10,40],"looping":true,"randomInterval":true,"time_down_event":{"event":"minecraft:start_death","target":"self"}}`
- `minecraft:behavior.nearest_attackable_target` (строки 26,30,38,65,85,156): `{"priority":2,"entity_types":[{"filters":{"any_of":[{"test":"is_family","subject":"other","value":"monster"},{"test":"is_family","subject":"other","value":"player"}]},"max_dist":16}]}`
- `minecraft:behavior.hurt_by_target` (строки 164): `{"priority":1,"alert_same_type":true}`
- `minecraft:health` (строки 168): `{"value":20}`
- `minecraft:collision_box` (строки 13,78,92,169): `{"width":0.8,"height":1.3}`
- `minecraft:physics` (строки 14,34,171): `{}`
- `minecraft:environment_sensor` (строки 172): `{"triggers":[{"filters":{"all_of":[{"test":"is_family","subject":"self","operator":"!=","value":"fire_sword_skill"},{"test":"is_family","subject":"self","operator":"!=","value":"target"}]},"event":"minecraft:set_fire"}]}`

### Группы компонентов

- `fire_sword_skill` (строки 11,15,176,204,270): `{"minecraft:damage_sensor":{"triggers":{"cause":"all","deals_damage":false}},"minecraft:collision_box":{"width":0.1,"height":0.1},"minecraft:physics":{"has_gravity":false,"has_collision":false},"minecraft:type_family":{"family":["fire_sword_skill","effect99_entities"]},"minecraft:timer":{"time":[10,10],"looping":false,"time_down_event":{"event":"minecraft:despawn","target":"self"}},"minecraft:behavior.ranged_attack":{"attack_interval":0.1,"attack_radius":64},"minecraft:shooter":{"def":"minecraft:small_fireball"},"minecraft:behavior.nearest_attackable_target":{"priority":2,"entity_types":[{"filters":{"test":"is_family","subject":"other","value":"target"},"max_dist":64}]}}`
- `target` (строки 17,27,29,32,33,46,72,80,84,94,105,130,154,177,205,268): `{"minecraft:behavior.nearest_attackable_target":{},"minecraft:damage_sensor":{"triggers":{"cause":"all","deals_damage":false}},"minecraft:type_family":{"family":["target","effect99_entities"]},"minecraft:timer":{"time":[10,10],"looping":false,"time_down_event":{"event":"minecraft:despawn","target":"self"}},"minecraft:physics":{"has_gravity":false,"has_collision":false}}`
- `living_flame_projectile` (строки 36,37,189,203,243,259): `{"minecraft:type_family":{"family":["living_flame","living_flame_projectile","effect99_entities"]},"minecraft:behavior.nearest_attackable_target":{},"minecraft:damage_sensor":{"triggers":{"cause":"all","deals_damage":false}},"minecraft:projectile":{"on_hit":{"definition_event":{"affect_projectile":true,"event_trigger":{"event":"minecraft:stop_projectile","target":"self"}},"impact_damage":{"damage":1,"knockback":true,"catch_fire":true}},"power":1,"gravity":0.02,"inertia":1,"liquid_inertia":1}}`
- `despawn` (строки 61,221,233,266): `{"minecraft:despawn":{}}`
- `hostile_entity` (строки 64,194,195,208,259): `{"minecraft:behavior.nearest_attackable_target":{"priority":1,"entity_types":[{"filters":{"any_of":[{"test":"is_family","subject":"other","value":"monster"},{"test":"is_family","subject":"other","value":"player"}]},"max_dist":16}]},"minecraft:on_death":{"event":"start_death_hostile","target":"self"},"minecraft:damage_sensor":{"triggers":{"on_damage":{"filters":{"all_of":[{"test":"is_family","subject":"other","value":"player"}]},"event":"start_death_hostile"},"deals_damage":false}},"minecraft:collision_box":{"width":0.8,"height":1.3},"minecraft:type_family":{"family":["living_flame","living_flame_hostile","effect99_entities"]},"minecraft:timer":{"time":[25,60],"looping":true,"randomInterval":true,"time_down_event":{"event":"minecraft:start_death","target":"self"}}}`
- `passive_entity` (строки 83,262): `{"minecraft:on_death":{"event":"minecraft:start_death","target":"self"},"minecraft:behavior.nearest_attackable_target":{"entity_types":[{"filters":{"any_of":[{"test":"is_family","subject":"other","value":"monster"}]},"max_dist":16}]},"minecraft:collision_box":{"width":0.8,"height":1.3},"minecraft:type_family":{"family":["living_flame","living_flame_passive","effect99_entities"]},"minecraft:timer":{"time":[10,30],"looping":true,"randomInterval":true,"time_down_event":{"event":"minecraft:start_death","target":"self"}},"minecraft:damage_sensor":{"triggers":{"on_damage":{"filters":{"all_of":[{"test":"is_family","subject":"other","value":"player"}]},"event":"minecraft:start_death"},"deals_damage":false}}}`

### События

**`minecraft:entity_spawned`** (строки 184):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"has_equipment","subject":"other","domain":"hand","value":"effect:fire_sword"},"add":{"component_groups":["living_flame_projectile"]}}`

**`hostile_entity`** (строки 64,194,195,208,259):

- `$` — поля действия: `{"add":{"component_groups":["hostile_entity"]}}`

**`hostile_entity_detect`** (строки 129,197):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"all_of":[{"test":"is_family","subject":"self","operator":"!=","value":"living_flame_hostile"},{"test":"is_family","subject":"self","operator":"!=","value":"living_flame_passive"},{"test":"is_family","subject":"self","operator":"!=","value":"living_flame_projectile"},{"test":"is_family","subject":"self","operator":"!=","value":"fire_sword_skill"},{"test":"is_family","subject":"self","operator":"!=","value":"target"}]},"add":{"component_groups":["hostile_entity"]}}`

**`minecraft:set_fire`** (строки 178,212):

- `$` — поля действия: `{"run_command":{"command":["fill ~ ~ ~ ~ ~ ~ fire 0 replace air","particle minecraft:basic_flame_particle ~ ~1 ~"]}}`

**`minecraft:start_death`** (строки 80,84,94,97,105,154,220):

- `$` — поля действия: `{"add":{"component_groups":["despawn"]},"run_command":{"command":["fill ~ ~ ~ ~ ~ ~ air 0 replace fire","particle minecraft:example_linearcurve ~ ~0.4 ~","playsound random.fizz @a[r=12] ~ ~ ~"]}}`

**`start_death_hostile`** (строки 72,74,230):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"add":{"component_groups":["despawn"]},"run_command":{"command":["fill ~ ~ ~ ~ ~ ~ air 0 replace fire","particle minecraft:example_linearcurve ~ ~0.4 ~","playsound random.fizz @a[r=12] ~ ~ ~"]}}`
  - `$.sequence[1]` — поля действия: `{"filters":{"all_of":[{"test":"is_family","subject":"self","operator":"!=","value":"living_flame_passive"},{"test":"is_family","subject":"self","operator":"!=","value":"living_flame_projectile"}]}}`
  - `$.sequence[1].randomize`: альтернативы, веса `[85,15]`, сумма 100:
    - ветвь 0, weight `85`; условная доля 17/20 (85%):
      - пустое действие
    - ветвь 1, weight `15`; условная доля 3/20 (15%):
      - `$.sequence[1].randomize[1]` — поля действия: `{"run_command":{"command":["loot spawn ~ ~ ~ loot \"entities/living_flame\""]}}`

**`minecraft:stop_projectile`** (строки 45,256):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"remove":{"component_groups":["hostile_entity","living_flame_projectile"]}}`
  - `$.sequence[1]` — поля действия: `{"add":{"component_groups":["passive_entity"]}}`

**`minecraft:despawn`** (строки 17,33,62,266):

- `$` — поля действия: `{"add":{"component_groups":["despawn"]}}`

**`minecraft:target`** (строки 268):

- `$` — поля действия: `{"add":{"component_groups":["target"]}}`

**`fire_sword_skill`** (строки 11,15,176,204,270):

- `$` — поля действия: `{"add":{"component_groups":["fire_sword_skill"]}}`

## `entity:mountable_slime`

- Путь `Swords_B/entities/mountable_slime.json`; format_version `"1.13.0"`.
- description: `{"identifier":"entity:mountable_slime","runtime_identifier":"minecraft:slime","is_spawnable":false,"is_summonable":true,"is_experimental":false,"scripts":{"animate":["despawn","mountable_slime"]},"animations":{"despawn":"controller.animation.despawn","mountable_slime":"controller.animation.mountable_slime"}}`.
- **Повторяющиеся ключи: `["despawn"]`; следующие выписки могут потерять ранее встреченные значения. Обязательно читать исходник.**

### Постоянные компоненты

- `minecraft:environment_sensor` (строки 67,150): `{"triggers":[{"filters":{},"event":"minecraft:is_jumping"}]}`
- `minecraft:damage_sensor` (строки 158): `{"triggers":[{"on_damage":{"filters":{"all_of":[{"test":"has_damage","subject":"self","value":"fall"}]},"event":"fall_damage"},"deals_damage":false},{"on_damage":{"filters":{"all_of":[{"test":"has_damage","subject":"self","operator":"!=","value":"void"}]}},"deals_damage":false}]}`

### Группы компонентов

- `despawn` (строки 11,14,19,144,180,182): `{"minecraft:despawn":{}}`
- `minecraft:is_jumping` (строки 22,71,154,202,225,227): `{"minecraft:is_baby":{}}`
- `slime_random_direction` (строки 26,222): `{"minecraft:behavior.slime_random_direction":{"priority":4}}`
- `default_slime` (строки 31,176,220): `{"minecraft:behavior.slime_float":{"priority":1},"minecraft:behavior.slime_keep_on_jumping":{"priority":5},"minecraft:movement":{"value":0.25},"minecraft:movement.jump":{"jump_delay":[0.16,0.5]},"minecraft:navigation.walk":{"can_path_over_water":true},"minecraft:jump.static":{},"minecraft:can_climb":{},"minecraft:type_family":{"family":["effect99_entities","tamed_slime"]},"minecraft:health":{"value":1},"minecraft:collision_box":{"width":0.6,"height":0.0},"minecraft:physics":{},"minecraft:rideable":{"crouching_skip_interact":true,"seat_count":1,"family_types":["player"],"seats":{"position":[0.0,0.35,0.0]}},"minecraft:input_ground_controlled":{},"minecraft:behavior.controlled_by_player":{"priority":0},"minecraft:can_power_jump":{},"minecraft:horse.jump_strength":{"value":{"range_min":0.8,"range_max":2.0}},"minecraft:is_tamed":{}}`
- `defense_mode_slime` (строки 52,178): `{"minecraft:type_family":{"family":["effect99_entities","tamed_slime","player"]},"minecraft:movement":{"value":0.45},"minecraft:behavior.slime_attack":{"priority":3,"set_persistent":true},"minecraft:behavior.slime_random_direction":{"priority":4},"minecraft:behavior.slime_keep_on_jumping":{"priority":5},"minecraft:environment_sensor":{"triggers":[{"filters":{},"event":"minecraft:is_jumping"},{"filters":{},"event":"slime_events"}]},"minecraft:behavior.nearest_attackable_target":{"priority":1,"entity_types":[{"filters":{"any_of":[{"test":"is_family","subject":"other","value":"monster"},{"test":"is_family","subject":"other","value":"undead"}]},"max_dist":16}],"must_see":true,"set_persistent":true,"must_reach":false},"minecraft:attack":{"damage":1}}`
- `minecraft:slime_large` (строки 108): `{"minecraft:type_family":{"family":["effect99_entities","slime3","tamed_slime"]},"minecraft:rideable":{"crouching_skip_interact":true,"seat_count":1,"family_types":["player"],"seats":{"position":[0.0,1.9,0.0]}},"minecraft:collision_box":{"width":0.4,"height":0.0},"minecraft:movement":{"value":0.25},"minecraft:scale":{"value":0.4}}`
- `minecraft:slime_medium` (строки 120): `{"minecraft:type_family":{"family":["effect99_entities","slime2","tamed_slime"]},"minecraft:rideable":{"crouching_skip_interact":true,"seat_count":1,"family_types":["player"],"seats":{"position":[0.0,0.9,0.0]}},"minecraft:collision_box":{"width":0.4,"height":0.0},"minecraft:movement":{"value":0.25},"minecraft:scale":{"value":0.8}}`
- `minecraft:slime_small` (строки 132): `{"minecraft:type_family":{"family":["effect99_entities","slime1","tamed_slime"]},"minecraft:rideable":{"crouching_skip_interact":true,"seat_count":1,"family_types":["player"],"seats":{"position":[0.0,0.46,0.0]}},"minecraft:collision_box":{"width":0.4,"height":0.0},"minecraft:movement":{"value":0.25},"minecraft:scale":{"value":1.5}}`

### События

**`minecraft:entity_spawned`** (строки 175):

- `$` — поля действия: `{"add":{"component_groups":["default_slime"]}}`

**`minecraft:despawn`** (строки 20,145,178):

- `$` — поля действия: `{"add":{"component_groups":["defense_mode_slime"]}}`

**`despawn`** (строки 11,14,19,144,180,182):

- `$` — поля действия: `{"add":{"component_groups":["despawn"]},"run_command":{"command":["particle minecraft:crop_growth_emitter ~ ~ ~","particle minecraft:crop_growth_emitter ~ ~0.6 ~","particle minecraft:crop_growth_emitter ~ ~-0.6 ~","particle minecraft:crop_growth_emitter ~0.6 ~ ~","particle minecraft:crop_growth_emitter ~ ~ ~0.6","particle minecraft:crop_growth_emitter ~-0.6 ~ ~","particle minecraft:crop_growth_emitter ~ ~ ~-0.6","playsound random.orb @a[r=12] ~ ~ ~ 1 0.6"]}}`

**`fall_damage`** (строки 162,197):

- `$` — поля действия: `{"run_command":{"command":["effect @e[r=1,family=!slime_sword,family=!undead] instant_damage 1 1 true","effect @e[r=1,family=undead] instant_health 3 1 true","event entity @s not_baby"]}}`

**`minecraft:is_jumping`** (строки 22,71,154,202,225,227):

- `$` — поля действия: `{"run_command":{"command":["execute @s ~~~ detect ~ ~-1 ~ air 0 execute @s ~~~ detect ~ ~-2 ~ air 0 event entity @s is_baby"]}}`

**`slime_events`** (строки 75,209):

- `$` — поля действия: `{"run_command":{"command":["effect @s jump_boost 1 2 true","execute @e[r=1,family=monster] ~~~ summon entity:slime_damage","tp @s[scores={slime_despawn=0}] @e[type=player,family=slime_sword,c=1,rm=8,r=12]","scoreboard players add @s slime_despawn 1","execute @s[scores={slime_despawn=100}] ~~~ event entity @s despawn"]}}`

**`default_slime`** (строки 31,176,220):

- `$` — поля действия: `{"remove":{"component_groups":["slime_random_direction"]}}`

**`is_baby`** (строки 225):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:is_jumping"]}}`

**`not_baby`** (строки 227):

- `$` — поля действия: `{"remove":{"component_groups":["minecraft:is_jumping"]}}`

## `entity:nether_star_projectile`

- Путь `Swords_B/entities/nether_star_projectile.json`; format_version `"1.13.0"`.
- description: `{"identifier":"entity:nether_star_projectile","runtime_identifier":"minecraft:snowball","is_spawnable":false,"is_summonable":true,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 47): `{"family":["effect99_entities","nether_star_projectile"]}`
- `minecraft:timer` (строки 16,49): `{"time":[5,5],"looping":true,"time_down_event":{"event":"minecraft:despawn","target":"self"}}`
- `minecraft:collision_box` (строки 52): `{"width":1,"height":1}`
- `minecraft:projectile` (строки 22,56): `{"on_hit":{"definition_event":{"affect_projectile":true,"event_trigger":{"event":"set_sound","target":"self"}},"impact_damage":{"damage":6,"knockback":true,"destroy_on_hit":true},"remove_on_hit":{}},"power":1,"gravity":0,"angle_offset":0.0}`
- `minecraft:environment_sensor` (строки 20,76): `{"triggers":[{"filters":{},"event":"set_particle"}]}`
- `minecraft:physics` (строки 84): `{}`
- `minecraft:pushable` (строки 86): `{"is_pushable":false,"is_pushable_by_piston":false}`

### Группы компонентов

- `nether_star_sword` (строки 12,96): `{"minecraft:scale":{"value":0.0},"minecraft:timer":{"time":[0.1,0.1],"looping":true,"time_down_event":{"event":"minecraft:despawn","target":"self"}},"minecraft:environment_sensor":{},"minecraft:projectile":{"on_hit":{"definition_event":{"affect_projectile":true,"event_trigger":{"event":"set_objective","target":"self"}},"impact_damage":{"damage":-1,"knockback":false,"destroy_on_hit":true},"remove_on_hit":{}},"power":5,"gravity":0,"angle_offset":0.0}}`
- `despawn` (строки 43,138): `{"minecraft:despawn":{}}`

### События

**`minecraft:entity_spawned`** (строки 92):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"has_equipment","subject":"other","domain":"hand","value":"effect:nether_star_sword"},"add":{"component_groups":["nether_star_sword"]}}`

**`set_objective`** (строки 27,101):

- `$` — поля действия: `{"run_command":{"command":["summon entity:objective"]}}`

**`set_sound`** (строки 61,106):

- `$.randomize`: альтернативы, веса `[1,1,1]`, сумма 3:
  - ветвь 0, weight `1`; условная доля 1/3 (33.3333%):
    - `$.randomize[0]` — поля действия: `{"run_command":{"command":["playsound item.trident.thunder @a[r=20] ~ ~ ~ 1 5.5"]}}`
  - ветвь 1, weight `1`; условная доля 1/3 (33.3333%):
    - `$.randomize[1]` — поля действия: `{"run_command":{"command":["playsound item.trident.thunder @a[r=20] ~ ~ ~ 1 6"]}}`
  - ветвь 2, weight `1`; условная доля 1/3 (33.3333%):
    - `$.randomize[2]` — поля действия: `{"run_command":{"command":["playsound item.trident.thunder @a[r=20] ~ ~ ~ 1 7"]}}`

**`set_particle`** (строки 80,128):

- `$` — поля действия: `{"run_command":{"command":["particle minecraft:nether_star_hit ~ ~2.5 ~"]}}`

**`objective`** (строки 133,135):

- `$` — поля действия: `{"add":{"component_groups":["objective"]}}`

**`minecraft:despawn`** (строки 17,43,50,138):

- `$` — поля действия: `{"add":{"component_groups":["despawn"]}}`

## `entity:objective`

- Путь `Swords_B/entities/objective.json`; format_version `"1.13.0"`.
- description: `{"identifier":"entity:objective","is_spawnable":false,"is_summonable":true,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 15): `{"family":["effect99_entities","objective"]}`
- `minecraft:timer` (строки 17): `{"time":[1,1],"looping":true,"time_down_event":{"event":"minecraft:despawn","target":"self"}}`
- `minecraft:damage_sensor` (строки 20): `{"triggers":{"cause":"all","deals_damage":false}}`
- `minecraft:collision_box` (строки 26): `{"width":0.25,"height":0.25}`
- `minecraft:physics` (строки 30): `{"has_gravity":false,"has_collision":false}`
- `minecraft:environment_sensor` (строки 34): `{"triggers":[{"filters":{},"event":"follow_entity"}]}`
- `minecraft:pushable` (строки 42): `{"is_pushable":false,"is_pushable_by_piston":true}`

### Группы компонентов

- `despawn` (строки 11,53): `{"minecraft:despawn":{}}`

### События

**`follow_entity`** (строки 38,48):

- `$` — поля действия: `{"run_command":{"command":["tp @s @e[r=8,c=1,type=!player,type=!item,family=!parrot_tame,family=!tamed,type=!arrow,type=!xp_orb,family=!effect99_entities]"]}}`

**`minecraft:despawn`** (строки 11,18,53):

- `$` — поля действия: `{"add":{"component_groups":["despawn"]}}`

## `minecraft:parrot`

- Путь `Swords_B/entities/parrot.json`; format_version `"1.13.0"`.
- description: `{"identifier":"minecraft:parrot","is_spawnable":true,"is_summonable":true,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:behavior.tempt` (строки 100): `{"speed_multiplier":1.0,"items":["effect:jungle_sword"]}`
- `minecraft:breathable` (строки 106): `{"total_supply":15,"suffocate_time":0}`
- `minecraft:collision_box` (строки 110): `{"width":0.5,"height":1}`
- `minecraft:nameable` (строки 114): `{}`
- `minecraft:health` (строки 116): `{"value":6,"max":6}`
- `minecraft:hurt_on_condition` (строки 120): `{"damage_conditions":[{"filters":{"test":"in_lava","subject":"self","operator":"==","value":true},"cause":"lava","damage_per_tick":4}]}`
- `minecraft:movement` (строки 129): `{"value":0.4}`
- `minecraft:damage_sensor` (строки 132): `{"triggers":{"cause":"fall","deals_damage":false}}`
- `minecraft:jump.static` (строки 138): `{}`
- `minecraft:can_fly` (строки 140): `{}`
- `minecraft:navigation.fly` (строки 142): `{"can_path_over_water":true}`
- `minecraft:movement.fly` (строки 145): `{}`
- `minecraft:physics` (строки 147): `{}`
- `minecraft:pushable` (строки 149): `{"is_pushable":true,"is_pushable_by_piston":true}`
- `minecraft:behavior.float` (строки 153): `{"priority":0}`
- `minecraft:behavior.panic` (строки 156): `{"priority":0,"speed_multiplier":1.25}`
- `minecraft:behavior.look_at_player` (строки 160): `{"priority":1,"look_distance":8.0}`
- `minecraft:healable` (строки 164): `{"force_use":true,"filters":{"test":"is_riding","operator":"!=","value":true},"items":[{"item":"cookie","heal_amount":0,"effects":[{"name":"fatal_poison","chance":1.0,"duration":1000,"amplifier":0}]}]}`

### Группы компонентов

- `minecraft:parrot_red` (строки 12,191): `{"minecraft:variant":{"value":0}}`
- `minecraft:parrot_blue` (строки 15,201): `{"minecraft:variant":{"value":1}}`
- `minecraft:parrot_green` (строки 18,211): `{"minecraft:variant":{"value":2}}`
- `minecraft:parrot_cyan` (строки 21,221): `{"minecraft:variant":{"value":3}}`
- `minecraft:parrot_silver` (строки 24,231): `{"minecraft:variant":{"value":4}}`
- `minecraft:parrot_adult` (строки 28,192,202,212,222,232): `{"minecraft:experience_reward":{"on_death":"query.last_hit_by_player ? Math.Random(1,3) : 0"},"minecraft:loot":{"table":"loot_tables/entities/parrot.json"}}`
- `minecraft:parrot_wild` (строки 37,193,203,213,223,233,242): `{"minecraft:type_family":{"family":["parrot_wild","mob"]},"minecraft:tameable":{"probability":0.33,"tame_items":["wheat_seeds","pumpkin_seeds","melon_seeds","beetroot_seeds"],"tame_event":{"event":"minecraft:on_tame","target":"self"}},"minecraft:behavior.random_fly":{"priority":2,"xz_dist":15,"y_dist":1,"y_offset":0,"speed_multiplier":1.0,"can_land_on_trees":true,"avoid_damage_blocks":true},"minecraft:behavior.follow_mob":{"priority":3,"speed_multiplier":1.0,"stop_distance":3,"search_range":20}}`
- `minecraft:parrot_tame` (строки 71,247): `{"minecraft:type_family":{"family":["parrot_tame","mob"]},"minecraft:is_tamed":{},"minecraft:behavior.follow_owner":{"priority":2,"speed_multiplier":1.0,"start_distance":5,"stop_distance":1},"minecraft:sittable":{},"minecraft:behavior.stay_while_sitting":{"priority":1},"minecraft:behavior.find_mount":{"priority":3,"within_radius":16,"avoid_water":true,"start_delay":100,"target_needed":false,"mount_distance":2.0}}`

### События

**`minecraft:entity_spawned`** (строки 185):

- `$.randomize`: альтернативы, веса `[20,20,20,20,20]`, сумма 100:
  - ветвь 0, weight `20`; условная доля 1/5 (20%):
    - `$.randomize[0]` — поля действия: `{"add":{"component_groups":["minecraft:parrot_red","minecraft:parrot_adult","minecraft:parrot_wild"]}}`
  - ветвь 1, weight `20`; условная доля 1/5 (20%):
    - `$.randomize[1]` — поля действия: `{"add":{"component_groups":["minecraft:parrot_blue","minecraft:parrot_adult","minecraft:parrot_wild"]}}`
  - ветвь 2, weight `20`; условная доля 1/5 (20%):
    - `$.randomize[2]` — поля действия: `{"add":{"component_groups":["minecraft:parrot_green","minecraft:parrot_adult","minecraft:parrot_wild"]}}`
  - ветвь 3, weight `20`; условная доля 1/5 (20%):
    - `$.randomize[3]` — поля действия: `{"add":{"component_groups":["minecraft:parrot_cyan","minecraft:parrot_adult","minecraft:parrot_wild"]}}`
  - ветвь 4, weight `20`; условная доля 1/5 (20%):
    - `$.randomize[4]` — поля действия: `{"add":{"component_groups":["minecraft:parrot_silver","minecraft:parrot_adult","minecraft:parrot_wild"]}}`

**`minecraft:on_tame`** (строки 50,239):

- `$` — поля действия: `{"remove":{"component_groups":["minecraft:parrot_wild"]},"add":{"component_groups":["minecraft:parrot_tame"]}}`

## `minecraft:player`

- Путь `Swords_B/entities/player.json`; format_version `"1.11.0"`.
- description: `{"identifier":"minecraft:player","is_spawnable":false,"is_summonable":false,"is_experimental":false,"scripts":{"animate":["shulker_sword","wither_sword","wolf_sword_0","wolf_sword_1","wolf_sword_2","ghost_sword"]},"animations":{"shulker_sword":"controller.animation.shulker_sword","wither_sword":"controller.animation.wither_sword","wolf_sword_1":"controller.animation.start_wolf_sword","wolf_sword_2":"controller.animation.end_wolf_sword","wolf_sword_0":"controller.animation.wolf_sword","ghost_sword":"controller.animation.ghost_sword"}}`.

### Постоянные компоненты

- `minecraft:experience_reward` (строки 519): `{"on_death":"Math.Min(query.player_level * 7, 100)"}`
- `minecraft:type_family` (строки 26,33,36,42,62,68,71,90,142,179,189,204,208,214,217,226,230,239,242,260,273,284,292,297,303,311,314,318,332,335,344,350,370,376,440,522): `{"family":["player","default_player"]}`
- `minecraft:is_hidden_when_invisible` (строки 525): `{}`
- `minecraft:loot` (строки 527): `{"table":"loot_tables/empty.json"}`
- `minecraft:collision_box` (строки 54,263,436,530): `{"width":0.6,"height":1.8}`
- `minecraft:can_climb` (строки 534): `{}`
- `minecraft:movement` (строки 45,65,93,145,207,211,276,338,443,536): `{"value":0.1}`
- `minecraft:hurt_on_condition` (строки 170,361,539): `{"damage_conditions":[{"filters":{"test":"in_lava","subject":"self","operator":"==","value":true},"cause":"lava","damage_per_tick":4}]}`
- `minecraft:attack` (строки 87,433,548): `{"damage":1}`
- `minecraft:player.saturation` (строки 551): `{"value":20}`
- `minecraft:player.exhaustion` (строки 554): `{"value":0,"max":4}`
- `minecraft:player.level` (строки 558): `{"value":0,"max":24791}`
- `minecraft:player.experience` (строки 562): `{"value":0,"max":1}`
- `minecraft:breathable` (строки 57,270,453,566): `{"total_supply":15,"suffocate_time":-1,"inhale_time":3.75,"generates_bubbles":false}`
- `minecraft:nameable` (строки 572): `{"always_show":true,"allow_name_tag_renaming":false}`
- `minecraft:physics` (строки 426,576): `{}`
- `minecraft:pushable` (строки 578): `{"is_pushable":false,"is_pushable_by_piston":true}`
- `minecraft:insomnia` (строки 582): `{"days_until_insomnia":3}`
- `minecraft:rideable` (строки 192,255,459,585): `{"seat_count":2,"family_types":["parrot_tame"],"pull_in_entities":true,"seats":[{"position":[0.4,-0.2,-0.1],"min_rider_count":0,"max_rider_count":0,"lock_rider_rotation":0},{"position":[-0.4,-0.2,-0.1],"min_rider_count":1,"max_rider_count":2,"lock_rider_rotation":0}]}`
- `minecraft:scaffolding_climber` (строки 606): `{}`
- `minecraft:environment_sensor` (строки 607): `[{"on_environment":{"filters":{"all_of":[{"test":"has_mob_effect","subject":"self","value":"bad_omen"},{"test":"is_in_village","subject":"self","value":true}]},"event":"minecraft:trigger_raid"}},{"on_environment":{"filters":{"test":"is_family","operator":"!=","value":"null"},"event":"minecraft:constant_events"}},{"on_environment":{"filters":{"any_of":[{"test":"is_family","subject":"self","value":"default_player"},{"test":"is_family","subject":"self","operator":"!=","value":"spectral_sword"}]},"event":"minecraft:stop_sword_events"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:blaze_sword"}]},"event":"minecraft:blaze_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:blaze_sword"}]},"event":"stop_blaze_sword_event"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:bone_sword"}]},"event":"minecraft:bone_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:bone_sword"}]},"event":"stop_bone_sword_event"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:cactus_sword"}]},"event":"minecraft:cactus_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:cactus_sword"}]},"event":"stop_cactus_sword_event"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:emerald_sword"}]},"event":"minecraft:emerald_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:emerald_sword"}]},"event":"stop_emerald_sword_event"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:fire_sword"}]},"event":"minecraft:fire_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:fire_sword"}]},"event":"stop_fire_sword_event"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:grass_sword"}]},"event":"minecraft:grass_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:grass_sword"}]},"event":"stop_grass_sword_event"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:jungle_sword"}]},"event":"minecraft:jungle_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:jungle_sword"}]},"event":"stop_jungle_sword_event"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:magma_sword"}]},"event":"minecraft:magma_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:magma_sword"}]},"event":"stop_magma_sword_event"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:ice_sword"}]},"event":"minecraft:ice_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:ice_sword"}]},"event":"stop_ice_sword_event"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:lapis_sword"}]},"event":"minecraft:lapis_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:lapis_sword"}]},"event":"stop_lapis_sword_event"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:obsidian_sword"}]},"event":"minecraft:obsidian_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:obsidian_sword"}]},"event":"stop_obsidian_sword_event"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:quartz_sword"}]},"event":"minecraft:quartz_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:quartz_sword"}]},"event":"stop_quartz_sword_event"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:sea_sword"}]},"event":"minecraft:sea_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:sea_sword"}]},"event":"stop_sea_sword_event"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:spectral_sword"}]},"event":"minecraft:spectral_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:spectral_sword"}]},"event":"stop_spectral_sword_event"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:slime_sword"}]},"event":"minecraft:slime_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:slime_sword"}]},"event":"stop_slime_sword_event"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:shulker_sword"}]},"event":"minecraft:shulker_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:shulker_sword"}]},"event":"stop_shulker_sword_event"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:spider_sword"}]},"event":"minecraft:spider_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:spider_sword"}]},"event":"stop_spider_sword_event"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:sponge_sword"}]},"event":"minecraft:sponge_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:sponge_sword"}]},"event":"stop_sponge_sword_event"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:time_sword"}]},"event":"minecraft:time_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:time_sword"}]},"event":"stop_time_sword_event"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:wither_sword"}]},"event":"minecraft:wither_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:wither_sword"}]},"event":"stop_wither_sword_event"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:glowstone_sword"}]},"event":"minecraft:glowstone_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:lightning_sword"}]},"event":"minecraft:lightning_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:lightning_sword"}]},"event":"stop_lightning_sword_event"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:ender_sword"}]},"event":"minecraft:ender_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:ender_sword"}]},"event":"stop_ender_sword_event"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:ultra_instinct_sword"}]},"event":"minecraft:ultra_instinct_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:ultra_instinct_sword"}]},"event":"stop_ultra_instinct_sword_event"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:wolf_sword"}]},"event":"minecraft:wolf_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:wolf_sword"}]},"event":"stop_wolf_sword_event"}},{"on_environment":{"filters":{"all_of":[{"test":"is_family","value":"wolf_transformation"}]},"event":"starting_wolf_transformation"}},{"on_environment":{"filters":{"all_of":[{"test":"is_family","value":"complete_wolf_transformation"}]},"event":"wolf_movement"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:ghost_sword"}]},"event":"minecraft:ghost_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:ghost_sword"}]},"event":"stop_ghost_sword_event"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:clock_sword"}]},"event":"minecraft:clock_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:clock_sword"}]},"event":"stop_clock_sword_event"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:nether_star_sword"}]},"event":"minecraft:nether_star_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:nether_star_sword"}]},"event":"stop_nether_star_sword_event"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:bee_sword"}]},"event":"minecraft:bee_sword"}},{"on_environment":{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:bee_sword"}]},"event":"stop_bee_sword_event"}}]`

### Группы компонентов

- `minecraft:bee_sword` (строки 22,1043,1125,1129,1137): `{"minecraft:timer":{"time":[3,8],"looping":true,"randomInterval":true,"time_down_event":{"event":"bee_sword_flower","target":"self"}},"minecraft:type_family":{"family":["player","bee_sword"]}}`
- `minecraft:nether_star_sword` (строки 28,1029,1161,1165,1173): `{"minecraft:damage_sensor":{"triggers":{"on_damage":{"filters":{"all_of":[{"test":"is_family","subject":"other","value":"nether_star_projectile"}]}},"deals_damage":false}},"minecraft:type_family":{"family":["player","nether_star_sword"]}}`
- `minecraft:clock_sword` (строки 35,1015,1178,1182,1202): `{"minecraft:type_family":{"family":["player","clock_sword"]}}`
- `clock_sword_skill` (строки 38,42,1185,1210): `{"minecraft:timer":{"time":[5,5],"looping":true,"randomInterval":false,"time_down_event":{"event":"stop_clock_sword_event","target":"self"}},"minecraft:type_family":{"family":["player","clock_sword","clock_sword_skill"]}}`
- `clock_sword_movement` (строки 44,1186,1213,1214): `{"minecraft:movement":{"value":1}}`
- `minecraft:ghost_sword` (строки 47,1001,1216,1220,1265): `{"minecraft:scale":{"value":1.05},"minecraft:knockback_resistance":{"value":1.0},"minecraft:collision_box":{"width":0.0,"height":0.0},"minecraft:breathable":{"total_supply":15,"suffocate_time":0,"inhale_time":3.75,"generates_bubbles":false,"breathes_water":true,"breathes_air":true,"breathes_lava":true},"minecraft:damage_sensor":{"triggers":{"cause":"all","deals_damage":false}},"minecraft:type_family":{"family":["ghost_sword"]}}`
- `ghost_movement` (строки 64,1234): `{"minecraft:movement":{"value":0.14}}`
- `minecraft:wolf_sword` (строки 67,973,1283,1287,1296,1356): `{"minecraft:type_family":{"family":["player","wolf_sword"]}}`
- `wolf_transformation` (строки 70,71,985,1296,1311,1312,1319,1335,1336,1355): `{"minecraft:type_family":{"family":["player","wolf_sword","wolf_transformation"]}}`
- `complete_wolf_transformation` (строки 73,90,992,1301,1302,1322,1332,1355): `{"minecraft:damage_sensor":{"triggers":[{"on_damage":{"filters":{"all_of":[{"test":"has_damage","operator":"!=","value":"void"}]},"event":"wolf_damage_sound"},"deals_damage":true}]},"minecraft:timer":{"time":[3,6],"looping":true,"randomInterval":true,"time_down_event":{"event":"wolf_sword_sounds","target":"self"}},"minecraft:attack":{"damage":15},"minecraft:type_family":{"family":["wolf","wolf_sword","complete_wolf_transformation","monster"]}}`
- `wolf_movement` (строки 92,994,1296,1340,1355): `{"minecraft:movement":{"value":0.18}}`
- `minecraft:ultra_instinct_sword` (строки 95,959,1360,1364,1389): `{"minecraft:knockback_resistance":{"value":1.0},"minecraft:timer":{"time":[0.1,0.2],"looping":true,"randomInterval":true,"time_down_event":{"event":"ultra_instinct_sword_effects","target":"self"}},"minecraft:damage_sensor":{"triggers":[{"on_damage":{"filters":{"all_of":[{"test":"has_damage","operator":"!=","value":"lava"},{"test":"has_damage","operator":"!=","value":"drowning"},{"test":"has_damage","operator":"!=","value":"void"},{"test":"has_damage","operator":"!=","value":"thorns"},{"test":"has_damage","operator":"!=","value":"suicide"},{"test":"has_damage","operator":"!=","value":"starve"},{"test":"has_damage","operator":"!=","value":"fire"},{"test":"has_damage","operator":"!=","value":"fire_tick"},{"test":"has_damage","operator":"!=","value":"magic"}]},"event":"ultra_instinct_sword_skill"},"deals_damage":false},{"on_damage":{"filters":{"test":"has_damage","value":"fire"}},"deals_damage":false},{"on_damage":{"filters":{"test":"has_damage","value":"fire_tick"}},"deals_damage":false},{"on_damage":{"filters":{"any_of":[{"test":"has_damage","value":"block_explosion"},{"test":"has_damage","value":"entity_explosion"}]}},"deals_damage":false},{"on_damage":{"filters":{"all_of":[{"test":"has_damage","value":"lava"}]}},"deals_damage":true}]},"minecraft:type_family":{"family":["player","ultra_instinct_sword"]}}`
- `ultra_instinct_sword_movement` (строки 144,1381,1389): `{"minecraft:movement":{"value":0.22}}`
- `minecraft:ender_sword` (строки 147,945,1416,1420,1432): `{"minecraft:damage_sensor":{"triggers":[{"on_damage":{"filters":{"all_of":[{"test":"has_damage","subject":"self","operator":"!=","value":"projectile"}]},"event":"ender_sword_skill"},"deals_damage":true},{"on_damage":{"filters":{"all_of":[{"test":"has_damage","subject":"self","value":"projectile"}]},"event":"ender_sword_tp"},"deals_damage":false},{"on_damage":{"filters":{"all_of":[{"test":"in_water_or_rain"}]},"event":"ender_sword_tp"},"deals_damage":true}]},"minecraft:hurt_on_condition":{"damage_conditions":[{"filters":{"test":"in_water_or_rain"},"cause":"drowning","damage_per_tick":1}]},"minecraft:type_family":{"family":["player","ender_sword"]},"minecraft:timer":{"time":[6,18],"looping":true,"randomInterval":true,"time_down_event":{"event":"ender_sword_sound","target":"self"}}}`
- `minecraft:lightning_sword` (строки 184,931,1468,1472,1484): `{"minecraft:damage_sensor":{"triggers":{"on_damage":{"filters":{"all_of":[{"test":"is_family","subject":"other","value":"lightning"}]}},"deals_damage":false}},"minecraft:type_family":{"family":["player","lightning_sword"]}}`
- `minecraft:wither_sword` (строки 191,910,1492,1496,1525): `{"minecraft:rideable":{"seat_count":1,"family_types":["entity_name"],"seats":{"position":[0.0,0.4,0.0],"lock_rider_rotation":0}},"minecraft:damage_sensor":{"triggers":{"on_damage":{"filters":{"all_of":[{"test":"has_damage","subject":"self","value":"wither"}]}},"deals_damage":false}},"minecraft:timer":{"time":[4,18],"looping":true,"randomInterval":true,"time_down_event":{"event":"wither_sword_effects","target":"self"}},"minecraft:type_family":{"family":["player","wither_sword"]}}`
- `minecraft:time_sword` (строки 206,896,1537,1540,1551): `{"minecraft:movement":{"value":1},"minecraft:type_family":{"family":["player","time_sword"]}}`
- `time_sword_movement` (строки 210,1557,1558): `{"minecraft:movement":{"value":1}}`
- `minecraft:sponge_sword` (строки 213,882,1560,1564,1603): `{"minecraft:type_family":{"family":["player","sponge_sword"]}}`
- `minecraft:spider_sword` (строки 216,868,1608,1612,1621,1632): `{"minecraft:type_family":{"family":["player","spider_sword"]}}`
- `spider_sword_skill` (строки 219,226,1621,1630,1631,1636,1639,1640): `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"single_use":false,"spawn_entity":"entity:web","num_to_spawn":1}],"minecraft:timer":{"time":[2,2],"looping":false,"time_down_event":{"event":"stop_spider_skill_event","target":"self"}},"minecraft:type_family":{"family":["player","spider_sword","spider_sword_skill"]}}`
- `minecraft:shulker_sword` (строки 228,854,1644,1648,1659): `{"minecraft:scale":{"value":1},"minecraft:type_family":{"family":["player","shulker_sword"]}}`
- `shulker_sword_skill` (строки 232,1665,1666): `{"minecraft:damage_sensor":{"triggers":[{"cause":"all","deals_damage":false}]},"minecraft:scale":{"value":0.7},"minecraft:type_family":{"family":["player","shulker_sword"]}}`
- `minecraft:slime_sword` (строки 241,840,1669,1673,1684): `{"minecraft:type_family":{"family":["player","slime_sword"]},"minecraft:timer":{"time":[0.4,0.4],"looping":false,"time_down_event":{"event":"slime_sword_skills","target":"self"}},"minecraft:damage_sensor":{"triggers":{"on_damage":{"filters":{"all_of":[{"test":"is_family","subject":"other","value":"tamed_slime"}]}},"deals_damage":false}}}`
- `minecraft:spectral_sword` (строки 251,826,1693,1697,1793,1821): `{"minecraft:timer":{"time":[0.4,0.4],"looping":false,"time_down_event":{"event":"spectral_sword_skills","target":"self"}},"minecraft:rideable":{"seat_count":1,"family_types":["ender_crystal","spectral_sword"],"seats":{"position":[0.0,0.4,0.0],"lock_rider_rotation":0}},"minecraft:type_family":{"family":["player","spectral_sword"]}}`
- `minecraft:sea_sword` (строки 262,812,1825,1834,1848): `{"minecraft:collision_box":{"width":0.6,"height":0.9},"minecraft:timer":{"time":[0.5,0.5],"looping":true,"time_down_event":{"event":"sea_sword_sound","target":"self"}},"minecraft:breathable":{"total_supply":2,"suffocate_time":-1,"inhale_time":3.75,"generates_bubbles":false,"breathes_water":true,"breathes_air":false,"breathes_lava":false},"minecraft:type_family":{"family":["player","sea_sword"]}}`
- `mermaid_movement_out_water` (строки 275,1829): `{"minecraft:movement":{"value":0.06}}`
- `mermaid_movement_in_water` (строки 278,1839,1848): `{"minecraft:underwater_movement":{"value":0.07}}`
- `minecraft:quartz_sword` (строки 283,798,1864,1869,1878): `{"minecraft:type_family":{"family":["player","quartz_sword"]}}`
- `minecraft:obsidian_sword` (строки 286,784,1883,1887,1895): `{"minecraft:damage_sensor":{"triggers":{"on_damage":{"filters":{"any_of":[{"test":"has_damage","subject":"self","value":"block_explosion"},{"test":"has_damage","subject":"self","value":"entity_explosion"}]}},"deals_damage":false}},"minecraft:type_family":{"family":["player","obsidian_sword"]},"minecraft:knockback_resistance":{"value":1.0}}`
- `minecraft:lapis_sword` (строки 296,770,1900,1904,1912): `{"minecraft:type_family":{"family":["player","lapis_sword"]},"minecraft:timer":{"time":[2.5,6.0],"looping":true,"randomInterval":true,"time_down_event":{"event":"lapis_sword_skills","target":"self"}}}`
- `minecraft:ice_sword` (строки 302,756,1920,1924,1956): `{"minecraft:type_family":{"family":["player","ice_sword"]}}`
- `minecraft:magma_sword` (строки 305,742,1961,1965,1996): `{"minecraft:damage_sensor":{"triggers":{"on_damage":{"filters":{"any_of":[{"test":"has_damage","subject":"self","value":"fire_tick"},{"test":"is_block","subject":"block","operator":"equals","value":"magma"}]}},"deals_damage":false}},"minecraft:type_family":{"family":["player","magma_sword"]}}`
- `minecraft:jungle_sword` (строки 313,728,2001,2005,2016): `{"minecraft:type_family":{"family":["player","jungle_sword"]},"minecraft:health":{"value":8,"max":8}}`
- `minecraft:grass_sword` (строки 317,714,2023,2027,2043): `{"minecraft:type_family":{"family":["player","grass_sword"]},"minecraft:timer":{"time":[0.2,0.2],"looping":true,"time_down_event":{"event":"grass_sword_skills","target":"self"}}}`
- `minecraft:fire_sword` (строки 323,700,2054,2058,2079): `{"minecraft:timer":{"time":[0.2,0.7],"looping":true,"randomInterval":true,"time_down_event":{"event":"fire_sword_sound","target":"self"}},"minecraft:damage_sensor":{"triggers":{"on_damage":{"filters":{"any_of":[{"test":"has_damage","subject":"self","value":"fire"},{"test":"has_damage","subject":"self","value":"fire_tick"}]}},"deals_damage":false}},"minecraft:type_family":{"family":["player","fire_sword"]}}`
- `minecraft:emerald_sword` (строки 334,686,2086,2090,2103): `{"minecraft:type_family":{"family":["player","emerald_sword"]}}`
- `start_player_explode_event` (строки 337,2108,2109,2113): `{"minecraft:movement":{"value":0.0},"minecraft:timer":{"time":[1.5,1.5],"looping":true,"time_down_event":{"event":"start_player_explode","target":"self"}}}`
- `minecraft:cactus_sword` (строки 343,672,2117,2121,2129): `{"minecraft:type_family":{"family":["player","cactus_sword"]},"minecraft:timer":{"time":[0.5,0.5],"looping":true,"time_down_event":{"event":"cactus_sword_skills","target":"self"}}}`
- `minecraft:bone_sword` (строки 349,658,2136,2140,2153): `{"minecraft:type_family":{"family":["player","bone_sword"]},"minecraft:timer":{"time":[1,1],"looping":true,"time_down_event":{"event":"bone_sword_skills","target":"self"}}}`
- `minecraft:blaze_sword` (строки 355,644,2163,2167,2209,2238): `{"minecraft:damage_sensor":{"triggers":{"on_damage":{"filters":{"any_of":[{"test":"has_damage","subject":"self","value":"fire"},{"test":"has_damage","subject":"self","value":"fire_tick"}]}},"deals_damage":false}},"minecraft:hurt_on_condition":{"damage_conditions":[{"filters":{"test":"in_water_or_rain"},"cause":"drowning","damage_per_tick":1}]},"minecraft:type_family":{"family":["player","blaze_sword"]},"minecraft:timer":{"time":[1,1],"looping":true,"time_down_event":{"event":"blaze_sword_effects","target":"self"}}}`
- `blaze_sword_skill` (строки 375,376,378,2192,2245,2249): `{"minecraft:type_family":{"family":["player","blaze_sword","blaze_sword_skill"]},"minecraft:timer":{"time":[6,6],"looping":false,"time_down_event":{"event":"blaze_sword_skill","target":"self"}}}`
- `shoot_small_fireball` (строки 381,2209,2237,2252): `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":1,"single_use":true,"spawn_entity":"entity:fake_fireball","spawn_event":"set_sound","num_to_spawn":1},{"min_wait_time":0,"max_wait_time":1,"single_use":true,"spawn_entity":"entity:fake_fireball","spawn_event":"set_sound","num_to_spawn":1},{"min_wait_time":0,"max_wait_time":1,"single_use":true,"spawn_entity":"entity:fake_fireball","spawn_event":"set_sound","num_to_spawn":1},{"min_wait_time":0,"max_wait_time":1,"single_use":true,"spawn_entity":"entity:fake_fireball","spawn_event":"set_sound","num_to_spawn":1}],"minecraft:timer":{"time":[2,2],"looping":false,"time_down_event":{"event":"stop_blaze_sword_skill","target":"self"}}}`
- `ultra_instinct_projectile` (строки 420,2268,2269): `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"single_use":true,"spawn_entity":"entity:ultra_instinct_projectile","num_to_spawn":1}]}`
- `minecraft:default_player` (строки 423,1138,1143,1174,1204,1266,1298,1304,1390,1433,1485,1526,1552,1604,1622,1660,1685,1795,1849,1879,1896,1913,1957,1997,2017,2044,2080,2104,2114,2130,2154,2229): `{"minecraft:damage_sensor":{},"minecraft:timer":{},"minecraft:physics":{"has_gravity":true,"has_collision":true},"minecraft:scale":{"value":1},"minecraft:attack":{"damage":1},"minecraft:collision_box":{"width":0.6,"height":1.8},"minecraft:type_family":{"family":["player","default_player"]},"minecraft:movement":{"value":0.1},"minecraft:underwater_movement":{"value":0.02},"minecraft:health":{"value":20,"max":20},"minecraft:breathable":{"total_supply":15,"suffocate_time":-1,"inhale_time":3.75,"generates_bubbles":false},"minecraft:rideable":{"seat_count":2,"family_types":["parrot_tame"],"pull_in_entities":true,"seats":[{"position":[0.4,-0.2,-0.1],"min_rider_count":0,"max_rider_count":0,"lock_rider_rotation":0},{"position":[-0.4,-0.2,-0.1],"min_rider_count":1,"max_rider_count":2,"lock_rider_rotation":0}]}}`
- `despawn` (строки 481,2300): `{"minecraft:despawn":{}}`
- `minecraft:add_bad_omen` (строки 483,2274,2281): `{"minecraft:spell_effects":{"add_effects":[{"effect":"bad_omen","duration":6000,"display_on_screen_animation":true}]},"minecraft:timer":{"time":[0.0,0.0],"looping":false,"time_down_event":{"event":"minecraft:clear_add_bad_omen","target":"self"}}}`
- `minecraft:clear_bad_omen_spell_effect` (строки 502,2286): `{"minecraft:spell_effects":{}}`
- `minecraft:raid_trigger` (строки 506,507,2292,2297): `{"minecraft:raid_trigger":{"triggered_event":{"event":"minecraft:remove_raid_trigger","target":"self"}},"minecraft:spell_effects":{"remove_effects":"bad_omen"}}`

### События

**`minecraft:constant_events`** (строки 630,1056):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"run_command":{"command":["function commands/swords_and_more_swords/swords_and_more_swords/tag_swords","gamerule sendcommandfeedback false","gamerule commandblockoutput false","scoreboard objectives add Effect99 dummy","scoreboard players add @s Effect99 1","title @s[scores={Effect99=12000}] actionbar §l§fCreated by §7Effect99","scoreboard players set @s[scores={Effect99=36001}] Effect99 1"]}}`

**`minecraft:stop_sword_events`** (строки 637,1070):

- `$.sequence`: 5 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"run_command":{"command":["execute @e[r=64,type=!player] ~ ~ ~ detect ~ ~ ~ ice 0 tp @s ~ ~ ~"]}}`
  - `$.sequence[1]` — поля действия: `{"filters":{"all_of":[{"test":"has_biome_tag","operator":"!=","value":"nether"},{"test":"has_biome_tag","operator":"!=","value":"the_end"}]},"run_command":{"command":["fill ~6 ~6 ~6 ~-6 ~-6 ~-6 stone 0 replace effect99:spectral_block","fill ~7 ~8 ~8 ~8 ~-8 ~-8 stone 0 replace effect99:spectral_block","fill ~-7 ~-8 ~-8 ~-8 ~8 ~8 stone 0 replace effect99:spectral_block","fill ~-6 ~8 ~7 ~6 ~-8 ~8 stone 0 replace effect99:spectral_block","fill ~6 ~-8 ~-7 ~-6 ~8 ~-8 stone 0 replace effect99:spectral_block","fill ~8 ~-8 ~8 ~-8 ~-7 ~-8 stone 0 replace effect99:spectral_block","fill ~8 ~8 ~8 ~-8 ~7 ~-8 stone 0 replace effect99:spectral_block"]}}`
  - `$.sequence[2]` — поля действия: `{"filters":{"test":"has_biome_tag","value":"nether"},"run_command":{"command":["fill ~6 ~6 ~6 ~-6 ~-6 ~-6 netherrack 0 replace effect99:spectral_block","fill ~7 ~8 ~8 ~8 ~-8 ~-8 netherrack 0 replace effect99:spectral_block","fill ~-7 ~-8 ~-8 ~-8 ~8 ~8 netherrack 0 replace effect99:spectral_block","fill ~-6 ~8 ~7 ~6 ~-8 ~8 netherrack 0 replace effect99:spectral_block","fill ~6 ~-8 ~-7 ~-6 ~8 ~-8 netherrack 0 replace effect99:spectral_block","fill ~8 ~-8 ~8 ~-8 ~-7 ~-8 netherrack 0 replace effect99:spectral_block","fill ~8 ~8 ~8 ~-8 ~7 ~-8 netherrack 0 replace effect99:spectral_block"]}}`
  - `$.sequence[3]` — поля действия: `{"filters":{"test":"has_biome_tag","value":"the_end"},"run_command":{"command":["fill ~6 ~6 ~6 ~-6 ~-6 ~-6 end_stone 0 replace effect99:spectral_block","fill ~7 ~8 ~8 ~8 ~-8 ~-8 end_stone 0 replace effect99:spectral_block","fill ~-7 ~-8 ~-8 ~-8 ~8 ~8 end_stone 0 replace effect99:spectral_block","fill ~-6 ~8 ~7 ~6 ~-8 ~8 end_stone 0 replace effect99:spectral_block","fill ~6 ~-8 ~-7 ~-6 ~8 ~-8 end_stone 0 replace effect99:spectral_block","fill ~8 ~-8 ~8 ~-8 ~-7 ~-8 end_stone 0 replace effect99:spectral_block","fill ~8 ~8 ~8 ~-8 ~7 ~-8 end_stone 0 replace effect99:spectral_block"]}}`
  - `$.sequence[4]` — поля действия: `{"filters":{"all_of":[{"test":"has_equipment","subject":"self","domain":"hand","operator":"!=","value":"effect:slime_sword"}]},"run_command":{"command":["ride @e[type=entity:mountable_slime,r=1,y=~-1] evict_riders"]}}`

**`minecraft:bee_sword`** (строки 22,1043,1125,1129,1137):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"bee_sword"},"add":{"component_groups":["minecraft:bee_sword"]}}`

**`stop_bee_sword_event`** (строки 1050,1133):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"bee_sword"},"remove":{"component_groups":["minecraft:bee_sword"]},"add":{"component_groups":["minecraft:default_player"]}}`

**`default_player`** (строки 441,523,635,1142):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:default_player"]}}`

**`bee_sword_flower`** (строки 24,1145):

- `$.randomize`: альтернативы, веса `[1,1,1,1,1,1,1,1,1,1,1,1]`, сумма 12:
  - ветвь 0, weight `1`; условная доля 1/12 (8.33333%):
    - `$.randomize[0]` — поля действия: `{"run_command":{"command":["execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 0"]}}`
  - ветвь 1, weight `1`; условная доля 1/12 (8.33333%):
    - `$.randomize[1]` — поля действия: `{"run_command":{"command":["execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 1"]}}`
  - ветвь 2, weight `1`; условная доля 1/12 (8.33333%):
    - `$.randomize[2]` — поля действия: `{"run_command":{"command":["execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 2"]}}`
  - ветвь 3, weight `1`; условная доля 1/12 (8.33333%):
    - `$.randomize[3]` — поля действия: `{"run_command":{"command":["execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 3"]}}`
  - ветвь 4, weight `1`; условная доля 1/12 (8.33333%):
    - `$.randomize[4]` — поля действия: `{"run_command":{"command":["execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 4"]}}`
  - ветвь 5, weight `1`; условная доля 1/12 (8.33333%):
    - `$.randomize[5]` — поля действия: `{"run_command":{"command":["execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 5"]}}`
  - ветвь 6, weight `1`; условная доля 1/12 (8.33333%):
    - `$.randomize[6]` — поля действия: `{"run_command":{"command":["execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 6"]}}`
  - ветвь 7, weight `1`; условная доля 1/12 (8.33333%):
    - `$.randomize[7]` — поля действия: `{"run_command":{"command":["execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 7"]}}`
  - ветвь 8, weight `1`; условная доля 1/12 (8.33333%):
    - `$.randomize[8]` — поля действия: `{"run_command":{"command":["execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 8"]}}`
  - ветвь 9, weight `1`; условная доля 1/12 (8.33333%):
    - `$.randomize[9]` — поля действия: `{"run_command":{"command":["execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 9"]}}`
  - ветвь 10, weight `1`; условная доля 1/12 (8.33333%):
    - `$.randomize[10]` — поля действия: `{"run_command":{"command":["execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 10"]}}`
  - ветвь 11, weight `1`; условная доля 1/12 (8.33333%):
    - `$.randomize[11]` — поля действия: `{"run_command":{"command":["execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ yellow_flower 0"]}}`

**`minecraft:nether_star_sword`** (строки 28,1029,1161,1165,1173):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"nether_star_sword"},"add":{"component_groups":["minecraft:nether_star_sword"]}}`

**`stop_nether_star_sword_event`** (строки 1036,1169):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"nether_star_sword"},"remove":{"component_groups":["minecraft:nether_star_sword"]},"add":{"component_groups":["minecraft:default_player"]}}`

**`minecraft:clock_sword`** (строки 35,1015,1178,1182,1202):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"clock_sword"},"add":{"component_groups":["minecraft:clock_sword"]}}`
  - `$.sequence[1]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"clock_sword_skill"},"add":{"component_groups":["clock_sword_movement"]},"run_command":{"command":["gamerule randomtickspeed 100","effect @e[type=!player] speed 1 10 true","time add 10","event entity @a[family=default_player] clock_sword_movement"]}}`

**`stop_clock_sword_event`** (строки 40,1022,1198):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"clock_sword"},"remove":{"component_groups":["minecraft:clock_sword"]},"run_command":{"command":["gamerule randomtickspeed 1","effect @e[type=!player] speed 0 0","event entity @a[family=default_player] default_player"]},"add":{"component_groups":["minecraft:default_player"]}}`

**`clock_sword_skill_event`** (строки 1208):

- `$` — поля действия: `{"add":{"component_groups":["clock_sword_skill"]}}`

**`clock_sword_movement`** (строки 44,1186,1213,1214):

- `$` — поля действия: `{"add":{"component_groups":["clock_sword_movement"]}}`

**`minecraft:ghost_sword`** (строки 47,1001,1216,1220,1265):

- `$.sequence`: 6 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"ghost_sword"},"add":{"component_groups":["minecraft:ghost_sword"]},"run_command":{"command":["particle minecraft:egg_destroy_emitter ~ ~ ~","particle minecraft:egg_destroy_emitter ~ ~0.3 ~","particle minecraft:egg_destroy_emitter ~ ~0.6 ~","particle minecraft:egg_destroy_emitter ~ ~0.9 ~","particle minecraft:egg_destroy_emitter ~ ~1.2 ~","particle minecraft:egg_destroy_emitter ~ ~1.5 ~","playsound mob.wither.ambient @a[r=16] ~ ~1 ~ 2 0.3"]}}`
  - `$.sequence[1]` — поля действия: `{"run_command":{"command":["effect @s slow_falling 1 0 true","effect @s saturation 1 1 true"]},"add":{"component_groups":["ghost_movement"]}}`
  - `$.sequence[2]` — поля действия: `{"filters":{"test":"in_water"},"run_command":{"command":["effect @s levitation 1 0 true"]}}`
  - `$.sequence[3]` — поля действия: `{"filters":{"test":"in_lava"},"run_command":{"command":["effect @s levitation 1 0 true","effect @s fire_resistance 1 0 true"]}}`
  - `$.sequence[4]` — поля действия: `{"filters":{"test":"in_lava","operator":"!="},"run_command":{"command":["effect @s fire_resistance 0 0"]}}`
  - `$.sequence[5].randomize`: альтернативы, веса `[90,10]`, сумма 100:
    - ветвь 0, weight `90`; условная доля 9/10 (90%):
      - пустое действие
    - ветвь 1, weight `10`; условная доля 1/10 (10%):
      - `$.sequence[5].randomize[1]` — поля действия: `{"run_command":{"command":["playsound mob.wither.spawn @a[r=16] ~ ~ ~ 0.15 0.2"]}}`

**`stop_ghost_sword_event`** (строки 1008,1261):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"ghost_sword"},"remove":{"component_groups":["minecraft:ghost_sword"]},"add":{"component_groups":["minecraft:default_player"]},"run_command":{"command":["effect @s slow_falling 0 0","stopsound @a[r=18] mob.wither.spawn","playsound mob.wither.ambient @a[r=16] ~ ~1 ~ 2 0.2","particle minecraft:egg_destroy_emitter ~ ~ ~","particle minecraft:egg_destroy_emitter ~ ~0.3 ~","particle minecraft:egg_destroy_emitter ~ ~0.6 ~","particle minecraft:egg_destroy_emitter ~ ~0.9 ~","particle minecraft:egg_destroy_emitter ~ ~1.2 ~","particle minecraft:egg_destroy_emitter ~ ~1.5 ~","particle minecraft:ghost_spiral ~~~"]}}`

**`minecraft:wolf_sword`** (строки 67,973,1283,1287,1296,1356):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"wolf_sword"},"add":{"component_groups":["minecraft:wolf_sword"]},"run_command":{"command":["effect @s nausea 0 0","effect @s blindness 0 0","effect @s nausea 0 0"]}}`

**`stop_wolf_sword_event`** (строки 980,1292):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"wolf_sword"},"remove":{"component_groups":["minecraft:wolf_sword","wolf_transformation","wolf_movement"]},"run_command":{"command":["effect @s nausea 0 0"]},"add":{"component_groups":["minecraft:default_player"]}}`
  - `$.sequence[1]` — поля действия: `{"filters":{"test":"is_family","value":"complete_wolf_transformation"},"remove":{"component_groups":["complete_wolf_transformation"]},"run_command":{"command":["effect @s nausea 9999 0 true","effect @s blindness 9999 0 true"]},"add":{"component_groups":["minecraft:default_player"]}}`

**`wolf_sword_start_events`** (строки 1308):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"wolf_transformation"},"add":{"component_groups":["wolf_transformation"]},"run_command":{"command":["function commands/swords_and_more_swords/swords_and_more_swords/tellraw1"]}}`

**`starting_wolf_transformation`** (строки 987,1317):

- `$` — поля действия: `{"run_command":{"command":["effect @s nausea 5 0 true"]}}`

**`wolf_transformation`** (строки 70,71,985,1296,1311,1312,1319,1335,1336,1355):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"complete_wolf_transformation"},"run_command":{"command":["playsound random.fizz @a[r=16] ~~~","playsound wolf_sword.howl @a[r=24] ~~~","playsound wolf_sword.distant_howl @a[rm=25,r=100]","particle minecraft:egg_destroy_emitter ~ ~ ~","particle minecraft:egg_destroy_emitter ~ ~0.5 ~","particle minecraft:egg_destroy_emitter ~ ~0.8 ~"]},"add":{"component_groups":["complete_wolf_transformation"]}}`
  - `$.sequence[1]` — поля действия: `{"filters":{"test":"is_family","value":"wolf_transformation"},"remove":{"component_groups":["wolf_transformation"]}}`

**`wolf_movement`** (строки 92,994,1296,1340,1355):

- `$` — поля действия: `{"add":{"component_groups":["wolf_movement"]}}`

**`wolf_damage_sound`** (строки 78,1342):

- `$` — поля действия: `{"run_command":{"command":["playsound mob.wolf.bark @a[r=16] ~ ~ ~ 1 0.55"]}}`

**`wolf_sword_sounds`** (строки 85,1344):

- `$.randomize`: альтернативы, веса `[1]`, сумма 1:
  - ветвь 0, weight `1`; условная доля 1/1 (100%):
    - `$.randomize[0]` — поля действия: `{"run_command":{"command":["playsound mob.wolf.growl @a[r=16] ~ ~ ~ 1 0.9 24"]}}`

**`stop_wolf_transformation`** (строки 1349):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"run_command":{"command":["effect @s nausea 0 0","effect @s blindness 0 0","stopsound @a wolf_sword.howl","stopsound @a wolf_sword.distant_howl"]}}`
  - `$.sequence[1]` — поля действия: `{"remove":{"component_groups":["wolf_transformation","complete_wolf_transformation","wolf_movement"]},"add":{"component_groups":["minecraft:wolf_sword"]}}`

**`minecraft:ultra_instinct_sword`** (строки 95,959,1360,1364,1389):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"ultra_instinct_sword"},"add":{"component_groups":["minecraft:ultra_instinct_sword"]},"run_command":{"command":["particle minecraft:example_flipbook ~ ~ ~","particle minecraft:example_flipbook ~ ~1.5 ~","playsound mob.wither.ambient @a[r=16] ~ ~1 ~ 2 0.6"]}}`
  - `$.sequence[1]` — поля действия: `{"run_command":{"command":["camerashake add @a[r=32] 0.1 0.016 positional","fill ~1 ~2 ~1 ~-1 ~2 ~-1 effect99:lightblock 0 replace air","fill ~1 ~2 ~1 ~-1 ~2 ~-1 effect99:lightblock 0 replace effect99:lightblock","effect @s hunger 0 0","effect @s blindness 0 0","effect @s slowness 0 0","effect @s weakness 0 0","effect @s mining_fatigue 0 0","effect @s nausea 0 0","effect @s instant_damage 0 0","effect @s wither 0 0"]},"add":{"component_groups":["ultra_instinct_sword_movement"]}}`

**`stop_ultra_instinct_sword_event`** (строки 966,1385):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"ultra_instinct_sword"},"remove":{"component_groups":["minecraft:ultra_instinct_sword","ultra_instinct_sword_movement"]},"add":{"component_groups":["minecraft:default_player"]},"run_command":{"command":["particle minecraft:example_flipbook ~ ~ ~","particle minecraft:example_flipbook ~ ~1.5 ~","playsound mob.wither.ambient @a[r=16] ~ ~1 ~ 2 0.6"]}}`

**`ultra_instinct_sword_skill`** (строки 113,1395):

- `$` — поля действия: `{"run_command":{"command":["spreadplayers ~ ~ 1 3 @s","playsound mob.endermen.portal @a[r=17] ~ ~ ~ 1 0.6"]}}`

**`ultra_instinct_sword_effects`** (строки 98,1397):

- `$.randomize`: альтернативы, веса `[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]`, сумма 15:
  - ветвь 0, weight `1`; условная доля 1/15 (6.66667%):
    - `$.randomize[0]` — поля действия: `{"run_command":{"command":["particle minecraft:balloon_gas_particle ~0.3 ~1 ~","playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"]}}`
  - ветвь 1, weight `1`; условная доля 1/15 (6.66667%):
    - `$.randomize[1]` — поля действия: `{"run_command":{"command":["particle minecraft:balloon_gas_particle ~ ~2 ~0.3","playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"]}}`
  - ветвь 2, weight `1`; условная доля 1/15 (6.66667%):
    - `$.randomize[2]` — поля действия: `{"run_command":{"command":["particle minecraft:balloon_gas_particle ~-0.3 ~ ~","playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"]}}`
  - ветвь 3, weight `1`; условная доля 1/15 (6.66667%):
    - `$.randomize[3]` — поля действия: `{"run_command":{"command":["particle minecraft:balloon_gas_particle ~ ~0.3 ~-0.3","playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"]}}`
  - ветвь 4, weight `1`; условная доля 1/15 (6.66667%):
    - `$.randomize[4]` — поля действия: `{"run_command":{"command":["particle minecraft:balloon_gas_particle ~0.3 ~1.5 ~0.3","playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"]}}`
  - ветвь 5, weight `1`; условная доля 1/15 (6.66667%):
    - `$.randomize[5]` — поля действия: `{"run_command":{"command":["particle minecraft:balloon_gas_particle ~-0.3 ~0.8 ~-0.3","playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"]}}`
  - ветвь 6, weight `1`; условная доля 1/15 (6.66667%):
    - `$.randomize[6]` — поля действия: `{"run_command":{"command":["particle minecraft:balloon_gas_particle ~-0.3 ~2 ~0.3","playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"]}}`
  - ветвь 7, weight `1`; условная доля 1/15 (6.66667%):
    - `$.randomize[7]` — поля действия: `{"run_command":{"command":["particle minecraft:balloon_gas_particle ~0.2 ~1 ~0.3","playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"]}}`
  - ветвь 8, weight `1`; условная доля 1/15 (6.66667%):
    - `$.randomize[8]` — поля действия: `{"run_command":{"command":["particle minecraft:balloon_gas_particle ~0.3 ~0.9 ~0.1","playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"]}}`
  - ветвь 9, weight `1`; условная доля 1/15 (6.66667%):
    - `$.randomize[9]` — поля действия: `{"run_command":{"command":["particle minecraft:balloon_gas_particle ~0.2 ~2.3 ~-0.2","playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"]}}`
  - ветвь 10, weight `1`; условная доля 1/15 (6.66667%):
    - `$.randomize[10]` — поля действия: `{"run_command":{"command":["particle minecraft:balloon_gas_particle ~-0.3 ~1.2 ~","playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"]}}`
  - ветвь 11, weight `1`; условная доля 1/15 (6.66667%):
    - `$.randomize[11]` — поля действия: `{"run_command":{"command":["particle minecraft:balloon_gas_particle ~0.3 ~0.3 ~0.3","playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"]}}`
  - ветвь 12, weight `1`; условная доля 1/15 (6.66667%):
    - `$.randomize[12]` — поля действия: `{"run_command":{"command":["particle minecraft:balloon_gas_particle ~0.3 ~0.6 ~0.1","playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"]}}`
  - ветвь 13, weight `1`; условная доля 1/15 (6.66667%):
    - `$.randomize[13]` — поля действия: `{"run_command":{"command":["particle minecraft:balloon_gas_particle ~-0.3 ~0.2 ~0.3","playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"]}}`
  - ветвь 14, weight `1`; условная доля 1/15 (6.66667%):
    - `$.randomize[14]` — поля действия: `{"run_command":{"command":["particle minecraft:balloon_gas_particle ~0.1 ~0.7 ~-0.3","playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"]}}`

**`minecraft:ender_sword`** (строки 147,945,1416,1420,1432):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"ender_sword"},"add":{"component_groups":["minecraft:ender_sword"]},"run_command":{"command":["playsound mob.endermen.portal @a[r=8] ~ ~ ~"]}}`
  - `$.sequence[1]` — поля действия: `{"run_command":{"command":["particle minecraft:end_chest ~ ~0.6 ~"]}}`

**`stop_ender_sword_event`** (строки 952,1428):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"ender_sword"},"remove":{"component_groups":["minecraft:ender_sword"]},"add":{"component_groups":["minecraft:default_player"]}}`

**`ender_sword_sound`** (строки 181,1437):

- `$.randomize`: альтернативы, веса `[1,1,1]`, сумма 3:
  - ветвь 0, weight `1`; условная доля 1/3 (33.3333%):
    - `$.randomize[0]` — поля действия: `{"run_command":{"command":["playsound mob.endermen.scream @a[r=8] ~ ~ ~"]}}`
  - ветвь 1, weight `1`; условная доля 1/3 (33.3333%):
    - `$.randomize[1]` — поля действия: `{"run_command":{"command":["playsound mob.endermen.idle @a[r=8] ~ ~ ~"]}}`
  - ветвь 2, weight `1`; условная доля 1/3 (33.3333%):
    - `$.randomize[2]` — поля действия: `{"run_command":{"command":["playsound mob.endermen.stare @a[r=8] ~ ~ ~"]}}`

**`ender_sword_tp`** (строки 158,164,1444):

- `$` — поля действия: `{"run_command":{"command":["spreadplayers ~ ~ 0 16 @s","playsound mob.endermen.portal @a[r=17]"]}}`

**`ender_sword_skill`** (строки 152,1446):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"run_command":{"command":["playsound mob.endermen.hit @a[r=8] ~ ~ ~"]}}`
  - `$.sequence[1].randomize`: альтернативы, веса `[50,50]`, сумма 100:
    - ветвь 0, weight `50`; условная доля 1/2 (50%):
      - пустое действие
    - ветвь 1, weight `50`; условная доля 1/2 (50%):
      - `$.sequence[1].randomize[1]` — поля действия: `{"run_command":{"command":["spreadplayers ~ ~ 0 16 @s","playsound mob.endermen.portal @a[r=17]"]}}`

**`minecraft:lightning_sword`** (строки 184,931,1468,1472,1484):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"lightning_sword"},"add":{"component_groups":["minecraft:lightning_sword"]},"run_command":{"command":["summon lightning_bolt ~ 255 ~ default_lightning_bolt"]}}`
  - `$.sequence[1]` — поля действия: `{"run_command":{"command":["fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace air","fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace effect99:lightblock2"]}}`

**`stop_lightning_sword_event`** (строки 938,1480):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"lightning_sword"},"remove":{"component_groups":["minecraft:lightning_sword"]},"add":{"component_groups":["minecraft:default_player"]}}`

**`minecraft:glowstone_sword`** (строки 924,1489):

- `$` — поля действия: `{"run_command":{"command":["fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock 0 replace air","fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock 0 replace effect99:lightblock"]}}`

**`minecraft:wither_sword`** (строки 191,910,1492,1496,1525):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"wither_sword"},"add":{"component_groups":["minecraft:wither_sword"]},"run_command":{"command":["playsound mob.wither.spawn @a[r=16]"]}}`
  - `$.sequence[1]` — поля действия: `{"run_command":{"command":["fill ~5 ~5 ~5 ~-5 ~-5 ~-5 dirt 1 replace grass","fill ~5 ~5 ~5 ~-5 ~-5 ~-5 air 0 replace leaves2","fill ~5 ~5 ~5 ~-5 ~-5 ~-5 air 0 replace leaves","fill ~5 ~5 ~5 ~-5 ~-5 ~-5 air 0 replace vine","fill ~5 ~5 ~5 ~-5 ~-5 ~-5 water 0 replace ice","fill ~5 ~5 ~5 ~-5 ~-5 ~-5 dirt 0 replace farmland","fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace red_flower","fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace yellow_flower","fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace red_mushroom","fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace brown_mushroom","fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace double_plant","effect @s wither 39960 1 true","fill ~1 ~2 ~1 ~-1 ~2 ~-1 effect99:lightblock2 0 replace air","fill ~1 ~2 ~1 ~-1 ~2 ~-1 effect99:lightblock2 0 replace effect99:lightblock2"]}}`

**`stop_wither_sword_event`** (строки 917,1521):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"wither_sword"},"remove":{"component_groups":["minecraft:wither_sword"]},"add":{"component_groups":["minecraft:default_player"]},"run_command":{"command":["effect @s wither 0 0","ride @s evict_riders"]}}`

**`wither_sword_effects`** (строки 202,1531):

- `$.randomize`: альтернативы, веса `[50,50]`, сумма 100:
  - ветвь 0, weight `50`; условная доля 1/2 (50%):
    - `$.randomize[0]` — поля действия: `{"run_command":{"command":["playsound mob.wither.death @a[r=16]"]}}`
  - ветвь 1, weight `50`; условная доля 1/2 (50%):
    - `$.randomize[1]` — поля действия: `{"run_command":{"command":["playsound mob.wither.hurt @a[r=16]"]}}`

**`minecraft:time_sword`** (строки 206,896,1537,1540,1551):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"add":{"component_groups":["minecraft:time_sword"]}}`
  - `$.sequence[1]` — поля действия: `{"run_command":{"command":["gamerule randomtickspeed 300","effect @e[type=!player] speed 1 15 true","time add 30","event entity @a[family=default_player] time_sword_movement","fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace air","fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace effect99:lightblock2"]}}`

**`stop_time_sword_event`** (строки 903,1547):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"time_sword"},"remove":{"component_groups":["minecraft:time_sword"]},"add":{"component_groups":["minecraft:default_player"]},"run_command":{"command":["gamerule randomtickspeed 1","effect @e[type=!player] speed 0 0","event entity @a[family=default_player] default_player"]}}`

**`time_sword_movement`** (строки 210,1557,1558):

- `$` — поля действия: `{"add":{"component_groups":["time_sword_movement"]}}`

**`minecraft:sponge_sword`** (строки 213,882,1560,1564,1603):

- `$.sequence`: 3 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"sponge_sword"},"add":{"component_groups":["minecraft:sponge_sword"]},"run_command":{"command":["scoreboard objectives add sponge_sword dummy"]}}`
  - `$.sequence[1]` — поля действия: `{"filters":{"test":"in_water_or_rain"},"run_command":{"command":["fill ~2 ~2 ~2 ~-2 ~-2 ~-2 sponge 0 replace water","playsound random.fizz @a[r=12] ~~~ 0.6","particle minecraft:cauldron_explosion_emitter ~ ~ ~","scoreboard players add @s sponge_sword 1"]}}`
  - `$.sequence[2]` — поля действия: `{"run_command":{"command":["fill ~2 ~2 ~2 ~-2 ~-2 ~-2 air 0 replace sponge","fill ~2 ~2 ~2 ~-2 ~-2 ~-2 air 0 replace seagrass","execute @s[scores={sponge_sword=150}] ~ ~ ~ event entity @s wet_sponge_sword","execute @s[scores={sponge_sword=155}] ~ ~ ~ event entity @s wet_sponge_sword","execute @s[scores={sponge_sword=160}] ~ ~ ~ event entity @s wet_sponge_sword"]}}`

**`wet_sponge_sword`** (строки 1591):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:sponge_sword"},"run_command":{"command":["replaceitem entity @s slot.weapon.mainhand 0 effect:wet_sponge_sword 1","scoreboard players set @s sponge_sword 0","title @s actionbar §l§gWet Sponge Sword"]}}`

**`stop_sponge_sword_event`** (строки 889,1599):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"sponge_sword"},"remove":{"component_groups":["minecraft:sponge_sword"]},"add":{"component_groups":["minecraft:default_player"]}}`

**`minecraft:spider_sword`** (строки 216,868,1608,1612,1621,1632):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"spider_sword"},"add":{"component_groups":["minecraft:spider_sword"]},"run_command":{"command":["ride @s summon_ride minecraft:spider no_ride_change minecraft:spider_sword","particle minecraft:example_linearcurve ~ ~ ~"]}}`

**`stop_spider_sword_event`** (строки 875,1617):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"spider_sword"},"remove":{"component_groups":["minecraft:spider_sword","spider_sword_skill"]},"add":{"component_groups":["minecraft:default_player"]},"run_command":{"command":["ride @s stop_riding"]}}`

**`stop_spider_skill_event`** (строки 224,1627):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","value":"spider_sword_skill"},"remove":{"component_groups":["spider_sword_skill"]},"add":{"component_groups":["minecraft:spider_sword"]}}`

**`spider_sword_skill`** (строки 219,226,1621,1630,1631,1636,1639,1640):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"spider_sword_skill"},"add":{"component_groups":["spider_sword_skill"]}}`

**`minecraft:shulker_sword`** (строки 228,854,1644,1648,1659):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"shulker_sword"},"add":{"component_groups":["minecraft:shulker_sword"]}}`
  - `$.sequence[1]` — поля действия: `{"run_command":{"command":["effect @s levitation 0 0"]}}`

**`stop_shulker_sword_event`** (строки 861,1655):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"shulker_sword"},"remove":{"component_groups":["minecraft:shulker_sword"]},"add":{"component_groups":["minecraft:default_player"]},"run_command":{"command":["ride @s stop_riding"]}}`

**`shulker_sword_skill`** (строки 232,1665,1666):

- `$` — поля действия: `{"add":{"component_groups":["shulker_sword_skill"]},"run_command":{"command":["ride @s summon_ride entity:shulker_shield no_ride_change"]}}`

**`minecraft:slime_sword`** (строки 241,840,1669,1673,1684):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"slime_sword"},"add":{"component_groups":["minecraft:slime_sword"]}}`
  - `$.sequence[1]` — поля действия: `{"run_command":{"command":["scoreboard players set @e[type=entity:mountable_slime,c=1,r=12] slime_despawn 0"]}}`

**`stop_slime_sword_event`** (строки 847,1680):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"slime_sword"},"remove":{"component_groups":["minecraft:slime_sword"]},"add":{"component_groups":["minecraft:default_player"]},"run_command":{"command":["ride @s stop_riding","event entity @e[type=entity:mountable_slime,c=1,r=32] despawn"]}}`

**`slime_sword_skills`** (строки 244,1690):

- `$` — поля действия: `{"run_command":{"command":["ride @s summon_ride entity:mountable_slime no_ride_change","scoreboard objectives add slime_despawn dummy"]}}`

**`minecraft:spectral_sword`** (строки 251,826,1693,1697,1793,1821):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"spectral_sword"},"add":{"component_groups":["minecraft:spectral_sword"]}}`
  - `$.sequence[1]` — поля действия: `{"run_command":{"command":["fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace air","fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace effect99:lightblock2","execute @s[y=8,dy=247] ~~~ event entity @s spectral_sword_function","execute @s[y=0,dy=7] ~~~ event entity @s spectral_sword_function_1"]}}`

**`spectral_sword_function_1`** (строки 1711):

- `$.sequence`: 3 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"all_of":[{"test":"has_biome_tag","operator":"!=","value":"nether"},{"test":"has_biome_tag","operator":"!=","value":"the_end"}]},"run_command":{"command":["fill ~8 ~8 ~8 ~-8 ~-6 ~-8 stone 0 replace effect99:spectral_block"]}}`
  - `$.sequence[1]` — поля действия: `{"filters":{"test":"has_biome_tag","value":"nether"},"run_command":{"command":["fill ~8 ~8 ~8 ~-8 ~-6 ~-8 netherrack 0 replace effect99:spectral_block"]}}`
  - `$.sequence[2]` — поля действия: `{"filters":{"test":"has_biome_tag","value":"the_end"},"run_command":{"command":["fill ~8 ~8 ~8 ~-8 ~-6 ~-8 end_stone 0 replace effect99:spectral_block"]}}`

**`spectral_sword_function`** (строки 1741):

- `$.sequence`: 3 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"all_of":[{"test":"has_biome_tag","operator":"!=","value":"nether"},{"test":"has_biome_tag","operator":"!=","value":"the_end"}]},"run_command":{"command":["fill ~6 ~6 ~6 ~-6 ~-6 ~-6 effect99:spectral_block 0 replace stone","fill ~7 ~8 ~8 ~8 ~-8 ~-8 stone 0 replace effect99:spectral_block","fill ~-7 ~-8 ~-8 ~-8 ~8 ~8 stone 0 replace effect99:spectral_block","fill ~-6 ~8 ~7 ~6 ~-8 ~8 stone 0 replace effect99:spectral_block","fill ~6 ~-8 ~-7 ~-6 ~8 ~-8 stone 0 replace effect99:spectral_block","fill ~8 ~-8 ~8 ~-8 ~-7 ~-8 stone 0 replace effect99:spectral_block","fill ~8 ~8 ~8 ~-8 ~7 ~-8 stone 0 replace effect99:spectral_block"]}}`
  - `$.sequence[1]` — поля действия: `{"filters":{"test":"has_biome_tag","value":"nether"},"run_command":{"command":["fill ~6 ~6 ~6 ~-6 ~-6 ~-6 effect99:spectral_block 0 replace netherrack","fill ~7 ~8 ~8 ~8 ~-8 ~-8 netherrack 0 replace effect99:spectral_block","fill ~-7 ~-8 ~-8 ~-8 ~8 ~8 netherrack 0 replace effect99:spectral_block","fill ~-6 ~8 ~7 ~6 ~-8 ~8 netherrack 0 replace effect99:spectral_block","fill ~6 ~-8 ~-7 ~-6 ~8 ~-8 netherrack 0 replace effect99:spectral_block","fill ~8 ~-8 ~8 ~-8 ~-7 ~-8 netherrack 0 replace effect99:spectral_block","fill ~8 ~8 ~8 ~-8 ~7 ~-8 netherrack 0 replace effect99:spectral_block"]}}`
  - `$.sequence[2]` — поля действия: `{"filters":{"test":"has_biome_tag","value":"the_end"},"run_command":{"command":["fill ~6 ~6 ~6 ~-6 ~-6 ~-6 effect99:spectral_block 0 replace end_stone","fill ~7 ~8 ~8 ~8 ~-8 ~-8 end_stone 0 replace effect99:spectral_block","fill ~-7 ~-8 ~-8 ~-8 ~8 ~8 end_stone 0 replace effect99:spectral_block","fill ~-6 ~8 ~7 ~6 ~-8 ~8 end_stone 0 replace effect99:spectral_block","fill ~6 ~-8 ~-7 ~-6 ~8 ~-8 end_stone 0 replace effect99:spectral_block","fill ~8 ~-8 ~8 ~-8 ~-7 ~-8 end_stone 0 replace effect99:spectral_block","fill ~8 ~8 ~8 ~-8 ~7 ~-8 end_stone 0 replace effect99:spectral_block"]}}`

**`stop_spectral_sword_event`** (строки 833,1789):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"spectral_sword"},"remove":{"component_groups":["minecraft:spectral_sword"]},"run_command":{"command":["ride @s evict_riders"]},"add":{"component_groups":["minecraft:default_player"]}}`

**`spectral_sword_skills`** (строки 253,1799):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"has_biome_tag","operator":"!=","value":"the_end"},"run_command":{"command":["summon ender_crystal ~ ~1.8 ~ minecraft:detect_player"]}}`
  - `$.sequence[1]` — поля действия: `{"run_command":{"command":["playsound portal.travel @a[r=16] ~ ~ ~ 1 7","particle minecraft:example_flipbook ~ ~3 ~"]}}`

**`spectral_sword_reload_skill`** (строки 1817):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"spectral_sword"},"add":{"component_groups":["minecraft:spectral_sword"]}}`

**`minecraft:sea_sword`** (строки 262,812,1825,1834,1848):

- `$.sequence`: 3 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"in_water","operator":"!="},"add":{"component_groups":["mermaid_movement_out_water"]},"run_command":{"command":["camerashake add @s 0.01 1 positional","effect @s conduit_power 0 0"]}}`
  - `$.sequence[1]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"sea_sword"},"add":{"component_groups":["minecraft:sea_sword"]},"run_command":{"command":["particle minecraft:example_bounce ~ ~ ~","playsound random.splash @a[r=12] ~ ~ ~ 0.5"]}}`
  - `$.sequence[2]` — поля действия: `{"filters":{"test":"in_water"},"add":{"component_groups":["mermaid_movement_in_water"]},"run_command":{"command":["effect @s conduit_power 1 0 true"]}}`

**`stop_sea_sword_event`** (строки 819,1844):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"sea_sword"},"remove":{"component_groups":["minecraft:sea_sword","mermaid_movement_in_water"]},"add":{"component_groups":["minecraft:default_player"]},"run_command":{"command":["particle minecraft:example_bounce ~ ~ ~","playsound random.splash @a[r=12] ~ ~ ~ 0.5","effect @s conduit_power 0 0"]}}`

**`sea_sword_sound`** (строки 268,1854):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"in_water","operator":"!="},"run_command":{"command":["playsound mob.fish.flop @a[r=12] ~ ~ ~ 1 0.6"]}}`

**`minecraft:quartz_sword`** (строки 283,798,1864,1869,1878):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"quartz_sword"},"run_command":{"command":["damage @s 14 magic"]},"add":{"component_groups":["minecraft:quartz_sword"]}}`

**`stop_quartz_sword_event`** (строки 805,1873):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"quartz_sword"},"run_command":{"command":["damage @s 14 magic"]},"remove":{"component_groups":["minecraft:quartz_sword"]},"add":{"component_groups":["minecraft:default_player"]}}`

**`minecraft:obsidian_sword`** (строки 286,784,1883,1887,1895):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"obsidian_sword"},"add":{"component_groups":["minecraft:obsidian_sword"]}}`

**`stop_obsidian_sword_event`** (строки 791,1891):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"obsidian_sword"},"remove":{"component_groups":["minecraft:obsidian_sword"]},"add":{"component_groups":["minecraft:default_player"]}}`

**`minecraft:lapis_sword`** (строки 296,770,1900,1904,1912):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"lapis_sword"},"add":{"component_groups":["minecraft:lapis_sword"]}}`

**`stop_lapis_sword_event`** (строки 777,1908):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"lapis_sword"},"remove":{"component_groups":["minecraft:lapis_sword"]},"add":{"component_groups":["minecraft:default_player"]}}`

**`lapis_sword_skills`** (строки 299,1917):

- `$` — поля действия: `{"run_command":{"command":["xp 5 @s","playsound random.orb @s ~ ~ ~ 0.3"]}}`

**`minecraft:ice_sword`** (строки 302,756,1920,1924,1956):

- `$.sequence`: 4 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"ice_sword"},"add":{"component_groups":["minecraft:ice_sword"]}}`
  - `$.sequence[1]` — поля действия: `{"filters":{"all_of":[{"test":"in_lava"},{"test":"has_biome_tag","operator":"!=","value":"nether"}]},"run_command":{"command":["playsound random.fizz @a[r=10] ~ ~ ~","setblock ~ ~ ~ flowing_water","replaceitem entity @s slot.weapon.mainhand 0 air 1 0","particle minecraft:cauldron_explosion_emitter ~ ~ ~"]}}`
  - `$.sequence[2]` — поля действия: `{"filters":{"all_of":[{"test":"in_lava"},{"test":"has_biome_tag","value":"nether"}]},"run_command":{"command":["playsound random.fizz @a[r=10] ~ ~ ~","replaceitem entity @s slot.weapon.mainhand 0 air 1 0","particle minecraft:cauldron_explosion_emitter ~ ~ ~"]}}`
  - `$.sequence[3]` — поля действия: `{"run_command":{"command":["fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 effect99:fake_ice 0 replace water","fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 effect99:fake_ice 0 replace flowing_water","fill ~3 ~-1 ~ ~3 ~-1 ~ effect99:fake_ice 0 replace water","fill ~3 ~-1 ~ ~3 ~-1 ~ effect99:fake_ice 0 replace flowing_water","fill ~ ~-1 ~3 ~ ~-1 ~3 effect99:fake_ice 0 replace water","fill ~ ~-1 ~3 ~ ~-1 ~3 effect99:fake_ice 0 replace flowing_water","fill ~-3 ~-1 ~ ~-3 ~-1 ~ effect99:fake_ice 0 replace water","fill ~-3 ~-1 ~ ~-3 ~-1 ~ effect99:fake_ice 0 replace flowing_water","fill ~ ~-1 ~-3 ~ ~-1 ~-3 effect99:fake_ice 0 replace water","fill ~ ~-1 ~-3 ~ ~-1 ~-3 effect99:fake_ice 0 replace flowing_water","execute @e[r=64,type=!player] ~ ~ ~ detect ~ ~ ~ effect99:fake_ice 0 tp @s ~ ~ ~ ~1"]}}`

**`stop_ice_sword_event`** (строки 763,1952):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"ice_sword"},"remove":{"component_groups":["minecraft:ice_sword"]},"add":{"component_groups":["minecraft:default_player"]}}`

**`minecraft:magma_sword`** (строки 305,742,1961,1965,1996):

- `$.sequence`: 3 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"magma_sword"},"add":{"component_groups":["minecraft:magma_sword"]}}`
  - `$.sequence[1]` — поля действия: `{"run_command":{"command":["fill ~ ~-1 ~ ~ ~-1 ~ magma 0 replace lava","fill ~1 ~-1 ~1 ~ ~-1 ~ magma 0 replace lava","fill ~ ~-1 ~1 ~ ~-1 ~1 magma 0 replace lava","fill ~-1 ~-1 ~ ~-1 ~-1 ~ magma 0 replace lava","fill ~ ~-1 ~-1 ~ ~-1 ~-1 magma 0 replace lava","execute @s ~ ~1 ~ particle minecraft:guardian_attack_particle ^-0.4 ^ ^0.2"]}}`
  - `$.sequence[2]` — поля действия: `{"filters":{"test":"in_water","operator":"=="}}`
  - `$.sequence[2].randomize`: альтернативы, веса `[99,1]`, сумма 100:
    - ветвь 0, weight `99`; условная доля 99/100 (99%):
      - пустое действие
    - ветвь 1, weight `1`; условная доля 1/100 (1%):
      - `$.sequence[2].randomize[1]` — поля действия: `{"run_command":{"command":["playsound bubble.up @a ~ ~ ~ 1 0.9"]}}`

**`stop_magma_sword_event`** (строки 749,1992):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"magma_sword"},"remove":{"component_groups":["minecraft:magma_sword"]},"add":{"component_groups":["minecraft:default_player"]}}`

**`minecraft:jungle_sword`** (строки 313,728,2001,2005,2016):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"jungle_sword"},"add":{"component_groups":["minecraft:jungle_sword"]}}`
  - `$.sequence[1]` — поля действия: `{"run_command":{"command":["effect @s absorption 1 2 true","function commands/swords_and_more_swords/swords_and_more_swords/jungle_sword"]}}`

**`stop_jungle_sword_event`** (строки 735,2012):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"jungle_sword"},"remove":{"component_groups":["minecraft:jungle_sword"]},"add":{"component_groups":["minecraft:default_player"]},"run_command":{"command":["effect @s absorption 0"]}}`

**`minecraft:grass_sword`** (строки 317,714,2023,2027,2043):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"grass_sword"},"add":{"component_groups":["minecraft:grass_sword"]}}`
  - `$.sequence[1]` — поля действия: `{"run_command":{"command":["tag @e[tag=grass,rm=9,r=10] remove grass","fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 grass 0 replace dirt","execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 fill ~ ~ ~ ~ ~ ~ tallgrass 0 replace air"]}}`

**`stop_grass_sword_event`** (строки 721,2039):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"grass_sword"},"remove":{"component_groups":["minecraft:grass_sword"]},"add":{"component_groups":["minecraft:default_player"]}}`

**`grass_sword_skills`** (строки 320,2048):

- `$` — поля действия: `{"run_command":{"command":["execute @e[type=!player,type=!item,type=!entity:grass,type=!xp_orb,type=!arrow,r=8,tag=!grass] ~ ~ ~ detect ~ ~-0.1 ~ grass 0 execute @s ~ ~ ~ detect ~ ~ ~ air 0 summon entity:grass","execute @e[type=!player,type=!item,type=!entity:grass,type=!xp_orb,type=!arrow,r=8,tag=!grass] ~ ~ ~ detect ~ ~-0.1 ~ grass 0 execute @s ~ ~ ~ detect ~ ~ ~ tallgrass 0 summon entity:grass"]}}`

**`minecraft:fire_sword`** (строки 323,700,2054,2058,2079):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"fire_sword"},"add":{"component_groups":["minecraft:fire_sword"]}}`
  - `$.sequence[1]` — поля действия: `{"run_command":{"command":["fill ~3 ~3 ~3 ~-3 ~-3 ~-3 air 0 replace snow_layer","fill ~3 ~3 ~3 ~-3 ~-3 ~-3 water 0 replace ice","fill ~3 ~3 ~3 ~-3 ~-3 ~-3 water 0 replace blue_ice","fill ~3 ~3 ~3 ~-3 ~-3 ~-3 water 0 replace packed_ice","execute @e[family=!player,type=!item,r=3] ~ ~ ~ summon entity:fire","fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock 0 replace air","fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock 0 replace effect99:lightblock"]}}`

**`stop_fire_sword_event`** (строки 707,2075):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"fire_sword"},"remove":{"component_groups":["minecraft:fire_sword"]},"add":{"component_groups":["minecraft:default_player"]}}`

**`fire_sword_sound`** (строки 325,2084):

- `$` — поля действия: `{"run_command":{"command":["playsound fire.fire @a[r=8]"]}}`

**`minecraft:emerald_sword`** (строки 334,686,2086,2090,2103):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"emerald_sword"},"add":{"component_groups":["minecraft:emerald_sword"]}}`
  - `$.sequence[1]` — поля действия: `{"filters":{"all_of":[{"test":"is_in_village","subject":"self","value":true}]},"run_command":{"command":["effect @s village_hero 1 0 true","effect @e[family=villager,r=64] resistance 1 1 true"]}}`

**`stop_emerald_sword_event`** (строки 693,2098):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"emerald_sword"},"run_command":{"command":["effect @s village_hero 0 0 true"]},"remove":{"component_groups":["minecraft:emerald_sword"]},"add":{"component_groups":["minecraft:default_player"]}}`

**`start_player_explode_event`** (строки 337,2108,2109,2113):

- `$` — поля действия: `{"add":{"component_groups":["start_player_explode_event"]},"run_command":{"command":["playanimation @s animation.player.explode","playsound random.fuse"]}}`

**`start_player_explode`** (строки 340,2112):

- `$` — поля действия: `{"remove":{"component_groups":["start_player_explode_event"]},"add":{"component_groups":["minecraft:default_player"]},"run_command":{"command":["summon entity:instant_creeper_explode ~ ~1 ~","kill @s"]}}`

**`minecraft:cactus_sword`** (строки 343,672,2117,2121,2129):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"cactus_sword"},"add":{"component_groups":["minecraft:cactus_sword"]}}`

**`stop_cactus_sword_event`** (строки 679,2125):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"cactus_sword"},"remove":{"component_groups":["minecraft:cactus_sword"]},"add":{"component_groups":["minecraft:default_player"]}}`

**`cactus_sword_skills`** (строки 346,2134):

- `$` — поля действия: `{"run_command":{"command":["damage @e[r=1.4,type=!player] 1 contact entity @s","damage @s 1 contact"]}}`

**`minecraft:bone_sword`** (строки 349,658,2136,2140,2153):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"bone_sword"},"add":{"component_groups":["minecraft:bone_sword"]}}`
  - `$.sequence[1]` — поля действия: `{"run_command":{"command":["event entity @e[family=arrow,r=8] minecraft:inertia_disable"]}}`

**`stop_bone_sword_event`** (строки 665,2149):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"bone_sword"},"remove":{"component_groups":["minecraft:bone_sword"]},"add":{"component_groups":["minecraft:default_player"]}}`

**`bone_sword_skills`** (строки 352,2158):

- `$` — поля действия: `{"run_command":{"command":["summon entity:grows_crop ~ ~0.1 ~ grows_crop_event"]}}`

**`minecraft:blaze_sword`** (строки 355,644,2163,2167,2209,2238):

- `$.sequence`: 3 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"blaze_sword"},"add":{"component_groups":["minecraft:blaze_sword"]},"run_command":{"command":["particle minecraft:mobflame_single ~ ~ ~","particle minecraft:mobflame_single ~ ~1 ~","particle minecraft:mobflame_single ~ ~1.5 ~","particle minecraft:mobflame_single ~0.4 ~ ~","particle minecraft:mobflame_single ~ ~1 ~0.4","particle minecraft:mobflame_single ~-0.4 ~1.5 ~","particle minecraft:mobflame_single ~ ~ ~-0.4","particle minecraft:mobflame_single ~0.3 ~1 ~0.3","particle minecraft:mobflame_single ~-0.3 ~1.5 ~-0.3","particle minecraft:mobflame_single ~0.3 ~ ~-0.3","particle minecraft:mobflame_single ~-0.3 ~1 ~0.3","particle minecraft:example_linearcurve ~ ~1 ~","playsound random.fizz @a[r=16]"]}}`
  - `$.sequence[1]` — поля действия: `{"run_command":{"command":["event entity @e[family=shot_by_the_blaze,r=7] minecraft:inertia_disable","fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace air","fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace effect99:lightblock2"]}}`
  - `$.sequence[2]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"blaze_sword_skill"}}`
  - `$.sequence[2].randomize`: альтернативы, веса `[5,5,5,5,5,5,95]`, сумма 125:
    - ветвь 0, weight `5`; условная доля 1/25 (4%):
      - `$.sequence[2].randomize[0]` — поля действия: `{"run_command":{"command":["particle minecraft:mobflame_single ~ ~0.2 ~"]}}`
    - ветвь 1, weight `5`; условная доля 1/25 (4%):
      - `$.sequence[2].randomize[1]` — поля действия: `{"run_command":{"command":["particle minecraft:mobflame_single ~0.3 ~0.2 ~"]}}`
    - ветвь 2, weight `5`; условная доля 1/25 (4%):
      - `$.sequence[2].randomize[2]` — поля действия: `{"run_command":{"command":["particle minecraft:mobflame_single ~ ~0.2 ~0.3"]}}`
    - ветвь 3, weight `5`; условная доля 1/25 (4%):
      - `$.sequence[2].randomize[3]` — поля действия: `{"run_command":{"command":["particle minecraft:mobflame_single ~-0.3 ~0.2 ~"]}}`
    - ветвь 4, weight `5`; условная доля 1/25 (4%):
      - `$.sequence[2].randomize[4]` — поля действия: `{"run_command":{"command":["particle minecraft:mobflame_single ~ ~0.2 ~-0.3"]}}`
    - ветвь 5, weight `5`; условная доля 1/25 (4%):
      - `$.sequence[2].randomize[5]` — поля действия: `{"run_command":{"command":["playsound mob.blaze.breathe @a[r=12] ~ ~ ~ 0.5"]}}`
    - ветвь 6, weight `95`; условная доля 19/25 (76%):
      - пустое действие

**`stop_blaze_sword_event`** (строки 651,2205):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"blaze_sword"},"remove":{"component_groups":["minecraft:blaze_sword","shoot_small_fireball"]},"run_command":{"command":["particle minecraft:mobflame_single ~ ~ ~","particle minecraft:mobflame_single ~ ~1 ~","particle minecraft:mobflame_single ~ ~1.5 ~","particle minecraft:mobflame_single ~0.4 ~ ~","particle minecraft:mobflame_single ~ ~1 ~0.4","particle minecraft:mobflame_single ~-0.4 ~1.5 ~","particle minecraft:mobflame_single ~ ~ ~-0.4","particle minecraft:mobflame_single ~0.3 ~1 ~0.3","particle minecraft:mobflame_single ~-0.3 ~1.5 ~-0.3","particle minecraft:mobflame_single ~0.3 ~ ~-0.3","particle minecraft:mobflame_single ~-0.3 ~1 ~0.3","particle minecraft:example_linearcurve ~ ~1 ~","playsound random.fizz @a[r=16]","effect @s levitation 0 0 true","effect @s slow_falling 0 0 true"]},"add":{"component_groups":["minecraft:default_player"]}}`

**`stop_blaze_sword_skill`** (строки 417,2233):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"blaze_sword"},"remove":{"component_groups":["shoot_small_fireball"]},"add":{"component_groups":["minecraft:blaze_sword"]}}`

**`blaze_sword_skill_event`** (строки 2242):

- `$` — поля действия: `{"add":{"component_groups":["blaze_sword_skill"]}}`

**`blaze_sword_skill`** (строки 375,376,378,2192,2245,2249):

- `$` — поля действия: `{"add":{"component_groups":["shoot_small_fireball"]}}`

**`blaze_sword_effects`** (строки 372,2256):

- `$.randomize`: альтернативы, веса `[1,1,1,1,1,1]`, сумма 6:
  - ветвь 0, weight `1`; условная доля 1/6 (16.6667%):
    - `$.randomize[0]` — поля действия: `{"run_command":{"command":["particle minecraft:mobflame_single ~ ~0.2 ~"]}}`
  - ветвь 1, weight `1`; условная доля 1/6 (16.6667%):
    - `$.randomize[1]` — поля действия: `{"run_command":{"command":["particle minecraft:mobflame_single ~0.3 ~0.2 ~"]}}`
  - ветвь 2, weight `1`; условная доля 1/6 (16.6667%):
    - `$.randomize[2]` — поля действия: `{"run_command":{"command":["particle minecraft:mobflame_single ~ ~0.2 ~0.3"]}}`
  - ветвь 3, weight `1`; условная доля 1/6 (16.6667%):
    - `$.randomize[3]` — поля действия: `{"run_command":{"command":["particle minecraft:mobflame_single ~-0.3 ~0.2 ~"]}}`
  - ветвь 4, weight `1`; условная доля 1/6 (16.6667%):
    - `$.randomize[4]` — поля действия: `{"run_command":{"command":["particle minecraft:mobflame_single ~ ~0.2 ~-0.3"]}}`
  - ветвь 5, weight `1`; условная доля 1/6 (16.6667%):
    - `$.randomize[5]` — поля действия: `{"run_command":{"command":["playsound mob.blaze.breathe @a[r=12] ~ ~ ~ 0.5"]}}`

**`shoot_ultra_instinct_projectile`** (строки 2266):

- `$` — поля действия: `{"run_command":{"command":["playsound mob.wither.ambient @s ~ ~1 ~ 2 0.6"]},"add":{"component_groups":["ultra_instinct_projectile"]},"remove":{"component_groups":["ultra_instinct_projectile"]}}`

**`minecraft:gain_bad_omen`** (строки 2271):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:add_bad_omen"]}}`

**`minecraft:clear_add_bad_omen`** (строки 497,2278):

- `$` — поля действия: `{"remove":{"component_groups":["minecraft:add_bad_omen"]},"add":{"component_groups":["minecraft:clear_bad_omen_spell_effect"]}}`

**`minecraft:trigger_raid`** (строки 624,2290):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:raid_trigger"]}}`

**`minecraft:remove_raid_trigger`** (строки 509,2295):

- `$` — поля действия: `{"remove":{"component_groups":["minecraft:raid_trigger"]}}`

**`despawn`** (строки 481,2300):

- `$` — поля действия: `{"add":{"component_groups":["despawn"]}}`

## `entity:pumpkin_projectile`

- Путь `Swords_B/entities/pumpkin_projectile.json`; format_version `"1.10.0"`.
- description: `{"identifier":"entity:pumpkin_projectile","runtime_identifier":"minecraft:snowball","is_spawnable":false,"is_summonable":true,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:collision_box` (строки 17): `{"width":0.625,"height":0.625}`
- `minecraft:type_family` (строки 21): `{"family":["effect99_entities","projectile"]}`
- `minecraft:timer` (строки 24): `{"time":[12,15],"looping":true,"time_down_event":{"event":"despawn"}}`
- `minecraft:projectile` (строки 31): `{"on_hit":{"impact_damage":{"damage":1,"knockback":true,"should_bounce":true},"remove_on_hit":{},"particle_on_hit":{"particle_type":"largeexplode","on_other_hit":true}},"hit_sound":"bullet.hit","destroyOnHurt":true,"crit_particle_on_hurt":true,"power":0.3,"gravity":0.002,"uncertainty_base":16,"uncertainty_multiplier":4,"anchor":1,"offset":[0,-0.1,0],"homing":false}`
- `minecraft:physics` (строки 56): `{"has_collision":false}`
- `minecraft:conditional_bandwidth_optimization` (строки 59): `{"default_values":{"max_optimized_distance":80.0,"max_dropped_ticks":7,"use_motion_prediction_hints":true}}`

### Группы компонентов

- `despawn` (строки 12,28,68,69): `{"minecraft:despawn":{}}`

### События

**`despawn`** (строки 12,28,68,69):

- `$` — поля действия: `{"add":{"component_groups":["despawn"]}}`

## `minecraft:shulker_bullet`

- Путь `Swords_B/entities/shulker_bullet.json`; format_version `"1.10.0"`.
- description: `{"identifier":"minecraft:shulker_bullet","is_spawnable":false,"is_summonable":false,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:collision_box` (строки 47): `{"width":0.625,"height":0.625}`
- `minecraft:projectile` (строки 12,51): `{"on_hit":{"impact_damage":{"damage":4,"knockback":true,"should_bounce":true},"mob_effect":{"effect":"levitation","durationeasy":200,"durationnormal":200,"durationhard":200,"amplifier":1},"remove_on_hit":{},"particle_on_hit":{"particle_type":"largeexplode","on_other_hit":true}},"hit_sound":"bullet.hit","destroyOnHurt":true,"crit_particle_on_hurt":true,"power":1.6,"gravity":0.05,"uncertainty_base":16,"uncertainty_multiplier":4,"anchor":1,"offset":[0,-0.1,0],"homing":true}`
- `minecraft:physics` (строки 83): `{"has_collision":false}`

### Группы компонентов

- `shulker_sword` (строки 11,92): `{"minecraft:projectile":{"on_hit":{"impact_damage":{"damage":4,"knockback":true,"should_bounce":true},"mob_effect":{"effect":"levitation","durationeasy":200,"durationnormal":200,"durationhard":200,"amplifier":1},"remove_on_hit":{},"particle_on_hit":{"particle_type":"largeexplode","on_other_hit":true}},"hit_sound":"bullet.hit","destroyOnHurt":false,"crit_particle_on_hurt":true,"power":1.6,"gravity":0.01,"uncertainty_base":16,"uncertainty_multiplier":4,"anchor":1,"offset":[0,-0.1,0],"homing":false}}`

### События

**`minecraft:entity_spawned`** (строки 88):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"has_equipment","subject":"other","domain":"hand","value":"effect:shulker_sword"},"add":{"component_groups":["shulker_sword"]}}`

## `entity:shulker_shield`

- Путь `Swords_B/entities/shulker_shield.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:shulker_shield","runtime_identifier":"minecraft:shulker","is_spawnable":false,"is_summonable":true,"is_experimental":false,"scripts":{"animate":["despawn"]},"animations":{"despawn":"controller.animation.despawn"}}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 22): `{"family":["effect99_entities","player","shulker_sword"]}`
- `minecraft:collision_box` (строки 23): `{"width":0.6,"height":0.9}`
- `minecraft:health` (строки 24): `{"value":20}`
- `minecraft:rideable` (строки 25): `{"crouching_skip_interact":true,"seat_count":1,"family_types":["player"],"seats":{"position":[0.0,0,0.0]}}`
- `minecraft:physics` (строки 26): `{}`
- `minecraft:on_death` (строки 27): `{"event":"damage_player","target":"self"}`
- `minecraft:environment_sensor` (строки 28): `[{"on_environment":{"filters":{"all_of":[{"test":"is_family","subject":"self","value":"effect99_entities"}]},"event":"shulker_shield_clear_effect"}}]`

### Группы компонентов

- `minecraft:shulker_shield` (строки 18,44): `{}`
- `despawn` (строки 11,14,19,47): `{"minecraft:despawn":{}}`

### События

**`shulker_shield_clear_effect`** (строки 35,41):

- `$` — поля действия: `{"run_command":{"command":["effect @s levitation 0 0"]}}`

**`shulker_shield`** (строки 42):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:shulker_shield"]}}`

**`minecraft:despawn`** (строки 19,47):

- `$` — поля действия: `{"add":{"component_groups":["despawn"]},"run_command":{"command":["event entity @p[family=shulker_sword,r=6] stop_shulker_sword_event"]}}`

**`damage_player`** (строки 27,49):

- `$` — поля действия: `{"run_command":{"command":["effect @p[r=1,family=shulker_sword] instant_damage 1 2 true"]}}`

## `minecraft:skeleton`

- Путь `Swords_B/entities/skeleton.json`; format_version `"1.13.0"`.
- description: `{"identifier":"minecraft:skeleton","is_spawnable":true,"is_summonable":true,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:experience_reward` (строки 83): `{"on_death":"query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"}`
- `minecraft:damage_sensor` (строки 12,86): `{"triggers":[{"on_damage":{"filters":{"all_of":[{"test":"is_family","subject":"other","value":"player"},{"test":"has_damage","value":"fatal"}]},"event":"bone_sword"},"deals_damage":true}]}`
- `minecraft:collision_box` (строки 105): `{"width":0.6,"height":1.9}`
- `minecraft:type_family` (строки 109): `{"family":["skeleton","undead","monster","mob"]}`
- `minecraft:breathable` (строки 112): `{"total_supply":15,"suffocate_time":0,"breathes_water":true}`
- `minecraft:burns_in_daylight` (строки 118): `{}`
- `minecraft:health` (строки 121): `{"value":20,"max":20}`
- `minecraft:hurt_on_condition` (строки 125): `{"damage_conditions":[{"filters":{"test":"in_lava","subject":"self","operator":"==","value":true},"cause":"lava","damage_per_tick":4}]}`
- `minecraft:loot` (строки 134): `{"table":"loot_tables/entities/skeleton.json"}`
- `minecraft:movement` (строки 137): `{"value":0.25}`
- `minecraft:navigation.walk` (строки 140): `{"is_amphibious":true,"avoid_sun":true,"avoid_water":true}`
- `minecraft:movement.basic` (строки 145): `{}`
- `minecraft:jump.static` (строки 147): `{}`
- `minecraft:can_climb` (строки 149): `{}`
- `minecraft:nameable` (строки 151): `{}`
- `minecraft:equipment` (строки 153): `{"table":"loot_tables/entities/skeleton_gear.json"}`
- `minecraft:shooter` (строки 42,156): `{"type":"Arrow","def":"minecraft:arrow"}`
- `minecraft:environment_sensor` (строки 46,68,160): `{"triggers":{"filters":{"test":"is_underwater","subject":"self","operator":"==","value":true},"event":"minecraft:melee_mode"}}`
- `minecraft:behavior.ranged_attack` (строки 37,171): `{"attack_interval_min":1,"attack_interval_max":3,"attack_radius":15}`
- `minecraft:behavior.hurt_by_target` (строки 176): `{"priority":1}`
- `minecraft:behavior.nearest_attackable_target` (строки 179): `{"priority":2,"reselect_targets":true,"entity_types":[{"filters":{"test":"is_family","subject":"other","value":"player"},"max_dist":16},{"filters":{"test":"is_family","subject":"other","value":"irongolem"},"max_dist":16},{"filters":{"all_of":[{"test":"is_family","subject":"other","value":"baby_turtle"},{"test":"in_water","subject":"other","operator":"!=","value":true}]},"max_dist":16}],"must_see":true}`
- `minecraft:behavior.flee_sun` (строки 220): `{"priority":2,"speed_multiplier":1}`
- `minecraft:behavior.avoid_mob_type` (строки 224): `{"priority":4,"entity_types":[{"filters":{"test":"is_family","subject":"other","value":"wolf"},"max_dist":6,"walk_speed_multiplier":1.2,"sprint_speed_multiplier":1.2}]}`
- `minecraft:behavior.random_stroll` (строки 239): `{"priority":5,"speed_multiplier":1}`
- `minecraft:behavior.look_at_player` (строки 243): `{"priority":6,"look_distance":8}`
- `minecraft:behavior.random_look_around` (строки 247): `{"priority":6}`
- `minecraft:physics` (строки 250): `{}`
- `minecraft:pushable` (строки 252): `{"is_pushable":true,"is_pushable_by_piston":true}`

### Группы компонентов

- `minecraft:lightning_immune` (строки 11,282): `{"minecraft:damage_sensor":{"triggers":[{"on_damage":{"filters":{"all_of":[{"test":"is_family","subject":"other","value":"player"},{"test":"has_damage","value":"fatal"}]},"event":"bone_sword"},"deals_damage":true},{"on_damage":{"filters":{"other_with_families":"lightning"}},"deals_damage":false}]}}`
- `minecraft:ranged_attack` (строки 36,261,285,290): `{"minecraft:behavior.ranged_attack":{"attack_interval_min":1,"attack_interval_max":3,"attack_radius":15},"minecraft:shooter":{"type":"Arrow","def":"minecraft:arrow"},"minecraft:environment_sensor":{"triggers":{"filters":{"test":"is_underwater","subject":"self","operator":"==","value":true},"event":"minecraft:melee_mode"}}}`
- `minecraft:melee_attack` (строки 58,286,289): `{"minecraft:behavior.melee_attack":{"priority":4,"target_dist":1.2,"speed_multiplier":1.25,"track_target":true},"minecraft:attack":{"damage":3},"minecraft:environment_sensor":{"triggers":{"filters":{"test":"in_water","subject":"self","operator":"==","value":false},"event":"minecraft:ranged_mode"}}}`

### События

**`minecraft:entity_spawned`** (строки 258):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:ranged_attack"]}}`

**`bone_sword`** (строки 25,99,265):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"all_of":[{"test":"has_biome_tag","value":"desert"},{"test":"is_brightness","operator":"<","value":0.49}]}}`
  - `$.sequence[0].randomize`: альтернативы, веса `[993,7]`, сумма 1000:
    - ветвь 0, weight `993`; условная доля 993/1000 (99.3%):
      - пустое действие
    - ветвь 1, weight `7`; условная доля 7/1000 (0.7%):
      - `$.sequence[0].randomize[1]` — поля действия: `{"run_command":{"command":["structure load bone_sword ~ ~ ~"]}}`

**`minecraft:spring_trap`** (строки 281):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:lightning_immune"]}}`

**`minecraft:melee_mode`** (строки 54,168,284):

- `$` — поля действия: `{"remove":{"component_groups":["minecraft:ranged_attack"]},"add":{"component_groups":["minecraft:melee_attack"]}}`

**`minecraft:ranged_mode`** (строки 76,288):

- `$` — поля действия: `{"remove":{"component_groups":["minecraft:melee_attack"]},"add":{"component_groups":["minecraft:ranged_attack"]}}`

## `entity:slime_damage`

- Путь `Swords_B/entities/slime_damage.json`; format_version `"1.13.0"`.
- description: `{"identifier":"entity:slime_damage","runtime_identifier":"minecraft:snowball","is_spawnable":false,"is_summonable":true,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 16): `{"family":["effect99_entities"]}`
- `minecraft:timer` (строки 18): `{"time":[0.1,0.1],"looping":true,"time_down_event":{"event":"minecraft:despawn","target":"self"}}`
- `minecraft:collision_box` (строки 21): `{"width":0.0,"height":0.0}`
- `minecraft:projectile` (строки 25): `{"on_hit":{"impact_damage":{"damage":1,"knockback":true,"destroy_on_hit":true},"remove_on_hit":{}},"power":1.5,"gravity":0.1,"angle_offset":0.0}`
- `minecraft:physics` (строки 38): `{}`
- `minecraft:pushable` (строки 40): `{"is_pushable":false,"is_pushable_by_piston":true}`

### Группы компонентов

- `despawn` (строки 12,46): `{"minecraft:despawn":{}}`

### События

**`minecraft:despawn`** (строки 12,19,46):

- `$` — поля действия: `{"add":{"component_groups":["despawn"]}}`

## `entity:slime_king`

- Путь `Swords_B/entities/slime_king.json`; format_version `"1.13.0"`.
- description: `{"identifier":"entity:slime_king","runtime_identifier":"minecraft:slime","is_spawnable":true,"is_summonable":true,"is_experimental":false}`.
- **Повторяющиеся ключи: `["minecraft:movement.jump"]`; следующие выписки могут потерять ранее встреченные значения. Обязательно читать исходник.**

### Постоянные компоненты

- `minecraft:experience_reward` (строки 30): `{"on_death":"query.last_hit_by_player ? Math.Random(1,3) : 40"}`
- `minecraft:type_family` (строки 33): `{"family":["slime","monster","mob","slime_king"]}`
- `minecraft:attack` (строки 36): `{"damage":9}`
- `minecraft:scale` (строки 39): `{"value":4.3}`
- `minecraft:collision_box` (строки 42): `{"width":0.5,"height":0.5}`
- `minecraft:breathable` (строки 46): `{"total_supply":15,"suffocate_time":0}`
- `minecraft:navigation.walk` (строки 50): `{"can_path_over_water":true,"avoid_water":true}`
- `minecraft:jump.static` (строки 54): `{}`
- `minecraft:can_climb` (строки 56): `{}`
- `minecraft:movement` (строки 58): `{"value":1.1}`
- `minecraft:movement.jump` (строки 61,72): `{"jump_delay":[0.16,0.4]}`
- `minecraft:nameable` (строки 64): `{}`
- `minecraft:health` (строки 66): `{"value":300}`
- `minecraft:knockback_resistance` (строки 69): `{"value":0.5}`
- `minecraft:behavior.slime_float` (строки 75): `{"priority":1}`
- `minecraft:behavior.slime_attack` (строки 78): `{"priority":3}`
- `minecraft:behavior.slime_random_direction` (строки 81): `{"priority":4}`
- `minecraft:behavior.slime_keep_on_jumping` (строки 84): `{"priority":5}`
- `minecraft:behavior.nearest_attackable_target` (строки 87): `{"priority":2,"entity_types":[{"filters":{"any_of":[{"test":"is_family","subject":"other","value":"player"},{"test":"is_family","subject":"other","value":"snowgolem"},{"test":"is_family","subject":"other","value":"irongolem"}]},"max_dist":38}],"must_see":true}`
- `minecraft:damage_sensor` (строки 115): `{"triggers":[{"on_damage":{"filters":{"test":"is_family","subject":"other","value":"player"},"event":"health_bar"},"deals_damage":true},{"on_damage":{"filters":{"all_of":[{"test":"has_damage","subject":"self","value":"fall"}]},"event":"fall_damage"},"deals_damage":false}]}`
- `minecraft:environment_sensor` (строки 131): `{"triggers":[{"filters":{},"event":"slime_effects"}]}`
- `minecraft:physics` (строки 139): `{}`
- `minecraft:pushable` (строки 141): `{"is_pushable":true,"is_pushable_by_piston":true}`

### Группы компонентов

- `minecraft:slime_large` (строки 12): `{}`
- `minecraft:slime_medium` (строки 14): `{}`
- `minecraft:slime_small` (строки 16): `{}`
- `health_bar` (строки 18,119,149,153): `{"minecraft:boss":{"should_darken_sky":false,"name":"§l§aKing Slime","hud_range":32}}`
- `despawn` (строки 25,147): `{"minecraft:despawn":{}}`

### События

**`minecraft:despawn`** (строки 26,147):

- `$` — поля действия: `{"add":{"component_groups":["despawn"]}}`

**`health_bar`** (строки 18,119,149,153):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"add":{"component_groups":["health_bar"]}}`
  - `$.sequence[1].randomize`: альтернативы, веса `[95,5]`, сумма 100:
    - ветвь 0, weight `95`; условная доля 19/20 (95%):
      - пустое действие
    - ветвь 1, weight `5`; условная доля 1/20 (5%):
      - `$.sequence[1].randomize[1]` — поля действия: `{"run_command":{"command":["effect @s jump_boost 1 15 true"]}}`

**`fall_damage`** (строки 125,169):

- `$` — поля действия: `{"run_command":{"command":["effect @e[r=3,family=!slime_king] instant_damage 1 1 true","effect @e[r=4,type=iron_golem] instant_damage 1 2 true"]}}`

**`slime_effects`** (строки 135,171):

- `$` — поля действия: `{"run_command":{"command":["effect @s jump_boost 1 0 true","damage @p[r=1.8] 4 magic","damage @e[r=1.5,family=!slime_king] 2 magic"]}}`

## `minecraft:small_fireball`

- Путь `Swords_B/entities/small_fireball.json`; format_version `"1.12.0"`.
- description: `{"identifier":"minecraft:small_fireball","is_spawnable":false,"is_summonable":false,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 12,66): `{"family":["small_fireball"]}`
- `minecraft:collision_box` (строки 67): `{"width":0.31,"height":0.31}`
- `minecraft:projectile` (строки 15,40,71): `{"on_hit":{"impact_damage":{"damage":5,"knockback":false,"catch_fire":true,"semi_random_diff_damage":false},"catch_fire":{"fire_affected_by_griefing":true},"remove_on_hit":{}},"power":1.3,"gravity":0.0,"inertia":1,"liquid_inertia":1,"anchor":2,"offset":[0,0.5,0],"semi_random_diff_damage":true,"uncertainty_base":10.0,"reflect_on_hurt":true}`
- `minecraft:physics` (строки 94): `{}`
- `minecraft:pushable` (строки 96): `{"is_pushable":true,"is_pushable_by_piston":true}`

### Группы компонентов

- `shot_by_the_blaze` (строки 11,12,118,136): `{"minecraft:type_family":{"family":["small_fireball","shot_by_the_blaze"]}}`
- `gravity_enable` (строки 14,107,124): `{"minecraft:projectile":{"on_hit":{"impact_damage":{"damage":5,"knockback":false,"catch_fire":true,"semi_random_diff_damage":false},"catch_fire":{"fire_affected_by_griefing":true},"remove_on_hit":{}},"power":1.3,"gravity":0.02,"inertia":1,"liquid_inertia":1,"anchor":2,"offset":[0,0.5,0],"semi_random_diff_damage":true,"uncertainty_base":10.0,"reflect_on_hurt":true}}`
- `minecraft:inertia_disable` (строки 39,134,139): `{"minecraft:projectile":{"on_hit":{"impact_damage":{"damage":5,"knockback":false,"catch_fire":true,"semi_random_diff_damage":false},"catch_fire":{"fire_affected_by_griefing":true},"remove_on_hit":{}},"power":0,"gravity":0.06,"inertia":0,"liquid_inertia":0,"anchor":0,"offset":[0,0.0,0],"semi_random_diff_damage":false,"uncertainty_base":0,"reflect_on_hurt":false}}`

### События

**`minecraft:entity_spawned`** (строки 102):

- `$.sequence`: 3 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"other","value":"player"},"add":{"component_groups":["gravity_enable"]},"run_command":{"command":["playsound mob.ghast.fireball @a[r=12] ~ ~ ~"]}}`
  - `$.sequence[1]` — поля действия: `{"filters":{"test":"is_family","subject":"other","value":"blaze"},"add":{"component_groups":["shot_by_the_blaze"]}}`
  - `$.sequence[2]` — поля действия: `{"filters":{"test":"is_family","subject":"other","value":"fire_sword_skill"},"add":{"component_groups":["gravity_enable"]},"run_command":{"command":["playsound mob.ghast.fireball @a[r=18] ~ ~ ~"]}}`

**`minecraft:inertia_disable`** (строки 39,134,139):

- `$` — поля действия: `{"remove":{"component_groups":["shot_by_the_blaze"]},"add":{"component_groups":["minecraft:inertia_disable"]}}`

## `minecraft:snowball`

- Путь `Swords_B/entities/snowball.json`; format_version `"1.12.0"`.
- description: `{"identifier":"minecraft:snowball","is_spawnable":false,"is_summonable":true,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 41): `{"family":["snowball"]}`
- `minecraft:collision_box` (строки 44): `{"width":0.25,"height":0.25}`
- `minecraft:projectile` (строки 12,48): `{"on_hit":{"impact_damage":{"filter":"blaze","damage":3,"knockback":true},"remove_on_hit":{},"particle_on_hit":{"particle_type":"snowballpoof","num_particles":6,"on_entity_hit":true,"on_other_hit":true}},"power":1.5,"gravity":0.03,"angle_offset":0}`
- `minecraft:physics` (строки 67): `{}`
- `minecraft:pushable` (строки 68): `{"is_pushable":true,"is_pushable_by_piston":true}`

### Группы компонентов

- `ice_sword` (строки 11,17,74,79): `{"minecraft:projectile":{"on_hit":{"definition_event":{"affect_projectile":true,"event_trigger":{"event":"ice_sword","target":"self"}},"impact_damage":{"filter":"blaze","damage":3,"knockback":true},"remove_on_hit":{},"particle_on_hit":{"particle_type":"snowballpoof","num_particles":6,"on_entity_hit":true,"on_other_hit":true}},"power":1.5,"gravity":0.03,"angle_offset":0}}`

### События

**`ice_sword`** (строки 11,17,74,79):

- `$` — поля действия: `{"run_command":{"command":["fill ~ ~ ~ ~ ~ ~ snow_layer 0 replace air"]}}`

**`minecraft:entity_spawned`** (строки 75):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"has_equipment","subject":"other","domain":"hand","value":"effect:ice_sword"},"add":{"component_groups":["ice_sword"]}}`

## `minecraft:spider`

- Путь `Swords_B/entities/spider.json`; format_version `"1.13.0"`.
- description: `{"identifier":"minecraft:spider","is_spawnable":true,"is_summonable":true,"is_experimental":false,"scripts":{"animate":["despawn","climb_spider"]},"animations":{"despawn":"controller.animation.despawn","climb_spider":"controller.animation.climb_spider"}}`.

### Постоянные компоненты

- `minecraft:experience_reward` (строки 187): `{"on_death":"query.last_hit_by_player ? 5 : 0"}`
- `minecraft:nameable` (строки 190): `{}`
- `minecraft:type_family` (строки 21,192): `{"family":["spider","monster","mob","arthropod"]}`
- `minecraft:breathable` (строки 195): `{"total_supply":15,"suffocate_time":0}`
- `minecraft:loot` (строки 26,199): `{"table":"loot_tables/entities/spider.json"}`
- `minecraft:collision_box` (строки 202): `{"width":1.4,"height":0.9}`
- `minecraft:health` (строки 27,206): `{"value":16,"max":16}`
- `minecraft:hurt_on_condition` (строки 210): `{"damage_conditions":[{"filters":{"test":"in_lava","subject":"self","operator":"==","value":true},"cause":"lava","damage_per_tick":4}]}`
- `minecraft:movement` (строки 219): `{"value":0.3}`
- `minecraft:navigation.climb` (строки 222): `{"can_path_over_water":true}`
- `minecraft:movement.basic` (строки 225): `{}`
- `minecraft:jump.static` (строки 227): `{}`
- `minecraft:can_climb` (строки 229): `{}`
- `minecraft:attack` (строки 231): `{"damage":3}`
- `minecraft:behavior.float` (строки 234): `{"priority":1}`
- `minecraft:behavior.mount_pathing` (строки 237): `{"priority":5,"speed_multiplier":1.25,"target_dist":0.0,"track_target":true}`
- `minecraft:rideable` (строки 28,50,64,78,243): `{"seat_count":1,"family_types":["zombie"],"seats":{"position":[0.0,0.54,-0.1]}}`
- `minecraft:physics` (строки 252): `{}`
- `minecraft:pushable` (строки 254): `{"is_pushable":true,"is_pushable_by_piston":true}`

### Группы компонентов

- `despawn` (строки 10,13,18,404): `{"minecraft:despawn":{}}`
- `minecraft:spider_player_jockey` (строки 20,396): `{"minecraft:type_family":{"family":["spider","monster","mob","arthropod","spider_sword"]},"minecraft:input_ground_controlled":{},"minecraft:behavior.controlled_by_player":{"priority":0},"minecraft:can_power_jump":{},"minecraft:horse.jump_strength":{"value":{"range_min":0.4,"range_max":0.7}},"minecraft:loot":{"table":"loot_tables/entities/empty.json"},"minecraft:health":{"value":20,"max":20},"minecraft:rideable":{"seat_count":1,"family_types":["player"],"seats":{"position":[0.0,0.54,0.0]}},"minecraft:environment_sensor":{"triggers":[{"filters":{},"event":"not_climb"}]}}`
- `minecraft:spider_jockey` (строки 46,328): `{"minecraft:addrider":{"entity_type":"minecraft:skeleton"},"minecraft:rideable":{"seat_count":1,"family_types":["skeleton"],"seats":{"position":[0.0,0.54,0.0]}}}`
- `minecraft:spider_stray_jockey` (строки 60,292): `{"minecraft:addrider":{"entity_type":"minecraft:skeleton.stray"},"minecraft:rideable":{"seat_count":1,"family_types":["skeleton"],"seats":{"position":[0.0,0.54,0.0]}}}`
- `minecraft:spider_wither_jockey` (строки 74,306): `{"minecraft:addrider":{"entity_type":"minecraft:skeleton.wither"},"minecraft:rideable":{"seat_count":1,"family_types":["skeleton"],"seats":{"position":[0.0,0.54,0.0]}}}`
- `minecraft:spider_neutral` (строки 88,293,307,329,340,351,368,390): `{"minecraft:environment_sensor":{"triggers":{"filters":{"test":"is_brightness","operator":"<","value":0.49},"event":"minecraft:become_hostile"}},"minecraft:on_target_acquired":{"event":"minecraft:become_angry"}}`
- `minecraft:spider_hostile` (строки 103,356,363,389): `{"minecraft:environment_sensor":{"triggers":{"filters":{"test":"is_brightness","operator":">","value":0.49},"event":"minecraft:become_neutral"}},"minecraft:on_target_acquired":{"event":"minecraft:become_angry"},"minecraft:behavior.nearest_attackable_target":{"priority":2,"entity_types":[{"filters":{"any_of":[{"test":"is_family","subject":"other","value":"player"},{"test":"is_family","subject":"other","value":"snowgolem"},{"test":"is_family","subject":"other","value":"irongolem"}]},"max_dist":16}],"attack_interval":5,"must_see":true}}`
- `minecraft:spider_angry` (строки 147,375,382): `{"minecraft:angry":{"duration":10,"duration_delta":3,"calm_event":{"event":"minecraft:become_calm","target":"self"}},"minecraft:behavior.leap_at_target":{"priority":4,"yd":0.4,"must_be_on_ground":false},"minecraft:behavior.melee_attack":{"priority":3,"speed_multiplier":1.0,"track_target":true,"reach_multiplier":0.8}}`
- `minecraft:default_spider` (строки 168,264,391): `{"minecraft:behavior.hurt_by_target":{"priority":1},"minecraft:behavior.random_stroll":{"priority":6,"speed_multiplier":0.8},"minecraft:behavior.look_at_player":{"priority":7,"look_distance":6.0,"probability":0.02},"minecraft:behavior.random_look_around":{"priority":7}}`

### События

**`minecraft:entity_spawned`** (строки 261):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"add":{"component_groups":["minecraft:default_spider"]}}`
  - `$.sequence[1].randomize`: альтернативы, веса `[1,99]`, сумма 100:
    - ветвь 0, weight `1`; условная доля 1/100 (1%):
      - `$.sequence[1].randomize[0].randomize`: альтернативы, веса `[80,80,20]`, сумма 180:
        - ветвь 0, weight `80`; условная доля 4/9 (44.4444%):
          - `$.sequence[1].randomize[0].randomize[0]` — поля действия: `{"filters":{"all_of":[{"test":"is_daytime","value":false},{"test":"is_snow_covered","value":true},{"test":"is_underground","value":false}]},"remove":{},"add":{"component_groups":["minecraft:spider_stray_jockey","minecraft:spider_neutral"]}}`
        - ветвь 1, weight `80`; условная доля 4/9 (44.4444%):
          - `$.sequence[1].randomize[0].randomize[1]` — поля действия: `{"filters":{"test":"is_biome","value":"the_nether"},"remove":{},"add":{"component_groups":["minecraft:spider_wither_jockey","minecraft:spider_neutral"]}}`
        - ветвь 2, weight `20`; условная доля 1/9 (11.1111%):
          - `$.sequence[1].randomize[0].randomize[2]` — поля действия: `{"filters":{"any_of":[{"test":"is_daytime","value":false},{"test":"is_underground","value":true}]},"remove":{},"add":{"component_groups":["minecraft:spider_jockey","minecraft:spider_neutral"]}}`
    - ветвь 1, weight `99`; условная доля 99/100 (99%):
      - `$.sequence[1].randomize[1]` — поля действия: `{"remove":{},"add":{"component_groups":["minecraft:spider_neutral"]}}`

**`minecraft:become_hostile`** (строки 96,348):

- `$` — поля действия: `{"remove":{"component_groups":["minecraft:spider_neutral"]},"add":{"component_groups":["minecraft:spider_hostile"]}}`

**`minecraft:become_neutral`** (строки 111,360):

- `$` — поля действия: `{"remove":{"component_groups":["minecraft:spider_hostile"]},"add":{"component_groups":["minecraft:spider_neutral"]}}`

**`minecraft:become_angry`** (строки 100,115,372):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:spider_angry"]}}`

**`minecraft:become_calm`** (строки 152,379):

- `$` — поля действия: `{"remove":{"component_groups":["minecraft:spider_angry"]}}`

**`minecraft:spider_sword`** (строки 386):

- `$` — поля действия: `{"remove":{"component_groups":["minecraft:spider_hostile","minecraft:spider_neutral","minecraft:default_spider"]},"add":{"component_groups":["minecraft:spider_player_jockey"]}}`

**`minecraft:despawn`** (строки 18,400):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"spider_sword"},"add":{"component_groups":["despawn"]},"run_command":{"command":["particle minecraft:example_linearcurve ~ ~ ~","playsound random.fizz @a[r=16]"]}}`

**`not_climb`** (строки 41,409):

- `$` — поля действия: `{"run_command":{"command":["execute @s ~~~ detect ~0.8 ~ ~ air 0 execute @s ~~~ detect ~-0.8 ~ ~ air 0 execute @s ~~~ detect ~ ~ ~0.8 air 0 execute @s ~~~ detect ~ ~ ~-0.8 air 0 effect @s levitation 0 0 true"]}}`

## `minecraft:tnt`

- Путь `Swords_B/entities/tnt.json`; format_version `"1.12.0"`.
- description: `{"identifier":"minecraft:tnt","is_spawnable":false,"is_summonable":true,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 52): `{"family":["tnt","inanimate"]}`
- `minecraft:collision_box` (строки 55): `{"width":0.98,"height":0.98}`
- `minecraft:physics` (строки 59): `{}`
- `minecraft:pushable` (строки 61): `{"is_pushable":false,"is_pushable_by_piston":true}`

### Группы компонентов

- `giant_tnt` (строки 11,72,74): `{"minecraft:timer":{"time":[7.99,7.99],"looping":false,"time_down_event":{"event":"camerashake","target":"self"}},"minecraft:scale":{"value":2},"minecraft:explode":{"fuse_length":8,"fuse_lit":true,"power":16,"causes_fire":true,"destroy_affected_by_griefing":true},"minecraft:environment_sensor":[{"on_environment":{"filters":{"all_of":[{"test":"is_family","value":"tnt"}]},"event":"particle"}}]}`
- `from_explosion` (строки 30,69,70): `{"minecraft:explode":{"fuse_length":{"range_min":0.5,"range_max":2.0},"fuse_lit":true,"power":4,"causes_fire":false}}`
- `default_tnt` (строки 41,67,73): `{"minecraft:explode":{"fuse_length":4,"fuse_lit":true,"power":4,"causes_fire":false,"destroy_affected_by_griefing":true}}`

### События

**`minecraft:entity_spawned`** (строки 67):

- `$` — поля действия: `{"add":{"component_groups":["default_tnt"]}}`

**`from_explosion`** (строки 30,69,70):

- `$` — поля действия: `{"add":{"component_groups":["from_explosion"]}}`

**`giant_tnt`** (строки 11,72,74):

- `$` — поля действия: `{"remove":{"component_groups":["default_tnt"]},"add":{"component_groups":["giant_tnt"]}}`

**`particle`** (строки 25,76):

- `$` — поля действия: `{"run_command":{"command":["particle minecraft:example_linearcurve ~ ~ ~"]}}`

**`camerashake`** (строки 13,78):

- `$` — поля действия: `{"run_command":{"command":["camerashake add @a[r=32] 0.2 0.8 positional","playsound random.explode @a[r=32] ~ ~ ~ 2 0.4 2"]}}`

## `entity:ultra_instinct_explode`

- Путь `Swords_B/entities/ultra_instinct_explode.json`; format_version `"1.12.0"`.
- description: `{"identifier":"entity:ultra_instinct_explode","is_spawnable":false,"is_summonable":true,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 6): `{"family":["effect99_entities"]}`
- `minecraft:collision_box` (строки 7): `{"width":0.0,"height":0.0}`
- `minecraft:damage_sensor` (строки 8): `{"triggers":{"cause":"all","deals_damage":false}}`
- `minecraft:explode` (строки 9): `{"fuse_length":0,"fuse_lit":true,"power":8,"causes_fire":false,"max_resistance":4.0,"destroy_affected_by_griefing":true}`
- `minecraft:physics` (строки 10): `{}`

### Группы компонентов


### События

## `entity:ultra_instinct_projectile`

- Путь `Swords_B/entities/ultra_instinct_projectile.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:ultra_instinct_projectile","runtime_identifier":"minecraft:snowball","is_spawnable":false,"is_summonable":true,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:despawn` (строки 13): `{"despawn_from_simulation_edge":true}`
- `minecraft:ageable` (строки 16): `{"duration":3,"grow_up":{"event":"minecraft:end_scale","target":"self"}}`
- `minecraft:scale_by_age` (строки 20): `{"start_scale":1,"end_scale":3}`
- `minecraft:type_family` (строки 21): `{"family":["ultra_instinct_sword","effect99_entities"]}`
- `minecraft:collision_box` (строки 22): `{"width":0,"height":0}`
- `minecraft:projectile` (строки 26): `{"on_hit":{"definition_event":{"affect_projectile":true,"event_trigger":{"event":"minecraft:explode","target":"self"}},"impact_damage":{"damage":64,"knockback":true}},"power":2,"gravity":0,"inertia":1,"liquid_inertia":2,"uncertainty_base":0,"uncertainty_multiplier":0,"anchor":1,"offset":[0,0,0],"reflect_on_hurt":false}`
- `minecraft:environment_sensor` (строки 50): `[{"on_environment":{"filters":{"all_of":[{"test":"is_family","value":"ultra_instinct_sword"}]},"event":"projectile_particle"}}]`
- `minecraft:pushable` (строки 51): `{"is_pushable":false,"is_pushable_by_piston":false}`
- `minecraft:physics` (строки 52): `{"has_gravity":false,"has_collision":false}`

### Группы компонентов


### События

**`minecraft:explode`** (строки 31,55):

- `$` — поля действия: `{"run_command":{"command":["summon entity:ultra_instinct_explode"]}}`

**`projectile_particle`** (строки 50,58):

- `$` — поля действия: `{"run_command":{"command":["particle minecraft:example_flipbook ~ ~ ~","kill @e[type=item,r=24]"]}}`

## `entity:web`

- Путь `Swords_B/entities/web.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:web","runtime_identifier":"minecraft:snowball","is_spawnable":false,"is_summonable":true,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:type_family` (строки 12,15): `{"family":["effect99_entities","shoot_sound"]}`
- `minecraft:scale` (строки 16): `{"value":0.5}`
- `minecraft:collision_box` (строки 19): `{"width":0.25,"height":0.25}`
- `minecraft:projectile` (строки 23): `{"on_hit":{"definition_event":{"affect_projectile":true,"event_trigger":{"event":"set_web","target":"self"}},"impact_damage":{"damage":1,"knockback":true,"destroy_on_hit":true},"remove_on_hit":{},"particle_on_hit":{"particle_type":"iconcrack","num_particles":1,"on_entity_hit":true,"on_other_hit":true}},"hit_sound":"pop","power":1.5,"gravity":0.03,"angle_offset":0.0}`
- `minecraft:physics` (строки 50): `{}`
- `minecraft:environment_sensor` (строки 51): `[{"on_environment":{"filters":{"all_of":[{"test":"is_family","subject":"self","value":"shoot_sound"}]},"event":"shoot_sound"}}]`

### Группы компонентов

- `remove_shoot_sound` (строки 12,68): `{"minecraft:type_family":{"family":["effect99_entities"]}}`

### События

**`set_web`** (строки 28,60):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"run_command":{"command":["fill ~ ~ ~ ~ ~ ~ web 0 replace air"]}}`

**`shoot_sound`** (строки 15,54,55,67):

- `$` — поля действия: `{"add":{"component_groups":["remove_shoot_sound"]},"run_command":{"command":["playsound random.bow @a[r=12] ~ ~ ~ 1 0.33"]}}`

## `minecraft:witch`

- Путь `Swords_B/entities/witch.json`; format_version `"1.13.0"`.
- description: `{"identifier":"minecraft:witch","is_spawnable":true,"is_summonable":true,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:experience_reward` (строки 92): `{"on_death":"query.last_hit_by_player ? (query.is_baby ? 12 : 5) + (Math.die_roll(query.equipment_count,1,3)) : 0"}`
- `minecraft:breathable` (строки 95): `{"total_supply":15,"suffocate_time":0}`
- `minecraft:nameable` (строки 99): `{}`
- `minecraft:loot` (строки 25,101): `{"table":"loot_tables/entities/witch.json"}`
- `minecraft:health` (строки 37,104): `{"value":26,"max":26}`
- `minecraft:hurt_on_condition` (строки 108): `{"damage_conditions":[{"filters":{"test":"in_lava","subject":"self","operator":"==","value":true},"cause":"lava","damage_per_tick":4}]}`
- `minecraft:movement` (строки 117): `{"value":0.25}`
- `minecraft:navigation.walk` (строки 120): `{"can_path_over_water":true,"avoid_water":false}`
- `minecraft:movement.basic` (строки 124): `{}`
- `minecraft:jump.static` (строки 126): `{}`
- `minecraft:can_climb` (строки 128): `{}`
- `minecraft:behavior.float` (строки 130): `{"priority":1}`
- `minecraft:behavior.ranged_attack` (строки 133): `{"priority":2,"speed_multiplier":1.0,"attack_interval_min":3,"attack_interval_max":3,"attack_radius":10.0}`
- `minecraft:behavior.random_stroll` (строки 140): `{"priority":4,"speed_multiplier":1.0}`
- `minecraft:behavior.look_at_player` (строки 144): `{"priority":5,"look_distance":8.0}`
- `minecraft:behavior.random_look_around` (строки 148): `{"priority":5,"look_distance":8.0}`
- `minecraft:behavior.hurt_by_target` (строки 152): `{"priority":1}`
- `minecraft:behavior.nearest_attackable_target` (строки 155): `{"priority":2,"entity_types":[{"filters":{"any_of":[{"test":"is_family","subject":"other","value":"player"},{"test":"is_family","subject":"other","value":"snowgolem"},{"test":"is_family","subject":"other","value":"irongolem"}]},"max_dist":10}],"must_reach":true}`
- `minecraft:type_family` (строки 22,183): `{"family":["witch","monster","mob"]}`
- `minecraft:collision_box` (строки 186): `{"width":0.6,"height":1.9}`
- `minecraft:physics` (строки 190): `{}`
- `minecraft:pushable` (строки 192): `{"is_pushable":true,"is_pushable_by_piston":true}`
- `minecraft:follow_range` (строки 31,196): `{"value":64}`

### Группы компонентов

- `minecraft:default_witch` (строки 11,205): `{"minecraft:variant":{"value":0}}`
- `minecraft:grass_witch` (строки 16,209,224,225): `{"minecraft:variant":{"value":1}}`
- `grass_witch` (строки 21,23,209,225): `{"minecraft:type_family":{"family":["witch","monster","mob","grass_witch"]},"minecraft:loot":{},"minecraft:on_death":{"event":"grass_sword","target":"self"},"minecraft:follow_range":{"value":80},"minecraft:scale":{"value":1.1},"minecraft:health":{"value":32,"max":32},"minecraft:environment_sensor":{"triggers":[{"filters":{},"event":"grass_witch_skill"}]}}`
- `minecraft:celebrate` (строки 50,241,244): `{"minecraft:behavior.celebrate":{"priority":5,"celebration_sound":"celebrate","sound_interval":{"range_min":2.0,"range_max":7.0},"jump_interval":{"range_min":1.0,"range_max":3.5},"duration":30.0,"on_celebration_end_event":{"event":"minecraft:stop_celebrating","target":"self"}}}`
- `minecraft:raid_configuration` (строки 69,236): `{"minecraft:dweller":{"dwelling_type":"village","dweller_role":"hostile","update_interval_base":60,"update_interval_variant":40,"can_find_poi":false,"can_migrate":false,"first_founding_reward":0},"minecraft:behavior.move_to_village":{"priority":3,"speed_multiplier":1.2,"goal_radius":2.0},"minecraft:ambient_sound_interval":{"value":2.0,"range":4.0,"event_name":"ambient.in.raid"}}`

### События

**`minecraft:entity_spawned`** (строки 201):

- `$.randomize`: альтернативы, веса `[80,20]`, сумма 100:
  - ветвь 0, weight `80`; условная доля 4/5 (80%):
    - `$.randomize[0]` — поля действия: `{"add":{"component_groups":["minecraft:default_witch"]}}`
  - ветвь 1, weight `20`; условная доля 1/5 (20%):
    - `$.randomize[1]` — поля действия: `{"add":{"component_groups":["minecraft:grass_witch","grass_witch"]}}`

**`grass_sword`** (строки 28,213):

- `$.randomize`: альтернативы, веса `[80,20]`, сумма 100:
  - ветвь 0, weight `80`; условная доля 4/5 (80%):
    - пустое действие
  - ветвь 1, weight `20`; условная доля 1/5 (20%):
    - `$.randomize[1]` — поля действия: `{"run_command":{"command":["structure load grass_sword ~~~","setblock ~ ~ ~ double_plant 2","playsound dig.grass @a[r=12] ~~~"]}}`

**`minecraft:grass_witch`** (строки 16,209,224,225):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:grass_witch","grass_witch"]}}`

**`grass_witch_skill`** (строки 45,227):

- `$` — поля действия: `{"run_command":{"command":["execute @e[family=!grass_witch,type=!item,type=!entity:grass,type=!xp_orb,type=!arrow,r=8,tag=!grass,family=!shulker_sword] ~ ~ ~ detect ~ ~-0.1 ~ grass 0 execute @s ~ ~ ~ detect ~ ~ ~ air 0 summon entity:grass","execute @e[family=!grass_witch,type=!item,type=!entity:grass,type=!xp_orb,type=!arrow,r=8,tag=!grass,family=!shulker_sword] ~ ~ ~ detect ~ ~-0.1 ~ grass 0 execute @s ~ ~ ~ detect ~ ~ ~ tallgrass 0 summon entity:grass"]}}`

**`minecraft:spawn_for_raid`** (строки 233):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:raid_configuration"]}}`

**`minecraft:start_celebrating`** (строки 240):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:celebrate"]}}`

**`minecraft:stop_celebrating`** (строки 64,243):

- `$` — поля действия: `{"remove":{"component_groups":["minecraft:celebrate"]}}`

## `minecraft:wither`

- Путь `Swords_B/entities/wither.json`; format_version `"1.13.0"`.
- description: `{"identifier":"minecraft:wither","is_spawnable":false,"is_summonable":true,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:experience_reward` (строки 11): `{"on_death":"50"}`
- `minecraft:breathable` (строки 14): `{"total_supply":15,"suffocate_time":0}`
- `minecraft:boss` (строки 18): `{"should_darken_sky":true,"hud_range":55}`
- `minecraft:damage_sensor` (строки 22): `{"triggers":[{"on_damage":{"filters":{"test":"is_family","subject":"other","value":"undead"}},"deals_damage":false},{"on_damage":{"filters":{"all_of":[{"test":"has_equipment","subject":"other","domain":"hand","value":"effect:nether_star_sword"},{"test":"is_family","subject":"other","value":"player"},{"test":"has_damage","value":"fatal"}]},"event":"wither_sword"},"deals_damage":true}]}`
- `minecraft:health` (строки 54): `{"value":600,"max":600}`
- `minecraft:collision_box` (строки 58): `{"width":1,"height":3}`
- `minecraft:fire_immune` (строки 62): `true`
- `minecraft:loot` (строки 63): `{"table":"loot_tables/entities/wither_boss.json"}`
- `minecraft:nameable` (строки 66): `{}`
- `minecraft:movement` (строки 68): `{"value":0.25}`
- `minecraft:navigation.walk` (строки 71): `{"can_path_over_water":true,"avoid_water":true}`
- `minecraft:movement.basic` (строки 75): `{"max_turn":180.0}`
- `minecraft:jump.static` (строки 78): `{}`
- `minecraft:can_climb` (строки 80): `{}`
- `minecraft:can_fly` (строки 82): `{}`
- `minecraft:behavior.float` (строки 84): `{"priority":1}`
- `minecraft:behavior.wither_random_attack_pos_goal` (строки 87): `{"priority":3}`
- `minecraft:behavior.wither_target_highest_damage` (строки 90): `{"priority":1}`
- `minecraft:behavior.hurt_by_target` (строки 93): `{"priority":2}`
- `minecraft:behavior.nearest_attackable_target` (строки 96): `{"priority":3,"entity_types":[{"filters":{"test":"is_family","subject":"other","value":"player"},"max_dist":70},{"filters":{"all_of":[{"test":"is_family","subject":"other","operator":"!=","value":"undead"},{"test":"is_family","subject":"other","operator":"!=","value":"inanimate"}]},"max_dist":70}],"must_see":true}`
- `minecraft:behavior.random_stroll` (строки 125): `{"priority":5,"speed_multiplier":1}`
- `minecraft:behavior.look_at_target` (строки 129): `{"priority":5}`
- `minecraft:behavior.look_at_player` (строки 132): `{"priority":6,"look_distance":8}`
- `minecraft:behavior.random_look_around` (строки 136): `{"priority":7}`
- `minecraft:type_family` (строки 139): `{"family":["wither","skeleton","monster","undead","mob"]}`
- `minecraft:persistent` (строки 142): `{}`
- `minecraft:physics` (строки 144): `{}`
- `minecraft:pushable` (строки 146): `{"is_pushable":true,"is_pushable_by_piston":true}`

### Группы компонентов


### События

**`minecraft:entity_spawned`** (строки 152):


**`wither_sword`** (строки 48,154):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0].randomize`: альтернативы, веса `[87,13]`, сумма 100:
    - ветвь 0, weight `87`; условная доля 87/100 (87%):
      - пустое действие
    - ветвь 1, weight `13`; условная доля 13/100 (13%):
      - `$.sequence[0].randomize[1]` — поля действия: `{"run_command":{"command":["structure load wither_sword ~ ~ ~"]}}`

## `entity:wither_effect`

- Путь `Swords_B/entities/wither_effect.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:wither_effect","runtime_identifier":"minecraft:snowball","is_spawnable":false,"is_summonable":true,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:timer` (строки 16): `{"time":[0.1,0.1],"looping":true,"time_down_event":{"event":"despawn","target":"self"}}`
- `minecraft:projectile` (строки 19): `{"on_hit":{"mob_effect":{"effect":"wither","durationeasy":200,"durationnormal":200,"durationhard":200,"amplifier":0},"impact_damage":{"damage":0,"knockback":true,"destroy_on_hit":true},"particle_on_hit":{}},"power":2,"gravity":0.0,"angle_offset":0.0}`
- `minecraft:type_family` (строки 39): `{"family":["effect99_entities"]}`
- `minecraft:collision_box` (строки 40): `{"width":0.0,"height":0.0}`
- `minecraft:physics` (строки 41): `{}`
- `minecraft:environment_sensor` (строки 42): `[{"on_environment":{"filters":{"all_of":[{"test":"is_family","value":"effect99_entities"}]},"event":"particle"}}]`

### Группы компонентов

- `despawn` (строки 12,17,50): `{"minecraft:despawn":{}}`

### События

**`despawn`** (строки 12,17,50):

- `$` — поля действия: `{"add":{"component_groups":["despawn"]}}`

## `minecraft:wither_skull`

- Путь `Swords_B/entities/wither_skull.json`; format_version `"1.12.0"`.
- description: `{"identifier":"minecraft:wither_skull","is_spawnable":false,"is_summonable":false,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:collision_box` (строки 12,57): `{"width":0.15,"height":0.15}`
- `minecraft:projectile` (строки 16,61): `{"on_hit":{"definition_event":{"affect_projectile":true,"event_trigger":{"event":"minecraft:explode","target":"self"}},"mob_effect":{"effect":"wither","durationeasy":0,"durationnormal":200,"durationhard":800,"amplifier":1}},"power":1.2,"gravity":0.0,"uncertainty_base":7.5,"uncertainty_multiplier":1,"shoot_sound":"bow","hit_sound":"bow.hit","anchor":1,"offset":[0,-0.1,0],"inertia":1.0,"liquid_inertia":1.0,"shoot_target":false}`
- `minecraft:physics` (строки 90): `{}`
- `minecraft:pushable` (строки 92): `{"is_pushable":true,"is_pushable_by_piston":true}`

### Группы компонентов

- `wither_sword` (строки 11,102): `{"minecraft:collision_box":{"width":0,"height":0},"minecraft:projectile":{"on_hit":{"definition_event":{"affect_projectile":true,"event_trigger":{"event":"minecraft:explode","target":"self"}},"mob_effect":{"effect":"wither","durationeasy":0,"durationnormal":200,"durationhard":800,"amplifier":1}},"power":1.2,"gravity":0.05,"uncertainty_base":7.5,"uncertainty_multiplier":1,"shoot_sound":"bow","hit_sound":"bow.hit","anchor":1,"offset":[0,-0.1,0],"inertia":1.0,"liquid_inertia":1.0,"shoot_target":false}}`
- `minecraft:exploding` (строки 46,109): `{"minecraft:explode":{"fuse_length":0,"fuse_lit":true,"power":1,"causes_fire":false,"destroy_affected_by_griefing":true}}`

### События

**`minecraft:entity_spawned`** (строки 98):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"has_equipment","subject":"other","domain":"hand","value":"effect:wither_sword"},"add":{"component_groups":["wither_sword"]}}`

**`minecraft:explode`** (строки 21,47,66,106):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:exploding"]}}`

## `minecraft:wither_skull_dangerous`

- Путь `Swords_B/entities/wither_skull_dangerous.json`; format_version `"1.12.0"`.
- description: `{"identifier":"minecraft:wither_skull_dangerous","is_spawnable":false,"is_summonable":false,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:collision_box` (строки 12,60): `{"width":0.15,"height":0.15}`
- `minecraft:projectile` (строки 16,64): `{"on_hit":{"definition_event":{"affect_projectile":true,"event_trigger":{"event":"minecraft:explode","target":"self"}},"mob_effect":{"effect":"wither","durationeasy":0,"durationnormal":200,"durationhard":800,"amplifier":1}},"power":0.6,"gravity":0.0,"uncertainty_base":7.5,"uncertainty_multiplier":1,"shoot_sound":"bow","hit_sound":"bow.hit","anchor":1,"offset":[0,-0.1,0],"is_dangerous":true,"inertia":1.0,"liquid_inertia":1.0,"shoot_target":false,"reflect_on_hurt":true}`
- `minecraft:physics` (строки 95): `{}`
- `minecraft:pushable` (строки 97): `{"is_pushable":true,"is_pushable_by_piston":true}`

### Группы компонентов

- `wither_sword` (строки 11,107): `{"minecraft:collision_box":{"width":0,"height":0},"minecraft:projectile":{"on_hit":{"definition_event":{"affect_projectile":true,"event_trigger":{"event":"minecraft:explode","target":"self"}},"mob_effect":{"effect":"wither","durationeasy":0,"durationnormal":200,"durationhard":800,"amplifier":1}},"power":0.6,"gravity":0.005,"uncertainty_base":7.5,"uncertainty_multiplier":1,"shoot_sound":"bow","hit_sound":"bow.hit","anchor":1,"offset":[0,-0.1,0],"is_dangerous":true,"inertia":1.0,"liquid_inertia":1.0,"shoot_target":false,"reflect_on_hurt":true}}`
- `minecraft:exploding` (строки 48,114): `{"minecraft:explode":{"fuse_length":0,"fuse_lit":true,"power":1,"causes_fire":false,"max_resistance":4.0,"destroy_affected_by_griefing":true}}`

### События

**`minecraft:entity_spawned`** (строки 103):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"has_equipment","subject":"other","domain":"hand","value":"effect:wither_sword"},"add":{"component_groups":["wither_sword"]}}`

**`minecraft:explode`** (строки 21,49,69,111):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:exploding"]}}`

## `minecraft:wolf`

- Путь `Swords_B/entities/wolf.json`; format_version `"1.13.0"`.
- description: `{"identifier":"minecraft:wolf","is_spawnable":true,"is_summonable":true,"is_experimental":false}`.

### Постоянные компоненты

- `minecraft:nameable` (строки 249): `{}`
- `minecraft:type_family` (строки 182,251): `{"family":["wolf","mob"]}`
- `minecraft:breathable` (строки 254): `{"total_supply":15,"suffocate_time":0}`
- `minecraft:collision_box` (строки 258): `{"width":0.6,"height":0.8}`
- `minecraft:health` (строки 187,262): `{"value":8,"max":8}`
- `minecraft:hurt_on_condition` (строки 266): `{"damage_conditions":[{"filters":{"test":"in_lava","subject":"self","operator":"==","value":true},"cause":"lava","damage_per_tick":4}]}`
- `minecraft:movement` (строки 275): `{"value":0.3}`
- `minecraft:navigation.walk` (строки 278): `{"can_path_over_water":true,"avoid_damage_blocks":true}`
- `minecraft:movement.basic` (строки 282): `{}`
- `minecraft:jump.static` (строки 284): `{}`
- `minecraft:can_climb` (строки 286): `{}`
- `minecraft:attack` (строки 200,288): `{"damage":3}`
- `minecraft:healable` (строки 291): `{"items":[{"item":"porkchop","heal_amount":3},{"item":"cooked_porkchop","heal_amount":8},{"item":"fish","heal_amount":2},{"item":"salmon","heal_amount":2},{"item":"clownfish","heal_amount":1},{"item":"pufferfish","heal_amount":1},{"item":"cooked_fish","heal_amount":5},{"item":"cooked_salmon","heal_amount":6},{"item":"beef","heal_amount":3},{"item":"cooked_beef","heal_amount":8},{"item":"chicken","heal_amount":2},{"item":"cooked_chicken","heal_amount":6},{"item":"muttonRaw","heal_amount":2},{"item":"muttonCooked","heal_amount":6},{"item":"rotten_flesh","heal_amount":4},{"item":"rabbit","heal_amount":3},{"item":"cooked_rabbit","heal_amount":5},{"item":"rabbit_stew","heal_amount":10}]}`
- `minecraft:behavior.float` (строки 367): `{"priority":0}`
- `minecraft:behavior.mount_pathing` (строки 370): `{"priority":1,"speed_multiplier":1.25,"target_dist":0,"track_target":true}`
- `minecraft:behavior.stay_while_sitting` (строки 376): `{"priority":3}`
- `minecraft:behavior.leap_at_target` (строки 379): `{"priority":4,"target_dist":0.4}`
- `minecraft:behavior.melee_attack` (строки 383): `{"priority":5,"target_dist":1.2,"track_target":true,"reach_multiplier":1.0}`
- `minecraft:behavior.random_stroll` (строки 389): `{"priority":8,"speed_multiplier":1.0}`
- `minecraft:behavior.look_at_player` (строки 393): `{"priority":6,"target_distance":6.0,"probability":0.02}`
- `minecraft:behavior.beg` (строки 398): `{"priority":9,"look_distance":8,"look_time":[2,4],"items":["bone","porkchop","cooked_porkchop","chicken","cooked_chicken","beef","cooked_beef","rotten_flesh","muttonraw","muttoncooked","rabbit","cooked_rabbit"]}`
- `minecraft:behavior.hurt_by_target` (строки 406): `{"priority":3}`
- `minecraft:physics` (строки 409): `{}`
- `minecraft:pushable` (строки 411): `{"is_pushable":true,"is_pushable_by_piston":true}`

### Группы компонентов

- `minecraft:wolf_baby` (строки 12,438,452,461,479): `{"minecraft:is_baby":{},"minecraft:scale":{"value":0.5},"minecraft:ageable":{"duration":1200,"feed_items":["chicken","cooked_chicken","beef","cooked_beef","muttonRaw","muttonCooked","porkchop","cooked_porkchop","rabbit","cooked_rabbit","rotten_flesh"],"grow_up":{"event":"minecraft:ageable_grow_up","target":"self"}}}`
- `minecraft:wolf_adult` (строки 41,427,466,474): `{"minecraft:experience_reward":{"on_bred":"Math.Random(1,7)","on_death":"query.last_hit_by_player ? Math.Random(1,3) : 0"},"minecraft:loot":{"table":"loot_tables/entities/wolf.json"},"minecraft:breedable":{"require_tame":true,"breeds_with":{"mate_type":"minecraft:wolf","baby_type":"minecraft:wolf","breed_event":{"event":"minecraft:entity_born","target":"baby"}},"breed_items":["chicken","cooked_chicken","beef","cooked_beef","muttonRaw","muttonCooked","porkchop","cooked_porkchop","rabbit","cooked_rabbit","rotten_flesh"]}}`
- `minecraft:wolf_angry` (строки 75,504,511): `{"minecraft:angry":{"duration":25,"broadcast_anger":true,"broadcast_range":20,"calm_event":{"event":"minecraft:on_calm","target":"self"}},"minecraft:on_target_acquired":{}}`
- `minecraft:wolf_wild` (строки 89,428,439,487,499,516): `{"minecraft:behavior.avoid_mob_type":{"priority":3,"entity_types":[{"filters":{"test":"is_family","subject":"other","value":"llama"},"max_dist":24,"walk_speed_multiplier":1.5,"sprint_speed_multiplier":1.5}],"probability_per_strength":0.14},"minecraft:tameable":{"probability":0.33,"tame_items":"bone","tame_event":{"event":"minecraft:on_tame","target":"self"}},"minecraft:behavior.nearest_attackable_target":{"priority":4,"attack_interval":10,"reselect_targets":true,"entity_types":[{"filters":{"any_of":[{"test":"is_family","subject":"other","value":"skeleton"},{"test":"is_family","subject":"other","value":"sheep"},{"test":"is_family","subject":"other","value":"rabbit"},{"test":"is_family","subject":"other","value":"fox"}]},"max_dist":16},{"filters":{"all_of":[{"test":"is_family","subject":"other","value":"baby_turtle"},{"test":"in_water","subject":"other","operator":"!=","value":true}]},"max_dist":16},{"filters":{"all_of":[{"test":"is_family","subject":"other","value":"skeleton"},{"test":"is_underwater","subject":"other","operator":"!=","value":true}]},"max_dist":16}],"must_see":true},"minecraft:on_target_acquired":{"event":"minecraft:become_angry","target":"self"},"minecraft:rideable":{"seat_count":1,"family_types":["zombie"],"seats":{"position":[0.0,0.675,-0.1]}}}`
- `minecraft:wolf_tame` (строки 181,453,492): `{"minecraft:type_family":{"family":["wolf","mob","tamed"]},"minecraft:is_tamed":{},"minecraft:health":{"value":20,"max":20},"minecraft:color":{"value":14},"minecraft:behavior.follow_owner":{"priority":6,"speed_multiplier":1.0,"start_distance":10,"stop_distance":2},"minecraft:attack":{"damage":4},"minecraft:behavior.breed":{"priority":7},"minecraft:behavior.owner_hurt_by_target":{"priority":1},"minecraft:behavior.owner_hurt_target":{"priority":2},"minecraft:behavior.nearest_attackable_target":{"priority":5,"attack_interval":10,"entity_types":[{"filters":{"test":"is_family","subject":"other","value":"skeleton"},"max_dist":16}],"must_see":true},"minecraft:sittable":{},"minecraft:is_dyeable":{"interact_text":"action.interact.dye"},"minecraft:leashable":{"soft_distance":4.0,"hard_distance":6.0,"max_distance":10.0,"on_leash":{"event":"minecraft:on_leash","target":"self"},"on_unleash":{"event":"minecraft:on_unleash","target":"self"}}}`

### События

**`minecraft:entity_spawned`** (строки 419):

- `$.randomize`: альтернативы, веса `[9,1]`, сумма 10:
  - ветвь 0, weight `9`; условная доля 9/10 (90%):
    - `$.randomize[0]` — поля действия: `{"remove":{},"add":{"component_groups":["minecraft:wolf_adult","minecraft:wolf_wild"]}}`
  - ветвь 1, weight `1`; условная доля 1/10 (10%):
    - `$.randomize[1]` — поля действия: `{"remove":{},"add":{"component_groups":["minecraft:wolf_baby","minecraft:wolf_wild"]}}`

**`minecraft:entity_born`** (строки 55,447):

- `$` — поля действия: `{"remove":{},"add":{"component_groups":["minecraft:wolf_baby","minecraft:wolf_tame"]}}`

**`minecraft:ageable_grow_up`** (строки 35,458):

- `$` — поля действия: `{"remove":{"component_groups":["minecraft:wolf_baby"]},"add":{"component_groups":["minecraft:wolf_adult"]}}`

**`minecraft:ageable_set_baby`** (строки 471):

- `$` — поля действия: `{"remove":{"component_groups":["minecraft:wolf_adult"]},"add":{"component_groups":["minecraft:wolf_baby"]}}`

**`minecraft:on_tame`** (строки 106,484):

- `$` — поля действия: `{"remove":{"component_groups":["minecraft:wolf_wild"]},"add":{"component_groups":["minecraft:wolf_tame"]}}`

**`minecraft:become_angry`** (строки 167,496):

- `$` — поля действия: `{"remove":{"component_groups":["minecraft:wolf_wild"]},"add":{"component_groups":["minecraft:wolf_angry"]}}`

**`minecraft:on_calm`** (строки 81,508):

- `$` — поля действия: `{"remove":{"component_groups":["minecraft:wolf_angry"]},"add":{"component_groups":["minecraft:wolf_wild"]}}`

