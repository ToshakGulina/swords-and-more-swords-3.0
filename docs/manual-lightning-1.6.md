# Lightning Sword 1.6 и геометрия 2.x

Статическое сравнение исходных архивов; [все 26 селекторов 1.6 и 41 точка 2.x](lightning-patterns.md) извлечены с сохранением порядка команд. Реальное исполнение, призыв молнии, ущерб миру и модель вероятностей не проверены в Minecraft.

## Предмет, клиент и получение 1.6

`Sword_B/items/lightning_sword.json`: ID `effect:lightning_sword`, `format_version:1.20.20`, max stack **1**, damage **8**, max durability **2000**, `minecraft:glint:true`, `allow_off_hand:true`, `hand_equipped:true`, `can_destroy_in_creative:false`; enchantable `{value:9,slot:sword}`; ремонт самим `effect:lightning_sword` amount **2000**. Digger использует efficiency и скорости web **15**, bamboo **10**. Числа — объявления, а не результат удара/ремонта в игре.

В 1.6 локальный shaped recipe `Sword_B/recipes/lightning_sword.json` имеет pattern `F / F / E`: два `minecraft:gold_block`, затем **буквальный** ID `minecraft:netherstar`, результат `effect:lightning_sword`, tag `crafting_table`. Не подменять старое имя ингредиента на предполагаемый современный аналог без отдельной проверки регистрации рецепта. Прямых локальных записей предмета в loot/trade/структурах 1.6 не найдено; это не доказывает отсутствие других путей. В 2.x локальные recipe и прямые loot для этого ID не обнаружены, зато есть структура с предметом и структура с armor stand ([получение 2.8.14](acquisition-index-2.8.14.md#effectlightning_sword)); реальную выдачу надо проверять по цепи Centella и регистрации структур.

Значок 1.6 **16×16**, 2.8.14 **64×64**; это различающиеся размеры, не автоматическая эквивалентность ([аудит PNG](icon-comparison.md)). Ресурс 1.6 называет item `§g§lLightning Sword`. Разные `minecraft:glint` и `minecraft:foil` не следует без испытания считать полностью одинаковыми.

## Сенсор и helper 1.6

`Sword_B/entities/player.json`: sensor `has_equipment`, self, domain `hand`, value `effect:lightning_sword` посылает event `minecraft:lightning_sword`; он добавляет одноимённую component group. Её `minecraft:spawn_entity` задаёт `entity:lightning`, wait min/max **0/0**, `num_to_spawn:1`, `single_use:true`. Другая player-ветвь `minecraft:event_normal_player` удаляет группу, поэтому один helper на всё время удержания или определённая частота не доказаны ([общая цепь 1.6](manual-global-state-1.6.md)). Не отождествлять helper `entity:lightning` с призываемой им ванильной `lightning_bolt`.

`Sword_B/entities/lightning.json` — helper с family `despawnear`, фильтром despawn по собственной family, health **1**, collision **0×0**, fire immune true, physics `{}`; summonable true, spawnable false, experimental false. В описании нет таймера с явно заданной продолжительностью. scripts animate `lightning` ссылается на `controller.animation.lightning` из файла **с пробелом** `Sword_B/animation_controllers/lightning sword.json`.

У этого контроллера состояния `default` и `lightning` переходят друг в друга по `(1.0)`; в обоих `on_entry` списки **побайтово равных строк в том же порядке**: по одной команде для 26 типов, затем `scoreboard players set @a swords 2`. Каждый selector записан `@e[type=...,r=16,rm=10]`; далее старый `execute ... ~ ~ ~ summon lightning_bolt` задаёт контекст позиции выбранной сущности. Здесь нет явно заданной вероятности, отдельного on-use или призыва фиксированной сетки из 41 точки. Перечень включает, в частности, creeper, blaze, `zombie_pigman`, `evocation_fang`, ravager, guardian и phantom; игрок как отдельный тип в списке отсутствует. Значение score `swords` изменяется у **всех** `@a`, не только у владельца.

Из двух состояний с одинаковыми командами нельзя вывести частоту ударов или доказать, что молнии реально призываются: порядок переходов/entry, жизнь helper, исполнение устаревших selector/type ID, пересечения и взаимодействие многопользовательских команд подлежат испытанию. Radius `rm=10,r=16` записан относительно контекста helper, а не подтверждён относительно персонажа после перемещения helper.

## Основные отличия 2.x

У одинакового ID damage **8**, max durability **2012**, off-hand **false**, self-repair **2012**, cooldown duration **12**; в JSON используются `minecraft:foil:true` и другая render-offset конфигурация. Три item weapon hook направлены в `weapon`: отдельно задано damage durability **1**, затем `randomize` с весами **15** пусто и **85** shoot `entity:lightning_projectile`, launch_power **1**. Это условный выбор при срабатывании события, а не доказанный шанс попадания молнии.

`on_use` содержит `run_command` из **41** строк и рядом в том же объекте damage durability **9**, target self. Порядок между полями `run_command` и `damage` не декларирован как sequence и не установлен. Все команды summon используют `default_lightning_bolt`; это **точки**, не селекторы сущностей:

- Одна точка `(0,+2,0)` относительно контекста команды; ещё **40** на y=0: по четыре осевых при расстояниях **7, 14, 28, 34, 42**, и по четыре диагональных в координатах `(±d,±d)` для **d=6, 12, 24, 30, 38**.
- Все 41 тройки координат уникальны; ограничения x/z от **−42 до +42**. Дальнейшие диагональные точки `(±38,0,±38)` находятся на горизонтальном расстоянии `38√2 ≈ 53.740`, больше 42. Это не радиус поражения и не обещание загрузки каждой точки.
- Точные точки и порядок сохранены в [индексе](lightning-patterns.md). Нельзя заменить рисунок кругом, равномерной выборкой или ближайшими целями: в 1.6 смысл команд другой.

Player group 2.x содержит damage_sensor, где `other` family `lightning` → `deals_damage:false`; это не универсальная защита от огня и других причин урона. Событие при отсутствии family `lightning_sword` одновременно добавляет группу и содержит summon на `~ 255 ~`, а другой шаг задаёт заполнение `effect99:lightblock2`. Снаряд, естественные молнии, Centella, выброшенный предмет и отсутствующие ссылки разобраны в [карточке 2.8.14](manual-traces-2.8.14.md#lightning-sword-effectlightning_sword).

## Условная модель 41 молнии и Centella

В обеих 2.x `entities/lightning_bolt.json` entity_spawned добавляет группу timer `[0,0]`, event `spawn_centella`: weights **80** пусто и **20** команда `summon entity:centella ~ ~1 ~`. Эта декларация не проверяет источник или грозу, но сами срабатывание таймера и сочетание с `default_lightning_bolt` не установлены.

Только при гипотезе, что **все 41** призыва создали подходящие lightning, все 41 timer/event сработали, выборы независимы и веса трактуются как 80/20, математически ожидалось бы **8.2 успешной ветви**, а вероятность хотя бы одной — `1 − (4/5)^41 ≈ 99.9894%`; вероятность нуля ≈0.0106%. Это **не измеренный шанс появления Centella при использовании меча** и не гарантированное количество сущностей: команды, обработка событий, спавн сущности и загруженность мира могут нарушить предпосылки. Цепь Centella может порождать дополнительные молнии на fatal-событиях; их в эту модель не включали.
