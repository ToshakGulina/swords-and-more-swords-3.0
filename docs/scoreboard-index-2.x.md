# Scoreboard: буквальные операции и selectors — 2.8.8 и 2.8.14

Лексический поиск `scoreboard`, `scores=` и старых ключей `score_*` во всех `.json`, `.mcfunction`, `.js` behavior pack даёт **15 исходных строк**. Сканируются и строки JSON с ошибками, комментарии, JS и возможные строковые данные; запись сама по себе не доказывает выполнение команды. Имена objectives извлекаются только из буквальных `objectives add/remove`, `players add/set/remove` с числовым аргументом и `scores={...}`; иные формы перечислены как нераспознанные, если встретились.

Числа — **значения score**, не секунды или тики. Операция objective и конкретная запись игрока/сущности различны; селектор, `@s`, ближайший `@p`, контекст execute, наличие objective, прерывание последовательности и конкуренцию игроков нельзя игнорировать. Здесь группировка по имени облегчает поиск, но не заменяет исходный порядок внутри события, условий и вызовов. Один и тот же ряд может попасть в несколько групп; повторы сохраняются.

Распознанные objectives: `Effect99` (4 строк), `slime_despawn` (5 строк), `sponge_sword` (6 строк).

- Нераспознанные кандидаты: нет в ограниченной области сканирования.

В 2.x команды `sponge_sword` находятся в `player.json` и указывают `@s`; `slime_despawn` в одних командах сбрасывается по selector ближайшего слизня, а в других увеличивается для `@s` в событии слизня. Проверки и сбросы в разных событиях не гарантируют фиксированную длительность. [Подробный Slime](manual-traces-2.8.14.md#slime-sword-effectslime_sword-и-slime-king) · [Sponge](manual-traces-2.8.14.md#sponge-sword-и-wet-sponge-sword-effectsponge_sword-effectwet_sponge_sword). В выбранных строках 2.8.8/2.8.14 совпадают пути, номера и текст; другие части файлов могут различаться.

## Все строки по имени objective

### Effect99

| Файл и строка | Найденные формы | Исходная строка целиком |
|---|---|---|
| `Swords_B/entities/player.json:1063` | `"objectives add"` | `"              \"scoreboard objectives add Effect99 dummy\","` |
| `Swords_B/entities/player.json:1064` | `"players add @s 1"` | `"              \"scoreboard players add @s Effect99 1\","` |
| `Swords_B/entities/player.json:1065` | `"selector Effect99=12000"` | `"              \"title @s[scores={Effect99=12000}] actionbar §l§fCreated by §7Effect99\","` |
| `Swords_B/entities/player.json:1066` | `"players set @s[scores={Effect99=36001}] 1"`, `"selector Effect99=36001"` | `"              \"scoreboard players set @s[scores={Effect99=36001}] Effect99 1\" ] }"` |

### slime_despawn

| Файл и строка | Найденные формы | Исходная строка целиком |
|---|---|---|
| `Swords_B/entities/mountable_slime.json:214` | `"selector slime_despawn=0"` | `"            \"tp @s[scores={slime_despawn=0}] @e[type=player,family=slime_sword,c=1,rm=8,r=12]\","` |
| `Swords_B/entities/mountable_slime.json:215` | `"players add @s 1"` | `"            \"scoreboard players add @s slime_despawn 1\","` |
| `Swords_B/entities/mountable_slime.json:216` | `"selector slime_despawn=100"` | `"            \"execute @s[scores={slime_despawn=100}] ~~~ event entity @s despawn\""` |
| `Swords_B/entities/player.json:1676` | `"players set @e[type=entity:mountable_slime,c=1,r=12] 0"` | `"            \"run_command\": { \"command\": [ \"scoreboard players set @e[type=entity:mountable_slime,c=1,r=12] slime_despawn 0\" ] }"` |
| `Swords_B/entities/player.json:1691` | `"objectives add"` | `"        \"run_command\": { \"command\": [ \"ride @s summon_ride entity:mountable_slime no_ride_change\", \"scoreboard objectives add slime_despawn dummy\" ] }"` |

### sponge_sword

| Файл и строка | Найденные формы | Исходная строка целиком |
|---|---|---|
| `Swords_B/entities/player.json:1565` | `"objectives add"` | `"            \"run_command\": { \"command\": [ \"scoreboard objectives add sponge_sword dummy\" ] }"` |
| `Swords_B/entities/player.json:1574` | `"players add @s 1"` | `"               \"scoreboard players add @s sponge_sword 1\""` |
| `Swords_B/entities/player.json:1583` | `"selector sponge_sword=150"` | `"               \"execute @s[scores={sponge_sword=150}] ~ ~ ~ event entity @s wet_sponge_sword\","` |
| `Swords_B/entities/player.json:1584` | `"selector sponge_sword=155"` | `"               \"execute @s[scores={sponge_sword=155}] ~ ~ ~ event entity @s wet_sponge_sword\","` |
| `Swords_B/entities/player.json:1585` | `"selector sponge_sword=160"` | `"               \"execute @s[scores={sponge_sword=160}] ~ ~ ~ event entity @s wet_sponge_sword\""` |
| `Swords_B/entities/player.json:1595` | `"players set @s 0"` | `"            \"run_command\": { \"command\": [ \"replaceitem entity @s slot.weapon.mainhand 0 effect:wet_sponge_sword 1\", \"scoreboard players set @s sponge_sword 0\", \"title @s actionbar §l§gWet Sponge Sword\" ] }"` |
