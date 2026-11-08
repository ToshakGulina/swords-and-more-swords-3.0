# Ресурсы для будущего ремейка: каталог 2.8.8

Это **архивные ресурсы для изучения и последующего использования**, а не готовый ремейк и не подключаемый пакет. Все файлы скопированы без изменений, с исходными именами и относительными путями. Старый `manifest.json`, настройки рендера, UI и другие декларации не следует автоматически подключать к современному проекту: их совместимость предстоит проверять. По отдельной инструкции версию 2.8.14 не использовали.

## Что сохранено

- `Swords_R/` — все 184 файла исходного ресурсного пакета: текстуры предметов, блоков, существ, интерфейса и частиц; все модели, анимации, контроллеры, описания клиентских сущностей, материалы, интерфейс, локализация и настройки звука.
- `Swords_B/pack_icon.png` — иконка behavior pack; `Swords_B/structures/` — все 18 структур, включая витрину armor stand, предметы и образцы руд. Это сохранённые данные старой версии, а не обязательно готовые ресурсы для новой игры. Механика, рецепты и старые скрипты из behavior pack сюда не переносились.
- Всего **203 файла**: 88 PNG (включая обе иконки пакетов), 7 JPEG, 3 TGA, 3 OGG, 82 JSON, 1 LANG, 1 MATERIAL и 18 MCSTRUCTURE; размер содержимого 2 285 824 байта. Есть файлы, которые совпадают побайтово, но они сохранены по обоим путям, поскольку ссылки могут различаться.
- `inventory.json` содержит точный путь, размер и SHA-256 каждого из 203 файлов; `SHA256SUMS` — тот же список хэшей для автоматической проверки. Эти два индекса и этот README не входят в число 203 ресурсов.

## Проверка и ограничения

При извлечении сверены SHA-256 всех файлов; вторая проверка не требует исходного архива. Все 98 изображений успешно декодированы, все 3 OGG полностью декодированы, 82 JSON прочитаны JSON5-парсером без дублирующих ключей. Все 42 item-ID из сохранённой выписки имеют в atlas по одному существующему графическому файлу. Это проверка целостности и связей, **не** проверка визуального воспроизведения в Minecraft и совместимости старых форматов с новой версией.

Исходный 2.8.8 архив предоставлен пользователем, SHA-256 `ab8cbb75c930948f386bf0119bb0a4ee79c084db888c2e9b05deac61b799bb7f`. Наличие файлов не устанавливает лицензию на распространение: права и условия использования ресурсов нужно проверить до публикации. Некоторые ресурсы могут быть основаны на материалах Minecraft или третьих сторон.

## Навигация

| Что нужно | Папка/файл |
|---|---|
| Структуры и витрина | `Swords_B/structures/` |
| Значки 38 мечей и 4 материалов | `Swords_R/textures/items/` и таблица ниже |
| Блоки и анимация текстур | `Swords_R/textures/blocks/`, `Swords_R/textures/terrain_texture.json`, `Swords_R/textures/flipbook_textures.json` |
| Существа и облики | `Swords_R/textures/entity/`, `Swords_R/entity/`, `Swords_R/models/` |
| Игровая справка и картинки | `Swords_R/ui/`, `Swords_R/textures/ui/`, `Swords_R/texts/` |
| Анимации и их условия | `Swords_R/animations/`, `Swords_R/animation_controllers/`, `Swords_R/render_controllers/` |
| Частицы и материалы | `Swords_R/particles/`, `Swords_R/materials/`, текстуры частиц |
| Звуковые файлы и привязки | `Swords_R/sounds/`, `Swords_R/sounds.json` |

Три аудиофайла — стерео 44 100 Гц: `wolf_sword/howl.ogg` 4,715079 с; `wolf_sword/distant_howl.ogg` 5,192132 с; `ghost_sword/wailing.ogg` 27,213787 с. Анимированная текстура кварц-алмазного блока: 8 кадров, 2 тика на кадр, без смешивания кадров.

## Значки всех 42 предметов

Путь ниже относится к этой папке; регистр и имена сохранены. Наличие значка не доказывает корректность его отображения в современном клиенте.

| ID предмета | Ключ atlas | Файл |
|---|---|---|
| `effect:bedrock_stick` | `bedrock_stick` | `Swords_R/textures/items/bedrock_stick.png` |
| `effect:bedrock_sword` | `bedrock_sword` | `Swords_R/textures/items/bedrock_sword.png` |
| `effect:bee_sword` | `bee_sword` | `Swords_R/textures/items/bee_sword.png` |
| `effect:blaze_sword` | `blaze_sword` | `Swords_R/textures/items/blaze_sword.png` |
| `effect:bone_sword` | `bone_sword` | `Swords_R/textures/items/bone_sword.png` |
| `effect:cactus_sword` | `cactus_sword` | `Swords_R/textures/items/cactus_sword.png` |
| `effect:clock_sword` | `clock_sword` | `Swords_R/textures/items/clock_sword.png` |
| `effect:coal_sword` | `coal_sword` | `Swords_R/textures/items/coal_sword.png` |
| `effect:creeper_sword` | `creeper_sword` | `Swords_R/textures/items/creeper_sword.png` |
| `effect:emerald_sword` | `emerald_sword` | `Swords_R/textures/items/emerald_sword.png` |
| `effect:ender_sword` | `ender_sword` | `Swords_R/textures/items/ender_sword.png` |
| `effect:fire_sword` | `fire_sword` | `Swords_R/textures/items/fire_sword.png` |
| `effect:ghost_sword` | `ghost_sword` | `Swords_R/textures/items/ghost_sword.png` |
| `effect:glass_sword` | `glass_sword` | `Swords_R/textures/items/glass_sword.png` |
| `effect:glowstone_sword` | `glowstone_sword` | `Swords_R/textures/items/glowstone_sword.png` |
| `effect:grass_sword` | `grass_sword` | `Swords_R/textures/items/grass_sword.png` |
| `effect:ice_sword` | `ice_sword` | `Swords_R/textures/items/ice_sword.png` |
| `effect:jungle_sword` | `jungle_sword` | `Swords_R/textures/items/jungle_sword.png` |
| `effect:lapis_sword` | `lapis_sword` | `Swords_R/textures/items/lapis_sword.png` |
| `effect:lightning_sword` | `lightning_sword` | `Swords_R/textures/items/lightning_sword.png` |
| `effect:magma_sword` | `magma_sword` | `Swords_R/textures/items/magma_sword.png` |
| `effect:nether_star_sword` | `nether_star_sword` | `Swords_R/textures/items/nether_star_sword.png` |
| `effect:obsidian_sword` | `obsidian_sword` | `Swords_R/textures/items/obsidian_sword.png` |
| `effect:cursed_pumpkin_sword` | `cursed_pumpkin_sword` | `Swords_R/textures/items/cursed_pumpkin_sword.png` |
| `effect:quartz_diamond` | `quartz_diamond` | `Swords_R/textures/items/quartz_diamond.png` |
| `effect:quartz_diamond_stick` | `quartz_diamond_stick` | `Swords_R/textures/items/quartz_diamond_stick.png` |
| `effect:quartz_sword` | `quartz_sword` | `Swords_R/textures/items/quartz_sword.png` |
| `effect:sea_sword` | `sea_sword` | `Swords_R/textures/items/sea_sword.png` |
| `effect:shulker_sword` | `shulker_sword` | `Swords_R/textures/items/shulker_sword.png` |
| `effect:silver_ingot` | `silver_ingot` | `Swords_R/textures/items/silver_ingot.png` |
| `effect:silver_sword` | `silver_sword` | `Swords_R/textures/items/silver_sword.png` |
| `effect:slime_sword` | `slime_sword` | `Swords_R/textures/items/slime_sword.png` |
| `effect:spectral_sword` | `spectral_sword` | `Swords_R/textures/items/spectral_sword.png` |
| `effect:spider_sword` | `spider_sword` | `Swords_R/textures/items/spider_sword.png` |
| `effect:sponge_sword` | `sponge_sword` | `Swords_R/textures/items/sponge_sword.png` |
| `effect:time_sword` | `time_sword` | `Swords_R/textures/items/time_sword.png` |
| `effect:tnt_sword` | `tnt_sword` | `Swords_R/textures/items/tnt_sword.png` |
| `effect:ultra_instinct_sword` | `ultra_instinct_sword` | `Swords_R/textures/items/ultra_instinct_sword.png` |
| `effect:wet_sponge_sword` | `wet_sponge_sword` | `Swords_R/textures/items/wet_sponge_sword.png` |
| `effect:wither_skeleton_sword` | `wither_skeleton_sword` | `Swords_R/textures/items/wither_skeleton_sword.png` |
| `effect:wither_sword` | `wither_sword` | `Swords_R/textures/items/wither_sword.png` |
| `effect:wolf_sword` | `wolf_sword` | `Swords_R/textures/items/wolf_sword.png` |
