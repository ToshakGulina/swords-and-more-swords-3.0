# Добавление и удаление групп игрока — 2.8.14

Автоматический индекс для `Swords_B/entities/player.json`: все упоминания `add.component_groups` и `remove.component_groups` внутри событий этого файла, включая вложенные sequence/randomize. Ссылки — пути внутри разобранного объекта `minecraft:entity`; индекс показывает объявления, не вызовы и не последовательность исполнения.

«Нет» значит только, что такой операции не найдено среди событий данного файла: другие события, команды, внешние пакеты, дефолты и правила разрешения наложенных компонентов могут влиять на результат. Не следует считать отсутствие remove доказательством постоянно действующего эффекта. Фильтры на ветвях и в вызывающих сенсорах смотреть в [реестре сущностей](entity-ledger-2.8.14.md), [ручных цепочках 2.x](manual-traces-2.8.14.md) и [Clock/Time](manual-time-interactions-2.8.md).

Объявлено групп: 49. У групп с add без локального remove: 10. Ссылки на группы, не объявленные в player: 0.

| Группа | Есть определение | Добавление | Удаление |
|---|---|---|---|
| `blaze_sword_skill` | да | `$.events.blaze_sword_skill_event.add.component_groups` | нет |
| `clock_sword_movement` | да | `$.events.minecraft:clock_sword.sequence[1].add.component_groups`<br>`$.events.clock_sword_movement.add.component_groups` | нет |
| `clock_sword_skill` | да | `$.events.clock_sword_skill_event.add.component_groups` | нет |
| `complete_wolf_transformation` | да | `$.events.wolf_transformation.sequence[0].add.component_groups` | `$.events.stop_wolf_sword_event.sequence[1].remove.component_groups`<br>`$.events.stop_wolf_transformation.sequence[1].remove.component_groups` |
| `despawn` | да | `$.events.despawn.add.component_groups` | нет |
| `ghost_movement` | да | `$.events.minecraft:ghost_sword.sequence[1].add.component_groups` | нет |
| `mermaid_movement_in_water` | да | `$.events.minecraft:sea_sword.sequence[2].add.component_groups` | `$.events.stop_sea_sword_event.sequence[0].remove.component_groups` |
| `mermaid_movement_out_water` | да | `$.events.minecraft:sea_sword.sequence[0].add.component_groups` | нет |
| `minecraft:add_bad_omen` | да | `$.events.minecraft:gain_bad_omen.add.component_groups` | `$.events.minecraft:clear_add_bad_omen.remove.component_groups` |
| `minecraft:bee_sword` | да | `$.events.minecraft:bee_sword.sequence[0].add.component_groups` | `$.events.stop_bee_sword_event.sequence[0].remove.component_groups` |
| `minecraft:blaze_sword` | да | `$.events.minecraft:blaze_sword.sequence[0].add.component_groups`<br>`$.events.stop_blaze_sword_skill.sequence[0].add.component_groups` | `$.events.stop_blaze_sword_event.sequence[0].remove.component_groups` |
| `minecraft:bone_sword` | да | `$.events.minecraft:bone_sword.sequence[0].add.component_groups` | `$.events.stop_bone_sword_event.sequence[0].remove.component_groups` |
| `minecraft:cactus_sword` | да | `$.events.minecraft:cactus_sword.sequence[0].add.component_groups` | `$.events.stop_cactus_sword_event.sequence[0].remove.component_groups` |
| `minecraft:clear_bad_omen_spell_effect` | да | `$.events.minecraft:clear_add_bad_omen.add.component_groups` | нет |
| `minecraft:clock_sword` | да | `$.events.minecraft:clock_sword.sequence[0].add.component_groups` | `$.events.stop_clock_sword_event.sequence[0].remove.component_groups` |
| `minecraft:default_player` | да | `$.events.stop_bee_sword_event.sequence[0].add.component_groups`<br>`$.events.default_player.add.component_groups`<br>`$.events.stop_nether_star_sword_event.sequence[0].add.component_groups`<br>`$.events.stop_clock_sword_event.sequence[0].add.component_groups`<br>`$.events.stop_ghost_sword_event.sequence[0].add.component_groups`<br>`$.events.stop_wolf_sword_event.sequence[0].add.component_groups`<br>`$.events.stop_wolf_sword_event.sequence[1].add.component_groups`<br>`$.events.stop_ultra_instinct_sword_event.sequence[0].add.component_groups`<br>`$.events.stop_ender_sword_event.sequence[0].add.component_groups`<br>`$.events.stop_lightning_sword_event.sequence[0].add.component_groups`<br>`$.events.stop_wither_sword_event.sequence[0].add.component_groups`<br>`$.events.stop_time_sword_event.sequence[0].add.component_groups`<br>`$.events.stop_sponge_sword_event.sequence[0].add.component_groups`<br>`$.events.stop_spider_sword_event.sequence[0].add.component_groups`<br>`$.events.stop_shulker_sword_event.sequence[0].add.component_groups`<br>`$.events.stop_slime_sword_event.sequence[0].add.component_groups`<br>`$.events.stop_spectral_sword_event.sequence[0].add.component_groups`<br>`$.events.stop_sea_sword_event.sequence[0].add.component_groups`<br>`$.events.stop_quartz_sword_event.sequence[0].add.component_groups`<br>`$.events.stop_obsidian_sword_event.sequence[0].add.component_groups`<br>`$.events.stop_lapis_sword_event.sequence[0].add.component_groups`<br>`$.events.stop_ice_sword_event.sequence[0].add.component_groups`<br>`$.events.stop_magma_sword_event.sequence[0].add.component_groups`<br>`$.events.stop_jungle_sword_event.sequence[0].add.component_groups`<br>`$.events.stop_grass_sword_event.sequence[0].add.component_groups`<br>`$.events.stop_fire_sword_event.sequence[0].add.component_groups`<br>`$.events.stop_emerald_sword_event.sequence[0].add.component_groups`<br>`$.events.start_player_explode.add.component_groups`<br>`$.events.stop_cactus_sword_event.sequence[0].add.component_groups`<br>`$.events.stop_bone_sword_event.sequence[0].add.component_groups`<br>`$.events.stop_blaze_sword_event.sequence[0].add.component_groups` | нет |
| `minecraft:emerald_sword` | да | `$.events.minecraft:emerald_sword.sequence[0].add.component_groups` | `$.events.stop_emerald_sword_event.sequence[0].remove.component_groups` |
| `minecraft:ender_sword` | да | `$.events.minecraft:ender_sword.sequence[0].add.component_groups` | `$.events.stop_ender_sword_event.sequence[0].remove.component_groups` |
| `minecraft:fire_sword` | да | `$.events.minecraft:fire_sword.sequence[0].add.component_groups` | `$.events.stop_fire_sword_event.sequence[0].remove.component_groups` |
| `minecraft:ghost_sword` | да | `$.events.minecraft:ghost_sword.sequence[0].add.component_groups` | `$.events.stop_ghost_sword_event.sequence[0].remove.component_groups` |
| `minecraft:grass_sword` | да | `$.events.minecraft:grass_sword.sequence[0].add.component_groups` | `$.events.stop_grass_sword_event.sequence[0].remove.component_groups` |
| `minecraft:ice_sword` | да | `$.events.minecraft:ice_sword.sequence[0].add.component_groups` | `$.events.stop_ice_sword_event.sequence[0].remove.component_groups` |
| `minecraft:jungle_sword` | да | `$.events.minecraft:jungle_sword.sequence[0].add.component_groups` | `$.events.stop_jungle_sword_event.sequence[0].remove.component_groups` |
| `minecraft:lapis_sword` | да | `$.events.minecraft:lapis_sword.sequence[0].add.component_groups` | `$.events.stop_lapis_sword_event.sequence[0].remove.component_groups` |
| `minecraft:lightning_sword` | да | `$.events.minecraft:lightning_sword.sequence[0].add.component_groups` | `$.events.stop_lightning_sword_event.sequence[0].remove.component_groups` |
| `minecraft:magma_sword` | да | `$.events.minecraft:magma_sword.sequence[0].add.component_groups` | `$.events.stop_magma_sword_event.sequence[0].remove.component_groups` |
| `minecraft:nether_star_sword` | да | `$.events.minecraft:nether_star_sword.sequence[0].add.component_groups` | `$.events.stop_nether_star_sword_event.sequence[0].remove.component_groups` |
| `minecraft:obsidian_sword` | да | `$.events.minecraft:obsidian_sword.sequence[0].add.component_groups` | `$.events.stop_obsidian_sword_event.sequence[0].remove.component_groups` |
| `minecraft:quartz_sword` | да | `$.events.minecraft:quartz_sword.sequence[0].add.component_groups` | `$.events.stop_quartz_sword_event.sequence[0].remove.component_groups` |
| `minecraft:raid_trigger` | да | `$.events.minecraft:trigger_raid.add.component_groups` | `$.events.minecraft:remove_raid_trigger.remove.component_groups` |
| `minecraft:sea_sword` | да | `$.events.minecraft:sea_sword.sequence[1].add.component_groups` | `$.events.stop_sea_sword_event.sequence[0].remove.component_groups` |
| `minecraft:shulker_sword` | да | `$.events.minecraft:shulker_sword.sequence[0].add.component_groups` | `$.events.stop_shulker_sword_event.sequence[0].remove.component_groups` |
| `minecraft:slime_sword` | да | `$.events.minecraft:slime_sword.sequence[0].add.component_groups` | `$.events.stop_slime_sword_event.sequence[0].remove.component_groups` |
| `minecraft:spectral_sword` | да | `$.events.minecraft:spectral_sword.sequence[0].add.component_groups`<br>`$.events.spectral_sword_reload_skill.sequence[0].add.component_groups` | `$.events.stop_spectral_sword_event.sequence[0].remove.component_groups` |
| `minecraft:spider_sword` | да | `$.events.minecraft:spider_sword.sequence[0].add.component_groups`<br>`$.events.stop_spider_skill_event.sequence[0].add.component_groups` | `$.events.stop_spider_sword_event.sequence[0].remove.component_groups` |
| `minecraft:sponge_sword` | да | `$.events.minecraft:sponge_sword.sequence[0].add.component_groups` | `$.events.stop_sponge_sword_event.sequence[0].remove.component_groups` |
| `minecraft:time_sword` | да | `$.events.minecraft:time_sword.sequence[0].add.component_groups` | `$.events.stop_time_sword_event.sequence[0].remove.component_groups` |
| `minecraft:ultra_instinct_sword` | да | `$.events.minecraft:ultra_instinct_sword.sequence[0].add.component_groups` | `$.events.stop_ultra_instinct_sword_event.sequence[0].remove.component_groups` |
| `minecraft:wither_sword` | да | `$.events.minecraft:wither_sword.sequence[0].add.component_groups` | `$.events.stop_wither_sword_event.sequence[0].remove.component_groups` |
| `minecraft:wolf_sword` | да | `$.events.minecraft:wolf_sword.sequence[0].add.component_groups`<br>`$.events.stop_wolf_transformation.sequence[1].add.component_groups` | `$.events.stop_wolf_sword_event.sequence[0].remove.component_groups` |
| `shoot_small_fireball` | да | `$.events.blaze_sword_skill.add.component_groups` | `$.events.stop_blaze_sword_event.sequence[0].remove.component_groups`<br>`$.events.stop_blaze_sword_skill.sequence[0].remove.component_groups` |
| `shulker_sword_skill` | да | `$.events.shulker_sword_skill.add.component_groups` | нет |
| `spider_sword_skill` | да | `$.events.spider_sword_skill.sequence[0].add.component_groups` | `$.events.stop_spider_sword_event.sequence[0].remove.component_groups`<br>`$.events.stop_spider_skill_event.sequence[0].remove.component_groups` |
| `start_player_explode_event` | да | `$.events.start_player_explode_event.add.component_groups` | `$.events.start_player_explode.remove.component_groups` |
| `time_sword_movement` | да | `$.events.time_sword_movement.add.component_groups` | нет |
| `ultra_instinct_projectile` | да | `$.events.shoot_ultra_instinct_projectile.add.component_groups` | `$.events.shoot_ultra_instinct_projectile.remove.component_groups` |
| `ultra_instinct_sword_movement` | да | `$.events.minecraft:ultra_instinct_sword.sequence[1].add.component_groups` | `$.events.stop_ultra_instinct_sword_event.sequence[0].remove.component_groups` |
| `wolf_movement` | да | `$.events.wolf_movement.add.component_groups` | `$.events.stop_wolf_sword_event.sequence[0].remove.component_groups`<br>`$.events.stop_wolf_transformation.sequence[1].remove.component_groups` |
| `wolf_transformation` | да | `$.events.wolf_sword_start_events.sequence[0].add.component_groups` | `$.events.stop_wolf_sword_event.sequence[0].remove.component_groups`<br>`$.events.wolf_transformation.sequence[1].remove.component_groups`<br>`$.events.stop_wolf_transformation.sequence[1].remove.component_groups` |
