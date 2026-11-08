# Sea Sword: цепь 1.6 и группы воды 2.x

Статическая реконструкция архивов; названия версий здесь соответствуют именам файлов. Срабатывание сенсоров, приоритет component groups, таймеры, команды, дыхание и реальный лут Bedrock не проверены. Основные выписки: [1.6](items-1.6.md#effectsea_sword), [2.8.14](items-2.8.14.md#effectsea_sword), [player-группы 2.8.14](player-groups-2.8.14.md).

## Предмет и источники

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

## 1.6: helper и эффекты не обязательно владельцу

- `player.json`: sensor `has_equipment`, self, domain `hand`, value `effect:sea_sword` → `minecraft:sea_sword`, добавляет одноимённую группу. Она объявляет `minecraft:spawn_entity`: `entity:sea`, wait **0/0**, `num_to_spawn:1`, `single_use:true`. Общий `minecraft:event_normal_player` удаляет эту группу, поэтому количество/период spawn не выводятся из одного `single_use`.
- `entities/sea.json`: helper family `despawnear`, despawn filter на ту же family, health **1**, collision width/height **0/0**, fire immune true, physics `{}`; summonable true, spawnable false. `scripts.animate` `sea` → `controller.animation.sea`.
- `animation_controllers/sea_sword.json`: `default` ↔ `sea` с переходами `(1.0)` и одинаковыми четырьмя строками `on_entry` в каждом: `/effect @e[type=guardian,r=6] fatal_poison 5 0 true`, аналог для `drowned`, `/effect @p conduit_power 16 0 true`, `/scoreboard players set @a swords 2`. Числа в командах effect — duration **5**/**16**, amplifier **0**, `true`; единицы и совместимость старой команды проверять в движке.
- Guardian и drowned выбираются в r=6 от контекста helper. `@p` означает ближайшего игрока относительно контекста, не гарантированно того, кто вызвал helper; команда scoreboard касается всех `@a`. В списке нет отдельной команды `elder_guardian` и нет проверки «игрок в воде». Не предполагать, что эффект poison действует на все морские виды, что эффект применяется раз в фиксированное время или что владелец всегда выбран.

## 2.x: события и фактические объявления групп

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

### Неполное явное снятие групп

В имеющихся JSON, mcfunction и JS обоих 2.x буквальное имя `mermaid_movement_out_water` встречается только в определении и в `add` вышеприведённой ветви; его **явного remove в этих файлах не найдено**. При ветви воды `mermaid_movement_in_water` добавляется без явного удаления out-water; при выходе добавляется out-water без явного удаления in-water; stop явно удаляет только in-water вместе с sea group. Это перечисление операций в источнике, а не доказательство, что обе группы фактически сохраняются и складываются в движке.

Особенно важно: stop добавляет `minecraft:default_player`, где объявлены movement **0.1**, underwater_movement **0.02**, collision **0.6×1.8**, breathable total_supply **15**, inhale_time **3.75**, suffocate_time **−1**. Если движок допускает совместное наличие или замену групп с одинаковыми компонентами, приоритет значений и фактическое восстановление зависят от движка и порядка событий. Проверить последовательности «взять на суше → войти в воду → выйти → убрать меч», «взять в воде → выйти → убрать», быстрое переключение и несколько игроков. Не обещать ни постоянного замедления, ни гарантированного восстановления по одному отсутствию remove.

## Условная модель получения из buried treasure 2.x

Файл `Swords_B/loot_tables/chests/buriedtreasure.json` одинаков побайтово в обеих 2.x. Pool 0: **1** roll, одна запись `minecraft:heart_of_the_sea`, без указанного weight. Pool 1: rolls **5…12**, у 19 записей все веса явно заданы, их сумма **219**, у Sea Sword **15**, отсутствует функция set_count в самой записи. При стандартной модели весов один выбор даёт `15/219 = 5/73 ≈ 6.8493%`.

Если дополнительно предположить равномерный выбор целого числа rolls в диапазоне 5…12, независимые выборы с возвращением, отсутствие модификаторов и успешную регистрацию/применение именно этой таблицы, вероятность хотя бы одной выбранной записи — среднее `1 − (1 − 15/219)^n` по n=5…12, то есть **≈44.5623%**, математическое ожидание числа выбранных записей ≈**0.5822**. Это не измеренная вероятность конкретного сундука или мира: генерация структуры, выбор таблицы, регистрация предмета и правила игры остаются непроверенными. Наличие heart_of_the_sea в отдельном pool не доказывает, что 1.6-рецепт присутствует в 2.x.
