# Coal, Cactus, Emerald, Lapis и Glass: предмет → условия → действия → получение

Это статический разбор конкретных архивов `SwordsAndMoreSwords.1.6.mcaddon`, `swordsandmoreswords_2_8_8.mcaddon`, `swordsandmoreswords-2-8-14.mcaddon`. Цифры item — объявления, а не измеренный боевой урон; применимость старых команд и активность групп не предполагаются. Наименование «2.8.14» означает имя архива. У пяти предметов item JSON обеих версий 2.x побайтово одинаков; у рассмотренных ниже player-групп/событий совпадают разобранные значения, хотя целиком `player.json` различается. Пул loot описан условно на его активацию, без гарантии регистрации таблицы или получения результата.

Карта источников: [исходные карточки 1.6](items-1.6.md) / [2.8.14](items-2.8.14.md), [все item-компоненты](item-version-matrix.md), [полные действия weapon](weapon-event-index.md), [заявления встроенной справки](ui-localization-index.md), [пути получения 1.6](acquisition-index-1.6.md) / [2.8.8](acquisition-index-2.8.8.md) / [2.8.14](acquisition-index-2.8.14.md).

## Общая база и ограничения

У четырёх общих ID max stack 1 и `hand_equipped:true`. Во всех версиях `enchantable:{"value":9,"slot":"sword"}`, web speed 15, bamboo 10; указанный offhand `true` в 1.6 и `false` в 2.x. Это не означает, что любой движок примет или одинаково применит поля. В 1.6 у всех четырёх не объявлены item `weapon` и `on_use`; отсутствие поля не приравнивается к нулевому стандартному износу. В 2.x у Coal, Cactus и Lapis указан только `weapon.on_hurt_entity`; у Emerald — также `on_not_hurt_entity` и `on_hit_block`. Все указанные хуки ведут в `weapon` с прямым `damage:{"type":"durability","amount":1,"target":"self"}`. Не складывать его со штатным расходом и не считать число вызовов доказанным.

Общая схема четырёх мечей 1.6: `Sword_B/entities/player.json` имеет sensor `has_equipment`, `subject:self`, `domain:hand` для точного ID; одноимённое событие добавляет группу со `spawn_entity` helper, `min_wait_time:0`, `max_wait_time:0`, `num_to_spawn:1`, `single_use:true`. Одноразовость свойства spawn не определяет число повторных добавлений группы. Helper `entity:coal`, `entity:cactus`, `entity:emerald`, `entity:lapis` каждый объявляет family `despawnear`, despawn-фильтр по ней, health 1, collision width/height 0, fire_immune true, physics `{}` и соответствующий `controller.animation.*`. В двух состояниях каждого контроллера обратные переходы `(1.0)` и одинаковые `on_entry`; `@p` выбирается в контексте helper, а не обязательно владельца. В конце каждого списка `scoreboard players set @a swords 2`: это глобальные имена objective и selector всех игроков, не независимый личный таймер. [Схема сброса](manual-global-state-1.6.md) и [строки objective](scoreboard-index-1.6.md).

## Coal Sword

**Характеристики и получение.** `Sword_B/items/coal_sword.json` 1.6: damage 6, durability 121, ремонт только `effect:coal_sword` на 121, `minecraft:glint:false`; fuel в item не задан. В `Swords_B/items/coal_sword.json` 2.x damage 4, durability 121, `foil:false`, `minecraft:fuel.duration:360.0`, ремонт тем же мечом на 121, `minecraft:coal` на 58, `minecraft:stick` на 2. Число fuel оставлено в единицах исходного поля, не автоматически переведено в секунды. В трёх архивах одноимённый рецепт `recipes/coal_sword.json`: pattern `2/2/1`, ключ 2 = `minecraft:coal_block`, 1 = `minecraft:stick`, результат `effect:coal_sword`. В 2.x `loot_tables/chests/spawn_bonus_chest.json` имеет pool 0, rolls 1, три записи с суммой явно указанных весов 5, меч weight 1: 1/5 при стандартном взвешенном выборе **условно на активированный пул**. Это не гарантированный предмет в каждом бонусном сундуке.

**Удержание 1.6.** `entities/player.json:204–214,520–533,925–931` создаёт helper по вышеописанной цепочке. В `animation_controllers/coal_sword.json` каждый вход содержит 13 команд `replaceitem block <позиция> slot.container 1 coal`, затем запись общего score. Позиции относительно контекста команды в исходном порядке:

```
(-1,0,0) (1,0,0) (0,0,-1) (0,0,1) (0,-1,0)
(-1,1,0) (1,1,0) (0,1,-1) (0,1,1)
(-1,-1,0) (1,-1,0) (0,-1,-1) (0,-1,1)
```

Нет команды для `(0,1,0)` или `(0,0,0)`. Текст выбирает slot.container **1**, а не первый слот по естественному языку или проверенный тип печи; попытки могут затрагивать уже занятые контейнеры. Наличие блока/контейнера, возможность перезаписи и поддержка команды не установлены.

**2.x.** В базовом player sensor нет строгого одиночного hand-фильтра по `effect:coal_sword`, а в `player.json` нет буквального имени `coal_sword`. Это ограниченный поиск, а не доказательство отсутствия всех косвенных механизмов. Прежний controller с 13 `replaceitem` в 2.x локально не объявлен; предмет вместо этого содержит fuel и weapon выше. Не переносить helper 1.6 в новую версию автоматически.

## Cactus Sword

**Характеристики/рецепт.** Все версии имеют damage 6 и durability 125, self repair 125. Рецепт `recipes/cactus_sword.json` одинаков по разобранному содержимому: `F/F/E`, F = `minecraft:cactus`, E = `minecraft:stick`. 2.x дополнительно задаёт render_offsets main hand: first-person position `[0.67,0,-1.24]`, third-person `[0.36,1.5,-0.66]`; прочие transform не объявлены, поэтому не подставлять нулевые значения. PNG 1.6 16×16, 2.x 21×21, оба PNG 2.x одинаковы по SHA-256; детали — [сравнение значков](icon-comparison.md).

**1.6.** `animation_controllers/cactus_sword.json` в обоих состояниях последовательно: создать objective `ct`; прибавить `@p ct 1`; прибавить `@e[r=3,type=!entity:cactus,type=!player] ct 1`; через `execute @p[scores={ct=1}]` выдать `effect @s poison 1 1 true`; отдельно через `@e[scores={ct=1},r=2]` выдать тот же effect; при `@p[scores={ct=20}]` удалить objective `ct`; установить `@a swords 2`. Второй селектор отравления **не** исключает игроков и не является копией селектора прибавления: подходящий игрок может фигурировать в обеих проверках. Удаление objective глобально по имени, а не только сброс одного игрока. Это текст и возможное пересечение, а не гарантия двойного воздействия.

**2.x.** Sensor игрока по `hand` вызывает `minecraft:cactus_sword`; при family != `cactus_sword` добавляется группа с family `[player,cactus_sword]` и timer `time:[0.5,0.5]`, `looping:true`, `time_down_event:cactus_sword_skills`, target self. Событие имеет две команды в порядке: `damage @e[r=1.4,type=!player] 1 contact entity @s`, затем `damage @s 1 contact`. Таким образом, первая строка исключает entity **типа** player, вторая адресована самому исполнителю; они не означают только отравление 1.6. Сенсор с operator `!=` вызывает stop, который при family `cactus_sword` удаляет соответствующую группу и добавляет `minecraft:default_player`. Время реального цикла, одновременные группы, успешность damage и последствия смены предмета по этим записям не определяются.

## Emerald Sword

**Характеристики/получение.** Damage 7, durability 2300 и self repair 2300 во всех трёх архивах. В 1.6 есть рецепт `recipes/emerald sword.json`: `F/F/E`, F = `minecraft:emerald_block`, E = `minecraft:stick`. В локальных recipes обоих 2.x такой результат буквально не найден. В 2.x меч есть в chest loot: stronghold corridor pool 0, rolls 2–3, weight 5 из суммы 521; woodland mansion pool 0, rolls 1–3, weight 25 из 670. В pillager outpost pool 3, rolls 2–3, weight 3 и `set_count` 0–1, но другой элемент этого пула не имеет явно указанного weight: без интерпретации его default точную долю не заявляем. Эти доли — на выбор записи, не на целый сундук.

Только 2.8.8 содержит два файла торговли оружейника: один вариант хочет 32 emerald_block, выдаёт меч с `enchant_with_levels` 5–60 и `max_uses:2`; другой задаёт цену 24–32 блока и ту же функцию зачарования. В 2.8.14 оба файла отсутствуют. Точный контекст tier и неопределённость регистрации — [версионный разбор](manual-version-2.8.8.md#emerald-sword-два-объявления-торговли-только-в-288).

**Удержание.** В 1.6 helper-контроллер без проверки деревни выполняет `/effect @p village_hero 16 0 true` и `@a swords 2` в каждом из двух одинаковых on_entry. В 2.x `player.json` имеет отдельную группу family `[player,emerald_sword]`: первая ветвь при family != emerald_sword добавляет группу, а **следующий отдельный шаг** при `is_in_village:true` выполняет `effect @s village_hero 1 0 true` и `effect @e[family=villager,r=64] resistance 1 1 true`. В stop при соответствующей family выполняется `effect @s village_hero 0 0 true`, удаляется группа и добавляется default_player; отдельного снятия resistance у жителей в этом событии нет. Частоту вызова sensor, значения эффекта и результат при конфликтующих группах текст не доказывает.

## Lapis Sword

**Характеристики/получение.** В 1.6 damage 6, durability 528 и только self repair 528; в 2.x damage 5, durability 528 и ремонт self 528 либо `minecraft:lapis_lazuli` 48. Рецепт `recipes/lapis_sword.json` есть в 1.6: `F/F/E`, F = `minecraft:lapis_block`, E = `minecraft:stick`; в локальных recipes 2.x точный результат не найден. В 2.x прямые loot-записи: stronghold corridor pool 0 rolls 2–3 и weight 5/521; stronghold library pool 0 rolls 2–10 и weight 5/275; pillager outpost pool 3 weight 3 и `set_count` 0–1 при другом элементе с отсутствующим weight. Последняя доля не выводится без дополнительных допущений. Условные доли — не вероятность получения из структуры.

**1.6.** Helper-controller в обоих on_entry: `scoreboard objectives add l dummy`; `scoreboard players add @p l 1`; при `@p[scores={l=10}]` выполнить `xp 5 @s`; при `@p[scores={l=30}]` удалить objective `l`; затем `@a swords 2`. Фильтрованный `@p` может выбрать не того же игрока, что получил add. В `normal.mcfunction` прямой команды удалить `l` нет; не исключены другие пути изменения состояния.

**2.x.** Sensor hand вызывает группу `minecraft:lapis_sword`, если у self нет family `lapis_sword`. Группа задаёт family `[player,lapis_sword]` и timer `time:[2.5,6.0]`, `randomInterval:true`, `looping:true`; `lapis_sword_skills` выполняет `xp 5 @s` и `playsound random.orb @s ~ ~ ~ 0.3`. Stop при соответствующей family удаляет группу и добавляет default_player. Таймер — объявленный диапазон, не измеренный период и не перенос scoreboard `l` из 1.6.

## Glass Sword — только 2.x среди точных ID

`effect:glass_sword` отсутствует как точный item ID в 1.6. В обеих 2.x: damage 33, durability 1, stack 1, enchantable 9/sword, offhand false, `repairable` с self 1 и `minecraft:glass` 1. Это прямо расходится с текстом `Repairable: false` в локальной справке; наличие компонента тоже не доказывает фактическую работу ремонта.

`minecraft:digger` имеет общий `on_dig` → `weapon`, а также отдельный `on_dig` на web speed 25 и bamboo speed 15. Все три weapon-хука тоже ведут в то же событие: один элемент sequence одновременно задаёт durability damage 10, target self, и `playsound random.glass @a[r=8,m=0]`. Не считать эти пути взаимоисключающими, не утверждать число вызовов и не выдумывать порядок одноуровневых полей. Sensor с точным item ID в player не найден; это не доказательство отсутствия других связей.

Результат в локальных recipes, прямых loot item entries и торговле не найден. Основной рассмотренный путь: Fire Sword как выброшенный item с tag `fire_sword`, при `in_water` вызывает `fire_sword_event_2`, который загружает `glass_sword` и затем `kill @s`. В структуре `Swords_B/structures/glass_sword.mcstructure` хранится item `effect:glass_sword`, Count 1. Сам тег ранее ставится по отображаемому имени функцией игрока; ни сохранение исходной прочности/чар, ни работоспособность всех шагов не выводится из текста. Отдельно `give.mcfunction` содержит выдачу Glass. Подробная цепь и конкурирующие события — [выброшенные предметы](manual-dropped-items-2.8.md).

## Что остаётся неустановленным статически

Движковые значения по умолчанию, успешность старых команд и event-полей, селектор `@s` в каждом контексте, разрешение конкурирующих компонентных групп, реальная частота сенсоров и таймеров, фактическая регистрация loot/торговли, результаты замены item и состояние нескольких игроков. Автоматические перечни и эта карточка не доказывают выполнения этих операций; исходные архивы сохранены без изменений.
