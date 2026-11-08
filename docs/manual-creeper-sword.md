# Creeper Sword: предмет, мини-крипер и получение

Статический разбор `effect:creeper_sword`, соответствующего player-event, `minecraft:creeper` и структуры. Рассматриваемые item, creeper entity, instant explode entity, loot creeper и структура **побайтово одинаковы** в архивах 2.8.8 и 2.8.14; используемые группы и события player структурно одинаковы, хотя весь `player.json` между версиями различается. Для 1.6 см. [отдельную старую цепочку и сравнение](manual-traces-1.6.md#creeper-sword-и-tnt-sword-16) и [массовые цели 1.6](manual-area-targets-1.6.md#creeper-и-tnt-разные-выборки-для-одной-сущности-взрыва). Игровых испытаний не было.

**Оговорка для основной сущности:** исходный `Swords_B/entities/creeper.json` не разбирается JSON5: неожиданная последняя `}` на строке 430. Если убрать именно эту скобку только в памяти, оставшийся текст разбирается; ниже приводится эта диагностическая интерпретация вместе с буквальными строками. Это не изменение архива, не единственно возможное исправление и не доказательство, что исходный Bedrock загрузит файл. Автоматические [индексы групп](entity-groups-2.x.md) и [randomize](randomize-index.md) исключают этот повреждённый файл; в нём дополнительно есть описанная ниже ветвь 95/5.

## Сопоставление с образцами: только диагностическая копия в памяти

[Полная сравнительная выписка](vanilla-creeper-diagnostic-ledger.md) и [машинные данные](../data/vanilla-creeper-diagnostic.json) показывают различия гипотетического результата удаления последней `}` с двумя официальными образцами Mojang. Их идентичные `creeper.json` имеют SHA-256 `6f8a46400a440580a9f450404476c17132e448f010cc7c81c9dd9984ffab8bce`; оригинальный повреждённый файл обеих 2.x — `8c8f169be60ee52a224928d57575cb3b47f19bf41c03e8dd5326f8440d6c33c2`. Источники и ограничения образцов — в [сравнении](manual-vanilla-override-review.md). Это отдельно от 22 безошибочно разобранных файлов, **не** подтверждение единственного исправления или загрузки игры.

В варианте разбора из двух образцов base `minecraft:despawn` присутствует, а в гипотетическом add-on объекте отсутствует; `must_see_forget_duration` в `minecraft:behavior.nearest_attackable_target` — **3.0** в образцах и **0.0** в варианте аддона; в forced charged группе образцов нет таймера, описанного далее. Вариант аддона дополнительно содержит `minecraft:minicreeper`, projectile, exploding и соответствующие события. Наличие и отсутствие полей не доказывает работу, default или порядок групп.

После скачивания двух ZIP по ссылкам выше сравнение воспроизводится без изменения источника:

```sh
python tools/build_creeper_diagnostic_diff.py \
  --reference-119 /путь/bedrock-samples-v1.19.40.2.zip \
  --reference-120 /путь/bedrock-samples-v1.20.30.1.zip
```

## Предмет и две разные цепочки

- `items/creeper_sword.json:8–78`: damage 6, durability 1500, max stack 1, offhand false, enchantable 9/sword; ремонт самим предметом на 1500 либо `minecraft:gunpowder` на 256, web 15 и bamboo 10; cooldown `{category:"creeper_sword",duration:3}`. Значения компонентов приведены буквально; их исполнение и единицы в целевой версии требуют проверки.
- `:100–128`: все три заявленных weapon-hook указывают на одно событие. В `sequence` сначала `damage` durability 1 target self, затем выбор веса 20 — `shoot` projectile `minecraft:creeper`, launch_power 1; веса 80 — ещё `damage` durability 1 target self. При стандартном взвешенном выборе и полном прохождении sequence это **20% выбора shoot на вызов**, а суммы прямого damage 1/2 имеют доли 20%/80%, среднее 1.8. Это не шанс успешного рождения мини-крипера и не фактический расход предмета: количество хуков, прерывание, стандартный износ и интерпретация target требуют проверки. Подробнее [модель weapon](manual-weapon-durability-model.md).
- `:81–98`: другой, on-use event содержит `sequence`: команда `event entity @s start_player_explode_event` с target `holder`, затем `damage` durability 1 target self. Это **не** тот же 20/80 randomize. Отсутствие выбранной/рабочей цели или прерывание может влиять на реальный результат; свойства target нельзя выводить из имени.

## Самовзрыв игрока

`entities/player.json:337–342,2108–2116`: `start_player_explode_event` добавляет одноимённую группу movement value 0 и looping timer `[1.5,1.5]` → `start_player_explode`, а рядом содержит run_command с `playanimation @s animation.player.explode`, `playsound random.fuse`. Порядок выполнения **соседних полей** add и run_command не задан только порядком их записи.

Событие таймера содержит соседние remove этой группы, add `minecraft:default_player` и список команд `summon entity:instant_creeper_explode ~ ~1 ~`, затем `kill @s`. Список команд в исходнике именно в этом порядке, но успешность, порядок относительно соседних add/remove и контекст `@s` нужно испытать. Нельзя обещать убийство игрока, взрыв или точное время по одному объявлению; повторный вызов при looping timer и наложение движения/default также зависят от движка.

`entities/instant_creeper_explode.json:1–12` — **отдельная** `entity:instant_creeper_explode`, не мини-крипер и не `minecraft:creeper`: summonable true, spawnable false, family `[effect99_entities]`, collision 0×0, damage sensor cause all/deals_damage false, `minecraft:explode` fuse_length 0, fuse_lit true, power 4, causes_fire false, destroy_affected_by_griefing true. Фактическое разрушение зависит от игры и правил мира.

## Мини-крипер: условия и переключение компонентов

В гипотетически разобранном `entities/creeper.json:10–86,321–330` событие `minecraft:entity_spawned` содержит один sequence-шаг с фильтром `has_equipment`, subject `other`, domain `hand`, value `effect:creeper_sword`; он добавляет **обе** группы `minecraft:minicreeper` и `minecraft:minicreeper_projectile`. Важная неопределённость — кто именно разрешается как `other` при данном spawn/shoot; простое объявление projectile в item не доказывает прохождение этого фильтра. Отдельное событие `minecraft:minicreeper` добавляет только первую группу; не считать эти два пути одинаковыми.

Если соответствующие группы реально применены:

- Mini: scale 0.3; family `[creeper,player,mob,effect99_entities]` вместо базового `[creeper,monster,mob]`; nearest-attackable-target имеет priority 1, family `monster`, max_dist 16, must_see true; timer `[10,10]`, looping true, `randomInterval:false` вызывает `start_minicreeper_exploding`; sensor внутри 2.5 и damage-событие `has_damage != void` также вызывают его. Наследование и конфликт с базовыми компонентами — предмет проверки, не доказанное замещение во всех условиях.
- Projectile: power 1, gravity 0.02, inertia 1/liquid_inertia 1, impact_damage 1 и knockback true; on-hit вызывает definition event `minecraft:stop_projectile`, target self, affect_projectile true. Это событие удаляет projectile-группу, а не прямо выполняет kill/remove-on-hit. Взрыв mini — другая группа и другой event.
- `start_minicreeper_exploding` добавляет группу с damage sensor cause all/deals_damage false и explode fuse 1.5, power 1, causes_fire false, destroy_affected_by_griefing true. Не следует автоматически предполагать, что цель, timer и damage срабатывают или что их действия суммируются.

## Обычный и заряженный крипер: важное различие stop

В том же файле базовые components объявляют health 20/20, collision 0.6×1.8, movement 0.2, attack damage 3, ближайшую цель family player/max_dist 16 и loot `loot_tables/entities/creeper.json`. Target-nearby sensor с inside 2.5, outside 6, must_see true вызывает start/stop; on-target-escape также указывает stop. Damage sensor с `other` family lightning вызывает `minecraft:become_charged` и содержит `deals_damage:false` — конкретная применимость trigger и фактический урон молнии зависят от семантики компонента.

`minecraft:start_exploding` выбирает разные sequence-шаги по фильтру отсутствия/наличия `minecraft:is_charged`: обычная группа fuse 1.5/power 3 или заряженная fuse 1.5/power 6. `minecraft:become_charged` рядом объявляет remove `minecraft:exploding` и add `minecraft:charged_creeper` с `minecraft:is_charged`. **`minecraft:stop_exploding` удаляет только `minecraft:exploding`**, а не `minecraft:charged_exploding`, `minecraft:forced_exploding`, `minecraft:forced_charged_exploding` или `minecraft:minicreeper_exploding`. Локально в этом файле явного remove этих четырёх групп нет. Это наблюдение о тексте, а не доказательство, что они остаются активны или что взрыв нельзя отменить: может действовать движок, внешний event или иное разрешение компонентов.

`minecraft:start_exploding_forced` аналогично выбирает forced ordinary power 3 или forced charged power 6. Interact требует other family player, `flint_and_steel` в hand и отсутствующий `minecraft:explode`, вызывает forced-событие; содержит hurt_item 1, swing true и звук `ignite`. Forced-группы задают пустые target-nearby-sensor и on-target-escape; не трактовать пустые объекты как гарантированное отключение сенсора на любой версии.

## Путь структуры и не равный ему обычный loot

Только в группе `minecraft:forced_charged_exploding` есть одноразовый timer `[1.4,1.4]` → event `creeper_sword`, рядом explode fuse_length 1.5. По этому событию randomize задаёт weight 95 пусто и 5 команду `structure load creeper_sword ~ ~ ~` (`:123–135,332–341`). При стандартном выборе доля **5/100 условно на вызов event**; разница 1.4 и 1.5 сама по себе не доказывает, что timer гарантированно опередит взрыв или что структура загрузится. Зажигание, заряд, существование сущности, обработка файла, ветвь и команда — отдельные условия.

Файл `Swords_B/structures/creeper_sword.mcstructure` присутствует; [полный NBT](structures-2.8.14.md#creeper_sword) показывает размер `[1,1,1]` и одну item-сущность: `Item.Name:effect:creeper_sword`, `Count:1`, `Damage:0`, `Age:159`. Это сохранённое состояние, а не доказательство успешного получения. Синтаксис и положение при `structure load` нужно проверить.

Привязанная таблица `loot_tables/entities/creeper.json` **не содержит меч**: первый пул — gunpowder, weight 1, set_count 0…2 и looting_enchant 0…1; ещё два отдельных пула с условиями `killed_by_entity` `minecraft:skeleton` и `minecraft:stray` содержат по 12 записей пластинок и один roll. Срабатывание этих условий и результат функций не определяются нашей условной арифметикой. Структурный путь 95/5 нельзя складывать с обычным loot или называть шансом с каждого крипера.

## Что проверить в игре перед переносом

1. Загрузчик исходного файла с лишней `}`; отдельные пробы оригинала и диагностической исправленной копии, без подмены источника.
2. Контекст `other` при `shoot minecraft:creeper` и при обычном spawn, применение mini/projectile-групп и реальное столкновение.
3. Заряжение, зажигание, stop/escape, конфликт групп и таймер 1.4 против fuse 1.5; возможность загрузки структуры и её содержимое.
4. Самовзрыв holder, порядок событий/команд, воздействие на нескольких игроков и блоки, а также gamerule и существование игрока после `kill`.
