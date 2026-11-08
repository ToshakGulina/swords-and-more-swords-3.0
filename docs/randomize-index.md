# Где в исходниках используется randomize

Автоматический указатель по разобранным JSON behavior pack. Порядок и вес каждой ветви, сумма только явно заданных целых неотрицательных весов и названия полей ветки приведены без вывода о фактическом исполнении. Сумма и отношение weight/сумма — только сырой относительный вес; фильтры, внешние события, выбор сущностей, вложенные randomize и их порядок могут изменить результат. Соседние поля не считаются последовательностью. Подробности — в исходном архиве и ручных карточках.

Это НЕ реестр всех источников случайности: loot `random_chance_with_looting`, веса пулов, timers, spawn weights, JS `Math.random`, команды и дефолты движка рассматриваются отдельно. Не разбирающиеся файлы и повторные ключи требуют чтения оригинала: JSON5 сохраняет последний ключ. В неразобранном creeper 2.x отдельно присутствует ветвь 95/5, см. [диагностическую трассу](manual-creeper-sword.md).

## Диагностика разбора

- 1.6: 0 списков; не разобраны `Sword_B/entities/blaze2.json`, `Sword_B/entities/bone2.json`, `Sword_B/entities/shulker2.json`; повторные ключи нет.
- 2.8.8: 60 списков; не разобраны `Swords_B/entities/creeper.json`; повторные ключи `Swords_B/entities/living_flame.json` (["minecraft:fire_immune"]), `Swords_B/entities/mountable_slime.json` (["despawn"]), `Swords_B/entities/slime_king.json` (["minecraft:movement.jump"]).
- 2.8.14: 60 списков; не разобраны `Swords_B/entities/creeper.json`; повторные ключи `Swords_B/entities/living_flame.json` (["minecraft:fire_immune"]), `Swords_B/entities/mountable_slime.json` (["despawn"]), `Swords_B/entities/slime_king.json` (["minecraft:movement.jump"]).

Сопоставление 2.8.x: все распознанные пути и сами массивы ветвей равны структурно; окружающий код и фактические триггеры отдельно не сравниваются.

## 1.6

Найдено списков: 0.

| Исходный файл | Путь к `randomize` | Веса → сумма | Поля веток в исходном порядке |
|---|---|---|---|

## 2.8.8 и 2.8.14

Найдено списков: 60.

| Исходный файл | Путь к `randomize` | Веса → сумма | Поля веток в исходном порядке |
|---|---|---|---|
| `Swords_B/entities/alpha_wolf.json` | `$.minecraft:entity.events.minecraft:wolf_sword.sequence[0].randomize` | `[90,10]` → 100 | `пусто`; `run_command` |
| `Swords_B/entities/bee.json` | `$.minecraft:entity.events.countdown_to_perish_event.sequence[0].randomize` | `[2,98]` → 100 | `run_command; filters={"test":"is_family","subject":"self","operator":"!=","value":"bee_sword"}`; `пусто` |
| `Swords_B/entities/bee.json` | `$.minecraft:entity.events.minecraft:entity_spawned.sequence[0].randomize` | `[95,5]` → 100 | `add`; `add` |
| `Swords_B/entities/blaze.json` | `$.minecraft:entity.events.blaze_sword.randomize` | `[995,5]` → 1000 | `пусто`; `run_command` |
| `Swords_B/entities/cat.json` | `$.minecraft:entity.events.minecraft:entity_spawned.sequence[0].randomize` | `[3,1]` → 4 | `remove+add`; `remove+add` |
| `Swords_B/entities/cat.json` | `$.minecraft:entity.events.minecraft:entity_spawned.sequence[1].randomize` | `[15,15,15,15,15,15,15,15,15,15,15]` → 165 | `add`; `add`; `add`; `add`; `add`; `add`; `add`; `add`; `add`; `add`; `add` |
| `Swords_B/entities/cat.json` | `$.minecraft:entity.events.minecraft:spawn_from_village.sequence[0].randomize` | `[3,1]` → 4 | `remove+add`; `remove+add` |
| `Swords_B/entities/cat.json` | `$.minecraft:entity.events.minecraft:spawn_from_village.sequence[1].randomize` | `[15,15,15,15,15,15,15,15,15,15]` → 150 | `add`; `add`; `add`; `add`; `add`; `add`; `add`; `add`; `add`; `add` |
| `Swords_B/entities/centella.json` | `$.minecraft:entity.events.centella_death_by_player.sequence[1].randomize` | `[98,2]` → 100 | `пусто`; `run_command` |
| `Swords_B/entities/ender_crystal.json` | `$.minecraft:entity.events.spectral_crystal_explode.sequence[0].randomize` | `[98,2]` → 100 | `пусто`; `run_command` |
| `Swords_B/entities/enderman.json` | `$.minecraft:entity.events.minecraft:entity_spawned.randomize` | `[80,20]` → 100 | `add`; `add; filters={"test":"has_biome_tag","operator":"==","value":"overworld"}` |
| `Swords_B/entities/ghast.json` | `$.minecraft:entity.events.spectral_ghast.randomize` | `[94,6]` → 100 | `пусто`; `run_command` |
| `Swords_B/entities/ghost.json` | `$.minecraft:entity.events.disturbed_ghost.randomize` | `[987,10,3]` → 1000 | `пусто`; `run_command`; `add+run_command` |
| `Swords_B/entities/ghost.json` | `$.minecraft:entity.events.ghost_effects.randomize` | `[90,10]` → 100 | `пусто`; `run_command` |
| `Swords_B/entities/ghost.json` | `$.minecraft:entity.events.ghost_wailing.randomize` | `[70,30]` → 100 | `пусто`; `randomize` |
| `Swords_B/entities/ghost.json` | `$.minecraft:entity.events.ghost_wailing.randomize[1].randomize` | `[50,50]` → 100 | `run_command`; `run_command` |
| `Swords_B/entities/grass.json` | `$.minecraft:entity.events.despawn.sequence[1].randomize` | `[50,50]` → 100 | `run_command`; `пусто` |
| `Swords_B/entities/item.json` | `$.minecraft:entity.events.wish_1.randomize` | `[992,8]` → 1000 | `run_command`; `run_command` |
| `Swords_B/entities/item.json` | `$.minecraft:entity.events.wish_2.randomize` | `[975,25]` → 1000 | `run_command`; `run_command` |
| `Swords_B/entities/item.json` | `$.minecraft:entity.events.wish_3.randomize` | `[975,25]` → 1000 | `run_command`; `run_command` |
| `Swords_B/entities/lightning_bolt.json` | `$.minecraft:entity.events.spawn_centella.randomize` | `[80,20]` → 100 | `пусто`; `run_command` |
| `Swords_B/entities/living_flame.json` | `$.minecraft:entity.events.start_death_hostile.sequence[1].randomize` | `[85,15]` → 100 | `пусто`; `run_command` |
| `Swords_B/entities/nether_star_projectile.json` | `$.minecraft:entity.events.set_sound.randomize` | `[1,1,1]` → 3 | `run_command`; `run_command`; `run_command` |
| `Swords_B/entities/parrot.json` | `$.minecraft:entity.events.minecraft:entity_spawned.randomize` | `[20,20,20,20,20]` → 100 | `add`; `add`; `add`; `add`; `add` |
| `Swords_B/entities/player.json` | `$.minecraft:entity.events.bee_sword_flower.randomize` | `[1,1,1,1,1,1,1,1,1,1,1,1]` → 12 | `run_command`; `run_command`; `run_command`; `run_command`; `run_command`; `run_command`; `run_command`; `run_command`; `run_command`; `run_command`; `run_command`; `run_command` |
| `Swords_B/entities/player.json` | `$.minecraft:entity.events.blaze_sword_effects.randomize` | `[1,1,1,1,1,1]` → 6 | `run_command`; `run_command`; `run_command`; `run_command`; `run_command`; `run_command` |
| `Swords_B/entities/player.json` | `$.minecraft:entity.events.ender_sword_skill.sequence[1].randomize` | `[50,50]` → 100 | `пусто`; `run_command` |
| `Swords_B/entities/player.json` | `$.minecraft:entity.events.ender_sword_sound.randomize` | `[1,1,1]` → 3 | `run_command`; `run_command`; `run_command` |
| `Swords_B/entities/player.json` | `$.minecraft:entity.events.minecraft:blaze_sword.sequence[2].randomize` | `[5,5,5,5,5,5,95]` → 125 | `run_command`; `run_command`; `run_command`; `run_command`; `run_command`; `run_command`; `пусто` |
| `Swords_B/entities/player.json` | `$.minecraft:entity.events.minecraft:ghost_sword.sequence[5].randomize` | `[90,10]` → 100 | `пусто`; `run_command` |
| `Swords_B/entities/player.json` | `$.minecraft:entity.events.minecraft:magma_sword.sequence[2].randomize` | `[99,1]` → 100 | `пусто`; `run_command` |
| `Swords_B/entities/player.json` | `$.minecraft:entity.events.ultra_instinct_sword_effects.randomize` | `[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]` → 15 | `run_command`; `run_command`; `run_command`; `run_command`; `run_command`; `run_command`; `run_command`; `run_command`; `run_command`; `run_command`; `run_command`; `run_command`; `run_command`; `run_command`; `run_command` |
| `Swords_B/entities/player.json` | `$.minecraft:entity.events.wither_sword_effects.randomize` | `[50,50]` → 100 | `run_command`; `run_command` |
| `Swords_B/entities/player.json` | `$.minecraft:entity.events.wolf_sword_sounds.randomize` | `[1]` → 1 | `run_command` |
| `Swords_B/entities/skeleton.json` | `$.minecraft:entity.events.bone_sword.sequence[0].randomize` | `[993,7]` → 1000 | `пусто`; `run_command` |
| `Swords_B/entities/slime_king.json` | `$.minecraft:entity.events.health_bar.sequence[1].randomize` | `[95,5]` → 100 | `пусто`; `run_command` |
| `Swords_B/entities/spider.json` | `$.minecraft:entity.events.minecraft:entity_spawned.sequence[1].randomize` | `[1,99]` → 100 | `randomize`; `remove+add` |
| `Swords_B/entities/spider.json` | `$.minecraft:entity.events.minecraft:entity_spawned.sequence[1].randomize[0].randomize` | `[80,80,20]` → 180 | `remove+add; filters={"all_of":[{"test":"is_daytime","value":false},{"test":"is_snow_covered","value":true},{"test":"is_underground","value":false}]}`; `remove+add; filters={"test":"is_biome","value":"the_nether"}`; `remove+add; filters={"any_of":[{"test":"is_daytime","value":false},{"test":"is_underground","value":true}]}` |
| `Swords_B/entities/witch.json` | `$.minecraft:entity.events.grass_sword.randomize` | `[80,20]` → 100 | `пусто`; `run_command` |
| `Swords_B/entities/witch.json` | `$.minecraft:entity.events.minecraft:entity_spawned.randomize` | `[80,20]` → 100 | `add`; `add` |
| `Swords_B/entities/wither.json` | `$.minecraft:entity.events.wither_sword.sequence[0].randomize` | `[87,13]` → 100 | `пусто`; `run_command` |
| `Swords_B/entities/wolf.json` | `$.minecraft:entity.events.minecraft:entity_spawned.randomize` | `[9,1]` → 10 | `remove+add`; `remove+add` |
| `Swords_B/items/bee_sword.json` | `$.minecraft:item.events.weapon.sequence[1].randomize` | `[30,70]` → 100 | `shoot`; `damage` |
| `Swords_B/items/blaze_sword.json` | `$.minecraft:item.events.weapon.sequence[1].randomize` | `[14,1,85]` → 100 | `run_command+shoot`; `run_command+shoot`; `damage` |
| `Swords_B/items/bone_sword.json` | `$.minecraft:item.events.weapon.sequence[1].randomize` | `[20,80]` → 100 | `shoot`; `damage` |
| `Swords_B/items/creeper_sword.json` | `$.minecraft:item.events.weapon.sequence[1].randomize` | `[20,80]` → 100 | `shoot`; `damage` |
| `Swords_B/items/fire_sword.json` | `$.minecraft:item.events.weapon.sequence[1].randomize` | `[85,15]` → 100 | `shoot`; `shoot` |
| `Swords_B/items/ice_sword.json` | `$.minecraft:item.events.weapon.sequence[1].randomize` | `[70,30]` → 100 | `пусто`; `shoot+run_command` |
| `Swords_B/items/lightning_sword.json` | `$.minecraft:item.events.weapon.sequence[1].randomize` | `[15,85]` → 100 | `пусто`; `shoot` |
| `Swords_B/items/nether_star_sword.json` | `$.minecraft:item.events.weapon.sequence[1].randomize` | `[80,20]` → 100 | `run_command`; `run_command` |
| `Swords_B/items/nether_star_sword.json` | `$.minecraft:item.events.weapon.sequence[2].randomize` | `[9999,1]` → 10000 | `damage`; `run_command` |
| `Swords_B/items/obsidian_sword.json` | `$.minecraft:item.events.weapon.randomize` | `[55,30,15]` → 100 | `damage`; `damage`; `damage` |
| `Swords_B/items/pumpkin_sword.json` | `$.minecraft:item.events.weapon.sequence[1].randomize` | `[80,20]` → 100 | `shoot`; `пусто` |
| `Swords_B/items/quartz_diamond_stick.json` | `$.minecraft:item.events.weapon.randomize` | `[10,85,5]` → 100 | `run_command`; `run_command`; `run_command` |
| `Swords_B/items/shulker_sword.json` | `$.minecraft:item.events.weapon.sequence[1].randomize` | `[10,90]` → 100 | `shoot+run_command`; `пусто` |
| `Swords_B/items/spectral_sword.json` | `$.minecraft:item.events.weapon.randomize` | `[99,1]` → 100 | `damage`; `run_command` |
| `Swords_B/items/spider_sword.json` | `$.minecraft:item.events.weapon.sequence[1].randomize` | `[95,5]` → 100 | `пусто`; `shoot` |
| `Swords_B/items/time_sword.json` | `$.minecraft:item.events.weapon.randomize` | `[90,6,3,1]` → 100 | `damage`; `damage`; `damage`; `damage` |
| `Swords_B/items/tnt_sword.json` | `$.minecraft:item.events.weapon.sequence[1].randomize` | `[10,90]` → 100 | `пусто`; `shoot` |
| `Swords_B/items/wither_sword.json` | `$.minecraft:item.events.weapon.sequence[1].randomize` | `[90,10]` → 100 | `пусто`; `shoot+run_command` |

