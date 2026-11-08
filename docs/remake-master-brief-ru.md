# Swords and More Swords — памятка по предметам и существам

**Принцип сверки:** определять задуманное поведение по описанию и коду 2.8.8 и фиксировать реализуемые правила. Не ставить реализацию в зависимость от того, удалось ли воспроизвести исходный код в старом движке. При существенном противоречии или неоднозначной задумке согласовывать конкретный выбор с пользователем; сохранённые наблюдения — справочные данные. Техническая приёмка готового ремейка по-прежнему необходима. Сверка исходных полей всех 38 мечей: базовый урон, явно заданная прочность и входы weapon совпадают с кодом 2.8.8. Полные сохранённые выписки компонентов и событий предметов также совпадают с архивом. Дополнительно непосредственно с архивом сопоставлены JSON-выписки событий во всех 38 карточках, а также 42 включённые группы и 94 выписки событий игрока в 31 карточке (93 уникальных имени); это проверка записанных данных, а не полноты цепочек, текстовых выводов или всей игровой логики. Дополнительно сверены выписки постоянных компонентов, групп и деревьев событий 12 связанных сущностей: 215 компонентов, 48 групп и 66 событий после разбора JSON. Проверены данные и последовательности/веса, но не вызовы событий, совместимость и игровое исполнение. Повторяющиеся ключи проверены отдельно: у Slime King разные задержки прыжка; у Living Flame повторяется одинаковое fire_immune true, а у ездового слизня — одинаковая группа despawn. Крипер с лишней скобкой в исходнике в эту автоматическую сверку не входит.

**Общая команда выдачи:** описание обещает `/function give` для всех мечей. В функции 2.8.8 записано 35 выдач, отсутствуют Bee Stinger, Wet Sponge и Cursed Pumpkin; 34 используют `@p`, Lightning использует `@s`. В опыте BDS 1.20.50 с исходной функцией при 34 свободных ячейках в выживании 34 меча попали в инвентарь, Silver Sword оказался рядом; в творчестве при тех же условиях Silver Sword не наблюдался ни в инвентаре, ни рядом. Существующие предметы не заменились. Это результаты конкретного опыта, не гарантия для всех версий. По решению пользователя `/function give` выдаёт все 38 мечей в двух заполненных шалкерах по 19; для выдачи нужны две свободные ячейки инвентаря. Если их нет, ничего не выдавать и сообщить, что нужно освободить место; имеющиеся предметы не заменять, шалкеры не выбрасывать. Способ создания заполненных шалкеров и сохранение содержимого при установке и разрушении проверить при реализации и приёмке на целевой версии; при запуске игроком шалкеры получает он сам, при запуске командным блоком — ближайший к блоку игрок.

**Игрок в превращении:** по решению пользователя при проверках получения наград и соответствующих реакций учитывать реального игрока даже в форме Wolf или Ghost, а не терять его из-за отсутствия family `player` в исходной группе. Это не даёт новых способов атаки и не превращает помощников игрока автоматически в игрока. Требование описания, что монстры не нападают на игрока в этих формах, сохраняется отдельно.

## 38 карточек мечей

<a id="sword-bee_sword"></a>
### 01. Bee Stinger — `effect:bee_sword`

**Параметры предмета:** блеск foil: нет; левая рука: нет; should_despawn: не указан; digger: web 15, bamboo 10.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** 5. **Прочность:** 1080. **Кулдаун:** не указан. **Расход применения:** не указан. **Зачарование:** есть: value 9, слот sword.
**Ремонт, единиц за материал:** такой же меч: 1080; honey block: 400; honeycomb: 150.
**Способности:** у `weapon` три входа: удар с уроном, удар без урона и удар по блоку. На каждом вызове сначала записан износ 1, затем выбор: 30/100 — выпустить `entity:bee_sword` с launch_power 1; 70/100 — дополнительный износ 1. По решению пользователя каждую призванную пчелу привязать к владельцу: она не выбирает его целью и не наносит ему вред, в том числе после его превращения в волка. Для других игроков отдельного нового правила не добавлять. По следующему решению пользователя пчёлы не атакуют и не наносят урон призванным помощникам любых игроков, в том числе ездовым паукам. Поведение и параметры призванной сущности — [Пчела меча](#mob-bee-sword). При удержании запускается повторяющийся случайный таймер 3–8 с: если блок под игроком — grass data 0, выбирается одна из 12 равновесных команд, ставящая в позицию игрока один из 11 вариантов red_flower data 0–10 либо yellow_flower data 0; исходная команда не проверяет, что целевой блок пуст. По решению пользователя сохранить исходное поведение: постановка цветка может заменить уже находящийся там блок.
**Получение:** когда обычная пчела атакует, событие countdown_to_perish выбирает выдачу меча 2 из 100 при отсутствии family bee_sword. Это не 2% при каждой смерти пчелы. По решению пользователя не добавлять ограничение на игрока: попытка действует при атаке обычной пчелой игрока или другого моба. В опыте BDS 1.20.50 с 2.8.8 пчела после приписанного скелету урона ответила ему атакой на 2 урона; одна атака не проверяет шанс выпадения.
**Условная модель износа weapon-события:** 1: 3/10, 2: 7/10.

**Вход weapon-события:** при попадании с уроном, ударе без урона и ударе по блоку. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Значок 2.8.8:** `Swords_R/textures/items/bee_sword.png` (ключ атласа `bee_sword`; файл сохранён в наборе ресурсов 2.8.8).

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
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

#### Записанные группы и события владельца 2.8.8

Это относящиеся к предмету поля игрока из сохранённого реестра, а не утверждение об их выполнении; если старый код расходится с решениями выше (например восстановление настроек мира или блоков), выполнять решение, а не переносить старую ошибку. Пустое или отсутствующее поле не подменять предположением.

**Группы:**

- `minecraft:bee_sword` (строки 22,1043,1125,1129,1137): `{"minecraft:timer":{"time":[3,8],"looping":true,"randomInterval":true,"time_down_event":{"event":"bee_sword_flower","target":"self"}},"minecraft:type_family":{"family":["player","bee_sword"]}}`

**События:**

**`minecraft:bee_sword`** (строки 22,1043,1125,1129,1137):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"bee_sword"},"add":{"component_groups":["minecraft:bee_sword"]}}`

**`stop_bee_sword_event`** (строки 1050,1133):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"bee_sword"},"remove":{"component_groups":["minecraft:bee_sword"]},"add":{"component_groups":["minecraft:default_player"]}}`

**`bee_sword_flower`** (строки 24,1145):

- `$.randomize`: альтернативы, веса `[1,1,1,1,1,1,1,1,1,1,1,1]`, сумма 12:
  - ветвь 0, weight `1`; условная доля 1/12 (8.33333%):
    - `$.randomize[0]` — поля действия: `{"run_command":{"command":["execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 0"]}}`
  - ветвь 1, weight `1`; условная доля 1/12 (8.33333%):
    - `$.randomize[1]` — поля действия: `{"run_command":{"command":["execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 1"]}}`
  - ветвь 2, weight `1`; условная доля 1/12 (8.33333%):
    - `$.randomize[2]` — поля действия: `{"run_command":{"command":["execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 2"]}}`
  - ветвь 3, weight `1`; условная доля 1/12 (8.33333%):
    - `$.randomize[3]` — поля действия: `{"run_command":{"command":["execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 3"]}}`
  - ветвь 4, weight `1`; условная доля 1/12 (8.33333%):
    - `$.randomize[4]` — поля действия: `{"run_command":{"command":["execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 4"]}}`
  - ветвь 5, weight `1`; условная доля 1/12 (8.33333%):
    - `$.randomize[5]` — поля действия: `{"run_command":{"command":["execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 5"]}}`
  - ветвь 6, weight `1`; условная доля 1/12 (8.33333%):
    - `$.randomize[6]` — поля действия: `{"run_command":{"command":["execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 6"]}}`
  - ветвь 7, weight `1`; условная доля 1/12 (8.33333%):
    - `$.randomize[7]` — поля действия: `{"run_command":{"command":["execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 7"]}}`
  - ветвь 8, weight `1`; условная доля 1/12 (8.33333%):
    - `$.randomize[8]` — поля действия: `{"run_command":{"command":["execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 8"]}}`
  - ветвь 9, weight `1`; условная доля 1/12 (8.33333%):
    - `$.randomize[9]` — поля действия: `{"run_command":{"command":["execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 9"]}}`
  - ветвь 10, weight `1`; условная доля 1/12 (8.33333%):
    - `$.randomize[10]` — поля действия: `{"run_command":{"command":["execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 10"]}}`
  - ветвь 11, weight `1`; условная доля 1/12 (8.33333%):
    - `$.randomize[11]` — поля действия: `{"run_command":{"command":["execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ yellow_flower 0"]}}`


<a id="sword-ice_sword"></a>
### 02. Ice Sword — `effect:ice_sword`

**Параметры предмета:** блеск foil: да; левая рука: нет; should_despawn: не указан; digger: web 15, bamboo 10.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** 8.5. **Прочность:** 500. **Кулдаун:** 5 с. **Расход применения:** 6. **Зачарование:** есть: value 9, слот sword.
**Ремонт, единиц за материал:** такой же меч: 500; ice: 55.
**Способности:** Вода под ногами замерзает и восстанавливается; 30% на снежок при weapon-событии. Применение: ловушка вокруг подходящих сущностей во всём радиусе 8, включая вплотную, около 8 секунд, расход 6; по решению пользователя владельца не выбирать целью, прочие исключения типов и формы сохранять; горящий игрок превращает меч в воду. Отдельно: выброшенный горящий меч уничтожается, в биоме без тега nether может создать воду; ветка игрока ранее проверялась только для меча в руке, а не в остальных слотах инвентаря.
**Получение:** сундуки иглу — 2–8 выборов, вес меча 1/64 на выбор; снежные деревни — 3–8 выборов, вес 4/57 на выбор при допущении неуказанного веса 1. Это не шанс на весь сундук.
**Пулы добычи:** иглу — 2–8 выборов, 1/64; снежная деревня — 3–8, 4/57*. Доли — вес записи на один выбор, не шанс всего сундука или любой рыбалки. *Сумма с допущением неуказанного веса 1.
**Условная модель износа weapon-события:** 1: 1.

#### Формы ледяных ловушек

Согласованный радиус выбора цели — **8 блоков**, срок льда около 8 секунд; исходную воду восстанавливать. Старые записи также фиксируют разные формы для разных сущностей; число в таблице — размер геометрической рамки, а не гарантия изменения всех клеток. Создавать лёд вместо воздуха, не перезаписывать чужие блоки; при восстановлении не удалять чужой лёд.

| Цель | Внешняя рамка | Внутренняя полость / особенность |
|---|---|---|
| Общая сущность и игрок | 3 × 4 × 3 | заполнение рамки |
| Эндермен | 3 × 5 × 3 | заполнение рамки |
| Большой слизень | 5 × 5 × 5 | убрать внутренний куб 3 × 3 × 3 |
| Средний и маленький слизень | 3 × 3 × 3 | очистить центральную клетку |
| Гаст | 9 × 8 × 9 | убрать внутреннюю область 7 × 6 × 7 |
| Лошадь | 3 × 3 × 3 | очистить центральную клетку |
| Древний страж | 5 × 5 × 5 | заполнение рамки |
| Мелкие снаряды и silverfish | 1 клетка | только подходящие записанные типы |
| Другие перечисленные небольшие сущности | 3 × 3 × 3 | точные типы и исключения приведены в 40 операциях ниже |

Для рамки 3 × 3 × 3 в записи отдельно перечислены: spider, cave_spider, tnt, vex, chicken, pig, wolf, cat, endermite, rabbit, parrot, phantom, shulker, guardian, ocelot, turtle, fox, squid и bat; размеры относятся к рамке, а не к реальному объёму льда. Одна клетка записана для silverfish, small_fireball, fireball, arrow, lingering_potion, dragon_fireball и thrown_trident. Общий селектор имеет отдельный перечень исключений (в том числе item, xp_orb, fish и effect99_entities); его не превращать в безусловное «все сущности». Геометрия, смещения и полный список исключений каждой из 40 команд приведены ниже в этом пункте.

В сохранённых командах были разные минимальные расстояния 2 и 3 и пересекающиеся выборки сущностей и игроков. Изменение максимального радиуса на 8 — решение пользователя, а не утверждение, что в старых командах стояло 8. Временный лёд имел четыре видимые стадии с записанным интервалом блока `[2,2]`; в испытании переходы и исчезновение заняли около 8 секунд. Вода под ногами: квадрат 5 × 5 на y−1 и четыре осевые точки на расстоянии 3.

**Выброшенный предмет:** Выброшенный Ice в огне уничтожается и в биоме без тега nether пытается создать воду; в nether вода не создаётся. Это отдельное условие от согласованного превращения меча в руке при горении игрока.

**Вход weapon-события:** при попадании с уроном, ударе без урона и ударе по блоку. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Приёмка после разрешения на разработку:** радиус 8, около 8 с, горящий игрок и восстановление воды; не затирать чужие блоки или лёд.

**Значок 2.8.8:** `Swords_R/textures/items/ice_sword.png` (ключ атласа `ice_sword`; файл сохранён в наборе ресурсов 2.8.8).

#### Точные 40 операций исходной формы

В таблице приведены selector, смещения и порядок 2.8.8. `r=12` — исходная запись, для ремейка согласован максимальный радиус **8**; сохранять согласованные формы и исключения типов. По решению пользователя в ремейке минимальные расстояния `rm=2` и `rm=3` не применять: выбирать подходящие цели во всём радиусе 8, исключая владельца; остальные исключения типов и формы сохранить. В общем исходном селекторе стоит `rm=2`, и он не исключает игроков; отдельный селектор `type=player` имеет `rm=3`. Поэтому `rm=3` не является общим минимальным расстоянием для игрока: обычный игрок может подходить и под общий селектор от 2 блоков. При применении способностей учитывать пересечение селекторов; сам селектор не доказывает успешное исполнение команды. По решению пользователя старый лёд других источников не удалять. Размер рамки не равен количеству реально изменённых клеток.

| № | Селектор | Execute-смещение | Fill от → до | Позиции рамки | Материал и фильтр |
|---:|---|---|---|---:|---|
| 1 | `@e[type=!enderman,type=!horse,type=!slime,type=!silverfish,type=!spider,type=!cave_spider,type=!tnt,type=!vex,type=!chicken,type=!pig,type=!wolf,type=!cat,type=!item,type=!xp_orb,type=!xp_bottle,type=!egg,type=!snowball,type=!fireball,type=!small_fireball,type=!eye_of_ender_signal,type=!ender_pearl,type=!fishing_hook,type=!falling_block,type=!lightning_bolt,type=!lingering_potion,type=!dragon_fireball,type=!ender_dragon,type=!endermite,type=!arrow,type=!thrown_trident,type=!leash_knot,type=!bat,type=!rabbit,type=!parrot,type=!ghast,type=!shulker,type=!elder_guardian,type=!guardian,type=!turtle,type=!fox,type=!squid,type=!ocelot,type=!phantom,type=!area_effect_cloud,family=!fish,family=!effect99_entities,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~2 ~-1` | 36 | `effect99:fake_ice 0 replace air 0` |
| 2 | `@e[type=enderman,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~3 ~-1` | 45 | `effect99:fake_ice 0 replace air 0` |
| 3 | `@e[family=slime_large,rm=2,r=12]` | `~ ~ ~` | `~2 ~-1 ~2` → `~-2 ~3 ~-2` | 125 | `effect99:fake_ice 0 replace air 0` |
| 4 | `@e[family=slime_large,rm=2,r=12]` | `~ ~1 ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `air 0 replace effect99:fake_ice` |
| 5 | `@e[family=slime_medium,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `effect99:fake_ice 0 replace air 0` |
| 6 | `@e[family=slime_medium,rm=2,r=12]` | `~ ~ ~` | `~ ~ ~` → `~ ~ ~` | 1 | `air 0 replace effect99:fake_ice` |
| 7 | `@e[family=slime_small,rm=2,r=12]` | `~ ~ ~` | `~1 ~1 ~1` → `~-1 ~-1 ~-1` | 27 | `effect99:fake_ice 0 replace air 0` |
| 8 | `@e[family=slime_small,rm=2,r=12]` | `~ ~ ~` | `~ ~ ~` → `~ ~ ~` | 1 | `air 0 replace effect99:fake_ice` |
| 9 | `@e[type=silverfish,rm=2,r=12]` | `~ ~ ~` | `~ ~ ~` → `~ ~ ~` | 1 | `effect99:fake_ice 0 replace air 0` |
| 10 | `@e[type=spider,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `effect99:fake_ice 0 replace air 0` |
| 11 | `@e[type=cave_spider,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `effect99:fake_ice 0 replace air 0` |
| 12 | `@e[type=tnt,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `effect99:fake_ice 0 replace air 0` |
| 13 | `@e[type=vex,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `effect99:fake_ice 0 replace air 0` |
| 14 | `@e[type=chicken,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `effect99:fake_ice 0 replace air 0` |
| 15 | `@e[type=pig,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `effect99:fake_ice 0 replace air 0` |
| 16 | `@e[type=wolf,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `effect99:fake_ice 0 replace air 0` |
| 17 | `@e[type=cat,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `effect99:fake_ice 0 replace air 0` |
| 18 | `@e[type=small_fireball,rm=2,r=12]` | `~ ~ ~` | `~ ~ ~` → `~ ~ ~` | 1 | `effect99:fake_ice 0 replace air 0` |
| 19 | `@e[type=fireball,rm=2,r=12]` | `~ ~ ~` | `~ ~ ~` → `~ ~ ~` | 1 | `effect99:fake_ice 0 replace air 0` |
| 20 | `@e[type=arrow,rm=2,r=12]` | `~ ~ ~` | `~ ~ ~` → `~ ~ ~` | 1 | `effect99:fake_ice 0 replace air 0` |
| 21 | `@e[type=lingering_potion,rm=2,r=12]` | `~ ~ ~` | `~ ~ ~` → `~ ~ ~` | 1 | `effect99:fake_ice 0 replace air 0` |
| 22 | `@e[type=dragon_fireball,rm=2,r=12]` | `~ ~ ~` | `~ ~ ~` → `~ ~ ~` | 1 | `effect99:fake_ice 0 replace air 0` |
| 23 | `@e[type=thrown_trident,rm=2,r=12]` | `~ ~ ~` | `~ ~ ~` → `~ ~ ~` | 1 | `effect99:fake_ice 0 replace air 0` |
| 24 | `@e[type=endermite,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `effect99:fake_ice 0 replace air 0` |
| 25 | `@e[type=rabbit,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `effect99:fake_ice 0 replace air 0` |
| 26 | `@e[type=parrot,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `effect99:fake_ice 0 replace air 0` |
| 27 | `@e[type=phantom,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `effect99:fake_ice 0 replace air 0` |
| 28 | `@e[type=shulker,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `effect99:fake_ice 0 replace air 0` |
| 29 | `@e[type=guardian,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `effect99:fake_ice 0 replace air 0` |
| 30 | `@e[type=ocelot,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `effect99:fake_ice 0 replace air 0` |
| 31 | `@e[type=turtle,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `effect99:fake_ice 0 replace air 0` |
| 32 | `@e[type=fox,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `effect99:fake_ice 0 replace air 0` |
| 33 | `@e[type=squid,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `effect99:fake_ice 0 replace air 0` |
| 34 | `@e[type=elder_guardian,rm=2,r=12]` | `~ ~ ~` | `~2 ~-1 ~2` → `~-2 ~3 ~-2` | 125 | `effect99:fake_ice 0 replace air 0` |
| 35 | `@e[type=bat,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `effect99:fake_ice 0 replace air 0` |
| 36 | `@e[type=ghast,rm=2,r=12]` | `~ ~ ~` | `~4 ~-3 ~4` → `~-4 ~4 ~-4` | 648 | `effect99:fake_ice 0 replace air 0` |
| 37 | `@e[type=ghast,rm=2,r=12]` | `~ ~ ~` | `~3 ~-2 ~3` → `~-3 ~3 ~-3` | 294 | `air 0 replace effect99:fake_ice` |
| 38 | `@e[type=horse,rm=2,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~1 ~-1` | 27 | `effect99:fake_ice 0 replace air 0` |
| 39 | `@e[type=horse,rm=2,r=12]` | `~ ~ ~` | `~ ~ ~` → `~ ~ ~` | 1 | `air 0 replace effect99:fake_ice 0` |
| 40 | `@e[type=player,rm=3,r=12]` | `~ ~ ~` | `~1 ~-1 ~1` → `~-1 ~2 ~-1` | 36 | `effect99:fake_ice 0 replace air 0` |

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
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
    },
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:cooldown": {
      "category": "ice_sword",
      "duration": 5
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

#### Записанные группы и события владельца 2.8.8

Это относящиеся к предмету поля игрока из сохранённого реестра, а не утверждение об их выполнении; если старый код расходится с решениями выше (например восстановление настроек мира или блоков), выполнять решение, а не переносить старую ошибку. Пустое или отсутствующее поле не подменять предположением.

**Группы:**

- `minecraft:ice_sword` (строки 302,756,1920,1924,1956): `{"minecraft:type_family":{"family":["player","ice_sword"]}}`

**События:**

**`minecraft:ice_sword`** (строки 302,756,1920,1924,1956):

- `$.sequence`: 4 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"ice_sword"},"add":{"component_groups":["minecraft:ice_sword"]}}`
  - `$.sequence[1]` — поля действия: `{"filters":{"all_of":[{"test":"in_lava"},{"test":"has_biome_tag","operator":"!=","value":"nether"}]},"run_command":{"command":["playsound random.fizz @a[r=10] ~ ~ ~","setblock ~ ~ ~ flowing_water","replaceitem entity @s slot.weapon.mainhand 0 air 1 0","particle minecraft:cauldron_explosion_emitter ~ ~ ~"]}}`
  - `$.sequence[2]` — поля действия: `{"filters":{"all_of":[{"test":"in_lava"},{"test":"has_biome_tag","value":"nether"}]},"run_command":{"command":["playsound random.fizz @a[r=10] ~ ~ ~","replaceitem entity @s slot.weapon.mainhand 0 air 1 0","particle minecraft:cauldron_explosion_emitter ~ ~ ~"]}}`
  - `$.sequence[3]` — поля действия: `{"run_command":{"command":["fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 effect99:fake_ice 0 replace water","fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 effect99:fake_ice 0 replace flowing_water","fill ~3 ~-1 ~ ~3 ~-1 ~ effect99:fake_ice 0 replace water","fill ~3 ~-1 ~ ~3 ~-1 ~ effect99:fake_ice 0 replace flowing_water","fill ~ ~-1 ~3 ~ ~-1 ~3 effect99:fake_ice 0 replace water","fill ~ ~-1 ~3 ~ ~-1 ~3 effect99:fake_ice 0 replace flowing_water","fill ~-3 ~-1 ~ ~-3 ~-1 ~ effect99:fake_ice 0 replace water","fill ~-3 ~-1 ~ ~-3 ~-1 ~ effect99:fake_ice 0 replace flowing_water","fill ~ ~-1 ~-3 ~ ~-1 ~-3 effect99:fake_ice 0 replace water","fill ~ ~-1 ~-3 ~ ~-1 ~-3 effect99:fake_ice 0 replace flowing_water","execute @e[r=64,type=!player] ~ ~ ~ detect ~ ~ ~ effect99:fake_ice 0 tp @s ~ ~ ~ ~1"]}}`

**`stop_ice_sword_event`** (строки 763,1952):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"ice_sword"},"remove":{"component_groups":["minecraft:ice_sword"]},"add":{"component_groups":["minecraft:default_player"]}}`


<a id="sword-nether_star_sword"></a>
### 03. Nether Star Sword — `effect:nether_star_sword`

**Параметры предмета:** блеск foil: да; левая рука: нет; should_despawn: false; digger: web 15, bamboo 10.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** 7. **Прочность:** 3256. **Кулдаун:** не указан. **Расход применения:** не указан. **Зачарование:** есть: value 9, слот sword.
**Ремонт, единиц за материал:** такой же меч: 3256; nether star: 3000.
**Способности:** При weapon-событии меч отдельно выпускает снаряд и вызывает одну звезду с весом 80 или две с весом 20; базовый impact урона снаряда 6; отдельная условная группа задаёт impact −1 и power 5 вместо базовой конфигурации, их не складывать. Независимый выбор 0,01% вызывает мощный взрыв вместо записанного износа этого шага. Выброшенный в огонь меч вызывает взрыв power 8, max resistance 4, без огня; по решению пользователя затронутый бедрок разрушается и выпадает как блок.
**Получение:** Алмазный меч + звезда Незера. Убийство Wither этим мечом: Wither Sword 13%.
**Рецепт:** minecraft:nether_star + minecraft:diamond_sword.
**Условная модель износа weapon-события:** 0: 1/10000, 1: 9999/10000.

#### Падающие звёзды

В `weapon` самого предмета последовательно записаны выстрел `entity:nether_star_projectile`, отдельный выбор вызова одной `entity:nether_star` весом 80 или двух весом 20, затем независимый выбор редкого взрыва весом 1 из 10000 вместо записанного износа данного шага. Вызов звёзд не поставлен в зависимость от попадания выпущенного снаряда. В исходном пространстве падения координаты заданы локально относительно направления взгляда: `^ ^20 ^-6` и дополнительно `^ ^18 ^-6` для второй звезды. У выпущенного снаряда при условии `has_equipment` в группе указан отдельный `on_hit`, создающий `entity:objective`; эту условную ветвь не приравнивать к базовому impact 6. Helper цели выбирает ближайшую подходящую сущность в радиусе 8 с набором исключений, а не гарантированно ту, в которую попал снаряд; каждая вызванная звезда ищет цели family objective в радиусе 28 и имеет shooter с тем же ID снаряда. Время жизни в исходных таймерах: у звезды 0,5 с, у objective 1 с. Группа игрока отменяет урон от сущности family `nether_star_projectile`. По этим данным нельзя гарантировать появление, привязку или попадание каждой звезды.

**Выброшенный предмет:** при огне взрыв power 8, max resistance 4, fire false и уничтожение предмета; затронутый взрывом бедрок разрушается и выпадает как блок. Это решение для ремейка, не подтверждение выпадения в оригинале.

**Вход weapon-события:** при попадании с уроном, ударе без урона и ударе по блоку. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Значок 2.8.8:** `Swords_R/textures/items/nether_star_sword.png` (ключ атласа `nether_star_sword`; файл сохранён в наборе ресурсов 2.8.8).

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
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

#### Записанные группы и события владельца 2.8.8

Это относящиеся к предмету поля игрока из сохранённого реестра, а не утверждение об их выполнении; если старый код расходится с решениями выше (например восстановление настроек мира или блоков), выполнять решение, а не переносить старую ошибку. Пустое или отсутствующее поле не подменять предположением.

**Группы:**

- `minecraft:nether_star_sword` (строки 28,1029,1161,1165,1173): `{"minecraft:damage_sensor":{"triggers":{"on_damage":{"filters":{"all_of":[{"test":"is_family","subject":"other","value":"nether_star_projectile"}]}},"deals_damage":false}},"minecraft:type_family":{"family":["player","nether_star_sword"]}}`

**События:**

**`minecraft:nether_star_sword`** (строки 28,1029,1161,1165,1173):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"nether_star_sword"},"add":{"component_groups":["minecraft:nether_star_sword"]}}`

**`stop_nether_star_sword_event`** (строки 1036,1169):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"nether_star_sword"},"remove":{"component_groups":["minecraft:nether_star_sword"]},"add":{"component_groups":["minecraft:default_player"]}}`


<a id="sword-blaze_sword"></a>
### 04. Blaze Sword — `effect:blaze_sword`

**Параметры предмета:** блеск foil: нет; левая рука: нет; should_despawn: не указан; digger: web 15, bamboo 10.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** 6. **Прочность:** 2300. **Кулдаун:** 20 с. **Расход применения:** 10. **Зачарование:** есть: value 9, слот sword.
**Ремонт, единиц за материал:** такой же меч: 2300.
**Способности:** Защита от огня и тления; вода/дождь причиняют drowning-урон 1 за условный тик; по решению пользователя обычные малые огненные шары в радиусе 7 обрабатывать, если источник неизвестен или является враждебным мобом; при включённом PvP добавляются снаряды других игроков; собственные снаряды владельца не обрабатывать независимо от PvP. По решению пользователя менять движение по параметрам оригинала power 0, inertia 0, gravity 0,06, без гарантии непроницаемого барьера. Отдельные fake_fireball и большие fireball не включать; внешний вид с огненными стержнями. Применение: левитация 7 секунд, медленное падение 10 секунд, четыре снаряда, расход 10; кулдаун 20 секунд. Weapon-событие: малый шар 14%, большой 1%.
**Получение:** Blaze, убитый снежным големом: базовый шанс 2,5%, параметр Looting 0,02; его применимость к убийству големом не проверена.
**Условная модель износа weapon-события:** 1: 3/20, 2: 17/20.

**Снаряды и завершение навыка:** после запуска записан таймер 6 с, затем четыре отдельных `spawn_entity` fake_fireball с ожиданием 0–1 с и таймер остановки 2 с. Fake fireball: power 1,3, gravity 0,02, impact 5, поджигание и удаление при попадании. Это не те же `minecraft:small_fireball` и `minecraft:fireball`, что выбираются weapon-событием. При смене предмета до залпа отменять ожидаемые выстрелы и снимать levitation и slow falling: в опытах оригинала 2.8.8 на Bedrock 1.20.50 снятие примерно через 1 и 4 с после запуска прервало оба эффекта; после снятия снаряды не наблюдались, тогда как в контрольном запуске без снятия наблюдались четыре fake_fireball. Это подтверждает создание снарядов в контроле, но не их попадания. Уже созданные снаряды при смене не удалять: исходное stop-событие снимает группу создания, но не содержит команды удаления существующих снарядов; отдельно в игре этот случай не испытан. Другая записанная ветвь получения выбирает структуру с весом 5/1000, но локальная структура `blaze_sword` и прямой вызов события не найдены; не складывать её с пулом голема. [Сохранённый разбор](manual-companion-projectile-swords.md#blaze-sword).

**Blaze:** применение назначает levitation I на 7 с и slow falling IV на 10 с. Цепочка навыка записывает таймер `[6,6]` секунд, затем четыре отдельных spawn-свойства fake_fireball и таймер остановки `[2,2]` секунды; не обещать четыре попадания. Отдельный визуально-звуковой randomize для состояния навыка имеет шесть ветвей по 5 и пустую весом 95: при стандартной нормализации каждая ветвь 4%, пустая 76%, а не 5%/95%. При смене меча до залпа отменять ожидаемые выстрелы и снимать levitation и slow falling; это наблюдалось при смене примерно через 1 и 4 с после запуска на оригинале 2.8.8/1.20.50.

**Вход weapon-события:** при попадании с уроном, ударе без урона и ударе по блоку. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Looting:** при реально переданных уровнях 0/1/2/3 условные шансы записанной ветви — 2,5%, 4,5%, 6,5%, 8,5%. Множитель 0,02 добавляет 2 п.п. за уровень; не доказывает подключение таблицы или успешность события. Для убийства снежным големом ненулевой эффективный уровень Looting не доказан.

**Модель, анимация и звук:** огненные стержни и аура вокруг владельца.

**Значок 2.8.8:** `Swords_R/textures/items/blaze_sword.png` (ключ атласа `blaze_sword`; файл сохранён в наборе ресурсов 2.8.8).

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
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
    },
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:cooldown": {
      "category": "blaze_sword",
      "duration": 20
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

#### Записанные группы и события владельца 2.8.8

Это относящиеся к предмету поля игрока из сохранённого реестра, а не утверждение об их выполнении; если старый код расходится с решениями выше (например восстановление настроек мира или блоков), выполнять решение, а не переносить старую ошибку. Пустое или отсутствующее поле не подменять предположением.

**Группы:**

- `minecraft:blaze_sword` (строки 355,644,2163,2167,2209,2238): `{"minecraft:damage_sensor":{"triggers":{"on_damage":{"filters":{"any_of":[{"test":"has_damage","subject":"self","value":"fire"},{"test":"has_damage","subject":"self","value":"fire_tick"}]}},"deals_damage":false}},"minecraft:hurt_on_condition":{"damage_conditions":[{"filters":{"test":"in_water_or_rain"},"cause":"drowning","damage_per_tick":1}]},"minecraft:type_family":{"family":["player","blaze_sword"]},"minecraft:timer":{"time":[1,1],"looping":true,"time_down_event":{"event":"blaze_sword_effects","target":"self"}}}`
- `blaze_sword_skill` (строки 375,376,378,2192,2245,2249): `{"minecraft:type_family":{"family":["player","blaze_sword","blaze_sword_skill"]},"minecraft:timer":{"time":[6,6],"looping":false,"time_down_event":{"event":"blaze_sword_skill","target":"self"}}}`

**События:**

**`minecraft:blaze_sword`** (строки 355,644,2163,2167,2209,2238):

- `$.sequence`: 3 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"blaze_sword"},"add":{"component_groups":["minecraft:blaze_sword"]},"run_command":{"command":["particle minecraft:mobflame_single ~ ~ ~","particle minecraft:mobflame_single ~ ~1 ~","particle minecraft:mobflame_single ~ ~1.5 ~","particle minecraft:mobflame_single ~0.4 ~ ~","particle minecraft:mobflame_single ~ ~1 ~0.4","particle minecraft:mobflame_single ~-0.4 ~1.5 ~","particle minecraft:mobflame_single ~ ~ ~-0.4","particle minecraft:mobflame_single ~0.3 ~1 ~0.3","particle minecraft:mobflame_single ~-0.3 ~1.5 ~-0.3","particle minecraft:mobflame_single ~0.3 ~ ~-0.3","particle minecraft:mobflame_single ~-0.3 ~1 ~0.3","particle minecraft:example_linearcurve ~ ~1 ~","playsound random.fizz @a[r=16]"]}}`
  - `$.sequence[1]` — поля действия: `{"run_command":{"command":["event entity @e[family=shot_by_the_blaze,r=7] minecraft:inertia_disable","fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace air","fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace effect99:lightblock2"]}}`
  - `$.sequence[2]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"blaze_sword_skill"}}`
  - `$.sequence[2].randomize`: альтернативы, веса `[5,5,5,5,5,5,95]`, сумма 125:
    - ветвь 0, weight `5`; условная доля 1/25 (4%):
      - `$.sequence[2].randomize[0]` — поля действия: `{"run_command":{"command":["particle minecraft:mobflame_single ~ ~0.2 ~"]}}`
    - ветвь 1, weight `5`; условная доля 1/25 (4%):
      - `$.sequence[2].randomize[1]` — поля действия: `{"run_command":{"command":["particle minecraft:mobflame_single ~0.3 ~0.2 ~"]}}`
    - ветвь 2, weight `5`; условная доля 1/25 (4%):
      - `$.sequence[2].randomize[2]` — поля действия: `{"run_command":{"command":["particle minecraft:mobflame_single ~ ~0.2 ~0.3"]}}`
    - ветвь 3, weight `5`; условная доля 1/25 (4%):
      - `$.sequence[2].randomize[3]` — поля действия: `{"run_command":{"command":["particle minecraft:mobflame_single ~-0.3 ~0.2 ~"]}}`
    - ветвь 4, weight `5`; условная доля 1/25 (4%):
      - `$.sequence[2].randomize[4]` — поля действия: `{"run_command":{"command":["particle minecraft:mobflame_single ~ ~0.2 ~-0.3"]}}`
    - ветвь 5, weight `5`; условная доля 1/25 (4%):
      - `$.sequence[2].randomize[5]` — поля действия: `{"run_command":{"command":["playsound mob.blaze.breathe @a[r=12] ~ ~ ~ 0.5"]}}`
    - ветвь 6, weight `95`; условная доля 19/25 (76%):
      - пустое действие

**`stop_blaze_sword_event`** (строки 651,2205):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"blaze_sword"},"remove":{"component_groups":["minecraft:blaze_sword","shoot_small_fireball"]},"run_command":{"command":["particle minecraft:mobflame_single ~ ~ ~","particle minecraft:mobflame_single ~ ~1 ~","particle minecraft:mobflame_single ~ ~1.5 ~","particle minecraft:mobflame_single ~0.4 ~ ~","particle minecraft:mobflame_single ~ ~1 ~0.4","particle minecraft:mobflame_single ~-0.4 ~1.5 ~","particle minecraft:mobflame_single ~ ~ ~-0.4","particle minecraft:mobflame_single ~0.3 ~1 ~0.3","particle minecraft:mobflame_single ~-0.3 ~1.5 ~-0.3","particle minecraft:mobflame_single ~0.3 ~ ~-0.3","particle minecraft:mobflame_single ~-0.3 ~1 ~0.3","particle minecraft:example_linearcurve ~ ~1 ~","playsound random.fizz @a[r=16]","effect @s levitation 0 0 true","effect @s slow_falling 0 0 true"]},"add":{"component_groups":["minecraft:default_player"]}}`

**`stop_blaze_sword_skill`** (строки 417,2233):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"blaze_sword"},"remove":{"component_groups":["shoot_small_fireball"]},"add":{"component_groups":["minecraft:blaze_sword"]}}`

**`blaze_sword_skill_event`** (строки 2242):

- `$` — поля действия: `{"add":{"component_groups":["blaze_sword_skill"]}}`

**`blaze_sword_skill`** (строки 375,376,378,2192,2245,2249):

- `$` — поля действия: `{"add":{"component_groups":["shoot_small_fireball"]}}`

**`blaze_sword_effects`** (строки 372,2256):

- `$.randomize`: альтернативы, веса `[1,1,1,1,1,1]`, сумма 6:
  - ветвь 0, weight `1`; условная доля 1/6 (16.6667%):
    - `$.randomize[0]` — поля действия: `{"run_command":{"command":["particle minecraft:mobflame_single ~ ~0.2 ~"]}}`
  - ветвь 1, weight `1`; условная доля 1/6 (16.6667%):
    - `$.randomize[1]` — поля действия: `{"run_command":{"command":["particle minecraft:mobflame_single ~0.3 ~0.2 ~"]}}`
  - ветвь 2, weight `1`; условная доля 1/6 (16.6667%):
    - `$.randomize[2]` — поля действия: `{"run_command":{"command":["particle minecraft:mobflame_single ~ ~0.2 ~0.3"]}}`
  - ветвь 3, weight `1`; условная доля 1/6 (16.6667%):
    - `$.randomize[3]` — поля действия: `{"run_command":{"command":["particle minecraft:mobflame_single ~-0.3 ~0.2 ~"]}}`
  - ветвь 4, weight `1`; условная доля 1/6 (16.6667%):
    - `$.randomize[4]` — поля действия: `{"run_command":{"command":["particle minecraft:mobflame_single ~ ~0.2 ~-0.3"]}}`
  - ветвь 5, weight `1`; условная доля 1/6 (16.6667%):
    - `$.randomize[5]` — поля действия: `{"run_command":{"command":["playsound mob.blaze.breathe @a[r=12] ~ ~ ~ 0.5"]}}`


<a id="sword-slime_sword"></a>
### 05. Slime Sword — `effect:slime_sword`

**Параметры предмета:** блеск foil: нет; левая рука: нет; should_despawn: не указан; digger: web 15, bamboo 10.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** 6. **Прочность:** 675. **Кулдаун:** не указан. **Расход применения:** не указан. **Зачарование:** есть: value 9, слот sword.
**Ремонт, единиц за материал:** такой же меч: 675; slime: 48.
**Способности:** при удержании меча группа игрока блокирует урон от family `tamed_slime`; одноразовый таймер `[0,4;0,4]` с вызывает попытку посадить игрока на `entity:mountable_slime`. При удержании сбрасывается счётчик ближайшего слизня в радиусе 12, а при снятии выбирается ближайший в радиусе 32, что не гарантирует выбор своего слизня. По решению пользователя в ремейке слизня привязать к владельцу: после спешивания он защищает именно его и телепортируется именно к нему; снятие меча управляет только собственным слизнем, а не ближайшим чужим. По отдельному решению пользователя слизень не выбирает владельца целью и не задевает его своими эффектами, включая эффект при падении после спешивания и случай превращения владельца в волка; для других игроков отдельного нового правила не добавлять. По следующему решению пользователя защитный слизень не атакует и не наносит урон призванным помощникам любых игроков, включая эффект падения. Поведение, характеристики и жизненный цикл — в пункте [Ездовой слизень](#mob-mountable-slime); условия получения — [Slime King](#mob-slime-king).
**Получение:** при убийстве Slime King игроком выдавать меч с базовым шансом 4% и добавкой 2 процентных пункта за уровень Looting. По решению пользователя Slime King появляется только ночью; в исходном правиле указаны biome swamp и вес 10, но отдельной проверки ночи нет. В исходнике локальная привязка таблицы к боссу не найдена; в ремейке её необходимо явно обеспечить согласно описанию.
**Условная модель износа weapon-события:** 1: 1.

**Вход weapon-события:** только при попадании по сущности с уроном. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Looting:** при реально переданных уровнях 0/1/2/3 условные шансы записанной ветви — 4%, 6%, 8%, 10%. Множитель 0,02 добавляет 2 п.п. за уровень; не доказывает подключение таблицы или успешность события.

**Связанный моб:** [Slime King](#mob-slime-king).

**Значок 2.8.8:** `Swords_R/textures/items/slime_sword.png` (ключ атласа `slime_sword`; файл сохранён в наборе ресурсов 2.8.8).

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
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

#### Записанные группы и события владельца 2.8.8

Это относящиеся к предмету поля игрока из сохранённого реестра, а не утверждение об их выполнении; если старый код расходится с решениями выше (например восстановление настроек мира или блоков), выполнять решение, а не переносить старую ошибку. Пустое или отсутствующее поле не подменять предположением.

**Группы:**

- `minecraft:slime_sword` (строки 241,840,1669,1673,1684): `{"minecraft:type_family":{"family":["player","slime_sword"]},"minecraft:timer":{"time":[0.4,0.4],"looping":false,"time_down_event":{"event":"slime_sword_skills","target":"self"}},"minecraft:damage_sensor":{"triggers":{"on_damage":{"filters":{"all_of":[{"test":"is_family","subject":"other","value":"tamed_slime"}]}},"deals_damage":false}}}`

**События:**

**`minecraft:slime_sword`** (строки 241,840,1669,1673,1684):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"slime_sword"},"add":{"component_groups":["minecraft:slime_sword"]}}`
  - `$.sequence[1]` — поля действия: `{"run_command":{"command":["scoreboard players set @e[type=entity:mountable_slime,c=1,r=12] slime_despawn 0"]}}`

**`stop_slime_sword_event`** (строки 847,1680):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"slime_sword"},"remove":{"component_groups":["minecraft:slime_sword"]},"add":{"component_groups":["minecraft:default_player"]},"run_command":{"command":["ride @s stop_riding","event entity @e[type=entity:mountable_slime,c=1,r=32] despawn"]}}`

**`slime_sword_skills`** (строки 244,1690):

- `$` — поля действия: `{"run_command":{"command":["ride @s summon_ride entity:mountable_slime no_ride_change","scoreboard objectives add slime_despawn dummy"]}}`


<a id="sword-sea_sword"></a>
### 06. Sea Sword — `effect:sea_sword`

**Параметры предмета:** блеск foil: да; левая рука: нет; should_despawn: не указан; digger: web 15, bamboo 10.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** 7. **Прочность:** 1356. **Кулдаун:** не указан. **Расход применения:** не указан. **Зачарование:** есть: value 9, слот sword.
**Ремонт, единиц за материал:** такой же меч: 1356; heart of the sea: 482.
**Способности:** Облик русалки; дыхание водой, но не воздухом и не лавой; при нахождении в воде параметр underwater_movement 0,07 и Conduit Power I на 1 с, вне воды movement 0,06 и звуки рыбы. Дыхание: запас 2, inhale_time 3,75 (сохранённые значения полей; фактическое время проверить); hitbox 0,6×0,9. Прыжки как рыба на суше.
**Получение:** Сундуки с сокровищами.
**Пулы добычи:** клад — 5–12 выборов, 15/219. Доли — вес записи на один выбор, не шанс всего сундука или любой рыбалки.
**Условная модель износа weapon-события:** 1: 1.

**Вход weapon-события:** только при попадании по сущности с уроном. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Модель, анимация и звук:** хвост русалки от третьего лица; анимации плавания, неподвижной позы и удушья на суше.

**Значок 2.8.8:** `Swords_R/textures/items/sea_sword.png` (ключ атласа `sea_sword`; файл сохранён в наборе ресурсов 2.8.8).

**Входы и выходы:** при hand=Sea записано добавление группы с дыханием water=true, air=false, lava=false, total_supply 2, inhale_time 3,75, suffocate_time −1, без пузырьков. Водная группа задаёт underwater_movement 0,07 и conduit_power amplifier 0 на 1 с; вневодная — movement 0,06 и camerashake 0,01 на 1 с. Фильтры `in_water` в исходном тексте не содержат value. В опыте оригинала 2.8.8 на Bedrock 1.20.50 при погружении в воду Conduit Power I появлялся и обновлялся; при выходе на воздух или снятии меча под водой удалялся. В отдельном опыте пакеты атрибутов игрока показывали movement 0,06 на воздухе, underwater_movement 0,07 в воде и восстановление 0,1/0,02 после снятия. Реальные скорость перемещения и звук ботом не измерялись. Исходный stop явно снимает основную и водную группы, но не перечисляет вневодную: в ремейке восстановить прежнее состояние игрока при снятии и смене среды.

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
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

#### Записанные группы и события владельца 2.8.8

Это относящиеся к предмету поля игрока из сохранённого реестра, а не утверждение об их выполнении; если старый код расходится с решениями выше (например восстановление настроек мира или блоков), выполнять решение, а не переносить старую ошибку. Пустое или отсутствующее поле не подменять предположением.

**Группы:**

- `minecraft:sea_sword` (строки 262,812,1825,1834,1848): `{"minecraft:collision_box":{"width":0.6,"height":0.9},"minecraft:timer":{"time":[0.5,0.5],"looping":true,"time_down_event":{"event":"sea_sword_sound","target":"self"}},"minecraft:breathable":{"total_supply":2,"suffocate_time":-1,"inhale_time":3.75,"generates_bubbles":false,"breathes_water":true,"breathes_air":false,"breathes_lava":false},"minecraft:type_family":{"family":["player","sea_sword"]}}`
- `mermaid_movement_out_water` (строки 275,1829): `{"minecraft:movement":{"value":0.06}}`
- `mermaid_movement_in_water` (строки 278,1839,1848): `{"minecraft:underwater_movement":{"value":0.07}}`

**События:**

**`minecraft:sea_sword`** (строки 262,812,1825,1834,1848):

- `$.sequence`: 3 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"in_water","operator":"!="},"add":{"component_groups":["mermaid_movement_out_water"]},"run_command":{"command":["camerashake add @s 0.01 1 positional","effect @s conduit_power 0 0"]}}`
  - `$.sequence[1]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"sea_sword"},"add":{"component_groups":["minecraft:sea_sword"]},"run_command":{"command":["particle minecraft:example_bounce ~ ~ ~","playsound random.splash @a[r=12] ~ ~ ~ 0.5"]}}`
  - `$.sequence[2]` — поля действия: `{"filters":{"test":"in_water"},"add":{"component_groups":["mermaid_movement_in_water"]},"run_command":{"command":["effect @s conduit_power 1 0 true"]}}`

**`stop_sea_sword_event`** (строки 819,1844):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"sea_sword"},"remove":{"component_groups":["minecraft:sea_sword","mermaid_movement_in_water"]},"add":{"component_groups":["minecraft:default_player"]},"run_command":{"command":["particle minecraft:example_bounce ~ ~ ~","playsound random.splash @a[r=12] ~ ~ ~ 0.5","effect @s conduit_power 0 0"]}}`

**`sea_sword_sound`** (строки 268,1854):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"in_water","operator":"!="},"run_command":{"command":["playsound mob.fish.flop @a[r=12] ~ ~ ~ 1 0.6"]}}`


<a id="sword-clock_sword"></a>
### 07. Clock Sword — `effect:clock_sword`

**Параметры предмета:** блеск foil: да; левая рука: нет; should_despawn: не указан; digger: web 15, bamboo 10.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** 7. **Прочность:** 4800. **Кулдаун:** 30 с. **Расход применения:** 10. **Зачарование:** есть: value 9, слот sword.
**Ремонт, единиц за материал:** такой же меч: 4800; clock: 900; gold block: 780; gold ingot: 87.
**Способности:** Применение 5 секунд: randomtickspeed 100, отдельно +10 игровых тиков на срабатывание, скорость XI для подходящих неигровых сущностей, параметр движения игрока 1; расход 10, кулдаун 30 секунд. В конкретном серверном опыте за действие время продвинулось примерно на 1000 игровых тиков; не повреждать исходные настройки, учитывать других игроков.
**Получение:** Верстак: .GG/GCG/IG.; G золотой блок, C часы, I золотой слиток, точка пусто.
**Рецепт:** .GG / GCG / IG.; G=minecraft:gold_block, C=minecraft:clock, I=minecraft:gold_ingot. Схема взята с изображения; в старом JSON есть неопределённый символ X, регистрацию проверить.
**Условная модель износа weapon-события:** 1: 1.

**Вход weapon-события:** при попадании с уроном, ударе без урона и ударе по блоку. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Одновременно с Time:** каждая способность выполняет собственные исходные команды: Clock добавляет времени 10, Time — 30 на своё срабатывание; записи `randomtickspeed` 100 и 300 не складываются, действует последняя выполненная запись. В опыте двух игроков 2.8.8/1.20.50 при обоих активных наблюдалось 300, при снятии Time во время Clock — 100. Сохранять и восстанавливать настройки мира после завершения всех активных воздействий; не удалять эффекты других источников.

**Колодец:** каждая единица Clock даёт независимую попытку получить Time с вероятностью 2,5%; возможны несколько наград. Проверять настоящий ID и форму колодца; построенные копии допустимы.

**Значок 2.8.8:** `Swords_R/textures/items/clock_sword.png` (ключ атласа `clock_sword`; файл сохранён в наборе ресурсов 2.8.8).

**Записанные цели и остановка:** пока активна группа навыка, команды задают `randomtickspeed 100`, `time add 10`, `speed 1 10` всем `type=!player` и движение 1 выбранным `@a[family=default_player]`, а не только владельцу; фактическая область зависит от исполнения селекторов. Таймер навыка 5 с; при остановке оригинал писал `randomtickspeed 1` и снимал speed, не сохраняя прежние значения. В ремейке сохранять и восстанавливать исходные gamerule и эффекты других источников; учесть совместное действие Time и нескольких игроков.

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
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
    },
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:cooldown": {
      "category": "clock_sword",
      "duration": 30
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

#### Записанные группы и события владельца 2.8.8

Это относящиеся к предмету поля игрока из сохранённого реестра, а не утверждение об их выполнении; если старый код расходится с решениями выше (например восстановление настроек мира или блоков), выполнять решение, а не переносить старую ошибку. Пустое или отсутствующее поле не подменять предположением.

**Группы:**

- `minecraft:clock_sword` (строки 35,1015,1178,1182,1202): `{"minecraft:type_family":{"family":["player","clock_sword"]}}`
- `clock_sword_skill` (строки 38,42,1185,1210): `{"minecraft:timer":{"time":[5,5],"looping":true,"randomInterval":false,"time_down_event":{"event":"stop_clock_sword_event","target":"self"}},"minecraft:type_family":{"family":["player","clock_sword","clock_sword_skill"]}}`
- `clock_sword_movement` (строки 44,1186,1213,1214): `{"minecraft:movement":{"value":1}}`

**События:**

**`minecraft:clock_sword`** (строки 35,1015,1178,1182,1202):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"clock_sword"},"add":{"component_groups":["minecraft:clock_sword"]}}`
  - `$.sequence[1]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"clock_sword_skill"},"add":{"component_groups":["clock_sword_movement"]},"run_command":{"command":["gamerule randomtickspeed 100","effect @e[type=!player] speed 1 10 true","time add 10","event entity @a[family=default_player] clock_sword_movement"]}}`

**`stop_clock_sword_event`** (строки 40,1022,1198):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"clock_sword"},"remove":{"component_groups":["minecraft:clock_sword"]},"run_command":{"command":["gamerule randomtickspeed 1","effect @e[type=!player] speed 0 0","event entity @a[family=default_player] default_player"]},"add":{"component_groups":["minecraft:default_player"]}}`

**`clock_sword_skill_event`** (строки 1208):

- `$` — поля действия: `{"add":{"component_groups":["clock_sword_skill"]}}`

**`clock_sword_movement`** (строки 44,1186,1213,1214):

- `$` — поля действия: `{"add":{"component_groups":["clock_sword_movement"]}}`


<a id="sword-spider_sword"></a>
### 08. Spider Sword — `effect:spider_sword`

**Параметры предмета:** блеск foil: нет; левая рука: нет; should_despawn: не указан; digger: web 100, bamboo 10.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** 5. **Прочность:** 628. **Кулдаун:** 28 с. **Расход применения:** 8. **Зачарование:** есть: value 9, слот sword.
**Ремонт, единиц за материал:** такой же меч: 628; web: 128; spider eye: 48.
**Способности:** удержание создаёт `minecraft:spider` с событием `minecraft:spider_sword`; при прекращении снимаются группа игрока и группа навыка, вызывается stop_riding. Характеристики и лазание — в пункте [Ездовой паук](#mob-riding-spider). В weapon-событии выбор снаряда `entity:web` — 5/100. Применение активирует спавн этого же снаряда с wait 0/0, single_use false и таймером остановки 2 с; точное число снарядов за интервал из записи не следует. Расход 8, кулдаун 28 с.
**Получение:** Сундуки заброшенной шахты.
**Пулы добычи:** заброшенная шахта — 2–4 выбора, 3/86. Доли — вес записи на один выбор, не шанс всего сундука или любой рыбалки.
**Условная модель износа weapon-события:** 1: 1.

**Снаряд `entity:web`:** power 1,5, gravity 0,03, impact 1, knockback и удаление при попадании; collision 0,25×0,25, scale 0,5, звук pop и одна частица. Событие ставит web только вместо воздуха; вызвать попадание до удаления нельзя гарантировать одним выбором ветви.

**Вход weapon-события:** при попадании с уроном, ударе без урона и ударе по блоку. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Значок 2.8.8:** `Swords_R/textures/items/spider_sword.png` (ключ атласа `spider_sword`; файл сохранён в наборе ресурсов 2.8.8).

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
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
    },
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:cooldown": {
      "category": "spider_sword",
      "duration": 28
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

#### Записанные группы и события владельца 2.8.8

Это относящиеся к предмету поля игрока из сохранённого реестра, а не утверждение об их выполнении; если старый код расходится с решениями выше (например восстановление настроек мира или блоков), выполнять решение, а не переносить старую ошибку. Пустое или отсутствующее поле не подменять предположением.

**Группы:**

- `minecraft:spider_sword` (строки 216,868,1608,1612,1621,1632): `{"minecraft:type_family":{"family":["player","spider_sword"]}}`
- `spider_sword_skill` (строки 219,226,1621,1630,1631,1636,1639,1640): `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"single_use":false,"spawn_entity":"entity:web","num_to_spawn":1}],"minecraft:timer":{"time":[2,2],"looping":false,"time_down_event":{"event":"stop_spider_skill_event","target":"self"}},"minecraft:type_family":{"family":["player","spider_sword","spider_sword_skill"]}}`

**События:**

**`minecraft:spider_sword`** (строки 216,868,1608,1612,1621,1632):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"spider_sword"},"add":{"component_groups":["minecraft:spider_sword"]},"run_command":{"command":["ride @s summon_ride minecraft:spider no_ride_change minecraft:spider_sword","particle minecraft:example_linearcurve ~ ~ ~"]}}`

**`stop_spider_sword_event`** (строки 875,1617):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"spider_sword"},"remove":{"component_groups":["minecraft:spider_sword","spider_sword_skill"]},"add":{"component_groups":["minecraft:default_player"]},"run_command":{"command":["ride @s stop_riding"]}}`

**`spider_sword_skill`** (строки 219,226,1621,1630,1631,1636,1639,1640):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"spider_sword_skill"},"add":{"component_groups":["spider_sword_skill"]}}`


<a id="sword-ender_sword"></a>
### 09. Ender Sword — `effect:ender_sword`

**Параметры предмета:** блеск foil: да; левая рука: нет; should_despawn: не указан; digger: web 15, bamboo 10.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** 9. **Прочность:** 1256. **Кулдаун:** 2 с. **Расход применения:** 5. **Зачарование:** есть: value 9, слот sword.
**Ремонт, единиц за материал:** такой же меч: 1256; ender pearl: 28; ender eye: 32.
**Способности:** Защита от снарядов с телепортацией; при любом неснарядном уроне, включая урон окружающей среды, по решению пользователя делать попытку телепортации в радиусе до 16 с вероятностью 50%. Вода или дождь также причиняют отдельный урон и могут вызывать телепортацию. По решению пользователя реакцию на снаряд при одновременном нахождении в воде/под дождём сделать как у обычного эндермена целевой версии; проверить это пересечение сравнением при приёмке. Исходные фильтры допускают пересечение, но приоритет старого движка не установлен; отдельную 50%-ветвь для неснарядного урона этим выбором не отменять. По решению пользователя при совпадении водной и 50%-ветви выполнять не более одной телепортации на одно событие урона. Применение: случайно на 16–32 блока по описанию, расход 5, кулдаун 2 секунды. Исходная команда `spreadplayers ~ ~ 16 32 @s` сама по себе не доказывает минимальную дистанцию 16 от исходной позиции: первый числовой параметр задаёт расстояние между выбранными сущностями, а выбран только `@s`.
**Получение:** у эндермена в обычном мире записан выбор красной формы весом 20 из 100; группа красноглазого эндермена прямо указывает таблицу `loot_tables/entities/red_enderman.json`. При убийстве игроком в этой таблице шанс меча — 2,5% плюс 2 процентных пункта за уровень Looting. В ремейке явно связать эту таблицу с [красноглазым эндерменом](#mob-red-enderman); не приравнивать шанс к 2,5% для любого эндермена.
**Условная модель износа weapon-события:** 1: 1.

**Выброшенный предмет:** при огне вызывается событие удаления предмета; это не обычный despawn.

**Положение в основной руке:** первое лицо `{"position":[1,0.4,-3],"scale":[0.04,0.04,0.04]}`; третье лицо `{"position":[0.5,1.6,-0.8],"scale":[0.038,0.038,0.038]}`. Неуказанные поля не заменять нулями; фактический вид проверить на целевой версии.

**Вход weapon-события:** только при попадании по сущности с уроном. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Looting:** при реально переданных уровнях 0/1/2/3 условные шансы записанной ветви — 2,5%, 4,5%, 6,5%, 8,5%. Множитель 0,02 добавляет 2 п.п. за уровень; не доказывает подключение таблицы или успешность события.

**Значок 2.8.8:** `Swords_R/textures/items/ender_sword.png` (ключ атласа `ender_sword`; файл сохранён в наборе ресурсов 2.8.8).

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      }
    },
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:cooldown": {
      "category": "ender_sword",
      "duration": 2
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

#### Записанные группы и события владельца 2.8.8

Это относящиеся к предмету поля игрока из сохранённого реестра, а не утверждение об их выполнении; если старый код расходится с решениями выше (например восстановление настроек мира или блоков), выполнять решение, а не переносить старую ошибку. Пустое или отсутствующее поле не подменять предположением.

**Группы:**

- `minecraft:ender_sword` (строки 147,945,1416,1420,1432): `{"minecraft:damage_sensor":{"triggers":[{"on_damage":{"filters":{"all_of":[{"test":"has_damage","subject":"self","operator":"!=","value":"projectile"}]},"event":"ender_sword_skill"},"deals_damage":true},{"on_damage":{"filters":{"all_of":[{"test":"has_damage","subject":"self","value":"projectile"}]},"event":"ender_sword_tp"},"deals_damage":false},{"on_damage":{"filters":{"all_of":[{"test":"in_water_or_rain"}]},"event":"ender_sword_tp"},"deals_damage":true}]},"minecraft:hurt_on_condition":{"damage_conditions":[{"filters":{"test":"in_water_or_rain"},"cause":"drowning","damage_per_tick":1}]},"minecraft:type_family":{"family":["player","ender_sword"]},"minecraft:timer":{"time":[6,18],"looping":true,"randomInterval":true,"time_down_event":{"event":"ender_sword_sound","target":"self"}}}`

**События:**

**`minecraft:ender_sword`** (строки 147,945,1416,1420,1432):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"ender_sword"},"add":{"component_groups":["minecraft:ender_sword"]},"run_command":{"command":["playsound mob.endermen.portal @a[r=8] ~ ~ ~"]}}`
  - `$.sequence[1]` — поля действия: `{"run_command":{"command":["particle minecraft:end_chest ~ ~0.6 ~"]}}`

**`stop_ender_sword_event`** (строки 952,1428):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"ender_sword"},"remove":{"component_groups":["minecraft:ender_sword"]},"add":{"component_groups":["minecraft:default_player"]}}`

**`ender_sword_sound`** (строки 181,1437):

- `$.randomize`: альтернативы, веса `[1,1,1]`, сумма 3:
  - ветвь 0, weight `1`; условная доля 1/3 (33.3333%):
    - `$.randomize[0]` — поля действия: `{"run_command":{"command":["playsound mob.endermen.scream @a[r=8] ~ ~ ~"]}}`
  - ветвь 1, weight `1`; условная доля 1/3 (33.3333%):
    - `$.randomize[1]` — поля действия: `{"run_command":{"command":["playsound mob.endermen.idle @a[r=8] ~ ~ ~"]}}`
  - ветвь 2, weight `1`; условная доля 1/3 (33.3333%):
    - `$.randomize[2]` — поля действия: `{"run_command":{"command":["playsound mob.endermen.stare @a[r=8] ~ ~ ~"]}}`

**`ender_sword_tp`** (строки 158,164,1444):

- `$` — поля действия: `{"run_command":{"command":["spreadplayers ~ ~ 0 16 @s","playsound mob.endermen.portal @a[r=17]"]}}`

**`ender_sword_skill`** (строки 152,1446):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"run_command":{"command":["playsound mob.endermen.hit @a[r=8] ~ ~ ~"]}}`
  - `$.sequence[1].randomize`: альтернативы, веса `[50,50]`, сумма 100:
    - ветвь 0, weight `50`; условная доля 1/2 (50%):
      - пустое действие
    - ветвь 1, weight `50`; условная доля 1/2 (50%):
      - `$.sequence[1].randomize[1]` — поля действия: `{"run_command":{"command":["spreadplayers ~ ~ 0 16 @s","playsound mob.endermen.portal @a[r=17]"]}}`


<a id="sword-coal_sword"></a>
### 10. Coal Sword — `effect:coal_sword`

**Параметры предмета:** блеск foil: нет; левая рука: нет; should_despawn: не указан; digger: web 15, bamboo 10.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** 4. **Прочность:** 121. **Кулдаун:** не указан. **Расход применения:** не указан. **Зачарование:** есть: value 9, слот sword.
**Ремонт, единиц за материал:** такой же меч: 121; coal: 58; stick: 2.
**Способности:** Меч можно использовать как топливо обычной печи: одного Coal Sword хватает на 36 плавок, около 360 секунд (6 минут, 7200 игровых тиков; записано fuel duration 360). В испытании оригинала 2.8.8 на Bedrock 1.20.50 печь с 64 железными рудами получила один меч и выдала 36 железных слитков; после 7200 тиков ещё горела на снимке, к 7210-му погасла, а 28 руд осталось. Контрольный уголь в тех же условиях дал 8 слитков, палка не успела завершить одну плавку. Для ремейка задать длительность топлива 360 секунд; работу на целевой версии проверить при приёмке.
**Получение:** Два угольных блока над палкой; также бонусный сундук, пул с весом 1 из 5.
**Пулы добычи:** бонусный сундук — 1 выбор, 1/5. Доли — вес записи на один выбор, не шанс всего сундука или любой рыбалки.
**Рецепт:** 2 / 2 / 1; 2=minecraft:coal_block, 1=minecraft:stick.
**Условная модель износа weapon-события:** 1: 1.

**Вход weapon-события:** только при попадании по сущности с уроном. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Значок 2.8.8:** `Swords_R/textures/items/coal_sword.png` (ключ атласа `coal_sword`; файл сохранён в наборе ресурсов 2.8.8).

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
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

<a id="sword-shulker_sword"></a>
### 11. Shulker Sword — `effect:shulker_sword`

**Параметры предмета:** блеск foil: нет; левая рука: нет; should_despawn: не указан; digger: web 15, bamboo 10.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** 6. **Прочность:** 2609. **Кулдаун:** 8 с. **Расход применения:** 8. **Зачарование:** есть: value 9, слот sword.
**Ремонт, единиц за материал:** такой же меч: 2609.
**Способности:** При атаке снаряд 10%; применение накладывает левитацию XIX на 1 секунду в радиусе 6 на сущности без семейства shulker_sword, расход 8, кулдаун 8 секунд. Иммунитет к левитации; при приседании защищающая раковина. Если раковину уничтожили, пока владелец внутри, владелец погибает согласно описанию. Для этого привязать раковину к её владельцу; исходная команда выбирала ближайшего подходящего игрока в радиусе 1 и не гарантировала правильную цель.
**Получение:** при убийстве обычного шалкера игроком выдавать меч с шансом 4,5% плюс 2 процентных пункта за уровень Looting, сохраняя обычную добычу шалкера. В исходном пакете таблица есть, а локальное определение ванильного шалкера, которое её подключает, отсутствует; в ремейке привязку обеспечить явно. Призванная защитная раковина — отдельная [сущность щита](#mob-shulker-shield), не источник меча.
**Условная модель износа weapon-события:** 1: 1.

**Цели навыка:** все сущности без family `shulker_sword` в радиусе 6, включая возможных игроков, а не только враги. При защите игроку записаны scale 0,7 и отмена урона cause all; состояние и параметры создаваемой раковины — [щит шалкера](#mob-shulker-shield). Корректность привязки и снятия проверить для нескольких игроков.

**Вход weapon-события:** при попадании с уроном, ударе без урона и ударе по блоку. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Looting:** при реально переданных уровнях 0/1/2/3 условные шансы записанной ветви — 4,5%, 6,5%, 8,5%, 10,5%. Множитель 0,02 добавляет 2 п.п. за уровень; не доказывает подключение таблицы или успешность события.

**Привязка добычи:** соответствующая ванильная сущность в образце Mojang v1.26.60.5 указывает путь таблицы, совпадающий с сохранённым путём аддона. Это совпадение путей, а не доказательство загрузки таблицы в конкретном мире или выдачи меча; сохранить ванильную добычу.

**Приёмка после разрешения на разработку:** проверить владельца щита и своевременное снятие защитной группы, в том числе при нескольких игроках.

**Значок 2.8.8:** `Swords_R/textures/items/shulker_sword.png` (ключ атласа `shulker_sword`; файл сохранён в наборе ресурсов 2.8.8).

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
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
    },
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:cooldown": {
      "category": "shulker_sword",
      "duration": 8
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

#### Записанные группы и события владельца 2.8.8

Это относящиеся к предмету поля игрока из сохранённого реестра, а не утверждение об их выполнении; если старый код расходится с решениями выше (например восстановление настроек мира или блоков), выполнять решение, а не переносить старую ошибку. Пустое или отсутствующее поле не подменять предположением.

**Группы:**

- `minecraft:shulker_sword` (строки 228,854,1644,1648,1659): `{"minecraft:scale":{"value":1},"minecraft:type_family":{"family":["player","shulker_sword"]}}`
- `shulker_sword_skill` (строки 232,1665,1666): `{"minecraft:damage_sensor":{"triggers":[{"cause":"all","deals_damage":false}]},"minecraft:scale":{"value":0.7},"minecraft:type_family":{"family":["player","shulker_sword"]}}`

**События:**

**`minecraft:shulker_sword`** (строки 228,854,1644,1648,1659):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"shulker_sword"},"add":{"component_groups":["minecraft:shulker_sword"]}}`
  - `$.sequence[1]` — поля действия: `{"run_command":{"command":["effect @s levitation 0 0"]}}`

**`stop_shulker_sword_event`** (строки 861,1655):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"shulker_sword"},"remove":{"component_groups":["minecraft:shulker_sword"]},"add":{"component_groups":["minecraft:default_player"]},"run_command":{"command":["ride @s stop_riding"]}}`

**`shulker_sword_skill`** (строки 232,1665,1666):

- `$` — поля действия: `{"add":{"component_groups":["shulker_sword_skill"]},"run_command":{"command":["ride @s summon_ride entity:shulker_shield no_ride_change"]}}`


<a id="sword-jungle_sword"></a>
### 12. Jungle Sword — `effect:jungle_sword`

**Параметры предмета:** блеск foil: нет; левая рука: нет; should_despawn: не указан; digger: web 15, bamboo 10.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** 4. **Прочность:** 128. **Кулдаун:** не указан. **Расход применения:** не указан. **Зачарование:** есть: value 9, слот sword.
**Ремонт, единиц за материал:** такой же меч: 128.
**Способности:** Здоровье 4 сердца, Absorption III на 1 с; рядом растут лианы на подходящих природных и строительных блоках. В функции 2.8.8 записаны 148 команд: проверяются четыре горизонтальные соседние клетки на высоте игрока +1, а лиана ставится только в воздушную клетку над игроком (`~ ~1 ~`); выбор направления записан как data 8/2/1/4 для +X/−X/+Z/−Z соответственно. Подходящие исходные блоки и data: log 0–3, log2 0–1, stone 0/1/3/5, cobblestone 0, dirt 0, leaves 0–3/11, leaves2 0–1, planks 0–5, grass 0, netherrack 0, nether_brick 0, sand 0, glass 0, obsidian 0, end_stone 0, sandstone 0, gravel 0, snow 0, packed_ice 0, ice 0. Команды идут в исходном порядке, выбирают `@p` и заменяют только air; перенос соответствий старых data в современные состояния и контекст `@p` проверить при реализации. Применение предмета на земле или траве размещает саженец джунглевого дерева; предмет также приманивает попугаев.
**Получение:** сундук храма джунглей либо рыбалка только в биоме джунглей — по решению пользователя, как в описании. В исходных таблицах обычная и jungle-рыбалка ссылаются на общую treasure-таблицу с мечом; ограничение биома — выбранное требование ремейка.
**Пулы добычи:** храм джунглей — 2–6 выборов, 16/457; отдельный пул treasure при рыбалке — 1 выбор, 5/41. Доли — вес записи на один выбор, не шанс всего сундука или любой рыбалки.
**Условная модель износа weapon-события:** 1: 1.

#### Опоры и направления лозы

Список допустимых пар блока/data в сохранённом порядке: log 0–3; log2 0–1; stone 0; cobblestone 0; dirt 0; leaves 0–3 и 11; leaves2 0–1; planks 0–5; grass 0; netherrack 0; nether_brick 0; sand 0; glass 0; obsidian 0; end_stone 0; sandstone 0; gravel 0; stone 1, 3 и 5; snow 0; packed_ice 0; ice 0. Всего 37 пар; каждой соответствуют четыре направления.

Целевая клетка для лозы — на y+1 от игрока и только вместо воздуха. Опоры проверяются на y+1: x+1 → data 8; x−1 → 2; z+1 → 1; z−1 → 4. Порядок важен: после успешной постановки следующая команда с условием замены воздуха не должна затирать лозу. Значения старого data надо сопоставить с современными состояниями блоков, не считать их современной схемой напрямую.

**Вход weapon-события:** только при попадании по сущности с уроном. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Значок 2.8.8:** `Swords_R/textures/items/jungle_sword.png` (ключ атласа `jungle_sword`; файл сохранён в наборе ресурсов 2.8.8).

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
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

#### Записанные группы и события владельца 2.8.8

Это относящиеся к предмету поля игрока из сохранённого реестра, а не утверждение об их выполнении; если старый код расходится с решениями выше (например восстановление настроек мира или блоков), выполнять решение, а не переносить старую ошибку. Пустое или отсутствующее поле не подменять предположением.

**Группы:**

- `minecraft:jungle_sword` (строки 313,728,2001,2005,2016): `{"minecraft:type_family":{"family":["player","jungle_sword"]},"minecraft:health":{"value":8,"max":8}}`

**События:**

**`minecraft:jungle_sword`** (строки 313,728,2001,2005,2016):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"jungle_sword"},"add":{"component_groups":["minecraft:jungle_sword"]}}`
  - `$.sequence[1]` — поля действия: `{"run_command":{"command":["effect @s absorption 1 2 true","function commands/swords_and_more_swords/swords_and_more_swords/jungle_sword"]}}`

**`stop_jungle_sword_event`** (строки 735,2012):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"jungle_sword"},"remove":{"component_groups":["minecraft:jungle_sword"]},"add":{"component_groups":["minecraft:default_player"]},"run_command":{"command":["effect @s absorption 0"]}}`


<a id="sword-cactus_sword"></a>
### 13. Cactus Sword — `effect:cactus_sword`

**Параметры предмета:** блеск foil: нет; левая рука: нет; should_despawn: не указан; digger: web 15, bamboo 10.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** 6. **Прочность:** 125. **Кулдаун:** не указан. **Расход применения:** не указан. **Зачарование:** есть: value 9, слот sword.
**Ремонт, единиц за материал:** такой же меч: 125.
**Способности:** таймер с записанным интервалом 0,5; урон 1 владельцу и 1 всем сущностям, кроме игроков, в радиусе 1,4.
**Получение:** Два кактуса над палкой.
**Рецепт:** F / F / E; E=minecraft:stick, F=minecraft:cactus.
**Условная модель износа weapon-события:** 1: 1.

**Положение в основной руке:** первое лицо `{"position":[0.67,0,-1.24]}`; третье лицо `{"position":[0.36,1.5,-0.66]}`. Неуказанные поля не заменять нулями; фактический вид проверить на целевой версии.

**Вход weapon-события:** только при попадании по сущности с уроном. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Значок 2.8.8:** `Swords_R/textures/items/cactus_sword.png` (ключ атласа `cactus_sword`; файл сохранён в наборе ресурсов 2.8.8).

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
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

#### Записанные группы и события владельца 2.8.8

Это относящиеся к предмету поля игрока из сохранённого реестра, а не утверждение об их выполнении; если старый код расходится с решениями выше (например восстановление настроек мира или блоков), выполнять решение, а не переносить старую ошибку. Пустое или отсутствующее поле не подменять предположением.

**Группы:**

- `minecraft:cactus_sword` (строки 343,672,2117,2121,2129): `{"minecraft:type_family":{"family":["player","cactus_sword"]},"minecraft:timer":{"time":[0.5,0.5],"looping":true,"time_down_event":{"event":"cactus_sword_skills","target":"self"}}}`

**События:**

**`minecraft:cactus_sword`** (строки 343,672,2117,2121,2129):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"cactus_sword"},"add":{"component_groups":["minecraft:cactus_sword"]}}`

**`stop_cactus_sword_event`** (строки 679,2125):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"cactus_sword"},"remove":{"component_groups":["minecraft:cactus_sword"]},"add":{"component_groups":["minecraft:default_player"]}}`

**`cactus_sword_skills`** (строки 346,2134):

- `$` — поля действия: `{"run_command":{"command":["damage @e[r=1.4,type=!player] 1 contact entity @s","damage @s 1 contact"]}}`


<a id="sword-emerald_sword"></a>
### 14. Emerald Sword — `effect:emerald_sword`

**Параметры предмета:** блеск foil: нет; левая рука: нет; should_despawn: не указан; digger: web 15, bamboo 10.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** 7. **Прочность:** 2300. **Кулдаун:** не указан. **Расход применения:** не указан. **Зачарование:** есть: value 9, слот sword.
**Ремонт, единиц за материал:** такой же меч: 2300.
**Способности:** внутри деревни владелец получает Hero of the Village I, жители в радиусе 64 — Resistance II; обе команды задают длительность 1.
**Получение:** сундуки крепости, лесного особняка и аванпоста; сделка кузнеца за 24–32 изумрудных блока с чарами уровней 5–60. По решению пользователя вторую отдельную сделку с фиксированной ценой 32 блока не добавлять.
**Пулы добычи:** коридор крепости — 2–3 выбора, 5/521; лесной особняк — 1–3, 25/670; аванпост — 2–3, 3/28*, count 0–1. Доли — вес записи на один выбор, не шанс всего сундука или любой рыбалки. *Сумма с допущением неуказанного веса 1.
**Условная модель износа weapon-события:** 1: 1.

**Вход weapon-события:** при попадании с уроном, ударе без урона и ударе по блоку. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Значок 2.8.8:** `Swords_R/textures/items/emerald_sword.png` (ключ атласа `emerald_sword`; файл сохранён в наборе ресурсов 2.8.8).

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
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

#### Записанные группы и события владельца 2.8.8

Это относящиеся к предмету поля игрока из сохранённого реестра, а не утверждение об их выполнении; если старый код расходится с решениями выше (например восстановление настроек мира или блоков), выполнять решение, а не переносить старую ошибку. Пустое или отсутствующее поле не подменять предположением.

**Группы:**

- `minecraft:emerald_sword` (строки 334,686,2086,2090,2103): `{"minecraft:type_family":{"family":["player","emerald_sword"]}}`

**События:**

**`minecraft:emerald_sword`** (строки 334,686,2086,2090,2103):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"emerald_sword"},"add":{"component_groups":["minecraft:emerald_sword"]}}`
  - `$.sequence[1]` — поля действия: `{"filters":{"all_of":[{"test":"is_in_village","subject":"self","value":true}]},"run_command":{"command":["effect @s village_hero 1 0 true","effect @e[family=villager,r=64] resistance 1 1 true"]}}`

**`stop_emerald_sword_event`** (строки 693,2098):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"emerald_sword"},"run_command":{"command":["effect @s village_hero 0 0 true"]},"remove":{"component_groups":["minecraft:emerald_sword"]},"add":{"component_groups":["minecraft:default_player"]}}`


<a id="sword-spectral_sword"></a>
### 15. Spectral Sword — `effect:spectral_sword`

**Параметры предмета:** блеск foil: да; левая рука: нет; should_despawn: false; digger: web 15, bamboo 10.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** 9. **Прочность:** 3256. **Кулдаун:** 18 с. **Расход применения:** 15. **Зачарование:** есть: value 9, слот sword.
**Ремонт, единиц за материал:** такой же меч: 3256; end crystal: 620; nether star: 2052.
**Способности:** Камень обычного мира, незерак Незера и эндерняк Энда становятся прозрачными в кубе ±6 блоков; сохранять и точно возвращать реальные исходные состояния блоков. Свет и следующий за игроком кристалл; в исходной записи при weapon-событии выбор 1% на попытку взорвать подходящий кристалл (см. уточнение ниже). Применение: взрывной снаряд, расход 15, кулдаун 18 секунд.
**Получение:** по решению пользователя при обычном появлении кристалла в биоме с тегом `nether` он получает условие награды; при его повреждении выполняется 2%-попытка и запускается взрыв. Взрыв от 1%-ветви Spectral сам по себе 2%-попытку не запускает. Также при гибели гаста от его собственного огненного шара — одна попытка 6%. Учитывать исходного гаста, выпустившего шар, даже если игрок отразил его и текущий владелец изменился; проверять идентификацию на целевой версии. В коде оригинала проверка при получении урона не указывает смертельный удар или собственный снаряд; выбранное правило соответствует описанию. Зачарование — согласно сохранённой компонентной настройке, несмотря на текст «false».
**Условная модель износа weapon-события:** 0: 1/100, 1: 99/100.

**Два разных взрыва:** снаряд применения `entity:ender_crystal_projectile` при попадании запускает взрыв power 6 с огнём; его поля projectile power 5, gravity 0,001, inertia и liquid inertia 1, reflect_on_hurt и catch_fire true. Взрыв сопровождающего или обычного кристалла — power 6 без огня. Это разные сущности и параметры; оба исходных взрыва имеют `destroy_affected_by_griefing: true`.

**Источник 2% у кристалла:** в оригинале обычное событие при появлении кристалла в биоме с тегом `nether` добавляет группу `spectral_sword_drop`; её `on_hurt` запускает выбор 98/2 и затем взрыв. Фильтр записан при появлении кристалла, а не в самом выборе 98/2. Прямое событие `minecraft:crystal_explode`, используемое 1%-ветвью меча, само по себе только добавляет группу взрыва, без отдельной записанной 2%-попытки. Не считать каждый взрыв доказанной попыткой получения меча; специальные события появления и фактическое исполнение движка нужно учитывать отдельно.

**Кристалл: исходные условия и решения пользователя.** В описании сказано, что кристалл следует за игроком повсюду, но исходный одноразовый таймер 0,4 с вызывает создание лишь при отсутствии у биома тега `the_end`. В ветви weapon с весом 1/100 команда выбирает ближайший подходящий `ender_crystal` без явного ограничения радиуса и без привязки к владельцу; исключены обычная family `ender_crystal_default` и растущая `ender_crystal_scale`. Если подходящего кристалла нет, команда не находит цель; один выбор 1% не является безусловным взрывом. При использовании снаряда исходная отдельная команда выбирает подходящий кристалл в r=4 без привязки к владельцу и задаёт группу с ростом от 0,1 до 1 за 18 с; пока на нём family `ender_crystal_scale`, он исключён из этой ветви weapon. По решению пользователя в ремейке при выстреле уменьшать и растить только собственный подходящий кристалл владельца в r=4; если такого нет, кристалл не менять, но выстрел выполнять. Прямых вызовов `spectral_sword_reload_skill` по буквальному поиску в файлах пакета не найдено, поэтому автоматическое появление кристалла после взрыва по этим данным не подтверждено. По решению пользователя в ремейке 1%-попытка должна выбирать только собственный кристалл владельца; чужие кристаллы не затрагивать, если своего подходящего нет — взрыва нет. Кристалл с активной исходной группой роста исключён из выбора. По решению пользователя в ремейке сохранять исходный фильтр: не создавать кристалл в биоме с тегом `the_end`. После взрыва автоматически не восстанавливать; новый кристалл появляется после повторного снятия и взятия меча с исходной задержкой 0,4 с, если в момент создания биом допускает создание. Дракон обычно лечится от ближайших энд-кристаллов, что может объяснять исходное ограничение, но его причина автором не установлена, а взаимодействие именно спутника с драконом не проверено. Одноразовый таймер и отсутствие найденного вызова reload указывают на вероятное отсутствие пересоздания без повторной активации меча; фактический цикл после взрыва в опыте не подтверждён. Фильтр ограничивает создание, а не доказывает исчезновение существующего кристалла при переходе в Край. По следующему решению пользователя, если владелец держит меч и с ним есть собственный кристалл, при переходе в биом с тегом `the_end` убрать кристалл без взрыва и без 2%-попытки; при выходе в биом, где создание допускается, автоматически вернуть кристалл, если меч всё ещё удерживается. Это возвращение относится только к кристаллу, убранному при входе; ранее взорванный кристалл автоматически не возвращать. По отдельному решению пользователя, если снять меч до выхода, ожидаемый автоматический возврат отменяется, даже если снова взять меч внутри биома `the_end`. В таком случае после выхода снять и снова взять меч в подходящем биоме; новый кристалл создаётся по ранее согласованным условиям с задержкой 0,4 с.

**Положение в основной руке:** первое лицо `{"position":[0.57,0.1,-1.24]}`; третье лицо `{"position":[0.41,1.7,-0.7]}`. Неуказанные поля не заменять нулями; фактический вид проверить на целевой версии.

**Вход weapon-события:** при попадании с уроном, ударе без урона и ударе по блоку. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Приёмка после разрешения на разработку:** сохранять и точно возвращать исходные блоки и их состояния; проверить измерения, чужие изменения, нескольких игроков и перезагрузку.

**Значок 2.8.8:** `Swords_R/textures/items/spectral_sword.png` (ключ атласа `spectral_sword`; файл сохранён в наборе ресурсов 2.8.8).

**Область и восстановление:** создавать прозрачные замены в кубе x/y/z ±6 (13×13×13); в Overworld исходный материал stone, в Nether — netherrack, в End — end_stone. В оригинале основной selector ограничен `y=8,dy=247`, нижний `y=0,dy=7` только восстанавливает; для нового диапазона мира не переносить старые границы автоматически. В оригинальной пробе гранит восстановился как обычный stone; для ремейка это неприемлемо: до замены хранить конкретный ID и все состояния каждой позиции, восстанавливать именно их, учитывать выгрузку и наложение игроков и не перезаписывать сторонние изменения.

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
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
    },
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:cooldown": {
      "category": "spectral_sword",
      "duration": 18
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

#### Записанные группы и события владельца 2.8.8

Это относящиеся к предмету поля игрока из сохранённого реестра, а не утверждение об их выполнении; если старый код расходится с решениями выше (например восстановление настроек мира или блоков), выполнять решение, а не переносить старую ошибку. Пустое или отсутствующее поле не подменять предположением.

**Группы:**

- `minecraft:spectral_sword` (строки 251,826,1693,1697,1793,1821): `{"minecraft:timer":{"time":[0.4,0.4],"looping":false,"time_down_event":{"event":"spectral_sword_skills","target":"self"}},"minecraft:rideable":{"seat_count":1,"family_types":["ender_crystal","spectral_sword"],"seats":{"position":[0.0,0.4,0.0],"lock_rider_rotation":0}},"minecraft:type_family":{"family":["player","spectral_sword"]}}`

**События:**

**`minecraft:spectral_sword`** (строки 251,826,1693,1697,1793,1821):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"spectral_sword"},"add":{"component_groups":["minecraft:spectral_sword"]}}`
  - `$.sequence[1]` — поля действия: `{"run_command":{"command":["fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace air","fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace effect99:lightblock2","execute @s[y=8,dy=247] ~~~ event entity @s spectral_sword_function","execute @s[y=0,dy=7] ~~~ event entity @s spectral_sword_function_1"]}}`

**`spectral_sword_function_1`** (строки 1711):

- `$.sequence`: 3 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"all_of":[{"test":"has_biome_tag","operator":"!=","value":"nether"},{"test":"has_biome_tag","operator":"!=","value":"the_end"}]},"run_command":{"command":["fill ~8 ~8 ~8 ~-8 ~-6 ~-8 stone 0 replace effect99:spectral_block"]}}`
  - `$.sequence[1]` — поля действия: `{"filters":{"test":"has_biome_tag","value":"nether"},"run_command":{"command":["fill ~8 ~8 ~8 ~-8 ~-6 ~-8 netherrack 0 replace effect99:spectral_block"]}}`
  - `$.sequence[2]` — поля действия: `{"filters":{"test":"has_biome_tag","value":"the_end"},"run_command":{"command":["fill ~8 ~8 ~8 ~-8 ~-6 ~-8 end_stone 0 replace effect99:spectral_block"]}}`

**`spectral_sword_function`** (строки 1741):

- `$.sequence`: 3 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"all_of":[{"test":"has_biome_tag","operator":"!=","value":"nether"},{"test":"has_biome_tag","operator":"!=","value":"the_end"}]},"run_command":{"command":["fill ~6 ~6 ~6 ~-6 ~-6 ~-6 effect99:spectral_block 0 replace stone","fill ~7 ~8 ~8 ~8 ~-8 ~-8 stone 0 replace effect99:spectral_block","fill ~-7 ~-8 ~-8 ~-8 ~8 ~8 stone 0 replace effect99:spectral_block","fill ~-6 ~8 ~7 ~6 ~-8 ~8 stone 0 replace effect99:spectral_block","fill ~6 ~-8 ~-7 ~-6 ~8 ~-8 stone 0 replace effect99:spectral_block","fill ~8 ~-8 ~8 ~-8 ~-7 ~-8 stone 0 replace effect99:spectral_block","fill ~8 ~8 ~8 ~-8 ~7 ~-8 stone 0 replace effect99:spectral_block"]}}`
  - `$.sequence[1]` — поля действия: `{"filters":{"test":"has_biome_tag","value":"nether"},"run_command":{"command":["fill ~6 ~6 ~6 ~-6 ~-6 ~-6 effect99:spectral_block 0 replace netherrack","fill ~7 ~8 ~8 ~8 ~-8 ~-8 netherrack 0 replace effect99:spectral_block","fill ~-7 ~-8 ~-8 ~-8 ~8 ~8 netherrack 0 replace effect99:spectral_block","fill ~-6 ~8 ~7 ~6 ~-8 ~8 netherrack 0 replace effect99:spectral_block","fill ~6 ~-8 ~-7 ~-6 ~8 ~-8 netherrack 0 replace effect99:spectral_block","fill ~8 ~-8 ~8 ~-8 ~-7 ~-8 netherrack 0 replace effect99:spectral_block","fill ~8 ~8 ~8 ~-8 ~7 ~-8 netherrack 0 replace effect99:spectral_block"]}}`
  - `$.sequence[2]` — поля действия: `{"filters":{"test":"has_biome_tag","value":"the_end"},"run_command":{"command":["fill ~6 ~6 ~6 ~-6 ~-6 ~-6 effect99:spectral_block 0 replace end_stone","fill ~7 ~8 ~8 ~8 ~-8 ~-8 end_stone 0 replace effect99:spectral_block","fill ~-7 ~-8 ~-8 ~-8 ~8 ~8 end_stone 0 replace effect99:spectral_block","fill ~-6 ~8 ~7 ~6 ~-8 ~8 end_stone 0 replace effect99:spectral_block","fill ~6 ~-8 ~-7 ~-6 ~8 ~-8 end_stone 0 replace effect99:spectral_block","fill ~8 ~-8 ~8 ~-8 ~-7 ~-8 end_stone 0 replace effect99:spectral_block","fill ~8 ~8 ~8 ~-8 ~7 ~-8 end_stone 0 replace effect99:spectral_block"]}}`

**`stop_spectral_sword_event`** (строки 833,1789):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"spectral_sword"},"remove":{"component_groups":["minecraft:spectral_sword"]},"run_command":{"command":["ride @s evict_riders"]},"add":{"component_groups":["minecraft:default_player"]}}`

**`spectral_sword_skills`** (строки 253,1799):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"has_biome_tag","operator":"!=","value":"the_end"},"run_command":{"command":["summon ender_crystal ~ ~1.8 ~ minecraft:detect_player"]}}`
  - `$.sequence[1]` — поля действия: `{"run_command":{"command":["playsound portal.travel @a[r=16] ~ ~ ~ 1 7","particle minecraft:example_flipbook ~ ~3 ~"]}}`

**`spectral_sword_reload_skill`** (строки 1817):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"spectral_sword"},"add":{"component_groups":["minecraft:spectral_sword"]}}`


<a id="sword-lapis_sword"></a>
### 16. Lapis Sword — `effect:lapis_sword`

**Параметры предмета:** блеск foil: нет; левая рука: нет; should_despawn: не указан; digger: web 15, bamboo 10.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** 5. **Прочность:** 528. **Кулдаун:** не указан. **Расход применения:** не указан. **Зачарование:** есть: value 9, слот sword.
**Ремонт, единиц за материал:** такой же меч: 528; lapis lazuli: 48.
**Способности:** группа игрока задаёт повторяющийся случайный таймер `[2,5;6]` с; событие выдаёт `xp 5 @s`. Это пять единиц опыта на срабатывание, не пять уровней. В опыте оригинала 2.8.8/Bedrock 1.20.50 после выдачи меча наблюдались пять прибавлений по 5 очков; промежутки между наблюдавшимися прибавлениями составляли примерно 4,1–4,9 с. После снятия меча за следующие 13 с прибавлений не было. Эта выборка не доказывает распределение таймера.
**Получение:** Сундуки коридора и библиотеки крепости, а также аванпоста разбойников.
**Пулы добычи:** коридор крепости — 2–3 выбора, 5/521; библиотека — 2–10, 5/275; аванпост — 2–3, 3/28*, count 0–1. Доли — вес записи на один выбор, не шанс всего сундука или любой рыбалки. *Сумма с допущением неуказанного веса 1.
**Условная модель износа weapon-события:** 1: 1.

**Вход weapon-события:** только при попадании по сущности с уроном. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Значок 2.8.8:** `Swords_R/textures/items/lapis_sword.png` (ключ атласа `lapis_sword`; файл сохранён в наборе ресурсов 2.8.8).

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
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

#### Записанные группы и события владельца 2.8.8

Это относящиеся к предмету поля игрока из сохранённого реестра, а не утверждение об их выполнении; если старый код расходится с решениями выше (например восстановление настроек мира или блоков), выполнять решение, а не переносить старую ошибку. Пустое или отсутствующее поле не подменять предположением.

**Группы:**

- `minecraft:lapis_sword` (строки 296,770,1900,1904,1912): `{"minecraft:type_family":{"family":["player","lapis_sword"]},"minecraft:timer":{"time":[2.5,6.0],"looping":true,"randomInterval":true,"time_down_event":{"event":"lapis_sword_skills","target":"self"}}}`

**События:**

**`minecraft:lapis_sword`** (строки 296,770,1900,1904,1912):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"lapis_sword"},"add":{"component_groups":["minecraft:lapis_sword"]}}`

**`stop_lapis_sword_event`** (строки 777,1908):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"lapis_sword"},"remove":{"component_groups":["minecraft:lapis_sword"]},"add":{"component_groups":["minecraft:default_player"]}}`

**`lapis_sword_skills`** (строки 299,1917):

- `$` — поля действия: `{"run_command":{"command":["xp 5 @s","playsound random.orb @s ~ ~ ~ 0.3"]}}`


<a id="sword-grass_sword"></a>
### 17. Grass Sword — `effect:grass_sword`

**Параметры предмета:** блеск foil: нет; левая рука: нет; should_despawn: не указан; digger: web 15, bamboo 10.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** 8. **Прочность:** 250. **Кулдаун:** не указан. **Расход применения:** не указан. **Зачарование:** есть: value 9, слот sword.
**Ремонт, единиц за материал:** такой же меч: 250.
**Способности:** при удержании повторяющийся таймер `[0,2;0,2]` вызывает поиск `r=8`, исключая player, item, `entity:grass`, xp_orb, arrow и существующий tag grass. Для каждой подходящей цели проверяется grass под ней и air либо tallgrass в её позиции; затем вызывается [травяной помощник](#mob-grass-helper). Отдельная команда заменяет dirt на grass в плоскости 5×5 на y−1 и при grass снизу ставит tallgrass вместо air в позиции игрока. Тег grass удаляется в кольце 9–10 блоков; он общий и не привязан к создателю.
**Получение:** по решению пользователя при появлении ведьмы ночью выбор 20/100 на травяную форму; при её смерти отдельный выбор 20/100 на загрузку структуры меча. Это два последовательных условных выбора, а не гарантированные 4% с любой ведьмы. Условия и параметры существа — [Grass Witch](#mob-grass-witch).
**Условная модель износа weapon-события:** 1: 1.

**Положение в основной руке:** первое лицо `{"position":[0.8,0.15,-1.74]}`; третье лицо `{"position":[0.69,2.5,-0.96]}`. Неуказанные поля не заменять нулями; фактический вид проверить на целевой версии.

**Вход weapon-события:** только при попадании по сущности с уроном. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Значок 2.8.8:** `Swords_R/textures/items/grass_sword.png` (ключ атласа `grass_sword`; файл сохранён в наборе ресурсов 2.8.8).

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
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

#### Записанные группы и события владельца 2.8.8

Это относящиеся к предмету поля игрока из сохранённого реестра, а не утверждение об их выполнении; если старый код расходится с решениями выше (например восстановление настроек мира или блоков), выполнять решение, а не переносить старую ошибку. Пустое или отсутствующее поле не подменять предположением.

**Группы:**

- `minecraft:grass_sword` (строки 317,714,2023,2027,2043): `{"minecraft:type_family":{"family":["player","grass_sword"]},"minecraft:timer":{"time":[0.2,0.2],"looping":true,"time_down_event":{"event":"grass_sword_skills","target":"self"}}}`

**События:**

**`minecraft:grass_sword`** (строки 317,714,2023,2027,2043):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"grass_sword"},"add":{"component_groups":["minecraft:grass_sword"]}}`
  - `$.sequence[1]` — поля действия: `{"run_command":{"command":["tag @e[tag=grass,rm=9,r=10] remove grass","fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 grass 0 replace dirt","execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 fill ~ ~ ~ ~ ~ ~ tallgrass 0 replace air"]}}`

**`stop_grass_sword_event`** (строки 721,2039):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"grass_sword"},"remove":{"component_groups":["minecraft:grass_sword"]},"add":{"component_groups":["minecraft:default_player"]}}`

**`grass_sword_skills`** (строки 320,2048):

- `$` — поля действия: `{"run_command":{"command":["execute @e[type=!player,type=!item,type=!entity:grass,type=!xp_orb,type=!arrow,r=8,tag=!grass] ~ ~ ~ detect ~ ~-0.1 ~ grass 0 execute @s ~ ~ ~ detect ~ ~ ~ air 0 summon entity:grass","execute @e[type=!player,type=!item,type=!entity:grass,type=!xp_orb,type=!arrow,r=8,tag=!grass] ~ ~ ~ detect ~ ~-0.1 ~ grass 0 execute @s ~ ~ ~ detect ~ ~ ~ tallgrass 0 summon entity:grass"]}}`


<a id="sword-obsidian_sword"></a>
### 18. Obsidian Sword — `effect:obsidian_sword`

**Параметры предмета:** блеск foil: нет; левая рука: нет; should_despawn: не указан; digger: web 15, bamboo 10.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** 8. **Прочность:** 3000. **Кулдаун:** не указан. **Расход применения:** не указан. **Зачарование:** есть: value 9, слот sword.
**Ремонт, единиц за материал:** такой же меч: 3000; obsidian: 120.
**Способности:** Иммунитет к block_explosion и entity_explosion, сопротивление отбрасыванию 1; другие источники урона не отменены. На weapon-событие расход 1 с 55%, 2 с 30%, 3 с 15%.
**Получение:** Выбросить Fire Sword под дождь: превращение в Obsidian.
**Условная модель износа weapon-события:** 1: 11/20, 2: 3/10, 3: 3/20.

**Вход weapon-события:** только при попадании по сущности с уроном. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Значок 2.8.8:** `Swords_R/textures/items/obsidian_sword.png` (ключ атласа `obsidian_sword`; файл сохранён в наборе ресурсов 2.8.8).

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
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

#### Записанные группы и события владельца 2.8.8

Это относящиеся к предмету поля игрока из сохранённого реестра, а не утверждение об их выполнении; если старый код расходится с решениями выше (например восстановление настроек мира или блоков), выполнять решение, а не переносить старую ошибку. Пустое или отсутствующее поле не подменять предположением.

**Группы:**

- `minecraft:obsidian_sword` (строки 286,784,1883,1887,1895): `{"minecraft:damage_sensor":{"triggers":{"on_damage":{"filters":{"any_of":[{"test":"has_damage","subject":"self","value":"block_explosion"},{"test":"has_damage","subject":"self","value":"entity_explosion"}]}},"deals_damage":false}},"minecraft:type_family":{"family":["player","obsidian_sword"]},"minecraft:knockback_resistance":{"value":1.0}}`

**События:**

**`minecraft:obsidian_sword`** (строки 286,784,1883,1887,1895):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"obsidian_sword"},"add":{"component_groups":["minecraft:obsidian_sword"]}}`

**`stop_obsidian_sword_event`** (строки 791,1891):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"obsidian_sword"},"remove":{"component_groups":["minecraft:obsidian_sword"]},"add":{"component_groups":["minecraft:default_player"]}}`


<a id="sword-glowstone_sword"></a>
### 19. Glowstone Sword — `effect:glowstone_sword`

**Параметры предмета:** блеск foil: да; левая рука: да; should_despawn: не указан; digger: web 15, bamboo 10.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** 4. **Прочность:** 128. **Кулдаун:** не указан. **Расход применения:** не указан. **Зачарование:** есть: value 9, слот sword.
**Ремонт, единиц за материал:** такой же меч: 128; glowstone: 64; glowstone dust: 16.
**Способности:** по решению пользователя меч освещает пространство при удержании в любой руке; уровень излучения — 15 по шкале Minecraft 0–15. В исходнике сенсор `hand` выполняет две операции в кубе ±1: поставить `effect99:lightblock` вместо воздуха и обновить его вместо самого себя; записаны emission 1, absorption 0, нулевые collision и ticking `[0,2;0,2]` с заменой на воздух. Значение 15 и действие в левой руке — выбранные требования ремейка, а не установленный результат старого кода.
**Получение:** Два блока светокамня над огненным стержнем.
**Рецепт:** 2 / 2 / 1; 1=minecraft:blaze_rod, 2=minecraft:glowstone.
**Условная модель износа weapon-события:** 1: 1.

**Вход weapon-события:** только при попадании по сущности с уроном. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Значок 2.8.8:** `Swords_R/textures/items/glowstone_sword.png` (ключ атласа `glowstone_sword`; файл сохранён в наборе ресурсов 2.8.8).

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
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

#### Записанные группы и события владельца 2.8.8

Это относящиеся к предмету поля игрока из сохранённого реестра, а не утверждение об их выполнении; если старый код расходится с решениями выше (например восстановление настроек мира или блоков), выполнять решение, а не переносить старую ошибку. Пустое или отсутствующее поле не подменять предположением.

**События:**

**`minecraft:glowstone_sword`** (строки 924,1489):

- `$` — поля действия: `{"run_command":{"command":["fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock 0 replace air","fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock 0 replace effect99:lightblock"]}}`


<a id="sword-time_sword"></a>
### 20. Time Sword — `effect:time_sword`

**Параметры предмета:** блеск foil: да; левая рука: нет; should_despawn: не указан; digger: web 15, bamboo 10.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** 13. **Прочность:** 13770. **Кулдаун:** не указан. **Расход применения:** не указан. **Зачарование:** есть: value 9, слот sword.
**Ремонт, единиц за материал:** компонент не указан.
**Способности:** Пока удерживается: randomtickspeed 300; отдельно +30 игровых тиков на срабатывание; скорость XVI для подходящих неигровых сущностей; параметр движения игрока 1; свет. На weapon-событие расход 1/16/32/64 с вероятностями 90/6/3/1%. Не повреждать прежние настройки мира.
**Получение:** Колодец: выбросить Clock Sword, 2,5% на предмет. В заметках есть компонент зачарования, хотя текст говорит false: применять выбранное правило по компонентам.
**Условная модель износа weapon-события:** 1: 9/10, 16: 3/50, 32: 3/100, 64: 1/100.

**Положение в основной руке:** первое лицо `{"position":[1,0.5,-3],"scale":[0.04,0.04,0.04]}`; третье лицо `{"position":[0.95,3.3,-1.2],"scale":[0.06,0.06,0.06]}`. Неуказанные поля не заменять нулями; фактический вид проверить на целевой версии.

**Вход weapon-события:** при попадании с уроном, ударе без урона и ударе по блоку. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Одновременно с Clock:** сохранять обе независимые команды добавления времени (Time +30, Clock +10 на собственное срабатывание); `randomtickspeed` задаётся последней из команд, а не сложением 100 и 300. В опыте двух игроков 2.8.8/1.20.50 при обоих активных наблюдалось 300, после снятия Time при работающем Clock — 100. Прежние настройки мира восстанавливать после завершения всех активных воздействий, не удаляя эффекты других источников.

**Колодец:** каждая единица Clock даёт независимую попытку получить Time с вероятностью 2,5%; возможны несколько наград. Проверять настоящий ID и форму колодца; построенные копии допустимы.

**Значок 2.8.8:** `Swords_R/textures/items/time_sword.png` (ключ атласа `time_sword`; файл сохранён в наборе ресурсов 2.8.8).

**Записанные цели и остановка:** пока меч в руке, команды назначают `randomtickspeed 300`, `time add 30`, `speed 1 15` всем `type=!player` и движение 1 подходящим `@a[family=default_player]`; кроме того, создают световой блок в кубе ±1. Оригинальный stop пишет `randomtickspeed 1` и сбрасывает speed, не сохраняя прежние значения. В ремейке сохранять исходные настройки и эффекты, а не сбрасывать в 1; предусмотреть параллельное действие Clock и нескольких игроков.

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
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

#### Записанные группы и события владельца 2.8.8

Это относящиеся к предмету поля игрока из сохранённого реестра, а не утверждение об их выполнении; если старый код расходится с решениями выше (например восстановление настроек мира или блоков), выполнять решение, а не переносить старую ошибку. Пустое или отсутствующее поле не подменять предположением.

**Группы:**

- `minecraft:time_sword` (строки 206,896,1537,1540,1551): `{"minecraft:movement":{"value":1},"minecraft:type_family":{"family":["player","time_sword"]}}`
- `time_sword_movement` (строки 210,1557,1558): `{"minecraft:movement":{"value":1}}`

**События:**

**`minecraft:time_sword`** (строки 206,896,1537,1540,1551):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"add":{"component_groups":["minecraft:time_sword"]}}`
  - `$.sequence[1]` — поля действия: `{"run_command":{"command":["gamerule randomtickspeed 300","effect @e[type=!player] speed 1 15 true","time add 30","event entity @a[family=default_player] time_sword_movement","fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace air","fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace effect99:lightblock2"]}}`

**`stop_time_sword_event`** (строки 903,1547):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"time_sword"},"remove":{"component_groups":["minecraft:time_sword"]},"add":{"component_groups":["minecraft:default_player"]},"run_command":{"command":["gamerule randomtickspeed 1","effect @e[type=!player] speed 0 0","event entity @a[family=default_player] default_player"]}}`

**`time_sword_movement`** (строки 210,1557,1558):

- `$` — поля действия: `{"add":{"component_groups":["time_sword_movement"]}}`


<a id="sword-creeper_sword"></a>
### 21. Creeper Sword — `effect:creeper_sword`

**Параметры предмета:** блеск foil: нет; левая рука: нет; should_despawn: не указан; digger: web 15, bamboo 10.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** 6. **Прочность:** 1500. **Кулдаун:** 3 с. **Расход применения:** 1. **Зачарование:** есть: value 9, слот sword.
**Ремонт, единиц за материал:** такой же меч: 1500; gunpowder: 256.
**Способности:** При weapon-событии мини-крипер 20%; применение останавливает движение и через 1,5 секунды взрывает игрока с силой 4 и убивает его, расход 1, кулдаун 3 секунды. Мини-крипер: scale 0,3, радиус обнаружения 16, срабатывание рядом с целью на 2,5 или по таймеру 10, взрыв сила 1 с задержкой 1,5. Выброшенный меч устойчив к взрыву по описанию.
**Получение:** зажечь заряженного крипера; записанный таймер на 1,4 и взрыв на 1,5, при срабатывании таймера выбор меча 5 из 100. Порядок таймера и взрыва зависит от движка.
**Условная модель износа weapon-события:** 1: 1/5, 2: 4/5.

**Вход weapon-события:** при попадании с уроном, ударе без урона и ударе по блоку. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Приёмка после разрешения на разработку:** проверить контекст other, призыв мини-крипера, таймер 1,4 и взрыв 1,5 и работу сохранённой структуры.

**Связанный моб:** [заряженный и мини-крипер](#mob-creeper).

**Значок 2.8.8:** `Swords_R/textures/items/creeper_sword.png` (ключ атласа `creeper_sword`; файл сохранён в наборе ресурсов 2.8.8).

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
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
    },
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:cooldown": {
      "category": "creeper_sword",
      "duration": 3
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

#### Записанные группы и события владельца 2.8.8

Это относящиеся к предмету поля игрока из сохранённого реестра, а не утверждение об их выполнении; если старый код расходится с решениями выше (например восстановление настроек мира или блоков), выполнять решение, а не переносить старую ошибку. Пустое или отсутствующее поле не подменять предположением.

**Группы:**

- `start_player_explode_event` (строки 337,2108,2109,2113): `{"minecraft:movement":{"value":0.0},"minecraft:timer":{"time":[1.5,1.5],"looping":true,"time_down_event":{"event":"start_player_explode","target":"self"}}}`

**События:**

**`start_player_explode_event`** (строки 337,2108,2109,2113):

- `$` — поля действия: `{"add":{"component_groups":["start_player_explode_event"]},"run_command":{"command":["playanimation @s animation.player.explode","playsound random.fuse"]}}`

**`start_player_explode`** (строки 340,2112):

- `$` — поля действия: `{"remove":{"component_groups":["start_player_explode_event"]},"add":{"component_groups":["minecraft:default_player"]},"run_command":{"command":["summon entity:instant_creeper_explode ~ ~1 ~","kill @s"]}}`


<a id="sword-fire_sword"></a>
### 22. Fire Sword — `effect:fire_sword`

**Параметры предмета:** блеск foil: да; левая рука: нет; should_despawn: не указан; digger: web 15, bamboo 10.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** 6. **Прочность:** 2000. **Кулдаун:** 25 с. **Расход применения:** 20. **Зачарование:** есть: value 9, слот sword.
**Ремонт, единиц за материал:** такой же меч: 2000; fire: 1000.
**Способности:** Поджигает подходящие сущности в радиусе 3, иммунитет к fire/fire_tick; по решению пользователя других игроков независимо от их формы выбирать для ближнего поджога только при включённом PvP, владельца не выбирать. Это правило выбора цели, а не гарантия поджога или иммунитет к огню других источников; живое пламя при weapon-событии 15%, другая огненная сущность 85%. По решению пользователя пассивное Living Flame, выпущенное мечом, не выбирает владельца и призванных помощников любых игроков целью и не наносит им прямой урон или поджог; это отдельное правило от враждебных естественных форм и огненного дождя. Тает лёд/снег в кубе ±3, свет. Применение создаёт одну цель на y+14 и пять огненных помощников на y+4. Применение — огненный дождь, расход 20, кулдаун 25 секунд. Выброшенный меч: вода → Glass, дождь → Obsidian. Пользователь проверил: при входе игрока в воду меч не исчезает. Проверка самого кода 2.8.8 показала: в цепочке удержания проверка воды и удаление меча не записаны. По решению пользователя в ремейке при входе игрока в воду меч из руки/инвентаря не удалять. В условиях пользовательского испытания версия, слот и другие детали не уточнены.
**Получение:** Живое пламя: в сохранённом событии враждебной, не-снарядной формы выбор 15% на выдачу и 85% без выдачи; событие вызывается при подходящем взаимодействии с игроком или смерти, но не при каждом истечении таймера. Значение 4,9% в описании не заменяет записанные веса. Для враждебной формы записан таймер 25–60 секунд; фактический срок жизни нужно проверить.
**Рецепт:** F / F / #; #=minecraft:blaze_rod, F=minecraft:fire. В описании указан способ получения убийством Living Flame, а этот рецепт — запись кода, не подтверждённый способ получения в выживании. Новые ингредиенты не придумывать.
**Условная модель износа weapon-события:** 1: 1.

**Почему Fire Sword не пропадает при входе в воду — проверка непосредственно исходного кода 2.8.8:**
1. Сенсор `Swords_B/entities/player.json` проверяет `has_equipment` с `domain:hand` и ID `effect:fire_sword` и вызывает `minecraft:fire_sword`; условие `in_water` в этом сенсоре отсутствует. Другой сенсор при отсутствии меча в руке вызывает `stop_fire_sword_event`.
2. Событие удержания добавляет группу Fire и выполняет команды для снега/льда, огненных сущностей и света; оно не содержит проверки воды игрока и команды удаления предмета из руки. Группа защищает от `fire`/`fire_tick` и включает звуковой таймер, но не содержит водного обработчика. При снятии меча stop-событие убирает группу, а не сам предмет. Определение предмета имеет события применения и weapon, но не обработчик входа игрока в воду.
3. Проверка `in_water` находится в `Swords_B/entities/item.json` и применяется к **выброшенной item-сущности** с тегом `fire_sword`, а не к предмету в инвентаре. Она запускает загрузку Glass Sword и `kill @s` для старой item-сущности. При дожде вне воды — отдельная ветка с таймером и Obsidian. Тег проставляется функцией по отображаемому имени, поэтому это не проверка ID.
4. Вывод: в прослеженной цепочке 2.8.8 нет удаления меча при погружении владельца; наблюдение пользователя с этим согласуется. Проверены все 282 текстовых JSON, mcfunction и JS пакета поиском упоминаний Fire и команд работы с инвентарём, а также непосредственно прочитаны связанные объекты player/item и подключённый скрипт. Три буквальные команды replaceitem в player относятся к Sponge и Ice, не к Fire; скрипт обрабатывает только тыквы. Лексический поиск не доказывает отсутствие всех возможных косвенных механизмов или поведения внешних пакетов. По решению пользователя исчезновение Fire Sword при входе игрока в воду в ремейк не добавлять. Это не отменяет превращение выброшенного меча.

**Код оригинала:** `Swords_B/entities/player.json:323–333,696–707,2054–2084`; `Swords_B/entities/item.json:34–51,216–229`; `Swords_B/items/fire_sword.json`; `Swords_B/functions/.../tag_swords.mcfunction:1`; `Swords_B/scripts/javascript.js`. Отчёт [прямой проверки](../data/remake-audits/fire-water-original-2.8.8.json), SHA-256 архива `ab8cbb75c930948f386bf0119bb0a4ee79c084db888c2e9b05deac61b799bb7f`.

**Снаряды weapon-события:** для `entity:fire` базовая запись содержит impact 0, поджог, power 1 и gravity 0,01; при добавлении условной группы Fire Sword вместо неё заданы impact 1, поджог, power 10 и gravity 0,1. Условия добавления группы проверяют экипировку источника; не складывать базовые и условные параметры. У `entity:living_flame` условная группа снаряда задаёт impact 1, поджог, power 1 и gravity 0,02; при попадании событие удаляет снарядную и враждебную группы и добавляет пассивную форму живого пламени. Эти условия и переходы относятся к исходным записям, а не к гарантированному результату каждого выстрела.

**Цели огня:** при удержании селектор `family=!player,type=!item,r=3` не ограничен врагами; изменённая family игрока может пересекаться с фильтром. Применение создаёт одну цель на y+14 и пять огненных помощников на y+4; они стреляют в эту цель, а не автоматически в пять врагов. Параметры живого пламени и получение Fire — [Living Flame](#mob-living-flame).

**Выброшенный предмет:** Fire в воде → Glass; дождь вне воды → Obsidian после таймера 5–6; прекращение дождя до срабатывания отменяет таймер. Это исправленное пользователем соответствие. При горении выброшенного Fire с обычным тегом в отдельном событии записаны девять частиц пламени, пять призывов враждебного Living Flame, звук и уничтожение item-сущности. Отдельный тег `fire_sword_respawn` ведёт к загрузке структуры вместо этой ветви; исполнение и сохранение состояния проверить.

**Вход weapon-события:** при попадании с уроном, ударе без урона и ударе по блоку. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Приёмка после разрешения на разработку:** не удалять меч при погружении игрока; проверить отдельно преобразования выброшенного предмета и рецепт с fire.

**Значок 2.8.8:** `Swords_R/textures/items/fire_sword.png` (ключ атласа `fire_sword`; файл сохранён в наборе ресурсов 2.8.8).

**Область действия:** таймер удержания/команды выбирают `family=!player,type=!item,r=3` и поджигают подходящих сущностей; семейство и тип — разные фильтры, игрок с изменённой family может совпасть. Блоки снега и льда меняются в кубе ±3; точные старые ID и их условия приведены в цепочке событий предмета. Свет и огненный дождь не означают автоматический выбор пяти врагов.

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
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
    },
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:cooldown": {
      "category": "fire_sword",
      "duration": 25
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

#### Записанные группы и события владельца 2.8.8

Это относящиеся к предмету поля игрока из сохранённого реестра, а не утверждение об их выполнении; если старый код расходится с решениями выше (например восстановление настроек мира или блоков), выполнять решение, а не переносить старую ошибку. Пустое или отсутствующее поле не подменять предположением.

**Группы:**

- `minecraft:fire_sword` (строки 323,700,2054,2058,2079): `{"minecraft:timer":{"time":[0.2,0.7],"looping":true,"randomInterval":true,"time_down_event":{"event":"fire_sword_sound","target":"self"}},"minecraft:damage_sensor":{"triggers":{"on_damage":{"filters":{"any_of":[{"test":"has_damage","subject":"self","value":"fire"},{"test":"has_damage","subject":"self","value":"fire_tick"}]}},"deals_damage":false}},"minecraft:type_family":{"family":["player","fire_sword"]}}`

**События:**

**`minecraft:fire_sword`** (строки 323,700,2054,2058,2079):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"fire_sword"},"add":{"component_groups":["minecraft:fire_sword"]}}`
  - `$.sequence[1]` — поля действия: `{"run_command":{"command":["fill ~3 ~3 ~3 ~-3 ~-3 ~-3 air 0 replace snow_layer","fill ~3 ~3 ~3 ~-3 ~-3 ~-3 water 0 replace ice","fill ~3 ~3 ~3 ~-3 ~-3 ~-3 water 0 replace blue_ice","fill ~3 ~3 ~3 ~-3 ~-3 ~-3 water 0 replace packed_ice","execute @e[family=!player,type=!item,r=3] ~ ~ ~ summon entity:fire","fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock 0 replace air","fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock 0 replace effect99:lightblock"]}}`

**`stop_fire_sword_event`** (строки 707,2075):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"fire_sword"},"remove":{"component_groups":["minecraft:fire_sword"]},"add":{"component_groups":["minecraft:default_player"]}}`

**`fire_sword_sound`** (строки 325,2084):

- `$` — поля действия: `{"run_command":{"command":["playsound fire.fire @a[r=8]"]}}`


<a id="sword-magma_sword"></a>
### 23. Magma Sword — `effect:magma_sword`

**Параметры предмета:** блеск foil: нет; левая рука: нет; should_despawn: не указан; digger: web 15, bamboo 10.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** 7.2. **Прочность:** 1316. **Кулдаун:** не указан. **Расход применения:** не указан. **Зачарование:** есть: value 9, слот sword.
**Ремонт, единиц за материал:** такой же меч: 1316; magma: 100.
**Способности:** при удержании damage sensor отменяет `fire_tick` и урон от блока с ID `magma`; отмена лавы и любого урона `fire` не записана. Пять fill заменяют `lava` на `magma` на y−1: центр, прямоугольник от (1,1) до (0,0), отдельные точки (0,1), (−1,0), (0,−1); это шесть различных координат с перекрытиями, а не гарантированное число замен. Дополнительно записана ветка звука `bubble.up` с весом 1/100 при `in_water` без value: согласно сохранённой современной официальной документации value по умолчанию равно true, subject — self. Следовательно, для ремейка это условная попытка звука при нахождении владельца в воде; частота вызова события и фактическое исполнение старым движком не установлены.
**Получение:** Большие подводные руины.
**Пулы добычи:** большие подводные руины — 1 выбор, 1/24. Доли — вес записи на один выбор, не шанс всего сундука или любой рыбалки.
**Условная модель износа weapon-события:** 1: 1.

**Вход weapon-события:** только при попадании по сущности с уроном. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Значок 2.8.8:** `Swords_R/textures/items/magma_sword.png` (ключ атласа `magma_sword`; файл сохранён в наборе ресурсов 2.8.8).

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
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

#### Записанные группы и события владельца 2.8.8

Это относящиеся к предмету поля игрока из сохранённого реестра, а не утверждение об их выполнении; если старый код расходится с решениями выше (например восстановление настроек мира или блоков), выполнять решение, а не переносить старую ошибку. Пустое или отсутствующее поле не подменять предположением.

**Группы:**

- `minecraft:magma_sword` (строки 305,742,1961,1965,1996): `{"minecraft:damage_sensor":{"triggers":{"on_damage":{"filters":{"any_of":[{"test":"has_damage","subject":"self","value":"fire_tick"},{"test":"is_block","subject":"block","operator":"equals","value":"magma"}]}},"deals_damage":false}},"minecraft:type_family":{"family":["player","magma_sword"]}}`

**События:**

**`minecraft:magma_sword`** (строки 305,742,1961,1965,1996):

- `$.sequence`: 3 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"magma_sword"},"add":{"component_groups":["minecraft:magma_sword"]}}`
  - `$.sequence[1]` — поля действия: `{"run_command":{"command":["fill ~ ~-1 ~ ~ ~-1 ~ magma 0 replace lava","fill ~1 ~-1 ~1 ~ ~-1 ~ magma 0 replace lava","fill ~ ~-1 ~1 ~ ~-1 ~1 magma 0 replace lava","fill ~-1 ~-1 ~ ~-1 ~-1 ~ magma 0 replace lava","fill ~ ~-1 ~-1 ~ ~-1 ~-1 magma 0 replace lava","execute @s ~ ~1 ~ particle minecraft:guardian_attack_particle ^-0.4 ^ ^0.2"]}}`
  - `$.sequence[2]` — поля действия: `{"filters":{"test":"in_water","operator":"=="}}`
  - `$.sequence[2].randomize`: альтернативы, веса `[99,1]`, сумма 100:
    - ветвь 0, weight `99`; условная доля 99/100 (99%):
      - пустое действие
    - ветвь 1, weight `1`; условная доля 1/100 (1%):
      - `$.sequence[2].randomize[1]` — поля действия: `{"run_command":{"command":["playsound bubble.up @a ~ ~ ~ 1 0.9"]}}`

**`stop_magma_sword_event`** (строки 749,1992):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"magma_sword"},"remove":{"component_groups":["minecraft:magma_sword"]},"add":{"component_groups":["minecraft:default_player"]}}`


<a id="sword-wither_sword"></a>
### 24. Wither Sword — `effect:wither_sword`

**Параметры предмета:** блеск foil: да; левая рука: нет; should_despawn: false; digger: web 15, bamboo 10.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** 10. **Прочность:** 3856. **Кулдаун:** 3 с. **Расход применения:** 3. **Зачарование:** компонент не указан.
**Ремонт, единиц за материал:** такой же меч: 3856.
**Способности:** При weapon-событии обычный череп визера 10%; применение — опасный череп. В обоих записан Wither II с duration easy/normal/hard 0/200/800 и взрывом power 1; опасный имеет max resistance 4. Защита от Wither; в кубе ±5 листья и лозы исчезают, цветы становятся визер-розами, трава и грядки — землёй, лёд — водой. Свет, декоративная шкала босса и безвредный визуальный эффект Wither. Применение: опасный череп, расход 3, кулдаун 3 секунды.
**Получение:** фатальный удар игрока с Nether Star Sword по Wither запускает выбор 13 из 100 на меч.
**Условная модель износа weapon-события:** 1: 1.

**Выброшенный предмет:** при огне вызывается событие удаления предмета, несмотря на should_despawn:false; это разные механизмы.

**Положение в основной руке:** первое лицо `{"position":[0.8,0.1,-1.8],"scale":[0.01,0.01,0.01]}`; третье лицо `{"position":[0.8,2.5,-1.2],"scale":[0.027,0.027,0.027]}`. Неуказанные поля не заменять нулями; фактический вид проверить на целевой версии.

**Вход weapon-события:** при попадании с уроном, ударе без урона и ударе по блоку. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Приёмка после разрешения на разработку:** не отменять согласованное разрушение блоков; отдельно проверить урон, длительность, отображение и очистку эффектов.

**Значок 2.8.8:** `Swords_R/textures/items/wither_sword.png` (ключ атласа `wither_sword`; файл сохранён в наборе ресурсов 2.8.8).

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
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
    },
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:cooldown": {
      "category": "wither_sword",
      "duration": 3
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

#### Записанные группы и события владельца 2.8.8

Это относящиеся к предмету поля игрока из сохранённого реестра, а не утверждение об их выполнении; если старый код расходится с решениями выше (например восстановление настроек мира или блоков), выполнять решение, а не переносить старую ошибку. Пустое или отсутствующее поле не подменять предположением.

**Группы:**

- `minecraft:wither_sword` (строки 191,910,1492,1496,1525): `{"minecraft:rideable":{"seat_count":1,"family_types":["entity_name"],"seats":{"position":[0.0,0.4,0.0],"lock_rider_rotation":0}},"minecraft:damage_sensor":{"triggers":{"on_damage":{"filters":{"all_of":[{"test":"has_damage","subject":"self","value":"wither"}]}},"deals_damage":false}},"minecraft:timer":{"time":[4,18],"looping":true,"randomInterval":true,"time_down_event":{"event":"wither_sword_effects","target":"self"}},"minecraft:type_family":{"family":["player","wither_sword"]}}`

**События:**

**`minecraft:wither_sword`** (строки 191,910,1492,1496,1525):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"wither_sword"},"add":{"component_groups":["minecraft:wither_sword"]},"run_command":{"command":["playsound mob.wither.spawn @a[r=16]"]}}`
  - `$.sequence[1]` — поля действия: `{"run_command":{"command":["fill ~5 ~5 ~5 ~-5 ~-5 ~-5 dirt 1 replace grass","fill ~5 ~5 ~5 ~-5 ~-5 ~-5 air 0 replace leaves2","fill ~5 ~5 ~5 ~-5 ~-5 ~-5 air 0 replace leaves","fill ~5 ~5 ~5 ~-5 ~-5 ~-5 air 0 replace vine","fill ~5 ~5 ~5 ~-5 ~-5 ~-5 water 0 replace ice","fill ~5 ~5 ~5 ~-5 ~-5 ~-5 dirt 0 replace farmland","fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace red_flower","fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace yellow_flower","fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace red_mushroom","fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace brown_mushroom","fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace double_plant","effect @s wither 39960 1 true","fill ~1 ~2 ~1 ~-1 ~2 ~-1 effect99:lightblock2 0 replace air","fill ~1 ~2 ~1 ~-1 ~2 ~-1 effect99:lightblock2 0 replace effect99:lightblock2"]}}`

**`stop_wither_sword_event`** (строки 917,1521):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"wither_sword"},"remove":{"component_groups":["minecraft:wither_sword"]},"add":{"component_groups":["minecraft:default_player"]},"run_command":{"command":["effect @s wither 0 0","ride @s evict_riders"]}}`

**`wither_sword_effects`** (строки 202,1531):

- `$.randomize`: альтернативы, веса `[50,50]`, сумма 100:
  - ветвь 0, weight `50`; условная доля 1/2 (50%):
    - `$.randomize[0]` — поля действия: `{"run_command":{"command":["playsound mob.wither.death @a[r=16]"]}}`
  - ветвь 1, weight `50`; условная доля 1/2 (50%):
    - `$.randomize[1]` — поля действия: `{"run_command":{"command":["playsound mob.wither.hurt @a[r=16]"]}}`


<a id="sword-tnt_sword"></a>
### 25. TNT Sword — `effect:tnt_sword`

**Параметры предмета:** блеск foil: нет; левая рука: нет; should_despawn: не указан; digger: компонент не указан.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** 4. **Прочность:** 64. **Кулдаун:** 10 с. **Расход применения:** 18. **Зачарование:** есть: value 9, слот sword.
**Ремонт, единиц за материал:** такой же меч: 64; tnt: 18.
**Способности:** weapon-событие выбирает малый взрывной снаряд с весом 90 из 100, сила взрыва 1; при применении большой TNT взрывается через 8 секунд, сила 16, огонь включён, расход 18, кулдаун 10 секунд; выброшенный в огонь взрывается.
**Получение:** Сундуки пустынного храма.
**Пулы добычи:** пустынный храм — 2–4 выбора, 10/242. Доли — вес записи на один выбор, не шанс всего сундука или любой рыбалки.
**Условная модель износа weapon-события:** 1: 1.

**Малый снаряд `entity:tnt`:** при попадании impact 1 с отбрасыванием и взрыв power 1 без огня; projectile power 2, gravity 0. Одновременно исходный таймер `[0,1;0,1]` с вызывает удаление: одно только срабатывание 90%-ветви не гарантирует попадание и взрыв. Взрыв зависит от правил разрушения согласно `destroy_affected_by_griefing: true`.

**Выброшенный предмет:** при огне взрыв power 16, fire true, fuse 0,02 и уничтожение предмета.

**Вход weapon-события:** при попадании с уроном, ударе без урона и ударе по блоку. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Приёмка после разрешения на разработку:** сохранить согласованное разрушение; проверить действие правил мира, урон и отдельные виды взрыва.

**Значок 2.8.8:** `Swords_R/textures/items/tnt_sword.png` (ключ атласа `tnt_sword`; файл сохранён в наборе ресурсов 2.8.8).

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
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
    },
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:cooldown": {
      "category": "tnt_sword",
      "duration": 10
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

<a id="sword-lightning_sword"></a>
### 26. Lightning Sword — `effect:lightning_sword`

**Параметры предмета:** блеск foil: да; левая рука: нет; should_despawn: не указан; digger: web 15, bamboo 10.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** 8. **Прочность:** 2012. **Кулдаун:** 12 с. **Расход применения:** 9. **Зачарование:** есть: value 9, слот sword.
**Ремонт, единиц за материал:** такой же меч: 2012.
**Способности:** weapon-событие выбирает снаряд молнии с весом 85 из 100; применение вызывает 41 молнию, расход 9, кулдаун 12 секунд; иммунитет к молнии, но не огню; свет.
**Получение:** при обычном событии появления молнии выбор Centella с весом 20/100 без записанной проверки грозы. Молнии, создаваемые самим мечом и гибелью Centella с событием `default_lightning_bolt`, не запускать этот выбор: в тесте оригинала из 25 таких молний Centella не появилась, а из 25 вызванных без специального события появилась 6 раз. Это выборка, а не измерение точного шанса. Смертельный удар игрока по Centella запускает отдельный выбор меча 2/100; подробности — [Centella](#mob-centella).
**Условная модель износа weapon-события:** 1: 1.

**Снаряд `entity:lightning_projectile`:** power 2, gravity 0, impact 1, timer `[0,1;0,1]` с удалением; при попадании вызывает молнию. Попадание до удаления не гарантировано. Environment sensor ссылается на локально отсутствующий event `particle`. Условия двух событий смерти и поведения источника меча указаны в пункте [Centella](#mob-centella).

#### Форма призыва молний

Относительно владельца: центр `(0,+2,0)`, затем на высоте y=0 пять комплектов по восемь точек. Каждый комплект состоит из четырёх осевых `(±a,0)`, `(0,±a)` и четырёх диагональных `(±d,±d)` по x/z, независимо выбирая знаки. Пары `(a,d)`: `(7,6)`, `(14,12)`, `(28,24)`, `(34,30)`, `(42,38)`. Это 1 + 5×8 = 41, не круговой радиус поражения. Эти 41 молния в исходном коде вызываются с событием `default_lightning_bolt`; в ремейке они не должны запускать выбор Centella.

**Выброшенный предмет:** при попадании выброшенного Lightning Sword в огонь один раз вызвать молнию в его позиции и уничтожить предмет; не создавать из этой молнии Centella. Идентифицировать меч по ID, а не по отображаемому имени. В испытании оригинала 2.8.8 на Bedrock 1.20.50 самостоятельно полученный тег у выброшенного меча не обнаружился: без тега в двух повторениях меч сгорел без молнии. При ручном назначении исходного тега `lightning_sword` в трёх повторениях каждый меч вызвал по одной молнии и исчез в огне. Контрольная палка тоже сгорела. Пользователь проверил в настоящем клиенте с оригиналом 2.8.8: дважды при попадании выброшенного меча в огонь в этом месте ударила молния, а меч исчез; причина исчезновения — сгорание или иное удаление — отдельно не определена. Это наблюдение не доказывает, какой именно механизм назначил тег. В исходном событии нет явной команды удаления.

**Положение в основной руке:** первое лицо `{"position":[1,0.4,-3],"scale":[0.04,0.04,0.04]}`; третье лицо `{"position":[0.7,2.2,-1],"scale":[0.05,0.05,0.05]}`. Неуказанные поля не заменять нулями; фактический вид проверить на целевой версии.

**Вход weapon-события:** при попадании с уроном, ударе без урона и ударе по блоку. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Значок 2.8.8:** `Swords_R/textures/items/lightning_sword.png` (ключ атласа `lightning_sword`; файл сохранён в наборе ресурсов 2.8.8).

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
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
    },
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:cooldown": {
      "category": "lightning_sword",
      "duration": 12
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

#### Записанные группы и события владельца 2.8.8

Это относящиеся к предмету поля игрока из сохранённого реестра, а не утверждение об их выполнении; если старый код расходится с решениями выше (например восстановление настроек мира или блоков), выполнять решение, а не переносить старую ошибку. Пустое или отсутствующее поле не подменять предположением.

**Группы:**

- `minecraft:lightning_sword` (строки 184,931,1468,1472,1484): `{"minecraft:damage_sensor":{"triggers":{"on_damage":{"filters":{"all_of":[{"test":"is_family","subject":"other","value":"lightning"}]}},"deals_damage":false}},"minecraft:type_family":{"family":["player","lightning_sword"]}}`

**События:**

**`minecraft:lightning_sword`** (строки 184,931,1468,1472,1484):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"lightning_sword"},"add":{"component_groups":["minecraft:lightning_sword"]},"run_command":{"command":["summon lightning_bolt ~ 255 ~ default_lightning_bolt"]}}`
  - `$.sequence[1]` — поля действия: `{"run_command":{"command":["fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace air","fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace effect99:lightblock2"]}}`

**`stop_lightning_sword_event`** (строки 938,1480):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"lightning_sword"},"remove":{"component_groups":["minecraft:lightning_sword"]},"add":{"component_groups":["minecraft:default_player"]}}`


<a id="sword-sponge_sword"></a>
### 27. Sponge Sword — `effect:sponge_sword`

**Параметры предмета:** блеск foil: нет; левая рука: нет; should_despawn: не указан; digger: web 15, bamboo 10.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** 5. **Прочность:** 128. **Кулдаун:** не указан. **Расход применения:** не указан. **Зачарование:** компонент не указан.
**Ремонт, единиц за материал:** такой же меч: 128; sponge: 62.
**Способности:** обрабатывает куб ±2 блока, включая воду и водоросли, не уничтожая существовавшие блоки губки. По решению пользователя, как в оригинале, вода поглощается только при нахождении владельца в воде или под дождём. Вода или дождь запускают счётчик; по решению пользователя сохранять исходный порог 150 срабатываний, а не заменять его числом секунд. В оригинале также записаны проверки счёта 155 и 160. Выброшенная губка в воде или под дождём имеет отдельный таймер 0–1. Компонент зачарования в заметках отсутствует, текст говорит true; это не доказательство запрета или разрешения движка.
**Получение:** при убийстве древнего стража игроком выдавать меч с шансом 6,5% плюс 2 процентных пункта за уровень Looting, сохраняя обычную добычу; явно связать правило с древним стражем. Другой путь — переплавка [Wet Sponge Sword](#sword-wet_sponge_sword).
**Рецепт:** effect:wet_sponge_sword → effect:sponge_sword (furnace, blast_furnace).
**Условная модель износа weapon-события:** 1: 1.

**Sponge:** исходный код удаляет воду в кубе 5 × 5 × 5 только при `in_water_or_rain` владельца; удаление водорослей записано в отдельном шаге без этого фильтра. В описании сказано поглощение воды в радиусе 2 без оговорки о нахождении владельца в воде или под дождём; по выбору пользователя для воды сохранять исходное условие `in_water_or_rain`. Счёт увеличивается при воде или дожде без проверки числа обработанных блоков; при счёте 150 меч становится мокрым, при сохранении исходных резервных проверок 155 и 160. Исходный счёт относится к игроку, не к конкретному экземпляру меча; событие снятия не сбрасывает его, а событие превращения в Wet сбрасывает на 0. По решению пользователя ранее существовавшие блоки губки сохранять; исходную команду удаления любой губки не переносить. Выброшенный предмет использует независимый таймер, не счётчик игрока.

**Выброшенный предмет:** Выброшенный Sponge при воде/дожде отдельно обрабатывает воду и водоросли в кубе ±2 и использует таймер 0–1 с для превращения в Wet Sponge. По выбранному правилу ранее существовавшие губки сохранять и при этом варианте; исходная команда удаляет все губки в кубе. Удерживаемый меч использует счётчик 150/155/160, а не этот таймер.

**Вход weapon-события:** только при попадании по сущности с уроном. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Looting:** при реально переданных уровнях 0/1/2/3 условные шансы записанной ветви — 6,5%, 8,5%, 10,5%, 12,5%. Множитель 0,02 добавляет 2 п.п. за уровень; не доказывает подключение таблицы или успешность события.

**Привязка добычи:** соответствующая ванильная сущность в образце Mojang v1.26.60.5 указывает путь таблицы, совпадающий с сохранённым путём аддона. Это совпадение путей, а не доказательство загрузки таблицы в конкретном мире или выдачи меча; сохранить ванильную добычу.

**Приёмка после разрешения на разработку:** проверить пересечение с существующими губками, счётчик/дождь и сохранение состояния предмета.

**Значок 2.8.8:** `Swords_R/textures/items/sponge_sword.png` (ключ атласа `sponge_sword`; файл сохранён в наборе ресурсов 2.8.8).

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
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

#### Записанные группы и события владельца 2.8.8

Это относящиеся к предмету поля игрока из сохранённого реестра, а не утверждение об их выполнении; если старый код расходится с решениями выше (например восстановление настроек мира или блоков), выполнять решение, а не переносить старую ошибку. Пустое или отсутствующее поле не подменять предположением.

**Группы:**

- `minecraft:sponge_sword` (строки 213,882,1560,1564,1603): `{"minecraft:type_family":{"family":["player","sponge_sword"]}}`

**События:**

**`minecraft:sponge_sword`** (строки 213,882,1560,1564,1603):

- `$.sequence`: 3 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"sponge_sword"},"add":{"component_groups":["minecraft:sponge_sword"]},"run_command":{"command":["scoreboard objectives add sponge_sword dummy"]}}`
  - `$.sequence[1]` — поля действия: `{"filters":{"test":"in_water_or_rain"},"run_command":{"command":["fill ~2 ~2 ~2 ~-2 ~-2 ~-2 sponge 0 replace water","playsound random.fizz @a[r=12] ~~~ 0.6","particle minecraft:cauldron_explosion_emitter ~ ~ ~","scoreboard players add @s sponge_sword 1"]}}`
  - `$.sequence[2]` — поля действия: `{"run_command":{"command":["fill ~2 ~2 ~2 ~-2 ~-2 ~-2 air 0 replace sponge","fill ~2 ~2 ~2 ~-2 ~-2 ~-2 air 0 replace seagrass","execute @s[scores={sponge_sword=150}] ~ ~ ~ event entity @s wet_sponge_sword","execute @s[scores={sponge_sword=155}] ~ ~ ~ event entity @s wet_sponge_sword","execute @s[scores={sponge_sword=160}] ~ ~ ~ event entity @s wet_sponge_sword"]}}`

**`wet_sponge_sword`** (строки 1591):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:sponge_sword"},"run_command":{"command":["replaceitem entity @s slot.weapon.mainhand 0 effect:wet_sponge_sword 1","scoreboard players set @s sponge_sword 0","title @s actionbar §l§gWet Sponge Sword"]}}`

**`stop_sponge_sword_event`** (строки 889,1599):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"sponge_sword"},"remove":{"component_groups":["minecraft:sponge_sword"]},"add":{"component_groups":["minecraft:default_player"]}}`


<a id="sword-bone_sword"></a>
### 28. Skeleton Bone Sword — `effect:bone_sword`

**Параметры предмета:** блеск foil: нет; левая рука: нет; should_despawn: не указан; digger: web 15, bamboo 10.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** 5. **Прочность:** 820. **Кулдаун:** не указан. **Расход применения:** не указан. **Зачарование:** есть: value 9, слот sword.
**Ремонт, единиц за материал:** такой же меч: 820; bone: 70; bone block: 300; bone meal: 18.
**Способности:** При атаке стрела 20%; рост растений в радиусе 2, замедление стрел в радиусе 8.
**Получение:** смертельный удар игрока по скелету в биоме desert при brightness < 0,49 запускает выбор 7 из 1000 на меч; по решению пользователя реальный игрок считается игроком и при превращении, не теряя возможности этой попытки. Условие освещённости не является прямой проверкой ночи. В описании упомянута ночь; по решению пользователя сохранить условие освещённости из кода без отдельной проверки ночи.
**Условная модель износа weapon-события:** 1: 1/5, 2: 4/5.

**Bone:** weapon-событие на удар с уроном, удар без урона и удар по блоку выбирает стрелу с шансом 20/100. По решению пользователя при удержании обрабатывать стрелы family arrow в радиусе 8, если источник неизвестен или является враждебным мобом; при включённом PvP добавляются стрелы других игроков; собственные стрелы владельца не обрабатывать независимо от PvP. По решению пользователя менять движение по параметрам исходной группы, без гарантии непроницаемого барьера. В коде 2.8.8 выбираются все стрелы без фильтра владельца. В актуальной документации Script API есть читаемое правило мира `gameRules.pvp` и необязательный `owner` у снаряда; сам факт наличия поля не гарантирует владельца у каждого снаряда. Для выбранных стрел использовать параметры движения исходной группы power 0, gravity 1, inertia 0, liquid inertia 0; не подменять изменение движения удалением стрел. Рост реализовать по исходной схеме: каждую секунду запускать помощника, который каждые 0,3 с создаёт помощников роста в 13 точках — центр, восемь соседей и четыре оси расстояния 2; дочерние помощники не запускают эту цепочку заново. Компонент роста имеет chance 0,5 и charges 10, время жизни помощника 1 в записанных единицах; не заменять эти значения выдуманной фиксированной скоростью роста.

**Вход weapon-события:** при попадании с уроном, ударе без урона и ударе по блоку. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Значок 2.8.8:** `Swords_R/textures/items/bone_sword.png` (ключ атласа `bone_sword`; файл сохранён в наборе ресурсов 2.8.8).

**Рост и стрелы в исходнике:** при удержании всем сущностям `family=arrow` в r=8 отправляется `minecraft:inertia_disable`, не только стрелам владельца. Таймер `[1,1]` с создаёт `entity:grows_crop` на y+0,1 с событием `grows_crop_event`. Помощник имеет ageable duration 1 и `minecraft:grows_crop` chance 0,5/charges 10; его таймер `[0,3;0,3]` создаёт 13 точек: центр, восемь соседей ±1 и четыре осевые точки на расстоянии 2. Дочерние вызовы не передают `grows_crop_event`; рекурсия и реальное число выросших растений не доказаны.

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
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

#### Записанные группы и события владельца 2.8.8

Это относящиеся к предмету поля игрока из сохранённого реестра, а не утверждение об их выполнении; если старый код расходится с решениями выше (например восстановление настроек мира или блоков), выполнять решение, а не переносить старую ошибку. Пустое или отсутствующее поле не подменять предположением.

**Группы:**

- `minecraft:bone_sword` (строки 349,658,2136,2140,2153): `{"minecraft:type_family":{"family":["player","bone_sword"]},"minecraft:timer":{"time":[1,1],"looping":true,"time_down_event":{"event":"bone_sword_skills","target":"self"}}}`

**События:**

**`minecraft:bone_sword`** (строки 349,658,2136,2140,2153):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"bone_sword"},"add":{"component_groups":["minecraft:bone_sword"]}}`
  - `$.sequence[1]` — поля действия: `{"run_command":{"command":["event entity @e[family=arrow,r=8] minecraft:inertia_disable"]}}`

**`stop_bone_sword_event`** (строки 665,2149):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"bone_sword"},"remove":{"component_groups":["minecraft:bone_sword"]},"add":{"component_groups":["minecraft:default_player"]}}`

**`bone_sword_skills`** (строки 352,2158):

- `$` — поля действия: `{"run_command":{"command":["summon entity:grows_crop ~ ~0.1 ~ grows_crop_event"]}}`


<a id="sword-quartz_sword"></a>
### 29. Quartz Diamond Sword — `effect:quartz_sword`

**Параметры предмета:** блеск foil: да; левая рука: нет; should_despawn: не указан; digger: web 15, bamboo 10.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** 600. **Прочность:** 1. **Кулдаун:** не указан. **Расход применения:** не указан. **Зачарование:** компонент не указан.
**Ремонт, единиц за материал:** компонент не указан.
**Способности:** Урон 600 и прочность 1; при взятии/снятии записан magic-урон 14 владельцу, а событие weapon записывает instant damage 1 с усилителем 99 всем игрокам в радиусе 1, а не только владельцу. По решению пользователя в ремейке эффект также распространяется на всех игроков в радиусе 1. По решению пользователя входы и последовательность weapon брать из кода: попадание с уроном, удар без урона по сущности и удар по блоку; сначала износ 10, затем выполнить эффект и частицу, даже если на первом шаге меч сломался: это заданная последовательность способности, а не условие повторной проверки наличия меча. Не подменять эффект безусловным убийством: защита и режим игры учитываются обычными правилами.
**Получение:** Два блока кварц-алмаза над кварц-алмазной палкой.
**Рецепт:** Q / Q / #; #=effect:quartz_diamond_stick, Q=effect99:quartz_diamond_block.
**Условная модель износа weapon-события:** 10: 1.

**Положение в основной руке:** первое лицо `{"position":[1.0,0,-2],"scale":[0.07,0.07,0.07]}`; третье лицо `{"position":[0.2,1.1,-0.5],"scale":[0.08,0.08,0.08]}`. Неуказанные поля не заменять нулями; фактический вид проверить на целевой версии.

**Вход weapon-события:** при попадании с уроном, ударе без урона и ударе по блоку. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Расход материалов:** при одном результате каждого рецепта нужно 20 кварц-алмазов: 18 на два блока и два на палку; наличие ресурсов и крафт проверить.

**Значок 2.8.8:** `Swords_R/textures/items/quartz_sword.png` (ключ атласа `quartz_sword`; файл сохранён в наборе ресурсов 2.8.8).

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
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

#### Записанные группы и события владельца 2.8.8

Это относящиеся к предмету поля игрока из сохранённого реестра, а не утверждение об их выполнении; если старый код расходится с решениями выше (например восстановление настроек мира или блоков), выполнять решение, а не переносить старую ошибку. Пустое или отсутствующее поле не подменять предположением.

**Группы:**

- `minecraft:quartz_sword` (строки 283,798,1864,1869,1878): `{"minecraft:type_family":{"family":["player","quartz_sword"]}}`

**События:**

**`minecraft:quartz_sword`** (строки 283,798,1864,1869,1878):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"quartz_sword"},"run_command":{"command":["damage @s 14 magic"]},"add":{"component_groups":["minecraft:quartz_sword"]}}`

**`stop_quartz_sword_event`** (строки 805,1873):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"quartz_sword"},"run_command":{"command":["damage @s 14 magic"]},"remove":{"component_groups":["minecraft:quartz_sword"]},"add":{"component_groups":["minecraft:default_player"]}}`


<a id="sword-bedrock_sword"></a>
### 30. Bedrock Sword — `effect:bedrock_sword`

**Параметры предмета:** блеск foil: нет; левая рука: нет; should_despawn: false; digger: 68 отдельных правил, см. раздел Bedrock Sword ниже.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** 18. **Прочность:** бесконечная по игровой задумке; в настройке значение не указано. **Кулдаун:** не указан. **Расход применения:** не указан. **Зачарование:** компонент не указан.
**Ремонт, единиц за материал:** компонент не указан.
**Способности:** Урон 18, бесконечная прочность по игровой задумке; скорость добычи 999 для указанных категорий, 50 для блока кварц-алмаза и 100 для его руды, с возможным перекрытием категорий; мощная кирка; выброшенный предмет не должен исчезать и устойчив к взрыву по описанию.
**Получение:** два блока бедрока над бедроковой палкой. По решению пользователя бедрок, разрушенный снарядом Ultra Instinct или взрывом выброшенного в огонь Nether Star Sword, выпадает как блок; для меча вместе с палкой требуется четыре блока.
**Рецепт:** B / B / #; #=effect:bedrock_stick, B=minecraft:bedrock.
**Условная модель износа weapon-события:** компонент weapon пуст; явного события износа не записано.

#### Все 68 правил добычи

Ниже — буквальная последовательность 68 правил из сохранённого индекса 2.8.8, не перечень подтверждённых современных ID. Скорость в компоненте — не время разрушения. Приоритет пересекающихся правил в исходном движке не установлен; для ремейка пользователь выбрал приоритет точного ID, см. границу списка ниже. Записи `pumkin` и повторённые строки сохранены для проверки, не как рекомендация переносить опечатку. Поддержку `use_efficiency` и выход ресурсов проверять при приёмке.

| № | Блок / условие | Остальные поля правила |
|---:|---|---|
| 1 | `{"tags":"q.any_tag('stone', 'metal', 'diamond_pick_diggable', 'wood', 'pumpkin', 'plant', 'dirt', 'sand', 'gravel', 'grass', 'snow')"}` | `{"speed":999}` |
| 2 | `"effect99:quartz_diamond_block"` | `{"speed":50}` |
| 3 | `"effect99:quartz_diamond_ore"` | `{"speed":100}` |
| 4 | `"effect99:silver_ore"` | `{"speed":999}` |
| 5 | `"minecraft:warped_wart_block"` | `{"speed":999}` |
| 6 | `"minecraft:nether_wart_block"` | `{"speed":999}` |
| 7 | `"minecraft:leaves"` | `{"speed":999}` |
| 8 | `"minecraft:leaves2"` | `{"speed":999}` |
| 9 | `"minecraft:hay_block"` | `{"speed":999}` |
| 10 | `"minecraft:soul_soil"` | `{"speed":999}` |
| 11 | `"minecraft:soul_sand"` | `{"speed":999}` |
| 12 | `"minecraft:chest"` | `{"speed":999}` |
| 13 | `"minecraft:melon_block"` | `{"speed":999}` |
| 14 | `"minecraft:bookshelf"` | `{"speed":999}` |
| 15 | `"minecraft:lectern"` | `{"speed":999}` |
| 16 | `"minecraft:pumkin"` | `{"speed":999}` |
| 17 | `"minecraft:ice"` | `{"speed":999}` |
| 18 | `"minecraft:bone_block"` | `{"speed":999}` |
| 19 | `"minecraft:mob_spawner"` | `{"speed":999}` |
| 20 | `"minecraft:anvil"` | `{"speed":999}` |
| 21 | `"minecraft:netherite_block"` | `{"speed":999}` |
| 22 | `"minecraft:sandstone"` | `{"speed":999}` |
| 23 | `"minecraft:diamond_block"` | `{"speed":999}` |
| 24 | `"minecraft:lapis_block"` | `{"speed":999}` |
| 25 | `"minecraft:emerald_block"` | `{"speed":999}` |
| 26 | `"minecraft:ancient_debris"` | `{"speed":999}` |
| 27 | `"minecraft:cracked_polished_blackstone_bricks"` | `{"speed":999}` |
| 28 | `"minecraft:nether_brick"` | `{"speed":999}` |
| 29 | `"minecraft:cracked_nether_bricks"` | `{"speed":999}` |
| 30 | `"minecraft:quartz_ore"` | `{"speed":999}` |
| 31 | `"minecraft:netherrack"` | `{"speed":999}` |
| 32 | `"minecraft:basalt"` | `{"speed":999}` |
| 33 | `"minecraft:end_bricks"` | `{"speed":999}` |
| 34 | `"minecraft:purpur_block"` | `{"speed":999}` |
| 35 | `"minecraft:purpur_stairs"` | `{"speed":999}` |
| 36 | `"minecraft:end_brick_stairs"` | `{"speed":999}` |
| 37 | `"minecraft:stone_slab2"` | `{"speed":999}` |
| 38 | `"minecraft:stone_slab3"` | `{"speed":999}` |
| 39 | `"minecraft:polished_basalt"` | `{"speed":999}` |
| 40 | `"minecraft:warped_nylium"` | `{"speed":999}` |
| 41 | `"minecraft:crimson_nylium"` | `{"speed":999}` |
| 42 | `"minecraft:end_stone"` | `{"speed":999}` |
| 43 | `"minecraft:ender_chest"` | `{"speed":999}` |
| 44 | `"minecraft:quartz_block"` | `{"speed":999}` |
| 45 | `"minecraft:quartz_stairs"` | `{"speed":999}` |
| 46 | `"minecraft:quartz_bricks"` | `{"speed":999}` |
| 47 | `"minecraft:quartz_stairs"` | `{"speed":999}` |
| 48 | `"minecraft:nether_gold_ore"` | `{"speed":999}` |
| 49 | `"minecraft:blackstone"` | `{"speed":999}` |
| 50 | `"minecraft:furnace"` | `{"speed":999}` |
| 51 | `"minecraft:blast_furnace"` | `{"speed":999}` |
| 52 | `"minecraft:lit_furnace"` | `{"speed":999}` |
| 53 | `"minecraft:blast_furnace"` | `{"speed":999}` |
| 54 | `"minecraft:chain"` | `{"speed":999}` |
| 55 | `"minecraft:lantern"` | `{"speed":999}` |
| 56 | `"minecraft:soul_lantern"` | `{"speed":999}` |
| 57 | `"minecraft:grindstone"` | `{"speed":999}` |
| 58 | `"minecraft:brewing_stand"` | `{"speed":999}` |
| 59 | `"minecraft:smooth_stone"` | `{"speed":999}` |
| 60 | `"minecraft:stonebrick"` | `{"speed":999}` |
| 61 | `"minecraft:enchanting_table"` | `{"speed":999}` |
| 62 | `"minecraft:stone_brick_stairs"` | `{"speed":999}` |
| 63 | `"minecraft:mossy_stone_brick_stairs"` | `{"speed":999}` |
| 64 | `"minecraft:polished_blackstone_bricks"` | `{"speed":999}` |
| 65 | `"minecraft:polished_blackstone_stairs"` | `{"speed":999}` |
| 66 | `"minecraft:blackstone_wall"` | `{"speed":999}` |
| 67 | `"minecraft:blackstone_wall"` | `{"speed":999}` |
| 68 | `"minecraft:polished_blackstone_wall"` | `{"speed":999}` |

**Выброшенный предмет:** восстановление через старую структуру; сохранение состояния после восстановления не установлено.

**Вход weapon-события:** weapon-компонент пуст; явный weapon-event не указан. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Расход материалов:** четыре блока бедрока при одном результате каждого рецепта, включая два на палку; добыча — снарядом Ultra Instinct или взрывом выброшенного в огонь Nether Star Sword.

**Значок 2.8.8:** `Swords_R/textures/items/bedrock_sword.png` (ключ атласа `bedrock_sword`; файл сохранён в наборе ресурсов 2.8.8).

**Граница списка добычи:** явного отдельного правила `minecraft:bedrock` среди 68 записей нет. По решению пользователя Bedrock Sword не должен ломать сам бедрок в выживании; описание называет два согласованных способа его получения: снаряд Ultra и взрыв Nether Star. При пересечении правил точного ID и общего тега приоритет у точного ID: для кварц-алмазного блока и руды использовать специально записанные скорости 50 и 100. `should_despawn:false` означает отсутствие обычного исчезновения предмета; устойчивость к взрыву — отдельное требование из описания.

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
    "minecraft:weapon": {}
  },
  "events": {}
}
```

<a id="sword-wither_skeleton_sword"></a>
### 31. Wither Skeleton Sword — `effect:wither_skeleton_sword`

**Параметры предмета:** блеск foil: нет; левая рука: нет; should_despawn: не указан; digger: web 15, bamboo 10.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** 4. **Прочность:** 128. **Кулдаун:** не указан. **Расход применения:** не указан. **Зачарование:** есть: value 9, слот sword.
**Ремонт, единиц за материал:** такой же меч: 128; coal: 58; stick: 2.
**Способности:** при weapon-событии выпускает снаряд с эффектом Wither I на 10 секунд; в исходных полях записано 200 для каждой сложности. В опыте оригинала 2.8.8 на Bedrock 1.20.50 эффект у другого игрока появился на 200 тиков и исчез примерно через 10 секунд на каждой из трёх сложностей — лёгкой, обычной и высокой. В этом опыте удар по свинье выпустил снаряд, который попал в другого игрока на пути: попадание именно в атакованную цель не гарантировано. Собственный прямой урон снаряда 0, отбрасывание включено.
**Получение:** при убийстве Wither Skeleton игроком выдавать меч с шансом 2,5% плюс 2 процентных пункта за уровень Looting, сохраняя обычную добычу; явно связать правило с этим мобом.
**Условная модель износа weapon-события:** 1: 1.

**Вход weapon-события:** только при попадании по сущности с уроном. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Looting:** при реально переданных уровнях 0/1/2/3 условные шансы записанной ветви — 2,5%, 4,5%, 6,5%, 8,5%. Множитель 0,02 добавляет 2 п.п. за уровень; не доказывает подключение таблицы или успешность события.

**Привязка добычи:** соответствующая ванильная сущность в образце Mojang v1.26.60.5 указывает путь таблицы, совпадающий с сохранённым путём аддона. Это совпадение путей, а не доказательство загрузки таблицы в конкретном мире или выдачи меча; сохранить ванильную добычу.

**Значок 2.8.8:** `Swords_R/textures/items/wither_skeleton_sword.png` (ключ атласа `wither_skeleton_sword`; файл сохранён в наборе ресурсов 2.8.8).

**Снаряд `entity:wither_effect`:** runtime snowball, collision 0×0, power 2, gravity 0, impact 0, knockback true, destroy_on_hit true; wither amplifier 0, durationeasy/normal/hard по 200 в исходных полях. Таймер `[0,1;0,1]` посылает despawn; sensor ссылается на отсутствующий локальный event `particle`. При попадании назначать Wither I на 10 секунд; это соответствует измеренным 200 тикам и примерно 10 секундам в испытаниях на трёх сложностях. Исходное поле 200 одинаково для лёгкой, обычной и высокой сложности.

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
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

<a id="sword-glass_sword"></a>
### 32. Glass Sword — `effect:glass_sword`

**Параметры предмета:** блеск foil: нет; левая рука: нет; should_despawn: не указан; digger: web 25, bamboo 15; on_dig вызывает weapon.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** 33. **Прочность:** 1. **Кулдаун:** не указан. **Расход применения:** не указан. **Зачарование:** есть: value 9, слот sword.
**Ремонт, единиц за материал:** такой же меч: 1; glass: 1.
**Способности:** Урон 33, прочность 1; обычный проверенный удар ломает меч. Зачарование и ремонт по записанным настройкам, несмотря на отрицание ремонта в тексте; фактический результат наковальни не проверен.
**Получение:** Fire Sword, выброшенный в воду.
**Условная модель износа weapon-события:** 10: 1.

**Вход weapon-события:** при попадании с уроном, ударе без урона и ударе по блоку. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Приёмка после разрешения на разработку:** проверить, что обычный удар без чар ломает меч; действие чар и ремонт через настоящий интерфейс наковальни отдельно проверить.

**Значок 2.8.8:** `Swords_R/textures/items/glass_sword.png` (ключ атласа `glass_sword`; файл сохранён в наборе ресурсов 2.8.8).

**Разрушение и звук:** все три weapon-хука ведут в событие с прямым durability damage 10 и `playsound random.glass` игрокам `r=8,m=0`; общий digger и два правила web 25/bamboo 15 также ссылаются на weapon. Порядок соседних полей и количество вызовов движком не доказаны; не считать каждый путь независимым гарантированным ударом.

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
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

<a id="sword-silver_sword"></a>
### 33. Silver Sword — `effect:silver_sword`

**Параметры предмета:** блеск foil: нет; левая рука: нет; should_despawn: не указан; digger: web 15, bamboo 10.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** 6. **Прочность:** 1800. **Кулдаун:** не указан. **Расход применения:** не указан. **Зачарование:** есть: value 9, слот sword.
**Ремонт, единиц за материал:** такой же меч: 1800.
**Способности:** Урон предмета 6. При попадании игрока по Alpha Wolf учитывать уже действующее сопротивление в расчёте этого удара; после несмертельного попадания снять с волка Resistance и Regeneration. Отдельный множитель урона Silver против волка не добавлять: преимущество создаётся снятием защиты. В оригинале 2.8.8 на Bedrock 1.20.50 два удара Silver без чар по разным свежим волкам сняли по 7 здоровья (480 → 473), как и два удара железным мечом без чар; 7 — результат данного испытания, а не новое значение параметра предмета. После железного удара волк получил Resistance III и Regeneration III; следующий удар Silver снял 2,8 здоровья и убрал оба эффекта, а последующий удар Silver снял 7. Это наблюдение для данных условий, не гарантия итогового урона при других обстоятельствах.
**Получение:** Два серебряных слитка над палкой; переплавка руды обычного мира Y10–35.
**Рецепт:** 2 / 2 / 1; 2=effect:silver_ingot, 1=minecraft:stick.
**Условная модель износа weapon-события:** 1: 1.

**Положение в основной руке:** первое лицо `{"position":[0.67,0,-1.19]}`; третье лицо `{"position":[0.36,1.5,-0.66]}`. Неуказанные поля не заменять нулями; фактический вид проверить на целевой версии.

**Вход weapon-события:** только при попадании по сущности с уроном. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Приёмка после разрешения на разработку:** проверить генерацию серебра, рецепт и взаимодействие с Alpha Wolf.

**Расход материалов:** два серебряных слитка и палка при одном результате рецепта; доступность и крафт проверить.

**Связанный моб:** [Alpha Wolf](#mob-alpha-wolf).

**Значок 2.8.8:** `Swords_R/textures/items/silver_sword.png` (ключ атласа `silver_sword`; файл сохранён в наборе ресурсов 2.8.8).

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
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

<a id="sword-wolf_sword"></a>
### 34. Wolf Sword — `effect:wolf_sword`

**Параметры предмета:** блеск foil: нет; левая рука: нет; should_despawn: не указан; digger: web 15, bamboo 10.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** 5. **Прочность:** 2800. **Кулдаун:** не указан. **Расход применения:** не указан. **Зачарование:** компонент не указан.
**Ремонт, единиц за материал:** такой же меч: 2800.
**Способности:** В полнолуние преобразование, ускорение, красное зрение, монстры не нападают; окно подготовки по времени суток 0,77–0,78 с nausea 5 с; превращение при времени ≤0,20 или ≥0,80 и фазе луны 0. В полной форме параметр movement 0,18; при раннем снятии nausea и blindness с записанной длительностью 9999. Базовый урон меча 5, компонент полной трансформации 15; в испытании оригинала 2.8.8 на Bedrock 1.20.50 один удар по железному голему снял 20 здоровья (100 → 80) при подтверждённой полной трансформации. Для ремейка использовать 20 базового урона при полной трансформации; броня, эффекты и другие обстоятельства могут изменить итог.
**Получение:** смертельный удар игрока с Silver Sword по Alpha Wolf запускает выбор 10 из 100 на Wolf Sword. В записанном фильтре добычи прямой проверки полнолуния нет. В ремейке Alpha Wolf допускается при фазе луны 0 и исчезает при её смене; в эту фазу он может сохраняться и днём. Остальные условия появления: трава, тайга кроме mega-таги, освещённость 0–7 и сложность easy–hard.
**Условная модель износа weapon-события:** 1: 1.

#### Границы превращения

Для владельца меча в основной руке и фазы луны 0 подготовка запускается при времени суток 0,77–0,78; превращение предусмотрено при времени ≤0,20 либо ≥0,80. Старый контроллер остановки содержит конкурирующее условие: его буквальная логика при обычном приоритете допускает остановку также при удержании меча. Это не основание случайно прерывать превращение: сохранять согласованную задумку полнолуния, а конкуренцию состояний устранить и проверить. При снятии в полной форме записаны nausea и blindness duration 9999/amplifier 0, а обычное окончание отдельно снимает эффекты; возвращение предыдущих эффектов игрока и завершение на рассвете реализовать без глобального воздействия на других игроков.

**Положение в основной руке:** первое лицо `{"position":[0.67,0,-1.22]}`; третье лицо `{"position":[0.36,1.5,-0.66]}`. Неуказанные поля не заменять нулями; фактический вид проверить на целевой версии.

**Вход weapon-события:** только при попадании по сущности с уроном. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Модель, анимация и звук:** модель превращения от третьего лица, красное зрение при полнолунии от первого; звуки wolf_sword.howl (4,715 с) и wolf_sword.distant_howl (5,192 с), ближний выбор до 24 блоков, дальний от 25 до 100; слышимость зависит от клиента, не останавливать другие звуки глобально.

**Приёмка после разрешения на разработку:** проверить границы полнолуния, рассвет, смену меча и восстановление прежних эффектов.

**Связанный моб:** [Alpha Wolf](#mob-alpha-wolf).

**Значок 2.8.8:** `Swords_R/textures/items/wolf_sword.png` (ключ атласа `wolf_sword`; файл сохранён в наборе ресурсов 2.8.8).

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
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

#### Записанные группы и события владельца 2.8.8

Это относящиеся к предмету поля игрока из сохранённого реестра, а не утверждение об их выполнении; если старый код расходится с решениями выше (например восстановление настроек мира или блоков), выполнять решение, а не переносить старую ошибку. Пустое или отсутствующее поле не подменять предположением.

**Группы:**

- `minecraft:wolf_sword` (строки 67,973,1283,1287,1296,1356): `{"minecraft:type_family":{"family":["player","wolf_sword"]}}`
- `wolf_transformation` (строки 70,71,985,1296,1311,1312,1319,1335,1336,1355): `{"minecraft:type_family":{"family":["player","wolf_sword","wolf_transformation"]}}`
- `complete_wolf_transformation` (строки 73,90,992,1301,1302,1322,1332,1355): `{"minecraft:damage_sensor":{"triggers":[{"on_damage":{"filters":{"all_of":[{"test":"has_damage","operator":"!=","value":"void"}]},"event":"wolf_damage_sound"},"deals_damage":true}]},"minecraft:timer":{"time":[3,6],"looping":true,"randomInterval":true,"time_down_event":{"event":"wolf_sword_sounds","target":"self"}},"minecraft:attack":{"damage":15},"minecraft:type_family":{"family":["wolf","wolf_sword","complete_wolf_transformation","monster"]}}`

**События:**

**`minecraft:wolf_sword`** (строки 67,973,1283,1287,1296,1356):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"wolf_sword"},"add":{"component_groups":["minecraft:wolf_sword"]},"run_command":{"command":["effect @s nausea 0 0","effect @s blindness 0 0","effect @s nausea 0 0"]}}`

**`stop_wolf_sword_event`** (строки 980,1292):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"wolf_sword"},"remove":{"component_groups":["minecraft:wolf_sword","wolf_transformation","wolf_movement"]},"run_command":{"command":["effect @s nausea 0 0"]},"add":{"component_groups":["minecraft:default_player"]}}`
  - `$.sequence[1]` — поля действия: `{"filters":{"test":"is_family","value":"complete_wolf_transformation"},"remove":{"component_groups":["complete_wolf_transformation"]},"run_command":{"command":["effect @s nausea 9999 0 true","effect @s blindness 9999 0 true"]},"add":{"component_groups":["minecraft:default_player"]}}`

**`wolf_sword_start_events`** (строки 1308):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"wolf_transformation"},"add":{"component_groups":["wolf_transformation"]},"run_command":{"command":["function commands/swords_and_more_swords/swords_and_more_swords/tellraw1"]}}`

**`starting_wolf_transformation`** (строки 987,1317):

- `$` — поля действия: `{"run_command":{"command":["effect @s nausea 5 0 true"]}}`

**`wolf_transformation`** (строки 70,71,985,1296,1311,1312,1319,1335,1336,1355):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"complete_wolf_transformation"},"run_command":{"command":["playsound random.fizz @a[r=16] ~~~","playsound wolf_sword.howl @a[r=24] ~~~","playsound wolf_sword.distant_howl @a[rm=25,r=100]","particle minecraft:egg_destroy_emitter ~ ~ ~","particle minecraft:egg_destroy_emitter ~ ~0.5 ~","particle minecraft:egg_destroy_emitter ~ ~0.8 ~"]},"add":{"component_groups":["complete_wolf_transformation"]}}`
  - `$.sequence[1]` — поля действия: `{"filters":{"test":"is_family","value":"wolf_transformation"},"remove":{"component_groups":["wolf_transformation"]}}`

**`wolf_sword_sounds`** (строки 85,1344):

- `$.randomize`: альтернативы, веса `[1]`, сумма 1:
  - ветвь 0, weight `1`; условная доля 1/1 (100%):
    - `$.randomize[0]` — поля действия: `{"run_command":{"command":["playsound mob.wolf.growl @a[r=16] ~ ~ ~ 1 0.9 24"]}}`

**`stop_wolf_transformation`** (строки 1349):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"run_command":{"command":["effect @s nausea 0 0","effect @s blindness 0 0","stopsound @a wolf_sword.howl","stopsound @a wolf_sword.distant_howl"]}}`
  - `$.sequence[1]` — поля действия: `{"remove":{"component_groups":["wolf_transformation","complete_wolf_transformation","wolf_movement"]},"add":{"component_groups":["minecraft:wolf_sword"]}}`


<a id="sword-ghost_sword"></a>
### 35. Ghost Sword — `effect:ghost_sword`

**Параметры предмета:** блеск foil: да; левая рука: нет; should_despawn: false; digger: web 15, bamboo 10.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** −666 в записанной настройке; целевое действие — не наносить урон, лечение не установлено. **Прочность:** 3333. **Кулдаун:** 2 с. **Расход применения:** 6. **Зачарование:** компонент не указан.
**Ремонт, единиц за материал:** компонент не указан.
**Способности:** Не наносит урон; полная неуязвимость, призрачный облик, белое зрение, скорость, монстры не нападают; movement 0,14, отсутствие обычной коллизии, дыхание в воздухе/воде/лаве; slow falling I и saturation II, в воде левитация I, в лаве левитация I и fire resistance I. Приседание вызывает левитацию IV. Применение телепортирует по взгляду при попадании снаряда, расход 6, кулдаун 2 секунды; снаряд power 2,5, gravity 0, liquid inertia 2,8; около 250 блоков в горизонтальной проверке, не искусственный жёсткий предел. При приближении к стене игрок должен видеть расположенные за ней близкие пещеры и иметь возможность телепортироваться в пещеру по направлению взгляда, как указано в описании; приёмку видимости и телепортации выполнить в клиенте.
**Получение:** в исходнике при событии урона по [призраку](#mob-ghost) с источником family `player` его damage sensor отменяет урон и запускает один выбор: меч 3/1000, телепортация призрака 10/1000 либо пустая ветвь 987/1000. Это доли одного выбора, а не три независимые вероятности; смерть призрака для попытки не требуется. По решению пользователя в ремейке реальный игрок считается игроком для этой реакции и при превращении, когда соответствующее игровое событие возникает; это не добавляет возможность атаковать при удержании Ghost Sword. Условия появления и поведения указаны в пункте существа.
**Условная модель износа weapon-события:** 1: 1.

**Положение в основной руке:** первое лицо `{"position":[0.67,0,-1.24]}`; третье лицо `{"position":[0.36,1.5,-0.66]}`. Неуказанные поля не заменять нулями; фактический вид проверить на целевой версии.

**Вход weapon-события:** при попадании с уроном, ударе без урона и ударе по блоку. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Модель игрока:** `controller.render.player_ghost`, `geometry.player_ghost`, текстура `textures/entity/ghost`, material `player_ghost`, light_color_multiplier 0,2, ignore_lighting true. От третьего лица используется move.player_ghost, от первого — vision.player_ghost. Плач призрака относится к [самому мобу](#mob-ghost), не к способности игрока.

**Приёмка после разрешения на разработку:** проверить защиту от каждого типа урона и перемещение по взгляду, включая жидкости и препятствия.

**Значок 2.8.8:** `Swords_R/textures/items/ghost_sword.png` (ключ атласа `ghost_sword`; файл сохранён в наборе ресурсов 2.8.8).

**Снаряд:** `entity:ghost_projectile` power 2,5, gravity 0, liquid_inertia 2,8, impact −1, изначально collision 0×0 и has_collision false. Повторяющийся timer `[0,0]` проверяет air/water и может добавить `teleport_enable`; группа задаёт collision 10×10 и on-hit teleport_owner/remove_on_hit. Это не доказательство прохождения любых стен. При снятии исходная группа movement 0,14 явно не перечислена в remove: состояние игрока нужно восстанавливать корректно.

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
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
    },
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:cooldown": {
      "category": "ghost_sword",
      "duration": 2
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

#### Записанные группы и события владельца 2.8.8

Это относящиеся к предмету поля игрока из сохранённого реестра, а не утверждение об их выполнении; если старый код расходится с решениями выше (например восстановление настроек мира или блоков), выполнять решение, а не переносить старую ошибку. Пустое или отсутствующее поле не подменять предположением.

**Группы:**

- `minecraft:ghost_sword` (строки 47,1001,1216,1220,1265): `{"minecraft:scale":{"value":1.05},"minecraft:knockback_resistance":{"value":1.0},"minecraft:collision_box":{"width":0.0,"height":0.0},"minecraft:breathable":{"total_supply":15,"suffocate_time":0,"inhale_time":3.75,"generates_bubbles":false,"breathes_water":true,"breathes_air":true,"breathes_lava":true},"minecraft:damage_sensor":{"triggers":{"cause":"all","deals_damage":false}},"minecraft:type_family":{"family":["ghost_sword"]}}`
- `ghost_movement` (строки 64,1234): `{"minecraft:movement":{"value":0.14}}`

**События:**

**`minecraft:ghost_sword`** (строки 47,1001,1216,1220,1265):

- `$.sequence`: 6 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"ghost_sword"},"add":{"component_groups":["minecraft:ghost_sword"]},"run_command":{"command":["particle minecraft:egg_destroy_emitter ~ ~ ~","particle minecraft:egg_destroy_emitter ~ ~0.3 ~","particle minecraft:egg_destroy_emitter ~ ~0.6 ~","particle minecraft:egg_destroy_emitter ~ ~0.9 ~","particle minecraft:egg_destroy_emitter ~ ~1.2 ~","particle minecraft:egg_destroy_emitter ~ ~1.5 ~","playsound mob.wither.ambient @a[r=16] ~ ~1 ~ 2 0.3"]}}`
  - `$.sequence[1]` — поля действия: `{"run_command":{"command":["effect @s slow_falling 1 0 true","effect @s saturation 1 1 true"]},"add":{"component_groups":["ghost_movement"]}}`
  - `$.sequence[2]` — поля действия: `{"filters":{"test":"in_water"},"run_command":{"command":["effect @s levitation 1 0 true"]}}`
  - `$.sequence[3]` — поля действия: `{"filters":{"test":"in_lava"},"run_command":{"command":["effect @s levitation 1 0 true","effect @s fire_resistance 1 0 true"]}}`
  - `$.sequence[4]` — поля действия: `{"filters":{"test":"in_lava","operator":"!="},"run_command":{"command":["effect @s fire_resistance 0 0"]}}`
  - `$.sequence[5].randomize`: альтернативы, веса `[90,10]`, сумма 100:
    - ветвь 0, weight `90`; условная доля 9/10 (90%):
      - пустое действие
    - ветвь 1, weight `10`; условная доля 1/10 (10%):
      - `$.sequence[5].randomize[1]` — поля действия: `{"run_command":{"command":["playsound mob.wither.spawn @a[r=16] ~ ~ ~ 0.15 0.2"]}}`

**`stop_ghost_sword_event`** (строки 1008,1261):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"ghost_sword"},"remove":{"component_groups":["minecraft:ghost_sword"]},"add":{"component_groups":["minecraft:default_player"]},"run_command":{"command":["effect @s slow_falling 0 0","stopsound @a[r=18] mob.wither.spawn","playsound mob.wither.ambient @a[r=16] ~ ~1 ~ 2 0.2","particle minecraft:egg_destroy_emitter ~ ~ ~","particle minecraft:egg_destroy_emitter ~ ~0.3 ~","particle minecraft:egg_destroy_emitter ~ ~0.6 ~","particle minecraft:egg_destroy_emitter ~ ~0.9 ~","particle minecraft:egg_destroy_emitter ~ ~1.2 ~","particle minecraft:egg_destroy_emitter ~ ~1.5 ~","particle minecraft:ghost_spiral ~~~"]}}`


<a id="sword-ultra_instinct_sword"></a>
### 36. Ultra Instinct Sword — `effect:ultra_instinct_sword`

**Параметры предмета:** блеск foil: да; левая рука: нет; should_despawn: false; digger: web 999, bamboo 999.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** 16. **Прочность:** 9999. **Кулдаун:** 61 с. **Расход применения:** 48. **Зачарование:** компонент не указан.
**Ремонт, единиц за материал:** компонент не указан.
**Способности:** Защита от ближнего боя, снарядов, огня и взрывов; уклонение с телепортацией поблизости (исходная команда `spreadplayers ~ ~ 1 3 @s` не задаёт гарантированную минимальную дистанцию 1 от прежней позиции), movement 0,22, сопротивление отбрасыванию 1. Снимаются hunger, blindness, slowness, weakness, mining fatigue, nausea, instant damage и wither; урон от лавы отдельно не отменён. Применение — мощный снаряд с impact damage 64, power 2, gravity 0; взрыв power 8, max resistance 4,0, огонь выключен. По решению пользователя затронутый бедрок разрушается и выпадает как блок. Расход 48, кулдаун 61 секунда; не удалять выброшенные предметы.
**Получение:** Колодец: кварц-алмаз 0,8% на единицу или его блок 2,5% на единицу.
**Условная модель износа weapon-события:** 1: 1.

**Положение в основной руке:** первое лицо `{"rotation":[0,-5.0,95],"position":[1.8,-1.4,-5.5],"scale":[0.04,0.04,0.04]}`; третье лицо `{"position":[1.5,3.6,-1.8],"scale":[0.04,0.04,0.04]}`. Неуказанные поля не заменять нулями; фактический вид проверить на целевой версии.

**Вход weapon-события:** только при попадании по сущности с уроном. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Модель, анимация и звук:** аура и анимации движения и атаки.

**Приёмка после разрешения на разработку:** проверить разрушение и выпадение затронутого бедрока; не удалять выброшенные предметы.

**Колодец:** кварц-алмаз даёт независимую попытку Ultra с шансом 0,8% на единицу, блок — 2,5% на единицу; возможны несколько наград. Проверять настоящий ID и форму колодца; построенные копии допустимы.

**Значок 2.8.8:** `Swords_R/textures/items/ultra_instinct_sword.png` (ключ атласа `ultra_instinct_sword`; файл сохранён в наборе ресурсов 2.8.8).

**Фильтр защиты:** в исходном первом damage trigger одновременно исключены lava, drowning, void, thorns, suicide, starve, fire, fire_tick и magic; для fire, fire_tick и block/entity explosion объявлены отдельные запреты, для lava — отдельное deals_damage true. Не распространять этот запрет на все исключённые типы; разрешение пересекающихся триггеров проверить. Исходный `projectile_particle` содержит `kill @e[type=item,r=24]`; по решению пользователя **не переносить удаление выброшенных предметов**.

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      }
    },
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:cooldown": {
      "category": "ultra_instinct_sword",
      "duration": 61
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

#### Записанные группы и события владельца 2.8.8

Это относящиеся к предмету поля игрока из сохранённого реестра, а не утверждение об их выполнении; если старый код расходится с решениями выше (например восстановление настроек мира или блоков), выполнять решение, а не переносить старую ошибку. Пустое или отсутствующее поле не подменять предположением.

**Группы:**

- `minecraft:ultra_instinct_sword` (строки 95,959,1360,1364,1389): `{"minecraft:knockback_resistance":{"value":1.0},"minecraft:timer":{"time":[0.1,0.2],"looping":true,"randomInterval":true,"time_down_event":{"event":"ultra_instinct_sword_effects","target":"self"}},"minecraft:damage_sensor":{"triggers":[{"on_damage":{"filters":{"all_of":[{"test":"has_damage","operator":"!=","value":"lava"},{"test":"has_damage","operator":"!=","value":"drowning"},{"test":"has_damage","operator":"!=","value":"void"},{"test":"has_damage","operator":"!=","value":"thorns"},{"test":"has_damage","operator":"!=","value":"suicide"},{"test":"has_damage","operator":"!=","value":"starve"},{"test":"has_damage","operator":"!=","value":"fire"},{"test":"has_damage","operator":"!=","value":"fire_tick"},{"test":"has_damage","operator":"!=","value":"magic"}]},"event":"ultra_instinct_sword_skill"},"deals_damage":false},{"on_damage":{"filters":{"test":"has_damage","value":"fire"}},"deals_damage":false},{"on_damage":{"filters":{"test":"has_damage","value":"fire_tick"}},"deals_damage":false},{"on_damage":{"filters":{"any_of":[{"test":"has_damage","value":"block_explosion"},{"test":"has_damage","value":"entity_explosion"}]}},"deals_damage":false},{"on_damage":{"filters":{"all_of":[{"test":"has_damage","value":"lava"}]}},"deals_damage":true}]},"minecraft:type_family":{"family":["player","ultra_instinct_sword"]}}`
- `ultra_instinct_sword_movement` (строки 144,1381,1389): `{"minecraft:movement":{"value":0.22}}`
- `ultra_instinct_projectile` (строки 420,2268,2269): `{"minecraft:spawn_entity":[{"min_wait_time":0,"max_wait_time":0,"single_use":true,"spawn_entity":"entity:ultra_instinct_projectile","num_to_spawn":1}]}`

**События:**

**`minecraft:ultra_instinct_sword`** (строки 95,959,1360,1364,1389):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"!=","value":"ultra_instinct_sword"},"add":{"component_groups":["minecraft:ultra_instinct_sword"]},"run_command":{"command":["particle minecraft:example_flipbook ~ ~ ~","particle minecraft:example_flipbook ~ ~1.5 ~","playsound mob.wither.ambient @a[r=16] ~ ~1 ~ 2 0.6"]}}`
  - `$.sequence[1]` — поля действия: `{"run_command":{"command":["camerashake add @a[r=32] 0.1 0.016 positional","fill ~1 ~2 ~1 ~-1 ~2 ~-1 effect99:lightblock 0 replace air","fill ~1 ~2 ~1 ~-1 ~2 ~-1 effect99:lightblock 0 replace effect99:lightblock","effect @s hunger 0 0","effect @s blindness 0 0","effect @s slowness 0 0","effect @s weakness 0 0","effect @s mining_fatigue 0 0","effect @s nausea 0 0","effect @s instant_damage 0 0","effect @s wither 0 0"]},"add":{"component_groups":["ultra_instinct_sword_movement"]}}`

**`stop_ultra_instinct_sword_event`** (строки 966,1385):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"ultra_instinct_sword"},"remove":{"component_groups":["minecraft:ultra_instinct_sword","ultra_instinct_sword_movement"]},"add":{"component_groups":["minecraft:default_player"]},"run_command":{"command":["particle minecraft:example_flipbook ~ ~ ~","particle minecraft:example_flipbook ~ ~1.5 ~","playsound mob.wither.ambient @a[r=16] ~ ~1 ~ 2 0.6"]}}`

**`ultra_instinct_sword_skill`** (строки 113,1395):

- `$` — поля действия: `{"run_command":{"command":["spreadplayers ~ ~ 1 3 @s","playsound mob.endermen.portal @a[r=17] ~ ~ ~ 1 0.6"]}}`

**`ultra_instinct_sword_effects`** (строки 98,1397):

- `$.randomize`: альтернативы, веса `[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]`, сумма 15:
  - ветвь 0, weight `1`; условная доля 1/15 (6.66667%):
    - `$.randomize[0]` — поля действия: `{"run_command":{"command":["particle minecraft:balloon_gas_particle ~0.3 ~1 ~","playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"]}}`
  - ветвь 1, weight `1`; условная доля 1/15 (6.66667%):
    - `$.randomize[1]` — поля действия: `{"run_command":{"command":["particle minecraft:balloon_gas_particle ~ ~2 ~0.3","playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"]}}`
  - ветвь 2, weight `1`; условная доля 1/15 (6.66667%):
    - `$.randomize[2]` — поля действия: `{"run_command":{"command":["particle minecraft:balloon_gas_particle ~-0.3 ~ ~","playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"]}}`
  - ветвь 3, weight `1`; условная доля 1/15 (6.66667%):
    - `$.randomize[3]` — поля действия: `{"run_command":{"command":["particle minecraft:balloon_gas_particle ~ ~0.3 ~-0.3","playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"]}}`
  - ветвь 4, weight `1`; условная доля 1/15 (6.66667%):
    - `$.randomize[4]` — поля действия: `{"run_command":{"command":["particle minecraft:balloon_gas_particle ~0.3 ~1.5 ~0.3","playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"]}}`
  - ветвь 5, weight `1`; условная доля 1/15 (6.66667%):
    - `$.randomize[5]` — поля действия: `{"run_command":{"command":["particle minecraft:balloon_gas_particle ~-0.3 ~0.8 ~-0.3","playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"]}}`
  - ветвь 6, weight `1`; условная доля 1/15 (6.66667%):
    - `$.randomize[6]` — поля действия: `{"run_command":{"command":["particle minecraft:balloon_gas_particle ~-0.3 ~2 ~0.3","playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"]}}`
  - ветвь 7, weight `1`; условная доля 1/15 (6.66667%):
    - `$.randomize[7]` — поля действия: `{"run_command":{"command":["particle minecraft:balloon_gas_particle ~0.2 ~1 ~0.3","playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"]}}`
  - ветвь 8, weight `1`; условная доля 1/15 (6.66667%):
    - `$.randomize[8]` — поля действия: `{"run_command":{"command":["particle minecraft:balloon_gas_particle ~0.3 ~0.9 ~0.1","playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"]}}`
  - ветвь 9, weight `1`; условная доля 1/15 (6.66667%):
    - `$.randomize[9]` — поля действия: `{"run_command":{"command":["particle minecraft:balloon_gas_particle ~0.2 ~2.3 ~-0.2","playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"]}}`
  - ветвь 10, weight `1`; условная доля 1/15 (6.66667%):
    - `$.randomize[10]` — поля действия: `{"run_command":{"command":["particle minecraft:balloon_gas_particle ~-0.3 ~1.2 ~","playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"]}}`
  - ветвь 11, weight `1`; условная доля 1/15 (6.66667%):
    - `$.randomize[11]` — поля действия: `{"run_command":{"command":["particle minecraft:balloon_gas_particle ~0.3 ~0.3 ~0.3","playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"]}}`
  - ветвь 12, weight `1`; условная доля 1/15 (6.66667%):
    - `$.randomize[12]` — поля действия: `{"run_command":{"command":["particle minecraft:balloon_gas_particle ~0.3 ~0.6 ~0.1","playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"]}}`
  - ветвь 13, weight `1`; условная доля 1/15 (6.66667%):
    - `$.randomize[13]` — поля действия: `{"run_command":{"command":["particle minecraft:balloon_gas_particle ~-0.3 ~0.2 ~0.3","playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"]}}`
  - ветвь 14, weight `1`; условная доля 1/15 (6.66667%):
    - `$.randomize[14]` — поля действия: `{"run_command":{"command":["particle minecraft:balloon_gas_particle ~0.1 ~0.7 ~-0.3","playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"]}}`

**`shoot_ultra_instinct_projectile`** (строки 2266):

- `$` — поля действия: `{"run_command":{"command":["playsound mob.wither.ambient @s ~ ~1 ~ 2 0.6"]},"add":{"component_groups":["ultra_instinct_projectile"]},"remove":{"component_groups":["ultra_instinct_projectile"]}}`


<a id="sword-wet_sponge_sword"></a>
### 37. Wet Sponge Sword — `effect:wet_sponge_sword`

**Параметры предмета:** блеск foil: нет; левая рука: нет; should_despawn: не указан; digger: компонент не указан.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** 3. **Прочность:** 64. **Кулдаун:** не указан. **Расход применения:** не указан. **Зачарование:** компонент не указан.
**Ремонт, единиц за материал:** Sponge Sword: 64; sponge: 32; Wet Sponge Sword: 64.
**Способности:** Особых способностей нет; компонент зачарования не указан в сохранённых заметках, текст говорит false.
**Получение:** Мокрая Sponge Sword; в печи снова становится Sponge Sword.
**Условная модель износа weapon-события:** 1: 1.

**Вход weapon-события:** только при попадании по сущности с уроном. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Значок 2.8.8:** `Swords_R/textures/items/wet_sponge_sword.png` (ключ атласа `wet_sponge_sword`; файл сохранён в наборе ресурсов 2.8.8).

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
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

#### Записанные группы и события владельца 2.8.8

Это относящиеся к предмету поля игрока из сохранённого реестра, а не утверждение об их выполнении; если старый код расходится с решениями выше (например восстановление настроек мира или блоков), выполнять решение, а не переносить старую ошибку. Пустое или отсутствующее поле не подменять предположением.

**События:**

**`wet_sponge_sword`** (строки 1591):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"has_equipment","subject":"self","domain":"hand","value":"effect:sponge_sword"},"run_command":{"command":["replaceitem entity @s slot.weapon.mainhand 0 effect:wet_sponge_sword 1","scoreboard players set @s sponge_sword 0","title @s actionbar §l§gWet Sponge Sword"]}}`


<a id="sword-cursed_pumpkin_sword"></a>
### 38. Cursed Pumpkin Sword — `effect:cursed_pumpkin_sword`

**Параметры предмета:** блеск foil: нет; левая рука: нет; should_despawn: не указан; digger: web 15, bamboo 10.
**Поля предмета:** максимум в стопке 1; hand_equipped: true; can_destroy_in_creative: false.

**Урон:** 5. **Прочность:** 606. **Кулдаун:** не указан. **Расход применения:** не указан. **Зачарование:** есть: value 9, слот sword.
**Ремонт, единиц за материал:** такой же меч: 606; honey block: 400; honeycomb: 150.
**Способности:** При weapon-событии тыквенный снаряд с весом 80 из 100. Снаряд: урон при контакте 1, отбрасывание и отскок, удаление при попадании, power 0,3, gravity 0,002, разброс base 16/multiplier 4, столкновение 0,625 × 0,625; таймер удаления 12–15 в записанных единицах, частица largeexplode.
**Получение:** при разрушении игроком блока, в ID которого есть `pumpkin`, но нет `stem`, проверяется случайный шанс 5 из 1000 (0,5%). После успешной проверки меч выдаётся только при отсутствии у игрока тега `pumpkin_sword`: сначала добавить этот тег, затем запустить выдачу меча в месте разрушения блока. Пока тег есть, дальнейшие выдачи этому игроку блокируются. По решению пользователя механизм тега сохраняется как в оригинале; его автоматическое снятие не добавлять. Если команда выдачи не сработает после установки тега, исходный код не снимает его обратно.
**Условная модель износа weapon-события:** 1: 1.

**Вход weapon-события:** при попадании с уроном, ударе без урона и ударе по блоку. Значения износа выше — только условная модель явного события, не итоговый износ движка.

**Модель, анимация и звук:** модель снаряда имеет текстурные координаты 48×48 (это не физический размер).

**Приёмка после разрешения на разработку:** проверить, что при наличии тега повторная выдача блокируется и что порядок — сначала тег, затем выдача; после смерти игрока и после повторного входа сохранять тег. В проверке пользователя на Bedrock 1.20.50 (телефон) и 26.63 (ПК; версии со слов пользователя) после смерти, а затем после сохранения, выхода и повторного входа сохранились оба вручную добавленных тега `pumpkin_sword` и `arena_control` и контрольный алмаз. Проверялись общие теги игры, не получение меча через аддон.

**Значок 2.8.8:** `Swords_R/textures/items/cursed_pumpkin_sword.png` (ключ атласа `cursed_pumpkin_sword`; файл сохранён в наборе ресурсов 2.8.8).

#### Точные входы и события предмета 2.8.8

Сохранённые поля этого предмета; команды, условия, цели и порядок проверять вместе с описанием его способности. Отсутствующее поле не означает нулевое значение или доказанное поведение движка.

```json
{
  "components": {
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

## Материалы и блоки

### effect:quartz_diamond

**Свойства:** stack 9, foil true, hand_equipped false; другие неуказанные поля не приравнивать к false.

`effect:quartz_diamond`: кварц-алмаз, стек до 9; 9 штук создают кварц-алмазный блок. Генерация по записи: биомы Overworld или End, Y 0–16, 5 попыток, scatter 160/200, размещение в stone или end_stone; это параметры размещения, не шанс руды на каждый чанк. Сопутствующий урон при разрушении — игроку в радиусе 6.

**Колодец:** независимая попытка на каждую единицу стопки; Ultra Instinct с вероятностью 0,8% на единицу. Несколько успехов дают несколько наград; проверять реальный ID.


**Значок 2.8.8:** `Swords_R/textures/items/quartz_diamond.png`; ключ атласа `quartz_diamond`.

#### Компоненты и события материала 2.8.8

```json
{
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

### effect:quartz_diamond_stick

**Свойства:** stack 1, foil true, offhand false, hand_equipped true, can_destroy_in_creative true; прочность 20, damage 24.

`effect:quartz_diamond_stick`: урон 24, прочность 20, крафт из двух кварц-алмазов вертикально; повреждает владельца при ударе. Зафиксированные ветви урона владельцу: 1/3/6 при весах 10/85/5.

**Рецепт:** # / #; #=effect:quartz_diamond.


**Значок 2.8.8:** `Swords_R/textures/items/quartz_diamond_stick.png`; ключ атласа `quartz_diamond_stick`.

#### Компоненты и события материала 2.8.8

```json
{
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

### effect:silver_ingot

**Свойства:** stack 64, hand_equipped false; foil и offhand не указаны.

`effect:silver_ingot`: выплавить руду серебра; руда обычного мира Y10–35, 5 попыток, scatter 160/200, материал stone; восстановить генерацию и наличие в креативном инвентаре.

**Рецепт:** effect99:silver_ore → effect:silver_ingot (furnace, blast_furnace).


**Значок 2.8.8:** `Swords_R/textures/items/silver_ingot.png`; ключ атласа `silver_ingot`.

#### Компоненты и события материала 2.8.8

```json
{
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

### effect:bedrock_stick

**Свойства:** stack 1, foil false, should_despawn true, offhand false, hand_equipped true, can_destroy_in_creative true; damage 6, durability не указана.

`effect:bedrock_stick`: урон 6, бесконечная прочность по игровой задумке, рецепт из двух бедроков вертикально.

**Рецепт:** # / #; #=minecraft:bedrock.


**Значок 2.8.8:** `Swords_R/textures/items/bedrock_stick.png`; ключ атласа `bedrock_stick`.

#### Компоненты и события материала 2.8.8

```json
{
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

### Кварц-алмазная руда — `effect99:quartz_diamond_ore`

Время разрушения 10, устойчивость к взрыву 999. Записаны Overworld или End, Y0–16, пять попыток, scatter 160/200, x/z uniform [0,16], y gaussian, underground_pass, adjustment_radius 1 и случайное направление; каждый сохранённый шаблон содержит один блок. Это параметры, не вероятность на чанк; проверять новые чанки. В отдельной loot-таблице руды нет явно записанной ветви Silk Touch или множителя Fortune; условия работы чар движком не установлены. Без Шёлкового касания и Удачи при вызове добычи три ветви 89/10/1 с количеством 1, 1–2 и 2–4; при равномерном целочисленном выборе условное распределение: 1 — 94%, 2 — 5⅓%, 3/4 — по ⅓%, среднее 1,07. Записаны шесть команд призыва сфер опыта, частица и instant damage ближайшему игроку в r=6; ближайший игрок может быть не добывающим. По решению пользователя для руды и блока сохранить выбор ближайшего игрока в радиусе 6, даже если это не добывающий игрок.

**Чары при добыче кварц-алмазной руды:** по решению пользователя Шёлковое касание подходящей кирки выдаёт сам блок руды; Удача увеличивает базовое количество кварц-алмазов по правилам обычной руды целевой версии. Без этих чар применять исходный выбор 89/10/1; при Шёлковом касании и при Удаче сохранять шесть сфер опыта и урон ближайшему игроку в радиусе 6. Совместимость чар, их влияние на количество и сохранение этих побочных эффектов проверить при технической приёмке.

**Условия добычи этого блока:** добычу и специальные эффекты вызывать при разрушении игроком с железной, алмазной, незеритовой киркой либо Bedrock Sword. По решению пользователя в выживании неподходящим инструментом блок разрушается без выпадения, специального урона и сфер опыта. Базовый путь `loot_tables/blocks/null.json` локально отсутствует и не доказывает фактический результат в старой игре. 


#### Точная запись блока 2.8.8

Исходные поля и условия разрушения; незаписанные свойства не угадывать, совместимость в целевой версии проверить.

```json
{
  "format_version": "1.10.0",
  "minecraft:block": {
    "description": {
      "identifier": "effect99:quartz_diamond_ore"
    },
    "components": {
      "minecraft:loot": "loot_tables/blocks/null.json",
      "minecraft:destroy_time": 10,
      "minecraft:explosion_resistance": 999,
      "minecraft:light_emission": 0,
      "minecraft:on_player_destroyed": {
        "condition": "q.get_equipped_item_name == 'iron_pickaxe' || q.get_equipped_item_name == 'diamond_pickaxe'|| q.get_equipped_item_name == 'netherite_pickaxe' || q.get_equipped_item_name == 'bedrock_sword'",
        "event": "quartz_diamond_ore"
      },
      "minecraft:block_light_absorption": 15,
      "minecraft:map_color": "#000000"
    },
    "events": {
      "quartz_diamond_ore": {
        "spawn_loot": {
          "table": "loot_tables/blocks/quartz_diamond_ore.json"
        },
        "run_command": {
          "command": [
            "summon xp_orb",
            "summon xp_orb",
            "summon xp_orb",
            "summon xp_orb",
            "summon xp_orb",
            "summon xp_orb",
            "particle minecraft:knockback_roar_particle ~ ~1 ~",
            "effect @p[r=6] instant_damage 1 0 true"
          ]
        }
      }
    }
  }
}
```

### Кварц-алмазный блок — `effect99:quartz_diamond_block`

Время разрушения 20, устойчивость к взрыву 999. Рецепт ### / ### / ###; #=effect:quartz_diamond. В записи выдаётся один блок; предусмотрены частица и instant damage ближайшему игроку в r=6; по решению пользователя сохранить выбор ближайшего игрока, даже если это не добывающий игрок. В колодце каждая единица даёт независимую попытку Ultra с шансом 2,5%.

**Условия добычи этого блока:** добычу и специальные эффекты вызывать при разрушении игроком с железной, алмазной, незеритовой киркой либо Bedrock Sword. По решению пользователя в выживании неподходящим инструментом блок разрушается без выпадения, специального урона и сфер опыта. Базовый путь `loot_tables/blocks/null.json` локально отсутствует и не доказывает фактический результат в старой игре.


#### Точная запись блока 2.8.8

Исходные поля и условия разрушения; незаписанные свойства не угадывать, совместимость в целевой версии проверить.

```json
{
  "format_version": "1.10.0",
  "minecraft:block": {
    "description": {
      "identifier": "effect99:quartz_diamond_block"
    },
    "components": {
      "minecraft:loot": "loot_tables/blocks/null.json",
      "minecraft:destroy_time": 20,
      "minecraft:explosion_resistance": 999,
      "minecraft:block_light_emission": 0,
      "minecraft:flammable": {
        "flame_odds": 0,
        "burn_odds": 0
      },
      "minecraft:on_player_destroyed": {
        "condition": "q.get_equipped_item_name == 'iron_pickaxe' || q.get_equipped_item_name == 'diamond_pickaxe'|| q.get_equipped_item_name == 'netherite_pickaxe' || q.get_equipped_item_name == 'bedrock_sword'",
        "event": "quartz_diamond_block"
      },
      "minecraft:block_light_absorption": 15,
      "minecraft:map_color": "#000000"
    },
    "events": {
      "quartz_diamond_block": {
        "spawn_loot": {
          "table": "loot_tables/blocks/quartz_diamond_block.json"
        },
        "run_command": {
          "command": [
            "particle minecraft:knockback_roar_particle ~ ~1 ~",
            "effect @p[r=6] instant_damage 1 0 true"
          ]
        }
      }
    }
  }
}
```

### Серебряная руда — `effect99:silver_ore`

Время разрушения 8, устойчивость к взрыву 1. Записана генерация Overworld, Y10–35, пять попыток, scatter 160/200, x/z uniform [0,16], y gaussian, underground_pass, adjustment_radius 1 и случайное направление; каждый сохранённый шаблон содержит один блок. Руда выдаёт блок руды, слиток получают плавкой. Восстановить генерацию и наличие в творческом инвентаре; проверять новые чанки.

**Условия добычи этого блока:** добычу и специальные эффекты вызывать при разрушении игроком с железной, алмазной, незеритовой киркой либо Bedrock Sword. По решению пользователя в выживании неподходящим инструментом блок разрушается без выпадения, специального урона и сфер опыта. Базовый путь `loot_tables/blocks/null.json` локально отсутствует и не доказывает фактический результат в старой игре.

#### Точная запись блока 2.8.8

Исходные поля и условия разрушения; незаписанные свойства не угадывать, совместимость в целевой версии проверить.

```json
{
  "format_version": "1.10.0",
  "minecraft:block": {
    "description": {
      "identifier": "effect99:silver_ore"
    },
    "components": {
      "minecraft:loot": "loot_tables/blocks/null.json",
      "minecraft:destroy_time": 8,
      "minecraft:explosion_resistance": 1,
      "minecraft:block_light_emission": 0,
      "minecraft:on_player_destroyed": {
        "condition": "q.get_equipped_item_name == 'iron_pickaxe' || q.get_equipped_item_name == 'diamond_pickaxe'|| q.get_equipped_item_name == 'netherite_pickaxe' || q.get_equipped_item_name == 'bedrock_sword'",
        "event": "silver_ore"
      },
      "minecraft:block_light_absorption": 15,
      "minecraft:map_color": "#000000"
    },
    "events": {
      "silver_ore": {
        "spawn_loot": {
          "table": "loot_tables/blocks/silver_ore.json"
        }
      }
    }
  }
}
```


## Колодец желаний

В колодец допускается бросать кварц-алмаз, кварц-алмазный блок и Clock Sword по реальному ID. Форма проверяется по блокам, не происхождению; построенная копия работает. Поглощать всю подходящую стопку и делать независимую попытку для каждой единицы: несколько успехов дают несколько наград. Шансы: кварц-алмаз → Ultra 0,8%; его блок → Ultra 2,5%; Clock → Time 2,5%.

Проверять относительно блока, в котором находится выброшенный предмет: вода `(0,0,0)`, `(1,0,0)`, `(-1,0,0)`, `(0,0,1)`, `(0,0,-1)`; песчаник `(0,-1,0)`, `(1,-1,0)`, `(-1,-1,0)`, `(0,-1,1)`, `(0,-1,-1)`, `(0,4,0)`, `(1,2,1)`, `(-1,2,-1)`, `(-1,2,1)`, `(1,2,-1)`. Это проверка формы, не происхождения. Отдельно хранить соответствие типов воды и песчаника современным состояниям блока.

При каждом успехе кварц-алмаза/его блока выдаётся Ultra Instinct Sword; при успехе Clock — Time Sword и `time add 6000`; при неуспехе Clock — `time add 1000`. В успешных ветках дополнительно записана замена песка на concrete powder в рамке x/z ±15 и y −15…+10, для ветки Time — data 4, для Ultra — data 0. При обработке стопки независимые попытки и несколько наград обязательны; сохранение побочных эффектов и их порядок при нескольких результатах надо протестировать, не теряя предметы за пределами жертвы.


## Боссы, мобы и связанные сущности

<a id="mob-slime-king"></a>

### Slime King — `entity:slime_king`

Связан с [Slime Sword](#sword-slime_sword). Появление на поверхности: биом swamp, сложности easy–hard, вес 10; по решению пользователя только ночью, хотя прямой проверки ночи в исходном правиле нет. При убийстве босса игроком выдавать Slime Sword с шансом 4% плюс 2 п.п. за уровень Looting. В оригинале есть отдельная таблица с этими значениями, но её явная привязка к сущности не найдена; в ремейке связать таблицу с боссом. Health 300, attack 9, scale 4,3, movement 1,1, сопротивление отбрасыванию 0,5, boss bar range 32; видимые игроки и големы до 38. При уроне от игрока выбор 5/100 на jump_boost amplifier 15. При событии урона от падения вызываются instant_damage r=3 для существ без family slime_king и r=4 для iron_golem; сам урон от падения отменяется. Отдельный environment sensor с пустым фильтром вызывает `slime_effects`: jump_boost себе и пересекающиеся magic damage r=1,8 ближайшему игроку и r=1,5 сущностям без family slime_king. Эти команды не являются частью события падения; частота sensor не определяется одним пустым фильтром. В исходнике повторяются `minecraft:movement.jump` с задержками после приземления [0,5;1,5] и [0,16;0,4] секунд. По просьбе пользователя проведена проверка оригинала 2.8.8 на Bedrock 1.20.50 с двумя отдельными контролями: за 1000 тиков исходный босс и контроль только с [0,16;0,4] имели по 52 полных паузы 4–8 тиков (медиана 6), контроль только с [0,5;1,5] — 30 пауз 11–29 тиков (медиана 19,5). Это указывает на поведение, соответствующее быстрой записи в условиях опыта; причина двойной записи неизвестна. По решению пользователя в ремейке использовать задержку [0,16;0,4] секунды.


**Клиентские ресурсы 2.8.8:** `Swords_R/entity/slime_king.entity.json`, `textures/entity/slime/slime_king.png`, `models/entity/slime_king_armor.geo.json`; geometry.slime и render.controllers ссылаются на ванильные определения.

#### Записанные компоненты и события 2.8.8

Ниже — точные поля сохранённого разбора, не гарантия их исполнения в новой версии. В случае повторяющихся ключей и неподтверждённых условий не подставлять значения по догадке.

- Путь `Swords_B/entities/slime_king.json`; format_version `"1.13.0"`.
- description: `{"identifier":"entity:slime_king","runtime_identifier":"minecraft:slime","is_spawnable":true,"is_summonable":true,"is_experimental":false}`.
- **Повторяющиеся ключи: `["minecraft:movement.jump"]`; следующие выписки могут потерять ранее встреченные значения. Обязательно читать исходник.**

##### Постоянные компоненты

- `minecraft:experience_reward` (строки 30): `{"on_death":"query.last_hit_by_player ? Math.Random(1,3) : 40"}`
- `minecraft:type_family` (строки 33): `{"family":["slime","monster","mob","slime_king"]}`
- `minecraft:attack` (строки 36): `{"damage":9}`
- `minecraft:scale` (строки 39): `{"value":4.3}`
- `minecraft:collision_box` (строки 42): `{"width":0.5,"height":0.5}`
- `minecraft:breathable` (строки 46): `{"total_supply":15,"suffocate_time":0}`
- `minecraft:navigation.walk` (строки 50): `{"can_path_over_water":true,"avoid_water":true}`
- `minecraft:jump.static` (строки 54): `{}`
- `minecraft:can_climb` (строки 56): `{}`
- `minecraft:movement` (строки 58): `{"value":1.1}`
- `minecraft:movement.jump` (строки 61,72): `{"jump_delay":[0.16,0.4]}`
- `minecraft:nameable` (строки 64): `{}`
- `minecraft:health` (строки 66): `{"value":300}`
- `minecraft:knockback_resistance` (строки 69): `{"value":0.5}`
- `minecraft:behavior.slime_float` (строки 75): `{"priority":1}`
- `minecraft:behavior.slime_attack` (строки 78): `{"priority":3}`
- `minecraft:behavior.slime_random_direction` (строки 81): `{"priority":4}`
- `minecraft:behavior.slime_keep_on_jumping` (строки 84): `{"priority":5}`
- `minecraft:behavior.nearest_attackable_target` (строки 87): `{"priority":2,"entity_types":[{"filters":{"any_of":[{"test":"is_family","subject":"other","value":"player"},{"test":"is_family","subject":"other","value":"snowgolem"},{"test":"is_family","subject":"other","value":"irongolem"}]},"max_dist":38}],"must_see":true}`
- `minecraft:damage_sensor` (строки 115): `{"triggers":[{"on_damage":{"filters":{"test":"is_family","subject":"other","value":"player"},"event":"health_bar"},"deals_damage":true},{"on_damage":{"filters":{"all_of":[{"test":"has_damage","subject":"self","value":"fall"}]},"event":"fall_damage"},"deals_damage":false}]}`
- `minecraft:environment_sensor` (строки 131): `{"triggers":[{"filters":{},"event":"slime_effects"}]}`
- `minecraft:physics` (строки 139): `{}`
- `minecraft:pushable` (строки 141): `{"is_pushable":true,"is_pushable_by_piston":true}`

##### Группы компонентов

- `minecraft:slime_large` (строки 12): `{}`
- `minecraft:slime_medium` (строки 14): `{}`
- `minecraft:slime_small` (строки 16): `{}`
- `health_bar` (строки 18,119,149,153): `{"minecraft:boss":{"should_darken_sky":false,"name":"§l§aKing Slime","hud_range":32}}`
- `despawn` (строки 25,147): `{"minecraft:despawn":{}}`

##### События

**`minecraft:despawn`** (строки 26,147):

- `$` — поля действия: `{"add":{"component_groups":["despawn"]}}`

**`health_bar`** (строки 18,119,149,153):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"add":{"component_groups":["health_bar"]}}`
  - `$.sequence[1].randomize`: альтернативы, веса `[95,5]`, сумма 100:
    - ветвь 0, weight `95`; условная доля 19/20 (95%):
      - пустое действие
    - ветвь 1, weight `5`; условная доля 1/20 (5%):
      - `$.sequence[1].randomize[1]` — поля действия: `{"run_command":{"command":["effect @s jump_boost 1 15 true"]}}`

**`fall_damage`** (строки 125,169):

- `$` — поля действия: `{"run_command":{"command":["effect @e[r=3,family=!slime_king] instant_damage 1 1 true","effect @e[r=4,type=iron_golem] instant_damage 1 2 true"]}}`

**`slime_effects`** (строки 135,171):

- `$` — поля действия: `{"run_command":{"command":["effect @s jump_boost 1 0 true","damage @p[r=1.8] 4 magic","damage @e[r=1.5,family=!slime_king] 2 magic"]}}`

<a id="mob-alpha-wolf"></a>
### Alpha Wolf — `entity:alpha_wolf`

Связан с [Silver Sword](#sword-silver_sword) и [Wolf Sword](#sword-wolf_sword). Появление: поверхность `minecraft:grass`, biome taiga без mega, яркость 0–7 с adjust_for_weather, сложность easy–hard, weight 10, herd 1; weight не процент и прямого фильтра ночи нет. По выбору пользователя в ремейке допускать появление при фазе луны 0 и указанных условиях освещённости без отдельного запрета дня; при смене фазы удалять волка. В испытаниях вручную призванный волк сохранялся при времени суток 0, 6000, 18000 и 23999 в день 0 и при 192000 и 210000 в день 8; при 24000, 42000 и 191999 исчезал в пределах 0,25 с. Уже живой волк исчезал при переходе 23999 → 24000 и 210000 → 42000. Естественный дневной спавн отдельно не проверен; фаза 0 с освещённостью 0–7 — выбранное правило ремейка. Health 480, attack 8, movement 0,4, scale 1,8, knockback resistance 0,5, family `[wolf,mob,monster,alpha_wolf]`. Исходное поле опыта записано как `query.last_hit_by_player ? Math.Random(1,3) : 30`: в ветви игрока 1–3, в другой 30; наличие записи не доказывает, что опыт действительно выпадет при любой причине смерти. При несмертельном ударе игрока без Silver в руке после расчёта удара назначить Resistance III и Regeneration III на 20 с; при несмертельном ударе игрока с Silver после расчёта снять оба эффекта. Если удар игрока с Silver смертельный, выполнить одну независимую попытку выдачи Wolf Sword с шансом 10%; отдельный множитель урона Silver не добавлять. В исходнике фильтры смертельного и обычного серебряного попадания пересекаются. В пяти опытах с фатальным командным уроном, приписанным игроку с Silver, оба ранее наложенных эффекта оставались на волке в событии урона; в отдельной серии из 25 таких смертей получен один Wolf Sword. Это подтверждает возможность выдачи, но не измеряет точно её вероятность. Подробности последовательности обычных ударов — в карточке Silver Sword. Клиентский `controller.render.wolf` с default/angry/tame и 27 других алиасов современного контроллера представляют риск совместимости, а не доказанную чёрную текстуру.


**Клиентские ресурсы 2.8.8:** `Swords_R/entity/alpha_wolf.entity.json`, `textures/entity/wolf_transformation.png`; geometry.wolf и controller.render.wolf, ссылки на ванильные wolf_angry/wolf_tame и риск несовпадения алиасов указаны выше.

#### Записанные компоненты и события 2.8.8

Ниже — точные поля сохранённого разбора, не гарантия их исполнения в новой версии. В случае повторяющихся ключей и неподтверждённых условий не подставлять значения по догадке.

- Путь `Swords_B/entities/alpha_wolf.json`; format_version `"1.13.0"`.
- description: `{"animations":{"despawn_wolf":"controller.animation.despawn_wolf"},"identifier":"entity:alpha_wolf","is_experimental":false,"is_spawnable":true,"is_summonable":true,"runtime_identifier":"minecraft:wolf","scripts":{"animate":["despawn_wolf"]}}`.

##### Постоянные компоненты

- `minecraft:angry` (строки 32): `{"broadcast_anger":true,"broadcast_range":30,"calm_event":{},"duration":75}`
- `minecraft:attack` (строки 38): `{"damage":8}`
- `minecraft:behavior.float` (строки 41): `{"priority":0}`
- `minecraft:behavior.hurt_by_target` (строки 44): `{"priority":1}`
- `minecraft:behavior.melee_attack` (строки 47): `{"priority":1,"reach_multiplier":1,"target_dist":3,"track_target":true}`
- `minecraft:behavior.nearest_attackable_target` (строки 53): `{"entity_types":[{"filters":{"any_of":[{"subject":"other","test":"is_family","value":"player"},{"subject":"other","test":"is_family","value":"panda"},{"subject":"other","test":"is_family","value":"irongolem"},{"subject":"other","test":"is_family","value":"snowgolem"},{"subject":"other","test":"is_family","value":"dolphin"},{"subject":"other","test":"is_family","value":"fox"},{"subject":"other","test":"is_family","value":"llama"},{"subject":"other","test":"is_family","value":"mushroomcow"},{"subject":"other","test":"is_family","value":"mule"},{"subject":"other","test":"is_family","value":"panda"},{"subject":"other","test":"is_family","value":"pig"},{"subject":"other","test":"is_family","value":"polarbear"},{"subject":"other","test":"is_family","value":"rabbit"},{"subject":"other","test":"is_family","value":"villager"},{"subject":"other","test":"is_family","value":"wandering_trader"},{"subject":"other","test":"is_family","value":"sheep"},{"subject":"other","test":"is_family","value":"chicken"},{"subject":"other","test":"is_family","value":"cow"},{"subject":"other","test":"is_family","value":"horse"},{"subject":"other","test":"is_family","value":"donkey"}]},"max_dist":30}],"priority":1}`
- `minecraft:behavior.random_stroll` (строки 85): `{"priority":2,"speed_multiplier":1}`
- `minecraft:breathable` (строки 89): `{"suffocate_time":0,"total_supply":15}`
- `minecraft:can_climb` (строки 93): `{}`
- `minecraft:collision_box` (строки 94): `{"height":0.8,"width":0.6}`
- `minecraft:damage_sensor` (строки 98): `{"triggers":[{"deals_damage":true,"on_damage":{"event":"minecraft:wolf_sword","filters":{"all_of":[{"domain":"hand","subject":"other","test":"has_equipment","value":"effect:silver_sword"},{"subject":"other","test":"is_family","value":"player"},{"test":"has_damage","value":"fatal"}]}}},{"deals_damage":true,"on_damage":{"event":"add_effects","filters":{"all_of":[{"domain":"hand","operator":"!=","subject":"other","test":"has_equipment","value":"effect:silver_sword"},{"subject":"other","test":"is_family","value":"player"}]}}},{"deals_damage":true,"on_damage":{"event":"clear_effects","filters":{"all_of":[{"domain":"hand","subject":"other","test":"has_equipment","value":"effect:silver_sword"},{"subject":"other","test":"is_family","value":"player"}]}}}]}`
- `minecraft:experience_reward` (строки 170): `{"on_bred":"Math.Random(1,7)","on_death":"query.last_hit_by_player ? Math.Random(1,3) : 30"}`
- `minecraft:health` (строки 174): `{"max":480,"value":480}`
- `minecraft:hurt_on_condition` (строки 178): `{"damage_conditions":[{"cause":"lava","damage_per_tick":4,"filters":{"operator":"==","subject":"self","test":"in_lava","value":true}}]}`
- `minecraft:jump.static` (строки 192): `{}`
- `minecraft:knockback_resistance` (строки 193): `{"value":0.5}`
- `minecraft:movement` (строки 196): `{"value":0.4}`
- `minecraft:movement.basic` (строки 199): `{}`
- `minecraft:nameable` (строки 200): `{}`
- `minecraft:navigation.walk` (строки 201): `{"avoid_damage_blocks":true,"can_path_over_water":true}`
- `minecraft:physics` (строки 205): `{}`
- `minecraft:pushable` (строки 206): `{"is_pushable":true,"is_pushable_by_piston":true}`
- `minecraft:scale` (строки 210): `{"value":1.8}`
- `minecraft:type_family` (строки 213): `{"family":["wolf","mob","monster","alpha_wolf"]}`

##### Группы компонентов

- `despawn` (строки 20,249,252): `{"minecraft:despawn":{}}`
- `health_bar` (строки 23,226,239): `{"minecraft:boss":{"hud_range":16,"name":"§l§7Alpha Wolf","should_darken_sky":false}}`

##### События

**`add_effects`** (строки 128,223):

- `$` — поля действия: `{"add":{"component_groups":["health_bar"]},"run_command":{"command":["effect @s resistance 20 2 true","effect @s regeneration 20 2 true"]}}`

**`clear_effects`** (строки 150,236):

- `$` — поля действия: `{"add":{"component_groups":["health_bar"]},"run_command":{"command":["effect @s resistance 0","effect @s regeneration 0"]}}`

**`despawn`** (строки 20,249,252):

- `$` — поля действия: `{"add":{"component_groups":["despawn"]},"run_command":{"command":["stopsound @a wolf_sword.distant_howl"]}}`

**`minecraft:entity_spawned`** (строки 261):

- `$` — поля действия: `{"run_command":{"command":["playsound wolf_sword.distant_howl @a[rm=25,r=100]"]}}`

**`minecraft:wolf_sword`** (строки 103,268):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0].randomize`: альтернативы, веса `[90,10]`, сумма 100:
    - ветвь 0, weight `90`; условная доля 9/10 (90%):
      - пустое действие
    - ветвь 1, weight `10`; условная доля 1/10 (10%):
      - `$.sequence[0].randomize[1]` — поля действия: `{"run_command":{"command":["structure load wolf_sword ~ ~ ~"]}}`

<a id="mob-grass-witch"></a>
### Grass Witch — `minecraft:witch`

Связана с [Grass Sword](#sword-grass_sword) и [травяным помощником](#mob-grass-helper). При событии появления ночью выбирать обычный вариант или группы grass_witch с весами 80/20; по решению пользователя добавлено ограничение ночи, которого в исходном выборе нет. Вне ночи этот выбор травяной формы не выполнять. Специальная форма: variant 1, family `[witch,monster,mob,grass_witch]`, health 32, scale 1,1, follow_range 80; отдельный боевой selector цели max_dist 10. По смерти специальной формы отдельный выбор 80/20: пусто или загрузка меча, установка double_plant data 2 и звук. Обе выборки в идеальной модели дают 4%, но не доказывают итоговую выдачу. Навык ищет в r=8, исключая family grass_witch и shulker_sword, item, `entity:grass`, xp_orb, arrow и tag grass; **игрок не исключён**. Дополнительные условия блока и поведение помощника — в его пункте. Пустой filters у sensor не задаёт проверенную частоту.


**Клиентские ресурсы 2.8.8:** `Swords_R/entity/witch.entity.json` и `witch.v1.0.entity.json` оба объявляют `minecraft:witch`; `textures/entity/grass_witch.png`. Варианты контроллера и приоритет загрузки двух определений проверить.

#### Записанные компоненты и события 2.8.8

Ниже — точные поля сохранённого разбора, не гарантия их исполнения в новой версии. В случае повторяющихся ключей и неподтверждённых условий не подставлять значения по догадке.

- Путь `Swords_B/entities/witch.json`; format_version `"1.13.0"`.
- description: `{"identifier":"minecraft:witch","is_spawnable":true,"is_summonable":true,"is_experimental":false}`.

##### Постоянные компоненты

- `minecraft:experience_reward` (строки 92): `{"on_death":"query.last_hit_by_player ? (query.is_baby ? 12 : 5) + (Math.die_roll(query.equipment_count,1,3)) : 0"}`
- `minecraft:breathable` (строки 95): `{"total_supply":15,"suffocate_time":0}`
- `minecraft:nameable` (строки 99): `{}`
- `minecraft:loot` (строки 25,101): `{"table":"loot_tables/entities/witch.json"}`
- `minecraft:health` (строки 37,104): `{"value":26,"max":26}`
- `minecraft:hurt_on_condition` (строки 108): `{"damage_conditions":[{"filters":{"test":"in_lava","subject":"self","operator":"==","value":true},"cause":"lava","damage_per_tick":4}]}`
- `minecraft:movement` (строки 117): `{"value":0.25}`
- `minecraft:navigation.walk` (строки 120): `{"can_path_over_water":true,"avoid_water":false}`
- `minecraft:movement.basic` (строки 124): `{}`
- `minecraft:jump.static` (строки 126): `{}`
- `minecraft:can_climb` (строки 128): `{}`
- `minecraft:behavior.float` (строки 130): `{"priority":1}`
- `minecraft:behavior.ranged_attack` (строки 133): `{"priority":2,"speed_multiplier":1.0,"attack_interval_min":3,"attack_interval_max":3,"attack_radius":10.0}`
- `minecraft:behavior.random_stroll` (строки 140): `{"priority":4,"speed_multiplier":1.0}`
- `minecraft:behavior.look_at_player` (строки 144): `{"priority":5,"look_distance":8.0}`
- `minecraft:behavior.random_look_around` (строки 148): `{"priority":5,"look_distance":8.0}`
- `minecraft:behavior.hurt_by_target` (строки 152): `{"priority":1}`
- `minecraft:behavior.nearest_attackable_target` (строки 155): `{"priority":2,"entity_types":[{"filters":{"any_of":[{"test":"is_family","subject":"other","value":"player"},{"test":"is_family","subject":"other","value":"snowgolem"},{"test":"is_family","subject":"other","value":"irongolem"}]},"max_dist":10}],"must_reach":true}`
- `minecraft:type_family` (строки 22,183): `{"family":["witch","monster","mob"]}`
- `minecraft:collision_box` (строки 186): `{"width":0.6,"height":1.9}`
- `minecraft:physics` (строки 190): `{}`
- `minecraft:pushable` (строки 192): `{"is_pushable":true,"is_pushable_by_piston":true}`
- `minecraft:follow_range` (строки 31,196): `{"value":64}`

##### Группы компонентов

- `minecraft:default_witch` (строки 11,205): `{"minecraft:variant":{"value":0}}`
- `minecraft:grass_witch` (строки 16,209,224,225): `{"minecraft:variant":{"value":1}}`
- `grass_witch` (строки 21,23,209,225): `{"minecraft:type_family":{"family":["witch","monster","mob","grass_witch"]},"minecraft:loot":{},"minecraft:on_death":{"event":"grass_sword","target":"self"},"minecraft:follow_range":{"value":80},"minecraft:scale":{"value":1.1},"minecraft:health":{"value":32,"max":32},"minecraft:environment_sensor":{"triggers":[{"filters":{},"event":"grass_witch_skill"}]}}`
- `minecraft:celebrate` (строки 50,241,244): `{"minecraft:behavior.celebrate":{"priority":5,"celebration_sound":"celebrate","sound_interval":{"range_min":2.0,"range_max":7.0},"jump_interval":{"range_min":1.0,"range_max":3.5},"duration":30.0,"on_celebration_end_event":{"event":"minecraft:stop_celebrating","target":"self"}}}`
- `minecraft:raid_configuration` (строки 69,236): `{"minecraft:dweller":{"dwelling_type":"village","dweller_role":"hostile","update_interval_base":60,"update_interval_variant":40,"can_find_poi":false,"can_migrate":false,"first_founding_reward":0},"minecraft:behavior.move_to_village":{"priority":3,"speed_multiplier":1.2,"goal_radius":2.0},"minecraft:ambient_sound_interval":{"value":2.0,"range":4.0,"event_name":"ambient.in.raid"}}`

##### События

**`minecraft:entity_spawned`** (строки 201):

- `$.randomize`: альтернативы, веса `[80,20]`, сумма 100:
  - ветвь 0, weight `80`; условная доля 4/5 (80%):
    - `$.randomize[0]` — поля действия: `{"add":{"component_groups":["minecraft:default_witch"]}}`
  - ветвь 1, weight `20`; условная доля 1/5 (20%):
    - `$.randomize[1]` — поля действия: `{"add":{"component_groups":["minecraft:grass_witch","grass_witch"]}}`

**`grass_sword`** (строки 28,213):

- `$.randomize`: альтернативы, веса `[80,20]`, сумма 100:
  - ветвь 0, weight `80`; условная доля 4/5 (80%):
    - пустое действие
  - ветвь 1, weight `20`; условная доля 1/5 (20%):
    - `$.randomize[1]` — поля действия: `{"run_command":{"command":["structure load grass_sword ~~~","setblock ~ ~ ~ double_plant 2","playsound dig.grass @a[r=12] ~~~"]}}`

**`minecraft:grass_witch`** (строки 16,209,224,225):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:grass_witch","grass_witch"]}}`

**`grass_witch_skill`** (строки 45,227):

- `$` — поля действия: `{"run_command":{"command":["execute @e[family=!grass_witch,type=!item,type=!entity:grass,type=!xp_orb,type=!arrow,r=8,tag=!grass,family=!shulker_sword] ~ ~ ~ detect ~ ~-0.1 ~ grass 0 execute @s ~ ~ ~ detect ~ ~ ~ air 0 summon entity:grass","execute @e[family=!grass_witch,type=!item,type=!entity:grass,type=!xp_orb,type=!arrow,r=8,tag=!grass,family=!shulker_sword] ~ ~ ~ detect ~ ~-0.1 ~ grass 0 execute @s ~ ~ ~ detect ~ ~ ~ tallgrass 0 summon entity:grass"]}}`

**`minecraft:spawn_for_raid`** (строки 233):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:raid_configuration"]}}`

**`minecraft:start_celebrating`** (строки 240):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:celebrate"]}}`

**`minecraft:stop_celebrating`** (строки 64,243):

- `$` — поля действия: `{"remove":{"component_groups":["minecraft:celebrate"]}}`

<a id="mob-centella"></a>
### Centella — `entity:centella`

Связана с [Lightning Sword](#sword-lightning_sword): обычное событие появления молнии запускает выбор сущности с весом 20/100 без прямой проверки грозы; специальные молнии не запускают этот выбор в ремейке. Health 200, movement 0,22, family `[effect99_entities,centella,spherical_lightning]`, иммунитет к огню, случайный таймер `[10,60]` с на despawn. Sensor в r=2 назначает instant_damage amplifier 0 сущностям без family effect99_entities; также slow_falling себе, свет и звук. При фатальном уроне вызвать одну молнию; если источник — игрок, дополнительно выбрать Lightning Sword с шансом 2%; по решению пользователя реальный игрок считается игроком и при превращении. В исходнике два пересекающихся damage trigger: игрок+fatal и общий при любом fatal. В пяти опытах с фатальным уроном, приписанным игроку, наблюдалось только событие игрока и одна молния; в пяти опытах с магическим уроном без игрока — только общее событие и одна молния. Молния вызывается с `default_lightning_bolt`: в отдельном сравнении 25 таких вызовов не создали Centella, в отличие от 6 появлений после 25 вызовов без этого события. Это результаты ограниченной выборки, не доказательство частоты или всех возможных контекстов. Локальной таблицы `loot_tables/entity/centella.json` не найдено.

#### Записанные компоненты и события 2.8.8

Ниже — точные поля сохранённого разбора, не гарантия их исполнения в новой версии. В случае повторяющихся ключей и неподтверждённых условий не подставлять значения по догадке.

- Путь `Swords_B/entities/centella.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:centella","is_spawnable":false,"is_summonable":true,"is_experimental":false}`.

##### Постоянные компоненты

- `minecraft:type_family` (строки 16): `{"family":["effect99_entities","centella","spherical_lightning"]}`
- `minecraft:on_death` (строки 18): `{"event":"minecraft:start_death","target":"self"}`
- `minecraft:damage_sensor` (строки 21): `{"triggers":[{"on_damage":{"filters":{"all_of":[{"test":"has_damage","value":"fatal"},{"test":"is_family","subject":"other","value":"player"}]},"event":"centella_death_by_player"},"deals_damage":true},{"on_damage":{"filters":{"all_of":[{"test":"has_damage","value":"fatal"}]},"event":"centella_death"},"deals_damage":true}]}`
- `minecraft:movement` (строки 39): `{"value":0.22}`
- `minecraft:loot` (строки 42): `{"table":"loot_tables/entity/centella.json"}`
- `minecraft:navigation.walk` (строки 45): `{"can_path_over_water":false,"can_path_over_lava":true,"can_walk_in_lava":true,"can_jump":false,"avoid_water":true,"avoid_damage_blocks":false}`
- `minecraft:movement.basic` (строки 53): `{}`
- `minecraft:jump.static` (строки 55): `{}`
- `minecraft:can_climb` (строки 57): `{}`
- `minecraft:behavior.random_stroll` (строки 59): `{"priority":1,"speed_multiplier":0.7}`
- `minecraft:behavior.float` (строки 63): `{"priority":1}`
- `minecraft:timer` (строки 66): `{"time":[10,60],"looping":true,"randomInterval":true,"time_down_event":{"event":"minecraft:start_death","target":"self"}}`
- `minecraft:health` (строки 68): `{"value":200}`
- `minecraft:collision_box` (строки 69): `{"width":0.8,"height":1.5}`
- `minecraft:fire_immune` (строки 70): `true`
- `minecraft:physics` (строки 71): `{}`
- `minecraft:environment_sensor` (строки 72): `[{"on_environment":{"filters":{"test":"is_family","value":"centella"},"event":"minecraft:centella"}}]`

##### Группы компонентов

- `despawn` (строки 11,93): `{"minecraft:despawn":{}}`

##### События

**`minecraft:entity_spawned`** (строки 75):


**`minecraft:centella`** (строки 72,77):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"run_command":{"command":["particle minecraft:example_directional_sphere ~ ~1.3 ~","effect @e[family=!effect99_entities,r=2] instant_damage 1 0 true","effect @s slow_falling 10 0 true","playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3","fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock 0 replace air","fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock 0 replace effect99:lightblock"]}}`

**`minecraft:start_death`** (строки 19,66,92):

- `$` — поля действия: `{"add":{"component_groups":["despawn"]}}`

**`centella_death_by_player`** (строки 27,95):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"run_command":{"command":["summon lightning_bolt ~~~ default_lightning_bolt","say 1"]}}`
  - `$.sequence[1].randomize`: альтернативы, веса `[98,2]`, сумма 100:
    - ветвь 0, weight `98`; условная доля 49/50 (98%):
      - пустое действие
    - ветвь 1, weight `2`; условная доля 1/50 (2%):
      - `$.sequence[1].randomize[1]` — поля действия: `{"run_command":{"command":["structure load lightning_sword ~ ~10 ~"]}}`

**`centella_death`** (строки 33,113):

- `$` — поля действия: `{"run_command":{"command":["summon lightning_bolt ~~~ default_lightning_bolt","say 2"]}}`

<a id="mob-living-flame"></a>
### Living Flame — `entity:living_flame`

Связано с [Fire Sword](#sword-fire_sword). Естественное появление: под землёй в биоме с тегом nether, сложность easy–hard, вес 20, группа 1–4; вес не процент. Базовые health 20 и attack 3; пассивная форма ищет монстров до 16 и использует таймер 10–30 с, враждебная — монстров и игроков до 16 и таймер 25–60 с; применение групп и итоговую жизнь проверить. По решению пользователя пассивное Living Flame, выпущенное Fire Sword, не выбирает своего владельца и призванных помощников любых игроков целью и не наносит им прямой урон или поджог, включая случай превращения владельца в волка; это не объявляет все формы Living Flame помощниками. В сохранённой ветви враждебной не-снарядной формы при подходящем событии игрока/смерти выбор 15/100 вызывает `loot spawn` для таблицы `entities/living_flame`, содержащей Fire Sword, 85/100 не выдаёт. Исходный sensor на удар игрока также вызывает событие без обычного нанесения урона; в ремейке получение при убийстве сохранять по описанию пользователя. Не приравнивать к шансу при каждом истечении таймера. Отдельные пять помощников огненного дождя нацеливаются на единую созданную цель; их timer 10 с и дальность 64 не означают пять врагов.

#### Записанные компоненты и события 2.8.8

Ниже — точные поля сохранённого разбора, не гарантия их исполнения в новой версии. В случае повторяющихся ключей и неподтверждённых условий не подставлять значения по догадке.

- Путь `Swords_B/entities/living_flame.json`; format_version `"1.13.0"`.
- description: `{"identifier":"entity:living_flame","is_spawnable":false,"is_summonable":true,"is_experimental":false}`.
- **Повторяющиеся ключи: `["minecraft:fire_immune"]`; следующие выписки могут потерять ранее встреченные значения. Обязательно читать исходник.**

##### Постоянные компоненты

- `minecraft:type_family` (строки 15,32,37,79,93,104): `{"family":["living_flame","effect99_entities"]}`
- `minecraft:on_death` (строки 72,84,105): `{"event":"minecraft:start_death","target":"self"}`
- `minecraft:movement` (строки 107): `{"value":0.25}`
- `minecraft:behavior.random_stroll` (строки 109): `{"interval":60,"xz_dist":16}`
- `minecraft:navigation.walk` (строки 113): `{"can_path_over_water":false,"can_path_over_lava":true,"can_walk_in_lava":true,"can_jump":false,"avoid_water":true,"avoid_damage_blocks":false}`
- `minecraft:movement.basic` (строки 121): `{}`
- `minecraft:fire_immune` (строки 123,170): `true`
- `minecraft:nameable` (строки 124): `{"allow_name_tag_renaming":false,"always_show":true}`
- `minecraft:ageable` (строки 126): `{"duration":1,"grow_up":{"event":"hostile_entity_detect","target":"self"}}`
- `minecraft:hurt_on_condition` (строки 133): `{"damage_conditions":[{"filters":{"test":"in_water_or_rain","operator":"==","value":true},"cause":"drowning","damage_per_tick":1}]}`
- `minecraft:jump.static` (строки 138): `{}`
- `minecraft:can_climb` (строки 140): `{}`
- `minecraft:behavior.float` (строки 142): `{"priority":1}`
- `minecraft:attack` (строки 145): `{"damage":3}`
- `minecraft:behavior.melee_attack` (строки 148): `{"priority":4,"target_dist":1.2,"speed_multiplier":1.0,"track_target":true}`
- `minecraft:timer` (строки 16,33,80,94,154): `{"time":[10,40],"looping":true,"randomInterval":true,"time_down_event":{"event":"minecraft:start_death","target":"self"}}`
- `minecraft:behavior.nearest_attackable_target` (строки 26,30,38,65,85,156): `{"priority":2,"entity_types":[{"filters":{"any_of":[{"test":"is_family","subject":"other","value":"monster"},{"test":"is_family","subject":"other","value":"player"}]},"max_dist":16}]}`
- `minecraft:behavior.hurt_by_target` (строки 164): `{"priority":1,"alert_same_type":true}`
- `minecraft:health` (строки 168): `{"value":20}`
- `minecraft:collision_box` (строки 13,78,92,169): `{"width":0.8,"height":1.3}`
- `minecraft:physics` (строки 14,34,171): `{}`
- `minecraft:environment_sensor` (строки 172): `{"triggers":[{"filters":{"all_of":[{"test":"is_family","subject":"self","operator":"!=","value":"fire_sword_skill"},{"test":"is_family","subject":"self","operator":"!=","value":"target"}]},"event":"minecraft:set_fire"}]}`

##### Группы компонентов

- `fire_sword_skill` (строки 11,15,176,204,270): `{"minecraft:damage_sensor":{"triggers":{"cause":"all","deals_damage":false}},"minecraft:collision_box":{"width":0.1,"height":0.1},"minecraft:physics":{"has_gravity":false,"has_collision":false},"minecraft:type_family":{"family":["fire_sword_skill","effect99_entities"]},"minecraft:timer":{"time":[10,10],"looping":false,"time_down_event":{"event":"minecraft:despawn","target":"self"}},"minecraft:behavior.ranged_attack":{"attack_interval":0.1,"attack_radius":64},"minecraft:shooter":{"def":"minecraft:small_fireball"},"minecraft:behavior.nearest_attackable_target":{"priority":2,"entity_types":[{"filters":{"test":"is_family","subject":"other","value":"target"},"max_dist":64}]}}`
- `target` (строки 17,27,29,32,33,46,72,80,84,94,105,130,154,177,205,268): `{"minecraft:behavior.nearest_attackable_target":{},"minecraft:damage_sensor":{"triggers":{"cause":"all","deals_damage":false}},"minecraft:type_family":{"family":["target","effect99_entities"]},"minecraft:timer":{"time":[10,10],"looping":false,"time_down_event":{"event":"minecraft:despawn","target":"self"}},"minecraft:physics":{"has_gravity":false,"has_collision":false}}`
- `living_flame_projectile` (строки 36,37,189,203,243,259): `{"minecraft:type_family":{"family":["living_flame","living_flame_projectile","effect99_entities"]},"minecraft:behavior.nearest_attackable_target":{},"minecraft:damage_sensor":{"triggers":{"cause":"all","deals_damage":false}},"minecraft:projectile":{"on_hit":{"definition_event":{"affect_projectile":true,"event_trigger":{"event":"minecraft:stop_projectile","target":"self"}},"impact_damage":{"damage":1,"knockback":true,"catch_fire":true}},"power":1,"gravity":0.02,"inertia":1,"liquid_inertia":1}}`
- `despawn` (строки 61,221,233,266): `{"minecraft:despawn":{}}`
- `hostile_entity` (строки 64,194,195,208,259): `{"minecraft:behavior.nearest_attackable_target":{"priority":1,"entity_types":[{"filters":{"any_of":[{"test":"is_family","subject":"other","value":"monster"},{"test":"is_family","subject":"other","value":"player"}]},"max_dist":16}]},"minecraft:on_death":{"event":"start_death_hostile","target":"self"},"minecraft:damage_sensor":{"triggers":{"on_damage":{"filters":{"all_of":[{"test":"is_family","subject":"other","value":"player"}]},"event":"start_death_hostile"},"deals_damage":false}},"minecraft:collision_box":{"width":0.8,"height":1.3},"minecraft:type_family":{"family":["living_flame","living_flame_hostile","effect99_entities"]},"minecraft:timer":{"time":[25,60],"looping":true,"randomInterval":true,"time_down_event":{"event":"minecraft:start_death","target":"self"}}}`
- `passive_entity` (строки 83,262): `{"minecraft:on_death":{"event":"minecraft:start_death","target":"self"},"minecraft:behavior.nearest_attackable_target":{"entity_types":[{"filters":{"any_of":[{"test":"is_family","subject":"other","value":"monster"}]},"max_dist":16}]},"minecraft:collision_box":{"width":0.8,"height":1.3},"minecraft:type_family":{"family":["living_flame","living_flame_passive","effect99_entities"]},"minecraft:timer":{"time":[10,30],"looping":true,"randomInterval":true,"time_down_event":{"event":"minecraft:start_death","target":"self"}},"minecraft:damage_sensor":{"triggers":{"on_damage":{"filters":{"all_of":[{"test":"is_family","subject":"other","value":"player"}]},"event":"minecraft:start_death"},"deals_damage":false}}}`

##### События

**`minecraft:entity_spawned`** (строки 184):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"has_equipment","subject":"other","domain":"hand","value":"effect:fire_sword"},"add":{"component_groups":["living_flame_projectile"]}}`

**`hostile_entity`** (строки 64,194,195,208,259):

- `$` — поля действия: `{"add":{"component_groups":["hostile_entity"]}}`

**`hostile_entity_detect`** (строки 129,197):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"all_of":[{"test":"is_family","subject":"self","operator":"!=","value":"living_flame_hostile"},{"test":"is_family","subject":"self","operator":"!=","value":"living_flame_passive"},{"test":"is_family","subject":"self","operator":"!=","value":"living_flame_projectile"},{"test":"is_family","subject":"self","operator":"!=","value":"fire_sword_skill"},{"test":"is_family","subject":"self","operator":"!=","value":"target"}]},"add":{"component_groups":["hostile_entity"]}}`

**`minecraft:set_fire`** (строки 178,212):

- `$` — поля действия: `{"run_command":{"command":["fill ~ ~ ~ ~ ~ ~ fire 0 replace air","particle minecraft:basic_flame_particle ~ ~1 ~"]}}`

**`minecraft:start_death`** (строки 80,84,94,97,105,154,220):

- `$` — поля действия: `{"add":{"component_groups":["despawn"]},"run_command":{"command":["fill ~ ~ ~ ~ ~ ~ air 0 replace fire","particle minecraft:example_linearcurve ~ ~0.4 ~","playsound random.fizz @a[r=12] ~ ~ ~"]}}`

**`start_death_hostile`** (строки 72,74,230):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"add":{"component_groups":["despawn"]},"run_command":{"command":["fill ~ ~ ~ ~ ~ ~ air 0 replace fire","particle minecraft:example_linearcurve ~ ~0.4 ~","playsound random.fizz @a[r=12] ~ ~ ~"]}}`
  - `$.sequence[1]` — поля действия: `{"filters":{"all_of":[{"test":"is_family","subject":"self","operator":"!=","value":"living_flame_passive"},{"test":"is_family","subject":"self","operator":"!=","value":"living_flame_projectile"}]}}`
  - `$.sequence[1].randomize`: альтернативы, веса `[85,15]`, сумма 100:
    - ветвь 0, weight `85`; условная доля 17/20 (85%):
      - пустое действие
    - ветвь 1, weight `15`; условная доля 3/20 (15%):
      - `$.sequence[1].randomize[1]` — поля действия: `{"run_command":{"command":["loot spawn ~ ~ ~ loot \"entities/living_flame\""]}}`

**`minecraft:stop_projectile`** (строки 45,256):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"remove":{"component_groups":["hostile_entity","living_flame_projectile"]}}`
  - `$.sequence[1]` — поля действия: `{"add":{"component_groups":["passive_entity"]}}`

**`minecraft:despawn`** (строки 17,33,62,266):

- `$` — поля действия: `{"add":{"component_groups":["despawn"]}}`

**`minecraft:target`** (строки 268):

- `$` — поля действия: `{"add":{"component_groups":["target"]}}`

**`fire_sword_skill`** (строки 11,15,176,204,270):

- `$` — поля действия: `{"add":{"component_groups":["fire_sword_skill"]}}`

<a id="mob-mountable-slime"></a>
### Ездовой слизень — `entity:mountable_slime`

Вызывается [Slime Sword](#sword-slime_sword). Начальная группа: health 1, movement 0,25, одно место, jump delay 0,16–0,5, jump strength 0,8–2. После спешивания `minecraft:despawn` добавляет защитный режим, а отдельное событие `despawn` запускает удаление: имена не равнозначны. Защитный режим movement 0,45, attack 1, видимые family monster/undead до 16. При падении записаны instant_damage для не-undead и instant_health для undead r=1 с отдельными исключениями. Защита не включает void. Защитное событие при score 0 выбирает ближайшего подходящего игрока на расстоянии 8–12, повышает счётчик и при 100 отправляет despawn. Удержание меча способно сбрасывать ближайшего слизня в r=12; снятие выбирает ближайшего в r=32, а не идентификатор владельца. Повторяющийся ключ `despawn` делает часть исходного разбора неоднозначной. В ремейке по решению пользователя защиту, поиск игрока и снятие привязать к конкретному владельцу, а не к ближайшему подходящему игроку. Собственный слизень не выбирает владельца целью и не задевает его своими эффектами, включая эффект падения после спешивания, даже если владелец превратился в волка; для других игроков отдельного нового правила не добавлять. Защитный слизень также не атакует и не наносит урон призванным помощникам любых игроков, включая эффект падения. Модель использует текстурные координаты 64×32, это не физический размер.


**Клиентские ресурсы 2.8.8:** `Swords_R/entity/mountable_slime.v1.0.json`, `textures/entity/slime/baby_slime.png`, `models/entity/mountable_slime.geo.json`, `models/entity/baby_slime.geo.json`, `animations/baby_slime.animation.json`.

#### Записанные компоненты и события 2.8.8

Ниже — точные поля сохранённого разбора, не гарантия их исполнения в новой версии. В случае повторяющихся ключей и неподтверждённых условий не подставлять значения по догадке.

- Путь `Swords_B/entities/mountable_slime.json`; format_version `"1.13.0"`.
- description: `{"identifier":"entity:mountable_slime","runtime_identifier":"minecraft:slime","is_spawnable":false,"is_summonable":true,"is_experimental":false,"scripts":{"animate":["despawn","mountable_slime"]},"animations":{"despawn":"controller.animation.despawn","mountable_slime":"controller.animation.mountable_slime"}}`.
- **Повторяющиеся ключи: `["despawn"]`; следующие выписки могут потерять ранее встреченные значения. Обязательно читать исходник.**

##### Постоянные компоненты

- `minecraft:environment_sensor` (строки 67,150): `{"triggers":[{"filters":{},"event":"minecraft:is_jumping"}]}`
- `minecraft:damage_sensor` (строки 158): `{"triggers":[{"on_damage":{"filters":{"all_of":[{"test":"has_damage","subject":"self","value":"fall"}]},"event":"fall_damage"},"deals_damage":false},{"on_damage":{"filters":{"all_of":[{"test":"has_damage","subject":"self","operator":"!=","value":"void"}]}},"deals_damage":false}]}`

##### Группы компонентов

- `despawn` (строки 11,14,19,144,180,182): `{"minecraft:despawn":{}}`
- `minecraft:is_jumping` (строки 22,71,154,202,225,227): `{"minecraft:is_baby":{}}`
- `slime_random_direction` (строки 26,222): `{"minecraft:behavior.slime_random_direction":{"priority":4}}`
- `default_slime` (строки 31,176,220): `{"minecraft:behavior.slime_float":{"priority":1},"minecraft:behavior.slime_keep_on_jumping":{"priority":5},"minecraft:movement":{"value":0.25},"minecraft:movement.jump":{"jump_delay":[0.16,0.5]},"minecraft:navigation.walk":{"can_path_over_water":true},"minecraft:jump.static":{},"minecraft:can_climb":{},"minecraft:type_family":{"family":["effect99_entities","tamed_slime"]},"minecraft:health":{"value":1},"minecraft:collision_box":{"width":0.6,"height":0.0},"minecraft:physics":{},"minecraft:rideable":{"crouching_skip_interact":true,"seat_count":1,"family_types":["player"],"seats":{"position":[0.0,0.35,0.0]}},"minecraft:input_ground_controlled":{},"minecraft:behavior.controlled_by_player":{"priority":0},"minecraft:can_power_jump":{},"minecraft:horse.jump_strength":{"value":{"range_min":0.8,"range_max":2.0}},"minecraft:is_tamed":{}}`
- `defense_mode_slime` (строки 52,178): `{"minecraft:type_family":{"family":["effect99_entities","tamed_slime","player"]},"minecraft:movement":{"value":0.45},"minecraft:behavior.slime_attack":{"priority":3,"set_persistent":true},"minecraft:behavior.slime_random_direction":{"priority":4},"minecraft:behavior.slime_keep_on_jumping":{"priority":5},"minecraft:environment_sensor":{"triggers":[{"filters":{},"event":"minecraft:is_jumping"},{"filters":{},"event":"slime_events"}]},"minecraft:behavior.nearest_attackable_target":{"priority":1,"entity_types":[{"filters":{"any_of":[{"test":"is_family","subject":"other","value":"monster"},{"test":"is_family","subject":"other","value":"undead"}]},"max_dist":16}],"must_see":true,"set_persistent":true,"must_reach":false},"minecraft:attack":{"damage":1}}`
- `minecraft:slime_large` (строки 108): `{"minecraft:type_family":{"family":["effect99_entities","slime3","tamed_slime"]},"minecraft:rideable":{"crouching_skip_interact":true,"seat_count":1,"family_types":["player"],"seats":{"position":[0.0,1.9,0.0]}},"minecraft:collision_box":{"width":0.4,"height":0.0},"minecraft:movement":{"value":0.25},"minecraft:scale":{"value":0.4}}`
- `minecraft:slime_medium` (строки 120): `{"minecraft:type_family":{"family":["effect99_entities","slime2","tamed_slime"]},"minecraft:rideable":{"crouching_skip_interact":true,"seat_count":1,"family_types":["player"],"seats":{"position":[0.0,0.9,0.0]}},"minecraft:collision_box":{"width":0.4,"height":0.0},"minecraft:movement":{"value":0.25},"minecraft:scale":{"value":0.8}}`
- `minecraft:slime_small` (строки 132): `{"minecraft:type_family":{"family":["effect99_entities","slime1","tamed_slime"]},"minecraft:rideable":{"crouching_skip_interact":true,"seat_count":1,"family_types":["player"],"seats":{"position":[0.0,0.46,0.0]}},"minecraft:collision_box":{"width":0.4,"height":0.0},"minecraft:movement":{"value":0.25},"minecraft:scale":{"value":1.5}}`

##### События

**`minecraft:entity_spawned`** (строки 175):

- `$` — поля действия: `{"add":{"component_groups":["default_slime"]}}`

**`minecraft:despawn`** (строки 20,145,178):

- `$` — поля действия: `{"add":{"component_groups":["defense_mode_slime"]}}`

**`despawn`** (строки 11,14,19,144,180,182):

- `$` — поля действия: `{"add":{"component_groups":["despawn"]},"run_command":{"command":["particle minecraft:crop_growth_emitter ~ ~ ~","particle minecraft:crop_growth_emitter ~ ~0.6 ~","particle minecraft:crop_growth_emitter ~ ~-0.6 ~","particle minecraft:crop_growth_emitter ~0.6 ~ ~","particle minecraft:crop_growth_emitter ~ ~ ~0.6","particle minecraft:crop_growth_emitter ~-0.6 ~ ~","particle minecraft:crop_growth_emitter ~ ~ ~-0.6","playsound random.orb @a[r=12] ~ ~ ~ 1 0.6"]}}`

**`fall_damage`** (строки 162,197):

- `$` — поля действия: `{"run_command":{"command":["effect @e[r=1,family=!slime_sword,family=!undead] instant_damage 1 1 true","effect @e[r=1,family=undead] instant_health 3 1 true","event entity @s not_baby"]}}`

**`minecraft:is_jumping`** (строки 22,71,154,202,225,227):

- `$` — поля действия: `{"run_command":{"command":["execute @s ~~~ detect ~ ~-1 ~ air 0 execute @s ~~~ detect ~ ~-2 ~ air 0 event entity @s is_baby"]}}`

**`slime_events`** (строки 75,209):

- `$` — поля действия: `{"run_command":{"command":["effect @s jump_boost 1 2 true","execute @e[r=1,family=monster] ~~~ summon entity:slime_damage","tp @s[scores={slime_despawn=0}] @e[type=player,family=slime_sword,c=1,rm=8,r=12]","scoreboard players add @s slime_despawn 1","execute @s[scores={slime_despawn=100}] ~~~ event entity @s despawn"]}}`

**`default_slime`** (строки 31,176,220):

- `$` — поля действия: `{"remove":{"component_groups":["slime_random_direction"]}}`

**`is_baby`** (строки 225):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:is_jumping"]}}`

**`not_baby`** (строки 227):

- `$` — поля действия: `{"remove":{"component_groups":["minecraft:is_jumping"]}}`

<a id="mob-bee-sword"></a>
### Пчела меча — `entity:bee_sword`

Создаётся [Bee Stinger](#sword-bee_sword) и не является обычной `minecraft:bee`. Health 10, scale 0,5, collision 0,55×0,5, movement 0,3, flying_speed 0,15, follow_range 1024. Target: family monster, within_radius 16, max_dist 10, must_see true; melee speed multiplier 1,4, attack 1, fatal_poison duration 3. Angry duration 99999, broadcast range 20; лава задаёт damage_per_tick 4. Damage от other family player и fall отменяется; это не проверка владельца и не защита от всех видов урона. Timer `[6,8]` с вызывает `tp @s ~ -103 ~` (абсолютная y=−103), а не объявленный kill; реальное удаление проверить. При Wolf-превращении family игрока может включать monster и не включать player; исходные фильтры не доказывают защиты конкретного владельца. По решению пользователя каждая призванная пчела привязана к владельцу и не выбирает его целью и не наносит ему вред, включая случай Wolf-превращения; для других игроков отдельного нового правила не добавлять. Пчела также не атакует и не наносит урон призванным помощникам любых игроков, в том числе ездовым паукам.


**Клиентские ресурсы 2.8.8:** `Swords_R/entity/bee_sword.json`: texture `textures/entity/bee/bee_angry`, geometry `geometry.bee`, controller.render.default; текстура и геометрия ссылаются на ванильные ресурсы, их разрешение проверять.

#### Записанные компоненты и события 2.8.8

Ниже — точные поля сохранённого разбора, не гарантия их исполнения в новой версии. В случае повторяющихся ключей и неподтверждённых условий не подставлять значения по догадке.

- Путь `Swords_B/entities/bee_entity.json`; format_version `"1.16.100"`.
- description: `{"identifier":"entity:bee_sword","is_spawnable":false,"is_summonable":true,"is_experimental":false}`.

##### Постоянные компоненты

- `minecraft:timer` (строки 16): `{"looping":true,"time":[6,8],"randomInterval":true,"time_down_event":{"event":"despawn","target":"self"}}`
- `minecraft:damage_sensor` (строки 25): `{"triggers":[{"deals_damage":false,"on_damage":{"filters":{"test":"is_family","subject":"other","value":"player"}}},{"cause":"fall","deals_damage":false}]}`
- `minecraft:scale` (строки 39): `{"value":0.5}`
- `minecraft:behavior.melee_attack` (строки 42): `{"priority":1,"speed_multiplier":1.4,"track_target":true}`
- `minecraft:type_family` (строки 47): `{"family":["bee","mob","arthropod"]}`
- `minecraft:angry` (строки 50): `{"duration":99999,"broadcastAnger":true,"broadcastRange":20,"broadcast_filters":{},"calm_event":{}}`
- `minecraft:behavior.nearest_attackable_target` (строки 57): `{"priority":1,"within_radius":16,"entity_types":[{"filters":{"test":"is_family","subject":"other","value":"monster"},"max_dist":10}],"must_see":true}`
- `minecraft:attack` (строки 72): `{"damage":1,"effect_name":"fatal_poison","effect_duration":3}`
- `minecraft:is_hidden_when_invisible` (строки 77): `{}`
- `minecraft:behavior.move_towards_home_restriction` (строки 78): `{"priority":9}`
- `minecraft:behavior.random_hover` (строки 81): `{"priority":12,"xz_dist":8,"y_dist":8,"y_offset":-1,"interval":1,"hover_height":[1,4]}`
- `minecraft:leashable` (строки 89): `{"soft_distance":4,"hard_distance":6,"max_distance":10}`
- `minecraft:behavior.float` (строки 94): `{"priority":19}`
- `minecraft:breathable` (строки 97): `{"totalSupply":15,"suffocateTime":0}`
- `minecraft:collision_box` (строки 101): `{"width":0.55,"height":0.5}`
- `minecraft:conditional_bandwidth_optimization` (строки 105): `{}`
- `minecraft:follow_range` (строки 106): `{"value":1024}`
- `minecraft:hurt_on_condition` (строки 109): `{"damage_conditions":[{"filters":{"test":"in_lava","subject":"self","operator":"==","value":true},"cause":"lava","damage_per_tick":4}]}`
- `minecraft:movement` (строки 123): `{"value":0.3}`
- `minecraft:flying_speed` (строки 126): `{"value":0.15}`
- `minecraft:navigation.hover` (строки 129): `{"can_path_over_water":true,"can_sink":false,"can_pass_doors":false,"can_path_from_air":true,"avoid_water":true,"avoid_damage_blocks":true,"avoid_sun":false}`
- `minecraft:movement.hover` (строки 138): `{}`
- `minecraft:jump.static` (строки 139): `{}`
- `minecraft:can_fly` (строки 140): `{}`
- `minecraft:health` (строки 141): `{"value":10,"max":10}`
- `minecraft:nameable` (строки 145): `{}`
- `minecraft:physics` (строки 146): `{}`
- `minecraft:pushable` (строки 147): `{"is_pushable":true,"is_pushable_by_piston":true}`

##### Группы компонентов

- `despawn` (строки 11,21,153): `{"minecraft:despawn":{}}`

##### События

**`despawn`** (строки 11,21,153):

- `$` — поля действия: `{"run_command":{"command":["tp @s ~ -103 ~"]}}`

<a id="mob-riding-spider"></a>
### Ездовой паук — `minecraft:spider`

Специальная группа вызывается [Spider Sword](#sword-spider_sword). Health 20, одно место с координатой `[0,0.54,0]`, движение управляется игроком, jump strength 0,4–0,7. Контроллер при rider назначает levitation на 10 с с amplifier 3; `not_climb` снимает эффект при четырёх проверках окружающего воздуха. Это записанная модель лазания, а не доказанное ванильное лазание. Путь `loot_tables/entities/empty.json` локально отсутствует; сохранить корректную политику добычи современным способом. Снятие меча вызывает stop_riding.

#### Записанные компоненты и события 2.8.8

Ниже — точные поля сохранённого разбора, не гарантия их исполнения в новой версии. В случае повторяющихся ключей и неподтверждённых условий не подставлять значения по догадке.

- Путь `Swords_B/entities/spider.json`; format_version `"1.13.0"`.
- description: `{"identifier":"minecraft:spider","is_spawnable":true,"is_summonable":true,"is_experimental":false,"scripts":{"animate":["despawn","climb_spider"]},"animations":{"despawn":"controller.animation.despawn","climb_spider":"controller.animation.climb_spider"}}`.

##### Постоянные компоненты

- `minecraft:experience_reward` (строки 187): `{"on_death":"query.last_hit_by_player ? 5 : 0"}`
- `minecraft:nameable` (строки 190): `{}`
- `minecraft:type_family` (строки 21,192): `{"family":["spider","monster","mob","arthropod"]}`
- `minecraft:breathable` (строки 195): `{"total_supply":15,"suffocate_time":0}`
- `minecraft:loot` (строки 26,199): `{"table":"loot_tables/entities/spider.json"}`
- `minecraft:collision_box` (строки 202): `{"width":1.4,"height":0.9}`
- `minecraft:health` (строки 27,206): `{"value":16,"max":16}`
- `minecraft:hurt_on_condition` (строки 210): `{"damage_conditions":[{"filters":{"test":"in_lava","subject":"self","operator":"==","value":true},"cause":"lava","damage_per_tick":4}]}`
- `minecraft:movement` (строки 219): `{"value":0.3}`
- `minecraft:navigation.climb` (строки 222): `{"can_path_over_water":true}`
- `minecraft:movement.basic` (строки 225): `{}`
- `minecraft:jump.static` (строки 227): `{}`
- `minecraft:can_climb` (строки 229): `{}`
- `minecraft:attack` (строки 231): `{"damage":3}`
- `minecraft:behavior.float` (строки 234): `{"priority":1}`
- `minecraft:behavior.mount_pathing` (строки 237): `{"priority":5,"speed_multiplier":1.25,"target_dist":0.0,"track_target":true}`
- `minecraft:rideable` (строки 28,50,64,78,243): `{"seat_count":1,"family_types":["zombie"],"seats":{"position":[0.0,0.54,-0.1]}}`
- `minecraft:physics` (строки 252): `{}`
- `minecraft:pushable` (строки 254): `{"is_pushable":true,"is_pushable_by_piston":true}`

##### Группы компонентов

- `despawn` (строки 10,13,18,404): `{"minecraft:despawn":{}}`
- `minecraft:spider_player_jockey` (строки 20,396): `{"minecraft:type_family":{"family":["spider","monster","mob","arthropod","spider_sword"]},"minecraft:input_ground_controlled":{},"minecraft:behavior.controlled_by_player":{"priority":0},"minecraft:can_power_jump":{},"minecraft:horse.jump_strength":{"value":{"range_min":0.4,"range_max":0.7}},"minecraft:loot":{"table":"loot_tables/entities/empty.json"},"minecraft:health":{"value":20,"max":20},"minecraft:rideable":{"seat_count":1,"family_types":["player"],"seats":{"position":[0.0,0.54,0.0]}},"minecraft:environment_sensor":{"triggers":[{"filters":{},"event":"not_climb"}]}}`
- `minecraft:spider_jockey` (строки 46,328): `{"minecraft:addrider":{"entity_type":"minecraft:skeleton"},"minecraft:rideable":{"seat_count":1,"family_types":["skeleton"],"seats":{"position":[0.0,0.54,0.0]}}}`
- `minecraft:spider_stray_jockey` (строки 60,292): `{"minecraft:addrider":{"entity_type":"minecraft:skeleton.stray"},"minecraft:rideable":{"seat_count":1,"family_types":["skeleton"],"seats":{"position":[0.0,0.54,0.0]}}}`
- `minecraft:spider_wither_jockey` (строки 74,306): `{"minecraft:addrider":{"entity_type":"minecraft:skeleton.wither"},"minecraft:rideable":{"seat_count":1,"family_types":["skeleton"],"seats":{"position":[0.0,0.54,0.0]}}}`
- `minecraft:spider_neutral` (строки 88,293,307,329,340,351,368,390): `{"minecraft:environment_sensor":{"triggers":{"filters":{"test":"is_brightness","operator":"<","value":0.49},"event":"minecraft:become_hostile"}},"minecraft:on_target_acquired":{"event":"minecraft:become_angry"}}`
- `minecraft:spider_hostile` (строки 103,356,363,389): `{"minecraft:environment_sensor":{"triggers":{"filters":{"test":"is_brightness","operator":">","value":0.49},"event":"minecraft:become_neutral"}},"minecraft:on_target_acquired":{"event":"minecraft:become_angry"},"minecraft:behavior.nearest_attackable_target":{"priority":2,"entity_types":[{"filters":{"any_of":[{"test":"is_family","subject":"other","value":"player"},{"test":"is_family","subject":"other","value":"snowgolem"},{"test":"is_family","subject":"other","value":"irongolem"}]},"max_dist":16}],"attack_interval":5,"must_see":true}}`
- `minecraft:spider_angry` (строки 147,375,382): `{"minecraft:angry":{"duration":10,"duration_delta":3,"calm_event":{"event":"minecraft:become_calm","target":"self"}},"minecraft:behavior.leap_at_target":{"priority":4,"yd":0.4,"must_be_on_ground":false},"minecraft:behavior.melee_attack":{"priority":3,"speed_multiplier":1.0,"track_target":true,"reach_multiplier":0.8}}`
- `minecraft:default_spider` (строки 168,264,391): `{"minecraft:behavior.hurt_by_target":{"priority":1},"minecraft:behavior.random_stroll":{"priority":6,"speed_multiplier":0.8},"minecraft:behavior.look_at_player":{"priority":7,"look_distance":6.0,"probability":0.02},"minecraft:behavior.random_look_around":{"priority":7}}`

##### События

**`minecraft:entity_spawned`** (строки 261):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"add":{"component_groups":["minecraft:default_spider"]}}`
  - `$.sequence[1].randomize`: альтернативы, веса `[1,99]`, сумма 100:
    - ветвь 0, weight `1`; условная доля 1/100 (1%):
      - `$.sequence[1].randomize[0].randomize`: альтернативы, веса `[80,80,20]`, сумма 180:
        - ветвь 0, weight `80`; условная доля 4/9 (44.4444%):
          - `$.sequence[1].randomize[0].randomize[0]` — поля действия: `{"filters":{"all_of":[{"test":"is_daytime","value":false},{"test":"is_snow_covered","value":true},{"test":"is_underground","value":false}]},"remove":{},"add":{"component_groups":["minecraft:spider_stray_jockey","minecraft:spider_neutral"]}}`
        - ветвь 1, weight `80`; условная доля 4/9 (44.4444%):
          - `$.sequence[1].randomize[0].randomize[1]` — поля действия: `{"filters":{"test":"is_biome","value":"the_nether"},"remove":{},"add":{"component_groups":["minecraft:spider_wither_jockey","minecraft:spider_neutral"]}}`
        - ветвь 2, weight `20`; условная доля 1/9 (11.1111%):
          - `$.sequence[1].randomize[0].randomize[2]` — поля действия: `{"filters":{"any_of":[{"test":"is_daytime","value":false},{"test":"is_underground","value":true}]},"remove":{},"add":{"component_groups":["minecraft:spider_jockey","minecraft:spider_neutral"]}}`
    - ветвь 1, weight `99`; условная доля 99/100 (99%):
      - `$.sequence[1].randomize[1]` — поля действия: `{"remove":{},"add":{"component_groups":["minecraft:spider_neutral"]}}`

**`minecraft:become_hostile`** (строки 96,348):

- `$` — поля действия: `{"remove":{"component_groups":["minecraft:spider_neutral"]},"add":{"component_groups":["minecraft:spider_hostile"]}}`

**`minecraft:become_neutral`** (строки 111,360):

- `$` — поля действия: `{"remove":{"component_groups":["minecraft:spider_hostile"]},"add":{"component_groups":["minecraft:spider_neutral"]}}`

**`minecraft:become_angry`** (строки 100,115,372):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:spider_angry"]}}`

**`minecraft:become_calm`** (строки 152,379):

- `$` — поля действия: `{"remove":{"component_groups":["minecraft:spider_angry"]}}`

**`minecraft:spider_sword`** (строки 386):

- `$` — поля действия: `{"remove":{"component_groups":["minecraft:spider_hostile","minecraft:spider_neutral","minecraft:default_spider"]},"add":{"component_groups":["minecraft:spider_player_jockey"]}}`

**`minecraft:despawn`** (строки 18,400):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"filters":{"test":"is_family","subject":"self","operator":"==","value":"spider_sword"},"add":{"component_groups":["despawn"]},"run_command":{"command":["particle minecraft:example_linearcurve ~ ~ ~","playsound random.fizz @a[r=16]"]}}`

**`not_climb`** (строки 41,409):

- `$` — поля действия: `{"run_command":{"command":["execute @s ~~~ detect ~0.8 ~ ~ air 0 execute @s ~~~ detect ~-0.8 ~ ~ air 0 execute @s ~~~ detect ~ ~ ~0.8 air 0 execute @s ~~~ detect ~ ~ ~-0.8 air 0 effect @s levitation 0 0 true"]}}`

<a id="mob-shulker-shield"></a>
### Щит шалкера — `entity:shulker_shield`

Создаётся при приседании с [Shulker Sword](#sword-shulker_sword). Health 20, одно место; у защищаемого игрока записаны scale 0,7 и запрет урона cause all. Если щит уничтожен, пока владелец внутри, погибает именно владелец. У щита должна быть явная привязка к владельцу; при выходе владельца восстановить его состояние, не затрагивая чужие щиты. В старом коде команда выбирает ближайшего подходящего игрока r=1, а не обязательно владельца; координаты текстуры модели 64×64 не являются физическим размером.


**Клиентские ресурсы 2.8.8:** `Swords_R/entity/shulker_shield.v1.0.json`, `textures/entity/shulker_shield.png`, `models/entity/shulker_shield.geo.json`, `animations/shulker_shield.animation.json`, `animation_controllers/shulker_shield.animation_controllers.json`.

#### Записанные компоненты и события 2.8.8

Ниже — точные поля сохранённого разбора, не гарантия их исполнения в новой версии. В случае повторяющихся ключей и неподтверждённых условий не подставлять значения по догадке.

- Путь `Swords_B/entities/shulker_shield.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:shulker_shield","runtime_identifier":"minecraft:shulker","is_spawnable":false,"is_summonable":true,"is_experimental":false,"scripts":{"animate":["despawn"]},"animations":{"despawn":"controller.animation.despawn"}}`.

##### Постоянные компоненты

- `minecraft:type_family` (строки 22): `{"family":["effect99_entities","player","shulker_sword"]}`
- `minecraft:collision_box` (строки 23): `{"width":0.6,"height":0.9}`
- `minecraft:health` (строки 24): `{"value":20}`
- `minecraft:rideable` (строки 25): `{"crouching_skip_interact":true,"seat_count":1,"family_types":["player"],"seats":{"position":[0.0,0,0.0]}}`
- `minecraft:physics` (строки 26): `{}`
- `minecraft:on_death` (строки 27): `{"event":"damage_player","target":"self"}`
- `minecraft:environment_sensor` (строки 28): `[{"on_environment":{"filters":{"all_of":[{"test":"is_family","subject":"self","value":"effect99_entities"}]},"event":"shulker_shield_clear_effect"}}]`

##### Группы компонентов

- `minecraft:shulker_shield` (строки 18,44): `{}`
- `despawn` (строки 11,14,19,47): `{"minecraft:despawn":{}}`

##### События

**`shulker_shield_clear_effect`** (строки 35,41):

- `$` — поля действия: `{"run_command":{"command":["effect @s levitation 0 0"]}}`

**`shulker_shield`** (строки 42):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:shulker_shield"]}}`

**`minecraft:despawn`** (строки 19,47):

- `$` — поля действия: `{"add":{"component_groups":["despawn"]},"run_command":{"command":["event entity @p[family=shulker_sword,r=6] stop_shulker_sword_event"]}}`

**`damage_player`** (строки 27,49):

- `$` — поля действия: `{"run_command":{"command":["effect @p[r=1,family=shulker_sword] instant_damage 1 2 true"]}}`

<a id="mob-grass-helper"></a>
### Травяной помощник — `entity:grass`

Вызывается [Grass Sword](#sword-grass_sword) и [Grass Witch](#mob-grass-witch). Family `[effect99_entities]`, collision 0×0, запрет всех damage, без гравитации/коллизии и толкания. При создании звук dig.grass, slowness на 2 с amplifier 15 для `type=!entity:grass,r=1`; затем tag grass назначается по отдельному selector, где игрок и item явно не исключены. Таймер `[1,08;1,08]` выбирает `c=1,r=1,tag=grass`, проверяет grass снизу и air/tallgrass в позиции цели, после чего пытается опустить выбранную сущность на 1 блок. Две команды выбирают цель отдельно. Затем снимается общий tag в r=2 и добавляется группа с timer `[0,52;0,52]`; порядок действий в одном event не доказан. При despawn ветви 50/50: поставить tallgrass вместо air или пусто. Тег не привязан к создателю: несколько помощников могут пересекаться.


**Клиентские ресурсы 2.8.8:** `Swords_R/entity/grass.v1.0.json`, `textures/entity/grass.png`, `models/entity/grass.geo.json`, `animations/grass.animation.json`, `animation_controllers/grass.animation_controllers.json`.

#### Записанные компоненты и события 2.8.8

Ниже — точные поля сохранённого разбора, не гарантия их исполнения в новой версии. В случае повторяющихся ключей и неподтверждённых условий не подставлять значения по догадке.

- Путь `Swords_B/entities/grass.json`; format_version `"1.11.0"`.
- description: `{"identifier":"entity:grass","is_spawnable":false,"is_summonable":true,"is_experimental":false}`.

##### Постоянные компоненты

- `minecraft:type_family` (строки 25): `{"family":["effect99_entities"]}`
- `minecraft:collision_box` (строки 26): `{"width":0.0,"height":0.0}`
- `minecraft:damage_sensor` (строки 27): `{"triggers":{"cause":"all","deals_damage":false}}`
- `minecraft:physics` (строки 28): `{"has_gravity":false,"has_collision":false}`
- `minecraft:pushable` (строки 29): `{"is_pushable":false,"is_pushable_by_piston":false}`

##### Группы компонентов

- `despawn` (строки 11,15,54,56): `{"minecraft:despawn":{}}`
- `start_despawn` (строки 13,52): `{"minecraft:timer":{"time":[0.52,0.52],"looping":false,"time_down_event":{"event":"despawn","target":"self"}}}`
- `grass_sword` (строки 18,34): `{"minecraft:timer":{"time":[1.08,1.08],"looping":false,"time_down_event":{"event":"grass_sword_skill","target":"self"}}}`

##### События

**`minecraft:entity_spawned`** (строки 32):

- `$.sequence`: 1 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"add":{"component_groups":["grass_sword"]},"run_command":{"command":["playsound dig.grass @a[r=12]","effect @e[type=!entity:grass,r=1] slowness 2 15 true","execute @e[family=!grass_witch,type=!entity:grass,type=!xp_orb,type=!arrow,r=1,tag=!grass] ~ ~ ~ tag @s add grass"]}}`

**`grass_sword_skill`** (строки 20,44):

- `$` — поля действия: `{"run_command":{"command":["playsound dig.grass @a[r=12] ~ ~ ~ 1 0.4","execute @e[type=!entity:grass,c=1,r=1,tag=grass] ~ ~ ~ detect ~ ~-1 ~ grass 0 execute @s ~ ~ ~ detect ~ ~ ~ air 0 tp @s ~ ~-1 ~","execute @e[type=!entity:grass,c=1,r=1,tag=grass] ~ ~ ~ detect ~ ~-1 ~ grass 0 execute @s ~ ~ ~ detect ~ ~ ~ tallgrass 0 tp @s ~ ~-1 ~","tag @e[tag=grass,r=2] remove grass"]},"add":{"component_groups":["start_despawn"]}}`

**`despawn`** (строки 11,15,54,56):

- `$.sequence`: 2 шаг(ов), порядок как в исходнике:
  - `$.sequence[0]` — поля действия: `{"add":{"component_groups":["despawn"]}}`
  - `$.sequence[1].randomize`: альтернативы, веса `[50,50]`, сумма 100:
    - ветвь 0, weight `50`; условная доля 1/2 (50%):
      - `$.sequence[1].randomize[0]` — поля действия: `{"run_command":{"command":["fill ~ ~ ~ ~ ~ ~ tallgrass 0 replace air"]}}`
    - ветвь 1, weight `50`; условная доля 1/2 (50%):
      - пустое действие

<a id="mob-ghost"></a>
### Призрак — `entity:ghost`

Источник [Ghost Sword](#sword-ghost_sword). Health 666, collision 0,6×1,8, scale 1,05, movement 0,3, knockback resistance 1, fire_immune true, family `[ghost,mob,monster]`. Damage sensor отменяет урон и при попадании other family player вызывает disturbed_ghost: 987/1000 пусто, 10/1000 teleport до 16, 3/1000 загрузка Ghost Sword и despawn. При brightness >0,1 указан despawn. Правило underground: блок stone, brightness 0–7 с adjust_for_weather, сложность easy–hard, biome tag monster, weight 100, herd 1–2, событие ghost_wailing. Правило surface: блок grass, те же brightness/difficulty/biome, weight 50 и surface density limit 3; событие плача в этой ветви явно не задано. Веса не являются шансами появления. В описании сказано, что призраки появляются ночью; отдельная проверка времени в этих двух исходных spawn rules не записана. По решению пользователя не добавлять отдельный запрет дня ни для одной ветви: применять указанные условия освещённости. Не считать отсутствие проверки времени доказательством частоты или условий появления в старой игре. При вызове `ghost_wailing` два равных вложенных варианта в ветке 30/100 дают по 15/100 на вызов; адресаты r=10–50, файл `ghost_sword.wailing` длится 27,214 с. Эта ветка явно назначена underground-правилу, не каждому призраку.


**Клиентские ресурсы 2.8.8:** `Swords_R/entity/ghost.v1.0.json`, `textures/entity/ghost.png`, `models/entity/ghost.geo.json`, `animations/ghost.animation.json`, `animation_controllers/ghost.animation_controllers.json`, `sounds/ghost_sword/wailing.ogg`.

#### Записанные компоненты и события 2.8.8

Ниже — точные поля сохранённого разбора, не гарантия их исполнения в новой версии. В случае повторяющихся ключей и неподтверждённых условий не подставлять значения по догадке.

- Путь `Swords_B/entities/ghost.json`; format_version `"1.13.0"`.
- description: `{"identifier":"entity:ghost","runtime_identifier":"minecraft:chicken","is_spawnable":true,"is_summonable":true,"is_experimental":false}`.

##### Постоянные компоненты

- `minecraft:damage_sensor` (строки 17): `{"triggers":[{"on_damage":{"filters":{"test":"is_family","subject":"other","value":"player"},"event":"disturbed_ghost"},"deals_damage":false},{"cause":"all","deals_damage":false}]}`
- `minecraft:behavior.look_at_entity` (строки 31): `{"priority":3,"look_distance":6.0,"probability":1.0,"angle_of_view_vertical":135,"angle_of_view_horizontal":170,"filters":{"any_of":[{"test":"is_family","subject":"other","value":"mob"},{"test":"is_family","subject":"other","value":"ghost_sword"}]}}`
- `minecraft:type_family` (строки 44): `{"family":["ghost","mob","monster"]}`
- `minecraft:collision_box` (строки 47): `{"width":0.6,"height":1.8}`
- `minecraft:health` (строки 51): `{"value":666,"max":666}`
- `minecraft:scale` (строки 55): `{"value":1.05}`
- `minecraft:movement` (строки 58): `{"value":0.3}`
- `minecraft:navigation.walk` (строки 61): `{"can_path_over_water":true,"avoid_damage_blocks":true}`
- `minecraft:movement.basic` (строки 65): `{}`
- `minecraft:jump.static` (строки 67): `{}`
- `minecraft:can_climb` (строки 69): `{}`
- `minecraft:behavior.float` (строки 71): `{"priority":0}`
- `minecraft:behavior.flee_sun` (строки 74): `{"priority":2,"speed_multiplier":1}`
- `minecraft:behavior.random_stroll` (строки 78): `{"priority":1,"speed_multiplier":1.0,"xz_dist":30}`
- `minecraft:knockback_resistance` (строки 83): `{"value":1.0}`
- `minecraft:fire_immune` (строки 86): `true`
- `minecraft:physics` (строки 87): `{}`
- `minecraft:pushable` (строки 89): `{"is_pushable":false,"is_pushable_by_piston":false}`
- `minecraft:environment_sensor` (строки 93): `{"triggers":[{"filters":{"test":"is_brightness","operator":">","value":0.1},"event":"despawn"},{"filters":{},"event":"ghost_effects"}]}`

##### Группы компонентов

- `despawn` (строки 12,97,120,165,166): `{"minecraft:despawn":{}}`

##### События

**`minecraft:entity_spawned`** (строки 107):


**`disturbed_ghost`** (строки 21,109):

- `$.randomize`: альтернативы, веса `[987,10,3]`, сумма 1000:
  - ветвь 0, weight `987`; условная доля 987/1000 (98.7%):
    - пустое действие
  - ветвь 1, weight `10`; условная доля 1/100 (1%):
    - `$.randomize[1]` — поля действия: `{"run_command":{"command":["playsound mob.endermen.portal @a[r=17] ~~~","spreadplayers ~ ~ 0 16 @s"]}}`
  - ветвь 2, weight `3`; условная доля 3/1000 (0.3%):
    - `$.randomize[2]` — поля действия: `{"add":{"component_groups":["despawn"]},"run_command":{"command":["structure load ghost_sword ~~~","particle minecraft:ghost_spiral ~~~","playsound mob.wither.ambient @a[r=16] ~ ~1 ~ 2 0.3","particle minecraft:egg_destroy_emitter ~ ~ ~","particle minecraft:egg_destroy_emitter ~ ~0.3 ~","particle minecraft:egg_destroy_emitter ~ ~0.6 ~","particle minecraft:egg_destroy_emitter ~ ~0.9 ~","particle minecraft:egg_destroy_emitter ~ ~1.2 ~","particle minecraft:egg_destroy_emitter ~ ~1.5 ~"]}}`

**`ghost_wailing`** (строки 136):

- `$.randomize`: альтернативы, веса `[70,30]`, сумма 100:
  - ветвь 0, weight `70`; условная доля 7/10 (70%):
    - пустое действие
  - ветвь 1, weight `30`; условная доля 3/10 (30%):
    - `$.randomize[1].randomize`: альтернативы, веса `[50,50]`, сумма 100:
      - ветвь 0, weight `50`; условная доля 1/2 (50%):
        - `$.randomize[1].randomize[0]` — поля действия: `{"run_command":{"command":["playsound ghost_sword.wailing @a[rm=10,r=50]"]}}`
      - ветвь 1, weight `50`; условная доля 1/2 (50%):
        - `$.randomize[1].randomize[1]` — поля действия: `{"run_command":{"command":["playsound ghost_sword.wailing @a[rm=10,r=50] ~~~ 1 7"]}}`

**`ghost_effects`** (строки 101,154):

- `$.randomize`: альтернативы, веса `[90,10]`, сумма 100:
  - ветвь 0, weight `90`; условная доля 9/10 (90%):
    - пустое действие
  - ветвь 1, weight `10`; условная доля 1/10 (10%):
    - `$.randomize[1]` — поля действия: `{"run_command":{"command":["playsound mob.wither.spawn @a[r=16] ~ ~ ~ 0.15 0.2"]}}`

**`despawn`** (строки 12,97,120,165,166):

- `$` — поля действия: `{"add":{"component_groups":["despawn"]},"run_command":{"command":["particle minecraft:ghost_spiral ~~~","playsound mob.wither.ambient @a[r=16] ~ ~1 ~ 2 0.3","particle minecraft:egg_destroy_emitter ~ ~ ~","particle minecraft:egg_destroy_emitter ~ ~0.3 ~","particle minecraft:egg_destroy_emitter ~ ~0.6 ~","particle minecraft:egg_destroy_emitter ~ ~0.9 ~","particle minecraft:egg_destroy_emitter ~ ~1.2 ~","particle minecraft:egg_destroy_emitter ~ ~1.5 ~"]}}`

<a id="mob-red-enderman"></a>
### Красноглазый Enderman — `minecraft:enderman`

Источник [Ender Sword](#sword-ender_sword): красная форма имеет health 120, attack 12, scale 1,2, follow_range 64, random teleport cube 32×32×32, target_distance 32, target/light teleport chance 0,04; при появлении в Overworld записан выбор красной формы весом 20/100; группа `red_enderman` прямо ссылается на `loot_tables/entities/red_enderman.json`: таблица требует убийства игроком и содержит шанс меча 2,5% плюс 2 процентных пункта за уровень Looting. В ремейке явно закрепить эту таблицу за красной формой. Само наличие ссылки в коде не доказывает успешное исполнение в старой игре; не распространять шанс на любого эндермена.




**Клиентские ресурсы 2.8.8:** `Swords_R/entity/enderman.entity.json` задаёт geometry.enderman.v1.8, controller.render.enderman и `textures/entity/enderman/red_enderman`; использовать сохранённый ресурс, а ванильные зависимости проверить.

#### Записанные компоненты и события 2.8.8

Ниже — точные поля сохранённого разбора, не гарантия их исполнения в новой версии. В случае повторяющихся ключей и неподтверждённых условий не подставлять значения по догадке.

- Путь `Swords_B/entities/enderman.json`; format_version `"1.13.0"`.
- description: `{"identifier":"minecraft:enderman","is_spawnable":true,"is_summonable":true,"is_experimental":false}`.

##### Постоянные компоненты

- `minecraft:experience_reward` (строки 80): `{"on_death":"query.last_hit_by_player ? 5 : 0"}`
- `minecraft:type_family` (строки 83): `{"family":["enderman","monster","mob"]}`
- `minecraft:breathable` (строки 86): `{"total_supply":15,"suffocate_time":0}`
- `minecraft:nameable` (строки 90): `{}`
- `minecraft:loot` (строки 70,92): `{"table":"loot_tables/entities/enderman.json"}`
- `minecraft:health` (строки 66,95): `{"value":40,"max":40}`
- `minecraft:hurt_on_condition` (строки 99): `{"damage_conditions":[{"filters":{"test":"in_lava","subject":"self","operator":"==","value":true},"cause":"lava","damage_per_tick":4},{"filters":{"test":"in_water_or_rain","operator":"==","value":true},"cause":"drowning","damage_per_tick":1}]}`
- `minecraft:attack` (строки 63,113): `{"damage":7}`
- `minecraft:follow_range` (строки 59,116): `{"value":32,"max":32}`
- `minecraft:collision_box` (строки 120): `{"width":0.6,"height":2.9}`
- `minecraft:teleport` (строки 51,124): `{"random_teleports":true,"max_random_teleport_time":30,"random_teleport_cube":[32,32,32],"target_distance":16,"target_teleport_chance":0.05,"light_teleport_chance":0.05}`
- `minecraft:lookat` (строки 73,132): `{"search_radius":64.0,"set_target":true,"look_cooldown":5.0,"filters":{"all_of":[{"subject":"other","test":"is_family","value":"player"},{"test":"has_equipment","domain":"head","subject":"other","operator":"not","value":"carved_pumpkin"}]}}`
- `minecraft:behavior.nearest_attackable_target` (строки 153): `{"priority":5,"attack_interval":10,"entity_types":[{"filters":{"test":"is_family","subject":"other","value":"endermite"},"max_dist":64}],"must_see":true}`
- `minecraft:navigation.walk` (строки 168): `{"can_path_over_water":false,"avoid_water":true}`
- `minecraft:movement.basic` (строки 172): `{}`
- `minecraft:jump.static` (строки 175): `{}`
- `minecraft:can_climb` (строки 177): `{}`
- `minecraft:behavior.float` (строки 179): `{"priority":0}`
- `minecraft:behavior.random_stroll` (строки 182): `{"priority":7,"speed_multiplier":1.0}`
- `minecraft:behavior.look_at_player` (строки 186): `{"priority":8,"look_distance":8.0,"probability":8.0}`
- `minecraft:behavior.random_look_around` (строки 191): `{"priority":8}`
- `minecraft:behavior.hurt_by_target` (строки 194): `{"priority":3}`
- `minecraft:behavior.enderman_leave_block` (строки 197): `{"priority":10}`
- `minecraft:behavior.enderman_take_block` (строки 200): `{"priority":11}`
- `minecraft:physics` (строки 203): `{}`
- `minecraft:pushable` (строки 205): `{"is_pushable":true,"is_pushable_by_piston":true}`

##### Группы компонентов

- `minecraft:default_enderman` (строки 11,215,249): `{"minecraft:variant":{"value":0}}`
- `minecraft:red_enderman` (строки 16,220,252): `{"minecraft:variant":{"value":1}}`
- `minecraft:enderman_calm` (строки 21,215,220,227,244,249,252): `{"minecraft:on_target_acquired":{"event":"minecraft:become_angry","target":"self"},"minecraft:movement":{"value":0.3}}`
- `minecraft:enderman_angry` (строки 30,232,239): `{"minecraft:angry":{"duration":25,"calm_event":{"event":"minecraft:on_calm","target":"self"}},"minecraft:movement":{"value":0.45},"minecraft:behavior.melee_attack":{"priority":2,"speed_multiplier":1.0,"track_target":false}}`
- `red_enderman` (строки 47,220,251,252): `{"minecraft:scale":{"value":1.2},"minecraft:teleport":{"random_teleports":true,"max_random_teleport_time":20,"random_teleport_cube":[32,32,32],"target_distance":32,"target_teleport_chance":0.04,"light_teleport_chance":0.04},"minecraft:follow_range":{"value":64,"max":64},"minecraft:attack":{"damage":12},"minecraft:health":{"value":120,"max":120},"minecraft:loot":{"table":"loot_tables/entities/red_enderman.json"},"minecraft:lookat":{"search_radius":64.0,"set_target":true,"look_cooldown":5.0,"filters":{"all_of":[{"subject":"other","test":"is_family","value":"player"}]}}}`

##### События

**`minecraft:entity_spawned`** (строки 211):

- `$.randomize`: альтернативы, веса `[80,20]`, сумма 100:
  - ветвь 0, weight `80`; условная доля 4/5 (80%):
    - `$.randomize[0]` — поля действия: `{"add":{"component_groups":["minecraft:default_enderman","minecraft:enderman_calm"]}}`
  - ветвь 1, weight `20`; условная доля 1/5 (20%):
    - `$.randomize[1]` — поля действия: `{"filters":{"test":"has_biome_tag","operator":"==","value":"overworld"},"add":{"component_groups":["minecraft:red_enderman","red_enderman","minecraft:enderman_calm"]}}`

**`minecraft:become_angry`** (строки 23,224):

- `$` — поля действия: `{"remove":{"component_groups":["minecraft:enderman_calm"]},"add":{"component_groups":["minecraft:enderman_angry"]}}`

**`minecraft:on_calm`** (строки 34,236):

- `$` — поля действия: `{"remove":{"component_groups":["minecraft:enderman_angry"]},"add":{"component_groups":["minecraft:enderman_calm"]}}`

**`default_enderman`** (строки 248):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:default_enderman","minecraft:enderman_calm"]}}`

**`red_enderman`** (строки 47,220,251,252):

- `$` — поля действия: `{"add":{"component_groups":["minecraft:red_enderman","red_enderman","minecraft:enderman_calm"]}}`

<a id="mob-creeper"></a>
### Заряженный и мини-крипер — `minecraft:creeper`

Исходный файл 2.8.8 содержит лишнюю закрывающую скобку и не разбирается как JSON5. Ниже — диагностическое чтение после её удаления **только в памяти**; загрузка файла игрой и единственность исправления не доказаны.

Источник и помощник [Creeper Sword](#sword-creeper_sword): при зажигании заряженного крипера записан таймер 1,4 с на выбор меча 5/100 и fuse взрыва 1,5 с. Порядок срабатывания движком не доказан. От weapon-события мини-крипер выбирается с весом 20/100: scale 0,3, обнаружение до 16, порог приближения 2,5, timer 10 с и взрыв power 1 с fuse 1,5 с. Контекст `other` при призыве проверить.



#### Записанные компоненты и события 2.8.8

Ниже — точные поля сохранённого разбора, не гарантия их исполнения в новой версии. В случае повторяющихся ключей и неподтверждённых условий не подставлять значения по догадке.

**Не разобран JSON5:** `<string>:430 Unexpected "}" at column 3`. Исходник не изменять и изучать вручную.

**Диагностические группы крипера:** mini имеет family `[creeper,player,mob,effect99_entities]`, цель family monster, max_dist 16, must_see true. `minecraft:entity_spawned` проверяет `other` с Creeper Sword в hand и добавляет mini и projectile; кто является other при выстреле, не установлен. Projectile power 1, gravity 0,02, impact 1 и knockback; on-hit снимает projectile-группу, не обязательно удаляет сущность. Взрыв mini fire=false, griefing=true, при активации запрещает damage cause all. Базовый крипер health 20, collision 0,6×1,8, movement 0,2, attack 3; при заряде обычный взрыв power 6, без заряда power 3; оба fuse 1,5. При forced charged timer 1,4 запускает 95/5 на структуру меча.
