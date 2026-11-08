# Построчное сравнение архивов 2.8.8 → 2.8.14

Имена корневых папок `Sword_B`/`Sword_R` в 1.6 нормализованы к `Swords_B`/`Swords_R` исключительно для сопоставления. Остальные пути сопоставляются буквально. Переименования файлов и смысловые эквиваленты автоматически не обнаруживаются; совпадение ID не гарантирует одинаковой механики. Двоичные файлы сравниваются по байтам без визуальной оценки. Для текстовых diff перенесены строки без различия CRLF/LF; изменение только окончания строк отражено в таблице как изменённый файл, но diff может быть пустым. Исходные архивы и их инвентаризации остаются эталоном.

## Сопоставление ID предметов

| ID | Старый путь | Новый путь |
|---|---|---|
| `effect:bedrock_stick` | `Swords_B/items/bedrock_stick.json` | `Swords_B/items/bedrock_stick.json` |
| `effect:bedrock_sword` | `Swords_B/items/bedrock_sword.json` | `Swords_B/items/bedrock_sword.json` |
| `effect:bee_sword` | `Swords_B/items/bee_sword.json` | `Swords_B/items/bee_sword.json` |
| `effect:blaze_sword` | `Swords_B/items/blaze_sword.json` | `Swords_B/items/blaze_sword.json` |
| `effect:bone_sword` | `Swords_B/items/bone_sword.json` | `Swords_B/items/bone_sword.json` |
| `effect:cactus_sword` | `Swords_B/items/cactus_sword.json` | `Swords_B/items/cactus_sword.json` |
| `effect:clock_sword` | `Swords_B/items/clock_sword.json` | `Swords_B/items/clock_sword.json` |
| `effect:coal_sword` | `Swords_B/items/coal_sword.json` | `Swords_B/items/coal_sword.json` |
| `effect:creeper_sword` | `Swords_B/items/creeper_sword.json` | `Swords_B/items/creeper_sword.json` |
| `effect:cursed_pumpkin_sword` | `Swords_B/items/pumpkin_sword.json` | `Swords_B/items/pumpkin_sword.json` |
| `effect:emerald_sword` | `Swords_B/items/emerald_sword.json` | `Swords_B/items/emerald_sword.json` |
| `effect:ender_sword` | `Swords_B/items/ender_sword.json` | `Swords_B/items/ender_sword.json` |
| `effect:fire_sword` | `Swords_B/items/fire_sword.json` | `Swords_B/items/fire_sword.json` |
| `effect:ghost_sword` | `Swords_B/items/ghost_sword.json` | `Swords_B/items/ghost_sword.json` |
| `effect:glass_sword` | `Swords_B/items/glass_sword.json` | `Swords_B/items/glass_sword.json` |
| `effect:glowstone_sword` | `Swords_B/items/glowstone_sword.json` | `Swords_B/items/glowstone_sword.json` |
| `effect:grass_sword` | `Swords_B/items/grass_sword.json` | `Swords_B/items/grass_sword.json` |
| `effect:ice_sword` | `Swords_B/items/ice_sword.json` | `Swords_B/items/ice_sword.json` |
| `effect:jungle_sword` | `Swords_B/items/jungle_sword.json` | `Swords_B/items/jungle_sword.json` |
| `effect:lapis_sword` | `Swords_B/items/lapis_sword.json` | `Swords_B/items/lapis_sword.json` |
| `effect:lightning_sword` | `Swords_B/items/lightning_sword.json` | `Swords_B/items/lightning_sword.json` |
| `effect:magma_sword` | `Swords_B/items/magma_sword.json` | `Swords_B/items/magma_sword.json` |
| `effect:nether_star_sword` | `Swords_B/items/nether_star_sword.json` | `Swords_B/items/nether_star_sword.json` |
| `effect:obsidian_sword` | `Swords_B/items/obsidian_sword.json` | `Swords_B/items/obsidian_sword.json` |
| `effect:quartz_diamond` | `Swords_B/items/quartz_diamond.json` | `Swords_B/items/quartz_diamond.json` |
| `effect:quartz_diamond_stick` | `Swords_B/items/quartz_diamond_stick.json` | `Swords_B/items/quartz_diamond_stick.json` |
| `effect:quartz_sword` | `Swords_B/items/quartz_sword.json` | `Swords_B/items/quartz_sword.json` |
| `effect:sea_sword` | `Swords_B/items/sea_sword.json` | `Swords_B/items/sea_sword.json` |
| `effect:shulker_sword` | `Swords_B/items/shulker_sword.json` | `Swords_B/items/shulker_sword.json` |
| `effect:silver_ingot` | `Swords_B/items/silver_ingot.json` | `Swords_B/items/silver_ingot.json` |
| `effect:silver_sword` | `Swords_B/items/silver_sword.json` | `Swords_B/items/silver_sword.json` |
| `effect:slime_sword` | `Swords_B/items/slime_sword.json` | `Swords_B/items/slime_sword.json` |
| `effect:spectral_sword` | `Swords_B/items/spectral_sword.json` | `Swords_B/items/spectral_sword.json` |
| `effect:spider_sword` | `Swords_B/items/spider_sword.json` | `Swords_B/items/spider_sword.json` |
| `effect:sponge_sword` | `Swords_B/items/sponge_sword.json` | `Swords_B/items/sponge_sword.json` |
| `effect:time_sword` | `Swords_B/items/time_sword.json` | `Swords_B/items/time_sword.json` |
| `effect:tnt_sword` | `Swords_B/items/tnt_sword.json` | `Swords_B/items/tnt_sword.json` |
| `effect:ultra_instinct_sword` | `Swords_B/items/ultra_instinct_sword.json` | `Swords_B/items/ultra_instinct_sword.json` |
| `effect:wet_sponge_sword` | `Swords_B/items/wet_sponge_sword.json` | `Swords_B/items/wet_sponge_sword.json` |
| `effect:wither_skeleton_sword` | `Swords_B/items/wither_skeleton_sword.json` | `Swords_B/items/wither_skeleton_sword.json` |
| `effect:wither_sword` | `Swords_B/items/wither_sword.json` | `Swords_B/items/wither_sword.json` |
| `effect:wolf_sword` | `Swords_B/items/wolf_sword.json` | `Swords_B/items/wolf_sword.json` |

## Все несовпадающие пути

| Статус | Нормализованный путь | SHA-256 старый | SHA-256 новый |
|---|---|---|---|
| только 2.8.8 | `Swords_B/blocks/fake_ice.json` | `e8414350bf374784ae96a9d27f69202ca0df0f9dac42b4d66e1c92eb77f8749a` | `—` |
| изменён | `Swords_B/entities/player.json` | `2f499faf84dfc33f9ad0ad0d43ae18b3645ba4c15213b79a511ac7b6776972a3` | `d25d5fe1e885ef35c4027cc25290950b814b96e48a3a211b87bdabc77df2000f` |
| только 2.8.8 | `Swords_B/feature_rules/quartz_diamond_ore_feature.json` | `cacbedb00c7c19f0715c8db0daed9f07ebfe25f825136a5d360f21edbb4a6e30` | `—` |
| только 2.8.8 | `Swords_B/feature_rules/silver_ore_feature.json` | `874fff4eb1e76adb73b65ba8c26368b49a94ab555b5b08e5d36ddd227eb53ae0` | `—` |
| только 2.8.8 | `Swords_B/features/quartz_diamond_ore.json` | `d4c0b1a6963dfdd3b7432dea2c1564ba1d212a11269574dc0144a1111ea0f941` | `—` |
| только 2.8.8 | `Swords_B/features/silver_ore.json` | `ab797c097c7c8bb81d84e0e1d7892bf91eefe85c055aa258389cb86d1028ce2f` | `—` |
| изменён | `Swords_B/items/ice_sword.json` | `19e0fef910cef02c45454da4e0002bdfb2655e7157b35158ec1e5f339fca5bac` | `809dd3dfe17e45a18475f58039395a57453c0cf8579394d1a6811e7578abbe4d` |
| изменён | `Swords_B/manifest.json` | `e02fe32ae3eadb055a7b7b821ac4aaf0f774bf9fd73d6958436ee05d15d4589e` | `b85029ad07cd7c4b22ba6b80e4a63a2e27e7c86556bb8523119abd44e90f3491` |
| изменён | `Swords_B/scripts/javascript.js` | `8ad116f1d8d64ae9d6ee3a0393faa48df6f08246a1452e26d79a560e9ac39a51` | `20ca25df1439d33395c80f697620b2eccac5dbed715c383d3ce05650ab93837b` |
| только 2.8.8 | `Swords_B/structures/quartz_diamond_ore.mcstructure` | `05037a12b1bdaaf22700285709ddecc917ee56f5c8bbc18bbe704cd8ec39ea55` | `—` |
| только 2.8.8 | `Swords_B/trading/economy_trades/weapon_smith_trades.json` | `54dad42718fd2d2472078c26f9bfc4d39d4522dc06a87f89ede8c1bdd1046df6` | `—` |
| только 2.8.8 | `Swords_B/trading/weapon_smith_trades.json` | `3296a3544cb5bd4090144e08141ecf1acb0a4563d4bd2c6d024934899c55f6cb` | `—` |
| изменён | `Swords_R/blocks.json` | `1331675b1b19b5c746bfba5a9baa8ed85e900cec15533bddeb692f906d0d8323` | `5c2f6926da7475319dff6b590bee53a1119e3b8857a0d1f0a070c396637d0546` |
| изменён | `Swords_R/manifest.json` | `54814d2f2e54806620d4606c88b86ac8954d8660883f1c0103de27786d011cf5` | `70f511ffa887bb51c00e9b538af281cdbcd7397604abcaac6f6dfb9486ddcadd` |
| изменён | `Swords_R/texts/en_US.lang` | `824e9ad38b2388dde75b49a99f3d7ef24d5ddf94f6652a41c8425eba070250db` | `37ee50014e83f21d8ee4621d51171f8a475f4bce2b3640fd027aca8f3ce90393` |
| изменён | `Swords_R/textures/terrain_texture.json` | `bd237ff3e0f77c262d20f7aff4c202961b3144b6a86ab49903ef3c0db278774a` | `6795b0800448f2bcfa9aef3404a0f6f5ac0c606ed32f713565fb9223804e46f9` |

Совпадают по нормализованному пути и байтам: 387.

## Построчные изменения совпадающих текстовых путей

### `Swords_B/entities/player.json`

```diff
--- 2.8.8/Swords_B/entities/player.json
+++ 2.8.14/Swords_B/entities/player.json
@@ -1933,17 +1933,17 @@
           },
           {
             "run_command": { "command": [ 
-              "fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 effect99:fake_ice 0 replace water",
-              "fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 effect99:fake_ice 0 replace flowing_water",
-              "fill ~3 ~-1 ~ ~3 ~-1 ~ effect99:fake_ice 0 replace water",
-              "fill ~3 ~-1 ~ ~3 ~-1 ~ effect99:fake_ice 0 replace flowing_water",
-              "fill ~ ~-1 ~3 ~ ~-1 ~3 effect99:fake_ice 0 replace water",
-              "fill ~ ~-1 ~3 ~ ~-1 ~3 effect99:fake_ice 0 replace flowing_water",
-              "fill ~-3 ~-1 ~ ~-3 ~-1 ~ effect99:fake_ice 0 replace water",
-              "fill ~-3 ~-1 ~ ~-3 ~-1 ~ effect99:fake_ice 0 replace flowing_water",
-              "fill ~ ~-1 ~-3 ~ ~-1 ~-3 effect99:fake_ice 0 replace water",
-              "fill ~ ~-1 ~-3 ~ ~-1 ~-3 effect99:fake_ice 0 replace flowing_water",
-              "execute @e[r=64,type=!player] ~ ~ ~ detect ~ ~ ~ effect99:fake_ice 0 tp @s ~ ~ ~ ~1"
+              "fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 frosted_ice 0 replace water",
+              "fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 frosted_ice 0 replace flowing_water",
+              "fill ~3 ~-1 ~ ~3 ~-1 ~ frosted_ice 0 replace water",
+              "fill ~3 ~-1 ~ ~3 ~-1 ~ frosted_ice 0 replace flowing_water",
+              "fill ~ ~-1 ~3 ~ ~-1 ~3 frosted_ice 0 replace water",
+              "fill ~ ~-1 ~3 ~ ~-1 ~3 frosted_ice 0 replace flowing_water",
+              "fill ~-3 ~-1 ~ ~-3 ~-1 ~ frosted_ice 0 replace water",
+              "fill ~-3 ~-1 ~ ~-3 ~-1 ~ frosted_ice 0 replace flowing_water",
+              "fill ~ ~-1 ~-3 ~ ~-1 ~-3 frosted_ice 0 replace water",
+              "fill ~ ~-1 ~-3 ~ ~-1 ~-3 frosted_ice 0 replace flowing_water",
+              "execute @e[r=64,type=!player] ~ ~ ~ detect ~ ~ ~ frosted_ice 0 tp @s ~ ~ ~ ~1"
               ] 
             }
           }
```

### `Swords_B/items/ice_sword.json`

```diff
--- 2.8.8/Swords_B/items/ice_sword.json
+++ 2.8.14/Swords_B/items/ice_sword.json
@@ -82,46 +82,46 @@
           {
             "run_command": {
               "command": [
-                "execute @e[type=!enderman,type=!horse,type=!slime,type=!silverfish,type=!spider,type=!cave_spider,type=!tnt,type=!vex,type=!chicken,type=!pig,type=!wolf,type=!cat,type=!item,type=!xp_orb,type=!xp_bottle,type=!egg,type=!snowball,type=!fireball,type=!small_fireball,type=!eye_of_ender_signal,type=!ender_pearl,type=!fishing_hook,type=!falling_block,type=!lightning_bolt,type=!lingering_potion,type=!dragon_fireball,type=!ender_dragon,type=!endermite,type=!arrow,type=!thrown_trident,type=!leash_knot,type=!bat,type=!rabbit,type=!parrot,type=!ghast,type=!shulker,type=!elder_guardian,type=!guardian,type=!turtle,type=!fox,type=!squid,type=!ocelot,type=!phantom,type=!area_effect_cloud,family=!fish,family=!effect99_entities,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 effect99:fake_ice 0 replace air 0",
-                "execute @e[type=enderman,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~3 ~-1 effect99:fake_ice 0 replace air 0",
-                "execute @e[family=slime_large,rm=2,r=12] ~ ~ ~ fill ~2 ~-1 ~2 ~-2 ~3 ~-2 effect99:fake_ice 0 replace air 0",
-                "execute @e[family=slime_large,rm=2,r=12] ~ ~1 ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 air 0 replace effect99:fake_ice",
-                "execute @e[family=slime_medium,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
-                "execute @e[family=slime_medium,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ air 0 replace effect99:fake_ice",
-                "execute @e[family=slime_small,rm=2,r=12] ~ ~ ~ fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:fake_ice 0 replace air 0",
-                "execute @e[family=slime_small,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ air 0 replace effect99:fake_ice",
-                "execute @e[type=silverfish,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ effect99:fake_ice 0 replace air 0",
-                "execute @e[type=spider,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
-                "execute @e[type=cave_spider,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
-                "execute @e[type=tnt,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
-                "execute @e[type=vex,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
-                "execute @e[type=chicken,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
-                "execute @e[type=pig,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
-                "execute @e[type=wolf,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
-                "execute @e[type=cat,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
-                "execute @e[type=small_fireball,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ effect99:fake_ice 0 replace air 0",
-                "execute @e[type=fireball,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ effect99:fake_ice 0 replace air 0",
-                "execute @e[type=arrow,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ effect99:fake_ice 0 replace air 0",
-                "execute @e[type=lingering_potion,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ effect99:fake_ice 0 replace air 0",
-                "execute @e[type=dragon_fireball,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ effect99:fake_ice 0 replace air 0",
-                "execute @e[type=thrown_trident,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ effect99:fake_ice 0 replace air 0",
-                "execute @e[type=endermite,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
-                "execute @e[type=rabbit,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
-                "execute @e[type=parrot,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
-                "execute @e[type=phantom,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
-                "execute @e[type=shulker,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
-                "execute @e[type=guardian,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
-                "execute @e[type=ocelot,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
-                "execute @e[type=turtle,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
-                "execute @e[type=fox,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
-                "execute @e[type=squid,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
-                "execute @e[type=elder_guardian,rm=2,r=12] ~ ~ ~ fill ~2 ~-1 ~2 ~-2 ~3 ~-2 effect99:fake_ice 0 replace air 0",
-                "execute @e[type=bat,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
-                "execute @e[type=ghast,rm=2,r=12] ~ ~ ~ fill ~4 ~-3 ~4 ~-4 ~4 ~-4 effect99:fake_ice 0 replace air 0",
-                "execute @e[type=ghast,rm=2,r=12] ~ ~ ~ fill ~3 ~-2 ~3 ~-3 ~3 ~-3 air 0 replace effect99:fake_ice",
-                "execute @e[type=horse,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
-                "execute @e[type=horse,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ air 0 replace effect99:fake_ice 0",
-                "execute @e[type=player,rm=3,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 effect99:fake_ice 0 replace air 0",
+                "execute @e[type=!enderman,type=!horse,type=!slime,type=!silverfish,type=!spider,type=!cave_spider,type=!tnt,type=!vex,type=!chicken,type=!pig,type=!wolf,type=!cat,type=!item,type=!xp_orb,type=!xp_bottle,type=!egg,type=!snowball,type=!fireball,type=!small_fireball,type=!eye_of_ender_signal,type=!ender_pearl,type=!fishing_hook,type=!falling_block,type=!lightning_bolt,type=!lingering_potion,type=!dragon_fireball,type=!ender_dragon,type=!endermite,type=!arrow,type=!thrown_trident,type=!leash_knot,type=!bat,type=!rabbit,type=!parrot,type=!ghast,type=!shulker,type=!elder_guardian,type=!guardian,type=!turtle,type=!fox,type=!squid,type=!ocelot,type=!phantom,type=!area_effect_cloud,family=!fish,family=!effect99_entities,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 frosted_ice 0 replace air 0",
+                "execute @e[type=enderman,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~3 ~-1 frosted_ice 0 replace air 0",
+                "execute @e[family=slime_large,rm=2,r=12] ~ ~ ~ fill ~2 ~-1 ~2 ~-2 ~3 ~-2 frosted_ice 0 replace air 0",
+                "execute @e[family=slime_large,rm=2,r=12] ~ ~1 ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 air 0 replace frosted_ice",
+                "execute @e[family=slime_medium,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
+                "execute @e[family=slime_medium,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ air 0 replace frosted_ice",
+                "execute @e[family=slime_small,rm=2,r=12] ~ ~ ~ fill ~1 ~1 ~1 ~-1 ~-1 ~-1 frosted_ice 0 replace air 0",
+                "execute @e[family=slime_small,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ air 0 replace frosted_ice",
+                "execute @e[type=silverfish,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ frosted_ice 0 replace air 0",
+                "execute @e[type=spider,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
+                "execute @e[type=cave_spider,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
+                "execute @e[type=tnt,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
+                "execute @e[type=vex,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
+                "execute @e[type=chicken,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
+                "execute @e[type=pig,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
+                "execute @e[type=wolf,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
+                "execute @e[type=cat,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
+                "execute @e[type=small_fireball,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ frosted_ice 0 replace air 0",
+                "execute @e[type=fireball,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ frosted_ice 0 replace air 0",
+                "execute @e[type=arrow,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ frosted_ice 0 replace air 0",
+                "execute @e[type=lingering_potion,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ frosted_ice 0 replace air 0",
+                "execute @e[type=dragon_fireball,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ frosted_ice 0 replace air 0",
+                "execute @e[type=thrown_trident,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ frosted_ice 0 replace air 0",
+                "execute @e[type=endermite,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
+                "execute @e[type=rabbit,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
+                "execute @e[type=parrot,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
+                "execute @e[type=phantom,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
+                "execute @e[type=shulker,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
+                "execute @e[type=guardian,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
+                "execute @e[type=ocelot,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
+                "execute @e[type=turtle,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
+                "execute @e[type=fox,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
+                "execute @e[type=squid,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
+                "execute @e[type=elder_guardian,rm=2,r=12] ~ ~ ~ fill ~2 ~-1 ~2 ~-2 ~3 ~-2 frosted_ice 0 replace air 0",
+                "execute @e[type=bat,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
+                "execute @e[type=ghast,rm=2,r=12] ~ ~ ~ fill ~4 ~-3 ~4 ~-4 ~4 ~-4 frosted_ice 0 replace air 0",
+                "execute @e[type=ghast,rm=2,r=12] ~ ~ ~ fill ~3 ~-2 ~3 ~-3 ~3 ~-3 air 0 replace frosted_ice",
+                "execute @e[type=horse,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 frosted_ice 0 replace air 0",
+                "execute @e[type=horse,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ air 0 replace frosted_ice 0",
+                "execute @e[type=player,rm=3,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 frosted_ice 0 replace air 0",
                 "title @s actionbar §l§bIce Skill",
                 "playsound random.fizz @a[r=12] ~ ~ ~ 1 2.3",
                 "particle minecraft:knockback_roar_particle ~ ~1 ~"
```

### `Swords_B/manifest.json`

```diff
--- 2.8.8/Swords_B/manifest.json
+++ 2.8.14/Swords_B/manifest.json
@@ -1,8 +1,8 @@
 {
     "format_version": 2,
     "header": {
-        "description": "§l§fCreated by Effect99",
-        "name": "§l§fSwords and more swords §6V2.8.8 B",
+        "name": "§l§fSwords and more swords §6V2.8.9.5 B",
+        "description": "§7By Effect99",
         "uuid": "1acf4d4b-3a3c-1be3-bc21-9512946109b1",
         "version": [1, 0, 0],
         "min_engine_version": [ 1, 19, 40 ]
@@ -24,7 +24,7 @@
         {
             "description": "@minecraft/server",
             "uuid": "b26a4d4c-afdf-4690-88f8-931846312678",
-            "version": "1.8.0-beta"
+            "version": "1.12.0-beta"
         },
         {
             "version": [1, 0, 0],
```

### `Swords_B/scripts/javascript.js`

```diff
--- 2.8.8/Swords_B/scripts/javascript.js
+++ 2.8.14/Swords_B/scripts/javascript.js
@@ -1,7 +1,7 @@
 import { world } from "@minecraft/server"
 
 world.afterEvents.playerBreakBlock.subscribe(f => {
-    if (f.brokenBlockPermutation.type.id.includes('pumpkin') && !f.brokenBlockPermutation.type.id.includes('stem')) {
+    if (f.brokenBlockPermutation.type.id.includes('pumpkin') && !f.brokenBlockPermutation.type.id.includes('stem')) { 
         const { x, y, z } = f.block.location
         if (Math.floor(Math.random() * 1000 + 1) <= 5 && !f.player.hasTag('pumpkin_sword')) {
             f.player.addTag('pumpkin_sword')
```

### `Swords_R/blocks.json`

```diff
--- 2.8.8/Swords_R/blocks.json
+++ 2.8.14/Swords_R/blocks.json
@@ -17,8 +17,5 @@
    },
    "effect99:lightblock2": { 
      "textures": "lightblock2", "sound": "stone" 
-   },
-   "effect99:fake_ice": {
-     "textures": "fake_ice", "sound": "glass" 
    }
 }
```

### `Swords_R/manifest.json`

```diff
--- 2.8.8/Swords_R/manifest.json
+++ 2.8.14/Swords_R/manifest.json
@@ -2,7 +2,7 @@
     "format_version": 2,
     "header": {
         "description": "§l§fCreated by Effect99",
-        "name": "§l§fSwords and more swords §6V2.8.8 R",
+        "name": "§l§fSwords and more swords §6V2.8.9.5 R",
         "uuid": "3f15ae41-a1c1-4111-aa1e-855a98a06316",
         "version": [ 1, 0, 0 ],
         "min_engine_version": [ 1, 19, 40 ]
```

### `Swords_R/texts/en_US.lang`

```diff
--- 2.8.8/Swords_R/texts/en_US.lang
+++ 2.8.14/Swords_R/texts/en_US.lang
@@ -66,7 +66,7 @@
 action.hint.exit.entity:shulker_shield=§l§5Shulker Shield
 action.hint.exit.spider=§lSpider
 
-updates_changelog.header.title=§l§6Changelog §r§fV2.8.8                                                                                     
+updates_changelog.header.title=§l§6Changelog §r§fV2.8.9                                                                                     
 basic_information.header.title=§l§6About                                                                                           
 howtoplay.updates_changelog.title=§lInformation
 howtoplay.basic_information.title=§lInformation
@@ -82,9 +82,9 @@
 howtoplay.sword_mobs.title=§lBlocks, Items and Mobs
 sword_mobs.header.title=§l§6Mobs                                                                                                      
 
-effect.updates_changelog.text_0=• Updated for minecraft 1.20.50+
+effect.updates_changelog.text_0=• Small changes
 effect.updates_changelog.text_1=• Bug fixes
-effect.updates_changelog.text_2=• Small changes
+effect.updates_changelog.text_2=§r
 effect.updates_changelog.text_3=§r
 effect.updates_changelog.text_4=§r 
 effect.updates_changelog.text_5=§r
```

### `Swords_R/textures/terrain_texture.json`

```diff
--- 2.8.8/Swords_R/textures/terrain_texture.json
+++ 2.8.14/Swords_R/textures/terrain_texture.json
@@ -9,7 +9,6 @@
      "quartz_diamond_ore": { "textures": [ "textures/blocks/quartz_diamond_ore"] },
      "quartz_diamond_block": { "textures": [ "textures/blocks/quartz_diamond_block"] },
      "lightblock": { "textures": [ "textures/blocks/lightblock"] },
-     "lightblock2": { "textures": [ "textures/blocks/lightblock2"] },
-     "fake_ice": { "textures": [ "textures/blocks/fake_ice"] }
+     "lightblock2": { "textures": [ "textures/blocks/lightblock2"] }
    }
 }
```
