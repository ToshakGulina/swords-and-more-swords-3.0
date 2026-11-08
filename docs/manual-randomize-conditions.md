# Ручная проверка некоторых условий случайного выбора 2.x

Строки относятся к `swordsandmoreswords-2-8-14.mcaddon`. Сами массивы `randomize` для 2.8.8 структурно совпадают с 2.8.14; окружающие условия по всему архиву этим сравнением не подтверждены. Этот разбор — статический, фильтры и порядок их применения движком не испытаны. Полный указатель массивов: [randomize-index.md](randomize-index.md).

## Пчела: выпадение не равно 2% на любую смерть

`Swords_B/entities/bee.json:85–108,842–…`: в группе `angry_bee` поведение `minecraft:behavior.melee_attack` с `attack_once: true` объявляет `on_attack` → `countdown_to_perish_event` на `self`. У этого события сначала стоит `randomize`: вес 2 запускает `loot spawn ~ ~ ~ loot bee_sword` только при фильтре self family `!= bee_sword`, вес 98 — пустая ветвь. Затем следующий элемент `sequence` удаляет восемь групп (включая отсутствующую локально `collect_nectar`) и добавляет `countdown_to_perish`. Следовательно, 2/100 — лишь отношение весов в событии, а не доказанный шанс выпадения на убийство, атаку или за жизнь. Неизвестно, отбрасывается ли сначала недопустимая ветвь и перенормируются ли веса; возможность выполнить loot-команду и состав самой таблицы надо анализировать отдельно.

## Эндермен: биом относится к одной ветви

`Swords_B/entities/enderman.json:211–…`: при объявленном `minecraft:entity_spawned` вес 80 добавляет `minecraft:default_enderman` и `minecraft:enderman_calm`; вес 20 добавляет `minecraft:red_enderman`, `red_enderman`, `minecraft:enderman_calm`, только если `has_biome_tag == overworld`. Здесь `minecraft:red_enderman` — variant 1; отдельная группа `red_enderman` задаёт scale 1.2, health 120/120, attack damage 12 и loot `loot_tables/entities/red_enderman.json` (`:16–19,47–72`). Ветвь 20/100 не следует представлять как гарантированные 20% красных эндерменов во всех биомах: способ обработки невыполненного фильтра не установлен, есть также отдельное событие `red_enderman` в том же файле.

## Паук: вложенность и пересекающиеся фильтры

`Swords_B/entities/spider.json:261–…`: событие `minecraft:entity_spawned` сначала добавляет `minecraft:default_spider`. Затем наружный выбор `[1,99]`: ветвь 1 содержит ещё один выбор, ветвь 99 добавляет `minecraft:spider_neutral`. Внутренние веса `[80,80,20]` с отдельными фильтрами:

1. 80: ночь (`is_daytime: false`) И снег (`is_snow_covered: true`) И не под землёй (`is_underground: false`); добавить `minecraft:spider_stray_jockey`, `minecraft:spider_neutral`.
2. 80: `is_biome: the_nether`; добавить `minecraft:spider_wither_jockey`, `minecraft:spider_neutral`.
3. 20: ночь ИЛИ под землёй; добавить `minecraft:spider_jockey`, `minecraft:spider_neutral`.

У каждой внутренней ветви также присутствует пустой `remove: {}`. Фильтры первой и третьей ветвей могут выполняться одновременно. Простое умножение 1/100 на 80/180 или 20/180 не доказывает частоту: движок может иначе учитывать недопустимые и пересекающиеся ветви. Это поведение заменённого ванильного паука, не утверждение о прямой связи с Spider Sword.

## Blaze: семь весов не складываются в 100

`Swords_B/entities/player.json:640–645,2163–…`: environment sensor проверяет `effect:blaze_sword` в `domain: hand` и вызывает `minecraft:blaze_sword`. Третий элемент последовательности отдельно требует self family `== blaze_sword_skill` и содержит `[5,5,5,5,5,5,95]`, сумма **125**. Первые пять ветвей — частица `minecraft:mobflame_single` в пяти координатах; шестая — `playsound mob.blaze.breathe @a[r=12] ~ ~ ~ 0.5`; последняя пуста. При обычной нормализации заданных весов каждая непустая ветвь — 5/125 = 4%, пустая — 95/125 = 76%, но только при вызове именно этого элемента и при стандартной интерпретации весов. Это не шансы активации умения или срабатывания на удар. Частота вызова environment sensor и сосуществование групп/таймеров нуждаются в испытании.
