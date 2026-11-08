# Grass Sword: глобальная трава 1.6 и общие теги 2.x

Статическое чтение архивов; [таблица тип/family/tag](grass-selector-samples.md) демонстрирует только условные совпадения селекторов. Частота сенсоров и таймеров, разрешение legacy-команд и реальный выбор сущности/блоков не проверены в Minecraft.

## Общие предмет и получение

`effect:grass_sword` в обеих версиях объявляет damage **8**, max durability **250**, self-repair **250**, max stack **1**, enchantable `{value:9,slot:sword}`, hand_equipped true, can_destroy_in_creative false, digger web **15**/bamboo **10**, use_efficiency true. Off-hand **true** в 1.6 и **false** в 2.x; в 2.x `on_hurt_entity` запускает weapon event с durability damage **1**. PNG 1.6 **16×16**, 2.x **32×32**; хотя ID одинаковый, это разные размеры ([аудит](icon-comparison.md)).

В 1.6 shaped recipe для crafting_table: `F / F / E`, F=`minecraft:grass`, E=`minecraft:stick`, результат `effect:grass_sword`. Разрешение старого блока-ингредиента и регистрация не проверены. В 2.x локальный рецепт, прямой loot и торговля для ID не обнаружены; есть сохранённая структура предмета и armor stand ([получение](acquisition-index-2.8.14.md#effectgrass_sword)).

## 1.6: один helper и все игроки

Sensor `has_equipment`, self, domain hand, value `effect:grass_sword` вызывает event `minecraft:grass_sword`; он добавляет группу со spawn `entity:grass`, min/max wait **0/0**, num_to_spawn **1**, single_use true. Общая ветвь `minecraft:event_normal_player` её удаляет, поэтому число spawn и частота не доказаны. В 1.6 этот `entity:grass` — helper family `despawnear`, health 1, collision 0×0, fire_immune true и physics `{}`, а не helper с другой реализацией в 2.x. Animation `grass` указывает на `controller.animation.grass`; default и grass переходят друг в друга по `(1.0)` и имеют одинаковые четыре строки on_entry.

1. `/execute @a ~ ~ ~ detect ~ ~ ~ air 0 fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 grass 0 replace dirt` — для **всех выбранных игроков**, у кого detect air, плоскость y−1 **5×5 = 25** позиций. Слово `dirt` после replace здесь без указанного data; число фактических замен зависит от мира и двигателя.
2. `/execute @a ~ ~ ~ detect ~ ~-1 ~ grass 0 fill ~ ~ ~ ~ ~ ~ tallgrass 0 replace air` — опять все игроки с grass 0 под ними, не только владелец.
3. `/execute @e[r=10] ~ ~ ~ detect ~ ~-1 ~ grass 0 fill ~ ~ ~ ~ ~ ~ tallgrass 0 replace air` — selector относительно helper, без явно перечисленных исключений type/family; при допустимых условиях может включать различные виды сущностей и игроков, но движковые ограничения надо проверить.
4. `/scoreboard players set @a swords 2` — глобальный для выбранных игроков счётчик.

Выполнение одной команды на разных выбранных сущностях, пересечения областей и существующие блоки делают результат зависимым от порядка и состояния мира. Это не декларация механизма ловушки 2.x.

## 2.x: создание helper и общий tag

Предметы, `entities/grass.json`, `entities/witch.json` и структура grass_sword совпадают побайтово между 2.8.8/2.8.14; соответствующие ветви player совпадают структурно, хотя целый player.json различается в Ice.

Player sensor удержания добавляет `minecraft:grass_sword` с family `[player,grass_sword]` и looping timer `[0.2,0.2]` → `grass_sword_skills`. Отдельный шаг события содержит в исходном порядке: `tag @e[tag=grass,rm=9,r=10] remove grass`; `fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 grass 0 replace dirt`; detect grass 0 ниже `@s` и заполнение текущей точки tallgrass 0 с `replace air`. Первая команда снимает одноимённый тег у подходящих **любых** сущностей в кольце, не только созданных данным игроком. Stop при family `grass_sword` снимает группу и добавляет default_player. Реальная частота и одновременные вызовы не следуют автоматически из timer.

При timer-event player две команды ищут `@e[type=!player,type=!item,type=!entity:grass,type=!xp_orb,type=!arrow,r=8,tag=!grass]`: detect grass 0 на `~ ~-0.1 ~`, затем detect в позиции цели **air 0** или **tallgrass 0**, соответственно `summon entity:grass`. Это два вложенных detect, а не гарантия spawn для каждого выбранного типа. Синтаксис с дробной координатой и скорость событий проверить в движке.

Grass Witch использует похожие две команды в `grass_witch_skill`, но selector другой: `family=!grass_witch`, `family=!shulker_sword`, `type=!item,!entity:grass,!xp_orb,!arrow`, `r=8,tag=!grass`. Он **не содержит `type=!player`**. У специальной группы witch environment_sensor задан как `triggers:[{filters:{},event:"grass_witch_skill"}]`: пустой filters и формат triggers не доказывают, когда или как часто он сработает.

## Что делает `entity:grass` 2.x

Entity family `[effect99_entities]`, collision 0×0, damage_sensor cause all/deals_damage false, physics gravity/collision false, pushable и piston false. Его `minecraft:entity_spawned` указывает группу timer `[1.08,1.08]`, looping false, и список команд: sound `dig.grass`, `effect @e[type=!entity:grass,r=1] slowness 2 15 true`, затем назначение tag grass через `@e[family=!grass_witch,type=!entity:grass,type=!xp_orb,type=!arrow,r=1,tag=!grass]`. В **этом** selector назначения тега нет исключений `type=!player` и `type=!item`, хотя они есть у поиска player. Slowness отдельно исключает только type helper и не требует tag.

Timer-event `grass_sword_skill` содержит два `execute` для `@e[type=!entity:grass,c=1,r=1,tag=grass]`, далее два detect: grass 0 снизу `~ ~-1 ~`, затем в позиции air 0 либо tallgrass 0; при прохождении — `tp @s ~ ~-1 ~`. После этих строк указан `tag @e[tag=grass,r=2] remove grass`, без привязки тега к создателю. В том же объекте события объявлено add группы `start_despawn` с timer `[0.52,0.52]`, looping false. Относительный порядок `run_command` и `add` в одном объекте отдельно не установлен; не считать строго доказанным расписанием **1.08 + 0.52** до удаления.

`c=1` означает ограничение числа выбранных целей, но порядок выбора, идентичность этой сущности в двух отдельных командах и возможное совпадение с исходной целью требуется испытать. Selector для телепорта **не исключает player, item, arrow или xp_orb**; он требует tag, который мог быть назначен другим механизмом или прежним вызовом. Обе команды выполняют собственный выбор. Снятие tag в r=2 и player-очистка в кольце 9…10 не различают авторство, поэтому несколько helper/игроков/ведьм могут конфликтовать при выполнении одновременно. Это риск, а не доказанный сценарий телепорта конкретного игрока.

При `despawn` sequence сначала add группы despawn, затем randomize **50**: `fill ~ ~ ~ ~ ~ ~ tallgrass 0 replace air`, **50**: пусто. При обычном взвешивании 50/100 — условная доля ветви события, не гарантированный шанс травы в мире; состояние блока, успешность команд и время despawn остаются неизвестными.

## Type не равен family: показательные пересечения

[Таблица](grass-selector-samples.md) сравнивает условия без имитации радиуса, detect и ограничения `c=1`:

- В модели обычный `type=player` не проходит поиск player из-за `type=!player`, но может пройти поиск witch и назначение tag helper, если выполняет остальные условия. Срабатывание, наличие игрока в радиусе и способность назначить ему tag нужно проверить.
- Player с полной Wolf family `[wolf,wolf_sword,complete_wolf_transformation,monster]` всё равно остаётся **type player** в этой условной модели; отсутствие family `player` не превращает его в иной type. Поиск player всё равно исключает `type=player`.
- `entity:shulker_shield` объявляет family `[effect99_entities,player,shulker_sword]`, но его **type — отдельный** `entity:shulker_shield`: он может пройти только текстовые type-условия поиска player, тогда как поиск witch исключает family `shulker_sword`. Это не подтверждение физической совместимости или spawn.
- Специальная Grass Witch family `[witch,monster,mob,grass_witch]` исключена из поиска witch и назначения tag, но текст поиска player её отдельно не исключает. Снятие существующего tag r=2/кольцо не ограничено family.
- Item исключён из обоих первичных поисков, но не исключён из назначения tag при spawn helper. Arrow исключён из первичных поисков и назначения tag, но если tag уже был назначен извне, selector `c=1` его явно не исключает. Другие условия всё равно обязательны.

## Ведьма и условная модель выдачи

`minecraft:entity_spawned` witch выбирает weight **80** default или **20** add обеих групп `minecraft:grass_witch` и `grass_witch`. Последняя задаёт variant 1 через другую группу, family `[witch,monster,mob,grass_witch]`, health **32/32**, follow_range **80**, scale **1.1**, `minecraft:loot:{}` и on_death `grass_sword`. У death-event randomize **80** пусто / **20**: `structure load grass_sword ~~~`, `setblock ~ ~ ~ double_plant 2`, `playsound dig.grass @a[r=12] ~~~`. Эти три строки и старую запись `~~~` сохранять без предположения об успешном исполнении.

Структура `grass_sword.mcstructure` 1×1×1 содержит одну entity `minecraft:item` с `Item.Name=effect:grass_sword`, Count **1**, Damage **0**, `Age:196s` и пустым `Tags:[]`; точная сериализация и origin — в [SNBT](structures-2.8.14.md). Наличие этих данных не доказывает успешную выдачу, время существования или перерасчёт координат при загрузке.

Если условно оба выбора работают с весами 20/100, независимы, специальная группа получена именно через указанную ветвь spawn и затем выполняется её on_death, вероятность выбора **обеих ветвей** равна `0.2 × 0.2 = 4%`. Это не шанс выпадения с любой ведьмы: специальные группы можно добавлять отдельным event, а гибель, команды, структура и наличие предмета требуют отдельной проверки. Факт существования 2-х вариантов client witch также не определяет их выбор конкретным движком ([аудит пакетов](manual-package-identities.md)).
