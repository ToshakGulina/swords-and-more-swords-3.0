# 2.x: выброшенные предметы — огонь, вода, таймеры и NBT

Статическое чтение `entities/item.json`, `animation_controllers/item_events.json`, функции тегирования и NBT структур. Указанные файлы item/controller/function, структуры воспроизведения и определения `entity:instant_giant_explode`/`entity:ultra_instinct_explode` побайтово совпадают в 2.8.8 и 2.8.14. Факт запуска события, интерпретация старых команд и сохранение данных при загрузке структуры должны проверяться в игре. [Подробный NBT](structures-2.8.14.md) · [поля 15 item-структур](manual-acquisition-issues.md#сохранённые-предметы-структур-2x) · [фонтан желаний](manual-fountain-2.8.md).

## Источник тегов и изменение контекста

`player.json` в `minecraft:constant_events` вызывает `.../tag_swords.mcfunction`. Она назначает десять тегов мечам по **тексту имени item-сущности**, плюс три `wish_*`; не проверяет ID исходного Item. Совпадение имени, локализация, форматирование, переименование, работа событий при отсутствии активного игрока и одновременные теги требуют испытаний. В отличие от функции, сама NBT структура `fire_sword.mcstructure` уже содержит теги `fire_sword`, `fire_sword_respawn`; структуры `lightning_sword` и `wither_sword` содержат одноимённые теги, а `bedrock_sword`, `obsidian_sword`, `glass_sword`, `wet_sponge_sword` — без таких тегов. Это NBT источника, не гарантия сохранения их после загрузки.

Проверка `has_tag fire_immune` в `item.json` вызывает `delete_fire_blocks`: `fill ~2 ~2 ~2 ~-2 ~-2 ~-2 air 0 replace fire`, рамка **5³ = 125** координат. В просмотренных JSON, mcfunction и JS обоих архивов найдено это условие, но не найдено буквальной команды назначения именно тега `fire_immune`; в `.mcstructure` буквальная строка также не найдена. Это ограниченный текстовый/байтовый поиск, не исключающий внешние источники и динамику; не подменять совпадающим по имени компонентом `minecraft:fire_immune` и не обещать, что обычный меч этот tag получает.

## Контроллер горения: все девять запросов, по порядку

`minecraft:item` подключает `controller.animation.item_events`. `default → on_fire_swords` при `q.is_on_fire`; при входе в `on_fire_swords` отправляются **девять** команд `/event entity @s[...] ...` в порядке ниже; переход в `default` записан `1.0`. Частота проверок, поведение нескольких одновременно подходящих тегов и действительное исполнение последующих команд после возможного `kill @s` не установлены.

| № | Селектор-тег (другие условия опущены только в заголовке) | Event | Что записано в event |
|---:|---|---|---|
| 1 | `fire_sword`, **без** `fire_sword_respawn` | `fire_sword_event_3` | Внутренне снова проверяет `fire_sword`; 9 flame particles, 5 × `summon entity:living_flame ~~~ hostile_entity`, звук, `kill @s`. |
| 2 | `tnt_sword` | `despawn_event_5` | `summon entity:instant_giant_explode`, `kill @s`. У сущности fuse 0.02, power 16, fire true; timer `[0,0]` на sound/camerashake. |
| 3 | `ice_sword` | `despawn_event_4` | См. две biome-ветки ниже; обе содержат звук, частицы и `kill @s`. |
| 4 | `ender_sword` | `despawn_event_1` | Частицы, `mob.endermen.death`, `kill @s`. |
| 5 | `wither_sword` | `despawn_event_2` | Частицы, `mob.wither.death`, `kill @s`. |
| 6 | `lightning_sword` | `despawn_event_3` | Частицы, `summon lightning_bolt ~~~ default_lightning_bolt`; **нет** `kill @s` в событии. |
| 7 | `nether_star_sword` | `despawn_event_6` | `summon entity:ultra_instinct_explode`, `kill @s`; у сущности fuse 0, power 8, fire false, `max_resistance:4.0`. |
| 8 | `bedrock_sword` | `respawn_event_1` | `structure load bedrock_sword ~ ~1 ~`, `kill @s`. |
| 9 | `fire_sword_respawn` | `respawn_event_2` | `structure load fire_sword ~ ~1 ~`, `kill @s`; этот селектор сам по себе не требует tag `fire_sword`. |

При обычной семантике отрицательного тега пункты 1 и 9 не одновременно подходят только из-за `fire_sword`/`fire_sword_respawn`; другие теги не исключены. `despawn_event_3` без kill и переход контроллера обратно в default допускают повторное срабатывание при продолжающемся огне, но частота/срок жизни сущности не доказаны. Сохранённый `fire_sword_respawn` может вновь запустить загрузку структуры при огне; это не доказательство бесконечного цикла.

Ice `despawn_event_4` записан как `sequence` двух веток: `has_biome_tag != nether` и `has_biome_tag nether`. Первая перед звуком/частицами/kill выполняет три **одноточечных** `fill ~~~ ~~~ flowing_water 0 replace air/fire/lava`; вторая не содержит fill. Это проверки biome tag, не гарантированное определение измерения; слитные `~~~`, соответствие блоков и одновременность/порядок фильтров нужно проверить. Каскад с другими предметами и водой не предполагается только по исходнику.

## Дождь и вода: Fire и Sponge

| Тег и условие sensor | Действие в исходнике |
|---|---|
| `fire_sword`, `in_water !=` и `in_water_or_rain` | `fading_fire_sword`: при family != fire_sword добавить группу fire_sword c non-looping random timer `[5,6]` → `fire_sword_event_1`; отдельный sequence-шаг воспроизводит fizz/частицы. Event таймера: загрузить `obsidian_sword` в `~ ~ ~`, fizz, `kill @s`. |
| `fire_sword`, `in_water` | `fire_sword_event_2`: fizz/частицы, загрузить `glass_sword` в `~ ~ ~`, `kill @s`. |
| family `fire_sword`, `in_water_or_rain !=` | `stop_fire_sword` удаляет группу fire_sword. |
| `sponge_sword`, `in_water_or_rain` | `sponge_sword_event`: при family != sponge_sword добавить группу с non-looping random timer `[0,1]` → `wet_sponge_sword`; отдельный шаг выполняет water→sponge, fizz/частица, sponge→air и seagrass→air в кубе ±2. Таймер event загружает `wet_sponge_sword ~ ~ ~`, затем `kill @s`. |
| family `sponge_sword`, `in_water_or_rain !=` | `stop_sponge_sword` удаляет группу sponge_sword. |

Каждый соответствующий sequence-шаг команд не находится внутри условия на добавление группы: нельзя заявлять, что звук и fill исполняются ровно один раз только из-за одноразового таймера. При уходе из дождя/воды отмена начатого таймера, приоритет столкновений с горением и поведение `in_water !=` без явного value требуют испытаний. `sponge→air` удаляет и уже находившуюся в кубе губку, не различая её происхождение.

Структурные замены не копируют в тексте `Item.tag` исходной сущности: они загружают заранее записанный item, затем вызывают `kill @s`. Все пять нужных структур (`fire`, `bedrock`, `glass`, `obsidian` и wet sponge) содержат по одному `Item.Count=1`. В `obsidian_sword` дополнительно `Item.Damage=0` и `Item.tag.Damage=1000`; у `fire_sword` вложенный Damage 0. Это исходные NBT-данные, не доказательство фактической прочности, стирания чар, сохранения имени или единственности результата без испытания загрузчика.
