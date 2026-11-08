# Wolf Sword 2.x: условия контроллеров, клиент и пересечения family

Статический разбор обеих версий: `wolf_sword.json`, клиентский `player.entity.json` и выбранные файлы Slime/Living Flame побайтово одинаковы; **серверный** `entities/player.json` различается между версиями, однако рассмотренные здесь wolf-группы, события и сенсоры в нём структурно совпадают. [Воспроизводимая таблица примерных значений условий](wolf-condition-samples-2.8.md) предполагает обычный приоритет `&&` выше `||` и точные десятичные сравнения: это **не** исполнение Molang и не симуляция смены состояний. Реальные численные значения, порядок трёх контроллеров, компонентов и сенсоров, действия событий и совместимость с новой версией нужно проверять.

## Три независимых условия, а не один таймер

В `player.json` в `scripts.animate` включены `wolf_sword_0`, `_1`, `_2`; aliases ведут к трём отдельным контроллерам. Каждый имеет два состояния и безусловный возврат `1.0`. Переходы, ведущие к on_entry:

| Контроллер | Условие в исходнике кратко | Event на входе в целевое состояние |
|---|---|---|
| `wolf_sword` | main-hand имя `wolf_sword`, phase 0, `0.77 ≤ time ≤ 0.78` | `wolf_sword_start_events` |
| `start_wolf_sword` | main-hand имя `wolf_sword`, phase 0, `time ≤ 0.20` **или** `time ≥ 0.80` | `wolf_transformation` |
| `end_wolf_sword` | `W || !W && phase == 0 && time == 0.20` без дополнительных скобок, где W — запрос имени main hand равен `wolf_sword` | `stop_wolf_transformation` |

При обычном приоритете && выше || третье выражение равно `W || (!W && phase == 0 && time == 0.20)`: когда W истинно, его условие также истинно при **любых** значениях phase/time. Если W ложно, оно истинно только при одновременных phase 0 и **точном** 0.20. Фактическую достижимость такого точного значения и семантику Molang нельзя принять на веру.

Отсюда в простой модели: на 0.77/0.78 первое и третье условия одновременно истинны; на 0.80 и 0.20 — второе и третье; на 0.79 только третье. Если меча в main hand нет, при phase 0 и точно 0.20 условие третьего тоже истинно. Это **не** значит, что оба события обязательно выполнятся одновременно: переход зависит от текущего состояния каждого контроллера, а частота, порядок и приоритет не проверены. При обычном прочтении полей `stop_wolf_transformation` также не проверяет наличие меча или family перед командами и добавлением группы `minecraft:wolf_sword`; соперничающий hand-sensor может вызывать другое stop-событие.

В behavior-сенсоре используется `has_equipment`, `domain:hand`, ID `effect:wolf_sword`; в контроллерах и клиенте — `query.get_equipped_item_name('main_hand') == 'wolf_sword'`. Не считать их условия автоматически идентичными для offhand, пространства имён, переименования и другой версии запроса; предмет записывает `allow_off_hand:false`, но разрешение исключительных ситуаций всё равно проверяется движком.

## Что делают события и группы

- `wolf_sword_start_events`, если self family != `wolf_transformation`, добавляет `wolf_transformation` и вызывает функцию, которая содержит `tellraw @s` с текстом `§fFor some reason you feel nauseous...`. Sensor family `wolf_transformation` направляет в `starting_wolf_transformation`, где `effect @s nausea 5 0 true`.
- `wolf_transformation` при family != `complete_wolf_transformation` посылает fizz, два воя, три частицы и добавляет группу `complete_wolf_transformation`; отдельный следующий sequence-шаг при family `wolf_transformation` удаляет группу `wolf_transformation`. Изменение family между шагами и порядок обработки нуждаются в игровом тесте.
- `complete_wolf_transformation`: `type_family` **буквально** `[wolf,wolf_sword,complete_wolf_transformation,monster]`, без слова `player`; `attack.damage:15`, looping random timer `[3,6]` на одноэлементный randomize рычания, damage sensor при `has_damage != void` с `deals_damage:true` и bark-событием. Это не доказывает сложение 15 с item damage 5, а наличие одного weight 1 не устанавливает частоту рычания.
- Sensor по family `complete_wolf_transformation` запускает `wolf_movement`, который добавляет группу `movement.value:0.18`. Конфликты с базовым движением и другие одновременно активные группы не разрешаются автоматически в памятке.
- `stop_wolf_transformation` без filters в первом sequence-шаге задаёт nausea 0, blindness 0 и два `stopsound @a`; следующий шаг удаляет три группы превращения и добавляет `minecraft:wolf_sword`. Это не та же функция, что `stop_wolf_sword_event`, который вызывается из hand-sensor при `has_equipment != effect:wolf_sword`. Последний при family `wolf_sword` удаляет три группы и задаёт nausea 0, а при family `complete_wolf_transformation` отдельной ветвью снимает complete и задаёт nausea/blindness **9999, amplifier 0**. Как добавление `default_player` и изменение family влияет на применимость следующего шага, не установлено.

## Клиент не является подтверждением серверной способности

Клиентский `player.entity.json` вычисляет `variable.wolf_transformation` в третьем лице и `variable.wolf_vision` в первом: обе проверки используют W, phase 0 и `time ≤ 0.20 || time ≥ 0.80`, дополнительно различая `variable.is_first_person`. Эти условия не проверяют серверную family `complete_wolf_transformation` и не включают окно подготовки 0.77…0.78. Таким образом, клиентское условие графики и серверное событие могут логически расходиться; реальный выбор рендера, загрузка assets и синхронизация тоже нуждаются в проверке.

## Возможное пересечение с другими мечами

[Условная межигровая матрица family и type](manual-family-cross-effects-2.8.md).

Базовый player и `minecraft:default_player` объявляют family `[player,default_player]`, в то время как группа complete выше записывает `[wolf,...,monster]`. Как движок разрешает конкурирующие `minecraft:type_family`, необходимо измерить; **не** считать исчезновение `player` или присутствие `monster` гарантированным состоянием.

Если действующая family действительно содержит `monster`, `entity:mountable_slime` в `slime_events` выполняет `execute @e[r=1,family=monster] ~~~ summon entity:slime_damage`: потенциальная цель может включать другого превращённого игрока. Его снаряд имеет impact damage 1; попадание от одного summon не доказано. Группа passive Living Flame выбирает цели family `monster` в max_dist 16 — это ещё одна потенциальная реакция на игрока.

Если действующая family не содержит `player`, удержание Fire Sword другим игроком вызывает `execute @e[family=!player,type=!item,r=3] ~ ~ ~ summon entity:fire` и потенциально включает такого игрока в выборку. Это условие **family**, не `type=!player`; реальное действие entity:fire и успешность команды не установлены. Эти сценарии важны в мультиплеере, но являются гипотезами на основе объявленных групп, не установленными эффектами.
