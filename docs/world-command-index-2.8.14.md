# Команды изменения мира и создания loot: исходные строки — 2.8.14

Лексический поиск по всем `.json`, `.mcfunction`, `.js` behavior pack: **330 исходных строк**, содержащих `fill`, `setblock`, `clone`, `structure load` или `loot spawn`. Сохранены точные строки, отступы, номера, порядок файла и повторы; строка может содержать несколько команд и несколько меток. Отсортировано по пути и номеру, а не по времени исполнения.

Это **кандидаты по тексту**, не Bedrock-парсер или доказательство вызова, применимости синтаксиса и изменений мира. Комментарии, неразобранные JSON, строковые данные и шаблоны JS включены; координаты, selector, detect, replace, порядок в sequence, случайные фильтры и исполнитель сохраняются в исходном тексте, но здесь не вычисляются. Вне области: другие команды, функции из других пакетов, block components, взрывы, вызовы `summon`/`event entity`, автоматические механизмы и косвенные эффекты. Показан только найденный текст, а не число затронутых блоков.

Метки по числу строк (не вхождений и не исполнений): `fill` — 297, `setblock` — 16, `clone` — 0, `structure load` — 18, `loot spawn` — 3. Сумма может превышать количество строк. Для структур см. [NBT 2.8.8](structures-2.8.8.md) / [2.8.14](structures-2.8.14.md), для loot — [условия](loot-context.md), для льда — [геометрию](manual-ice-geometry-2.8.md), для Jungle — [лианы](jungle-vine-index.md).

Сравнение 2.x в этой выборке: 50 общих строк отличаются заменой `effect99:fake_ice` на `frosted_ice` (40 в Ice item, 10 в player); дополнительно только 2.8.8 содержит строку `setblock ~ ~ ~ air 0 destroy` в `blocks/fake_ice.json`. Исходные точки с иными командами и 11-е вхождение замены в `player.json` могут находиться вне данной выборки. Из замены нельзя вывести эквивалентность блоков.

| Файл / строка | Метки | Исходная строка целиком |
|---|---|---|
| `Swords_B/blocks/lightblock.json:31` | `setblock` | `"           \"run_command\": { \"command\": [ \"setblock ~ ~ ~ air 0\" ] }"` |
| `Swords_B/blocks/lightblock2.json:31` | `setblock` | `"           \"run_command\": { \"command\": [ \"setblock ~ ~ ~ air 0\" ] }"` |
| `Swords_B/blocks/sapling3.json:27` | `fill` | `"               \"fill ~ ~ ~ ~ ~ ~ sapling 3\""` |
| `Swords_B/entities/alpha_wolf.json:278` | `structure load` | `"                    \"structure load wolf_sword ~ ~ ~\""` |
| `Swords_B/entities/bee.json:849` | `loot spawn` | `"                                \"run_command\": { \"command\": [ \"loot spawn ~ ~ ~ loot bee_sword\" ] }"` |
| `Swords_B/entities/blaze.json:134` | `structure load` | `"            \"run_command\": { \"command\": [ \"structure load blaze_sword ~ ~ ~\" ] }"` |
| `Swords_B/entities/centella.json:86` | `fill` | `"             \"fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock 0 replace air\","` |
| `Swords_B/entities/centella.json:87` | `fill` | `"             \"fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock 0 replace effect99:lightblock\" ] "` |
| `Swords_B/entities/centella.json:107` | `structure load` | `"                \"run_command\": { \"command\": [ \"structure load lightning_sword ~ ~10 ~\" ] }"` |
| `Swords_B/entities/creeper.json:339` | `structure load` | `"              \"run_command\": { \"command\": [ \"structure load creeper_sword ~ ~ ~\" ] }"` |
| `Swords_B/entities/ender_crystal.json:102` | `structure load` | `"                \"run_command\": { \"command\": [ \"structure load spectral_sword ~~~\" ] }"` |
| `Swords_B/entities/ghast.json:112` | `structure load` | `"            \"run_command\": { \"command\": [ \"structure load spectral_sword ~~~\" ] }"` |
| `Swords_B/entities/ghost.json:122` | `structure load` | `"              \"structure load ghost_sword ~~~\","` |
| `Swords_B/entities/grass.json:58` | `fill` | `"            { \"weight\": 50, \"run_command\": { \"command\": [ \"fill ~ ~ ~ ~ ~ ~ tallgrass 0 replace air\" ] } },"` |
| `Swords_B/entities/item.json:124` | `fill` | `"               \"fill ~2 ~2 ~2 ~-2 ~-2 ~-2 sponge 0 replace water\","` |
| `Swords_B/entities/item.json:127` | `fill` | `"               \"fill ~2 ~2 ~2 ~-2 ~-2 ~-2 air 0 replace sponge\","` |
| `Swords_B/entities/item.json:128` | `fill` | `"               \"fill ~2 ~2 ~2 ~-2 ~-2 ~-2 air 0 replace seagrass\""` |
| `Swords_B/entities/item.json:134` | `structure load` | `"      \"wet_sponge_sword\": { \"run_command\": { \"command\": [ \"structure load wet_sponge_sword ~ ~ ~\", \"kill @s\" ] } "` |
| `Swords_B/entities/item.json:152` | `fill`, `structure load` | `"            \"run_command\": { \"command\": [ \"structure load ultra_instinct_sword ~ ~1 ~\", \"fill ~15 ~10 ~15 ~-15 ~-15 ~-15 concretepowder 0 replace sand\", \"particle minecraft:example_flipbook ~ ~ ~\", \"particle minecraft:example_flipbook ~ ~1.5 ~\", \"playsound mob.wither.ambient @a[r=16] ~ ~1 ~ 2 0.6\", \"kill @s\" ] }"` |
| `Swords_B/entities/item.json:164` | `fill`, `structure load` | `"            \"run_command\": { \"command\": [ \"structure load ultra_instinct_sword ~ ~1 ~\", \"fill ~15 ~10 ~15 ~-15 ~-15 ~-15 concretepowder 0 replace sand\", \"particle minecraft:example_flipbook ~ ~ ~\", \"particle minecraft:example_flipbook ~ ~1.5 ~\", \"playsound mob.wither.ambient @a[r=16] ~ ~1 ~ 2 0.6\", \"kill @s\" ] }"` |
| `Swords_B/entities/item.json:176` | `fill`, `structure load` | `"            \"run_command\": { \"command\": [ \"structure load time_sword ~ ~1 ~\", \"time add 6000\", \"fill ~15 ~10 ~15 ~-15 ~-15 ~-15 concretepowder 4 replace sand\", \"particle minecraft:knockback_roar_particle ~ ~0.3 ~\", \"playsound random.levelup @a[r=16] ~ ~ ~ 1 0.5\", \"kill @s\" ] }"` |
| `Swords_B/entities/item.json:181` | `structure load` | `"        \"run_command\": { \"command\": [ \"structure load bedrock_sword ~ ~1 ~\", \"kill @s\" ] }"` |
| `Swords_B/entities/item.json:184` | `structure load` | `"        \"run_command\": { \"command\": [ \"structure load fire_sword ~ ~1 ~\", \"kill @s\" ] }"` |
| `Swords_B/entities/item.json:199` | `fill` | `"            \"run_command\": { \"command\": [ \"fill ~~~ ~~~ flowing_water 0 replace air\", \"fill ~~~ ~~~ flowing_water 0 replace fire\", \"fill ~~~ ~~~ flowing_water 0 replace lava\", \"playsound random.fizz @a[r=12] ~ ~ ~ 0.6\", \"particle minecraft:cauldron_explosion_emitter ~ ~ ~\", \"kill @s\" ] }"` |
| `Swords_B/entities/item.json:214` | `fill` | `"        \"run_command\": { \"command\": [ \"fill ~2 ~2 ~2 ~-2 ~-2 ~-2 air 0 replace fire\" ] }"` |
| `Swords_B/entities/item.json:228` | `structure load` | `"      \"fire_sword_event_1\": { \"run_command\": { \"command\": [ \"structure load obsidian_sword ~ ~ ~\", \"playsound random.fizz @a[r=12] ~ ~ ~\", \"kill @s\" ] } },"` |
| `Swords_B/entities/item.json:229` | `structure load` | `"      \"fire_sword_event_2\": { \"run_command\": { \"command\": [ \"playsound random.fizz @a[r=12] ~ ~ ~ 0.6\", \"particle minecraft:cauldron_explosion_emitter ~ ~ ~\", \"structure load glass_sword ~ ~ ~\", \"kill @s\" ] } },"` |
| `Swords_B/entities/living_flame.json:215` | `fill` | `"            \"fill ~ ~ ~ ~ ~ ~ fire 0 replace air\","` |
| `Swords_B/entities/living_flame.json:224` | `fill` | `"            \"fill ~ ~ ~ ~ ~ ~ air 0 replace fire\","` |
| `Swords_B/entities/living_flame.json:236` | `fill` | `"                \"fill ~ ~ ~ ~ ~ ~ air 0 replace fire\","` |
| `Swords_B/entities/living_flame.json:250` | `loot spawn` | `"                \"run_command\": { \"command\": [ \"loot spawn ~ ~ ~ loot \\\"entities/living_flame\\\"\" ] }"` |
| `Swords_B/entities/player.json:1081` | `fill` | `"                \"fill ~6 ~6 ~6 ~-6 ~-6 ~-6 stone 0 replace effect99:spectral_block\","` |
| `Swords_B/entities/player.json:1082` | `fill` | `"                \"fill ~7 ~8 ~8 ~8 ~-8 ~-8 stone 0 replace effect99:spectral_block\","` |
| `Swords_B/entities/player.json:1083` | `fill` | `"                \"fill ~-7 ~-8 ~-8 ~-8 ~8 ~8 stone 0 replace effect99:spectral_block\","` |
| `Swords_B/entities/player.json:1084` | `fill` | `"                \"fill ~-6 ~8 ~7 ~6 ~-8 ~8 stone 0 replace effect99:spectral_block\","` |
| `Swords_B/entities/player.json:1085` | `fill` | `"                \"fill ~6 ~-8 ~-7 ~-6 ~8 ~-8 stone 0 replace effect99:spectral_block\","` |
| `Swords_B/entities/player.json:1086` | `fill` | `"                \"fill ~8 ~-8 ~8 ~-8 ~-7 ~-8 stone 0 replace effect99:spectral_block\","` |
| `Swords_B/entities/player.json:1087` | `fill` | `"                \"fill ~8 ~8 ~8 ~-8 ~7 ~-8 stone 0 replace effect99:spectral_block\""` |
| `Swords_B/entities/player.json:1095` | `fill` | `"                \"fill ~6 ~6 ~6 ~-6 ~-6 ~-6 netherrack 0 replace effect99:spectral_block\","` |
| `Swords_B/entities/player.json:1096` | `fill` | `"                \"fill ~7 ~8 ~8 ~8 ~-8 ~-8 netherrack 0 replace effect99:spectral_block\","` |
| `Swords_B/entities/player.json:1097` | `fill` | `"                \"fill ~-7 ~-8 ~-8 ~-8 ~8 ~8 netherrack 0 replace effect99:spectral_block\","` |
| `Swords_B/entities/player.json:1098` | `fill` | `"                \"fill ~-6 ~8 ~7 ~6 ~-8 ~8 netherrack 0 replace effect99:spectral_block\","` |
| `Swords_B/entities/player.json:1099` | `fill` | `"                \"fill ~6 ~-8 ~-7 ~-6 ~8 ~-8 netherrack 0 replace effect99:spectral_block\","` |
| `Swords_B/entities/player.json:1100` | `fill` | `"                \"fill ~8 ~-8 ~8 ~-8 ~-7 ~-8 netherrack 0 replace effect99:spectral_block\","` |
| `Swords_B/entities/player.json:1101` | `fill` | `"                \"fill ~8 ~8 ~8 ~-8 ~7 ~-8 netherrack 0 replace effect99:spectral_block\""` |
| `Swords_B/entities/player.json:1109` | `fill` | `"                \"fill ~6 ~6 ~6 ~-6 ~-6 ~-6 end_stone 0 replace effect99:spectral_block\","` |
| `Swords_B/entities/player.json:1110` | `fill` | `"                \"fill ~7 ~8 ~8 ~8 ~-8 ~-8 end_stone 0 replace effect99:spectral_block\","` |
| `Swords_B/entities/player.json:1111` | `fill` | `"                \"fill ~-7 ~-8 ~-8 ~-8 ~8 ~8 end_stone 0 replace effect99:spectral_block\","` |
| `Swords_B/entities/player.json:1112` | `fill` | `"                \"fill ~-6 ~8 ~7 ~6 ~-8 ~8 end_stone 0 replace effect99:spectral_block\","` |
| `Swords_B/entities/player.json:1113` | `fill` | `"                \"fill ~6 ~-8 ~-7 ~-6 ~8 ~-8 end_stone 0 replace effect99:spectral_block\","` |
| `Swords_B/entities/player.json:1114` | `fill` | `"                \"fill ~8 ~-8 ~8 ~-8 ~-7 ~-8 end_stone 0 replace effect99:spectral_block\","` |
| `Swords_B/entities/player.json:1115` | `fill` | `"                \"fill ~8 ~8 ~8 ~-8 ~7 ~-8 end_stone 0 replace effect99:spectral_block\""` |
| `Swords_B/entities/player.json:1147` | `setblock` | `"          { \"weight\": 1, \"run_command\": { \"command\": [ \"execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 0\" ] } },"` |
| `Swords_B/entities/player.json:1148` | `setblock` | `"          { \"weight\": 1, \"run_command\": { \"command\": [ \"execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 1\" ] } },"` |
| `Swords_B/entities/player.json:1149` | `setblock` | `"          { \"weight\": 1, \"run_command\": { \"command\": [ \"execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 2\" ] } },"` |
| `Swords_B/entities/player.json:1150` | `setblock` | `"          { \"weight\": 1, \"run_command\": { \"command\": [ \"execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 3\" ] } },"` |
| `Swords_B/entities/player.json:1151` | `setblock` | `"          { \"weight\": 1, \"run_command\": { \"command\": [ \"execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 4\" ] } },"` |
| `Swords_B/entities/player.json:1152` | `setblock` | `"          { \"weight\": 1, \"run_command\": { \"command\": [ \"execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 5\" ] } },"` |
| `Swords_B/entities/player.json:1153` | `setblock` | `"          { \"weight\": 1, \"run_command\": { \"command\": [ \"execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 6\" ] } },"` |
| `Swords_B/entities/player.json:1154` | `setblock` | `"          { \"weight\": 1, \"run_command\": { \"command\": [ \"execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 7\" ] } },"` |
| `Swords_B/entities/player.json:1155` | `setblock` | `"          { \"weight\": 1, \"run_command\": { \"command\": [ \"execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 8\" ] } },"` |
| `Swords_B/entities/player.json:1156` | `setblock` | `"          { \"weight\": 1, \"run_command\": { \"command\": [ \"execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 9\" ] } },"` |
| `Swords_B/entities/player.json:1157` | `setblock` | `"          { \"weight\": 1, \"run_command\": { \"command\": [ \"execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 10\" ] } },"` |
| `Swords_B/entities/player.json:1158` | `setblock` | `"          { \"weight\": 1, \"run_command\": { \"command\": [ \"execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ yellow_flower 0\" ] } }"` |
| `Swords_B/entities/player.json:1370` | `fill` | `"              \"fill ~1 ~2 ~1 ~-1 ~2 ~-1 effect99:lightblock 0 replace air\", "` |
| `Swords_B/entities/player.json:1371` | `fill` | `"              \"fill ~1 ~2 ~1 ~-1 ~2 ~-1 effect99:lightblock 0 replace effect99:lightblock\","` |
| `Swords_B/entities/player.json:1476` | `fill` | `"            \"run_command\": { \"command\": [ \"fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace air\", \"fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace effect99:lightblock2\" ] }"` |
| `Swords_B/entities/player.json:1490` | `fill` | `"        \"run_command\": { \"command\": [ \"fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock 0 replace air\", \"fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock 0 replace effect99:lightblock\" ] }"` |
| `Swords_B/entities/player.json:1502` | `fill` | `"                \"fill ~5 ~5 ~5 ~-5 ~-5 ~-5 dirt 1 replace grass\","` |
| `Swords_B/entities/player.json:1503` | `fill` | `"                \"fill ~5 ~5 ~5 ~-5 ~-5 ~-5 air 0 replace leaves2\","` |
| `Swords_B/entities/player.json:1504` | `fill` | `"                \"fill ~5 ~5 ~5 ~-5 ~-5 ~-5 air 0 replace leaves\","` |
| `Swords_B/entities/player.json:1505` | `fill` | `"                \"fill ~5 ~5 ~5 ~-5 ~-5 ~-5 air 0 replace vine\","` |
| `Swords_B/entities/player.json:1506` | `fill` | `"                \"fill ~5 ~5 ~5 ~-5 ~-5 ~-5 water 0 replace ice\","` |
| `Swords_B/entities/player.json:1507` | `fill` | `"                \"fill ~5 ~5 ~5 ~-5 ~-5 ~-5 dirt 0 replace farmland\","` |
| `Swords_B/entities/player.json:1508` | `fill` | `"                \"fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace red_flower\","` |
| `Swords_B/entities/player.json:1509` | `fill` | `"                \"fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace yellow_flower\","` |
| `Swords_B/entities/player.json:1510` | `fill` | `"                \"fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace red_mushroom\","` |
| `Swords_B/entities/player.json:1511` | `fill` | `"                \"fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace brown_mushroom\","` |
| `Swords_B/entities/player.json:1512` | `fill` | `"                \"fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace double_plant\","` |
| `Swords_B/entities/player.json:1514` | `fill` | `"                \"fill ~1 ~2 ~1 ~-1 ~2 ~-1 effect99:lightblock2 0 replace air\", "` |
| `Swords_B/entities/player.json:1515` | `fill` | `"                \"fill ~1 ~2 ~1 ~-1 ~2 ~-1 effect99:lightblock2 0 replace effect99:lightblock2\""` |
| `Swords_B/entities/player.json:1543` | `fill` | `"            \"run_command\": { \"command\": [ \"gamerule randomtickspeed 300\", \"effect @e[type=!player] speed 1 15 true\", \"time add 30\", \"event entity @a[family=default_player] time_sword_movement\", \"fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace air\", \"fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace effect99:lightblock2\" ] }"` |
| `Swords_B/entities/player.json:1571` | `fill` | `"               \"fill ~2 ~2 ~2 ~-2 ~-2 ~-2 sponge 0 replace water\","` |
| `Swords_B/entities/player.json:1581` | `fill` | `"               \"fill ~2 ~2 ~2 ~-2 ~-2 ~-2 air 0 replace sponge\","` |
| `Swords_B/entities/player.json:1582` | `fill` | `"               \"fill ~2 ~2 ~2 ~-2 ~-2 ~-2 air 0 replace seagrass\","` |
| `Swords_B/entities/player.json:1702` | `fill` | `"               \"fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace air\", "` |
| `Swords_B/entities/player.json:1703` | `fill` | `"               \"fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace effect99:lightblock2\","` |
| `Swords_B/entities/player.json:1719` | `fill` | `"                \"fill ~8 ~8 ~8 ~-8 ~-6 ~-8 stone 0 replace effect99:spectral_block\""` |
| `Swords_B/entities/player.json:1727` | `fill` | `"                \"fill ~8 ~8 ~8 ~-8 ~-6 ~-8 netherrack 0 replace effect99:spectral_block\""` |
| `Swords_B/entities/player.json:1735` | `fill` | `"                \"fill ~8 ~8 ~8 ~-8 ~-6 ~-8 end_stone 0 replace effect99:spectral_block\""` |
| `Swords_B/entities/player.json:1749` | `fill` | `"                \"fill ~6 ~6 ~6 ~-6 ~-6 ~-6 effect99:spectral_block 0 replace stone\","` |
| `Swords_B/entities/player.json:1750` | `fill` | `"                \"fill ~7 ~8 ~8 ~8 ~-8 ~-8 stone 0 replace effect99:spectral_block\","` |
| `Swords_B/entities/player.json:1751` | `fill` | `"                \"fill ~-7 ~-8 ~-8 ~-8 ~8 ~8 stone 0 replace effect99:spectral_block\","` |
| `Swords_B/entities/player.json:1752` | `fill` | `"                \"fill ~-6 ~8 ~7 ~6 ~-8 ~8 stone 0 replace effect99:spectral_block\","` |
| `Swords_B/entities/player.json:1753` | `fill` | `"                \"fill ~6 ~-8 ~-7 ~-6 ~8 ~-8 stone 0 replace effect99:spectral_block\","` |
| `Swords_B/entities/player.json:1754` | `fill` | `"                \"fill ~8 ~-8 ~8 ~-8 ~-7 ~-8 stone 0 replace effect99:spectral_block\","` |
| `Swords_B/entities/player.json:1755` | `fill` | `"                \"fill ~8 ~8 ~8 ~-8 ~7 ~-8 stone 0 replace effect99:spectral_block\""` |
| `Swords_B/entities/player.json:1763` | `fill` | `"                \"fill ~6 ~6 ~6 ~-6 ~-6 ~-6 effect99:spectral_block 0 replace netherrack\","` |
| `Swords_B/entities/player.json:1764` | `fill` | `"                \"fill ~7 ~8 ~8 ~8 ~-8 ~-8 netherrack 0 replace effect99:spectral_block\","` |
| `Swords_B/entities/player.json:1765` | `fill` | `"                \"fill ~-7 ~-8 ~-8 ~-8 ~8 ~8 netherrack 0 replace effect99:spectral_block\","` |
| `Swords_B/entities/player.json:1766` | `fill` | `"                \"fill ~-6 ~8 ~7 ~6 ~-8 ~8 netherrack 0 replace effect99:spectral_block\","` |
| `Swords_B/entities/player.json:1767` | `fill` | `"                \"fill ~6 ~-8 ~-7 ~-6 ~8 ~-8 netherrack 0 replace effect99:spectral_block\","` |
| `Swords_B/entities/player.json:1768` | `fill` | `"                \"fill ~8 ~-8 ~8 ~-8 ~-7 ~-8 netherrack 0 replace effect99:spectral_block\","` |
| `Swords_B/entities/player.json:1769` | `fill` | `"                \"fill ~8 ~8 ~8 ~-8 ~7 ~-8 netherrack 0 replace effect99:spectral_block\""` |
| `Swords_B/entities/player.json:1777` | `fill` | `"                \"fill ~6 ~6 ~6 ~-6 ~-6 ~-6 effect99:spectral_block 0 replace end_stone\","` |
| `Swords_B/entities/player.json:1778` | `fill` | `"                \"fill ~7 ~8 ~8 ~8 ~-8 ~-8 end_stone 0 replace effect99:spectral_block\","` |
| `Swords_B/entities/player.json:1779` | `fill` | `"                \"fill ~-7 ~-8 ~-8 ~-8 ~8 ~8 end_stone 0 replace effect99:spectral_block\","` |
| `Swords_B/entities/player.json:1780` | `fill` | `"                \"fill ~-6 ~8 ~7 ~6 ~-8 ~8 end_stone 0 replace effect99:spectral_block\","` |
| `Swords_B/entities/player.json:1781` | `fill` | `"                \"fill ~6 ~-8 ~-7 ~-6 ~8 ~-8 end_stone 0 replace effect99:spectral_block\","` |
| `Swords_B/entities/player.json:1782` | `fill` | `"                \"fill ~8 ~-8 ~8 ~-8 ~-7 ~-8 end_stone 0 replace effect99:spectral_block\","` |
| `Swords_B/entities/player.json:1783` | `fill` | `"                \"fill ~8 ~8 ~8 ~-8 ~7 ~-8 end_stone 0 replace effect99:spectral_block\""` |
| `Swords_B/entities/player.json:1928` | `setblock` | `"            \"run_command\": { \"command\": [ \"playsound random.fizz @a[r=10] ~ ~ ~\", \"setblock ~ ~ ~ flowing_water\", \"replaceitem entity @s slot.weapon.mainhand 0 air 1 0\", \"particle minecraft:cauldron_explosion_emitter ~ ~ ~\" ] }"` |
| `Swords_B/entities/player.json:1936` | `fill` | `"              \"fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 frosted_ice 0 replace water\","` |
| `Swords_B/entities/player.json:1937` | `fill` | `"              \"fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 frosted_ice 0 replace flowing_water\","` |
| `Swords_B/entities/player.json:1938` | `fill` | `"              \"fill ~3 ~-1 ~ ~3 ~-1 ~ frosted_ice 0 replace water\","` |
| `Swords_B/entities/player.json:1939` | `fill` | `"              \"fill ~3 ~-1 ~ ~3 ~-1 ~ frosted_ice 0 replace flowing_water\","` |
| `Swords_B/entities/player.json:1940` | `fill` | `"              \"fill ~ ~-1 ~3 ~ ~-1 ~3 frosted_ice 0 replace water\","` |
| `Swords_B/entities/player.json:1941` | `fill` | `"              \"fill ~ ~-1 ~3 ~ ~-1 ~3 frosted_ice 0 replace flowing_water\","` |
| `Swords_B/entities/player.json:1942` | `fill` | `"              \"fill ~-3 ~-1 ~ ~-3 ~-1 ~ frosted_ice 0 replace water\","` |
| `Swords_B/entities/player.json:1943` | `fill` | `"              \"fill ~-3 ~-1 ~ ~-3 ~-1 ~ frosted_ice 0 replace flowing_water\","` |
| `Swords_B/entities/player.json:1944` | `fill` | `"              \"fill ~ ~-1 ~-3 ~ ~-1 ~-3 frosted_ice 0 replace water\","` |
| `Swords_B/entities/player.json:1945` | `fill` | `"              \"fill ~ ~-1 ~-3 ~ ~-1 ~-3 frosted_ice 0 replace flowing_water\","` |
| `Swords_B/entities/player.json:1969` | `fill` | `"              \"fill ~ ~-1 ~ ~ ~-1 ~ magma 0 replace lava\","` |
| `Swords_B/entities/player.json:1970` | `fill` | `"              \"fill ~1 ~-1 ~1 ~ ~-1 ~ magma 0 replace lava\","` |
| `Swords_B/entities/player.json:1971` | `fill` | `"              \"fill ~ ~-1 ~1 ~ ~-1 ~1 magma 0 replace lava\","` |
| `Swords_B/entities/player.json:1972` | `fill` | `"              \"fill ~-1 ~-1 ~ ~-1 ~-1 ~ magma 0 replace lava\","` |
| `Swords_B/entities/player.json:1973` | `fill` | `"              \"fill ~ ~-1 ~-1 ~ ~-1 ~-1 magma 0 replace lava\","` |
| `Swords_B/entities/player.json:2032` | `fill` | `"              \"fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 grass 0 replace dirt\","` |
| `Swords_B/entities/player.json:2033` | `fill` | `"              \"execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 fill ~ ~ ~ ~ ~ ~ tallgrass 0 replace air\""` |
| `Swords_B/entities/player.json:2063` | `fill` | `"               \"fill ~3 ~3 ~3 ~-3 ~-3 ~-3 air 0 replace snow_layer\","` |
| `Swords_B/entities/player.json:2064` | `fill` | `"               \"fill ~3 ~3 ~3 ~-3 ~-3 ~-3 water 0 replace ice\","` |
| `Swords_B/entities/player.json:2065` | `fill` | `"               \"fill ~3 ~3 ~3 ~-3 ~-3 ~-3 water 0 replace blue_ice\","` |
| `Swords_B/entities/player.json:2066` | `fill` | `"               \"fill ~3 ~3 ~3 ~-3 ~-3 ~-3 water 0 replace packed_ice\","` |
| `Swords_B/entities/player.json:2068` | `fill` | `"               \"fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock 0 replace air\", "` |
| `Swords_B/entities/player.json:2069` | `fill` | `"               \"fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock 0 replace effect99:lightblock\""` |
| `Swords_B/entities/player.json:2188` | `fill` | `"            \"command\": [ \"event entity @e[family=shot_by_the_blaze,r=7] minecraft:inertia_disable\", \"fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace air\", \"fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace effect99:lightblock2\" ]"` |
| `Swords_B/entities/skeleton.json:275` | `structure load` | `"                \"run_command\": { \"command\": [ \"structure load bone_sword ~ ~ ~\" ] }"` |
| `Swords_B/entities/snowball.json:74` | `fill` | `"      \"ice_sword\": { \"run_command\": { \"command\": [ \"fill ~ ~ ~ ~ ~ ~ snow_layer 0 replace air\" ] } },"` |
| `Swords_B/entities/web.json:63` | `fill` | `"           \"run_command\": { \"command\": [  \"fill ~ ~ ~ ~ ~ ~ web 0 replace air\" ] }"` |
| `Swords_B/entities/witch.json:220` | `setblock`, `structure load` | `"            \"run_command\": { \"command\": [ \"structure load grass_sword ~~~\", \"setblock ~ ~ ~ double_plant 2\", \"playsound dig.grass @a[r=12] ~~~\" ] }"` |
| `Swords_B/entities/wither.json:163` | `structure load` | `"                \"run_command\": { \"command\": [ \"structure load wither_sword ~ ~ ~\" ] }"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:1` | `fill` | `"execute @p ~~~ detect ~1 ~1 ~ log 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:2` | `fill` | `"execute @p ~~~ detect ~-1 ~1 ~ log 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:3` | `fill` | `"execute @p ~~~ detect ~ ~1 ~1 log 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:4` | `fill` | `"execute @p ~~~ detect ~ ~1 ~-1 log 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:5` | `fill` | `"execute @p ~~~ detect ~1 ~1 ~ log 1 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:6` | `fill` | `"execute @p ~~~ detect ~-1 ~1 ~ log 1 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:7` | `fill` | `"execute @p ~~~ detect ~ ~1 ~1 log 1 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:8` | `fill` | `"execute @p ~~~ detect ~ ~1 ~-1 log 1 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:9` | `fill` | `"execute @p ~~~ detect ~1 ~1 ~ log 2 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:10` | `fill` | `"execute @p ~~~ detect ~-1 ~1 ~ log 2 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:11` | `fill` | `"execute @p ~~~ detect ~ ~1 ~1 log 2 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:12` | `fill` | `"execute @p ~~~ detect ~ ~1 ~-1 log 2 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:13` | `fill` | `"execute @p ~~~ detect ~1 ~1 ~ log 3 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:14` | `fill` | `"execute @p ~~~ detect ~-1 ~1 ~ log 3 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:15` | `fill` | `"execute @p ~~~ detect ~ ~1 ~1 log 3 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:16` | `fill` | `"execute @p ~~~ detect ~ ~1 ~-1 log 3 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:17` | `fill` | `"execute @p ~~~ detect ~1 ~1 ~ log2 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:18` | `fill` | `"execute @p ~~~ detect ~-1 ~1 ~ log2 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:19` | `fill` | `"execute @p ~~~ detect ~ ~1 ~1 log2 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:20` | `fill` | `"execute @p ~~~ detect ~ ~1 ~-1 log2 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:21` | `fill` | `"execute @p ~~~ detect ~1 ~1 ~ log2 1 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:22` | `fill` | `"execute @p ~~~ detect ~-1 ~1 ~ log2 1 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:23` | `fill` | `"execute @p ~~~ detect ~ ~1 ~1 log2 1 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:24` | `fill` | `"execute @p ~~~ detect ~ ~1 ~-1 log2 1 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:25` | `fill` | `"execute @p ~~~ detect ~1 ~1 ~ stone 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:26` | `fill` | `"execute @p ~~~ detect ~-1 ~1 ~ stone 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:27` | `fill` | `"execute @p ~~~ detect ~ ~1 ~1 stone 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:28` | `fill` | `"execute @p ~~~ detect ~ ~1 ~-1 stone 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:29` | `fill` | `"execute @p ~~~ detect ~1 ~1 ~ cobblestone 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:30` | `fill` | `"execute @p ~~~ detect ~-1 ~1 ~ cobblestone 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:31` | `fill` | `"execute @p ~~~ detect ~ ~1 ~1 cobblestone 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:32` | `fill` | `"execute @p ~~~ detect ~ ~1 ~-1 cobblestone 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:33` | `fill` | `"execute @p ~~~ detect ~1 ~1 ~ dirt 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:34` | `fill` | `"execute @p ~~~ detect ~-1 ~1 ~ dirt 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:35` | `fill` | `"execute @p ~~~ detect ~ ~1 ~1 dirt 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:36` | `fill` | `"execute @p ~~~ detect ~ ~1 ~-1 dirt 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:37` | `fill` | `"execute @p ~~~ detect ~1 ~1 ~ leaves 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:38` | `fill` | `"execute @p ~~~ detect ~-1 ~1 ~ leaves 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:39` | `fill` | `"execute @p ~~~ detect ~ ~1 ~1 leaves 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:40` | `fill` | `"execute @p ~~~ detect ~ ~1 ~-1 leaves 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:41` | `fill` | `"execute @p ~~~ detect ~1 ~1 ~ leaves 1 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:42` | `fill` | `"execute @p ~~~ detect ~-1 ~1 ~ leaves 1 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:43` | `fill` | `"execute @p ~~~ detect ~ ~1 ~1 leaves 1 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:44` | `fill` | `"execute @p ~~~ detect ~ ~1 ~-1 leaves 1 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:45` | `fill` | `"execute @p ~~~ detect ~1 ~1 ~ leaves 2 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:46` | `fill` | `"execute @p ~~~ detect ~-1 ~1 ~ leaves 2 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:47` | `fill` | `"execute @p ~~~ detect ~ ~1 ~1 leaves 2 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:48` | `fill` | `"execute @p ~~~ detect ~ ~1 ~-1 leaves 2 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:49` | `fill` | `"execute @p ~~~ detect ~1 ~1 ~ leaves 3 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:50` | `fill` | `"execute @p ~~~ detect ~-1 ~1 ~ leaves 3 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:51` | `fill` | `"execute @p ~~~ detect ~ ~1 ~1 leaves 3 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:52` | `fill` | `"execute @p ~~~ detect ~ ~1 ~-1 leaves 3 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:53` | `fill` | `"execute @p ~~~ detect ~1 ~1 ~ leaves 11 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:54` | `fill` | `"execute @p ~~~ detect ~-1 ~1 ~ leaves 11 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:55` | `fill` | `"execute @p ~~~ detect ~ ~1 ~1 leaves 11 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:56` | `fill` | `"execute @p ~~~ detect ~ ~1 ~-1 leaves 11 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:57` | `fill` | `"execute @p ~~~ detect ~1 ~1 ~ leaves2 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:58` | `fill` | `"execute @p ~~~ detect ~-1 ~1 ~ leaves2 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:59` | `fill` | `"execute @p ~~~ detect ~ ~1 ~1 leaves2 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:60` | `fill` | `"execute @p ~~~ detect ~ ~1 ~-1 leaves2 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:61` | `fill` | `"execute @p ~~~ detect ~1 ~1 ~ leaves2 1 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:62` | `fill` | `"execute @p ~~~ detect ~-1 ~1 ~ leaves2 1 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:63` | `fill` | `"execute @p ~~~ detect ~ ~1 ~1 leaves2 1 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:64` | `fill` | `"execute @p ~~~ detect ~ ~1 ~-1 leaves2 1 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:65` | `fill` | `"execute @p ~~~ detect ~1 ~1 ~ planks 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:66` | `fill` | `"execute @p ~~~ detect ~-1 ~1 ~ planks 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:67` | `fill` | `"execute @p ~~~ detect ~ ~1 ~1 planks 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:68` | `fill` | `"execute @p ~~~ detect ~ ~1 ~-1 planks 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:69` | `fill` | `"execute @p ~~~ detect ~1 ~1 ~ planks 1 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:70` | `fill` | `"execute @p ~~~ detect ~-1 ~1 ~ planks 1 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:71` | `fill` | `"execute @p ~~~ detect ~ ~1 ~1 planks 1 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:72` | `fill` | `"execute @p ~~~ detect ~ ~1 ~-1 planks 1 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:73` | `fill` | `"execute @p ~~~ detect ~1 ~1 ~ planks 2 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:74` | `fill` | `"execute @p ~~~ detect ~-1 ~1 ~ planks 2 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:75` | `fill` | `"execute @p ~~~ detect ~ ~1 ~1 planks 2 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:76` | `fill` | `"execute @p ~~~ detect ~ ~1 ~-1 planks 2 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:77` | `fill` | `"execute @p ~~~ detect ~1 ~1 ~ planks 3 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:78` | `fill` | `"execute @p ~~~ detect ~-1 ~1 ~ planks 3 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:79` | `fill` | `"execute @p ~~~ detect ~ ~1 ~1 planks 3 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:80` | `fill` | `"execute @p ~~~ detect ~ ~1 ~-1 planks 3 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:81` | `fill` | `"execute @p ~~~ detect ~1 ~1 ~ planks 4 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:82` | `fill` | `"execute @p ~~~ detect ~-1 ~1 ~ planks 4 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:83` | `fill` | `"execute @p ~~~ detect ~ ~1 ~1 planks 4 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:84` | `fill` | `"execute @p ~~~ detect ~ ~1 ~-1 planks 4 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:85` | `fill` | `"execute @p ~~~ detect ~1 ~1 ~ planks 5 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:86` | `fill` | `"execute @p ~~~ detect ~-1 ~1 ~ planks 5 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:87` | `fill` | `"execute @p ~~~ detect ~ ~1 ~1 planks 5 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:88` | `fill` | `"execute @p ~~~ detect ~ ~1 ~-1 planks 5 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:89` | `fill` | `"execute @p ~~~ detect ~1 ~1 ~ grass 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:90` | `fill` | `"execute @p ~~~ detect ~-1 ~1 ~ grass 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:91` | `fill` | `"execute @p ~~~ detect ~ ~1 ~1 grass 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:92` | `fill` | `"execute @p ~~~ detect ~ ~1 ~-1 grass 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:93` | `fill` | `"execute @p ~~~ detect ~1 ~1 ~ netherrack 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:94` | `fill` | `"execute @p ~~~ detect ~-1 ~1 ~ netherrack 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:95` | `fill` | `"execute @p ~~~ detect ~ ~1 ~1 netherrack 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:96` | `fill` | `"execute @p ~~~ detect ~ ~1 ~-1 netherrack 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:97` | `fill` | `"execute @p ~~~ detect ~1 ~1 ~ nether_brick 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:98` | `fill` | `"execute @p ~~~ detect ~-1 ~1 ~ nether_brick 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:99` | `fill` | `"execute @p ~~~ detect ~ ~1 ~1 nether_brick 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:100` | `fill` | `"execute @p ~~~ detect ~ ~1 ~-1 nether_brick 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:101` | `fill` | `"execute @p ~~~ detect ~1 ~1 ~ sand 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:102` | `fill` | `"execute @p ~~~ detect ~-1 ~1 ~ sand 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:103` | `fill` | `"execute @p ~~~ detect ~ ~1 ~1 sand 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:104` | `fill` | `"execute @p ~~~ detect ~ ~1 ~-1 sand 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:105` | `fill` | `"execute @p ~~~ detect ~1 ~1 ~ glass 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:106` | `fill` | `"execute @p ~~~ detect ~-1 ~1 ~ glass 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:107` | `fill` | `"execute @p ~~~ detect ~ ~1 ~1 glass 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:108` | `fill` | `"execute @p ~~~ detect ~ ~1 ~-1 glass 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:109` | `fill` | `"execute @p ~~~ detect ~1 ~1 ~ obsidian 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:110` | `fill` | `"execute @p ~~~ detect ~-1 ~1 ~ obsidian 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:111` | `fill` | `"execute @p ~~~ detect ~ ~1 ~1 obsidian 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:112` | `fill` | `"execute @p ~~~ detect ~ ~1 ~-1 obsidian 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:113` | `fill` | `"execute @p ~~~ detect ~1 ~1 ~ end_stone 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:114` | `fill` | `"execute @p ~~~ detect ~-1 ~1 ~ end_stone 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:115` | `fill` | `"execute @p ~~~ detect ~ ~1 ~1 end_stone 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:116` | `fill` | `"execute @p ~~~ detect ~ ~1 ~-1 end_stone 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:117` | `fill` | `"execute @p ~~~ detect ~1 ~1 ~ sandstone 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:118` | `fill` | `"execute @p ~~~ detect ~-1 ~1 ~ sandstone 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:119` | `fill` | `"execute @p ~~~ detect ~ ~1 ~1 sandstone 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:120` | `fill` | `"execute @p ~~~ detect ~ ~1 ~-1 sandstone 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:121` | `fill` | `"execute @p ~~~ detect ~1 ~1 ~ gravel 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:122` | `fill` | `"execute @p ~~~ detect ~-1 ~1 ~ gravel 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:123` | `fill` | `"execute @p ~~~ detect ~ ~1 ~1 gravel 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:124` | `fill` | `"execute @p ~~~ detect ~ ~1 ~-1 gravel 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:125` | `fill` | `"execute @p ~~~ detect ~1 ~1 ~ stone 1 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:126` | `fill` | `"execute @p ~~~ detect ~-1 ~1 ~ stone 1 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:127` | `fill` | `"execute @p ~~~ detect ~ ~1 ~1 stone 1 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:128` | `fill` | `"execute @p ~~~ detect ~ ~1 ~-1 stone 1 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:129` | `fill` | `"execute @p ~~~ detect ~1 ~1 ~ stone 3 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:130` | `fill` | `"execute @p ~~~ detect ~-1 ~1 ~ stone 3 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:131` | `fill` | `"execute @p ~~~ detect ~ ~1 ~1 stone 3 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:132` | `fill` | `"execute @p ~~~ detect ~ ~1 ~-1 stone 3 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:133` | `fill` | `"execute @p ~~~ detect ~1 ~1 ~ stone 5 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:134` | `fill` | `"execute @p ~~~ detect ~-1 ~1 ~ stone 5 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:135` | `fill` | `"execute @p ~~~ detect ~ ~1 ~1 stone 5 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:136` | `fill` | `"execute @p ~~~ detect ~ ~1 ~-1 stone 5 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:137` | `fill` | `"execute @p ~~~ detect ~1 ~1 ~ snow 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:138` | `fill` | `"execute @p ~~~ detect ~-1 ~1 ~ snow 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:139` | `fill` | `"execute @p ~~~ detect ~ ~1 ~1 snow 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:140` | `fill` | `"execute @p ~~~ detect ~ ~1 ~-1 snow 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:141` | `fill` | `"execute @p ~~~ detect ~1 ~1 ~ packed_ice 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:142` | `fill` | `"execute @p ~~~ detect ~-1 ~1 ~ packed_ice 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:143` | `fill` | `"execute @p ~~~ detect ~ ~1 ~1 packed_ice 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:144` | `fill` | `"execute @p ~~~ detect ~ ~1 ~-1 packed_ice 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:145` | `fill` | `"execute @p ~~~ detect ~1 ~1 ~ ice 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:146` | `fill` | `"execute @p ~~~ detect ~-1 ~1 ~ ice 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:147` | `fill` | `"execute @p ~~~ detect ~ ~1 ~1 ice 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air"` |
| `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction:148` | `fill` | `"execute @p ~~~ detect ~ ~1 ~-1 ice 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air"` |
| `Swords_B/items/ice_sword.json:85` | `fill` | `"                \"execute @e[type=!enderman,type=!horse,type=!slime,type=!silverfish,type=!spider,type=!cave_spider,type=!tnt,type=!vex,type=!chicken,type=!pig,type=!wolf,type=!cat,type=!item,type=!xp_orb,type=!xp_bottle,type=!egg,type=!snowball,type=!fireball,type=!small_fireball,type=!eye_of_ender_signal,type=!ender_pearl,type=!fishing_hook,type=!falling_block,type=!lightning_bolt,type=!lingering_potion,type=!dragon_fireball,type=!ender_dragon,type=!endermite,type=!arrow,type=!thrown_trident,type=!leash_knot,type=!bat,type=!rabbit,type=!parrot,type=!ghast,type=!shulker,type=!elder_guardian,type=!guardian,type=!turtle,type=!fox,type=!squid,type=!ocelot,type=!phantom,type=!area_effect_cloud,family=!fish,family=!effect99_entities,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 frosted_ice 0 replace air 0\","` |
| `Swords_B/items/ice_sword.json:86` | `fill` | `"                \"execute @e[type=enderman,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~3 ~-1 frosted_ice 0 replace air 0\","` |
| `Swords_B/items/ice_sword.json:87` | `fill` | `"                \"execute @e[family=slime_large,rm=2,r=12] ~ ~ ~ fill ~2 ~-1 ~2 ~-2 ~3 ~-2 frosted_ice 0 replace air 0\","` |
| `Swords_B/items/ice_sword.json:88` | `fill` | `"                \"execute @e[family=slime_large,rm=2,r=12] ~ ~1 ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 air 0 replace frosted_ice\","` |
| `Swords_B/items/ice_sword.json:89` | `fill` | `"                \"execute @e[family=slime_medium,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0\","` |
| `Swords_B/items/ice_sword.json:90` | `fill` | `"                \"execute @e[family=slime_medium,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ air 0 replace frosted_ice\","` |
| `Swords_B/items/ice_sword.json:91` | `fill` | `"                \"execute @e[family=slime_small,rm=2,r=12] ~ ~ ~ fill ~1 ~1 ~1 ~-1 ~-1 ~-1 frosted_ice 0 replace air 0\","` |
| `Swords_B/items/ice_sword.json:92` | `fill` | `"                \"execute @e[family=slime_small,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ air 0 replace frosted_ice\","` |
| `Swords_B/items/ice_sword.json:93` | `fill` | `"                \"execute @e[type=silverfish,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ frosted_ice 0 replace air 0\","` |
| `Swords_B/items/ice_sword.json:94` | `fill` | `"                \"execute @e[type=spider,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0\","` |
| `Swords_B/items/ice_sword.json:95` | `fill` | `"                \"execute @e[type=cave_spider,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0\","` |
| `Swords_B/items/ice_sword.json:96` | `fill` | `"                \"execute @e[type=tnt,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0\","` |
| `Swords_B/items/ice_sword.json:97` | `fill` | `"                \"execute @e[type=vex,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0\","` |
| `Swords_B/items/ice_sword.json:98` | `fill` | `"                \"execute @e[type=chicken,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0\","` |
| `Swords_B/items/ice_sword.json:99` | `fill` | `"                \"execute @e[type=pig,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0\","` |
| `Swords_B/items/ice_sword.json:100` | `fill` | `"                \"execute @e[type=wolf,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0\","` |
| `Swords_B/items/ice_sword.json:101` | `fill` | `"                \"execute @e[type=cat,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0\","` |
| `Swords_B/items/ice_sword.json:102` | `fill` | `"                \"execute @e[type=small_fireball,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ frosted_ice 0 replace air 0\","` |
| `Swords_B/items/ice_sword.json:103` | `fill` | `"                \"execute @e[type=fireball,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ frosted_ice 0 replace air 0\","` |
| `Swords_B/items/ice_sword.json:104` | `fill` | `"                \"execute @e[type=arrow,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ frosted_ice 0 replace air 0\","` |
| `Swords_B/items/ice_sword.json:105` | `fill` | `"                \"execute @e[type=lingering_potion,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ frosted_ice 0 replace air 0\","` |
| `Swords_B/items/ice_sword.json:106` | `fill` | `"                \"execute @e[type=dragon_fireball,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ frosted_ice 0 replace air 0\","` |
| `Swords_B/items/ice_sword.json:107` | `fill` | `"                \"execute @e[type=thrown_trident,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ frosted_ice 0 replace air 0\","` |
| `Swords_B/items/ice_sword.json:108` | `fill` | `"                \"execute @e[type=endermite,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0\","` |
| `Swords_B/items/ice_sword.json:109` | `fill` | `"                \"execute @e[type=rabbit,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0\","` |
| `Swords_B/items/ice_sword.json:110` | `fill` | `"                \"execute @e[type=parrot,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0\","` |
| `Swords_B/items/ice_sword.json:111` | `fill` | `"                \"execute @e[type=phantom,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0\","` |
| `Swords_B/items/ice_sword.json:112` | `fill` | `"                \"execute @e[type=shulker,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0\","` |
| `Swords_B/items/ice_sword.json:113` | `fill` | `"                \"execute @e[type=guardian,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0\","` |
| `Swords_B/items/ice_sword.json:114` | `fill` | `"                \"execute @e[type=ocelot,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0\","` |
| `Swords_B/items/ice_sword.json:115` | `fill` | `"                \"execute @e[type=turtle,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0\","` |
| `Swords_B/items/ice_sword.json:116` | `fill` | `"                \"execute @e[type=fox,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0\","` |
| `Swords_B/items/ice_sword.json:117` | `fill` | `"                \"execute @e[type=squid,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0\","` |
| `Swords_B/items/ice_sword.json:118` | `fill` | `"                \"execute @e[type=elder_guardian,rm=2,r=12] ~ ~ ~ fill ~2 ~-1 ~2 ~-2 ~3 ~-2 frosted_ice 0 replace air 0\","` |
| `Swords_B/items/ice_sword.json:119` | `fill` | `"                \"execute @e[type=bat,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0\","` |
| `Swords_B/items/ice_sword.json:120` | `fill` | `"                \"execute @e[type=ghast,rm=2,r=12] ~ ~ ~ fill ~4 ~-3 ~4 ~-4 ~4 ~-4 frosted_ice 0 replace air 0\","` |
| `Swords_B/items/ice_sword.json:121` | `fill` | `"                \"execute @e[type=ghast,rm=2,r=12] ~ ~ ~ fill ~3 ~-2 ~3 ~-3 ~3 ~-3 air 0 replace frosted_ice\","` |
| `Swords_B/items/ice_sword.json:122` | `fill` | `"                \"execute @e[type=horse,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0\","` |
| `Swords_B/items/ice_sword.json:123` | `fill` | `"                \"execute @e[type=horse,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ air 0 replace frosted_ice 0\","` |
| `Swords_B/items/ice_sword.json:124` | `fill` | `"                \"execute @e[type=player,rm=3,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 frosted_ice 0 replace air 0\","` |
| `Swords_B/scripts/javascript.js:8` | `loot spawn` | `"            f.player.runCommand(\u0060execute @s ~ ~ ~ loot spawn ${x} ${y} ${z} loot pumpkin_sword\u0060)"` |

Условия и полные определения: [реестр мира](world-ledger-2.8.14.md), [реестр сущностей](entity-ledger-2.8.14.md), [предметы](items-2.8.14.md).
