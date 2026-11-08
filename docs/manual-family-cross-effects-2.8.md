# Семейства и пересечение эффектов между игроками 2.x

Это **условная модель текстовых селекторов**, не имитация Bedrock. В обеих 2.x версиях `minecraft:player` базово объявляет family `[player,default_player]`. Из **35** его component groups, которые сами содержат `minecraft:type_family`, ровно две не перечисляют `player`: `minecraft:ghost_sword` и `complete_wolf_transformation`. Это подсчёт объявлений, а не доказательство, что базовая family исчезает при добавлении группы или что одновременно возможны все состояния. Остальные 33 группы с type_family слово `player` содержат. [Группы 2.x](player-groups-2.8.14.md) · [Ghost](manual-ghost-nether-ultra.md#ghost-sword) · [Wolf](manual-wolf-conditions-2.8.md).

## Почему `family` и `type` нельзя отождествлять

| Кандидат | Type/ID сущности в объявлении | Family в выбранной группе/базе | Где объявлено |
|---|---|---|---|
| Обычный игрок | `minecraft:player` | `[player,default_player]` | базовые components player |
| Игрок с Ghost-группой | `minecraft:player` | `[ghost_sword]` | `minecraft:ghost_sword` |
| Игрок с полной Wolf-группой | `minecraft:player` | `[wolf,wolf_sword,complete_wolf_transformation,monster]` | `complete_wolf_transformation` |
| Щит Shulker | `entity:shulker_shield`, runtime shulker | `[effect99_entities,player,shulker_sword]` | база shield |
| Ездовой слизень в defense | `entity:mountable_slime`, runtime slime | `[effect99_entities,tamed_slime,player]` | `defense_mode_slime` |

Игроки остаются **идентификатором сущности** `minecraft:player` в объявлении, а две пользовательские сущности не становятся игроками только из-за слова `player` в family. Фактическое совпадение `type` с runtime identifier, правила объединения семей и состояние одновременных групп необходимо проверять на движке. Следующая таблица использует исключительно гипотезу, что перечисленная family является действующей и что `type=player` выбирает объявленный тип игрока, а не family.

## Таблица потенциальных совпадений

Столбцы не учитывают расстояние, измерение, доступность команд, столкновение и другие фильтры. «Да» означает лишь, что **показанный текстовый предикат** совпадает при этих допущениях; не что эффект сработал.

| Предикат | Обычный player | Ghost player | Wolf player | Shulker shield | Слизень defense |
|---|---:|---:|---:|---:|---:|
| `family=!player` | нет | да | да | нет | нет |
| `type=!player` | нет | нет | нет | да | да |
| `family=monster` | нет | нет | да | нет | нет |
| `family=!shulker_sword` | да | да | да | нет | да |
| `family=default_player` | да | нет | нет | нет | нет |

Эти столбцы особенно чувствительны к тому, заменяет ли группа базовое семейство или объединяется с ним. Например, при сохранённой базовой family `player` предикат `family=!player` для Ghost/Wolf не будет совпадать; условную строку выше нельзя выдавать за факт в игре.

## Где эти различия реально записаны

1. При удержании Fire Sword `player.json` содержит `execute @e[family=!player,type=!item,r=3] ~ ~ ~ summon entity:fire`. При только family из таблицы Ghost и Wolf потенциально проходят family-исключение, щит и defense-слизень — нет. `type=!item`, радиус и исполнение также важны; `summon` не равен доказанному урону.
2. У Cactus Sword событие `damage @e[r=1.4,type=!player] 1 contact entity @s` исключает по **type**, а затем отдельно выполняет `damage @s 1 contact`. Clock/Time выбирают `effect @e[type=!player] ...`, а не `family=!player`. Если тип разрешается по указанным ID, player с любой family по-прежнему не совпадает с первым селектором, а пользовательский shield или slime потенциально совпадают. Защита самих сущностей и другие условия здесь не рассмотрены.
3. В событии defense-слизня `execute @e[r=1,family=monster] ~~~ summon entity:slime_damage` может выбрать игрока, если у него действительно активна содержащая monster Wolf-family. Пчела-меч и passive Living Flame в своих `nearest_attackable_target` тоже смотрят family monster, но также имеют собственные условия, дальность и AI. Сам summon снаряда не доказывает попадания.
4. On-use Shulker Sword задаёт `effect @e[r=6,family=!shulker_sword] levitation 1 18 false`: в исходном предикате **нет** исключения `type=player` или `family=player`. Щит с указанной family исключён, обычный игрок и Ghost/Wolf потенциально попадают. Это не утверждение, что два защитных компонента совместимы или levitation реально подействует.
5. Clock/Time посылают movement-event `@a[family=default_player]`. Даже если `@a` по-прежнему выбирает игроков, добавочный family-фильтр не совпадает с моделируемыми только Ghost/Wolf-группами. При иной семантике объединения семей результат может быть другим.

Защитный trigger пчелы проверяет `other` family player, а не ID владельца; условная Wolf-family может одновременно подойти фильтру monster и не подойти защите от других player-family. Применимость зависит от активных компонентов, `other`, AI и порядка обработки. Все такие пункты — риски при будущей проверке, не требования менять исходное поведение.

## Предел статической модели

Таблица не перечисляет все взаимодействия семей в архиве; также не предполагается, что записи всегда выполняются. Она сопоставляет точные объявленные family и выбранные оригинальные selector. Внешние компоненты, другие пакеты, положение сущностей, интерпретация type/runtime и порядок add/remove групп остаются за пределами статического результата.
