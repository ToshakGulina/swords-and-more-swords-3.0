# Lightning Sword: цели 1.6 и координаты 2.x

Автоматическая выписка из `Sword_B/animation_controllers/lightning sword.json` и `Swords_B/items/lightning_sword.json`. Обе 2.x версии имеют одинаковый item JSON. Список — статические команды, не оценка успешных призывов, поражённых целей или порядка исполнения; контекст относительных координат и обработка устаревшего синтаксиса нуждаются в проверке. [Ручной разбор](manual-lightning-1.6.md).

## 1.6 — 26 type

В состояниях `default` и `lightning` одинаковые 27 строк `on_entry`: сначала 26 команд ниже, затем `/scoreboard players set @a swords 2`. В каждой команде указан `r=16,rm=10` относительно текущего контекста helper; `execute` позиционируется у каждой выбранной сущности. Номера соответствуют исходному порядку.

| № | Тип | Исходная команда |
|---:|---|---|
| 1 | `zombie` | `/execute @e[type=zombie,r=16,rm=10] ~ ~ ~ summon lightning_bolt` |
| 2 | `husk` | `/execute @e[type=husk,r=16,rm=10] ~ ~ ~ summon lightning_bolt` |
| 3 | `drowned` | `/execute @e[type=drowned,r=16,rm=10] ~ ~ ~ summon lightning_bolt` |
| 4 | `creeper` | `/execute @e[type=creeper,r=16,rm=10] ~ ~ ~ summon lightning_bolt` |
| 5 | `enderman` | `/execute @e[type=enderman,r=16,rm=10] ~ ~ ~ summon lightning_bolt` |
| 6 | `slime` | `/execute @e[type=slime,r=16,rm=10] ~ ~ ~ summon lightning_bolt` |
| 7 | `skeleton` | `/execute @e[type=skeleton,r=16,rm=10] ~ ~ ~ summon lightning_bolt` |
| 8 | `stray` | `/execute @e[type=stray,r=16,rm=10] ~ ~ ~ summon lightning_bolt` |
| 9 | `blaze` | `/execute @e[type=blaze,r=16,rm=10] ~ ~ ~ summon lightning_bolt` |
| 10 | `wither_skeleton` | `/execute @e[type=wither_skeleton,r=16,rm=10] ~ ~ ~ summon lightning_bolt` |
| 11 | `witch` | `/execute @e[type=witch,r=16,rm=10] ~ ~ ~ summon lightning_bolt` |
| 12 | `magma_cube` | `/execute @e[type=magma_cube,r=16,rm=10] ~ ~ ~ summon lightning_bolt` |
| 13 | `ghast` | `/execute @e[type=ghast,r=16,rm=10] ~ ~ ~ summon lightning_bolt` |
| 14 | `zombie_pigman` | `/execute @e[type=zombie_pigman,r=16,rm=10] ~ ~ ~ summon lightning_bolt` |
| 15 | `spider` | `/execute @e[type=spider,r=16,rm=10] ~ ~ ~ summon lightning_bolt` |
| 16 | `cave_spider` | `/execute @e[type=cave_spider,r=16,rm=10] ~ ~ ~ summon lightning_bolt` |
| 17 | `silverfish` | `/execute @e[type=silverfish,r=16,rm=10] ~ ~ ~ summon lightning_bolt` |
| 18 | `evocation_fang` | `/execute @e[type=evocation_fang,r=16,rm=10] ~ ~ ~ summon lightning_bolt` |
| 19 | `evocation_illager` | `/execute @e[type=evocation_illager,r=16,rm=10] ~ ~ ~ summon lightning_bolt` |
| 20 | `vex` | `/execute @e[type=vex,r=16,rm=10] ~ ~ ~ summon lightning_bolt` |
| 21 | `ravager` | `/execute @e[type=ravager,r=16,rm=10] ~ ~ ~ summon lightning_bolt` |
| 22 | `endermite` | `/execute @e[type=endermite,r=16,rm=10] ~ ~ ~ summon lightning_bolt` |
| 23 | `guardian` | `/execute @e[type=guardian,r=16,rm=10] ~ ~ ~ summon lightning_bolt` |
| 24 | `vindicator` | `/execute @e[type=vindicator,r=16,rm=10] ~ ~ ~ summon lightning_bolt` |
| 25 | `phantom` | `/execute @e[type=phantom,r=16,rm=10] ~ ~ ~ summon lightning_bolt` |
| 26 | `zombie_villager` | `/execute @e[type=zombie_villager,r=16,rm=10] ~ ~ ~ summon lightning_bolt` |

## 2.x — 41 относительная координата

Координаты приведены относительно контекста команды `run_command`; квадрат горизонтального расстояния вычислен как x²+z², для человека показан его корень. Это геометрия **точек призыва**, а не радиус урона или гарантированный охват. Для первой точки y=+2, остальные y=0.

| № | x | y | z | x²+z² | Горизонтальное расстояние ≈ | Исходная команда |
|---:|---:|---:|---:|---:|---:|---|
| 1 | 0 | 2 | 0 | 0 | 0.000 | `summon lightning_bolt ~ ~2 ~ default_lightning_bolt` |
| 2 | 7 | 0 | 0 | 49 | 7.000 | `summon lightning_bolt ~7 ~ ~ default_lightning_bolt` |
| 3 | 0 | 0 | 7 | 49 | 7.000 | `summon lightning_bolt ~ ~ ~7 default_lightning_bolt` |
| 4 | -7 | 0 | 0 | 49 | 7.000 | `summon lightning_bolt ~-7 ~ ~ default_lightning_bolt` |
| 5 | 0 | 0 | -7 | 49 | 7.000 | `summon lightning_bolt ~ ~ ~-7 default_lightning_bolt` |
| 6 | 6 | 0 | 6 | 72 | 8.485 | `summon lightning_bolt ~6 ~ ~6 default_lightning_bolt` |
| 7 | -6 | 0 | -6 | 72 | 8.485 | `summon lightning_bolt ~-6 ~ ~-6 default_lightning_bolt` |
| 8 | -6 | 0 | 6 | 72 | 8.485 | `summon lightning_bolt ~-6 ~ ~6 default_lightning_bolt` |
| 9 | 6 | 0 | -6 | 72 | 8.485 | `summon lightning_bolt ~6 ~ ~-6 default_lightning_bolt` |
| 10 | 14 | 0 | 0 | 196 | 14.000 | `summon lightning_bolt ~14 ~ ~ default_lightning_bolt` |
| 11 | 0 | 0 | 14 | 196 | 14.000 | `summon lightning_bolt ~ ~ ~14 default_lightning_bolt` |
| 12 | -14 | 0 | 0 | 196 | 14.000 | `summon lightning_bolt ~-14 ~ ~ default_lightning_bolt` |
| 13 | 0 | 0 | -14 | 196 | 14.000 | `summon lightning_bolt ~ ~ ~-14 default_lightning_bolt` |
| 14 | 12 | 0 | 12 | 288 | 16.971 | `summon lightning_bolt ~12 ~ ~12 default_lightning_bolt` |
| 15 | -12 | 0 | -12 | 288 | 16.971 | `summon lightning_bolt ~-12 ~ ~-12 default_lightning_bolt` |
| 16 | -12 | 0 | 12 | 288 | 16.971 | `summon lightning_bolt ~-12 ~ ~12 default_lightning_bolt` |
| 17 | 12 | 0 | -12 | 288 | 16.971 | `summon lightning_bolt ~12 ~ ~-12 default_lightning_bolt` |
| 18 | 28 | 0 | 0 | 784 | 28.000 | `summon lightning_bolt ~28 ~ ~ default_lightning_bolt` |
| 19 | 0 | 0 | 28 | 784 | 28.000 | `summon lightning_bolt ~ ~ ~28 default_lightning_bolt` |
| 20 | -28 | 0 | 0 | 784 | 28.000 | `summon lightning_bolt ~-28 ~ ~ default_lightning_bolt` |
| 21 | 0 | 0 | -28 | 784 | 28.000 | `summon lightning_bolt ~ ~ ~-28 default_lightning_bolt` |
| 22 | 24 | 0 | 24 | 1152 | 33.941 | `summon lightning_bolt ~24 ~ ~24 default_lightning_bolt` |
| 23 | -24 | 0 | -24 | 1152 | 33.941 | `summon lightning_bolt ~-24 ~ ~-24 default_lightning_bolt` |
| 24 | -24 | 0 | 24 | 1152 | 33.941 | `summon lightning_bolt ~-24 ~ ~24 default_lightning_bolt` |
| 25 | 24 | 0 | -24 | 1152 | 33.941 | `summon lightning_bolt ~24 ~ ~-24 default_lightning_bolt` |
| 26 | 34 | 0 | 0 | 1156 | 34.000 | `summon lightning_bolt ~34 ~ ~ default_lightning_bolt` |
| 27 | 0 | 0 | 34 | 1156 | 34.000 | `summon lightning_bolt ~ ~ ~34 default_lightning_bolt` |
| 28 | -34 | 0 | 0 | 1156 | 34.000 | `summon lightning_bolt ~-34 ~ ~ default_lightning_bolt` |
| 29 | 0 | 0 | -34 | 1156 | 34.000 | `summon lightning_bolt ~ ~ ~-34 default_lightning_bolt` |
| 30 | 30 | 0 | 30 | 1800 | 42.426 | `summon lightning_bolt ~30 ~ ~30 default_lightning_bolt` |
| 31 | -30 | 0 | -30 | 1800 | 42.426 | `summon lightning_bolt ~-30 ~ ~-30 default_lightning_bolt` |
| 32 | -30 | 0 | 30 | 1800 | 42.426 | `summon lightning_bolt ~-30 ~ ~30 default_lightning_bolt` |
| 33 | 30 | 0 | -30 | 1800 | 42.426 | `summon lightning_bolt ~30 ~ ~-30 default_lightning_bolt` |
| 34 | 42 | 0 | 0 | 1764 | 42.000 | `summon lightning_bolt ~42 ~ ~ default_lightning_bolt` |
| 35 | 0 | 0 | 42 | 1764 | 42.000 | `summon lightning_bolt ~ ~ ~42 default_lightning_bolt` |
| 36 | -42 | 0 | 0 | 1764 | 42.000 | `summon lightning_bolt ~-42 ~ ~ default_lightning_bolt` |
| 37 | 0 | 0 | -42 | 1764 | 42.000 | `summon lightning_bolt ~ ~ ~-42 default_lightning_bolt` |
| 38 | 38 | 0 | 38 | 2888 | 53.740 | `summon lightning_bolt ~38 ~ ~38 default_lightning_bolt` |
| 39 | -38 | 0 | -38 | 2888 | 53.740 | `summon lightning_bolt ~-38 ~ ~-38 default_lightning_bolt` |
| 40 | -38 | 0 | 38 | 2888 | 53.740 | `summon lightning_bolt ~-38 ~ ~38 default_lightning_bolt` |
| 41 | 38 | 0 | -38 | 2888 | 53.740 | `summon lightning_bolt ~38 ~ ~-38 default_lightning_bolt` |

У события `on_use` вместе с `run_command` объявлен `damage` type durability amount 9 target self; порядок обработки этих полей движком не установлен.
