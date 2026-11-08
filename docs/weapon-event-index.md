# Weapon-хуки и условная модель прочности предметов 2.x

Сопоставлены все 42 ID, совпадающие между архивами 2.8.8 и 2.8.14: проверено структурное равенство `minecraft:weapon` и соответствующего event `weapon`, но **не** равенство всего поведения предмета/сущностей. `не задан` — отсутствующее поле, `{}` — явно пустой объект. [Как читать модель и её ограничения](manual-weapon-durability-model.md).

Условная модель в последнем столбце учитывает только **явные** `damage {type:durability,target:self}` внутри event, при успешном выполнении всех sequence и независимых weighted randomize с указанными весами. Доли — точные дроби по этой модели, не наблюдаемые игровые вероятности. Команды, on-use, digger, обычный износ движка, раннее разрушение и косвенные эффекты не включены; `0` **не** доказывает нулевой износ или отсутствие урона игроку.

| ID | on_hurt_entity | on_not_hurt_entity | on_hit_block | Условная сумма явных damage: доля |
|---|---|---|---|---|
| [`effect:bedrock_stick`](items-2.8.14.md#effectbedrock_stick) | не задан | не задан | не задан | пустой `minecraft:weapon` |
| [`effect:bedrock_sword`](items-2.8.14.md#effectbedrock_sword) | не задан | не задан | не задан | пустой `minecraft:weapon` |
| [`effect:bee_sword`](items-2.8.14.md#effectbee_sword) | `{"event":"weapon"}` | `{"event":"weapon"}` | `{"event":"weapon"}` | `1: 3/10, 2: 7/10` |
| [`effect:blaze_sword`](items-2.8.14.md#effectblaze_sword) | `{"event":"weapon"}` | `{"event":"weapon"}` | `{"event":"weapon"}` | `1: 3/20, 2: 17/20` |
| [`effect:bone_sword`](items-2.8.14.md#effectbone_sword) | `{"event":"weapon"}` | `{"event":"weapon"}` | `{"event":"weapon"}` | `1: 1/5, 2: 4/5` |
| [`effect:cactus_sword`](items-2.8.14.md#effectcactus_sword) | `{"event":"weapon"}` | не задан | не задан | `1: 1` |
| [`effect:clock_sword`](items-2.8.14.md#effectclock_sword) | `{"event":"weapon"}` | `{"event":"weapon"}` | `{"event":"weapon"}` | `1: 1` |
| [`effect:coal_sword`](items-2.8.14.md#effectcoal_sword) | `{"event":"weapon"}` | не задан | не задан | `1: 1` |
| [`effect:creeper_sword`](items-2.8.14.md#effectcreeper_sword) | `{"event":"weapon"}` | `{"event":"weapon"}` | `{"event":"weapon"}` | `1: 1/5, 2: 4/5` |
| [`effect:cursed_pumpkin_sword`](items-2.8.14.md#effectcursed_pumpkin_sword) | `{"event":"weapon"}` | `{"event":"weapon"}` | `{"event":"weapon"}` | `1: 1` |
| [`effect:emerald_sword`](items-2.8.14.md#effectemerald_sword) | `{"event":"weapon"}` | `{"event":"weapon"}` | `{"event":"weapon"}` | `1: 1` |
| [`effect:ender_sword`](items-2.8.14.md#effectender_sword) | `{"event":"weapon"}` | не задан | не задан | `1: 1` |
| [`effect:fire_sword`](items-2.8.14.md#effectfire_sword) | `{"event":"weapon"}` | `{"event":"weapon"}` | `{"event":"weapon"}` | `1: 1` |
| [`effect:ghost_sword`](items-2.8.14.md#effectghost_sword) | `{"event":"weapon"}` | `{"event":"weapon"}` | `{"event":"weapon"}` | `1: 1` |
| [`effect:glass_sword`](items-2.8.14.md#effectglass_sword) | `{"event":"weapon"}` | `{"event":"weapon"}` | `{"event":"weapon"}` | `10: 1` |
| [`effect:glowstone_sword`](items-2.8.14.md#effectglowstone_sword) | `{"event":"weapon"}` | не задан | не задан | `1: 1` |
| [`effect:grass_sword`](items-2.8.14.md#effectgrass_sword) | `{"event":"weapon"}` | не задан | не задан | `1: 1` |
| [`effect:ice_sword`](items-2.8.14.md#effectice_sword) | `{"event":"weapon"}` | `{"event":"weapon"}` | `{"event":"weapon"}` | `1: 1` |
| [`effect:jungle_sword`](items-2.8.14.md#effectjungle_sword) | `{"event":"weapon"}` | не задан | не задан | `1: 1` |
| [`effect:lapis_sword`](items-2.8.14.md#effectlapis_sword) | `{"event":"weapon"}` | не задан | не задан | `1: 1` |
| [`effect:lightning_sword`](items-2.8.14.md#effectlightning_sword) | `{"event":"weapon"}` | `{"event":"weapon"}` | `{"event":"weapon"}` | `1: 1` |
| [`effect:magma_sword`](items-2.8.14.md#effectmagma_sword) | `{"event":"weapon"}` | не задан | не задан | `1: 1` |
| [`effect:nether_star_sword`](items-2.8.14.md#effectnether_star_sword) | `{"event":"weapon"}` | `{"event":"weapon"}` | `{"event":"weapon"}` | `0: 1/10000, 1: 9999/10000` |
| [`effect:obsidian_sword`](items-2.8.14.md#effectobsidian_sword) | `{"event":"weapon"}` | не задан | не задан | `1: 11/20, 2: 3/10, 3: 3/20` |
| [`effect:quartz_diamond`](items-2.8.14.md#effectquartz_diamond) | не задан | не задан | не задан | нет компонента |
| [`effect:quartz_diamond_stick`](items-2.8.14.md#effectquartz_diamond_stick) | `{"event":"weapon"}` | `{"event":"weapon"}` | `{"event":"weapon"}` | `0: 1` |
| [`effect:quartz_sword`](items-2.8.14.md#effectquartz_sword) | `{"event":"weapon"}` | `{"event":"weapon"}` | `{"event":"weapon"}` | `10: 1` |
| [`effect:sea_sword`](items-2.8.14.md#effectsea_sword) | `{"event":"weapon"}` | не задан | не задан | `1: 1` |
| [`effect:shulker_sword`](items-2.8.14.md#effectshulker_sword) | `{"event":"weapon"}` | `{"event":"weapon"}` | `{"event":"weapon"}` | `1: 1` |
| [`effect:silver_ingot`](items-2.8.14.md#effectsilver_ingot) | не задан | не задан | не задан | нет компонента |
| [`effect:silver_sword`](items-2.8.14.md#effectsilver_sword) | `{"event":"weapon"}` | не задан | не задан | `1: 1` |
| [`effect:slime_sword`](items-2.8.14.md#effectslime_sword) | `{"event":"weapon"}` | не задан | не задан | `1: 1` |
| [`effect:spectral_sword`](items-2.8.14.md#effectspectral_sword) | `{"event":"weapon"}` | `{"event":"weapon"}` | `{"event":"weapon"}` | `0: 1/100, 1: 99/100` |
| [`effect:spider_sword`](items-2.8.14.md#effectspider_sword) | `{"event":"weapon"}` | `{"event":"weapon"}` | `{"event":"weapon"}` | `1: 1` |
| [`effect:sponge_sword`](items-2.8.14.md#effectsponge_sword) | `{"event":"weapon"}` | не задан | не задан | `1: 1` |
| [`effect:time_sword`](items-2.8.14.md#effecttime_sword) | `{"event":"weapon"}` | `{"event":"weapon"}` | `{"event":"weapon"}` | `1: 9/10, 16: 3/50, 32: 3/100, 64: 1/100` |
| [`effect:tnt_sword`](items-2.8.14.md#effecttnt_sword) | `{"event":"weapon"}` | `{"event":"weapon"}` | `{"event":"weapon"}` | `1: 1` |
| [`effect:ultra_instinct_sword`](items-2.8.14.md#effectultra_instinct_sword) | `{"event":"weapon"}` | не задан | не задан | `1: 1` |
| [`effect:wet_sponge_sword`](items-2.8.14.md#effectwet_sponge_sword) | `{"event":"weapon"}` | не задан | не задан | `1: 1` |
| [`effect:wither_skeleton_sword`](items-2.8.14.md#effectwither_skeleton_sword) | `{"event":"weapon"}` | не задан | не задан | `1: 1` |
| [`effect:wither_sword`](items-2.8.14.md#effectwither_sword) | `{"event":"weapon"}` | `{"event":"weapon"}` | `{"event":"weapon"}` | `1: 1` |
| [`effect:wolf_sword`](items-2.8.14.md#effectwolf_sword) | `{"event":"weapon"}` | не задан | не задан | `1: 1` |

## Полные event `weapon`

Буквальные структуры после JSON5-разбора, сохранён порядок массивов; комментарии и форматирование оригинала не воспроизводятся. Компоненты с пустым объектом и отсутствующие объекты перечислены в таблице выше; ссылки на исходные файлы — в карточках.

| ID | Значение event |
|---|---|
| `effect:bee_sword` | `{"sequence":[{"damage":{"type":"durability","amount":1,"target":"self"}},{"randomize":[{"weight":30,"shoot":{"projectile":"entity:bee_sword","launch_power":1}},{"weight":70,"damage":{"type":"durability","amount":1,"target":"self"}}]}]}` |
| `effect:blaze_sword` | `{"sequence":[{"damage":{"type":"durability","amount":1,"target":"self"}},{"randomize":[{"weight":14,"run_command":{"command":["effect @s fire_resistance 1 0 true"]},"shoot":{"projectile":"minecraft:small_fireball","launch_power":1}},{"weight":1,"run_command":{"command":["effect @s fire_resistance 1 0 true"]},"shoot":{"projectile":"minecraft:fireball","launch_power":1}},{"weight":85,"damage":{"type":"durability","amount":1,"target":"self"}}]}]}` |
| `effect:bone_sword` | `{"sequence":[{"damage":{"type":"durability","amount":1,"target":"self"}},{"randomize":[{"weight":20,"shoot":{"projectile":"minecraft:arrow","launch_power":1}},{"weight":80,"damage":{"type":"durability","amount":1,"target":"self"}}]}]}` |
| `effect:cactus_sword` | `{"sequence":[{"damage":{"type":"durability","amount":1,"target":"self"}}]}` |
| `effect:clock_sword` | `{"sequence":[{"damage":{"type":"durability","amount":1,"target":"self"}}]}` |
| `effect:coal_sword` | `{"sequence":[{"damage":{"type":"durability","amount":1,"target":"self"}}]}` |
| `effect:creeper_sword` | `{"sequence":[{"damage":{"type":"durability","amount":1,"target":"self"}},{"randomize":[{"weight":20,"shoot":{"projectile":"minecraft:creeper","launch_power":1}},{"weight":80,"damage":{"type":"durability","amount":1,"target":"self"}}]}]}` |
| `effect:cursed_pumpkin_sword` | `{"sequence":[{"damage":{"type":"durability","amount":1,"target":"self"}},{"randomize":[{"weight":80,"shoot":{"projectile":"entity:pumpkin_projectile","launch_power":1}},{"weight":20}]}]}` |
| `effect:emerald_sword` | `{"sequence":[{"damage":{"type":"durability","amount":1,"target":"self"}}]}` |
| `effect:ender_sword` | `{"sequence":[{"damage":{"type":"durability","amount":1,"target":"self"}}]}` |
| `effect:fire_sword` | `{"sequence":[{"damage":{"type":"durability","amount":1,"target":"self"}},{"randomize":[{"weight":85,"shoot":{"projectile":"entity:fire","launch_power":1}},{"weight":15,"shoot":{"projectile":"entity:living_flame","launch_power":1}}]}]}` |
| `effect:ghost_sword` | `{"sequence":[{"damage":{"type":"durability","amount":1,"target":"self"}}]}` |
| `effect:glass_sword` | `{"sequence":[{"damage":{"type":"durability","amount":10,"target":"self"},"run_command":{"command":["playsound random.glass @a[r=8,m=0]"]}}]}` |
| `effect:glowstone_sword` | `{"sequence":[{"damage":{"type":"durability","amount":1,"target":"self"}}]}` |
| `effect:grass_sword` | `{"sequence":[{"damage":{"type":"durability","amount":1,"target":"self"}}]}` |
| `effect:ice_sword` | `{"sequence":[{"damage":{"type":"durability","amount":1,"target":"self"}},{"randomize":[{"weight":70},{"weight":30,"shoot":{"projectile":"minecraft:snowball","launch_power":1},"run_command":{"command":["playsound random.bow @a[r=10] ~ ~ ~ 1 0.4"]}}]}]}` |
| `effect:jungle_sword` | `{"sequence":[{"damage":{"type":"durability","amount":1,"target":"self"}}]}` |
| `effect:lapis_sword` | `{"sequence":[{"damage":{"type":"durability","amount":1,"target":"self"}}]}` |
| `effect:lightning_sword` | `{"sequence":[{"damage":{"type":"durability","amount":1,"target":"self"}},{"randomize":[{"weight":15},{"weight":85,"shoot":{"projectile":"entity:lightning_projectile","launch_power":1}}]}]}` |
| `effect:magma_sword` | `{"sequence":[{"damage":{"type":"durability","amount":1,"target":"self"}}]}` |
| `effect:nether_star_sword` | `{"sequence":[{"shoot":{"projectile":"entity:nether_star_projectile","launch_power":1}},{"randomize":[{"weight":80,"run_command":{"command":["summon entity:nether_star ^ ^20 ^-6"]}},{"weight":20,"run_command":{"command":["summon entity:nether_star ^ ^20 ^-6","summon entity:nether_star ^ ^18 ^-6"]}}]},{"randomize":[{"weight":9999,"damage":{"type":"durability","amount":1,"target":"self"}},{"weight":1,"run_command":{"command":["summon entity:ultra_instinct_explode"]}}]}]}` |
| `effect:obsidian_sword` | `{"randomize":[{"weight":55,"damage":{"type":"durability","amount":1,"target":"self"}},{"weight":30,"damage":{"type":"durability","amount":2,"target":"self"}},{"weight":15,"damage":{"type":"durability","amount":3,"target":"self"}}]}` |
| `effect:quartz_diamond_stick` | `{"randomize":[{"weight":10,"run_command":{"command":["damage @s 1 magic"]}},{"weight":85,"run_command":{"command":["damage @s 3 magic"]}},{"weight":5,"run_command":{"command":["damage @s 6 magic"]}}]}` |
| `effect:quartz_sword` | `{"sequence":[{"damage":{"type":"durability","amount":10,"target":"self"}},{"run_command":{"command":["effect @a[r=1] instant_damage 1 99 true","particle minecraft:knockback_roar_particle ~ ~1 ~"]}}]}` |
| `effect:sea_sword` | `{"sequence":[{"damage":{"type":"durability","amount":1,"target":"self"}}]}` |
| `effect:shulker_sword` | `{"sequence":[{"damage":{"type":"durability","amount":1,"target":"self"}},{"randomize":[{"weight":10,"shoot":{"projectile":"minecraft:shulker_bullet","launch_power":1},"run_command":{"command":["playsound random.bow @a[r=10] ~ ~ ~ 1 0.4"]}},{"weight":90}]}]}` |
| `effect:silver_sword` | `{"sequence":[{"damage":{"type":"durability","amount":1,"target":"self"}}]}` |
| `effect:slime_sword` | `{"sequence":[{"damage":{"type":"durability","amount":1,"target":"self"}}]}` |
| `effect:spectral_sword` | `{"randomize":[{"weight":99,"damage":{"type":"durability","amount":1,"target":"self"}},{"weight":1,"run_command":{"command":["event entity @e[type=ender_crystal,family=!ender_crystal_default,family=!ender_crystal_scale,c=1] minecraft:crystal_explode"]}}]}` |
| `effect:spider_sword` | `{"sequence":[{"damage":{"type":"durability","amount":1,"target":"self"}},{"randomize":[{"weight":95},{"weight":5,"shoot":{"projectile":"entity:web","launch_power":1}}]}]}` |
| `effect:sponge_sword` | `{"sequence":[{"damage":{"type":"durability","amount":1,"target":"self"}}]}` |
| `effect:time_sword` | `{"randomize":[{"weight":90,"damage":{"type":"durability","amount":1,"target":"self"}},{"weight":6,"damage":{"type":"durability","amount":16,"target":"self"}},{"weight":3,"damage":{"type":"durability","amount":32,"target":"self"}},{"weight":1,"damage":{"type":"durability","amount":64,"target":"self"}}]}` |
| `effect:tnt_sword` | `{"sequence":[{"damage":{"type":"durability","amount":1,"target":"self"}},{"randomize":[{"weight":10},{"weight":90,"shoot":{"projectile":"entity:tnt","launch_power":1}}]}]}` |
| `effect:ultra_instinct_sword` | `{"sequence":[{"damage":{"type":"durability","amount":1,"target":"self"}}]}` |
| `effect:wet_sponge_sword` | `{"sequence":[{"damage":{"type":"durability","amount":1,"target":"self"}}]}` |
| `effect:wither_skeleton_sword` | `{"sequence":[{"damage":{"type":"durability","amount":1,"target":"self"},"shoot":{"projectile":"entity:wither_effect","launch_power":1}}]}` |
| `effect:wither_sword` | `{"sequence":[{"damage":{"type":"durability","amount":1,"target":"self"}},{"randomize":[{"weight":90},{"weight":10,"shoot":{"projectile":"minecraft:wither_skull","launch_power":1},"run_command":{"command":["playsound mob.wither.shoot @a[r=16]"]}}]}]}` |
| `effect:wolf_sword` | `{"sequence":[{"damage":{"type":"durability","amount":1,"target":"self"}}]}` |
