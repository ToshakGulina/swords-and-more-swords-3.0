# Эффекты: команды и выбранные компоненты — 2.8.8 и 2.8.14

Лексический поиск во всех текстовых `.json`, `.mcfunction`, `.js` behavior pack: 60 исходных строк с буквальным `effect` и selector `@…`, 69 распознанных вхождений. Исходные строки сохранены целиком с номерами, даже если один JSON-ряд содержит несколько команд; сохраняются повторы разных состояний. Строка может быть комментарием или недостижимой ветвью. Это не парсер команд и не подтверждение исполнения. Выборка не включает команды с другим синтаксисом, динамически составленные строки, ресурсы извне, ванильные функции или эффекты, приходящие по косвенным цепям.

Селекторы, фильтры, нули, порядок и числовые аргументы приведены буквально. Не переводить duration/amplifier в секунды или уровни без учёта конкретной формы и версии; `0` не приравнивается автоматически к одному и тому же действию во всех контекстах. Необъявленный target не следует считать self. Имена ниже — лишь разбор подстроки, не гарантированный effect ID или цель.

Вхождения имён после selector: `absorption` — 2, `blindness` — 4, `conduit_power` — 3, `fire_resistance` — 4, `hunger` — 1, `instant_damage` — 9, `instant_health` — 1, `jump_boost` — 3, `levitation` — 11, `mining_fatigue` — 1, `nausea` — 7, `regeneration` — 2, `resistance` — 3, `saturation` — 1, `slow_falling` — 5, `slowness` — 2, `speed` — 4, `village_hero` — 2, `weakness` — 1, `wither` — 3.

Отдельно среди разобранных JSON извлечены **20** структурных объектов: `arrow_effect` — 6, `minecraft:attack` — 3, `minecraft:healable` — 1, `minecraft:spell_effects` — 3, `mob_effect` — 7. Включены `minecraft:spell_effects`, `minecraft:attack` с `effect_name`/`effect_duration`, `minecraft:healable` с `items[].effects`, а также `mob_effect` и `arrow_effect`. Пустой `arrow_effect` не означает отсутствие стрелочных эффектов: обработка остаётся за движком. Списки, значения и вложенные фильтры сохранены целиком.

- Неразобранные JSON: `Swords_B/entities/creeper.json` (<string>:430 Unexpected "}" at column 3). Исходные строки с командами ищутся и в них, но структурные объекты этих файлов исключены.
- Повторные ключи в разобранных файлах: `Swords_B/entities/living_flame.json`: `minecraft:fire_immune`; `Swords_B/entities/mountable_slime.json`: `despawn`; `Swords_B/entities/slime_king.json`: `minecraft:movement.jump`. JSON5 сохраняет последнее значение; подлинник остаётся эталоном.
- Вхождения не соответствующие ограниченному шаблону извлечения имени: нет.

В выбранных строках команд и структурных объектах обеих 2.x совпадают пути, номера строк и значения; это не сравнение всех остальных частей файлов.

## Исходные строки с командами

| Файл и строка | Распознанные имена | Исходная строка целиком |
|---|---|---|
| `Swords_B/animation_controllers/climb_spider.json:15` | `levitation` | `"            \"/effect @s levitation 10 3 true\""` |
| `Swords_B/animation_controllers/ghost_sword.json:18` | `levitation` | `"            \"/effect @s levitation 1 3 true\""` |
| `Swords_B/animation_controllers/ghost_sword.json:28` | `levitation` | `"            \"/effect @s levitation 0 0\""` |
| `Swords_B/blocks/quartz_diamond_block.json:28` | `instant_damage` | `"        \"run_command\": { \"command\": [ \"particle minecraft:knockback_roar_particle ~ ~1 ~\", \"effect @p[r=6] instant_damage 1 0 true\" ] "` |
| `Swords_B/blocks/quartz_diamond_ore.json:25` | `instant_damage` | `"          \"particle minecraft:knockback_roar_particle ~ ~1 ~\", \"effect @p[r=6] instant_damage 1 0 true\""` |
| `Swords_B/entities/alpha_wolf.json:231` | `resistance` | `"            \"effect @s resistance 20 2 true\","` |
| `Swords_B/entities/alpha_wolf.json:232` | `regeneration` | `"            \"effect @s regeneration 20 2 true\""` |
| `Swords_B/entities/alpha_wolf.json:244` | `resistance` | `"            \"effect @s resistance 0\","` |
| `Swords_B/entities/alpha_wolf.json:245` | `regeneration` | `"            \"effect @s regeneration 0\""` |
| `Swords_B/entities/centella.json:83` | `instant_damage` | `"             \"effect @e[family=!effect99_entities,r=2] instant_damage 1 0 true\","` |
| `Swords_B/entities/centella.json:84` | `slow_falling` | `"             \"effect @s slow_falling 10 0 true\","` |
| `Swords_B/entities/grass.json:37` | `slowness` | `"                \"effect @e[type=!entity:grass,r=1] slowness 2 15 true\","` |
| `Swords_B/entities/mountable_slime.json:199` | `instant_damage`, `instant_health` | `"          \"command\": [ \"effect @e[r=1,family=!slime_sword,family=!undead] instant_damage 1 1 true\", \"effect @e[r=1,family=undead] instant_health 3 1 true\", \"event entity @s not_baby\" ] "` |
| `Swords_B/entities/mountable_slime.json:212` | `jump_boost` | `"            \"effect @s jump_boost 1 2 true\", "` |
| `Swords_B/entities/player.json:1190` | `speed` | `"                \"effect @e[type=!player] speed 1 10 true\", "` |
| `Swords_B/entities/player.json:1203` | `speed` | `"          \"run_command\": { \"command\": [ \"gamerule randomtickspeed 1\", \"effect @e[type=!player] speed 0 0\", \"event entity @a[family=default_player] default_player\" ] },"` |
| `Swords_B/entities/player.json:1233` | `slow_falling`, `saturation` | `"            \"run_command\": { \"command\": [ \"effect @s slow_falling 1 0 true\", \"effect @s saturation 1 1 true\" ] },"` |
| `Swords_B/entities/player.json:1238` | `levitation` | `"            \"run_command\": { \"command\": [ \"effect @s levitation 1 0 true\" ] }"` |
| `Swords_B/entities/player.json:1242` | `levitation`, `fire_resistance` | `"            \"run_command\": { \"command\": [ \"effect @s levitation 1 0 true\", \"effect @s fire_resistance 1 0 true\" ] }"` |
| `Swords_B/entities/player.json:1246` | `fire_resistance` | `"            \"run_command\": { \"command\": [ \"effect @s fire_resistance 0 0\" ] }"` |
| `Swords_B/entities/player.json:1268` | `slow_falling` | `"               \"effect @s slow_falling 0 0\", "` |
| `Swords_B/entities/player.json:1288` | `nausea`, `blindness`, `nausea` | `"            \"run_command\": { \"command\": [ \"effect @s nausea 0 0\", \"effect @s blindness 0 0\", \"effect @s nausea 0 0\" ] }"` |
| `Swords_B/entities/player.json:1297` | `nausea` | `"          \"run_command\": { \"command\": [ \"effect @s nausea 0 0\" ] },"` |
| `Swords_B/entities/player.json:1303` | `nausea`, `blindness` | `"            \"run_command\": { \"command\": [ \"effect @s nausea 9999 0 true\", \"effect @s blindness 9999 0 true\" ] },"` |
| `Swords_B/entities/player.json:1317` | `nausea` | `"      \"starting_wolf_transformation\": { \"run_command\": { \"command\": [ \"effect @s nausea 5 0 true\" ] }"` |
| `Swords_B/entities/player.json:1352` | `nausea`, `blindness` | `"            \"run_command\": { \"command\": [ \"effect @s nausea 0 0\", \"effect @s blindness 0 0\", \"stopsound @a wolf_sword.howl\", \"stopsound @a wolf_sword.distant_howl\" ] }"` |
| `Swords_B/entities/player.json:1372` | `hunger` | `"              \"effect @s hunger 0 0\","` |
| `Swords_B/entities/player.json:1373` | `blindness` | `"              \"effect @s blindness 0 0\","` |
| `Swords_B/entities/player.json:1374` | `slowness` | `"              \"effect @s slowness 0 0\","` |
| `Swords_B/entities/player.json:1375` | `weakness` | `"              \"effect @s weakness 0 0\","` |
| `Swords_B/entities/player.json:1376` | `mining_fatigue` | `"              \"effect @s mining_fatigue 0 0\","` |
| `Swords_B/entities/player.json:1377` | `nausea` | `"              \"effect @s nausea 0 0\","` |
| `Swords_B/entities/player.json:1378` | `instant_damage` | `"              \"effect @s instant_damage 0 0\","` |
| `Swords_B/entities/player.json:1379` | `wither` | `"              \"effect @s wither 0 0\" ] "` |
| `Swords_B/entities/player.json:1513` | `wither` | `"                \"effect @s wither 39960 1 true\","` |
| `Swords_B/entities/player.json:1527` | `wither` | `"          \"run_command\": { \"command\": [ \"effect @s wither 0 0\", \"ride @s evict_riders\" ] }"` |
| `Swords_B/entities/player.json:1543` | `speed` | `"            \"run_command\": { \"command\": [ \"gamerule randomtickspeed 300\", \"effect @e[type=!player] speed 1 15 true\", \"time add 30\", \"event entity @a[family=default_player] time_sword_movement\", \"fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace air\", \"fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace effect99:lightblock2\" ] }"` |
| `Swords_B/entities/player.json:1553` | `speed` | `"          \"run_command\": { \"command\": [ \"gamerule randomtickspeed 1\", \"effect @e[type=!player] speed 0 0\", \"event entity @a[family=default_player] default_player\" ] }"` |
| `Swords_B/entities/player.json:1651` | `levitation` | `"            \"run_command\": { \"command\": [ \"effect @s levitation 0 0\" ] }"` |
| `Swords_B/entities/player.json:1830` | `conduit_power` | `"            \"run_command\": { \"command\": [ \"camerashake add @s 0.01 1 positional\", \"effect @s conduit_power 0 0\" ] }"` |
| `Swords_B/entities/player.json:1840` | `conduit_power` | `"            \"run_command\": { \"command\": [ \"effect @s conduit_power 1 0 true\" ] }"` |
| `Swords_B/entities/player.json:1850` | `conduit_power` | `"          \"run_command\": { \"command\": [ \"particle minecraft:example_bounce ~ ~ ~\", \"playsound random.splash @a[r=12] ~ ~ ~ 0.5\", \"effect @s conduit_power 0 0\" ] }"` |
| `Swords_B/entities/player.json:2008` | `absorption` | `"            \"run_command\": { \"command\": [ \"effect @s absorption 1 2 true\", \"function commands/swords_and_more_swords/swords_and_more_swords/jungle_sword\" ] }"` |
| `Swords_B/entities/player.json:2018` | `absorption` | `"          \"run_command\": { \"command\": [ \"effect @s absorption 0\" ] }"` |
| `Swords_B/entities/player.json:2094` | `village_hero`, `resistance` | `"            \"run_command\": { \"command\": [ \"effect @s village_hero 1 0 true\", \"effect @e[family=villager,r=64] resistance 1 1 true\" ] }"` |
| `Swords_B/entities/player.json:2102` | `village_hero` | `"          \"run_command\": { \"command\": [ \"effect @s village_hero 0 0 true\" ] },"` |
| `Swords_B/entities/player.json:2225` | `levitation` | `"            \"effect @s levitation 0 0 true\", "` |
| `Swords_B/entities/player.json:2226` | `slow_falling` | `"            \"effect @s slow_falling 0 0 true\""` |
| `Swords_B/entities/shulker_shield.json:41` | `levitation` | `"      \"shulker_shield_clear_effect\": { \"run_command\": { \"command\": [ \"effect @s levitation 0 0\" ] } },"` |
| `Swords_B/entities/shulker_shield.json:49` | `instant_damage` | `"      \"damage_player\": { \"run_command\": { \"command\": [ \"effect @p[r=1,family=shulker_sword] instant_damage 1 2 true\" ] } }"` |
| `Swords_B/entities/slime_king.json:163` | `jump_boost` | `"                \"run_command\": { \"command\": [ \"effect @s jump_boost 1 15 true\" ] }"` |
| `Swords_B/entities/slime_king.json:169` | `instant_damage`, `instant_damage` | `"      \"fall_damage\": { \"run_command\": { \"command\": [ \"effect @e[r=3,family=!slime_king] instant_damage 1 1 true\", \"effect @e[r=4,type=iron_golem] instant_damage 1 2 true\" ] }"` |
| `Swords_B/entities/slime_king.json:171` | `jump_boost` | `"      \"slime_effects\": { \"run_command\": { \"command\": [ \"effect @s jump_boost 1 0 true\", \"damage @p[r=1.8] 4 magic\", \"damage @e[r=1.5,family=!slime_king] 2 magic\" ] }"` |
| `Swords_B/entities/spider.json:411` | `levitation` | `"          \"command\": [ \"execute @s ~~~ detect ~0.8 ~ ~ air 0 execute @s ~~~ detect ~-0.8 ~ ~ air 0 execute @s ~~~ detect ~ ~ ~0.8 air 0 execute @s ~~~ detect ~ ~ ~-0.8 air 0 effect @s levitation 0 0 true\" ]"` |
| `Swords_B/items/blaze_sword.json:83` | `levitation` | `"            \"effect @s levitation 7 0 true\","` |
| `Swords_B/items/blaze_sword.json:84` | `slow_falling` | `"            \"effect @s slow_falling 10 3 true\""` |
| `Swords_B/items/blaze_sword.json:103` | `fire_resistance` | `"                    \"effect @s fire_resistance 1 0 true\""` |
| `Swords_B/items/blaze_sword.json:115` | `fire_resistance` | `"                    \"effect @s fire_resistance 1 0 true\""` |
| `Swords_B/items/quartz_sword.json:91` | `instant_damage` | `"                \"effect @a[r=1] instant_damage 1 99 true\","` |
| `Swords_B/items/shulker_sword.json:85` | `levitation` | `"            \"effect @e[r=6,family=!shulker_sword] levitation 1 18 false\""` |

## Структурные поля (все выбранные разобранные объекты)

| Файл / путь | Поле | Полный разобранный объект |
|---|---|---|
| `Swords_B/entities/arrow.json`<br>`$.minecraft:entity.component_groups.despawn_arrow.minecraft:projectile.on_hit.arrow_effect` | `arrow_effect` | `{}` |
| `Swords_B/entities/arrow.json`<br>`$.minecraft:entity.component_groups.minecraft:inertia_disable.minecraft:projectile.on_hit.arrow_effect` | `arrow_effect` | `{}` |
| `Swords_B/entities/arrow.json`<br>`$.minecraft:entity.component_groups.minecraft:hard_arrow.minecraft:projectile.on_hit.arrow_effect` | `arrow_effect` | `{}` |
| `Swords_B/entities/arrow.json`<br>`$.minecraft:entity.component_groups.minecraft:player_arrow.minecraft:projectile.on_hit.arrow_effect` | `arrow_effect` | `{}` |
| `Swords_B/entities/arrow.json`<br>`$.minecraft:entity.component_groups.minecraft:pillager_arrow.minecraft:projectile.on_hit.arrow_effect` | `arrow_effect` | `{}` |
| `Swords_B/entities/arrow.json`<br>`$.minecraft:entity.components.minecraft:projectile.on_hit.arrow_effect` | `arrow_effect` | `{}` |
| `Swords_B/entities/bee.json`<br>`$.minecraft:entity.component_groups.normal_attack.minecraft:attack` | `minecraft:attack` | `{"damage":2,"effect_name":"poison","effect_duration":10}` |
| `Swords_B/entities/bee.json`<br>`$.minecraft:entity.component_groups.hard_attack.minecraft:attack` | `minecraft:attack` | `{"damage":2,"effect_name":"poison","effect_duration":18}` |
| `Swords_B/entities/bee_entity.json`<br>`$.minecraft:entity.components.minecraft:attack` | `minecraft:attack` | `{"damage":1,"effect_name":"fatal_poison","effect_duration":3}` |
| `Swords_B/entities/parrot.json`<br>`$.minecraft:entity.components.minecraft:healable` | `minecraft:healable` | `{"force_use":true,"filters":{"test":"is_riding","operator":"!=","value":true},"items":[{"item":"cookie","heal_amount":0,"effects":[{"name":"fatal_poison","chance":1.0,"duration":1000,"amplifier":0}]}]}` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.component_groups.minecraft:add_bad_omen.minecraft:spell_effects` | `minecraft:spell_effects` | `{"add_effects":[{"effect":"bad_omen","duration":6000,"display_on_screen_animation":true}]}` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.component_groups.minecraft:clear_bad_omen_spell_effect.minecraft:spell_effects` | `minecraft:spell_effects` | `{}` |
| `Swords_B/entities/player.json`<br>`$.minecraft:entity.component_groups.minecraft:raid_trigger.minecraft:spell_effects` | `minecraft:spell_effects` | `{"remove_effects":"bad_omen"}` |
| `Swords_B/entities/shulker_bullet.json`<br>`$.minecraft:entity.component_groups.shulker_sword.minecraft:projectile.on_hit.mob_effect` | `mob_effect` | `{"effect":"levitation","durationeasy":200,"durationnormal":200,"durationhard":200,"amplifier":1}` |
| `Swords_B/entities/shulker_bullet.json`<br>`$.minecraft:entity.components.minecraft:projectile.on_hit.mob_effect` | `mob_effect` | `{"effect":"levitation","durationeasy":200,"durationnormal":200,"durationhard":200,"amplifier":1}` |
| `Swords_B/entities/wither_effect.json`<br>`$.minecraft:entity.components.minecraft:projectile.on_hit.mob_effect` | `mob_effect` | `{"effect":"wither","durationeasy":200,"durationnormal":200,"durationhard":200,"amplifier":0}` |
| `Swords_B/entities/wither_skull.json`<br>`$.minecraft:entity.component_groups.wither_sword.minecraft:projectile.on_hit.mob_effect` | `mob_effect` | `{"effect":"wither","durationeasy":0,"durationnormal":200,"durationhard":800,"amplifier":1}` |
| `Swords_B/entities/wither_skull.json`<br>`$.minecraft:entity.components.minecraft:projectile.on_hit.mob_effect` | `mob_effect` | `{"effect":"wither","durationeasy":0,"durationnormal":200,"durationhard":800,"amplifier":1}` |
| `Swords_B/entities/wither_skull_dangerous.json`<br>`$.minecraft:entity.component_groups.wither_sword.minecraft:projectile.on_hit.mob_effect` | `mob_effect` | `{"effect":"wither","durationeasy":0,"durationnormal":200,"durationhard":800,"amplifier":1}` |
| `Swords_B/entities/wither_skull_dangerous.json`<br>`$.minecraft:entity.components.minecraft:projectile.on_hit.mob_effect` | `mob_effect` | `{"effect":"wither","durationeasy":0,"durationnormal":200,"durationhard":800,"amplifier":1}` |

Контекст событий, включение групп и полные списки команд: [реестр сущностей](entity-ledger-2.8.14.md), [projectile](projectile-component-index.md), [weapon-хуки](weapon-event-index.md), [команды](command-risk-index-2.8.14.md).
