# Ice Sword 2.x: 40 последовательных fill on-use

Списки из `Swords_B/items/ice_sword.json`, `events.on_use.sequence[0].run_command` с `target:holder`; команды перечислены в исходном порядке. В 2.8.8 вместо `frosted_ice` употреблено `effect99:fake_ice` во всех 40 позициях; исходные файлы побайтово совпадают после этой буквальной замены в памяти. Объём — включительный геометрический размер рамки, **не** число фактически изменённых блоков. Контекст старого execute, selectors, доступность блоков/чанков, состояния и приоритет изменений не проверены. Селекторы могут пересекаться. Нельзя считать `rm`/`r` доказанной геометрией в игре без эксперимента. [Ручное пояснение](manual-ice-geometry-2.8.md).

| № | Селектор | Execute-смещение | Fill от → до | Позиции рамки | Материал и фильтр |
|---:|---|---|---|---:|---|
| 1 | `@e[type=!enderman,type=!horse,type=!slime,type=!silverfish,type=!spider,type=!cave_spider,type=!tnt,type=!vex,type=!chicken,type=!pig,type=!wolf,type=!cat,type=!item,type=!xp_orb,type=!xp_bottle,type=!egg,type=!snowball,type=!fireball,type=!small_fireball,type=!eye_of_ender_signal,type=!ender_pearl,type=!fishing_hook,type=!falling_block,type=!lightning_bolt,type=!lingering_potion,type=!dragon_fireball,type=!ender_dragon,type=!endermite,type=!arrow,type=!thrown_trident,type=!leash_knot,type=!bat,type=!rabbit,type=!parrot,type=!ghast,type=!shulker,type=!elder_guardian,type=!guardian,type=!turtle,type=!fox,type=!squid,type=!ocelot,type=!phantom,type=!area_effect_cloud,family=!fish,family=!effect99_entities,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~2 ~-1` | 36 | `frosted_ice 0 replace air 0` |
| 2 | `@e[type=enderman,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~3 ~-1` | 45 | `frosted_ice 0 replace air 0` |
| 3 | `@e[family=slime_large,rm=2,r=12]` | `~ ~ ~` | `~2 ~-1 ~2` → `~-2 ~3 ~-2` | 125 | `frosted_ice 0 replace air 0` |
| 4 | `@e[family=slime_large,rm=2,r=12]` | `~ ~1 ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `air 0 replace frosted_ice` |
| 5 | `@e[family=slime_medium,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `frosted_ice 0 replace air 0` |
| 6 | `@e[family=slime_medium,rm=2,r=12]` | `~ ~ ~` | `~ ~ ~` → `~ ~ ~` | 1 | `air 0 replace frosted_ice` |
| 7 | `@e[family=slime_small,rm=2,r=12]` | `~ ~ ~` | `~1 ~1 ~1` → `~-1 ~-1 ~-1` | 27 | `frosted_ice 0 replace air 0` |
| 8 | `@e[family=slime_small,rm=2,r=12]` | `~ ~ ~` | `~ ~ ~` → `~ ~ ~` | 1 | `air 0 replace frosted_ice` |
| 9 | `@e[type=silverfish,rm=2,r=12]` | `~ ~ ~` | `~ ~ ~` → `~ ~ ~` | 1 | `frosted_ice 0 replace air 0` |
| 10 | `@e[type=spider,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `frosted_ice 0 replace air 0` |
| 11 | `@e[type=cave_spider,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `frosted_ice 0 replace air 0` |
| 12 | `@e[type=tnt,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `frosted_ice 0 replace air 0` |
| 13 | `@e[type=vex,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `frosted_ice 0 replace air 0` |
| 14 | `@e[type=chicken,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `frosted_ice 0 replace air 0` |
| 15 | `@e[type=pig,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `frosted_ice 0 replace air 0` |
| 16 | `@e[type=wolf,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `frosted_ice 0 replace air 0` |
| 17 | `@e[type=cat,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `frosted_ice 0 replace air 0` |
| 18 | `@e[type=small_fireball,rm=2,r=12]` | `~ ~ ~` | `~ ~ ~` → `~ ~ ~` | 1 | `frosted_ice 0 replace air 0` |
| 19 | `@e[type=fireball,rm=2,r=12]` | `~ ~ ~` | `~ ~ ~` → `~ ~ ~` | 1 | `frosted_ice 0 replace air 0` |
| 20 | `@e[type=arrow,rm=2,r=12]` | `~ ~ ~` | `~ ~ ~` → `~ ~ ~` | 1 | `frosted_ice 0 replace air 0` |
| 21 | `@e[type=lingering_potion,rm=2,r=12]` | `~ ~ ~` | `~ ~ ~` → `~ ~ ~` | 1 | `frosted_ice 0 replace air 0` |
| 22 | `@e[type=dragon_fireball,rm=2,r=12]` | `~ ~ ~` | `~ ~ ~` → `~ ~ ~` | 1 | `frosted_ice 0 replace air 0` |
| 23 | `@e[type=thrown_trident,rm=2,r=12]` | `~ ~ ~` | `~ ~ ~` → `~ ~ ~` | 1 | `frosted_ice 0 replace air 0` |
| 24 | `@e[type=endermite,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `frosted_ice 0 replace air 0` |
| 25 | `@e[type=rabbit,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `frosted_ice 0 replace air 0` |
| 26 | `@e[type=parrot,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `frosted_ice 0 replace air 0` |
| 27 | `@e[type=phantom,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `frosted_ice 0 replace air 0` |
| 28 | `@e[type=shulker,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `frosted_ice 0 replace air 0` |
| 29 | `@e[type=guardian,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `frosted_ice 0 replace air 0` |
| 30 | `@e[type=ocelot,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `frosted_ice 0 replace air 0` |
| 31 | `@e[type=turtle,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `frosted_ice 0 replace air 0` |
| 32 | `@e[type=fox,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `frosted_ice 0 replace air 0` |
| 33 | `@e[type=squid,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `frosted_ice 0 replace air 0` |
| 34 | `@e[type=elder_guardian,rm=2,r=12]` | `~ ~ ~` | `~2 ~-1 ~2` → `~-2 ~3 ~-2` | 125 | `frosted_ice 0 replace air 0` |
| 35 | `@e[type=bat,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `frosted_ice 0 replace air 0` |
| 36 | `@e[type=ghast,rm=2,r=12]` | `~ ~ ~` | `~4 ~-3 ~4` → `~-4 ~4 ~-4` | 648 | `frosted_ice 0 replace air 0` |
| 37 | `@e[type=ghast,rm=2,r=12]` | `~ ~ ~` | `~3 ~-2 ~3` → `~-3 ~3 ~-3` | 294 | `air 0 replace frosted_ice` |
| 38 | `@e[type=horse,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `frosted_ice 0 replace air 0` |
| 39 | `@e[type=horse,rm=2,r=12]` | `~ ~ ~` | `~ ~ ~` → `~ ~ ~` | 1 | `air 0 replace frosted_ice 0` |
| 40 | `@e[type=player,rm=3,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~2 ~-1` | 36 | `frosted_ice 0 replace air 0` |

После этих команд в той же последовательности:

- `title @s actionbar §l§bIce Skill`
- `playsound random.fizz @a[r=12] ~ ~ ~ 1 2.3`
- `particle minecraft:knockback_roar_particle ~ ~1 ~`

Далее отдельным шагом sequence задан `damage` durability `6`, target `self`. Порядок команд и успешность не доказывают итоговый расход или выбор целей.
