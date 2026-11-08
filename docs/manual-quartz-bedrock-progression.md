# Quartz Diamond и Bedrock: рецепты, получение и границы зависимостей

Сравнение 1.6 и двух 2.x архивов, без запуска Bedrock. Ни наличие JSON, ни арифметика ингредиентов не подтверждают регистрацию рецепта, добычу или работу команд. В таблицах ниже «предмет/блок» — точный ID, не перевод названия. [Указатель предметов](quick-reference.md) · [руды и loot](manual-ore-and-loot-paths-2.8.md) · [фонтан](manual-fountain-2.8.md) · [правила добычи Bedrock Sword](manual-digger-2.8.md).

## Quartz Sword: одинаковый ID, разные рецепты и побочные эффекты

`effect:quartz_sword` есть в обоих поколениях: damage 600, max durability 1, stack 1 и web/bamboo 15/10. В 1.6 `glint:true`, offhand true и repair self 1; enchantable не объявлен. В 2.x `foil:true`, offhand false, repairable и enchantable не объявлены. Отсутствие компонента не означает доказанной невозможности ремонта или зачарования на произвольном движке.

1.6 `recipes/quartz_sword.json`: pattern `#/#/0` (три однобуквенных ряда), `# = minecraft:quartz_block` data 0, `0 = minecraft:stick` data 0; **result записан массивом** из одного объекта `effect:quartz_sword`, data 0, count 1. Нужно сохранить и этот тип result, не предполагать, что конкретный загрузчик принимает массив. Player sensor добавляет пустую группу `minecraft:quartz_sword`; в item нет `minecraft:weapon` и on-use. Это только локальная прямая цепь, а не доказательство отсутствия внешних эффектов.

2.x `recipes/quartz_diamond_sword.json`: `Q/Q/#`, Q = `effect99:quartz_diamond_block`, # = `effect:quartz_diamond_stick` data 0, result = `effect:quartz_sword`. На три weapon-хука: в sequence сначала direct durability damage 10, затем `effect @a[r=1] instant_damage 1 99 true` и particle. Это selector **всех игроков** в радиусе, не команда строго по владельцу. Player hand-event при отсутствии family `quartz_sword` задаёт `damage @s 14 magic` и добавляет группу; stop при наличии этой family снова задаёт `damage @s 14 magic`, снимает группу и добавляет default_player. Конфликт family, порядок соседних полей и успех damage не установлены.

## Граф крафта 2.x: Quartz Diamond

| Рецепт | Pattern и key | Точный result в файле |
|---|---|---|
| `quartz_diamond_block` | `###/###/###`, # = `effect:quartz_diamond` | `effect99:quartz_diamond_block` |
| `quartz_diamond_stick` | `#/#`, # = `effect:quartz_diamond` | `effect:quartz_diamond_stick` |
| `quartz_diamond_sword` | `Q/Q/#`, Q = `effect99:quartz_diamond_block`, # = `effect:quartz_diamond_stick`, data 0 | `effect:quartz_sword` |

При **условных** допущениях, что все три рецепта зарегистрированы, каждый выполняется штатно и result без count даёт по одному предмету, на один меч по этой цепи нужно 2×9 + 2 = **20** Quartz Diamond. Это стоимость именно данных рецептов, не утверждение о единственном пути в мире или проверенной семантике отсутствующего count. `quartz_diamond` stack 9 и сам является предметом; `quartz_diamond_block` — отдельный блок; `quartz_diamond_stick` — отдельный item damage 24, durability 20, offhand false. У палки три weapon-хука randomize 10/85/5 на `damage @s` 1/3/6 magic соответственно; direct durability damage в этих ветвях не объявлен. При стандартном выборе условное среднее заявленного magic damage = **2.95** на вызов; нельзя добавлять предполагаемый штатный износ или превращать это в средний урон на секунду.

`effect99:quartz_diamond_ore` при условии on_player_destroyed проверяет буквальное Molang-выражение для iron/diamond/netherite pickaxe или bedrock_sword, без скобок вызова; при активации события запрашивает отдельную таблицу. Она даёт один выбор с весами 89/10/1 и set_count 1…1/1…2/2…4 для `effect:quartz_diamond`, а также event содержит шесть команд summon XP-orb и instant_damage ближайшему `@p[r=6]`. Эти веса — не вероятность нахождения руды или гарантия успеха loot. Базовый `minecraft:loot` ссылается на отсутствующий в обоих архивах `loot_tables/blocks/null.json`, отдельно от таблицы события: внешний/ванильный путь не исключён.

Только архив 2.8.8 содержит соответствующие feature и feature_rule: 5 iterations, scatter 160/200, biome overworld или the_end, y gaussian extent `[0,16]`, allowlist stone/end_stone, структура `mystructure:quartz_diamond_ore`; файл структуры 1×1×1 с этим блоком есть. В 2.8.14 отсутствуют и оба файла feature/feature_rule, и файл этой структуры, хотя block и loot существуют. Имя структуры, регистрация и среда могут зависеть от движка/других пакетов; 160/200 не является шансом появления руды на блок или чанк.

## Фонтан — не крафт Quartz Sword

Выброшенный предмет, который функция пометила по имени `Quartz Diamond`, получает тег `wish_1`; соответствующее имя блока получает `wish_2`. При выполнении отдельной геометрии фонтана и вызове `item.json` randomize: успех `wish_1` 8/1000, `wish_2` 25/1000, загружает **`ultra_instinct_sword`**, не Quartz Sword. Остальные ветви также завершают исходную item-сущность; успешная ветвь меняет sand на concretepowder в заданном объёме и выполняет `kill @s`. Это условные доли после тега, проверки блоков и события, а не шанс на любой выброшенный материал. Подробные 15 detect, выбор `@s` и NBT — [разбор фонтана](manual-fountain-2.8.md).

## Bedrock Stick и Bedrock Sword

Оба точных ID существуют в 2.x, не в item 1.6. `effect:bedrock_stick` damage 6, stack 1, offhand false, `should_despawn:true`, `can_destroy_in_creative:true`; `effect:bedrock_sword` damage 18, stack 1, offhand false, `should_despawn:false`, `can_destroy_in_creative:false`. У обоих в JSON **пустой** `minecraft:weapon`; durability, repairable и enchantable не объявлены. Эти отсутствия и `should_despawn` нельзя превращать в гарантированную неразрушимость/несгораемость.

Рецепты: `bedrock_stick` = два `minecraft:bedrock` вертикально; `bedrock_sword` = два `minecraft:bedrock` над `effect:bedrock_stick`. При допущении по одному result без count и штатной регистрации: **четыре** bedrock на палку и меч по двум рецептам, если палка ещё не получена и нет альтернатив. В исходных определениях эти рецепты не доказывают доступности или добычи bedrock.

Bedrock Sword объявляет digger с 68 упорядоченными правилами: tags-селектор speed 999; отдельные `quartz_diamond_block` 50, `quartz_diamond_ore` 100, `silver_ore` 999; далее конкретные блоки со speed 999. Там есть буквальный `minecraft:pumkin` и повторы трёх правил; приоритет пересекающихся tags и block IDs не определён этими цифрами. Явного правила `minecraft:bedrock` в списке нет. Отсутствие отдельного правила не доказывает отсутствия внешнего тега, возможности добычи или скорости по умолчанию.

В 2.x тегированный выпавший Bedrock Sword при огне направляется в `respawn_event_1`: `structure load bedrock_sword ~ ~1 ~` и `kill @s`. NBT содержит сохранённую item-сущность этого ID; это **создание из структуры**, а не доказанный перенос прочности, имени, чар или иной информации исходного item. Назначение тега зависит от буквального форматированного имени и последовательности событий.

## Источники Bedrock и Ultra Instinct: только объявленные механизмы

`entity:ultra_instinct_explode` объявляет explosion power 8, `max_resistance:4.0`, griefing true; он вызывается при попадании Ultra Instinct projectile и в редкой 1/10000 ветви одного из событий Nether Star Sword. Это не доказательство разрушения `minecraft:bedrock`, выпадения блока или действительного срабатывания. Projectile Ultra также содержит `kill @e[type=item,r=24]` в event частиц: возможна потеря всех подходящих выпавших предметов вокруг снаряда, а не только материалов владельца. Эти цепи отдельно от фонтанной выдачи Ultra и от прямого крафта Bedrock Sword.

## Что ещё не следует из данных

Арифметика крафта и условные ожидания используют явно перечисленные допущения. Запуск Bedrock, проверка рецептов/выпадения, обработка отсутствующих путей, конфликт тегов блоков и фактическое поведение взрывов не проводились; архивы не редактировались.
