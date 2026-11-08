# Выбранные побочные команды: буквальные кандидаты — 2.8.14

Из 945 строк следующих источников выделено **69** строк, содержащих одно или более ключевых слов: `gamerule, scoreboard, time, weather, kill, damage, tp, teleport, ride, replaceitem, clear, tickingarea`. Область поиска: `run_command.command`, строковые `on_entry`/`on_exit` в разобранных behavior JSON и непустые, не начинающиеся с `#` строки behavior mcfunction. Дубли из разных состояний и повторённые строки сохранены; номера/пути позволяют видеть порядок в конкретном списке.

Это **лексический поиск**, не парсер команд и не подтверждение действия. Совпадение слова может находиться в аргументе или вложенном execute, а условие, адресат, область и разрешение `@s` зависят от контекста. `target` показан только явно записанный рядом с `run_command`; отсутствие не превращается в self. Состояния `on_entry`/`on_exit` могут содержать не только команды. Отдельные метки могут пересекаться, поэтому их количества нельзя складывать как число строк.

Вне поиска: JS, строки команд в других полях, неразобранные JSON, внешние/ванильные вызовы, интерпретация `/function`, `fill`, `setblock`, `summon`, структуры и действия компонентов. Например, изменение мира может происходить и без команд из этого списка. Для обычных вызовов и полных условий сверять [реестр сущностей](entity-ledger-2.8.14.md), [контроллеры](animation-ledger-2.8.14.md), [предметы](items-2.8.14.md) и исходный архив.

Метки по числу **строк**, а не исполнений: `gamerule` — 6, `scoreboard` — 9, `time` — 4, `weather` — 0, `kill` — 20, `damage` — 9, `tp` — 7, `teleport` — 0, `ride` — 11, `replaceitem` — 3, `clear` — 0, `tickingarea` — 0.

- Неразобранные JSON: `Swords_B/entities/creeper.json` (<string>:430 Unexpected "}" at column 3).
- Повторные ключи: `Swords_B/entities/living_flame.json`: `minecraft:fire_immune`; `Swords_B/entities/mountable_slime.json`: `despawn`; `Swords_B/entities/slime_king.json`: `minecraft:movement.jump`. JSON5 сохраняет последнее значение.

Сопоставление выбранных строк с [2.8.8](command-risk-index-2.8.8.md): один путь содержит различающийся аргумент блока в Ice teleport (`effect99:fake_ice` / `frosted_ice`); остальные найденные кандидаты совпадают. Это не сравнение остальных команд и файлов.

| Файл / путь | Источник / target | Метки | Исходная строка |
|---|---|---|---|
| `Swords_B/animation_controllers/wither_sword.json`<br>`$.animation_controllers.controller.animation.wither_sword.states.wither_sword.on_entry[0]` | on_entry | `ride` | `/ride @s summon_rider entity:name minecraft:wither_sword` |
| `Swords_B/entities/bee_entity.json`<br>`$.minecraft:entity.events.despawn.run_command.command[0]` | run_command; target не указан | `tp` | `tp @s ~ -103 ~` |
| `Swords_B/entities/ender_crystal.json`<br>`$.minecraft:entity.events.ride_player.run_command.command[0]` | run_command; target не указан | `ride` | `ride @s start_riding @p[family=spectral_sword,r=3] teleport_rider` |
| `Swords_B/entities/grass.json`<br>`$.minecraft:entity.events.grass_sword_skill.run_command.command[1]` | run_command; target не указан | `tp` | `execute @e[type=!entity:grass,c=1,r=1,tag=grass] ~ ~ ~ detect ~ ~-1 ~ grass 0 execute @s ~ ~ ~ detect ~ ~ ~ air 0 tp @s ~ ~-1 ~` |
| `Swords_B/entities/grass.json`<br>`$.minecraft:entity.events.grass_sword_skill.run_command.command[2]` | run_command; target не указан | `tp` | `execute @e[type=!entity:grass,c=1,r=1,tag=grass] ~ ~ ~ detect ~ ~-1 ~ grass 0 execute @s ~ ~ ~ detect ~ ~ ~ tallgrass 0 tp @s ~ ~-1 ~` |
| `Swords_B/entities/item.json`<br>`$.minecraft:entity.events.wet_sponge_sword.run_command.command[1]` | run_command; target не указан | `kill` | `kill @s` |
| `Swords_B/entities/item.json`<br>`$.minecraft:entity.events.wish_1.randomize[0].run_command.command[1]` | run_command; target не указан | `kill` | `kill @s` |
| `Swords_B/entities/item.json`<br>`$.minecraft:entity.events.wish_1.randomize[1].run_command.command[5]` | run_command; target не указан | `kill` | `kill @s` |
| `Swords_B/entities/item.json`<br>`$.minecraft:entity.events.wish_2.randomize[0].run_command.command[1]` | run_command; target не указан | `kill` | `kill @s` |
| `Swords_B/entities/item.json`<br>`$.minecraft:entity.events.wish_2.randomize[1].run_command.command[5]` | run_command; target не указан | `kill` | `kill @s` |
| `Swords_B/entities/item.json`<br>`$.minecraft:entity.events.wish_3.randomize[0].run_command.command[1]` | run_command; target не указан | `time` | `time add 1000` |
| `Swords_B/entities/item.json`<br>`$.minecraft:entity.events.wish_3.randomize[0].run_command.command[3]` | run_command; target не указан | `kill` | `kill @s` |
| `Swords_B/entities/item.json`<br>`$.minecraft:entity.events.wish_3.randomize[1].run_command.command[1]` | run_command; target не указан | `time` | `time add 6000` |
| `Swords_B/entities/item.json`<br>`$.minecraft:entity.events.wish_3.randomize[1].run_command.command[5]` | run_command; target не указан | `kill` | `kill @s` |
| `Swords_B/entities/item.json`<br>`$.minecraft:entity.events.respawn_event_1.run_command.command[1]` | run_command; target не указан | `kill` | `kill @s` |
| `Swords_B/entities/item.json`<br>`$.minecraft:entity.events.respawn_event_2.run_command.command[1]` | run_command; target не указан | `kill` | `kill @s` |
| `Swords_B/entities/item.json`<br>`$.minecraft:entity.events.despawn_event_1.run_command.command[2]` | run_command; target не указан | `kill` | `kill @s` |
| `Swords_B/entities/item.json`<br>`$.minecraft:entity.events.despawn_event_2.run_command.command[2]` | run_command; target не указан | `kill` | `kill @s` |
| `Swords_B/entities/item.json`<br>`$.minecraft:entity.events.despawn_event_4.sequence[0].run_command.command[5]` | run_command; target не указан | `kill` | `kill @s` |
| `Swords_B/entities/item.json`<br>`$.minecraft:entity.events.despawn_event_4.sequence[1].run_command.command[2]` | run_command; target не указан | `kill` | `kill @s` |
| `Swords_B/entities/item.json`<br>`$.minecraft:entity.events.despawn_event_5.run_command.command[1]` | run_command; target не указан | `kill` | `kill @s` |
| `Swords_B/entities/item.json`<br>`$.minecraft:entity.events.despawn_event_6.run_command.command[1]` | run_command; target не указан | `kill` | `kill @s` |
| `Swords_B/entities/item.json`<br>`$.minecraft:entity.events.fire_sword_event_1.run_command.command[2]` | run_command; target не указан | `kill` | `kill @s` |
| `Swords_B/entities/item.json`<br>`$.minecraft:entity.events.fire_sword_event_2.run_command.command[3]` | run_command; target не указан | `kill` | `kill @s` |
| `Swords_B/entities/item.json`<br>`$.minecraft:entity.events.fire_sword_event_3.sequence[0].run_command.command[15]` | run_command; target не указан | `kill` | `kill @s` |
| `Swords_B/entities/mountable_slime.json`<br>`$.minecraft:entity.events.slime_events.run_command.command[2]` | run_command; target не указан | `tp` | `tp @s[scores={slime_despawn=0}] @e[type=player,family=slime_sword,c=1,rm=8,r=12]` |
| `Swords_B/entities/mountable_slime.json`<br>`$.minecraft:entity.events.slime_events.run_command.command[3]` | run_command; target не указан | `scoreboard` | `scoreboard players add @s slime_despawn 1` |
| `Swords_B/entities/objective.json`<br>`$.minecraft:entity.events.follow_entity.run_command.command[0]` | run_command; target не указан | `tp` | `tp @s @e[r=8,c=1,type=!player,type=!item,family=!parrot_tame,family=!tamed,type=!arrow,type=!xp_orb,family=!effect99_entities]` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.events.minecraft:constant_events.sequence[0].run_command.command[1]` | run_command; target не указан | `gamerule` | `gamerule sendcommandfeedback false` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.events.minecraft:constant_events.sequence[0].run_command.command[2]` | run_command; target не указан | `gamerule` | `gamerule commandblockoutput false` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.events.minecraft:constant_events.sequence[0].run_command.command[3]` | run_command; target не указан | `scoreboard` | `scoreboard objectives add Effect99 dummy` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.events.minecraft:constant_events.sequence[0].run_command.command[4]` | run_command; target не указан | `scoreboard` | `scoreboard players add @s Effect99 1` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.events.minecraft:constant_events.sequence[0].run_command.command[6]` | run_command; target не указан | `scoreboard` | `scoreboard players set @s[scores={Effect99=36001}] Effect99 1` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.events.minecraft:stop_sword_events.sequence[0].run_command.command[0]` | run_command; target не указан | `tp` | `execute @e[r=64,type=!player] ~ ~ ~ detect ~ ~ ~ ice 0 tp @s ~ ~ ~` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.events.minecraft:stop_sword_events.sequence[4].run_command.command[0]` | run_command; target не указан | `ride` | `ride @e[type=entity:mountable_slime,r=1,y=~-1] evict_riders` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.events.minecraft:clock_sword.sequence[1].run_command.command[0]` | run_command; target не указан | `gamerule` | `gamerule randomtickspeed 100` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.events.minecraft:clock_sword.sequence[1].run_command.command[2]` | run_command; target не указан | `time` | `time add 10` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.events.stop_clock_sword_event.sequence[0].run_command.command[0]` | run_command; target не указан | `gamerule` | `gamerule randomtickspeed 1` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.events.stop_wither_sword_event.sequence[0].run_command.command[1]` | run_command; target не указан | `ride` | `ride @s evict_riders` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.events.minecraft:time_sword.sequence[1].run_command.command[0]` | run_command; target не указан | `gamerule` | `gamerule randomtickspeed 300` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.events.minecraft:time_sword.sequence[1].run_command.command[2]` | run_command; target не указан | `time` | `time add 30` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.events.stop_time_sword_event.sequence[0].run_command.command[0]` | run_command; target не указан | `gamerule` | `gamerule randomtickspeed 1` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.events.minecraft:sponge_sword.sequence[0].run_command.command[0]` | run_command; target не указан | `scoreboard` | `scoreboard objectives add sponge_sword dummy` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.events.minecraft:sponge_sword.sequence[1].run_command.command[3]` | run_command; target не указан | `scoreboard` | `scoreboard players add @s sponge_sword 1` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.events.wet_sponge_sword.sequence[0].run_command.command[0]` | run_command; target не указан | `replaceitem` | `replaceitem entity @s slot.weapon.mainhand 0 effect:wet_sponge_sword 1` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.events.wet_sponge_sword.sequence[0].run_command.command[1]` | run_command; target не указан | `scoreboard` | `scoreboard players set @s sponge_sword 0` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.events.minecraft:spider_sword.sequence[0].run_command.command[0]` | run_command; target не указан | `ride` | `ride @s summon_ride minecraft:spider no_ride_change minecraft:spider_sword` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.events.stop_spider_sword_event.sequence[0].run_command.command[0]` | run_command; target не указан | `ride` | `ride @s stop_riding` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.events.stop_shulker_sword_event.sequence[0].run_command.command[0]` | run_command; target не указан | `ride` | `ride @s stop_riding` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.events.shulker_sword_skill.run_command.command[0]` | run_command; target не указан | `ride` | `ride @s summon_ride entity:shulker_shield no_ride_change` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.events.minecraft:slime_sword.sequence[1].run_command.command[0]` | run_command; target не указан | `scoreboard` | `scoreboard players set @e[type=entity:mountable_slime,c=1,r=12] slime_despawn 0` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.events.stop_slime_sword_event.sequence[0].run_command.command[0]` | run_command; target не указан | `ride` | `ride @s stop_riding` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.events.slime_sword_skills.run_command.command[0]` | run_command; target не указан | `ride` | `ride @s summon_ride entity:mountable_slime no_ride_change` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.events.slime_sword_skills.run_command.command[1]` | run_command; target не указан | `scoreboard` | `scoreboard objectives add slime_despawn dummy` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.events.stop_spectral_sword_event.sequence[0].run_command.command[0]` | run_command; target не указан | `ride` | `ride @s evict_riders` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.events.minecraft:quartz_sword.sequence[0].run_command.command[0]` | run_command; target не указан | `damage` | `damage @s 14 magic` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.events.stop_quartz_sword_event.sequence[0].run_command.command[0]` | run_command; target не указан | `damage` | `damage @s 14 magic` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.events.minecraft:ice_sword.sequence[1].run_command.command[2]` | run_command; target не указан | `replaceitem` | `replaceitem entity @s slot.weapon.mainhand 0 air 1 0` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.events.minecraft:ice_sword.sequence[2].run_command.command[1]` | run_command; target не указан | `replaceitem` | `replaceitem entity @s slot.weapon.mainhand 0 air 1 0` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.events.minecraft:ice_sword.sequence[3].run_command.command[10]` | run_command; target не указан | `tp` | `execute @e[r=64,type=!player] ~ ~ ~ detect ~ ~ ~ frosted_ice 0 tp @s ~ ~ ~ ~1` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.events.start_player_explode.run_command.command[1]` | run_command; target не указан | `kill` | `kill @s` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.events.cactus_sword_skills.run_command.command[0]` | run_command; target не указан | `damage` | `damage @e[r=1.4,type=!player] 1 contact entity @s` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.events.cactus_sword_skills.run_command.command[1]` | run_command; target не указан | `damage` | `damage @s 1 contact` |
| `Swords_B/entities/slime_king.json`<br>`$.minecraft:entity.events.slime_effects.run_command.command[1]` | run_command; target не указан | `damage` | `damage @p[r=1.8] 4 magic` |
| `Swords_B/entities/slime_king.json`<br>`$.minecraft:entity.events.slime_effects.run_command.command[2]` | run_command; target не указан | `damage` | `damage @e[r=1.5,family=!slime_king] 2 magic` |
| `Swords_B/entities/ultra_instinct_projectile.json`<br>`$.minecraft:entity.events.projectile_particle.run_command.command[1]` | run_command; target не указан | `kill` | `kill @e[type=item,r=24]` |
| `Swords_B/items/quartz_diamond_stick.json`<br>`$.minecraft:item.events.weapon.randomize[0].run_command.command[0]` | run_command; target не указан | `damage` | `damage @s 1 magic` |
| `Swords_B/items/quartz_diamond_stick.json`<br>`$.minecraft:item.events.weapon.randomize[1].run_command.command[0]` | run_command; target не указан | `damage` | `damage @s 3 magic` |
| `Swords_B/items/quartz_diamond_stick.json`<br>`$.minecraft:item.events.weapon.randomize[2].run_command.command[0]` | run_command; target не указан | `damage` | `damage @s 6 magic` |
