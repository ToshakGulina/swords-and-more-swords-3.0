# Буквальные ссылки на файлы — архив 2.8.14

Механический поиск в UTF-8 текстах архива: `loot_tables/*.json`, команды `structure load` и `function`. Сравниваются только буквальные пути внутри того же корневого пакета. Список не является полным графом: пропускает динамические имена, встроенные ссылки и другие виды ресурсов; может захватить комментарии или некомандный текст. **«Не найден в пакете» не означает ошибка:** путь может быть ванильным, разрешаться из другого пакета или по правилам движка; поведение нужно проверять. Обратная ситуация тоже не доказывает доступность в игре.

## Не найдены по буквальному пути в том же пакете

| Тип | Буквальная ссылка | Проверенный путь | Источники: строки |
|---|---|---|---|
| function | `give` | `Swords_R/functions/give.mcfunction` | `Swords_R/texts/en_US.lang`: 127 |
| loot | `loot_tables/blocks/null.json` | `Swords_B/loot_tables/blocks/null.json` | `Swords_B/blocks/quartz_diamond_block.json`: 8; `Swords_B/blocks/quartz_diamond_ore.json`: 8; `Swords_B/blocks/silver_ore.json`: 8 |
| loot | `loot_tables/entities/cat.json` | `Swords_B/loot_tables/entities/cat.json` | `Swords_B/entities/cat.json`: 33 |
| loot | `loot_tables/entities/cat_gift.json` | `Swords_B/loot_tables/entities/cat_gift.json` | `Swords_B/entities/cat.json`: 215 |
| loot | `loot_tables/entities/empty.json` | `Swords_B/loot_tables/entities/empty.json` | `Swords_B/entities/spider.json`: 26 |
| loot | `loot_tables/entities/enderman.json` | `Swords_B/loot_tables/entities/enderman.json` | `Swords_B/entities/enderman.json`: 93 |
| loot | `loot_tables/entities/ghast.json` | `Swords_B/loot_tables/entities/ghast.json` | `Swords_B/entities/ghast.json`: 42 |
| loot | `loot_tables/entities/parrot.json` | `Swords_B/loot_tables/entities/parrot.json` | `Swords_B/entities/parrot.json`: 33 |
| loot | `loot_tables/entities/skeleton.json` | `Swords_B/loot_tables/entities/skeleton.json` | `Swords_B/entities/skeleton.json`: 135 |
| loot | `loot_tables/entities/skeleton_gear.json` | `Swords_B/loot_tables/entities/skeleton_gear.json` | `Swords_B/entities/skeleton.json`: 154 |
| loot | `loot_tables/entities/spider.json` | `Swords_B/loot_tables/entities/spider.json` | `Swords_B/entities/spider.json`: 200 |
| loot | `loot_tables/entities/witch.json` | `Swords_B/loot_tables/entities/witch.json` | `Swords_B/entities/witch.json`: 102 |
| loot | `loot_tables/entities/wither_boss.json` | `Swords_B/loot_tables/entities/wither_boss.json` | `Swords_B/entities/wither.json`: 64 |
| loot | `loot_tables/entities/wolf.json` | `Swords_B/loot_tables/entities/wolf.json` | `Swords_B/entities/wolf.json`: 47 |
| loot | `loot_tables/entity/centella.json` | `Swords_B/loot_tables/entity/centella.json` | `Swords_B/entities/centella.json`: 43 |
| structure | `blaze_sword` | `Swords_B/structures/blaze_sword.mcstructure` | `Swords_B/entities/blaze.json`: 134 |

## Найдены по буквальному пути в том же пакете

| Тип | Буквальная ссылка | Проверенный путь | Источники: строки |
|---|---|---|---|
| function | `commands/swords_and_more_swords/swords_and_more_swords/jungle_sword` | `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction` | `Swords_B/entities/player.json`: 2008 |
| function | `commands/swords_and_more_swords/swords_and_more_swords/tag_swords` | `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/tag_swords.mcfunction` | `Swords_B/entities/player.json`: 1060 |
| function | `commands/swords_and_more_swords/swords_and_more_swords/tellraw1` | `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/tellraw1.mcfunction` | `Swords_B/entities/player.json`: 1313 |
| loot | `loot_tables/blocks/quartz_diamond_block.json` | `Swords_B/loot_tables/blocks/quartz_diamond_block.json` | `Swords_B/blocks/quartz_diamond_block.json`: 26 |
| loot | `loot_tables/blocks/quartz_diamond_ore.json` | `Swords_B/loot_tables/blocks/quartz_diamond_ore.json` | `Swords_B/blocks/quartz_diamond_ore.json`: 22 |
| loot | `loot_tables/blocks/silver_ore.json` | `Swords_B/loot_tables/blocks/silver_ore.json` | `Swords_B/blocks/silver_ore.json`: 22 |
| loot | `loot_tables/empty.json` | `Swords_B/loot_tables/empty.json` | `Swords_B/blocks/lightblock.json`: 8; `Swords_B/blocks/lightblock2.json`: 8; `Swords_B/blocks/spectral_block.json`: 8; `Swords_B/entities/player.json`: 528 |
| loot | `loot_tables/entities/blaze.json` | `Swords_B/loot_tables/entities/blaze.json` | `Swords_B/entities/blaze.json`: 15 |
| loot | `loot_tables/entities/creeper.json` | `Swords_B/loot_tables/entities/creeper.json` | `Swords_B/entities/creeper.json`: 171 |
| loot | `loot_tables/entities/red_enderman.json` | `Swords_B/loot_tables/entities/red_enderman.json` | `Swords_B/entities/enderman.json`: 71 |
| loot | `loot_tables/gameplay/fishing/fish.json` | `Swords_B/loot_tables/gameplay/fishing/fish.json` | `Swords_B/loot_tables/gameplay/fishing.json`: 20 |
| loot | `loot_tables/gameplay/fishing/jungle_fish.json` | `Swords_B/loot_tables/gameplay/fishing/jungle_fish.json` | `Swords_B/loot_tables/gameplay/jungle_fishing.json`: 20 |
| loot | `loot_tables/gameplay/fishing/jungle_junk.json` | `Swords_B/loot_tables/gameplay/fishing/jungle_junk.json` | `Swords_B/loot_tables/gameplay/jungle_fishing.json`: 8 |
| loot | `loot_tables/gameplay/fishing/junk.json` | `Swords_B/loot_tables/gameplay/fishing/junk.json` | `Swords_B/loot_tables/gameplay/fishing.json`: 8 |
| loot | `loot_tables/gameplay/fishing/treasure.json` | `Swords_B/loot_tables/gameplay/fishing/treasure.json` | `Swords_B/loot_tables/gameplay/fishing.json`: 14; `Swords_B/loot_tables/gameplay/jungle_fishing.json`: 14 |
| structure | `bedrock_sword` | `Swords_B/structures/bedrock_sword.mcstructure` | `Swords_B/entities/item.json`: 181 |
| structure | `bone_sword` | `Swords_B/structures/bone_sword.mcstructure` | `Swords_B/entities/skeleton.json`: 275 |
| structure | `creeper_sword` | `Swords_B/structures/creeper_sword.mcstructure` | `Swords_B/entities/creeper.json`: 339 |
| structure | `fire_sword` | `Swords_B/structures/fire_sword.mcstructure` | `Swords_B/entities/item.json`: 184 |
| structure | `ghost_sword` | `Swords_B/structures/ghost_sword.mcstructure` | `Swords_B/entities/ghost.json`: 122 |
| structure | `glass_sword` | `Swords_B/structures/glass_sword.mcstructure` | `Swords_B/entities/item.json`: 229 |
| structure | `grass_sword` | `Swords_B/structures/grass_sword.mcstructure` | `Swords_B/entities/witch.json`: 220 |
| structure | `lightning_sword` | `Swords_B/structures/lightning_sword.mcstructure` | `Swords_B/entities/centella.json`: 107 |
| structure | `obsidian_sword` | `Swords_B/structures/obsidian_sword.mcstructure` | `Swords_B/entities/item.json`: 228 |
| structure | `spectral_sword` | `Swords_B/structures/spectral_sword.mcstructure` | `Swords_B/entities/ender_crystal.json`: 102; `Swords_B/entities/ghast.json`: 112 |
| structure | `time_sword` | `Swords_B/structures/time_sword.mcstructure` | `Swords_B/entities/item.json`: 176 |
| structure | `ultra_instinct_sword` | `Swords_B/structures/ultra_instinct_sword.mcstructure` | `Swords_B/entities/item.json`: 152, 164 |
| structure | `wet_sponge_sword` | `Swords_B/structures/wet_sponge_sword.mcstructure` | `Swords_B/entities/item.json`: 134 |
| structure | `wither_sword` | `Swords_B/structures/wither_sword.mcstructure` | `Swords_B/entities/wither.json`: 163 |
| structure | `wolf_sword` | `Swords_B/structures/wolf_sword.mcstructure` | `Swords_B/entities/alpha_wolf.json`: 278 |
