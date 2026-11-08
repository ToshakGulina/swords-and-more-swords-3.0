# Bee Stinger: триггеры, обычная и призванная пчела

В обоих архивах 2.x существуют предмет `effect:bee_sword`, отдельная сущность `entity:bee_sword` и замена `minecraft:bee`; их нельзя считать одним объектом. В архиве 1.6 item ID `effect:bee_sword` отсутствует. Ниже — декларации и условная арифметика, **не** проверка Minecraft, успешного получения меча, цели или времени существования пчелы.

## Предмет и weapon event

`Swords_B/items/bee_sword.json`: damage **5**, max durability **1080**, stack **1**, `allow_off_hand:false`, hand_equipped true, enchantable `{value:9,slot:sword}`, ремонт self **1080**, `minecraft:honey_block` **400**, `minecraft:honeycomb` **150**. Digger web **15**, bamboo **10**, use_efficiency true. Все три `on_hurt_entity`, `on_not_hurt_entity`, `on_hit_block` указывают на `weapon`: sequence сначала содержит durability damage **1**, затем randomize вес **30** — `shoot entity:bee_sword` launch_power **1**, вес **70** — ещё durability damage **1**.

При условии выполнения всего события и стандартного выбора по весам условные суммы прямых damage — **1 с 30%**, **2 с 70%**, средняя **1.7**. Это не фактический расход на удар/блок: стандартный износ, поведение shoot, ранняя поломка, порядок/число хуков и зачарования не учтены ([индекс 42 предметов](weapon-event-index.md)). Попадание, спавн и поведение пчелы не гарантируются самим weight 30.

## Цветы и потенциальная замена блока

Player sensor проверяет `has_equipment` domain `hand`, затем event добавляет группу при family `!= bee_sword`. Группа содержит family `[player,bee_sword]`, looping timer с `randomInterval:true`, время `[3,8]`, событие `bee_sword_flower`. Stop при family `bee_sword` удаляет группу и добавляет `minecraft:default_player`. Единицы и реальную частоту, повторное добавление группы и переключение оружия надо испытать.

`bee_sword_flower` содержит 12 ветвей по **weight 1**. Каждая выполняет `execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ …`: 11 вариантов `red_flower` с data **0…10**, одна `yellow_flower 0`. При стандартном равномерном выборе это **1/12 на каждую строку**, суммарно **11/12** на red и **1/12** на yellow, условно на вызов/выбор; detect grass и возможный неуспех команды дополнительно влияют на результат.

В этих 12 командах detect проверяет **блок под игроком**, а не пустоту целевой позиции `~ ~ ~`. После `setblock` нет явного режима `keep` и нет отдельного detect air. Поэтому нельзя описывать команды как гарантированно ставящие цветок только в воздух: они **потенциально** затрагивают уже существующий блок в позиции игрока. Фактический default mode setblock, совместимость data 0…10, защита блоков и результат требуют испытания; не считать, что все 12 вариантов обязательно допустимы в новой версии.

## Призванная `entity:bee_sword`

`Swords_B/entities/bee_entity.json` описывает отдельный ID `entity:bee_sword`, spawnable false, summonable true; он не является просто ссылкой на `minecraft:bee.json`. Базовая family **`[bee,mob,arthropod]` не содержит `bee_sword`**, хотя такая строка присутствует в ID. Внутри этого файла среди component_groups объявлена `despawn`, а среди events — только `despawn`: он выполняет `tp @s ~ -103 ~`, **не** add `despawn` и не `kill`. Timer looping/randomInterval true `[6,8]` вызывает этот event. Значение y **−103 абсолютное**, x/z относительные; поведение вне мира и последствия телепортации не установлены.

Основные численные объявления: health **10/10**, scale **0.5**, collision **0.55×0.5**, movement **0.3**, flying_speed **0.15**, `follow_range:1024`; `behavior.nearest_attackable_target` priority **1**, within_radius **16**, max_dist **10**, must_see true, фильтр цели `other` family `monster`; melee priority **1**, speed_multiplier **1.4**, track_target true; атака damage **1**, fatal_poison duration **3**. Angry duration **99999**, broadcastAnger true/range **20**, lava condition damage_per_tick **4**. Радиусы/приоритеты не следует сводить к одному гарантированному эффективному диапазону.

Damage_sensor запрещает damage, когда `other` имеет family `player`, и отдельно cause fall. Это не все виды урона и не проверка ID владельца. В полной Wolf-группе player может иметь family `[wolf,wolf_sword,complete_wolf_transformation,monster]`, **без `player`**, тогда как bee target-filter ищет family `monster`. Поэтому при условном одновременном применении этих семейств/фильтров player в Wolf-состоянии может не подходить под защиту `other family player` и может подходить под выбор цели пчелы. Дистанция, видимость, приоритеты и фактическая обработка групп не проверены; это риск для испытания, не доказательство нападения на владельца. См. [условия Wolf](manual-wolf-conditions-2.8.md).

## Обычная `minecraft:bee` и источник меча

В `Swords_B/entities/bee.json` angry_bee содержит `minecraft:behavior.melee_attack`, priority **2**, attack_once true, speed_multiplier **1.4**, `on_attack` → `countdown_to_perish_event` target self. Первый шаг этого события — randomize: weight **2**, filter self family `!= bee_sword`, команда `loot spawn ~ ~ ~ loot bee_sword`; weight **98** — пусто. Следующий шаг удаляет перечисленные группы, в том числе локально отсутствующую `collect_nectar`, и добавляет `countdown_to_perish`.

В `countdown_to_perish` объявлены mark_variant **1**, panic priority **1**/speed_multiplier **1.25**/force true, timer `[10,60]`, randomInterval true, looping false, event `perish_event`, и family `[bee,mob,arthropod,pacified]`. `loot_tables/bee_sword.json` содержит один roll и одну запись `effect:bee_sword`, weight **1**. Сопоставление локального `loot bee_sword` с таблицей, работоспособность и момент on_attack требуют движка.

**2/100 не означает 2% на любую смерть пчелы.** Оно относится к записанному randomize в конкретном событии, при выполнении filter и принятой семантике фильтрации/весов. Неизвестно, выбираются ли недопустимые ветви до или после нормализации, сколько раз событие может вызваться и будет ли команда успешна. Не доказывать общую частоту убийств/получения.

У призванной отдельной `entity:bee_sword` family также не содержит `bee_sword`, но в её локальном файле **нет** event `countdown_to_perish_event`: отсутствие этой family не доказывает, что её укус исполнит код обычной `minecraft:bee`. Внешнее/ванильное поведение и любые дополнительные компоненты нужно проверить отдельно.
