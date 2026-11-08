# Буквальные поля event в behavior-сущностях — 2.8.8 и 2.8.14

Поиск значений свойства `event`, являющихся строкой, во всём объекте `minecraft:entity`: разобранных файлов 51, вхождений 228. Это **не полный граф вызовов**: `spawn_event`, строковые команды `event entity`, анимационные контроллеры, внешние вызовы, ванильные правила и динамическое разрешение не входят в этот поиск.

Колонка локального объявления только проверяет наличие имени среди `events` **того же файла**, независимо от `target`. Она не определяет объект-адресат, фактическое исполнение или отсутствие события в игре: в частности, target `block` и `baby` не следует автоматически проверять как self. Если target не задан, его дефолт здесь не предположен. Само имя `self` не гарантирует, какой объект движок выберет в каждом контексте. Повторные ключи JSON5 сводит к последнему значению; неразобранные файлы исключены.

Вхождения по буквально записанному target: не указан — 123, `baby` — 3, `block` — 2, `self` — 100.
Из них вхождений с именем, отсутствующим в локальном `events`: не указан — 2, `block` — 2, `self` — 3. Эти числа не являются количеством ошибок.

- Неразобранные файлы: `Swords_B/entities/creeper.json` (<string>:430 Unexpected "}" at column 3).
- Повторные ключи: `Swords_B/entities/living_flame.json`: `minecraft:fire_immune`; `Swords_B/entities/mountable_slime.json`: `despawn`; `Swords_B/entities/slime_king.json`: `minecraft:movement.jump`.

Сопоставление 2.8.x: имена локальных событий и все найденные поля `event`, их пути и target совпадают. Сами тела событий и другие части сущностей полностью не сравнивались.

| Файл / ID | Значение event | target | Локально объявлено имя | Буквальные пути |
|---|---|---|---|---|
| `Swords_B/entities/alpha_wolf.json`<br>`entity:alpha_wolf` | `add_effects` | не указан | да | `$.components.minecraft:damage_sensor.triggers[1].on_damage.event` |
| `Swords_B/entities/alpha_wolf.json`<br>`entity:alpha_wolf` | `clear_effects` | не указан | да | `$.components.minecraft:damage_sensor.triggers[2].on_damage.event` |
| `Swords_B/entities/alpha_wolf.json`<br>`entity:alpha_wolf` | `minecraft:wolf_sword` | не указан | да | `$.components.minecraft:damage_sensor.triggers[0].on_damage.event` |
| `Swords_B/entities/arrow.json`<br>`minecraft:arrow` | `start_despawn_arrow` | `self` | да | `$.component_groups.despawn_arrow.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/bee.json`<br>`minecraft:bee` | `abort_sheltering` | не указан | да | `$.component_groups.abort_shelter_detection.minecraft:environment_sensor.triggers[0].event` |
| `Swords_B/entities/bee.json`<br>`minecraft:bee` | `attacked` | `self` | да | `$.components.minecraft:on_target_acquired.event` |
| `Swords_B/entities/bee.json`<br>`minecraft:bee` | `calmed_down` | `self` | да | `$.component_groups.angry_bee.minecraft:angry.calm_event.event`<br>`$.component_groups.take_nearest_target.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/bee.json`<br>`minecraft:bee` | `collected_nectar` | `self` | да | `$.component_groups.look_for_food.minecraft:behavior.move_to_block.on_stay_completed[0].event` |
| `Swords_B/entities/bee.json`<br>`minecraft:bee` | `countdown_to_perish_event` | `self` | да | `$.component_groups.angry_bee.minecraft:behavior.melee_attack.on_attack.event` |
| `Swords_B/entities/bee.json`<br>`minecraft:bee` | `find_flower_timeout` | не указан | да | `$.component_groups.look_for_food.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/bee.json`<br>`minecraft:bee` | `find_hive_event` | `self` | да | `$.component_groups.return_to_home.minecraft:behavior.go_home.on_home[1].event`<br>`$.component_groups.return_to_home.minecraft:behavior.go_home.on_failed[0].event`<br>`$.component_groups.hive_full.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/bee.json`<br>`minecraft:bee` | `find_hive_timeout` | `self` | да | `$.component_groups.find_hive.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/bee.json`<br>`minecraft:bee` | `minecraft:ageable_grow_up` | `self` | да | `$.component_groups.bee_baby.minecraft:ageable.grow_up.event` |
| `Swords_B/entities/bee.json`<br>`minecraft:bee` | `minecraft:bee_returned_to_hive` | `block` | нет | `$.component_groups.return_to_home.minecraft:behavior.go_home.on_home[0].event`<br>`$.component_groups.find_hive.minecraft:behavior.move_to_block.on_reach[0].event` |
| `Swords_B/entities/bee.json`<br>`minecraft:bee` | `minecraft:entity_born` | `baby` | да | `$.component_groups.bee_adult.minecraft:breedable.breeds_with.breed_event.event` |
| `Swords_B/entities/bee.json`<br>`minecraft:bee` | `perish_event` | `self` | да | `$.component_groups.countdown_to_perish.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/bee.json`<br>`minecraft:bee` | `seek_shelter` | не указан | да | `$.component_groups.shelter_detection.minecraft:environment_sensor.triggers[0].event` |
| `Swords_B/entities/bee.json`<br>`minecraft:bee` | `stop_panicking_after_fire` | `self` | да | `$.component_groups.escape_fire.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/bee_entity.json`<br>`entity:bee_sword` | `despawn` | `self` | да | `$.components.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/cat.json`<br>`minecraft:cat` | `minecraft:ageable_grow_up` | `self` | да | `$.component_groups.minecraft:cat_baby.minecraft:ageable.grow_up.event` |
| `Swords_B/entities/cat.json`<br>`minecraft:cat` | `minecraft:cat_gifted_owner` | `self` | да | `$.component_groups.minecraft:cat_gift_for_owner.minecraft:behavior.drop_item_for.on_drop_attempt.event` |
| `Swords_B/entities/cat.json`<br>`minecraft:cat` | `minecraft:entity_born` | `baby` | да | `$.component_groups.minecraft:cat_adult.minecraft:breedable.breeds_with.breed_event.event` |
| `Swords_B/entities/cat.json`<br>`minecraft:cat` | `minecraft:on_tame` | `self` | да | `$.component_groups.minecraft:cat_wild.minecraft:tameable.tame_event.event` |
| `Swords_B/entities/cat.json`<br>`minecraft:cat` | `minecraft:pet_slept_with_owner` | `self` | да | `$.component_groups.minecraft:cat_tame.minecraft:on_wake_with_owner.event` |
| `Swords_B/entities/centella.json`<br>`entity:centella` | `centella_death` | не указан | да | `$.components.minecraft:damage_sensor.triggers[1].on_damage.event` |
| `Swords_B/entities/centella.json`<br>`entity:centella` | `centella_death_by_player` | не указан | да | `$.components.minecraft:damage_sensor.triggers[0].on_damage.event` |
| `Swords_B/entities/centella.json`<br>`entity:centella` | `minecraft:centella` | не указан | да | `$.components.minecraft:environment_sensor[0].on_environment.event` |
| `Swords_B/entities/centella.json`<br>`entity:centella` | `minecraft:start_death` | `self` | да | `$.components.minecraft:on_death.event`<br>`$.components.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/ender_crystal.json`<br>`minecraft:ender_crystal` | `minecraft:crystal_explode` | `self` | да | `$.component_groups.on_hurt_crystal.minecraft:on_hurt.event` |
| `Swords_B/entities/ender_crystal.json`<br>`minecraft:ender_crystal` | `minecraft:end_scale` | `self` | да | `$.component_groups.ender_crystal_scale.minecraft:ageable.grow_up.event` |
| `Swords_B/entities/ender_crystal.json`<br>`minecraft:ender_crystal` | `ride_player` | не указан | да | `$.component_groups.detect_player.minecraft:environment_sensor[0].on_environment.event` |
| `Swords_B/entities/ender_crystal.json`<br>`minecraft:ender_crystal` | `spectral_crystal_explode` | `self` | да | `$.component_groups.spectral_sword_drop.minecraft:on_hurt.event` |
| `Swords_B/entities/ender_crystal_projectile.json`<br>`entity:ender_crystal_projectile` | `minecraft:crystal_explode` | `self` | да | `$.components.minecraft:projectile.on_hit.definition_event.event_trigger.event` |
| `Swords_B/entities/ender_crystal_projectile.json`<br>`entity:ender_crystal_projectile` | `projectile_particle` | не указан | да | `$.components.minecraft:environment_sensor[0].on_environment.event` |
| `Swords_B/entities/enderman.json`<br>`minecraft:enderman` | `minecraft:become_angry` | `self` | да | `$.component_groups.minecraft:enderman_calm.minecraft:on_target_acquired.event` |
| `Swords_B/entities/enderman.json`<br>`minecraft:enderman` | `minecraft:on_calm` | `self` | да | `$.component_groups.minecraft:enderman_angry.minecraft:angry.calm_event.event` |
| `Swords_B/entities/entity_nether_star.json`<br>`entity:nether_star` | `minecraft:despawn` | `self` | да | `$.components.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/entity_tnt.json`<br>`entity:tnt` | `despawn` | `self` | да | `$.components.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/entity_tnt.json`<br>`entity:tnt` | `mini_explosion` | `self` | да | `$.components.minecraft:projectile.on_hit.definition_event.event_trigger.event` |
| `Swords_B/entities/entity_tnt.json`<br>`entity:tnt` | `particle` | не указан | да | `$.components.minecraft:environment_sensor[0].on_environment.event` |
| `Swords_B/entities/fireball.json`<br>`minecraft:fireball` | `minecraft:explode` | `self` | да | `$.component_groups.gravity_enable.minecraft:projectile.on_hit.definition_event.event_trigger.event`<br>`$.components.minecraft:projectile.on_hit.definition_event.event_trigger.event` |
| `Swords_B/entities/ghast.json`<br>`minecraft:ghast` | `spectral_ghast` | не указан | да | `$.components.minecraft:damage_sensor.triggers[0].on_damage.event` |
| `Swords_B/entities/ghost.json`<br>`entity:ghost` | `despawn` | не указан | да | `$.components.minecraft:environment_sensor.triggers[0].event` |
| `Swords_B/entities/ghost.json`<br>`entity:ghost` | `disturbed_ghost` | не указан | да | `$.components.minecraft:damage_sensor.triggers[0].on_damage.event` |
| `Swords_B/entities/ghost.json`<br>`entity:ghost` | `ghost_effects` | не указан | да | `$.components.minecraft:environment_sensor.triggers[1].event` |
| `Swords_B/entities/ghost_projectile.json`<br>`entity:ghost_projectile` | `teleport_owner` | `self` | да | `$.components.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/grass.json`<br>`entity:grass` | `despawn` | `self` | да | `$.component_groups.start_despawn.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/grass.json`<br>`entity:grass` | `grass_sword_skill` | `self` | да | `$.component_groups.grass_sword.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/grows_crop.json`<br>`entity:grows_crop` | `despawn` | `self` | да | `$.components.minecraft:ageable.grow_up.event` |
| `Swords_B/entities/grows_crop.json`<br>`entity:grows_crop` | `grows_crop` | `self` | да | `$.component_groups.grows_crop_event.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/instant_giant_explode.json`<br>`entity:instant_giant_explode` | `explode_effects` | `self` | да | `$.components.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/item.json`<br>`minecraft:item` | `delete_fire_blocks` | не указан | да | `$.components.minecraft:environment_sensor[5].on_environment.event` |
| `Swords_B/entities/item.json`<br>`minecraft:item` | `fading_fire_sword` | не указан | да | `$.components.minecraft:environment_sensor[0].on_environment.event` |
| `Swords_B/entities/item.json`<br>`minecraft:item` | `fire_sword_event_1` | `self` | да | `$.component_groups.fire_sword.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/item.json`<br>`minecraft:item` | `fire_sword_event_2` | не указан | да | `$.components.minecraft:environment_sensor[1].on_environment.event` |
| `Swords_B/entities/item.json`<br>`minecraft:item` | `fountain_of_wishes_1` | не указан | да | `$.components.minecraft:environment_sensor[6].on_environment.event` |
| `Swords_B/entities/item.json`<br>`minecraft:item` | `fountain_of_wishes_2` | не указан | да | `$.components.minecraft:environment_sensor[7].on_environment.event` |
| `Swords_B/entities/item.json`<br>`minecraft:item` | `fountain_of_wishes_3` | не указан | да | `$.components.minecraft:environment_sensor[8].on_environment.event` |
| `Swords_B/entities/item.json`<br>`minecraft:item` | `sponge_sword_event` | не указан | да | `$.components.minecraft:environment_sensor[3].on_environment.event` |
| `Swords_B/entities/item.json`<br>`minecraft:item` | `stop_fire_sword` | не указан | да | `$.components.minecraft:environment_sensor[2].on_environment.event` |
| `Swords_B/entities/item.json`<br>`minecraft:item` | `stop_sponge_sword` | не указан | да | `$.components.minecraft:environment_sensor[4].on_environment.event` |
| `Swords_B/entities/item.json`<br>`minecraft:item` | `wet_sponge_sword` | `self` | да | `$.component_groups.sponge_sword.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/lightning_bolt.json`<br>`minecraft:lightning_bolt` | `spawn_centella` | `self` | да | `$.component_groups.spawn_centella.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/lightning_projectile.json`<br>`entity:lightning_projectile` | `despawn` | `self` | да | `$.components.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/lightning_projectile.json`<br>`entity:lightning_projectile` | `lightning_bolt` | `self` | да | `$.components.minecraft:projectile.on_hit.definition_event.event_trigger.event` |
| `Swords_B/entities/lightning_projectile.json`<br>`entity:lightning_projectile` | `particle` | не указан | нет | `$.components.minecraft:environment_sensor[0].on_environment.event` |
| `Swords_B/entities/living_flame.json`<br>`entity:living_flame` | `hostile_entity_detect` | `self` | да | `$.components.minecraft:ageable.grow_up.event` |
| `Swords_B/entities/living_flame.json`<br>`entity:living_flame` | `minecraft:despawn` | `self` | да | `$.component_groups.fire_sword_skill.minecraft:timer.time_down_event.event`<br>`$.component_groups.target.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/living_flame.json`<br>`entity:living_flame` | `minecraft:set_fire` | не указан | да | `$.components.minecraft:environment_sensor.triggers[0].event` |
| `Swords_B/entities/living_flame.json`<br>`entity:living_flame` | `minecraft:start_death` | не указан | да | `$.component_groups.passive_entity.minecraft:damage_sensor.triggers.on_damage.event` |
| `Swords_B/entities/living_flame.json`<br>`entity:living_flame` | `minecraft:start_death` | `self` | да | `$.component_groups.hostile_entity.minecraft:timer.time_down_event.event`<br>`$.component_groups.passive_entity.minecraft:on_death.event`<br>`$.component_groups.passive_entity.minecraft:timer.time_down_event.event`<br>`$.components.minecraft:on_death.event`<br>`$.components.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/living_flame.json`<br>`entity:living_flame` | `minecraft:stop_projectile` | `self` | да | `$.component_groups.living_flame_projectile.minecraft:projectile.on_hit.definition_event.event_trigger.event` |
| `Swords_B/entities/living_flame.json`<br>`entity:living_flame` | `start_death_hostile` | не указан | да | `$.component_groups.hostile_entity.minecraft:damage_sensor.triggers.on_damage.event` |
| `Swords_B/entities/living_flame.json`<br>`entity:living_flame` | `start_death_hostile` | `self` | да | `$.component_groups.hostile_entity.minecraft:on_death.event` |
| `Swords_B/entities/mountable_slime.json`<br>`entity:mountable_slime` | `fall_damage` | не указан | да | `$.components.minecraft:damage_sensor.triggers[0].on_damage.event` |
| `Swords_B/entities/mountable_slime.json`<br>`entity:mountable_slime` | `minecraft:is_jumping` | не указан | да | `$.component_groups.defense_mode_slime.minecraft:environment_sensor.triggers[0].event`<br>`$.components.minecraft:environment_sensor.triggers[0].event` |
| `Swords_B/entities/mountable_slime.json`<br>`entity:mountable_slime` | `slime_events` | не указан | да | `$.component_groups.defense_mode_slime.minecraft:environment_sensor.triggers[1].event` |
| `Swords_B/entities/nether_star_projectile.json`<br>`entity:nether_star_projectile` | `minecraft:despawn` | `self` | да | `$.component_groups.nether_star_sword.minecraft:timer.time_down_event.event`<br>`$.components.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/nether_star_projectile.json`<br>`entity:nether_star_projectile` | `set_objective` | `self` | да | `$.component_groups.nether_star_sword.minecraft:projectile.on_hit.definition_event.event_trigger.event` |
| `Swords_B/entities/nether_star_projectile.json`<br>`entity:nether_star_projectile` | `set_particle` | не указан | да | `$.components.minecraft:environment_sensor.triggers[0].event` |
| `Swords_B/entities/nether_star_projectile.json`<br>`entity:nether_star_projectile` | `set_sound` | `self` | да | `$.components.minecraft:projectile.on_hit.definition_event.event_trigger.event` |
| `Swords_B/entities/objective.json`<br>`entity:objective` | `follow_entity` | не указан | да | `$.components.minecraft:environment_sensor.triggers[0].event` |
| `Swords_B/entities/objective.json`<br>`entity:objective` | `minecraft:despawn` | `self` | да | `$.components.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/parrot.json`<br>`minecraft:parrot` | `minecraft:on_tame` | `self` | да | `$.component_groups.minecraft:parrot_wild.minecraft:tameable.tame_event.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `bee_sword_flower` | `self` | да | `$.component_groups.minecraft:bee_sword.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `blaze_sword_effects` | `self` | да | `$.component_groups.minecraft:blaze_sword.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `blaze_sword_skill` | `self` | да | `$.component_groups.blaze_sword_skill.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `bone_sword_skills` | `self` | да | `$.component_groups.minecraft:bone_sword.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `cactus_sword_skills` | `self` | да | `$.component_groups.minecraft:cactus_sword.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `ender_sword_skill` | не указан | да | `$.component_groups.minecraft:ender_sword.minecraft:damage_sensor.triggers[0].on_damage.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `ender_sword_sound` | `self` | да | `$.component_groups.minecraft:ender_sword.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `ender_sword_tp` | не указан | да | `$.component_groups.minecraft:ender_sword.minecraft:damage_sensor.triggers[1].on_damage.event`<br>`$.component_groups.minecraft:ender_sword.minecraft:damage_sensor.triggers[2].on_damage.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `fire_sword_sound` | `self` | да | `$.component_groups.minecraft:fire_sword.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `grass_sword_skills` | `self` | да | `$.component_groups.minecraft:grass_sword.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `lapis_sword_skills` | `self` | да | `$.component_groups.minecraft:lapis_sword.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `minecraft:bee_sword` | не указан | да | `$.components.minecraft:environment_sensor[60].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `minecraft:blaze_sword` | не указан | да | `$.components.minecraft:environment_sensor[3].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `minecraft:bone_sword` | не указан | да | `$.components.minecraft:environment_sensor[5].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `minecraft:cactus_sword` | не указан | да | `$.components.minecraft:environment_sensor[7].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `minecraft:clear_add_bad_omen` | `self` | да | `$.component_groups.minecraft:add_bad_omen.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `minecraft:clock_sword` | не указан | да | `$.components.minecraft:environment_sensor[56].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `minecraft:constant_events` | не указан | да | `$.components.minecraft:environment_sensor[1].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `minecraft:emerald_sword` | не указан | да | `$.components.minecraft:environment_sensor[9].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `minecraft:ender_sword` | не указан | да | `$.components.minecraft:environment_sensor[46].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `minecraft:fire_sword` | не указан | да | `$.components.minecraft:environment_sensor[11].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `minecraft:ghost_sword` | не указан | да | `$.components.minecraft:environment_sensor[54].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `minecraft:glowstone_sword` | не указан | да | `$.components.minecraft:environment_sensor[43].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `minecraft:grass_sword` | не указан | да | `$.components.minecraft:environment_sensor[13].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `minecraft:ice_sword` | не указан | да | `$.components.minecraft:environment_sensor[19].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `minecraft:jungle_sword` | не указан | да | `$.components.minecraft:environment_sensor[15].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `minecraft:lapis_sword` | не указан | да | `$.components.minecraft:environment_sensor[21].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `minecraft:lightning_sword` | не указан | да | `$.components.minecraft:environment_sensor[44].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `minecraft:magma_sword` | не указан | да | `$.components.minecraft:environment_sensor[17].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `minecraft:nether_star_sword` | не указан | да | `$.components.minecraft:environment_sensor[58].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `minecraft:obsidian_sword` | не указан | да | `$.components.minecraft:environment_sensor[23].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `minecraft:quartz_sword` | не указан | да | `$.components.minecraft:environment_sensor[25].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `minecraft:remove_raid_trigger` | `self` | да | `$.component_groups.minecraft:raid_trigger.minecraft:raid_trigger.triggered_event.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `minecraft:sea_sword` | не указан | да | `$.components.minecraft:environment_sensor[27].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `minecraft:shulker_sword` | не указан | да | `$.components.minecraft:environment_sensor[33].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `minecraft:slime_sword` | не указан | да | `$.components.minecraft:environment_sensor[31].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `minecraft:spectral_sword` | не указан | да | `$.components.minecraft:environment_sensor[29].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `minecraft:spider_sword` | не указан | да | `$.components.minecraft:environment_sensor[35].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `minecraft:sponge_sword` | не указан | да | `$.components.minecraft:environment_sensor[37].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `minecraft:stop_sword_events` | не указан | да | `$.components.minecraft:environment_sensor[2].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `minecraft:time_sword` | не указан | да | `$.components.minecraft:environment_sensor[39].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `minecraft:trigger_raid` | не указан | да | `$.components.minecraft:environment_sensor[0].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `minecraft:ultra_instinct_sword` | не указан | да | `$.components.minecraft:environment_sensor[48].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `minecraft:wither_sword` | не указан | да | `$.components.minecraft:environment_sensor[41].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `minecraft:wolf_sword` | не указан | да | `$.components.minecraft:environment_sensor[50].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `sea_sword_sound` | `self` | да | `$.component_groups.minecraft:sea_sword.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `slime_sword_skills` | `self` | да | `$.component_groups.minecraft:slime_sword.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `spectral_sword_skills` | `self` | да | `$.component_groups.minecraft:spectral_sword.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `start_player_explode` | `self` | да | `$.component_groups.start_player_explode_event.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `starting_wolf_transformation` | не указан | да | `$.components.minecraft:environment_sensor[52].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `stop_bee_sword_event` | не указан | да | `$.components.minecraft:environment_sensor[61].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `stop_blaze_sword_event` | не указан | да | `$.components.minecraft:environment_sensor[4].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `stop_blaze_sword_skill` | `self` | да | `$.component_groups.shoot_small_fireball.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `stop_bone_sword_event` | не указан | да | `$.components.minecraft:environment_sensor[6].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `stop_cactus_sword_event` | не указан | да | `$.components.minecraft:environment_sensor[8].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `stop_clock_sword_event` | не указан | да | `$.components.minecraft:environment_sensor[57].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `stop_clock_sword_event` | `self` | да | `$.component_groups.clock_sword_skill.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `stop_emerald_sword_event` | не указан | да | `$.components.minecraft:environment_sensor[10].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `stop_ender_sword_event` | не указан | да | `$.components.minecraft:environment_sensor[47].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `stop_fire_sword_event` | не указан | да | `$.components.minecraft:environment_sensor[12].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `stop_ghost_sword_event` | не указан | да | `$.components.minecraft:environment_sensor[55].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `stop_grass_sword_event` | не указан | да | `$.components.minecraft:environment_sensor[14].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `stop_ice_sword_event` | не указан | да | `$.components.minecraft:environment_sensor[20].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `stop_jungle_sword_event` | не указан | да | `$.components.minecraft:environment_sensor[16].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `stop_lapis_sword_event` | не указан | да | `$.components.minecraft:environment_sensor[22].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `stop_lightning_sword_event` | не указан | да | `$.components.minecraft:environment_sensor[45].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `stop_magma_sword_event` | не указан | да | `$.components.minecraft:environment_sensor[18].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `stop_nether_star_sword_event` | не указан | да | `$.components.minecraft:environment_sensor[59].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `stop_obsidian_sword_event` | не указан | да | `$.components.minecraft:environment_sensor[24].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `stop_quartz_sword_event` | не указан | да | `$.components.minecraft:environment_sensor[26].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `stop_sea_sword_event` | не указан | да | `$.components.minecraft:environment_sensor[28].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `stop_shulker_sword_event` | не указан | да | `$.components.minecraft:environment_sensor[34].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `stop_slime_sword_event` | не указан | да | `$.components.minecraft:environment_sensor[32].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `stop_spectral_sword_event` | не указан | да | `$.components.minecraft:environment_sensor[30].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `stop_spider_skill_event` | `self` | да | `$.component_groups.spider_sword_skill.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `stop_spider_sword_event` | не указан | да | `$.components.minecraft:environment_sensor[36].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `stop_sponge_sword_event` | не указан | да | `$.components.minecraft:environment_sensor[38].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `stop_time_sword_event` | не указан | да | `$.components.minecraft:environment_sensor[40].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `stop_ultra_instinct_sword_event` | не указан | да | `$.components.minecraft:environment_sensor[49].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `stop_wither_sword_event` | не указан | да | `$.components.minecraft:environment_sensor[42].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `stop_wolf_sword_event` | не указан | да | `$.components.minecraft:environment_sensor[51].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `ultra_instinct_sword_effects` | `self` | да | `$.component_groups.minecraft:ultra_instinct_sword.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `ultra_instinct_sword_skill` | не указан | да | `$.component_groups.minecraft:ultra_instinct_sword.minecraft:damage_sensor.triggers[0].on_damage.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `wither_sword_effects` | `self` | да | `$.component_groups.minecraft:wither_sword.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `wolf_damage_sound` | не указан | да | `$.component_groups.complete_wolf_transformation.minecraft:damage_sensor.triggers[0].on_damage.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `wolf_movement` | не указан | да | `$.components.minecraft:environment_sensor[53].on_environment.event` |
| `Swords_B/entities/player.json`<br>`minecraft:player` | `wolf_sword_sounds` | `self` | да | `$.component_groups.complete_wolf_transformation.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/pumpkin_projectile.json`<br>`entity:pumpkin_projectile` | `despawn` | не указан | да | `$.components.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/shulker_shield.json`<br>`entity:shulker_shield` | `damage_player` | `self` | да | `$.components.minecraft:on_death.event` |
| `Swords_B/entities/shulker_shield.json`<br>`entity:shulker_shield` | `shulker_shield_clear_effect` | не указан | да | `$.components.minecraft:environment_sensor[0].on_environment.event` |
| `Swords_B/entities/skeleton.json`<br>`minecraft:skeleton` | `bone_sword` | не указан | да | `$.component_groups.minecraft:lightning_immune.minecraft:damage_sensor.triggers[0].on_damage.event`<br>`$.components.minecraft:damage_sensor.triggers[0].on_damage.event` |
| `Swords_B/entities/skeleton.json`<br>`minecraft:skeleton` | `minecraft:melee_mode` | не указан | да | `$.component_groups.minecraft:ranged_attack.minecraft:environment_sensor.triggers.event`<br>`$.components.minecraft:environment_sensor.triggers.event` |
| `Swords_B/entities/skeleton.json`<br>`minecraft:skeleton` | `minecraft:ranged_mode` | не указан | да | `$.component_groups.minecraft:melee_attack.minecraft:environment_sensor.triggers.event` |
| `Swords_B/entities/slime_damage.json`<br>`entity:slime_damage` | `minecraft:despawn` | `self` | да | `$.components.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/slime_king.json`<br>`entity:slime_king` | `fall_damage` | не указан | да | `$.components.minecraft:damage_sensor.triggers[1].on_damage.event` |
| `Swords_B/entities/slime_king.json`<br>`entity:slime_king` | `health_bar` | не указан | да | `$.components.minecraft:damage_sensor.triggers[0].on_damage.event` |
| `Swords_B/entities/slime_king.json`<br>`entity:slime_king` | `slime_effects` | не указан | да | `$.components.minecraft:environment_sensor.triggers[0].event` |
| `Swords_B/entities/snowball.json`<br>`minecraft:snowball` | `ice_sword` | `self` | да | `$.component_groups.ice_sword.minecraft:projectile.on_hit.definition_event.event_trigger.event` |
| `Swords_B/entities/spider.json`<br>`minecraft:spider` | `minecraft:become_angry` | не указан | да | `$.component_groups.minecraft:spider_neutral.minecraft:on_target_acquired.event`<br>`$.component_groups.minecraft:spider_hostile.minecraft:on_target_acquired.event` |
| `Swords_B/entities/spider.json`<br>`minecraft:spider` | `minecraft:become_calm` | `self` | да | `$.component_groups.minecraft:spider_angry.minecraft:angry.calm_event.event` |
| `Swords_B/entities/spider.json`<br>`minecraft:spider` | `minecraft:become_hostile` | не указан | да | `$.component_groups.minecraft:spider_neutral.minecraft:environment_sensor.triggers.event` |
| `Swords_B/entities/spider.json`<br>`minecraft:spider` | `minecraft:become_neutral` | не указан | да | `$.component_groups.minecraft:spider_hostile.minecraft:environment_sensor.triggers.event` |
| `Swords_B/entities/spider.json`<br>`minecraft:spider` | `not_climb` | не указан | да | `$.component_groups.minecraft:spider_player_jockey.minecraft:environment_sensor.triggers[0].event` |
| `Swords_B/entities/tnt.json`<br>`minecraft:tnt` | `camerashake` | `self` | да | `$.component_groups.giant_tnt.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/tnt.json`<br>`minecraft:tnt` | `particle` | не указан | да | `$.component_groups.giant_tnt.minecraft:environment_sensor[0].on_environment.event` |
| `Swords_B/entities/ultra_instinct_projectile.json`<br>`entity:ultra_instinct_projectile` | `minecraft:end_scale` | `self` | нет | `$.components.minecraft:ageable.grow_up.event` |
| `Swords_B/entities/ultra_instinct_projectile.json`<br>`entity:ultra_instinct_projectile` | `minecraft:explode` | `self` | да | `$.components.minecraft:projectile.on_hit.definition_event.event_trigger.event` |
| `Swords_B/entities/ultra_instinct_projectile.json`<br>`entity:ultra_instinct_projectile` | `projectile_particle` | не указан | да | `$.components.minecraft:environment_sensor[0].on_environment.event` |
| `Swords_B/entities/web.json`<br>`entity:web` | `set_web` | `self` | да | `$.components.minecraft:projectile.on_hit.definition_event.event_trigger.event` |
| `Swords_B/entities/web.json`<br>`entity:web` | `shoot_sound` | не указан | да | `$.components.minecraft:environment_sensor[0].on_environment.event` |
| `Swords_B/entities/witch.json`<br>`minecraft:witch` | `grass_sword` | `self` | да | `$.component_groups.grass_witch.minecraft:on_death.event` |
| `Swords_B/entities/witch.json`<br>`minecraft:witch` | `grass_witch_skill` | не указан | да | `$.component_groups.grass_witch.minecraft:environment_sensor.triggers[0].event` |
| `Swords_B/entities/witch.json`<br>`minecraft:witch` | `minecraft:stop_celebrating` | `self` | да | `$.component_groups.minecraft:celebrate.minecraft:behavior.celebrate.on_celebration_end_event.event` |
| `Swords_B/entities/wither.json`<br>`minecraft:wither` | `wither_sword` | не указан | да | `$.components.minecraft:damage_sensor.triggers[1].on_damage.event` |
| `Swords_B/entities/wither_effect.json`<br>`entity:wither_effect` | `despawn` | `self` | да | `$.components.minecraft:timer.time_down_event.event` |
| `Swords_B/entities/wither_effect.json`<br>`entity:wither_effect` | `particle` | не указан | нет | `$.components.minecraft:environment_sensor[0].on_environment.event` |
| `Swords_B/entities/wither_skull.json`<br>`minecraft:wither_skull` | `minecraft:explode` | `self` | да | `$.component_groups.wither_sword.minecraft:projectile.on_hit.definition_event.event_trigger.event`<br>`$.components.minecraft:projectile.on_hit.definition_event.event_trigger.event` |
| `Swords_B/entities/wither_skull_dangerous.json`<br>`minecraft:wither_skull_dangerous` | `minecraft:explode` | `self` | да | `$.component_groups.wither_sword.minecraft:projectile.on_hit.definition_event.event_trigger.event`<br>`$.components.minecraft:projectile.on_hit.definition_event.event_trigger.event` |
| `Swords_B/entities/wolf.json`<br>`minecraft:wolf` | `minecraft:ageable_grow_up` | `self` | да | `$.component_groups.minecraft:wolf_baby.minecraft:ageable.grow_up.event` |
| `Swords_B/entities/wolf.json`<br>`minecraft:wolf` | `minecraft:become_angry` | `self` | да | `$.component_groups.minecraft:wolf_wild.minecraft:on_target_acquired.event` |
| `Swords_B/entities/wolf.json`<br>`minecraft:wolf` | `minecraft:entity_born` | `baby` | да | `$.component_groups.minecraft:wolf_adult.minecraft:breedable.breeds_with.breed_event.event` |
| `Swords_B/entities/wolf.json`<br>`minecraft:wolf` | `minecraft:on_calm` | `self` | да | `$.component_groups.minecraft:wolf_angry.minecraft:angry.calm_event.event` |
| `Swords_B/entities/wolf.json`<br>`minecraft:wolf` | `minecraft:on_leash` | `self` | нет | `$.component_groups.minecraft:wolf_tame.minecraft:leashable.on_leash.event` |
| `Swords_B/entities/wolf.json`<br>`minecraft:wolf` | `minecraft:on_tame` | `self` | да | `$.component_groups.minecraft:wolf_wild.minecraft:tameable.tame_event.event` |
| `Swords_B/entities/wolf.json`<br>`minecraft:wolf` | `minecraft:on_unleash` | `self` | нет | `$.component_groups.minecraft:wolf_tame.minecraft:leashable.on_unleash.event` |

Полные объявления и условия: [реестр сущностей 2.8.14](entity-ledger-2.8.14.md); отдельный [индекс групп](entity-groups-2.x.md).
