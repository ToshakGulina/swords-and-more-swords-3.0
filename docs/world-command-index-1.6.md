# Команды изменения мира и создания loot: исходные строки — 1.6

Лексический поиск по всем `.json`, `.mcfunction`, `.js` behavior pack: **412 исходных строк**, содержащих `fill`, `setblock`, `clone`, `structure load` или `loot spawn`. Сохранены точные строки, отступы, номера, порядок файла и повторы; строка может содержать несколько команд и несколько меток. Отсортировано по пути и номеру, а не по времени исполнения.

Это **кандидаты по тексту**, не Bedrock-парсер или доказательство вызова, применимости синтаксиса и изменений мира. Комментарии, неразобранные JSON, строковые данные и шаблоны JS включены; координаты, selector, detect, replace, порядок в sequence, случайные фильтры и исполнитель сохраняются в исходном тексте, но здесь не вычисляются. Вне области: другие команды, функции из других пакетов, block components, взрывы, вызовы `summon`/`event entity`, автоматические механизмы и косвенные эффекты. Показан только найденный текст, а не число затронутых блоков.

Метки по числу строк (не вхождений и не исполнений): `fill` — 306, `setblock` — 106, `clone` — 0, `structure load` — 0, `loot spawn` — 0. Сумма может превышать количество строк. Для структур см. [NBT 2.8.8](structures-2.8.8.md) / [2.8.14](structures-2.8.14.md), для loot — [условия](loot-context.md), для льда — [геометрию](manual-ice-geometry-2.8.md), для Jungle — [лианы](jungle-vine-index.md).

| Файл / строка | Метки | Исходная строка целиком |
|---|---|---|
| `Sword_B/animation_controllers/fire_sword.json:14` | `setblock` | `"          \t\"/execute @p ~ ~ ~ detect ~ ~ ~ air 0 setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:15` | `fill` | `"          \t\"/execute @p ~ ~ ~ fill ~3 ~3 ~3 ~-3 ~-3 ~-3 air 0 replace snow_layer\","` |
| `Sword_B/animation_controllers/fire_sword.json:16` | `fill` | `"          \t\"/execute @p ~ ~ ~ fill ~3 ~3 ~3 ~-3 ~-3 ~-3 water 0 replace ice\","` |
| `Sword_B/animation_controllers/fire_sword.json:17` | `fill` | `"          \t\"/execute @p ~ ~ ~ fill ~3 ~3 ~3 ~-3 ~-3 ~-3 water 0 replace blue_ice\","` |
| `Sword_B/animation_controllers/fire_sword.json:18` | `fill` | `"          \t\"/execute @p ~ ~ ~ fill ~3 ~3 ~3 ~-3 ~-3 ~-3 water 0 replace packed_ice\","` |
| `Sword_B/animation_controllers/fire_sword.json:19` | `fill` | `"          \t\"/execute @p ~ ~ ~ fill ~3 ~3 ~3 ~-3 ~-3 ~-3 grass 0 replace snow\","` |
| `Sword_B/animation_controllers/fire_sword.json:20` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=zombie] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:21` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=husk] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:22` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=drowned] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:23` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=creeper] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:24` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=enderman] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:25` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=slime] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:26` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=skeleton] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:27` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=stray] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:28` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=witch] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:29` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=spider] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:30` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=cave_spider] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:31` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=silverfish] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:32` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=evocation_fang] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:33` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=evocation_illager] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:34` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=vex] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:35` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=ravager] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:36` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=endermite] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:37` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=guardian] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:38` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=vindicator] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:39` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=phantom] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:40` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=cow] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:41` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=pig] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:42` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=chicken] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:43` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=horse] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:44` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=rabbit] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:45` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=sheep] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:46` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=fox] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:47` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=bat] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:48` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=polar_bear] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:49` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=villager] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:50` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=zombie_villager] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:65` | `setblock` | `"          \t\"/execute @p ~ ~ ~ detect ~ ~ ~ air 0 setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:66` | `fill` | `"          \t\"/execute @p ~ ~ ~ fill ~3 ~3 ~3 ~-3 ~-3 ~-3 air 0 replace snow_layer\","` |
| `Sword_B/animation_controllers/fire_sword.json:67` | `fill` | `"          \t\"/execute @p ~ ~ ~ fill ~3 ~3 ~3 ~-3 ~-3 ~-3 water 0 replace ice\","` |
| `Sword_B/animation_controllers/fire_sword.json:68` | `fill` | `"          \t\"/execute @p ~ ~ ~ fill ~3 ~3 ~3 ~-3 ~-3 ~-3 water 0 replace blue_ice\","` |
| `Sword_B/animation_controllers/fire_sword.json:69` | `fill` | `"          \t\"/execute @p ~ ~ ~ fill ~3 ~3 ~3 ~-3 ~-3 ~-3 water 0 replace packed_ice\","` |
| `Sword_B/animation_controllers/fire_sword.json:70` | `fill` | `"          \t\"/execute @p ~ ~ ~ fill ~3 ~3 ~3 ~-3 ~-3 ~-3 grass 0 replace snow\","` |
| `Sword_B/animation_controllers/fire_sword.json:71` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=zombie] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:72` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=husk] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:73` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=drowned] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:74` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=creeper] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:75` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=enderman] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:76` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=slime] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:77` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=skeleton] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:78` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=stray] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:79` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=witch] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:80` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=spider] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:81` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=cave_spider] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:82` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=silverfish] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:83` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=evocation_fang] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:84` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=evocation_illager] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:85` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=vex] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:86` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=ravager] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:87` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=endermite] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:88` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=guardian] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:89` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=vindicator] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:90` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=phantom] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:91` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=cow] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:92` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=pig] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:93` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=chicken] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:94` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=horse] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:95` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=rabbit] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:96` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=sheep] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:97` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=fox] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:98` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=bat] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:99` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=polar_bear] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:100` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=villager] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/fire_sword.json:101` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=zombie_villager] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/glowstone_sword.json:13` | `fill` | `"          \t\"/execute @p ~~~ fill ~ ~1 ~ ~ ~1 ~ light_block 15 replace air\","` |
| `Sword_B/animation_controllers/glowstone_sword.json:14` | `fill` | `"          \t\"/execute @p ~~~ fill ~5 ~5 ~5 ~-5 ~-5 ~-5 air 0 replace light_block 15\","` |
| `Sword_B/animation_controllers/glowstone_sword.json:15` | `fill` | `"          \t\"/execute @p ~~~ fill ~ ~1 ~ ~ ~1 ~ light_block 15 replace air\","` |
| `Sword_B/animation_controllers/glowstone_sword.json:26` | `fill` | `"          \t\"/execute @p ~~~ fill ~ ~1 ~ ~ ~1 ~ light_block 15 replace air\","` |
| `Sword_B/animation_controllers/glowstone_sword.json:27` | `fill` | `"          \t\"/execute @p ~~~ fill ~5 ~5 ~5 ~-5 ~-5 ~-5 air 0 replace light_block 15\","` |
| `Sword_B/animation_controllers/glowstone_sword.json:28` | `fill` | `"          \t\"/execute @p ~~~ fill ~ ~1 ~ ~ ~1 ~ light_block 15 replace air\","` |
| `Sword_B/animation_controllers/grass_sword.json:13` | `fill` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ air 0 fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 grass 0 replace dirt\","` |
| `Sword_B/animation_controllers/grass_sword.json:14` | `fill` | `"            \"/execute @a ~ ~ ~ detect ~ ~-1 ~ grass 0 fill ~ ~ ~ ~ ~ ~ tallgrass 0 replace air\","` |
| `Sword_B/animation_controllers/grass_sword.json:15` | `fill` | `"            \"/execute @e[r=10] ~ ~ ~ detect ~ ~-1 ~ grass 0 fill ~ ~ ~ ~ ~ ~ tallgrass 0 replace air\","` |
| `Sword_B/animation_controllers/grass_sword.json:26` | `fill` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ air 0 fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 grass 0 replace dirt\","` |
| `Sword_B/animation_controllers/grass_sword.json:27` | `fill` | `"            \"/execute @a ~ ~ ~ detect ~ ~-1 ~ grass 0 fill ~ ~ ~ ~ ~ ~ tallgrass 0 replace air\","` |
| `Sword_B/animation_controllers/grass_sword.json:28` | `fill` | `"            \"/execute @e[r=10] ~ ~ ~ detect ~ ~-1 ~ grass 0 fill ~ ~ ~ ~ ~ ~ tallgrass 0 replace air\","` |
| `Sword_B/animation_controllers/ice_sword.json:23` | `fill` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ air 0 fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 ice 0 replace water 0\","` |
| `Sword_B/animation_controllers/ice_sword.json:24` | `fill` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ air 0 fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 ice 0 replace flowing_water 0\","` |
| `Sword_B/animation_controllers/ice_sword.json:25` | `fill` | `"            \"/execute @e[type=zombie,rm=5,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 ice 0 replace air 0\","` |
| `Sword_B/animation_controllers/ice_sword.json:26` | `fill` | `"            \"/execute @e[type=creeper,rm=5,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 ice 0 replace air 0\","` |
| `Sword_B/animation_controllers/ice_sword.json:27` | `fill` | `"            \"/execute @e[type=zombie_villager,rm=5,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 ice 0 replace air 0\","` |
| `Sword_B/animation_controllers/ice_sword.json:28` | `fill` | `"            \"/execute @e[type=phantom,rm=5,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 ice 0 replace air 0\","` |
| `Sword_B/animation_controllers/ice_sword.json:29` | `fill` | `"            \"/execute @e[type=witch,rm=5,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 ice 0 replace air 0\","` |
| `Sword_B/animation_controllers/ice_sword.json:30` | `fill` | `"            \"/execute @e[type=skeleton,rm=5,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 ice 0 replace air 0\","` |
| `Sword_B/animation_controllers/ice_sword.json:31` | `fill` | `"            \"/execute @e[type=stray,rm=5,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 ice 0 replace air 0\","` |
| `Sword_B/animation_controllers/ice_sword.json:32` | `fill` | `"            \"/execute @e[type=husk,rm=5,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 ice 0 replace air 0\","` |
| `Sword_B/animation_controllers/ice_sword.json:33` | `fill` | `"            \"/execute @e[type=drowned,rm=5,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 ice 0 replace air 0\","` |
| `Sword_B/animation_controllers/ice_sword.json:34` | `fill` | `"            \"/execute @e[type=enderman,rm=5,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~3 ~-1 ice 0 replace air 0\","` |
| `Sword_B/animation_controllers/ice_sword.json:35` | `fill` | `"            \"/execute @e[type=silverfish,rm=5,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 ice 0 replace air 0\","` |
| `Sword_B/animation_controllers/ice_sword.json:36` | `fill` | `"            \"/execute @e[type=spider,rm=5,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 ice 0 replace air 0\","` |
| `Sword_B/animation_controllers/ice_sword.json:37` | `fill` | `"            \"/execute @e[type=cave_spider,rm=5,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 ice 0 replace air 0\","` |
| `Sword_B/animation_controllers/ice_sword.json:38` | `fill` | `"            \"/execute @e[r=12,rm=5,type=slime] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 ice 0 replace air 0\","` |
| `Sword_B/animation_controllers/ice_sword.json:40` | `fill` | `"            \"/execute @e[r=12,rm=5,type=evocation_fang] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 ice 0 replace air 0\","` |
| `Sword_B/animation_controllers/ice_sword.json:41` | `fill` | `"            \"/execute @e[r=12,rm=5,type=evocation_illager] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 ice 0 replace air 0\","` |
| `Sword_B/animation_controllers/ice_sword.json:42` | `fill` | `"            \"/execute @e[r=12,rm=5,type=vex] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 ice 0 replace air 0\","` |
| `Sword_B/animation_controllers/ice_sword.json:43` | `fill` | `"            \"/execute @e[r=12,rm=5,type=ravager] ~ ~ ~ fill ~2 ~-1 ~2 ~-2 ~2 ~-2 ice 0 replace air 0\","` |
| `Sword_B/animation_controllers/ice_sword.json:44` | `fill` | `"            \"/execute @e[r=12,rm=5,type=endermite] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 ice 0 replace air 0\","` |
| `Sword_B/animation_controllers/ice_sword.json:45` | `fill` | `"            \"/execute @e[r=12,rm=5,type=guardian] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 ice 0 replace air 0\","` |
| `Sword_B/animation_controllers/ice_sword.json:46` | `fill` | `"            \"/execute @e[r=12,rm=5,type=vindicator] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 ice 0 replace air 0\","` |
| `Sword_B/animation_controllers/ice_sword.json:47` | `fill` | `"            \"/execute @e[r=12,rm=5,type=tnt] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 ice 0 replace air 0\","` |
| `Sword_B/animation_controllers/jungle_sword.json:23` | `fill` | `"          \t\"/execute @p ~~~ detect ~1 ~1 ~ log 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:24` | `fill` | `"          \t\"/execute @p ~~~ detect ~-1 ~1 ~ log 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:25` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~1 log 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:26` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~-1 log 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:27` | `fill` | `"          \t\"/execute @p ~~~ detect ~1 ~1 ~ log 1 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:28` | `fill` | `"          \t\"/execute @p ~~~ detect ~-1 ~1 ~ log 1 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:29` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~1 log 1 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:30` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~-1 log 1 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:31` | `fill` | `"          \t\"/execute @p ~~~ detect ~1 ~1 ~ log 2 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:32` | `fill` | `"          \t\"/execute @p ~~~ detect ~-1 ~1 ~ log 2 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:33` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~1 log 2 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:34` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~-1 log 2 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:35` | `fill` | `"          \t\"/execute @p ~~~ detect ~1 ~1 ~ log 3 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:36` | `fill` | `"          \t\"/execute @p ~~~ detect ~-1 ~1 ~ log 3 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:37` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~1 log 3 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:38` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~-1 log 3 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:39` | `fill` | `"          \t\"/execute @p ~~~ detect ~1 ~1 ~ log2 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:40` | `fill` | `"          \t\"/execute @p ~~~ detect ~-1 ~1 ~ log2 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:41` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~1 log2 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:42` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~-1 log2 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:43` | `fill` | `"          \t\"/execute @p ~~~ detect ~1 ~1 ~ log2 1 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:44` | `fill` | `"          \t\"/execute @p ~~~ detect ~-1 ~1 ~ log2 1 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:45` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~1 log2 1 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:46` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~-1 log2 1 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:47` | `fill` | `"          \t\"/execute @p ~~~ detect ~1 ~1 ~ stone 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:48` | `fill` | `"          \t\"/execute @p ~~~ detect ~-1 ~1 ~ stone 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:49` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~1 stone 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:50` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~-1 stone 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:51` | `fill` | `"          \t\"/execute @p ~~~ detect ~1 ~1 ~ cobblestone 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:52` | `fill` | `"          \t\"/execute @p ~~~ detect ~-1 ~1 ~ cobblestone 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:53` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~1 cobblestone 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:54` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~-1 cobblestone 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:55` | `fill` | `"          \t\"/execute @p ~~~ detect ~1 ~1 ~ dirt 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:56` | `fill` | `"          \t\"/execute @p ~~~ detect ~-1 ~1 ~ dirt 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:57` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~1 dirt 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:58` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~-1 dirt 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:59` | `fill` | `"          \t\"/execute @p ~~~ detect ~1 ~1 ~ leaves 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:60` | `fill` | `"          \t\"/execute @p ~~~ detect ~-1 ~1 ~ leaves 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:61` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~1 leaves 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:62` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~-1 leaves 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:63` | `fill` | `"          \t\"/execute @p ~~~ detect ~1 ~1 ~ leaves 1 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:64` | `fill` | `"          \t\"/execute @p ~~~ detect ~-1 ~1 ~ leaves 1 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:65` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~1 leaves 1 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:66` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~-1 leaves 1 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:67` | `fill` | `"          \t\"/execute @p ~~~ detect ~1 ~1 ~ leaves 2 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:68` | `fill` | `"          \t\"/execute @p ~~~ detect ~-1 ~1 ~ leaves 2 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:69` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~1 leaves 2 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:70` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~-1 leaves 2 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:71` | `fill` | `"          \t\"/execute @p ~~~ detect ~1 ~1 ~ leaves 3 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:72` | `fill` | `"          \t\"/execute @p ~~~ detect ~-1 ~1 ~ leaves 3 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:73` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~1 leaves 3 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:74` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~-1 leaves 3 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:75` | `fill` | `"          \t\"/execute @p ~~~ detect ~1 ~1 ~ leaves2 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:76` | `fill` | `"          \t\"/execute @p ~~~ detect ~-1 ~1 ~ leaves2 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:77` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~1 leaves2 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:78` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~-1 leaves2 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:79` | `fill` | `"          \t\"/execute @p ~~~ detect ~1 ~1 ~ leaves2 1 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:80` | `fill` | `"          \t\"/execute @p ~~~ detect ~-1 ~1 ~ leaves2 1 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:81` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~1 leaves2 1 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:82` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~-1 leaves2 1 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:83` | `fill` | `"          \t\"/execute @p ~~~ detect ~1 ~1 ~ planks 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:84` | `fill` | `"          \t\"/execute @p ~~~ detect ~-1 ~1 ~ planks 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:85` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~1 planks 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:86` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~-1 planks 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:87` | `fill` | `"          \t\"/execute @p ~~~ detect ~1 ~1 ~ planks 1 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:88` | `fill` | `"          \t\"/execute @p ~~~ detect ~-1 ~1 ~ planks 1 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:89` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~1 planks 1 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:90` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~-1 planks 1 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:91` | `fill` | `"          \t\"/execute @p ~~~ detect ~1 ~1 ~ planks 2 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:92` | `fill` | `"          \t\"/execute @p ~~~ detect ~-1 ~1 ~ planks 2 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:93` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~1 planks 2 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:94` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~-1 planks 2 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:95` | `fill` | `"          \t\"/execute @p ~~~ detect ~1 ~1 ~ planks 3 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:96` | `fill` | `"          \t\"/execute @p ~~~ detect ~-1 ~1 ~ planks 3 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:97` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~1 planks 3 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:98` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~-1 planks 3 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:99` | `fill` | `"          \t\"/execute @p ~~~ detect ~1 ~1 ~ planks 4 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:100` | `fill` | `"          \t\"/execute @p ~~~ detect ~-1 ~1 ~ planks 4 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:101` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~1 planks 4 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:102` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~-1 planks 4 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:103` | `fill` | `"          \t\"/execute @p ~~~ detect ~1 ~1 ~ planks 5 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:104` | `fill` | `"          \t\"/execute @p ~~~ detect ~-1 ~1 ~ planks 5 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:105` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~1 planks 5 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:106` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~-1 planks 5 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:107` | `fill` | `"          \t\"/execute @p ~~~ detect ~1 ~1 ~ grass 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:108` | `fill` | `"          \t\"/execute @p ~~~ detect ~-1 ~1 ~ grass 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:109` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~1 grass 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:110` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~-1 grass 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:111` | `fill` | `"          \t\"/execute @p ~~~ detect ~1 ~1 ~ netherrack 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:112` | `fill` | `"          \t\"/execute @p ~~~ detect ~-1 ~1 ~ netherrack 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:113` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~1 netherrack 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:114` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~-1 netherrack 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:115` | `fill` | `"          \t\"/execute @p ~~~ detect ~1 ~1 ~ nether_brick 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:116` | `fill` | `"          \t\"/execute @p ~~~ detect ~-1 ~1 ~ nether_brick 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:117` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~1 nether_brick 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:118` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~-1 nether_brick 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:119` | `fill` | `"          \t\"/execute @p ~~~ detect ~1 ~1 ~ sand 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:120` | `fill` | `"          \t\"/execute @p ~~~ detect ~-1 ~1 ~ sand 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:121` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~1 sand 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:122` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~-1 sand 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:123` | `fill` | `"          \t\"/execute @p ~~~ detect ~1 ~1 ~ glass 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:124` | `fill` | `"          \t\"/execute @p ~~~ detect ~-1 ~1 ~ glass 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:125` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~1 glass 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:126` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~-1 glass 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:127` | `fill` | `"          \t\"/execute @p ~~~ detect ~1 ~1 ~ obsidian 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:128` | `fill` | `"          \t\"/execute @p ~~~ detect ~-1 ~1 ~ obsidian 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:129` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~1 obsidian 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:130` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~-1 obsidian 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:131` | `fill` | `"          \t\"/execute @p ~~~ detect ~1 ~1 ~ end_stone 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:132` | `fill` | `"          \t\"/execute @p ~~~ detect ~-1 ~1 ~ end_stone 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:133` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~1 end_stone 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:134` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~-1 end_stone 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:135` | `fill` | `"          \t\"/execute @p ~~~ detect ~1 ~1 ~ sandstone 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:136` | `fill` | `"          \t\"/execute @p ~~~ detect ~-1 ~1 ~ sandstone 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:137` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~1 sandstone 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:138` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~-1 sandstone 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:139` | `fill` | `"          \t\"/execute @p ~~~ detect ~1 ~1 ~ gravel 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:140` | `fill` | `"          \t\"/execute @p ~~~ detect ~-1 ~1 ~ gravel 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:141` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~1 gravel 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:142` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~-1 gravel 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:143` | `fill` | `"          \t\"/execute @p ~~~ detect ~1 ~1 ~ stone 1 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:144` | `fill` | `"          \t\"/execute @p ~~~ detect ~-1 ~1 ~ stone 1 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:145` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~1 stone 1 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:146` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~-1 stone 1 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:147` | `fill` | `"          \t\"/execute @p ~~~ detect ~1 ~1 ~ stone 3 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:148` | `fill` | `"          \t\"/execute @p ~~~ detect ~-1 ~1 ~ stone 3 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:149` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~1 stone 3 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:150` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~-1 stone 3 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:151` | `fill` | `"          \t\"/execute @p ~~~ detect ~1 ~1 ~ stone 5 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:152` | `fill` | `"          \t\"/execute @p ~~~ detect ~-1 ~1 ~ stone 5 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:153` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~1 stone 5 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:154` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~-1 stone 5 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:155` | `fill` | `"          \t\"/execute @p ~~~ detect ~1 ~1 ~ snow 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:156` | `fill` | `"          \t\"/execute @p ~~~ detect ~-1 ~1 ~ snow 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:157` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~1 snow 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:158` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~-1 snow 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:159` | `fill` | `"          \t\"/execute @p ~~~ detect ~1 ~1 ~ packed_ice 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:160` | `fill` | `"          \t\"/execute @p ~~~ detect ~-1 ~1 ~ packed_ice 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:161` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~1 packed_ice 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:162` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~-1 packed_ice 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:163` | `fill` | `"          \t\"/execute @p ~~~ detect ~1 ~1 ~ ice 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:164` | `fill` | `"          \t\"/execute @p ~~~ detect ~-1 ~1 ~ ice 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:165` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~1 ice 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air\","` |
| `Sword_B/animation_controllers/jungle_sword.json:166` | `fill` | `"          \t\"/execute @p ~~~ detect ~ ~1 ~-1 ice 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air\","` |
| `Sword_B/animation_controllers/magma_sword.json:14` | `fill` | `"          \t\"/execute @p ~ ~ ~ fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 magma 0 replace lava\","` |
| `Sword_B/animation_controllers/magma_sword.json:15` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=zombie] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:16` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=husk] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:17` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=drowned] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:18` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=creeper] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:19` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=enderman] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:20` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=slime] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:21` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=skeleton] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:22` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=stray] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:23` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=witch] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:24` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=spider] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:25` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=cave_spider] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:26` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=silverfish] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:27` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=evocation_fang] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:28` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=evocation_illager] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:29` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=vex] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:30` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=ravager] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:31` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=endermite] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:32` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=guardian] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:33` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=vindicator] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:34` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=phantom] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:35` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=zombie_villager] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:47` | `fill` | `"          \t\"/execute @p ~ ~ ~ fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 magma 0 replace lava\","` |
| `Sword_B/animation_controllers/magma_sword.json:48` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=zombie] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:49` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=husk] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:50` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=drowned] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:51` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=creeper] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:52` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=enderman] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:53` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=slime] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:54` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=skeleton] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:55` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=stray] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:56` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=witch] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:57` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=spider] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:58` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=cave_spider] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:59` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=silverfish] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:60` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=evocation_fang] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:61` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=evocation_illager] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:62` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=vex] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:63` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=ravager] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:64` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=endermite] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:65` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=guardian] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:66` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=vindicator] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:67` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=phantom] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/magma_sword.json:68` | `setblock` | `"            \"/execute @e[r=15,rm=2,type=zombie_villager] ~ ~ ~ setblock ~ ~ ~ fire\","` |
| `Sword_B/animation_controllers/obsidian_sword.json:13` | `fill` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ air 0 fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 obsidian 0 replace lava 0\","` |
| `Sword_B/animation_controllers/obsidian_sword.json:14` | `fill` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ air 0 fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 obsidian 0 replace flowing_lava 0\","` |
| `Sword_B/animation_controllers/obsidian_sword.json:35` | `fill` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ air 0 fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 obsidian 0 replace lava 0\","` |
| `Sword_B/animation_controllers/obsidian_sword.json:36` | `fill` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ air 0 fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 obsidian 0 replace flowing_lava 0\",    "` |
| `Sword_B/animation_controllers/spectral_sword.json:13` | `fill` | `"            \"/execute @p ~~~ fill ~6 ~6 ~6 ~-6 ~-6 ~-6 barrier 0 replace stone 0\","` |
| `Sword_B/animation_controllers/spectral_sword.json:14` | `fill` | `"            \"/fill ~7 ~8 ~8 ~8 ~-8 ~-8 stone 0 replace barrier\","` |
| `Sword_B/animation_controllers/spectral_sword.json:15` | `fill` | `"            \"/fill ~-7 ~-8 ~-8 ~-8 ~8 ~8 stone 0 replace barrier\","` |
| `Sword_B/animation_controllers/spectral_sword.json:16` | `fill` | `"            \"/fill ~-6 ~8 ~7 ~6 ~-8 ~8 stone 0 replace barrier\","` |
| `Sword_B/animation_controllers/spectral_sword.json:17` | `fill` | `"            \"/fill ~6 ~-8 ~-7 ~-6 ~8 ~-8 stone 0 replace barrier\","` |
| `Sword_B/animation_controllers/spectral_sword.json:18` | `fill` | `"            \"/fill ~8 ~-8 ~8 ~-8 ~-7 ~-8 stone 0 replace barrier\","` |
| `Sword_B/animation_controllers/spectral_sword.json:19` | `fill` | `"            \"/fill ~8 ~8 ~8 ~-8 ~7 ~-8 stone 0 replace barrier\","` |
| `Sword_B/animation_controllers/spectral_sword.json:30` | `fill` | `"            \"/execute @p ~~~ fill ~6 ~6 ~6 ~-6 ~-6 ~-6 barrier 0 replace stone 0\","` |
| `Sword_B/animation_controllers/spectral_sword.json:31` | `fill` | `"            \"/fill ~7 ~8 ~8 ~8 ~-8 ~-8 stone 0 replace barrier\","` |
| `Sword_B/animation_controllers/spectral_sword.json:32` | `fill` | `"            \"/fill ~-7 ~-8 ~-8 ~-8 ~8 ~8 stone 0 replace barrier\","` |
| `Sword_B/animation_controllers/spectral_sword.json:33` | `fill` | `"            \"/fill ~-6 ~8 ~7 ~6 ~-8 ~8 stone 0 replace barrier\","` |
| `Sword_B/animation_controllers/spectral_sword.json:34` | `fill` | `"            \"/fill ~6 ~-8 ~-7 ~-6 ~8 ~-8 stone 0 replace barrier\","` |
| `Sword_B/animation_controllers/spectral_sword.json:35` | `fill` | `"            \"/fill ~8 ~-8 ~8 ~-8 ~-7 ~-8 stone 0 replace barrier\","` |
| `Sword_B/animation_controllers/spectral_sword.json:36` | `fill` | `"            \"/fill ~8 ~8 ~8 ~-8 ~7 ~-8 stone 0 replace barrier\","` |
| `Sword_B/animation_controllers/spider_sword.json:14` | `fill` | `"          \t\"/execute @p ~ ~ ~ detect ~ ~ ~ web 0 fill ~ ~ ~ ~ ~ ~ air 0 replace web\","` |
| `Sword_B/animation_controllers/spider_sword.json:15` | `fill` | `"          \t\"/execute @p ~ ~ ~ detect ~ ~1 ~ web 0 fill ~ ~1 ~ ~ ~1 ~ air 0 replace web\","` |
| `Sword_B/animation_controllers/spider_sword.json:18` | `fill` | `"            \"/execute @e[r=5,type=zombie] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:19` | `fill` | `"            \"/execute @e[r=5,type=creeper] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:20` | `fill` | `"            \"/execute @e[r=5,type=husk] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:21` | `fill` | `"            \"/execute @e[r=5,type=drowned] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:22` | `fill` | `"            \"/execute @e[r=5,type=enderman] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:23` | `fill` | `"            \"/execute @e[r=5,type=slime] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:24` | `fill` | `"            \"/execute @e[r=5,type=skeleton] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:25` | `fill` | `"            \"/execute @e[r=5,type=stray] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:26` | `fill` | `"            \"/execute @e[r=5,type=blaze] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:27` | `fill` | `"            \"/execute @e[r=5,type=wither_skeleton] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:28` | `fill` | `"            \"/execute @e[r=5,type=witch] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:29` | `fill` | `"            \"/execute @e[r=5,type=magma_cube] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:30` | `fill` | `"            \"/execute @e[r=5,type=ghast] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:31` | `fill` | `"            \"/execute @e[r=5,type=zombie_pigman] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:32` | `fill` | `"            \"/execute @e[r=5,type=silverfish] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:33` | `fill` | `"            \"/execute @e[r=5,type=evocation_fang] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:34` | `fill` | `"            \"/execute @e[r=5,type=evocation_illager] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:35` | `fill` | `"            \"/execute @e[r=5,type=vex] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:36` | `fill` | `"            \"/execute @e[r=5,type=ravager] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:37` | `fill` | `"            \"/execute @e[r=5,type=endermite] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:38` | `fill` | `"            \"/execute @e[r=5,type=guardian] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:39` | `fill` | `"            \"/execute @e[r=5,type=vindicator] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:40` | `fill` | `"            \"/execute @e[r=5,type=phantom] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:41` | `fill` | `"            \"/execute @e[r=5,type=tnt] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:42` | `fill` | `"            \"/execute @e[r=5,type=zombie_villager] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:58` | `fill` | `"          \t\"/execute @p ~ ~ ~ detect ~ ~ ~ web 0 fill ~ ~ ~ ~ ~ ~ air 0 replace web\","` |
| `Sword_B/animation_controllers/spider_sword.json:59` | `fill` | `"          \t\"/execute @p ~ ~ ~ detect ~ ~1 ~ web 0 fill ~ ~1 ~ ~ ~1 ~ air 0 replace web\","` |
| `Sword_B/animation_controllers/spider_sword.json:62` | `fill` | `"            \"/execute @e[r=5,type=zombie] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:63` | `fill` | `"            \"/execute @e[r=5,type=creeper] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:64` | `fill` | `"            \"/execute @e[r=5,type=husk] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:65` | `fill` | `"            \"/execute @e[r=5,type=drowned] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:66` | `fill` | `"            \"/execute @e[r=5,type=enderman] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:67` | `fill` | `"            \"/execute @e[r=5,type=slime] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:68` | `fill` | `"            \"/execute @e[r=5,type=skeleton] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:69` | `fill` | `"            \"/execute @e[r=5,type=stray] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:70` | `fill` | `"            \"/execute @e[r=5,type=blaze] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:71` | `fill` | `"            \"/execute @e[r=5,type=wither_skeleton] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:72` | `fill` | `"            \"/execute @e[r=5,type=witch] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:73` | `fill` | `"            \"/execute @e[r=5,type=magma_cube] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:74` | `fill` | `"            \"/execute @e[r=5,type=ghast] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:75` | `fill` | `"            \"/execute @e[r=5,type=zombie_pigman] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:76` | `fill` | `"            \"/execute @e[r=5,type=silverfish] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:77` | `fill` | `"            \"/execute @e[r=5,type=evocation_fang] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:78` | `fill` | `"            \"/execute @e[r=5,type=evocation_illager] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:79` | `fill` | `"            \"/execute @e[r=5,type=vex] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:80` | `fill` | `"            \"/execute @e[r=5,type=ravager] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:81` | `fill` | `"            \"/execute @e[r=5,type=endermite] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:82` | `fill` | `"            \"/execute @e[r=5,type=guardian] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:83` | `fill` | `"            \"/execute @e[r=5,type=vindicator] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:84` | `fill` | `"            \"/execute @e[r=5,type=phantom] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:85` | `fill` | `"            \"/execute @e[r=5,type=tnt] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/spider_sword.json:86` | `fill` | `"            \"/execute @e[r=5,type=zombie_villager] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air\","` |
| `Sword_B/animation_controllers/sponge_sword.json:13` | `fill` | `"            \"/execute @a ~ ~ ~ fill ~4 ~4 ~4 ~-4 ~-4 ~-4 sponge 0 replace water\","` |
| `Sword_B/animation_controllers/sponge_sword.json:14` | `fill` | `"            \"/execute @a ~ ~ ~ fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace sponge\","` |
| `Sword_B/animation_controllers/sponge_sword.json:15` | `fill` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ water 0 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass\","` |
| `Sword_B/animation_controllers/sponge_sword.json:16` | `fill` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ water 1 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass\","` |
| `Sword_B/animation_controllers/sponge_sword.json:17` | `fill` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ water 2 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass\","` |
| `Sword_B/animation_controllers/sponge_sword.json:18` | `fill` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ water 3 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass\","` |
| `Sword_B/animation_controllers/sponge_sword.json:19` | `fill` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ water 4 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass\","` |
| `Sword_B/animation_controllers/sponge_sword.json:20` | `fill` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ water 5 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass\","` |
| `Sword_B/animation_controllers/sponge_sword.json:21` | `fill` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ water 6 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass\","` |
| `Sword_B/animation_controllers/sponge_sword.json:22` | `fill` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ water 7 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass\","` |
| `Sword_B/animation_controllers/sponge_sword.json:23` | `fill` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ water 8 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass\","` |
| `Sword_B/animation_controllers/sponge_sword.json:24` | `fill` | `"            \"/execute @a ~ ~ ~ detect ~ ~1 ~ air 0 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass\","` |
| `Sword_B/animation_controllers/sponge_sword.json:35` | `fill` | `"            \"/execute @a ~ ~ ~ fill ~4 ~4 ~4 ~-4 ~-4 ~-4 sponge 0 replace water\","` |
| `Sword_B/animation_controllers/sponge_sword.json:36` | `fill` | `"            \"/execute @a ~ ~ ~ fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace sponge\","` |
| `Sword_B/animation_controllers/sponge_sword.json:37` | `fill` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ water 0 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass\","` |
| `Sword_B/animation_controllers/sponge_sword.json:38` | `fill` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ water 1 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass\","` |
| `Sword_B/animation_controllers/sponge_sword.json:39` | `fill` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ water 2 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass\","` |
| `Sword_B/animation_controllers/sponge_sword.json:40` | `fill` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ water 3 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass\","` |
| `Sword_B/animation_controllers/sponge_sword.json:41` | `fill` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ water 4 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass\","` |
| `Sword_B/animation_controllers/sponge_sword.json:42` | `fill` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ water 5 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass\","` |
| `Sword_B/animation_controllers/sponge_sword.json:43` | `fill` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ water 6 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass\","` |
| `Sword_B/animation_controllers/sponge_sword.json:44` | `fill` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ water 7 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass\","` |
| `Sword_B/animation_controllers/sponge_sword.json:45` | `fill` | `"            \"/execute @a ~ ~ ~ detect ~ ~ ~ water 8 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass\","` |
| `Sword_B/animation_controllers/sponge_sword.json:46` | `fill` | `"            \"/execute @a ~ ~ ~ detect ~ ~1 ~ air 0 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass\","` |
| `Sword_B/animation_controllers/wither_sword.json:25` | `fill` | `"            \"/fill ~5 ~5 ~5 ~-5 ~-5 ~-5 dirt 1 replace grass\","` |
| `Sword_B/animation_controllers/wither_sword.json:26` | `fill` | `"            \"/fill ~5 ~5 ~5 ~-5 ~-5 ~-5 air 0 replace leaves2\","` |
| `Sword_B/animation_controllers/wither_sword.json:27` | `fill` | `"            \"/fill ~5 ~5 ~5 ~-5 ~-5 ~-5 air 0 replace leaves\","` |
| `Sword_B/animation_controllers/wither_sword.json:28` | `fill` | `"            \"/fill ~5 ~5 ~5 ~-5 ~-5 ~-5 water 0 replace ice\","` |
| `Sword_B/animation_controllers/wither_sword.json:29` | `fill` | `"            \"/fill ~5 ~5 ~5 ~-5 ~-5 ~-5 dirt 0 replace farmland\","` |
| `Sword_B/animation_controllers/wither_sword.json:30` | `fill` | `"            \"/fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace red_flower\","` |
| `Sword_B/animation_controllers/wither_sword.json:31` | `fill` | `"            \"/fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace yellow_flower\","` |
| `Sword_B/animation_controllers/wither_sword.json:32` | `fill` | `"            \"/fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace red_mushroom\","` |
| `Sword_B/animation_controllers/wither_sword.json:33` | `fill` | `"            \"/fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace brown_mushroom\","` |
| `Sword_B/animation_controllers/wither_sword.json:34` | `fill` | `"            \"/fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace double_plant\","` |
| `Sword_B/functions/normal.mcfunction:10` | `fill` | `"fill ~7 ~8 ~8 ~8 ~-8 ~-8 stone 0 replace barrier"` |
| `Sword_B/functions/normal.mcfunction:11` | `fill` | `"fill ~-7 ~-8 ~-8 ~-8 ~8 ~8 stone 0 replace barrier"` |
| `Sword_B/functions/normal.mcfunction:12` | `fill` | `"fill ~-6 ~8 ~7 ~6 ~-8 ~8 stone 0 replace barrier"` |
| `Sword_B/functions/normal.mcfunction:13` | `fill` | `"fill ~6 ~-8 ~-7 ~-6 ~8 ~-8 stone 0 replace barrier"` |
| `Sword_B/functions/normal.mcfunction:14` | `fill` | `"fill ~8 ~-8 ~8 ~-8 ~-7 ~-8 stone 0 replace barrier"` |
| `Sword_B/functions/normal.mcfunction:15` | `fill` | `"fill ~8 ~8 ~8 ~-8 ~7 ~-8 stone 0 replace barrier"` |
| `Sword_B/functions/normal.mcfunction:16` | `fill` | `"fill ~6 ~6 ~6 ~-6 ~-6 ~-6 stone 0 replace barrier"` |
| `Sword_B/functions/normal.mcfunction:20` | `fill` | `"execute @p ~~~ fill ~5 ~5 ~5 ~-5 ~-5 ~-5 air 0 replace light_block 15"` |

Условия и полные определения: [реестр мира](world-ledger-1.6.md), [реестр сущностей](entity-ledger-1.6.md), [предметы](items-1.6.md).
