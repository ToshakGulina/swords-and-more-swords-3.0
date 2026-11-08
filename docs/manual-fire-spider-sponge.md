# Fire, Spider, Sponge и Wet Sponge: мир, помощники и превращения

Сопоставление 1.6 с 2.8.8/2.8.14 по текстам и структурам архивов, без игровых испытаний. Четыре item JSON 2.x побайтово совпадают. Геометрия — число координат в командах, а не число доказанно заменённых блоков; вероятность относится только к конкретному вызванному выбору. [Указатель](quick-reference.md) · [типы Fire/Spider 1.6](fire-web-targets-1.6.md) · [выброшенные предметы 2.x](manual-dropped-items-2.8.md).

## Fire Sword

[Условная межигровая матрица family и type](manual-family-cross-effects-2.8.md).

**Предмет и получение.** 1.6 damage 12, durability 2000, offhand true; 2.x damage 6, durability 2000, offhand false; self repair 2000, enchantable 9/sword и web/bamboo 15/10 указаны в обеих. Дополнительно 2.x repair буквальным `minecraft:fire` 1000 и cooldown 25. Рецепт 1.6 `#SM/SBS/NS#`: S blaze_powder, M magma_cream, B iron_sword, N blaze_rod, но `#` не задан в key. В 2.x `F/F/#`, F = `minecraft:fire`, # = blaze_rod. Нельзя подставлять другой ингредиент или утверждать, что fire доступен как предмет и рецепт работает.

В 2.x `living_flame` имеет `start_death_hostile` с фильтром не passive и не projectile, randomize 85 пусто/15 `loot spawn ... entities/living_flame`; локальная таблица содержит один Fire Sword. В hostile-группе damage sensor вызывает это событие от `other` family player с `deals_damage:false` и **без** явного fatal; on_death тоже ведёт туда, но hostile timer `[25,60]` вызывает другое событие `minecraft:start_death`. 15/100 нельзя приписать каждому убийству или каждому истечению таймера.

**1.6.** Hand sensor → spawn `entity:fire` → `controller.animation.fire`. На входе каждого из двух состояний одинаковые 39 строк: fire_resistance ближайшему `@p` и detect воздуха в его позиции с setblock fire; пять fill в кубе ±3 относительно `@p` (snow_layer→air, ice/blue_ice/packed_ice→water, snow→grass); 31 отдельная type-команда `setblock fire` у сущностей r=15/rm=2 относительно helper, включая ряд мирных животных и villager; затем `@a swords=2`. В этих 31 командах нет явного `replace air`; выбор ближайшего игрока и сущностей имеет разные центры. [Порядок и список](manual-fire-magma-spider-1.6.md#fire-31-тип-и-изменения-блоков).

**2.x.** Три weapon-хука задают durability 1, затем randomize 85 `shoot entity:fire` / 15 `shoot entity:living_flame`; группа projectile может изменить power/gravity после entity_spawned. On-use `sequence` содержит шесть summon living_flame: одну цель y+14 и пять помощников y+4 в центре и на осях ±3; затем durability 20. Помощники выбирают созданную family target, а не прямо всех мобов. Player group отменяет fire/fire_tick, удержание меняет snow_layer/ice/blue_ice/packed_ice в кубе ±3 и вызывает `entity:fire` у `@e[family=!player,type=!item,r=3]`; вместе с ними обновляется lightblock в кубе ±1. Целевой selector шире перечня враждебных мобов, чем «поджечь только противников».

Выброшенный предмет после тега по **форматированному имени** при `in_water` вызывает загрузку структуры **Glass Sword** и kill исходной item-сущности; вне воды при `in_water_or_rain` одноразовый random timer `[5,6]` ведёт к структуре **Obsidian Sword**, а при прекращении условия группа таймера снимается. Это противоположно формулировке просмотренного скриншота о воде/дожде; версия скриншота неизвестна. Огонь вызывает другую цепь. Ни сохранение прежних чар, ни фактический порядок тега/таймера не доказаны.

## Spider Sword

**Предмет и получение.** Damage 6 → 5, durability 628 в обеих, offhand true → false; enchantable 9/sword и self repair 628 остаются, 2.x добавляет web 128 и spider_eye 48 для ремонта. Speed web в digger 15 → **100**, bamboo остаётся 10. Рецепт 1.6 `#SS/SBS/NS#`, S web, B spider_eye, N stick, но `#` отсутствует в key. Прямого локального рецепта с этим result в 2.x не найдено. `chests/abandoned_mineshaft.json`, pool 1: 2…4 rolls, меч weight 3 из явно заданной суммы 86; 3/86 относится к одному выбору в условной модели, не к полному сундуку.

**1.6.** Hand sensor → `entity:spider` → controller: снять poison у `@p`; при detect web в его позиции и y+1 заменить его на air; относительно `@p` назначить slowness 1 amplifier 128 отдельно spider и cave_spider в r=6; затем 25 отдельных type-команд относительно helper в r=5 ставят web в позиции цели только через `replace air`, и `@a swords=2`. Паук и пещерный паук присутствуют в slowness, но не в 25 типах установки web; центры выбора тоже различаются.

**2.x.** Все три weapon-хука задают durability 1, затем 95 пусто/5 `shoot entity:web`. On-use отдельно задаёт расход 8 и event `spider_sword_skill` target holder, cooldown 28. При удержании событие вызывает `ride @s summon_ride minecraft:spider no_ride_change minecraft:spider_sword`; skill-группа добавляет spawn `entity:web` с wait 0/0, single_use false и одноразовый timer `[2,2]` для stop. Количество созданий в этот интервал не определяется только нулями wait. Снаряд web при попадании может выполнить `fill ... web 0 replace air` на одной позиции.

Spider jockey имеет family `[spider,monster,mob,arthropod,spider_sword]`, health 20, одно место и player-controlled movement; ссылка на `loot_tables/entities/empty.json` отсутствует в обоих 2.x архивах и не равна существующему `loot_tables/empty.json`. Animation controllers при rider/соседнем воздухе назначают или снимают levitation; не приравнивать это автоматически к ванильному лазанию. При stop игрока указано удаление обеих групп и stop_riding; выбор, загрузка и путь loot требуют проверки.

## Sponge Sword и Wet Sponge Sword

**Предметы и получение.** 1.6 имеет только точный `effect:sponge_sword`: damage 6, durability 128, offhand true, enchantable 9/sword, self repair 128, recipe `F/F/E` с sponge и stick. В 2.x dry: damage 5, durability 128, offhand false, self repair 128/sponge 62, web/bamboo 15/10. Wet — отдельный ID damage 3, durability 64, offhand false, repair dry 64/sponge 32/wet 64 и **без** digger. У обоих 2.x не объявлен enchantable; оба имеют только on_hurt_entity → durability 1. Furnace/blast_furnace recipe получает wet и выдаёт dry, не наоборот. `elder_guardian` pool на dry содержит killed_by_player и chance 0.065, looting_multiplier 0.02; локальная привязка таблицы к ванильному entity отдельно не доказана.

**1.6.** Player → helper `entity:sponge` → controller: от **каждого** `@a` fill куба ±4 (729 геометрических координат) water→sponge и затем sponge→air. Далее девять detect water data 0…8 в позиции игрока и одна проверка air на y+1, каждая при прохождении запускает fill того же куба `air replace seagrass`; в конце `@a swords=2`. Команда очистки sponge не различает ранее существовавшую губку и созданную предыдущей командой; из-за порядка вода к моменту detect уже может измениться.

**2.x, удержание dry.** Family-gated первый шаг создаёт группу и objective `sponge_sword`. Отдельный шаг с `in_water_or_rain` делает fill куба ±2 (125 координат) water→sponge, звук и частицу, и добавляет игроку 1 к счёту — без проверки числа действительно заменённых water блоков. Следующий шаг **без того же фильтра** делает sponge→air и seagrass→air в том же кубе; существующую губку он тоже не отличает от временной. При точном score 150, 155 или 160 запускается wet-событие: при dry в `hand` команда заменяет `slot.weapon.mainhand` на wet, обнуляет score и показывает title. Проверка hand не идентична явно выбранному mainhand в команде; состояние исходного item и результат при конфликтующих слотах не установлены.

**2.x, выброшенный dry.** По имени функция добавляет tag `sponge_sword`; `item.json` при теге и `in_water_or_rain` включает отдельную группу с random timer `[0,1]` и командами, меняющими water, sponge и seagrass в кубе ±2. По timer загружается структура `wet_sponge_sword`, затем исходная item-сущность уничтожается; stop при выходе из условия снимает группу. Это **не** player scoreboard 150/155/160. Возможное состояние предмета, назначение тега и взаимный порядок событий не доказываются NBT.

## Границы

Исходные рецепты, фильтры и старый синтаксис сохранены как написаны; запуск, приоритет компонентных групп и работа команд не проверялись. Описание скриншота и код различаются, но версия скриншота не установлена.
