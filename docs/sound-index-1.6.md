# Звуковые команды и локальные звуки — 1.6

Автоматический указатель строк `playsound`/`stopsound` в JSON-значениях и в текстовых строках mcfunction/JS; приведён весь исходный командный текст и путь внутри разобранного JSON. Это не полный граф звука: `sounds.json`, animation sound_effects, ванильные события, динамические команды и другие пакеты могут вызывать звуки без этих строк. Текстовый просмотр JS/mcfunction может включать неисполняемые строки; валидность, условия события, громкость/единицы и воспроизведение не проверены.

Определение отсутствует локально ≠ ошибка: имя может быть ванильным или предоставлено другим пакетом. `stopsound` разбирается в порядке команда → цель → имя, отсутствие имени отмечено `<all>`. JSON5 пропускает повторённые ключи кроме последнего, а некорректные файлы исключены; полная диагностика ниже. Связи `sounds.json` — в [реестре ресурсов](resource-graph-1.6.md), медиа — в [реестре ассетов](assets-1.6.md).

Объявлено локальных sound ID: 0; командных строк: 14; разных пар команда/звук: 8.

## Диагностика

- Не разобраны: `Sword_B/entities/blaze2.json`, `Sword_B/entities/bone2.json`, `Sword_B/entities/shulker2.json`.
- Повторные ключи при разборе: нет.

## Локальные определения и файлы

## Все обнаруженные строки команд

### `playsound mob.creeper.say`

Локальное sound definition: не найдено; упоминаний: 2.

- `Sword_B/animation_controllers/creeper_sword.json` · `$.animation_controllers.controller.animation.creeper.states.default.on_entry[2]` · `/playsound mob.creeper.say @p[scores={c=90}]`
- `Sword_B/animation_controllers/creeper_sword.json` · `$.animation_controllers.controller.animation.creeper.states.creeper.on_entry[2]` · `/playsound mob.creeper.say @p[scores={c=90}]`

### `playsound mob.endermen.hit`

Локальное sound definition: не найдено; упоминаний: 2.

- `Sword_B/animation_controllers/ender_sword.json` · `$.animation_controllers.controller.animation.ender.states.default.on_entry[6]` · `/playsound mob.endermen.hit @p[scores={e=140}]`
- `Sword_B/animation_controllers/ender_sword.json` · `$.animation_controllers.controller.animation.ender.states.ender.on_entry[6]` · `/playsound mob.endermen.hit @p[scores={e=140}]`

### `playsound mob.endermen.idle`

Локальное sound definition: не найдено; упоминаний: 2.

- `Sword_B/animation_controllers/ender_sword.json` · `$.animation_controllers.controller.animation.ender.states.default.on_entry[7]` · `/playsound mob.endermen.idle @p[scores={e=300}]`
- `Sword_B/animation_controllers/ender_sword.json` · `$.animation_controllers.controller.animation.ender.states.ender.on_entry[7]` · `/playsound mob.endermen.idle @p[scores={e=300}]`

### `playsound mob.endermen.portal`

Локальное sound definition: не найдено; упоминаний: 2.

- `Sword_B/animation_controllers/ender_sword.json` · `$.animation_controllers.controller.animation.ender.states.default.on_entry[5]` · `/playsound mob.endermen.portal @p[scores={e=90}]`
- `Sword_B/animation_controllers/ender_sword.json` · `$.animation_controllers.controller.animation.ender.states.ender.on_entry[5]` · `/playsound mob.endermen.portal @p[scores={e=90}]`

### `playsound mob.endermen.scream`

Локальное sound definition: не найдено; упоминаний: 2.

- `Sword_B/animation_controllers/ender_sword.json` · `$.animation_controllers.controller.animation.ender.states.default.on_entry[4]` · `/playsound mob.endermen.scream @p[scores={e=10}]`
- `Sword_B/animation_controllers/ender_sword.json` · `$.animation_controllers.controller.animation.ender.states.ender.on_entry[4]` · `/playsound mob.endermen.scream @p[scores={e=10}]`

### `playsound mob.endermen.stare`

Локальное sound definition: не найдено; упоминаний: 2.

- `Sword_B/animation_controllers/ender_sword.json` · `$.animation_controllers.controller.animation.ender.states.default.on_entry[8]` · `/playsound mob.endermen.stare @p[scores={e=500}]`
- `Sword_B/animation_controllers/ender_sword.json` · `$.animation_controllers.controller.animation.ender.states.ender.on_entry[8]` · `/playsound mob.endermen.stare @p[scores={e=500}]`

### `playsound mob.wither.death`

Локальное sound definition: не найдено; упоминаний: 1.

- `Sword_B/animation_controllers/wither_sword.json` · `$.animation_controllers.controller.animation.wither.states.wither.on_entry[14]` · `/execute @p[scores={w=200}] ~ ~ ~ playsound mob.wither.death`

### `playsound mob.wither.hurt`

Локальное sound definition: не найдено; упоминаний: 1.

- `Sword_B/animation_controllers/wither_sword.json` · `$.animation_controllers.controller.animation.wither.states.wither.on_entry[15]` · `/execute @p[scores={w=500}] ~ ~ ~ playsound mob.wither.hurt`
