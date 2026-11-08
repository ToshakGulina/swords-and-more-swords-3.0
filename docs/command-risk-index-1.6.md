# Выбранные побочные команды: буквальные кандидаты — 1.6

Из 922 строк следующих источников выделено **158** строк, содержащих одно или более ключевых слов: `gamerule, scoreboard, time, weather, kill, damage, tp, teleport, ride, replaceitem, clear, tickingarea`. Область поиска: `run_command.command`, строковые `on_entry`/`on_exit` в разобранных behavior JSON и непустые, не начинающиеся с `#` строки behavior mcfunction. Дубли из разных состояний и повторённые строки сохранены; номера/пути позволяют видеть порядок в конкретном списке.

Это **лексический поиск**, не парсер команд и не подтверждение действия. Совпадение слова может находиться в аргументе или вложенном execute, а условие, адресат, область и разрешение `@s` зависят от контекста. `target` показан только явно записанный рядом с `run_command`; отсутствие не превращается в self. Состояния `on_entry`/`on_exit` могут содержать не только команды. Отдельные метки могут пересекаться, поэтому их количества нельзя складывать как число строк.

Вне поиска: JS, строки команд в других полях, неразобранные JSON, внешние/ванильные вызовы, интерпретация `/function`, `fill`, `setblock`, `summon`, структуры и действия компонентов. Например, изменение мира может происходить и без команд из этого списка. Для обычных вызовов и полных условий сверять [реестр сущностей](entity-ledger-1.6.md), [контроллеры](animation-ledger-1.6.md), [предметы](items-1.6.md) и исходный архив.

Метки по числу **строк**, а не исполнений: `gamerule` — 5, `scoreboard` — 109, `time` — 2, `weather` — 0, `kill` — 6, `damage` — 0, `tp` — 10, `teleport` — 0, `ride` — 0, `replaceitem` — 26, `clear` — 0, `tickingarea` — 0.

- Неразобранные JSON: `Sword_B/entities/blaze2.json` (<string>:78 Unexpected "}" at column 1); `Sword_B/entities/bone2.json` (<string>:75 Unexpected "}" at column 1); `Sword_B/entities/shulker2.json` (<string>:75 Unexpected "}" at column 1).
- Повторные ключи: нет. JSON5 сохраняет последнее значение.

| Файл / путь | Источник / target | Метки | Исходная строка |
|---|---|---|---|
| `Sword_B/animation_controllers/blaze_sword.json`<br>`$.animation_controllers.controller.animation.blaze.states.default.on_entry[0]` | on_entry | `tp` | `/execute @p ~ ~ ~ tp @e[type=entity:blaze2] ~ ~2 ~` |
| `Sword_B/animation_controllers/blaze_sword.json`<br>`$.animation_controllers.controller.animation.blaze.states.default.on_entry[1]` | on_entry | `scoreboard` | `/scoreboard objectives add b dummy` |
| `Sword_B/animation_controllers/blaze_sword.json`<br>`$.animation_controllers.controller.animation.blaze.states.default.on_entry[2]` | on_entry | `scoreboard` | `/scoreboard players add @p b 1` |
| `Sword_B/animation_controllers/blaze_sword.json`<br>`$.animation_controllers.controller.animation.blaze.states.default.on_entry[4]` | on_entry | `scoreboard` | `/execute @p[scores={b=5000}] ~ ~ ~ scoreboard objectives remove b` |
| `Sword_B/animation_controllers/blaze_sword.json`<br>`$.animation_controllers.controller.animation.blaze.states.default.on_entry[5]` | on_entry | `kill` | `/execute @p[scores={b=4990}] ~ ~ ~ kill @e[type=entity:blaze2,r=5] ~ 0 ~` |
| `Sword_B/animation_controllers/blaze_sword.json`<br>`$.animation_controllers.controller.animation.blaze.states.default.on_entry[6]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/blaze_sword.json`<br>`$.animation_controllers.controller.animation.blaze.states.blaze.on_entry[0]` | on_entry | `tp` | `/execute @p ~ ~ ~ tp @e[type=entity:blaze2] ~ ~2 ~` |
| `Sword_B/animation_controllers/blaze_sword.json`<br>`$.animation_controllers.controller.animation.blaze.states.blaze.on_entry[1]` | on_entry | `scoreboard` | `/scoreboard objectives add b dummy` |
| `Sword_B/animation_controllers/blaze_sword.json`<br>`$.animation_controllers.controller.animation.blaze.states.blaze.on_entry[2]` | on_entry | `scoreboard` | `/scoreboard players add @p b 1` |
| `Sword_B/animation_controllers/blaze_sword.json`<br>`$.animation_controllers.controller.animation.blaze.states.blaze.on_entry[4]` | on_entry | `scoreboard` | `/execute @p[scores={b=5000}] ~ ~ ~ scoreboard objectives remove b` |
| `Sword_B/animation_controllers/blaze_sword.json`<br>`$.animation_controllers.controller.animation.blaze.states.blaze.on_entry[5]` | on_entry | `kill` | `/execute @p[scores={b=4990}] ~ ~ ~ kill @e[type=entity:blaze2,r=5] ~ 0 ~` |
| `Sword_B/animation_controllers/blaze_sword.json`<br>`$.animation_controllers.controller.animation.blaze.states.blaze.on_entry[6]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/bone_sword.json`<br>`$.animation_controllers.controller.animation.bone.states.default.on_entry[0]` | on_entry | `tp` | `/execute @p ~ ~ ~ tp @e[type=entity:bone2] ~ ~2 ~` |
| `Sword_B/animation_controllers/bone_sword.json`<br>`$.animation_controllers.controller.animation.bone.states.default.on_entry[1]` | on_entry | `scoreboard` | `/scoreboard objectives add bn dummy` |
| `Sword_B/animation_controllers/bone_sword.json`<br>`$.animation_controllers.controller.animation.bone.states.default.on_entry[2]` | on_entry | `scoreboard` | `/scoreboard players add @p bn 1` |
| `Sword_B/animation_controllers/bone_sword.json`<br>`$.animation_controllers.controller.animation.bone.states.default.on_entry[4]` | on_entry | `scoreboard` | `/execute @p[scores={bn=5000}] ~ ~ ~ scoreboard objectives remove bn` |
| `Sword_B/animation_controllers/bone_sword.json`<br>`$.animation_controllers.controller.animation.bone.states.default.on_entry[5]` | on_entry | `kill` | `/execute @p[scores={bn=4990}] ~ ~ ~ kill @e[type=entity:bone2,r=5] ~ 0 ~` |
| `Sword_B/animation_controllers/bone_sword.json`<br>`$.animation_controllers.controller.animation.bone.states.default.on_entry[6]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/bone_sword.json`<br>`$.animation_controllers.controller.animation.bone.states.bone.on_entry[0]` | on_entry | `tp` | `/execute @p ~ ~ ~ tp @e[type=entity:bone2] ~ ~2 ~` |
| `Sword_B/animation_controllers/bone_sword.json`<br>`$.animation_controllers.controller.animation.bone.states.bone.on_entry[1]` | on_entry | `scoreboard` | `/scoreboard objectives add bn dummy` |
| `Sword_B/animation_controllers/bone_sword.json`<br>`$.animation_controllers.controller.animation.bone.states.bone.on_entry[2]` | on_entry | `scoreboard` | `/scoreboard players add @p bn 1` |
| `Sword_B/animation_controllers/bone_sword.json`<br>`$.animation_controllers.controller.animation.bone.states.bone.on_entry[4]` | on_entry | `scoreboard` | `/execute @p[scores={bn=5000}] ~ ~ ~ scoreboard objectives remove bn` |
| `Sword_B/animation_controllers/bone_sword.json`<br>`$.animation_controllers.controller.animation.bone.states.bone.on_entry[5]` | on_entry | `kill` | `/execute @p[scores={bn=4990}] ~ ~ ~ kill @e[type=entity:bone2,r=5] ~ 0 ~` |
| `Sword_B/animation_controllers/bone_sword.json`<br>`$.animation_controllers.controller.animation.bone.states.bone.on_entry[6]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/cactus_sword.json`<br>`$.animation_controllers.controller.animation.cactus.states.default.on_entry[0]` | on_entry | `scoreboard` | `/scoreboard objectives add ct dummy` |
| `Sword_B/animation_controllers/cactus_sword.json`<br>`$.animation_controllers.controller.animation.cactus.states.default.on_entry[1]` | on_entry | `scoreboard` | `/scoreboard players add @p ct 1` |
| `Sword_B/animation_controllers/cactus_sword.json`<br>`$.animation_controllers.controller.animation.cactus.states.default.on_entry[2]` | on_entry | `scoreboard` | `/scoreboard players add @e[r=3,type=!entity:cactus,type=!player] ct 1` |
| `Sword_B/animation_controllers/cactus_sword.json`<br>`$.animation_controllers.controller.animation.cactus.states.default.on_entry[5]` | on_entry | `scoreboard` | `/execute @p[scores={ct=20}] ~ ~ ~ scoreboard objectives remove ct` |
| `Sword_B/animation_controllers/cactus_sword.json`<br>`$.animation_controllers.controller.animation.cactus.states.default.on_entry[6]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/cactus_sword.json`<br>`$.animation_controllers.controller.animation.cactus.states.cactus.on_entry[0]` | on_entry | `scoreboard` | `/scoreboard objectives add ct dummy` |
| `Sword_B/animation_controllers/cactus_sword.json`<br>`$.animation_controllers.controller.animation.cactus.states.cactus.on_entry[1]` | on_entry | `scoreboard` | `/scoreboard players add @p ct 1` |
| `Sword_B/animation_controllers/cactus_sword.json`<br>`$.animation_controllers.controller.animation.cactus.states.cactus.on_entry[2]` | on_entry | `scoreboard` | `/scoreboard players add @e[r=3,type=!entity:cactus,type=!player] ct 1` |
| `Sword_B/animation_controllers/cactus_sword.json`<br>`$.animation_controllers.controller.animation.cactus.states.cactus.on_entry[5]` | on_entry | `scoreboard` | `/execute @p[scores={ct=20}] ~ ~ ~ scoreboard objectives remove ct` |
| `Sword_B/animation_controllers/cactus_sword.json`<br>`$.animation_controllers.controller.animation.cactus.states.cactus.on_entry[6]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/coal_sword.json`<br>`$.animation_controllers.controller.animation.coal.states.default.on_entry[0]` | on_entry | `replaceitem` | `/replaceitem block ~-1 ~ ~ slot.container 1 coal` |
| `Sword_B/animation_controllers/coal_sword.json`<br>`$.animation_controllers.controller.animation.coal.states.default.on_entry[1]` | on_entry | `replaceitem` | `/replaceitem block ~1 ~ ~ slot.container 1 coal` |
| `Sword_B/animation_controllers/coal_sword.json`<br>`$.animation_controllers.controller.animation.coal.states.default.on_entry[2]` | on_entry | `replaceitem` | `/replaceitem block ~ ~ ~-1 slot.container 1 coal` |
| `Sword_B/animation_controllers/coal_sword.json`<br>`$.animation_controllers.controller.animation.coal.states.default.on_entry[3]` | on_entry | `replaceitem` | `/replaceitem block ~ ~ ~1 slot.container 1 coal` |
| `Sword_B/animation_controllers/coal_sword.json`<br>`$.animation_controllers.controller.animation.coal.states.default.on_entry[4]` | on_entry | `replaceitem` | `/replaceitem block ~ ~-1 ~ slot.container 1 coal` |
| `Sword_B/animation_controllers/coal_sword.json`<br>`$.animation_controllers.controller.animation.coal.states.default.on_entry[5]` | on_entry | `replaceitem` | `/replaceitem block ~-1 ~1 ~ slot.container 1 coal` |
| `Sword_B/animation_controllers/coal_sword.json`<br>`$.animation_controllers.controller.animation.coal.states.default.on_entry[6]` | on_entry | `replaceitem` | `/replaceitem block ~1 ~1 ~ slot.container 1 coal` |
| `Sword_B/animation_controllers/coal_sword.json`<br>`$.animation_controllers.controller.animation.coal.states.default.on_entry[7]` | on_entry | `replaceitem` | `/replaceitem block ~ ~1 ~-1 slot.container 1 coal` |
| `Sword_B/animation_controllers/coal_sword.json`<br>`$.animation_controllers.controller.animation.coal.states.default.on_entry[8]` | on_entry | `replaceitem` | `/replaceitem block ~ ~1 ~1 slot.container 1 coal` |
| `Sword_B/animation_controllers/coal_sword.json`<br>`$.animation_controllers.controller.animation.coal.states.default.on_entry[9]` | on_entry | `replaceitem` | `/replaceitem block ~-1 ~-1 ~ slot.container 1 coal` |
| `Sword_B/animation_controllers/coal_sword.json`<br>`$.animation_controllers.controller.animation.coal.states.default.on_entry[10]` | on_entry | `replaceitem` | `/replaceitem block ~1 ~-1 ~ slot.container 1 coal` |
| `Sword_B/animation_controllers/coal_sword.json`<br>`$.animation_controllers.controller.animation.coal.states.default.on_entry[11]` | on_entry | `replaceitem` | `/replaceitem block ~ ~-1 ~-1 slot.container 1 coal` |
| `Sword_B/animation_controllers/coal_sword.json`<br>`$.animation_controllers.controller.animation.coal.states.default.on_entry[12]` | on_entry | `replaceitem` | `/replaceitem block ~ ~-1 ~1 slot.container 1 coal` |
| `Sword_B/animation_controllers/coal_sword.json`<br>`$.animation_controllers.controller.animation.coal.states.default.on_entry[13]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/coal_sword.json`<br>`$.animation_controllers.controller.animation.coal.states.coal.on_entry[0]` | on_entry | `replaceitem` | `/replaceitem block ~-1 ~ ~ slot.container 1 coal` |
| `Sword_B/animation_controllers/coal_sword.json`<br>`$.animation_controllers.controller.animation.coal.states.coal.on_entry[1]` | on_entry | `replaceitem` | `/replaceitem block ~1 ~ ~ slot.container 1 coal` |
| `Sword_B/animation_controllers/coal_sword.json`<br>`$.animation_controllers.controller.animation.coal.states.coal.on_entry[2]` | on_entry | `replaceitem` | `/replaceitem block ~ ~ ~-1 slot.container 1 coal` |
| `Sword_B/animation_controllers/coal_sword.json`<br>`$.animation_controllers.controller.animation.coal.states.coal.on_entry[3]` | on_entry | `replaceitem` | `/replaceitem block ~ ~ ~1 slot.container 1 coal` |
| `Sword_B/animation_controllers/coal_sword.json`<br>`$.animation_controllers.controller.animation.coal.states.coal.on_entry[4]` | on_entry | `replaceitem` | `/replaceitem block ~ ~-1 ~ slot.container 1 coal` |
| `Sword_B/animation_controllers/coal_sword.json`<br>`$.animation_controllers.controller.animation.coal.states.coal.on_entry[5]` | on_entry | `replaceitem` | `/replaceitem block ~-1 ~1 ~ slot.container 1 coal` |
| `Sword_B/animation_controllers/coal_sword.json`<br>`$.animation_controllers.controller.animation.coal.states.coal.on_entry[6]` | on_entry | `replaceitem` | `/replaceitem block ~1 ~1 ~ slot.container 1 coal` |
| `Sword_B/animation_controllers/coal_sword.json`<br>`$.animation_controllers.controller.animation.coal.states.coal.on_entry[7]` | on_entry | `replaceitem` | `/replaceitem block ~ ~1 ~-1 slot.container 1 coal` |
| `Sword_B/animation_controllers/coal_sword.json`<br>`$.animation_controllers.controller.animation.coal.states.coal.on_entry[8]` | on_entry | `replaceitem` | `/replaceitem block ~ ~1 ~1 slot.container 1 coal` |
| `Sword_B/animation_controllers/coal_sword.json`<br>`$.animation_controllers.controller.animation.coal.states.coal.on_entry[9]` | on_entry | `replaceitem` | `/replaceitem block ~-1 ~-1 ~ slot.container 1 coal` |
| `Sword_B/animation_controllers/coal_sword.json`<br>`$.animation_controllers.controller.animation.coal.states.coal.on_entry[10]` | on_entry | `replaceitem` | `/replaceitem block ~1 ~-1 ~ slot.container 1 coal` |
| `Sword_B/animation_controllers/coal_sword.json`<br>`$.animation_controllers.controller.animation.coal.states.coal.on_entry[11]` | on_entry | `replaceitem` | `/replaceitem block ~ ~-1 ~-1 slot.container 1 coal` |
| `Sword_B/animation_controllers/coal_sword.json`<br>`$.animation_controllers.controller.animation.coal.states.coal.on_entry[12]` | on_entry | `replaceitem` | `/replaceitem block ~ ~-1 ~1 slot.container 1 coal` |
| `Sword_B/animation_controllers/coal_sword.json`<br>`$.animation_controllers.controller.animation.coal.states.coal.on_entry[13]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/creeper_sword.json`<br>`$.animation_controllers.controller.animation.creeper.states.default.on_entry[0]` | on_entry | `scoreboard` | `/scoreboard objectives add c dummy` |
| `Sword_B/animation_controllers/creeper_sword.json`<br>`$.animation_controllers.controller.animation.creeper.states.default.on_entry[1]` | on_entry | `scoreboard` | `/scoreboard players add @e[r=16] c 1` |
| `Sword_B/animation_controllers/creeper_sword.json`<br>`$.animation_controllers.controller.animation.creeper.states.default.on_entry[30]` | on_entry | `scoreboard` | `/execute @p[scores={c=300}] ~ ~ ~ scoreboard objectives remove c` |
| `Sword_B/animation_controllers/creeper_sword.json`<br>`$.animation_controllers.controller.animation.creeper.states.default.on_entry[31]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/creeper_sword.json`<br>`$.animation_controllers.controller.animation.creeper.states.creeper.on_entry[0]` | on_entry | `scoreboard` | `/scoreboard objectives add c dummy` |
| `Sword_B/animation_controllers/creeper_sword.json`<br>`$.animation_controllers.controller.animation.creeper.states.creeper.on_entry[1]` | on_entry | `scoreboard` | `/scoreboard players add @e[r=16] c 1` |
| `Sword_B/animation_controllers/creeper_sword.json`<br>`$.animation_controllers.controller.animation.creeper.states.creeper.on_entry[30]` | on_entry | `scoreboard` | `/execute @p[scores={c=300}] ~ ~ ~ scoreboard objectives remove c` |
| `Sword_B/animation_controllers/creeper_sword.json`<br>`$.animation_controllers.controller.animation.creeper.states.creeper.on_entry[31]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/emerald_sword.json`<br>`$.animation_controllers.controller.animation.emerald.states.default.on_entry[1]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/emerald_sword.json`<br>`$.animation_controllers.controller.animation.emerald.states.emerald.on_entry[1]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/ender_sword.json`<br>`$.animation_controllers.controller.animation.ender.states.default.on_entry[2]` | on_entry | `scoreboard` | `/scoreboard objectives add e dummy` |
| `Sword_B/animation_controllers/ender_sword.json`<br>`$.animation_controllers.controller.animation.ender.states.default.on_entry[3]` | on_entry | `scoreboard` | `/scoreboard players add @e[r=16] e 1` |
| `Sword_B/animation_controllers/ender_sword.json`<br>`$.animation_controllers.controller.animation.ender.states.default.on_entry[9]` | on_entry | `scoreboard` | `/execute @p[scores={e=700}] ~ ~ ~ scoreboard objectives remove e` |
| `Sword_B/animation_controllers/ender_sword.json`<br>`$.animation_controllers.controller.animation.ender.states.default.on_entry[10]` | on_entry | `scoreboard` | `/execute @p[scores={e=750}] ~ ~ ~ scoreboard objectives remove e` |
| `Sword_B/animation_controllers/ender_sword.json`<br>`$.animation_controllers.controller.animation.ender.states.default.on_entry[39]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/ender_sword.json`<br>`$.animation_controllers.controller.animation.ender.states.ender.on_entry[2]` | on_entry | `scoreboard` | `/scoreboard objectives add e dummy` |
| `Sword_B/animation_controllers/ender_sword.json`<br>`$.animation_controllers.controller.animation.ender.states.ender.on_entry[3]` | on_entry | `scoreboard` | `/scoreboard players add @e[r=16] e 1` |
| `Sword_B/animation_controllers/ender_sword.json`<br>`$.animation_controllers.controller.animation.ender.states.ender.on_entry[9]` | on_entry | `scoreboard` | `/execute @p[scores={e=700}] ~ ~ ~ scoreboard objectives remove e` |
| `Sword_B/animation_controllers/ender_sword.json`<br>`$.animation_controllers.controller.animation.ender.states.ender.on_entry[10]` | on_entry | `scoreboard` | `/execute @p[scores={e=750}] ~ ~ ~ scoreboard objectives remove e` |
| `Sword_B/animation_controllers/ender_sword.json`<br>`$.animation_controllers.controller.animation.ender.states.ender.on_entry[39]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/fire_sword.json`<br>`$.animation_controllers.controller.animation.fire.states.default.on_entry[38]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/fire_sword.json`<br>`$.animation_controllers.controller.animation.fire.states.fire.on_entry[38]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/glowstone_sword.json`<br>`$.animation_controllers.controller.animation.glow.states.default.on_entry[3]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/glowstone_sword.json`<br>`$.animation_controllers.controller.animation.glow.states.glow.on_entry[3]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/grass_sword.json`<br>`$.animation_controllers.controller.animation.grass.states.default.on_entry[3]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/grass_sword.json`<br>`$.animation_controllers.controller.animation.grass.states.grass.on_entry[3]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/ice_sword.json`<br>`$.animation_controllers.controller.animation.ice.states.ice.on_entry[16]` | on_entry | `tp` | `/execute @e[r=12,rm=5,type=slime] ~ ~ ~ detect ~ ~ ~ ice 0 tp @s ~ ~ ~` |
| `Sword_B/animation_controllers/ice_sword.json`<br>`$.animation_controllers.controller.animation.ice.states.ice.on_entry[25]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/jungle_sword.json`<br>`$.animation_controllers.controller.animation.jungle.states.jungle.on_entry[144]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/lapis_sword.json`<br>`$.animation_controllers.controller.animation.lapis.states.default.on_entry[0]` | on_entry | `scoreboard` | `/scoreboard objectives add l dummy` |
| `Sword_B/animation_controllers/lapis_sword.json`<br>`$.animation_controllers.controller.animation.lapis.states.default.on_entry[1]` | on_entry | `scoreboard` | `/scoreboard players add @p l 1` |
| `Sword_B/animation_controllers/lapis_sword.json`<br>`$.animation_controllers.controller.animation.lapis.states.default.on_entry[3]` | on_entry | `scoreboard` | `/execute @p[scores={l=30}] ~ ~ ~ scoreboard objectives remove l` |
| `Sword_B/animation_controllers/lapis_sword.json`<br>`$.animation_controllers.controller.animation.lapis.states.default.on_entry[4]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/lapis_sword.json`<br>`$.animation_controllers.controller.animation.lapis.states.lapis.on_entry[0]` | on_entry | `scoreboard` | `/scoreboard objectives add l dummy` |
| `Sword_B/animation_controllers/lapis_sword.json`<br>`$.animation_controllers.controller.animation.lapis.states.lapis.on_entry[1]` | on_entry | `scoreboard` | `/scoreboard players add @p l 1` |
| `Sword_B/animation_controllers/lapis_sword.json`<br>`$.animation_controllers.controller.animation.lapis.states.lapis.on_entry[3]` | on_entry | `scoreboard` | `/execute @p[scores={l=30}] ~ ~ ~ scoreboard objectives remove l` |
| `Sword_B/animation_controllers/lapis_sword.json`<br>`$.animation_controllers.controller.animation.lapis.states.lapis.on_entry[4]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/lightning sword.json`<br>`$.animation_controllers.controller.animation.lightning.states.default.on_entry[26]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/lightning sword.json`<br>`$.animation_controllers.controller.animation.lightning.states.lightning.on_entry[26]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/magma_sword.json`<br>`$.animation_controllers.controller.animation.magma.states.default.on_entry[23]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/magma_sword.json`<br>`$.animation_controllers.controller.animation.magma.states.magma.on_entry[23]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/obsidian_sword.json`<br>`$.animation_controllers.controller.animation.ob.states.default.on_entry[12]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/obsidian_sword.json`<br>`$.animation_controllers.controller.animation.ob.states.ob.on_entry[12]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/sea_sword.json`<br>`$.animation_controllers.controller.animation.sea.states.default.on_entry[3]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/sea_sword.json`<br>`$.animation_controllers.controller.animation.sea.states.sea.on_entry[3]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/shulker_sword.json`<br>`$.animation_controllers.controller.animation.shulker.states.default.on_entry[1]` | on_entry | `tp` | `/execute @p ~ ~ ~ tp @e[type=entity:shulker2] ~ ~2.5 ~` |
| `Sword_B/animation_controllers/shulker_sword.json`<br>`$.animation_controllers.controller.animation.shulker.states.default.on_entry[2]` | on_entry | `scoreboard` | `/scoreboard objectives add sh dummy` |
| `Sword_B/animation_controllers/shulker_sword.json`<br>`$.animation_controllers.controller.animation.shulker.states.default.on_entry[3]` | on_entry | `scoreboard` | `/scoreboard players add @p sh 1` |
| `Sword_B/animation_controllers/shulker_sword.json`<br>`$.animation_controllers.controller.animation.shulker.states.default.on_entry[5]` | on_entry | `scoreboard` | `/execute @p[scores={sh=2400}] ~ ~ ~ scoreboard objectives remove sh` |
| `Sword_B/animation_controllers/shulker_sword.json`<br>`$.animation_controllers.controller.animation.shulker.states.default.on_entry[6]` | on_entry | `kill` | `/execute @p[scores={sh=2390}] ~ ~ ~ kill @e[type=entity:shulker2,r=5] ~ 0 ~` |
| `Sword_B/animation_controllers/shulker_sword.json`<br>`$.animation_controllers.controller.animation.shulker.states.default.on_entry[7]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/shulker_sword.json`<br>`$.animation_controllers.controller.animation.shulker.states.shulker.on_entry[1]` | on_entry | `tp` | `/execute @p ~ ~ ~ tp @e[type=entity:shulker2] ~ ~2.5 ~` |
| `Sword_B/animation_controllers/shulker_sword.json`<br>`$.animation_controllers.controller.animation.shulker.states.shulker.on_entry[2]` | on_entry | `scoreboard` | `/scoreboard objectives add sh dummy` |
| `Sword_B/animation_controllers/shulker_sword.json`<br>`$.animation_controllers.controller.animation.shulker.states.shulker.on_entry[3]` | on_entry | `scoreboard` | `/scoreboard players add @p sh 1` |
| `Sword_B/animation_controllers/shulker_sword.json`<br>`$.animation_controllers.controller.animation.shulker.states.shulker.on_entry[5]` | on_entry | `scoreboard` | `/execute @p[scores={sh=2400}] ~ ~ ~ scoreboard objectives remove sh` |
| `Sword_B/animation_controllers/shulker_sword.json`<br>`$.animation_controllers.controller.animation.shulker.states.shulker.on_entry[6]` | on_entry | `kill` | `/execute @p[scores={sh=2390}] ~ ~ ~ kill @e[type=entity:shulker2,r=5] ~ 0 ~` |
| `Sword_B/animation_controllers/shulker_sword.json`<br>`$.animation_controllers.controller.animation.shulker.states.shulker.on_entry[7]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/slime_sword.json`<br>`$.animation_controllers.controller.animation.slime.states.default.on_entry[0]` | on_entry | `scoreboard` | `/scoreboard objectives add s dummy` |
| `Sword_B/animation_controllers/slime_sword.json`<br>`$.animation_controllers.controller.animation.slime.states.default.on_entry[1]` | on_entry | `scoreboard` | `/scoreboard players add @p s 1` |
| `Sword_B/animation_controllers/slime_sword.json`<br>`$.animation_controllers.controller.animation.slime.states.default.on_entry[4]` | on_entry | `scoreboard` | `/execute @p[scores={s=600}] ~ ~ ~ scoreboard objectives remove s` |
| `Sword_B/animation_controllers/slime_sword.json`<br>`$.animation_controllers.controller.animation.slime.states.default.on_entry[5]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/slime_sword.json`<br>`$.animation_controllers.controller.animation.slime.states.slime.on_entry[0]` | on_entry | `scoreboard` | `/scoreboard objectives add s dummy` |
| `Sword_B/animation_controllers/slime_sword.json`<br>`$.animation_controllers.controller.animation.slime.states.slime.on_entry[1]` | on_entry | `scoreboard` | `/scoreboard players add @p s 1` |
| `Sword_B/animation_controllers/slime_sword.json`<br>`$.animation_controllers.controller.animation.slime.states.slime.on_entry[4]` | on_entry | `scoreboard` | `/execute @p[scores={s=600}] ~ ~ ~ scoreboard objectives remove s` |
| `Sword_B/animation_controllers/slime_sword.json`<br>`$.animation_controllers.controller.animation.slime.states.slime.on_entry[5]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/spectral_sword.json`<br>`$.animation_controllers.controller.animation.spectral.states.default.on_entry[7]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/spectral_sword.json`<br>`$.animation_controllers.controller.animation.spectral.states.spectral.on_entry[7]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/spider_sword.json`<br>`$.animation_controllers.controller.animation.spider.states.default.on_entry[30]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/spider_sword.json`<br>`$.animation_controllers.controller.animation.spider.states.spider.on_entry[30]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/sponge_sword.json`<br>`$.animation_controllers.controller.animation.sponge.states.default.on_entry[12]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/sponge_sword.json`<br>`$.animation_controllers.controller.animation.sponge.states.sponge.on_entry[12]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/sword of time.json`<br>`$.animation_controllers.controller.animation.time.states.default.on_entry[0]` | on_entry | `gamerule` | `/gamerule randomtickspeed 300` |
| `Sword_B/animation_controllers/sword of time.json`<br>`$.animation_controllers.controller.animation.time.states.default.on_entry[2]` | on_entry | `time` | `/time add 30` |
| `Sword_B/animation_controllers/sword of time.json`<br>`$.animation_controllers.controller.animation.time.states.default.on_entry[3]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/sword of time.json`<br>`$.animation_controllers.controller.animation.time.states.time.on_entry[0]` | on_entry | `gamerule` | `/gamerule randomtickspeed 300` |
| `Sword_B/animation_controllers/sword of time.json`<br>`$.animation_controllers.controller.animation.time.states.time.on_entry[2]` | on_entry | `time` | `/time add 30` |
| `Sword_B/animation_controllers/sword of time.json`<br>`$.animation_controllers.controller.animation.time.states.time.on_entry[3]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/tnt_sword.json`<br>`$.animation_controllers.controller.animation.tnt.states.default.on_entry[26]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/tnt_sword.json`<br>`$.animation_controllers.controller.animation.tnt.states.tnt.on_entry[26]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/animation_controllers/wither_sword.json`<br>`$.animation_controllers.controller.animation.wither.states.wither.on_entry[12]` | on_entry | `scoreboard` | `/scoreboard objectives add w dummy` |
| `Sword_B/animation_controllers/wither_sword.json`<br>`$.animation_controllers.controller.animation.wither.states.wither.on_entry[13]` | on_entry | `scoreboard` | `/scoreboard players add @e[r=16,type=!cow,type=!pig,type=!sheep,type=!horse,type=!rabbit,type=!villager,type=!wolf,type=!cat,type=!fox,type=!chicken] w 1` |
| `Sword_B/animation_controllers/wither_sword.json`<br>`$.animation_controllers.controller.animation.wither.states.wither.on_entry[44]` | on_entry | `scoreboard` | `/execute @p[scores={w=600}] ~ ~ ~ scoreboard objectives remove w` |
| `Sword_B/animation_controllers/wither_sword.json`<br>`$.animation_controllers.controller.animation.wither.states.wither.on_entry[45]` | on_entry | `scoreboard` | `/scoreboard players set @a swords 2` |
| `Sword_B/functions/normal.mcfunction`<br>`line:2` | mcfunction | `gamerule` | `gamerule commandblockoutput false` |
| `Sword_B/functions/normal.mcfunction`<br>`line:3` | mcfunction | `gamerule` | `gamerule sendcommandfeedback false` |
| `Sword_B/functions/normal.mcfunction`<br>`line:5` | mcfunction | `tp` | `tp @e[r=4,type=entity:blaze2] ~ 0 ~` |
| `Sword_B/functions/normal.mcfunction`<br>`line:6` | mcfunction | `tp` | `tp @e[r=4,type=entity:bone2] ~ 0 ~` |
| `Sword_B/functions/normal.mcfunction`<br>`line:7` | mcfunction | `scoreboard` | `execute @p[r=2] ~ ~ ~ scoreboard objectives remove b` |
| `Sword_B/functions/normal.mcfunction`<br>`line:8` | mcfunction | `scoreboard` | `execute @p[r=2] ~ ~ ~ scoreboard objectives remove bn` |
| `Sword_B/functions/normal.mcfunction`<br>`line:9` | mcfunction | `scoreboard` | `execute @p[r=2] ~ ~ ~ scoreboard objectives remove sh` |
| `Sword_B/functions/normal.mcfunction`<br>`line:17` | mcfunction | `tp` | `tp @e[r=4,type=entity:shulker2] ~ 0 ~` |
| `Sword_B/functions/normal.mcfunction`<br>`line:18` | mcfunction | `scoreboard` | `execute @p[r=2] ~ ~ ~ scoreboard objectives remove s` |
| `Sword_B/functions/normal.mcfunction`<br>`line:19` | mcfunction | `gamerule` | `gamerule randomtickspeed 1` |
| `Sword_B/functions/normalft.mcfunction`<br>`line:1` | mcfunction | `scoreboard` | `scoreboard objectives add swords dummy` |
| `Sword_B/functions/normalft.mcfunction`<br>`line:2` | mcfunction | `scoreboard` | `scoreboard players remove @a[scores={swords=1}] swords 1` |
| `Sword_B/functions/normalft.mcfunction`<br>`line:3` | mcfunction | `scoreboard` | `scoreboard players remove @a[scores={swords=2}] swords 1` |
