# Scoreboard: буквальные операции и selectors — 1.6

Лексический поиск `scoreboard`, `scores=` и старых ключей `score_*` во всех `.json`, `.mcfunction`, `.js` behavior pack даёт **228 исходных строк**. Сканируются и строки JSON с ошибками, комментарии, JS и возможные строковые данные; запись сама по себе не доказывает выполнение команды. Имена objectives извлекаются только из буквальных `objectives add/remove`, `players add/set/remove` с числовым аргументом и `scores={...}`; иные формы перечислены как нераспознанные, если встретились.

Числа — **значения score**, не секунды или тики. Операция objective и конкретная запись игрока/сущности различны; селектор, `@s`, ближайший `@p`, контекст execute, наличие objective, прерывание последовательности и конкуренцию игроков нельзя игнорировать. Здесь группировка по имени облегчает поиск, но не заменяет исходный порядок внутри события, условий и вызовов. Один и тот же ряд может попасть в несколько групп; повторы сохраняются.

Распознанные objectives: `b` (11 строк), `bn` (11 строк), `c` (62 строк), `ct` (12 строк), `e` (20 строк), `l` (8 строк), `s` (9 строк), `sh` (11 строк), `swords` (51 строк), `w` (33 строк).

- Нераспознанные кандидаты: нет в ограниченной области сканирования.

Важно: `normal.mcfunction` выполняет через ближайшего подходящего игрока `scoreboard objectives remove b/bn/sh/s`; это операции над именами objective, не команда удаления только его отдельного счёта. `normalft.mcfunction` работает с `@a` и `swords`, а многие контроллеры записывают `@a swords 2`. [Ручная схема глобального состояния](manual-global-state-1.6.md) · [спутники и счётчики](manual-counter-helpers-1.6.md).

## Все строки по имени objective

### b

| Файл и строка | Найденные формы | Исходная строка целиком |
|---|---|---|
| `Sword_B/animation_controllers/blaze_sword.json:14` | `"objectives add"` | `"            \"/scoreboard objectives add b dummy\","` |
| `Sword_B/animation_controllers/blaze_sword.json:15` | `"players add @p 1"` | `"            \"/scoreboard players add @p b 1\","` |
| `Sword_B/animation_controllers/blaze_sword.json:16` | `"selector b=10"` | `"            \"/execute @p[scores={b=10}] ~ ~ ~ summon entity:blaze2\","` |
| `Sword_B/animation_controllers/blaze_sword.json:17` | `"objectives remove"`, `"selector b=5000"` | `"            \"/execute @p[scores={b=5000}] ~ ~ ~ scoreboard objectives remove b\","` |
| `Sword_B/animation_controllers/blaze_sword.json:18` | `"selector b=4990"` | `"            \"/execute @p[scores={b=4990}] ~ ~ ~ kill @e[type=entity:blaze2,r=5] ~ 0 ~\","` |
| `Sword_B/animation_controllers/blaze_sword.json:30` | `"objectives add"` | `"            \"/scoreboard objectives add b dummy\","` |
| `Sword_B/animation_controllers/blaze_sword.json:31` | `"players add @p 1"` | `"            \"/scoreboard players add @p b 1\","` |
| `Sword_B/animation_controllers/blaze_sword.json:32` | `"selector b=10"` | `"            \"/execute @p[scores={b=10}] ~ ~ ~ summon entity:blaze2\","` |
| `Sword_B/animation_controllers/blaze_sword.json:33` | `"objectives remove"`, `"selector b=5000"` | `"            \"/execute @p[scores={b=5000}] ~ ~ ~ scoreboard objectives remove b\","` |
| `Sword_B/animation_controllers/blaze_sword.json:34` | `"selector b=4990"` | `"            \"/execute @p[scores={b=4990}] ~ ~ ~ kill @e[type=entity:blaze2,r=5] ~ 0 ~\","` |
| `Sword_B/functions/normal.mcfunction:7` | `"objectives remove"` | `"execute @p[r=2] ~ ~ ~ scoreboard objectives remove b"` |

### bn

| Файл и строка | Найденные формы | Исходная строка целиком |
|---|---|---|
| `Sword_B/animation_controllers/bone_sword.json:14` | `"objectives add"` | `"            \"/scoreboard objectives add bn dummy\","` |
| `Sword_B/animation_controllers/bone_sword.json:15` | `"players add @p 1"` | `"            \"/scoreboard players add @p bn 1\","` |
| `Sword_B/animation_controllers/bone_sword.json:16` | `"selector bn=10"` | `"            \"/execute @p[scores={bn=10}] ~ ~ ~ summon entity:bone2\","` |
| `Sword_B/animation_controllers/bone_sword.json:17` | `"objectives remove"`, `"selector bn=5000"` | `"            \"/execute @p[scores={bn=5000}] ~ ~ ~ scoreboard objectives remove bn\","` |
| `Sword_B/animation_controllers/bone_sword.json:18` | `"selector bn=4990"` | `"            \"/execute @p[scores={bn=4990}] ~ ~ ~ kill @e[type=entity:bone2,r=5] ~ 0 ~\","` |
| `Sword_B/animation_controllers/bone_sword.json:30` | `"objectives add"` | `"            \"/scoreboard objectives add bn dummy\","` |
| `Sword_B/animation_controllers/bone_sword.json:31` | `"players add @p 1"` | `"            \"/scoreboard players add @p bn 1\","` |
| `Sword_B/animation_controllers/bone_sword.json:32` | `"selector bn=10"` | `"            \"/execute @p[scores={bn=10}] ~ ~ ~ summon entity:bone2\","` |
| `Sword_B/animation_controllers/bone_sword.json:33` | `"objectives remove"`, `"selector bn=5000"` | `"            \"/execute @p[scores={bn=5000}] ~ ~ ~ scoreboard objectives remove bn\","` |
| `Sword_B/animation_controllers/bone_sword.json:34` | `"selector bn=4990"` | `"            \"/execute @p[scores={bn=4990}] ~ ~ ~ kill @e[type=entity:bone2,r=5] ~ 0 ~\","` |
| `Sword_B/functions/normal.mcfunction:8` | `"objectives remove"` | `"execute @p[r=2] ~ ~ ~ scoreboard objectives remove bn"` |

### c

| Файл и строка | Найденные формы | Исходная строка целиком |
|---|---|---|
| `Sword_B/animation_controllers/creeper_sword.json:13` | `"objectives add"` | `"            \"/scoreboard objectives add c dummy\","` |
| `Sword_B/animation_controllers/creeper_sword.json:14` | `"players add @e[r=16] 1"` | `"            \"/scoreboard players add @e[r=16] c 1\","` |
| `Sword_B/animation_controllers/creeper_sword.json:15` | `"selector c=90"` | `"            \"/playsound mob.creeper.say @p[scores={c=90}]\","` |
| `Sword_B/animation_controllers/creeper_sword.json:16` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=zombie] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:17` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=husk] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:18` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=drowned] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:19` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=enderman] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:20` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=slime] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:21` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=skeleton] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:22` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=stray] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:23` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=blaze] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:24` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=wither_skeleton] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:25` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=witch] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:26` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=magma_cube] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:27` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=ghast] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:28` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=zombie_pigman] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:29` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=spider] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:30` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=cave_spider] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:31` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=silverfish] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:32` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=evocation_fang] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:33` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=evocation_illager] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:34` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=vex] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:35` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=ravager] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:36` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=endermite] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:37` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=guardian] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:38` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=vindicator] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:39` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=phantom] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:40` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=tnt] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:41` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=zombie_villager] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:42` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=wither] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:43` | `"objectives remove"`, `"selector c=300"` | `"            \"/execute @p[scores={c=300}] ~ ~ ~ scoreboard objectives remove c\","` |
| `Sword_B/animation_controllers/creeper_sword.json:54` | `"objectives add"` | `"            \"/scoreboard objectives add c dummy\","` |
| `Sword_B/animation_controllers/creeper_sword.json:55` | `"players add @e[r=16] 1"` | `"            \"/scoreboard players add @e[r=16] c 1\","` |
| `Sword_B/animation_controllers/creeper_sword.json:56` | `"selector c=90"` | `"            \"/playsound mob.creeper.say @p[scores={c=90}]\","` |
| `Sword_B/animation_controllers/creeper_sword.json:57` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=zombie] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:58` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=husk] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:59` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=drowned] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:60` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=enderman] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:61` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=slime] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:62` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=skeleton] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:63` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=stray] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:64` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=blaze] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:65` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=wither_skeleton] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:66` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=witch] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:67` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=magma_cube] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:68` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=ghast] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:69` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=zombie_pigman] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:70` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=spider] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:71` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=cave_spider] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:72` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=silverfish] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:73` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=evocation_fang] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:74` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=evocation_illager] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:75` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=vex] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:76` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=ravager] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:77` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=endermite] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:78` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=guardian] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:79` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=vindicator] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:80` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=phantom] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:81` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=tnt] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:82` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=zombie_villager] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:83` | `"selector c=100"` | `"            \"/execute @e[scores={c=100},r=16,type=wither] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/creeper_sword.json:84` | `"objectives remove"`, `"selector c=300"` | `"            \"/execute @p[scores={c=300}] ~ ~ ~ scoreboard objectives remove c\","` |

### ct

| Файл и строка | Найденные формы | Исходная строка целиком |
|---|---|---|
| `Sword_B/animation_controllers/cactus_sword.json:13` | `"objectives add"` | `"          \t\"/scoreboard objectives add ct dummy\","` |
| `Sword_B/animation_controllers/cactus_sword.json:14` | `"players add @p 1"` | `"            \"/scoreboard players add @p ct 1\","` |
| `Sword_B/animation_controllers/cactus_sword.json:15` | `"players add @e[r=3,type=!entity:cactus,type=!player] 1"` | `"            \"/scoreboard players add @e[r=3,type=!entity:cactus,type=!player] ct 1\","` |
| `Sword_B/animation_controllers/cactus_sword.json:16` | `"selector ct=1"` | `"            \"/execute @p[scores={ct=1}] ~ ~ ~ effect @s poison 1 1 true\","` |
| `Sword_B/animation_controllers/cactus_sword.json:17` | `"selector ct=1"` | `"            \"/execute @e[scores={ct=1},r=2] ~ ~ ~ effect @s poison 1 1 true\","` |
| `Sword_B/animation_controllers/cactus_sword.json:18` | `"objectives remove"`, `"selector ct=20"` | `"            \"/execute @p[scores={ct=20}] ~ ~ ~ scoreboard objectives remove ct\","` |
| `Sword_B/animation_controllers/cactus_sword.json:29` | `"objectives add"` | `"            \"/scoreboard objectives add ct dummy\","` |
| `Sword_B/animation_controllers/cactus_sword.json:30` | `"players add @p 1"` | `"            \"/scoreboard players add @p ct 1\","` |
| `Sword_B/animation_controllers/cactus_sword.json:31` | `"players add @e[r=3,type=!entity:cactus,type=!player] 1"` | `"            \"/scoreboard players add @e[r=3,type=!entity:cactus,type=!player] ct 1\","` |
| `Sword_B/animation_controllers/cactus_sword.json:32` | `"selector ct=1"` | `"            \"/execute @p[scores={ct=1}] ~ ~ ~ effect @s poison 1 1 true\","` |
| `Sword_B/animation_controllers/cactus_sword.json:33` | `"selector ct=1"` | `"            \"/execute @e[scores={ct=1},r=2] ~ ~ ~ effect @s poison 1 1 true\","` |
| `Sword_B/animation_controllers/cactus_sword.json:34` | `"objectives remove"`, `"selector ct=20"` | `"            \"/execute @p[scores={ct=20}] ~ ~ ~ scoreboard objectives remove ct\","` |

### e

| Файл и строка | Найденные формы | Исходная строка целиком |
|---|---|---|
| `Sword_B/animation_controllers/ender_sword.json:15` | `"objectives add"` | `"          \t\"/scoreboard objectives add e dummy\","` |
| `Sword_B/animation_controllers/ender_sword.json:16` | `"players add @e[r=16] 1"` | `"            \"/scoreboard players add @e[r=16] e 1\","` |
| `Sword_B/animation_controllers/ender_sword.json:17` | `"selector e=10"` | `"            \"/playsound mob.endermen.scream @p[scores={e=10}]\","` |
| `Sword_B/animation_controllers/ender_sword.json:18` | `"selector e=90"` | `"            \"/playsound mob.endermen.portal @p[scores={e=90}]\","` |
| `Sword_B/animation_controllers/ender_sword.json:19` | `"selector e=140"` | `"            \"/playsound mob.endermen.hit @p[scores={e=140}]\","` |
| `Sword_B/animation_controllers/ender_sword.json:20` | `"selector e=300"` | `"            \"/playsound mob.endermen.idle @p[scores={e=300}]\","` |
| `Sword_B/animation_controllers/ender_sword.json:21` | `"selector e=500"` | `"            \"/playsound mob.endermen.stare @p[scores={e=500}]\","` |
| `Sword_B/animation_controllers/ender_sword.json:22` | `"objectives remove"`, `"selector e=700"` | `"            \"/execute @p[scores={e=700}] ~ ~ ~ scoreboard objectives remove e\","` |
| `Sword_B/animation_controllers/ender_sword.json:23` | `"objectives remove"`, `"selector e=750"` | `"            \"/execute @p[scores={e=750}] ~ ~ ~ scoreboard objectives remove e\","` |
| `Sword_B/animation_controllers/ender_sword.json:24` | `"selector e=85"` | `"            \"/execute @p[scores={e=85}] ~ ~ ~ spreadplayers ~ ~ 8 16 @s\","` |
| `Sword_B/animation_controllers/ender_sword.json:64` | `"objectives add"` | `"          \t\"/scoreboard objectives add e dummy\","` |
| `Sword_B/animation_controllers/ender_sword.json:65` | `"players add @e[r=16] 1"` | `"            \"/scoreboard players add @e[r=16] e 1\","` |
| `Sword_B/animation_controllers/ender_sword.json:66` | `"selector e=10"` | `"            \"/playsound mob.endermen.scream @p[scores={e=10}]\","` |
| `Sword_B/animation_controllers/ender_sword.json:67` | `"selector e=90"` | `"            \"/playsound mob.endermen.portal @p[scores={e=90}]\","` |
| `Sword_B/animation_controllers/ender_sword.json:68` | `"selector e=140"` | `"            \"/playsound mob.endermen.hit @p[scores={e=140}]\","` |
| `Sword_B/animation_controllers/ender_sword.json:69` | `"selector e=300"` | `"            \"/playsound mob.endermen.idle @p[scores={e=300}]\","` |
| `Sword_B/animation_controllers/ender_sword.json:70` | `"selector e=500"` | `"            \"/playsound mob.endermen.stare @p[scores={e=500}]\","` |
| `Sword_B/animation_controllers/ender_sword.json:71` | `"objectives remove"`, `"selector e=700"` | `"            \"/execute @p[scores={e=700}] ~ ~ ~ scoreboard objectives remove e\","` |
| `Sword_B/animation_controllers/ender_sword.json:72` | `"objectives remove"`, `"selector e=750"` | `"            \"/execute @p[scores={e=750}] ~ ~ ~ scoreboard objectives remove e\","` |
| `Sword_B/animation_controllers/ender_sword.json:73` | `"selector e=85"` | `"            \"/execute @p[scores={e=85}] ~ ~ ~ spreadplayers ~ ~ 8 16 @s\","` |

### l

| Файл и строка | Найденные формы | Исходная строка целиком |
|---|---|---|
| `Sword_B/animation_controllers/lapis_sword.json:13` | `"objectives add"` | `"            \"/scoreboard objectives add l dummy\","` |
| `Sword_B/animation_controllers/lapis_sword.json:14` | `"players add @p 1"` | `"            \"/scoreboard players add @p l 1\","` |
| `Sword_B/animation_controllers/lapis_sword.json:15` | `"selector l=10"` | `"            \"/execute @p[scores={l=10}] ~ ~ ~ xp 5 @s\","` |
| `Sword_B/animation_controllers/lapis_sword.json:16` | `"objectives remove"`, `"selector l=30"` | `"            \"/execute @p[scores={l=30}] ~ ~ ~ scoreboard objectives remove l\","` |
| `Sword_B/animation_controllers/lapis_sword.json:27` | `"objectives add"` | `"            \"/scoreboard objectives add l dummy\","` |
| `Sword_B/animation_controllers/lapis_sword.json:28` | `"players add @p 1"` | `"            \"/scoreboard players add @p l 1\","` |
| `Sword_B/animation_controllers/lapis_sword.json:29` | `"selector l=10"` | `"            \"/execute @p[scores={l=10}] ~ ~ ~ xp 5 @s\","` |
| `Sword_B/animation_controllers/lapis_sword.json:30` | `"objectives remove"`, `"selector l=30"` | `"            \"/execute @p[scores={l=30}] ~ ~ ~ scoreboard objectives remove l\","` |

### s

| Файл и строка | Найденные формы | Исходная строка целиком |
|---|---|---|
| `Sword_B/animation_controllers/slime_sword.json:13` | `"objectives add"` | `"          \t\"/scoreboard objectives add s dummy\","` |
| `Sword_B/animation_controllers/slime_sword.json:14` | `"players add @p 1"` | `"            \"/scoreboard players add @p s 1\","` |
| `Sword_B/animation_controllers/slime_sword.json:15` | `"selector s=1"` | `"            \"/execute @p[scores={s=1}] ~ ~ ~ summon slime\","` |
| `Sword_B/animation_controllers/slime_sword.json:17` | `"objectives remove"`, `"selector s=600"` | `"            \"/execute @p[scores={s=600}] ~ ~ ~ scoreboard objectives remove s\","` |
| `Sword_B/animation_controllers/slime_sword.json:32` | `"objectives add"` | `"            \"/scoreboard objectives add s dummy\","` |
| `Sword_B/animation_controllers/slime_sword.json:33` | `"players add @p 1"` | `"            \"/scoreboard players add @p s 1\","` |
| `Sword_B/animation_controllers/slime_sword.json:34` | `"selector s=1"` | `"            \"/execute @p[scores={s=1}] ~ ~ ~ summon slime\","` |
| `Sword_B/animation_controllers/slime_sword.json:36` | `"objectives remove"`, `"selector s=600"` | `"            \"/execute @p[scores={s=600}] ~ ~ ~ scoreboard objectives remove s\","` |
| `Sword_B/functions/normal.mcfunction:18` | `"objectives remove"` | `"execute @p[r=2] ~ ~ ~ scoreboard objectives remove s"` |

### sh

| Файл и строка | Найденные формы | Исходная строка целиком |
|---|---|---|
| `Sword_B/animation_controllers/shulker_sword.json:15` | `"objectives add"` | `"            \"/scoreboard objectives add sh dummy\","` |
| `Sword_B/animation_controllers/shulker_sword.json:16` | `"players add @p 1"` | `"            \"/scoreboard players add @p sh 1\","` |
| `Sword_B/animation_controllers/shulker_sword.json:17` | `"selector sh=40"` | `"            \"/execute @p[scores={sh=40}] ~ ~ ~ summon entity:shulker2\","` |
| `Sword_B/animation_controllers/shulker_sword.json:18` | `"objectives remove"`, `"selector sh=2400"` | `"            \"/execute @p[scores={sh=2400}] ~ ~ ~ scoreboard objectives remove sh\","` |
| `Sword_B/animation_controllers/shulker_sword.json:19` | `"selector sh=2390"` | `"            \"/execute @p[scores={sh=2390}] ~ ~ ~ kill @e[type=entity:shulker2,r=5] ~ 0 ~\","` |
| `Sword_B/animation_controllers/shulker_sword.json:32` | `"objectives add"` | `"            \"/scoreboard objectives add sh dummy\","` |
| `Sword_B/animation_controllers/shulker_sword.json:33` | `"players add @p 1"` | `"            \"/scoreboard players add @p sh 1\","` |
| `Sword_B/animation_controllers/shulker_sword.json:34` | `"selector sh=40"` | `"            \"/execute @p[scores={sh=40}] ~ ~ ~ summon entity:shulker2\","` |
| `Sword_B/animation_controllers/shulker_sword.json:35` | `"objectives remove"`, `"selector sh=2400"` | `"            \"/execute @p[scores={sh=2400}] ~ ~ ~ scoreboard objectives remove sh\","` |
| `Sword_B/animation_controllers/shulker_sword.json:36` | `"selector sh=2390"` | `"            \"/execute @p[scores={sh=2390}] ~ ~ ~ kill @e[type=entity:shulker2,r=5] ~ 0 ~\","` |
| `Sword_B/functions/normal.mcfunction:9` | `"objectives remove"` | `"execute @p[r=2] ~ ~ ~ scoreboard objectives remove sh"` |

### swords

| Файл и строка | Найденные формы | Исходная строка целиком |
|---|---|---|
| `Sword_B/animation_controllers/blaze_sword.json:19` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/blaze_sword.json:35` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/bone_sword.json:19` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/bone_sword.json:35` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/cactus_sword.json:19` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/cactus_sword.json:35` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/coal_sword.json:26` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/coal_sword.json:49` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/creeper_sword.json:44` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/creeper_sword.json:85` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/emerald_sword.json:14` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/emerald_sword.json:25` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/ender_sword.json:52` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/ender_sword.json:101` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/fire_sword.json:51` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/fire_sword.json:102` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/glowstone_sword.json:16` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/glowstone_sword.json:29` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/grass_sword.json:16` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/grass_sword.json:29` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/ice_sword.json:48` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/jungle_sword.json:167` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/lapis_sword.json:17` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/lapis_sword.json:31` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/lightning sword.json:39` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/lightning sword.json:75` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/magma_sword.json:36` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/magma_sword.json:69` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/obsidian_sword.json:25` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/obsidian_sword.json:47` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\"   "` |
| `Sword_B/animation_controllers/sea_sword.json:16` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/sea_sword.json:30` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/shulker_sword.json:20` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/shulker_sword.json:37` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/slime_sword.json:18` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/slime_sword.json:37` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/spectral_sword.json:20` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/spectral_sword.json:37` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/spider_sword.json:43` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/spider_sword.json:87` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/sponge_sword.json:25` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/sponge_sword.json:47` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/sword of time.json:16` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/sword of time.json:29` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/tnt_sword.json:39` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/tnt_sword.json:75` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/animation_controllers/wither_sword.json:68` | `"players set @a 2"` | `"            \"/scoreboard players set @a swords 2\""` |
| `Sword_B/functions/normalft.mcfunction:1` | `"objectives add"` | `"scoreboard objectives add swords dummy"` |
| `Sword_B/functions/normalft.mcfunction:2` | `"players remove @a[scores={swords=1}] 1"`, `"selector swords=1"` | `"scoreboard players remove @a[scores={swords=1}] swords 1"` |
| `Sword_B/functions/normalft.mcfunction:3` | `"players remove @a[scores={swords=2}] 1"`, `"selector swords=2"` | `"scoreboard players remove @a[scores={swords=2}] swords 1"` |
| `Sword_B/functions/normalft.mcfunction:4` | `"selector swords=0"` | `"execute @a[scores={swords=0}] ~ ~ ~ function normal"` |

### w

| Файл и строка | Найденные формы | Исходная строка целиком |
|---|---|---|
| `Sword_B/animation_controllers/wither_sword.json:35` | `"objectives add"` | `"          \t\"/scoreboard objectives add w dummy\","` |
| `Sword_B/animation_controllers/wither_sword.json:36` | `"players add @e[r=16,type=!cow,type=!pig,type=!sheep,type=!horse,type=!rabbit,type=!villager,type=!wolf,type=!cat,type=!fox,type=!chicken] 1"` | `"          \t\"/scoreboard players add @e[r=16,type=!cow,type=!pig,type=!sheep,type=!horse,type=!rabbit,type=!villager,type=!wolf,type=!cat,type=!fox,type=!chicken] w 1\","` |
| `Sword_B/animation_controllers/wither_sword.json:37` | `"selector w=200"` | `"          \t\"/execute @p[scores={w=200}] ~ ~ ~ playsound mob.wither.death\","` |
| `Sword_B/animation_controllers/wither_sword.json:38` | `"selector w=500"` | `"          \t\"/execute @p[scores={w=500}] ~ ~ ~ playsound mob.wither.hurt\","` |
| `Sword_B/animation_controllers/wither_sword.json:39` | `"selector w=100"` | `"          \t\"/execute @e[scores={w=100},r=16,type=zombie] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/wither_sword.json:40` | `"selector w=100"` | `"            \"/execute @e[scores={w=100},r=16,type=husk] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/wither_sword.json:41` | `"selector w=100"` | `"            \"/execute @e[scores={w=100},r=16,type=drowned] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/wither_sword.json:42` | `"selector w=100"` | `"            \"/execute @e[scores={w=100},r=16,type=creeper] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/wither_sword.json:43` | `"selector w=100"` | `"            \"/execute @e[scores={w=100},r=16,type=enderman] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/wither_sword.json:44` | `"selector w=100"` | `"            \"/execute @e[scores={w=100},r=16,type=slime] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/wither_sword.json:45` | `"selector w=100"` | `"            \"/execute @e[scores={w=100},r=16,type=skeleton] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/wither_sword.json:46` | `"selector w=100"` | `"            \"/execute @e[scores={w=100},r=16,type=stray] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/wither_sword.json:47` | `"selector w=100"` | `"            \"/execute @e[scores={w=100},r=16,type=blaze] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/wither_sword.json:48` | `"selector w=100"` | `"            \"/execute @e[scores={w=100},r=16,type=wither_skeleton] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/wither_sword.json:49` | `"selector w=100"` | `"            \"/execute @e[scores={w=100},r=16,type=witch] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/wither_sword.json:50` | `"selector w=100"` | `"            \"/execute @e[scores={w=100},r=16,type=magma_cube] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/wither_sword.json:51` | `"selector w=100"` | `"            \"/execute @e[scores={w=100},r=16,type=ghast] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/wither_sword.json:52` | `"selector w=100"` | `"            \"/execute @e[scores={w=100},r=16,type=zombie_pigman] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/wither_sword.json:53` | `"selector w=100"` | `"            \"/execute @e[scores={w=100},r=16,type=spider] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/wither_sword.json:54` | `"selector w=100"` | `"            \"/execute @e[scores={w=100},r=16,type=cave_spider] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/wither_sword.json:55` | `"selector w=100"` | `"            \"/execute @e[scores={w=100},r=16,type=silverfish] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/wither_sword.json:56` | `"selector w=100"` | `"            \"/execute @e[scores={w=100},r=16,type=evocation_fang] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/wither_sword.json:57` | `"selector w=100"` | `"            \"/execute @e[scores={w=100},r=16,type=evocation_illager] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/wither_sword.json:58` | `"selector w=100"` | `"            \"/execute @e[scores={w=100},r=16,type=vex] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/wither_sword.json:59` | `"selector w=100"` | `"            \"/execute @e[scores={w=100},r=16,type=ravager] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/wither_sword.json:60` | `"selector w=100"` | `"            \"/execute @e[scores={w=100},r=16,type=endermite] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/wither_sword.json:61` | `"selector w=100"` | `"            \"/execute @e[scores={w=100},r=16,type=guardian] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/wither_sword.json:62` | `"selector w=100"` | `"            \"/execute @e[scores={w=100},r=16,type=vindicator] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/wither_sword.json:63` | `"selector w=100"` | `"            \"/execute @e[scores={w=100},r=16,type=phantom] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/wither_sword.json:64` | `"selector w=100"` | `"            \"/execute @e[scores={w=100},r=16,type=tnt] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/wither_sword.json:65` | `"selector w=100"` | `"            \"/execute @e[scores={w=100},r=16,type=zombie_villager] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/wither_sword.json:66` | `"selector w=100"` | `"            \"/execute @e[scores={w=100},r=16,type=wither] ~ ~ ~ summon entity:explode\","` |
| `Sword_B/animation_controllers/wither_sword.json:67` | `"objectives remove"`, `"selector w=600"` | `"          \t\"/execute @p[scores={w=600}] ~ ~ ~ scoreboard objectives remove w\","` |
