# Сопоставление исходных значков предметов

Автоматическое разрешение `minecraft:icon` через локальный `textures/item_texture.json` и PNG. Сопоставление версий — **только по точному item ID**, без догадок о переименованиях. Размер указан в пикселях. PNG «байты одинаковы» сравниваются по SHA-256; «RGBA совпадают» — после декодирования Pillow, при совпадении размеров; многокадровый PNG вызывает ошибку генерации. Различия RGBA включают цвета полностью прозрачных пикселей и не являются визуальной оценкой. Рендер, материалы, анимации и масштаб в игре не проверены. Полные исходные пути и хэши каждого ассета: [1.6](assets-1.6.md), [2.8.8](assets-2.8.8.md), [2.8.14](assets-2.8.14.md).

Охват: 1.6 — 26 ID; 2.8.8 — 42; 2.8.14 — 42; общих между 1.6 и 2.8.14 — 25. Различаются размером или RGBA — 8 из 25; PNG обеих 2.x нужно оценивать по колонке ниже. Пробел в одной версии означает отсутствие именно этого ID, не обязательно отсутствие аналогичного предмета.

| Точный ID | 1.6 размер | 2.8.14 размер | 1.6 ↔ 2.8.14 RGBA | 2.8.8 ↔ 2.8.14 PNG байты |
|---|---:|---:|---|---|
| `effect:bedrock_stick` | — | 16×16 | нет ID | да |
| `effect:bedrock_sword` | — | 16×16 | нет ID | да |
| `effect:bee_sword` | — | 17×17 | нет ID | да |
| `effect:blaze_sword` | 16×16 | 16×16 | RGBA совпадают | да |
| `effect:bone_sword` | 16×16 | 16×16 | различаются 240 пикс. | да |
| `effect:cactus_sword` | 16×16 | 21×21 | другой размер | да |
| `effect:clock_sword` | — | 16×16 | нет ID | да |
| `effect:coal_sword` | 16×16 | 16×16 | RGBA совпадают | да |
| `effect:creeper_sword` | 16×16 | 16×16 | RGBA совпадают | да |
| `effect:cursed_pumpkin_sword` | — | 16×16 | нет ID | да |
| `effect:emerald_sword` | 16×16 | 16×16 | RGBA совпадают | да |
| `effect:ender_sword` | 16×16 | 64×64 | другой размер | да |
| `effect:fire_sword` | 16×16 | 16×16 | RGBA совпадают | да |
| `effect:ghost_sword` | — | 21×21 | нет ID | да |
| `effect:glass_sword` | — | 16×16 | нет ID | да |
| `effect:glowstone_sword` | 16×16 | 16×16 | RGBA совпадают | да |
| `effect:grass_sword` | 16×16 | 32×32 | другой размер | да |
| `effect:ice_sword` | 16×16 | 16×16 | RGBA совпадают | да |
| `effect:jungle_sword` | 16×16 | 16×16 | RGBA совпадают | да |
| `effect:lapis_sword` | 16×16 | 16×16 | RGBA совпадают | да |
| `effect:lightning_sword` | 16×16 | 64×64 | другой размер | да |
| `effect:magma_sword` | 16×16 | 16×16 | RGBA совпадают | да |
| `effect:nether_star_sword` | — | 16×16 | нет ID | да |
| `effect:obsidian_sword` | 16×16 | 16×16 | RGBA совпадают | да |
| `effect:quartz_diamond` | — | 16×16 | нет ID | да |
| `effect:quartz_diamond_stick` | — | 16×16 | нет ID | да |
| `effect:quartz_sword` | 16×16 | 19×19 | другой размер | да |
| `effect:sea_sword` | 16×16 | 16×16 | RGBA совпадают | да |
| `effect:shulker_sword` | 16×16 | 16×16 | RGBA совпадают | да |
| `effect:silver_ingot` | — | 16×16 | нет ID | да |
| `effect:silver_sword` | — | 21×21 | нет ID | да |
| `effect:slime_sword` | 16×16 | 16×16 | RGBA совпадают | да |
| `effect:spectral_sword` | 16×16 | 24×24 | другой размер | да |
| `effect:spider_sword` | 16×16 | 16×16 | RGBA совпадают | да |
| `effect:sponge_sword` | 16×16 | 16×16 | RGBA совпадают | да |
| `effect:sword_of_time` | 16×16 | — | нет ID | нет ID |
| `effect:time_sword` | — | 64×64 | нет ID | да |
| `effect:tnt_sword` | 16×16 | 16×16 | RGBA совпадают | да |
| `effect:ultra_instinct_sword` | — | 128×128 | нет ID | да |
| `effect:wet_sponge_sword` | — | 16×16 | нет ID | да |
| `effect:wither_skeleton_sword` | — | 16×16 | нет ID | да |
| `effect:wither_sword` | 16×16 | 128×128 | другой размер | да |
| `effect:wolf_sword` | — | 21×21 | нет ID | да |
