# Silver → Alpha Wolf → Wolf Sword: цепочка 2.x

Статическое сравнение 2.8.8/2.8.14. Точные item ID `effect:silver_ingot`, `effect:silver_sword`, `effect:wolf_sword` отсутствуют среди определений 1.6; не предполагается, что другие ресурсы не могут давать подобное поведение. Их item JSON, рудный блок/loot, определения Alpha Wolf и рецепты в двух 2.x архивах совпадают; файлы природной генерации silver различаются. Условные веса и последовательность деклараций не гарантируют добычу или работу Bedrock. [Предметы](quick-reference.md) · [правила руды](manual-ore-and-loot-paths-2.8.md) · [условия Wolf](manual-wolf-conditions-2.8.md) · [конфликты family](manual-family-cross-effects-2.8.md).

## Руда, слиток и меч

`effect99:silver_ore` задаёт destroy_time 8, explosion_resistance 1, light absorption 15. Базовый `minecraft:loot` указывает `loot_tables/blocks/null.json`, отсутствующий в обоих архивах; внешний/ванильный файл не исключён. Отдельный event разрушения игроком проверяет имена iron_pickaxe/diamond_pickaxe/netherite_pickaxe/bedrock_sword выражением `q.get_equipped_item_name` без скобок, затем `spawn_loot` на `loot_tables/blocks/silver_ore.json`: один roll, одна запись **самого блока** `effect99:silver_ore`, count 1. Это не прямая выдача слитка, и срабатывание on_player_destroyed с этим Molang и данным инструментом не доказано.

В 2.8.8 есть feature/feature_rule silver: overworld, underground_pass, 5 iterations, y gaussian extent `[10,35]`, scatter 160/200 и allowlist stone; есть структура 1×1×1. В 2.8.14 этих двух feature-файлов нет, но определение блока, loot и файл silver-структуры остаются. Возможное внешнее разрешение структуры и фактическая генерация неизвестны; 160/200 не есть шанс руды в каждом блоке/чанке. [Полная таблица](manual-version-2.8.8.md#silver-ore-и-quartz-diamond-ore).

`recipes/silver_ingot.json` объявляет furnace/blast_furnace input `effect99:silver_ore` → output `effect:silver_ingot`; слиток stack 64, hand_equipped false, durability и weapon не объявлены. `recipes/silver_sword.json`: crafting_table `2/2/1`, 2 = `effect:silver_ingot`, 1 = `minecraft:stick`, result `effect:silver_sword`. При штатной регистрации и выдаче одного слитка на плавку для этой цепочки необходимо **два** блока руды и одна палка на меч; альтернативные внешние источники и эффект чар не исключены.

`effect:silver_sword`: damage 6, durability/self repair 1800, enchantable 9/sword, offhand false, web/bamboo 15/10, только weapon `on_hurt_entity` → direct durability damage 1. Дополнительного множителя урона по волкам в item нет; описание «больше урона» не эквивалентно доказанному коэффициенту.

## Alpha Wolf и получение Wolf Sword

`entity:alpha_wolf`: health 480, attack 8, movement 0.4, scale 1.8, knockback resistance 0.5, family `[wolf,mob,monster,alpha_wolf]`. Spawn rule: поверхность на `minecraft:grass`, brightness min 0/max 7 с adjust_for_weather true, difficulty easy…hard, weight 10, herd 1, biome tag taiga и не mega. Вес 10 — не процент спавна, указанные brightness-поля не задают явный тест «ночь».

Damage sensor имеет три **отдельных** trigger, у всех `deals_damage:true`:

1. `other` family player и silver sword в hand и `has_damage:fatal` → event `minecraft:wolf_sword`.
2. `other` family player и silver sword **не** в hand → `add_effects`: добавить health_bar, `effect @s resistance 20 2 true` и regeneration 20 2 true.
3. `other` family player и silver sword в hand → `clear_effects`: health_bar и `effect @s resistance 0`, `effect @s regeneration 0`.

Первый и третий фильтры могут совпасть при фатальном ударе. Event `minecraft:wolf_sword` выбирает 90 пусто/10 `structure load wolf_sword`; 10/100 — только условно на вызов выбора, а успешное прохождение фильтра, порядок trigger, загрузка структуры и подбор — отдельные условия. `wolf_sword.mcstructure` содержит item нужного ID. Возможность снять/не получить защиту в событиях волка не доказывает прямого бонуса урона предмета; не предполагать порядок действия обоих trigger.

## Wolf Sword и конкурирующие контроллеры

`effect:wolf_sword`: damage 5, max durability/self repair 2800, offhand false, enchantable не объявлен, web/bamboo 15/10, только on_hurt_entity → direct durability 1. Player hand-sensor и три animation controller — разные входы. Контроллеры проверяют **main_hand** и moon_phase/time_of_day: подготовка 0.77…0.78, превращение при `≤0.20 || ≥0.80`, а остановка буквально `W || !W && moon_phase == 0 && time_of_day == 0.20`. При обычном приоритете && выше || наличие меча W делает выражение остановки истинным независимо от времени; это логическое чтение, не доказанная семантика Molang или одновременное выполнение событий.

Полная группа превращения объявляет family `[wolf,wolf_sword,complete_wolf_transformation,monster]`, **без** `player`, и `minecraft:attack.damage:15`; нельзя суммировать 15 с item damage 5 без правил движка. Другая группа movement value 0.18. В stop при снятии меча отдельная ветвь complete задаёт nausea и blindness 9999 с amplifier 0; обычный stop_transformation делает иные действия и включает `stopsound @a`. При конфликте family, датчиков и нескольких контроллеров конечное состояние и тайминг неизвестны. [Граничные значения и пересечения](manual-wolf-conditions-2.8.md) разобраны без запуска игры.

## Границы

Все ресурсы, структуры и семантические связи указаны по локальным архивам; внешние пакеты, загрузка генерации, столкновения, проигрывание событий и многопользовательский порядок не проверялись. Отсутствующее поле не объявляется значением по умолчанию.
