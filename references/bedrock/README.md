# Offline references: Minecraft Bedrock Creator

Собранные официальные источники для исследования, не ремейк. Тематический разбор, границы проверки и порядок использования: [документация для будущего ремейка](../../docs/remake-bedrock-documentation-ru.md). Версия пользовательского сервера — **1.26.63.1**; версии архивов ниже не следует выдавать за точные данные этого сервера.

## 1. Creator / Script API — документация Microsoft

- `creator-docs-markdown.zip` — 3849 файлов: Markdown из `creator/Documents`, `creator/Reference`, `creator/ScriptAPI`, `creator/Commands`, доступные файлы TOC и лицензии. Справочники предметов, сущностей, компонентов, эффектов, рецептов, генерации, модулей Script API, изменений версий.
- Источник: https://github.com/MicrosoftDocs/minecraft-creator, ветка main, commit `457cdeaa5aa428429884b092895f3979b1f69ad3`.
- SHA-256: `2b2ee5ece5dd2185d2b60670ea49f3e3352eae1ad4c82edf0fd2d7888bb0a95e`.
- Официальный онлайн-вход: https://learn.microsoft.com/minecraft/creator/ . Документация и код лицензируются по условиям `LICENSE` и `LICENSE-CODE` внутри архива. Изображения статей не скачивались, поэтому ссылки на отдельные иллюстрации могут не работать офлайн.
- Это общий снимок, не отдельная версия для каждого движка: в нём встречаются stable и pre-release API, а некоторые статьи устаревают. Наличие метода в тексте не означает, что он стабилен или доступен в целевом движке.

## 2. Версионные ванильные справочники и данные Mojang

- `bedrock-1.26.60.5-reference.zip` — 3735 файлов: HTML `documentation/index.html` и документы про items, blocks, entities, features, loot, recipes и др.; данные схем и Script API в `metadata`; выбранные ванильные определения предметов, блоков, существ, таблиц добычи, рецептов и правил появления.
- Источник: https://github.com/Mojang/bedrock-samples/releases/tag/v1.26.60.5 , commit `15701fa9c13923f12662984c32c124327e40e3d3`. Это найденный официальный стабильный тег, **не** точная версия сервера 1.26.63.1. На целевой версии все спорные компоненты нужно проверять.
- `metadata/script_modules/@minecraft/server_2.11.0.json` и `server-bindings_2.11.0.json` показывают стабильный набор версии 2.11.0 в этом слепке; beta-записи включены для справки и не становятся из-за этого стабильными.
- SHA-256: `f875d57e46cb4681650a0f6aea1c0b02b799ba974b341058281d7398aeb9e8d6`.
- Содержимое — Mojang, условия в `LICENSE.md` внутри архива; применяются условия Minecraft EULA. Ванильные ресурсы и файлы предназначены для справки, лицензия не приравнивается к разрешению свободно распространять их как свои.

## 3. Ванильный ресурсный пакет — текстовые справочники

- `bedrock-1.26.60.5-resource-reference.zip` — 4966 файлов, полученных из исходного архива тега `v1.26.60.5` того же репозитория Mojang. Включены JSON и `.material` внутри `resource_pack`, английская/русская локализация, `languages.json`, а также корневые README, version и лицензия.
- Содержит клиентские определения существ, модели, анимации и контроллеры, attachables, описание частиц, атласы, определения звуков и UI. **Не включает все PNG и аудио**, поэтому это не полный функциональный ресурсный пакет.
- SHA-256: `b36391010e511fdec7a9e991085f266ad8753ab81730b8583b60b78cd5e3c9bf`. Первоисточник: https://github.com/Mojang/bedrock-samples/tree/v1.26.60.5/resource_pack . Условия — `LICENSE.md` внутри архива.

## 4. Примеры скриптов Microsoft

- `microsoft-script-samples.zip` — 83 файла из `howto-gallery` и `custom-components`: примеры обработчиков, предметов, состояний и структур, с лицензией.
- Источник: https://github.com/microsoft/minecraft-scripting-samples, commit `73a171fc8393a1052b4ca0669dc82231f775d8b1`.
- SHA-256: `f84c42bd75872481d31f16c685b35c79ca1d51d4b4688b3445b7d3daafa13437`.
- Репозиторий предупреждает, что примеры могут использовать экспериментальные Beta APIs. Не использовать примеры как доказательство наличия функций в stable; проверять манифест, метаданные и точную версию движка.

## 5. Дополнительные официальные примеры аддонов Microsoft

- `microsoft-addon-examples.zip` — 563 файла из выбранных каталогов `microsoft/minecraft-samples`: `custom_items`, `custom_blocks`, `custom_projectiles`, `custom_features`, `shapeshifter`, `add_entity_robot`, `starter_items`, `starter_blocks`, `addon_starter`, `particles_examples_1.19`, `custom_sounds`, `structure_blocks_sample_behavior_pack`; включены исходные README и LICENSE.
- Источник: https://github.com/microsoft/minecraft-samples, commit `5e04b6f719c316b0611f569af0cab7d6e9a2fb26` (совпал с комментарием исходного ZIP). SHA-256 подборки: `c16349f1c60fc5c2b9794a145f7938192d07e3d82036defb145e20015c0efab9`.
- Это избранные примеры, не полный репозиторий, и они не проверены на сервере 1.26.63.1. Их варианты версий и экспериментальные требования необходимо проверять отдельно. Например, `shapeshifter` демонстрирует состояние и внешний вид отдельной сущности, а не полноценное превращение реального игрока.

## 6. Versioned TypeScript declarations из npm

- `npm/minecraft-server-2.11.0.tgz` — официальный пакет `@minecraft/server@2.11.0`: https://registry.npmjs.org/@minecraft/server/-/server-2.11.0.tgz . SHA-256 `0ba02700b94ac4acf3875a629d3a63fa9d4c737d5eb43c8b7929ab00fd4ea546`.
- `npm/minecraft-server-ui-2.3.0.tgz` — официальный пакет `@minecraft/server-ui@2.3.0`: https://registry.npmjs.org/@minecraft/server-ui/-/server-ui-2.3.0.tgz . SHA-256 `5b13b8ccbb21220672f51ee4888e20cc93f3c8617538ffdf7945530ea90864c3`.
- Оба пакета указывают MIT в своей npm-метаинформации; лицензии и условия проверять по содержимому и публикации. Это объявления типов и документация к API, не движок Minecraft. Простейшие импорты обоих модулей проверены на 1.26.63.1; UI пользователю не показывался. Успешный импорт не гарантирует работу каждого члена.

## 7. Текстовые сведения из предоставленного сервера 1.26.63.1

- `bedrock-server-1.26.63.1-text-reference.zip` — 262 исходных текстовых файла из предоставленного пользователем серверного ZIP: `bedrock_server_how_to.html`, заводской `server.properties`, `release-notes.txt`, `definitions/features/` и `definitions/feature_rules/`. Серверных программ и мира в этой выборке нет.
- Источник — пользовательский `bedrock-server-1.26.63.1.zip` на Google Диске: https://drive.google.com/file/d/1Frpkz7dSquy71iOTbUnkLosx5C5K5jwQ/view ; SHA-256 исходного ZIP `b40b04c8f5a7c42a19ee685c22fc593e66116b9c22741b8c75489306b252ff62`. Исходный архив остаётся на Диске; не рассчитывать на сохранность `/tmp`.
- SHA-256 выборки: `c065d9ae2aa0bd43fdc6bdf9d0ae858d59fc82c48261c3ad869229482c33a40d`. Путь, размер и SHA-256 каждого исходного файла приведены в `bedrock-server-1.26.63.1-text-reference-inventory.json`; сохранено исходное содержимое, но это не полный состав сервера.
- Условия использования смотрите в руководстве и условиях Minecraft; до публичного распространения проверить применимые права. Это точечный справочный снимок, не современный образец готового аддона и не гарантия поведения форматов.

## Как использовать

Открыть ZIP и затем, например, `documentation/index.html` для офлайн-справочника Mojang; в архиве Creator читать Markdown (`creator/Documents/AddCustomItems.md`, `creator/Reference/Content/ItemReference/`, `creator/ScriptAPI/minecraft/server/`). Типы npm лежат в `package/index.d.ts`. Поиск по содержимому можно сделать после извлечения во временный каталог. Перед любым применением сверять стабильный API и формат с целевой версией Bedrock, затем проверять реальные механики на сервере и при необходимости в официальном клиенте. Не заявлять совместимость без испытания.
