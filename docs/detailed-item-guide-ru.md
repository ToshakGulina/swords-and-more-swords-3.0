# Swords and More Swords — подробная памятка по каждому предмету

## Как пользоваться документом

Это развернутый единый документ для проверки собранного материала. В нём **43 карточки точных ID**: 42 предмета 2.x и ещё Sword of Time 1.6. Некоторые из них — материалы, а не мечи. В структуре Google Документа выберите название нужного предмета: внутри указаны характеристики по версиям, материалы ремонта, объявленные рецепты и добыча, описание эффектов, условия, вероятности, отличия старой версии и то, что осталось неясным. В приложении В — полные машинно разобранные определения предметов, чтобы не потерять точные числа и события. Это техническая часть, её можно пропустить при первом чтении.

**Границы:** это преимущественно статический разбор исходных файлов; отдельные серверные испытания обозначены отдельно и не подтверждают остальные механики. Наличие команды, рецепта или условия не доказывает, что конкретная версия Bedrock их примет и выполнит. Условные доли randomize относятся к выбору после выполнения условий, а не автоматически к каждому удару, мобу или сундуку. Веса loot не равны процентам без суммы весов, rolls и других условий. Если поле не указано — не подставляйте ноль, false или бесконечность. Версия текстов скриншотов не установлена; OCR может ошибаться. Все 21 распознанных текста приведены в приложении.

В 1.6 три JSON сущностей не разбираются, в обеих 2.x не разбирается creeper.json; есть повторные ключи. Поэтому гипотетически исправленный в памяти файл и декларацию нельзя принимать за подтверждённую работу. Архивы не менялись. Отдельные проверки оригинала на сервере и личное наблюдение игрока документированы; ремейк не начат.

**Исходники:** 1.6 — 26 определений, 2.8.8 и 2.8.14 — по 42. У одноимённых ID 2.x все item-компоненты структурно совпадают; Ice отличается в событиях и окружении. Другие различия 2.x включают генерацию руд и торговлю. Названия версий взяты из имён архивов.

В повторяющихся подробных разделах сохранены исходные технические термины и уточнения из исследования; они намеренно не заменены выдуманными игровыми результатами. Ссылки на оригинальные скриншоты ведут на Google Диск.

## 01. Bedrock Stick — `effect:bedrock_stick`

**Кратко:** Материал для Bedrock Sword. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

- В 1.6 предмет с этим точным ID не найден.

**2.8.8 / 2.8.14** — определение `Swords_B/items/bedrock_stick.json`.
- урон: `6`; максимальная прочность: не указан; зачарование: не указан; перезарядка: не указан; левая рука: `false`; размер стопки: `1`; свечение: `false`; предмет исчезает: `true`.
- Ремонт: компонент не указан; это не доказывает невозможности ремонта.
- Оружейные хуки: компонент пустой.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 2.8.14:**

- Рецепт `Swords_B/recipes/bedrock_stick.json`; тип `minecraft:recipe_shaped`.
  - Схема сверху вниз: `#` / `#`.
  - Обозначения: `{"#":{"item":"minecraft:bedrock"}}`.
  - Результат: `{"item":"effect:bedrock_stick"}`; рабочие станции/tags: `["crafting_table"]`.

- Определение: `Swords_B/items/bedrock_stick.json`.
- Результаты рецептов: `Swords_B/recipes/bedrock_stick.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Bedrock Stick и Bedrock Sword (`effect:bedrock_stick`, `effect:bedrock_sword`)

[Граф материалов и различия версий](manual-quartz-bedrock-progression.md#bedrock-stick-и-bedrock-sword).

[Полный порядок правил добычи и потенциальные пересечения](manual-digger-2.8.md).

- `items/bedrock_stick.json`: damage 6, stack 1, hand_equipped true, allow_off_hand false, `should_despawn:true`, `can_destroy_in_creative:true`, пустой `minecraft:weapon`; components durability, repairable и enchantable не указаны. Не приписывать автоматически «бесконечную прочность» как установленную семантику без испытания движка. Рецепт `recipes/bedrock_stick.json`: вертикально два `minecraft:bedrock` → палка.
- `items/bedrock_sword.json`: damage 18, max stack 1, offhand false, `should_despawn:false`, `can_destroy_in_creative:false`; durability, repairable и enchantable не указаны, weapon пустой. `digger.use_efficiency:true`, общее условие тега `q.any_tag('stone', 'metal', 'diamond_pick_diggable', 'wood', 'pumpkin', 'plant', 'dirt', 'sand', 'gravel', 'grass', 'snow')` — speed 999; отдельные quartz_diamond_block speed 50, quartz_diamond_ore 100, silver_ore 999; длинный перечень буквальных блоков со скоростью 999 см. [полную карточку](items-2.8.14.md). Список содержит опечатку `minecraft:pumkin`, повторы `quartz_stairs`, `blast_furnace`, `blackstone_wall`: не исправлять незаметно и не считать, что все блоки или bedrock добываются этим компонентом.
- `recipes/bedrock_sword.json`: два `minecraft:bedrock` над `effect:bedrock_stick` вертикально. Изученные альтернативы получения bedrock — взрывные цепочки Nether Star/Ultra Instinct, но реальное получение зависит от правил разрушения в игре. Выброшенный меч, помеченный функцией по имени `§l§7Bedrock Sword`, при `q.is_on_fire` вызывает `item.json` `respawn_event_1`: `structure load bedrock_sword ~ ~1 ~` и `kill @s`. Реконструкция через структуру не доказывает сохранение состояния исходного предмета; см. также условия и порядок тегирования.

**Дополнительный подробный разбор** (источник: `docs/manual-quartz-bedrock-progression.md`):

#### Bedrock Stick и Bedrock Sword

Оба точных ID существуют в 2.x, не в item 1.6. `effect:bedrock_stick` damage 6, stack 1, offhand false, `should_despawn:true`, `can_destroy_in_creative:true`; `effect:bedrock_sword` damage 18, stack 1, offhand false, `should_despawn:false`, `can_destroy_in_creative:false`. У обоих в JSON **пустой** `minecraft:weapon`; durability, repairable и enchantable не объявлены. Эти отсутствия и `should_despawn` нельзя превращать в гарантированную неразрушимость/несгораемость.

Рецепты: `bedrock_stick` = два `minecraft:bedrock` вертикально; `bedrock_sword` = два `minecraft:bedrock` над `effect:bedrock_stick`. При допущении по одному result без count и штатной регистрации: **четыре** bedrock на палку и меч по двум рецептам, если палка ещё не получена и нет альтернатив. В исходных определениях эти рецепты не доказывают доступности или добычи bedrock.

Bedrock Sword объявляет digger с 68 упорядоченными правилами: tags-селектор speed 999; отдельные `quartz_diamond_block` 50, `quartz_diamond_ore` 100, `silver_ore` 999; далее конкретные блоки со speed 999. Там есть буквальный `minecraft:pumkin` и повторы трёх правил; приоритет пересекающихся tags и block IDs не определён этими цифрами. Явного правила `minecraft:bedrock` в списке нет. Отсутствие отдельного правила не доказывает отсутствия внешнего тега, возможности добычи или скорости по умолчанию.

В 2.x тегированный выпавший Bedrock Sword при огне направляется в `respawn_event_1`: `structure load bedrock_sword ~ ~1 ~` и `kill @s`. NBT содержит сохранённую item-сущность этого ID; это **создание из структуры**, а не доказанный перенос прочности, имени, чар или иной информации исходного item. Назначение тега зависит от буквального форматированного имени и последовательности событий.

### Что написано на скриншотах

На изображении вручную считаны: damage = `6`; durability = `"Unbreakable"`. Оригинал: [скриншот 120050](https://drive.google.com/file/d/1QxBp8CUoeiK1tSXeUCHVwz48f_9-dqGc/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 02. Bedrock Sword — `effect:bedrock_sword`

**Кратко:** Связан с добычей блоков и цепочкой Bedrock. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

- В 1.6 предмет с этим точным ID не найден.

**2.8.8 / 2.8.14** — определение `Swords_B/items/bedrock_sword.json`.
- урон: `18`; максимальная прочность: не указан; зачарование: не указан; перезарядка: не указан; левая рука: `false`; размер стопки: `1`; свечение: `false`; предмет исчезает: `false`.
- Ремонт: компонент не указан; это не доказывает невозможности ремонта.
- Оружейные хуки: компонент пустой.
- Правила добычи: 68 записей; точные блоки, скорости и события приведены в полном определении в приложении В.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 2.8.14:**

- Рецепт `Swords_B/recipes/bedrock_sword.json`; тип `minecraft:recipe_shaped`.
  - Схема сверху вниз: `B` / `B` / `#`.
  - Обозначения: `{"#":{"item":"effect:bedrock_stick"},"B":{"item":"minecraft:bedrock"}}`.
  - Результат: `{"item":"effect:bedrock_sword"}`; рабочие станции/tags: `["crafting_table"]`.

- Определение: `Swords_B/items/bedrock_sword.json`.
- Результаты рецептов: `Swords_B/recipes/bedrock_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[35].Mainhand[0].Name
  - `Swords_B/structures/bedrock_sword.mcstructure` $.entities[0].Item.Name

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Bedrock Stick и Bedrock Sword (`effect:bedrock_stick`, `effect:bedrock_sword`)

[Граф материалов и различия версий](manual-quartz-bedrock-progression.md#bedrock-stick-и-bedrock-sword).

[Полный порядок правил добычи и потенциальные пересечения](manual-digger-2.8.md).

- `items/bedrock_stick.json`: damage 6, stack 1, hand_equipped true, allow_off_hand false, `should_despawn:true`, `can_destroy_in_creative:true`, пустой `minecraft:weapon`; components durability, repairable и enchantable не указаны. Не приписывать автоматически «бесконечную прочность» как установленную семантику без испытания движка. Рецепт `recipes/bedrock_stick.json`: вертикально два `minecraft:bedrock` → палка.
- `items/bedrock_sword.json`: damage 18, max stack 1, offhand false, `should_despawn:false`, `can_destroy_in_creative:false`; durability, repairable и enchantable не указаны, weapon пустой. `digger.use_efficiency:true`, общее условие тега `q.any_tag('stone', 'metal', 'diamond_pick_diggable', 'wood', 'pumpkin', 'plant', 'dirt', 'sand', 'gravel', 'grass', 'snow')` — speed 999; отдельные quartz_diamond_block speed 50, quartz_diamond_ore 100, silver_ore 999; длинный перечень буквальных блоков со скоростью 999 см. [полную карточку](items-2.8.14.md). Список содержит опечатку `minecraft:pumkin`, повторы `quartz_stairs`, `blast_furnace`, `blackstone_wall`: не исправлять незаметно и не считать, что все блоки или bedrock добываются этим компонентом.
- `recipes/bedrock_sword.json`: два `minecraft:bedrock` над `effect:bedrock_stick` вертикально. Изученные альтернативы получения bedrock — взрывные цепочки Nether Star/Ultra Instinct, но реальное получение зависит от правил разрушения в игре. Выброшенный меч, помеченный функцией по имени `§l§7Bedrock Sword`, при `q.is_on_fire` вызывает `item.json` `respawn_event_1`: `structure load bedrock_sword ~ ~1 ~` и `kill @s`. Реконструкция через структуру не доказывает сохранение состояния исходного предмета; см. также условия и порядок тегирования.

**Дополнительный подробный разбор** (источник: `docs/manual-quartz-bedrock-progression.md`):

#### Bedrock Stick и Bedrock Sword

Оба точных ID существуют в 2.x, не в item 1.6. `effect:bedrock_stick` damage 6, stack 1, offhand false, `should_despawn:true`, `can_destroy_in_creative:true`; `effect:bedrock_sword` damage 18, stack 1, offhand false, `should_despawn:false`, `can_destroy_in_creative:false`. У обоих в JSON **пустой** `minecraft:weapon`; durability, repairable и enchantable не объявлены. Эти отсутствия и `should_despawn` нельзя превращать в гарантированную неразрушимость/несгораемость.

Рецепты: `bedrock_stick` = два `minecraft:bedrock` вертикально; `bedrock_sword` = два `minecraft:bedrock` над `effect:bedrock_stick`. При допущении по одному result без count и штатной регистрации: **четыре** bedrock на палку и меч по двум рецептам, если палка ещё не получена и нет альтернатив. В исходных определениях эти рецепты не доказывают доступности или добычи bedrock.

Bedrock Sword объявляет digger с 68 упорядоченными правилами: tags-селектор speed 999; отдельные `quartz_diamond_block` 50, `quartz_diamond_ore` 100, `silver_ore` 999; далее конкретные блоки со speed 999. Там есть буквальный `minecraft:pumkin` и повторы трёх правил; приоритет пересекающихся tags и block IDs не определён этими цифрами. Явного правила `minecraft:bedrock` в списке нет. Отсутствие отдельного правила не доказывает отсутствия внешнего тега, возможности добычи или скорости по умолчанию.

В 2.x тегированный выпавший Bedrock Sword при огне направляется в `respawn_event_1`: `structure load bedrock_sword ~ ~1 ~` и `kill @s`. NBT содержит сохранённую item-сущность этого ID; это **создание из структуры**, а не доказанный перенос прочности, имени, чар или иной информации исходного item. Назначение тега зависит от буквального форматированного имени и последовательности событий.

### Что написано на скриншотах

На изображении вручную считаны: damage = `18`; durability = `"Infinite"`; enchantable = `false`. Оригинал: [скриншот 120003](https://drive.google.com/file/d/1tAeJ-EbPeExgoe9AX_AR_p9cgZEangmO/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 03. Bee Sword — `effect:bee_sword`

**Кратко:** Пчёлы при событиях оружия; цветы при удержании. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

- В 1.6 предмет с этим точным ID не найден.

**2.8.8 / 2.8.14** — определение `Swords_B/items/bee_sword.json`.
- урон: `5`; максимальная прочность: `{"max_durability":1080}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `false`; размер стопки: `1`; свечение: `false`; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:bee_sword"]` → `1080`; `["minecraft:honey_block"]` → `400`; `["minecraft:honeycomb"]` → `150`.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`; событие без нанесения урона существу → `{"event":"weapon"}`; удар по блоку → `{"event":"weapon"}`.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 2.8.14:**

- Рецептов с этим точным результатом локально не найдено. Это не исключает других путей.

- Определение: `Swords_B/items/bee_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - `Swords_B/loot_tables/bee_sword.json` $.pools[0].entries[0]: `{"type":"item","name":"effect:bee_sword","weight":1}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

**Условная математическая модель выбора loot в 2.x:**

Числа ниже — вероятность выбрать хотя бы одну запись предмета внутри уже активированного пула, а не шанс реальной добычи. Допущения: все записи доступны; отсутствующий вес принят за 1; quality и условия записей игнорируются; выборы независимы с возвращением; число rolls равномерно в указанном диапазоне. Условия пула считаются уже выполненными. Загрузка таблицы, дополнительный отбор, количество предметов и функции не эмулируются.

- Таблица/пул: `bee_sword.json` / 0; entries: 0; rolls: `1`; вес ID/сумма: 1/1; выбор хотя бы одной записи по модели: **100.0000%**. Условия и оговорки: functions: не задано.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Bee Stinger (`effect:bee_sword`)

[Подробная цепь пчёл и риск setblock](manual-bee-sword.md); [weapon-хуки и условный расход](weapon-event-index.md).

##### Предмет

`Swords_B/items/bee_sword.json`: 1080 прочности, damage 5, max stack 1; enchantability value 9, slot sword; нельзя в левую руку, hand_equipped true. Ремонт: такой же меч 1080, `honey_block` 400, `honeycomb` 150. На web speed 15, bamboo 10. `weapon` привязан ко всем трём хукам `on_hurt_entity`, `on_not_hurt_entity`, `on_hit_block`. Событие последовательно расходует 1 прочности и выбирает: 30/100 — `shoot entity:bee_sword` с launch_power 1, 70/100 — ещё 1 прочность. Это не обязательно означает 30% на каждый успешный урон: набор входных хуков шире, а работа shoot на старом движке требует проверки.

##### Эффект удержания и цветы

- `Swords_B/entities/player.json:1039–1051`: environment sensor проверяет наличие/отсутствие предмета в domain `hand` и вызывает соответственно `minecraft:bee_sword` или `stop_bee_sword_event`. Нельзя без теста предполагать, какие именно слоты попадают в этот domain на старом движке.
- `player.json:22–26,1125–1140`: первая ветвь добавляет группу только если у игрока нет family `bee_sword`; в группе family `[player,bee_sword]` и повторяющийся таймер со случайным интервалом `[3,8]`, событие `bee_sword_flower`. Вторая при наличии family удаляет группу и добавляет `minecraft:default_player`. Порядок и взаимодействие разных групп игрока надо проверить, особенно при смене оружия.
- `player.json:1145–1159`: при каждом вызове `bee_sword_flower` выбирается одна из 12 одинаковых ветвей weight 1. В 11 из них команда `execute ... detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower N`, где N последовательно 0…10; в одной — `yellow_flower 0`. Соответственно каждая ветвь 1/12, но только если выбор дошёл до неё; установка зависит от блока под игроком и выполнения команды. Описание «цветы растут в траве» слишком общее, чтобы восстанавливать точный механизм.

##### Призванная пчела

`Swords_B/entities/bee_entity.json:1–162` — идентификатор `entity:bee_sword`, не spawnable, summonable. По тексту кода: размер 0.5, здоровье 10/10, collision box 0.55×0.5, movement 0.3, flying_speed 0.15; timer looping/randomInterval true `[6,8]` вызывает `despawn`, но событие **не добавляет** объявленную группу `despawn`, а выполняет `tp @s ~ -103 ~`. Не заменять эту команду сразу на удаление сущности без проверки измерения и границы мира.

Пчела не получает урон от источника family `player` и от падения. Она выбирает видимую цель family `monster` (`within_radius:16`, `max_dist:10`, `must_see:true`), имеет melee `speed_multiplier:1.4`, `attack damage:1`, `fatal_poison` duration 3; angry duration 99999, broadcastAnger true, broadcastRange 20. Навигация, приоритеты, параметры hover и остальная физика — в исходном файле. Формулировка «защищает игрока» не доказывает выбор нападающего: фильтр в коде проверяет family цели.

##### Добыча от обычной пчелы

`Swords_B/entities/bee.json:85–107,842–875`: в группе `angry_bee` у `behavior.melee_attack` установлены `attack_once:true` и on_attack → `countdown_to_perish_event`. Его первый шаг — `randomize`: вес 2, с фильтром self family != `bee_sword` и командой `loot spawn ~ ~ ~ loot bee_sword`; вес 98 — пустая ветвь. Следующий шаг удаляет перечисленные группы и добавляет `countdown_to_perish`. В группе `countdown_to_perish` таймер `[10,60]`, randomInterval true, looping false (`bee.json:126–147`). Списки удаления `seek_shelter` и `countdown_to_perish_event` включают `collect_nectar`, однако такой component group в файле нет; не подменять его группой `look_for_food` без проверки загрузчика и ванильного поведения. `Swords_B/loot_tables/bee_sword.json:1–14`: 1 roll, единственный `effect:bee_sword`, weight 1. Это **2/100 на выбор ветви в данном событии**, не доказательство общего шанса при любой атаке или смерти.

[Скриншот описания](https://drive.google.com/file/d/18mrcZhBh-Z3MbkF1Su19Yu7C9HNa31zs/view) тоже сообщает 1080, damage 5, цветы, пчёл и 2%, но является описанием, а не доказательством выполнения ветви. Версия описания не установлена.

**Дополнительный подробный разбор** (источник: `docs/manual-bee-sword.md`):

### Bee Stinger: триггеры, обычная и призванная пчела

В обоих архивах 2.x существуют предмет `effect:bee_sword`, отдельная сущность `entity:bee_sword` и замена `minecraft:bee`; их нельзя считать одним объектом. В архиве 1.6 item ID `effect:bee_sword` отсутствует. Ниже — декларации и условная арифметика, **не** проверка Minecraft, успешного получения меча, цели или времени существования пчелы.

#### Предмет и weapon event

`Swords_B/items/bee_sword.json`: damage **5**, max durability **1080**, stack **1**, `allow_off_hand:false`, hand_equipped true, enchantable `{value:9,slot:sword}`, ремонт self **1080**, `minecraft:honey_block` **400**, `minecraft:honeycomb` **150**. Digger web **15**, bamboo **10**, use_efficiency true. Все три `on_hurt_entity`, `on_not_hurt_entity`, `on_hit_block` указывают на `weapon`: sequence сначала содержит durability damage **1**, затем randomize вес **30** — `shoot entity:bee_sword` launch_power **1**, вес **70** — ещё durability damage **1**.

При условии выполнения всего события и стандартного выбора по весам условные суммы прямых damage — **1 с 30%**, **2 с 70%**, средняя **1.7**. Это не фактический расход на удар/блок: стандартный износ, поведение shoot, ранняя поломка, порядок/число хуков и зачарования не учтены ([индекс 42 предметов](weapon-event-index.md)). Попадание, спавн и поведение пчелы не гарантируются самим weight 30.

#### Цветы и потенциальная замена блока

Player sensor проверяет `has_equipment` domain `hand`, затем event добавляет группу при family `!= bee_sword`. Группа содержит family `[player,bee_sword]`, looping timer с `randomInterval:true`, время `[3,8]`, событие `bee_sword_flower`. Stop при family `bee_sword` удаляет группу и добавляет `minecraft:default_player`. Единицы и реальную частоту, повторное добавление группы и переключение оружия надо испытать.

`bee_sword_flower` содержит 12 ветвей по **weight 1**. Каждая выполняет `execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ …`: 11 вариантов `red_flower` с data **0…10**, одна `yellow_flower 0`. При стандартном равномерном выборе это **1/12 на каждую строку**, суммарно **11/12** на red и **1/12** на yellow, условно на вызов/выбор; detect grass и возможный неуспех команды дополнительно влияют на результат.

В этих 12 командах detect проверяет **блок под игроком**, а не пустоту целевой позиции `~ ~ ~`. После `setblock` нет явного режима `keep` и нет отдельного detect air. Поэтому нельзя описывать команды как гарантированно ставящие цветок только в воздух: они **потенциально** затрагивают уже существующий блок в позиции игрока. Фактический default mode setblock, совместимость data 0…10, защита блоков и результат требуют испытания; не считать, что все 12 вариантов обязательно допустимы в новой версии.

#### Призванная `entity:bee_sword`

`Swords_B/entities/bee_entity.json` описывает отдельный ID `entity:bee_sword`, spawnable false, summonable true; он не является просто ссылкой на `minecraft:bee.json`. Базовая family **`[bee,mob,arthropod]` не содержит `bee_sword`**, хотя такая строка присутствует в ID. Внутри этого файла среди component_groups объявлена `despawn`, а среди events — только `despawn`: он выполняет `tp @s ~ -103 ~`, **не** add `despawn` и не `kill`. Timer looping/randomInterval true `[6,8]` вызывает этот event. Значение y **−103 абсолютное**, x/z относительные; поведение вне мира и последствия телепортации не установлены.

Основные численные объявления: health **10/10**, scale **0.5**, collision **0.55×0.5**, movement **0.3**, flying_speed **0.15**, `follow_range:1024`; `behavior.nearest_attackable_target` priority **1**, within_radius **16**, max_dist **10**, must_see true, фильтр цели `other` family `monster`; melee priority **1**, speed_multiplier **1.4**, track_target true; атака damage **1**, fatal_poison duration **3**. Angry duration **99999**, broadcastAnger true/range **20**, lava condition damage_per_tick **4**. Радиусы/приоритеты не следует сводить к одному гарантированному эффективному диапазону.

Damage_sensor запрещает damage, когда `other` имеет family `player`, и отдельно cause fall. Это не все виды урона и не проверка ID владельца. В полной Wolf-группе player может иметь family `[wolf,wolf_sword,complete_wolf_transformation,monster]`, **без `player`**, тогда как bee target-filter ищет family `monster`. Поэтому при условном одновременном применении этих семейств/фильтров player в Wolf-состоянии может не подходить под защиту `other family player` и может подходить под выбор цели пчелы. Дистанция, видимость, приоритеты и фактическая обработка групп не проверены; это риск для испытания, не доказательство нападения на владельца. См. [условия Wolf](manual-wolf-conditions-2.8.md).

#### Обычная `minecraft:bee` и источник меча

В `Swords_B/entities/bee.json` angry_bee содержит `minecraft:behavior.melee_attack`, priority **2**, attack_once true, speed_multiplier **1.4**, `on_attack` → `countdown_to_perish_event` target self. Первый шаг этого события — randomize: weight **2**, filter self family `!= bee_sword`, команда `loot spawn ~ ~ ~ loot bee_sword`; weight **98** — пусто. Следующий шаг удаляет перечисленные группы, в том числе локально отсутствующую `collect_nectar`, и добавляет `countdown_to_perish`.

В `countdown_to_perish` объявлены mark_variant **1**, panic priority **1**/speed_multiplier **1.25**/force true, timer `[10,60]`, randomInterval true, looping false, event `perish_event`, и family `[bee,mob,arthropod,pacified]`. `loot_tables/bee_sword.json` содержит один roll и одну запись `effect:bee_sword`, weight **1**. Сопоставление локального `loot bee_sword` с таблицей, работоспособность и момент on_attack требуют движка.

**2/100 не означает 2% на любую смерть пчелы.** Оно относится к записанному randomize в конкретном событии, при выполнении filter и принятой семантике фильтрации/весов. Неизвестно, выбираются ли недопустимые ветви до или после нормализации, сколько раз событие может вызваться и будет ли команда успешна. Не доказывать общую частоту убийств/получения.

У призванной отдельной `entity:bee_sword` family также не содержит `bee_sword`, но в её локальном файле **нет** event `countdown_to_perish_event`: отсутствие этой family не доказывает, что её укус исполнит код обычной `minecraft:bee`. Внешнее/ванильное поведение и любые дополнительные компоненты нужно проверить отдельно.

### Что написано на скриншотах

На изображении вручную считаны: damage = `5`; durability = `1080`; enchantable = `true`; repairable = `true`. Оригинал: [скриншот 115821](https://drive.google.com/file/d/18mrcZhBh-Z3MbkF1Su19Yu7C9HNa31zs/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 04. Blaze Sword — `effect:blaze_sword`

**Кратко:** Огненные снаряды и отдельный активируемый навык. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

**1.6** — определение `Sword_B/items/blaze_sword.json`.
- урон: `8`; максимальная прочность: `{"max_durability":2300}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `true`; размер стопки: `1`; свечение: не указан; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:blaze_sword"]` → `2300`.
- Оружейный компонент не указан.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**2.8.8 / 2.8.14** — определение `Swords_B/items/blaze_sword.json`.
- урон: `6`; максимальная прочность: `{"max_durability":2300}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: `{"category":"blaze_sword","duration":20}`; левая рука: `false`; размер стопки: `1`; свечение: `false`; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:blaze_sword"]` → `2300`.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`; событие без нанесения урона существу → `{"event":"weapon"}`; удар по блоку → `{"event":"weapon"}`.
- При использовании предмета указано: `{"on_use":{"event":"on_use"}}`.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 1.6:**

- Рецепт `Sword_B/recipes/blaze_sword.json`; тип `minecraft:recipe_shaped`.
  - Схема сверху вниз: `F` / `F` / `E`.
  - Обозначения: `{"E":{"item":"minecraft:blaze_rod"},"F":{"item":"minecraft:blaze_powder"}}`.
  - Результат: `{"item":"effect:blaze_sword"}`; рабочие станции/tags: `["crafting_table"]`.

- Определение: `Sword_B/items/blaze_sword.json`.
- Результаты рецептов: `Sword_B/recipes/blaze_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

**Архив 2.8.14:**

- Рецептов с этим точным результатом локально не найдено. Это не исключает других путей.

- Определение: `Swords_B/items/blaze_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - `Swords_B/loot_tables/entities/blaze.json` $.pools[1].entries[0]: `{"type":"item","name":"effect:blaze_sword","weight":1,"functions":[{"function":"set_data","data":0}]}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[16].Mainhand[0].Name

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

**Условная математическая модель выбора loot в 2.x:**

Числа ниже — вероятность выбрать хотя бы одну запись предмета внутри уже активированного пула, а не шанс реальной добычи. Допущения: все записи доступны; отсутствующий вес принят за 1; quality и условия записей игнорируются; выборы независимы с возвращением; число rolls равномерно в указанном диапазоне. Условия пула считаются уже выполненными. Загрузка таблицы, дополнительный отбор, количество предметов и функции не эмулируются.

- Таблица/пул: `entities/blaze.json` / 1; entries: 0; rolls: `1`; вес ID/сумма: 1/1; выбор хотя бы одной записи по модели: **100.0000%**. Условия и оговорки: pool conditions: `[{"condition":"killed_by_entity","entity_type":"minecraft:snow_golem"},{"condition":"random_chance_with_looting","chance":0.025,"looting_multiplier":0.02}]`; functions: `[{"function":"set_data","data":0}]`.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Blaze Sword: цепочка навыка и два разных способа получения

[Сопоставление предмета и цепочек 1.6/2.x](manual-companion-projectile-swords.md#blaze-sword).

Прямые данные предмета — в [общем статусе](analysis-status.md#blaze-sword-effectblaze_sword). Дополнительно:

- `player.json:355–419`: в базовой группе damage_sensor отменяет `fire` и `fire_tick`; `hurt_on_condition` задаёт `in_water_or_rain`, cause drowning и damage_per_tick 1; looping timer `[1,1]` вызывает `blaze_sword_effects`. On-use добавляет `blaze_sword_skill` с family `[player,blaze_sword,blaze_sword_skill]` и одноразовым timer `[6,6]` → event `blaze_sword_skill`. Это событие добавляет `shoot_small_fireball`: **четыре** независимые записи spawn_entity `entity:fake_fireball`, каждая min_wait 0/max_wait 1, single_use true, num 1, spawn_event set_sound; ещё один одноразовый timer `[2,2]` → stop_blaze_sword_skill. Не предполагать, что четыре выстрела успешны или происходят одновременно.
- `player.json:2163–2264`: при удержании команды отправляют `minecraft:inertia_disable` всем `@e[family=shot_by_the_blaze,r=7]`; два fill обновляют `effect99:lightblock2` в кубе ±1. Для family blaze_sword_skill randomize имеет шесть ветвей weight 5 (пять отдельных положений частиц и один звук) и пустую ветвь weight 95, всего **125**, поэтому каждая из шести ветвей имеет 5/125 = 4%, пустая — 95/125 = 76%, условно на выбор. Отдельный `blaze_sword_effects` имеет шесть равных весов 1. При прекращении удаляются группы `minecraft:blaze_sword` и `shoot_small_fireball`, очищаются levitation и slow_falling, добавляется default_player; `blaze_sword_skill` в этом списке не указан — поведение таймера при преждевременной смене меча требуется испытать.
- `entities/fake_fireball.json:1–52`: runtime snowball, collision 0.31×0.31, power 1.3, gravity 0.02, inertia и liquid_inertia 1, offset `[0,0.5,0]`, impact damage 5, knockback false, catch_fire true, remove_on_hit, звук ghast fireball в r=16. Указывается `is_summonable:false`, хотя создаётся через spawn_entity; проверить поддержку движком. У `minecraft:small_fireball` отдельная группа `minecraft:inertia_disable` с power 0, gravity 0.06, inertia 0 и liquid_inertia 0; не путать с fake_fireball.
- `loot_tables/entities/blaze.json:34–57`: один пул на меч содержит условие `killed_by_entity` с `minecraft:snow_golem`, `random_chance_with_looting` base **0.025** и multiplier **0.02**, один roll, меч weight 1, set_data 0. `entities/blaze.json:14–16` явно привязывает таблицу `loot_tables/entities/blaze.json`. Скриншот описывает 0.5% при убийстве снежным големом, но база в этом пуле — **2.5%**, не 0.5%; итоговую вероятность и работу условия нужно проверить на соответствующей версии.
- Другая цепочка: `entities/blaze.json:127–136` содержит событие с weight 995 пусто / 5 `structure load blaze_sword ~ ~ ~`, то есть 5/1000 при вызове события. Однако в **обоих** архивах 2.8.x нет структуры `blaze_sword.mcstructure`, а прямой вызов данного события в просмотренных текстовых файлах не найден. Это отдельный путь, его нельзя складывать с loot-pool или принимать за гарантированно действующий. Отсутствие файла зафиксировано в [реестре структур](structures-2.8.14.md); возможная внешняя структура и динамические вызовы пока не исключены.

**Старая версия 1.6** (источник: `docs/manual-traces-1.6.md`):

#### Blaze и Bone: краткие различия и ошибки JSON 1.6

[Счётчики Blaze, Bone, Shulker, Slime и Lapis: порядок команд и межигровые риски](manual-counter-helpers-1.6.md).

`items/blaze_sword.json` задаёт damage 8 и offhand true (в 2.8.14 — 6 и false), `items/bone_sword.json` — damage 7 и offhand true (в 2.8.14 — 5 и false). Их сенсоры создают `entity:blaze`/`entity:bone`, контроллеры используют глобальные objectives `b`/`bn`, добавляют 1 ближайшему игроку, при ровно 10 призывают `entity:blaze2`/`entity:bone2`, при 5000 удаляют objective, при 4990 содержат буквальную команду `kill @e[...] ~ 0 ~`, далее `swords=2` всем игрокам. В архиве 1.6 вспомогательные `entities/blaze2.json` и `bone2.json` не разбираются JSON5; вывод об исполнении/работоспособности и старом синтаксисе kill нельзя делать только по тексту. Также 1.6 `shulker2.json` не проходит JSON5. Ни один из этих дефектов не исправлен в архиве.

##### Что написано в повреждённых helper-файлах

В каждом из `blaze2.json`, `bone2.json`, `shulker2.json` JSON5 останавливается на **последней лишней закрывающей скобке** (строки 78, 75, 75 соответственно). Для диагностики в памяти удалена только последняя `}`: тогда каждый текст разбирается JSON5. Это гипотетическая структура, а не исправление архива и не свидетельство, что исходный Bedrock примет файл. Данные ниже непосредственно видны в исходном тексте:

| ID | health | collision | Цель `other` family monster / max_dist | Ranged attack | Shooter |
|---|---:|---|---:|---|---|
| `entity:blaze2` | 5/5 | 0×0 | 64; must_see false | priority 1, speed_multiplier 2, attack_interval 1, attack_radius 48, charge_shoot_trigger 1, charge_charged_trigger 1 | type `smallfireball`, def `minecraft:small_fireball` |
| `entity:bone2` | 5/5 | 0×0 | 64; must_see false | attack_interval_min 1, max 3, radius 48; priority не указан | type `Arrow`, def `minecraft:arrow` |
| `entity:shulker2` | 1/1 | 0×0 | 16; must_see false | priority 1, attack_interval_min 1, max 3, radius 15 | def `minecraft:shulker_bullet` |

У всех movement 0, follow_range value/max 64, 64 и 16 соответственно, persistent и pushable true, physics `{}`. Фактическое создание, выстрелы, интерпретация интервалов и дополнительная ошибка в команде kill контроллеров требуют проверки. Исправленная в памяти версия не используется как эталон для ремейка.

**Дополнительный подробный разбор** (источник: `docs/manual-companion-projectile-swords.md`):

#### Blaze Sword

**Предмет и получение.** 1.6 damage 8, durability и self repair 2300; рецепт `F/F/E`, F = `minecraft:blaze_powder`, E = `minecraft:blaze_rod`. В 2.x damage 6, durability и self repair 2300, cooldown `blaze_sword` duration 20. Рецепта с точным result ID локально не найдено. Локальная таблица `loot_tables/entities/blaze.json` прямо привязана в `entities/blaze.json`: отдельный pool требует `killed_by_entity` `minecraft:snow_golem`, `random_chance_with_looting` chance 0.025 и multiplier 0.02, один roll и один меч. Это не шанс любой смерти blaze. Другой entity-event содержит выбор 995 пусто / 5 `structure load blaze_sword`, но одноимённая структура в 2.x архивах отсутствует; пути не складываются автоматически.

**1.6.** Hand sensor → `minecraft:blaze_sword` → spawn `entity:blaze`, wait 0/0, num 1, single_use true → `controller.animation.blaze`. Два одинаковых on_entry телепортируют все выбираемые `entity:blaze2` на y+2 от `@p`, создают global objective `b`, увеличивают score `@p`, при score 10 вызывают `entity:blaze2`, при 5000 удаляют objective, при 4990 содержат kill с буквальными лишними аргументами `~ 0 ~`, затем всем `@a` задают `swords=2`. Удаление objective стоит раньше kill; выбираемые на каждом шаге игроки не обязаны совпадать. `entities/blaze2.json` не разбирается JSON5: после удаления одной последней `}` **только в памяти** диагностически видны health 5, цель family monster и shooter `minecraft:small_fireball`. Это не исправление архива и не доказательство, что файл принимается Bedrock.

**2.x.** Каждый из трёх weapon-хуков объявляет прямой расход 1, затем randomize weight 14 → `minecraft:small_fireball` и fire_resistance, weight 1 → `minecraft:fireball` и fire_resistance, weight 85 → ещё 1 износа; при нормализованном выборе это 14%/1%/85% на вызов, не на успешную атаку. On-use отдельно задаёт durability 10, `event entity @s[family=blaze_sword] blaze_sword_skill_event`, levitation 7 amplifier 0 и slow_falling 10 amplifier 3; порядок соседних полей damage/run_command не установлен.

Группа игрока отменяет damage для `fire` или `fire_tick`, но также задаёт `hurt_on_condition` при `in_water_or_rain`, cause drowning, damage_per_tick 1; не обобщать это на другие типы урона. Навык добавляет группу с таймером `[6,6]` → `blaze_sword_skill` → `shoot_small_fireball` с четырьмя записями `entity:fake_fireball` wait 0…1, single_use true, num 1 и timer `[2,2]` для остановки. Это не четыре гарантированных попадания. Для skill randomize шесть ветвей весом 5 и пустая 95, сумма **125**, а не 100; stop не перечисляет саму группу `blaze_sword_skill`. Fake fireball и выдаваемые weapon `minecraft:small_fireball` — разные определения. [Полная цепочка, фильтры и получение](manual-traces-2.8.14.md#blaze-sword-цепочка-навыка-и-два-разных-способа-получения).

### Что написано на скриншотах

На изображении вручную считаны: damage = `6`; durability = `2300`; enchantable = `true`; repairable = `true`. Оригинал: [скриншот 115826](https://drive.google.com/file/d/18SAkmYz1M8hva9FAv8bJfFTWOM7OD8F6/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 05. Bone Sword — `effect:bone_sword`

**Кратко:** Стрелы и цепочка, связанная с ростом растений. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

**1.6** — определение `Sword_B/items/bone_sword.json`.
- урон: `7`; максимальная прочность: `{"max_durability":820}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `true`; размер стопки: `1`; свечение: не указан; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:bone_sword"]` → `820`.
- Оружейный компонент не указан.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**2.8.8 / 2.8.14** — определение `Swords_B/items/bone_sword.json`.
- урон: `5`; максимальная прочность: `{"max_durability":820}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `false`; размер стопки: `1`; свечение: `false`; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:bone_sword"]` → `820`; `["minecraft:bone"]` → `70`; `["minecraft:bone_block"]` → `300`; `["minecraft:bone_meal"]` → `18`.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`; событие без нанесения урона существу → `{"event":"weapon"}`; удар по блоку → `{"event":"weapon"}`.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 1.6:**

- Рецепт `Sword_B/recipes/bone_sword.json`; тип `minecraft:recipe_shaped`.
  - Схема сверху вниз: `F` / `F` / `E`.
  - Обозначения: `{"E":{"item":"minecraft:bone"},"F":{"item":"minecraft:bone_block"}}`.
  - Результат: `{"item":"effect:bone_sword"}`; рабочие станции/tags: `["crafting_table"]`.

- Определение: `Sword_B/items/bone_sword.json`.
- Результаты рецептов: `Sword_B/recipes/bone_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

**Архив 2.8.14:**

- Рецептов с этим точным результатом локально не найдено. Это не исключает других путей.

- Определение: `Swords_B/items/bone_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[13].Mainhand[0].Name
  - `Swords_B/structures/bone_sword.mcstructure` $.entities[0].Item.Name

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Bone Sword (`effect:bone_sword`)

[Сопоставление предмета и цепочек 1.6/2.x](manual-companion-projectile-swords.md#bone-sword).

- `items/bone_sword.json`: damage 5, durability 820, enchantability 9/sword, repair self 820, bone 70, bone_block 300, bone_meal 18, offhand false; web 15/bamboo 10. Все три weapon-хука: расход 1, затем 20/100 `shoot minecraft:arrow` power 1 либо 80/100 ещё 1 durability. Результирующий износ по этим ветвям 1 или 2 при условии исполнения действий; нельзя сводить к 20% только успешных ударов.
- `player.json`: сенсор hand добавляет family `[player,bone_sword]` и looping timer `[1,1]`, событие `bone_sword_skills` выполняет `summon entity:grows_crop ~ ~0.1 ~ grows_crop_event`. В том же событии удержания выполняется `event entity @e[family=arrow,r=8] minecraft:inertia_disable`: фильтр **family arrow**, не принадлежность врагу. `entities/arrow.json` при этом событии снимает четыре перечисленные группы и добавляет projectile power 0, gravity 1, inertia/liquid_inertia 0, impact damage 1, критический диапазон 9…10 и power_multiplier 0.97; уже летящие стрелы и одновременные группы требуют теста. В `entity_spawned` стрелы при `other` с bone sword получает `despawn_arrow`: таймер 1 и projectile с damage `[1,4]`, family `[bone_sword_arrow,effect99_entities]`; наличие стрелы нужной family зависит от взаимодействия других групп и `other`.
- `entities/grows_crop.json`: `entity:grows_crop` с runtime bee, возраст duration 1, grows_crop chance 0.5/charges 10; событие запускает looping timer 0.3 с `grows_crop`. Его команды вызывают 13 сущностей на y+0.1: центр, восемь соседей в квадрате x/z ±1, четыре по осям на расстоянии 2. Дочерние summon не передают `grows_crop_event`; нельзя считать их рекурсивными таймерами без подтверждения. Точные единицы ageable и конкуренция despawn с timer требуют эксперимента.
- `entities/skeleton.json`: sensor при фатальном damage от family player вызывает `bone_sword`, который при biome tag desert и `is_brightness < 0.49` выбирает 993 пусто / 7 `structure load bone_sword`. 0.7% — только при прохождении этих условий и вызове выбора, а не любая смерть скелета ночью; brightness — не прямой тест времени суток. Два экземпляра sensor присутствуют в различных группах, порядок действия зависит от состояния.

**Старая версия 1.6** (источник: `docs/manual-traces-1.6.md`):

#### Blaze и Bone: краткие различия и ошибки JSON 1.6

[Счётчики Blaze, Bone, Shulker, Slime и Lapis: порядок команд и межигровые риски](manual-counter-helpers-1.6.md).

`items/blaze_sword.json` задаёт damage 8 и offhand true (в 2.8.14 — 6 и false), `items/bone_sword.json` — damage 7 и offhand true (в 2.8.14 — 5 и false). Их сенсоры создают `entity:blaze`/`entity:bone`, контроллеры используют глобальные objectives `b`/`bn`, добавляют 1 ближайшему игроку, при ровно 10 призывают `entity:blaze2`/`entity:bone2`, при 5000 удаляют objective, при 4990 содержат буквальную команду `kill @e[...] ~ 0 ~`, далее `swords=2` всем игрокам. В архиве 1.6 вспомогательные `entities/blaze2.json` и `bone2.json` не разбираются JSON5; вывод об исполнении/работоспособности и старом синтаксисе kill нельзя делать только по тексту. Также 1.6 `shulker2.json` не проходит JSON5. Ни один из этих дефектов не исправлен в архиве.

##### Что написано в повреждённых helper-файлах

В каждом из `blaze2.json`, `bone2.json`, `shulker2.json` JSON5 останавливается на **последней лишней закрывающей скобке** (строки 78, 75, 75 соответственно). Для диагностики в памяти удалена только последняя `}`: тогда каждый текст разбирается JSON5. Это гипотетическая структура, а не исправление архива и не свидетельство, что исходный Bedrock примет файл. Данные ниже непосредственно видны в исходном тексте:

| ID | health | collision | Цель `other` family monster / max_dist | Ranged attack | Shooter |
|---|---:|---|---:|---|---|
| `entity:blaze2` | 5/5 | 0×0 | 64; must_see false | priority 1, speed_multiplier 2, attack_interval 1, attack_radius 48, charge_shoot_trigger 1, charge_charged_trigger 1 | type `smallfireball`, def `minecraft:small_fireball` |
| `entity:bone2` | 5/5 | 0×0 | 64; must_see false | attack_interval_min 1, max 3, radius 48; priority не указан | type `Arrow`, def `minecraft:arrow` |
| `entity:shulker2` | 1/1 | 0×0 | 16; must_see false | priority 1, attack_interval_min 1, max 3, radius 15 | def `minecraft:shulker_bullet` |

У всех movement 0, follow_range value/max 64, 64 и 16 соответственно, persistent и pushable true, physics `{}`. Фактическое создание, выстрелы, интерпретация интервалов и дополнительная ошибка в команде kill контроллеров требуют проверки. Исправленная в памяти версия не используется как эталон для ремейка.

**Дополнительный подробный разбор** (источник: `docs/manual-companion-projectile-swords.md`):

#### Bone Sword

**Предмет и получение.** 1.6 damage 7, durability/self repair 820; рецепт `F/F/E`, F = `minecraft:bone_block`, E = `minecraft:bone`. 2.x damage 5, durability 820, self repair 820, bone 70, bone_block 300, bone_meal 18; прямой локальный recipe и loot entry с точным ID не найдены. В `skeleton.json` sensor при фатальном уроне от family player вызывает event `bone_sword`: при biome tag desert и `is_brightness < 0.49` randomize 993 пусто / 7 `structure load bone_sword`; локальная структура содержит сохранённую item-сущность нужного ID. 0.7% — условно на вызванный выбор при стандартной семантике, не шанс любого убийства и не прямой тест ночи.

**1.6.** Hand sensor создаёт `entity:bone` с wait 0/0, num 1, single_use true → `controller.animation.bone`. Общий objective `bn`, увеличение `@p`, summon `entity:bone2` при score 10, удаление objective при 5000, буквальный kill с `~ 0 ~` при 4990, глобальный `@a swords=2`. До счёта всем выбираемым `entity:bone2` предписан tp к `@p` на y+2. JSON5 не принимает `entities/bone2.json` из-за последней `}`; диагностически удалив её в памяти, получаем объявление цели monster и shooter `minecraft:arrow`. Как и с Blaze, это лишь восстановление для чтения, а не исправление или доказательство исполнения.

**2.x.** Три weapon-хука сначала задают расход 1, затем выбор 20 → стрелять `minecraft:arrow` launch_power 1 либо 80 → ещё расход 1. Числа — условные веса на вызов соответствующего хука; эффект стандартного износа не определён этим расчётом. Hand event отправляет `minecraft:inertia_disable` всем `@e[family=arrow,r=8]`, не только выпущенным самим игроком. Добавленная player-группа имеет timer `[1,1]` looping → `summon entity:grows_crop ~ ~0.1 ~ grows_crop_event`. Helper runtime bee имеет ageable duration 1, `minecraft:grows_crop` chance 0.5/charges 10. Начальный event добавляет looping timer `[0.3,0.3]`; при timer-event 13 summon создают центр, восемь соседей ±1 и четыре осевые точки на расстоянии 2. **Дочерние команды не передают `grows_crop_event`**; рекурсивное создание таймеров не следует из текста. Семейства, стрелы и конкуренция timer/ageable — в [полной трассе](manual-traces-2.8.14.md#bone-sword-effectbone_sword).

### Что написано на скриншотах

На изображении вручную считаны: damage = `5`; durability = `820`; enchantable = `true`; repairable = `true`. Оригинал: [скриншот 115955](https://drive.google.com/file/d/1a7kOeS7_zMxTw7QFgoCGLAlh_f1O3_vp/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 06. Cactus Sword — `effect:cactus_sword`

**Кратко:** Команды урона рядом и самому владельцу. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

**1.6** — определение `Sword_B/items/cactus_sword.json`.
- урон: `6`; максимальная прочность: `{"max_durability":125}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `true`; размер стопки: `1`; свечение: не указан; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:cactus_sword"]` → `125`.
- Оружейный компонент не указан.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**2.8.8 / 2.8.14** — определение `Swords_B/items/cactus_sword.json`.
- урон: `6`; максимальная прочность: `{"max_durability":125}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `false`; размер стопки: `1`; свечение: `false`; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:cactus_sword"]` → `125`.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 1.6:**

- Рецепт `Sword_B/recipes/cactus_sword.json`; тип `minecraft:recipe_shaped`.
  - Схема сверху вниз: `F` / `F` / `E`.
  - Обозначения: `{"E":{"item":"minecraft:stick"},"F":{"item":"minecraft:cactus"}}`.
  - Результат: `{"item":"effect:cactus_sword"}`; рабочие станции/tags: `["crafting_table"]`.

- Определение: `Sword_B/items/cactus_sword.json`.
- Результаты рецептов: `Sword_B/recipes/cactus_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

**Архив 2.8.14:**

- Рецепт `Swords_B/recipes/cactus_sword.json`; тип `minecraft:recipe_shaped`.
  - Схема сверху вниз: `F` / `F` / `E`.
  - Обозначения: `{"E":{"item":"minecraft:stick"},"F":{"item":"minecraft:cactus"}}`.
  - Результат: `{"item":"effect:cactus_sword"}`; рабочие станции/tags: `["crafting_table"]`.

- Определение: `Swords_B/items/cactus_sword.json`.
- Результаты рецептов: `Swords_B/recipes/cactus_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[24].Mainhand[0].Name

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Cactus Sword (`effect:cactus_sword`)

[Полная сравнительная карточка 1.6/2.x](manual-basic-swords.md#cactus-sword).

- `Swords_B/items/cactus_sword.json`: damage 6, max durability 125, max stack 1, enchantable slot sword/value 9, offhand false, ремонт только таким же мечом на 125. На `on_hurt_entity` событие расходует 1 прочности; два других weapon-хука в этом определении не заданы. Web speed 15, bamboo 10. Указаны специальные смещения main hand: first person `[0.67,0,-1.24]`, third person `[0.36,1.5,-0.66]`.
- `recipes/cactus_sword.json`: shaped crafting_table, вертикально `F/F/E`; F — `minecraft:cactus`, E — `minecraft:stick`, результат cactus sword. Других путей, кроме точных текстовых совпадений, этот поиск не исключает.
- `entities/player.json:343–347,670–679,2117–2135`: сенсор проверяет `has_equipment` в domain `hand`, при наличии добавляет группу с family `[player,cactus_sword]`, таймер `[0.5,0.5]`, looping true; его `cactus_sword_skills` выполняет последовательно `damage @e[r=1.4,type=!player] 1 contact entity @s` и `damage @s 1 contact`. Исключены все игроки из первого селектора, но сам носитель получает отдельную команду; видимые повреждения зависят от исполнения и защит движка. При отсутствии предмета удаляется группа и добавляется default_player. Нельзя считать, что радиус гарантированно измеряется от корпуса или что каждая команда успешно наносит урон.

**Старая версия 1.6** (источник: `docs/manual-traces-1.6.md`):

#### Cactus Sword: 1.6 против 2.8.14

[Полная сравнительная карточка 1.6/2.x](manual-basic-swords.md#cactus-sword).

`Sword_B/items/cactus_sword.json`: damage 6, durability 125, enchantability 9/sword, repair self 125, offhand true, web 15/bamboo 10. Тот же ID в 2.8.14 имеет offhand false и другую механику повреждения. 1.6: sensor игрока добавляет группу спавна `entity:cactus`; он подключает `controller.animation.cactus` (`entities/cactus.json`, `animation_controllers/cactus_sword.json`). Оба состояния при входе выполняют одинаковую последовательность: создать objective `ct`, добавить 1 ближайшему `@p` и сущностям `@e[r=3,type=!entity:cactus,type=!player]`; ближайшему игроку со score ровно 1 и отдельно всем `@e[scores={ct=1},r=2]` назначить poison 1 с amplifier 1 и скрытыми частицами; при `@p[scores={ct=20}]` удалить objective `ct`; всем игрокам `swords=2`. Это команды яда, не прямые `damage ... contact` из 2.8.14. Селекторы, ошибки повторного создания objective и конфликт счётчиков имеют значение; длительность и период действия не доказаны без игры.

**Дополнительный подробный разбор** (источник: `docs/manual-basic-swords.md`):

#### Cactus Sword

**Характеристики/рецепт.** Все версии имеют damage 6 и durability 125, self repair 125. Рецепт `recipes/cactus_sword.json` одинаков по разобранному содержимому: `F/F/E`, F = `minecraft:cactus`, E = `minecraft:stick`. 2.x дополнительно задаёт render_offsets main hand: first-person position `[0.67,0,-1.24]`, third-person `[0.36,1.5,-0.66]`; прочие transform не объявлены, поэтому не подставлять нулевые значения. PNG 1.6 16×16, 2.x 21×21, оба PNG 2.x одинаковы по SHA-256; детали — [сравнение значков](icon-comparison.md).

**1.6.** `animation_controllers/cactus_sword.json` в обоих состояниях последовательно: создать objective `ct`; прибавить `@p ct 1`; прибавить `@e[r=3,type=!entity:cactus,type=!player] ct 1`; через `execute @p[scores={ct=1}]` выдать `effect @s poison 1 1 true`; отдельно через `@e[scores={ct=1},r=2]` выдать тот же effect; при `@p[scores={ct=20}]` удалить objective `ct`; установить `@a swords 2`. Второй селектор отравления **не** исключает игроков и не является копией селектора прибавления: подходящий игрок может фигурировать в обеих проверках. Удаление objective глобально по имени, а не только сброс одного игрока. Это текст и возможное пересечение, а не гарантия двойного воздействия.

**2.x.** Sensor игрока по `hand` вызывает `minecraft:cactus_sword`; при family != `cactus_sword` добавляется группа с family `[player,cactus_sword]` и timer `time:[0.5,0.5]`, `looping:true`, `time_down_event:cactus_sword_skills`, target self. Событие имеет две команды в порядке: `damage @e[r=1.4,type=!player] 1 contact entity @s`, затем `damage @s 1 contact`. Таким образом, первая строка исключает entity **типа** player, вторая адресована самому исполнителю; они не означают только отравление 1.6. Сенсор с operator `!=` вызывает stop, который при family `cactus_sword` удаляет соответствующую группу и добавляет `minecraft:default_player`. Время реального цикла, одновременные группы, успешность damage и последствия смены предмета по этим записям не определяются.

### Что написано на скриншотах

На изображении вручную считаны: damage = `6`; durability = `125`; enchantable = `true`; repairable = `true`. Оригинал: [скриншот 115853](https://drive.google.com/file/d/1g4UIpjMFNG1uYe8hAo8IOzVw5ctqxL-i/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 07. Clock Sword — `effect:clock_sword`

**Кратко:** Навык с изменением времени и глобальных правил мира. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

- В 1.6 предмет с этим точным ID не найден.

**2.8.8 / 2.8.14** — определение `Swords_B/items/clock_sword.json`.
- урон: `7`; максимальная прочность: `{"max_durability":4800}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: `{"category":"clock_sword","duration":30}`; левая рука: `false`; размер стопки: `1`; свечение: `true`; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:clock_sword"]` → `4800`; `["minecraft:clock"]` → `900`; `["minecraft:gold_block"]` → `780`; `["minecraft:gold_ingot"]` → `87`.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`; событие без нанесения урона существу → `{"event":"weapon"}`; удар по блоку → `{"event":"weapon"}`.
- При использовании предмета указано: `{"on_use":{"event":"on_use"}}`.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 2.8.14:**

- Рецепт `Swords_B/recipes/clock_sword.json`; тип `minecraft:recipe_shaped`.
  - Схема сверху вниз: `X##` / `#C#` / `I#X`.
  - Обозначения: `{"#":{"item":"minecraft:gold_block"},"C":{"item":"minecraft:clock"},"I":{"item":"minecraft:gold_ingot"}}`.
  - **В схеме есть символы без определения key: `["X"]`.** Их смысл и принятие рецепта движком не установлены.
  - Результат: `{"item":"effect:clock_sword"}`; рабочие станции/tags: `["crafting_table"]`.

- Определение: `Swords_B/items/clock_sword.json`.
- Результаты рецептов: `Swords_B/recipes/clock_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[34].Mainhand[0].Name

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Clock Sword (`effect:clock_sword`)

[Сравнение 1.6/2.x и глобальных эффектов](manual-spectral-time-comparison.md#clock-sword-и-time-sword-2x).

[Совместное влияние Clock и Time, условия остановки и глобальные конфликты](manual-time-interactions-2.8.md).

- `Swords_B/items/clock_sword.json:68–114`: damage 7, cooldown duration 30; все три weapon-хука запускают расход 1 прочности. `on_use` задаёт расход 10 и команду `event entity @s[family=clock_sword] clock_sword_skill_event`. При несоответствии family нельзя предполагать выполнение команды, но расход задан отдельно.
- `Swords_B/entities/player.json:35–45,1011–1024,1178–1215`: при подходящем состоянии событие добавляет `clock_sword_skill`, у которой timer `[5,5]`, looping true, randomInterval false и событие завершения `stop_clock_sword_event`; также family `[player,clock_sword,clock_sword_skill]`. При family `clock_sword_skill` в шаге `minecraft:clock_sword` добавляется movement value 1, затем команды: `gamerule randomtickspeed 100`, `effect @e[type=!player] speed 1 10 true`, `time add 10`, `event entity @a[family=default_player] clock_sword_movement`. Частота повторения зависит от работы сенсора движка; не делать вывод, что `time add 10` срабатывает ровно 100 раз.
- При условии family clock_sword `stop_clock_sword_event` удаляет группу `minecraft:clock_sword`, устанавливает **randomtickspeed 1**, выполняет `effect @e[type=!player] speed 0 0`, посылает событие default_player игрокам и добавляет default_player. Код не сохраняет и не восстанавливает предыдущее значение gamerule; это важный побочный эффект и риск многопользовательского режима. Проверить, как взаимодействуют оставшиеся группы и повторный таймер.
- Рецепт `Swords_B/recipes/clock_sword.json:8–23`: шаблон `X## / #C# / I#X`; ключи заданы для `#` (gold_block), C (clock), I (gold_ingot), но **X отсутствует**. Не исправлять автоматически по описанию — исходная фактическая работоспособность пока неизвестна.

**Дополнительный подробный разбор** (источник: `docs/manual-spectral-time-comparison.md`):

#### Clock Sword и Time Sword 2.x

`effect:clock_sword`: damage 7, durability 4800, offhand false, enchantable 9/sword, repair self 4800/clock 900/gold_block 780/gold_ingot 87, cooldown 30. Три weapon-хука → direct durability 1; on-use отдельно damage 10 и вызов `clock_sword_skill_event` только по `@s[family=clock_sword]`. Recipe `X##/#C#/I#X`: `#` = gold_block, C = clock, I = gold_ingot, но **X не определён** в key. Это исходная неоднозначность, не разрешение автоматически трактовать X как пустоту.

`effect:time_sword`: damage 13, durability 13770, offhand false, enchantable 9/sword, repairable не объявлен; все три weapon-хука выбирают direct durability 1/16/32/64 с весами 90/6/3/1. Математическое ожидание **3.46** относится только к этому вызову и стандартной нормализации, без штатного износа; не является расходом за секунду. Прямого локального рецепта этого результата нет. Отдельная фонтанная цепочка для тега выброшенного Clock Sword `wish_3` выбирает вес 975/25; в ветви 25 грузится структура Time Sword. Это 2.5% **на вызванный выбор** после 15 проверок блока, не шанс любого выброшенного Clock Sword.

Действие удержания Time задаёт randomtickspeed 300, `effect @e[type=!player] speed 1 15 true`, `time add 30` и событие ускорения для `@a[family=default_player]`; у Clock аналогичные 100, speed 1/10 и time add 10 записаны в отдельном шаге при family `clock_sword_skill`. Skill Clock использует таймер `[5,5]` looping; stop обоих мечей записывает фиксированный randomtickspeed **1**, speed 0 для non-player и default_player выбранным игрокам. Это не сохранение старого gamerule или эффектов. В player ни `clock_sword_skill`, ни `clock_sword_movement`, ни `time_sword_movement` явно не названы в `remove.component_groups`; это не доказательство вечного действия, поскольку разрешение конфликтов компонент и replacement групп неизвестно.

Селекторы 2.x не гарантируют область за пределами текущего измерения или права выполнения; `@a` не привязывается исключительно к владельцу. При нескольких игроках и конкуренции со сбросом результат зависит от порядка и частоты вызовов. [Подробные условия и сценарии](manual-time-interactions-2.8.md) отделяют статический текст от будущей проверки.

**Связанный подробный механизм** (источник: `docs/manual-time-interactions-2.8.md`):

### Clock Sword и Time Sword 2.x: конкуренция глобального состояния

Статический разбор файлов из `swordsandmoreswords-2-8-14.mcaddon`; соответствующие определения и команды, перечисленные ниже, проверены также в 2.8.8. Серверные испытания оригинала с одним игроком приведены ниже; эффекты на других игроков и мобов остаются отдельными вопросами. [Карточки Clock и Time](manual-traces-2.8.14.md) · [состояние анализа](analysis-status.md).

#### Входы, значения и цели

**Испытание оригинала 2.8.8 / Bedrock 1.20.50.03:** в отдельном мире отключили обычную смену дня и установили `randomtickspeed = 7`. Без меча время не менялось. С Time Sword в руке скорость случайных обновлений стала 300, игровое время ускорилось; после смены предмета скорость стала **1, не прежние 7**, а ускорение времени остановилось.

При удержании Clock Sword до применения значение оставалось 7; после применения ботом оно стало 100 и время ускорилось. Спустя несколько секунд способность прекратилась при всё ещё удерживаемом мече, а `randomtickspeed` стало 1. Износ меча при применении изменился с 0 до 10. Это наблюдения одного игрока на тестовом сервере, не проверка конфликтов нескольких игроков. [Журналы и сценарии](../data/original-mechanics-2026-11-07/README.md).

| Действие | Откуда вызывается | Глобальные команды и объекты |
|---|---|---|
| Удержание Clock | `player.json:1011–1015,1178–1196` проверяет в `hand` `effect:clock_sword`. При отсутствии family clock_sword первый шаг добавляет группу; **отдельный второй шаг** срабатывает при family clock_sword_skill. | В нём добавляется `clock_sword_movement`; `gamerule randomtickspeed 100`; `effect @e[type=!player] speed 1 10 true`; `time add 10`; `event entity @a[family=default_player] clock_sword_movement`. |
| Использование Clock | `items/clock_sword.json:68–76,103–114`: cooldown duration 30; задан durability damage 10 и команда `event entity @s[family=clock_sword] clock_sword_skill_event`. | `player.json:38–45,1208–1214`: событие добавляет `clock_sword_skill`, где family `[player,clock_sword,clock_sword_skill]` и looping timer `[5,5]`, randomInterval false, вызывает `stop_clock_sword_event` на self. `damage` и `run_command` — поля одного объекта, их очередность не предполагается. |
| Удержание Time | `player.json:894–896,1537–1545` проверяет в `hand` `effect:time_sword`; событие без дополнительного family-фильтра сначала добавляет `minecraft:time_sword`, затем выполняет команды. | `gamerule randomtickspeed 300`; `effect @e[type=!player] speed 1 15 true`; `time add 30`; `event entity @a[family=default_player] time_sword_movement`; два fill куба ±1 для `effect99:lightblock2`, сначала replace air, затем replace того же блока. |
| Остановка Clock | Таймер skill и отдельный sensor отсутствия Clock вызывают `stop_clock_sword_event`; его шаг требует self family `clock_sword` (`player.json:1018–1022,1198–1206`). | Удалить `minecraft:clock_sword`, выполнить `gamerule randomtickspeed 1`, `effect @e[type=!player] speed 0 0`, `event entity @a[family=default_player] default_player`, добавить `minecraft:default_player`. |
| Остановка Time | Sensor отсутствия Time вызывает `stop_time_sword_event`; его шаг требует self family `time_sword` (`player.json:899–903,1547–1555`). | Удалить `minecraft:time_sword`, добавить `minecraft:default_player`, выполнить те же три команды сброса (randomtickspeed 1, speed 0, default_player). |

`randomtickspeed` — gamerule, не записанная копия исходного значения; `time add` меняет время, и отдельной обратной команды в этих событиях нет. У `@e` нет радиуса и указан `type=!player`; нельзя из этого заключать, что целью являются игроки или все сущности во всех измерениях. `@a[family=default_player]` выбирает не только владельца: области действия селекторов и действия command permission зависят от движка/контекста. Фактическое действие `speed 0 0` и совместимость старой команды необходимо проверить; нельзя утверждать, что она точно восстанавливает доаддонные эффекты.

#### Что остаётся без явного удаления

В `Swords_B/entities/player.json` буквальные ссылки на `clock_sword_skill`, `clock_sword_movement`, `time_sword_movement` встречаются в определениях, добавлениях, фильтрах и командах, но **ни одна группа не перечислена в `remove.component_groups` этого файла**. Событие `default_player` лишь добавляет `minecraft:default_player`; его компоненты включают пустой `minecraft:timer`, movement 0.1 и family `[player,default_player]`. Группы Clock/Time movement задают movement 1.

Это не доказательство вечного ускорения или многократного срабатывания таймера: добавление `default_player` и других групп может переопределить те же компоненты, а правила порядка/замещения неизвестны. В частности, хотя timer `clock_sword_skill` записан looping, нельзя без опыта считать, что он гарантированно сохраняется после добавления другой группы. Семантику следует сравнить на исходной версии.

#### Сценарии конфликтов для проверки

1. В мире предварительно выставить отличное от 1 значение randomtickspeed, затем активировать и остановить каждый меч отдельно: зафиксировать точное значение до, во время и после, а также время и эффекты.
2. Игрок A удерживает Time, игрок B активирует и останавливает Clock; повторить в обратном порядке и при смене меча одним игроком. Обе остановки записывают 1, а активные команды записывают 100 или 300; какая запись окажется последней и как часто она повторится, заранее не известно.
3. Проверить игрока без меча с family default_player и с другим мечом; зафиксировать movement и принадлежность к группам до, во время и после действия. Внешние `@a` и наложение одноимённого компонента нельзя безопасно заменить локальным ускорением владельца без сравнения.
4. После одного использования Clock наблюдать минимум несколько таймерных интервалов, оставляя меч в руке и сменив его до окончания; записать условия stop, сохранение family и фактические вызовы. Не предполагать, что `duration 30` предмета и timer `[5,5]` имеют одну и ту же роль.
5. Наблюдать обычных мобов, помощников и предсуществующие speed-эффекты до и после остановки каждого меча. Проверить ограничения измерения, радиуса и совместимость синтаксиса, не принимая текст команды за гарантированное восстановление состояния.

### Что написано на скриншотах

На изображении вручную считаны: damage = `7`; durability = `4800`; enchantable = `true`; repairable = `true`. Оригинал: [скриншот 115837](https://drive.google.com/file/d/1eO2vurHVipmTvKj_7XzYz3KWOhZA23ic/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 08. Coal Sword — `effect:coal_sword`

**Кратко:** Помимо оружия, в 2.x задан как топливо. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

**1.6** — определение `Sword_B/items/coal_sword.json`.
- урон: `6`; максимальная прочность: `{"max_durability":121}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `true`; размер стопки: `1`; свечение: не указан; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:coal_sword"]` → `121`.
- Оружейный компонент не указан.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**2.8.8 / 2.8.14** — определение `Swords_B/items/coal_sword.json`.
- урон: `4`; максимальная прочность: `{"max_durability":121}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `false`; размер стопки: `1`; свечение: `false`; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:coal_sword"]` → `121`; `["minecraft:coal"]` → `58`; `["minecraft:stick"]` → `2`.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 1.6:**

- Рецепт `Sword_B/recipes/coal_sword.json`; тип `minecraft:recipe_shaped`.
  - Схема сверху вниз: `2` / `2` / `1`.
  - Обозначения: `{"2":{"item":"minecraft:coal_block"},"1":{"item":"minecraft:stick"}}`.
  - Результат: `{"item":"effect:coal_sword"}`; рабочие станции/tags: `["crafting_table"]`.

- Определение: `Sword_B/items/coal_sword.json`.
- Результаты рецептов: `Sword_B/recipes/coal_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

**Архив 2.8.14:**

- Рецепт `Swords_B/recipes/coal_sword.json`; тип `minecraft:recipe_shaped`.
  - Схема сверху вниз: `2` / `2` / `1`.
  - Обозначения: `{"2":{"item":"minecraft:coal_block"},"1":{"item":"minecraft:stick"}}`.
  - Результат: `{"item":"effect:coal_sword"}`; рабочие станции/tags: `["crafting_table"]`.

- Определение: `Swords_B/items/coal_sword.json`.
- Результаты рецептов: `Swords_B/recipes/coal_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - `Swords_B/loot_tables/chests/spawn_bonus_chest.json` $.pools[0].entries[0]: `{"type":"item","name":"effect:coal_sword","weight":1}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[19].Mainhand[0].Name

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

**Условная математическая модель выбора loot в 2.x:**

Числа ниже — вероятность выбрать хотя бы одну запись предмета внутри уже активированного пула, а не шанс реальной добычи. Допущения: все записи доступны; отсутствующий вес принят за 1; quality и условия записей игнорируются; выборы независимы с возвращением; число rolls равномерно в указанном диапазоне. Условия пула считаются уже выполненными. Загрузка таблицы, дополнительный отбор, количество предметов и функции не эмулируются.

- Таблица/пул: `chests/spawn_bonus_chest.json` / 0; entries: 0; rolls: `1`; вес ID/сумма: 1/5; выбор хотя бы одной записи по модели: **20.0000%**. Условия и оговорки: functions: не задано.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Coal Sword (`effect:coal_sword`)

[Полная сравнительная карточка 1.6/2.x](manual-basic-swords.md#coal-sword).

`items/coal_sword.json`: damage 4, durability 121, enchantability 9/sword, fuel duration **360.0**, repair self 121, `minecraft:coal` 58, `minecraft:stick` 2, web speed 15/bamboo 10; on_hurt_entity расходует 1. `recipes/coal_sword.json`: два `minecraft:coal_block` над палкой. `loot_tables/chests/spawn_bonus_chest.json`: пул 1 roll, sword weight 1, stone axe 1, wooden axe 3, доля 1/5 на выбор при стандартных весах; применение модифицированной таблицы bonus chest зависит от загрузки пакета.

**Старая версия 1.6** (источник: `docs/manual-traces-1.6.md`):

#### Coal Sword: 1.6 против 2.8.14

[Полная сравнительная карточка 1.6/2.x](manual-basic-swords.md#coal-sword).

- `Sword_B/items/coal_sword.json`: формат предмета 1.20.20, damage **6**, durability 121, enchantability 9/sword, allow_off_hand **true**, self repair 121, web speed 15 и bamboo 10; нет компонента fuel и явно заданных хуков weapon. В 2.8.14 damage 4, offhand false, есть fuel duration 360 и другие материалы ремонта. Это не косметическая разница; отсутствующие поля сами по себе не устанавливают движковые значения по умолчанию.
- `Sword_B/entities/player.json:204–214,520–533,925–931`: sensor по `effect:coal_sword` вызывает одноимённое событие, добавляющее группу со spawn_entity `entity:coal`, min/max wait 0, num 1, single_use true. Не предполагать число созданных объектов при повторных добавлениях группы без теста.
- `Sword_B/entities/coal.json`: family `despawnear`, `minecraft:despawn` с фильтром на эту family, health 1, collision 0×0, fire_immune true, physics и `controller.animation.coal`. Длительность жизни определяется движком, не установлена фиксированным числом в файле.
- `Sword_B/animation_controllers/coal_sword.json`: оба состояния default/coal переходят друг в друга по `1.0`, при входе каждое выполняет 13 отдельных команд `replaceitem block ... slot.container 1 coal` по соседним координатам и `scoreboard players set @a swords 2`. Если команды принимаются, они могут перезаписывать слот контейнера и менять глобальный счёт всех игроков; это не эквивалент компонента топлива у 2.8.14. Наличие контейнера, допустимость старого `replaceitem`, контекст координат и очередность с normalft требуют испытаний.

**Дополнительный подробный разбор** (источник: `docs/manual-basic-swords.md`):

#### Coal Sword

**Характеристики и получение.** `Sword_B/items/coal_sword.json` 1.6: damage 6, durability 121, ремонт только `effect:coal_sword` на 121, `minecraft:glint:false`; fuel в item не задан. В `Swords_B/items/coal_sword.json` 2.x damage 4, durability 121, `foil:false`, `minecraft:fuel.duration:360.0`, ремонт тем же мечом на 121, `minecraft:coal` на 58, `minecraft:stick` на 2. Число fuel оставлено в единицах исходного поля, не автоматически переведено в секунды. В трёх архивах одноимённый рецепт `recipes/coal_sword.json`: pattern `2/2/1`, ключ 2 = `minecraft:coal_block`, 1 = `minecraft:stick`, результат `effect:coal_sword`. В 2.x `loot_tables/chests/spawn_bonus_chest.json` имеет pool 0, rolls 1, три записи с суммой явно указанных весов 5, меч weight 1: 1/5 при стандартном взвешенном выборе **условно на активированный пул**. Это не гарантированный предмет в каждом бонусном сундуке.

**Удержание 1.6.** `entities/player.json:204–214,520–533,925–931` создаёт helper по вышеописанной цепочке. В `animation_controllers/coal_sword.json` каждый вход содержит 13 команд `replaceitem block <позиция> slot.container 1 coal`, затем запись общего score. Позиции относительно контекста команды в исходном порядке:

```
(-1,0,0) (1,0,0) (0,0,-1) (0,0,1) (0,-1,0)
(-1,1,0) (1,1,0) (0,1,-1) (0,1,1)
(-1,-1,0) (1,-1,0) (0,-1,-1) (0,-1,1)
```

Нет команды для `(0,1,0)` или `(0,0,0)`. Текст выбирает slot.container **1**, а не первый слот по естественному языку или проверенный тип печи; попытки могут затрагивать уже занятые контейнеры. Наличие блока/контейнера, возможность перезаписи и поддержка команды не установлены.

**2.x.** В базовом player sensor нет строгого одиночного hand-фильтра по `effect:coal_sword`, а в `player.json` нет буквального имени `coal_sword`. Это ограниченный поиск, а не доказательство отсутствия всех косвенных механизмов. Прежний controller с 13 `replaceitem` в 2.x локально не объявлен; предмет вместо этого содержит fuel и weapon выше. Не переносить helper 1.6 в новую версию автоматически.

### Что написано на скриншотах

На изображении вручную считаны: damage = `4`; durability = `121`; enchantable = `true`; repairable = `true`. Оригинал: [скриншот 115842](https://drive.google.com/file/d/117ulXVShaEZGyc0CdADa5mQUYlmAveAT/view). Оригинал: [скриншот 115849](https://drive.google.com/file/d/1YEOBZ0aW8jOnH1Uw26aexwJX-C9nx5Jq/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 09. Creeper Sword — `effect:creeper_sword`

**Кратко:** События со взрывами и призывом крипера. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

**1.6** — определение `Sword_B/items/creeper_sword.json`.
- урон: `8`; максимальная прочность: `{"max_durability":1500}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `true`; размер стопки: `1`; свечение: не указан; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:creeper_sword"]` → `1500`.
- Оружейный компонент не указан.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**2.8.8 / 2.8.14** — определение `Swords_B/items/creeper_sword.json`.
- урон: `6`; максимальная прочность: `{"max_durability":1500}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: `{"category":"creeper_sword","duration":3}`; левая рука: `false`; размер стопки: `1`; свечение: `false`; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:creeper_sword"]` → `1500`; `["minecraft:gunpowder"]` → `256`.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`; событие без нанесения урона существу → `{"event":"weapon"}`; удар по блоку → `{"event":"weapon"}`.
- При использовании предмета указано: `{"on_use":{"event":"on_use"}}`.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 1.6:**

- Рецепт `Sword_B/recipes/creeper_sword.json`; тип `minecraft:recipe_shaped`.
  - Схема сверху вниз: `F` / `F` / `E`.
  - Обозначения: `{"E":{"item":"minecraft:stick"},"F":{"item":"minecraft:skull","data":4}}`.
  - Результат: `{"item":"effect:creeper_sword"}`; рабочие станции/tags: `["crafting_table"]`.

- Определение: `Sword_B/items/creeper_sword.json`.
- Результаты рецептов: `Sword_B/recipes/creeper_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

**Архив 2.8.14:**

- Рецептов с этим точным результатом локально не найдено. Это не исключает других путей.

- Определение: `Swords_B/items/creeper_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[17].Mainhand[0].Name
  - `Swords_B/structures/creeper_sword.mcstructure` $.entities[0].Item.Name

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Creeper Sword (`effect:creeper_sword`)

[Подробная цепь крипера, conditional 95/5 и отличие stop-групп](manual-creeper-sword.md).

- `items/creeper_sword.json`: damage 6, durability 1500, enchantability 9/sword, cooldown 3, repair self 1500/gunpowder 256, web 15/bamboo 10. Все три weapon-хука: durability 1, затем 20/100 shoot `minecraft:creeper` power 1 или 80/100 ещё 1 durability. On-use вызывает `start_player_explode_event` target holder, затем durability 1.
- `player.json:337–342,2108–2116`: событие добавляет movement 0 и looping timer `[1.5,1.5]`, запускает анимацию и fuse sound; таймер вызывает `start_player_explode`, который снимает группу, добавляет default_player, `summon entity:instant_creeper_explode ~ ~1 ~` и `kill @s`. Сущность `instant_creeper_explode.json`: fuse 0, power 4, fire false, griefing true. Исполнение kill и повторного использования зависит от движка, а не гарантировано одной декларацией.
- `entities/creeper.json` **не разбирается JSON5** в обоих 2.8.x: парсер останавливается на последней `}` (строка 430), и удаление этой одной скобки только в памяти позволяет разобрать текст. Это диагностика, не исправление архива и не свидетельство принятия исходника движком; ниже — буквальное чтение исходника. При spawn и `other` с мечом описаны группы mini: scale 0.3, timer 10, family `[creeper,player,mob,effect99_entities]`, цель monster max_dist 16; при дистанции 2.5 или повреждении кроме void — start_minicreeper_exploding. Группа взрыва fuse 1.5, power 1, fire false; projectile on-hit убирает группу projectile, impact 1, power 1/gravity 0.02. Реальность этих путей требует проверки загрузчика, в особенности с другим/исправленным парсером.
- Там же forced charged exploding задан timer 1.4 и взрыв fuse 1.5/power 6; таймер вызывает выбор 95 пусто/5 структура `creeper_sword`. `minecraft:start_exploding_forced` выбирает forced charged только при наличии `minecraft:is_charged`; интерактивное зажигание и валидность синтаксиса дополнительно проверять. 5/100 — условная ветвь, не вероятность от любого крипера.

**Старая версия 1.6** (источник: `docs/manual-traces-1.6.md`):

#### Creeper Sword и TNT Sword: 1.6

[Массовые цели Ender/Wither/Creeper/TNT и матрица типов](manual-area-targets-1.6.md).

- `items/creeper_sword.json`: damage 8, durability 1500, enchantability 9, self repair 1500, offhand true; явного on-use/cooldown и weapon-event в определении нет. Sensor → `entity:creeper` → `controller.animation.creeper`. Оба состояния создают objective c, прибавляют 1 всем сущностям r=16, при `@p[c=90]` воспроизводят звук; 27 отдельных селекторов перечисленных типов с точным `c=100` и r=16 призывают `entity:explode`, при score ближайшего игрока c=300 удаляется objective, затем `@a swords 2`. Типы включают tnt и wither, но не все сущности; точный список и порядок — в [реестре](animation-ledger-1.6.md). Это не мини-криперы по вероятности 20/100 из 2.8.14.
- `items/tnt_sword.json`: damage 7, durability **1**, self repair 1, offhand true, enchantable не указан. Sensor → `entity:tnt_sword` → `controller.animation.tnt`; каждый вход обоих состояний содержит 26 команд summon `entity:explode` в точках указанных типов в кольце `rm=10,r=15`, потом устанавливает `swords=2` всем игрокам. Командой не проверяется использование предмета. `entities/explode.json`: `minecraft:explode` с legacy-ключами `fuseLength:0`, `fuseLit:true`, power 4, `causesFire:false`, destroy_affected_by_griefing true; это отдельный формат от `entity:tnt` и `minecraft:tnt` 2.8.14. Работоспособность camelCase, частота state transitions, радиусы и конфликт scoreboard нужно проверить.

**Дополнительный подробный разбор** (источник: `docs/manual-creeper-sword.md`):

### Creeper Sword: предмет, мини-крипер и получение

Статический разбор `effect:creeper_sword`, соответствующего player-event, `minecraft:creeper` и структуры. Рассматриваемые item, creeper entity, instant explode entity, loot creeper и структура **побайтово одинаковы** в архивах 2.8.8 и 2.8.14; используемые группы и события player структурно одинаковы, хотя весь `player.json` между версиями различается. Для 1.6 см. [отдельную старую цепочку и сравнение](manual-traces-1.6.md#creeper-sword-и-tnt-sword-16) и [массовые цели 1.6](manual-area-targets-1.6.md#creeper-и-tnt-разные-выборки-для-одной-сущности-взрыва). Игровых испытаний не было.

**Оговорка для основной сущности:** исходный `Swords_B/entities/creeper.json` не разбирается JSON5: неожиданная последняя `}` на строке 430. Если убрать именно эту скобку только в памяти, оставшийся текст разбирается; ниже приводится эта диагностическая интерпретация вместе с буквальными строками. Это не изменение архива, не единственно возможное исправление и не доказательство, что исходный Bedrock загрузит файл. Автоматические [индексы групп](entity-groups-2.x.md) и [randomize](randomize-index.md) исключают этот повреждённый файл; в нём дополнительно есть описанная ниже ветвь 95/5.

#### Сопоставление с образцами: только диагностическая копия в памяти

[Полная сравнительная выписка](vanilla-creeper-diagnostic-ledger.md) и [машинные данные](../data/vanilla-creeper-diagnostic.json) показывают различия гипотетического результата удаления последней `}` с двумя официальными образцами Mojang. Их идентичные `creeper.json` имеют SHA-256 `6f8a46400a440580a9f450404476c17132e448f010cc7c81c9dd9984ffab8bce`; оригинальный повреждённый файл обеих 2.x — `8c8f169be60ee52a224928d57575cb3b47f19bf41c03e8dd5326f8440d6c33c2`. Источники и ограничения образцов — в [сравнении](manual-vanilla-override-review.md). Это отдельно от 22 безошибочно разобранных файлов, **не** подтверждение единственного исправления или загрузки игры.

В варианте разбора из двух образцов base `minecraft:despawn` присутствует, а в гипотетическом add-on объекте отсутствует; `must_see_forget_duration` в `minecraft:behavior.nearest_attackable_target` — **3.0** в образцах и **0.0** в варианте аддона; в forced charged группе образцов нет таймера, описанного далее. Вариант аддона дополнительно содержит `minecraft:minicreeper`, projectile, exploding и соответствующие события. Наличие и отсутствие полей не доказывает работу, default или порядок групп.

После скачивания двух ZIP по ссылкам выше сравнение воспроизводится без изменения источника:

```sh
python tools/build_creeper_diagnostic_diff.py \
  --reference-119 /путь/bedrock-samples-v1.19.40.2.zip \
  --reference-120 /путь/bedrock-samples-v1.20.30.1.zip
```

#### Предмет и две разные цепочки

- `items/creeper_sword.json:8–78`: damage 6, durability 1500, max stack 1, offhand false, enchantable 9/sword; ремонт самим предметом на 1500 либо `minecraft:gunpowder` на 256, web 15 и bamboo 10; cooldown `{category:"creeper_sword",duration:3}`. Значения компонентов приведены буквально; их исполнение и единицы в целевой версии требуют проверки.
- `:100–128`: все три заявленных weapon-hook указывают на одно событие. В `sequence` сначала `damage` durability 1 target self, затем выбор веса 20 — `shoot` projectile `minecraft:creeper`, launch_power 1; веса 80 — ещё `damage` durability 1 target self. При стандартном взвешенном выборе и полном прохождении sequence это **20% выбора shoot на вызов**, а суммы прямого damage 1/2 имеют доли 20%/80%, среднее 1.8. Это не шанс успешного рождения мини-крипера и не фактический расход предмета: количество хуков, прерывание, стандартный износ и интерпретация target требуют проверки. Подробнее [модель weapon](manual-weapon-durability-model.md).
- `:81–98`: другой, on-use event содержит `sequence`: команда `event entity @s start_player_explode_event` с target `holder`, затем `damage` durability 1 target self. Это **не** тот же 20/80 randomize. Отсутствие выбранной/рабочей цели или прерывание может влиять на реальный результат; свойства target нельзя выводить из имени.

#### Самовзрыв игрока

`entities/player.json:337–342,2108–2116`: `start_player_explode_event` добавляет одноимённую группу movement value 0 и looping timer `[1.5,1.5]` → `start_player_explode`, а рядом содержит run_command с `playanimation @s animation.player.explode`, `playsound random.fuse`. Порядок выполнения **соседних полей** add и run_command не задан только порядком их записи.

Событие таймера содержит соседние remove этой группы, add `minecraft:default_player` и список команд `summon entity:instant_creeper_explode ~ ~1 ~`, затем `kill @s`. Список команд в исходнике именно в этом порядке, но успешность, порядок относительно соседних add/remove и контекст `@s` нужно испытать. Нельзя обещать убийство игрока, взрыв или точное время по одному объявлению; повторный вызов при looping timer и наложение движения/default также зависят от движка.

`entities/instant_creeper_explode.json:1–12` — **отдельная** `entity:instant_creeper_explode`, не мини-крипер и не `minecraft:creeper`: summonable true, spawnable false, family `[effect99_entities]`, collision 0×0, damage sensor cause all/deals_damage false, `minecraft:explode` fuse_length 0, fuse_lit true, power 4, causes_fire false, destroy_affected_by_griefing true. Фактическое разрушение зависит от игры и правил мира.

#### Мини-крипер: условия и переключение компонентов

В гипотетически разобранном `entities/creeper.json:10–86,321–330` событие `minecraft:entity_spawned` содержит один sequence-шаг с фильтром `has_equipment`, subject `other`, domain `hand`, value `effect:creeper_sword`; он добавляет **обе** группы `minecraft:minicreeper` и `minecraft:minicreeper_projectile`. Важная неопределённость — кто именно разрешается как `other` при данном spawn/shoot; простое объявление projectile в item не доказывает прохождение этого фильтра. Отдельное событие `minecraft:minicreeper` добавляет только первую группу; не считать эти два пути одинаковыми.

Если соответствующие группы реально применены:

- Mini: scale 0.3; family `[creeper,player,mob,effect99_entities]` вместо базового `[creeper,monster,mob]`; nearest-attackable-target имеет priority 1, family `monster`, max_dist 16, must_see true; timer `[10,10]`, looping true, `randomInterval:false` вызывает `start_minicreeper_exploding`; sensor внутри 2.5 и damage-событие `has_damage != void` также вызывают его. Наследование и конфликт с базовыми компонентами — предмет проверки, не доказанное замещение во всех условиях.
- Projectile: power 1, gravity 0.02, inertia 1/liquid_inertia 1, impact_damage 1 и knockback true; on-hit вызывает definition event `minecraft:stop_projectile`, target self, affect_projectile true. Это событие удаляет projectile-группу, а не прямо выполняет kill/remove-on-hit. Взрыв mini — другая группа и другой event.
- `start_minicreeper_exploding` добавляет группу с damage sensor cause all/deals_damage false и explode fuse 1.5, power 1, causes_fire false, destroy_affected_by_griefing true. Не следует автоматически предполагать, что цель, timer и damage срабатывают или что их действия суммируются.

#### Обычный и заряженный крипер: важное различие stop

В том же файле базовые components объявляют health 20/20, collision 0.6×1.8, movement 0.2, attack damage 3, ближайшую цель family player/max_dist 16 и loot `loot_tables/entities/creeper.json`. Target-nearby sensor с inside 2.5, outside 6, must_see true вызывает start/stop; on-target-escape также указывает stop. Damage sensor с `other` family lightning вызывает `minecraft:become_charged` и содержит `deals_damage:false` — конкретная применимость trigger и фактический урон молнии зависят от семантики компонента.

`minecraft:start_exploding` выбирает разные sequence-шаги по фильтру отсутствия/наличия `minecraft:is_charged`: обычная группа fuse 1.5/power 3 или заряженная fuse 1.5/power 6. `minecraft:become_charged` рядом объявляет remove `minecraft:exploding` и add `minecraft:charged_creeper` с `minecraft:is_charged`. **`minecraft:stop_exploding` удаляет только `minecraft:exploding`**, а не `minecraft:charged_exploding`, `minecraft:forced_exploding`, `minecraft:forced_charged_exploding` или `minecraft:minicreeper_exploding`. Локально в этом файле явного remove этих четырёх групп нет. Это наблюдение о тексте, а не доказательство, что они остаются активны или что взрыв нельзя отменить: может действовать движок, внешний event или иное разрешение компонентов.

`minecraft:start_exploding_forced` аналогично выбирает forced ordinary power 3 или forced charged power 6. Interact требует other family player, `flint_and_steel` в hand и отсутствующий `minecraft:explode`, вызывает forced-событие; содержит hurt_item 1, swing true и звук `ignite`. Forced-группы задают пустые target-nearby-sensor и on-target-escape; не трактовать пустые объекты как гарантированное отключение сенсора на любой версии.

#### Путь структуры и не равный ему обычный loot

Только в группе `minecraft:forced_charged_exploding` есть одноразовый timer `[1.4,1.4]` → event `creeper_sword`, рядом explode fuse_length 1.5. По этому событию randomize задаёт weight 95 пусто и 5 команду `structure load creeper_sword ~ ~ ~` (`:123–135,332–341`). При стандартном выборе доля **5/100 условно на вызов event**; разница 1.4 и 1.5 сама по себе не доказывает, что timer гарантированно опередит взрыв или что структура загрузится. Зажигание, заряд, существование сущности, обработка файла, ветвь и команда — отдельные условия.

Файл `Swords_B/structures/creeper_sword.mcstructure` присутствует; [полный NBT](structures-2.8.14.md#creeper_sword) показывает размер `[1,1,1]` и одну item-сущность: `Item.Name:effect:creeper_sword`, `Count:1`, `Damage:0`, `Age:159`. Это сохранённое состояние, а не доказательство успешного получения. Синтаксис и положение при `structure load` нужно проверить.

Привязанная таблица `loot_tables/entities/creeper.json` **не содержит меч**: первый пул — gunpowder, weight 1, set_count 0…2 и looting_enchant 0…1; ещё два отдельных пула с условиями `killed_by_entity` `minecraft:skeleton` и `minecraft:stray` содержат по 12 записей пластинок и один roll. Срабатывание этих условий и результат функций не определяются нашей условной арифметикой. Структурный путь 95/5 нельзя складывать с обычным loot или называть шансом с каждого крипера.

#### Что проверить в игре перед переносом

1. Загрузчик исходного файла с лишней `}`; отдельные пробы оригинала и диагностической исправленной копии, без подмены источника.
2. Контекст `other` при `shoot minecraft:creeper` и при обычном spawn, применение mini/projectile-групп и реальное столкновение.
3. Заряжение, зажигание, stop/escape, конфликт групп и таймер 1.4 против fuse 1.5; возможность загрузки структуры и её содержимое.
4. Самовзрыв holder, порядок событий/команд, воздействие на нескольких игроков и блоки, а также gamerule и существование игрока после `kill`.

### Что написано на скриншотах

На изображении вручную считаны: damage = `6`; durability = `1500`; enchantable = `true`; repairable = `true`. Оригинал: [скриншот 115910](https://drive.google.com/file/d/1rCL9RKVJCIfjHme7CkmOEe82NpJyCn1A/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 10. Cursed Pumpkin Sword — `effect:cursed_pumpkin_sword`

**Кратко:** Тыквенный снаряд; получение связано со скриптом при ломании тыкв. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

- В 1.6 предмет с этим точным ID не найден.

**2.8.8 / 2.8.14** — определение `Swords_B/items/pumpkin_sword.json`.
- урон: `5`; максимальная прочность: `{"max_durability":606}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `false`; размер стопки: `1`; свечение: `false`; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:cursed_pumpkin_sword"]` → `606`; `["minecraft:honey_block"]` → `400`; `["minecraft:honeycomb"]` → `150`.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`; событие без нанесения урона существу → `{"event":"weapon"}`; удар по блоку → `{"event":"weapon"}`.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 2.8.14:**

- Рецептов с этим точным результатом локально не найдено. Это не исключает других путей.

- Определение: `Swords_B/items/pumpkin_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - `Swords_B/loot_tables/pumpkin_sword.json` $.pools[0].entries[0]: `{"type":"item","name":"effect:cursed_pumpkin_sword","weight":1}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

**Условная математическая модель выбора loot в 2.x:**

Числа ниже — вероятность выбрать хотя бы одну запись предмета внутри уже активированного пула, а не шанс реальной добычи. Допущения: все записи доступны; отсутствующий вес принят за 1; quality и условия записей игнорируются; выборы независимы с возвращением; число rolls равномерно в указанном диапазоне. Условия пула считаются уже выполненными. Загрузка таблицы, дополнительный отбор, количество предметов и функции не эмулируются.

- Таблица/пул: `pumpkin_sword.json` / 0; entries: 0; rolls: `1`; вес ID/сумма: 1/1; выбор хотя бы одной записи по модели: **100.0000%**. Условия и оговорки: functions: не задано.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Cursed Pumpkin Sword (`effect:cursed_pumpkin_sword`)

[Точная последовательность скрипта, версия API и проверка на фиктивных событиях](manual-pumpkin-script-2.8.md).

- `items/pumpkin_sword.json`: damage 5, durability 606, enchantability 9/sword, offhand false, repair self 606/**honey_block 400/honeycomb 150** — буквальные ингредиенты в файле, даже если кажутся скопированными от пчелиного меча. Все три weapon-хука задают durability 1 и randomize 80/100 `shoot entity:pumpkin_projectile` power 1 / 20/100 пусто.
- `entities/pumpkin_projectile.json`: runtime snowball, collision 0.625×0.625, family effect99_entities/projectile, projectile impact damage 1/knockback true/should_bounce true, remove_on_hit, particle largeexplode, power 0.3, gravity 0.002, homing false, uncertainty_base 16/multiplier 4; looping timer time `[12,15]` вызывает despawn, `randomInterval` явно не указан. Не выводить распределение интервала по умолчанию без теста.
- `scripts/javascript.js`: afterEvents.playerBreakBlock, id **содержит** `pumpkin` и не содержит `stem`, `Math.floor(Math.random()*1000+1)<=5`, и у игрока отсутствует tag `pumpkin_sword`; tag добавляется **до** запуска старой `execute ... loot spawn` из позиции блока. При обычном равномерном генераторе проверка 5/1000 на подходящий вызов, не вероятность успешной выдачи; после добавления тега даже ошибка команды может блокировать дальнейшие попытки. Текстовый поиск по всем оригинальным файлам 2.8.14 обнаружил назначение и проверку этого тега в скрипте, но не команду снятия — это не доказательство невозможности снятия внешними средствами. `loot_tables/pumpkin_sword.json`: 1 roll, один item с weight 1. Манифест требует `@minecraft/server` `1.12.0-beta`; совместимость API, разрешение старого синтаксиса и свойства break event нужно тестировать на конкретных версиях.

**Дополнительный подробный разбор** (источник: `docs/manual-pumpkin-script-2.8.md`):

### 2.x: Cursed Pumpkin Sword — скриптовое получение и проверка логики

Исходники: `Swords_B/scripts/javascript.js`, `manifest.json`, `loot_tables/pumpkin_sword.json`, `items/pumpkin_sword.json`, `entities/pumpkin_projectile.json`. Событие Minecraft, разрешение скриптов, конкретная версия API, выдача и команды в игре **не проверены**. [Карточка предмета](manual-traces-2.8.14.md#cursed-pumpkin-sword-effectcursed_pumpkin_sword) · [loot-контекст](loot-context.md).

#### Что выполняет скрипт

1. Импортирует `world` из `@minecraft/server`, подписывается на `world.afterEvents.playerBreakBlock`. Другая причина разрушения блока этим фрагментом напрямую не подписана; фактический состав событий определяется API.
2. Проверяет, что `f.brokenBlockPermutation.type.id.includes('pumpkin')` и **не** `.includes('stem')`. Это регистрозависимый поиск подстроки, а не перечень ванильных ID или проверка пространства имён: синтетический `test:glowing_pumpkin` подходит; `test:pumpkin_stem` — нет. Фактическое существование и регистрации любых тестовых блоков не предполагается.
3. Берёт `{x,y,z}` из `f.block.location`. Затем вычисляет `Math.floor(Math.random() * 1000 + 1) <= 5` **раньше**, чем `!f.player.hasTag('pumpkin_sword')`, поскольку используется короткое замыкание `&&`. Когда случайная проверка не проходит, `hasTag` этой строкой не вызывается; если тег уже есть, но блок подходит, random всё равно вычисляется.
4. При прохождении обеих проверок вызывает `f.player.addTag('pumpkin_sword')`, а затем ``f.player.runCommand(`execute @s ~ ~ ~ loot spawn ${x} ${y} ${z} loot pumpkin_sword`)``. Код не проверяет результат добавления тега или команды и не содержит обработчик исключения.
5. `loot_tables/pumpkin_sword.json` определяет один pool `rolls:1`, единственную item-запись `effect:cursed_pumpkin_sword` weight 1, **без явно заданного set_count**. Нельзя по одному этому полю гарантировать конкретный размер или успешное появление: разрешение имени таблицы, синтаксис `execute`, доступность команды и регистрация loot требуют проверки в игре.

В обоих архивах текстовый поиск нашёл `hasTag` и `addTag` именно в этом скрипте; буквальной команды снятия тега `pumpkin_sword` в просмотренных JSON/JS/mcfunction не обнаружено. Это не доказательство, что внешние команды/другие пакеты не могут снять тег, что он сохраняется после смерти или перезахода, либо что `addTag` успешно выполнен. Если тег добавлен, а `runCommand` затем не выполнится, не вернёт успешный результат или выбросит исключение, код сам не откатывает тег; при сохранении тега последующие проверки уже не выполнят команду даже после новой успешной случайной проверки.

#### Математическая модель, не гарантия получения

Если считать `Math.random` независимым равномерным на `[0,1)` и вычисления идеальными, тест имеет долю **5/1000 = 0.5%** на каждый подходящий вызов. Дополнительно игрок должен не иметь тег; тест скрипта, успешное добавление тега, исполнение старой команды и получение предмета — разные события. Дальнейшие числа относятся только к *первому прохождению случайной проверки* среди n независимых подходящих событий при отсутствии иных изменений тега:

| n | `1 − (0.995)^n` |
|---:|---:|
| 1 | 0.5000% |
| 10 | 4.8890% |
| 100 | 39.4230% |
| 139 | 50.1795% |
| 200 | 63.3042% |
| 1000 | 99.3346% |

Математическое ожидание количества таких попыток до первой успешной проверки — 200, медиана — 139; это не обещание, что игрок получит меч за указанный срок/число блоков. Дискретность фактического генератора JS и состояние окружения не исследованы.

#### Сопоставление версий и имитация

В 2.8.8 и 2.8.14 скрипты отличаются **одним пробелом в конце строки** условия; после удаления только пробелов в концах строк совпадают. Предмет, снаряд и loot-таблица побайтово идентичны, но manifest задаёт разные строки версии `@minecraft/server`: `1.8.0-beta` для файла 2.8.8 и `1.12.0-beta` для файла 2.8.14. В обоих указан script module `scripts/javascript.js`, min_engine_version `[1,19,40]`; из этого не следует совместимость с целевым Bedrock 26.62.

В `tools/test_pumpkin_script.cjs` оригинальный текст **из ZIP** исполняется Node.js в `vm` с подставленными объектами world/player, заранее заданным Math.random и имитируемой командой; только исходная строка import удаляется в памяти, сами архивы не меняются. Для обеих версий проверены: подходящее имя, граница 0.004999/0.005, исключение stem, посторонний блок, существующий tag, порядок addTag→runCommand, исключение команды после присвоения тега и следующая попытка. Это проверка ветвления JavaScript на фиктивных интерфейсах, **не** запуск Minecraft или проверка API/команд/сохранения тегов. Тест пропускается, если Node.js не установлен.

### Что написано на скриншотах

Сопоставленной карточки чисел на скриншотах нет; это не значит, что предмет нигде на изображениях не упомянут.

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 11. Emerald Sword — `effect:emerald_sword`

**Кратко:** Эффекты при условиях деревни; торговля отличается между версиями. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

**1.6** — определение `Sword_B/items/emerald_sword.json`.
- урон: `7`; максимальная прочность: `{"max_durability":2300}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `true`; размер стопки: `1`; свечение: не указан; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:emerald_sword"]` → `2300`.
- Оружейный компонент не указан.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**2.8.8 / 2.8.14** — определение `Swords_B/items/emerald_sword.json`.
- урон: `7`; максимальная прочность: `{"max_durability":2300}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `false`; размер стопки: `1`; свечение: `false`; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:emerald_sword"]` → `2300`.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`; событие без нанесения урона существу → `{"event":"weapon"}`; удар по блоку → `{"event":"weapon"}`.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 1.6:**

- Рецепт `Sword_B/recipes/emerald sword.json`; тип `minecraft:recipe_shaped`.
  - Схема сверху вниз: `F` / `F` / `E`.
  - Обозначения: `{"E":{"item":"minecraft:stick"},"F":{"item":"minecraft:emerald_block"}}`.
  - Результат: `{"item":"effect:emerald_sword"}`; рабочие станции/tags: `["crafting_table"]`.

- Определение: `Sword_B/items/emerald_sword.json`.
- Результаты рецептов: `Sword_B/recipes/emerald sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

**Архив 2.8.14:**

- Рецептов с этим точным результатом локально не найдено. Это не исключает других путей.

- Определение: `Swords_B/items/emerald_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - `Swords_B/loot_tables/chests/pillager_outpost.json` $.pools[3].entries[5]: `{"type":"item","weight":3,"functions":[{"function":"set_count","count":{"min":0,"max":1}}],"name":"effect:emerald_sword"}`
  - `Swords_B/loot_tables/chests/stronghold_corridor.json` $.pools[0].entries[16]: `{"type":"item","name":"effect:emerald_sword","weight":5}`
  - `Swords_B/loot_tables/chests/woodland_mansion.json` $.pools[0].entries[9]: `{"type":"item","name":"effect:emerald_sword","weight":25}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[14].Mainhand[0].Name

**Отличающиеся записи архива 2.8.8:**

- Рецептов с этим точным результатом локально не найдено. Это не исключает других путей.

- Определение: `Swords_B/items/emerald_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - `Swords_B/loot_tables/chests/pillager_outpost.json` $.pools[3].entries[5]: `{"type":"item","weight":3,"functions":[{"function":"set_count","count":{"min":0,"max":1}}],"name":"effect:emerald_sword"}`
  - `Swords_B/loot_tables/chests/stronghold_corridor.json` $.pools[0].entries[16]: `{"type":"item","name":"effect:emerald_sword","weight":5}`
  - `Swords_B/loot_tables/chests/woodland_mansion.json` $.pools[0].entries[9]: `{"type":"item","name":"effect:emerald_sword","weight":25}`
- Сделки локальных таблиц (поле `gives`):
  - `Swords_B/trading/economy_trades/weapon_smith_trades.json` $.tiers[4].groups[1].trades[0]: `{"wants":[{"item":"minecraft:emerald_block","quantity":32,"price_multiplier":0}],"gives":[{"item":"effect:emerald_sword","quantity":1,"functions":[{"function":"enchant_with_levels","treasure":false,"levels":{"min":5,"max":60}}]}],"trader_exp":0,"max_uses":2,"reward_exp":true}`
  - `Swords_B/trading/weapon_smith_trades.json` $.tiers[2].trades[3]: `{"wants":[{"item":"minecraft:emerald_block","quantity":{"min":24,"max":32}}],"gives":[{"item":"effect:emerald_sword","functions":[{"function":"enchant_with_levels","treasure":false,"levels":{"min":5,"max":60}}]}]}`
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[14].Mainhand[0].Name

**Условная математическая модель выбора loot в 2.x:**

Числа ниже — вероятность выбрать хотя бы одну запись предмета внутри уже активированного пула, а не шанс реальной добычи. Допущения: все записи доступны; отсутствующий вес принят за 1; quality и условия записей игнорируются; выборы независимы с возвращением; число rolls равномерно в указанном диапазоне. Условия пула считаются уже выполненными. Загрузка таблицы, дополнительный отбор, количество предметов и функции не эмулируются.

- Таблица/пул: `chests/pillager_outpost.json` / 3; entries: 5; rolls: `{"min":2,"max":3}`; вес ID/сумма: 3/28; выбор хотя бы одной записи по модели: **24.5513%**. Условия и оговорки: 1 отсутствующих weight → 1 в модели; functions: `[{"function":"set_count","count":{"min":0,"max":1}}]`.
- Таблица/пул: `chests/stronghold_corridor.json` / 0; entries: 16; rolls: `{"min":2,"max":3}`; вес ID/сумма: 5/521; выбор хотя бы одной записи по модели: **2.3809%**. Условия и оговорки: functions: не задано.
- Таблица/пул: `chests/woodland_mansion.json` / 0; entries: 9; rolls: `{"min":1,"max":3}`; вес ID/сумма: 25/670; выбор хотя бы одной записи по модели: **7.2788%**. Условия и оговорки: functions: не задано.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Emerald Sword (`effect:emerald_sword`)

[Полная сравнительная карточка 1.6/2.x](manual-basic-swords.md#emerald-sword).

- `items/emerald_sword.json`: damage 7, durability 2300, enchantability 9/sword; ремонт только таким же мечом на 2300; на все три weapon-хука расход 1. Web speed 15, bamboo 10, offhand false.
- `player.json:334–336,684–693,2086–2107`: сенсор `hand` вызывает группу family `[player,emerald_sword]`. Отдельный шаг в `minecraft:emerald_sword` проверяет `is_in_village=true`, после чего выполняет `effect @s village_hero 1 0 true` и `effect @e[family=villager,r=64] resistance 1 1 true`. Это командные параметры, а не доказанная частота обновления и не обещание охватить только живых жителей. При снятии есть `effect @s village_hero 0 0 true`, удаление группы и default_player; отдельной команды снятия resistance с жителей нет.
- В `loot_tables/chests/stronghold_corridor.json` пул 2–3 rolls, вес меча 5 из суммы явно заданных 521 (5/521 на выбор); в `woodland_mansion.json` пул 1–3, вес 25 из 670 (25/670 на выбор). В `pillager_outpost.json` пул 2–3 rolls, вес 3, `set_count` 0…1, и у другого элемента вес не задан: не вычислять точную долю без проверки значения по умолчанию и обработки set_count. Все три — не вероятность «на сундук»; реальная привязка таблиц к генерации проверяется отдельно.

**Старая версия 1.6** (источник: `docs/manual-traces-1.6.md`):

#### Emerald Sword: 1.6 против 2.8.14

[Полная сравнительная карточка 1.6/2.x](manual-basic-swords.md#emerald-sword).

`items/emerald_sword.json`: damage 7, durability 2300, enchantable 9, self repair 2300, offhand true. Sensor → группа → `entity:emerald` → `controller.animation.emerald`: при входе в оба состояния команды `/effect @p village_hero 16 0 true` и `/scoreboard players set @a swords 2`, без явной проверки деревни и без команд resistance для жителей. В 2.8.14, напротив, `is_in_village` является фильтром и effect для жителей имеет r=64. `@p` в контроллере 1.6 — ближайший к исполняющей сущности игрок, не заведомо владелец меча.

**Дополнительный подробный разбор** (источник: `docs/manual-basic-swords.md`):

#### Emerald Sword

**Характеристики/получение.** Damage 7, durability 2300 и self repair 2300 во всех трёх архивах. В 1.6 есть рецепт `recipes/emerald sword.json`: `F/F/E`, F = `minecraft:emerald_block`, E = `minecraft:stick`. В локальных recipes обоих 2.x такой результат буквально не найден. В 2.x меч есть в chest loot: stronghold corridor pool 0, rolls 2–3, weight 5 из суммы 521; woodland mansion pool 0, rolls 1–3, weight 25 из 670. В pillager outpost pool 3, rolls 2–3, weight 3 и `set_count` 0–1, но другой элемент этого пула не имеет явно указанного weight: без интерпретации его default точную долю не заявляем. Эти доли — на выбор записи, не на целый сундук.

Только 2.8.8 содержит два файла торговли оружейника: один вариант хочет 32 emerald_block, выдаёт меч с `enchant_with_levels` 5–60 и `max_uses:2`; другой задаёт цену 24–32 блока и ту же функцию зачарования. В 2.8.14 оба файла отсутствуют. Точный контекст tier и неопределённость регистрации — [версионный разбор](manual-version-2.8.8.md#emerald-sword-два-объявления-торговли-только-в-288).

**Удержание.** В 1.6 helper-контроллер без проверки деревни выполняет `/effect @p village_hero 16 0 true` и `@a swords 2` в каждом из двух одинаковых on_entry. В 2.x `player.json` имеет отдельную группу family `[player,emerald_sword]`: первая ветвь при family != emerald_sword добавляет группу, а **следующий отдельный шаг** при `is_in_village:true` выполняет `effect @s village_hero 1 0 true` и `effect @e[family=villager,r=64] resistance 1 1 true`. В stop при соответствующей family выполняется `effect @s village_hero 0 0 true`, удаляется группа и добавляется default_player; отдельного снятия resistance у жителей в этом событии нет. Частоту вызова sensor, значения эффекта и результат при конфликтующих группах текст не доказывает.

### Что написано на скриншотах

На изображении вручную считаны: damage = `7`; durability = `2300`; enchantable = `true`; repairable = `true`. Оригинал: [скриншот 115853](https://drive.google.com/file/d/1g4UIpjMFNG1uYe8hAo8IOzVw5ctqxL-i/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 12. Ender Sword — `effect:ender_sword`

**Кратко:** При использовании задано случайное перемещение игрока. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

**1.6** — определение `Sword_B/items/ender_sword.json`.
- урон: `9`; максимальная прочность: `{"max_durability":1256}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `true`; размер стопки: `1`; свечение: не указан; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:ender_sword"]` → `1256`.
- Оружейный компонент не указан.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**2.8.8 / 2.8.14** — определение `Swords_B/items/ender_sword.json`.
- урон: `9`; максимальная прочность: `{"max_durability":1256}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: `{"category":"ender_sword","duration":2}`; левая рука: `false`; размер стопки: `1`; свечение: `true`; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:ender_sword"]` → `1256`; `["minecraft:ender_pearl"]` → `28`; `["minecraft:ender_eye"]` → `32`.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`.
- При использовании предмета указано: `{"on_use":{"event":"on_use"}}`.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 1.6:**

- Рецепт `Sword_B/recipes/ender_sword.json`; тип `minecraft:recipe_shaped`.
  - Схема сверху вниз: `F` / `F` / `E`.
  - Обозначения: `{"E":{"item":"minecraft:ender_pearl"},"F":{"item":"minecraft:ender_eye"}}`.
  - Результат: `{"item":"effect:ender_sword"}`; рабочие станции/tags: `["crafting_table"]`.

- Определение: `Sword_B/items/ender_sword.json`.
- Результаты рецептов: `Sword_B/recipes/ender_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

**Архив 2.8.14:**

- Рецептов с этим точным результатом локально не найдено. Это не исключает других путей.

- Определение: `Swords_B/items/ender_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - `Swords_B/loot_tables/entities/red_enderman.json` $.pools[0].entries[0]: `{"type":"item","name":"effect:ender_sword","weight":1,"functions":[{"function":"set_data","data":0}]}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[7].Mainhand[0].Name

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

**Условная математическая модель выбора loot в 2.x:**

Числа ниже — вероятность выбрать хотя бы одну запись предмета внутри уже активированного пула, а не шанс реальной добычи. Допущения: все записи доступны; отсутствующий вес принят за 1; quality и условия записей игнорируются; выборы независимы с возвращением; число rolls равномерно в указанном диапазоне. Условия пула считаются уже выполненными. Загрузка таблицы, дополнительный отбор, количество предметов и функции не эмулируются.

- Таблица/пул: `entities/red_enderman.json` / 0; entries: 0; rolls: `1`; вес ID/сумма: 1/1; выбор хотя бы одной записи по модели: **100.0000%**. Условия и оговорки: pool conditions: `[{"condition":"killed_by_player"},{"condition":"random_chance_with_looting","chance":0.025,"looting_multiplier":0.02}]`; functions: `[{"function":"set_data","data":0}]`.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Ender Sword (`effect:ender_sword`)

[Сравнение цепочек 1.6/2.x](manual-ender-wither-tnt-slime.md#ender-sword).

- `items/ender_sword.json`: damage 9, max durability 1256, foil true, enchantability 9/sword, cooldown 2, repair self 1256/ender_pearl 28/ender_eye 32, offhand false, web 15/bamboo 10. On use `spreadplayers ~ ~ 16 32 @s`, portal sound @a r34 и durability 5; on_hurt_entity durability 1. Размещение и успешность spreadplayers зависят от окружающего мира.
- `player.json:147–182,943–952,1416–1465`: family `[player,ender_sword]`, random looping timer 6…18 выбирает один из трёх звуков с равными весами. `hurt_on_condition` при `in_water_or_rain` задаёт cause drowning, damage_per_tick 1. В sensor non-projectile → `ender_sword_skill` с deals_damage true: hit sound и 50/100 пусто, 50/100 `spreadplayers ~ ~ 0 16 @s` + звук. Projectile → `ender_sword_tp` и deals_damage false. Третий trigger при `in_water_or_rain` тоже вызывает tp, deals_damage true, а фильтры могут пересекаться; порядок, сочетание и шанс фактической телепортации необходимо проверить в игре, не подменять одной таблицей исходов.
- `entities/enderman.json`: в spawn randomize weight 80 обычный и weight 20 red с фильтром biome tag overworld; поведение фильтра внутри выбора за пределами overworld требует теста. Red группа: health 120, attack 12, scale 1.2, teleport cube `[32,32,32]`, max_random_teleport_time 20, target/light teleport chance 0.04; явно привязана `loot_tables/entities/red_enderman.json`, где пул killed_by_player chance 0.025/looting_multiplier 0.02, один меч. Вес спавна и chance пула не являются доказанной общей вероятностью получения с любого эндермена.
- Выброшенный меч по имени `§l§5Ender Sword` получает tag ender_sword; при `q.is_on_fire` контроллер вызывает `despawn_event_1`: particle, звук и kill. Срабатывание зависит от порядка тегирования и анимации.

- В отдельном контроллере выброшенный item с тегом `ender_sword` при `q.is_on_fire` направляется в `despawn_event_1`: частицы `example_linearcurve`, звук `mob.endermen.death` для `@a[r=16]` volume 1/pitch 0.5 и `kill @s`. Тег назначается по имени функцией игрока; состояние до назначения тега и успех команд не доказаны.

**Старая версия 1.6** (источник: `docs/manual-traces-1.6.md`):

- **Ender** — 9/1256; `controller.animation.ender`: портальные частицы у `@p`; objective e увеличивается у `@e[r=16]`; звуки при score ближайшего игрока 10, 90, 140, 300, 500; при 85 выполняется `spreadplayers ~ ~ 8 16 @s`. Также без этой проверки score отдельные команды `spreadplayers ~ ~ 8 16` для перечисленных типов `r=10,rm=5` относительно ближайшего игрока. Удаление objective назначено при 700 и 750, поэтому второе условие может быть недостижимо при последовательном штатном исполнении — это не доказательство фактической недостижимости в игре.

**Дополнительный подробный разбор** (источник: `docs/manual-ender-wither-tnt-slime.md`):

#### Ender Sword

**Предмет и получение.** Damage 9 и durability 1256 в обеих версиях; enchantable 9/sword и self repair 1256, web 15/bamboo 10 также указаны в обеих. Offhand true в 1.6 и false в 2.x; дополнительно 2.x содержит repair `minecraft:ender_pearl` 28, `minecraft:ender_eye` 32. Рецепт 1.6 `F/F/E`, F = ender_eye, E = ender_pearl; прямого локального рецепта 2.x с результатом этого ID не найдено. В 2.x `entities/enderman.json` в spawn randomize 80 обычный / 20 red с фильтром biome tag overworld; red группа явно использует `loot_tables/entities/red_enderman.json`, где отдельный pool требует killed_by_player и chance 0.025, looting_multiplier 0.02. Это не безусловные 20% × 2.5% для любого эндермена: применимость фильтра, разрешение групп и лут нуждаются в проверке движка.

**1.6: две отдельные способности в группе и helper.** Hand sensor добавляет `minecraft:ender_sword`; группа содержит **не только** `spawn_entity` для `entity:ender` с wait 0/0, num 1, single_use true. Она также задаёт `minecraft:teleport`: `random_teleports:true`, `max_random_teleport_time:30`, `random_teleport_cube:[32,32,32]`, `target_distance:16`, `target_teleport_chance:0.05`, `light_teleport_chance:0.05`; `minecraft:hurt_on_condition` с фильтром `in_water_or_rain == true`, cause `drowning`, damage_per_tick 1. Эти параметры существуют на игроке независимо от команд helper; исходный текст не задаёт гарантированной частоты или направления телепортации.

Helper `controller.animation.ender`: оба состояния на входе содержат 40 одинаковых команд. Score `e` прибавляется **всем** `@e[r=16]` в контексте helper; звуки и проверка score 85 выбирают `@p`, причём `spreadplayers ~ ~ 8 16 @s` зависит от точного score. Ещё 27 отдельных строк от `@p` выполняют `spreadplayers ~ ~ 8 16` для указанных типов `@e[r=10,rm=5,type=…]` **без** score-фильтра. При 700 и при 750 отдельные команды удаляют глобальный objective, затем глобальный `@a swords=2`. Это не единый круг вокруг владельца; точные типы и порядок см. [матрицу](manual-area-targets-1.6.md#ender-разные-центры-и-разные-фильтры).

**2.x.** Только on_hurt_entity назначает durability damage 1. On-use — `spreadplayers ~ ~ 16 32 @s`, звук `@a[r=34]` и отдельно расход 5, cooldown 2; порядок соседних полей не доказан. Группа player не содержит `minecraft:teleport` 1.6: вместо него три damage trigger — non-projectile → event skill, deals_damage true; projectile → tp, false; `in_water_or_rain` → tp, true. Первое событие исполняет звук и выбор 50 пусто/50 `spreadplayers ~ ~ 0 16 @s`, два остальных вызывают tp без этого randomize. Вода и damage могут перекрываться: не считать результат взаимоисключающим или шансом на любую атаку. Отдельный random looping timer `[6,18]` выбирает один из трёх звуков; `hurt_on_condition` при `in_water_or_rain` остаётся, но фильтр 2.x **не содержит** явно записанного value. Выброшенный меч после тега по локализованному имени при огне получает событие с `kill @s`, а не гарантированную сохранность.

### Что написано на скриншотах

На изображении вручную считаны: damage = `9`; durability = `1256`; enchantable = `true`; repairable = `true`. Оригинал: [скриншот 115842](https://drive.google.com/file/d/117ulXVShaEZGyc0CdADa5mQUYlmAveAT/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 13. Fire Sword — `effect:fire_sword`

**Кратко:** Огонь, живое пламя и превращение выброшенного меча. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

**1.6** — определение `Sword_B/items/fire_sword.json`.
- урон: `12`; максимальная прочность: `{"max_durability":2000}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `true`; размер стопки: `1`; свечение: не указан; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:fire_sword"]` → `2000`.
- Оружейный компонент не указан.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**2.8.8 / 2.8.14** — определение `Swords_B/items/fire_sword.json`.
- урон: `6`; максимальная прочность: `{"max_durability":2000}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: `{"category":"fire_sword","duration":25}`; левая рука: `false`; размер стопки: `1`; свечение: `true`; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:fire_sword"]` → `2000`; `["minecraft:fire"]` → `1000`.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`; событие без нанесения урона существу → `{"event":"weapon"}`; удар по блоку → `{"event":"weapon"}`.
- При использовании предмета указано: `{"on_use":{"event":"on_use"}}`.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 1.6:**

- Рецепт `Sword_B/recipes/fire_sword.json`; тип `minecraft:recipe_shaped`.
  - Схема сверху вниз: `#SM` / `SBS` / `NS#`.
  - Обозначения: `{"N":{"item":"minecraft:blaze_rod"},"S":{"item":"minecraft:blaze_powder"},"B":{"item":"minecraft:iron_sword"},"M":{"item":"minecraft:magma_cream"}}`.
  - **В схеме есть символы без определения key: `["#"]`.** Их смысл и принятие рецепта движком не установлены.
  - Результат: `{"item":"effect:fire_sword"}`; рабочие станции/tags: `["crafting_table"]`.

- Определение: `Sword_B/items/fire_sword.json`.
- Результаты рецептов: `Sword_B/recipes/fire_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

**Архив 2.8.14:**

- Рецепт `Swords_B/recipes/fire_sword.json`; тип `minecraft:recipe_shaped`.
  - Схема сверху вниз: `F` / `F` / `#`.
  - Обозначения: `{"#":{"item":"minecraft:blaze_rod"},"F":{"item":"minecraft:fire"}}`.
  - Результат: `{"item":"effect:fire_sword"}`; рабочие станции/tags: `["crafting_table"]`.

- Определение: `Swords_B/items/fire_sword.json`.
- Результаты рецептов: `Swords_B/recipes/fire_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - `Swords_B/loot_tables/entities/living_flame.json` $.pools[0].entries[0]: `{"type":"item","name":"effect:fire_sword","weight":1,"functions":[{"function":"set_data","data":0}]}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[15].Mainhand[0].Name
  - `Swords_B/structures/fire_sword.mcstructure` $.entities[0].Item.Name

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

**Условная математическая модель выбора loot в 2.x:**

Числа ниже — вероятность выбрать хотя бы одну запись предмета внутри уже активированного пула, а не шанс реальной добычи. Допущения: все записи доступны; отсутствующий вес принят за 1; quality и условия записей игнорируются; выборы независимы с возвращением; число rolls равномерно в указанном диапазоне. Условия пула считаются уже выполненными. Загрузка таблицы, дополнительный отбор, количество предметов и функции не эмулируются.

- Таблица/пул: `entities/living_flame.json` / 0; entries: 0; rolls: `1`; вес ID/сумма: 1/1; выбор хотя бы одной записи по модели: **100.0000%**. Условия и оговорки: functions: `[{"function":"set_data","data":0}]`.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Fire Sword (`effect:fire_sword`), живое пламя и превращение выброшенного предмета

[Сравнение цепочек 1.6/2.x](manual-fire-spider-sponge.md#fire-sword).

##### Предмет и получение

`items/fire_sword.json:8–77`: damage 6, durability 2000, cooldown duration 25, foil true, enchantability 9/slot sword, stack 1, offhand false. Ремонт самим мечом на 2000 или буквальным ID `minecraft:fire` на 1000; скорости web 15 и bamboo 10. `recipes/fire_sword.json:1–25` задаёт crafting_table pattern `F / F / #`, F = `minecraft:fire`, # = `minecraft:blaze_rod`. Способность добыть/использовать fire как предмет и валидность такого рецепта надо проверить, а не молча заменить ингредиент.

`entities/living_flame.json:230–255` событие `start_death_hostile` сначала добавляет despawn и выполняет очистку огня/частицы/звук, затем при family != living_flame_passive и != living_flame_projectile выбирает 85 пусто / 15 `loot spawn ~ ~ ~ loot "entities/living_flame"`. `loot_tables/entities/living_flame.json:1–20` содержит 1 roll, единственный `effect:fire_sword` weight 1, set_data 0. Условная доля выбора ветви 15/100, но достижимость события, фильтр, исход команды после добавления despawn и фактическое появление добычи требуют проверки.

`living_flame.json:61–100,103–106`: группа `hostile_entity` вызывает `start_death_hostile` не только через `minecraft:on_death`, но и через `minecraft:damage_sensor` при `other` family player, с `deals_damage:false` и **без явного фильтра fatal**. Passive-группа на аналогичный урон вызывает другое событие, `minecraft:start_death`, тоже с `deals_damage:false`; базовый `minecraft:on_death` также указывает `minecraft:start_death`. Таймер hostile `[25,60]` вызывает именно `minecraft:start_death`, а не `start_death_hostile`. Поэтому не заменять условие на «15% только после смертельного удара игрока» и не считать таймер hostile автоматически шансом на меч: применение группы, приоритеты компонентов, отмену урона и обе возможные точки вызова события требуется проверить в игре.

##### Удары и удержание

`items/fire_sword.json:106–132`: все три weapon-хука запускают sequence: damage durability 1, затем 85/100 shoot `entity:fire` power 1 или 15/100 shoot `entity:living_flame` power 1. `entities/fire.json:11–56`: базовый projectile power 1, gravity 0.01, impact damage 0 и catch_fire true; при entity_spawned с other, у которого в hand fire_sword, добавляется группа fire_sword с projectile power **10**, gravity **0.1**, impact damage **1**, knockback false, catch_fire true, fire_affected_by_griefing true. Family-проверку и изменение группы нужно воспроизводить отдельно от метательного launch_power.

`player.json:323–333,696–708,2054–2084`: группа игрока отменяет только `fire`/`fire_tick`, задаёт looping random timer `[0.2,0.7]` → звук `fire.fire @a[r=8]` и family `[player,fire_sword]`. При удержании команды в кубе ±3 заменяют snow_layer на air, ice/blue_ice/packed_ice на water; для `@e[family=!player,type=!item,r=3]` вызывают summon `entity:fire`; в кубе ±1 заменяют air и существующий `effect99:lightblock` на этот же блок. Он имеет emission 1, absorption 0, destroy_time 0.1, explosion_resistance 999, нулевую геометрию коллизии и ticking range `[0.2,0.2]` с командой setblock air (`blocks/lightblock.json:1–35`). Это временные блоки, которые могут взаимодействовать с миром, а не только визуальная подсветка.

##### Fire rain

`items/fire_sword.json:79–105`: по on_use в последовательности первым шагом вызываются шесть summon `entity:living_flame`: один `~ ~14 ~ minecraft:target`; пять с событием `fire_sword_skill` на `~ ~4 ~`, `~3 ~4 ~`, `~ ~4 ~3`, `~-3 ~4 ~`, `~ ~4 ~-3`; затем частица `example_linearcurve ~ ~0.2 ~`, actionbar `§l§6Fire rain`. Следующим шагом durability damage 20. Команды используют target holder; cooldown задан в item.

`entities/living_flame.json:10–35,268–270`: target family `[target,effect99_entities]`, защита cause all, physics no gravity/no collision и timer `[10,10]` → despawn. Пять элементов skill имеют family `[fire_sword_skill,effect99_entities]`, тот же 10-секундный таймер, collision 0.1×0.1, no gravity/no collision и защиту от всего урона; ranged_attack interval 0.1, radius 64, shooter `minecraft:small_fireball`, nearest target family `target` max_dist 64. Это наводка на отдельно созданный объект, а не непосредственно на всех мобов. Порядок вызовов, spawn events и разрешение одновременных компонентов необходимо проверить.

`living_flame_projectile` при попадании задаёт impact damage 1/knockback true/catch_fire true, power 1, gravity 0.02 и событие `minecraft:stop_projectile`, которое удаляет hostile_entity и living_flame_projectile и добавляет passive_entity. Passive имеет family living_flame_passive, выбирает monster max_dist 16 и random timer `[10,30]`; hostile выбирает monster или player max_dist 16 и random timer `[25,60]`. Общая база содержит ещё timer `[10,40]`, health 20, attack 3 и другие AI; поведение при наложении групп нельзя вывести простой суммой. В `components` два раза встречается `minecraft:fire_immune: true`, что не меняет записанное значение, но остаётся признаком неоднозначного JSON.

##### Выброшенный меч: вода, дождь и огонь

[Единая схема всех девяти команд горения и sensor-таймеров](manual-dropped-items-2.8.md).

`player.json:627–630,1055–1066` вызывает функцию `.../tag_swords` из `minecraft:constant_events`; она ищет `@e[type=item,name="§l§6Fire Sword",tag=!fire_sword]` и добавляет tag fire_sword. Это выбор **по отображаемому имени**, а не по item ID. Переименование, локализация, отсутствие игрока/выполнения функции и порядок tick-ов могут изменить результат; модель «любая сущность с ID fire_sword всегда помечена» недоказана.

`entities/item.json:25–30,34–61,216–229`: если item имеет tag fire_sword, не in_water, но in_water_or_rain, вызывается fading_fire_sword: при отсутствии family fire_sword добавляет одноразовый random timer `[5,6]` → fire_sword_event_1; отдельно воспроизводит fizz и частицы. По окончании event_1 выполняет `structure load obsidian_sword ~ ~ ~`, звук, `kill @s`. Если до окончания таймера условие `in_water_or_rain !=` выполнено, `stop_fire_sword` удаляет группу. При tag fire_sword и **in_water** event_2 сразу выполняет fizz, частицы, `structure load glass_sword ~ ~ ~`, затем `kill @s`. Расшифрованные NBT структур показывают по одной `minecraft:item` с Name `effect:obsidian_sword` и `effect:glass_sword`; сохранённые поля предмета, включая Count и Damage, см. [структуры](structures-2.8.14.md). Нельзя предполагать, что старая прочность/зачарования переносятся: создаётся сохранённая сущность из структуры. Для `obsidian_sword.mcstructure` в NBT указаны `Item.Damage=0` и вложенное `Item.tag.Damage=1000` при `Count=1`; как движок интерпретирует оба поля прочности, нужно проверить.

`animation_controllers/item_events.json:4–29` при `q.is_on_fire` отправляет `fire_sword_event_3` только item с tag fire_sword **без** fire_sword_respawn. В event_3 (`item.json:230–255`) ещё раз проверяется tag fire_sword, затем девять частиц в координатах ±1 на y+0.3, пять раз `summon entity:living_flame ~~~ hostile_entity`, звук `mob.wither.spawn @a[r=16]` volume 1/pitch 2 и `kill @s`. Очередность назначения тегов, дождя/воды и fire-controller влияет на результат. Отдельная ветка `tag=fire_sword_respawn` вызывает `respawn_event_2`: загрузку `fire_sword` на y+1 и удаление старой item-сущности. В `structures/fire_sword.mcstructure` уже записаны оба тега `fire_sword` и `fire_sword_respawn`, а вложенный `Item.tag.Damage=0`. При сохранении тегов после загрузки это может повторно запускать ветку возрождения при горении; сохранение тегов, очередность событий и число повторений нужно проверить в игре, не предполагая бесконечный цикл. Это необходимо проверить на старой версии без предположений об атомарности команд.

**Старая версия 1.6** (источник: `docs/manual-traces-1.6.md`):

#### Fire, Magma и Spider 1.6: типы и мир

[Три контроллера, рецепты и риск изменения мира](manual-fire-magma-spider-1.6.md) · [матрица type-селекторов](fire-web-targets-1.6.md).

**Дополнительный подробный разбор** (источник: `docs/manual-fire-spider-sponge.md`):

#### Fire Sword

[Условная межигровая матрица family и type](manual-family-cross-effects-2.8.md).

**Предмет и получение.** 1.6 damage 12, durability 2000, offhand true; 2.x damage 6, durability 2000, offhand false; self repair 2000, enchantable 9/sword и web/bamboo 15/10 указаны в обеих. Дополнительно 2.x repair буквальным `minecraft:fire` 1000 и cooldown 25. Рецепт 1.6 `#SM/SBS/NS#`: S blaze_powder, M magma_cream, B iron_sword, N blaze_rod, но `#` не задан в key. В 2.x `F/F/#`, F = `minecraft:fire`, # = blaze_rod. Нельзя подставлять другой ингредиент или утверждать, что fire доступен как предмет и рецепт работает.

В 2.x `living_flame` имеет `start_death_hostile` с фильтром не passive и не projectile, randomize 85 пусто/15 `loot spawn ... entities/living_flame`; локальная таблица содержит один Fire Sword. В hostile-группе damage sensor вызывает это событие от `other` family player с `deals_damage:false` и **без** явного fatal; on_death тоже ведёт туда, но hostile timer `[25,60]` вызывает другое событие `minecraft:start_death`. 15/100 нельзя приписать каждому убийству или каждому истечению таймера.

**1.6.** Hand sensor → spawn `entity:fire` → `controller.animation.fire`. На входе каждого из двух состояний одинаковые 39 строк: fire_resistance ближайшему `@p` и detect воздуха в его позиции с setblock fire; пять fill в кубе ±3 относительно `@p` (snow_layer→air, ice/blue_ice/packed_ice→water, snow→grass); 31 отдельная type-команда `setblock fire` у сущностей r=15/rm=2 относительно helper, включая ряд мирных животных и villager; затем `@a swords=2`. В этих 31 командах нет явного `replace air`; выбор ближайшего игрока и сущностей имеет разные центры. [Порядок и список](manual-fire-magma-spider-1.6.md#fire-31-тип-и-изменения-блоков).

**2.x.** Три weapon-хука задают durability 1, затем randomize 85 `shoot entity:fire` / 15 `shoot entity:living_flame`; группа projectile может изменить power/gravity после entity_spawned. On-use `sequence` содержит шесть summon living_flame: одну цель y+14 и пять помощников y+4 в центре и на осях ±3; затем durability 20. Помощники выбирают созданную family target, а не прямо всех мобов. Player group отменяет fire/fire_tick, удержание меняет snow_layer/ice/blue_ice/packed_ice в кубе ±3 и вызывает `entity:fire` у `@e[family=!player,type=!item,r=3]`; вместе с ними обновляется lightblock в кубе ±1. Целевой selector шире перечня враждебных мобов, чем «поджечь только противников».

Выброшенный предмет после тега по **форматированному имени** при `in_water` вызывает загрузку структуры **Glass Sword** и kill исходной item-сущности; вне воды при `in_water_or_rain` одноразовый random timer `[5,6]` ведёт к структуре **Obsidian Sword**, а при прекращении условия группа таймера снимается. Это противоположно формулировке просмотренного скриншота о воде/дожде; версия скриншота неизвестна. Огонь вызывает другую цепь. Ни сохранение прежних чар, ни фактический порядок тега/таймера не доказаны.

**Дополнительные детали 1.6** (источник: `docs/manual-fire-magma-spider-1.6.md`):

### Fire, Magma и Spider 1.6: цели и воздействие на мир

[Сравнительная таблица всех type-селекторов](fire-web-targets-1.6.md) извлекает строки из трёх исходных контроллеров. Ни одна команда не проверена на выполнение в игре: старые имена, селекторы, замена блоков, контекст `@p` и частота зависят от движка.

#### Общая цепь и разные центры

Для каждого предмета `player.json` проверяет `has_equipment` в domain `hand`, передаёт одноимённый event и добавляет группу `minecraft:fire_sword` / `minecraft:magma_sword` / `minecraft:spider_sword`. Группы соответственно объявляют spawn `entity:fire`, `entity:magma`, `entity:spider`, каждая wait 0/0, num_to_spawn 1, single_use true. Другая player-ветвь удаляет эти группы; повторное добавление и длительность жизни помощника не установлены. Helpers используют family `despawnear` и одноимённые animation controllers; их положение не гарантированно следует за владельцем.

В каждом из трёх контроллеров `default` и состояние с именем меча переходят друг в друга по `(1.0)` и содержат одинаковые строки `on_entry`. Соответственно, сравнение ниже относится к **одному списку**, а не двум одновременно выполненным копиям. Каждая последовательность заканчивается `/scoreboard players set @a swords 2` для всех выбранных игроков; глобальные взаимодействия и возможные повторы описаны [отдельно](manual-global-state-1.6.md).

`@p` выбирается из контекста helper и не гарантированно означает владельца. Отдельные `@e[r=...,type=...]` сначала выбираются относительно контекста helper, после чего `execute` использует позицию соответствующей цели. Не заменять их единой областью вокруг игрока.

#### Предметы и рецепты 1.6

| Предмет | damage / max durability / self repair | Локальный shaped recipe |
|---|---|---|
| Fire | 12 / 2000 / 2000 | `#SM / SBS / NS#`; `N=blaze_rod`, `S=blaze_powder`, `B=iron_sword`, `M=magma_cream`; **`#` отсутствует в key** |
| Magma | 7 / 1000 / 1000 | `F / F / E`; `F=minecraft:magma`, `E=minecraft:blaze_rod` |
| Spider | 6 / 628 / 628 | `#SS / SBS / NS#`; `N=stick`, `S=web`, `B=spider_eye`; **`#` отсутствует в key** |

Все три: max stack 1, `allow_off_hand:true`, `hand_equipped:true`, `can_destroy_in_creative:false`, `minecraft:glint:false`, enchantable value 9/slot sword, digger web 15/bamboo 10/use_efficiency true. Ремонт — самим предметом; названия ингредиентов без namespace в таблице обозначают исходный `minecraft:`. Нет основания автоматически дописывать key `#`, исправлять буквальный `minecraft:magma` или считать объявленные рецепты работающими. [Полная проверка рецептов](manual-acquisition-issues.md), [сравнение компонентов с 2.x](item-version-matrix.md).

#### Fire: 31 тип и изменения блоков

`Sword_B/animation_controllers/fire_sword.json`, в каждом состоянии **39** строк:

1. `/effect @p fire_resistance 10 0 true` — длительность 10, amplifier 0.
2. `execute @p ... detect ~ ~ ~ air 0 setblock ~ ~ ~ fire` — проверка воздуха в позиции ближайшего игрока.
3. Пять fill относительно `@p` в кубе `~3 ~3 ~3` → `~-3 ~-3 ~-3`: **7×7×7 = 343** возможных позиций в каждой геометрической рамке. В исходном порядке: `snow_layer → air 0`; `ice → water 0`; `blue_ice → water 0`; `packed_ice → water 0`; `snow → grass 0`. Это замена существующего мира, не декоративная частица и не сохранение исходных блоков; фактическое число замен зависит от содержимого, интерпретации data и успеха команд.
4. **31** команда `@e[r=15,rm=2,type=…] ... setblock ~ ~ ~ fire` для типов из [матрицы](fire-web-targets-1.6.md), включая корову, свинью, овцу, лошадь, кролика, курицу, лису, летучую мышь, белого медведя и жителя. Нет ограничения только на враждебных существ. В этих отдельных командах нет `detect` или `replace air`; запись `setblock` потенциально затрагивает имеющийся блок в позиции цели, но точные стандартные режимы, перенос координат и результат при занятом блоке нужно проверить в исходном движке.
5. Глобальный scoreboard для `@a`.

Самому ближайшему игроку команда №2 может поставить огонь при detect air, хотя №1 отдельно объявляет fire resistance. Успех одной команды не доказывает успех другой, а сопротивление не является доказанной защитой от любых причин урона.

#### Magma: 21 тип и плоскость лавы

`Sword_B/animation_controllers/magma_sword.json`, **24** строки на состояние: та же запись `fire_resistance 10 0 true` для ближайшего игрока; затем `fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 magma 0 replace lava` от `@p`, плоскость **5×5 = 25** геометрических позиций. После `replace lava` в этой команде **нет явного data**; не добавлять `0` по аналогии с другими файлами. В исходнике нет такой же отдельной команды для `flowing_lava`; это не доказательство того, какие именно состояния лавы выберет движок.

Далее **21** type-команда `setblock fire` в `r=15,rm=2` от helper и глобальный scoreboard. Эти 21 типа — точное подмножество 31 Fire; **10** типов, имеющихся в Fire и отсутствующих в Magma, — `cow`, `pig`, `chicken`, `horse`, `rabbit`, `sheep`, `fox`, `bat`, `polar_bear`, `villager`. Это сопоставление только буквальных команд данного контроллера, не утверждение о полной безопасности перечисленных существ.

#### Spider: паутина и два разных селектора

`Sword_B/animation_controllers/spider_sword.json`, **31** строка на состояние:

1. `effect @p poison 0 0 true`.
2. Две команды с `detect ... web 0` удаляют web в позиции `@p` или на y+1, заменяя web на air только в соответствующей точке.
3. От позиции `@p` задаётся `slowness 1 128 true` для `@e[r=6,type=spider]` и отдельно `type=cave_spider`. Эти эффекты не направлены на весь список паутины и имеют другой центр выбора.
4. **25** отдельных типов выбираются в `@e[r=5,type=…]` от helper; в позиции каждой цели команда `fill ~ ~ ~ ~ ~ ~ web 0 replace air` проверяет одну позицию. Список содержит, среди прочего, `tnt`, `evocation_fang`, `blaze` и `zombie_pigman`, но **не содержит** отдельного web-fill по `spider` или `cave_spider`. Их наличие в командах slowness не означает наличие в списке fill.
5. `scoreboard players set @a swords 2`.

Не путать статическое количество строк с количеством целей/реальных блоков: каждая команда может выбрать ноль, одну или много сущностей, выполняться несколько раз или не пройти. Отсутствие type-команды в этих трёх списках не доказывает отсутствия воздействия из другой механики, vanilla или иного пакета. Реализации 2.x используют дополнительные события/loot/сущности и не сводятся к этим старым контроллерам; см. [карточки 2.8.14](manual-traces-2.8.14.md).

### Что написано на скриншотах

На изображении вручную считаны: damage = `6`; durability = `2000`; enchantable = `true`; repairable = `true`. Оригинал: [скриншот 115915](https://drive.google.com/file/d/1PepsprtsCCeeGxcvjyUMemLzYdbtQMM6/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 14. Ghost Sword — `effect:ghost_sword`

**Кратко:** Группа призрака и отдельный снаряд; отрицательный урон не расшифрован. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

- В 1.6 предмет с этим точным ID не найден.

**2.8.8 / 2.8.14** — определение `Swords_B/items/ghost_sword.json`.
- урон: `-666`; максимальная прочность: `{"max_durability":3333}`; зачарование: не указан; перезарядка: `{"category":"ghost_sword","duration":2}`; левая рука: `false`; размер стопки: `1`; свечение: `true`; предмет исчезает: `false`.
- Ремонт: компонент не указан; это не доказывает невозможности ремонта.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`; событие без нанесения урона существу → `{"event":"weapon"}`; удар по блоку → `{"event":"weapon"}`.
- При использовании предмета указано: `{"on_use":{"event":"on_use"}}`.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 2.8.14:**

- Рецептов с этим точным результатом локально не найдено. Это не исключает других путей.

- Определение: `Swords_B/items/ghost_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[33].Mainhand[0].Name
  - `Swords_B/structures/ghost_sword.mcstructure` $.entities[0].Item.Name

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Ghost Sword (`effect:ghost_sword`)

[Подробные получение, снаряды и связи](manual-ghost-nether-ultra.md#ghost-sword).

- В item damage `-666`, durability 3333, cooldown 2, enchantable и repairable не объявлены. On-use стреляет `entity:ghost_projectile`, launch_power 1, и задаёт потерю 6 прочности; weapon-триггеры всех трёх типов запускают расход 1. Отрицательное damage нельзя автоматически трактовать как лечение или как гарантированный урон.
- `player.json:47–65,999–1008,1216–1280`: группа задаёт scale 1.05, knockback resistance 1, collision box 0×0, дыхание в воде/воздухе/лаве, damage_sensor `cause:all, deals_damage:false`, family `[ghost_sword]`; ghost_movement value 0.14. Во время события выдаются slow_falling 1 amplifier 0 и saturation 1 amplifier 1; при `in_water` — levitation 1/0; при `in_lava` — levitation 1/0 и fire_resistance 1/0; в противоположной ветви задаётся fire_resistance 0/0. Случайный звук weight 10 против пустой ветви weight 90. Команды входа/выхода, частицы и их координаты оставить как в исходнике.
- `animation_controllers/ghost_sword.json:4–35`: при q.get_equipped_item_name == ghost_sword и sneak в состоянии levitation_ghost выполняется `effect @s levitation 1 3 true`, затем переход `1.0` в default; если не sneak — `effect @s levitation 0 0` и возврат. Это независимая цепочка, не только событие предмета.
- `entities/ghost_projectile.json:1–79`: runtime snowball; исходно collision 0×0, physics has_collision false, projectile power 2.5, gravity 0, liquid_inertia 2.8, impact_damage -1. Looping timer `[0,0]` вызывает `teleport_owner`; он командой при обнаружении air или отдельной ветвью при in_water добавляет группу `teleport_enable`. В ней collision 10×10, has_collision true, impact_damage -1, knockback false, `teleport_owner` и `remove_on_hit`; power/gravity/inertia сохранены. Это не просто мгновенная телепортация в точку взгляда. Неясные старые значения и время до столкновения нужны для реального испытания.

##### Призрак и получение меча

- `entities/ghost.json`: `entity:ghost`, runtime `minecraft:chicken`, family `[ghost,mob,monster]`, health 666/666, collision 0.6×1.8, scale 1.05, movement 0.3, knockback resistance 1, fire_immune true, pushable false. У damage_sensor есть два потенциально перекрывающихся триггера: урон от `other` family player вызывает `disturbed_ghost` и `deals_damage:false`; отдельный cause all также `deals_damage:false`. Фактическое срабатывание при разных атаках и порядок триггеров нужно испытать.
- `disturbed_ghost`: один randomize суммарного веса 1000: 987 — пусто; 10 — звук и `spreadplayers ~ ~ 0 16 @s`; 3 — добавить группу despawn и выполнить `structure load ghost_sword ~~~` с частицами/звуком. Это **1% и 0,3% условно на этот выбор**, не вероятность получения на любой контакт. `structures/ghost_sword.mcstructure` действительно содержит одну item-сущность с `Item.Name=effect:ghost_sword`, Count 1, Damage 0; успех загрузки и подбора не доказан.
- `spawn_rules/ghost.json` содержит два условия: underground на `minecraft:stone`, brightness 0…7 `adjust_for_weather:true`, difficulty easy…hard, вес 100, herd 1…2 и biome tag `monster`; surface на `minecraft:grass`, те же brightness/difficulty/biome, вес 50 и surface density 3. Только underground-условие явно назначает spawn_event `ghost_wailing`: его ветви 70 пусто/30 вложенный выбор 50/50 двух вариантов звука, по 15/100 на каждый при стандартной семантике. В файле нет прямого условия ночи; вес спавна не означает процент. Сенсор самой сущности вызывает despawn при `is_brightness > 0.1`; связь чисел brightness фильтра спавна и сенсора без проверки движка не предполагается.

**Дополнительный подробный разбор** (источник: `docs/manual-ghost-nether-ultra.md`):

#### Ghost Sword

**Серверное испытание 2.8.8 / 1.20.50.03:** свинье заранее снизили здоровье с 10 до 6 HP. Две отправленные ботом атаки с Ghost Sword в подтверждённой руке не изменили здоровье цели; контрольный удар пустой рукой после замены меча снизил его с 6 до 5. Нет отдельного подтверждения, что оба пакета Ghost Sword стали успешными попаданиями, поэтому это наблюдение не доказывает ни лечение, ни точное правило отрицательного урона. [Сценарий и журнал](../data/original-mechanics-2026-11-07/README.md).


**Защита и применение (практика 2.8.8 / 1.20.50.03):** без меча серверная команда урона `entity_attack` на 4 HP снизила здоровье с 20 до 16. После лечения при активной family Ghost аналогичные команды `entity_attack` и `fire` были отклонены, здоровье осталось 20. Проверены только эти серверные команды, а не все причины урона и не удары мобов. Применение создало ghost_projectile, израсходовало 6 прочности и переместило игрока примерно на 3,5 блока по горизонтали и 1,62 по вертикали; конечную позицию подтвердил сервер. При повторных пробах с каменной стеной на z=202 игрок не переместился, а при стенах на z=204 и z=206 конечная координата совпала с плоскостью стены; пересечение на другую сторону не доказано. В открытом очищенном коридоре без конечного препятствия перемещения также не было. [Условия](../data/original-mechanics-2026-11-07/README.md). После снятия меча игрок получил непрерывный урон огнём, поэтому этот этап нельзя использовать как чистый контроль защиты. [Журнал](../data/original-mechanics-2026-11-07/README.md).

[Условная межигровая матрица family и type](manual-family-cross-effects-2.8.md).

`effect:ghost_sword`: damage **−666**, durability 3333, cooldown 2, offhand false, foil true, `should_despawn:false`; enchantable и repairable не объявлены. На три weapon-хука direct durability 1; on-use задаёт shoot `entity:ghost_projectile` launch_power 1 и отдельный durability damage 6. Отрицательный damage не доказывает лечение, отрицательный урон или иное поведение.

Прямой локальный recipe и loot entry с этим ID не найдены. У `entity:ghost` runtime chicken, health 666, family `[ghost,mob,monster]`; damage sensor при `other` family player вызывает `disturbed_ghost`, deals_damage false, и отдельный trigger cause all также false. `disturbed_ghost` выбирает 987 пусто / 10 звук и `spreadplayers` / 3 `structure load ghost_sword` плюс despawn/частицы. 0.3% и 1% — только доли соответствующего выбора, не безусловный шанс любой атаки или фактической загрузки. Структура содержит один сохранённый предмет нужного ID. Underground и surface spawn rules имеют разные веса, а sensor самой сущности проверяет `is_brightness > 0.1`; их единицы, порядок и соответствие ночи не выводятся арифметически.

Player group задаёт scale 1.05, collision 0×0, breathes water/air/lava, knockback resistance 1, damage_sensor cause all/deals_damage false и **family только `[ghost_sword]`**, без явно перечисленной `player`. Отдельная добавляемая группа `ghost_movement` задаёт movement 0.14. Stop явно удаляет `minecraft:ghost_sword` и добавляет default_player, но **не перечисляет `ghost_movement`**. Это не доказательство постоянной скорости или потери family player: разрешение перекрывающихся компонентов/групп неизвестно. В частности, другие селекторы с family player/default_player могут взаимодействовать с таким объявлением; считать взаимодействие доказанным нельзя.

`entity:ghost_projectile` исходно имеет collision 0×0, has_collision false, projectile power 2.5, gravity 0, liquid_inertia 2.8, impact_damage −1; looping timer `[0,0]` запускает логику `teleport_owner`, которая при указанных air/water проверках добавляет `teleport_enable`. Эта группа изменяет collision до 10×10, включает collision и on-hit `teleport_owner`/`remove_on_hit`. Исходный timer и наличие группы не доказывают телепортацию сквозь каждый блок. Отдельный animation controller при sneak назначает levitation 1/3, при отсутствии sneak снимает её; это независимый вход от item on-use.

### Что написано на скриншотах

На изображении вручную считаны: damage = `-666`; durability = `3333`; enchantable = `false`; repairable = `false`. Оригинал: [скриншот 120011](https://drive.google.com/file/d/1tY_bT4l7lOkdHRfKqglYbqXP2_FiM70D/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 15. Glass Sword — `effect:glass_sword`

**Кратко:** Высокий записанный урон и прочность 1; связан с Fire Sword в воде. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

- В 1.6 предмет с этим точным ID не найден.

**2.8.8 / 2.8.14** — определение `Swords_B/items/glass_sword.json`.
- урон: `33`; максимальная прочность: `{"max_durability":1}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `false`; размер стопки: `1`; свечение: `false`; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:glass_sword"]` → `1`; `["minecraft:glass"]` → `1`.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`; событие без нанесения урона существу → `{"event":"weapon"}`; удар по блоку → `{"event":"weapon"}`.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":25,"on_dig":{"event":"weapon"}},{"block":"minecraft:bamboo","speed":15,"on_dig":{"event":"weapon"}}],"on_dig":{"event":"weapon"}}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 2.8.14:**

- Рецептов с этим точным результатом локально не найдено. Это не исключает других путей.

- Определение: `Swords_B/items/glass_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[29].Mainhand[0].Name
  - `Swords_B/structures/glass_sword.mcstructure` $.entities[0].Item.Name

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Glass Sword (`effect:glass_sword`)

[Полная сравнительная карточка 1.6/2.x](manual-basic-swords.md#glass-sword--только-2x-среди-точных-id).

- `items/glass_sword.json`: damage 33, max durability 1, enchantability 9/sword, offhand false. **Repairable задан**: self 1 и `minecraft:glass` 1; описание на изображении `Screenshot_20261104_120007_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg` сообщает `Repairable: false`, поэтому поведение на исходном движке следует проверить. Digger web speed 25 и bamboo 15, у обоих и у общего digger указан `on_dig` → weapon.
- Все три weapon-хука вызывают событие с durability damage **10** и `playsound random.glass @a[r=8,m=0]`; оба поля находятся в одном шаге sequence, их фактический порядок и сочетание с `on_dig` не выводить как единственное срабатывание. Источник в прослеженной цепочке Fire Sword: выброшенный меч в воде, с тегом по имени, загружает структуру `glass_sword` и уничтожает прежний item; состояние не гарантируется.

**Дополнительный подробный разбор** (источник: `docs/manual-basic-swords.md`):

#### Glass Sword — только 2.x среди точных ID

`effect:glass_sword` отсутствует как точный item ID в 1.6. В обеих 2.x: damage 33, durability 1, stack 1, enchantable 9/sword, offhand false, `repairable` с self 1 и `minecraft:glass` 1. Это прямо расходится с текстом `Repairable: false` в локальной справке; наличие компонента тоже не доказывает фактическую работу ремонта.

`minecraft:digger` имеет общий `on_dig` → `weapon`, а также отдельный `on_dig` на web speed 25 и bamboo speed 15. Все три weapon-хука тоже ведут в то же событие: один элемент sequence одновременно задаёт durability damage 10, target self, и `playsound random.glass @a[r=8,m=0]`. Не считать эти пути взаимоисключающими, не утверждать число вызовов и не выдумывать порядок одноуровневых полей. Sensor с точным item ID в player не найден; это не доказательство отсутствия других связей.

Результат в локальных recipes, прямых loot item entries и торговле не найден. Основной рассмотренный путь: Fire Sword как выброшенный item с tag `fire_sword`, при `in_water` вызывает `fire_sword_event_2`, который загружает `glass_sword` и затем `kill @s`. В структуре `Swords_B/structures/glass_sword.mcstructure` хранится item `effect:glass_sword`, Count 1. Сам тег ранее ставится по отображаемому имени функцией игрока; ни сохранение исходной прочности/чар, ни работоспособность всех шагов не выводится из текста. Отдельно `give.mcfunction` содержит выдачу Glass. Подробная цепь и конкурирующие события — [выброшенные предметы](manual-dropped-items-2.8.md).

### Что написано на скриншотах

На изображении вручную считаны: damage = `33`; durability = `1`; enchantable = `true`; repairable = `false`. Оригинал: [скриншот 120007](https://drive.google.com/file/d/18xMWPEmEQ3k8DUxotbJS2CD1IIXMbY6s/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 16. Glowstone Sword — `effect:glowstone_sword`

**Кратко:** Создаёт временные световые блоки; доступна левая рука. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

**1.6** — определение `Sword_B/items/glowstone_sword.json`.
- урон: `6`; максимальная прочность: `{"max_durability":128}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `true`; размер стопки: `1`; свечение: не указан; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:glowstone_sword"]` → `128`.
- Оружейный компонент не указан.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**2.8.8 / 2.8.14** — определение `Swords_B/items/glowstone_sword.json`.
- урон: `4`; максимальная прочность: `{"max_durability":128}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `true`; размер стопки: `1`; свечение: `true`; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:glowstone_sword"]` → `128`; `["minecraft:glowstone"]` → `64`; `["minecraft:glowstone_dust"]` → `16`.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 1.6:**

- Рецепт `Sword_B/recipes/glowstone_sword.json`; тип `minecraft:recipe_shaped`.
  - Схема сверху вниз: `020` / `020` / `010`.
  - Обозначения: `{"1":{"item":"minecraft:blaze_rod"},"2":{"item":"minecraft:glowstone"}}`.
  - **В схеме есть символы без определения key: `["0"]`.** Их смысл и принятие рецепта движком не установлены.
  - Результат: `{"item":"effect:glowstone_sword"}`; рабочие станции/tags: `["crafting_table"]`.

- Определение: `Sword_B/items/glowstone_sword.json`.
- Результаты рецептов: `Sword_B/recipes/glowstone_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

**Архив 2.8.14:**

- Рецепт `Swords_B/recipes/glowstone_sword.json`; тип `minecraft:recipe_shaped`.
  - Схема сверху вниз: `2` / `2` / `1`.
  - Обозначения: `{"1":{"item":"minecraft:blaze_rod"},"2":{"item":"minecraft:glowstone"}}`.
  - Результат: `{"item":"effect:glowstone_sword"}`; рабочие станции/tags: `["crafting_table"]`.

- Определение: `Swords_B/items/glowstone_sword.json`.
- Результаты рецептов: `Swords_B/recipes/glowstone_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[10].Mainhand[0].Name

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Светящиеся блоки и Glowstone Sword (`effect:glowstone_sword`)

[Полная сравнительная карточка 1.6/2.x](manual-heat-light-swords.md#glowstone-sword).

- `items/glowstone_sword.json`: damage 4, durability 128, enchantability 9/sword, `foil:true`, max stack 1, **allow_off_hand:true**; ремонт self 128, `minecraft:glowstone` 64, `minecraft:glowstone_dust` 16. On hurt entity — расход 1, web 15/bamboo 10. `recipes/glowstone_sword.json`: crafting_table, вертикаль `2/2/1`, 2 — glowstone, 1 — blaze_rod.
- `entities/player.json` проверяет наличие в `domain:hand`, затем `minecraft:glowstone_sword` выполняет две команды в кубе 3×3×3 от `~1 ~1 ~1` до `~-1 ~-1 ~-1`: заменить воздух на `effect99:lightblock`, затем заменить этот же блок на него же. Нет отдельной группы/события остановки по имени меча. Фактическую частоту и учёт обеих рук в domain `hand` надо измерить.
- `blocks/lightblock.json` и `lightblock2.json`: `geometry.null`, blend, коллизии размера `[0,0,0]`, destroy_time 0.1, explosion_resistance 999, absorption 0; заданные `block_light_emission` соответственно **1 и 0.5**. У обоих `minecraft:ticking` looping true, range `[0.2,0.2]`, событие выполняет `setblock ~ ~ ~ air 0`. Это исходные значения формата, а не доказанные уровни освещения и строгое время жизни на новом движке. Вызов fill заново заменяет существующий светоблок: сброс его таймера при этом нуждается в тесте. Блоки используют и другие мечи, поэтому их изменение глобально.

**Старая версия 1.6** (источник: `docs/manual-traces-1.6.md`):

- **Glowstone** — 6/128; три команды в порядке: поставить light_block data 15 на блок выше ближайшего игрока, заменить light_block 15 на air в кубе ±5 вокруг него, снова поставить блок на высоте +1, затем scoreboard. Удаление не различает исходное происхождение световых блоков. Аргумент `~~~` оставлен в оригинале.

**Дополнительный подробный разбор** (источник: `docs/manual-heat-light-swords.md`):

#### Glowstone Sword

**Предмет и рецепты.** Damage 6 → 4 (1.6 → 2.x), durability 128 в обеих; `allow_off_hand:true` указан в **обеих** версиях. В 1.6 `glint:true`, self repair 128; в 2.x `foil:true`, ремонт self 128, `minecraft:glowstone` 64, `minecraft:glowstone_dust` 16. В 1.6 рецепт pattern `020/020/010` задаёт key 2 = glowstone, 1 = blaze_rod, но **не задаёт символ 0**; нельзя молча считать его пустым слотом или исправлять. В 2.x рецепт использует `2/2/1` с теми же двумя ключами. Принимает ли конкретный движок исходный 1.6 pattern, из JSON не следует.

**1.6.** Player sensor создаёт `entity:glow`, controller `controller.animation.glow`. На каждом on_entry последовательно: `execute @p ~~~ fill ~ ~1 ~ ~ ~1 ~ light_block 15 replace air`; очистка куба `~5 ~5 ~5` … `~-5 ~-5 ~-5` командой `air 0 replace light_block 15`; снова первая команда и `@a swords 2`. Куб геометрически 11³ = 1331 позиция; очистка не различает световые блоки этого меча и заранее существовавшие подходящие блоки. `normal.mcfunction` также выполняет очистку light_block 15 около `@p`; нельзя гарантировать период, продолжительность или отсутствие взаимодействий других игроков.

**2.x.** Базовый hand-sensor вызывает `minecraft:glowstone_sword`, содержащий два `fill` куба ±1, сначала `effect99:lightblock 0 replace air`, затем `effect99:lightblock 0 replace effect99:lightblock`. В player нет одноимённой component group или отдельного stop-события. Блок `effect99:lightblock` в `blocks/lightblock.json`: `geometry.null`, материал blend, размеры entity/pick collision `[0,0,0]`, destroy_time 0.1, explosion_resistance 999, block_light_emission 1, absorption 0, ticking `looping:true, range:[0.2,0.2]`; event задаёт `setblock ~ ~ ~ air 0`. Это буквально записанные значения, не доказанное время жизни или освещённость. Другие цепочки тоже используют lightblock, поэтому не считать его частной визуальной частицей одного меча.

### Что написано на скриншотах

На изображении вручную считаны: damage = `4`; durability = `128`; enchantable = `true`; repairable = `true`. Оригинал: [скриншот 115902](https://drive.google.com/file/d/1bdPcV4MdHpWMaTX-HNVZZEjPZ7XbuusZ/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 17. Grass Sword — `effect:grass_sword`

**Кратко:** Трава и помощники, воздействующие на соседние сущности. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

**1.6** — определение `Sword_B/items/grass_sword.json`.
- урон: `8`; максимальная прочность: `{"max_durability":250}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `true`; размер стопки: `1`; свечение: не указан; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:grass_sword"]` → `250`.
- Оружейный компонент не указан.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**2.8.8 / 2.8.14** — определение `Swords_B/items/grass_sword.json`.
- урон: `8`; максимальная прочность: `{"max_durability":250}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `false`; размер стопки: `1`; свечение: `false`; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:grass_sword"]` → `250`.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 1.6:**

- Рецепт `Sword_B/recipes/grass_sword.json`; тип `minecraft:recipe_shaped`.
  - Схема сверху вниз: `F` / `F` / `E`.
  - Обозначения: `{"E":{"item":"minecraft:stick"},"F":{"item":"minecraft:grass"}}`.
  - Результат: `{"item":"effect:grass_sword"}`; рабочие станции/tags: `["crafting_table"]`.

- Определение: `Sword_B/items/grass_sword.json`.
- Результаты рецептов: `Sword_B/recipes/grass_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

**Архив 2.8.14:**

- Рецептов с этим точным результатом локально не найдено. Это не исключает других путей.

- Определение: `Swords_B/items/grass_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[23].Mainhand[0].Name
  - `Swords_B/structures/grass_sword.mcstructure` $.entities[0].Item.Name

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Grass Sword (`effect:grass_sword`)

[Цепь helper и общие теги](manual-grass-sword.md) · [условные пересечения type/family](grass-selector-samples.md).

- `items/grass_sword.json`: damage 8, durability 250, enchantability 9/sword, repair только self 250; on_hurt_entity — 1 durability, web 15/bamboo 10. Render offsets first `[0.8,0.15,-1.74]`, third `[0.69,2.5,-0.96]`.
- `player.json`: hand sensor, family `[player,grass_sword]`, looping timer `[0.2,0.2]`. При удержании удаляет tag `grass` у сущностей в кольце `rm=9,r=10`, заменяет dirt на grass в квадрате 5×5 y−1 и пытается заполнить воздух под условием grass в точке игрока `tallgrass 0`. Timer выполняет две `execute` для сущностей r=8 без player/item/entity:grass/xp_orb/arrow и tag grass; необходимо grass на `~ ~-0.1 ~`, а в точке цели air либо tallgrass. Вызов `summon entity:grass` следует за обоими detect: не всякая цель в радиусе выбирается автоматически.
- `entities/grass.json`: при spawn добавляется одноразовый таймер 1.08, звук, slowness 2 с amplifier 15 по `@e[type=!entity:grass,r=1]` (здесь игроки **не исключены**), и назначается tag grass сущностям поблизости кроме grass_witch, entity:grass, xp_orb и arrow. По таймеру команды выбирают ближайшего `c=1,r=1,tag=grass`, если под ним grass и в позиции air/tallgrass, и телепортируют вниз на 1; далее снимают tag grass со всех r=2 и добавляют timer 0.52 на despawn. При despawn выбор 50/100 поставить `tallgrass 0 replace air`, 50/100 ничего. Перекрывающиеся источники, тег и выбор ближайшего делают принадлежность к исходной цели неоднозначной.
- `entities/witch.json`: `minecraft:entity_spawned` выбирает default witch weight 80 или `minecraft:grass_witch` + `grass_witch` weight 20. Специальная группа family `[witch,monster,mob,grass_witch]`, health 32, follow_range 80, scale 1.1, on_death grass_sword. На on_death выбор 80 пусто/20 `structure load grass_sword`, `setblock ... double_plant 2`, звук. Доли 20/100 на выбор spawn и 20/100 на выбор смерти не следует без проверки перемножать в «шанс с любой ведьмы»: варианты создания, загрузка структуры и срабатывание on_death различаются. Специальная ведьма независимо запускает похожий поиск целей, но исключает family grass_witch и shulker_sword; `minecraft:environment_sensor` здесь имеет форму `triggers`, отличную от массива on_environment в других сущностях — интерпретацию/частоту проверить.

**Старая версия 1.6** (источник: `docs/manual-traces-1.6.md`):

#### Grass Sword: 1.6 и теги 2.x

[Глобальные команды 1.6, ловушка 2.x и условные пересечения](manual-grass-sword.md) · [таблица селекторов](grass-selector-samples.md).

**Дополнительный подробный разбор** (источник: `docs/manual-grass-sword.md`):

### Grass Sword: глобальная трава 1.6 и общие теги 2.x

Статическое чтение архивов; [таблица тип/family/tag](grass-selector-samples.md) демонстрирует только условные совпадения селекторов. Частота сенсоров и таймеров, разрешение legacy-команд и реальный выбор сущности/блоков не проверены в Minecraft.

#### Общие предмет и получение

`effect:grass_sword` в обеих версиях объявляет damage **8**, max durability **250**, self-repair **250**, max stack **1**, enchantable `{value:9,slot:sword}`, hand_equipped true, can_destroy_in_creative false, digger web **15**/bamboo **10**, use_efficiency true. Off-hand **true** в 1.6 и **false** в 2.x; в 2.x `on_hurt_entity` запускает weapon event с durability damage **1**. PNG 1.6 **16×16**, 2.x **32×32**; хотя ID одинаковый, это разные размеры ([аудит](icon-comparison.md)).

В 1.6 shaped recipe для crafting_table: `F / F / E`, F=`minecraft:grass`, E=`minecraft:stick`, результат `effect:grass_sword`. Разрешение старого блока-ингредиента и регистрация не проверены. В 2.x локальный рецепт, прямой loot и торговля для ID не обнаружены; есть сохранённая структура предмета и armor stand ([получение](acquisition-index-2.8.14.md#effectgrass_sword)).

#### 1.6: один helper и все игроки

Sensor `has_equipment`, self, domain hand, value `effect:grass_sword` вызывает event `minecraft:grass_sword`; он добавляет группу со spawn `entity:grass`, min/max wait **0/0**, num_to_spawn **1**, single_use true. Общая ветвь `minecraft:event_normal_player` её удаляет, поэтому число spawn и частота не доказаны. В 1.6 этот `entity:grass` — helper family `despawnear`, health 1, collision 0×0, fire_immune true и physics `{}`, а не helper с другой реализацией в 2.x. Animation `grass` указывает на `controller.animation.grass`; default и grass переходят друг в друга по `(1.0)` и имеют одинаковые четыре строки on_entry.

1. `/execute @a ~ ~ ~ detect ~ ~ ~ air 0 fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 grass 0 replace dirt` — для **всех выбранных игроков**, у кого detect air, плоскость y−1 **5×5 = 25** позиций. Слово `dirt` после replace здесь без указанного data; число фактических замен зависит от мира и двигателя.
2. `/execute @a ~ ~ ~ detect ~ ~-1 ~ grass 0 fill ~ ~ ~ ~ ~ ~ tallgrass 0 replace air` — опять все игроки с grass 0 под ними, не только владелец.
3. `/execute @e[r=10] ~ ~ ~ detect ~ ~-1 ~ grass 0 fill ~ ~ ~ ~ ~ ~ tallgrass 0 replace air` — selector относительно helper, без явно перечисленных исключений type/family; при допустимых условиях может включать различные виды сущностей и игроков, но движковые ограничения надо проверить.
4. `/scoreboard players set @a swords 2` — глобальный для выбранных игроков счётчик.

Выполнение одной команды на разных выбранных сущностях, пересечения областей и существующие блоки делают результат зависимым от порядка и состояния мира. Это не декларация механизма ловушки 2.x.

#### 2.x: создание helper и общий tag

Предметы, `entities/grass.json`, `entities/witch.json` и структура grass_sword совпадают побайтово между 2.8.8/2.8.14; соответствующие ветви player совпадают структурно, хотя целый player.json различается в Ice.

Player sensor удержания добавляет `minecraft:grass_sword` с family `[player,grass_sword]` и looping timer `[0.2,0.2]` → `grass_sword_skills`. Отдельный шаг события содержит в исходном порядке: `tag @e[tag=grass,rm=9,r=10] remove grass`; `fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 grass 0 replace dirt`; detect grass 0 ниже `@s` и заполнение текущей точки tallgrass 0 с `replace air`. Первая команда снимает одноимённый тег у подходящих **любых** сущностей в кольце, не только созданных данным игроком. Stop при family `grass_sword` снимает группу и добавляет default_player. Реальная частота и одновременные вызовы не следуют автоматически из timer.

При timer-event player две команды ищут `@e[type=!player,type=!item,type=!entity:grass,type=!xp_orb,type=!arrow,r=8,tag=!grass]`: detect grass 0 на `~ ~-0.1 ~`, затем detect в позиции цели **air 0** или **tallgrass 0**, соответственно `summon entity:grass`. Это два вложенных detect, а не гарантия spawn для каждого выбранного типа. Синтаксис с дробной координатой и скорость событий проверить в движке.

Grass Witch использует похожие две команды в `grass_witch_skill`, но selector другой: `family=!grass_witch`, `family=!shulker_sword`, `type=!item,!entity:grass,!xp_orb,!arrow`, `r=8,tag=!grass`. Он **не содержит `type=!player`**. У специальной группы witch environment_sensor задан как `triggers:[{filters:{},event:"grass_witch_skill"}]`: пустой filters и формат triggers не доказывают, когда или как часто он сработает.

#### Что делает `entity:grass` 2.x

Entity family `[effect99_entities]`, collision 0×0, damage_sensor cause all/deals_damage false, physics gravity/collision false, pushable и piston false. Его `minecraft:entity_spawned` указывает группу timer `[1.08,1.08]`, looping false, и список команд: sound `dig.grass`, `effect @e[type=!entity:grass,r=1] slowness 2 15 true`, затем назначение tag grass через `@e[family=!grass_witch,type=!entity:grass,type=!xp_orb,type=!arrow,r=1,tag=!grass]`. В **этом** selector назначения тега нет исключений `type=!player` и `type=!item`, хотя они есть у поиска player. Slowness отдельно исключает только type helper и не требует tag.

Timer-event `grass_sword_skill` содержит два `execute` для `@e[type=!entity:grass,c=1,r=1,tag=grass]`, далее два detect: grass 0 снизу `~ ~-1 ~`, затем в позиции air 0 либо tallgrass 0; при прохождении — `tp @s ~ ~-1 ~`. После этих строк указан `tag @e[tag=grass,r=2] remove grass`, без привязки тега к создателю. В том же объекте события объявлено add группы `start_despawn` с timer `[0.52,0.52]`, looping false. Относительный порядок `run_command` и `add` в одном объекте отдельно не установлен; не считать строго доказанным расписанием **1.08 + 0.52** до удаления.

`c=1` означает ограничение числа выбранных целей, но порядок выбора, идентичность этой сущности в двух отдельных командах и возможное совпадение с исходной целью требуется испытать. Selector для телепорта **не исключает player, item, arrow или xp_orb**; он требует tag, который мог быть назначен другим механизмом или прежним вызовом. Обе команды выполняют собственный выбор. Снятие tag в r=2 и player-очистка в кольце 9…10 не различают авторство, поэтому несколько helper/игроков/ведьм могут конфликтовать при выполнении одновременно. Это риск, а не доказанный сценарий телепорта конкретного игрока.

При `despawn` sequence сначала add группы despawn, затем randomize **50**: `fill ~ ~ ~ ~ ~ ~ tallgrass 0 replace air`, **50**: пусто. При обычном взвешивании 50/100 — условная доля ветви события, не гарантированный шанс травы в мире; состояние блока, успешность команд и время despawn остаются неизвестными.

#### Type не равен family: показательные пересечения

[Таблица](grass-selector-samples.md) сравнивает условия без имитации радиуса, detect и ограничения `c=1`:

- В модели обычный `type=player` не проходит поиск player из-за `type=!player`, но может пройти поиск witch и назначение tag helper, если выполняет остальные условия. Срабатывание, наличие игрока в радиусе и способность назначить ему tag нужно проверить.
- Player с полной Wolf family `[wolf,wolf_sword,complete_wolf_transformation,monster]` всё равно остаётся **type player** в этой условной модели; отсутствие family `player` не превращает его в иной type. Поиск player всё равно исключает `type=player`.
- `entity:shulker_shield` объявляет family `[effect99_entities,player,shulker_sword]`, но его **type — отдельный** `entity:shulker_shield`: он может пройти только текстовые type-условия поиска player, тогда как поиск witch исключает family `shulker_sword`. Это не подтверждение физической совместимости или spawn.
- Специальная Grass Witch family `[witch,monster,mob,grass_witch]` исключена из поиска witch и назначения tag, но текст поиска player её отдельно не исключает. Снятие существующего tag r=2/кольцо не ограничено family.
- Item исключён из обоих первичных поисков, но не исключён из назначения tag при spawn helper. Arrow исключён из первичных поисков и назначения tag, но если tag уже был назначен извне, selector `c=1` его явно не исключает. Другие условия всё равно обязательны.

#### Ведьма и условная модель выдачи

`minecraft:entity_spawned` witch выбирает weight **80** default или **20** add обеих групп `minecraft:grass_witch` и `grass_witch`. Последняя задаёт variant 1 через другую группу, family `[witch,monster,mob,grass_witch]`, health **32/32**, follow_range **80**, scale **1.1**, `minecraft:loot:{}` и on_death `grass_sword`. У death-event randomize **80** пусто / **20**: `structure load grass_sword ~~~`, `setblock ~ ~ ~ double_plant 2`, `playsound dig.grass @a[r=12] ~~~`. Эти три строки и старую запись `~~~` сохранять без предположения об успешном исполнении.

Структура `grass_sword.mcstructure` 1×1×1 содержит одну entity `minecraft:item` с `Item.Name=effect:grass_sword`, Count **1**, Damage **0**, `Age:196s` и пустым `Tags:[]`; точная сериализация и origin — в [SNBT](structures-2.8.14.md). Наличие этих данных не доказывает успешную выдачу, время существования или перерасчёт координат при загрузке.

Если условно оба выбора работают с весами 20/100, независимы, специальная группа получена именно через указанную ветвь spawn и затем выполняется её on_death, вероятность выбора **обеих ветвей** равна `0.2 × 0.2 = 4%`. Это не шанс выпадения с любой ведьмы: специальные группы можно добавлять отдельным event, а гибель, команды, структура и наличие предмета требуют отдельной проверки. Факт существования 2-х вариантов client witch также не определяет их выбор конкретным движком ([аудит пакетов](manual-package-identities.md)).

### Что написано на скриншотах

На изображении вручную считаны: damage = `8`; durability = `250`; enchantable = `true`; repairable = `true`. Оригинал: [скриншот 115858](https://drive.google.com/file/d/1fvRODDZrL5CDlRdyvi4iuqupiY0pkRmc/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 18. Ice Sword — `effect:ice_sword`

**Кратко:** Замораживание области, лёд под игроком и снежки. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

**1.6** — определение `Sword_B/items/ice_sword.json`.
- урон: `11`; максимальная прочность: `{"max_durability":500}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `true`; размер стопки: `1`; свечение: не указан; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:ice_sword"]` → `500`.
- Оружейный компонент не указан.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**2.8.8 / 2.8.14** — определение `Swords_B/items/ice_sword.json`.
- урон: `8.5`; максимальная прочность: `{"max_durability":500}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: `{"category":"ice_sword","duration":5}`; левая рука: `false`; размер стопки: `1`; свечение: `true`; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:ice_sword"]` → `500`; `["minecraft:ice"]` → `55`.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`; событие без нанесения урона существу → `{"event":"weapon"}`; удар по блоку → `{"event":"weapon"}`.
- При использовании предмета указано: `{"on_use":{"event":"on_use"}}`.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 1.6:**

- Рецепт `Sword_B/recipes/ice_sword.json`; тип `minecraft:recipe_shaped`.
  - Схема сверху вниз: `F` / `F` / `E`.
  - Обозначения: `{"E":{"item":"minecraft:stick"},"F":{"item":"minecraft:blue_ice"}}`.
  - Результат: `{"item":"effect:ice_sword"}`; рабочие станции/tags: `["crafting_table"]`.

- Определение: `Sword_B/items/ice_sword.json`.
- Результаты рецептов: `Sword_B/recipes/ice_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

**Архив 2.8.14:**

- Рецептов с этим точным результатом локально не найдено. Это не исключает других путей.

- Определение: `Swords_B/items/ice_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - `Swords_B/loot_tables/chests/igloo_chest.json` $.pools[0].entries[6]: `{"type":"item","name":"effect:ice_sword","weight":1}`
  - `Swords_B/loot_tables/chests/village/village_snowy_house.json` $.pools[0].entries[9]: `{"type":"item","weight":4,"functions":[{"function":"minecraft:set_count","count":{"min":1,"max":1}}],"name":"effect:ice_sword"}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[26].Mainhand[0].Name

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

**Условная математическая модель выбора loot в 2.x:**

Числа ниже — вероятность выбрать хотя бы одну запись предмета внутри уже активированного пула, а не шанс реальной добычи. Допущения: все записи доступны; отсутствующий вес принят за 1; quality и условия записей игнорируются; выборы независимы с возвращением; число rolls равномерно в указанном диапазоне. Условия пула считаются уже выполненными. Загрузка таблицы, дополнительный отбор, количество предметов и функции не эмулируются.

- Таблица/пул: `chests/igloo_chest.json` / 0; entries: 6; rolls: `{"min":2,"max":8}`; вес ID/сумма: 1/64; выбор хотя бы одной записи по модели: **7.5263%**. Условия и оговорки: functions: не задано.
- Таблица/пул: `chests/village/village_snowy_house.json` / 0; entries: 9; rolls: `{"min":3,"max":8}`; вес ID/сумма: 4/57; выбор хотя бы одной записи по модели: **32.4613%**. Условия и оговорки: 4 отсутствующих weight → 1 в модели; другие поля таблицы: `{"type":"minecraft:chest"}`; functions: `[{"function":"minecraft:set_count","count":{"min":1,"max":1}}]`.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Ice Sword (`effect:ice_sword`)

[Все 40 fill, геометрия и пересечение общего selector с player](manual-ice-geometry-2.8.md).

- `Swords_B/items/ice_sword.json`: damage 8.5; max durability 500; cooldown category `ice_sword`, duration 5. При on_use — команды заполнения, затем damage durability 6. `weapon` вызывается тремя хуками; сначала durability 1, затем ветвь 70 пустая или 30 — снежок `minecraft:snowball`, launch_power 1 и звук `random.bow` для `@a[r=10]`, громкость 1, pitch 0.4 (`:141–170`).
- `:85–124`: использованы многочисленные старые `execute ... fill` с *разными* селекторами и объёмами: например, для большинства целей `rm=2,r=12`, для игроков `rm=3,r=12`, отдельные формы для slime, ghast, horse и др. Заполняется только воздух, а часть команд затем вырезает внутреннюю полость; порядок команд и перекрытие селекторов важны. Для ghast внешний объём от `~4 ~-3 ~4` до `~-4 ~4 ~-4`, затем очистка от `~3 ~-2 ~3` до `~-3 ~3 ~-3`. Все команды приведены в [карточке](items-2.8.14.md); не заменять одним радиальным алгоритмом без тестов.
- `player.json:752–763,1920–1959`: при наличии в `hand` выполняется событие игрока. Ветвь lava и biome tag != nether — звук, `setblock ~ ~ ~ flowing_water`, удаление предмета из mainhand через `replaceitem`, частицы; если lava и biome tag nether — те же действия без создания воды. Отдельно команды заменяют воду/flowing_water на `frosted_ice`: квадрат x/z -2…2 на y-1 и по одному блоку на четырёх осях с расстоянием 3. Последняя команда выбирает `@e[r=64,type=!player]`, обнаруживает лёд и выполняет старый `tp @s ~ ~ ~ ~1`. Эффекты, интервалы и кратность зависят от environment sensor; не считать шаги выполняющимися один раз только при взятии в руку.
- На [скриншоте](https://drive.google.com/file/d/18mrcZhBh-Z3MbkF1Su19Yu7C9HNa31zs/view) утверждаются радиус 8 и превращение меча в воду при горении. В коде конкретного архива большинство селекторов использует r=12 и проверяется **in_lava**, а не просто состояние огня. Описание может относиться к другой сборке. В архиве 2.8.8 используется `effect99:fake_ice`; здесь `frosted_ice`: время таяния не доказано константой 8 секунд. Не смешивать варианты.

**Старая версия 1.6** (источник: `docs/manual-traces-1.6.md`):

#### Ice Sword 1.6: подробная цепочка

[Предмет, helper, 26 команд и сравнение с 2.x](manual-ice-1.6.md) · [22 типа целей и геометрия](ice-target-matrix-1.6.md). Выписка остаётся статической: порядок работы сенсоров, состояний и legacy-команд требует проверки в игре.

**Дополнительный подробный разбор** (источник: `docs/manual-ice-geometry-2.8.md`):

### Ice Sword 2.x: геометрия 40 команд и пересечения целей

[Таблица всех 40 fill в исходном порядке](ice-geometry-index.md) формируется из item JSON и сохраняет полный selector, смещение `execute`, углы fill, фильтр замены и объём рамки. В 2.8.8 вместо `frosted_ice` указан `effect99:fake_ice`; это не просто визуальный вариант, поскольку обработка блока отличается ([разбор 2.8.8](manual-version-2.8.8.md)). Расчёты ниже относятся к геометрии относительных целочисленных координат, **не** к доказанному количеству блоков, расходу прочности или работоспособности команд.


#### Практическая проба 2.8.8

В Bedrock 1.20.50.03 применение к зафиксированной эффектом замедления свинье создало вокруг неё 17 блоков fake_ice в наблюдавшемся объёме из 18 позиций; контрольный камень в нём не заменился. Прочность меча уменьшилась на 6. Лёд последовательно прошёл состояния 1, 2, 3 и 4 и исчез примерно через 8 секунд; наблюдение проводилось каждые 5 тиков, поэтому точную длительность и моменты переходов не измеряли. Реальное удержание движущейся цели, другие сущности и 2.8.14 не проверены. [Условия и журнал](../data/original-mechanics-2026-11-07/README.md).

#### Общий порядок

`items/ice_sword.json`: `minecraft:on_use` вызывает item event `on_use`. В его sequence первым шагом `run_command` с `target:holder` перечисляет **40** старых `execute @e[...] ... fill` в порядке таблицы, затем `title @s actionbar §l§bIce Skill`, `playsound random.fizz @a[r=12] ~ ~ ~ 1 2.3`, `particle minecraft:knockback_roar_particle ~ ~1 ~`; вторым шагом указан durability damage **6**, target self. Влияние неуспешной команды, порядков исполнения и target нужно испытать, а не считать безусловным успешным замораживанием.

#### Возможное пересечение общего и player-селектора

Первая команда выбирает `@e` с большим списком `type=!…`, `family=!fish`, `family=!effect99_entities`, `rm=2,r=12`. В ней **нет `type=!player`**. Последняя из 40 отдельно выбирает `@e[type=player,rm=3,r=12]`; обе строят 3×4×3 рамку (`x/z ±1`, `y −1…+2`) с `replace air 0`.

При обычном понимании селекторов подходящий игрок в общем диапазоне и с допустимыми family может попасть в первую команду; при подходящем `rm=3,r=12` — потенциально и в обе. Игроки на расстояниях между порогами 2 и 3 могут подходить только первому условию, если движок принимает остальные аргументы. Это **не** доказательство, что дважды появятся блоки: команды последовательны, вторая заменяет только air, положения могут измениться, а `rm`/r, повторные type-фильтры, вычисление позиций и дробные координаты нужно проверить. Не считать 3 безусловным минимальным расстоянием воздействия на игроков.

Общий selector исключает тип `slime`, но отдельные команды выбирают `family=slime_large`, `slime_medium`, `slime_small`, без отдельного `type=slime`: предполагаемое соответствие family конкретному виду требует проверки. Остальные перечисленные типы и исключения сохранены буквально в индексе; не заменять их словами «все мобы» или «только враги».

#### Формы для отдельных целей

| Цель и номера fill | Внешняя рамка | Последующее вырезание | Геометрическая разность при общем центре и полном совпадении |
|---|---:|---:|---:|
| Общая / player №1/40 | 3×4×3 = 36 | нет | 36 |
| Enderman №2 | 3×5×3 = 45 | нет | 45 |
| `family=slime_large` №3–4 | 5×5×5 = 125 | 3×3×3 = 27, `execute ~ ~1 ~` | 98 |
| `family=slime_medium` №5–6 | 3×3×3 = 27 | 1 | 26 |
| `family=slime_small` №7–8 | 3×3×3 = 27 | 1 | 26 |
| Ghast №36–37 | 9×8×9 = 648 | 7×6×7 = 294 | 354 |
| Horse №38–39 | 3×3×3 = 27 | 1 | 26 |

Для остальных строк отдельно заданы одноточечные рамки либо 3×3×3; Elder Guardian №34 также 5×5×5 без последующего вырезания. Размеры и номера берутся из исходного порядка, не из внешнего описания радиуса.

Внешние команды создают ледяной блок **только вместо `air 0`**, а команды полостей заменяют соответствующий лёд на `air`. Поэтому разность столбцов — только величина, получаемая при идеализированном заполнении всей внешней рамки, совпадении центров и успешной очистке. Очистка может затронуть ранее существовавший `frosted_ice`/`fake_ice`, не только поставленный текущим вызовом; при отсутствии воздуха, столкновении нескольких целей или ограничении чанков фактические результаты отличаются. Некоторые команды очистки указывают data 0 после блока-фильтра, другие не указывают; таблица сохраняет это различие буквально.

#### Связанные, но отдельные механики

В weapon-event объявлен расход 1 и выбор 70 пусто/30 snowball; это другой триггер, не те же 40 команд on-use. Player-событие удержания содержит преобразование воды под игроком и ветви реакции на `in_lava`, а не только на горение; ещё `tp` non-player r=64 при проверке льда. Эти команды и их конфликты рассмотрены в [карточке Ice](manual-traces-2.8.14.md#ice-sword-effectice_sword). Точечный опыт выше не устанавливает общий радиус или длительность для других целей и версий.

**Дополнительные детали 1.6** (источник: `docs/manual-ice-1.6.md`):

### Ice Sword 1.6: предмет, помощник и отличие от 2.x

Это статическая реконструкция из архива `SwordsAndMoreSwords.1.6.mcaddon`. Полный порядок 22 команд fill по целям, формы и потенциальные соответствия 2.x — в [матрице целей](ice-target-matrix-1.6.md); все 40 более поздних fill — в [матрице 2.x](ice-geometry-index.md). Название архива не является гарантией версии игры; ни один вывод ниже не проверен запуском Bedrock.

#### Предмет и получение

`Sword_B/items/ice_sword.json`, ID `effect:ice_sword`: `format_version` **1.20.20**, max stack **1**, damage **11**, max durability **500**, off-hand `true`, hand-equipped `true`, can-destroy-in-creative `false`, enchantable `{value:9,slot:sword}`. Самим `effect:ice_sword` задан repair_amount **500**; `minecraft:ice` в списке ремонта 1.6 отсутствует. Digger: web speed **15**, bamboo **10**, `use_efficiency:true`. Эти декларации не гарантируют фактическое значение удара, работу ремонта или переноса в новую версию.

`Sword_B/recipes/ice_sword.json` — crafting_table, вертикальный pattern `F / F / E`: два `minecraft:blue_ice` над `minecraft:stick`, результат `effect:ice_sword`. Прямых записей этого ID в локальных loot, trade или структурах 1.6 не найдено; это не доказательство невозможности других путей. В 2.x локального рецепта этого результата не найдено, но есть записи в igloo и snowy village chest. Точные локальные связи: [1.6](acquisition-index-1.6.md#effectice_sword) и [2.8.14](acquisition-index-2.8.14.md#effectice_sword).

Клиентский item задаёт icon `ice_sword`, render_offsets `miscellaneous`; `en_US.lang`: `§l§bIce Sword`. Исходный PNG 16×16 совпадает побайтово со значком 2.8.14 ([аудит](icon-comparison.md)); это не доказывает одинаковый рендер в разных движках.

#### Удержание → helper → контроллер

1. `Sword_B/entities/player.json`: environment_sensor с `has_equipment`, subject self, domain `hand`, value `effect:ice_sword` вызывает `minecraft:ice_sword`. Толкование `hand`/off-hand и частота обработки в движке не установлены.
2. Событие **добавляет** группу `minecraft:ice_sword`. В ней `minecraft:spawn_entity`: `entity:ice`, min/max wait **0/0**, num_to_spawn **1**, `single_use:true`.
3. В том же player есть другой sensor по family `player`, вызывающий `minecraft:event_normal_player`; он удаляет в том числе группу `minecraft:ice_sword`. Относительный порядок и повторный spawn при добавлении/удалении группы не доказаны; нельзя обещать одного helper за всё удержание или одну команду за тик. Подробнее — [общее состояние 1.6](manual-global-state-1.6.md).
4. `Sword_B/entities/ice.json`: identifier `entity:ice`, spawnable **false**, summonable **true**, experimental **false**, family `[despawnear]`, `minecraft:despawn` с фильтром self family `despawnear`, health **1**, collision width/height **0/0**, fire_immune **true**, physics `{}`. Явного времени жизни здесь нет; не предполагать, что helper привязан к игроку или исчезает немедленно. В локальных ресурсах не найден client entity с ID `entity:ice`; это не доказывает, как именно движок покажет или загрузит helper.
5. Его scripts animate `ice` → `controller.animation.ice` из `Sword_B/animation_controllers/ice_sword.json`. `default` переходит в `ice` с выражением `(1.0)` и в `on_entry` содержит буквально `/Effect99`; `ice` переходит в `default` тоже с `(1.0)`. Не подменять неизвестную команду `/Effect99` функцией и не считать расписание переходов, успех команд и сохранение helper установленными.

#### Состояние `ice`: 26 записей

- №1–2: `/execute @a ~ ~ ~ detect ~ ~ ~ air 0 fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 ice 0 replace water 0` и аналог для `flowing_water 0`. Это две рамки по **25** позиций на уровне y−1 относительно **каждого** выбранного игрока с detect air в позиции; это не только владелец меча. Команды заменяют только указанные water/flowing_water data 0, а не любую воду. При нескольких helper воздействие на всех игроков может повторяться.
- №3–16 и №18–25: **22** конкретных type-селектора с `rm=5,r=12` относительно контекста helper; 22 рамки создаются вокруг соответствующих целей заменой `air 0` на `ice 0`. Среди необычных целей есть `evocation_fang` и `tnt`. Все типы и координаты — в [матрице](ice-target-matrix-1.6.md). Например, Enderman — 3×5×3 = **45**, Ravager — 5×4×5 = **100**, Silverfish — 3×3×3 = **27**, большинство перечисленных — 3×4×3 = **36**. Это геометрические рамки при целочисленных относительных координатах, а не гарантированное число изменённых блоков.
- №17, после fill по slime: `/execute @e[r=12,rm=5,type=slime] ~ ~ ~ detect ~ ~ ~ ice 0 tp @s ~ ~ ~`. Декларация направлена на slime, у которого detect проходит; не приписывать ей смену ориентации или доказанное изменение позиции.
- №26: `/scoreboard players set @a swords 2`. Это глобальное изменение для выбранных игроков, не только держателя. Зависимости других помощников и `normalft` — в [глобальной трассе](manual-global-state-1.6.md).

Радиусы, порядок и наличие data 0 приведены буквально; рамки целей могут пересекаться друг с другом и с блоками мира. `replace air 0` не создаёт полость, как некоторые более поздние команды. Нельзя по одной выписке установить порядок исполнения команд между разными сущностями, условия despawn или реальный результат при дробных координатах.

#### Сравнение с 2.x: одинаковый ID, другой механизм

| Аспект | 1.6 | 2.8.8 / 2.8.14 |
|---|---|---|
| Damage / durability | 11 / 500 | 8.5 / 500 |
| Off-hand | true | false |
| Ремонт | собственным мечом 500 | собственным мечом 500; `minecraft:ice` 55 |
| Активная способность | здесь обнаружена цепь через player sensor и helper controller | item `on_use`, cooldown duration 5, отдельная декларация durability damage 6 |
| Обычное попадание/блок | в item нет декларации item `minecraft:weapon` | три hook вызывают weapon event: 1 durability, ветви 70 пусто / 30 snowball; вероятности условны по весам и выполнению hook |
| Замораживание воды | `@a`, detect air; 5×5, только water и flowing_water data 0; лёд `ice` | player event, 5×5 плюс 4 осевые позиции на расстоянии 3 = 29 геометрических позиций; без этого detect air; в 2.8.8 fake ice, в 2.8.14 frosted ice |
| Цели | 22 отдельных type, rm=5/r=12 от helper | общий selector плюс индивидуальные типы и slime families; в основном rm=2/r=12 от holder, отдельный player rm=3/r=12 |
| Slime | одна рамка 3×4×3, затем detect/`tp @s ~ ~ ~` | разные family и рамки с очисткой; отдельный player-event содержит non-player r=64 detect и `tp @s ~ ~ ~ ~1` |
| Рецепт/loot | вышеуказанный shaped рецепт; локальных прямых loot-записей не найдено | локального shaped-рецепта для этого результата не найдено; две chest-таблицы ниже |

Сопоставление потенциальных типов — не доказательство эквивалентности: различны центр, условие вызова, семейства, материал и дополнительные действия. Например, геометрия Silverfish в 1.6 — 27 позиций, а отдельная команда 2.x — 1; Ravager в 1.6 — 100, потенциальный общий selector 2.x — 36 при соблюдении family-фильтров. Ни одна величина не равна автоматически числу новых ледяных блоков.

#### Условная оценка записей chest loot 2.x

Локальные таблицы igloo и snowy village одинаковы побайтово в 2.8.8/2.8.14. Это только модель, **не проверенная вероятность сундука в игре**: предположим, что таблица выбрана движком и предмет зарегистрирован; отсутствующий `weight` равен 1; целое число rolls выбирается равномерно включая концы; выборы независимы, с возвращением и без модификаторов весов. При иных правилах результаты изменятся.

| Таблица / pool | Rolls | Вес меча / сумма весов при предположении | Модель на один выбор | Модель ≥1 меча в этом pool |
|---|---:|---:|---:|---:|
| `chests/igloo_chest.json`, pool 0 | 2…8 | 1 / 64 | 1.5625% | ≈7.5263% |
| `chests/village/village_snowy_house.json`, pool 0 | 3…8 | 4 / 57 | ≈7.0175% | ≈32.4613% |

Формула последнего столбца: среднее `1 − (1 − вес/сумма)^n` по указанным целым n. Во втором pool igloo отдельно записан один golden apple; он не включён в сумму весов первого pool. Snowy entry явно задаёт count min/max 1/1. Условная модель не учитывает существование и генерацию структур, совместимость пакета, фактическое применение таблиц и возможные правила движка.

### Что написано на скриншотах

На изображении вручную считаны: damage = `8.5`; durability = `500`; enchantable = `true`; repairable = `true`. Оригинал: [скриншот 115821](https://drive.google.com/file/d/18mrcZhBh-Z3MbkF1Su19Yu7C9HNa31zs/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 19. Jungle Sword — `effect:jungle_sword`

**Кратко:** Лианы и размещение саженца; также есть путь через рыбалку. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

**1.6** — определение `Sword_B/items/jungle_sword.json`.
- урон: `4`; максимальная прочность: `{"max_durability":128}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `true`; размер стопки: `1`; свечение: не указан; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:jungle_sword"]` → `128`.
- Оружейный компонент не указан.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**2.8.8 / 2.8.14** — определение `Swords_B/items/jungle_sword.json`.
- урон: `4`; максимальная прочность: `{"max_durability":128}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `false`; размер стопки: `1`; свечение: `false`; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:jungle_sword"]` → `128`.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 1.6:**

- Рецепт `Sword_B/recipes/jungle_sword.json`; тип `minecraft:recipe_shaped`.
  - Схема сверху вниз: `F` / `F` / `E`.
  - Обозначения: `{"E":{"item":"minecraft:sapling","data":3},"F":{"item":"minecraft:leaves","data":3}}`.
  - Результат: `{"item":"effect:jungle_sword"}`; рабочие станции/tags: `["crafting_table"]`.

- Определение: `Sword_B/items/jungle_sword.json`.
- Результаты рецептов: `Sword_B/recipes/jungle_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

**Архив 2.8.14:**

- Рецептов с этим точным результатом локально не найдено. Это не исключает других путей.

- Определение: `Swords_B/items/jungle_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - `Swords_B/loot_tables/chests/jungle_temple.json` $.pools[0].entries[8]: `{"type":"item","name":"effect:jungle_sword","weight":16}`
  - `Swords_B/loot_tables/gameplay/fishing/treasure.json` $.pools[0].entries[4]: `{"type":"item","name":"effect:jungle_sword","weight":5}`
    - Родитель: `Swords_B/loot_tables/gameplay/fishing.json` $.pools[0].entries[1] `{"type":"loot_table","name":"loot_tables/gameplay/fishing/treasure.json","weight":5,"quality":2}`
    - Родитель: `Swords_B/loot_tables/gameplay/jungle_fishing.json` $.pools[0].entries[1] `{"type":"loot_table","name":"loot_tables/gameplay/fishing/treasure.json","weight":5,"quality":2}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[25].Mainhand[0].Name

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

**Условная математическая модель выбора loot в 2.x:**

Числа ниже — вероятность выбрать хотя бы одну запись предмета внутри уже активированного пула, а не шанс реальной добычи. Допущения: все записи доступны; отсутствующий вес принят за 1; quality и условия записей игнорируются; выборы независимы с возвращением; число rolls равномерно в указанном диапазоне. Условия пула считаются уже выполненными. Загрузка таблицы, дополнительный отбор, количество предметов и функции не эмулируются.

- Таблица/пул: `chests/jungle_temple.json` / 0; entries: 8; rolls: `{"min":2,"max":6}`; вес ID/сумма: 16/457; выбор хотя бы одной записи по модели: **13.1758%**. Условия и оговорки: functions: не задано.
- Таблица/пул: `gameplay/fishing/treasure.json` / 0; entries: 4; rolls: `1`; вес ID/сумма: 5/41; выбор хотя бы одной записи по модели: **12.1951%**. Условия и оговорки: functions: не задано.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Jungle Sword (`effect:jungle_sword`)

[Порядок 148 проверок, источники и условный приоритет](manual-jungle-vines.md) · [таблица block/data](jungle-vine-index.md).

- `items/jungle_sword.json`: damage 4, durability 128, enchantability 9/sword, repair self 128, offhand false, on_hurt_entity 1 durability, web 15/bamboo 10. `block_placer` ставит `effect99:sapling3` на dirt/grass; `blocks/sapling3.json` имеет on_placed со звуком и `fill ~ ~ ~ ~ ~ ~ sapling 3`, а не прямое описание дерева. Расход предмета/прочности при размещении и рост саженца нужно проверить; отсюда не следует гарантированное взрослое дерево.
- `player.json`: группа family `[player,jungle_sword]`, `minecraft:health {value:8,max:8}`, при удержании `effect @s absorption 1 2 true` и вызов функции jungle_sword; при снятии удаляет группу, добавляет default_player и `effect @s absorption 0`. Поведение текущего здоровья и возврата max health при замене групп не определено одним JSON.
- `functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction`: 148 строк старых `execute @p ... detect` для конкретных соседних блоков и data; при совпадении в позиции `~ ~1 ~` ставится vine data 8/2/1/4 с `replace air`. Порядок строк важен: после первого успешного заполнения последующие replace air могут не сработать. `@p` выбирается относительно контекста функции, а не явно `@s`; возможен выбор другого игрока. `entities/parrot.json` содержит `minecraft:behavior.tempt` с items `[effect:jungle_sword]` и speed_multiplier 1.0.
- `loot_tables/chests/jungle_temple.json`: weight 16 из 457, 2–6 rolls. `loot_tables/gameplay/fishing/treasure.json`: weight 5 из 41, 1 roll внутри treasure pool; это **не** доля от всех рыбацких забросов и сама таблица не содержит биомного фильтра. Условие попадания в treasure и ванильная привязка/биом проверяются отдельно.

##### Дополнение к Jungle Sword: вложенные таблицы рыбалки

`loot_tables/gameplay/fishing.json` **и** `jungle_fishing.json` обе ссылаются на один `fishing/treasure.json`: в каждой родительский пул выбирает junk weight 10/quality −2, treasure 5/quality 2, fish 85/quality −1, 1 roll. Меч имеет 5/41 уже внутри treasure. При нулевом влиянии quality и стандартной независимой семантике это произведение 5/100 × 5/41 = 25/4100 на проход через соответствующую родительскую таблицу, но luck/quality, способ выбора таблицы биомом и запуск в движке необходимо проверять; по исходному коду это не доказанная частота любого заброса. Описание «только джунгли» не подтверждается наличием меча только в jungle-пуле.

**Старая версия 1.6** (источник: `docs/manual-traces-1.6.md`):

#### Jungle: сопоставление 1.6 и 2.8.14

[Полный порядок пар block/data, условный приоритет и получение](manual-jungle-vines.md) · [индекс 36/37 групп](jungle-vine-index.md).

Текст `controller.animation.jungle.states.jungle.on_entry` 1.6 содержит 145 записей: 144 команды `execute @p ... detect ... fill ... vine ... replace air` и финальное `scoreboard players set @a swords 2`. В `states.default.on_entry` остаётся буквальная `/commands`; оба состояния переходят друг в друга с условием `1.0`. В 2.8.14 `functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction` содержит 148 строк, вызывается из `entities/player.json` вместе с `effect @s absorption 1 2 true`.

При удалении начальной `/` у строк 1.6 и сравнении как мультимножеств (с учётом кратности, **без** доказательства эквивалентного контекста или порядка вызовов) совпадают все 144 старые vine-команды. Дополнительно в 2.8.14 есть четыре команды detect `leaves 11`: на x+1/x−1/z+1/z−1 относительно `@p` с vine data 8/2/1/4; единственная не совпадающая старая команда — глобальный scoreboard. Оба текста проверяют воздух на конечной позиции как `replace air`. В старом списке 36 вариантов блока/data по четыре направления, в новом 37 по четыре; полный перечень 36 сохранён в оригинале и выписке контроллера. Повторные вызовы, частота и положение `@p` между entity-controller и функцией игрока могут отличаться; нельзя считать совпадение команд доказательством идентичного поведения.

**Дополнительный подробный разбор** (источник: `docs/manual-jungle-vines.md`):

### Jungle Sword: лоза, порядок, саженец и получение

Воспроизводимая [таблица 36/37 пар block/data и номеров команд](jungle-vine-index.md) дополняет [карточку 2.8.14](manual-traces-2.8.14.md#jungle-sword-effectjungle_sword) и [ручную цепочку 1.6](manual-traces-1.6.md#jungle-сопоставление-16-и-2814). Ниже — статический разбор трёх архивов, не проверка работы старого `execute`, регистрации block placer, дерева или loot в Minecraft.

#### Общие значения и разные пути

У точного `effect:jungle_sword` в 1.6 и 2.x объявлены damage **4**, max durability **128**, max stack **1**, enchantable `{value:9,slot:sword}`, self-repair **128**, `hand_equipped:true`, digger web **15**/bamboo **10**, `use_efficiency:true`. Off-hand в 1.6 **true**, в 2.x **false**. Исходный PNG во всех версиях 16×16 и побайтово совпадает; одинаковая текстура не доказывает равного поведения или рендера.

В 1.6 recipe — pattern `F / F / E` для crafting_table, `F=minecraft:leaves` data **3**, `E=minecraft:sapling` data **3**, результат `effect:jungle_sword`. В 2.x локального рецепта результата не обнаружено; ниже приведены две прямые loot-записи. Доступность рецепта и разрешение старых data-значений требуют испытания. [Получение 1.6](acquisition-index-1.6.md#effectjungle_sword) · [2.8.14](acquisition-index-2.8.14.md#effectjungle_sword).

1.6: player-sensor `has_equipment`, self, domain hand, value `effect:jungle_sword` вызывает событие, добавляющее `minecraft:jungle_sword`. Группа задаёт spawn `entity:jungle`, min/max wait **0/0**, количество **1**, `single_use:true`. В общей ветви `minecraft:event_normal_player` группа удаляется; повторные добавления и жизнь helper не сведены к известному периоду. Helper family `despawnear`, health **1**, collision **0×0**, fire_immune true, physics `{}`, summonable true, spawnable false. Его animation `jungle` ссылается на `controller.animation.jungle`. Состояния `default` ↔ `jungle` имеют переходы `(1.0)`; в default буквально `/commands`, не доказано, что это корректная команда или функция. В jungle 144 vine-команды и затем `/scoreboard players set @a swords 2`: score меняется у всех выбранных игроков, а не только у владельца.

2.x: sensor с удержанием вызывает `minecraft:jungle_sword`; в последовательности при family `!= jungle_sword` добавляется группа с family `[player,jungle_sword]` и health `{value:8,max:8}`; отдельный шаг выполняет `effect @s absorption 1 2 true`, затем `function commands/swords_and_more_swords/swords_and_more_swords/jungle_sword`. Stop при family `== jungle_sword` снимает группу, добавляет `minecraft:default_player`, вызывает `effect @s absorption 0`. Не утверждать по одним JSON реальное количество сердец, сохранность текущего здоровья, корректное восстановление группы или частоту запуска.

#### Где и в каком порядке ищется опора

Каждая строка функции буквально начинается `execute @p ~~~ detect`, и в ней целевой fill — **одна точка** `~ ~1 ~`, `vine <data> replace air`. Запись `~~~` без пробелов сохранена из оригинала: то, что мы разбираем текст, не доказывает, что конкретный движок примет устаревший синтаксис. `@p` разрешается относительно контекста команды и может отличаться от владельца/игрока, запустившего событие; разные исполнения не обязаны выбирать одного игрока.

Для каждой пары block/data команды проверяют опору на высоте y+1 относительно выбранного `@p`:

| Порядок внутри группы | Относительная позиция detect | Записанный vine data | Цель fill |
|---:|---|---:|---|
| 1 | x+1, y+1, z+0 | 8 | x+0, y+1, z+0 |
| 2 | x−1, y+1, z+0 | 2 | та же |
| 3 | x+0, y+1, z+1 | 1 | та же |
| 4 | x+0, y+1, z−1 | 4 | та же |

Это **числовые** data из команд; какой стороной и как отрисуется лоза, сможет ли она существовать на данном материале и как разрешается состояние блока — вопросы для движка. Проверяются не любые соседние блоки: только 36 пар 1.6 или 37 пар 2.x из индекса. Например, есть `stone` data 0, 1, 3, 5, но из этого не следует покрытие других data. `log` 0–3, `log2` 0–1, `leaves` 0–3, `leaves2` 0–1, `planks` 0–5 и прочие блоки перечислены с точными позициями в таблице.

После удаления начальной `/` у команд 1.6 и удаления **только четырёх** `leaves 11` строк 53–56 функции 2.x оставшиеся 144 строки совпадают **последовательно и буквально**. Это сильнее совпадения мультимножеств: относительный порядок общих проверок сохранён. Но вызов 1.6 идёт из on_entry helper, а 2.x — через функцию player, и у 1.6 ещё есть scoreboard; поэтому идентичность исполнения или результата не следует из текста команд.

#### Условная модель приоритета, не эмуляция Bedrock

Предположим, что в течение одного последовательного вызова `@p` постоянно выбирает одного игрока, все relevant-команды синтаксически работают, цель сначала air и первый успешно поставленный vine остаётся не-air до конца списка. Тогда первая успешная подходящая команда занимает единственную точку y+1, а последующие с `replace air` уже не заменят её; получается **не более одной** успешно установленной лозы в этом идеализированном проходе. Если разные команды выберут разных игроков, лоза сама изменится, внешний процесс изменит блок или движок иначе обрабатывает replace/data, вывод не переносится автоматически.

- Если из четырёх опор одновременно подходят `x+1 = stone 0` и `x−1 = log 0`, при прочих равных сначала встречается **log 0**: команда №2 в 1.6/2.x, vine data **2**. Команда stone на x+1 имеет №25 и не обязательно сможет заменить уже поставленную лозу. Приоритет сначала по положению блока в списке, потом по четырём направлениям, а не только по x+/x−.
- Если только `x+1 = leaves 11` и `x−1 = leaves2 0`, в 2.x первым подходит №53 (vine data **8**), а в 1.6 `leaves 11` не задан и первым подходит №54 (vine data **2**). Это пример влияния вставленных строк, не измеренный результат в игре.

Командная цель одна, а не четыре независимых блока вокруг игрока. Повторные вызовы и несколько helper/player могут дать другие эффекты; scoreboard 1.6 дополнительно взаимодействует с общей системой сброса.

#### 2.x: отдельный саженец и попугай

Item `minecraft:block_placer` задаёт block `effect99:sapling3`, `use_on:["dirt","grass"]`. Сам block определяет `minecraft:on_placed` event target self; в sequence идут `playsound dig.grass @a[r=12] ~ ~ ~` и `fill ~ ~ ~ ~ ~ ~ sapling 3`. Для блока заданы destroy_time **0.1**, explosion_resistance **1**, block_light_absorption **0**, geometry `geometry.null`, texture `null`/blend, entity/pick collision origin `[-8,0,-8]`, size `[0,0,0]`, map_color `#000000`. Это промежуточная замена блока саженцем data 3, не прямой summon взрослого дерева и не подтверждение расхода предмета, регистрации/роста блока или возможности установки на любую поверхность.

В `entities/parrot.json` компонент `minecraft:behavior.tempt` содержит `speed_multiplier:1.0` и `items:["effect:jungle_sword"]`; как приоритет и поведение компонента будут обработаны, проверить в игре.

#### Условные loot-расчёты 2.x

Оба 2.x содержат одинаковые эти таблицы. Для чисел ниже предполагаются стандартный независимый взвешенный выбор, отсутствие влияния luck/quality, успешное разрешение таблиц и регистрации предмета; это **не** измеренная частота сундуков или забросов:

- `chests/jungle_temple.json`, pool 0: rolls **2…6**, 13 явно взвешенных entries, сумма весов **457**, вес меча **16**. Один выбор — `16/457 ≈ 3.5011%`. Если число целых rolls равномерно по 2…6, вероятность хотя бы одной выбранной записи — среднее `1 − (1 − 16/457)^n`, **≈13.1758%** на этот pool. Генерация структуры и реальный выбор таблицы не входят в оценку.
- `gameplay/fishing.json` и `gameplay/jungle_fishing.json` имеют по одному roll родительского пула: junk weight **10**, quality **−2**; treasure **5**, quality **2**; fish **85**, quality **−1**. Обе ссылаются на один `gameplay/fishing/treasure.json`: вес меча **5**, сумма весов **41**, один roll. Если quality не влияет и оба перехода действительно используются, модель `5/100 × 5/41 = 25/4100 ≈ 0.6098%` на проход через соответствующий родительский пул. Это не установленный шанс на любой заброс: условия игры, luck, зачарования и выбор таблицы биомом могут изменять результат. Прямая запись меча находится в **общей** treasure-таблице, не только в jungle-пуле.

### Что написано на скриншотах

На изображении вручную считаны: damage = `4`; durability = `128`; enchantable = `true`; repairable = `true`. Оригинал: [скриншот 115849](https://drive.google.com/file/d/1YEOBZ0aW8jOnH1Uw26aexwJX-C9nx5Jq/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 20. Lapis Sword — `effect:lapis_sword`

**Кратко:** При удержании в коде предусмотрена выдача опыта. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

**1.6** — определение `Sword_B/items/lapis_sword.json`.
- урон: `6`; максимальная прочность: `{"max_durability":528}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `true`; размер стопки: `1`; свечение: не указан; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:lapis_sword"]` → `528`.
- Оружейный компонент не указан.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**2.8.8 / 2.8.14** — определение `Swords_B/items/lapis_sword.json`.
- урон: `5`; максимальная прочность: `{"max_durability":528}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `false`; размер стопки: `1`; свечение: `false`; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:lapis_sword"]` → `528`; `["minecraft:lapis_lazuli"]` → `48`.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 1.6:**

- Рецепт `Sword_B/recipes/lapis_sword.json`; тип `minecraft:recipe_shaped`.
  - Схема сверху вниз: `F` / `F` / `E`.
  - Обозначения: `{"E":{"item":"minecraft:stick"},"F":{"item":"minecraft:lapis_block"}}`.
  - Результат: `{"item":"effect:lapis_sword"}`; рабочие станции/tags: `["crafting_table"]`.

- Определение: `Sword_B/items/lapis_sword.json`.
- Результаты рецептов: `Sword_B/recipes/lapis_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

**Архив 2.8.14:**

- Рецептов с этим точным результатом локально не найдено. Это не исключает других путей.

- Определение: `Swords_B/items/lapis_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - `Swords_B/loot_tables/chests/pillager_outpost.json` $.pools[3].entries[6]: `{"type":"item","weight":3,"functions":[{"function":"set_count","count":{"min":0,"max":1}}],"name":"effect:lapis_sword"}`
  - `Swords_B/loot_tables/chests/stronghold_corridor.json` $.pools[0].entries[17]: `{"type":"item","name":"effect:lapis_sword","weight":5}`
  - `Swords_B/loot_tables/chests/stronghold_library.json` $.pools[0].entries[3]: `{"type":"item","name":"effect:lapis_sword","weight":5}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[12].Mainhand[0].Name

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

**Условная математическая модель выбора loot в 2.x:**

Числа ниже — вероятность выбрать хотя бы одну запись предмета внутри уже активированного пула, а не шанс реальной добычи. Допущения: все записи доступны; отсутствующий вес принят за 1; quality и условия записей игнорируются; выборы независимы с возвращением; число rolls равномерно в указанном диапазоне. Условия пула считаются уже выполненными. Загрузка таблицы, дополнительный отбор, количество предметов и функции не эмулируются.

- Таблица/пул: `chests/pillager_outpost.json` / 3; entries: 6; rolls: `{"min":2,"max":3}`; вес ID/сумма: 3/28; выбор хотя бы одной записи по модели: **24.5513%**. Условия и оговорки: 1 отсутствующих weight → 1 в модели; functions: `[{"function":"set_count","count":{"min":0,"max":1}}]`.
- Таблица/пул: `chests/stronghold_corridor.json` / 0; entries: 17; rolls: `{"min":2,"max":3}`; вес ID/сумма: 5/521; выбор хотя бы одной записи по модели: **2.3809%**. Условия и оговорки: functions: не задано.
- Таблица/пул: `chests/stronghold_library.json` / 0; entries: 3; rolls: `{"min":2,"max":10}`; вес ID/сумма: 5/275; выбор хотя бы одной записи по модели: **10.3245%**. Условия и оговорки: functions: не задано.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Lapis Sword (`effect:lapis_sword`)

[Полная сравнительная карточка 1.6/2.x](manual-basic-swords.md#lapis-sword).

- `items/lapis_sword.json`: damage 5, durability 528, enchantability 9/sword, max stack 1, offhand false; ремонт self 528 или `minecraft:lapis_lazuli` 48; `on_hurt_entity` расходует 1. Web speed 15, bamboo 10.
- `player.json:296–300,768–777,1900–1919`: сенсор hand и семейство `[player,lapis_sword]`; looping timer `time:[2.5,6.0]`, `randomInterval:true` вызывает `xp 5 @s` и `playsound random.orb @s ~ ~ ~ 0.3`. Заданный интервал и 5 единиц опыта — не доказательство непрерывной работы при любом сочетании групп. При отсутствии предмета группа снимается и добавляется default_player.
- В `stronghold_corridor.json` weight 5/521 на выбор и 2–3 rolls; `stronghold_library.json` 5/275 на выбор и 2–10 rolls. `pillager_outpost.json`: вес 3, set_count 0…1, ещё один элемент без явного веса; точную долю до проверки значения по умолчанию не приводим. См. полные пулы в реестре мира.

**Старая версия 1.6** (источник: `docs/manual-traces-1.6.md`):

- **Lapis** — 6/528; создаётся scoreboard l, ближайшему игроку прибавляется 1, при ровно 10 выполняется `xp 5 @s`, при 30 удаляется objective; длительность цикла и единица XP подлежат проверке движком.

**Дополнительный подробный разбор** (источник: `docs/manual-basic-swords.md`):

#### Lapis Sword

**Характеристики/получение.** В 1.6 damage 6, durability 528 и только self repair 528; в 2.x damage 5, durability 528 и ремонт self 528 либо `minecraft:lapis_lazuli` 48. Рецепт `recipes/lapis_sword.json` есть в 1.6: `F/F/E`, F = `minecraft:lapis_block`, E = `minecraft:stick`; в локальных recipes 2.x точный результат не найден. В 2.x прямые loot-записи: stronghold corridor pool 0 rolls 2–3 и weight 5/521; stronghold library pool 0 rolls 2–10 и weight 5/275; pillager outpost pool 3 weight 3 и `set_count` 0–1 при другом элементе с отсутствующим weight. Последняя доля не выводится без дополнительных допущений. Условные доли — не вероятность получения из структуры.

**1.6.** Helper-controller в обоих on_entry: `scoreboard objectives add l dummy`; `scoreboard players add @p l 1`; при `@p[scores={l=10}]` выполнить `xp 5 @s`; при `@p[scores={l=30}]` удалить objective `l`; затем `@a swords 2`. Фильтрованный `@p` может выбрать не того же игрока, что получил add. В `normal.mcfunction` прямой команды удалить `l` нет; не исключены другие пути изменения состояния.

**2.x.** Sensor hand вызывает группу `minecraft:lapis_sword`, если у self нет family `lapis_sword`. Группа задаёт family `[player,lapis_sword]` и timer `time:[2.5,6.0]`, `randomInterval:true`, `looping:true`; `lapis_sword_skills` выполняет `xp 5 @s` и `playsound random.orb @s ~ ~ ~ 0.3`. Stop при соответствующей family удаляет группу и добавляет default_player. Таймер — объявленный диапазон, не измеренный период и не перенос scoreboard `l` из 1.6.

### Что написано на скриншотах

На изображении вручную считаны: damage = `5`; durability = `528`; enchantable = `true`; repairable = `true`. Оригинал: [скриншот 115858](https://drive.google.com/file/d/1fvRODDZrL5CDlRdyvi4iuqupiY0pkRmc/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 21. Lightning Sword — `effect:lightning_sword`

**Кратко:** Снаряд и 41 команда призыва молний при использовании. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

**1.6** — определение `Sword_B/items/lightning_sword.json`.
- урон: `8`; максимальная прочность: `{"max_durability":2000}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `true`; размер стопки: `1`; свечение: не указан; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:lightning_sword"]` → `2000`.
- Оружейный компонент не указан.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**2.8.8 / 2.8.14** — определение `Swords_B/items/lightning_sword.json`.
- урон: `8`; максимальная прочность: `{"max_durability":2012}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: `{"category":"lightning_sword","duration":12}`; левая рука: `false`; размер стопки: `1`; свечение: `true`; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:lightning_sword"]` → `2012`.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`; событие без нанесения урона существу → `{"event":"weapon"}`; удар по блоку → `{"event":"weapon"}`.
- При использовании предмета указано: `{"on_use":{"event":"on_use"}}`.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 1.6:**

- Рецепт `Sword_B/recipes/lightning_sword.json`; тип `minecraft:recipe_shaped`.
  - Схема сверху вниз: `F` / `F` / `E`.
  - Обозначения: `{"E":{"item":"minecraft:netherstar"},"F":{"item":"minecraft:gold_block"}}`.
  - Результат: `{"item":"effect:lightning_sword"}`; рабочие станции/tags: `["crafting_table"]`.

- Определение: `Sword_B/items/lightning_sword.json`.
- Результаты рецептов: `Sword_B/recipes/lightning_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

**Архив 2.8.14:**

- Рецептов с этим точным результатом локально не найдено. Это не исключает других путей.

- Определение: `Swords_B/items/lightning_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[9].Mainhand[0].Name
  - `Swords_B/structures/lightning_sword.mcstructure` $.entities[0].Item.Name

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Lightning Sword (`effect:lightning_sword`)

[26 старых селекторов и все 41 координата 2.x](lightning-patterns.md) · [сравнение с 1.6 и условная модель](manual-lightning-1.6.md).

- `items/lightning_sword.json`: damage 8, durability 2012, enchantability 9/sword, cooldown 12, repair self 2012, offhand false, web 15/bamboo 10. Все три weapon-хука: durability 1, затем 15 пусто/85 shoot `entity:lightning_projectile` power 1. On-use — **41** буквальная команда `summon lightning_bolt ... default_lightning_bolt` и durability 9: одна на y+2, остальные на осях расстояний 7,14,28,34,42 и диагоналях ±6,±12,±24,±30,±38. Эти координаты сохранены в карточке; не заменять равномерным кругом. Успех команд не гарантирован.
- `player.json` группа с family `[player,lightning_sword]` отключает damage от `other` family lightning, не от всех причин огня. При добавлении группы также `summon lightning_bolt ~ 255 ~ default_lightning_bolt`; при удержании размещается `lightblock2`. Снаряд `entities/lightning_projectile.json` timer 0.1/despawn, impact 1, on-hit вызывает summon lightning, power 2/gravity 0; он ссылается на отсутствующий event `particle` из environment sensor. Проверить загрузку и попадание до удаления.
- `entities/lightning_bolt.json`: entity_spawned добавляет timer 0, который выбирает 80 пусто/20 `summon entity:centella ~ ~1 ~`; сам код этого выбора не проверяет грозу или источник молнии. Нужно проверить порядок `entity_spawned` и event `default_lightning_bolt` для вызванных молний и возможный каскад; считать описанные 20/100 условной ветвью, не частотой всех природных молний.
- `entities/centella.json`: health value 200, movement 0.22, timer random 10…60 looping на despawn, sensor при family centella применяет instant_damage 1 amplifier 0 к `@e[family=!effect99_entities,r=2]`, slow_falling себе, свет и звук. Фатальный damage от player запускает событие с summon lightning, `say 1`, выбором 98 пусто/2 `structure load lightning_sword ~ ~10 ~`; другой sensor при **любом** fatal вызывает отдельный summon lightning и `say 2`. Для player оба фильтра могут совпасть — порядок/кратность проверить. Описанный в сущности путь `loot_tables/entity/centella.json` не присутствует в архиве; эффект разрешения и альтернативные источники не доказаны.

- Выброшенный меч с тегом `lightning_sword` при `q.is_on_fire` направляется контроллером в `despawn_event_3`, который создаёт `particle minecraft:example_linearcurve ~ ~ ~` и `lightning_bolt ~~~ default_lightning_bolt`, но **не содержит `kill @s`**. Контроллер переходит обратно в default по `1.0`; возможно многократное срабатывание при продолжающемся огне, но частота, успешность и срок жизни предмета требуют испытаний. Структура `lightning_sword.mcstructure` сохраняет тег `lightning_sword` у item-сущности, поэтому здесь путь через сохранённые теги отличается от назначения тега только функцией игрока.

**Старая версия 1.6** (источник: `docs/manual-traces-1.6.md`):

#### Lightning Sword 1.6: подробная цепочка

[Сенсор, helper и геометрия 1.6/2.x](manual-lightning-1.6.md) · [26 селекторов и 41 координата](lightning-patterns.md). Это статические декларации, не установленный тайминг молний.

**Дополнительный подробный разбор** (источник: `docs/manual-lightning-1.6.md`):

### Lightning Sword 1.6 и геометрия 2.x

Статическое сравнение исходных архивов; [все 26 селекторов 1.6 и 41 точка 2.x](lightning-patterns.md) извлечены с сохранением порядка команд. Реальное исполнение, призыв молнии, ущерб миру и модель вероятностей не проверены в Minecraft.

#### Предмет, клиент и получение 1.6

`Sword_B/items/lightning_sword.json`: ID `effect:lightning_sword`, `format_version:1.20.20`, max stack **1**, damage **8**, max durability **2000**, `minecraft:glint:true`, `allow_off_hand:true`, `hand_equipped:true`, `can_destroy_in_creative:false`; enchantable `{value:9,slot:sword}`; ремонт самим `effect:lightning_sword` amount **2000**. Digger использует efficiency и скорости web **15**, bamboo **10**. Числа — объявления, а не результат удара/ремонта в игре.

В 1.6 локальный shaped recipe `Sword_B/recipes/lightning_sword.json` имеет pattern `F / F / E`: два `minecraft:gold_block`, затем **буквальный** ID `minecraft:netherstar`, результат `effect:lightning_sword`, tag `crafting_table`. Не подменять старое имя ингредиента на предполагаемый современный аналог без отдельной проверки регистрации рецепта. Прямых локальных записей предмета в loot/trade/структурах 1.6 не найдено; это не доказывает отсутствие других путей. В 2.x локальные recipe и прямые loot для этого ID не обнаружены, зато есть структура с предметом и структура с armor stand ([получение 2.8.14](acquisition-index-2.8.14.md#effectlightning_sword)); реальную выдачу надо проверять по цепи Centella и регистрации структур.

Значок 1.6 **16×16**, 2.8.14 **64×64**; это различающиеся размеры, не автоматическая эквивалентность ([аудит PNG](icon-comparison.md)). Ресурс 1.6 называет item `§g§lLightning Sword`. Разные `minecraft:glint` и `minecraft:foil` не следует без испытания считать полностью одинаковыми.

#### Сенсор и helper 1.6

`Sword_B/entities/player.json`: sensor `has_equipment`, self, domain `hand`, value `effect:lightning_sword` посылает event `minecraft:lightning_sword`; он добавляет одноимённую component group. Её `minecraft:spawn_entity` задаёт `entity:lightning`, wait min/max **0/0**, `num_to_spawn:1`, `single_use:true`. Другая player-ветвь `minecraft:event_normal_player` удаляет группу, поэтому один helper на всё время удержания или определённая частота не доказаны ([общая цепь 1.6](manual-global-state-1.6.md)). Не отождествлять helper `entity:lightning` с призываемой им ванильной `lightning_bolt`.

`Sword_B/entities/lightning.json` — helper с family `despawnear`, фильтром despawn по собственной family, health **1**, collision **0×0**, fire immune true, physics `{}`; summonable true, spawnable false, experimental false. В описании нет таймера с явно заданной продолжительностью. scripts animate `lightning` ссылается на `controller.animation.lightning` из файла **с пробелом** `Sword_B/animation_controllers/lightning sword.json`.

У этого контроллера состояния `default` и `lightning` переходят друг в друга по `(1.0)`; в обоих `on_entry` списки **побайтово равных строк в том же порядке**: по одной команде для 26 типов, затем `scoreboard players set @a swords 2`. Каждый selector записан `@e[type=...,r=16,rm=10]`; далее старый `execute ... ~ ~ ~ summon lightning_bolt` задаёт контекст позиции выбранной сущности. Здесь нет явно заданной вероятности, отдельного on-use или призыва фиксированной сетки из 41 точки. Перечень включает, в частности, creeper, blaze, `zombie_pigman`, `evocation_fang`, ravager, guardian и phantom; игрок как отдельный тип в списке отсутствует. Значение score `swords` изменяется у **всех** `@a`, не только у владельца.

Из двух состояний с одинаковыми командами нельзя вывести частоту ударов или доказать, что молнии реально призываются: порядок переходов/entry, жизнь helper, исполнение устаревших selector/type ID, пересечения и взаимодействие многопользовательских команд подлежат испытанию. Radius `rm=10,r=16` записан относительно контекста helper, а не подтверждён относительно персонажа после перемещения helper.

#### Основные отличия 2.x

У одинакового ID damage **8**, max durability **2012**, off-hand **false**, self-repair **2012**, cooldown duration **12**; в JSON используются `minecraft:foil:true` и другая render-offset конфигурация. Три item weapon hook направлены в `weapon`: отдельно задано damage durability **1**, затем `randomize` с весами **15** пусто и **85** shoot `entity:lightning_projectile`, launch_power **1**. Это условный выбор при срабатывании события, а не доказанный шанс попадания молнии.

`on_use` содержит `run_command` из **41** строк и рядом в том же объекте damage durability **9**, target self. Порядок между полями `run_command` и `damage` не декларирован как sequence и не установлен. Все команды summon используют `default_lightning_bolt`; это **точки**, не селекторы сущностей:

- Одна точка `(0,+2,0)` относительно контекста команды; ещё **40** на y=0: по четыре осевых при расстояниях **7, 14, 28, 34, 42**, и по четыре диагональных в координатах `(±d,±d)` для **d=6, 12, 24, 30, 38**.
- Все 41 тройки координат уникальны; ограничения x/z от **−42 до +42**. Дальнейшие диагональные точки `(±38,0,±38)` находятся на горизонтальном расстоянии `38√2 ≈ 53.740`, больше 42. Это не радиус поражения и не обещание загрузки каждой точки.
- Точные точки и порядок сохранены в [индексе](lightning-patterns.md). Нельзя заменить рисунок кругом, равномерной выборкой или ближайшими целями: в 1.6 смысл команд другой.

Player group 2.x содержит damage_sensor, где `other` family `lightning` → `deals_damage:false`; это не универсальная защита от огня и других причин урона. Событие при отсутствии family `lightning_sword` одновременно добавляет группу и содержит summon на `~ 255 ~`, а другой шаг задаёт заполнение `effect99:lightblock2`. Снаряд, естественные молнии, Centella, выброшенный предмет и отсутствующие ссылки разобраны в [карточке 2.8.14](manual-traces-2.8.14.md#lightning-sword-effectlightning_sword).

#### Условная модель 41 молнии и Centella

В обеих 2.x `entities/lightning_bolt.json` entity_spawned добавляет группу timer `[0,0]`, event `spawn_centella`: weights **80** пусто и **20** команда `summon entity:centella ~ ~1 ~`. Эта декларация не проверяет источник или грозу, но сами срабатывание таймера и сочетание с `default_lightning_bolt` не установлены.

Только при гипотезе, что **все 41** призыва создали подходящие lightning, все 41 timer/event сработали, выборы независимы и веса трактуются как 80/20, математически ожидалось бы **8.2 успешной ветви**, а вероятность хотя бы одной — `1 − (4/5)^41 ≈ 99.9894%`; вероятность нуля ≈0.0106%. Это **не измеренный шанс появления Centella при использовании меча** и не гарантированное количество сущностей: команды, обработка событий, спавн сущности и загруженность мира могут нарушить предпосылки. Цепь Centella может порождать дополнительные молнии на fatal-событиях; их в эту модель не включали.

### Что написано на скриншотах

На изображении вручную считаны: damage = `8`; durability = `2012`; enchantable = `true`; repairable = `true`. Оригинал: [скриншот 115934](https://drive.google.com/file/d/12oKa5cnYV5yDSpreB54Pfe2KaqOx8FaK/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 22. Magma Sword — `effect:magma_sword`

**Кратко:** Защита от отдельных источников урона и замена лавы магмой. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

**1.6** — определение `Sword_B/items/magma_sword.json`.
- урон: `7`; максимальная прочность: `{"max_durability":1000}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `true`; размер стопки: `1`; свечение: не указан; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:magma_sword"]` → `1000`.
- Оружейный компонент не указан.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**2.8.8 / 2.8.14** — определение `Swords_B/items/magma_sword.json`.
- урон: `7.2`; максимальная прочность: `{"max_durability":1316}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `false`; размер стопки: `1`; свечение: `false`; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:magma_sword"]` → `1316`; `["minecraft:magma"]` → `100`.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 1.6:**

- Рецепт `Sword_B/recipes/magma_sword.json`; тип `minecraft:recipe_shaped`.
  - Схема сверху вниз: `F` / `F` / `E`.
  - Обозначения: `{"E":{"item":"minecraft:blaze_rod"},"F":{"item":"minecraft:magma"}}`.
  - Результат: `{"item":"effect:magma_sword"}`; рабочие станции/tags: `["crafting_table"]`.

- Определение: `Sword_B/items/magma_sword.json`.
- Результаты рецептов: `Sword_B/recipes/magma_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

**Архив 2.8.14:**

- Рецептов с этим точным результатом локально не найдено. Это не исключает других путей.

- Определение: `Swords_B/items/magma_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - `Swords_B/loot_tables/chests/underwater_ruin_big.json` $.pools[1].entries[1]: `{"type":"item","name":"effect:magma_sword","weight":1}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[27].Mainhand[0].Name

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

**Условная математическая модель выбора loot в 2.x:**

Числа ниже — вероятность выбрать хотя бы одну запись предмета внутри уже активированного пула, а не шанс реальной добычи. Допущения: все записи доступны; отсутствующий вес принят за 1; quality и условия записей игнорируются; выборы независимы с возвращением; число rolls равномерно в указанном диапазоне. Условия пула считаются уже выполненными. Загрузка таблицы, дополнительный отбор, количество предметов и функции не эмулируются.

- Таблица/пул: `chests/underwater_ruin_big.json` / 1; entries: 1; rolls: `1`; вес ID/сумма: 1/24; выбор хотя бы одной записи по модели: **4.1667%**. Условия и оговорки: functions: не задано.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Magma Sword (`effect:magma_sword`)

[Полная сравнительная карточка 1.6/2.x](manual-heat-light-swords.md#magma-sword).

- `items/magma_sword.json`: damage 7.2, durability 1316, enchantability 9/sword; ремонт self 1316 либо буквальный `minecraft:magma` 100. On hurt entity — 1 прочности, web 15, bamboo 10.
- `player.json:305–312,740–749,1961–2000`: sensor damage отключает damage для `fire_tick` либо при фильтре `is_block` со значением `magma`; не обобщать это на lava или все виды fire. Группа имеет family `[player,magma_sword]`. Событие выполняет пять `fill ... magma 0 replace lava` в точных координатах под игроком: один центр, прямоугольник x=0…1/z=0…1 и по одному на x=−1, z=−1; некоторые позиции перекрываются. Сопутствует guardian attack particle. При `in_water` случайный выбор 99 пусто / 1 команда звука `bubble.up` — доля 1/100 в этой ветви при прохождении фильтра, не гарантированная частота.
- `loot_tables/chests/underwater_ruin_big.json`: второй пул (индекс 1), 1 roll, вес меча 1 из явно заданной суммы 24: 1/24 на выбор при стандартной семантике весов. Проверить привязку ванильной структуры к таблице и другие условия в полном файле.

**Старая версия 1.6** (источник: `docs/manual-traces-1.6.md`):

#### Fire, Magma и Spider 1.6: типы и мир

[Три контроллера, рецепты и риск изменения мира](manual-fire-magma-spider-1.6.md) · [матрица type-селекторов](fire-web-targets-1.6.md).

**Дополнительный подробный разбор** (источник: `docs/manual-heat-light-swords.md`):

#### Magma Sword

**Предмет и получение.** 1.6: damage 7, durability 1000, offhand true, self repair 1000; рецепт `F/F/E`, F = буквальный `minecraft:magma`, E = `minecraft:blaze_rod`. В 2.x: damage 7.2, durability 1316, offhand false, self repair 1316 и `minecraft:magma` 100, только on_hurt_entity → прямой расход 1. Точный ID `minecraft:magma` не заменяется на другой блок по предположению. В 2.x прямого рецепта с этим результатом локально не найдено; `chests/underwater_ruin_big.json` pool 1 имеет один roll, weight меча 1 при сумме явно заданных весов 24 — 1/24 на выбор при активации пула и стандартной семантике весов, не гарантия сундука.

**1.6.** Helper `entity:magma` использует `controller.animation.magma`; на каждом из двух одинаковых on_entry: `effect @p fire_resistance 10 0 true`; `fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 magma 0 replace lava` в контексте `@p`; затем **21** отдельная команда `execute @e[r=15,rm=2,type=…] ~ ~ ~ setblock ~ ~ ~ fire`; затем `@a swords 2`. На `replace lava` data явно не записано; отдельного `replace flowing_lava` нет. В установке fire нет явной проверки air или `replace`, поэтому не описывать её как безопасную установку огня только в пустоту. Полный точный список 21 типов и их отличие от Fire — [матрица](fire-web-targets-1.6.md).

**2.x.** Группа player `[player,magma_sword]` отменяет damage при `has_damage:fire_tick` **или** `is_block` subject block, operator equals, value `magma`; lava и произвольный fire в эти два условия не добавлены. Дальнейший отдельный шаг события содержит пять fill на `y=-1`, все `magma 0 replace lava`: центр `(0,0)`; прямоугольник от `(1,1)` до `(0,0)`; точка `(0,1)`; точка `(-1,0)`; точка `(0,-1)`. При идеальном пересечении это 8 позиций, считая повторения, но лишь **6 различных** координат x/z. Это геометрия команд, а не число заменённых блоков. Затем particle `minecraft:guardian_attack_particle` с относительными координатами как в исходнике. Третий шаг имеет фильтр `in_water`, operator `==`, **без поля value** и randomize 99 пусто / 1 `playsound bubble.up @a ~ ~ ~ 1 0.9`. Не приписывать фильтру отсутствующее значение или объявлять 1% на секунду; частота сенсора и исполнение не заданы этой дробью.

**Дополнительные детали 1.6** (источник: `docs/manual-fire-magma-spider-1.6.md`):

### Fire, Magma и Spider 1.6: цели и воздействие на мир

[Сравнительная таблица всех type-селекторов](fire-web-targets-1.6.md) извлекает строки из трёх исходных контроллеров. Ни одна команда не проверена на выполнение в игре: старые имена, селекторы, замена блоков, контекст `@p` и частота зависят от движка.

#### Общая цепь и разные центры

Для каждого предмета `player.json` проверяет `has_equipment` в domain `hand`, передаёт одноимённый event и добавляет группу `minecraft:fire_sword` / `minecraft:magma_sword` / `minecraft:spider_sword`. Группы соответственно объявляют spawn `entity:fire`, `entity:magma`, `entity:spider`, каждая wait 0/0, num_to_spawn 1, single_use true. Другая player-ветвь удаляет эти группы; повторное добавление и длительность жизни помощника не установлены. Helpers используют family `despawnear` и одноимённые animation controllers; их положение не гарантированно следует за владельцем.

В каждом из трёх контроллеров `default` и состояние с именем меча переходят друг в друга по `(1.0)` и содержат одинаковые строки `on_entry`. Соответственно, сравнение ниже относится к **одному списку**, а не двум одновременно выполненным копиям. Каждая последовательность заканчивается `/scoreboard players set @a swords 2` для всех выбранных игроков; глобальные взаимодействия и возможные повторы описаны [отдельно](manual-global-state-1.6.md).

`@p` выбирается из контекста helper и не гарантированно означает владельца. Отдельные `@e[r=...,type=...]` сначала выбираются относительно контекста helper, после чего `execute` использует позицию соответствующей цели. Не заменять их единой областью вокруг игрока.

#### Предметы и рецепты 1.6

| Предмет | damage / max durability / self repair | Локальный shaped recipe |
|---|---|---|
| Fire | 12 / 2000 / 2000 | `#SM / SBS / NS#`; `N=blaze_rod`, `S=blaze_powder`, `B=iron_sword`, `M=magma_cream`; **`#` отсутствует в key** |
| Magma | 7 / 1000 / 1000 | `F / F / E`; `F=minecraft:magma`, `E=minecraft:blaze_rod` |
| Spider | 6 / 628 / 628 | `#SS / SBS / NS#`; `N=stick`, `S=web`, `B=spider_eye`; **`#` отсутствует в key** |

Все три: max stack 1, `allow_off_hand:true`, `hand_equipped:true`, `can_destroy_in_creative:false`, `minecraft:glint:false`, enchantable value 9/slot sword, digger web 15/bamboo 10/use_efficiency true. Ремонт — самим предметом; названия ингредиентов без namespace в таблице обозначают исходный `minecraft:`. Нет основания автоматически дописывать key `#`, исправлять буквальный `minecraft:magma` или считать объявленные рецепты работающими. [Полная проверка рецептов](manual-acquisition-issues.md), [сравнение компонентов с 2.x](item-version-matrix.md).

#### Fire: 31 тип и изменения блоков

`Sword_B/animation_controllers/fire_sword.json`, в каждом состоянии **39** строк:

1. `/effect @p fire_resistance 10 0 true` — длительность 10, amplifier 0.
2. `execute @p ... detect ~ ~ ~ air 0 setblock ~ ~ ~ fire` — проверка воздуха в позиции ближайшего игрока.
3. Пять fill относительно `@p` в кубе `~3 ~3 ~3` → `~-3 ~-3 ~-3`: **7×7×7 = 343** возможных позиций в каждой геометрической рамке. В исходном порядке: `snow_layer → air 0`; `ice → water 0`; `blue_ice → water 0`; `packed_ice → water 0`; `snow → grass 0`. Это замена существующего мира, не декоративная частица и не сохранение исходных блоков; фактическое число замен зависит от содержимого, интерпретации data и успеха команд.
4. **31** команда `@e[r=15,rm=2,type=…] ... setblock ~ ~ ~ fire` для типов из [матрицы](fire-web-targets-1.6.md), включая корову, свинью, овцу, лошадь, кролика, курицу, лису, летучую мышь, белого медведя и жителя. Нет ограничения только на враждебных существ. В этих отдельных командах нет `detect` или `replace air`; запись `setblock` потенциально затрагивает имеющийся блок в позиции цели, но точные стандартные режимы, перенос координат и результат при занятом блоке нужно проверить в исходном движке.
5. Глобальный scoreboard для `@a`.

Самому ближайшему игроку команда №2 может поставить огонь при detect air, хотя №1 отдельно объявляет fire resistance. Успех одной команды не доказывает успех другой, а сопротивление не является доказанной защитой от любых причин урона.

#### Magma: 21 тип и плоскость лавы

`Sword_B/animation_controllers/magma_sword.json`, **24** строки на состояние: та же запись `fire_resistance 10 0 true` для ближайшего игрока; затем `fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 magma 0 replace lava` от `@p`, плоскость **5×5 = 25** геометрических позиций. После `replace lava` в этой команде **нет явного data**; не добавлять `0` по аналогии с другими файлами. В исходнике нет такой же отдельной команды для `flowing_lava`; это не доказательство того, какие именно состояния лавы выберет движок.

Далее **21** type-команда `setblock fire` в `r=15,rm=2` от helper и глобальный scoreboard. Эти 21 типа — точное подмножество 31 Fire; **10** типов, имеющихся в Fire и отсутствующих в Magma, — `cow`, `pig`, `chicken`, `horse`, `rabbit`, `sheep`, `fox`, `bat`, `polar_bear`, `villager`. Это сопоставление только буквальных команд данного контроллера, не утверждение о полной безопасности перечисленных существ.

#### Spider: паутина и два разных селектора

`Sword_B/animation_controllers/spider_sword.json`, **31** строка на состояние:

1. `effect @p poison 0 0 true`.
2. Две команды с `detect ... web 0` удаляют web в позиции `@p` или на y+1, заменяя web на air только в соответствующей точке.
3. От позиции `@p` задаётся `slowness 1 128 true` для `@e[r=6,type=spider]` и отдельно `type=cave_spider`. Эти эффекты не направлены на весь список паутины и имеют другой центр выбора.
4. **25** отдельных типов выбираются в `@e[r=5,type=…]` от helper; в позиции каждой цели команда `fill ~ ~ ~ ~ ~ ~ web 0 replace air` проверяет одну позицию. Список содержит, среди прочего, `tnt`, `evocation_fang`, `blaze` и `zombie_pigman`, но **не содержит** отдельного web-fill по `spider` или `cave_spider`. Их наличие в командах slowness не означает наличие в списке fill.
5. `scoreboard players set @a swords 2`.

Не путать статическое количество строк с количеством целей/реальных блоков: каждая команда может выбрать ноль, одну или много сущностей, выполняться несколько раз или не пройти. Отсутствие type-команды в этих трёх списках не доказывает отсутствия воздействия из другой механики, vanilla или иного пакета. Реализации 2.x используют дополнительные события/loot/сущности и не сводятся к этим старым контроллерам; см. [карточки 2.8.14](manual-traces-2.8.14.md).

### Что написано на скриншотах

На изображении вручную считаны: damage = `7.2`; durability = `1316`; enchantable = `true`; repairable = `true`. Оригинал: [скриншот 115920](https://drive.google.com/file/d/1ym1j2BhOsqJPPwqRzdPf0JUlIqYyPK4s/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 23. Nether Star Sword — `effect:nether_star_sword`

**Кратко:** Звёздные снаряды; связанные условия получения Wither Sword. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

- В 1.6 предмет с этим точным ID не найден.

**2.8.8 / 2.8.14** — определение `Swords_B/items/nether_star_sword.json`.
- урон: `7`; максимальная прочность: `{"max_durability":3256}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `false`; размер стопки: `1`; свечение: `true`; предмет исчезает: `false`.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:nether_star_sword"]` → `3256`; `["minecraft:nether_star"]` → `3000`.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`; событие без нанесения урона существу → `{"event":"weapon"}`; удар по блоку → `{"event":"weapon"}`.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 2.8.14:**

- Рецепт `Swords_B/recipes/nether_star_sword.json`; тип `minecraft:recipe_shapeless`.
  - Ингредиенты: `[{"item":"minecraft:nether_star","data":0},{"item":"minecraft:diamond_sword","data":0}]`.
  - Результат: `{"item":"effect:nether_star_sword","count":1}`; рабочие станции/tags: `["crafting_table"]`.

- Определение: `Swords_B/items/nether_star_sword.json`.
- Результаты рецептов: `Swords_B/recipes/nether_star_sword.json` (`minecraft:recipe_shapeless`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[32].Mainhand[0].Name

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Nether Star Sword (`effect:nether_star_sword`)

[Подробные получение, снаряды и связи](manual-ghost-nether-ultra.md#nether-star-sword).

- `Swords_B/items/nether_star_sword.json:8–70`: damage 7, max durability 3256, foil true, should_despawn false, stack 1, enchantability value 9/slot sword, offhand false, ремонт тем же мечом 3256 либо nether_star 3000, web speed 15 и bamboo 10. Все три weapon-хука ссылаются на одно событие.
- `:73–120`: строго в `sequence` сначала `shoot entity:nether_star_projectile` с launch_power 1; далее выбор с весами 80 и 20: либо один summon `entity:nether_star ^ ^20 ^-6`, либо тот же summon и ещё один `^ ^18 ^-6`; далее **другой** randomize: вес 9999 — потеря 1 прочности, вес 1 — summon `entity:ultra_instinct_explode`. Условные доли второй развилки 99,99% и 0,01%, но нельзя заменить её независимым событием «0,01% на каждый удар по сущности»: есть три типа хуков и неизвестно фактическое исполнение команд. В редкой ветви заявленного расхода прочности нет.
- `Swords_B/entities/nether_star_projectile.json:1–100`: базовый runtime snowball, семейства `effect99_entities`, `nether_star_projectile`, timer `[5,5]`, collision 1×1, projectile power 1/gravity 0, impact damage 6, knockback true, destroy_on_hit true, remove_on_hit и event `set_sound`. При событии entity_spawned, если `other` имеет в hand меч, добавляется группа `nether_star_sword`: scale 0, timer `[0.1,0.1]`, projectile power 5/gravity 0, impact damage -1, knockback false, event `set_objective`. Не считать базовое и групповое значение одновременно действующими: важно, какая группа реально применена и как движок разрешает компоненты.
- `nether_star_projectile.json:101–138`: `set_objective` вызывает summon `entity:objective`; `set_sound` выбирает три равновесных варианта thunder pitch 5.5, 6, 7 для `@a[r=20]`; `set_particle` создаёт `minecraft:nether_star_hit ~ ~2.5 ~`. Какое событие попадания реально запускается, зависит от активной группы. 
- `Swords_B/entities/entity_nether_star.json:15–77`: призванная звезда без гравитации, health 99/99, не получает урон cause all, collision 0.25×0.25, looping timer `[0.5,0.5]` на добавление группы despawn, `ranged_attack` interval 0.1, charge triggers 0.1, radius 28, shooter `entity:nether_star_projectile`. Цель выбирается по family `objective` с max_dist 28, `must_see:false`, scan_interval 1 и target_search_height 28. Детали `entities/objective.json` и её жизненного цикла приведены ниже; реальная цепочка запуска снарядов требует испытаний.

##### Продолжение: цель Nether Star

`Swords_B/entities/objective.json:1–57`: ID `entity:objective`, family `[effect99_entities,objective]`, spawnable false, summonable true; таймер `[1,1]`, looping true вызывает добавление группы `despawn`; не получает урон cause all, collision 0.25×0.25, has_gravity false и has_collision false. `environment_sensor` вызывает `follow_entity`: `tp @s @e[r=8,c=1,type=!player,type=!item,family=!parrot_tame,family=!tamed,type=!arrow,type=!xp_orb,family=!effect99_entities]`. Это выбор ближайшей подходящей сущности по старому селектору, не обязательно именно той, в которую попал снаряд; без подходящей цели и при изменении целей надо проверять исходный движок. Звезда выбирает family objective в радиусе 28, поэтому важны оба радиуса и исключения, а не просто «самонаведение на противника». Отдельно в `nether_star_projectile.json` есть событие `objective`, которое добавляет группу `objective`, но такая группа **в этой сущности не определена**; это не то же самое, что команда `set_objective` для создания `entity:objective`. Локальных вызовов события `objective` поиск по архиву не обнаружил, однако внешнее событие возможно. Регистрацию и последствия необходимо проверить в движке.

**Дополнительный подробный разбор** (источник: `docs/manual-ghost-nether-ultra.md`):

#### Nether Star Sword

`effect:nether_star_sword`: damage 7, durability/self repair 3256, дополнительный repair `minecraft:nether_star` 3000, enchantable 9/sword, offhand false, `should_despawn:false`. В обеих 2.x объявлен **shapeless** recipe crafting_table: `minecraft:nether_star` data 0 + `minecraft:diamond_sword` data 0 → один меч (`count:1`). Это точная рецептурная декларация, не доказательство её принятия движком.

Три weapon-хука ведут в один `sequence` из трёх шагов:

1. `shoot entity:nether_star_projectile` launch_power 1.
2. Randomize 80 — один summon `entity:nether_star ^ ^20 ^-6`; 20 — тот же и ещё один `^ ^18 ^-6`. При стандартном выборе условное среднее **1.2 записанного summon на вызов этого шага**; это не число созданных или попавших звёзд.
3. Отдельный randomize 9999 — durability damage 1 / 1 — summon `entity:ultra_instinct_explode`. Доля 1/10000 = 0.01% условна на этот выбор; в редкой ветви direct durability damage не указан. Разные шаги не следует заменять одним испытанным шансом на удар.

Базовый `nether_star_projectile` имеет timer `[5,5]`, collision 1×1, projectile power 1, impact damage 6 и `set_sound`; при entity_spawned и фильтре `other` с мечом в hand добавляемая группа вместо этого объявляет scale 0, timer `[0.1,0.1]`, power 5, impact damage −1 и `set_objective`. Значения базы и группы не нужно суммировать. `set_objective` вызывает `entity:objective`; тот с timer `[1,1]` выполняет `tp @s @e[r=8,c=1,type=!player,type=!item,family=!parrot_tame,family=!tamed,type=!arrow,type=!xp_orb,family=!effect99_entities]`, то есть выбор ближайшей подходящей сущности, не записанный идентификатор попадания. Звезда ищет family objective в радиусе 28, использует ranged shooter и timer `[0.5,0.5]`. Пустая выборка и приоритет групп не установлены.

Есть отдельное событие projectile `objective`, добавляющее группу `objective`, которая **в том же файле не объявлена**; не путать его с `set_objective` и призывом другой сущности. Локальный буквальный поиск вызовов этого события не обнаружил, но внешние/динамические вызовы возможны. При fatal damage Wither от player с этим мечом в hand другой event выбирает 87 пусто/13 загрузить структуру Wither Sword — не выпадает из самого рецепта и не гарантировано каждым применением.

### Что написано на скриншотах

На изображении вручную считаны: damage = `7`; durability = `3256`; enchantable = `true`; repairable = `true`. Оригинал: [скриншот 115826](https://drive.google.com/file/d/18SAkmYz1M8hva9FAv8bJfFTWOM7OD8F6/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 24. Obsidian Sword — `effect:obsidian_sword`

**Кратко:** Случайный расход прочности; связан с Fire Sword под дождём. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

**1.6** — определение `Sword_B/items/obsidian_sword.json`.
- урон: `12`; максимальная прочность: `{"max_durability":3000}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `true`; размер стопки: `1`; свечение: не указан; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:obsidian_sword"]` → `3000`.
- Оружейный компонент не указан.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**2.8.8 / 2.8.14** — определение `Swords_B/items/obsidian_sword.json`.
- урон: `8`; максимальная прочность: `{"max_durability":3000}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `false`; размер стопки: `1`; свечение: `false`; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:obsidian_sword"]` → `3000`; `["minecraft:obsidian"]` → `120`.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 1.6:**

- Рецепт `Sword_B/recipes/obsidian_sword.json`; тип `minecraft:recipe_shaped`.
  - Схема сверху вниз: `F` / `F` / `E`.
  - Обозначения: `{"E":{"item":"minecraft:blaze_rod"},"F":{"item":"minecraft:obsidian"}}`.
  - Результат: `{"item":"effect:obsidian_sword"}`; рабочие станции/tags: `["crafting_table"]`.

- Определение: `Sword_B/items/obsidian_sword.json`.
- Результаты рецептов: `Sword_B/recipes/obsidian_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

**Архив 2.8.14:**

- Рецептов с этим точным результатом локально не найдено. Это не исключает других путей.

- Определение: `Swords_B/items/obsidian_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[22].Mainhand[0].Name
  - `Swords_B/structures/obsidian_sword.mcstructure` $.entities[0].Item.Name

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Obsidian Sword (`effect:obsidian_sword`)

[Полная сравнительная карточка 1.6/2.x](manual-heat-light-swords.md#obsidian-sword).

- `items/obsidian_sword.json`: damage 8, max durability 3000, enchantability 9/sword, ремонт self 3000 или `minecraft:obsidian` 120, offhand false. Только `on_hurt_entity` вызывает `randomize`: 55/100 расходует 1, 30/100 — 2, 15/100 — 3 прочности; это условные доли указанного события, не любого взаимодействия.
- `player.json:286–294,782–791,1883–1898`: соответствующая группа игрока устанавливает sensor с `deals_damage:false` при `has_damage` `block_explosion` или `entity_explosion`, family `[player,obsidian_sword]`, `knockback_resistance` value 1.0. Другие источники урона из текста нельзя считать отменёнными. Сенсор по `hand` добавляет/снимает группу; default_player добавляется при остановке. Нужны тесты конкретных видов взрыва и сочетания с другими группами.
- Изученная цепочка Fire Sword загружает структуру `obsidian_sword` при дожде, а не при воде: см. раздел Fire Sword. В структуре сохранён `Item.tag.Damage=1000` при отдельном `Item.Damage=0`; структура и отдельное имя предмета не доказывают перенос исходного значения прочности или фактическое толкование этих полей в игре.

**Старая версия 1.6** (источник: `docs/manual-traces-1.6.md`):

- **Obsidian** — 12/3000; для всех игроков при detect air lava 0 и flowing_lava 0 в плоскости y−1 ±2 заменяются obsidian 0. Дополнительные detect lava data 0…8 и flowing_lava 0 назначают fire_resistance 10 с amplifier 0. Покрытие других состояний текущей лавы не предполагается.

**Дополнительный подробный разбор** (источник: `docs/manual-heat-light-swords.md`):

#### Obsidian Sword

**Предмет и получение.** `effect:obsidian_sword`: 1.6 damage 12, durability 3000, offhand true, self repair 3000. В 2.x damage 8, durability 3000, offhand false; ремонт self 3000 или `minecraft:obsidian` 120. Обе версии объявляют stack 1, enchantable 9/sword, web 15 и bamboo 10. В 1.6 `recipes/obsidian_sword.json` задаёт `F/F/E`, F = `minecraft:obsidian`, E = `minecraft:blaze_rod`. Локального рецепта с этим точным результатом в 2.x не найдено. Зато тегированный по имени выброшенный Fire Sword при дожде вне воды запускает таймер `[5,6]` и событие загрузки структуры `obsidian_sword`; при воде отдельная ветка грузит Glass. NBT `obsidian_sword.mcstructure` содержит один item нужного ID, `Item.Damage:0` и вложенный `Item.tag.Damage:1000`; значение в новой игре и перенос состояния исходного меча не доказаны. [Подробная цепь](manual-dropped-items-2.8.md).

**1.6.** Player hand sensor добавляет группу со spawn `entity:obsidian`, wait 0/0, num 1, single_use true; helper подключает `controller.animation.ob`. Оба состояния выполняют одинаковый список. Первые две команды при обнаружении `air 0` в позиции **каждого** `@a` заполняют плоскость `x,z=-2…2`, `y=-1` блоком obsidian, заменяя соответственно `lava 0` и `flowing_lava 0`. Далее девять отдельных detect `lava` data 0…8 и один `flowing_lava 0` выполняют `effect @s fire_resistance 10 0 true`; затем `scoreboard players set @a swords 2`. Проверка владельца в этих `@a` отсутствует, контекст `@s`, возможности замены и количество работающих команд движком не установлены.

**2.x.** Только weapon `on_hurt_entity` вызывает randomize: веса 55/30/15 назначают прямой durability damage 1/2/3. При нормализованном выборе среднее прямого действия 1,60 **условно на вызов**; штатный износ и число вызовов сюда не входят. Hand sensor добавляет группу `[player,obsidian_sword]` с `knockback_resistance.value:1.0` и damage sensor `deals_damage:false` при любом из двух `has_damage`: `block_explosion`, `entity_explosion`. Это не запись иммунитета к fire, lava или всем воздействиям; stop удаляет группу и добавляет default_player. Разрешение конфликтов групп неизвестно.

### Что написано на скриншотах

На изображении вручную считаны: damage = `8`; durability = `3000`; enchantable = `true`; repairable = `true`. Оригинал: [скриншот 115902](https://drive.google.com/file/d/1bdPcV4MdHpWMaTX-HNVZZEjPZ7XbuusZ/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 25. Quartz Diamond — `effect:quartz_diamond`

**Кратко:** Материал, используется для кварцевой цепочки и фонтана. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

- В 1.6 предмет с этим точным ID не найден.

**2.8.8 / 2.8.14** — определение `Swords_B/items/quartz_diamond.json`.
- урон: не указан; максимальная прочность: не указан; зачарование: не указан; перезарядка: не указан; левая рука: не указан; размер стопки: `9`; свечение: `true`; предмет исчезает: не указан.
- Ремонт: компонент не указан; это не доказывает невозможности ремонта.
- Оружейный компонент не указан.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 2.8.14:**

- Рецептов с этим точным результатом локально не найдено. Это не исключает других путей.

- Определение: `Swords_B/items/quartz_diamond.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - `Swords_B/loot_tables/blocks/quartz_diamond_ore.json` $.pools[0].entries[0]: `{"type":"item","name":"effect:quartz_diamond","weight":89,"functions":[{"function":"set_count","count":{"min":1,"max":1}}]}`
  - `Swords_B/loot_tables/blocks/quartz_diamond_ore.json` $.pools[0].entries[1]: `{"type":"item","name":"effect:quartz_diamond","weight":10,"functions":[{"function":"set_count","count":{"min":1,"max":2}}]}`
  - `Swords_B/loot_tables/blocks/quartz_diamond_ore.json` $.pools[0].entries[2]: `{"type":"item","name":"effect:quartz_diamond","weight":1,"functions":[{"function":"set_count","count":{"min":2,"max":4}}]}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

**Условная математическая модель выбора loot в 2.x:**

Числа ниже — вероятность выбрать хотя бы одну запись предмета внутри уже активированного пула, а не шанс реальной добычи. Допущения: все записи доступны; отсутствующий вес принят за 1; quality и условия записей игнорируются; выборы независимы с возвращением; число rolls равномерно в указанном диапазоне. Условия пула считаются уже выполненными. Загрузка таблицы, дополнительный отбор, количество предметов и функции не эмулируются.

- Таблица/пул: `blocks/quartz_diamond_ore.json` / 0; entries: 0, 1, 2; rolls: `1`; вес ID/сумма: 100/100; выбор хотя бы одной записи по модели: **100.0000%**. Условия и оговорки: functions: `[{"function":"set_count","count":{"min":1,"max":1}}]`, `[{"function":"set_count","count":{"min":1,"max":2}}]`, `[{"function":"set_count","count":{"min":2,"max":4}}]`.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Quartz Diamond, палка и Quartz Sword (`effect:quartz_diamond`, `effect:quartz_diamond_stick`, `effect:quartz_sword`)

[Граф материалов и различия версий](manual-quartz-bedrock-progression.md#граф-крафта-2x-quartz-diamond).

- `items/quartz_diamond.json`: category items, max stack **9**, foil true, hand_equipped false; отображаемое имя служит также для тега `wish_1` на выброшенном предмете. Рецепт 3×3 из него создаёт `effect99:quartz_diamond_block`; две штуки вертикально → `effect:quartz_diamond_stick`.
- `blocks/quartz_diamond_ore.json`: destroy_time 10, explosion_resistance 999, absorption 15; on_player_destroyed проверяет имена iron/diamond/netherite pickaxe или bedrock_sword через буквальное выражение `q.get_equipped_item_name` без скобок. Spawn loot из `loot_tables/blocks/quartz_diamond_ore.json` выбирает один пул: вес 89 → count 1, вес 10 → count 1…2, вес 1 → count 2…4, все выдают quartz_diamond. Это условные веса 89/100, 10/100, 1/100, не распределение числа предметов без проверки set_count. Команды дополнительно шесть раз вызывают `summon xp_orb`, particle, `effect @p[r=6] instant_damage 1 0 true` — ближайшему игроку, не обязательно разрушителю.
- `blocks/quartz_diamond_block.json`: destroy_time 20, explosion_resistance 999, те же условия инструмента, loot на один блок, particle и instant_damage ближайшему игроку r=6; огнестойкие flammable odds 0. **Оба блока и silver ore ссылаются на отсутствующий в обоих 2.8.x архивах `loot_tables/blocks/null.json`**. Может существовать ресурс ванильного/другого пакета; эффект отсутствия не установлен. Не считать его гарантированно пустой таблицей. В 2.8.14 отсутствуют файловые feature/feature_rule кварцевой руды, содержащиеся в 2.8.8; естественная генерация не доказана.
- `items/quartz_diamond_stick.json`: damage 24, max durability 20, foil true, stack 1/offhand false, can_destroy_in_creative true. На все три weapon-хука случайный выбор 10/100 `damage @s 1 magic`, 85/100 — 3 magic, 5/100 — 6 magic. Явного durability damage в этом событии нет; стандартный расход движка не установлен. Отсутствие repairable/enchantable не равняется доказанному значению соответствующего свойства.
- `items/quartz_sword.json`: damage 600, durability 1, foil true, offhand false; repairable/enchantable отсутствуют. Рецепт `recipes/quartz_diamond_sword.json` имеет Q/Q/#: два `effect99:quartz_diamond_block` и stick с `data:0`. На все три weapon-хука последовательность durability damage 10, затем `effect @a[r=1] instant_damage 1 99 true` и particle; это воздействует на игроков в радиусе, а не формально команда убийства только владельца. Сенсор hand при переходе в family `quartz_sword` и при выходе выполняет `damage @s 14 magic` каждый раз при прохождении соответствующего family-фильтра (`player.json`). Порядок смены групп и успех damage следует проверить.
- `item.json:87–108,138–166`, `tag_swords.mcfunction`: отображаемое имя `Quartz Diamond` получает `wish_1`, `Quartz Diamond block` — `wish_2`; оба используют ту же точную геометрию фонтана, что wish_3 у Time Sword. У wish_1 success 8/1000, у wish_2 25/1000; в success обе ветки грузят `ultra_instinct_sword` на y+1, выполняют замену sand на concretepowder data 0 в объёме `~15 ~10 ~15`…`~-15 ~-15 ~-15`, частицы/звук и `kill @s`. Остальные 992/1000 и 975/1000 — частица и kill; это не безусловный шанс получения результата до проверки тегирования, команды и условий.

**Дополнительный подробный разбор** (источник: `docs/manual-quartz-bedrock-progression.md`):

#### Граф крафта 2.x: Quartz Diamond

| Рецепт | Pattern и key | Точный result в файле |
|---|---|---|
| `quartz_diamond_block` | `###/###/###`, # = `effect:quartz_diamond` | `effect99:quartz_diamond_block` |
| `quartz_diamond_stick` | `#/#`, # = `effect:quartz_diamond` | `effect:quartz_diamond_stick` |
| `quartz_diamond_sword` | `Q/Q/#`, Q = `effect99:quartz_diamond_block`, # = `effect:quartz_diamond_stick`, data 0 | `effect:quartz_sword` |

При **условных** допущениях, что все три рецепта зарегистрированы, каждый выполняется штатно и result без count даёт по одному предмету, на один меч по этой цепи нужно 2×9 + 2 = **20** Quartz Diamond. Это стоимость именно данных рецептов, не утверждение о единственном пути в мире или проверенной семантике отсутствующего count. `quartz_diamond` stack 9 и сам является предметом; `quartz_diamond_block` — отдельный блок; `quartz_diamond_stick` — отдельный item damage 24, durability 20, offhand false. У палки три weapon-хука randomize 10/85/5 на `damage @s` 1/3/6 magic соответственно; direct durability damage в этих ветвях не объявлен. При стандартном выборе условное среднее заявленного magic damage = **2.95** на вызов; нельзя добавлять предполагаемый штатный износ или превращать это в средний урон на секунду.

`effect99:quartz_diamond_ore` при условии on_player_destroyed проверяет буквальное Molang-выражение для iron/diamond/netherite pickaxe или bedrock_sword, без скобок вызова; при активации события запрашивает отдельную таблицу. Она даёт один выбор с весами 89/10/1 и set_count 1…1/1…2/2…4 для `effect:quartz_diamond`, а также event содержит шесть команд summon XP-orb и instant_damage ближайшему `@p[r=6]`. Эти веса — не вероятность нахождения руды или гарантия успеха loot. Базовый `minecraft:loot` ссылается на отсутствующий в обоих архивах `loot_tables/blocks/null.json`, отдельно от таблицы события: внешний/ванильный путь не исключён.

Только архив 2.8.8 содержит соответствующие feature и feature_rule: 5 iterations, scatter 160/200, biome overworld или the_end, y gaussian extent `[0,16]`, allowlist stone/end_stone, структура `mystructure:quartz_diamond_ore`; файл структуры 1×1×1 с этим блоком есть. В 2.8.14 отсутствуют и оба файла feature/feature_rule, и файл этой структуры, хотя block и loot существуют. Имя структуры, регистрация и среда могут зависеть от движка/других пакетов; 160/200 не является шансом появления руды на блок или чанк.

### Что написано на скриншотах

Сопоставленной карточки чисел на скриншотах нет; это не значит, что предмет нигде на изображениях не упомянут.

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 26. Quartz Diamond Stick — `effect:quartz_diamond_stick`

**Кратко:** Материал для Quartz Sword; события могут наносить magic-урон игроку. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

- В 1.6 предмет с этим точным ID не найден.

**2.8.8 / 2.8.14** — определение `Swords_B/items/quartz_diamond_stick.json`.
- урон: `24`; максимальная прочность: `{"max_durability":20}`; зачарование: не указан; перезарядка: не указан; левая рука: `false`; размер стопки: `1`; свечение: `true`; предмет исчезает: не указан.
- Ремонт: компонент не указан; это не доказывает невозможности ремонта.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`; событие без нанесения урона существу → `{"event":"weapon"}`; удар по блоку → `{"event":"weapon"}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 2.8.14:**

- Рецепт `Swords_B/recipes/quartz_diamond_stick.json`; тип `minecraft:recipe_shaped`.
  - Схема сверху вниз: `#` / `#`.
  - Обозначения: `{"#":{"item":"effect:quartz_diamond"}}`.
  - Результат: `{"item":"effect:quartz_diamond_stick"}`; рабочие станции/tags: `["crafting_table"]`.

- Определение: `Swords_B/items/quartz_diamond_stick.json`.
- Результаты рецептов: `Swords_B/recipes/quartz_diamond_stick.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Quartz Diamond, палка и Quartz Sword (`effect:quartz_diamond`, `effect:quartz_diamond_stick`, `effect:quartz_sword`)

[Граф материалов и различия версий](manual-quartz-bedrock-progression.md#граф-крафта-2x-quartz-diamond).

- `items/quartz_diamond.json`: category items, max stack **9**, foil true, hand_equipped false; отображаемое имя служит также для тега `wish_1` на выброшенном предмете. Рецепт 3×3 из него создаёт `effect99:quartz_diamond_block`; две штуки вертикально → `effect:quartz_diamond_stick`.
- `blocks/quartz_diamond_ore.json`: destroy_time 10, explosion_resistance 999, absorption 15; on_player_destroyed проверяет имена iron/diamond/netherite pickaxe или bedrock_sword через буквальное выражение `q.get_equipped_item_name` без скобок. Spawn loot из `loot_tables/blocks/quartz_diamond_ore.json` выбирает один пул: вес 89 → count 1, вес 10 → count 1…2, вес 1 → count 2…4, все выдают quartz_diamond. Это условные веса 89/100, 10/100, 1/100, не распределение числа предметов без проверки set_count. Команды дополнительно шесть раз вызывают `summon xp_orb`, particle, `effect @p[r=6] instant_damage 1 0 true` — ближайшему игроку, не обязательно разрушителю.
- `blocks/quartz_diamond_block.json`: destroy_time 20, explosion_resistance 999, те же условия инструмента, loot на один блок, particle и instant_damage ближайшему игроку r=6; огнестойкие flammable odds 0. **Оба блока и silver ore ссылаются на отсутствующий в обоих 2.8.x архивах `loot_tables/blocks/null.json`**. Может существовать ресурс ванильного/другого пакета; эффект отсутствия не установлен. Не считать его гарантированно пустой таблицей. В 2.8.14 отсутствуют файловые feature/feature_rule кварцевой руды, содержащиеся в 2.8.8; естественная генерация не доказана.
- `items/quartz_diamond_stick.json`: damage 24, max durability 20, foil true, stack 1/offhand false, can_destroy_in_creative true. На все три weapon-хука случайный выбор 10/100 `damage @s 1 magic`, 85/100 — 3 magic, 5/100 — 6 magic. Явного durability damage в этом событии нет; стандартный расход движка не установлен. Отсутствие repairable/enchantable не равняется доказанному значению соответствующего свойства.
- `items/quartz_sword.json`: damage 600, durability 1, foil true, offhand false; repairable/enchantable отсутствуют. Рецепт `recipes/quartz_diamond_sword.json` имеет Q/Q/#: два `effect99:quartz_diamond_block` и stick с `data:0`. На все три weapon-хука последовательность durability damage 10, затем `effect @a[r=1] instant_damage 1 99 true` и particle; это воздействует на игроков в радиусе, а не формально команда убийства только владельца. Сенсор hand при переходе в family `quartz_sword` и при выходе выполняет `damage @s 14 magic` каждый раз при прохождении соответствующего family-фильтра (`player.json`). Порядок смены групп и успех damage следует проверить.
- `item.json:87–108,138–166`, `tag_swords.mcfunction`: отображаемое имя `Quartz Diamond` получает `wish_1`, `Quartz Diamond block` — `wish_2`; оба используют ту же точную геометрию фонтана, что wish_3 у Time Sword. У wish_1 success 8/1000, у wish_2 25/1000; в success обе ветки грузят `ultra_instinct_sword` на y+1, выполняют замену sand на concretepowder data 0 в объёме `~15 ~10 ~15`…`~-15 ~-15 ~-15`, частицы/звук и `kill @s`. Остальные 992/1000 и 975/1000 — частица и kill; это не безусловный шанс получения результата до проверки тегирования, команды и условий.

**Дополнительный подробный разбор** (источник: `docs/manual-quartz-bedrock-progression.md`):

#### Граф крафта 2.x: Quartz Diamond

| Рецепт | Pattern и key | Точный result в файле |
|---|---|---|
| `quartz_diamond_block` | `###/###/###`, # = `effect:quartz_diamond` | `effect99:quartz_diamond_block` |
| `quartz_diamond_stick` | `#/#`, # = `effect:quartz_diamond` | `effect:quartz_diamond_stick` |
| `quartz_diamond_sword` | `Q/Q/#`, Q = `effect99:quartz_diamond_block`, # = `effect:quartz_diamond_stick`, data 0 | `effect:quartz_sword` |

При **условных** допущениях, что все три рецепта зарегистрированы, каждый выполняется штатно и result без count даёт по одному предмету, на один меч по этой цепи нужно 2×9 + 2 = **20** Quartz Diamond. Это стоимость именно данных рецептов, не утверждение о единственном пути в мире или проверенной семантике отсутствующего count. `quartz_diamond` stack 9 и сам является предметом; `quartz_diamond_block` — отдельный блок; `quartz_diamond_stick` — отдельный item damage 24, durability 20, offhand false. У палки три weapon-хука randomize 10/85/5 на `damage @s` 1/3/6 magic соответственно; direct durability damage в этих ветвях не объявлен. При стандартном выборе условное среднее заявленного magic damage = **2.95** на вызов; нельзя добавлять предполагаемый штатный износ или превращать это в средний урон на секунду.

`effect99:quartz_diamond_ore` при условии on_player_destroyed проверяет буквальное Molang-выражение для iron/diamond/netherite pickaxe или bedrock_sword, без скобок вызова; при активации события запрашивает отдельную таблицу. Она даёт один выбор с весами 89/10/1 и set_count 1…1/1…2/2…4 для `effect:quartz_diamond`, а также event содержит шесть команд summon XP-orb и instant_damage ближайшему `@p[r=6]`. Эти веса — не вероятность нахождения руды или гарантия успеха loot. Базовый `minecraft:loot` ссылается на отсутствующий в обоих архивах `loot_tables/blocks/null.json`, отдельно от таблицы события: внешний/ванильный путь не исключён.

Только архив 2.8.8 содержит соответствующие feature и feature_rule: 5 iterations, scatter 160/200, biome overworld или the_end, y gaussian extent `[0,16]`, allowlist stone/end_stone, структура `mystructure:quartz_diamond_ore`; файл структуры 1×1×1 с этим блоком есть. В 2.8.14 отсутствуют и оба файла feature/feature_rule, и файл этой структуры, хотя block и loot существуют. Имя структуры, регистрация и среда могут зависеть от движка/других пакетов; 160/200 не является шансом появления руды на блок или чанк.

### Что написано на скриншотах

На изображении вручную считаны: damage = `24`; durability = `20`. Оригинал: [скриншот 120034](https://drive.google.com/file/d/14nhZwfS8-jwjz2vOlAQQd2-LXzlnE2l4/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 27. Quartz Sword — `effect:quartz_sword`

**Кратко:** Записан урон 600 и прочность 1; путь через кварцевые материалы. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

**1.6** — определение `Sword_B/items/quartz_sword.json`.
- урон: `600`; максимальная прочность: `{"max_durability":1}`; зачарование: не указан; перезарядка: не указан; левая рука: `true`; размер стопки: `1`; свечение: не указан; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:quartz_sword"]` → `1`.
- Оружейный компонент не указан.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**2.8.8 / 2.8.14** — определение `Swords_B/items/quartz_sword.json`.
- урон: `600`; максимальная прочность: `{"max_durability":1}`; зачарование: не указан; перезарядка: не указан; левая рука: `false`; размер стопки: `1`; свечение: `true`; предмет исчезает: не указан.
- Ремонт: компонент не указан; это не доказывает невозможности ремонта.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`; событие без нанесения урона существу → `{"event":"weapon"}`; удар по блоку → `{"event":"weapon"}`.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 1.6:**

- Рецепт `Sword_B/recipes/quartz_sword.json`; тип `minecraft:recipe_shaped`.
  - Схема сверху вниз: `#` / `#` / `0`.
  - Обозначения: `{"#":{"item":"minecraft:quartz_block","data":0},"0":{"item":"minecraft:stick","data":0}}`.
  - Результат: `[{"item":"effect:quartz_sword","data":0,"count":1}]`; рабочие станции/tags: `["crafting_table"]`.

- Определение: `Sword_B/items/quartz_sword.json`.
- Результаты рецептов: `Sword_B/recipes/quartz_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

**Архив 2.8.14:**

- Рецепт `Swords_B/recipes/quartz_diamond_sword.json`; тип `minecraft:recipe_shaped`.
  - Схема сверху вниз: `Q` / `Q` / `#`.
  - Обозначения: `{"#":{"item":"effect:quartz_diamond_stick","data":0},"Q":{"item":"effect99:quartz_diamond_block"}}`.
  - Результат: `{"item":"effect:quartz_sword"}`; рабочие станции/tags: `["crafting_table"]`.

- Определение: `Swords_B/items/quartz_sword.json`.
- Результаты рецептов: `Swords_B/recipes/quartz_diamond_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[21].Mainhand[0].Name

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Quartz Diamond, палка и Quartz Sword (`effect:quartz_diamond`, `effect:quartz_diamond_stick`, `effect:quartz_sword`)

[Граф материалов и различия версий](manual-quartz-bedrock-progression.md#граф-крафта-2x-quartz-diamond).

- `items/quartz_diamond.json`: category items, max stack **9**, foil true, hand_equipped false; отображаемое имя служит также для тега `wish_1` на выброшенном предмете. Рецепт 3×3 из него создаёт `effect99:quartz_diamond_block`; две штуки вертикально → `effect:quartz_diamond_stick`.
- `blocks/quartz_diamond_ore.json`: destroy_time 10, explosion_resistance 999, absorption 15; on_player_destroyed проверяет имена iron/diamond/netherite pickaxe или bedrock_sword через буквальное выражение `q.get_equipped_item_name` без скобок. Spawn loot из `loot_tables/blocks/quartz_diamond_ore.json` выбирает один пул: вес 89 → count 1, вес 10 → count 1…2, вес 1 → count 2…4, все выдают quartz_diamond. Это условные веса 89/100, 10/100, 1/100, не распределение числа предметов без проверки set_count. Команды дополнительно шесть раз вызывают `summon xp_orb`, particle, `effect @p[r=6] instant_damage 1 0 true` — ближайшему игроку, не обязательно разрушителю.
- `blocks/quartz_diamond_block.json`: destroy_time 20, explosion_resistance 999, те же условия инструмента, loot на один блок, particle и instant_damage ближайшему игроку r=6; огнестойкие flammable odds 0. **Оба блока и silver ore ссылаются на отсутствующий в обоих 2.8.x архивах `loot_tables/blocks/null.json`**. Может существовать ресурс ванильного/другого пакета; эффект отсутствия не установлен. Не считать его гарантированно пустой таблицей. В 2.8.14 отсутствуют файловые feature/feature_rule кварцевой руды, содержащиеся в 2.8.8; естественная генерация не доказана.
- `items/quartz_diamond_stick.json`: damage 24, max durability 20, foil true, stack 1/offhand false, can_destroy_in_creative true. На все три weapon-хука случайный выбор 10/100 `damage @s 1 magic`, 85/100 — 3 magic, 5/100 — 6 magic. Явного durability damage в этом событии нет; стандартный расход движка не установлен. Отсутствие repairable/enchantable не равняется доказанному значению соответствующего свойства.
- `items/quartz_sword.json`: damage 600, durability 1, foil true, offhand false; repairable/enchantable отсутствуют. Рецепт `recipes/quartz_diamond_sword.json` имеет Q/Q/#: два `effect99:quartz_diamond_block` и stick с `data:0`. На все три weapon-хука последовательность durability damage 10, затем `effect @a[r=1] instant_damage 1 99 true` и particle; это воздействует на игроков в радиусе, а не формально команда убийства только владельца. Сенсор hand при переходе в family `quartz_sword` и при выходе выполняет `damage @s 14 magic` каждый раз при прохождении соответствующего family-фильтра (`player.json`). Порядок смены групп и успех damage следует проверить.
- `item.json:87–108,138–166`, `tag_swords.mcfunction`: отображаемое имя `Quartz Diamond` получает `wish_1`, `Quartz Diamond block` — `wish_2`; оба используют ту же точную геометрию фонтана, что wish_3 у Time Sword. У wish_1 success 8/1000, у wish_2 25/1000; в success обе ветки грузят `ultra_instinct_sword` на y+1, выполняют замену sand на concretepowder data 0 в объёме `~15 ~10 ~15`…`~-15 ~-15 ~-15`, частицы/звук и `kill @s`. Остальные 992/1000 и 975/1000 — частица и kill; это не безусловный шанс получения результата до проверки тегирования, команды и условий.

**Старая версия 1.6** (источник: `docs/manual-traces-1.6.md`):

- **Quartz** — 600/1, glint true, enchantable в компонентах отсутствует, ремонт самим собой 1. Сенсор добавляет пустую `minecraft:quartz_sword` component group; в данной прямой цепи spawn/controller нет. Это не доказательство отсутствия любых других связей.

**Дополнительный подробный разбор** (источник: `docs/manual-quartz-bedrock-progression.md`):

#### Quartz Sword: одинаковый ID, разные рецепты и побочные эффекты

`effect:quartz_sword` есть в обоих поколениях: damage 600, max durability 1, stack 1 и web/bamboo 15/10. В 1.6 `glint:true`, offhand true и repair self 1; enchantable не объявлен. В 2.x `foil:true`, offhand false, repairable и enchantable не объявлены. Отсутствие компонента не означает доказанной невозможности ремонта или зачарования на произвольном движке.

1.6 `recipes/quartz_sword.json`: pattern `#/#/0` (три однобуквенных ряда), `# = minecraft:quartz_block` data 0, `0 = minecraft:stick` data 0; **result записан массивом** из одного объекта `effect:quartz_sword`, data 0, count 1. Нужно сохранить и этот тип result, не предполагать, что конкретный загрузчик принимает массив. Player sensor добавляет пустую группу `minecraft:quartz_sword`; в item нет `minecraft:weapon` и on-use. Это только локальная прямая цепь, а не доказательство отсутствия внешних эффектов.

2.x `recipes/quartz_diamond_sword.json`: `Q/Q/#`, Q = `effect99:quartz_diamond_block`, # = `effect:quartz_diamond_stick` data 0, result = `effect:quartz_sword`. На три weapon-хука: в sequence сначала direct durability damage 10, затем `effect @a[r=1] instant_damage 1 99 true` и particle. Это selector **всех игроков** в радиусе, не команда строго по владельцу. Player hand-event при отсутствии family `quartz_sword` задаёт `damage @s 14 magic` и добавляет группу; stop при наличии этой family снова задаёт `damage @s 14 magic`, снимает группу и добавляет default_player. Конфликт family, порядок соседних полей и успех damage не установлены.

### Что написано на скриншотах

На изображении вручную считаны: damage = `600`; durability = `1`; enchantable = `false`; repairable = `false`. Оригинал: [скриншот 120003](https://drive.google.com/file/d/1tAeJ-EbPeExgoe9AX_AR_p9cgZEangmO/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 28. Sea Sword — `effect:sea_sword`

**Кратко:** Связан с дыханием и передвижением в воде и вне воды. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

**1.6** — определение `Sword_B/items/sea_sword.json`.
- урон: `7`; максимальная прочность: `{"max_durability":1000}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `true`; размер стопки: `1`; свечение: не указан; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:sea_sword"]` → `1000`.
- Оружейный компонент не указан.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**2.8.8 / 2.8.14** — определение `Swords_B/items/sea_sword.json`.
- урон: `7`; максимальная прочность: `{"max_durability":1356}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `false`; размер стопки: `1`; свечение: `true`; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:sea_sword"]` → `1356`; `["minecraft:heart_of_the_sea"]` → `482`.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 1.6:**

- Рецепт `Sword_B/recipes/sea_sword.json`; тип `minecraft:recipe_shaped`.
  - Схема сверху вниз: `F` / `F` / `E`.
  - Обозначения: `{"E":{"item":"minecraft:prismarine_shard"},"F":{"item":"minecraft:heart_of_the_sea"}}`.
  - Результат: `{"item":"effect:sea_sword"}`; рабочие станции/tags: `["crafting_table"]`.

- Определение: `Sword_B/items/sea_sword.json`.
- Результаты рецептов: `Sword_B/recipes/sea_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

**Архив 2.8.14:**

- Рецептов с этим точным результатом локально не найдено. Это не исключает других путей.

- Определение: `Swords_B/items/sea_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - `Swords_B/loot_tables/chests/buriedtreasure.json` $.pools[1].entries[8]: `{"type":"item","name":"effect:sea_sword","weight":15}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[6].Mainhand[0].Name

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

**Условная математическая модель выбора loot в 2.x:**

Числа ниже — вероятность выбрать хотя бы одну запись предмета внутри уже активированного пула, а не шанс реальной добычи. Допущения: все записи доступны; отсутствующий вес принят за 1; quality и условия записей игнорируются; выборы независимы с возвращением; число rolls равномерно в указанном диапазоне. Условия пула считаются уже выполненными. Загрузка таблицы, дополнительный отбор, количество предметов и функции не эмулируются.

- Таблица/пул: `chests/buriedtreasure.json` / 1; entries: 8; rolls: `{"min":5,"max":12}`; вес ID/сумма: 15/219; выбор хотя бы одной записи по модели: **44.5623%**. Условия и оговорки: functions: не задано.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Sea Sword (`effect:sea_sword`)

[Пошаговые условия и отсутствие явного удаления out-water](manual-sea-sword.md). Фильтры `in_water` не содержат явного `value`; интерпретацию нужно проверить в движке.

- `items/sea_sword.json`: damage 7, durability 1356, foil true, enchantability 9/sword, repair self 1356/heart_of_the_sea 482, offhand false, on_hurt_entity durability 1, web 15/bamboo 10.
- `player.json`: группа sea_sword — collision 0.6×0.9, family `[player,sea_sword]`, looping timer `[0.5,0.5]`; breathable total_supply 2, suffocate_time −1, inhale_time 3.75, `breathes_water:true`, `breathes_air:false`, `breathes_lava:false`, bubbles false. Вне воды добавляется группа `mermaid_movement_out_water` movement 0.06, camerashake 0.01/1 и очистка conduit_power; таймер вне воды воспроизводит fish.flop для `@a[r=12]`. В воде добавляется `mermaid_movement_in_water` underwater_movement 0.07 и conduit_power 1 с amplifier 0. Стоп удаляет sea_sword и in-water группу, добавляет default_player, particle/звук и чистит conduit_power; явного удаления **out-water** группы в этом событии нет. Фактическое дыхание, возобновление движения и переключение сред требуют игры.
- `loot_tables/chests/buriedtreasure.json`: pool индекс 1, 5–12 rolls, weight 15 из явно заданной суммы 219, или 15/219 на один выбор при стандартной семантике; не шанс на сундук.

**Старая версия 1.6** (источник: `docs/manual-traces-1.6.md`):

#### Sea Sword: подробная цепочка 1.6 и группы 2.x

[Helper и эффекты 1.6; водные группы, условия и конфликт восстановления 2.x](manual-sea-sword.md). Это статическая реконструкция с незаданными в фильтрах значениями.

**Дополнительный подробный разбор** (источник: `docs/manual-sea-sword.md`):

### Sea Sword: цепь 1.6 и группы воды 2.x

Статическая реконструкция архивов; названия версий здесь соответствуют именам файлов. Срабатывание сенсоров, приоритет component groups, таймеры, команды, дыхание и реальный лут Bedrock не проверены. Основные выписки: [1.6](items-1.6.md#effectsea_sword), [2.8.14](items-2.8.14.md#effectsea_sword), [player-группы 2.8.14](player-groups-2.8.14.md).

#### Предмет и источники

| Поле в item JSON | 1.6 | 2.8.8 / 2.8.14 |
|---|---|---|
| ID / damage | `effect:sea_sword` / 7 | тот же / 7 |
| durability / self repair amount | 1000 / 1000 | 1356 / 1356 |
| Дополнительный ремонт | не задан | `minecraft:heart_of_the_sea`, 482 |
| off-hand / enchantable | true / `{value:9,slot:sword}` | false / тот же объект |
| glint/foil | `minecraft:glint:true` | `minecraft:foil:true`; эквивалентность не доказана |
| Digger | web 15, bamboo 10, use_efficiency true | те же объявленные значения |

Максимальный stack 1, hand_equipped true и can_destroy_in_creative false записаны в обеих версиях. В 2.x item `minecraft:weapon` содержит `on_hurt_entity` → weapon-event с durability damage **1**; не приписывать этот item-hook старой версии автоматически. Ни одна запись выше сама по себе не гарантирует исполнение или игровые значения.

1.6 содержит shaped recipe с pattern `F / F / E`, `F=minecraft:heart_of_the_sea`, `E=minecraft:prismarine_shard`, результат `effect:sea_sword`. Прямые локальные loot/trade/структуры этого ID не найдены. В 2.x локальный рецепт не найден, а таблица `chests/buriedtreasure.json` содержит меч и отдельно heart_of_the_sea; см. [получение 1.6](acquisition-index-1.6.md#effectsea_sword) / [2.8.14](acquisition-index-2.8.14.md#effectsea_sword). Значки 1.6 и 2.8.14 — одинаковый байтовый PNG 16×16 ([аудит](icon-comparison.md)); рендер в движке не проверен.

#### 1.6: helper и эффекты не обязательно владельцу

- `player.json`: sensor `has_equipment`, self, domain `hand`, value `effect:sea_sword` → `minecraft:sea_sword`, добавляет одноимённую группу. Она объявляет `minecraft:spawn_entity`: `entity:sea`, wait **0/0**, `num_to_spawn:1`, `single_use:true`. Общий `minecraft:event_normal_player` удаляет эту группу, поэтому количество/период spawn не выводятся из одного `single_use`.
- `entities/sea.json`: helper family `despawnear`, despawn filter на ту же family, health **1**, collision width/height **0/0**, fire immune true, physics `{}`; summonable true, spawnable false. `scripts.animate` `sea` → `controller.animation.sea`.
- `animation_controllers/sea_sword.json`: `default` ↔ `sea` с переходами `(1.0)` и одинаковыми четырьмя строками `on_entry` в каждом: `/effect @e[type=guardian,r=6] fatal_poison 5 0 true`, аналог для `drowned`, `/effect @p conduit_power 16 0 true`, `/scoreboard players set @a swords 2`. Числа в командах effect — duration **5**/**16**, amplifier **0**, `true`; единицы и совместимость старой команды проверять в движке.
- Guardian и drowned выбираются в r=6 от контекста helper. `@p` означает ближайшего игрока относительно контекста, не гарантированно того, кто вызвал helper; команда scoreboard касается всех `@a`. В списке нет отдельной команды `elder_guardian` и нет проверки «игрок в воде». Не предполагать, что эффект poison действует на все морские виды, что эффект применяется раз в фиксированное время или что владелец всегда выбран.

#### 2.x: события и фактические объявления групп

В обоих 2.x сравниваемые здесь sensor, sea events и группы одинаковы структурно, хотя `player.json` целиком между версиями отличается по Ice. Условия `in_water` **не содержат явного поля `value`**: вневодная ветвь и sound задают `{"test":"in_water","operator":"!="}`, водная — `{"test":"in_water"}`. Ниже «вода / вне воды» — вероятное предназначение, не доказательство того, как движок интерпретирует отсутствующий value или operator.

| Вход / условие | Буквальные операции |
|---|---|
| sensor has_equipment hand = Sea | event `minecraft:sea_sword` |
| Первый шаг event: `in_water`, `operator:!=`, value отсутствует | add `mermaid_movement_out_water`, movement value **0.06**; `camerashake add @s 0.01 1 positional`; `effect @s conduit_power 0 0` |
| Второй шаг: self family `!= sea_sword` | add `minecraft:sea_sword`, particle `minecraft:example_bounce`, `playsound random.splash @a[r=12] ~ ~ ~ 0.5` |
| Третий шаг: `in_water`, value отсутствует | add `mermaid_movement_in_water`, underwater_movement value **0.07**; `effect @s conduit_power 1 0 true` |
| sensor has_equipment hand `!=` Sea | event `stop_sea_sword_event` |
| Stop при self family `== sea_sword` | remove `minecraft:sea_sword` и `mermaid_movement_in_water`; add `minecraft:default_player`; частица/звук, `effect @s conduit_power 0 0` |
| Timer event `sea_sword_sound`, `in_water`, operator `!=`, value отсутствует | `playsound mob.fish.flop @a[r=12] ~ ~ ~ 1 0.6` |

`minecraft:sea_sword` содержит collision width **0.6**, height **0.9**, family `[player,sea_sword]`, looping timer `[0.5,0.5]` с `sea_sword_sound`, breathable total_supply **2**, suffocate_time **−1**, inhale_time **3.75**, generates_bubbles false, breathes_water true, breathes_air false, breathes_lava false. Значение timer не является доказанной частотой звука при длительном удержании: есть фильтр, повторное добавление группы и возможные конфликты компонентов.

##### Неполное явное снятие групп

В имеющихся JSON, mcfunction и JS обоих 2.x буквальное имя `mermaid_movement_out_water` встречается только в определении и в `add` вышеприведённой ветви; его **явного remove в этих файлах не найдено**. При ветви воды `mermaid_movement_in_water` добавляется без явного удаления out-water; при выходе добавляется out-water без явного удаления in-water; stop явно удаляет только in-water вместе с sea group. Это перечисление операций в источнике, а не доказательство, что обе группы фактически сохраняются и складываются в движке.

Особенно важно: stop добавляет `minecraft:default_player`, где объявлены movement **0.1**, underwater_movement **0.02**, collision **0.6×1.8**, breathable total_supply **15**, inhale_time **3.75**, suffocate_time **−1**. Если движок допускает совместное наличие или замену групп с одинаковыми компонентами, приоритет значений и фактическое восстановление зависят от движка и порядка событий. Проверить последовательности «взять на суше → войти в воду → выйти → убрать меч», «взять в воде → выйти → убрать», быстрое переключение и несколько игроков. Не обещать ни постоянного замедления, ни гарантированного восстановления по одному отсутствию remove.

#### Условная модель получения из buried treasure 2.x

Файл `Swords_B/loot_tables/chests/buriedtreasure.json` одинаков побайтово в обеих 2.x. Pool 0: **1** roll, одна запись `minecraft:heart_of_the_sea`, без указанного weight. Pool 1: rolls **5…12**, у 19 записей все веса явно заданы, их сумма **219**, у Sea Sword **15**, отсутствует функция set_count в самой записи. При стандартной модели весов один выбор даёт `15/219 = 5/73 ≈ 6.8493%`.

Если дополнительно предположить равномерный выбор целого числа rolls в диапазоне 5…12, независимые выборы с возвращением, отсутствие модификаторов и успешную регистрацию/применение именно этой таблицы, вероятность хотя бы одной выбранной записи — среднее `1 − (1 − 15/219)^n` по n=5…12, то есть **≈44.5623%**, математическое ожидание числа выбранных записей ≈**0.5822**. Это не измеренная вероятность конкретного сундука или мира: генерация структуры, выбор таблицы, регистрация предмета и правила игры остаются непроверенными. Наличие heart_of_the_sea в отдельном pool не доказывает, что 1.6-рецепт присутствует в 2.x.

### Что написано на скриншотах

На изображении вручную считаны: damage = `7`; durability = `1356`; enchantable = `true`; repairable = `true`. Оригинал: [скриншот 115830](https://drive.google.com/file/d/1u4b1golY1UN59CFF3zifu2aqiLwI5ypW/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 29. Shulker Sword — `effect:shulker_sword`

**Кратко:** Снаряд шалкера, левитация и отдельная цепочка щита. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

**1.6** — определение `Sword_B/items/shulker_sword.json`.
- урон: `7`; максимальная прочность: `{"max_durability":1000}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `true`; размер стопки: `1`; свечение: не указан; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:shulker_sword"]` → `1000`.
- Оружейный компонент не указан.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**2.8.8 / 2.8.14** — определение `Swords_B/items/shulker_sword.json`.
- урон: `6`; максимальная прочность: `{"max_durability":2609}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: `{"category":"shulker_sword","duration":8}`; левая рука: `false`; размер стопки: `1`; свечение: `false`; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:shulker_sword"]` → `2609`.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`; событие без нанесения урона существу → `{"event":"weapon"}`; удар по блоку → `{"event":"weapon"}`.
- При использовании предмета указано: `{"on_use":{"event":"on_use"}}`.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 1.6:**

- Рецепт `Sword_B/recipes/shulker_sword.json`; тип `minecraft:recipe_shaped`.
  - Схема сверху вниз: `F` / `F` / `E`.
  - Обозначения: `{"E":{"item":"minecraft:end_rod"},"F":{"item":"minecraft:shulker_shell"}}`.
  - Результат: `{"item":"effect:shulker_sword"}`; рабочие станции/tags: `["crafting_table"]`.

- Определение: `Sword_B/items/shulker_sword.json`.
- Результаты рецептов: `Sword_B/recipes/shulker_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

**Архив 2.8.14:**

- Рецептов с этим точным результатом локально не найдено. Это не исключает других путей.

- Определение: `Swords_B/items/shulker_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - `Swords_B/loot_tables/entities/shulker.json` $.pools[1].entries[0]: `{"type":"item","name":"effect:shulker_sword","weight":1,"functions":[{"function":"set_count","count":{"min":1,"max":1}},{"function":"set_data","data":0}]}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[3].Mainhand[0].Name

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

**Условная математическая модель выбора loot в 2.x:**

Числа ниже — вероятность выбрать хотя бы одну запись предмета внутри уже активированного пула, а не шанс реальной добычи. Допущения: все записи доступны; отсутствующий вес принят за 1; quality и условия записей игнорируются; выборы независимы с возвращением; число rolls равномерно в указанном диапазоне. Условия пула считаются уже выполненными. Загрузка таблицы, дополнительный отбор, количество предметов и функции не эмулируются.

- Таблица/пул: `entities/shulker.json` / 1; entries: 0; rolls: `1`; вес ID/сумма: 1/1; выбор хотя бы одной записи по модели: **100.0000%**. Условия и оговорки: pool conditions: `[{"condition":"killed_by_player"},{"condition":"random_chance_with_looting","chance":0.045,"looting_multiplier":0.02}]`; functions: `[{"function":"set_count","count":{"min":1,"max":1}},{"function":"set_data","data":0}]`.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Shulker Sword (`effect:shulker_sword`)

[Сопоставление предмета и цепочек 1.6/2.x](manual-companion-projectile-swords.md#shulker-sword).

- `items/shulker_sword.json`: damage 6, durability 2609, enchantability 9/sword, cooldown 8, ремонт self 2609, offhand false, web 15/bamboo 10. Все три weapon-хука: durability 1, затем 10/100 shoot `minecraft:shulker_bullet` power 1 и звук, 90/100 пусто. On use — восемь частиц на перечисленных x/z координатах, `effect @e[r=6,family=!shulker_sword] levitation 1 18 false` и отдельная durability damage 8. Селектор не ограничен монстрами и исключает любую сущность соответствующей family, не только владельца.
- `entities/shulker_bullet.json`: по умолчанию impact 4, levitation durations easy/normal/hard 200, amplifier 1, projectile gravity 0.05, homing true; при entity_spawned с `other` держащим sword добавляется группа с gravity 0.01, homing false и destroyOnHurt false. Проверять `other`, единицы duration и порядок групп, а не приписывать всем снарядам одинаковые значения.
- `animation_controllers/shulker_sword.json`: `q.get_equipped_item_name=='shulker_sword' && q.is_sneaking` вызывает `@s shulker_sword_skill`; эта группа игрока включает damage_sensor cause all/deals_damage false, scale 0.7, family `[player,shulker_sword]`, а команда `ride @s summon_ride entity:shulker_shield no_ride_change` создаёт средство передвижения. `entities/shulker_shield.json`: runtime shulker, health 20, collision 0.6×0.9, family `[effect99_entities,player,shulker_sword]`, одно место для player; при смерти `effect @p[r=1,family=shulker_sword] instant_damage 1 2 true`. Контроллер без rider вызывает событие shield `minecraft:despawn`, оно посылает stop ближайшему `@p[family=shulker_sword,r=6]`, не обязательно прежнему пассажиру. Stop игрока явно снимает `minecraft:shulker_sword`, но не `shulker_sword_skill`; не гарантировать немедленное снятие неуязвимости без тестов семей/групп.
- `loot_tables/entities/shulker.json`: пул killed_by_player с chance 0.045, looting_multiplier 0.02, 1 roll, меч 1; ванильную привязку таблицы, влияние looting и применение пакета проверить.

**Старая версия 1.6** (источник: `docs/manual-traces-1.6.md`):

- **Shulker** — 7/1000; ближайшему игроку levitation 0, все `entity:shulker2` телепортируются к нему на y+2.5; глобальный objective sh, score 40 summon, 2390 команда kill с дополнительными `~ 0 ~`, 2400 удалить objective. `shulker2.json` не разобран JSON5; факт работы не установлен.

**Дополнительный подробный разбор** (источник: `docs/manual-companion-projectile-swords.md`):

#### Shulker Sword

**Предмет и получение.** 1.6 damage 7, durability/self repair 1000, рецепт `F/F/E`, F = `minecraft:shulker_shell`, E = `minecraft:end_rod`. В 2.x damage 6, durability/self repair 2609, cooldown category `shulker_sword`, duration 8. Прямого рецепта с точным результатом в локальных 2.x нет; `loot_tables/entities/shulker.json` имеет отдельный pool с `killed_by_player`, chance 0.045, looting_multiplier 0.02 и одним roll меча. Явное подключение этой таблицы к локальному определению shulker не найдено; ванильную привязку не считать доказанной.

**1.6.** Player → `entity:shulker` → `controller.animation.shulker`: `effect @p levitation 0 0 true`, tp всех выбираемых `entity:shulker2` к `@p` y+2.5; global objective `sh`, увеличение score `@p`, summon при 40, удаление objective при 2400 **до** проверки kill с лишними `~ 0 ~` при 2390, `@a swords=2`. `entities/shulker2.json` диагностически разбирается только после удаления последней `}` в памяти; объявлены цель monster и shooter `minecraft:shulker_bullet`. Корректность архивного JSON и старой kill-команды не установлена.

**2.x.** Три weapon-хука задают расход 1, затем 10/100 `shoot minecraft:shulker_bullet` и звук / 90/100 пусто. On-use отдельно задаёт расход 8, восемь частиц и `effect @e[r=6,family=!shulker_sword] levitation 1 18 false`: selector не ограничивается враждебными существами и исключает **всю** эту family. Animation controller при sneaking вызывает `shulker_sword_skill`: группа player содержит `cause:all, deals_damage:false`, scale 0.7, family `[player,shulker_sword]`; команда `ride @s summon_ride entity:shulker_shield no_ride_change`. Shield runtime shulker, health 20, одно место для player; при смерти `instant_damage` получает ближайший `@p[r=1,family=shulker_sword]`, не доказано, что это исходный владелец. При despawn shield посылает stop ближайшему подходящему игроку в радиусе 6; stop игрока явно удаляет `minecraft:shulker_sword`, но не `shulker_sword_skill`. Устранение защитной группы и конфликт одновременных групп не гарантированы. [Полный снаряд, shield и ветви](manual-traces-2.8.14.md#shulker-sword-effectshulker_sword).

### Что написано на скриншотах

На изображении вручную считаны: damage = `6`; durability = `2609`; enchantable = `true`; repairable = `true`. Оригинал: [скриншот 115849](https://drive.google.com/file/d/1YEOBZ0aW8jOnH1Uw26aexwJX-C9nx5Jq/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 30. Silver Ingot — `effect:silver_ingot`

**Кратко:** Материал: в рецепте получается из серебряной руды. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

- В 1.6 предмет с этим точным ID не найден.

**2.8.8 / 2.8.14** — определение `Swords_B/items/silver_ingot.json`.
- урон: не указан; максимальная прочность: не указан; зачарование: не указан; перезарядка: не указан; левая рука: не указан; размер стопки: `64`; свечение: не указан; предмет исчезает: не указан.
- Ремонт: компонент не указан; это не доказывает невозможности ремонта.
- Оружейный компонент не указан.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 2.8.14:**

- Рецепт `Swords_B/recipes/silver_ingot.json`; тип `minecraft:recipe_furnace`.
  - Вход: `"effect99:silver_ore"`.
  - Результат: `"effect:silver_ingot"`; рабочие станции/tags: `["furnace","blast_furnace"]`.

- Определение: `Swords_B/items/silver_ingot.json`.
- Результаты рецептов: `Swords_B/recipes/silver_ingot.json` (`minecraft:recipe_furnace`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Silver Ingot, Silver Sword и Alpha Wolf (`effect:silver_ingot`, `effect:silver_sword`, `entity:alpha_wolf`)

[Сквозная цепь Silver → Alpha Wolf → Wolf Sword](manual-silver-wolf-path.md#руда-слиток-и-меч).

[Условия добычи руд, loot-пути и условное распределение кварца](manual-ore-and-loot-paths-2.8.md).

- `items/silver_ingot.json`: material, max stack 64, hand_equipped false. `recipes/silver_ingot.json` задаёт furnace/blast_furnace: `effect99:silver_ore` → `effect:silver_ingot`. `recipes/silver_sword.json` — crafting_table, вертикальные `2/2/1`: два silver_ingot и `minecraft:stick`.
- `items/silver_sword.json`: damage 6, durability 1800, enchantability 9/sword, repair только self 1800, offhand false, web 15/bamboo 10. `on_hurt_entity` расходует 1 прочности. First-person position `[0.67,0,-1.19]`, third-person `[0.36,1.5,-0.66]`. Сам предмет не содержит отдельной команды бонусного урона по alpha wolf: действие в определении цели, приведённое ниже, нельзя автоматически заменять фиксированным бонусом.
- `blocks/silver_ore.json` задаёт destroy_time 8, explosion_resistance 1, light absorption 15, ссылку на отсутствующую локально базовую loot-таблицу `loot_tables/blocks/null.json` и `on_player_destroyed`, проверяющий имена `iron_pickaxe`, `diamond_pickaxe`, `netherite_pickaxe`, `bedrock_sword`. Событие spawn_loot обращается к `loot_tables/blocks/silver_ore.json`, где один roll даёт сам блок `effect99:silver_ore`, count 1. Семантика выражения `q.get_equipped_item_name` без аргументов/скобок, эффект чар и разрешение отсутствующего локально пути loot требуют проверки. Архив 2.8.14 не содержит файлов feature/feature_rule серебряной руды, присутствующих в 2.8.8; естественное появление блока в 2.8.14 этим не доказано.
- `entities/alpha_wolf.json`: здоровье 480, attack 8, movement 0.4, scale 1.8, knockback_resistance 0.5; family `[wolf,mob,monster,alpha_wolf]`. `spawn_rules/alpha_wolf.json`: surface на `minecraft:grass`, brightness 0…7 с adjust_for_weather, difficulty easy…hard, weight 10, herd 1, биом с tag taiga и без mega. Вес 10 — не процент.
- Сенсор урона волка: когда other — player с silver sword в hand и `has_damage:fatal`, вызывает `minecraft:wolf_sword`; этот event выбирает 90 пусто/10 `structure load wolf_sword` (условно 10/100 при вызове и успехе структуры). При player без silver sword event `add_effects` добавляет boss bar и даёт самому волку resistance 20 с amplifier 2 и regeneration 20 с amplifier 2; при player с silver sword `clear_effects` добавляет boss bar и выполняет `effect @s resistance 0`, `effect @s regeneration 0`. Все trigger имеют `deals_damage:true`. Соответственно описание «серебро наносит больше урона» не доказывает численного множителя; оно может отражать отсутствие/снятие защиты. Порядок sensor при фатальном ударе и результат надо измерить.

**Дополнительный подробный разбор** (источник: `docs/manual-silver-wolf-path.md`):

#### Руда, слиток и меч

`effect99:silver_ore` задаёт destroy_time 8, explosion_resistance 1, light absorption 15. Базовый `minecraft:loot` указывает `loot_tables/blocks/null.json`, отсутствующий в обоих архивах; внешний/ванильный файл не исключён. Отдельный event разрушения игроком проверяет имена iron_pickaxe/diamond_pickaxe/netherite_pickaxe/bedrock_sword выражением `q.get_equipped_item_name` без скобок, затем `spawn_loot` на `loot_tables/blocks/silver_ore.json`: один roll, одна запись **самого блока** `effect99:silver_ore`, count 1. Это не прямая выдача слитка, и срабатывание on_player_destroyed с этим Molang и данным инструментом не доказано.

В 2.8.8 есть feature/feature_rule silver: overworld, underground_pass, 5 iterations, y gaussian extent `[10,35]`, scatter 160/200 и allowlist stone; есть структура 1×1×1. В 2.8.14 этих двух feature-файлов нет, но определение блока, loot и файл silver-структуры остаются. Возможное внешнее разрешение структуры и фактическая генерация неизвестны; 160/200 не есть шанс руды в каждом блоке/чанке. [Полная таблица](manual-version-2.8.8.md#silver-ore-и-quartz-diamond-ore).

`recipes/silver_ingot.json` объявляет furnace/blast_furnace input `effect99:silver_ore` → output `effect:silver_ingot`; слиток stack 64, hand_equipped false, durability и weapon не объявлены. `recipes/silver_sword.json`: crafting_table `2/2/1`, 2 = `effect:silver_ingot`, 1 = `minecraft:stick`, result `effect:silver_sword`. При штатной регистрации и выдаче одного слитка на плавку для этой цепочки необходимо **два** блока руды и одна палка на меч; альтернативные внешние источники и эффект чар не исключены.

`effect:silver_sword`: damage 6, durability/self repair 1800, enchantable 9/sword, offhand false, web/bamboo 15/10, только weapon `on_hurt_entity` → direct durability damage 1. Дополнительного множителя урона по волкам в item нет; описание «больше урона» не эквивалентно доказанному коэффициенту.

### Что написано на скриншотах

Сопоставленной карточки чисел на скриншотах нет; это не значит, что предмет нигде на изображениях не упомянут.

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 31. Silver Sword — `effect:silver_sword`

**Кратко:** Материал цепочки с Alpha Wolf и последующим Wolf Sword. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

- В 1.6 предмет с этим точным ID не найден.

**2.8.8 / 2.8.14** — определение `Swords_B/items/silver_sword.json`.
- урон: `6`; максимальная прочность: `{"max_durability":1800}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `false`; размер стопки: `1`; свечение: `false`; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:silver_sword"]` → `1800`.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 2.8.14:**

- Рецепт `Swords_B/recipes/silver_sword.json`; тип `minecraft:recipe_shaped`.
  - Схема сверху вниз: `2` / `2` / `1`.
  - Обозначения: `{"2":{"item":"effect:silver_ingot"},"1":{"item":"minecraft:stick"}}`.
  - Результат: `{"item":"effect:silver_sword"}`; рабочие станции/tags: `["crafting_table"]`.

- Определение: `Swords_B/items/silver_sword.json`.
- Результаты рецептов: `Swords_B/recipes/silver_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[30].Mainhand[0].Name

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Silver Ingot, Silver Sword и Alpha Wolf (`effect:silver_ingot`, `effect:silver_sword`, `entity:alpha_wolf`)

[Сквозная цепь Silver → Alpha Wolf → Wolf Sword](manual-silver-wolf-path.md#руда-слиток-и-меч).

[Условия добычи руд, loot-пути и условное распределение кварца](manual-ore-and-loot-paths-2.8.md).

- `items/silver_ingot.json`: material, max stack 64, hand_equipped false. `recipes/silver_ingot.json` задаёт furnace/blast_furnace: `effect99:silver_ore` → `effect:silver_ingot`. `recipes/silver_sword.json` — crafting_table, вертикальные `2/2/1`: два silver_ingot и `minecraft:stick`.
- `items/silver_sword.json`: damage 6, durability 1800, enchantability 9/sword, repair только self 1800, offhand false, web 15/bamboo 10. `on_hurt_entity` расходует 1 прочности. First-person position `[0.67,0,-1.19]`, third-person `[0.36,1.5,-0.66]`. Сам предмет не содержит отдельной команды бонусного урона по alpha wolf: действие в определении цели, приведённое ниже, нельзя автоматически заменять фиксированным бонусом.
- `blocks/silver_ore.json` задаёт destroy_time 8, explosion_resistance 1, light absorption 15, ссылку на отсутствующую локально базовую loot-таблицу `loot_tables/blocks/null.json` и `on_player_destroyed`, проверяющий имена `iron_pickaxe`, `diamond_pickaxe`, `netherite_pickaxe`, `bedrock_sword`. Событие spawn_loot обращается к `loot_tables/blocks/silver_ore.json`, где один roll даёт сам блок `effect99:silver_ore`, count 1. Семантика выражения `q.get_equipped_item_name` без аргументов/скобок, эффект чар и разрешение отсутствующего локально пути loot требуют проверки. Архив 2.8.14 не содержит файлов feature/feature_rule серебряной руды, присутствующих в 2.8.8; естественное появление блока в 2.8.14 этим не доказано.
- `entities/alpha_wolf.json`: здоровье 480, attack 8, movement 0.4, scale 1.8, knockback_resistance 0.5; family `[wolf,mob,monster,alpha_wolf]`. `spawn_rules/alpha_wolf.json`: surface на `minecraft:grass`, brightness 0…7 с adjust_for_weather, difficulty easy…hard, weight 10, herd 1, биом с tag taiga и без mega. Вес 10 — не процент.
- Сенсор урона волка: когда other — player с silver sword в hand и `has_damage:fatal`, вызывает `minecraft:wolf_sword`; этот event выбирает 90 пусто/10 `structure load wolf_sword` (условно 10/100 при вызове и успехе структуры). При player без silver sword event `add_effects` добавляет boss bar и даёт самому волку resistance 20 с amplifier 2 и regeneration 20 с amplifier 2; при player с silver sword `clear_effects` добавляет boss bar и выполняет `effect @s resistance 0`, `effect @s regeneration 0`. Все trigger имеют `deals_damage:true`. Соответственно описание «серебро наносит больше урона» не доказывает численного множителя; оно может отражать отсутствие/снятие защиты. Порядок sensor при фатальном ударе и результат надо измерить.

**Дополнительный подробный разбор** (источник: `docs/manual-silver-wolf-path.md`):

#### Alpha Wolf и получение Wolf Sword

`entity:alpha_wolf`: health 480, attack 8, movement 0.4, scale 1.8, knockback resistance 0.5, family `[wolf,mob,monster,alpha_wolf]`. Spawn rule: поверхность на `minecraft:grass`, brightness min 0/max 7 с adjust_for_weather true, difficulty easy…hard, weight 10, herd 1, biome tag taiga и не mega. Вес 10 — не процент спавна, указанные brightness-поля не задают явный тест «ночь».

Damage sensor имеет три **отдельных** trigger, у всех `deals_damage:true`:

1. `other` family player и silver sword в hand и `has_damage:fatal` → event `minecraft:wolf_sword`.
2. `other` family player и silver sword **не** в hand → `add_effects`: добавить health_bar, `effect @s resistance 20 2 true` и regeneration 20 2 true.
3. `other` family player и silver sword в hand → `clear_effects`: health_bar и `effect @s resistance 0`, `effect @s regeneration 0`.

Первый и третий фильтры могут совпасть при фатальном ударе. Event `minecraft:wolf_sword` выбирает 90 пусто/10 `structure load wolf_sword`; 10/100 — только условно на вызов выбора, а успешное прохождение фильтра, порядок trigger, загрузка структуры и подбор — отдельные условия. `wolf_sword.mcstructure` содержит item нужного ID. Возможность снять/не получить защиту в событиях волка не доказывает прямого бонуса урона предмета; не предполагать порядок действия обоих trigger.

### Что написано на скриншотах

На изображении вручную считаны: damage = `6`; durability = `1800`; enchantable = `true`; repairable = `true`. Оригинал: [скриншот 120007](https://drive.google.com/file/d/18xMWPEmEQ3k8DUxotbJS2CD1IIXMbY6s/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 32. Slime Sword — `effect:slime_sword`

**Кратко:** Цепочка ездового слизня и Slime King. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

**1.6** — определение `Sword_B/items/slime_sword.json`.
- урон: `6`; максимальная прочность: `{"max_durability":675}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `true`; размер стопки: `1`; свечение: не указан; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:slime_sword"]` → `675`.
- Оружейный компонент не указан.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**2.8.8 / 2.8.14** — определение `Swords_B/items/slime_sword.json`.
- урон: `6`; максимальная прочность: `{"max_durability":675}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `false`; размер стопки: `1`; свечение: `false`; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:slime_sword"]` → `675`; `["minecraft:slime"]` → `48`.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 1.6:**

- Рецепт `Sword_B/recipes/slime_sword.json`; тип `minecraft:recipe_shaped`.
  - Схема сверху вниз: `F` / `F` / `E`.
  - Обозначения: `{"E":{"item":"minecraft:stick"},"F":{"item":"minecraft:slime"}}`.
  - Результат: `{"item":"effect:slime_sword"}`; рабочие станции/tags: `["crafting_table"]`.

- Определение: `Sword_B/items/slime_sword.json`.
- Результаты рецептов: `Sword_B/recipes/slime_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

**Архив 2.8.14:**

- Рецептов с этим точным результатом локально не найдено. Это не исключает других путей.

- Определение: `Swords_B/items/slime_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - `Swords_B/loot_tables/entities/slime_king.json` $.pools[0].entries[0]: `{"type":"item","name":"effect:slime_sword","weight":1,"functions":[{"function":"set_data","data":0}]}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[4].Mainhand[0].Name

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

**Условная математическая модель выбора loot в 2.x:**

Числа ниже — вероятность выбрать хотя бы одну запись предмета внутри уже активированного пула, а не шанс реальной добычи. Допущения: все записи доступны; отсутствующий вес принят за 1; quality и условия записей игнорируются; выборы независимы с возвращением; число rolls равномерно в указанном диапазоне. Условия пула считаются уже выполненными. Загрузка таблицы, дополнительный отбор, количество предметов и функции не эмулируются.

- Таблица/пул: `entities/slime_king.json` / 0; entries: 0; rolls: `1`; вес ID/сумма: 1/1; выбор хотя бы одной записи по модели: **100.0000%**. Условия и оговорки: pool conditions: `[{"condition":"killed_by_player"},{"condition":"random_chance_with_looting","chance":0.04,"looting_multiplier":0.02}]`; functions: `[{"function":"set_data","data":0}]`.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Slime Sword (`effect:slime_sword`) и Slime King

[Сравнение цепочек 1.6/2.x](manual-ender-wither-tnt-slime.md#slime-sword).

##### Предмет и призыв

`Swords_B/items/slime_sword.json:8–75`: прочность 675, damage 6, enchantable value 9/slot sword, max stack 1, offhand false, hand_equipped true. Ремонт: сам меч на 675 и буквальный ID `minecraft:slime` на 48; **не подменять его на slime_ball без подтверждения**. Web speed 15, bamboo 10; только `on_hurt_entity` вызывает weapon, где задан расход 1 прочности.

`entities/player.json:241–249,836–847,1669–1692`: наличие предмета в `hand` вызывает событие `minecraft:slime_sword`. При отсутствии family `slime_sword` добавляется группа, задающая family `[player,slime_sword]`, одноразовый timer `[0.4,0.4]` и damage sensor с отменой урона от other family `tamed_slime`. Событие также сбрасывает scoreboard `slime_despawn` на 0 у ближайшего `entity:mountable_slime` в радиусе 12 (`c=1`). По таймеру `slime_sword_skills` выполняет команды `ride @s summon_ride entity:mountable_slime no_ride_change` и `scoreboard objectives add slime_despawn dummy` **в этом порядке**. Успех создания objective повторно и выбор ближайшего слизня в сетевой игре требуют теста.

При смене предмета событие `stop_slime_sword_event`, только при family `slime_sword`, удаляет группу, добавляет default_player, выполняет `ride @s stop_riding` и посылает `despawn` ближайшему `entity:mountable_slime` в радиусе 32. Кроме того `minecraft:constant_events` содержит условную команду `ride @e[type=entity:mountable_slime,r=1,y=~-1] evict_riders` при отсутствии меча (`player.json:1119–1122`). Это селекторы по расстоянию, а не доказанная привязка к владельцу.

##### Ездовой слизень

`entities/mountable_slime.json:1–231`: runtime `minecraft:slime`, spawnable false, summonable true. При появлении добавляется `default_slime`: family `[effect99_entities,tamed_slime]`, health value 1, collision 0.6×0, movement 0.25, jump_delay `[0.16,0.5]`, один игрок на seat `[0,0.35,0]`, контролируемое движение, power jump и horse.jump_strength range `[0.8,2.0]`. Исходник также содержит группы large/medium/small с разными масштабами 0.4/0.8/1.5 и высотами сиденья 1.9/0.9/0.46; явного назначения этих групп в данном файле не найдено — не считать их автоматически активными.

Два разных события с похожим именем критически различаются: `minecraft:despawn` **добавляет defense_mode_slime**, тогда как `despawn` добавляет группу `despawn` и выполняет семь частиц `crop_growth_emitter` и `random.orb @a[r=12]` pitch 0.6. `animation_controllers/despawn.json:4–24` при `!q.has_rider` посылает `@s minecraft:despawn`; `animation_controllers/mountable_slime.json:4–24` при `q.has_rider` посылает `@s default_slime`, а событие `default_slime` удаляет только `slime_random_direction`. Возврат из defense mode нельзя считать доказанным: нужно проверить разрешение групп движком.

Группа defense: family `[effect99_entities,tamed_slime,player]`, movement 0.45, attack damage 1; ищет видимых `monster` или `undead` в max_dist 16, `must_reach:false`. Sensor без фильтров вызывает `minecraft:is_jumping` и `slime_events`. Последнее задаёт jump_boost 1/2, создаёт `entity:slime_damage` у каждой `@e[r=1,family=monster]`, затем при score 0 телепортирует слизня к ближайшему игроку family slime_sword в диапазоне `rm=8,r=12`, увеличивает счёт на 1 и при score ровно 100 посылает `despawn`. Владелец явно не записан; значения счётчика, частота sensor, конфликт нескольких игроков и отсутствие objective — важные тесты.

**Конкуренция счётчика:** в `player.json:1669–1678` проверка family `!= slime_sword` относится только к первому элементу `sequence`; следующий элемент с `scoreboard players set ... slime_despawn 0` не содержит собственного filters. Поэтому при повторном вызове события удержания он может снова обнулять ближайшего слизня, даже если группа игрока уже добавлена. В `mountable_slime.json:211–217` обратный порядок действий другого события — сначала проверка score 0 для tp, затем `add 1`, затем проверка ровно 100 на despawn. Если повторные обнуления успевают между увеличениями, достижение 100 может откладываться; это зависит от частоты сенсоров, порядка выполнения, расстояний и выбора ближайшего слизня, а не доказанное поведение в игре. Первый сброс может также оказаться до команды создания objective, которая стоит после ride в событии одноразового таймера; успешность команд и инициализацию счёта проверить отдельно.

`entities/slime_damage.json:1–49`: snowball runtime, timer `[0.1,0.1]` → despawn, collision 0×0, projectile impact damage 1, knockback true, destroy_on_hit true, power 1.5, gravity 0.1. Реальный контакт с целью при `summon` нужно подтвердить. Damage sensor mount отменяет fall и весь non-void damage; при fall событие выполняет `instant_damage 1 1` по `@e[r=1,family=!slime_sword,family=!undead]`, `instant_health 3 1` по `@e[r=1,family=undead]` и `event entity @s not_baby`. Не писать просто «неуязвим ко всему»: void отдельно не покрыт.

##### Slime King и добыча

`entities/slime_king.json:29–145`: health value 300, attack 9, scale 4.3, collision 0.5×0.5, movement 1.1, knockback resistance 0.5. В одном объекте два ключа `minecraft:movement.jump`: строки 61–63 задают `[0.5,1.5]`, строки 72–74 задают `[0.16,0.4]`. JSON5-инструмент сохраняет последнее, но принятие и фактическое поведение Bedrock **не установлено**. Цели — семейства player/snowgolem/irongolem, max_dist 38, must_see true. При damage от игрока вызывается health_bar с boss HUD range 32 и ветвлением 95 пусто / 5 jump_boost 1/15. Fall-ветвь отменяет падение и запускает instant_damage r=3 для не-slime_king и отдельный instant_damage r=4 для iron_golem; `slime_effects` задаёт себе jump_boost 1/0, `damage @p[r=1.8] 4 magic` и `damage @e[r=1.5,family=!slime_king] 2 magic` — потенциальное перекрытие областей и частота зависят от движка.

`spawn_rules/slime_king.json:8–20`: поверхность, difficulty easy…hard, spawn weight **10**, biome tag `swamp`; явного ограничения по свету или времени суток в этом файле нет. Это не означает, что движок гарантирует спавн днём, и вес 10 не означает 10%.

`loot_tables/entities/slime_king.json:4–25`: pool с `killed_by_player` и `random_chance_with_looting`, base chance **0.040**, looting_multiplier **0.02**, 1 roll, один меч weight 1, set_data 0. Файл `entities/slime_king.json` не содержит явно заданного `minecraft:loot`; надо проверить применение таблицы по умолчанию для этого runtime/ID, а не утверждать гарантированный дроп. [Скриншот](https://drive.google.com/file/d/1u4b1golY1UN59CFF3zifu2aqiLwI5ypW/view) сообщает 4% и ночной болотный спавн, но не является подтверждением привязки таблицы или ограничения времени в коде.

**Старая версия 1.6** (источник: `docs/manual-traces-1.6.md`):

- **Slime** — 6/675; objective s, ближайшему игроку +1, при score 1 summon slime, jump_boost 1 с amplifier 5, при score 600 удалить objective. Нет доказательств, что это аналог mountable slime и Slime King 2.8.14.

**Дополнительный подробный разбор** (источник: `docs/manual-ender-wither-tnt-slime.md`):

#### Slime Sword

**Предмет и получение.** Damage 6, durability/self repair 675 и enchantable 9/sword в обеих; offhand true → false. В 1.6 рецепт `F/F/E`, F = буквальный `minecraft:slime`, E = stick. 2.x также содержит repair `minecraft:slime` 48 и только on_hurt_entity → durability 1; локального рецепта с результатом этого ID нет. В `loot_tables/entities/slime_king.json` указан pool killed_by_player с chance 0.040, looting_multiplier 0.02 и одним мечом. Файл `entities/slime_king.json` явно не содержит `minecraft:loot`; привязку и фактический дроп не считать доказанными. Правило spawn указывает swamp и weight 10, но отдельной проверки ночи не содержит.

**1.6.** Player создаёт `entity:slime`; оба состояния controller одинаковы: objective `s`, +1 ближайшему `@p`, при `@p[scores={s=1}]` summon `slime`, `effect @p jump_boost 1 5 true`, при score 600 удалить objective, затем `@a swords=2`. Фильтрованный и нефильтрованный `@p` могут выбрать разных игроков; `normal.mcfunction` также условно удаляет `s`. Не переводить score в время и не считать ванильного слизня ездовым по этим строкам.

**2.x.** Группа player включает family `[player,slime_sword]`, одноразовый timer `[0.4,0.4]` и отмену damage от `other` family `tamed_slime`. В отдельном, не имеющем filters шаге hand-события ближайшему `entity:mountable_slime` в r=12 ставится `slime_despawn=0`; по timer сначала `ride @s summon_ride ... no_ride_change`, **потом** `scoreboard objectives add slime_despawn dummy`. Порядок может иметь значение, а ближайший слизень не обязательно принадлежит игроку.

У mount события `minecraft:despawn` и `despawn` различны: первое добавляет defense_mode_slime, второе добавляет despawn с частицами и звуком. Defense event при score 0 может переместить его к ближайшему игроку family slime_sword в rm=8/r=12, затем увеличивает score и при ровно 100 вызывает `despawn`. Повторное обнуление player-событием способно конкурировать с этим счётом; постоянность и порядок вызовов не доказаны. Stop выбирает ближайший mount в r=32, а не записанного владельца. Разные группы, урон и ошибка повторного ключа Slime King разобраны [отдельно](manual-traces-2.8.14.md#slime-sword-effectslime_sword-и-slime-king).

### Что написано на скриншотах

На изображении вручную считаны: damage = `6`; durability = `675`; enchantable = `true`; repairable = `true`. Оригинал: [скриншот 115830](https://drive.google.com/file/d/1u4b1golY1UN59CFF3zifu2aqiLwI5ypW/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 33. Spectral Sword — `effect:spectral_sword`

**Кратко:** Кристалл и замена блоков вокруг игрока. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

**1.6** — определение `Sword_B/items/spectral_sword.json`.
- урон: `9`; максимальная прочность: `{"max_durability":3256}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `true`; размер стопки: `1`; свечение: не указан; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:spectral_sword"]` → `3256`.
- Оружейный компонент не указан.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**2.8.8 / 2.8.14** — определение `Swords_B/items/spectral_sword.json`.
- урон: `9`; максимальная прочность: `{"max_durability":3256}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: `{"category":"spectral_sword","duration":18}`; левая рука: `false`; размер стопки: `1`; свечение: `true`; предмет исчезает: `false`.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:spectral_sword"]` → `3256`; `["minecraft:end_crystal"]` → `620`; `["minecraft:nether_star"]` → `2052`.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`; событие без нанесения урона существу → `{"event":"weapon"}`; удар по блоку → `{"event":"weapon"}`.
- При использовании предмета указано: `{"on_use":{"event":"on_use"}}`.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 1.6:**

- Рецепт `Sword_B/recipes/spectral_sword.json`; тип `minecraft:recipe_shaped`.
  - Схема сверху вниз: `#SS` / `SBS` / `NS#`.
  - Обозначения: `{"N":{"item":"minecraft:end_rod"},"S":{"item":"minecraft:end_crystal"},"B":{"item":"minecraft:netherstar"}}`.
  - **В схеме есть символы без определения key: `["#"]`.** Их смысл и принятие рецепта движком не установлены.
  - Результат: `{"item":"effect:spectral_sword"}`; рабочие станции/tags: `["crafting_table"]`.

- Определение: `Sword_B/items/spectral_sword.json`.
- Результаты рецептов: `Sword_B/recipes/spectral_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

**Архив 2.8.14:**

- Рецептов с этим точным результатом локально не найдено. Это не исключает других путей.

- Определение: `Swords_B/items/spectral_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[5].Mainhand[0].Name
  - `Swords_B/structures/spectral_sword.mcstructure` $.entities[0].Item.Name

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Spectral Sword (`effect:spectral_sword`)

[Сравнение 1.6/2.x и глобальных эффектов](manual-spectral-time-comparison.md#spectral-sword).

[Подробная геометрия замены и восстановления, старые границы высоты и межигровые риски](manual-spectral-world-2.8.md).

- `items/spectral_sword.json`: damage 9, durability 3256, foil true, `should_despawn:false`, enchantable 9/sword, cooldown 18, repair self 3256/end_crystal 620/nether_star 2052, offhand false. Описание на `Screenshot_20261104_115853_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg` сообщает enchantable false, но исходный компонент задан — проверить семантику и версию. On-use задаёт durability 15, shoot `entity:ender_crystal_projectile` power 1, звук и событие scale ближайшему кристаллу `type=ender_crystal,family=!ender_crystal_default,family=!ender_crystal_scale,c=1,r=4`. В weapon randomize при всех трёх хуках 99/100 — durability 1, 1/100 — событие взрыва кристалла без ограничения r, выбираемого по family и `c=1`; в последней ветви явного расхода прочности нет.
- `entities/ender_crystal_projectile.json`: runtime snowball, family ender_crystal, projectile power 5, gravity 0.001, inertia 1, reflect_on_hurt/catch_fire true; on_hit добавляет crystal_exploding, fuse 0, power 6, fire true, griefing true. Это другой объект, чем `minecraft:ender_crystal` и его взрыв (power 6, fire false).
- `player.json`: group имеет timer 0.4 non-looping и rideable seat `[0,0.4,0]`; таймер призывает `ender_crystal ~ ~1.8 ~ minecraft:detect_player` только при biome tag != the_end, затем звук/частицы. `entities/ender_crystal.json` при detect ищет **ближайшего** игрока family spectral_sword r=3 и садится на него, а анимационный контроллер обрабатывает mounting/despawn. On-use scale group возраст duration 18 и scale 0.1→1; поведение группы и повторного призыва в связке с контроллерами надо испытать, особенно на нескольких игроках.
- Удержание также заменяет в кубе `~6…~-6` stone/netherrack/end_stone (выбор по biome tags) на `effect99:spectral_block`, а окружающие слои координатами ~7…~8 восстанавливает соответствующим обычным блоком; на y от 0 до 7 вызывается специальная функция восстановления в объёме с y−6…+8. При снятии действует отдельный общий `minecraft:stop_sword_events`. Блок имеет destroy_time 9999, explosion_resistance 999, light absorption 0 и отдельную blend geometry. Это **реальная массовая замена блоков**, не просто клиентская прозрачность; в сложных биомах, пересечениях игроков, изменениях/потере данных и при выгрузке чанка восстановление не гарантировано. Точные команды и порядок см. `player.json` и карточку.
- `entities/ender_crystal.json`: при spawn в biome tag nether добавляется on_hurt → `spectral_crystal_explode`: 98 пусто/2 структура spectral_sword, затем отдельно группа взрыва; условные 2/100 на событие. Вне nether иные группы. `entities/ghast.json` при damage sensor с фильтром `is_family:ghast` вызывает `spectral_ghast`, выбор 94 пусто/6 структура; filter не содержит явного `has_damage:fatal` или прямой проверки собственного снаряда. Поэтому скриншот «6% при убийстве собственным снарядом» нельзя подтвердить по этому фильтру без испытания subject/default semantics.

**Старая версия 1.6** (источник: `docs/manual-traces-1.6.md`):

- **Spectral** — 9/3256; вокруг `@p` stone 0 в кубе ±6 заменяется barrier 0, затем шесть slabs вокруг контроллера заменяют barrier на stone: x 7…8 и −8…−7, z 7…8 и −8…−7, y −8…−7 и 7…8 с поперечными пределами из команд. Это затрагивает и ранее существовавшие barrier в этих объёмах; никакого сохранения происхождения блоков в этих командах нет. При движении, исчезновении сущности и пересечении игроков восстановление не доказано.

**Дополнительный подробный разбор** (источник: `docs/manual-spectral-time-comparison.md`):

#### Spectral Sword

`effect:spectral_sword`: damage 9, max durability 3256, stack 1, enchantable 9/sword, self repair 3256 и digger web 15/bamboo 10 в обеих версиях; offhand true → false. 2.x добавляет ремонт `minecraft:end_crystal` 620 и `minecraft:nether_star` 2052, `should_despawn:false` и cooldown 18. Рецепт 1.6 `#SS/SBS/NS#`, S = `minecraft:end_crystal`, B = буквальный `minecraft:netherstar`, N = end_rod, но `#` не задан в key. Прямого локального recipe с этим результатом в 2.x нет; в них структуру вызывают отдельные условия у end crystal в Nether (2/100 при вызове выбора) и ghast (6/100 при вызове выбора). Ghast filter не содержит явно fatal или проверки собственного снаряда; не превращать текст скриншота в подтверждённое условие.

**1.6.** Hand sensor добавляет группу spawn `entity:spectral`, она подключает `controller.animation.spectral`. В двух одинаковых on_entry центральный куб ±6 `barrier 0 replace stone 0` выбирается относительно `@p`; шесть последующих fill `stone 0 replace barrier` в оболочке ±7…8 выполняются относительно **helper**. При общем целочисленном центре это 13³ = 2197 координат внутреннего куба и 17³−13³ = 2716 уникальных координат оболочки, но центры не обязательно совпадают. `normal.mcfunction` дополнительно восстанавливает шесть плит и центр при общем сбросе. Ни одна команда не хранит происхождение barrier или исходные состояния камня.

**2.x.** Три weapon-хука: randomize 99 direct durability 1 / 1 команда `minecraft:crystal_explode` ближайшему `type=ender_crystal` с family-исключениями и `c=1`, **без явного r**. В редкой ветви явной потери durability нет. On-use отдельно задаёт durability 15, shoot `entity:ender_crystal_projectile` power 1 и событие scale подходящему кристаллу `c=1,r=4`; соседние поля не доказывают порядок. Сам снаряд и `minecraft:ender_crystal` — разные сущности/взрывы.

Player-группа содержит timer `[0.4,0.4]`, non-looping, и rideable; связанное событие вызывает кристалл при biome tag != the_end. При удержании два отдельных `execute @s[y=8,dy=247]` и `@s[y=0,dy=7]` направляют к разным событиям. Первое в трёх отдельных biome-ветвях делает центральный fill на `effect99:spectral_block` вместо stone/netherrack/end_stone и шесть fill оболочки назад в материал ветви; второе выполняет только восстановление. Другой общий sensor вызывает `minecraft:stop_sword_events`, который тоже содержит восстановление, независимо от отдельного stop события группы Spectral. В тесте 2.8.8 гранит после восстановления стал обычным камнем; заранее поставленный spectral_block также заменился на камень без меча. Преобразование камня наблюдалось на Y8, но не на Y−10, Y7 и Y260; это не полные границы. Остальные условия см. в [испытании](manual-spectral-world-2.8.md).

**Связанный подробный механизм** (источник: `docs/manual-spectral-world-2.8.md`):

### Spectral Sword 2.x: след изменения блоков и границы высоты

Статическое чтение `Swords_B/entities/player.json` и `blocks/spectral_block.json` из архива 2.8.14. Соответствующие события и команды совпадают с 2.8.8; точечные результаты для 2.8.8 на 1.20.50.03 приведены ниже; остальные условия остаются непроверенными. [Основная карточка](manual-traces-2.8.14.md#spectral-sword-effectspectral_sword) · [сравнение версий](version-diff.md).


#### Практическое испытание 2.8.8

**Осторожно: потеря гранита.** В Overworld на Y100 рядом с игроком обычный камень и гранит стали spectral_block при удержании меча; золотой блок не изменился. Через 5 секунд после снятия меча обе каменные позиции были восстановлены как обычный камень, не гранит. Отдельно вручную установленный spectral_block без меча через 4 секунды также стал камнем. Проверка касалась конкретных позиций и состояний, не всех материалов и биомов.

В четырёх отдельных пробах с family spectral_sword и камнем на x+3 преобразование наблюдалось на Y8, но не на Y−10, Y7 и Y260. Это не полное определение границ: координаты селекторов и хитбокс важны. [Условия и журналы](../data/original-mechanics-2026-11-07/README.md).

#### Входы и высота

- При `has_equipment` `effect:spectral_sword` в `domain:hand` сенсор вызывает `minecraft:spectral_sword`. Первый элемент `sequence` добавляет группу игрока при family `!= spectral_sword`; второй содержит отдельные команды, в том числе два обращения к событиям на self: `execute @s[y=8,dy=247] ~~~ event entity @s spectral_sword_function` и `execute @s[y=0,dy=7] ~~~ event entity @s spectral_sword_function_1` (`player.json:1693–1709`). На двух командах заданы **разные** селекторы, не универсальный вызов для всех высот.
- При обычном понимании `y`/`dy` как ограничений объёма обе записи ориентированы на старый интервал около Y 0…255. Для отрицательных высот и Y выше старого потолка нет отдельной команды в этом списке. Точные границы, влияние размеров хитбокса, координаты и разбор `~~~` необходимо испытать; особенно нельзя автоматически считать, что целевая версия с изменёнными границами мира сохранит поведение.

#### Преобразование для основного диапазона

`player.json:1741–1787`: событие `spectral_sword_function` имеет три раздельных элемента sequence с biome filters:

| Условие, как записано | Материал для replace | Материал восстановления |
|---|---|---|
| оба `has_biome_tag != nether` и `!= the_end` | `stone` | `stone 0` |
| `has_biome_tag nether` | `netherrack` | `netherrack 0` |
| `has_biome_tag the_end` | `end_stone` | `end_stone 0` |

В каждой ветви сперва один `fill ~6 ~6 ~6 ~-6 ~-6 ~-6 effect99:spectral_block 0 replace <материал>`. Если считать концы по стандартным целочисленным координатам включительно, объём рамки — 13×13×13 = 2197 позиций, но команда **только выбирает подходящие блоки** и успешное изменение всех позиций не подтверждено; частичное изменение камня и гранита подтверждено в пробе выше.

Затем шесть команд заменяют `effect99:spectral_block` на материал этой же ветви, в таком исходном порядке (промежутки обозначают два конечных значения команды, а не требование порядка координат):

1. x `+7…+8`, y `+8…−8`, z `+8…−8`;
2. x `−7…−8`, y `−8…+8`, z `−8…+8`;
3. x `−6…+6`, y `+8…−8`, z `+7…+8`;
4. x `+6…−6`, y `−8…+8`, z `−7…−8`;
5. x `+8…−8`, y `−8…−7`, z `+8…−8`;
6. x `+8…−8`, y `+8…+7`, z `+8…−8`.

Геометрически при включительных целых концах объединение шести рамок — оболочка 17³ минус 13³, **2716 уникальных координат**; некоторые углы/рёбра перечислены более одного раза. Это геометрия текста, не число выполненных замен или частота работы. Исходный порядок и наличие повторов важны, их нельзя незаметно заменить другой логикой без проверки.

#### Нижний диапазон и общий сброс

- `spectral_sword_function_1` (`player.json:1711–1739`) в тех же трёх biome-ветвях выполняет **только восстановление** spectral_block в объёме `~8 ~8 ~8`…`~-8 ~-6 ~-8`: геометрически 17×15×17 = 4335 позиций. Команды создания нового spectral_block в этом событии нет. Применимость его y-селектора и исполнение fill нужно проверить.
- `minecraft:stop_sword_events` вызывается отдельным environment sensor с `any_of`: family `default_player` **или** family `!= spectral_sword`; это не буквальный фильтр только события снятия меча (`player.json:633–638`). Первый шаг выполняет `execute @e[r=64,type=!player] ~ ~ ~ detect ~ ~ ~ ice 0 tp @s ~ ~ ~`. Затем три biome-ветви каждая восстанавливает центральный куб ±6 и те же шесть внешних рамок; в последнем шаге при отсутствии Slime Sword выполняется `ride @e[type=entity:mountable_slime,r=1,y=~-1] evict_riders`. Это общие действия игрока, не только состояние отдельного Spectral Sword.
- `stop_spectral_sword_event` отдельно при family spectral_sword удаляет `minecraft:spectral_sword`, вызывает `ride @s evict_riders` и добавляет `minecraft:default_player`; сами команды block fill находятся в другом событии. Обе цепочки и их возможное пересечение нельзя сливать в одну атомарную операцию.

#### Риски восстановления и открытые вопросы

Исходник выбирает заменяющий материал по **текущим biome tags** исполнителя, а не по записанному происхождению каждого блока; ни один из рассмотренных fill не сохраняет исходный block state, data, положение владельца или идентификатор игрока. Поэтому пересечение областей игроков, переход между разными biome tags, и ранее существовавшие spectral_block потенциально могут привести к замене не тем материалом или потере информации. Потеря гранита и восстановление заранее поставленного spectral_block подтверждены для условий выше; нельзя утверждать, что любой state непременно теряется.

`blocks/spectral_block.json` задаёт destroy_time 9999, explosion_resistance 999 и light absorption 0; это пользовательский блок, а не чисто клиентский визуальный эффект. Для достоверного ремейка проверить на копии мира: границы Y ниже 0, на 0/7/8/255 и выше 255; пересечение двух игроков и биомов; перемещение, снятие меча, выход игрока и выгрузку чанка; заранее установленные spectral_block и исходные state. Зафиксировать все успешно выполненные команды и остаточные блоки, не испытывать на важном мире.

### Что написано на скриншотах

На изображении вручную считаны: damage = `9`; durability = `3256`; enchantable = `false`; repairable = `true`. Оригинал: [скриншот 115853](https://drive.google.com/file/d/1g4UIpjMFNG1uYe8hAo8IOzVw5ctqxL-i/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 34. Spider Sword — `effect:spider_sword`

**Кратко:** Паутина, паук для верховой езды и отдельный навык. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

**1.6** — определение `Sword_B/items/spider_sword.json`.
- урон: `6`; максимальная прочность: `{"max_durability":628}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `true`; размер стопки: `1`; свечение: не указан; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:spider_sword"]` → `628`.
- Оружейный компонент не указан.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**2.8.8 / 2.8.14** — определение `Swords_B/items/spider_sword.json`.
- урон: `5`; максимальная прочность: `{"max_durability":628}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: `{"category":"spider_sword","duration":28}`; левая рука: `false`; размер стопки: `1`; свечение: `false`; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:spider_sword"]` → `628`; `["minecraft:web"]` → `128`; `["minecraft:spider_eye"]` → `48`.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`; событие без нанесения урона существу → `{"event":"weapon"}`; удар по блоку → `{"event":"weapon"}`.
- При использовании предмета указано: `{"on_use":{"event":"on_use"}}`.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":100},{"block":"minecraft:bamboo","speed":10}]}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 1.6:**

- Рецепт `Sword_B/recipes/spider_sword.json`; тип `minecraft:recipe_shaped`.
  - Схема сверху вниз: `#SS` / `SBS` / `NS#`.
  - Обозначения: `{"N":{"item":"minecraft:stick"},"S":{"item":"minecraft:web"},"B":{"item":"minecraft:spider_eye"}}`.
  - **В схеме есть символы без определения key: `["#"]`.** Их смысл и принятие рецепта движком не установлены.
  - Результат: `{"item":"effect:spider_sword"}`; рабочие станции/tags: `["crafting_table"]`.

- Определение: `Sword_B/items/spider_sword.json`.
- Результаты рецептов: `Sword_B/recipes/spider_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

**Архив 2.8.14:**

- Рецептов с этим точным результатом локально не найдено. Это не исключает других путей.

- Определение: `Swords_B/items/spider_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - `Swords_B/loot_tables/chests/abandoned_mineshaft.json` $.pools[1].entries[5]: `{"type":"item","name":"effect:spider_sword","functions":[{"function":"set_count","count":{"min":1,"max":1}}],"weight":3}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[2].Mainhand[0].Name

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

**Условная математическая модель выбора loot в 2.x:**

Числа ниже — вероятность выбрать хотя бы одну запись предмета внутри уже активированного пула, а не шанс реальной добычи. Допущения: все записи доступны; отсутствующий вес принят за 1; quality и условия записей игнорируются; выборы независимы с возвращением; число rolls равномерно в указанном диапазоне. Условия пула считаются уже выполненными. Загрузка таблицы, дополнительный отбор, количество предметов и функции не эмулируются.

- Таблица/пул: `chests/abandoned_mineshaft.json` / 1; entries: 5; rolls: `{"min":2,"max":4}`; вес ID/сумма: 3/86; выбор хотя бы одной записи по модели: **10.0665%**. Условия и оговорки: functions: `[{"function":"set_count","count":{"min":1,"max":1}}]`.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Spider Sword (`effect:spider_sword`)

[Сравнение цепочек 1.6/2.x](manual-fire-spider-sponge.md#spider-sword).

`items/spider_sword.json:8–121`: damage 5, durability 628, cooldown 28, enchantable value 9/slot sword, offhand false; ремонт идентичным мечом 628, `minecraft:web` 128, `minecraft:spider_eye` 48. Web dig speed 100, bamboo 10. Все три weapon-хука: сначала durability 1, потом weight 95 — пусто и weight 5 — `shoot entity:web`, power 1; условная доля последнего 5/100. On-use отдельно задаёт команду `event entity @s spider_sword_skill` target holder и потерю 8 прочности.

`player.json:216–226,864–875,1608–1643`: при наличии в hand и отсутствии family spider_sword добавляется группа и команда `ride @s summon_ride minecraft:spider no_ride_change minecraft:spider_sword` плюс particle. При прекращении — удаление spider_sword и spider_sword_skill, добавление default_player, `ride @s stop_riding`. Навык добавляет группу только при отсутствии family spider_sword_skill; в ней `spawn_entity` `entity:web`, min_wait 0/max_wait 0, single_use false, num 1 и одноразовый timer `[2,2]` на stop_spider_skill_event. Он удаляет группу skill и восстанавливает базовую при соответствующей family. Величину «сколько паутин за две секунды» нельзя вывести просто из нулевых интервалов: её нужно измерять на исходном движке.

`entities/spider.json:20–45,386–412`: событие призыва удаляет группы hostile/neutral/default и добавляет `minecraft:spider_player_jockey`; family `[spider,monster,mob,arthropod,spider_sword]`, здоровье 20/20, ссылка loot `loot_tables/entities/empty.json` (не найдена в пакете; её поведение не установлено), seat 1 на `[0,0.54,0]`, horse jump range 0.4…0.7, input controlled by player. `controller.animation.despawn` при отсутствии rider посылает `minecraft:despawn`, но действие despawn у spider отфильтровано family spider_sword. `controller.animation.climb_spider` при наличии rider выполняет `effect @s levitation 10 3 true` и возвращается в default; `not_climb` удаляет levitation через `effect @s levitation 0 0 true`, если четыре проверки соседнего воздуха на ±0.8 выполнены. Это не доказанная точная копия ванильного лазания.

`entities/web.json:1–70`: runtime snowball, scale 0.5, collision 0.25×0.25, projectile power 1.5, gravity 0.03, impact damage 1/knockback true, remove_on_hit, hit_sound pop, одна iconcrack-частица на попадание. Event set_web выполняет `fill ~ ~ ~ ~ ~ ~ web 0 replace air` — заменяет только воздух в координате снаряда. При family shoot_sound вызывается звук `random.bow @a[r=12]` volume 1 pitch 0.33 и добавляется группа remove_shoot_sound.

`loot_tables/chests/abandoned_mineshaft.json:42–...`: меч присутствует во втором пуле, rolls `{min:2,max:4}`, weight 3, set_count 1…1. Сумма явно указанных весов 11 записей пула — 86; сырая доля выбора меча **3/86 ≈ 3.488% на один выбор**, если движок использует все эти веса без изменений. Это не шанс «на сундук»: число выборов 2…4, важны повторы, вставка предмета в слоты и семантика loot. Полный пул и соседние пулы см. [реестр мира](world-ledger-2.8.14.md).

**Старая версия 1.6** (источник: `docs/manual-traces-1.6.md`):

#### Fire, Magma и Spider 1.6: типы и мир

[Три контроллера, рецепты и риск изменения мира](manual-fire-magma-spider-1.6.md) · [матрица type-селекторов](fire-web-targets-1.6.md).

**Дополнительный подробный разбор** (источник: `docs/manual-fire-spider-sponge.md`):

#### Spider Sword

**Предмет и получение.** Damage 6 → 5, durability 628 в обеих, offhand true → false; enchantable 9/sword и self repair 628 остаются, 2.x добавляет web 128 и spider_eye 48 для ремонта. Speed web в digger 15 → **100**, bamboo остаётся 10. Рецепт 1.6 `#SS/SBS/NS#`, S web, B spider_eye, N stick, но `#` отсутствует в key. Прямого локального рецепта с этим result в 2.x не найдено. `chests/abandoned_mineshaft.json`, pool 1: 2…4 rolls, меч weight 3 из явно заданной суммы 86; 3/86 относится к одному выбору в условной модели, не к полному сундуку.

**1.6.** Hand sensor → `entity:spider` → controller: снять poison у `@p`; при detect web в его позиции и y+1 заменить его на air; относительно `@p` назначить slowness 1 amplifier 128 отдельно spider и cave_spider в r=6; затем 25 отдельных type-команд относительно helper в r=5 ставят web в позиции цели только через `replace air`, и `@a swords=2`. Паук и пещерный паук присутствуют в slowness, но не в 25 типах установки web; центры выбора тоже различаются.

**2.x.** Все три weapon-хука задают durability 1, затем 95 пусто/5 `shoot entity:web`. On-use отдельно задаёт расход 8 и event `spider_sword_skill` target holder, cooldown 28. При удержании событие вызывает `ride @s summon_ride minecraft:spider no_ride_change minecraft:spider_sword`; skill-группа добавляет spawn `entity:web` с wait 0/0, single_use false и одноразовый timer `[2,2]` для stop. Количество созданий в этот интервал не определяется только нулями wait. Снаряд web при попадании может выполнить `fill ... web 0 replace air` на одной позиции.

Spider jockey имеет family `[spider,monster,mob,arthropod,spider_sword]`, health 20, одно место и player-controlled movement; ссылка на `loot_tables/entities/empty.json` отсутствует в обоих 2.x архивах и не равна существующему `loot_tables/empty.json`. Animation controllers при rider/соседнем воздухе назначают или снимают levitation; не приравнивать это автоматически к ванильному лазанию. При stop игрока указано удаление обеих групп и stop_riding; выбор, загрузка и путь loot требуют проверки.

**Дополнительные детали 1.6** (источник: `docs/manual-fire-magma-spider-1.6.md`):

### Fire, Magma и Spider 1.6: цели и воздействие на мир

[Сравнительная таблица всех type-селекторов](fire-web-targets-1.6.md) извлекает строки из трёх исходных контроллеров. Ни одна команда не проверена на выполнение в игре: старые имена, селекторы, замена блоков, контекст `@p` и частота зависят от движка.

#### Общая цепь и разные центры

Для каждого предмета `player.json` проверяет `has_equipment` в domain `hand`, передаёт одноимённый event и добавляет группу `minecraft:fire_sword` / `minecraft:magma_sword` / `minecraft:spider_sword`. Группы соответственно объявляют spawn `entity:fire`, `entity:magma`, `entity:spider`, каждая wait 0/0, num_to_spawn 1, single_use true. Другая player-ветвь удаляет эти группы; повторное добавление и длительность жизни помощника не установлены. Helpers используют family `despawnear` и одноимённые animation controllers; их положение не гарантированно следует за владельцем.

В каждом из трёх контроллеров `default` и состояние с именем меча переходят друг в друга по `(1.0)` и содержат одинаковые строки `on_entry`. Соответственно, сравнение ниже относится к **одному списку**, а не двум одновременно выполненным копиям. Каждая последовательность заканчивается `/scoreboard players set @a swords 2` для всех выбранных игроков; глобальные взаимодействия и возможные повторы описаны [отдельно](manual-global-state-1.6.md).

`@p` выбирается из контекста helper и не гарантированно означает владельца. Отдельные `@e[r=...,type=...]` сначала выбираются относительно контекста helper, после чего `execute` использует позицию соответствующей цели. Не заменять их единой областью вокруг игрока.

#### Предметы и рецепты 1.6

| Предмет | damage / max durability / self repair | Локальный shaped recipe |
|---|---|---|
| Fire | 12 / 2000 / 2000 | `#SM / SBS / NS#`; `N=blaze_rod`, `S=blaze_powder`, `B=iron_sword`, `M=magma_cream`; **`#` отсутствует в key** |
| Magma | 7 / 1000 / 1000 | `F / F / E`; `F=minecraft:magma`, `E=minecraft:blaze_rod` |
| Spider | 6 / 628 / 628 | `#SS / SBS / NS#`; `N=stick`, `S=web`, `B=spider_eye`; **`#` отсутствует в key** |

Все три: max stack 1, `allow_off_hand:true`, `hand_equipped:true`, `can_destroy_in_creative:false`, `minecraft:glint:false`, enchantable value 9/slot sword, digger web 15/bamboo 10/use_efficiency true. Ремонт — самим предметом; названия ингредиентов без namespace в таблице обозначают исходный `minecraft:`. Нет основания автоматически дописывать key `#`, исправлять буквальный `minecraft:magma` или считать объявленные рецепты работающими. [Полная проверка рецептов](manual-acquisition-issues.md), [сравнение компонентов с 2.x](item-version-matrix.md).

#### Fire: 31 тип и изменения блоков

`Sword_B/animation_controllers/fire_sword.json`, в каждом состоянии **39** строк:

1. `/effect @p fire_resistance 10 0 true` — длительность 10, amplifier 0.
2. `execute @p ... detect ~ ~ ~ air 0 setblock ~ ~ ~ fire` — проверка воздуха в позиции ближайшего игрока.
3. Пять fill относительно `@p` в кубе `~3 ~3 ~3` → `~-3 ~-3 ~-3`: **7×7×7 = 343** возможных позиций в каждой геометрической рамке. В исходном порядке: `snow_layer → air 0`; `ice → water 0`; `blue_ice → water 0`; `packed_ice → water 0`; `snow → grass 0`. Это замена существующего мира, не декоративная частица и не сохранение исходных блоков; фактическое число замен зависит от содержимого, интерпретации data и успеха команд.
4. **31** команда `@e[r=15,rm=2,type=…] ... setblock ~ ~ ~ fire` для типов из [матрицы](fire-web-targets-1.6.md), включая корову, свинью, овцу, лошадь, кролика, курицу, лису, летучую мышь, белого медведя и жителя. Нет ограничения только на враждебных существ. В этих отдельных командах нет `detect` или `replace air`; запись `setblock` потенциально затрагивает имеющийся блок в позиции цели, но точные стандартные режимы, перенос координат и результат при занятом блоке нужно проверить в исходном движке.
5. Глобальный scoreboard для `@a`.

Самому ближайшему игроку команда №2 может поставить огонь при detect air, хотя №1 отдельно объявляет fire resistance. Успех одной команды не доказывает успех другой, а сопротивление не является доказанной защитой от любых причин урона.

#### Magma: 21 тип и плоскость лавы

`Sword_B/animation_controllers/magma_sword.json`, **24** строки на состояние: та же запись `fire_resistance 10 0 true` для ближайшего игрока; затем `fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 magma 0 replace lava` от `@p`, плоскость **5×5 = 25** геометрических позиций. После `replace lava` в этой команде **нет явного data**; не добавлять `0` по аналогии с другими файлами. В исходнике нет такой же отдельной команды для `flowing_lava`; это не доказательство того, какие именно состояния лавы выберет движок.

Далее **21** type-команда `setblock fire` в `r=15,rm=2` от helper и глобальный scoreboard. Эти 21 типа — точное подмножество 31 Fire; **10** типов, имеющихся в Fire и отсутствующих в Magma, — `cow`, `pig`, `chicken`, `horse`, `rabbit`, `sheep`, `fox`, `bat`, `polar_bear`, `villager`. Это сопоставление только буквальных команд данного контроллера, не утверждение о полной безопасности перечисленных существ.

#### Spider: паутина и два разных селектора

`Sword_B/animation_controllers/spider_sword.json`, **31** строка на состояние:

1. `effect @p poison 0 0 true`.
2. Две команды с `detect ... web 0` удаляют web в позиции `@p` или на y+1, заменяя web на air только в соответствующей точке.
3. От позиции `@p` задаётся `slowness 1 128 true` для `@e[r=6,type=spider]` и отдельно `type=cave_spider`. Эти эффекты не направлены на весь список паутины и имеют другой центр выбора.
4. **25** отдельных типов выбираются в `@e[r=5,type=…]` от helper; в позиции каждой цели команда `fill ~ ~ ~ ~ ~ ~ web 0 replace air` проверяет одну позицию. Список содержит, среди прочего, `tnt`, `evocation_fang`, `blaze` и `zombie_pigman`, но **не содержит** отдельного web-fill по `spider` или `cave_spider`. Их наличие в командах slowness не означает наличие в списке fill.
5. `scoreboard players set @a swords 2`.

Не путать статическое количество строк с количеством целей/реальных блоков: каждая команда может выбрать ноль, одну или много сущностей, выполняться несколько раз или не пройти. Отсутствие type-команды в этих трёх списках не доказывает отсутствия воздействия из другой механики, vanilla или иного пакета. Реализации 2.x используют дополнительные события/loot/сущности и не сводятся к этим старым контроллерам; см. [карточки 2.8.14](manual-traces-2.8.14.md).

### Что написано на скриншотах

На изображении вручную считаны: damage = `5`; durability = `628`; enchantable = `true`; repairable = `true`. Оригинал: [скриншот 115837](https://drive.google.com/file/d/1eO2vurHVipmTvKj_7XzYz3KWOhZA23ic/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 35. Sponge Sword — `effect:sponge_sword`

**Кратко:** Работа с водой и превращение в мокрую версию. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

**1.6** — определение `Sword_B/items/sponge_sword.json`.
- урон: `6`; максимальная прочность: `{"max_durability":128}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `true`; размер стопки: `1`; свечение: не указан; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:sponge_sword"]` → `128`.
- Оружейный компонент не указан.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**2.8.8 / 2.8.14** — определение `Swords_B/items/sponge_sword.json`.
- урон: `5`; максимальная прочность: `{"max_durability":128}`; зачарование: не указан; перезарядка: не указан; левая рука: `false`; размер стопки: `1`; свечение: `false`; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:sponge_sword"]` → `128`; `["minecraft:sponge"]` → `62`.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 1.6:**

- Рецепт `Sword_B/recipes/sponge_sword.json`; тип `minecraft:recipe_shaped`.
  - Схема сверху вниз: `F` / `F` / `E`.
  - Обозначения: `{"E":{"item":"minecraft:stick"},"F":{"item":"minecraft:sponge"}}`.
  - Результат: `{"item":"effect:sponge_sword"}`; рабочие станции/tags: `["crafting_table"]`.

- Определение: `Sword_B/items/sponge_sword.json`.
- Результаты рецептов: `Sword_B/recipes/sponge_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

**Архив 2.8.14:**

- Рецепт `Swords_B/recipes/wet_sponge_sword.json`; тип `minecraft:recipe_furnace`.
  - Вход: `"effect:wet_sponge_sword"`.
  - Результат: `"effect:sponge_sword"`; рабочие станции/tags: `["furnace","blast_furnace"]`.

- Определение: `Swords_B/items/sponge_sword.json`.
- Результаты рецептов: `Swords_B/recipes/wet_sponge_sword.json` (`minecraft:recipe_furnace`).
- Прямые записи loot:
  - `Swords_B/loot_tables/entities/elder_guardian.json` $.pools[1].entries[0]: `{"type":"item","name":"effect:sponge_sword","weight":1,"functions":[{"function":"set_count","count":{"min":1,"max":1}},{"function":"set_data","data":0}]}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[1].Mainhand[0].Name

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

**Условная математическая модель выбора loot в 2.x:**

Числа ниже — вероятность выбрать хотя бы одну запись предмета внутри уже активированного пула, а не шанс реальной добычи. Допущения: все записи доступны; отсутствующий вес принят за 1; quality и условия записей игнорируются; выборы независимы с возвращением; число rolls равномерно в указанном диапазоне. Условия пула считаются уже выполненными. Загрузка таблицы, дополнительный отбор, количество предметов и функции не эмулируются.

- Таблица/пул: `entities/elder_guardian.json` / 1; entries: 0; rolls: `1`; вес ID/сумма: 1/1; выбор хотя бы одной записи по модели: **100.0000%**. Условия и оговорки: pool conditions: `[{"condition":"killed_by_player"},{"condition":"random_chance_with_looting","chance":0.065,"looting_multiplier":0.02}]`; functions: `[{"function":"set_count","count":{"min":1,"max":1}},{"function":"set_data","data":0}]`.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Sponge Sword и Wet Sponge Sword (`effect:sponge_sword`, `effect:wet_sponge_sword`)

[Сравнение цепочек 1.6/2.x](manual-fire-spider-sponge.md#sponge-sword-и-wet-sponge-sword).

- `items/sponge_sword.json`: damage 5, durability 128, ремонт self 128 и `minecraft:sponge` 62. `items/wet_sponge_sword.json`: damage 3, durability 64, ремонт dry sword 64, sponge 32, wet sword 64. Оба on_hurt_entity расходуют 1, max stack 1, offhand false. В обоих файлах **не задан** `minecraft:enchantable`, хотя описание на скриншоте заявляет `Enchantable: true` для сухого меча; значение по умолчанию и совместимость надо проверять, а не подменять.
- `player.json:213–215,880–889,1560–1606`: при наличии dry sword в hand первая подходящая ветвь добавляет family `[player,sponge_sword]` и команду создания scoreboard objective `sponge_sword dummy`. При `in_water_or_rain` выполняет `fill ~2 ~2 ~2 ~-2 ~-2 ~-2 sponge 0 replace water`, звук и частицы, затем увеличивает счёт игрока на 1. То есть условие включает дождь и повышение счёта не проверяет, был ли реально заменён блок воды.
- Независимый следующий шаг **в том же событии** выполняет `fill` всего объёма 5×5×5 в воздух с `replace sponge`, затем `replace seagrass`; текст команд не ограничивает удаляемую губку только той, что была создана предыдущим шагом. При точных значениях scoreboard 150, 155 или 160 вызывается событие `wet_sponge_sword`; при проверке hand dry sword оно выполняет `replaceitem ... slot.weapon.mainhand 0 effect:wet_sponge_sword 1`, сброс счёта 0 и actionbar. Возможны потеря прочности/зачарований при замене и сложности со слотами — необходимо проверить в игре. Это точные пороги счётчика, не заданное число секунд, и не условие «150 поглощённых блоков».
- `recipes/wet_sponge_sword.json` задаёт furnace и blast_furnace: input wet → output dry. `loot_tables/entities/elder_guardian.json` задаёт пул с `killed_by_player`, chance 0.065 и looting_multiplier 0.02; это условие таблицы, а не доказательство, что она была привязана/сработала в конкретной игре. Проверить ванильную привязку и семантику looting на исходном движке.

##### Дополнение к Fire Sword: противоречие описания

На изображении `Screenshot_20261104_115915_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg` описание заявляет: вода → obsidian, дождь → crystal sword. Однако в `Swords_B/entities/item.json:39–50,228–229` вода вызывает `fire_sword_event_2` и загрузку `glass_sword`, а дождь вне воды через таймер — `fire_sword_event_1` и `obsidian_sword`. Проверено по изображению и исходнику; не следует считать описание однозначным источником поведения или предполагать, что его версия совпадает с архивом.

**Старая версия 1.6** (источник: `docs/manual-traces-1.6.md`):

#### Sponge Sword: 1.6 против 2.8.14

`items/sponge_sword.json`: damage 6, durability 128, enchantable 9, repair self 128, offhand true. В 2.8.14 damage 5, нет компонента enchantable, есть ремонт губкой и мокрая версия с отдельным счётчиком. Контроллер 1.6 `animation_controllers/sponge_sword.json` при входе в оба состояния выполняет `execute @a ... fill` в кубе **9×9×9** относительно каждого игрока: water→sponge, затем sponge→air. Далее девять отдельных проверок water data 0…8 в позиции игрока и отдельная проверка air на y+1, каждая с `fill ... air replace seagrass`. Команда удаления губки не отличает созданную губку от уже имеющейся, а селектор `@a` распространяет действия на всех игроков. Порядок команд может сделать предыдущую замену воды значимой для последующих detect; проверить движок и кратность.

**Дополнительный подробный разбор** (источник: `docs/manual-fire-spider-sponge.md`):

#### Sponge Sword и Wet Sponge Sword

**Предметы и получение.** 1.6 имеет только точный `effect:sponge_sword`: damage 6, durability 128, offhand true, enchantable 9/sword, self repair 128, recipe `F/F/E` с sponge и stick. В 2.x dry: damage 5, durability 128, offhand false, self repair 128/sponge 62, web/bamboo 15/10. Wet — отдельный ID damage 3, durability 64, offhand false, repair dry 64/sponge 32/wet 64 и **без** digger. У обоих 2.x не объявлен enchantable; оба имеют только on_hurt_entity → durability 1. Furnace/blast_furnace recipe получает wet и выдаёт dry, не наоборот. `elder_guardian` pool на dry содержит killed_by_player и chance 0.065, looting_multiplier 0.02; локальная привязка таблицы к ванильному entity отдельно не доказана.

**1.6.** Player → helper `entity:sponge` → controller: от **каждого** `@a` fill куба ±4 (729 геометрических координат) water→sponge и затем sponge→air. Далее девять detect water data 0…8 в позиции игрока и одна проверка air на y+1, каждая при прохождении запускает fill того же куба `air replace seagrass`; в конце `@a swords=2`. Команда очистки sponge не различает ранее существовавшую губку и созданную предыдущей командой; из-за порядка вода к моменту detect уже может измениться.

**2.x, удержание dry.** Family-gated первый шаг создаёт группу и objective `sponge_sword`. Отдельный шаг с `in_water_or_rain` делает fill куба ±2 (125 координат) water→sponge, звук и частицу, и добавляет игроку 1 к счёту — без проверки числа действительно заменённых water блоков. Следующий шаг **без того же фильтра** делает sponge→air и seagrass→air в том же кубе; существующую губку он тоже не отличает от временной. При точном score 150, 155 или 160 запускается wet-событие: при dry в `hand` команда заменяет `slot.weapon.mainhand` на wet, обнуляет score и показывает title. Проверка hand не идентична явно выбранному mainhand в команде; состояние исходного item и результат при конфликтующих слотах не установлены.

**2.x, выброшенный dry.** По имени функция добавляет tag `sponge_sword`; `item.json` при теге и `in_water_or_rain` включает отдельную группу с random timer `[0,1]` и командами, меняющими water, sponge и seagrass в кубе ±2. По timer загружается структура `wet_sponge_sword`, затем исходная item-сущность уничтожается; stop при выходе из условия снимает группу. Это **не** player scoreboard 150/155/160. Возможное состояние предмета, назначение тега и взаимный порядок событий не доказываются NBT.

### Что написано на скриншотах

На изображении вручную считаны: damage = `5`; durability = `128`; enchantable = `true`; repairable = `true`. Оригинал: [скриншот 115955](https://drive.google.com/file/d/1a7kOeS7_zMxTw7QFgoCGLAlh_f1O3_vp/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 36. Sword Of Time — `effect:sword_of_time`

**Кратко:** Отдельный ID версии 1.6: команды времени и глобальных правил. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

**1.6** — определение `Sword_B/items/Sword of Time.json`.
- урон: `7`; максимальная прочность: `{"max_durability":128}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `true`; размер стопки: `1`; свечение: не указан; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:sword_of_time"]` → `128`.
- Оружейный компонент не указан.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

- В 2.x предмет с этим точным ID не найден.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 1.6:**

- Рецептов с этим точным результатом локально не найдено. Это не исключает других путей.

- Определение: `Sword_B/items/Sword of Time.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

### Способности, условия и вероятности по файлам

**Старая версия 1.6** (источник: `docs/manual-traces-1.6.md`):

#### Sword of Time: 1.6

[Значки и render_offsets, включая разницу регистра client/atlas](item-visual-index.md).

Предмет называется `effect:sword_of_time` (не совпадает с `effect:time_sword` 2.8.14): `items/Sword of Time.json` задаёт damage 7, durability 128, enchantability 9, self repair 128, glint true, offhand true. `player.json` создаёт `entity:time`, который подключает `controller.animation.time`; оба состояния выполняют `gamerule randomtickspeed 300`, `effect @e speed 1 15 true`, `time add 30`, `scoreboard players set @a swords 2`. В отличие от Time Sword 2.8.14 selector `@e` не исключает игроков, и в архиве 1.6 отсутствует идентичный предмет ID `effect:time_sword`. `normal.mcfunction` задаёт randomtickspeed 1 без сохранения прежнего значения. Как часто контроллеры конкурируют друг с другом, устанавливается только испытаниями.

**Дополнительный подробный разбор** (источник: `docs/manual-spectral-time-comparison.md`):

#### Sword of Time 1.6

Точный ID `effect:sword_of_time`, файл `Sword_B/items/Sword of Time.json`: damage 7, durability 128, offhand true, glint true, enchantable 9/sword, self repair 128; прямого локального recipe/loot с этим **точным** result/ID не найдено. При этом `recipes/Sword_of_Time.json` задаёт result и identifier `effect:Sword_of_Time` с другим регистром; pattern `#SS/SBS/NS#`, но `#` отсутствует в key. Нельзя без проверки считать результат тем же ID или исправлять символы. Клиентский icon `Sword_of_Time` и atlas key `sword_of_time` различаются регистром; поведение разрешения имени на движке неизвестно. В item нет on-use/weapon.

Hand sensor добавляет группу spawn `entity:time` с wait 0/0, single_use true → `controller.animation.time`. Оба состояния on_entry идентичны: `gamerule randomtickspeed 300`, `effect @e speed 1 15 true`, `time add 30`, `scoreboard players set @a swords 2`. В `@e` **нет исключения player** и нет r; это не ограничение владельцем. Независимая функция общего сброса `normal.mcfunction` задаёт `randomtickspeed 1`, а не сохранённое прежнее значение. Частота переключения, сфера выбора `@e` и успех команд не известны.

### Что написано на скриншотах

Сопоставленной карточки чисел на скриншотах нет; это не значит, что предмет нигде на изображениях не упомянут.

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 37. Time Sword — `effect:time_sword`

**Кратко:** Отдельный предмет 2.x с влиянием на время и мир. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

- В 1.6 предмет с этим точным ID не найден.

**2.8.8 / 2.8.14** — определение `Swords_B/items/time_sword.json`.
- урон: `13`; максимальная прочность: `{"max_durability":13770}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `false`; размер стопки: `1`; свечение: `true`; предмет исчезает: не указан.
- Ремонт: компонент не указан; это не доказывает невозможности ремонта.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`; событие без нанесения урона существу → `{"event":"weapon"}`; удар по блоку → `{"event":"weapon"}`.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 2.8.14:**

- Рецептов с этим точным результатом локально не найдено. Это не исключает других путей.

- Определение: `Swords_B/items/time_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[0].Mainhand[0].Name
  - `Swords_B/structures/time_sword.mcstructure` $.entities[0].Item.Name

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Time Sword (`effect:time_sword`) и фонтан желаний

[Сравнение 1.6/2.x и глобальных эффектов](manual-spectral-time-comparison.md#clock-sword-и-time-sword-2x).

[Точные блоки фонтана, вложенные условия и расход сущности предмета](manual-fountain-2.8.md).

- `items/time_sword.json`: damage 13, durability 13770, foil true, max stack 1, offhand false, `minecraft:enchantable` **задан** value 9/slot sword; `minecraft:repairable` отсутствует. На все три weapon-хука вызывается выбор: 90/100 прочности 1, 6/100 — 16, 3/100 — 32, 1/100 — 64. Web 15/bamboo 10. Позиция/масштаб first-person `[1,0.5,-3]`/`[0.04,0.04,0.04]`, third-person `[0.95,3.3,-1.2]`/`[0.06,0.06,0.06]`. На скриншоте `Screenshot_20261104_115910_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg` заявлено `Enchantable: false` — это противоречит наличию компонента в архиве; проверить фактическое действие и версию описания.
- `player.json:206–212,894–903,1537–1559`: сенсор `hand` запускает без дополнительного фильтра добавление группы movement value 1/family `[player,time_sword]` и команды: `gamerule randomtickspeed 300`, `effect @e[type=!player] speed 1 15 true`, `time add 30`, `event entity @a[family=default_player] time_sword_movement`, два fill для `effect99:lightblock2` в кубе 3×3×3. Другим default_player добавляется группа movement value 1. Это глобальные воздействия: селекторы не ограничены радиусом и одна активация меняет gamerule мира. При остановке по family time_sword задаётся **фиксированное** randomtickspeed 1, speed 0 всем non-player и событие `default_player` для всех игроков family default_player; исходное значение и эффекты не сохраняются. Команда `default_player` только добавляет группу, явного удаления `time_sword_movement` в ней нет — поведение конфликтующих компонентов и взаимодействие с Clock Sword/несколькими владельцами требуется тестировать. Частота `time add 30` зависит от работы сенсора.
- Выброшенный Clock Sword сначала получает тег `wish_3` функцией `functions/commands/swords_and_more_swords/swords_and_more_swords/tag_swords.mcfunction` по **отображаемому имени** `§l§gClock Sword`; функция вызывается из `player.json` событием `minecraft:constant_events`. Затем `entities/item.json:87–108,138–142` для wish_3 последовательно проверяет точные блоки: water data 0 в центре и четырёх соседях x/z; sandstone data 0 в этих же пяти точках на y−1; sandstone в центре на y+4 и на четырёх диагоналях x/z ±1 на y+2. Только после всех старых `execute ... detect` запускается `wish_3`. Это распознавание конфигурации блоков, не проверка ID структуры или биома «пустыня».
- `item.json:168–178`: при `wish_3` weight 975/1000 выполняет `time add 1000`, частицы, звук и `kill @s`; weight 25/1000 (2.5% на выбор) загружает `time_sword` на y+1, выполняет `time add 6000`, `fill ~15 ~10 ~15 ~-15 ~-15 ~-15 concretepowder 4 replace sand`, частицы/звук и `kill @s`. В обеих ветвях источник уничтожается, но успешность команд и применимость случайного выбора зависят от движка. Огромный объём fill и возможная граница максимума блоков требуют тестирования; факт наличия команды не гарантирует замены каждого блока.

**Дополнительный подробный разбор** (источник: `docs/manual-spectral-time-comparison.md`):

#### Clock Sword и Time Sword 2.x

`effect:clock_sword`: damage 7, durability 4800, offhand false, enchantable 9/sword, repair self 4800/clock 900/gold_block 780/gold_ingot 87, cooldown 30. Три weapon-хука → direct durability 1; on-use отдельно damage 10 и вызов `clock_sword_skill_event` только по `@s[family=clock_sword]`. Recipe `X##/#C#/I#X`: `#` = gold_block, C = clock, I = gold_ingot, но **X не определён** в key. Это исходная неоднозначность, не разрешение автоматически трактовать X как пустоту.

`effect:time_sword`: damage 13, durability 13770, offhand false, enchantable 9/sword, repairable не объявлен; все три weapon-хука выбирают direct durability 1/16/32/64 с весами 90/6/3/1. Математическое ожидание **3.46** относится только к этому вызову и стандартной нормализации, без штатного износа; не является расходом за секунду. Прямого локального рецепта этого результата нет. Отдельная фонтанная цепочка для тега выброшенного Clock Sword `wish_3` выбирает вес 975/25; в ветви 25 грузится структура Time Sword. Это 2.5% **на вызванный выбор** после 15 проверок блока, не шанс любого выброшенного Clock Sword.

Действие удержания Time задаёт randomtickspeed 300, `effect @e[type=!player] speed 1 15 true`, `time add 30` и событие ускорения для `@a[family=default_player]`; у Clock аналогичные 100, speed 1/10 и time add 10 записаны в отдельном шаге при family `clock_sword_skill`. Skill Clock использует таймер `[5,5]` looping; stop обоих мечей записывает фиксированный randomtickspeed **1**, speed 0 для non-player и default_player выбранным игрокам. Это не сохранение старого gamerule или эффектов. В player ни `clock_sword_skill`, ни `clock_sword_movement`, ни `time_sword_movement` явно не названы в `remove.component_groups`; это не доказательство вечного действия, поскольку разрешение конфликтов компонент и replacement групп неизвестно.

Селекторы 2.x не гарантируют область за пределами текущего измерения или права выполнения; `@a` не привязывается исключительно к владельцу. При нескольких игроках и конкуренции со сбросом результат зависит от порядка и частоты вызовов. [Подробные условия и сценарии](manual-time-interactions-2.8.md) отделяют статический текст от будущей проверки.

**Связанный подробный механизм** (источник: `docs/manual-time-interactions-2.8.md`):

### Clock Sword и Time Sword 2.x: конкуренция глобального состояния

Статический разбор файлов из `swordsandmoreswords-2-8-14.mcaddon`; соответствующие определения и команды, перечисленные ниже, проверены также в 2.8.8. Серверные испытания оригинала с одним игроком приведены ниже; эффекты на других игроков и мобов остаются отдельными вопросами. [Карточки Clock и Time](manual-traces-2.8.14.md) · [состояние анализа](analysis-status.md).

#### Входы, значения и цели

**Испытание оригинала 2.8.8 / Bedrock 1.20.50.03:** в отдельном мире отключили обычную смену дня и установили `randomtickspeed = 7`. Без меча время не менялось. С Time Sword в руке скорость случайных обновлений стала 300, игровое время ускорилось; после смены предмета скорость стала **1, не прежние 7**, а ускорение времени остановилось.

При удержании Clock Sword до применения значение оставалось 7; после применения ботом оно стало 100 и время ускорилось. Спустя несколько секунд способность прекратилась при всё ещё удерживаемом мече, а `randomtickspeed` стало 1. Износ меча при применении изменился с 0 до 10. Это наблюдения одного игрока на тестовом сервере, не проверка конфликтов нескольких игроков. [Журналы и сценарии](../data/original-mechanics-2026-11-07/README.md).

| Действие | Откуда вызывается | Глобальные команды и объекты |
|---|---|---|
| Удержание Clock | `player.json:1011–1015,1178–1196` проверяет в `hand` `effect:clock_sword`. При отсутствии family clock_sword первый шаг добавляет группу; **отдельный второй шаг** срабатывает при family clock_sword_skill. | В нём добавляется `clock_sword_movement`; `gamerule randomtickspeed 100`; `effect @e[type=!player] speed 1 10 true`; `time add 10`; `event entity @a[family=default_player] clock_sword_movement`. |
| Использование Clock | `items/clock_sword.json:68–76,103–114`: cooldown duration 30; задан durability damage 10 и команда `event entity @s[family=clock_sword] clock_sword_skill_event`. | `player.json:38–45,1208–1214`: событие добавляет `clock_sword_skill`, где family `[player,clock_sword,clock_sword_skill]` и looping timer `[5,5]`, randomInterval false, вызывает `stop_clock_sword_event` на self. `damage` и `run_command` — поля одного объекта, их очередность не предполагается. |
| Удержание Time | `player.json:894–896,1537–1545` проверяет в `hand` `effect:time_sword`; событие без дополнительного family-фильтра сначала добавляет `minecraft:time_sword`, затем выполняет команды. | `gamerule randomtickspeed 300`; `effect @e[type=!player] speed 1 15 true`; `time add 30`; `event entity @a[family=default_player] time_sword_movement`; два fill куба ±1 для `effect99:lightblock2`, сначала replace air, затем replace того же блока. |
| Остановка Clock | Таймер skill и отдельный sensor отсутствия Clock вызывают `stop_clock_sword_event`; его шаг требует self family `clock_sword` (`player.json:1018–1022,1198–1206`). | Удалить `minecraft:clock_sword`, выполнить `gamerule randomtickspeed 1`, `effect @e[type=!player] speed 0 0`, `event entity @a[family=default_player] default_player`, добавить `minecraft:default_player`. |
| Остановка Time | Sensor отсутствия Time вызывает `stop_time_sword_event`; его шаг требует self family `time_sword` (`player.json:899–903,1547–1555`). | Удалить `minecraft:time_sword`, добавить `minecraft:default_player`, выполнить те же три команды сброса (randomtickspeed 1, speed 0, default_player). |

`randomtickspeed` — gamerule, не записанная копия исходного значения; `time add` меняет время, и отдельной обратной команды в этих событиях нет. У `@e` нет радиуса и указан `type=!player`; нельзя из этого заключать, что целью являются игроки или все сущности во всех измерениях. `@a[family=default_player]` выбирает не только владельца: области действия селекторов и действия command permission зависят от движка/контекста. Фактическое действие `speed 0 0` и совместимость старой команды необходимо проверить; нельзя утверждать, что она точно восстанавливает доаддонные эффекты.

#### Что остаётся без явного удаления

В `Swords_B/entities/player.json` буквальные ссылки на `clock_sword_skill`, `clock_sword_movement`, `time_sword_movement` встречаются в определениях, добавлениях, фильтрах и командах, но **ни одна группа не перечислена в `remove.component_groups` этого файла**. Событие `default_player` лишь добавляет `minecraft:default_player`; его компоненты включают пустой `minecraft:timer`, movement 0.1 и family `[player,default_player]`. Группы Clock/Time movement задают movement 1.

Это не доказательство вечного ускорения или многократного срабатывания таймера: добавление `default_player` и других групп может переопределить те же компоненты, а правила порядка/замещения неизвестны. В частности, хотя timer `clock_sword_skill` записан looping, нельзя без опыта считать, что он гарантированно сохраняется после добавления другой группы. Семантику следует сравнить на исходной версии.

#### Сценарии конфликтов для проверки

1. В мире предварительно выставить отличное от 1 значение randomtickspeed, затем активировать и остановить каждый меч отдельно: зафиксировать точное значение до, во время и после, а также время и эффекты.
2. Игрок A удерживает Time, игрок B активирует и останавливает Clock; повторить в обратном порядке и при смене меча одним игроком. Обе остановки записывают 1, а активные команды записывают 100 или 300; какая запись окажется последней и как часто она повторится, заранее не известно.
3. Проверить игрока без меча с family default_player и с другим мечом; зафиксировать movement и принадлежность к группам до, во время и после действия. Внешние `@a` и наложение одноимённого компонента нельзя безопасно заменить локальным ускорением владельца без сравнения.
4. После одного использования Clock наблюдать минимум несколько таймерных интервалов, оставляя меч в руке и сменив его до окончания; записать условия stop, сохранение family и фактические вызовы. Не предполагать, что `duration 30` предмета и timer `[5,5]` имеют одну и ту же роль.
5. Наблюдать обычных мобов, помощников и предсуществующие speed-эффекты до и после остановки каждого меча. Проверить ограничения измерения, радиуса и совместимость синтаксиса, не принимая текст команды за гарантированное восстановление состояния.

### Что написано на скриншотах

На изображении вручную считаны: damage = `13`; durability = `13770`; enchantable = `false`; repairable = `false`. Оригинал: [скриншот 115910](https://drive.google.com/file/d/1rCL9RKVJCIfjHme7CkmOEe82NpJyCn1A/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 38. Tnt Sword — `effect:tnt_sword`

**Кратко:** Малые снаряды и отдельный большой TNT при использовании. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

**1.6** — определение `Sword_B/items/tnt_sword.json`.
- урон: `7`; максимальная прочность: `{"max_durability":1}`; зачарование: не указан; перезарядка: не указан; левая рука: `true`; размер стопки: `1`; свечение: не указан; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:tnt_sword"]` → `1`.
- Оружейный компонент не указан.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**2.8.8 / 2.8.14** — определение `Swords_B/items/tnt_sword.json`.
- урон: `4`; максимальная прочность: `{"max_durability":64}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: `{"category":"tnt_sword","duration":10}`; левая рука: `false`; размер стопки: `1`; свечение: `false`; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:tnt_sword"]` → `64`; `["minecraft:tnt"]` → `18`.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`; событие без нанесения урона существу → `{"event":"weapon"}`; удар по блоку → `{"event":"weapon"}`.
- При использовании предмета указано: `{"on_use":{"event":"on_use"}}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 1.6:**

- Рецепт `Sword_B/recipes/tnt_sword.json`; тип `minecraft:recipe_shaped`.
  - Схема сверху вниз: `F` / `F` / `E`.
  - Обозначения: `{"E":{"item":"minecraft:stick"},"F":{"item":"minecraft:tnt"}}`.
  - Результат: `{"item":"effect:tnt_sword"}`; рабочие станции/tags: `["crafting_table"]`.

- Определение: `Sword_B/items/tnt_sword.json`.
- Результаты рецептов: `Sword_B/recipes/tnt_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

**Архив 2.8.14:**

- Рецептов с этим точным результатом локально не найдено. Это не исключает других путей.

- Определение: `Swords_B/items/tnt_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - `Swords_B/loot_tables/chests/desert_pyramid.json` $.pools[0].entries[8]: `{"type":"item","name":"effect:tnt_sword","weight":10}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[11].Mainhand[0].Name

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

**Условная математическая модель выбора loot в 2.x:**

Числа ниже — вероятность выбрать хотя бы одну запись предмета внутри уже активированного пула, а не шанс реальной добычи. Допущения: все записи доступны; отсутствующий вес принят за 1; quality и условия записей игнорируются; выборы независимы с возвращением; число rolls равномерно в указанном диапазоне. Условия пула считаются уже выполненными. Загрузка таблицы, дополнительный отбор, количество предметов и функции не эмулируются.

- Таблица/пул: `chests/desert_pyramid.json` / 0; entries: 8; rolls: `{"min":2,"max":4}`; вес ID/сумма: 10/242; выбор хотя бы одной записи по модели: **11.8392%**. Условия и оговорки: functions: не задано.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### TNT Sword (`effect:tnt_sword`)

[Сравнение цепочек 1.6/2.x](manual-ender-wither-tnt-slime.md#tnt-sword).

- `items/tnt_sword.json`: damage 4, durability 64, enchantability 9/sword, cooldown category tnt_sword duration 10, offhand false; repair self 64 или `minecraft:tnt` 18. На все три weapon-хука: расход 1, затем randomize 10 пусто / 90 `shoot entity:tnt`, launch_power 1; 90/100 — доля при вызове события, а не гарантированный взрыв. On use — summon `minecraft:tnt ~~~ giant_tnt`, actionbar `@a[r=18]`, `playsound random.fuse @a`, отдельно durability damage 18. Порядок двух соседних полей события и фактическая валидность старого синтаксиса требуют проверки.
- `entities/entity_tnt.json`: `entity:tnt`, runtime snowball, projectile power 2/gravity 0, collision 0×0, impact damage 1/knockback true/`destroy_on_hit:false`, on-hit вызывает `mini_explosion`: fuse_length 0, power 1, fire false, destroy affected by griefing true. Постоянный looping timer `[0.1,0.1]` добавляет компонент `despawn`. Существуют условия гонки между попаданием и удалением: не считать что 90% выбора означает 90% попадания.
- `entities/tnt.json`: кастомное определение `minecraft:tnt` добавляет `default_tnt` при entity_spawned (fuse 4, power 4, fire false). `giant_tnt` удаляет default_tnt и добавляет группу scale 2, fuse 8, power 16, fire true, destroy_affected_by_griefing true. Таймер `[7.99,7.99]` до взрыва запускает camerashake `@a[r=32] 0.2 0.8 positional` и звук `random.explode` с параметрами 2, 0.4, 2. В `from_explosion` задан диапазон fuse 0.5…2, power 4, fire false. Совместимость события summon и порядок entity_spawned/giant_tnt нужно проверить.
- Выпавшему предмету функция назначает тег `tnt_sword` по имени `§4TNT§f Sword`; `animation_controllers/item_events.json` при `q.is_on_fire` вызывает `despawn_event_5` для этого тега. В `item.json:207–209` event вызывает `summon entity:instant_giant_explode` без координат и `kill @s`; `instant_giant_explode.json` задаёт fuse 0.02, power 16, fire true и timer 0 для эффектов. Порядок вызова, в том числе до назначения тега, важен.
- `loot_tables/chests/desert_pyramid.json`: первый пул 2–4 rolls, weight меча 10 из 242; это 10/242 на одну выборку при стандартной семантике и не вероятность на сундук.

##### Дополнение к Sponge Sword: выброшенный предмет

Сухой меч на земле обрабатывается не тем же счётчиком, что удерживаемый: `tag_swords.mcfunction` добавляет тег `sponge_sword` по имени `§l§eSponge Sword`; `entities/item.json:18–24,63–79,115–137` при теге и `in_water_or_rain` добавляет family `sponge_sword` с одноразовым random timer `[0,1]` к событию `wet_sponge_sword`. Одновременно команды заменяют воду на губку в кубе 5×5×5, а затем без отдельного фильтра удаляют губку и морскую траву в этом объёме. Событие таймера грузит структуру `wet_sponge_sword` и уничтожает исходную item entity; при выходе из воды/дождя группа снимается. Время назначения тега, кратность сенсора, отмена таймера и перенос состояния предмета требуют испытаний. Эта отдельная цепочка ранее отсутствовала в ручной карточке.

**Старая версия 1.6** (источник: `docs/manual-traces-1.6.md`):

#### Creeper Sword и TNT Sword: 1.6

[Массовые цели Ender/Wither/Creeper/TNT и матрица типов](manual-area-targets-1.6.md).

- `items/creeper_sword.json`: damage 8, durability 1500, enchantability 9, self repair 1500, offhand true; явного on-use/cooldown и weapon-event в определении нет. Sensor → `entity:creeper` → `controller.animation.creeper`. Оба состояния создают objective c, прибавляют 1 всем сущностям r=16, при `@p[c=90]` воспроизводят звук; 27 отдельных селекторов перечисленных типов с точным `c=100` и r=16 призывают `entity:explode`, при score ближайшего игрока c=300 удаляется objective, затем `@a swords 2`. Типы включают tnt и wither, но не все сущности; точный список и порядок — в [реестре](animation-ledger-1.6.md). Это не мини-криперы по вероятности 20/100 из 2.8.14.
- `items/tnt_sword.json`: damage 7, durability **1**, self repair 1, offhand true, enchantable не указан. Sensor → `entity:tnt_sword` → `controller.animation.tnt`; каждый вход обоих состояний содержит 26 команд summon `entity:explode` в точках указанных типов в кольце `rm=10,r=15`, потом устанавливает `swords=2` всем игрокам. Командой не проверяется использование предмета. `entities/explode.json`: `minecraft:explode` с legacy-ключами `fuseLength:0`, `fuseLit:true`, power 4, `causesFire:false`, destroy_affected_by_griefing true; это отдельный формат от `entity:tnt` и `minecraft:tnt` 2.8.14. Работоспособность camelCase, частота state transitions, радиусы и конфликт scoreboard нужно проверить.

**Дополнительный подробный разбор** (источник: `docs/manual-ender-wither-tnt-slime.md`):

#### TNT Sword


**Практика 2.8.8 / 1.20.50.03:** в survival применение создало TNT и увеличило Damage меча на 18. При `mobgriefing=true` рядом стоявший каменный блок позже исчез; в отдельном creative-тесте камень на x+2 исчез, а на x+12 сохранился. Это не измерение полного радиуса. Игрок в survival погиб от взрыва после попытки отвода, но его позиция в момент взрыва не проверена — безопасная дистанция не установлена. [Журнал](../data/original-mechanics-2026-11-07/README.md).

**Предмет и получение.** 1.6 damage 7, durability/self repair 1, offhand true, enchantable не задан, digger web 15/bamboo 10; recipe `F/F/E`, F = TNT, E = stick. 2.x damage 4, durability/self repair 64, repair TNT 18, offhand false, enchantable 9/sword и cooldown 10; **digger не объявлен**. Прямого рецепта этого результата 2.x локально не найдено. В `chests/desert_pyramid.json` pool 0: 2…4 rolls, weight меча 10 при сумме явно указанных весов 242; 10/242 — модель одного выбора, не шанс на сундук.

**1.6.** Player → `entity:tnt_sword` → controller. Каждый вход обоих состояний содержит 26 отдельных type-команд `execute @e[r=15,rm=10,type=…] ... summon entity:explode` и `@a swords=2`, без on-use и без score-фильтра в самих командах. `entity:explode` задаёт legacy `fuseLength:0`, power 4, `causesFire:false`, destroy_affected_by_griefing true. Полный список и различие с Creeper/Wither — в [матрице](manual-area-targets-1.6.md#creeper-и-tnt-разные-выборки-для-одной-сущности-взрыва). Фактическую поддержку синтаксиса и разрушение нельзя вывести только из текста.

**2.x.** Три weapon-хука: durability 1 и randomize 10 пусто/90 `shoot entity:tnt` power 1. Эта кастомная сущность runtime snowball, impact damage 1, destroy_on_hit false; on-hit event добавляет `mini_explosion` fuse 0/power 1, а timer `[0.1,0.1]` может отправить despawn. Вероятность выбора не гарантирует попадание до удаления. On-use: `summon minecraft:tnt ~~~ giant_tnt`, actionbar `@a[r=18]`, `random.fuse @a`, отдельно durability 18; это **другая** сущность, чем `entity:tnt`. `minecraft:tnt` giant_tnt группа: scale 2, fuse 8, power 16, fire true, griefing true; timer `[7.99,7.99]` даёт shake и звук. Выброшенный item при огне после назначения тега вызывает ещё третью сущность `entity:instant_giant_explode` (fuse 0.02, power 16, fire true) и `kill @s`. События не следует объединять в одну вероятность взрыва.

### Что написано на скриншотах

На изображении вручную считаны: damage = `4`; durability = `64`; enchantable = `true`; repairable = `true`. Оригинал: [скриншот 115934](https://drive.google.com/file/d/12oKa5cnYV5yDSpreB54Pfe2KaqOx8FaK/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 39. Ultra Instinct Sword — `effect:ultra_instinct_sword`

**Кратко:** Снаряд, защита от части видов урона и цепочка фонтана. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

- В 1.6 предмет с этим точным ID не найден.

**2.8.8 / 2.8.14** — определение `Swords_B/items/ultra_instinct_sword.json`.
- урон: `16`; максимальная прочность: `{"max_durability":9999}`; зачарование: не указан; перезарядка: `{"category":"ultra_instinct_sword","duration":61}`; левая рука: `false`; размер стопки: `1`; свечение: `true`; предмет исчезает: `false`.
- Ремонт: компонент не указан; это не доказывает невозможности ремонта.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`.
- При использовании предмета указано: `{"on_use":{"event":"on_use"}}`.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":999},{"block":"minecraft:bamboo","speed":999}]}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 2.8.14:**

- Рецептов с этим точным результатом локально не найдено. Это не исключает других путей.

- Определение: `Swords_B/items/ultra_instinct_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[20].Mainhand[0].Name
  - `Swords_B/structures/ultra_instinct_sword.mcstructure` $.entities[0].Item.Name

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Ultra Instinct Sword (`effect:ultra_instinct_sword`)

[Подробные получение, снаряды и связи](manual-ghost-nether-ultra.md#ultra-instinct-sword).

- `items/ultra_instinct_sword.json`: damage 16, durability 9999, foil true, should_despawn false, enchantable/repairable не заданы, cooldown 61, offhand false, digger web/bamboo speed 999. On_hurt_entity durability 1; on_use shoot `entity:ultra_instinct_projectile` power 1, durability 48 и звук. Получение из фонтана через `wish_1` и `wish_2` описано в Quartz Diamond; данные самого предмета и результаты проверяются раздельно.
- `player.json`: группа knockback_resistance 1, movement в отдельной группе 0.22, таймер random `[0.1,0.2]` looping: выбор 15 равновесных частиц и звука. Действие удержания снимает перечисленные восемь эффектов hunger, blindness, slowness, weakness, mining_fatigue, nausea, instant_damage, wither и размещает светоблок; camerashake `@a[r=32]`. Sensor урона первая ветка исключает lava, drowning, void, thorns, suicide, starve, fire, fire_tick, magic и на другие виды задаёт `deals_damage:false` плюс `spreadplayers ~ ~ 1 3 @s`. Отдельные фильтры отключают fire, fire_tick и block/entity explosion; для lava явно deals_damage true. Не называть это иммунитетом ко всему и не предполагать успех телепортации. Перекрытие нескольких triggers надо проверить.
- `entities/ultra_instinct_projectile.json`: runtime snowball, collision 0, projectile power 2/gravity 0, impact 64, inertia 1/liquid_inertia 2; on_hit вызывает `summon entity:ultra_instinct_explode`. Environment sensor с `projectile_particle` выполняет не только particle, но и **`kill @e[type=item,r=24]`**, потенциально уничтожая все предметы на земле вокруг снаряда. Ageable duration 3 ссылается на `minecraft:end_scale`, но такого события в файле нет. `ultra_instinct_explode.json`: fuse 0, power 8, fire false, `max_resistance:4.0`, griefing true. Разрушение bedrock и фактическую семантику max_resistance нужно испытать; по одной записи нельзя гарантировать добычу.

**Дополнительный подробный разбор** (источник: `docs/manual-ghost-nether-ultra.md`):

#### Ultra Instinct Sword

`effect:ultra_instinct_sword`: damage 16, durability 9999, cooldown 61, offhand false, `should_despawn:false`, enchantable и repairable не объявлены; digger web/bamboo 999/999. Только on_hurt_entity задаёт прямую потерю durability 1; on-use отдельно задаёт shoot `entity:ultra_instinct_projectile`, durability 48 и звук. Прямых локальных recipe и loot entry с этим ID не найдено; структура содержится в архиве. В фонтане теги `wish_1`/`wish_2` срабатывают по именам выброшенных материалов и строгой геометрии, после чего выбирают success 8/1000 или 25/1000 соответственно — это не гарантия получения и не отдельные рецепты меча.

Player damage sensor для одного trigger требует все девять `has_damage !=` значений lava/drowning/void/thorns/suicide/starve/fire/fire_tick/magic и задаёт deals_damage false вместе с событием spreadplayers; отдельные triggers также задают false для fire, fire_tick и block/entity explosion, и **true для lava**. Отсутствие явно заданного false для drowning, void, thorns, suicide, starve или magic не доказывает общий иммунитет. Перекрытие возможных triggers и действительную защиту нельзя разрешить только по тексту. Отдельная movement-группа 0.22 явно снимается в stop Ultra, в отличие от `ghost_movement` в stop Ghost.

Projectile runtime snowball, collision 0×0, power 2/gravity 0, impact 64; on-hit вызывает `entity:ultra_instinct_explode`, power 8/max_resistance 4.0/fire false/griefing true. Event `projectile_particle` содержит **`kill @e[type=item,r=24]`**: это все подходящие item-сущности в селекторе вокруг контекста projectile, не только цель или предметы владельца. Ageable указывает отсутствующий в этом entity event `minecraft:end_scale`; потенциальный внешний механизм не исключён. Не выводить гарантированное разрушение bedrock или получение его блоков из одного max_resistance.

В `player.json` есть ещё событие `shoot_ultra_instinct_projectile`: в одном объекте оно одновременно **add и remove** группу `ultra_instinct_projectile`, которая объявляет spawn одного одноразового одноимённого projectile с wait 0/0. Буквальный поиск по текстам JSON, mcfunction и JS обоих архивов обнаруживает имя события только в его собственном объявлении; внешние/динамические вызовы не исключены. Порядок соседних add/remove и фактическое создание из этой группы не установлены. Важно: это **не** тот же путь, что прямо объявленный item on-use `shoot` выше; отсутствие локального вызова player-event не доказывает отсутствие работы item-снаряда.

**Связанный подробный механизм** (источник: `docs/manual-fountain-2.8.md`):

### Фонтан желаний 2.x: условия, ветви и расход предметов

Статический разбор `Swords_B/entities/item.json`, функции тегирования и NBT-структур 2.8.14; соответствующие события и функция одинаковы в 2.8.8. Подробный [указатель вероятностных ветвей](randomize-index.md), [структуры](structures-2.8.14.md), [проверка получения](manual-acquisition-issues.md). Серверные результаты для отдельных условий и событий приведены ниже; полноценный игровой клиент не проверялся.

#### Вход: имя и tag, а не проверка ID

**Испытания оригинала 2.8.8 / 1.20.50.03:** при подключённом headless-игроке тестовый кварц-алмаз с вручную заданным именем `Quartz Diamond` автоматически получил `wish_1`; обычный алмаз с таким же именем тоже получил этот тег. Оба по отдельности исчезли в полной конструкции фонтана. Предметы создавались скриптом, не проверялась наковальня или отображение имён в обычном клиенте. В отдельном опыте после ручного тега фонтан поглотил целую item-entity со стопкой из 9 кварц-алмазов.

Прямой принудительный вызов исходных событий `wish_1`, `wish_2`, `wish_3` дал соответственно Ultra Instinct Sword, Ultra Instinct Sword и Time Sword. Это не наблюдение естественного получения и не измерение вероятностей: вызовы повторялись пачками до обнаружения награды. [Сценарии, вспомогательный пакет и журналы](../data/original-mechanics-2026-11-07/README.md).

`functions/commands/swords_and_more_swords/swords_and_more_swords/tag_swords.mcfunction` вызывается из события `minecraft:constant_events` игрока. Последние три команды выбирают `@e[type=item,name=...,tag=!...]` и добавляют:

| Точная строка имени в селекторе | tag | Sensor в item | Результат |
|---|---|---|---|
| `Quartz Diamond` | `wish_1` | `fountain_of_wishes_1` | `wish_1` |
| `Quartz Diamond block` | `wish_2` | `fountain_of_wishes_2` | `wish_2` |
| `§l§gClock Sword` | `wish_3` | `fountain_of_wishes_3` | `wish_3` |

Sensor в `entities/item.json:87–108` проверяет соответствующий **tag**, но сам по себе не проверяет item ID. Переименованные предметы, локализация, порядок загрузки и отсутствие активного игрока могут изменить исход; не считать этот механизм проверкой конкретного ID. Совпадение имени с кварц-алмазом в контролируемых условиях подтверждено выше; приоритет совпадения разных тегов остаётся не проверен.

#### Распознаваемая геометрия

Каждый из трёх событий `fountain_of_wishes_*` (`item.json:138–142`) содержит одну старую цепь из **15** вложенных `execute @s ~ ~ ~ detect ...`; после последнего detect отправляет себе `wish_1`, `wish_2` или `wish_3`. Условия по типу и старому data `0` с позициями относительно контекста команды:

| Материал | Смещения (x, y, z) в порядке исходных команд |
|---|---|
| `water 0` | `(0,0,0)`, `(1,0,0)`, `(-1,0,0)`, `(0,0,1)`, `(0,0,-1)` |
| `sandstone 0` | `(0,-1,0)`, `(1,-1,0)`, `(-1,-1,0)`, `(0,-1,1)`, `(0,-1,-1)`, `(0,4,0)`, `(1,2,1)`, `(-1,2,-1)`, `(-1,2,1)`, `(1,2,-1)` |

Это проверка конкретных 15 позиций, а не явная проверка биома, ID сгенерированной структуры, прочих блоков фонтана или водного потока. Связь дробной позиции item-сущности с блоками, проверка water data, вложенный execute и фактический вызов события требуют теста движка. Точная строка без нормализации пробелов сохранена в исходнике и [реестре сущностей](entity-ledger-2.8.14.md).

#### Что делает каждая ветвь

| Событие | Веса в исходном порядке | Ветка меньшего веса | Ветка большего веса |
|---|---|---|---|
| `wish_1` | `992,8` | Загрузка `ultra_instinct_sword` на `~ ~1 ~`, fill песка, частицы/звук, `kill @s` | Частица, `kill @s` |
| `wish_2` | `975,25` | То же, что wish_1 | Частица, `kill @s` |
| `wish_3` | `975,25` | Загрузка `time_sword` на `~ ~1 ~`, `time add 6000`, fill песка, частица/звук, `kill @s` | Частица, `time add 1000`, звук, `kill @s` |

При стандартном выборе по заданным весам меньшие ветви равны 8/1000 = 0.8% и 25/1000 = 2.5% **на соответствующий выбор**, не обязательно на каждый выброшенный предмет или успешное получение. `wish_1`/`wish_2` в меньшей ветви используют `fill ~15 ~10 ~15 ~-15 ~-15 ~-15 concretepowder 0 replace sand`; `wish_3` — тот же объём с data **4**. При включительных координатах это 31×26×31 = **24 986 позиций рамки**, не обязательно столько изменённых блоков: фактически подходят только совпадающие `sand`, а успешность команды, ограничения мира и доступность чанков не проверены. Содержимое `time_sword.mcstructure` и `ultra_instinct_sword.mcstructure` — по одной item-сущности с одноимённым `Item.Name`, Count 1, дополнительные NBT поля в реестре структур.

**Все шесть ветвей содержат `kill @s`**, после остальных действий, поэтому в тексте удаляется item-**сущность**, а не явно снимается одна единица из Item.Count. `effect:quartz_diamond` имеет `minecraft:max_stack_size: 9`, тогда как Clock Sword — 1. Если выброшенный стак представлен одной сущностью с Count больше 1 и команды работают в обычном контексте, это может поглотить весь стак и всё равно произвести один выбор; реальное объединение стаков, момент тегирования и выполнения `kill` нужно измерить в игре. Нельзя переносить это как гарантированный расход одной штуки.

Если у одной сущности одновременно окажутся несколько `wish_*` tags, соответствуют нескольким sensor-условиям и каждый запускает собственную ветвь; код не содержит общей блокировки в этих строках. Как разрешается одновременное срабатывание и `kill @s`, не установлено. Аналогично нельзя считать успешной загрузку структуры только из-за присутствия команды: проверяются размер/координаты, регистрация структуры и завершение каждой команды по отдельности.

### Что написано на скриншотах

На изображении вручную считаны: damage = `16`; durability = `9999`; enchantable = `false`; repairable = `false`. Оригинал: [скриншот 120025](https://drive.google.com/file/d/1vSQHbdMLZTGGVBVDzBWT7r_Vm9oyZznG/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 40. Wet Sponge Sword — `effect:wet_sponge_sword`

**Кратко:** Мокрая версия; в печи указан рецепт возвращения сухой. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

- В 1.6 предмет с этим точным ID не найден.

**2.8.8 / 2.8.14** — определение `Swords_B/items/wet_sponge_sword.json`.
- урон: `3`; максимальная прочность: `{"max_durability":64}`; зачарование: не указан; перезарядка: не указан; левая рука: `false`; размер стопки: `1`; свечение: `false`; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:sponge_sword"]` → `64`; `["minecraft:sponge"]` → `32`; `["effect:wet_sponge_sword"]` → `64`.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 2.8.14:**

- Рецептов с этим точным результатом локально не найдено. Это не исключает других путей.

- Определение: `Swords_B/items/wet_sponge_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[18].Mainhand[0].Name
  - `Swords_B/structures/wet_sponge_sword.mcstructure` $.entities[0].Item.Name

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Sponge Sword и Wet Sponge Sword (`effect:sponge_sword`, `effect:wet_sponge_sword`)

[Сравнение цепочек 1.6/2.x](manual-fire-spider-sponge.md#sponge-sword-и-wet-sponge-sword).

- `items/sponge_sword.json`: damage 5, durability 128, ремонт self 128 и `minecraft:sponge` 62. `items/wet_sponge_sword.json`: damage 3, durability 64, ремонт dry sword 64, sponge 32, wet sword 64. Оба on_hurt_entity расходуют 1, max stack 1, offhand false. В обоих файлах **не задан** `minecraft:enchantable`, хотя описание на скриншоте заявляет `Enchantable: true` для сухого меча; значение по умолчанию и совместимость надо проверять, а не подменять.
- `player.json:213–215,880–889,1560–1606`: при наличии dry sword в hand первая подходящая ветвь добавляет family `[player,sponge_sword]` и команду создания scoreboard objective `sponge_sword dummy`. При `in_water_or_rain` выполняет `fill ~2 ~2 ~2 ~-2 ~-2 ~-2 sponge 0 replace water`, звук и частицы, затем увеличивает счёт игрока на 1. То есть условие включает дождь и повышение счёта не проверяет, был ли реально заменён блок воды.
- Независимый следующий шаг **в том же событии** выполняет `fill` всего объёма 5×5×5 в воздух с `replace sponge`, затем `replace seagrass`; текст команд не ограничивает удаляемую губку только той, что была создана предыдущим шагом. При точных значениях scoreboard 150, 155 или 160 вызывается событие `wet_sponge_sword`; при проверке hand dry sword оно выполняет `replaceitem ... slot.weapon.mainhand 0 effect:wet_sponge_sword 1`, сброс счёта 0 и actionbar. Возможны потеря прочности/зачарований при замене и сложности со слотами — необходимо проверить в игре. Это точные пороги счётчика, не заданное число секунд, и не условие «150 поглощённых блоков».
- `recipes/wet_sponge_sword.json` задаёт furnace и blast_furnace: input wet → output dry. `loot_tables/entities/elder_guardian.json` задаёт пул с `killed_by_player`, chance 0.065 и looting_multiplier 0.02; это условие таблицы, а не доказательство, что она была привязана/сработала в конкретной игре. Проверить ванильную привязку и семантику looting на исходном движке.

##### Дополнение к Fire Sword: противоречие описания

На изображении `Screenshot_20261104_115915_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg` описание заявляет: вода → obsidian, дождь → crystal sword. Однако в `Swords_B/entities/item.json:39–50,228–229` вода вызывает `fire_sword_event_2` и загрузку `glass_sword`, а дождь вне воды через таймер — `fire_sword_event_1` и `obsidian_sword`. Проверено по изображению и исходнику; не следует считать описание однозначным источником поведения или предполагать, что его версия совпадает с архивом.

**Дополнительный подробный разбор** (источник: `docs/manual-fire-spider-sponge.md`):

#### Sponge Sword и Wet Sponge Sword

**Предметы и получение.** 1.6 имеет только точный `effect:sponge_sword`: damage 6, durability 128, offhand true, enchantable 9/sword, self repair 128, recipe `F/F/E` с sponge и stick. В 2.x dry: damage 5, durability 128, offhand false, self repair 128/sponge 62, web/bamboo 15/10. Wet — отдельный ID damage 3, durability 64, offhand false, repair dry 64/sponge 32/wet 64 и **без** digger. У обоих 2.x не объявлен enchantable; оба имеют только on_hurt_entity → durability 1. Furnace/blast_furnace recipe получает wet и выдаёт dry, не наоборот. `elder_guardian` pool на dry содержит killed_by_player и chance 0.065, looting_multiplier 0.02; локальная привязка таблицы к ванильному entity отдельно не доказана.

**1.6.** Player → helper `entity:sponge` → controller: от **каждого** `@a` fill куба ±4 (729 геометрических координат) water→sponge и затем sponge→air. Далее девять detect water data 0…8 в позиции игрока и одна проверка air на y+1, каждая при прохождении запускает fill того же куба `air replace seagrass`; в конце `@a swords=2`. Команда очистки sponge не различает ранее существовавшую губку и созданную предыдущей командой; из-за порядка вода к моменту detect уже может измениться.

**2.x, удержание dry.** Family-gated первый шаг создаёт группу и objective `sponge_sword`. Отдельный шаг с `in_water_or_rain` делает fill куба ±2 (125 координат) water→sponge, звук и частицу, и добавляет игроку 1 к счёту — без проверки числа действительно заменённых water блоков. Следующий шаг **без того же фильтра** делает sponge→air и seagrass→air в том же кубе; существующую губку он тоже не отличает от временной. При точном score 150, 155 или 160 запускается wet-событие: при dry в `hand` команда заменяет `slot.weapon.mainhand` на wet, обнуляет score и показывает title. Проверка hand не идентична явно выбранному mainhand в команде; состояние исходного item и результат при конфликтующих слотах не установлены.

**2.x, выброшенный dry.** По имени функция добавляет tag `sponge_sword`; `item.json` при теге и `in_water_or_rain` включает отдельную группу с random timer `[0,1]` и командами, меняющими water, sponge и seagrass в кубе ±2. По timer загружается структура `wet_sponge_sword`, затем исходная item-сущность уничтожается; stop при выходе из условия снимает группу. Это **не** player scoreboard 150/155/160. Возможное состояние предмета, назначение тега и взаимный порядок событий не доказываются NBT.

### Что написано на скриншотах

На изображении вручную считаны: damage = `3`; durability = `64`; enchantable = `false`; repairable = `true`. Оригинал: [скриншот 120034](https://drive.google.com/file/d/14nhZwfS8-jwjz2vOlAQQd2-LXzlnE2l4/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 41. Wither Skeleton Sword — `effect:wither_skeleton_sword`

**Кратко:** Связан со снарядом wither_effect. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

- В 1.6 предмет с этим точным ID не найден.

**2.8.8 / 2.8.14** — определение `Swords_B/items/wither_skeleton_sword.json`.
- урон: `4`; максимальная прочность: `{"max_durability":128}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `false`; размер стопки: `1`; свечение: `false`; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:wither_skeleton_sword"]` → `128`; `["minecraft:coal"]` → `58`; `["minecraft:stick"]` → `2`.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 2.8.14:**

- Рецептов с этим точным результатом локально не найдено. Это не исключает других путей.

- Определение: `Swords_B/items/wither_skeleton_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - `Swords_B/loot_tables/entities/wither_skeleton.json` $.pools[3].entries[0]: `{"type":"item","name":"effect:wither_skeleton_sword","weight":1,"functions":[{"function":"set_data","data":0}]}`
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[28].Mainhand[0].Name

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

**Условная математическая модель выбора loot в 2.x:**

Числа ниже — вероятность выбрать хотя бы одну запись предмета внутри уже активированного пула, а не шанс реальной добычи. Допущения: все записи доступны; отсутствующий вес принят за 1; quality и условия записей игнорируются; выборы независимы с возвращением; число rolls равномерно в указанном диапазоне. Условия пула считаются уже выполненными. Загрузка таблицы, дополнительный отбор, количество предметов и функции не эмулируются.

- Таблица/пул: `entities/wither_skeleton.json` / 3; entries: 0; rolls: `1`; вес ID/сумма: 1/1; выбор хотя бы одной записи по модели: **100.0000%**. Условия и оговорки: pool conditions: `[{"condition":"killed_by_player"},{"condition":"random_chance_with_looting","chance":0.025,"looting_multiplier":0.02}]`; functions: `[{"function":"set_data","data":0}]`.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Wither Skeleton Sword (`effect:wither_skeleton_sword`)

[Полная сравнительная карточка 1.6/2.x](manual-heat-light-swords.md#wither-skeleton-sword--только-2x-среди-точных-id).

- `items/wither_skeleton_sword.json`: damage 4, durability 128, enchantability 9/sword, repair self 128, coal 58, stick 2; web speed 15/bamboo 10. On hurt entity в одном шаге задан durability damage 1 и shoot `entity:wither_effect` power 1, порядок соседних полей не доказан.
- `entities/wither_effect.json`: projectile runtime snowball, power 2/gravity 0, collision 0×0, impact damage 0/knockback true/destroy_on_hit true; `mob_effect` wither, `durationeasy`, `durationnormal`, `durationhard` все **200**, amplifier 0. Единицы этих параметров и реальное время эффекта следует подтвердить на целевой и исторической версии; не подменять молча секундами. Таймер `[0.1,0.1]` looping вызывает despawn, поэтому успешность применения зависит от столкновения до удаления. У environment sensor указан event `particle`, но в events этой сущности оно отсутствует: проверить сообщение загрузчика и поведение в игре.
- `loot_tables/entities/wither_skeleton.json`: четвёртый пул, killed_by_player, random_chance_with_looting chance 0.025 и multiplier 0.02, один roll и один меч, set_data 0. Таблица присутствует, но отсутствие одноимённого определения сущности в пакете требует проверки ванильной привязки; шанс заданного пула не означает гарантированный дроп в любой конфигурации мира.

**Дополнительный подробный разбор** (источник: `docs/manual-heat-light-swords.md`):

#### Wither Skeleton Sword — только 2.x среди точных ID

Точного ID `effect:wither_skeleton_sword` в item 1.6 нет. В обеих 2.x damage 4, max durability 128, stack 1, offhand false, enchantable 9/sword, web 15/bamboo 10; repair self 128, `minecraft:coal` 58 и `minecraft:stick` 2. Только weapon `on_hurt_entity` указан; его единственный элемент sequence одновременно задаёт durability damage 1 (`target:self`) и `shoot` projectile `entity:wither_effect`, `launch_power:1`. Не предполагать порядок соседних полей или попадание снаряда.

`entities/wither_effect.json` имеет runtime `minecraft:snowball`, collision 0×0, projectile power 2, gravity 0; impact damage 0, knockback true, destroy_on_hit true. `mob_effect` содержит wither, `durationeasy:200`, `durationnormal:200`, `durationhard:200`, amplifier 0. Timer `[0.1,0.1]`, looping true вызывает событие despawn, добавляющее группу despawn. Отдельный environment sensor ссылается на event `particle`, но в **этом** файле такого события нет; внешний/ванильный механизм не исключён. Параметры projectile и timer не доказывают контакт, применение эффекта или единицу его длительности.

Локальная `loot_tables/entities/wither_skeleton.json`, pool 3: `killed_by_player` и `random_chance_with_looting` chance 0.025, looting_multiplier 0.02, rolls 1, единственный меч weight 1 с `set_data:0`. В пакете нет одноимённого behavior entity, который явно привязывал бы таблицу; не считать её зарегистрированной или безусловной добычей. В отдельном соседнем pool 2 с аналогичными условиями указан skull, а не меч; не объединять вероятности без модели независимости/порядка движка.

### Что написано на скриншотах

На изображении вручную считаны: damage = `4`; durability = `128`; enchantable = `true`; repairable = `true`. Оригинал: [скриншот 120003](https://drive.google.com/file/d/1tAeJ-EbPeExgoe9AX_AR_p9cgZEangmO/view). Оригинал: [скриншот 120007](https://drive.google.com/file/d/18xMWPEmEQ3k8DUxotbJS2CD1IIXMbY6s/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 42. Wither Sword — `effect:wither_sword`

**Кратко:** Снаряды обычного и опасного черепа иссушителя. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

**1.6** — определение `Sword_B/items/wither_sword.json`.
- урон: `10`; максимальная прочность: `{"max_durability":1256}`; зачарование: `{"value":9,"slot":"sword"}`; перезарядка: не указан; левая рука: `true`; размер стопки: `1`; свечение: не указан; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:wither_sword"]` → `1256`.
- Оружейный компонент не указан.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

**2.8.8 / 2.8.14** — определение `Swords_B/items/wither_sword.json`.
- урон: `10`; максимальная прочность: `{"max_durability":3856}`; зачарование: не указан; перезарядка: `{"category":"wither_sword","duration":3}`; левая рука: `false`; размер стопки: `1`; свечение: `true`; предмет исчезает: `false`.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:wither_sword"]` → `3856`.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`; событие без нанесения урона существу → `{"event":"weapon"}`; удар по блоку → `{"event":"weapon"}`.
- При использовании предмета указано: `{"on_use":{"event":"on_use"}}`.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 1.6:**

- Рецепт `Sword_B/recipes/wither_sword.json`; тип `minecraft:recipe_shaped`.
  - Схема сверху вниз: `#SS` / `SBS` / `NS#`.
  - Обозначения: `{"N":{"item":"minecraft:blaze_rod"},"S":{"item":"minecraft:skull","data":1},"B":{"item":"minecraft:netherstar"}}`.
  - **В схеме есть символы без определения key: `["#"]`.** Их смысл и принятие рецепта движком не установлены.
  - Результат: `{"item":"effect:wither_sword"}`; рабочие станции/tags: `["crafting_table"]`.

- Определение: `Sword_B/items/wither_sword.json`.
- Результаты рецептов: `Sword_B/recipes/wither_sword.json` (`minecraft:recipe_shaped`).
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - Не обнаружено.

**Архив 2.8.14:**

- Рецептов с этим точным результатом локально не найдено. Это не исключает других путей.

- Определение: `Swords_B/items/wither_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[8].Mainhand[0].Name
  - `Swords_B/structures/wither_sword.mcstructure` $.entities[0].Item.Name

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Wither Sword (`effect:wither_sword`)

[Сравнение цепочек 1.6/2.x](manual-ender-wither-tnt-slime.md#wither-sword).

- `items/wither_sword.json`: damage 10, durability 3856, should_despawn false, foil true, repair self 3856, enchantable не задан, cooldown 3, offhand false; web 15/bamboo 10. On-use shoot `minecraft:wither_skull_dangerous` power 1, звук и durability 3. На три weapon-хука: durability 1, затем 90 пусто/10 обычный `minecraft:wither_skull` power 1 и звук.
- `entities/wither_skull.json` и `wither_skull_dangerous.json` указывают wither duration easy 0/normal 200/hard 800, amplifier 1; событие попадания добавляет fuse 0/power 1/fire false/griefing true, у dangerous дополнительно max_resistance 4.0. Для снарядов от other с мечом есть группы с отдельными параметрами: обычный projectile power 1.2/gravity 0.05; dangerous power 0.6/gravity 0.005, is_dangerous и reflect_on_hurt true. Единицы duration, принадлежность `other` и приоритет групп требуют проверки.
- `player.json`: family `[player,wither_sword]`, sensor не наносит damage wither, timer random 4…18 на два равновесных звука, rideable для family entity_name. При удержании в кубе 11×11×11 команды последовательно заменяют grass→dirt data 1, leaves/leaves2/vine→air, ice→water, farmland→dirt data 0, red/yellow flower и red/brown mushroom и double_plant→wither_rose; также `effect @s wither 39960 1 true` и свет. При снятии чистятся эффект и riders; предыдущие блоки не восстанавливаются. Селекторы и порядок команд могут менять окружение других игроков.
- `animation_controllers/wither_sword.json` при условии имени меча призывает rider `entity:name` с event `minecraft:wither_sword`; `entities/entity_name.json` назначает boss bar name `§l§4Wither Sword`, hud_range 64, `should_darken_sky:true`, health 1 и защиту от урона; отдельный controller удаляет его, когда он не riding. Это не health меча.
- `entities/wither.json`: сенсор fatal от other player с `effect:nether_star_sword` в hand вызывает `wither_sword`: 87 пусто/13 `structure load wither_sword` (13/100 условно на вызов). Выброшенному предмету по имени `§l§7Wither Sword` назначается тег, а `item_events` при огне вызывает `despawn_event_2`, звук/частицы и kill; сравнить с `should_despawn:false`, которое относится к другой характеристике.

- Выброшенный предмет с тегом `wither_sword` при `q.is_on_fire` получает событие `despawn_event_2`: частица `example_linearcurve`, `mob.wither.death @a[r=16]` volume 1/pitch 0.5, `kill @s`. NBT `wither_sword.mcstructure` содержит этот тег; его фактическое восстановление и взаимодействие с огнём зависят от загрузчика.

**Старая версия 1.6** (источник: `docs/manual-traces-1.6.md`):

- **Wither** — 10/1256; default содержит буквальную `/Effect99`, состояние wither — 46 команд: poison 30 amplifier 1 на `@e[r=16,type=!player]`, частицы всем игрокам, затем вокруг контроллера куб ±5 с grass→dirt 1, leaves/leaves2→air, ice→water, farmland→dirt 0 и перечисленными растениями/грибами→wither_rose. Objective w увеличивается у r=16 с перечнем исключений; на score 100 перечисленные типы призывают `entity:explode`, звуки при score игрока 200/500, удаление objective при 600. Точные селекторы и порядок — в исходном тексте; сравнение с более поздней реализацией и сохранность мира не установлены.

**Дополнительный подробный разбор** (источник: `docs/manual-ender-wither-tnt-slime.md`):

#### Wither Sword


**Практика 2.8.8 / 1.20.50.03:** при удержании в creative проверены превращения льда в воду, листьев в воздух и grass в dirt, а отдельно — красного цветка в wither_rose. После снятия меча исчезнувшие листья не восстановились, dirt и роза остались. Трава на x+7 от игрока не изменилась. Это конкретные проверенные блоки, не проверка всех материалов и расстояний. [Журнал](../data/original-mechanics-2026-11-07/README.md).

**Предмет и получение.** Damage 10 в обоих архивах, durability 1256 → 3856, offhand true → false, self repair соответствует максимальной durability. В 1.6 enchantable 9/sword, в 2.x он не объявлен; 2.x дополнительно `should_despawn:false`, cooldown 3. Рецепт 1.6 `#SS/SBS/NS#`, S = `minecraft:skull` data 1, B = буквальный `minecraft:netherstar`, N = blaze_rod; символ `#` в key не задан. Не исправлять отсутствующий key или ID по предположению. Прямого рецепта этого результата в 2.x локально нет; `entities/wither.json` на fatal damage от player с `effect:nether_star_sword` в hand вызывает randomize 87 пусто/13 `structure load wither_sword`. 13/100 — только условно на вызванный выбор. Сохранённая структура содержит меч; не гарантировать её загрузку или перенос состояния.

**1.6.** Hand sensor создаёт `entity:wither` через одноразовый spawn. В controller `default` содержит только буквальную `/Effect99`; состояние `wither` — **46** команд, а не тот же набор в обоих состояниях. Яд `@e[r=16,type=!player] poison 30 1 true`, частицы через `@a`, затем десять fill куба ±5 вокруг helper: grass→dirt 1, leaves/leaves2→air, ice→water, farmland→dirt 0 и пять видов растений→wither_rose. Objective `w` добавляется и начисляется отдельным `@e[r=16]` с десятью type-исключениями; 28 команд summon `entity:explode` выбирают отдельные типы с score ровно 100, удаление objective при подходящем `@p` score 600. Яд, начисление score и вызов взрывов используют разные селекторы; блоки не сохраняются для восстановления.

**2.x.** В weapon три хука: direct durability 1, randomize 90 пусто/10 `minecraft:wither_skull`; on-use отдельно запускает `minecraft:wither_skull_dangerous`, sound и durability 3. У обоих projectile wither durations easy/normal/hard 0/200/800, amplifier 1, и on-hit explosion power 1; опасный дополнительно max_resistance 4.0. Это не доказательство попадания или единиц duration.

Группа player отменяет damage с `has_damage:wither`, задаёт family, rideable и random timer `[4,18]`. Событие удержания содержит **11**, а не 10, fill в кубе ±5: к заменам 1.6 добавлен `vine→air`; далее `effect @s wither 39960 1 true` и два fill lightblock2 в плоскости y+2. Команда назначает эффект себе одновременно с damage sensor; иммунитет к урону и наличие значка/эффекта — разные вещи. Остановка очищает wither, удаляет группу и evict_riders, но не восстанавливает блоки. Выброшенный item после тега при огне получает отдельный event `kill @s`, несмотря на поле `should_despawn:false`; это разные механизмы.

### Что написано на скриншотах

На изображении вручную считаны: damage = `10`; durability = `3856`; enchantable = `false`; repairable = `true`. Оригинал: [скриншот 115920](https://drive.google.com/file/d/1ym1j2BhOsqJPPwqRzdPf0JUlIqYyPK4s/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## 43. Wolf Sword — `effect:wolf_sword`

**Кратко:** Цепочка превращения игрока и Alpha Wolf. Описана версия 2.x, кроме Sword of Time 1.6.

### Основные данные и ремонт

- В 1.6 предмет с этим точным ID не найден.

**2.8.8 / 2.8.14** — определение `Swords_B/items/wolf_sword.json`.
- урон: `5`; максимальная прочность: `{"max_durability":2800}`; зачарование: не указан; перезарядка: не указан; левая рука: `false`; размер стопки: `1`; свечение: `false`; предмет исчезает: не указан.
- Ремонт (буквальные материалы и значения repair_amount): `["effect:wolf_sword"]` → `2800`.
- Оружейные хуки: нанесение урона существу → `{"event":"weapon"}`.
- Скорости добычи и события digger: `{"use_efficiency":true,"destroy_speeds":[{"block":"minecraft:web","speed":15},{"block":"minecraft:bamboo","speed":10}]}`.

### Рецепты и пути получения

При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.

**Архив 2.8.14:**

- Рецептов с этим точным результатом локально не найдено. Это не исключает других путей.

- Определение: `Swords_B/items/wolf_sword.json`.
- Результаты рецептов: буквально не найдены в локальных файлах recipes.
- Прямые записи loot:
  - Буквально не найдены в локальных таблицах.
- Сделки локальных таблиц (поле `gives`):
  - Не обнаружено.
- В структурах (поля `Name`):
  - `Swords_B/structures/armor stands swords.mcstructure` $.entities[31].Mainhand[0].Name
  - `Swords_B/structures/wolf_sword.mcstructure` $.entities[0].Item.Name

Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.

### Способности, условия и вероятности по файлам

**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):

#### Wolf Sword (`effect:wolf_sword`)

[Сквозная цепь Silver → Alpha Wolf → Wolf Sword](manual-silver-wolf-path.md#wolf-sword-и-конкурирующие-контроллеры).

[Условия трёх контроллеров, графика и возможные пересечения family](manual-wolf-conditions-2.8.md).

- `items/wolf_sword.json`: damage 5, durability 2800, ремонт self 2800, max stack 1/offhand false; `minecraft:enchantable` отсутствует. Web 15/bamboo 10, on_hurt_entity — расход 1. Источник получения и условная ветвь 10/100 описаны в разделе Alpha Wolf; `structures/wolf_sword.mcstructure` содержит создаваемую сущность/предмет, см. реестр структур.
- `player.json:67–94,971–994,1283–1360`: hand sensor добавляет family `[player,wolf_sword]` и команды очистки nausea/blindness; группы превращения отдельно. `wolf_transformation` даёт family `[player,wolf_sword,wolf_transformation]`, сенсор вызывает nausea 5 с amplifier 0; при завершении добавляется `complete_wolf_transformation`: family `[wolf,wolf_sword,complete_wolf_transformation,monster]` (в списке **нет player**), `minecraft:attack` damage 15, looping random timer 3…6 секунд на звук рычания; отдельная группа движения value 0.18. Условие `has_damage != void` запускает звук, `deals_damage:true`. Нельзя уверенно заявлять, что урон меча равен 5+15: 15 — значение компонента attack игрока, а способ сложения с предметом зависит от движка.
- `animation_controllers/wolf_sword.json`: переход к start events: предмет в main_hand, moon_phase 0, time_of_day от 0.77 до 0.78 включительно; следующий переход на `wolf_transformation` — предмет, phase 0 и `time_of_day <= 0.20 || time_of_day >= 0.80`. В третьем контроллере условие остановки буквально `item == wolf_sword || item != wolf_sword && moon_phase == 0 && time_of_day == 0.20`, без скобок вокруг обеих частей. При обычном приоритете `&&` выше `||` первая часть срабатывает уже при наличии меча независимо от времени; взаимодействие трёх контроллеров, порядок и семантику Molang обязательно испытать, прежде чем обещать непрерывное превращение на всю ночь. Событие stop удаляет три группы и добавляет базовую группу wolf sword, также посылает `stopsound @a` на два звука (глобальный побочный эффект). Отдельный stop при снятии может задавать nausea/blindness 9999 с amplifier 0 в ветви complete transformation — это не эквивалент обычного сброса.

**Дополнительный подробный разбор** (источник: `docs/manual-wolf-conditions-2.8.md`):

### Wolf Sword 2.x: условия контроллеров, клиент и пересечения family

Статический разбор обеих версий: `wolf_sword.json`, клиентский `player.entity.json` и выбранные файлы Slime/Living Flame побайтово одинаковы; **серверный** `entities/player.json` различается между версиями, однако рассмотренные здесь wolf-группы, события и сенсоры в нём структурно совпадают. [Воспроизводимая таблица примерных значений условий](wolf-condition-samples-2.8.md) предполагает обычный приоритет `&&` выше `||` и точные десятичные сравнения: это **не** исполнение Molang и не симуляция смены состояний. Реальные численные значения, порядок трёх контроллеров, компонентов и сенсоров, действия событий и совместимость с новой версией нужно проверять.

#### Три независимых условия, а не один таймер

В `player.json` в `scripts.animate` включены `wolf_sword_0`, `_1`, `_2`; aliases ведут к трём отдельным контроллерам. Каждый имеет два состояния и безусловный возврат `1.0`. Переходы, ведущие к on_entry:

| Контроллер | Условие в исходнике кратко | Event на входе в целевое состояние |
|---|---|---|
| `wolf_sword` | main-hand имя `wolf_sword`, phase 0, `0.77 ≤ time ≤ 0.78` | `wolf_sword_start_events` |
| `start_wolf_sword` | main-hand имя `wolf_sword`, phase 0, `time ≤ 0.20` **или** `time ≥ 0.80` | `wolf_transformation` |
| `end_wolf_sword` | `W || !W && phase == 0 && time == 0.20` без дополнительных скобок, где W — запрос имени main hand равен `wolf_sword` | `stop_wolf_transformation` |

При обычном приоритете && выше || третье выражение равно `W || (!W && phase == 0 && time == 0.20)`: когда W истинно, его условие также истинно при **любых** значениях phase/time. Если W ложно, оно истинно только при одновременных phase 0 и **точном** 0.20. Фактическую достижимость такого точного значения и семантику Molang нельзя принять на веру.

Отсюда в простой модели: на 0.77/0.78 первое и третье условия одновременно истинны; на 0.80 и 0.20 — второе и третье; на 0.79 только третье. Если меча в main hand нет, при phase 0 и точно 0.20 условие третьего тоже истинно. Это **не** значит, что оба события обязательно выполнятся одновременно: переход зависит от текущего состояния каждого контроллера, а частота, порядок и приоритет не проверены. При обычном прочтении полей `stop_wolf_transformation` также не проверяет наличие меча или family перед командами и добавлением группы `minecraft:wolf_sword`; соперничающий hand-sensor может вызывать другое stop-событие.

В behavior-сенсоре используется `has_equipment`, `domain:hand`, ID `effect:wolf_sword`; в контроллерах и клиенте — `query.get_equipped_item_name('main_hand') == 'wolf_sword'`. Не считать их условия автоматически идентичными для offhand, пространства имён, переименования и другой версии запроса; предмет записывает `allow_off_hand:false`, но разрешение исключительных ситуаций всё равно проверяется движком.

#### Что делают события и группы

- `wolf_sword_start_events`, если self family != `wolf_transformation`, добавляет `wolf_transformation` и вызывает функцию, которая содержит `tellraw @s` с текстом `§fFor some reason you feel nauseous...`. Sensor family `wolf_transformation` направляет в `starting_wolf_transformation`, где `effect @s nausea 5 0 true`.
- `wolf_transformation` при family != `complete_wolf_transformation` посылает fizz, два воя, три частицы и добавляет группу `complete_wolf_transformation`; отдельный следующий sequence-шаг при family `wolf_transformation` удаляет группу `wolf_transformation`. Изменение family между шагами и порядок обработки нуждаются в игровом тесте.
- `complete_wolf_transformation`: `type_family` **буквально** `[wolf,wolf_sword,complete_wolf_transformation,monster]`, без слова `player`; `attack.damage:15`, looping random timer `[3,6]` на одноэлементный randomize рычания, damage sensor при `has_damage != void` с `deals_damage:true` и bark-событием. Это не доказывает сложение 15 с item damage 5, а наличие одного weight 1 не устанавливает частоту рычания.
- Sensor по family `complete_wolf_transformation` запускает `wolf_movement`, который добавляет группу `movement.value:0.18`. Конфликты с базовым движением и другие одновременно активные группы не разрешаются автоматически в памятке.
- `stop_wolf_transformation` без filters в первом sequence-шаге задаёт nausea 0, blindness 0 и два `stopsound @a`; следующий шаг удаляет три группы превращения и добавляет `minecraft:wolf_sword`. Это не та же функция, что `stop_wolf_sword_event`, который вызывается из hand-sensor при `has_equipment != effect:wolf_sword`. Последний при family `wolf_sword` удаляет три группы и задаёт nausea 0, а при family `complete_wolf_transformation` отдельной ветвью снимает complete и задаёт nausea/blindness **9999, amplifier 0**. Как добавление `default_player` и изменение family влияет на применимость следующего шага, не установлено.

#### Клиент не является подтверждением серверной способности

Клиентский `player.entity.json` вычисляет `variable.wolf_transformation` в третьем лице и `variable.wolf_vision` в первом: обе проверки используют W, phase 0 и `time ≤ 0.20 || time ≥ 0.80`, дополнительно различая `variable.is_first_person`. Эти условия не проверяют серверную family `complete_wolf_transformation` и не включают окно подготовки 0.77…0.78. Таким образом, клиентское условие графики и серверное событие могут логически расходиться; реальный выбор рендера, загрузка assets и синхронизация тоже нуждаются в проверке.

#### Возможное пересечение с другими мечами

[Условная межигровая матрица family и type](manual-family-cross-effects-2.8.md).

Базовый player и `minecraft:default_player` объявляют family `[player,default_player]`, в то время как группа complete выше записывает `[wolf,...,monster]`. Как движок разрешает конкурирующие `minecraft:type_family`, необходимо измерить; **не** считать исчезновение `player` или присутствие `monster` гарантированным состоянием.

Если действующая family действительно содержит `monster`, `entity:mountable_slime` в `slime_events` выполняет `execute @e[r=1,family=monster] ~~~ summon entity:slime_damage`: потенциальная цель может включать другого превращённого игрока. Его снаряд имеет impact damage 1; попадание от одного summon не доказано. Группа passive Living Flame выбирает цели family `monster` в max_dist 16 — это ещё одна потенциальная реакция на игрока.

Если действующая family не содержит `player`, удержание Fire Sword другим игроком вызывает `execute @e[family=!player,type=!item,r=3] ~ ~ ~ summon entity:fire` и потенциально включает такого игрока в выборку. Это условие **family**, не `type=!player`; реальное действие entity:fire и успешность команды не установлены. Эти сценарии важны в мультиплеере, но являются гипотезами на основе объявленных групп, не установленными эффектами.

### Что написано на скриншотах

На изображении вручную считаны: damage = `5`; durability = `2800`; enchantable = `false`; repairable = `true`. Оригинал: [скриншот 120007](https://drive.google.com/file/d/18xMWPEmEQ3k8DUxotbJS2CD1IIXMbY6s/view).

Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.

## Приложение А. Общие различия версий и риски

### Отличия 2.8.8: природная генерация, торговля и лёд

Это ручное статическое чтение отличающихся файлов; подробное содержимое и ссылки — в [реестре 2.8.8](world-ledger-2.8.8.md), [структурах](structures-2.8.8.md) и [построчном сравнении](version-lines-2.8.8-to-2.8.14.md). Архивы названы по именам файлов, не по проверенной версии манифеста. Доступность, регистрация и итог генерации не подтверждены запуском.

#### Silver ore и quartz-diamond ore

Только 2.8.8 содержит по два файла `features/*_ore.json` и `feature_rules/*_ore_feature.json`; в 2.8.14 эти четыре пути отсутствуют, хотя определения самих блоков и добычи есть в обоих. Буквальные исходные параметры:

| Поле | Silver | Quartz-diamond |
|---|---|---|
| Feature ID | `effect99:silver_ore` | `effect99:quartz_diamond_ore` |
| Structure name | `mystructure:silver_ore` | `mystructure:quartz_diamond_ore` |
| Биом, `any_of` | тег `overworld` | теги `overworld` или `the_end` |
| placement_pass | `underground_pass` | `underground_pass` |
| iterations | 5 | 5 |
| x, z | uniform, extent `[0,16]` | uniform, extent `[0,16]` |
| y | gaussian, extent `[10,35]` | gaussian, extent `[0,16]` |
| scatter_chance | numerator 160, denominator 200 | numerator 160, denominator 200 |
| adjustment_radius / facing | 1 / random | 1 / random |
| block_intersection allowlist | `minecraft:stone` | `minecraft:stone`, `minecraft:end_stone` |

В 2.8.8 оба соответствующих файла `Swords_B/structures/{silver_ore,quartz_diamond_ore}.mcstructure` содержат структуру 1×1×1 с одним блоком соответствующего `effect99:*_ore`, пустым states, без сущностей; второй слой индексов содержит −1. В 2.8.14 silver-структура остаётся, но quartz-структура отсутствует. Сопоставление файлов с `mystructure:` зависит от правил разрешения имён структуры в движке и пространстве мира; одно наличие файла не доказывает действительное размещение. 160/200 — записанная дробь scatter_chance, **не** безусловный шанс руды на блок, чанк или мир: влияют iterations, биомы, разрешение структуры, ограничения и обработка распределений.

#### Emerald Sword: два объявления торговли только в 2.8.8

- `Swords_B/trading/economy_trades/weapon_smith_trades.json`: tier `total_exp_required:310`, группа `num_to_select:1` содержит сделку: хочет 32 `minecraft:emerald_block`, price_multiplier 0, выдаёт один `effect:emerald_sword` с функцией `enchant_with_levels` (`treasure:false`, уровни min 5/max 60), trader_exp 0, max_uses 2, reward_exp true.
- `Swords_B/trading/weapon_smith_trades.json`: tier с индексом 2 содержит сделку: хочет `minecraft:emerald_block` quantity min 24/max 32, выдаёт `effect:emerald_sword` с той же функцией уровней 5…60; quantity результата явно не указан. Другие сделки tier содержат алмазные инструменты и изумруды. Точный список, группы и все остальные настройки — в реестре мира.
- Ни один из этих двух файлов не содержится в 2.8.14. Это не доказывает, какую из таблиц выберет движок, что торговец зарегистрирует сделку или что меч гарантированно появится. Обе версии также содержат отдельные loot-записи меча, которые нельзя сводить к торговле.

#### `effect99:fake_ice` и Ice Sword

Только 2.8.8 содержит `Swords_B/blocks/fake_ice.json`, где свойства `fake_ice:model` могут принимать 1, 2, 3, 4. Для 1, 2, 3 существуют отдельные permutations с `minecraft:ticking` `looping:false`, range `[2,2]`, события `set_model2`, `set_model3`, `set_model4` соответственно; события присваивают строковые выражения `"2"`, `"3"`, `"4"`. При модели 4 ticking `looping:true`, `[2,2]`, event `destroy_block` выполняет `setblock ~ ~ ~ air 0 destroy`. Геометрии `geometry.fake_ice`, `fake_ice2`, `fake_ice3`, `fake_ice4`; базово destroy_time 9999, explosion_resistance 10, loot `loot_tables/empty.json`. Настоящая длительность смены состояний, исходный property после команды fill, поведение destroy и замена ранее существовавшей воды не доказаны — проверить загрузку блока и мир в соответствующем движке.

В 2.8.14 те же участки команд `items/ice_sword.json` и `entities/player.json` используют `frosted_ice` вместо `effect99:fake_ice`, а файл блока fake_ice отсутствует. Это не доказательство идентичного таяния: даже если команды выполняются, меняется тип блока и логика его последующей обработки.

##### Точное побайтовое ограничение различия Ice

Сопоставлены все 42 item ID этих двух архивов: у **41** соответствующие behavior-item JSON совпадают побайтово; единственный отличающийся — `Swords_B/items/ice_sword.json`. В нём замена всех **40** буквальных вхождений `effect99:fake_ice` на `frosted_ice` в копии данных **в памяти** делает файл побайтово равным версии 2.8.14. Аналогично в `Swords_B/entities/player.json` замена всех **11** вхождений даёт побайтовое совпадение. Это не исправление файлов и не утверждение, что блоки функционально эквивалентны; это точное описание различия именно этих двух файлов. Остальные отличия архивов — в [полном побайтовом сравнении](version-diff.md). Даже идентичные item JSON могут вести себя иначе из-за сущностей, ресурсов, генерации или внешнего контекста.

### Общая архитектура и сбросы 1.6

#### Общая архитектура игрока

[Подробный разбор изменения мира пятью helper и их командных контекстов](manual-world-helpers-1.6.md).

Подробная проверка пересекающихся сенсоров, глобального счётчика и очистки мира: [общие состояния 1.6](manual-global-state-1.6.md).

`Sword_B/entities/player.json` содержит environment sensor с проверками `has_equipment` в `domain:hand` для мечей. Одноимённое событие добавляет группу, которая для многих мечей использует `minecraft:spawn_entity` с min/max wait 0, num_to_spawn 1, single_use true и собственным `entity:*`. Часть вспомогательных сущностей запускает animation controller с командами. Это принципиально иная цепь, чем группа и команды непосредственно в игроке архива 2.8.14; совпадающий ID не является доказательством совпадающего поведения.

`player.json` также запускает `controller.animation.normal`, который попеременно переходит между default и normal с условием `1.0`, и при входе в оба состояния вызывает `function normalft`. `functions/normalft.mcfunction` создаёт objective `swords dummy`, вычитает 1 у всех игроков со score 1 или 2 и выполняет `function normal` от каждого игрока со score 0. `functions/normal.mcfunction` задаёт `gamerule commandblockoutput false`, `sendcommandfeedback false`, `randomtickspeed 1`, удаляет несколько scoreboard objectives, телепортирует некоторые вспомогательные сущности и восстанавливает barrier в объёмах вокруг игрока в **stone**, также заменяет `light_block 15` на air вокруг `@p`. Это глобальные gamerule/scoreboard и потенциально разрушительное восстановление блоков, а не просто сброс визуального состояния. Не следует предполагать конкретную частоту входов или успешность команд без проверки движка, прав и координат контекста.

### Пересечения разных эффектов

### Семейства и пересечение эффектов между игроками 2.x

Это **условная модель текстовых селекторов**, не имитация Bedrock. В обеих 2.x версиях `minecraft:player` базово объявляет family `[player,default_player]`. Из **35** его component groups, которые сами содержат `minecraft:type_family`, ровно две не перечисляют `player`: `minecraft:ghost_sword` и `complete_wolf_transformation`. Это подсчёт объявлений, а не доказательство, что базовая family исчезает при добавлении группы или что одновременно возможны все состояния. Остальные 33 группы с type_family слово `player` содержат. [Группы 2.x](player-groups-2.8.14.md) · [Ghost](manual-ghost-nether-ultra.md#ghost-sword) · [Wolf](manual-wolf-conditions-2.8.md).

#### Почему `family` и `type` нельзя отождествлять

| Кандидат | Type/ID сущности в объявлении | Family в выбранной группе/базе | Где объявлено |
|---|---|---|---|
| Обычный игрок | `minecraft:player` | `[player,default_player]` | базовые components player |
| Игрок с Ghost-группой | `minecraft:player` | `[ghost_sword]` | `minecraft:ghost_sword` |
| Игрок с полной Wolf-группой | `minecraft:player` | `[wolf,wolf_sword,complete_wolf_transformation,monster]` | `complete_wolf_transformation` |
| Щит Shulker | `entity:shulker_shield`, runtime shulker | `[effect99_entities,player,shulker_sword]` | база shield |
| Ездовой слизень в defense | `entity:mountable_slime`, runtime slime | `[effect99_entities,tamed_slime,player]` | `defense_mode_slime` |

Игроки остаются **идентификатором сущности** `minecraft:player` в объявлении, а две пользовательские сущности не становятся игроками только из-за слова `player` в family. Фактическое совпадение `type` с runtime identifier, правила объединения семей и состояние одновременных групп необходимо проверять на движке. Следующая таблица использует исключительно гипотезу, что перечисленная family является действующей и что `type=player` выбирает объявленный тип игрока, а не family.

#### Таблица потенциальных совпадений

Столбцы не учитывают расстояние, измерение, доступность команд, столкновение и другие фильтры. «Да» означает лишь, что **показанный текстовый предикат** совпадает при этих допущениях; не что эффект сработал.

| Предикат | Обычный player | Ghost player | Wolf player | Shulker shield | Слизень defense |
|---|---:|---:|---:|---:|---:|
| `family=!player` | нет | да | да | нет | нет |
| `type=!player` | нет | нет | нет | да | да |
| `family=monster` | нет | нет | да | нет | нет |
| `family=!shulker_sword` | да | да | да | нет | да |
| `family=default_player` | да | нет | нет | нет | нет |

Эти столбцы особенно чувствительны к тому, заменяет ли группа базовое семейство или объединяется с ним. Например, при сохранённой базовой family `player` предикат `family=!player` для Ghost/Wolf не будет совпадать; условную строку выше нельзя выдавать за факт в игре.

#### Где эти различия реально записаны

1. При удержании Fire Sword `player.json` содержит `execute @e[family=!player,type=!item,r=3] ~ ~ ~ summon entity:fire`. При только family из таблицы Ghost и Wolf потенциально проходят family-исключение, щит и defense-слизень — нет. `type=!item`, радиус и исполнение также важны; `summon` не равен доказанному урону.
2. У Cactus Sword событие `damage @e[r=1.4,type=!player] 1 contact entity @s` исключает по **type**, а затем отдельно выполняет `damage @s 1 contact`. Clock/Time выбирают `effect @e[type=!player] ...`, а не `family=!player`. Если тип разрешается по указанным ID, player с любой family по-прежнему не совпадает с первым селектором, а пользовательский shield или slime потенциально совпадают. Защита самих сущностей и другие условия здесь не рассмотрены.
3. В событии defense-слизня `execute @e[r=1,family=monster] ~~~ summon entity:slime_damage` может выбрать игрока, если у него действительно активна содержащая monster Wolf-family. Пчела-меч и passive Living Flame в своих `nearest_attackable_target` тоже смотрят family monster, но также имеют собственные условия, дальность и AI. Сам summon снаряда не доказывает попадания.
4. On-use Shulker Sword задаёт `effect @e[r=6,family=!shulker_sword] levitation 1 18 false`: в исходном предикате **нет** исключения `type=player` или `family=player`. Щит с указанной family исключён, обычный игрок и Ghost/Wolf потенциально попадают. Это не утверждение, что два защитных компонента совместимы или levitation реально подействует.
5. Clock/Time посылают movement-event `@a[family=default_player]`. Даже если `@a` по-прежнему выбирает игроков, добавочный family-фильтр не совпадает с моделируемыми только Ghost/Wolf-группами. При иной семантике объединения семей результат может быть другим.

Защитный trigger пчелы проверяет `other` family player, а не ID владельца; условная Wolf-family может одновременно подойти фильтру monster и не подойти защите от других player-family. Применимость зависит от активных компонентов, `other`, AI и порядка обработки. Все такие пункты — риски при будущей проверке, не требования менять исходное поведение.

#### Предел статической модели

Таблица не перечисляет все взаимодействия семей в архиве; также не предполагается, что записи всегда выполняются. Она сопоставляет точные объявленные family и выбранные оригинальные selector. Внешние компоненты, другие пакеты, положение сущностей, интерпретация type/runtime и порядок add/remove групп остаются за пределами статического результата.

### Отмеченные расхождения со скриншотами

### Визуальная сверка скриншотов и выбранных противоречий

Проверены глазами 20 изображений описаний ниже; SHA-256 каждого совпал с индексом [OCR](screenshot-ocr.md). Обрезанные края и неоднозначный текст не восстанавливались догадками. Таблица содержит **выбранные** визуально прочитанные фразы, а не полную выверенную транскрипцию всех строк. Версия описания неизвестна; это заявления страницы, не подтверждение работоспособности Minecraft. Изображения, повторно загруженные для проверки, удалены из рабочего дерева; оригиналы доступны по ссылкам.

| Время имени файла (2026-11-04) | Скриншот и SHA-256 | Некоторые видимые утверждения |
|---|---|---|
| `115821` | [Screenshot_20261104_115821_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg](https://drive.google.com/file/d/18mrcZhBh-Z3MbkF1Su19Yu7C9HNa31zs/view)<br>`861130e986c13e923f7b527cf103cf06041de16da2c5e046252bdf57014ba680` | Bee: 2% при укусе; Ice: радиус 8 и −6 прочности. |
| `115826` | [Screenshot_20261104_115826_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg](https://drive.google.com/file/d/18SAkmYz1M8hva9FAv8bJfFTWOM7OD8F6/view)<br>`46e9b004ce9c488cfb7b3f11e0467a610abecd6bf48eac75113e3bf4b396df8b` | Nether Star: 0.01% взрыв; Blaze: прочность 2300, damage 6. |
| `115830` | [Screenshot_20261104_115830_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg](https://drive.google.com/file/d/1u4b1golY1UN59CFF3zifu2aqiLwI5ypW/view)<br>`7fce6af28feb396380a97390658201e0ca8aa3a085997c50ed0e954664d69757` | Blaze: 0.5% от снежного голема; Slime King: ночь в болоте, 4%. |
| `115837` | [Screenshot_20261104_115837_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg](https://drive.google.com/file/d/1eO2vurHVipmTvKj_7XzYz3KWOhZA23ic/view)<br>`e932260379d64d3d608e97e842dc43d9cb015d388937a8085befc80fa4322648` | Clock: 1000 ticks и пять секунд; показан шаблон `#GG/GCG/IG#` и `#` как nothing. |
| `115842` | [Screenshot_20261104_115842_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg](https://drive.google.com/file/d/117ulXVShaEZGyc0CdADa5mQUYlmAveAT/view)<br>`965e147c912cd70eb635b384ce13bafda24117a4139c0e9378fae80792dc1a5b` | Ender: 2.5% с красного эндермена, cooldown 2; начало Coal. |
| `115849` | [Screenshot_20261104_115849_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg](https://drive.google.com/file/d/1YEOBZ0aW8jOnH1Uw26aexwJX-C9nx5Jq/view)<br>`956058ad8fec154d3db0d14a74760e65f55eb12b40cadc343aa8a6953d99a1d4` | Shulker: 10% снаряд, 4.5% получение; Jungle: четыре сердца. |
| `115853` | [Screenshot_20261104_115853_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg](https://drive.google.com/file/d/1g4UIpjMFNG1uYe8hAo8IOzVw5ctqxL-i/view)<br>`280e8eead0f845630b4a4d9c17b4160c94d404ce8c7045c50c81742a5753b640` | Jungle: рыбалка в джунглях; Spectral: `Enchantable: false`. |
| `115858` | [Screenshot_20261104_115858_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg](https://drive.google.com/file/d/1fvRODDZrL5CDlRdyvi4iuqupiY0pkRmc/view)<br>`28ff0fd8851724cd07d8c566002ddc62d5ea195c8c4ec7b4dd3fda1ea0e103d2` | Spectral: 2% кристалл, 6% гаст; Lapis: 5 XP за 2.5–6 секунд. |
| `115902` | [Screenshot_20261104_115902_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg](https://drive.google.com/file/d/1bdPcV4MdHpWMaTX-HNVZZEjPZ7XbuusZ/view)<br>`8e956ba98048aab45569bd8db2381a782ff89c08933166df3d5ade5eb2d463b0` | Obsidian: бросить Fire Sword под дождь; веса износа 55/30/15. |
| `115910` | [Screenshot_20261104_115910_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg](https://drive.google.com/file/d/1rCL9RKVJCIfjHme7CkmOEe82NpJyCn1A/view)<br>`bfad50183376d689803f34462bf58767c5352cbb854e596f9e3815a0e18ec992` | Time: `Enchantable: false`, 90/6/3/1 износ; источник желаний 2.5%. |
| `115915` | [Screenshot_20261104_115915_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg](https://drive.google.com/file/d/1PepsprtsCCeeGxcvjyUMemLzYdbtQMM6/view)<br>`05bb7221dcb0530a112ce09e9484b8bcf16c1637531105e5bbe3c653f72a46d4` | Fire: вода → Obsidian, дождь → crystal; текст о добыче обрезан снизу. |
| `115920` | [Screenshot_20261104_115920_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg](https://drive.google.com/file/d/1ym1j2BhOsqJPPwqRzdPf0JUlIqYyPK4s/view)<br>`b4fc314ffaf43ca59a8b7654629cd57d6986e15c94aeedd59de86c7f39987506` | Продолжение описания Living Flame: 4.9%; Magma и Wither. |
| `115934` | [Screenshot_20261104_115934_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg](https://drive.google.com/file/d/12oKa5cnYV5yDSpreB54Pfe2KaqOx8FaK/view)<br>`55e5192b79c94fc2cdc3f45244352e3e47d166e9896e0cfa7a9a2223a84e7d40` | Wither: 13%; TNT: восемь секунд; Lightning: 41 разряд. |
| `115955` | [Screenshot_20261104_115955_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg](https://drive.google.com/file/d/1a7kOeS7_zMxTw7QFgoCGLAlh_f1O3_vp/view)<br>`ce6b729c673dcee51f3b322c423fbf6093c0ef3f5da26f1ea3d15099fc030736` | Sponge: `Enchantable: true`; Bone: 0.7% в пустыне ночью. |
| `120003` | [Screenshot_20261104_120003_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg](https://drive.google.com/file/d/1tAeJ-EbPeExgoe9AX_AR_p9cgZEangmO/view)<br>`d12991058469166352421a765a7b6691e0aa70fb1917470557423de2402edc5a` | Quartz: урон 600; Bedrock: infinite durability как утверждение страницы. |
| `120007` | [Screenshot_20261104_120007_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg](https://drive.google.com/file/d/18xMWPEmEQ3k8DUxotbJS2CD1IIXMbY6s/view)<br>`a10d3085eb39ebb721f15069e451201dcb99f6d87332c22e22944dcaadbd74da` | Glass: `Repairable: false`, вода → Glass; серебро ниже 15. |
| `120011` | [Screenshot_20261104_120011_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg](https://drive.google.com/file/d/1tY_bT4l7lOkdHRfKqglYbqXP2_FiM70D/view)<br>`ff6d6f365932585b08b1e12746e9c8974902d0d97d87dd5e9167f879a7d7170d` | Wolf: полнолуние и 10%; Ghost: damage −666 и заявленная неуязвимость. |
| `120025` | [Screenshot_20261104_120025_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg](https://drive.google.com/file/d/1vSQHbdMLZTGGVBVDzBWT7r_Vm9oyZznG/view)<br>`51ce1e01e844247ddd28e3787bfe7a377b3bc56c53cfaada1b5f27fd9c6f5e33` | Ghost: 0.3% меч, 1% телепорт; начало Ultra Instinct. |
| `120034` | [Screenshot_20261104_120034_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg](https://drive.google.com/file/d/14nhZwfS8-jwjz2vOlAQQd2-LXzlnE2l4/view)<br>`8c9b1137236e447294ccf6de71520be361e0dcd4c148225aa586ce9036151703` | Фонтан: 0.8%/2.5%; кварцевая руда ниже 15 и ниже 16, серебро ниже 35. |
| `120050` | [Screenshot_20261104_120050_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg](https://drive.google.com/file/d/1QxBp8CUoeiK1tSXeUCHVwz48f_9-dqGc/view)<br>`95a181d431de78e8c220c38067fba128d601ba9412b890a4584f4b307458d8f4` | `/function give` «all the swords» и указания экспериментальных переключателей. |

#### Важные сопоставления

- **Противоречие внутри описаний Fire:** на `115915` сказано «вода → obsidian, дождь → crystal», на `115902` — дождь → Obsidian, на `120007` — вода → Glass. В исходном `Swords_B/entities/item.json` 2.x water вызывает загрузку `glass_sword`, дождь без воды после таймера `[5,6]` — `obsidian_sword`; NBT обеих структур проверены. Это сравнение с кодом, а не с реальным ходом игры.
- **Blaze:** на `115830` видно **0.5%** при убийстве снежным големом; `loot_tables/entities/blaze.json` объявляет `killed_by_entity` snow_golem и `random_chance_with_looting` chance **0.025**, multiplier 0.02. Также отдельно есть ветвь 5/1000 загрузки отсутствующей локально структуры. Два способа/условия не следует смешивать; итоговую частоту нужно испытать.
- **Описание зачарований/ремонта:** `115853` и `115910` заявляют `Enchantable: false` для Spectral и Time, а оба соответствующих item JSON задают `minecraft:enchantable` value 9, slot sword. `120007` заявляет Glass `Repairable: false`, хотя в item задан `minecraft:repairable` с self 1 и glass 1. `115955` заявляет Sponge `Enchantable: true`, но в этом item компонент не задан; отсутствие компонента не устанавливает движковое значение по умолчанию. Проверить на исходном движке и учесть неизвестную версию описания.
- **Глубина руд:** `120007` сообщает silver ниже 15, а `120034` — ниже 35; последнее изображение также содержит утверждения ниже 15 и ниже 16 для quartz. В 2.8.8 y extent gaussian `[10,35]` и `[0,16]` соответственно, а в 2.8.14 локальных feature/rules этих руд нет. Отображаемые числа не доказывают реальных границ генерации или регистрации структур.
- **Clock:** `115837` визуально содержит `1000 ticks` и ключ `I` для gold ingot (OCR ошибочно прочитал как `10o0` и `|`). В JSON event за один вызов указан `time add 10` под фильтром группы skill; итог за пять секунд зависит от частоты вызовов и работы таймера. На картинке пустая клетка обозначена `#`, а JSON рецепта использует `X` без соответствующего key — нельзя считать этот символ автоматически пустым.
- **Пути и вероятности:** `115853` относит рыбалку Jungle Sword к джунглям, но обычный и jungle fishing в исходнике ссылаются на общую treasure-таблицу с мечом; регистрация и семантика рыбалки не проверены. `120050` заявляет, что `/function give` выдаёт все мечи, но в 2.x функция не перечисляет Bee, Cursed Pumpkin и Wet Sponge, см. [проверку функции](manual-acquisition-issues.md#команда-function-give-неполный-набор-в-2x).
- **Скриншот браузера** `132138` разобран отдельно в [проверке совместимости](manual-acquisition-issues.md#скриншот-браузера-и-совместимость). Он не подтверждает совместимость старых компонентов с Bedrock 26.62.

## Приложение Б. Распознанный текст всех 21 скриншотов

Ниже дословно приведён сохранённый OCR. Число в начале строки — оценка распознавания, а не часть описания. Возможны неверные слова, буквы, числа и пропуски; это **не** полностью вручную выверенная транскрипция.

### Скриншоты: машинный OCR-индекс

Это автоматическое распознавание, **не проверенная транскрипция**. Возможны пропуски, неверные цифры, знаки, порядок и объединение строк; низкая уверенность не выявляет всех ошибок. Сверяйте с JPEG. Текст описывает заявления автора, а не доказанную реализацию; версия страницы не установлена. Интерфейс и перекрытые части могут попасть в вывод. Хэши позволяют идентифицировать оригиналы из пользовательской папки Google Диска.

#### Screenshot_20261104_115821_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg

SHA-256: `861130e986c13e923f7b527cf103cf06041de16da2c5e046252bdf57014ba680`

```text
0.850  11:58 vPN *
0.648  ×
0.982  A packof39swordswithspecial powers.
0.965  ·Bee Stinger (Bee Sword)
0.988  -Durability: 1080
0.952  -Damage: 5
0.975  -Enchantable: true
0.989  -Repairable: true (bee sword, honeycomb, honey block)
0.980  -Special skills:
0.992  When attacking the enemies you will release from
0.949  time to time small aggressive bees thatwill defendyou.
1.000  -Description:
0.986  Flowers will appear from time to time, when you walk
0.998  through grass.
0.983  -How to create or get it:
0.994  When a bee stings you, it will drop its stinger with a
0.973  2% percent chance.
0.922  ·lce Sword
0.996  -Durability: 500
0.987  -Damage: 8.5
0.977  -Enchantable: true
0.992  -Repairable: true (For ice and the same sword.)
0.999  -Special skills:
0.972  The ice that is placed when using this sword will
0.997  disappear after approximately 8 seconds
0.988  All the water under your feet will turn to ice.
0.986  Sometimesyouwill throwsnowballs attheentitiesyou
0.999  attack.
0.984  Right-clicking or pressing the screen will cause entities
0.966  within a radius of 8 to be encased in blocks of ice. (Sword
0.991  durability: -6)
1.000  -Description:
0.979  If the player is on fire the sword will turn into water.
0.989  -How to create or get it:
0.985  In the chests of: Igloos and Villages in the snow.
1.000  27
0.991  Install (McAddon)
```

#### Screenshot_20261104_115826_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg

SHA-256: `46e9b004ce9c488cfb7b3f11e0467a610abecd6bf48eac75113e3bf4b396df8b`

```text
0.829  11:58 vPN *
0.535  ×
0.959  ·Nether Star Sword
0.993  -Durability: 3256
0.980  -Damage: 7 (12= Her damage was reduced to 7 as
0.986  her new power makes her too powerful in this Add-On
0.999  update.)
0.987  -Explodable: false
0.991  -Should Despawn Item: false
0.978  -Enchantable: true
0.993  -Repairable: true (With a nether star and the same
0.996  sword.)
0.990  -Special skills:
0.969  The stars of the nether will fall from the sky when you
0.993  are attacking an entity, these stars will deal 6 damage
1.000  per hit.
1.000  -Description:
0.980  When using it to kill the Wither you may get the
0.999  Wither sword.
0.990  When thrown into the fire it explodes violently, this
0.985  explosion is capable of breaking bedrock.
0.974  This sword is slightly unstable and can explode with a
0.990  0.01% chance when attacking entities.
0.982  -How to create or get it:
0.985  Crafting her with a diamond sword and a nether star.
0.956  ·Blaze Sword
0.986  -Durability: 2300
0.995  -Damage: 6
0.978  -Enchantable: true
0.983  -Repairable: true (Only with the same sword.)
0.983  -Special skills:
0.994  By right-clicking or pressing the screen, your body will
0.972  levitate for a few seconds and then launch several small
0.993  fireballs in the direction you are looking.
0.948  The fire won't hurt you.
0.981  Sometimes you will throw fireballs when hitting
0.999  entities.
1.000  27
0.991  Install (McAddon)
```

#### Screenshot_20261104_115830_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg

SHA-256: `7fce6af28feb396380a97390658201e0ca8aa3a085997c50ed0e954664d69757`

```text
0.829  11:58 vPN *
0.535  ×
0.988  Small fireballs will not be able to approach you within
0.975  a radius of 7.
1.000  -Description:
0.996  Blaze rods will surround you around your body.
0.944  Your body will turn somewhat orange.
0.994  -How to create or get it:
0.981  Asnowgolemmustkillablazethiswillrelease itwith
1.000  0.5%
0.931  · Slime Sword
0.992  -Durability: 675
0.995  -Damage: 6
0.991  -Enchantable: true
0.983  -Repairable: true (With slime and with the same sword.)
0.987  -Special skills:
0.981  By having the sword in hand you will get a baby slime
1.000  mount.
0.978  If you get off the slime mount, the slime will defend
0.998  you from all nearby monsters. (The slime deals one point
0.963  of damage and is immortal, plus it will teleport to its
0.971  ownerwhenitgetstoofar away.)
0.956  Jumping with the slime mount and falling on an entity
0.956  will damage it. (Jumping with the slime mount can be
0.999  tricky.)
0.972  -How to create or get it:
0.993  Killing the slime king that appears at night in the
0.999  swampbiomewitha4%chance.
0.943  ·Sea Sword
0.973  -Durability: 1356
0.963  -Damage: 7
0.981  -Enchantable: true
0.985  -Repairable: true (By heart of the sea and the same
0.998  sword.)
0.993  -Special skills:
0.995  You can swim as fast as dolphins.
1.000  27
0.993  Install (McAddon)
```

#### Screenshot_20261104_115837_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg

SHA-256: `e932260379d64d3d608e97e842dc43d9cb015d388937a8085befc80fa4322648`

```text
0.825  11:58 vPN*
0.798  X
0.998  You will become a mermaid.
0.986  You can breathe underwater but you cannot breathe air.
1.000  -Description:
0.983  You will jump like a fish when you are out of the water.
0.981  -How to create or get it:
0.999  In treasure chests.
0.959  ·Clock Sword
0.989  -Durability: 4800
0.994  -Damage: 7
0.986  -Enchantable: true
0.998  -Repairable: true (= Creation materials.)
0.971  -Special skills:
0.997  Right-clicking or pressing the screen will advance one
0.965  hour (10o0 ticks) into the game. (The game will go 10
0.982  times faster for 5 seconds)
0.998  -How to create or get it:
1.000  "pattern":
0.990  "#GG"
0.998  "GCG"
0.865  "IG#"
0.977  "G": "item": "minecraft:gold_block"
0.996  "C": "item": "minecraft:clock"
0.956  "|": "item": "minecraft:gold_ingot"
0.992  "#": "item": "nothing"
0.972  · Spider Sword
0.977  -Durability: 628
0.955  -Damage: 5
0.995  -Enchantable: true
0.997  -Repairable: true (With cobwebs, spider eyes and the
1.000  same sword.)
0.976  -Special skills:
0.995  Thespidermountwillbeabletoclimbwalls.
0.978  You will throw cobwebs when attacking entities with a
1.000  27
0.993  Install (McAddon)
```

#### Screenshot_20261104_115842_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg

SHA-256: `965e147c912cd70eb635b384ce13bafda24117a4139c0e9378fae80792dc1a5b`

```text
0.825  11:58 vPN*
0.572  n限69
0.998  5% chance.
0.983  Holding the sword in your hand you will get a spider
1.000  mount.
0.976  Right-clicking or pressing the screen will fire cobweb
0.988  projectiles for a few seconds. (Sword durability: -8)
0.949  -How to create or get it:
0.957  In the chests of the abandoned mineshaft
0.972  ·Ender Sword
0.996  -Durability: 1256
0.996  -Damage: 9
0.995  -Enchantable: true
0.984  -Repairable: true (By ender pearl, ender eye or the same
0.999  sword.)
0.985  -Special skills:
0.990  You will not take damage from any projectile and will
0.973  randomly teleportwithinaradius of 16whenyou are
0.979  attacked with one.
0.987  When they attack you, you will randomly teleport in a
0.992  radius of 16 with a 50% chance.
0.977  The water will cause you damage and you will teleport
0.999  randomly.
0.998  By right clicking or pressing the screen, you will
0.967  randomly teleport in a radius of between 16 to 32
0.982  blocks. (Sword durability: -5)
0.985  "minecraft:cooldown": {"category": "ender_sword",
0.991  "duration": 2 = seconds}
0.990  -How to create or get it:
0.994  By killing the red-eyed enderman with a 2.5% chance,
0.992  this enderman only appears in the overworld (normal
0.977  world) with a low probability.
0.973  ·Coal Sword
0.997  -Durability: 121
0.966  -Damage: 4
1.000  27
0.990  Install (McAddon)
```

#### Screenshot_20261104_115849_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg

SHA-256: `956058ad8fec154d3db0d14a74760e65f55eb12b40cadc343aa8a6953d99a1d4`

```text
0.858  11:58vPN*
0.524  ×
0.999  -Enchantable: true
0.991  -Repairable: true (With coal, sticks and the same
0.998  sword.)
0.973  -Special skills: None (It only serves as fuel for the
1.000  furnace.)
0.984  -How to create or get it:
0.972  Two blocks of coal and a stick.
0.926  · Shulker sword
0.967  -Durability: 2609
0.978  -Damage: 6
0.992  -Enchantable: true
0.999  -Repairable: true (Only with the same sword.)
0.997  -Special skills:
0.972  Throw shulker projectiles with a 10% chance when
0.999  attacking entities.
0.988  Right-clicking or pressing the screen will levitate
0.975  entities within a radius of 6. (Sword durability: -8)
0.969  You will be immune to the effect of levitation.
0.964  When you duck you will get a shulker shell, which will
0.998  protect you from enemy attacks but if they destroy the
0.982  shell with you inside you will die too.
0.982  -How to create or get it:
0.954  When killing shulkers with a 4.5% chance
0.955  · Jungle Sword
0.988  -Durability: 128
0.975  -Damage: 4
0.975  -Enchantable: true
0.999  -Repairable: true (Only with the same sword.)
0.998  -Special skills:
0.976  Your health will be reduced to 4 hearts, but an
0.978  absorption potion effect will be added.
0.997  Vines will be placed in nearby blocks. (Blocks: logs,
0.997  grass, dirt, sand, cobblestone, stone, obsidian, endstone,
0.993  gravel, ice, planks, leaves, netherrack, and nether bricks.)
1.000  27
0.991  Install (McAddon)
```

#### Screenshot_20261104_115853_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg

SHA-256: `280e8eead0f845630b4a4d9c17b4160c94d404ce8c7045c50c81742a5753b640`

```text
0.835  11:58 vPN *
0.633  X
0.966  -How to create or get it:
0.982  Fishing in the jungle biome or jungle temple.
0.944  ·Cactus Sword
0.997  -Durability: 125
0.985  -Damage: 6
0.994  -Enchantable: true
0.993  -Repairable: true (Only with the same sword.)
0.978  -Special skills:
0.970  You will receive damage when having the sword in
0.972  hand, but you will also damage very close entities.
0.999  -How to create or get it:
0.999  Astickandtwocacti
0.986  ·Emerald Sword
0.998  -Durability:2300
0.956  -Damage: 7
0.998  -Enchantable: true
0.998  -Repairable: true (Only with the same sword.)
0.981  -Special skills:
0.985  You'll get a village hero potion effect for being inside a
0.984  village and it will give villagers a resistance effect within
0.999  64 radius.
0.998  -How to create or get it:
0.994  Found in the chests of: Stronghold, Woodland Mansion,
0.996  and Pillager Outpost.
0.955  · Spectral Sword
0.996  -Durability: 3256
0.990  -Damage: 9
0.995  -Explodable: false
0.991  -Should Despawn Item: false
0.998  -Enchantable:false
0.995  -Repairable: true (By ender crystal, nether star and by
0.999  the same sword.)
0.969  -Special skills:
1.000  27
0.997  Install (McAddon)
```

#### Screenshot_20261104_115858_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg

SHA-256: `28ff0fd8851724cd07d8c566002ddc62d5ea195c8c4ec7b4dd3fda1ea0e103d2`

```text
0.850  11:58 vPN *
0.659  ×
0.959  It will make the main block of each dimension
0.974  transparent only in that dimension. (Overworld: stone,
0.999  Nether: netherrack, End: endstone.)
0.994  Fire an explosive projectile. (Sword durability: -15)
1.000  -Description:
0.978  This sword is somewhat unstable so it may explode
0.998  when attacking entities with a 1% chance.
0.963  This sword will emit a slight light.
1.000  everywhere.
0.982  -How to create or get it:
0.993  When exploding ender crystals in the Nether with a
0.950  2% chance.
0.993  Kill a Ghast with his own projectile with a 6% chance.
0.936  · Lapis Sword
0.997  -Durability: 528
0.995  -Damage: 5
0.972  -Enchantable: true
0.990  -Repairable: true (With lapis lazuli and the same sword.)
0.978  -Special skills:
0.992  You will be given 5 experience points in a random
0.987  period of between 2.5 and 6 seconds.
0.991  -How to create or get it:
0.987  Found in the chests of: Stronghold and Pillager
1.000  Outpost.
0.969  ·Grass Sword
0.974  -Durability: 250
0.991  -Damage: 8
0.994  -Enchantable: true
0.998  -Repairable: true (Only with the same sword.)
0.979  -Special skills:
0.971  All nearby entities within a radius of 8 will be attacked
0.988  by a strange grass entity that will bury them a bit
0.974  underground or completely depending on the size of the
1.000  27
0.997  Install (McAddon)
```

#### Screenshot_20261104_115902_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg

SHA-256: `8e956ba98048aab45569bd8db2381a782ff89c08933166df3d5ade5eb2d463b0`

```text
0.891  11:59 vPN *
0.572  niL
0.671  X
1.000  entity.
0.985  The dirt blocks will turn into grass.
0.972  -How to create or get it:
0.985  You will have to kill a grass witch, these appear at
0.967  nightwitha lowprobability andwilldrop theswordwith
0.997  a 20% probability.
0.964  (This witch will have the same abilities that the grass
0.995  sword grants you.)
0.945  · Obsidian Sword
0.995  -Durability: 3000
0.979  -Damage: 8
0.996  -Explodable: false
0.995  -Enchantable: true
0.996  -Repairable: true (By obsidian and the same sword.)
0.999  -Special skills:
0.978  You will be immune to explosions and you will have
0.989  knockback resistance.
1.000  -Description:
0.989  When attacking, the durability points of the sword
0.981  could lose 1 point with a probability of 55%, 2 points
0.989  withaprobabilityof30%and3pointswithaprobability
0.991  of 15%.
0.970  -How to create or get it:
0.960  You must throw the fire sword into the rain and wait a
0.976  few seconds.
0.963  ·GlowstoneSword
0.999  -Durability: 128
0.988  -Damage: 4
0.996  -Enchantable: true
0.995  -Repairable: true (By glowstone, glowstone dust and the
0.985  same sword.)
0.976  -Special skills:
0.976  This sword emits a lot of light and can be placed in the
0.994  left hand.
1.000  27
0.990  Install (McAddon)
```

#### Screenshot_20261104_115910_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg

SHA-256: `bfad50183376d689803f34462bf58767c5352cbb854e596f9e3815a0e18ec992`

```text
0.893  11:59 vPN *
0.535  ×
0.976  -How to create or get it:
0.971  Two glowstone blocks and a blaze rod
0.942  ·Time Sword
0.993  -Durability: 13770
0.995  -Damage: 13
0.995  -Enchantable: false
0.992  -Repairable: false
0.999  -Special skills:
0.979  Time will advance faster, you and all entities will be
0.986  able to move much faster, and the plants will grow much
1.000  faster.
1.000  -Description:
0.991  When attacking, the durability points of the sword
0.983  could lose 1 point with a probability of 90%, 16 points
0.941  with a probability of 6%,32 points with a probability of
0.957  3% and 64 points with a probability of 1%.
0.999  This sword emits light.
0.956  -How to create or get it:
0.942  You must throw clock swords into the water of the source
0.976  structure that is in the desert, this source will serve as
0.959  a source of wishes and will give you the sword with a
1.000  2.5% probability.
0.967  · Creeper Sword
0.998  -Durability: 1500
0.962  -Damage: 6
0.991  -Explodable: false
0.998  -Enchantable: true
0.983  -Repairable: true (For gunpowder and the same sword.)
0.997  -Special skills:
0.992  When attacking, it will launch small Creepers with a
0.985  20% chance that will explode in a few seconds with a
0.998  small explosion.
0.994  By right-clicking or pressing the screen, the player will
0.969  inflate like a Creeper and then the player will explode
1.000  27
0.992  Install (McAddon)
```

#### Screenshot_20261104_115915_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg

SHA-256: `05bb7221dcb0530a112ce09e9484b8bcf16c1637531105e5bbe3c653f72a46d4`

```text
0.870  11:59 vPN *
0.820   69
0.502  niL
0.716  ×
0.969  and die!(Sworddurability:-1)
0.981  -How to create or get it:
0.974  You will have to explode a Creeper loaded with a
0.993  lighter and it will drop the sword with a 5% probability.
0.970  ·Fire Sword
0.971  -Durability: 2000
0.988  -Damage: 6 (lt will burn the enemies you attack.)
0.984  -Enchantable: true
0.988  -Repairable: true (By fire blocks(rare) and the same
0.999  sword)
0.998  -Special skills:
0.970  You will be immune to fire.
0.965  When you attack you will launch living flames with a
0.967  15% probability, these entities will attack the monsters
0.972  and theywill die after a fewseconds.
0.992  By right clicking or pressing the screen, you will
0.946  activate the ability"rain of fire"this will create a shower
0.965  of fireballs that will set fire all around.(Sword durability:
0.998  -20)
0.977  Entities very close to you will burn.
0.968  The ice and snow will melt.
1.000  -Description:
0.991  It disappears if you enter the water.
0.983  This sword emits light.
0.995  By throwing the fire sword into the water it turns into
0.980  an obsidiansword.
0.952  Throwing the fire sword into the rain will cause it to
0.984  turn into a crystal sword after a few seconds.
0.998  -How to create or get it:
0.991  You must kill living flames, these appear in the Nether
0.985  and some of them will attack you, to kill this entity
0.954  correctly without the fire sword falling into the fire and
0.960  vanishing,you will have toplace blockssuchasslabs,
0.985  pressure plates or other types of I do not complete this to
0.987  prevent the entity from setting fire. The entity will drop
0.999  27
0.993  Install (McAddon)
```

#### Screenshot_20261104_115920_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg

SHA-256: `b4fc314ffaf43ca59a8b7654629cd57d6986e15c94aeedd59de86c7f39987506`

```text
0.891  11:59 vPN *
0.671  X
0.956  the sword with a 4.9% chance. This entity will disappear
0.989  in arandomperiodofbetween25and60seconds.
0.957  · Magma Sword
0.999  -Durability: 1316
0.997  -Damage: 7.2
0.991  -Enchantable: true
0.994  -Repairable: true (By magma blocks and the same
0.999  sword.)
0.977  -Special skills:
0.998  Magma blocks won't hurt you.
0.974  Fire will only hurt you if you are standing on it.
0.953  The lava under your feet will turn into magma blocks.
0.998  -How to create or get it:
0.993  In chests of great underwater ruins.
0.961  ·Wither Sword
0.972  -Durability: 3856
0.968  -Damage: 10
0.997  -Explodable:false
0.982  -Should Despawn Item: false
0.998  -Enchantable:false
0.988  -Repairable: true (Only with the same sword.)
0.981  -Special skills:
0.966  When attacking, it will drop wither skulls with a 10%
1.000  chance.
0.988  It will be immune to the wither effect.
0.982  The leaves of the trees will wither, the flowers will turn
0.993  into withered roses, the grass will turn to dirt.
0.972  Right clicking or pressing the screen will launch a
0.981  dangerous wither skull. (Sword durability: -3)
0.956  -Description:
0.985  This sword emits light.
0.944  By having the swordyouwill see a lifebar onyour
0.972  screen with the name "Wither Sword" this is only
1.000  decoration.
1.000  27
0.996  Install (McAddon)
```

#### Screenshot_20261104_115934_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg

SHA-256: `55e5192b79c94fc2cdc3f45244352e3e47d166e9896e0cfa7a9a2223a84e7d40`

```text
0.871  11:59 vPN *
0.535  ×
0.943  You will have the effect of wither but it will not hurt
0.999  you.
0.993  -How to create or get it:
0.971  You will have to kill the wither with a"Nether star
0.982  sword" and it will drop it with a 13% chance.
0.928  ·TNT Sword
0.991  -Durability: 64
0.993  -Damage: 4
0.987  -Enchantable: true
0.993  -Repairable: true (By tnt and the same sword.)
0.991  -Special skills:
0.996  When attacking, you will throw small explosions.
0.996  By right clicking or pressing the screen, a very powerful
0.986  tnt will appear that will explode in 8 seconds. (Sword
0.998  durability: -18)
0.999  -Description:
0.980  When thrown into the fire it will explode violently.
0.984  -How to create or get it:
0.982  In the chests of the desert temple.
0.998  Lightning sword
0.998  -Durability: 2012
0.976  -Damage: 8
0.998  -Enchantable: true
0.987  -Repairable: true (Only with the same sword.)
0.981  -Special skills:
0.988  When attacking it will throw thunder.
0.992  By right clicking or pressing the screen, 41 rays will fall
0.976  around you. (Sword durability: -9)
0.988  You will be immune to lightning damage but not fire.
1.000  -Description:
0.980  This sword emits light.
0.956  -How to create or get it:
0.968  You must kill an entity called "Centella in Spanish"or
0.982  "spherical lightning or ball lightning in English", this
1.000  27
0.990  Install (McAddon)
```

#### Screenshot_20261104_115955_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg

SHA-256: `ce6b729c673dcee51f3b322c423fbf6093c0ef3f5da26f1ea3d15099fc030736`

```text
0.893  11:59 vPN *
0.597  niL酸 69
0.572  ×
0.990  entitywillonlyappearwitha2o%probabilitywhen
0.993  lightning strikes during a storm, this entity will not try
0.994  to harm you but if you get too close you will receive a lot
0.982  damage, also this entity has 200 life points, that is, 100
0.990  hearts, it will not be easy to kill it, you must do it before
0.992  it disappears since it only lives in a random period of
0.969  between 10 to 60 seconds. (This entity is a reference to a
0.998  strange real-life atmospheric phenomenon.)
0.958  · Sponge Sword
1.000  -Durability: 128
0.986  -Damage: 5
0.999  -Enchantable: true
0.991  -Repairable: true (By sponge and the same sword.)
0.996  -Special skills:
0.964  It will absorb water in a radius of 2 blocks, after several
0.991  seconds absorbing water the sword will transform into a
0.990  "wet sponge sword".
0.971  -How to create or get it:
0.980  On killing the elder guardian with a 6.5% chance.
0.987  When putting the wet sponge sword in the oven.
0.979  ·SkeletonboneSword
0.999  -Durability: 820
0.994  -Damage: 5
0.996  -Enchantable: true
0.990  -Repairable: true (Everything that is made of: bone.)
0.984  -Special skills:
0.976  When attacking you will throw arrows with a 20%
1.000  chance.
0.981  Crops will grow much faster within a 2 block radius.
0.998  Enemyarrowswithin8radiuswillslowdown.
0.985  -How to create or get it:
0.999  Killing skeletons at night in the desert biome with a
0.971  0.7% chance.
0.999  27
0.989  Install (McAddon)
```

#### Screenshot_20261104_120003_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg

SHA-256: `d12991058469166352421a765a7b6691e0aa70fb1917470557423de2402edc5a`

```text
0.981  69
0.937  12:00 vPN 
0.782  ni
0.535  ×
0.960  ·Quartz Diamond Sword
0.953  -Durability: 1
0.999  -Damage: 600
0.990  -Enchantable: false
0.974  -Repairable: false
0.995  -Special skills: None
1.000  -Description:
0.950  Putting the sword in your hand will cause you a lot of
0.961  damage for a moment and taking it out of your hand will
0.999  too.
0.989  The sword causes so much damage that when you
0.993  attack an enemy you will die too. (everything has a price)
0.968  -How to create or get it:
0.954  With two quartz diamond blocks and a quartz diamond
0.980  stick that is created with the same material.
0.990  (You should look for quartz diamond ores below height
0.989  15 in small quantities. (they are rare to find))
0.969  ·Bedrock Sword
0.979  -Durability: (Infinite)
0.956  -Damage: 18
0.993  -Explodable: false
0.982  -Should Despawn Item: false
0.998  -Enchantable: false
0.973  -Special skills: none
0.995  -Description: It works as an extremely powerful pickaxe.
0.969  -How to create or get it:
0.976  It is created with two bedrock blocks and a bedrock
0.995  stick that is created with the same material.
0.984  (Bedrock can only be obtained by using the Ultra
0.984  Instinct sword projectile or by throwing the Nether Star
0.970  Sword into fire, which will cause a loud explosion that
0.996  will shatter the bedrock.)
0.977  ·WitherSkeletonSword
0.999  -Durability: 128
1.000  27
0.993  Install (McAddon)
```

#### Screenshot_20261104_120007_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg

SHA-256: `a10d3085eb39ebb721f15069e451201dcb99f6d87332c22e22944dcaadbd74da`

```text
0.917  12:00 vPN 
0.671  X
0.973  -Damage: 4
0.988  -Enchantable: true
0.991  -Repairable: true (Coal, sticks and the same sword)
0.981  -Special skills:
0.963  Will give wither effect to the entitiesyou attack
0.977  -How to create or get it:
0.963  Whenkillingwither skeletonswith a 2.5%chance
0.986  ·Glass Sword
1.000  -Durability: 1
0.984  -Damage: 33
0.999  -Enchantable: true
0.977  -Repairable: false
0.985  -Special skills: none
0.989  -How to create or get it:
0.978  You will have to throw the fire sword into the water.
0.953  · Silver Sword
0.990  -Durability: 1800
0.981  -Damage: 6
0.995  -Enchantable: true
0.990  -Repairable: true (Only with the same sword.)
0.992  -Special skills:
0.985  Causes more damage than normal to "alpha wolves"
0.962  -How to create or get it:
0.949  You must find the silver ore in the depths of the
0.977  overworld (normal world) below height 15 and place it in
0.946  the oven to obtain the silver ingot and be able to create
1.000  the sword.
0.943  · Wolf Sword
0.993  -Durability: 2800
0.994  -Damage: 5 (+15 points during the night of the full
0.983  moon. (They will not be visible in the sword damage))
0.997  -Enchantable: false
0.986  -Repairable: true (Only with the same sword.)
1.000  27
0.991  Install (McAddon)
```

#### Screenshot_20261104_120011_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg

SHA-256: `ff6d6f365932585b08b1e12746e9c8974902d0d97d87dd5e9167f879a7d7170d`

```text
0.937  12:00 vPN 
0.539  ×
0.988  -Special skills:
0.996  -During the night of the full moon:
0.992  The player will deal 15 points of damage per attack
0.979  plus 5 points of sword attack for a total of 20.
0.972  The player will move faster.
0.978  The monsters will not attack you, you will be part of
1.000  them.
1.000  -Description:
0.952  -During the night of the full moon:
0.964  Your vision will look somewhat red
0.952  If you remove the sword from your hand before the
0.989  end of the full moon night you will get negative potion
0.988  effects. (They will disappear at dawn.)
0.990  If you have the sword in your hand during the sunset
0.989  before the night of the full moon, you will feel dizzy.
0.996  -How to create or get it:
0.998  You must kill an alpha wolf during the full moon with
0.995  the silver sword and it will drop the sword with a 10%
0.999  chance.
0.997  (Alpha wolves appear in the taiga biome during the
0.993  night of the full moon, you will hear a distant howl when
0.993  one appears nearby.)
0.965  · Ghost Sword
0.997  -Durability:3333
0.997  -Damage: -666 (Being a negative number you cannot
0.986  harm any entity)
0.999  -Explodable:false
0.973  -Should Despawn Item: false
0.995  -Enchantable: false
0.997  -Repairable: false
0.998  -Special skills:
0.989  By holding the sword in hand, the player's legs will
0.965  disappear and the player will turn into a ghost.
0.987  Nothing can harm the player, not fire, not lava, not
0.998  explosions, basically nothing.
0.999  27
0.996  Install (McAddon)
```

#### Screenshot_20261104_120025_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg

SHA-256: `51ce1e01e844247ddd28e3787bfe7a377b3bc56c53cfaada1b5f27fd9c6f5e33`

```text
0.868  12:00 vPN 水
0.539  ×
0.993  By right-clicking or pressing the screen the player will
0.989  be able to teleport to any direction they are looking.
0.997  (Sword durability: -6)
0.981  By getting very close to the walls, the player will be
0.997  abletoseenearbycavesandwillbeabletoteleportto
0.952  any cave they are looking at.
0.972  By crouching,theplayerwilllevitate,he canbasically
0.995  fly.
0.961  You can move faster than normal.
0.984  The monsters will not attack you, now you are one of
1.000  them.
1.000  -Description:
0.976  The player's vision will look somewhat white.
0.996  The player will not be able to attack any entity.
0.948  -How to create or get it:
0.963  At night ghosts will appear, these entities are not
0.988  dangerous, they will not try to attack you and you will
0.960  notbeableto attack themeither,but ifyou touch them
0.975  as if you were trying to harm them, the entity will drop
0.955  theswordwith a probability of 0.3%soitcouldtakeyou
0.992  a while to get it. It will also be 1% likely that the entity
0.983  will teleport randomly so it could escape you. This entity
0.985  is also sensitive to light, so if it gets too close to the light
0.967  it will disappear. This entity only appears in blocks of
0.963  grass or stone.
0.951  ·UltraInstinctSword
0.996  -Durability: 9999
0.964  -Damage: 16
0.995  -Explodable:false
0.970  -Should Despawn Item: false
0.990  -Enchantable: false
0.989  -Repairable: false
0.997  -Special skills:
0.994  Melee attack, projectiles, fire, and explosions cannot
0.981  harm you. (You can dodge the melee attack and the
1.000  27
0.988  Install (McAddon)
```

#### Screenshot_20261104_120034_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg

SHA-256: `8c9b1137236e447294ccf6de71520be361e0dcd4c148225aa586ce9036151703`

```text
0.868  12:00 vPN 水
0.829   69
0.572  ×
0.991  projectiles automatically)
0.975  Right clicking or pressing the screen will fire a
0.988  powerful projectile capable of destroying everything in
0.977  its path and the bedrock will not be a problem. (This
0.991  ability recharges every 61 seconds) (Sword durability:
0.984  -48) (The Ultra Instinct projectile can cause a lot of lag
0.999  for a few seconds.)
0.978  -How to create or get it:
0.998  You must throw quartz diamonds or quartz diamond
0.990  blocks (new material) into the water of the source
0.956  structure that is in the desert, this source will serve as
0.960  a source of wishes and will give you the sword with a
0.999  0.8% probability when throwing quartz diamond or 2.5%
0.977  chance with the quartz diamond block.
0.973  (Quartz diamond ores arespawnedbelowheight15in
0.944  small quantities and are rare to find)
0.988  ·Wet Sponge Sword
0.995  -Durability: 64
1.000  -Damage:3
0.981  -Enchantable: false
0.991  -Repairable: true (Sponges and more sponges.)
0.992  -Special skills: none
0.999  -How to create or get it:
0.984  When wetting the sponge sword.
0.988  · New materials, ores and more:
0.987  -Quartz diamond ore { Spawns below height 16 (Rare)
0.975  (will deal damage when sting if you're too close) }
0.969  -Quartz diamond
0.973  -Quartz stick{Durability:20,Damage: 24,(Causes
0.969  you damage when you attack entities) (lt is crafted like a
0.972  common stick) }
0.984  -Silver ore { Spawns below height 35 (common) (Place
0.976  in the oven to get silver ingot) }
0.998  -Silver ingot
1.000  27
0.993  Install (McAddon)
```

#### Screenshot_20261104_120050_com_kayenworks_mcpeaddons_AddonDetailActivity.jpg

SHA-256: `95a181d431de78e8c220c38067fba128d601ba9412b890a4584f4b307458d8f4`

```text
0.977  -Bedrock stick { Durability: Unbreakable, Damage: 6 (It
0.988  is crafted like a common stick) }
0.982  Use the command "/function give" to get all the swords.
0.995  Swords can be found in the Creative Inventory under the
0.998  Swordstab.
0.975  # Report error to my Twitter @Effectoo
0.980  - Any suggestions to add in the addon are welcome as
0.985  long as you send them to me on my Twitter.
0.946  # How to install
0.994  · Download and install the behavior pack and resource
0.997  pack
0.988  · Activate both the behavior and the resource pack in
0.961  your world settings
0.986  · Activate the option "Holiday Creator Features" and
0.992  "Creation of Custom Biomes" and "Beta APls" for the
0.987  correct functioning of the Add-On.
```

#### Screenshot_20261104_132138_com_yandex_browser_YandexBrowserMainActivity.jpg

SHA-256: `b3d92dbc007a453f6bce4565d45ef864a6df5ad0fc310a79f3c0f228de588684`

```text
0.841  ЗkCnepNMeHTanbHaA ΦyHKLNA Holiday Creator
0.949  Features 6blna ynaneHa W3 Minecraft Bedrock Edition B
0.850  06HoBneHNN 1.21.20, KOTOpOe BblWno B aBryCTe 2024
0.986  rona.  minecraft.net
1.000  reddit.com
0.620  ormoenodu oih
0.840  B paMKaX 3TOrO *e o6HOBneHN9 pa3pa6oT4NKN y6paN
0.841  eKCnepNMeHTanbHbIN nepeknoyaTenb《Holiday
0.906  Creator Features》>. pИ 3ToM caMa ΦyHKLNoHanbHocTb
0.807  He ИC4e3na 6eCCeHO: B 6Onee paHHeM o6HOBneHИИ
0.857  1.19.80 ee 3aMeHNJN ByMA HOBbIMN KOMnOHeHTaMN:
0.849  - transformation — AnA ynpaBJeHИA BpaWeHNeM,
0.817  MacWTa6WpoBaHNeM W TepeMeWeHWem 6noKOB.
0.812  - bone_visibility 一 A ynpaBeHNA BИnИMocTbIO
0.721  YacTeИ MonenN.
0.774  MOCnEACTBNA
0.783  YaneHNe 3KCnepNMeHTanbHoN ΦyHKLNN npИBenO K
0.928  Creator Features, epecTanN pa6oTaTb.
0.820  Pa3pa6oT4NKaM npИWnocb ananTИpOBaTb CBOИ
0.851  npOeKTbI O HOBble KOMnOHeHTbl, YTO6bI NX annOHbl
0.823  OCTaBaJNCb COBMeCTHMbIMN C aKTyabHoИ BepCИeИ
0.931  Иrpbl.  minecraft.net 
0.997  feedback.minecraft.net
0.997  tac-onite.itch.io
0.808  EcnИ Bbl ИConb3yeTe CTapble annoHbl W OHN nepeCTaJИ
0.899  aBTOpbl CBOИ pa6oTbl nO HOBble CTaHnapTbl. B
0.899  KayeCTBe aJbTepHaTИBbl MoKHO paccMoTpeTb Custom
0.867  Components — MeXaHW3M, KOTOpbIM BO MHorOM
0.999  minecraft.net
```

## Приложение В. Точные компоненты и события предметов

Полное содержимое каждого `minecraft:item` после JSON5-разбора. Это машинная выписка, а не все косвенные файлы или доказательство выполнения.

### 01. Bedrock Stick — `effect:bedrock_stick`

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:bedrock_stick",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:should_despawn": true,
    "minecraft:max_stack_size": 1,
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:can_destroy_in_creative": true,
    "minecraft:icon": {
      "texture": "bedrock_stick"
    },
    "minecraft:display_name": {},
    "minecraft:damage": 6,
    "minecraft:weapon": {}
  },
  "events": {}
}
```

### 02. Bedrock Sword — `effect:bedrock_sword`

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:bedrock_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:should_despawn": false,
    "minecraft:max_stack_size": 1,
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "bedrock_sword"
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": {
            "tags": "q.any_tag('stone', 'metal', 'diamond_pick_diggable', 'wood', 'pumpkin', 'plant', 'dirt', 'sand', 'gravel', 'grass', 'snow')"
          },
          "speed": 999
        },
        {
          "block": "effect99:quartz_diamond_block",
          "speed": 50
        },
        {
          "block": "effect99:quartz_diamond_ore",
          "speed": 100
        },
        {
          "block": "effect99:silver_ore",
          "speed": 999
        },
        {
          "block": "minecraft:warped_wart_block",
          "speed": 999
        },
        {
          "block": "minecraft:nether_wart_block",
          "speed": 999
        },
        {
          "block": "minecraft:leaves",
          "speed": 999
        },
        {
          "block": "minecraft:leaves2",
          "speed": 999
        },
        {
          "block": "minecraft:hay_block",
          "speed": 999
        },
        {
          "block": "minecraft:soul_soil",
          "speed": 999
        },
        {
          "block": "minecraft:soul_sand",
          "speed": 999
        },
        {
          "block": "minecraft:chest",
          "speed": 999
        },
        {
          "block": "minecraft:melon_block",
          "speed": 999
        },
        {
          "block": "minecraft:bookshelf",
          "speed": 999
        },
        {
          "block": "minecraft:lectern",
          "speed": 999
        },
        {
          "block": "minecraft:pumkin",
          "speed": 999
        },
        {
          "block": "minecraft:ice",
          "speed": 999
        },
        {
          "block": "minecraft:bone_block",
          "speed": 999
        },
        {
          "block": "minecraft:mob_spawner",
          "speed": 999
        },
        {
          "block": "minecraft:anvil",
          "speed": 999
        },
        {
          "block": "minecraft:netherite_block",
          "speed": 999
        },
        {
          "block": "minecraft:sandstone",
          "speed": 999
        },
        {
          "block": "minecraft:diamond_block",
          "speed": 999
        },
        {
          "block": "minecraft:lapis_block",
          "speed": 999
        },
        {
          "block": "minecraft:emerald_block",
          "speed": 999
        },
        {
          "block": "minecraft:ancient_debris",
          "speed": 999
        },
        {
          "block": "minecraft:cracked_polished_blackstone_bricks",
          "speed": 999
        },
        {
          "block": "minecraft:nether_brick",
          "speed": 999
        },
        {
          "block": "minecraft:cracked_nether_bricks",
          "speed": 999
        },
        {
          "block": "minecraft:quartz_ore",
          "speed": 999
        },
        {
          "block": "minecraft:netherrack",
          "speed": 999
        },
        {
          "block": "minecraft:basalt",
          "speed": 999
        },
        {
          "block": "minecraft:end_bricks",
          "speed": 999
        },
        {
          "block": "minecraft:purpur_block",
          "speed": 999
        },
        {
          "block": "minecraft:purpur_stairs",
          "speed": 999
        },
        {
          "block": "minecraft:end_brick_stairs",
          "speed": 999
        },
        {
          "block": "minecraft:stone_slab2",
          "speed": 999
        },
        {
          "block": "minecraft:stone_slab3",
          "speed": 999
        },
        {
          "block": "minecraft:polished_basalt",
          "speed": 999
        },
        {
          "block": "minecraft:warped_nylium",
          "speed": 999
        },
        {
          "block": "minecraft:crimson_nylium",
          "speed": 999
        },
        {
          "block": "minecraft:end_stone",
          "speed": 999
        },
        {
          "block": "minecraft:ender_chest",
          "speed": 999
        },
        {
          "block": "minecraft:quartz_block",
          "speed": 999
        },
        {
          "block": "minecraft:quartz_stairs",
          "speed": 999
        },
        {
          "block": "minecraft:quartz_bricks",
          "speed": 999
        },
        {
          "block": "minecraft:quartz_stairs",
          "speed": 999
        },
        {
          "block": "minecraft:nether_gold_ore",
          "speed": 999
        },
        {
          "block": "minecraft:blackstone",
          "speed": 999
        },
        {
          "block": "minecraft:furnace",
          "speed": 999
        },
        {
          "block": "minecraft:blast_furnace",
          "speed": 999
        },
        {
          "block": "minecraft:lit_furnace",
          "speed": 999
        },
        {
          "block": "minecraft:blast_furnace",
          "speed": 999
        },
        {
          "block": "minecraft:chain",
          "speed": 999
        },
        {
          "block": "minecraft:lantern",
          "speed": 999
        },
        {
          "block": "minecraft:soul_lantern",
          "speed": 999
        },
        {
          "block": "minecraft:grindstone",
          "speed": 999
        },
        {
          "block": "minecraft:brewing_stand",
          "speed": 999
        },
        {
          "block": "minecraft:smooth_stone",
          "speed": 999
        },
        {
          "block": "minecraft:stonebrick",
          "speed": 999
        },
        {
          "block": "minecraft:enchanting_table",
          "speed": 999
        },
        {
          "block": "minecraft:stone_brick_stairs",
          "speed": 999
        },
        {
          "block": "minecraft:mossy_stone_brick_stairs",
          "speed": 999
        },
        {
          "block": "minecraft:polished_blackstone_bricks",
          "speed": 999
        },
        {
          "block": "minecraft:polished_blackstone_stairs",
          "speed": 999
        },
        {
          "block": "minecraft:blackstone_wall",
          "speed": 999
        },
        {
          "block": "minecraft:blackstone_wall",
          "speed": 999
        },
        {
          "block": "minecraft:polished_blackstone_wall",
          "speed": 999
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 18,
    "minecraft:weapon": {}
  },
  "events": {}
}
```

### 03. Bee Sword — `effect:bee_sword`

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:bee_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 1080
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "bee_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:bee_sword"
          ],
          "repair_amount": 1080
        },
        {
          "items": [
            "minecraft:honey_block"
          ],
          "repair_amount": 400
        },
        {
          "items": [
            "minecraft:honeycomb"
          ],
          "repair_amount": 150
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 5,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        },
        {
          "randomize": [
            {
              "weight": 30,
              "shoot": {
                "projectile": "entity:bee_sword",
                "launch_power": 1
              }
            },
            {
              "weight": 70,
              "damage": {
                "type": "durability",
                "amount": 1,
                "target": "self"
              }
            }
          ]
        }
      ]
    }
  }
}
```

### 04. Blaze Sword — `effect:blaze_sword`

**Архив 1.6:**

```json
{
  "description": {
    "identifier": "effect:blaze_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 2300
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "blaze_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:blaze_sword"
          ],
          "repair_amount": 2300
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 8
  }
}
```

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:blaze_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 2300
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "blaze_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:blaze_sword"
          ],
          "repair_amount": 2300
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:cooldown": {
      "category": "blaze_sword",
      "duration": 20
    },
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:damage": 6,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "on_use": {
      "damage": {
        "type": "durability",
        "amount": 10,
        "target": "self"
      },
      "run_command": {
        "command": [
          "event entity @s[family=blaze_sword] blaze_sword_skill_event",
          "effect @s levitation 7 0 true",
          "effect @s slow_falling 10 3 true"
        ]
      }
    },
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        },
        {
          "randomize": [
            {
              "weight": 14,
              "run_command": {
                "command": [
                  "effect @s fire_resistance 1 0 true"
                ]
              },
              "shoot": {
                "projectile": "minecraft:small_fireball",
                "launch_power": 1
              }
            },
            {
              "weight": 1,
              "run_command": {
                "command": [
                  "effect @s fire_resistance 1 0 true"
                ]
              },
              "shoot": {
                "projectile": "minecraft:fireball",
                "launch_power": 1
              }
            },
            {
              "weight": 85,
              "damage": {
                "type": "durability",
                "amount": 1,
                "target": "self"
              }
            }
          ]
        }
      ]
    }
  }
}
```

### 05. Bone Sword — `effect:bone_sword`

**Архив 1.6:**

```json
{
  "description": {
    "identifier": "effect:bone_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 820
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "bone_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:bone_sword"
          ],
          "repair_amount": 820
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 7
  }
}
```

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:bone_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 820
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "bone_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:bone_sword"
          ],
          "repair_amount": 820
        },
        {
          "items": [
            "minecraft:bone"
          ],
          "repair_amount": 70
        },
        {
          "items": [
            "minecraft:bone_block"
          ],
          "repair_amount": 300
        },
        {
          "items": [
            "minecraft:bone_meal"
          ],
          "repair_amount": 18
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 5,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        },
        {
          "randomize": [
            {
              "weight": 20,
              "shoot": {
                "projectile": "minecraft:arrow",
                "launch_power": 1
              }
            },
            {
              "weight": 80,
              "damage": {
                "type": "durability",
                "amount": 1,
                "target": "self"
              }
            }
          ]
        }
      ]
    }
  }
}
```

### 06. Cactus Sword — `effect:cactus_sword`

**Архив 1.6:**

```json
{
  "description": {
    "identifier": "effect:cactus_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 125
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "cactus_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:cactus_sword"
          ],
          "repair_amount": 125
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 6
  }
}
```

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:cactus_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 125
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "cactus_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:cactus_sword"
          ],
          "repair_amount": 125
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:render_offsets": {
      "main_hand": {
        "first_person": {
          "position": [
            0.67,
            0,
            -1.24
          ]
        },
        "third_person": {
          "position": [
            0.36,
            1.5,
            -0.66
          ]
        }
      }
    },
    "minecraft:display_name": {},
    "minecraft:damage": 6,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    }
  }
}
```

### 07. Clock Sword — `effect:clock_sword`

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:clock_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": true,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 4800
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "clock_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:clock_sword"
          ],
          "repair_amount": 4800
        },
        {
          "items": [
            "minecraft:clock"
          ],
          "repair_amount": 900
        },
        {
          "items": [
            "minecraft:gold_block"
          ],
          "repair_amount": 780
        },
        {
          "items": [
            "minecraft:gold_ingot"
          ],
          "repair_amount": 87
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:cooldown": {
      "category": "clock_sword",
      "duration": 30
    },
    "minecraft:display_name": {},
    "minecraft:damage": 7,
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    },
    "on_use": {
      "damage": {
        "type": "durability",
        "amount": 10,
        "target": "self"
      },
      "run_command": {
        "command": [
          "event entity @s[family=clock_sword] clock_sword_skill_event"
        ]
      }
    }
  }
}
```

### 08. Coal Sword — `effect:coal_sword`

**Архив 1.6:**

```json
{
  "description": {
    "identifier": "effect:coal_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 121
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "coal_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:coal_sword"
          ],
          "repair_amount": 121
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 6
  }
}
```

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:coal_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 121
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "coal_sword"
    },
    "minecraft:fuel": {
      "duration": 360.0
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:coal_sword"
          ],
          "repair_amount": 121
        },
        {
          "items": [
            "minecraft:coal"
          ],
          "repair_amount": 58
        },
        {
          "items": [
            "minecraft:stick"
          ],
          "repair_amount": 2
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 4,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    }
  }
}
```

### 09. Creeper Sword — `effect:creeper_sword`

**Архив 1.6:**

```json
{
  "description": {
    "identifier": "effect:creeper_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 1500
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "creeper_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:creeper_sword"
          ],
          "repair_amount": 1500
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 8
  }
}
```

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:creeper_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 1500
    },
    "minecraft:cooldown": {
      "category": "creeper_sword",
      "duration": 3
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "creeper_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:creeper_sword"
          ],
          "repair_amount": 1500
        },
        {
          "items": [
            "minecraft:gunpowder"
          ],
          "repair_amount": 256
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 6,
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "on_use": {
      "sequence": [
        {
          "run_command": {
            "command": [
              "event entity @s start_player_explode_event"
            ],
            "target": "holder"
          }
        },
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    },
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        },
        {
          "randomize": [
            {
              "weight": 20,
              "shoot": {
                "projectile": "minecraft:creeper",
                "launch_power": 1
              }
            },
            {
              "weight": 80,
              "damage": {
                "type": "durability",
                "amount": 1,
                "target": "self"
              }
            }
          ]
        }
      ]
    }
  }
}
```

### 10. Cursed Pumpkin Sword — `effect:cursed_pumpkin_sword`

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:cursed_pumpkin_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 606
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "cursed_pumpkin_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:cursed_pumpkin_sword"
          ],
          "repair_amount": 606
        },
        {
          "items": [
            "minecraft:honey_block"
          ],
          "repair_amount": 400
        },
        {
          "items": [
            "minecraft:honeycomb"
          ],
          "repair_amount": 150
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 5,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        },
        {
          "randomize": [
            {
              "weight": 80,
              "shoot": {
                "projectile": "entity:pumpkin_projectile",
                "launch_power": 1
              }
            },
            {
              "weight": 20
            }
          ]
        }
      ]
    }
  }
}
```

### 11. Emerald Sword — `effect:emerald_sword`

**Архив 1.6:**

```json
{
  "description": {
    "identifier": "effect:emerald_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 2300
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "emerald_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:emerald_sword"
          ],
          "repair_amount": 2300
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 7
  }
}
```

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:emerald_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 2300
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "emerald_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:emerald_sword"
          ],
          "repair_amount": 2300
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 7,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    }
  }
}
```

### 12. Ender Sword — `effect:ender_sword`

**Архив 1.6:**

```json
{
  "description": {
    "identifier": "effect:ender_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": true,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 1256
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "ender_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:ender_sword"
          ],
          "repair_amount": 1256
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 9
  }
}
```

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:ender_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": true,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 1256
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "ender_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:ender_sword"
          ],
          "repair_amount": 1256
        },
        {
          "items": [
            "minecraft:ender_pearl"
          ],
          "repair_amount": 28
        },
        {
          "items": [
            "minecraft:ender_eye"
          ],
          "repair_amount": 32
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:render_offsets": {
      "main_hand": {
        "first_person": {
          "position": [
            1,
            0.4,
            -3
          ],
          "scale": [
            0.04,
            0.04,
            0.04
          ]
        },
        "third_person": {
          "position": [
            0.5,
            1.6,
            -0.8
          ],
          "scale": [
            0.038,
            0.038,
            0.038
          ]
        }
      }
    },
    "minecraft:display_name": {},
    "minecraft:damage": 9,
    "minecraft:cooldown": {
      "category": "ender_sword",
      "duration": 2
    },
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "on_use": {
      "run_command": {
        "command": [
          "spreadplayers ~ ~ 16 32 @s",
          "playsound mob.endermen.portal @a[r=34]"
        ]
      },
      "damage": {
        "type": "durability",
        "amount": 5,
        "target": "self"
      }
    },
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    }
  }
}
```

### 13. Fire Sword — `effect:fire_sword`

**Архив 1.6:**

```json
{
  "description": {
    "identifier": "effect:fire_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 2000
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "fire_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:fire_sword"
          ],
          "repair_amount": 2000
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 12
  }
}
```

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:fire_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": true,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 2000
    },
    "minecraft:cooldown": {
      "category": "fire_sword",
      "duration": 25
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "fire_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:fire_sword"
          ],
          "repair_amount": 2000
        },
        {
          "items": [
            "minecraft:fire"
          ],
          "repair_amount": 1000
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 6,
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "on_use": {
      "sequence": [
        {
          "run_command": {
            "command": [
              "summon entity:living_flame ~ ~14 ~ minecraft:target",
              "summon entity:living_flame ~ ~4 ~ fire_sword_skill",
              "summon entity:living_flame ~3 ~4 ~ fire_sword_skill",
              "summon entity:living_flame ~ ~4 ~3 fire_sword_skill",
              "summon entity:living_flame ~-3 ~4 ~ fire_sword_skill",
              "summon entity:living_flame ~ ~4 ~-3 fire_sword_skill",
              "particle minecraft:example_linearcurve ~ ~0.2 ~",
              "title @s actionbar §l§6Fire rain"
            ],
            "target": "holder"
          }
        },
        {
          "damage": {
            "type": "durability",
            "amount": 20,
            "target": "self"
          }
        }
      ]
    },
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        },
        {
          "randomize": [
            {
              "weight": 85,
              "shoot": {
                "projectile": "entity:fire",
                "launch_power": 1
              }
            },
            {
              "weight": 15,
              "shoot": {
                "projectile": "entity:living_flame",
                "launch_power": 1
              }
            }
          ]
        }
      ]
    }
  }
}
```

### 14. Ghost Sword — `effect:ghost_sword`

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:ghost_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": true,
    "minecraft:should_despawn": false,
    "minecraft:max_stack_size": 1,
    "minecraft:durability": {
      "max_durability": 3333
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "ghost_sword"
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:render_offsets": {
      "main_hand": {
        "first_person": {
          "position": [
            0.67,
            0,
            -1.24
          ]
        },
        "third_person": {
          "position": [
            0.36,
            1.5,
            -0.66
          ]
        }
      }
    },
    "minecraft:cooldown": {
      "category": "ghost_sword",
      "duration": 2
    },
    "minecraft:display_name": {},
    "minecraft:damage": -666,
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "on_use": {
      "shoot": {
        "projectile": "entity:ghost_projectile",
        "launch_power": 1
      },
      "damage": {
        "type": "durability",
        "amount": 6,
        "target": "self"
      }
    },
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    }
  }
}
```

### 15. Glass Sword — `effect:glass_sword`

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:glass_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 1
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "glass_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:glass_sword"
          ],
          "repair_amount": 1
        },
        {
          "items": [
            "minecraft:glass"
          ],
          "repair_amount": 1
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 25,
          "on_dig": {
            "event": "weapon"
          }
        },
        {
          "block": "minecraft:bamboo",
          "speed": 15,
          "on_dig": {
            "event": "weapon"
          }
        }
      ],
      "on_dig": {
        "event": "weapon"
      }
    },
    "minecraft:display_name": {},
    "minecraft:damage": 33,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 10,
            "target": "self"
          },
          "run_command": {
            "command": [
              "playsound random.glass @a[r=8,m=0]"
            ]
          }
        }
      ]
    }
  }
}
```

### 16. Glowstone Sword — `effect:glowstone_sword`

**Архив 1.6:**

```json
{
  "description": {
    "identifier": "effect:glowstone_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": true,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 128
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "glowstone_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:glowstone_sword"
          ],
          "repair_amount": 128
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 6
  }
}
```

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:glowstone_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": true,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 128
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "glowstone_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:glowstone_sword"
          ],
          "repair_amount": 128
        },
        {
          "items": [
            "minecraft:glowstone"
          ],
          "repair_amount": 64
        },
        {
          "items": [
            "minecraft:glowstone_dust"
          ],
          "repair_amount": 16
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 4,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    }
  }
}
```

### 17. Grass Sword — `effect:grass_sword`

**Архив 1.6:**

```json
{
  "description": {
    "identifier": "effect:grass_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 250
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "grass_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:grass_sword"
          ],
          "repair_amount": 250
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 8
  }
}
```

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:grass_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 250
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "grass_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:grass_sword"
          ],
          "repair_amount": 250
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:render_offsets": {
      "main_hand": {
        "first_person": {
          "position": [
            0.8,
            0.15,
            -1.74
          ]
        },
        "third_person": {
          "position": [
            0.69,
            2.5,
            -0.96
          ]
        }
      }
    },
    "minecraft:display_name": {},
    "minecraft:damage": 8,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    }
  }
}
```

### 18. Ice Sword — `effect:ice_sword`

**Архив 1.6:**

```json
{
  "description": {
    "identifier": "effect:ice_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 500
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "ice_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:ice_sword"
          ],
          "repair_amount": 500
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 11
  }
}
```

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:ice_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": true,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 500
    },
    "minecraft:cooldown": {
      "category": "ice_sword",
      "duration": 5
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "ice_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:ice_sword"
          ],
          "repair_amount": 500
        },
        {
          "items": [
            "minecraft:ice"
          ],
          "repair_amount": 55
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 8.5,
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "on_use": {
      "sequence": [
        {
          "run_command": {
            "command": [
              "execute @e[type=!enderman,type=!horse,type=!slime,type=!silverfish,type=!spider,type=!cave_spider,type=!tnt,type=!vex,type=!chicken,type=!pig,type=!wolf,type=!cat,type=!item,type=!xp_orb,type=!xp_bottle,type=!egg,type=!snowball,type=!fireball,type=!small_fireball,type=!eye_of_ender_signal,type=!ender_pearl,type=!fishing_hook,type=!falling_block,type=!lightning_bolt,type=!lingering_potion,type=!dragon_fireball,type=!ender_dragon,type=!endermite,type=!arrow,type=!thrown_trident,type=!leash_knot,type=!bat,type=!rabbit,type=!parrot,type=!ghast,type=!shulker,type=!elder_guardian,type=!guardian,type=!turtle,type=!fox,type=!squid,type=!ocelot,type=!phantom,type=!area_effect_cloud,family=!fish,family=!effect99_entities,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 frosted_ice 0 replace air 0",
              "execute @e[type=enderman,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~3 ~-1 frosted_ice 0 replace air 0",
              "execute @e[family=slime_large,rm=2,r=12] ~ ~ ~ fill ~2 ~-1 ~2 ~-2 ~3 ~-2 frosted_ice 0 replace air 0",
              "execute @e[family=slime_large,rm=2,r=12] ~ ~1 ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 air 0 replace frosted_ice",
              "execute @e[family=slime_medium,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
              "execute @e[family=slime_medium,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ air 0 replace frosted_ice",
              "execute @e[family=slime_small,rm=2,r=12] ~ ~ ~ fill ~1 ~1 ~1 ~-1 ~-1 ~-1 frosted_ice 0 replace air 0",
              "execute @e[family=slime_small,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ air 0 replace frosted_ice",
              "execute @e[type=silverfish,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ frosted_ice 0 replace air 0",
              "execute @e[type=spider,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
              "execute @e[type=cave_spider,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
              "execute @e[type=tnt,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
              "execute @e[type=vex,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
              "execute @e[type=chicken,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
              "execute @e[type=pig,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
              "execute @e[type=wolf,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
              "execute @e[type=cat,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
              "execute @e[type=small_fireball,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ frosted_ice 0 replace air 0",
              "execute @e[type=fireball,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ frosted_ice 0 replace air 0",
              "execute @e[type=arrow,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ frosted_ice 0 replace air 0",
              "execute @e[type=lingering_potion,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ frosted_ice 0 replace air 0",
              "execute @e[type=dragon_fireball,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ frosted_ice 0 replace air 0",
              "execute @e[type=thrown_trident,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ frosted_ice 0 replace air 0",
              "execute @e[type=endermite,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
              "execute @e[type=rabbit,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
              "execute @e[type=parrot,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
              "execute @e[type=phantom,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
              "execute @e[type=shulker,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
              "execute @e[type=guardian,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
              "execute @e[type=ocelot,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
              "execute @e[type=turtle,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
              "execute @e[type=fox,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
              "execute @e[type=squid,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
              "execute @e[type=elder_guardian,rm=2,r=12] ~ ~ ~ fill ~2 ~-1 ~2 ~-2 ~3 ~-2 frosted_ice 0 replace air 0",
              "execute @e[type=bat,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
              "execute @e[type=ghast,rm=2,r=12] ~ ~ ~ fill ~4 ~-3 ~4 ~-4 ~4 ~-4 frosted_ice 0 replace air 0",
              "execute @e[type=ghast,rm=2,r=12] ~ ~ ~ fill ~3 ~-2 ~3 ~-3 ~3 ~-3 air 0 replace frosted_ice",
              "execute @e[type=horse,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
              "execute @e[type=horse,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ air 0 replace frosted_ice 0",
              "execute @e[type=player,rm=3,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 frosted_ice 0 replace air 0",
              "title @s actionbar §l§bIce Skill",
              "playsound random.fizz @a[r=12] ~ ~ ~ 1 2.3",
              "particle minecraft:knockback_roar_particle ~ ~1 ~"
            ],
            "target": "holder"
          }
        },
        {
          "damage": {
            "type": "durability",
            "amount": 6,
            "target": "self"
          }
        }
      ]
    },
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        },
        {
          "randomize": [
            {
              "weight": 70
            },
            {
              "weight": 30,
              "shoot": {
                "projectile": "minecraft:snowball",
                "launch_power": 1
              },
              "run_command": {
                "command": [
                  "playsound random.bow @a[r=10] ~ ~ ~ 1 0.4"
                ]
              }
            }
          ]
        }
      ]
    }
  }
}
```

**Архив 2.8.8: отдельное определение Ice из-за отличий событий:**

```json
{
  "description": {
    "identifier": "effect:ice_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": true,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 500
    },
    "minecraft:cooldown": {
      "category": "ice_sword",
      "duration": 5
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "ice_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:ice_sword"
          ],
          "repair_amount": 500
        },
        {
          "items": [
            "minecraft:ice"
          ],
          "repair_amount": 55
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 8.5,
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "on_use": {
      "sequence": [
        {
          "run_command": {
            "command": [
              "execute @e[type=!enderman,type=!horse,type=!slime,type=!silverfish,type=!spider,type=!cave_spider,type=!tnt,type=!vex,type=!chicken,type=!pig,type=!wolf,type=!cat,type=!item,type=!xp_orb,type=!xp_bottle,type=!egg,type=!snowball,type=!fireball,type=!small_fireball,type=!eye_of_ender_signal,type=!ender_pearl,type=!fishing_hook,type=!falling_block,type=!lightning_bolt,type=!lingering_potion,type=!dragon_fireball,type=!ender_dragon,type=!endermite,type=!arrow,type=!thrown_trident,type=!leash_knot,type=!bat,type=!rabbit,type=!parrot,type=!ghast,type=!shulker,type=!elder_guardian,type=!guardian,type=!turtle,type=!fox,type=!squid,type=!ocelot,type=!phantom,type=!area_effect_cloud,family=!fish,family=!effect99_entities,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=enderman,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~3 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[family=slime_large,rm=2,r=12] ~ ~ ~ fill ~2 ~-1 ~2 ~-2 ~3 ~-2 effect99:fake_ice 0 replace air 0",
              "execute @e[family=slime_large,rm=2,r=12] ~ ~1 ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 air 0 replace effect99:fake_ice",
              "execute @e[family=slime_medium,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[family=slime_medium,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ air 0 replace effect99:fake_ice",
              "execute @e[family=slime_small,rm=2,r=12] ~ ~ ~ fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[family=slime_small,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ air 0 replace effect99:fake_ice",
              "execute @e[type=silverfish,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ effect99:fake_ice 0 replace air 0",
              "execute @e[type=spider,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=cave_spider,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=tnt,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=vex,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=chicken,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=pig,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=wolf,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=cat,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=small_fireball,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ effect99:fake_ice 0 replace air 0",
              "execute @e[type=fireball,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ effect99:fake_ice 0 replace air 0",
              "execute @e[type=arrow,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ effect99:fake_ice 0 replace air 0",
              "execute @e[type=lingering_potion,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ effect99:fake_ice 0 replace air 0",
              "execute @e[type=dragon_fireball,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ effect99:fake_ice 0 replace air 0",
              "execute @e[type=thrown_trident,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ effect99:fake_ice 0 replace air 0",
              "execute @e[type=endermite,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=rabbit,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=parrot,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=phantom,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=shulker,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=guardian,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=ocelot,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=turtle,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=fox,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=squid,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=elder_guardian,rm=2,r=12] ~ ~ ~ fill ~2 ~-1 ~2 ~-2 ~3 ~-2 effect99:fake_ice 0 replace air 0",
              "execute @e[type=bat,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=ghast,rm=2,r=12] ~ ~ ~ fill ~4 ~-3 ~4 ~-4 ~4 ~-4 effect99:fake_ice 0 replace air 0",
              "execute @e[type=ghast,rm=2,r=12] ~ ~ ~ fill ~3 ~-2 ~3 ~-3 ~3 ~-3 air 0 replace effect99:fake_ice",
              "execute @e[type=horse,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=horse,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ air 0 replace effect99:fake_ice 0",
              "execute @e[type=player,rm=3,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 effect99:fake_ice 0 replace air 0",
              "title @s actionbar §l§bIce Skill",
              "playsound random.fizz @a[r=12] ~ ~ ~ 1 2.3",
              "particle minecraft:knockback_roar_particle ~ ~1 ~"
            ],
            "target": "holder"
          }
        },
        {
          "damage": {
            "type": "durability",
            "amount": 6,
            "target": "self"
          }
        }
      ]
    },
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        },
        {
          "randomize": [
            {
              "weight": 70
            },
            {
              "weight": 30,
              "shoot": {
                "projectile": "minecraft:snowball",
                "launch_power": 1
              },
              "run_command": {
                "command": [
                  "playsound random.bow @a[r=10] ~ ~ ~ 1 0.4"
                ]
              }
            }
          ]
        }
      ]
    }
  }
}
```

### 19. Jungle Sword — `effect:jungle_sword`

**Архив 1.6:**

```json
{
  "description": {
    "identifier": "effect:jungle_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 128
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "jungle_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:jungle_sword"
          ],
          "repair_amount": 128
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 4
  }
}
```

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:jungle_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 128
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:block_placer": {
      "block": "effect99:sapling3",
      "use_on": [
        "dirt",
        "grass"
      ]
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "jungle_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:jungle_sword"
          ],
          "repair_amount": 128
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 4,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    }
  }
}
```

### 20. Lapis Sword — `effect:lapis_sword`

**Архив 1.6:**

```json
{
  "description": {
    "identifier": "effect:lapis_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 528
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "lapis_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:lapis_sword"
          ],
          "repair_amount": 528
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 6
  }
}
```

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:lapis_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 528
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "lapis_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:lapis_sword"
          ],
          "repair_amount": 528
        },
        {
          "items": [
            "minecraft:lapis_lazuli"
          ],
          "repair_amount": 48
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 5,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    }
  }
}
```

### 21. Lightning Sword — `effect:lightning_sword`

**Архив 1.6:**

```json
{
  "description": {
    "identifier": "effect:lightning_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": true,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 2000
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "lightning_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:lightning_sword"
          ],
          "repair_amount": 2000
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 8
  }
}
```

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:lightning_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": true,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 2012
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "lightning_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:lightning_sword"
          ],
          "repair_amount": 2012
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:render_offsets": {
      "main_hand": {
        "first_person": {
          "position": [
            1,
            0.4,
            -3
          ],
          "scale": [
            0.04,
            0.04,
            0.04
          ]
        },
        "third_person": {
          "position": [
            0.7,
            2.2,
            -1
          ],
          "scale": [
            0.05,
            0.05,
            0.05
          ]
        }
      }
    },
    "minecraft:display_name": {},
    "minecraft:damage": 8,
    "minecraft:cooldown": {
      "category": "lightning_sword",
      "duration": 12
    },
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "on_use": {
      "run_command": {
        "command": [
          "summon lightning_bolt ~ ~2 ~ default_lightning_bolt",
          "summon lightning_bolt ~7 ~ ~ default_lightning_bolt",
          "summon lightning_bolt ~ ~ ~7 default_lightning_bolt",
          "summon lightning_bolt ~-7 ~ ~ default_lightning_bolt",
          "summon lightning_bolt ~ ~ ~-7 default_lightning_bolt",
          "summon lightning_bolt ~6 ~ ~6 default_lightning_bolt",
          "summon lightning_bolt ~-6 ~ ~-6 default_lightning_bolt",
          "summon lightning_bolt ~-6 ~ ~6 default_lightning_bolt",
          "summon lightning_bolt ~6 ~ ~-6 default_lightning_bolt",
          "summon lightning_bolt ~14 ~ ~ default_lightning_bolt",
          "summon lightning_bolt ~ ~ ~14 default_lightning_bolt",
          "summon lightning_bolt ~-14 ~ ~ default_lightning_bolt",
          "summon lightning_bolt ~ ~ ~-14 default_lightning_bolt",
          "summon lightning_bolt ~12 ~ ~12 default_lightning_bolt",
          "summon lightning_bolt ~-12 ~ ~-12 default_lightning_bolt",
          "summon lightning_bolt ~-12 ~ ~12 default_lightning_bolt",
          "summon lightning_bolt ~12 ~ ~-12 default_lightning_bolt",
          "summon lightning_bolt ~28 ~ ~ default_lightning_bolt",
          "summon lightning_bolt ~ ~ ~28 default_lightning_bolt",
          "summon lightning_bolt ~-28 ~ ~ default_lightning_bolt",
          "summon lightning_bolt ~ ~ ~-28 default_lightning_bolt",
          "summon lightning_bolt ~24 ~ ~24 default_lightning_bolt",
          "summon lightning_bolt ~-24 ~ ~-24 default_lightning_bolt",
          "summon lightning_bolt ~-24 ~ ~24 default_lightning_bolt",
          "summon lightning_bolt ~24 ~ ~-24 default_lightning_bolt",
          "summon lightning_bolt ~34 ~ ~ default_lightning_bolt",
          "summon lightning_bolt ~ ~ ~34 default_lightning_bolt",
          "summon lightning_bolt ~-34 ~ ~ default_lightning_bolt",
          "summon lightning_bolt ~ ~ ~-34 default_lightning_bolt",
          "summon lightning_bolt ~30 ~ ~30 default_lightning_bolt",
          "summon lightning_bolt ~-30 ~ ~-30 default_lightning_bolt",
          "summon lightning_bolt ~-30 ~ ~30 default_lightning_bolt",
          "summon lightning_bolt ~30 ~ ~-30 default_lightning_bolt",
          "summon lightning_bolt ~42 ~ ~ default_lightning_bolt",
          "summon lightning_bolt ~ ~ ~42 default_lightning_bolt",
          "summon lightning_bolt ~-42 ~ ~ default_lightning_bolt",
          "summon lightning_bolt ~ ~ ~-42 default_lightning_bolt",
          "summon lightning_bolt ~38 ~ ~38 default_lightning_bolt",
          "summon lightning_bolt ~-38 ~ ~-38 default_lightning_bolt",
          "summon lightning_bolt ~-38 ~ ~38 default_lightning_bolt",
          "summon lightning_bolt ~38 ~ ~-38 default_lightning_bolt"
        ]
      },
      "damage": {
        "type": "durability",
        "amount": 9,
        "target": "self"
      }
    },
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        },
        {
          "randomize": [
            {
              "weight": 15
            },
            {
              "weight": 85,
              "shoot": {
                "projectile": "entity:lightning_projectile",
                "launch_power": 1
              }
            }
          ]
        }
      ]
    }
  }
}
```

### 22. Magma Sword — `effect:magma_sword`

**Архив 1.6:**

```json
{
  "description": {
    "identifier": "effect:magma_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 1000
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "magma_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:magma_sword"
          ],
          "repair_amount": 1000
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 7
  }
}
```

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:magma_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 1316
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "magma_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:magma_sword"
          ],
          "repair_amount": 1316
        },
        {
          "items": [
            "minecraft:magma"
          ],
          "repair_amount": 100
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 7.2,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    }
  }
}
```

### 23. Nether Star Sword — `effect:nether_star_sword`

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:nether_star_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": true,
    "minecraft:should_despawn": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 3256
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "nether_star_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:nether_star_sword"
          ],
          "repair_amount": 3256
        },
        {
          "items": [
            "minecraft:nether_star"
          ],
          "repair_amount": 3000
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 7,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "shoot": {
            "projectile": "entity:nether_star_projectile",
            "launch_power": 1
          }
        },
        {
          "randomize": [
            {
              "weight": 80,
              "run_command": {
                "command": [
                  "summon entity:nether_star ^ ^20 ^-6"
                ]
              }
            },
            {
              "weight": 20,
              "run_command": {
                "command": [
                  "summon entity:nether_star ^ ^20 ^-6",
                  "summon entity:nether_star ^ ^18 ^-6"
                ]
              }
            }
          ]
        },
        {
          "randomize": [
            {
              "weight": 9999,
              "damage": {
                "type": "durability",
                "amount": 1,
                "target": "self"
              }
            },
            {
              "weight": 1,
              "run_command": {
                "command": [
                  "summon entity:ultra_instinct_explode"
                ]
              }
            }
          ]
        }
      ]
    }
  }
}
```

### 24. Obsidian Sword — `effect:obsidian_sword`

**Архив 1.6:**

```json
{
  "description": {
    "identifier": "effect:obsidian_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 3000
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "obsidian_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:obsidian_sword"
          ],
          "repair_amount": 3000
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 12
  }
}
```

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:obsidian_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 3000
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "obsidian_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:obsidian_sword"
          ],
          "repair_amount": 3000
        },
        {
          "items": [
            "minecraft:obsidian"
          ],
          "repair_amount": 120
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 8,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "randomize": [
        {
          "weight": 55,
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        },
        {
          "weight": 30,
          "damage": {
            "type": "durability",
            "amount": 2,
            "target": "self"
          }
        },
        {
          "weight": 15,
          "damage": {
            "type": "durability",
            "amount": 3,
            "target": "self"
          }
        }
      ]
    }
  }
}
```

### 25. Quartz Diamond — `effect:quartz_diamond`

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:quartz_diamond",
    "category": "items"
  },
  "components": {
    "minecraft:max_stack_size": 9,
    "minecraft:foil": true,
    "minecraft:hand_equipped": false,
    "minecraft:icon": {
      "texture": "quartz_diamond"
    },
    "minecraft:display_name": {}
  },
  "events": {}
}
```

### 26. Quartz Diamond Stick — `effect:quartz_diamond_stick`

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:quartz_diamond_stick",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": true,
    "minecraft:max_stack_size": 1,
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:can_destroy_in_creative": true,
    "minecraft:icon": {
      "texture": "quartz_diamond_stick"
    },
    "minecraft:durability": {
      "max_durability": 20
    },
    "minecraft:display_name": {},
    "minecraft:damage": 24,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "randomize": [
        {
          "weight": 10,
          "run_command": {
            "command": [
              "damage @s 1 magic"
            ]
          }
        },
        {
          "weight": 85,
          "run_command": {
            "command": [
              "damage @s 3 magic"
            ]
          }
        },
        {
          "weight": 5,
          "run_command": {
            "command": [
              "damage @s 6 magic"
            ]
          }
        }
      ]
    }
  }
}
```

### 27. Quartz Sword — `effect:quartz_sword`

**Архив 1.6:**

```json
{
  "description": {
    "identifier": "effect:quartz_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": true,
    "minecraft:max_stack_size": 1,
    "minecraft:durability": {
      "max_durability": 1
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "quartz_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:quartz_sword"
          ],
          "repair_amount": 1
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 600
  }
}
```

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:quartz_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": true,
    "minecraft:max_stack_size": 1,
    "minecraft:durability": {
      "max_durability": 1
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "quartz_sword"
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:render_offsets": {
      "main_hand": {
        "first_person": {
          "position": [
            1.0,
            0,
            -2
          ],
          "scale": [
            0.07,
            0.07,
            0.07
          ]
        },
        "third_person": {
          "position": [
            0.2,
            1.1,
            -0.5
          ],
          "scale": [
            0.08,
            0.08,
            0.08
          ]
        }
      }
    },
    "minecraft:display_name": {},
    "minecraft:damage": 600,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 10,
            "target": "self"
          }
        },
        {
          "run_command": {
            "command": [
              "effect @a[r=1] instant_damage 1 99 true",
              "particle minecraft:knockback_roar_particle ~ ~1 ~"
            ]
          }
        }
      ]
    }
  }
}
```

### 28. Sea Sword — `effect:sea_sword`

**Архив 1.6:**

```json
{
  "description": {
    "identifier": "effect:sea_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": true,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 1000
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "sea_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:sea_sword"
          ],
          "repair_amount": 1000
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 7
  }
}
```

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:sea_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": true,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 1356
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "sea_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:sea_sword"
          ],
          "repair_amount": 1356
        },
        {
          "items": [
            "minecraft:heart_of_the_sea"
          ],
          "repair_amount": 482
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 7,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    }
  }
}
```

### 29. Shulker Sword — `effect:shulker_sword`

**Архив 1.6:**

```json
{
  "description": {
    "identifier": "effect:shulker_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 1000
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "shulker_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:shulker_sword"
          ],
          "repair_amount": 1000
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 7
  }
}
```

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:shulker_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:cooldown": {
      "category": "shulker_sword",
      "duration": 8
    },
    "minecraft:durability": {
      "max_durability": 2609
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "shulker_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:shulker_sword"
          ],
          "repair_amount": 2609
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 6,
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "on_use": {
      "run_command": {
        "command": [
          "particle minecraft:cauldron_explosion_emitter ~3 ~ ~",
          "particle minecraft:cauldron_explosion_emitter ~ ~ ~3",
          "particle minecraft:cauldron_explosion_emitter ~-3 ~ ~",
          "particle minecraft:cauldron_explosion_emitter ~ ~ ~-3",
          "particle minecraft:cauldron_explosion_emitter ~-2.5 ~ ~2.5",
          "particle minecraft:cauldron_explosion_emitter ~2.5 ~ ~-2.5",
          "particle minecraft:cauldron_explosion_emitter ~2.5 ~ ~2.5",
          "particle minecraft:cauldron_explosion_emitter ~-2.5 ~ ~-2.5",
          "effect @e[r=6,family=!shulker_sword] levitation 1 18 false"
        ]
      },
      "damage": {
        "type": "durability",
        "amount": 8,
        "target": "self"
      }
    },
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        },
        {
          "randomize": [
            {
              "weight": 10,
              "shoot": {
                "projectile": "minecraft:shulker_bullet",
                "launch_power": 1
              },
              "run_command": {
                "command": [
                  "playsound random.bow @a[r=10] ~ ~ ~ 1 0.4"
                ]
              }
            },
            {
              "weight": 90
            }
          ]
        }
      ]
    }
  }
}
```

### 30. Silver Ingot — `effect:silver_ingot`

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:silver_ingot",
    "category": "items"
  },
  "components": {
    "minecraft:max_stack_size": 64,
    "minecraft:hand_equipped": false,
    "minecraft:icon": {
      "texture": "silver_ingot"
    },
    "minecraft:display_name": {}
  },
  "events": {}
}
```

### 31. Silver Sword — `effect:silver_sword`

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:silver_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 1800
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "silver_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:silver_sword"
          ],
          "repair_amount": 1800
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:render_offsets": {
      "main_hand": {
        "first_person": {
          "position": [
            0.67,
            0,
            -1.19
          ]
        },
        "third_person": {
          "position": [
            0.36,
            1.5,
            -0.66
          ]
        }
      }
    },
    "minecraft:display_name": {},
    "minecraft:damage": 6,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    }
  }
}
```

### 32. Slime Sword — `effect:slime_sword`

**Архив 1.6:**

```json
{
  "description": {
    "identifier": "effect:slime_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 675
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "slime_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:slime_sword"
          ],
          "repair_amount": 675
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 6
  }
}
```

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:slime_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 675
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "slime_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:slime_sword"
          ],
          "repair_amount": 675
        },
        {
          "items": [
            "minecraft:slime"
          ],
          "repair_amount": 48
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 6,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    }
  }
}
```

### 33. Spectral Sword — `effect:spectral_sword`

**Архив 1.6:**

```json
{
  "description": {
    "identifier": "effect:spectral_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": true,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 3256
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "spectral_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:spectral_sword"
          ],
          "repair_amount": 3256
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 9
  }
}
```

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:spectral_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": true,
    "minecraft:should_despawn": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:cooldown": {
      "category": "spectral_sword",
      "duration": 18
    },
    "minecraft:durability": {
      "max_durability": 3256
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "spectral_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:spectral_sword"
          ],
          "repair_amount": 3256
        },
        {
          "items": [
            "minecraft:end_crystal"
          ],
          "repair_amount": 620
        },
        {
          "items": [
            "minecraft:nether_star"
          ],
          "repair_amount": 2052
        }
      ]
    },
    "minecraft:render_offsets": {
      "main_hand": {
        "first_person": {
          "position": [
            0.57,
            0.1,
            -1.24
          ]
        },
        "third_person": {
          "position": [
            0.41,
            1.7,
            -0.7
          ]
        }
      }
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 9,
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "on_use": {
      "damage": {
        "type": "durability",
        "amount": 15,
        "target": "self"
      },
      "shoot": {
        "projectile": "entity:ender_crystal_projectile",
        "launch_power": 1
      },
      "run_command": {
        "command": [
          "playsound portal.travel @a[r=16] ~ ~ ~ 1 5",
          "event entity @e[type=ender_crystal,family=!ender_crystal_default,family=!ender_crystal_scale,c=1,r=4] minecraft:ender_crystal_scale"
        ]
      }
    },
    "weapon": {
      "randomize": [
        {
          "weight": 99,
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        },
        {
          "weight": 1,
          "run_command": {
            "command": [
              "event entity @e[type=ender_crystal,family=!ender_crystal_default,family=!ender_crystal_scale,c=1] minecraft:crystal_explode"
            ]
          }
        }
      ]
    }
  }
}
```

### 34. Spider Sword — `effect:spider_sword`

**Архив 1.6:**

```json
{
  "description": {
    "identifier": "effect:spider_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 628
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "spider_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:spider_sword"
          ],
          "repair_amount": 628
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 6
  }
}
```

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:spider_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 628
    },
    "minecraft:cooldown": {
      "category": "spider_sword",
      "duration": 28
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "spider_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:spider_sword"
          ],
          "repair_amount": 628
        },
        {
          "items": [
            "minecraft:web"
          ],
          "repair_amount": 128
        },
        {
          "items": [
            "minecraft:spider_eye"
          ],
          "repair_amount": 48
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 100
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 5,
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "on_use": {
      "run_command": {
        "command": [
          "event entity @s spider_sword_skill"
        ],
        "target": "holder"
      },
      "damage": {
        "type": "durability",
        "amount": 8,
        "target": "self"
      }
    },
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        },
        {
          "randomize": [
            {
              "weight": 95
            },
            {
              "weight": 5,
              "shoot": {
                "projectile": "entity:web",
                "launch_power": 1
              }
            }
          ]
        }
      ]
    }
  }
}
```

### 35. Sponge Sword — `effect:sponge_sword`

**Архив 1.6:**

```json
{
  "description": {
    "identifier": "effect:sponge_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 128
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "sponge_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:sponge_sword"
          ],
          "repair_amount": 128
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 6
  }
}
```

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:sponge_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:durability": {
      "max_durability": 128
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "sponge_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:sponge_sword"
          ],
          "repair_amount": 128
        },
        {
          "items": [
            "minecraft:sponge"
          ],
          "repair_amount": 62
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 5,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    }
  }
}
```

### 36. Sword Of Time — `effect:sword_of_time`

**Архив 1.6:**

```json
{
  "description": {
    "identifier": "effect:sword_of_time",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": true,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 128
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "sword_of_time"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:sword_of_time"
          ],
          "repair_amount": 128
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 7
  }
}
```

### 37. Time Sword — `effect:time_sword`

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:time_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": true,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 13770
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "time_sword"
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:render_offsets": {
      "main_hand": {
        "first_person": {
          "position": [
            1,
            0.5,
            -3
          ],
          "scale": [
            0.04,
            0.04,
            0.04
          ]
        },
        "third_person": {
          "position": [
            0.95,
            3.3,
            -1.2
          ],
          "scale": [
            0.06,
            0.06,
            0.06
          ]
        }
      }
    },
    "minecraft:display_name": {},
    "minecraft:damage": 13,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "randomize": [
        {
          "weight": 90,
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        },
        {
          "weight": 6,
          "damage": {
            "type": "durability",
            "amount": 16,
            "target": "self"
          }
        },
        {
          "weight": 3,
          "damage": {
            "type": "durability",
            "amount": 32,
            "target": "self"
          }
        },
        {
          "weight": 1,
          "damage": {
            "type": "durability",
            "amount": 64,
            "target": "self"
          }
        }
      ]
    }
  }
}
```

### 38. Tnt Sword — `effect:tnt_sword`

**Архив 1.6:**

```json
{
  "description": {
    "identifier": "effect:tnt_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": false,
    "minecraft:max_stack_size": 1,
    "minecraft:durability": {
      "max_durability": 1
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "tnt_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:tnt_sword"
          ],
          "repair_amount": 1
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 7
  }
}
```

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:tnt_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:durability": {
      "max_durability": 64
    },
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:cooldown": {
      "category": "tnt_sword",
      "duration": 10
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "tnt_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:tnt_sword"
          ],
          "repair_amount": 64
        },
        {
          "items": [
            "minecraft:tnt"
          ],
          "repair_amount": 18
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 4,
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "on_use": {
      "run_command": {
        "command": [
          "summon minecraft:tnt ~~~ giant_tnt",
          "title @a[r=18] actionbar §fSuper§4TNT §f§lhas been activated.",
          "playsound random.fuse @a ~~~"
        ]
      },
      "damage": {
        "type": "durability",
        "amount": 18,
        "target": "self"
      }
    },
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        },
        {
          "randomize": [
            {
              "weight": 10
            },
            {
              "weight": 90,
              "shoot": {
                "projectile": "entity:tnt",
                "launch_power": 1
              }
            }
          ]
        }
      ]
    }
  }
}
```

### 39. Ultra Instinct Sword — `effect:ultra_instinct_sword`

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:ultra_instinct_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": true,
    "minecraft:should_despawn": false,
    "minecraft:max_stack_size": 1,
    "minecraft:durability": {
      "max_durability": 9999
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "ultra_instinct_sword"
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 999
        },
        {
          "block": "minecraft:bamboo",
          "speed": 999
        }
      ]
    },
    "minecraft:render_offsets": {
      "main_hand": {
        "first_person": {
          "rotation": [
            0,
            -5.0,
            95
          ],
          "position": [
            1.8,
            -1.4,
            -5.5
          ],
          "scale": [
            0.04,
            0.04,
            0.04
          ]
        },
        "third_person": {
          "position": [
            1.5,
            3.6,
            -1.8
          ],
          "scale": [
            0.04,
            0.04,
            0.04
          ]
        }
      }
    },
    "minecraft:display_name": {},
    "minecraft:damage": 16,
    "minecraft:cooldown": {
      "category": "ultra_instinct_sword",
      "duration": 61
    },
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "on_use": {
      "shoot": {
        "projectile": "entity:ultra_instinct_projectile",
        "launch_power": 1
      },
      "damage": {
        "type": "durability",
        "amount": 48,
        "target": "self"
      },
      "run_command": {
        "command": [
          "playsound mob.wither.ambient @s ~ ~1 ~ 2 0.6"
        ]
      }
    },
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    }
  }
}
```

### 40. Wet Sponge Sword — `effect:wet_sponge_sword`

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:wet_sponge_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:durability": {
      "max_durability": 64
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "wet_sponge_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:sponge_sword"
          ],
          "repair_amount": 64
        },
        {
          "items": [
            "minecraft:sponge"
          ],
          "repair_amount": 32
        },
        {
          "items": [
            "effect:wet_sponge_sword"
          ],
          "repair_amount": 64
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 3,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    }
  }
}
```

### 41. Wither Skeleton Sword — `effect:wither_skeleton_sword`

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:wither_skeleton_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 128
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "wither_skeleton_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:wither_skeleton_sword"
          ],
          "repair_amount": 128
        },
        {
          "items": [
            "minecraft:coal"
          ],
          "repair_amount": 58
        },
        {
          "items": [
            "minecraft:stick"
          ],
          "repair_amount": 2
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 4,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          },
          "shoot": {
            "projectile": "entity:wither_effect",
            "launch_power": 1
          }
        }
      ]
    }
  }
}
```

### 42. Wither Sword — `effect:wither_sword`

**Архив 1.6:**

```json
{
  "description": {
    "identifier": "effect:wither_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": true,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 1256
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "wither_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:wither_sword"
          ],
          "repair_amount": 1256
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 10
  }
}
```

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:wither_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:should_despawn": false,
    "minecraft:foil": true,
    "minecraft:max_stack_size": 1,
    "minecraft:durability": {
      "max_durability": 3856
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "wither_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:wither_sword"
          ],
          "repair_amount": 3856
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:render_offsets": {
      "main_hand": {
        "first_person": {
          "position": [
            0.8,
            0.1,
            -1.8
          ],
          "scale": [
            0.01,
            0.01,
            0.01
          ]
        },
        "third_person": {
          "position": [
            0.8,
            2.5,
            -1.2
          ],
          "scale": [
            0.027,
            0.027,
            0.027
          ]
        }
      }
    },
    "minecraft:display_name": {},
    "minecraft:damage": 10,
    "minecraft:cooldown": {
      "category": "wither_sword",
      "duration": 3
    },
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "on_use": {
      "shoot": {
        "projectile": "minecraft:wither_skull_dangerous",
        "launch_power": 1
      },
      "run_command": {
        "command": [
          "playsound mob.wither.shoot @a[r=16] ~~~ 1 0.7"
        ]
      },
      "damage": {
        "type": "durability",
        "amount": 3,
        "target": "self"
      }
    },
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        },
        {
          "randomize": [
            {
              "weight": 90
            },
            {
              "weight": 10,
              "shoot": {
                "projectile": "minecraft:wither_skull",
                "launch_power": 1
              },
              "run_command": {
                "command": [
                  "playsound mob.wither.shoot @a[r=16]"
                ]
              }
            }
          ]
        }
      ]
    }
  }
}
```

### 43. Wolf Sword — `effect:wolf_sword`

**Архив 2.8.14:**

```json
{
  "description": {
    "identifier": "effect:wolf_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:durability": {
      "max_durability": 2800
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "wolf_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:wolf_sword"
          ],
          "repair_amount": 2800
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:render_offsets": {
      "main_hand": {
        "first_person": {
          "position": [
            0.67,
            0,
            -1.22
          ]
        },
        "third_person": {
          "position": [
            0.36,
            1.5,
            -0.66
          ]
        }
      }
    },
    "minecraft:display_name": {},
    "minecraft:damage": 5,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    }
  }
}
```
