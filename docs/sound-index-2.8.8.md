# Звуковые команды и локальные звуки — 2.8.8

Автоматический указатель строк `playsound`/`stopsound` в JSON-значениях и в текстовых строках mcfunction/JS; приведён весь исходный командный текст и путь внутри разобранного JSON. Это не полный граф звука: `sounds.json`, animation sound_effects, ванильные события, динамические команды и другие пакеты могут вызывать звуки без этих строк. Текстовый просмотр JS/mcfunction может включать неисполняемые строки; валидность, условия события, громкость/единицы и воспроизведение не проверены.

Определение отсутствует локально ≠ ошибка: имя может быть ванильным или предоставлено другим пакетом. `stopsound` разбирается в порядке команда → цель → имя, отсутствие имени отмечено `<all>`. JSON5 пропускает повторённые ключи кроме последнего, а некорректные файлы исключены; полная диагностика ниже. Связи `sounds.json` — в [реестре ресурсов](resource-graph-2.8.8.md), медиа — в [реестре ассетов](assets-2.8.8.md).

Объявлено локальных sound ID: 3; командных строк: 107; разных пар команда/звук: 35.

## Диагностика

- Не разобраны: `Swords_B/entities/creeper.json`.
- Повторные ключи при разборе: `Swords_B/entities/living_flame.json`: `["minecraft:fire_immune"]`, `Swords_B/entities/mountable_slime.json`: `["despawn"]`, `Swords_B/entities/slime_king.json`: `["minecraft:movement.jump"]`.

## Локальные определения и файлы

### `ghost_sword.wailing`

- Исходное определение: `{"category":"neutral","min_distance":60.0,"sounds":["sounds/ghost_sword/wailing"]}`
- `Swords_R/sounds/ghost_sword/wailing.ogg` — 27.213787 с; 44100 Гц; 2 канал(ов); SHA-256 `7f2574957dfa0b3ec48295bd94073e22840ac3c7eedf6739923deccaabcc1348`.

### `wolf_sword.distant_howl`

- Исходное определение: `{"category":"neutral","min_distance":100.0,"sounds":["sounds/wolf_sword/distant_howl"]}`
- `Swords_R/sounds/wolf_sword/distant_howl.ogg` — 5.192132 с; 44100 Гц; 2 канал(ов); SHA-256 `5d6bdea2ba2183e7ab965c17d36cb66a54a93c634047ca3163cf69552e66c0e8`.

### `wolf_sword.howl`

- Исходное определение: `{"category":"neutral","min_distance":32.0,"sounds":["sounds/wolf_sword/howl"]}`
- `Swords_R/sounds/wolf_sword/howl.ogg` — 4.715079 с; 44100 Гц; 2 канал(ов); SHA-256 `db2b08a2103d38d3b32feebe187c7c38b153b46e9e44ac147936fc6941c76020`.

## Все обнаруженные строки команд

### `playsound bubble.up`

Локальное sound definition: не найдено; упоминаний: 1.

- `Swords_B/entities/player.json` · `$.minecraft:entity.events.minecraft:magma_sword.sequence[2].randomize[1].run_command.command[0]` · `playsound bubble.up @a ~ ~ ~ 1 0.9`

### `playsound dig.grass`

Локальное sound definition: не найдено; упоминаний: 4.

- `Swords_B/blocks/sapling3.json` · `$.minecraft:block.events.on_placed.sequence[0].run_command.command[0]` · `playsound dig.grass @a[r=12] ~ ~ ~`
- `Swords_B/entities/grass.json` · `$.minecraft:entity.events.minecraft:entity_spawned.sequence[0].run_command.command[0]` · `playsound dig.grass @a[r=12]`
- `Swords_B/entities/grass.json` · `$.minecraft:entity.events.grass_sword_skill.run_command.command[0]` · `playsound dig.grass @a[r=12] ~ ~ ~ 1 0.4`
- `Swords_B/entities/witch.json` · `$.minecraft:entity.events.grass_sword.randomize[1].run_command.command[2]` · `playsound dig.grass @a[r=12] ~~~`

### `playsound fire.fire`

Локальное sound definition: не найдено; упоминаний: 1.

- `Swords_B/entities/player.json` · `$.minecraft:entity.events.fire_sword_sound.run_command.command[0]` · `playsound fire.fire @a[r=8]`

### `playsound ghost_sword.wailing`

Локальное sound definition: да; упоминаний: 2.

- `Swords_B/entities/ghost.json` · `$.minecraft:entity.events.ghost_wailing.randomize[1].randomize[0].run_command.command[0]` · `playsound ghost_sword.wailing @a[rm=10,r=50]`
- `Swords_B/entities/ghost.json` · `$.minecraft:entity.events.ghost_wailing.randomize[1].randomize[1].run_command.command[0]` · `playsound ghost_sword.wailing @a[rm=10,r=50] ~~~ 1 7`

### `playsound item.trident.thunder`

Локальное sound definition: не найдено; упоминаний: 3.

- `Swords_B/entities/nether_star_projectile.json` · `$.minecraft:entity.events.set_sound.randomize[0].run_command.command[0]` · `playsound item.trident.thunder @a[r=20] ~ ~ ~ 1 5.5`
- `Swords_B/entities/nether_star_projectile.json` · `$.minecraft:entity.events.set_sound.randomize[1].run_command.command[0]` · `playsound item.trident.thunder @a[r=20] ~ ~ ~ 1 6`
- `Swords_B/entities/nether_star_projectile.json` · `$.minecraft:entity.events.set_sound.randomize[2].run_command.command[0]` · `playsound item.trident.thunder @a[r=20] ~ ~ ~ 1 7`

### `playsound mob.blaze.breathe`

Локальное sound definition: не найдено; упоминаний: 2.

- `Swords_B/entities/player.json` · `$.minecraft:entity.events.minecraft:blaze_sword.sequence[2].randomize[5].run_command.command[0]` · `playsound mob.blaze.breathe @a[r=12] ~ ~ ~ 0.5`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.blaze_sword_effects.randomize[5].run_command.command[0]` · `playsound mob.blaze.breathe @a[r=12] ~ ~ ~ 0.5`

### `playsound mob.endermen.death`

Локальное sound definition: не найдено; упоминаний: 1.

- `Swords_B/entities/item.json` · `$.minecraft:entity.events.despawn_event_1.run_command.command[1]` · `playsound mob.endermen.death @a[r=16] ~ ~ ~ 1 0.5`

### `playsound mob.endermen.hit`

Локальное sound definition: не найдено; упоминаний: 1.

- `Swords_B/entities/player.json` · `$.minecraft:entity.events.ender_sword_skill.sequence[0].run_command.command[0]` · `playsound mob.endermen.hit @a[r=8] ~ ~ ~`

### `playsound mob.endermen.idle`

Локальное sound definition: не найдено; упоминаний: 1.

- `Swords_B/entities/player.json` · `$.minecraft:entity.events.ender_sword_sound.randomize[1].run_command.command[0]` · `playsound mob.endermen.idle @a[r=8] ~ ~ ~`

### `playsound mob.endermen.portal`

Локальное sound definition: не найдено; упоминаний: 6.

- `Swords_B/entities/ghost.json` · `$.minecraft:entity.events.disturbed_ghost.randomize[1].run_command.command[0]` · `playsound mob.endermen.portal @a[r=17] ~~~`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.ultra_instinct_sword_skill.run_command.command[1]` · `playsound mob.endermen.portal @a[r=17] ~ ~ ~ 1 0.6`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.minecraft:ender_sword.sequence[0].run_command.command[0]` · `playsound mob.endermen.portal @a[r=8] ~ ~ ~`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.ender_sword_tp.run_command.command[1]` · `playsound mob.endermen.portal @a[r=17]`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.ender_sword_skill.sequence[1].randomize[1].run_command.command[1]` · `playsound mob.endermen.portal @a[r=17]`
- `Swords_B/items/ender_sword.json` · `$.minecraft:item.events.on_use.run_command.command[1]` · `playsound mob.endermen.portal @a[r=34]`

### `playsound mob.endermen.scream`

Локальное sound definition: не найдено; упоминаний: 1.

- `Swords_B/entities/player.json` · `$.minecraft:entity.events.ender_sword_sound.randomize[0].run_command.command[0]` · `playsound mob.endermen.scream @a[r=8] ~ ~ ~`

### `playsound mob.endermen.stare`

Локальное sound definition: не найдено; упоминаний: 1.

- `Swords_B/entities/player.json` · `$.minecraft:entity.events.ender_sword_sound.randomize[2].run_command.command[0]` · `playsound mob.endermen.stare @a[r=8] ~ ~ ~`

### `playsound mob.fish.flop`

Локальное sound definition: не найдено; упоминаний: 1.

- `Swords_B/entities/player.json` · `$.minecraft:entity.events.sea_sword_sound.sequence[0].run_command.command[0]` · `playsound mob.fish.flop @a[r=12] ~ ~ ~ 1 0.6`

### `playsound mob.ghast.fireball`

Локальное sound definition: не найдено; упоминаний: 4.

- `Swords_B/entities/fake_fireball.json` · `$.minecraft:entity.events.set_sound.run_command.command[0]` · `playsound mob.ghast.fireball @a[r=16] ~ ~ ~`
- `Swords_B/entities/fireball.json` · `$.minecraft:entity.events.minecraft:entity_spawned.sequence[0].run_command.command[0]` · `playsound mob.ghast.fireball @a[r=12] ~ ~ ~`
- `Swords_B/entities/small_fireball.json` · `$.minecraft:entity.events.minecraft:entity_spawned.sequence[0].run_command.command[0]` · `playsound mob.ghast.fireball @a[r=12] ~ ~ ~`
- `Swords_B/entities/small_fireball.json` · `$.minecraft:entity.events.minecraft:entity_spawned.sequence[2].run_command.command[0]` · `playsound mob.ghast.fireball @a[r=18] ~ ~ ~`

### `playsound mob.wither.ambient`

Локальное sound definition: не найдено; упоминаний: 10.

- `Swords_B/entities/ghost.json` · `$.minecraft:entity.events.disturbed_ghost.randomize[2].run_command.command[2]` · `playsound mob.wither.ambient @a[r=16] ~ ~1 ~ 2 0.3`
- `Swords_B/entities/ghost.json` · `$.minecraft:entity.events.despawn.run_command.command[1]` · `playsound mob.wither.ambient @a[r=16] ~ ~1 ~ 2 0.3`
- `Swords_B/entities/item.json` · `$.minecraft:entity.events.wish_1.randomize[1].run_command.command[4]` · `playsound mob.wither.ambient @a[r=16] ~ ~1 ~ 2 0.6`
- `Swords_B/entities/item.json` · `$.minecraft:entity.events.wish_2.randomize[1].run_command.command[4]` · `playsound mob.wither.ambient @a[r=16] ~ ~1 ~ 2 0.6`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.minecraft:ghost_sword.sequence[0].run_command.command[6]` · `playsound mob.wither.ambient @a[r=16] ~ ~1 ~ 2 0.3`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.stop_ghost_sword_event.sequence[0].run_command.command[2]` · `playsound mob.wither.ambient @a[r=16] ~ ~1 ~ 2 0.2`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.minecraft:ultra_instinct_sword.sequence[0].run_command.command[2]` · `playsound mob.wither.ambient @a[r=16] ~ ~1 ~ 2 0.6`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.stop_ultra_instinct_sword_event.sequence[0].run_command.command[2]` · `playsound mob.wither.ambient @a[r=16] ~ ~1 ~ 2 0.6`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.shoot_ultra_instinct_projectile.run_command.command[0]` · `playsound mob.wither.ambient @s ~ ~1 ~ 2 0.6`
- `Swords_B/items/ultra_instinct_sword.json` · `$.minecraft:item.events.on_use.run_command.command[0]` · `playsound mob.wither.ambient @s ~ ~1 ~ 2 0.6`

### `playsound mob.wither.death`

Локальное sound definition: не найдено; упоминаний: 2.

- `Swords_B/entities/item.json` · `$.minecraft:entity.events.despawn_event_2.run_command.command[1]` · `playsound mob.wither.death @a[r=16] ~ ~ ~ 1 0.5`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.wither_sword_effects.randomize[0].run_command.command[0]` · `playsound mob.wither.death @a[r=16]`

### `playsound mob.wither.hurt`

Локальное sound definition: не найдено; упоминаний: 1.

- `Swords_B/entities/player.json` · `$.minecraft:entity.events.wither_sword_effects.randomize[1].run_command.command[0]` · `playsound mob.wither.hurt @a[r=16]`

### `playsound mob.wither.shoot`

Локальное sound definition: не найдено; упоминаний: 2.

- `Swords_B/items/wither_sword.json` · `$.minecraft:item.events.on_use.run_command.command[0]` · `playsound mob.wither.shoot @a[r=16] ~~~ 1 0.7`
- `Swords_B/items/wither_sword.json` · `$.minecraft:item.events.weapon.sequence[1].randomize[1].run_command.command[0]` · `playsound mob.wither.shoot @a[r=16]`

### `playsound mob.wither.spawn`

Локальное sound definition: не найдено; упоминаний: 20.

- `Swords_B/entities/centella.json` · `$.minecraft:entity.events.minecraft:centella.sequence[0].run_command.command[3]` · `playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3`
- `Swords_B/entities/ghost.json` · `$.minecraft:entity.events.ghost_effects.randomize[1].run_command.command[0]` · `playsound mob.wither.spawn @a[r=16] ~ ~ ~ 0.15 0.2`
- `Swords_B/entities/item.json` · `$.minecraft:entity.events.fire_sword_event_3.sequence[0].run_command.command[14]` · `playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 2`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.minecraft:ghost_sword.sequence[5].randomize[1].run_command.command[0]` · `playsound mob.wither.spawn @a[r=16] ~ ~ ~ 0.15 0.2`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.ultra_instinct_sword_effects.randomize[0].run_command.command[1]` · `playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.ultra_instinct_sword_effects.randomize[1].run_command.command[1]` · `playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.ultra_instinct_sword_effects.randomize[2].run_command.command[1]` · `playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.ultra_instinct_sword_effects.randomize[3].run_command.command[1]` · `playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.ultra_instinct_sword_effects.randomize[4].run_command.command[1]` · `playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.ultra_instinct_sword_effects.randomize[5].run_command.command[1]` · `playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.ultra_instinct_sword_effects.randomize[6].run_command.command[1]` · `playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.ultra_instinct_sword_effects.randomize[7].run_command.command[1]` · `playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.ultra_instinct_sword_effects.randomize[8].run_command.command[1]` · `playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.ultra_instinct_sword_effects.randomize[9].run_command.command[1]` · `playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.ultra_instinct_sword_effects.randomize[10].run_command.command[1]` · `playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.ultra_instinct_sword_effects.randomize[11].run_command.command[1]` · `playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.ultra_instinct_sword_effects.randomize[12].run_command.command[1]` · `playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.ultra_instinct_sword_effects.randomize[13].run_command.command[1]` · `playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.ultra_instinct_sword_effects.randomize[14].run_command.command[1]` · `playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.minecraft:wither_sword.sequence[0].run_command.command[0]` · `playsound mob.wither.spawn @a[r=16]`

### `playsound mob.wolf.bark`

Локальное sound definition: не найдено; упоминаний: 1.

- `Swords_B/entities/player.json` · `$.minecraft:entity.events.wolf_damage_sound.run_command.command[0]` · `playsound mob.wolf.bark @a[r=16] ~ ~ ~ 1 0.55`

### `playsound mob.wolf.growl`

Локальное sound definition: не найдено; упоминаний: 1.

- `Swords_B/entities/player.json` · `$.minecraft:entity.events.wolf_sword_sounds.randomize[0].run_command.command[0]` · `playsound mob.wolf.growl @a[r=16] ~ ~ ~ 1 0.9 24`

### `playsound portal.travel`

Локальное sound definition: не найдено; упоминаний: 4.

- `Swords_B/entities/ender_crystal.json` · `$.minecraft:entity.events.minecraft:end_scale.run_command.command[0]` · `playsound portal.travel @a[r=16] ~ ~ ~ 0.6 7`
- `Swords_B/entities/ender_crystal.json` · `$.minecraft:entity.events.minecraft:despawn.sequence[0].run_command.command[0]` · `playsound portal.travel @a[r=12] ~ ~ ~ 0.5 8`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.spectral_sword_skills.sequence[1].run_command.command[0]` · `playsound portal.travel @a[r=16] ~ ~ ~ 1 7`
- `Swords_B/items/spectral_sword.json` · `$.minecraft:item.events.on_use.run_command.command[0]` · `playsound portal.travel @a[r=16] ~ ~ ~ 1 5`

### `playsound random.bow`

Локальное sound definition: не найдено; упоминаний: 3.

- `Swords_B/entities/web.json` · `$.minecraft:entity.events.shoot_sound.run_command.command[0]` · `playsound random.bow @a[r=12] ~ ~ ~ 1 0.33`
- `Swords_B/items/ice_sword.json` · `$.minecraft:item.events.weapon.sequence[1].randomize[1].run_command.command[0]` · `playsound random.bow @a[r=10] ~ ~ ~ 1 0.4`
- `Swords_B/items/shulker_sword.json` · `$.minecraft:item.events.weapon.sequence[1].randomize[0].run_command.command[0]` · `playsound random.bow @a[r=10] ~ ~ ~ 1 0.4`

### `playsound random.explode`

Локальное sound definition: не найдено; упоминаний: 2.

- `Swords_B/entities/instant_giant_explode.json` · `$.minecraft:entity.events.explode_effects.run_command.command[1]` · `playsound random.explode @a[r=32] ~ ~ ~ 2 0.4 2`
- `Swords_B/entities/tnt.json` · `$.minecraft:entity.events.camerashake.run_command.command[1]` · `playsound random.explode @a[r=32] ~ ~ ~ 2 0.4 2`

### `playsound random.fizz`

Локальное sound definition: не найдено; упоминаний: 16.

- `Swords_B/entities/item.json` · `$.minecraft:entity.events.sponge_sword_event.sequence[1].run_command.command[1]` · `playsound random.fizz @a[r=12] ~~~ 0.5`
- `Swords_B/entities/item.json` · `$.minecraft:entity.events.despawn_event_4.sequence[0].run_command.command[3]` · `playsound random.fizz @a[r=12] ~ ~ ~ 0.6`
- `Swords_B/entities/item.json` · `$.minecraft:entity.events.despawn_event_4.sequence[1].run_command.command[0]` · `playsound random.fizz @a[r=12] ~ ~ ~ 0.6`
- `Swords_B/entities/item.json` · `$.minecraft:entity.events.fading_fire_sword.sequence[1].run_command.command[0]` · `playsound random.fizz @a[r=12] ~ ~ ~ 0.6`
- `Swords_B/entities/item.json` · `$.minecraft:entity.events.fire_sword_event_1.run_command.command[1]` · `playsound random.fizz @a[r=12] ~ ~ ~`
- `Swords_B/entities/item.json` · `$.minecraft:entity.events.fire_sword_event_2.run_command.command[0]` · `playsound random.fizz @a[r=12] ~ ~ ~ 0.6`
- `Swords_B/entities/living_flame.json` · `$.minecraft:entity.events.minecraft:start_death.run_command.command[2]` · `playsound random.fizz @a[r=12] ~ ~ ~`
- `Swords_B/entities/living_flame.json` · `$.minecraft:entity.events.start_death_hostile.sequence[0].run_command.command[2]` · `playsound random.fizz @a[r=12] ~ ~ ~`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.wolf_transformation.sequence[0].run_command.command[0]` · `playsound random.fizz @a[r=16] ~~~`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.minecraft:sponge_sword.sequence[1].run_command.command[1]` · `playsound random.fizz @a[r=12] ~~~ 0.6`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.minecraft:ice_sword.sequence[1].run_command.command[0]` · `playsound random.fizz @a[r=10] ~ ~ ~`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.minecraft:ice_sword.sequence[2].run_command.command[0]` · `playsound random.fizz @a[r=10] ~ ~ ~`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.minecraft:blaze_sword.sequence[0].run_command.command[12]` · `playsound random.fizz @a[r=16]`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.stop_blaze_sword_event.sequence[0].run_command.command[12]` · `playsound random.fizz @a[r=16]`
- `Swords_B/entities/spider.json` · `$.minecraft:entity.events.minecraft:despawn.sequence[0].run_command.command[1]` · `playsound random.fizz @a[r=16]`
- `Swords_B/items/ice_sword.json` · `$.minecraft:item.events.on_use.sequence[0].run_command.command[41]` · `playsound random.fizz @a[r=12] ~ ~ ~ 1 2.3`

### `playsound random.fuse`

Локальное sound definition: не найдено; упоминаний: 2.

- `Swords_B/entities/player.json` · `$.minecraft:entity.events.start_player_explode_event.run_command.command[1]` · `playsound random.fuse`
- `Swords_B/items/tnt_sword.json` · `$.minecraft:item.events.on_use.run_command.command[2]` · `playsound random.fuse @a ~~~`

### `playsound random.glass`

Локальное sound definition: не найдено; упоминаний: 1.

- `Swords_B/items/glass_sword.json` · `$.minecraft:item.events.weapon.sequence[0].run_command.command[0]` · `playsound random.glass @a[r=8,m=0]`

### `playsound random.levelup`

Локальное sound definition: не найдено; упоминаний: 1.

- `Swords_B/entities/item.json` · `$.minecraft:entity.events.wish_3.randomize[1].run_command.command[4]` · `playsound random.levelup @a[r=16] ~ ~ ~ 1 0.5`

### `playsound random.orb`

Локальное sound definition: не найдено; упоминаний: 3.

- `Swords_B/entities/item.json` · `$.minecraft:entity.events.wish_3.randomize[0].run_command.command[2]` · `playsound random.orb @a[r=16] ~ ~ ~ 1 0.5`
- `Swords_B/entities/mountable_slime.json` · `$.minecraft:entity.events.despawn.run_command.command[7]` · `playsound random.orb @a[r=12] ~ ~ ~ 1 0.6`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.lapis_sword_skills.run_command.command[1]` · `playsound random.orb @s ~ ~ ~ 0.3`

### `playsound random.splash`

Локальное sound definition: не найдено; упоминаний: 2.

- `Swords_B/entities/player.json` · `$.minecraft:entity.events.minecraft:sea_sword.sequence[1].run_command.command[1]` · `playsound random.splash @a[r=12] ~ ~ ~ 0.5`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.stop_sea_sword_event.sequence[0].run_command.command[1]` · `playsound random.splash @a[r=12] ~ ~ ~ 0.5`

### `playsound wolf_sword.distant_howl`

Локальное sound definition: да; упоминаний: 2.

- `Swords_B/entities/alpha_wolf.json` · `$.minecraft:entity.events.minecraft:entity_spawned.run_command.command[0]` · `playsound wolf_sword.distant_howl @a[rm=25,r=100]`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.wolf_transformation.sequence[0].run_command.command[2]` · `playsound wolf_sword.distant_howl @a[rm=25,r=100]`

### `playsound wolf_sword.howl`

Локальное sound definition: да; упоминаний: 1.

- `Swords_B/entities/player.json` · `$.minecraft:entity.events.wolf_transformation.sequence[0].run_command.command[1]` · `playsound wolf_sword.howl @a[r=24] ~~~`

### `stopsound mob.wither.spawn`

Локальное sound definition: не найдено; упоминаний: 1.

- `Swords_B/entities/player.json` · `$.minecraft:entity.events.stop_ghost_sword_event.sequence[0].run_command.command[1]` · `stopsound @a[r=18] mob.wither.spawn`

### `stopsound wolf_sword.distant_howl`

Локальное sound definition: да; упоминаний: 2.

- `Swords_B/entities/alpha_wolf.json` · `$.minecraft:entity.events.despawn.run_command.command[0]` · `stopsound @a wolf_sword.distant_howl`
- `Swords_B/entities/player.json` · `$.minecraft:entity.events.stop_wolf_transformation.sequence[0].run_command.command[3]` · `stopsound @a wolf_sword.distant_howl`

### `stopsound wolf_sword.howl`

Локальное sound definition: да; упоминаний: 1.

- `Swords_B/entities/player.json` · `$.minecraft:entity.events.stop_wolf_transformation.sequence[0].run_command.command[2]` · `stopsound @a wolf_sword.howl`
