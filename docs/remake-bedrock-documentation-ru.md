# Техническая документация Bedrock для будущего ремейка

## Границы этого этапа

Это подготовка и изучение, **не реализация аддона**. Игровые правила и выборы пользователя находятся в [памятке](remake-master-brief-ru.md); план испытаний — в [технической приёмке](remake-technical-verification-ru.md). Настоящий документ фиксирует, где искать нужные технические сведения, что непосредственно установлено и что остаётся проверить. В перечисленных разделах изучены положения, из которых сделаны выводы ниже; некоторые дополнительные ссылки служат указателями для дальнейшей проверки. Он не означает, что все тысячи страниц архивов прочитаны или что уже доказана реализуемость каждого сочетания механик. Ранее созданный код ремейка удалён по требованию пользователя; нового кода ремейка на этом этапе нет.

**Продолжение:** [карта всех 38 мечей, 13 существ и мировых систем](remake-readiness-matrix-ru.md) с дополнительными серверными опытами. Часть ранних замечаний ниже уточнена новыми результатами.

### Точная проверенная версия

- Полученный от пользователя файл — **`bedrock-server-1.26.63.1.zip`**, Drive ID `1Frpkz7dSquy71iOTbUnkLosx5C5K5jwQ`, 98 092 352 байта. MD5 `bfcf30b5f7d29bb89d0711eca40f5b60` совпал с метаданными Drive; SHA-256 `b40b04c8f5a7c42a19ee685c22fc593e66116b9c22741b8c75489306b252ff62`; `unzip -tq` не обнаружил повреждений. Это не ранее использованный сервер 1.26.62.1.
- В отдельной временной директории vanilla-сервер запустился, сам сообщил `Version: 1.26.63.1`, `Build ID: 53340802` и штатно остановился. Запуск проверен без игроков и без аддона. Архив хранится у пользователя на Drive; временные локальные копии могут исчезать и не являются хранилищем. В проекте дополнительно сохранена проверенная выборка 262 текстовых файлов из этого сервера, включая руководство и definitions (см. каталог справочников ниже). Сам серверный ZIP в репозиторий не помещён.
- Отдельный **временный диагностический** behavior pack, не являющийся ремейком, загрузил зависимость `@minecraft/server` **2.11.0** без Beta APIs. Его скрипт импортировал `world`, `system`, `ItemStack`, `EquipmentSlot`, `EntityDamageCause`, после запуска мира создал `minecraft:stone` и прочитал число игроков (0). Диагностический пакет и его тестовый мир затем удалены. Отдельная минимальная проверка импортировала `ActionFormData` из `@minecraft/server-ui` 2.3.0 без Beta APIs; форму пользователю не показывали. Это подтверждает именно эти загрузки и указанные операции, но не все методы API и не работу аддона.
- В первом запуске с включённой аутентификацией сервер ожидал Minecraft services и не дошёл до `Server started`; остановлен. Успешная проверка выполнена локально в изолированной копии с `online-mode=false`, `allow-list=false`, `allow-player-joining=false` и привязкой к `127.0.0.1`; это **не инструкция для публичного сервера** и не проверка клиентского подключения. Сам сервер сообщает в комплектном руководстве требования к системе и способ запуска.
- Последний найденный официальный образец Mojang — **v1.26.60.5**, не точная копия сервера 1.26.63.1. Он содержит ванильные данные, схемы и стабильные версии API, но все расхождения с текущим сервером проверяются на самом сервере и клиенте. Один образец не доказывает, что более новой версии игры не существует. Общая документация Creator может содержать старые сведения, preview и beta.

## Собранные материалы и воспроизведение

Все архивы с указанием источников, лицензий и хэшей перечислены в [`references/bedrock/README.md`](../references/bedrock/README.md). Внутри архивов сохраняется структура официальных репозиториев. Обозначения далее:

- **C** — `references/bedrock/creator-docs-markdown.zip`: документация Microsoft Creator (Markdown), снимок commit `457cdeaa5aa428429884b092895f3979b1f69ad3`. Официальный репозиторий: <https://github.com/MicrosoftDocs/minecraft-creator>. Это выбранный текстовый снимок, не все изображения или весь репозиторий.
- **B** — `references/bedrock/bedrock-1.26.60.5-reference.zip`: официальные поведенческие примеры, схемы и метаданные API Mojang по тегу `v1.26.60.5`. <https://github.com/Mojang/bedrock-samples/releases/tag/v1.26.60.5>.
- **R** — `references/bedrock/bedrock-1.26.60.5-resource-reference.zip`: дополнение из того же тега — текстовые JSON/material-файлы ресурсного пакета, английская и русская локализации и лицензия. Оно не содержит все изображения и звуки ванили; не считать его полным RP.
- **S** — `references/bedrock/microsoft-script-samples.zip`: выбранные примеры Microsoft. Проверять их конкретный манифест: часть примеров может требовать экспериментальные функции.
- **M** — `references/bedrock/microsoft-addon-examples.zip`: избранные официальные примеры предметов, блоков, сущностей, снарядов, фич и структур из Microsoft `minecraft-samples` (commit `5e04b6f719c316b0611f569af0cab7d6e9a2fb26`), с лицензией; не весь репозиторий и не доказательство исполнения на 1.26.63.1.
- **T** — `references/bedrock/npm/minecraft-server-2.11.0.tgz` и `minecraft-server-ui-2.3.0.tgz`: официальные versioned TypeScript declarations из npm, с `package/index.d.ts`, `README.md`, метаданными пакета. Это **типы, не движок** и не доказательство исполнения каждого вызова. Оба модуля частично проверены импортом выше; фактический показ форм и отдельные методы не проверены.
- **U** — `references/bedrock/bedrock-server-1.26.63.1-text-reference.zip`: `bedrock_server_how_to.html`, `server.properties`, `release-notes.txt`, `definitions/features/` и `definitions/feature_rules/`, сохранённые из пользовательского архива сервера. Отдельный инвентарь содержит SHA-256 каждого файла. Они относятся к самой серверной сборке и не заменяют документацию аддонов.

Примеры путей вида `C:creator/...` обозначают файл внутри архива C, не ссылку на распакованную папку репозитория. Найти их можно через `unzip -l` или открыть архив. Проверять `format_version`, `min_engine_version`, версию Script API и experimental-пометки в каждом применяемом примере отдельно.

## 1. Пакеты, версии, диагностика

**Разделы и ориентиры:** C:`creator/Documents/AddonDevelopmentWorkflow.md`, `BehaviorPack.md`, `ResourcePack.md`, `BaseGameVersioning.md`, `ExperimentalFeaturesToggle.md`; C:`creator/Reference/Content/ManifestReference/packmanifestdocument.md`, `header.md`, `module.md`, `dependency.md`; C:`creator/Documents/BedrockServer/scripting.md`; U:`bedrock_server_how_to.html` и `server.properties`.

**Вывод:** behavior и resource pack имеют отдельные манифесты и уникальные идентификаторы; зависимости, версии пакета, `min_engine_version`, `format_version` содержимого и версия Script API — разные вещи. Порядок паков и загрузка содержимого имеют значение. Для проверки смотреть content log, pack stack и ошибки скриптов, затем клиент; отсутствие ошибки не доказывает, что компонент работает так, как задумано. Наблюдавшийся раньше отказ старого значения creative group — пример того, что прежний формат нельзя просто скопировать.

## 2. Предметы, урон, износ, топливо и ремонт

**Разделы и ориентиры:** C:`creator/Documents/AddCustomItems.md`; C:`creator/Reference/Content/ItemReference/Examples/ItemComponents/` — `description_component.md`, `minecraft_damage.md`, `minecraft_durability.md`, `minecraft_enchantable.md`, `minecraft_repairable.md`, `minecraft_fuel.md`, `minecraft_digger.md`, `minecraft_icon.md`, `minecraft_weapon.md`, `minecraft_render_offsets.md`; B:`behavior_pack/items/`; R:`resource_pack/textures/item_texture.json`; M:`custom_items/`, `starter_items/`.

**Вывод:** `minecraft:damage` описан как добавка к базовому урону; `fuel.duration` измеряется в секундах; `repairable` задаёт допустимые материалы и величину ремонта; иконка через актуальный `textures.default` ссылается на ключ атласа. Старые `minecraft:weapon` и `minecraft:render_offsets` помечены устаревшими. Не предполагать без измерения, что число из старого JSON равно отображаемому и фактическому урону в новом движке. Наличие `durability` само по себе не доказывает эквивалентность старых событий износа, эффективности, чар, наковальни и отображения в руке: нужны отдельные проверки. У Quartz ограничение урона, указанные три входа и поломка требуют особого теста.

## 3. Рецепты и выдача

**Разделы и ориентиры:** C:`creator/Documents/RecipeIntroduction.md`, `FunctionsIntroduction.md`; C:`creator/Reference/Content/RecipeReference/Examples/RecipeDefinitions/` — `minecraftRecipe_Shaped.md`, `minecraftRecipe_Shapeless.md`, `minecraftRecipe_Furnace.md`, `RecipeTagList.md`; C:`creator/ScriptAPI/minecraft/server/ItemInventoryComponent.md`, `Container.md`, `ContainerSlot.md`, `ItemStack.md`; B:`behavior_pack/recipes/`.

**Вывод:** shaped-рецепт задаёт сетку и соответствия символов, shapeless и furnace — отдельные форматы; пример из документации не доказывает доступность конкретного ингредиента Fire Sword в обычной игре. Для `/function give` пользователь выбрал два шалкера по 19 мечей, проверку двух свободных ячеек и отказ без потери предметов. В тесте 1.26.63.1 у трёх только что созданных шалкеров компонент `ItemInventoryComponent` не обнаружен; созданный через диагностическую loot-таблицу шалкер тоже не предоставил его. Данные внутри, выдачу, установку и разрушение не проверяли; путь через `fill_container` требует дальнейшего опыта. Это не доказывает невозможности выполнить требование. Контекст исполнителя команды и командного блока проверить раздельно.

## 4. События, расписание и версии API

**Разделы и ориентиры:** C:`creator/Documents/scripting/versioning.md`, `v2-overview.md`, `custom-components.md`, `events.md`, `execution-privilege.md`, `system-run-guide.md`, `error-handling.md`, `script-performance.md`; C:`creator/ScriptAPI/minecraft/server/ItemCustomComponent.md`, `ItemComponentBeforeDurabilityDamageEvent.md`, `WorldBeforeEvents.md`, `WorldAfterEvents.md`, `System.md`; T:`package/index.d.ts`.

**Вывод:** stable и `-beta` — разные каналы; типовой пакет нужно сверять с фактически поддержанным сервером. Документ `v2-overview.md` содержит историческое предупреждение о preview V2, но указанная выше минимальная проверка показывает, что **конкретно 2.11.0** загружается на 1.26.63.1 без Beta APIs. Нельзя делать вывод о стабильности всех членов из статьи или общего названия версии.

В тесте 1.26.63.1 `world.beforeEvents.entityHurt` успешно отменил и изменил магический урон на свиньях; это не доказывает все случаи игрока и melee. В рассмотренных объявлениях 2.11.0 `ItemCustomComponent` имеет `onHitEntity`, `onMineBlock`, `onUse`, `onUseOn`, `onBeforeDurabilityDamage`; последний описан для повреждения предмета **при ударе сущности**, и его не следует автоматически считать обработчиком добычи блока. Before-events ограничивают изменение мира; отмена должна быть сделана в самом before-event, отложенные действия уже не могут отменить событие. `system.run`, `runTimeout`, `runInterval`, `runJob` имеют разную семантику задержек; `runJob` не обещает завершение в заданный тик. Таймеры и порядок случайных попыток следует испытывать, а не выводить из имени функции.

## 5. Сущности, формы, владельцы и многопользовательский режим

**Разделы и ориентиры:** C:`creator/Documents/EntityBehaviorIntroduction.md`, `EntityComponentsGuide.md`, `EntityEvents.md`, `IntroductionToEntityFamilies.md`, `IntroductionToEntityProperties.md`, `Spawning/EntitySpawningDeepDive.md`, `scripting/multiplayer-scripts.md`; C:`creator/Reference/Content/EntityReference/Examples/Filters/`; C:`creator/ScriptAPI/minecraft/server/Entity.md`, `EntityDamageSource.md`, `EntityDieAfterEvent.md`; B:`behavior_pack/entities/`, `behavior_pack/spawn_rules/`; R:`resource_pack/entity/`; M:`add_entity_robot/`, `shapeshifter/`. Пример shapeshifter переключает свойство и внешний вид **отдельного моба**, не заменяет исследование превращения игрока.

**Вывод:** события и component groups задают состояние сущности, `family` — фильтр, но семейство не равнозначно реальной идентичности игрока. Это важно для Wolf/Ghost и для пользовательского правила о наградах. Документация указывает, что скрипты серверные и в мире может быть ноль, один или несколько игроков; динамические свойства описаны как сохраняемые между перезапусками. При этом владение, обработка выхода/смерти/смены измерения и отношения помощников не появляются автоматически: их нужно отдельно проектировать и проверять по памятке. Вызовы и ссылки на сущности могут стать недействительными при выгрузке.

Документация по entity events отдельно предупреждает о разных spawn events: проверка только `/summon` не доказывает то же поведение естественного появления. Для Alpha Wolf, Slime King, Grass Witch, призраков и Skeleton Bone необходимо отдельно проверять указанные свет, фазу луны, ночь и варианты смерти, не добавляя лишние условия.

## 6. Источник урона, снаряды, PvP и защита

**Разделы и ориентиры:** C:`creator/ScriptAPI/minecraft/server/EntityDamageSource.md`, `EntityHurtAfterEvent.md`, `EntityDieAfterEvent.md`, `ProjectileHitEntityAfterEvent.md`, `EntityProjectileComponent.md`, `EntityApplyDamageOptions.md`, `GameRules.md`, `EntityQueryOptions.md`; T:`package/index.d.ts`; B:`behavior_pack/entities/`; M:`custom_projectiles/behavior_pack/entities/custom_arrow.json` и соседние клиентские ресурсы. В примере стрелы заданы projectile и on_hit, но это не подтверждает атрибуцию отражённого снаряда.

**Вывод:** в описании `EntityDamageSource` `damagingEntity` и `damagingProjectile` необязательны; у события попадания снаряда `source` также может отсутствовать. Компонент projectile описывает `owner`, но это не доказательство восстановления исходного владельца каждого отражённого или чужого снаряда. Нужны отдельные сценарии неизвестного источника, моба и другого игрока; PvP — отдельное условие, а не проверка только `family`. Документированные события необходимо проверить на реальных ванильных и пользовательских снарядах. Для пассивного Living Flame, пчёл и защитного слизня обязательны согласованные исключения владельца и призванных помощников; не расширять их на другие механики без решения пользователя.

## 7. Блоки, инструменты, чары и восстановление мира

**Разделы и ориентиры:** C:`creator/Documents/AdvancedCustomBlocks.md`; C:`creator/Reference/Content/BlockReference/Examples/BlockComponents/` — `minecraftBlock_destructible_by_mining.md`, `minecraftBlock_destructible_by_explosion.md`, `minecraftBlock_loot.md`, `minecraftBlock_material_instances.md`, `minecraftBlock_geometry.md`; C:`creator/ScriptAPI/minecraft/server/PlayerBreakBlockBeforeEvent.md`, `PlayerBreakBlockAfterEvent.md`, `BlockPermutation.md`, `Block.md`, `Dimension.md`.

**Вывод:** before-событие добычи предоставляет игрока и инструмент и допускает отмену; after-событие происходит после разрушения. Сначала нужно установить фактический порядок дропа, расхода инструмента, чар и игровых событий на сервере. Для трёх блоков выполнять особые правила подходящего инструмента, Silk Touch/Fortune, урона и опыта из памятки; не переносить ванильные значения на веру. `BlockPermutation` и состояние блоков изучить для восстановления Ice/Spectral; выгруженные чанки и изменение блока другим игроком делают простую замену безусловно небезопасной. Тестировать наложения, границы, сохранение и перезапуск.

## 8. Природная генерация, биомы, свет и погода

**Разделы и ориентиры:** C:`creator/Documents/FeaturesTaxonomy.md`, `FeaturesTutorial_1.md`, `FeaturesTutorial_2.md`; C:`creator/Reference/Content/FeatureRulesReference/Examples/`, `FeaturesReference/Examples/`, `EntityReference/Examples/Filters/in_water_or_rain.md`, `is_brightness.md`, `moon_phase.md`, `is_daytime.md`; C:`creator/ScriptAPI/minecraft/server/Dimension.md`, `Block.md`; U:`definitions/features/`, `definitions/feature_rules/`. M:`custom_features/basic_orange_ore/`. В архиве B этих двух каталогов нет; они доступны в самом пользовательском серверном архиве. Пример orange ore — геода и приведён для понимания структуры, не для копирования генерации пользовательской руды.

**Вывод:** feature и feature rule описывают разные части генерации; в документации sequence и aggregate имеют разную зависимость от успешного размещения. Для руд необходимо проверять биомы/измерения, высоты и заменяемые блоки на новых чанках. В U рассмотрены `features/diamond_ore_feature.json` и `feature_rules/overworld_underground_coal_ore_feature.json`: они показывают структуры ore_feature и соответствующего правила, но их старый `format_version` и поля не доказывают полного алгоритма современной ванильной генерации и не задают параметры пользовательских руд. В типах 2.11.0 есть `Dimension.getBiome` и `getLightLevel`, а доступ к выгруженным чанкам может приводить к ошибкам. Фильтр `is_brightness` документирован в диапазоне 0–1; не считать его порог автоматически равным целочисленному свету скриптового API без измерения.

Фильтр `in_water_or_rain` отдельно описывает воду **или** дождь. `Entity.isInWater` в рассмотренных типах — вода и не доказывает дождь; в проверенном `@minecraft/server` 2.11.0 декларации `Dimension.getWeather` нет, хотя есть события смены погоды и `setWeather`. Не подменять правило Sponge/Ender проверкой одной только воды или собственными допущениями о погоде: выбор способа и проверка дождя, укрытия, биомов и перезагрузки ещё впереди.

## 9. Loot, рыбалка и колодец

**Разделы и ориентиры:** C:`creator/Documents/IntroductionToLootTables.md`, `CreateLootTable.md`, `LootTableConditions.md`, `LootAndTradeTableFunctions.md`; C:`creator/Reference/Content/LootTableReference/Examples/`; B:`behavior_pack/loot_tables/`.

**Вывод:** пулы, число rolls, веса, условия и функции применяются на разных уровнях; вес внутри пула не является общей вероятностью события. Возможность Looting, ограничение `killed_by_player`, смертельный удар игрока в превращении, Blaze от снежного голема, сундуки и рыбалку проверять по отдельным ветвям. Геометрия колодца проверяется по блокам; точную копию не отличать от природного колодца.

## 10. Ресурсы и клиентское отображение

**Разделы и ориентиры:** C:`creator/Documents/EntityModelingAndAnimation.md`, `Animations/AnimationsOverview.md`, `Animations/AnimationController.md`, `Animations/AnimationRenderController.md`, `attachables.md`, `AddCustomSounds.md`; C:`creator/Reference/Content/ParticlesReference/`, `AnimationsReference/`, `AttachableReference/`; R:`resource_pack/entity/`, `animations/`, `animation_controllers/`, `render_controllers/`, `models/`, `attachables/`, `particles/`, `sounds.json`, `textures/`, `texts/`.

**Вывод:** серверная регистрация не доказывает, что клиент получил RP и правильно разрешил модель, анимацию, материал, текстуру, локализацию и звук. На этом этапе сохранены текстовые ванильные примеры и оригинальные пользовательские ресурсы 2.8.8; ванильные PNG и звуки полностью в новом справочном архиве не собраны. Внешний вид и звук требуют проверки официальным клиентом, в том числе риск алиасов Alpha Wolf и замену устаревших render offsets.

## 11. Структуры, команды и сохранность данных

**Разделы и ориентиры:** C:`creator/Documents/Structures/IntroductionToStructureBlocks.md`, `Structures/StructureBlocksCommandTutorial.md`; C:`creator/ScriptAPI/minecraft/server/StructureManager.md`, `Structure.md`, `StructurePlaceOptions.md`, `BlockPermutation.md`, `World.md`, `Entity.md`, `ItemStack.md`; B:`behavior_pack/structures/`, если конкретный пример присутствует, и `metadata/`.

**Дополнительно изучены команды:** C:`creator/Commands/commands/execute.md`, `damage.md`, `event.md`, `function.md`, `gamerule.md`, `loot.md`, `replaceitem.md`, `spreadplayers.md`, `structure.md`, `summon.md`. Их контекст и синтаксис зависят от версии; `spreadDistance` описан как расстояние между игроками, а не как минимальное смещение одного игрока.

**Вывод:** структуры, команды и API не дают автоматической гарантии точного восстановления блоков и контейнеров при пересечениях или перезапуске. Это критично для лёд/кристалл/объёмных эффектов и `/function give`. Сохранять и проверять не только ID, но состояние блока и данные контейнера, учитывая права владельца и изменения других игроков; объём проверки сформулирован в пользовательской памятке. Возможности конкретных API необходимо подтвердить на целевой версии.

## 12. Что ещё необходимо исследовать и проверить перед выводами о готовности

1. Выполнен [обзор всех 38 карточек, 13 существ и трёх блоков](remake-readiness-matrix-ru.md): в нём указаны документированные кандидаты и риски. Проверка конкретного исполнения и сочетаний остаётся открытой.
2. Проверить на 1.26.63.1 точное разрешение используемых методов и компонентов, наличие experimental-флагов, события урона/смерти/износа, добычу, выживание и мультиплеер; никаких выводов о выполнении ремейка на основании временного диагностического пакета.
3. Клиентом проверить импорт BP/RP, крафт, наковальню, чары, отображение, анимации, звуки, шалкеры и сохранения; сам сервер этого не демонстрирует.
4. Для чувствительных случаев — дождь, отражённые снаряды, повреждение бедрока, чужие сущности/блоки и перезапуск — провести целевые испытания по [плану приёмки](remake-technical-verification-ru.md), не придумывать поведение.
5. Если официальный образец для точной версии 1.26.63.1 появится или будет предоставлен, сверить его с уже собранным v1.26.60.5. Нельзя превращать совпадение части API в заявление о полной идентичности версий.
