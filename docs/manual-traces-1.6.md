# Первичные ручные цепочки архива 1.6

Это не полный построчный аудит 1.6. Имена `Sword_B`/`Sword_R` и номера строк — внутри `sources/SwordsAndMoreSwords.1.6.mcaddon`, а не в 2.8.x. Полные определения предметов — в [карточках 1.6](items-1.6.md), машинные [изменения относительно 2.8.14](version-lines-1.6-to-2.8.14.md) не доказывают смысловой эквивалентности. Старый синтаксис, события, компоненты и парсер необходимо проверить на подходящей игре.

## Общая архитектура игрока

[Подробный разбор изменения мира пятью helper и их командных контекстов](manual-world-helpers-1.6.md).

Подробная проверка пересекающихся сенсоров, глобального счётчика и очистки мира: [общие состояния 1.6](manual-global-state-1.6.md).

`Sword_B/entities/player.json` содержит environment sensor с проверками `has_equipment` в `domain:hand` для мечей. Одноимённое событие добавляет группу, которая для многих мечей использует `minecraft:spawn_entity` с min/max wait 0, num_to_spawn 1, single_use true и собственным `entity:*`. Часть вспомогательных сущностей запускает animation controller с командами. Это принципиально иная цепь, чем группа и команды непосредственно в игроке архива 2.8.14; совпадающий ID не является доказательством совпадающего поведения.

`player.json` также запускает `controller.animation.normal`, который попеременно переходит между default и normal с условием `1.0`, и при входе в оба состояния вызывает `function normalft`. `functions/normalft.mcfunction` создаёт objective `swords dummy`, вычитает 1 у всех игроков со score 1 или 2 и выполняет `function normal` от каждого игрока со score 0. `functions/normal.mcfunction` задаёт `gamerule commandblockoutput false`, `sendcommandfeedback false`, `randomtickspeed 1`, удаляет несколько scoreboard objectives, телепортирует некоторые вспомогательные сущности и восстанавливает barrier в объёмах вокруг игрока в **stone**, также заменяет `light_block 15` на air вокруг `@p`. Это глобальные gamerule/scoreboard и потенциально разрушительное восстановление блоков, а не просто сброс визуального состояния. Не следует предполагать конкретную частоту входов или успешность команд без проверки движка, прав и координат контекста.

## Coal Sword: 1.6 против 2.8.14

[Полная сравнительная карточка 1.6/2.x](manual-basic-swords.md#coal-sword).

- `Sword_B/items/coal_sword.json`: формат предмета 1.20.20, damage **6**, durability 121, enchantability 9/sword, allow_off_hand **true**, self repair 121, web speed 15 и bamboo 10; нет компонента fuel и явно заданных хуков weapon. В 2.8.14 damage 4, offhand false, есть fuel duration 360 и другие материалы ремонта. Это не косметическая разница; отсутствующие поля сами по себе не устанавливают движковые значения по умолчанию.
- `Sword_B/entities/player.json:204–214,520–533,925–931`: sensor по `effect:coal_sword` вызывает одноимённое событие, добавляющее группу со spawn_entity `entity:coal`, min/max wait 0, num 1, single_use true. Не предполагать число созданных объектов при повторных добавлениях группы без теста.
- `Sword_B/entities/coal.json`: family `despawnear`, `minecraft:despawn` с фильтром на эту family, health 1, collision 0×0, fire_immune true, physics и `controller.animation.coal`. Длительность жизни определяется движком, не установлена фиксированным числом в файле.
- `Sword_B/animation_controllers/coal_sword.json`: оба состояния default/coal переходят друг в друга по `1.0`, при входе каждое выполняет 13 отдельных команд `replaceitem block ... slot.container 1 coal` по соседним координатам и `scoreboard players set @a swords 2`. Если команды принимаются, они могут перезаписывать слот контейнера и менять глобальный счёт всех игроков; это не эквивалент компонента топлива у 2.8.14. Наличие контейнера, допустимость старого `replaceitem`, контекст координат и очередность с normalft требуют испытаний.

## Cactus Sword: 1.6 против 2.8.14

[Полная сравнительная карточка 1.6/2.x](manual-basic-swords.md#cactus-sword).

`Sword_B/items/cactus_sword.json`: damage 6, durability 125, enchantability 9/sword, repair self 125, offhand true, web 15/bamboo 10. Тот же ID в 2.8.14 имеет offhand false и другую механику повреждения. 1.6: sensor игрока добавляет группу спавна `entity:cactus`; он подключает `controller.animation.cactus` (`entities/cactus.json`, `animation_controllers/cactus_sword.json`). Оба состояния при входе выполняют одинаковую последовательность: создать objective `ct`, добавить 1 ближайшему `@p` и сущностям `@e[r=3,type=!entity:cactus,type=!player]`; ближайшему игроку со score ровно 1 и отдельно всем `@e[scores={ct=1},r=2]` назначить poison 1 с amplifier 1 и скрытыми частицами; при `@p[scores={ct=20}]` удалить objective `ct`; всем игрокам `swords=2`. Это команды яда, не прямые `damage ... contact` из 2.8.14. Селекторы, ошибки повторного создания objective и конфликт счётчиков имеют значение; длительность и период действия не доказаны без игры.

## Emerald Sword: 1.6 против 2.8.14

[Полная сравнительная карточка 1.6/2.x](manual-basic-swords.md#emerald-sword).

`items/emerald_sword.json`: damage 7, durability 2300, enchantable 9, self repair 2300, offhand true. Sensor → группа → `entity:emerald` → `controller.animation.emerald`: при входе в оба состояния команды `/effect @p village_hero 16 0 true` и `/scoreboard players set @a swords 2`, без явной проверки деревни и без команд resistance для жителей. В 2.8.14, напротив, `is_in_village` является фильтром и effect для жителей имеет r=64. `@p` в контроллере 1.6 — ближайший к исполняющей сущности игрок, не заведомо владелец меча.

## Sponge Sword: 1.6 против 2.8.14

`items/sponge_sword.json`: damage 6, durability 128, enchantable 9, repair self 128, offhand true. В 2.8.14 damage 5, нет компонента enchantable, есть ремонт губкой и мокрая версия с отдельным счётчиком. Контроллер 1.6 `animation_controllers/sponge_sword.json` при входе в оба состояния выполняет `execute @a ... fill` в кубе **9×9×9** относительно каждого игрока: water→sponge, затем sponge→air. Далее девять отдельных проверок water data 0…8 в позиции игрока и отдельная проверка air на y+1, каждая с `fill ... air replace seagrass`. Команда удаления губки не отличает созданную губку от уже имеющейся, а селектор `@a` распространяет действия на всех игроков. Порядок команд может сделать предыдущую замену воды значимой для последующих detect; проверить движок и кратность.

## Creeper Sword и TNT Sword: 1.6

[Массовые цели Ender/Wither/Creeper/TNT и матрица типов](manual-area-targets-1.6.md).

- `items/creeper_sword.json`: damage 8, durability 1500, enchantability 9, self repair 1500, offhand true; явного on-use/cooldown и weapon-event в определении нет. Sensor → `entity:creeper` → `controller.animation.creeper`. Оба состояния создают objective c, прибавляют 1 всем сущностям r=16, при `@p[c=90]` воспроизводят звук; 27 отдельных селекторов перечисленных типов с точным `c=100` и r=16 призывают `entity:explode`, при score ближайшего игрока c=300 удаляется objective, затем `@a swords 2`. Типы включают tnt и wither, но не все сущности; точный список и порядок — в [реестре](animation-ledger-1.6.md). Это не мини-криперы по вероятности 20/100 из 2.8.14.
- `items/tnt_sword.json`: damage 7, durability **1**, self repair 1, offhand true, enchantable не указан. Sensor → `entity:tnt_sword` → `controller.animation.tnt`; каждый вход обоих состояний содержит 26 команд summon `entity:explode` в точках указанных типов в кольце `rm=10,r=15`, потом устанавливает `swords=2` всем игрокам. Командой не проверяется использование предмета. `entities/explode.json`: `minecraft:explode` с legacy-ключами `fuseLength:0`, `fuseLit:true`, power 4, `causesFire:false`, destroy_affected_by_griefing true; это отдельный формат от `entity:tnt` и `minecraft:tnt` 2.8.14. Работоспособность camelCase, частота state transitions, радиусы и конфликт scoreboard нужно проверить.

## Sword of Time: 1.6

[Значки и render_offsets, включая разницу регистра client/atlas](item-visual-index.md).

Предмет называется `effect:sword_of_time` (не совпадает с `effect:time_sword` 2.8.14): `items/Sword of Time.json` задаёт damage 7, durability 128, enchantability 9, self repair 128, glint true, offhand true. `player.json` создаёт `entity:time`, который подключает `controller.animation.time`; оба состояния выполняют `gamerule randomtickspeed 300`, `effect @e speed 1 15 true`, `time add 30`, `scoreboard players set @a swords 2`. В отличие от Time Sword 2.8.14 selector `@e` не исключает игроков, и в архиве 1.6 отсутствует идентичный предмет ID `effect:time_sword`. `normal.mcfunction` задаёт randomtickspeed 1 без сохранения прежнего значения. Как часто контроллеры конкурируют друг с другом, устанавливается только испытаниями.

## Blaze и Bone: краткие различия и ошибки JSON 1.6

[Счётчики Blaze, Bone, Shulker, Slime и Lapis: порядок команд и межигровые риски](manual-counter-helpers-1.6.md).

`items/blaze_sword.json` задаёт damage 8 и offhand true (в 2.8.14 — 6 и false), `items/bone_sword.json` — damage 7 и offhand true (в 2.8.14 — 5 и false). Их сенсоры создают `entity:blaze`/`entity:bone`, контроллеры используют глобальные objectives `b`/`bn`, добавляют 1 ближайшему игроку, при ровно 10 призывают `entity:blaze2`/`entity:bone2`, при 5000 удаляют objective, при 4990 содержат буквальную команду `kill @e[...] ~ 0 ~`, далее `swords=2` всем игрокам. В архиве 1.6 вспомогательные `entities/blaze2.json` и `bone2.json` не разбираются JSON5; вывод об исполнении/работоспособности и старом синтаксисе kill нельзя делать только по тексту. Также 1.6 `shulker2.json` не проходит JSON5. Ни один из этих дефектов не исправлен в архиве.

### Что написано в повреждённых helper-файлах

В каждом из `blaze2.json`, `bone2.json`, `shulker2.json` JSON5 останавливается на **последней лишней закрывающей скобке** (строки 78, 75, 75 соответственно). Для диагностики в памяти удалена только последняя `}`: тогда каждый текст разбирается JSON5. Это гипотетическая структура, а не исправление архива и не свидетельство, что исходный Bedrock примет файл. Данные ниже непосредственно видны в исходном тексте:

| ID | health | collision | Цель `other` family monster / max_dist | Ranged attack | Shooter |
|---|---:|---|---:|---|---|
| `entity:blaze2` | 5/5 | 0×0 | 64; must_see false | priority 1, speed_multiplier 2, attack_interval 1, attack_radius 48, charge_shoot_trigger 1, charge_charged_trigger 1 | type `smallfireball`, def `minecraft:small_fireball` |
| `entity:bone2` | 5/5 | 0×0 | 64; must_see false | attack_interval_min 1, max 3, radius 48; priority не указан | type `Arrow`, def `minecraft:arrow` |
| `entity:shulker2` | 1/1 | 0×0 | 16; must_see false | priority 1, attack_interval_min 1, max 3, radius 15 | def `minecraft:shulker_bullet` |

У всех movement 0, follow_range value/max 64, 64 и 16 соответственно, persistent и pushable true, physics `{}`. Фактическое создание, выстрелы, интерпретация интервалов и дополнительная ошибка в команде kill контроллеров требуют проверки. Исправленная в памяти версия не используется как эталон для ремейка.

## Остальные предметы 1.6: первичные прямые цепочки

У каждого из следующих предметов `minecraft:allow_off_hand: true`; кроме Quartz, у перечисленных `minecraft:enchantable` = value 9, slot sword. Данные `damage/max_durability` приведены буквально. Все пункты — **первичная выборка**, не завершённый анализ получения, ресурсов, взаимодействий и исполнения; полные команды и точный список типов — в [контроллерах](animation-ledger-1.6.md), а sensor/spawn — в [индексе](chain-index-1.6.md). Заявленные эффекты относятся к командам, а не к доказанному их выполнению. Для всех пар состояний, перечисленных ниже, одинаковые команды входят в оба состояния, кроме Ice, Jungle и Wither.

- **Ender** — 9/1256; `controller.animation.ender`: портальные частицы у `@p`; objective e увеличивается у `@e[r=16]`; звуки при score ближайшего игрока 10, 90, 140, 300, 500; при 85 выполняется `spreadplayers ~ ~ 8 16 @s`. Также без этой проверки score отдельные команды `spreadplayers ~ ~ 8 16` для перечисленных типов `r=10,rm=5` относительно ближайшего игрока. Удаление objective назначено при 700 и 750, поэтому второе условие может быть недостижимо при последовательном штатном исполнении — это не доказательство фактической недостижимости в игре.
- **Fire** — 12/2000; fire resistance у `@p` на 10 с amplifier 0; постановка fire в позиции игрока при detect air; в кубе ±3 snow_layer→air, ice/blue_ice/packed_ice→water, snow→grass. Множество команд ставит fire в позиции конкретных типов существ `r=15,rm=2`, включая мирных животных и villager; реальные условия замены блоков и доступность команды надо проверить.
- **Glowstone** — 6/128; три команды в порядке: поставить light_block data 15 на блок выше ближайшего игрока, заменить light_block 15 на air в кубе ±5 вокруг него, снова поставить блок на высоте +1, затем scoreboard. Удаление не различает исходное происхождение световых блоков. Аргумент `~~~` оставлен в оригинале.
- **Grass** — 8/250; для каждого `@a` при detect air заменяет dirt на grass в плоскости y−1 ±2; при detect grass под игроком ставит tallgrass 0 на его позиции, и аналогично для `@e[r=10]` относительно контроллера. Это не эквивалент множества событий и мобов Grass 2.8.14.
- **Ice** — 11/500; состояние default содержит буквальную команду `/Effect99`, другое — 26 команд: `@a` при detect air создаёт лёд в плоскости 5×5 на y−1 заменой water 0 и flowing_water 0; перечисленные сущности `rm=5,r=12` окружаются ice заменой air, обычно 3×4×3, отличные размеры для enderman, ravager, мелких мобов и TNT. Для slime имеется также detect ice и `tp @s ~ ~ ~`. `/Effect99` не следует молча исправлять на функцию; переходы и старые команды требуют теста.
- **Jungle** — 4/128; default содержит `/commands`, а состояние jungle — 145 `on_entry` команд. Не предполагаем, что `/commands` успешно выполняется: полный текст, порядок и координаты — в реестре. Текстовое сопоставление с 148 строками функции 2.8.14 приведено ниже; полная семантическая эквивалентность не доказана.
- **Lapis** — 6/528; создаётся scoreboard l, ближайшему игроку прибавляется 1, при ровно 10 выполняется `xp 5 @s`, при 30 удаляется objective; длительность цикла и единица XP подлежат проверке движком.
- **Lightning** — 8/2000; отдельные команды `summon lightning_bolt` на перечисленных типах в диапазоне `r=16,rm=10`; затем глобальный scoreboard. Это не 41 вызов on-use из 2.8.14.
- **Magma** — 7/1000; ближайшему игроку fire_resistance 10 с amplifier 0; лава в плоскости y−1 ±2 заменяется magma; выборочным типам `r=15,rm=2` ставится fire по позиции. Не считать это вероятностной стрельбой Magma 2.8.14.
- **Obsidian** — 12/3000; для всех игроков при detect air lava 0 и flowing_lava 0 в плоскости y−1 ±2 заменяются obsidian 0. Дополнительные detect lava data 0…8 и flowing_lava 0 назначают fire_resistance 10 с amplifier 0. Покрытие других состояний текущей лавы не предполагается.
- **Quartz** — 600/1, glint true, enchantable в компонентах отсутствует, ремонт самим собой 1. Сенсор добавляет пустую `minecraft:quartz_sword` component group; в данной прямой цепи spawn/controller нет. Это не доказательство отсутствия любых других связей.
- **Sea** — 7/1000; guardian и drowned `r=6` получают fatal_poison 5 с amplifier 0; ближайший игрок получает conduit_power 16 с amplifier 0. В 2.8.14 отдельно исследована механика aquatic-движения, и переносить её в 1.6 без доказательства нельзя.
- **Shulker** — 7/1000; ближайшему игроку levitation 0, все `entity:shulker2` телепортируются к нему на y+2.5; глобальный objective sh, score 40 summon, 2390 команда kill с дополнительными `~ 0 ~`, 2400 удалить objective. `shulker2.json` не разобран JSON5; факт работы не установлен.
- **Slime** — 6/675; objective s, ближайшему игроку +1, при score 1 summon slime, jump_boost 1 с amplifier 5, при score 600 удалить objective. Нет доказательств, что это аналог mountable slime и Slime King 2.8.14.
- **Spectral** — 9/3256; вокруг `@p` stone 0 в кубе ±6 заменяется barrier 0, затем шесть slabs вокруг контроллера заменяют barrier на stone: x 7…8 и −8…−7, z 7…8 и −8…−7, y −8…−7 и 7…8 с поперечными пределами из команд. Это затрагивает и ранее существовавшие barrier в этих объёмах; никакого сохранения происхождения блоков в этих командах нет. При движении, исчезновении сущности и пересечении игроков восстановление не доказано.
- **Spider** — 6/628; ближайшему игроку poison 0, detect web удаляет паутину на позиции игрока и y+1; spider и cave_spider получают slowness 1 с amplifier 128 в r=6 относительно `@p`; отдельные перечисленные типы r=5 относительно контроллера получают web в позиции через fill replace air.
- **Wither** — 10/1256; default содержит буквальную `/Effect99`, состояние wither — 46 команд: poison 30 amplifier 1 на `@e[r=16,type=!player]`, частицы всем игрокам, затем вокруг контроллера куб ±5 с grass→dirt 1, leaves/leaves2→air, ice→water, farmland→dirt 0 и перечисленными растениями/грибами→wither_rose. Objective w увеличивается у r=16 с перечнем исключений; на score 100 перечисленные типы призывают `entity:explode`, звуки при score игрока 200/500, удаление objective при 600. Точные селекторы и порядок — в исходном тексте; сравнение с более поздней реализацией и сохранность мира не установлены.

## Grass Sword: 1.6 и теги 2.x

[Глобальные команды 1.6, ловушка 2.x и условные пересечения](manual-grass-sword.md) · [таблица селекторов](grass-selector-samples.md).

## Fire, Magma и Spider 1.6: типы и мир

[Три контроллера, рецепты и риск изменения мира](manual-fire-magma-spider-1.6.md) · [матрица type-селекторов](fire-web-targets-1.6.md).

## Sea Sword: подробная цепочка 1.6 и группы 2.x

[Helper и эффекты 1.6; водные группы, условия и конфликт восстановления 2.x](manual-sea-sword.md). Это статическая реконструкция с незаданными в фильтрах значениями.

## Lightning Sword 1.6: подробная цепочка

[Сенсор, helper и геометрия 1.6/2.x](manual-lightning-1.6.md) · [26 селекторов и 41 координата](lightning-patterns.md). Это статические декларации, не установленный тайминг молний.

## Ice Sword 1.6: подробная цепочка

[Предмет, helper, 26 команд и сравнение с 2.x](manual-ice-1.6.md) · [22 типа целей и геометрия](ice-target-matrix-1.6.md). Выписка остаётся статической: порядок работы сенсоров, состояний и legacy-команд требует проверки в игре.

## Jungle: сопоставление 1.6 и 2.8.14

[Полный порядок пар block/data, условный приоритет и получение](manual-jungle-vines.md) · [индекс 36/37 групп](jungle-vine-index.md).

Текст `controller.animation.jungle.states.jungle.on_entry` 1.6 содержит 145 записей: 144 команды `execute @p ... detect ... fill ... vine ... replace air` и финальное `scoreboard players set @a swords 2`. В `states.default.on_entry` остаётся буквальная `/commands`; оба состояния переходят друг в друга с условием `1.0`. В 2.8.14 `functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction` содержит 148 строк, вызывается из `entities/player.json` вместе с `effect @s absorption 1 2 true`.

При удалении начальной `/` у строк 1.6 и сравнении как мультимножеств (с учётом кратности, **без** доказательства эквивалентного контекста или порядка вызовов) совпадают все 144 старые vine-команды. Дополнительно в 2.8.14 есть четыре команды detect `leaves 11`: на x+1/x−1/z+1/z−1 относительно `@p` с vine data 8/2/1/4; единственная не совпадающая старая команда — глобальный scoreboard. Оба текста проверяют воздух на конечной позиции как `replace air`. В старом списке 36 вариантов блока/data по четыре направления, в новом 37 по четыре; полный перечень 36 сохранён в оригинале и выписке контроллера. Повторные вызовы, частота и положение `@p` между entity-controller и функцией игрока могут отличаться; нельзя считать совпадение команд доказательством идентичного поведения.
