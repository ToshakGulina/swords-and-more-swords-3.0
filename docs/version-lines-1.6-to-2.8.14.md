# Построчное сравнение архивов 1.6 → 2.8.14

Имена корневых папок `Sword_B`/`Sword_R` в 1.6 нормализованы к `Swords_B`/`Swords_R` исключительно для сопоставления. Остальные пути сопоставляются буквально. Переименования файлов и смысловые эквиваленты автоматически не обнаруживаются; совпадение ID не гарантирует одинаковой механики. Двоичные файлы сравниваются по байтам без визуальной оценки. Для текстовых diff перенесены строки без различия CRLF/LF; изменение только окончания строк отражено в таблице как изменённый файл, но diff может быть пустым. Исходные архивы и их инвентаризации остаются эталоном.

## Сопоставление ID предметов

| ID | Старый путь | Новый путь |
|---|---|---|
| `effect:bedrock_stick` | — | `Swords_B/items/bedrock_stick.json` |
| `effect:bedrock_sword` | — | `Swords_B/items/bedrock_sword.json` |
| `effect:bee_sword` | — | `Swords_B/items/bee_sword.json` |
| `effect:blaze_sword` | `Sword_B/items/blaze_sword.json` | `Swords_B/items/blaze_sword.json` |
| `effect:bone_sword` | `Sword_B/items/bone_sword.json` | `Swords_B/items/bone_sword.json` |
| `effect:cactus_sword` | `Sword_B/items/cactus_sword.json` | `Swords_B/items/cactus_sword.json` |
| `effect:clock_sword` | — | `Swords_B/items/clock_sword.json` |
| `effect:coal_sword` | `Sword_B/items/coal_sword.json` | `Swords_B/items/coal_sword.json` |
| `effect:creeper_sword` | `Sword_B/items/creeper_sword.json` | `Swords_B/items/creeper_sword.json` |
| `effect:cursed_pumpkin_sword` | — | `Swords_B/items/pumpkin_sword.json` |
| `effect:emerald_sword` | `Sword_B/items/emerald_sword.json` | `Swords_B/items/emerald_sword.json` |
| `effect:ender_sword` | `Sword_B/items/ender_sword.json` | `Swords_B/items/ender_sword.json` |
| `effect:fire_sword` | `Sword_B/items/fire_sword.json` | `Swords_B/items/fire_sword.json` |
| `effect:ghost_sword` | — | `Swords_B/items/ghost_sword.json` |
| `effect:glass_sword` | — | `Swords_B/items/glass_sword.json` |
| `effect:glowstone_sword` | `Sword_B/items/glowstone_sword.json` | `Swords_B/items/glowstone_sword.json` |
| `effect:grass_sword` | `Sword_B/items/grass_sword.json` | `Swords_B/items/grass_sword.json` |
| `effect:ice_sword` | `Sword_B/items/ice_sword.json` | `Swords_B/items/ice_sword.json` |
| `effect:jungle_sword` | `Sword_B/items/jungle_sword.json` | `Swords_B/items/jungle_sword.json` |
| `effect:lapis_sword` | `Sword_B/items/lapis_sword.json` | `Swords_B/items/lapis_sword.json` |
| `effect:lightning_sword` | `Sword_B/items/lightning_sword.json` | `Swords_B/items/lightning_sword.json` |
| `effect:magma_sword` | `Sword_B/items/magma_sword.json` | `Swords_B/items/magma_sword.json` |
| `effect:nether_star_sword` | — | `Swords_B/items/nether_star_sword.json` |
| `effect:obsidian_sword` | `Sword_B/items/obsidian_sword.json` | `Swords_B/items/obsidian_sword.json` |
| `effect:quartz_diamond` | — | `Swords_B/items/quartz_diamond.json` |
| `effect:quartz_diamond_stick` | — | `Swords_B/items/quartz_diamond_stick.json` |
| `effect:quartz_sword` | `Sword_B/items/quartz_sword.json` | `Swords_B/items/quartz_sword.json` |
| `effect:sea_sword` | `Sword_B/items/sea_sword.json` | `Swords_B/items/sea_sword.json` |
| `effect:shulker_sword` | `Sword_B/items/shulker_sword.json` | `Swords_B/items/shulker_sword.json` |
| `effect:silver_ingot` | — | `Swords_B/items/silver_ingot.json` |
| `effect:silver_sword` | — | `Swords_B/items/silver_sword.json` |
| `effect:slime_sword` | `Sword_B/items/slime_sword.json` | `Swords_B/items/slime_sword.json` |
| `effect:spectral_sword` | `Sword_B/items/spectral_sword.json` | `Swords_B/items/spectral_sword.json` |
| `effect:spider_sword` | `Sword_B/items/spider_sword.json` | `Swords_B/items/spider_sword.json` |
| `effect:sponge_sword` | `Sword_B/items/sponge_sword.json` | `Swords_B/items/sponge_sword.json` |
| `effect:sword_of_time` | `Sword_B/items/Sword of Time.json` | — |
| `effect:time_sword` | — | `Swords_B/items/time_sword.json` |
| `effect:tnt_sword` | `Sword_B/items/tnt_sword.json` | `Swords_B/items/tnt_sword.json` |
| `effect:ultra_instinct_sword` | — | `Swords_B/items/ultra_instinct_sword.json` |
| `effect:wet_sponge_sword` | — | `Swords_B/items/wet_sponge_sword.json` |
| `effect:wither_skeleton_sword` | — | `Swords_B/items/wither_skeleton_sword.json` |
| `effect:wither_sword` | `Sword_B/items/wither_sword.json` | `Swords_B/items/wither_sword.json` |
| `effect:wolf_sword` | — | `Swords_B/items/wolf_sword.json` |

## Все несовпадающие пути

| Статус | Нормализованный путь | SHA-256 старый | SHA-256 новый |
|---|---|---|---|
| только 1.6 | `Swords_B/animation_controllers/blaze_sword.json` | `cc16bec5fd8c4dd8d8ee068d7c6f2d3c1c7ca5b0b81d82da2ed28c6a9408c95d` | `—` |
| только 1.6 | `Swords_B/animation_controllers/bone_sword.json` | `33c6596d17a2c4ab9cc89f56575f21ea7dcc048b0bbcb743aa2daec4554876d9` | `—` |
| только 1.6 | `Swords_B/animation_controllers/cactus_sword.json` | `5d6c303c3a2b84306f62285df35858d6cd1375f8376fb8fbe92d8773b36ff706` | `—` |
| только 2.8.14 | `Swords_B/animation_controllers/climb_spider.json` | `—` | `09ef392cb7613277453ae1ba54b6f1ecce40e4b4b8e697cc4eede769c8d10ae3` |
| только 1.6 | `Swords_B/animation_controllers/coal_sword.json` | `850d2e67a12fbb3a6d807ab00488cc4f93d631573aeb327dbed9bb172df53a6a` | `—` |
| только 1.6 | `Swords_B/animation_controllers/creeper_sword.json` | `8954a3a1db47b4431906e73818e44edd4033c649d55ff95ad875216e578ae64c` | `—` |
| только 2.8.14 | `Swords_B/animation_controllers/despawn.json` | `—` | `db27ecd5ec0d5396f936c6d622e5fbfd2b7946100e728c517cbc6ab290ded4de` |
| только 1.6 | `Swords_B/animation_controllers/emerald_sword.json` | `5bed374fc4c2aeb4a13492fb61c032db751b0ac8b1a896f55ece7b9037d145db` | `—` |
| только 1.6 | `Swords_B/animation_controllers/ender_sword.json` | `2d5f77415a4004c48b0b81957170032e44f2afd6a55a504c4d6ca484b0ff9ed7` | `—` |
| только 1.6 | `Swords_B/animation_controllers/fire_sword.json` | `d556ef301007f656dae2576701567a392f27d347f1f26216062c77ac1aa03d0f` | `—` |
| только 2.8.14 | `Swords_B/animation_controllers/ghost_sword.json` | `—` | `21500da0d412ae1dfbf5145770638f0f4d904980541a47f30edd90c6d5e33375` |
| только 1.6 | `Swords_B/animation_controllers/glowstone_sword.json` | `ecb9fb79070200a9c3c0f160ce79412c02dd811b59a2d57e829328cf5457c753` | `—` |
| только 1.6 | `Swords_B/animation_controllers/grass_sword.json` | `7261c0f875424c8a27a6cf4f65f4d22bd0d0deee0db02942347783c6c135b763` | `—` |
| только 1.6 | `Swords_B/animation_controllers/ice_sword.json` | `c0b015bb19f9e231c925642efc7d378a80ab103a09779234fc5683c3d7e3f204` | `—` |
| только 2.8.14 | `Swords_B/animation_controllers/item_events.json` | `—` | `cd94e5eb2a99fcbb2cccfa950c7d6af269b73dfed54fee8c5bc05b03d618a3ec` |
| только 1.6 | `Swords_B/animation_controllers/jungle_sword.json` | `74900a8be15314c1555dfa19fec4bd6042d7aa04729b38f70aad1d08f1068563` | `—` |
| только 1.6 | `Swords_B/animation_controllers/lapis_sword.json` | `feb49eb14d80a60318d9b4456209438a8faf7d0a23138bbd4b0b85f4c79a764c` | `—` |
| только 1.6 | `Swords_B/animation_controllers/lightning sword.json` | `4d7ebd2f3d3d7af2e7d358786f02cc096b064d2239d67657f418a801b0170b09` | `—` |
| только 1.6 | `Swords_B/animation_controllers/magma_sword.json` | `ac249b853c6c1f292346b35bed57a9964bace2766b2d70f9009eb742d3e06af7` | `—` |
| только 2.8.14 | `Swords_B/animation_controllers/mountable_slime.json` | `—` | `7c925daf917a5ace053bf9e34423ea0bffe45f4bfedc94bcc1de2dfcdc46222d` |
| только 1.6 | `Swords_B/animation_controllers/normal.json` | `4c48dafeb7b17edaaa5417a8a243b2a79eddc39315d370ca091949aad31e53a3` | `—` |
| только 1.6 | `Swords_B/animation_controllers/obsidian_sword.json` | `169c7931557e50a4e9139f927032252de2f016d9a3ffe04e22e7e907c7526df1` | `—` |
| только 1.6 | `Swords_B/animation_controllers/sea_sword.json` | `dc0671ae56a8d0032fcde9f32ead29ebe1e283b1a1f1c1f10087c18e1bec9609` | `—` |
| изменён | `Swords_B/animation_controllers/shulker_sword.json` | `e0b1d1d735cb2a6c3d6736a32846560b606aeabcfd80275b7efacffbda077e67` | `ba6caf1d36b3540522679202d42e6bc3bed68a66d09042d031a9760f6cd9b579` |
| только 1.6 | `Swords_B/animation_controllers/slime_sword.json` | `7b60d114a4e33f6b29392da926800907cd06828f9065c12a67549a3551bf845e` | `—` |
| только 1.6 | `Swords_B/animation_controllers/spectral_sword.json` | `5b12c8746db6e6bf30a21a10105b16c65d9605ed23eb2190666ce20c7ae6979c` | `—` |
| только 1.6 | `Swords_B/animation_controllers/spider_sword.json` | `cdb42be02caa4532a9c7a9cf4f7decc2f7f6e509653423119bd45982248596a4` | `—` |
| только 1.6 | `Swords_B/animation_controllers/sponge_sword.json` | `93ee640d5ca783c7137ca10a74f744c711779af230197031ce7f5e1fbd90ca0d` | `—` |
| только 1.6 | `Swords_B/animation_controllers/sword of time.json` | `7f90bc896f5005db96739287849f48a827397c8e734f49e50c704073cf76f2bb` | `—` |
| только 1.6 | `Swords_B/animation_controllers/tnt_sword.json` | `c7ecc8f4dce5ddadeab5b9e77a10d5912c3bc5e8342f7674de05ac434b2eb031` | `—` |
| изменён | `Swords_B/animation_controllers/wither_sword.json` | `479b07e1047b6c874bac20cfda9dace019dc49026942265c404f7b4b2d94b1c3` | `ea030b9199bb623664e40d012884324f1cc1f5e838928a7db2a8af69c14b2c31` |
| только 2.8.14 | `Swords_B/animation_controllers/wolf_sword.json` | `—` | `dd904f887dc3a770b52d0fe6d1ccd51657b57463314b443e7bdecd2c44ceb1f6` |
| только 2.8.14 | `Swords_B/blocks/lightblock.json` | `—` | `54ca5569507e560b3263300bc53db86f6fc6dc7dccc5f298a464b5dff3282dec` |
| только 2.8.14 | `Swords_B/blocks/lightblock2.json` | `—` | `625eb8f6adf8eddb53664160a08f5aaa0fc7c99eea284dd2249146e4244e31d3` |
| только 2.8.14 | `Swords_B/blocks/quartz_diamond_block.json` | `—` | `7de1c560715ee41b55b7ac28df56afdca137879d5d4a3c38c555418951ed2431` |
| только 2.8.14 | `Swords_B/blocks/quartz_diamond_ore.json` | `—` | `e7540e2289a32789c705b47c74ee0a18f8bc789844690db054d0bf8260a1acb8` |
| только 2.8.14 | `Swords_B/blocks/sapling3.json` | `—` | `e4f4ff21949cf7b2fdd74c1d3571e93fbeee6f63afdeb48f0e0c7b481143b5a9` |
| только 2.8.14 | `Swords_B/blocks/silver_ore.json` | `—` | `614885cb79b6a9f6f3bd6f492bb05934c4f8c22172b1a17c919d44d4e3d03776` |
| только 2.8.14 | `Swords_B/blocks/spectral_block.json` | `—` | `88d37b9e578bdc3cbdcc99a5c92a67389624387732a90bce1f1a897f24258653` |
| только 2.8.14 | `Swords_B/entities/alpha_wolf.json` | `—` | `6aebaa796970ae812ec74289ae4abd93705dee25396afe3a14d73b69360397a6` |
| только 2.8.14 | `Swords_B/entities/arrow.json` | `—` | `6313708b77ccc059cfb34639463987aa30129db592bc0f5f0ab06f6072d7ed26` |
| только 2.8.14 | `Swords_B/entities/bee.json` | `—` | `8f2bf0bbbc54c9015a23406fb52caafade8d440c7bc22024a19a96a645a58f1e` |
| только 2.8.14 | `Swords_B/entities/bee_entity.json` | `—` | `af75243ec5ce81a95e75dc0b42abde9222b7b844f1099735a1474ff60227614b` |
| изменён | `Swords_B/entities/blaze.json` | `b260f5aa1c0c1f20325e9701de05fa73160ace8ab250bdbc7d07d39a72aadae4` | `9918581c5584a38910b0db61df2bdab370d33567c16af32bbe1298fc7893e169` |
| только 1.6 | `Swords_B/entities/blaze2.json` | `14a3472453a45ff5a05f71f1f0cf90dd2893b630292595cd04db52220139ced7` | `—` |
| только 1.6 | `Swords_B/entities/bone.json` | `f6e1f4cc23080a8ccf3703ee042e3b110d30a10056126b7e282e53ad79d61320` | `—` |
| только 1.6 | `Swords_B/entities/bone2.json` | `391e135656bd2848e914294782609a039ca4271d85a69a61fb297837573c154b` | `—` |
| только 1.6 | `Swords_B/entities/cactus.json` | `626114c9159f192caf20ae9c3825dad14f5ce933ce4f43ffbb283301df92d5ac` | `—` |
| только 2.8.14 | `Swords_B/entities/cat.json` | `—` | `d384969ec5f6f0c2280911b61c320801faba8354840c1764e8cece5dd3b6bd3f` |
| только 2.8.14 | `Swords_B/entities/centella.json` | `—` | `fba994aa1561e36c12489ec87341ed95f29b5149aed00015c92deda95d684c21` |
| только 1.6 | `Swords_B/entities/coal.json` | `ec69bd60703c993523641b1d9a1721b9d8fc29c0a173d4e79c7c14ae03bda7c7` | `—` |
| изменён | `Swords_B/entities/creeper.json` | `303b4ab16d87697a13425f40db3c5d375a70570d2ae65721374e6e3c8948f66c` | `8c8f169be60ee52a224928d57575cb3b47f19bf41c03e8dd5326f8440d6c33c2` |
| только 1.6 | `Swords_B/entities/emerald.json` | `bfe5c2bc42220766a7a12ba2b7545fe751ce0883a4089301eff0a6d9a192dece` | `—` |
| только 1.6 | `Swords_B/entities/ender.json` | `6fcdbb8b7f1f05f38b68148453784bf1228e151973e61c91bca2be200de510b1` | `—` |
| только 2.8.14 | `Swords_B/entities/ender_crystal.json` | `—` | `8c73c69996d0028e2bc2a1af3a129abfd79f6bebbe8d85ec7b2d261d28227f6e` |
| только 2.8.14 | `Swords_B/entities/ender_crystal_projectile.json` | `—` | `69f6c284942bb9adb98870a27d32701b65c5c5b4ed4f18d4a06a6c20df4435c4` |
| только 2.8.14 | `Swords_B/entities/enderman.json` | `—` | `664c2add376f538c15be3fcf5c9078123f2dd32f2d484e28a576f1e0fe5bef21` |
| только 2.8.14 | `Swords_B/entities/entity_name.json` | `—` | `9018995ca0fd7c61f35d4d073a5630d2c12567deb33709a39de496752845f93b` |
| только 2.8.14 | `Swords_B/entities/entity_nether_star.json` | `—` | `b62e34ded31cf7674147ed3e219655cb2ff348569d4f95d51e6890e984c939b4` |
| только 2.8.14 | `Swords_B/entities/entity_tnt.json` | `—` | `a523e4591d1c85092ff2430be178ebc0979e1603f1f165e5bee5cfcd13d1444b` |
| только 1.6 | `Swords_B/entities/explode.json` | `70a12edf4e34c52962583ad22f1fdae81642b4e28cc9f293deb4dbf2444c56c1` | `—` |
| только 2.8.14 | `Swords_B/entities/fake_fireball.json` | `—` | `4d93bad26e3611c3bed8977a063050adcf470c5b3688e9d21e24f2be158d9909` |
| изменён | `Swords_B/entities/fire.json` | `0bf9df5ff679d137ba58e90f1a7c8fb928a5c52ed8d57188fd95c71c25897eb7` | `03b9901161f0f36f1171b5ce8a9998a0f7253d83aab2f2cae32afc1b93600d70` |
| только 2.8.14 | `Swords_B/entities/fireball.json` | `—` | `ad8f0a90f96f0b84969bb92f11d607b5a525d688334cd6dc6433f317f619a5d8` |
| только 2.8.14 | `Swords_B/entities/ghast.json` | `—` | `786209e5dd0a1c347792ade5ae7ef8b911c2ef18284c820d625b1cb9f393ba70` |
| только 2.8.14 | `Swords_B/entities/ghost.json` | `—` | `fd18b65668fd677dddc43131e9a3bb97b8ffa7edb1b09b3c946b4ef8584b3a5c` |
| только 2.8.14 | `Swords_B/entities/ghost_projectile.json` | `—` | `13383fa1abb962ad08d4dfd7e22382d909c521de41eae18c3026f9dac3800f64` |
| только 1.6 | `Swords_B/entities/glowstone_sword.json` | `049d1ec6bc5dd4a4f04112d03a9ebfc545c062552690f8453aeffdcb18525ea2` | `—` |
| изменён | `Swords_B/entities/grass.json` | `eb58f97bad441fa77ddf3e3dc43f3b70f8ff138315d0cc87628683893bd29f77` | `909a377d533e0d1b1a769b2a16d1732694b35b08677bf48dda9222bf86dc8b72` |
| только 2.8.14 | `Swords_B/entities/grows_crop.json` | `—` | `2fd420a23f825a23ae2eb46f93930e64276d66a96b4da599e49b305226d1bc37` |
| только 1.6 | `Swords_B/entities/ice.json` | `c8036382b285cbc08905836432c6f7bb643845c0878466062d21569d3e7dec06` | `—` |
| только 2.8.14 | `Swords_B/entities/instant_creeper_explode.json` | `—` | `a963162a9843b98ce4c125d926a201e7cda076b2cb0a6470b231021c756a9feb` |
| только 2.8.14 | `Swords_B/entities/instant_giant_explode.json` | `—` | `936294619208bc568d3471f40803a595fee0b558b10a6462bd193d6db13a7037` |
| только 2.8.14 | `Swords_B/entities/item.json` | `—` | `e9a6312da65f1b1c7a786a15319986c65220b3ee900bbc58f732e14fe7265e59` |
| только 1.6 | `Swords_B/entities/jungle.json` | `8699019e63e90032ad975a16912b0450e68645d356bc08c71be885e2ceea3eee` | `—` |
| только 1.6 | `Swords_B/entities/lapis.json` | `3c5660ce6e5cc333e6d02fb02cb489eca57b6c26d5c40fa985a9714006881829` | `—` |
| только 1.6 | `Swords_B/entities/lightning.json` | `96253c00df6448cad164a66f8319dcf74c78b31e296ae902ae7a0b40ed9d96bb` | `—` |
| только 2.8.14 | `Swords_B/entities/lightning_bolt.json` | `—` | `73e4672ff27f2df2fa77b8c37d9e11345b1e48de0119c6272f5801bd59d60e6f` |
| только 2.8.14 | `Swords_B/entities/lightning_projectile.json` | `—` | `3e61e192e36707f20dc9b30acf03ecc2156b3440920c5b8bca7d39397fe03d9a` |
| только 2.8.14 | `Swords_B/entities/living_flame.json` | `—` | `d395f611e209b6547502e32c9b8ae438573a3982cb604e6890258dfe19743f72` |
| только 1.6 | `Swords_B/entities/magma.json` | `240a6fbf0267835f396dc589715d9bf97ad137d292fda7e4262a2e3ae1b5ddcf` | `—` |
| только 2.8.14 | `Swords_B/entities/mountable_slime.json` | `—` | `febd363c6f496640235087e02243c10bb617d83fd1e89c096063da94dc5c4efe` |
| только 2.8.14 | `Swords_B/entities/nether_star_projectile.json` | `—` | `8dd81910d2e6b35e72d0c764784e152b011cb3900dc9b365e6fa97ac967a59e6` |
| только 1.6 | `Swords_B/entities/normal.json` | `5c048bf452a456606c52eb8b5e0dea05950b72761a74feee40f3375ab5c03df1` | `—` |
| только 2.8.14 | `Swords_B/entities/objective.json` | `—` | `8ddd0e1bc53fe07ce4d33c894b295825f6791d703435fd31523e95565cf0ce61` |
| только 1.6 | `Swords_B/entities/obsidian.json` | `cbf8824d97b658f7c6d5b5b1ff2b13df98f4e369248413b516e3e684fa45ed93` | `—` |
| только 2.8.14 | `Swords_B/entities/parrot.json` | `—` | `92d8f706f3f853eb01913a34ade0ae588a9c24aa00bd50ce2c8c113d26585572` |
| изменён | `Swords_B/entities/player.json` | `ec003a118515a8ef9ae5fa3222fe9a618d06a887e24aee4467a0e0c5d908857f` | `d25d5fe1e885ef35c4027cc25290950b814b96e48a3a211b87bdabc77df2000f` |
| только 2.8.14 | `Swords_B/entities/pumpkin_projectile.json` | `—` | `a0a12b01aa40a650458d4d0aa298390cb66dc8068c3f34c22f238d65cac47f26` |
| только 1.6 | `Swords_B/entities/sea.json` | `560fb598c0e7d8054deb48ef5474fe3ab7039c1c559a9cd7dbf983f2de1f3739` | `—` |
| только 1.6 | `Swords_B/entities/shulker.json` | `7b51cd6c21a36fea61b0a75dcbc42800d18d51a9ea69d91229e4a2ec45d89bf1` | `—` |
| только 1.6 | `Swords_B/entities/shulker2.json` | `35e0c4668646971975258c814eadf709632d97ecc42abf05e01cf702baae0762` | `—` |
| только 2.8.14 | `Swords_B/entities/shulker_bullet.json` | `—` | `a3ab0cf6f6647883d9ca311213bc5526a0850b2dc7f3d540cae5206720b7f713` |
| только 2.8.14 | `Swords_B/entities/shulker_shield.json` | `—` | `5beef4dbb1907e5f436753427bd1212a1b905e0c2650dd3ce90a563e821f4961` |
| только 2.8.14 | `Swords_B/entities/skeleton.json` | `—` | `b6640a992aac64bf1d99b42660196096ab6fb55c55f6f387cea3bdcd1c84ef06` |
| только 1.6 | `Swords_B/entities/slime.json` | `d7b716a07e58fa776d81bd85ba9fb1f2856d4e643b80a1698440a738fbc7b715` | `—` |
| только 2.8.14 | `Swords_B/entities/slime_damage.json` | `—` | `eb9b9451f73e380a69d8f99bddd7a146a89bf642aef06975c27c01e7d8267eaa` |
| только 2.8.14 | `Swords_B/entities/slime_king.json` | `—` | `3660aa4782ca9f1a5d13da5dc2df3ea01ab24d4c1c23f06289676f7556715df8` |
| только 2.8.14 | `Swords_B/entities/small_fireball.json` | `—` | `38d90e0cfee37feec5af7151ac6caf3e8a53d749c0ce7fa2db9f067a2c425fa2` |
| только 2.8.14 | `Swords_B/entities/snowball.json` | `—` | `a056fbb54f02aed5f76680b97ee4eca04ad31aa5ea4b20d9d6c3913f6b662419` |
| только 1.6 | `Swords_B/entities/spectral.json` | `6d01460d2f7543ea3881cc336aa003260cf5fc587a62f61e359bb86f20ea17fb` | `—` |
| изменён | `Swords_B/entities/spider.json` | `80c1124f464f99ce675bedf8f89eb84984b750aad3c88a42e41742f2d1e35ec2` | `0df1f88a3415b607ea4625f2baa60afedeec77cddcfc60c9f63c7952dbe81fbf` |
| только 1.6 | `Swords_B/entities/sponge.json` | `66cefe863fdc7664d6d1fdbec19e3fe287a3b3e233c5e11900f672391f34d6c0` | `—` |
| только 1.6 | `Swords_B/entities/time.json` | `cb9336dbeff4bae1a4f3428392d2da79199b08f37154b4472e2dd8c8769a2c1f` | `—` |
| только 2.8.14 | `Swords_B/entities/tnt.json` | `—` | `3e0474e699f9f4ed9568c119cec2a0eefa18dcc1d01bf003e2ddc8b0c900a0ac` |
| только 1.6 | `Swords_B/entities/tnt_sword.json` | `19ce64450d32318ec3b27f5ef0735642c23a4e73a8e3a0a1ccfd2e1e876fd2f2` | `—` |
| только 2.8.14 | `Swords_B/entities/ultra_instinct_explode.json` | `—` | `27630043d62b3abdf14ad8c4e50c697f06b4c8e20aaf0b0bee2ce29251e45764` |
| только 2.8.14 | `Swords_B/entities/ultra_instinct_projectile.json` | `—` | `b622ef15d31127d91fbe41b55e00892539bc8aa70059919d98730bb02fcea887` |
| только 2.8.14 | `Swords_B/entities/web.json` | `—` | `ced0db9835d5f74852aef609c142598a375f2a885975d76b44f9987ad40e3edc` |
| только 2.8.14 | `Swords_B/entities/witch.json` | `—` | `5bcd147fbfd09b1cb42524fb08c90b7015049c9f1552a82670604e856c07d483` |
| только 2.8.14 | `Swords_B/entities/wither.json` | `—` | `b3afc7ea8512e055a372222a92e0de1f49107f7c75d9b5a2eb78b7cae09e8e94` |
| только 2.8.14 | `Swords_B/entities/wither_effect.json` | `—` | `dcd2c907c6514c016d427e6607755d028e6c86a4c0e07c79811ab970044192dd` |
| только 1.6 | `Swords_B/entities/wither_s.json` | `d680de22e5a95948ba5bc35c55dfd3b609b1d386fdb4e8ae38d1f9508bd9c120` | `—` |
| только 2.8.14 | `Swords_B/entities/wither_skull.json` | `—` | `ee3700ff1616bab7b4ed06195f2e75a7b4d8b20739328508380d8fad144e9ae5` |
| только 2.8.14 | `Swords_B/entities/wither_skull_dangerous.json` | `—` | `76f634aa2ef9c88ff6a7f1a14ec19b16eaecad23dbfdb4b38d790ea441114ca7` |
| только 2.8.14 | `Swords_B/entities/wolf.json` | `—` | `03caf1ef629458d090f9517820bf3218cf43694289782394e51dcbe13ee4d060` |
| только 2.8.14 | `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/jungle_sword.mcfunction` | `—` | `71fe36e10d77c5b8a55da101b36c9b06b9c7cca0e0e39fedbe030994a40d37d4` |
| только 2.8.14 | `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/tag_swords.mcfunction` | `—` | `4a03e64a5bbe2feb1038c3b2d8098d135abb37d70a6abe96046897da190e01d9` |
| только 2.8.14 | `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/tellraw1.mcfunction` | `—` | `0ee5960d0d6e4abbe2c460a74178b6309ef722d5f0a4261b4f7fa57c93ce63e4` |
| изменён | `Swords_B/functions/give.mcfunction` | `0dcf0acb17c76d9037cd0548da421033160f88bc897110e7b7fd5b4c2f743611` | `96b986ada305296f48142331386b6bbcd4e81bc3443521ba69fa81d490378de2` |
| только 1.6 | `Swords_B/functions/normal.mcfunction` | `b3b3889f0854cca24e1636087ca6ed6e865fa9a10263398f5a45a8cf3372ab8f` | `—` |
| только 1.6 | `Swords_B/functions/normalft.mcfunction` | `5463f2e761b48231421cecf265949bc22f15487d778bccfdcd4585a1504b9d52` | `—` |
| только 1.6 | `Swords_B/items/Sword of Time.json` | `0d7d50e3e244451bf86231f53daccb272a8ced2e39f10a2cd86016cb98c1e5c6` | `—` |
| только 2.8.14 | `Swords_B/items/bedrock_stick.json` | `—` | `ad3f156bc518c2ac0b7413ac1162d0ab4d4dae50857ce21e53d28130fdf8bb42` |
| только 2.8.14 | `Swords_B/items/bedrock_sword.json` | `—` | `62a2c3dd478c579a782647ea247aac8db02a825bea8de2046e1576ca6b68c6bc` |
| только 2.8.14 | `Swords_B/items/bee_sword.json` | `—` | `43a8a4640b9b107ae319cb6b1541a1af57f922e758c2d23c51436599354f5358` |
| изменён | `Swords_B/items/blaze_sword.json` | `5d057adf473997f9ecc6f3431ad60c5a8d47d7f7b119cba19423beb0e420fb86` | `5f942370498d9127c2fa6fad90d8162f9f8698e3cd831e4eb2b3463e9a9e9c8f` |
| изменён | `Swords_B/items/bone_sword.json` | `0d8e6f5cbca037defd2e13b1c9c42d45fc71206986968f649ac5aada7dd5aa2a` | `5e3664d27b910c1bbc6fd6ce2ad2124a4083edbfe5e50d4ebd6240c3134e0f25` |
| изменён | `Swords_B/items/cactus_sword.json` | `7519a467e9a6bca214146084f540aeae7bd5e615c9fcc69671df8b7b2a647d08` | `62bfcf5493504c659fe44cfac278cec670969c6ed773e15d8fb57925867d7d75` |
| только 2.8.14 | `Swords_B/items/clock_sword.json` | `—` | `3fe00db7658133db6ffe8d9dbfe123deee0ce7c881288b91cad350bc01dfbaf0` |
| изменён | `Swords_B/items/coal_sword.json` | `cff7144b2ec0887b717a2cea016b5e0d7e01e16bc59392790f371e3fdcb0e154` | `c012b481b9489040352bad877b28881c8e3bbf4d60bd8a8fa1b9ba23d76f190a` |
| изменён | `Swords_B/items/creeper_sword.json` | `293044b9bfe760e4a19230b96f7d2c10becc057bac01ea4977c20fbc96aa657e` | `72a8d7809427580780a7e89c0c3ebf4b6c0ce133ce6b34dfbe258732b844171d` |
| изменён | `Swords_B/items/emerald_sword.json` | `3975d125aec66f6f337857b7d8ca64912c1ed5da21fca20a3b0e3b0242ba6e14` | `bf57a74d7e3b96a81fed925d555e0bc2361fcc4b3b09888f4afe2166b8fdd87f` |
| изменён | `Swords_B/items/ender_sword.json` | `422c200a30438e242989184afe9125a6844c40e051f2c4106bf97eb3e75abb6f` | `09cd905c1bca9a986f2aba869729bea80b507735e8e0060208ddb600770baa6e` |
| изменён | `Swords_B/items/fire_sword.json` | `83cead635f8f3a01d907bb3621013b202a9af531ca681d990d13a231eccd217d` | `32b7f838da26a1dfcd9bdd7a4c22ecf04752f8b3fcb98cd29b14d6aaf1bcb4e7` |
| только 2.8.14 | `Swords_B/items/ghost_sword.json` | `—` | `8e96fa7ce0fbc799eb16d02cff185e708679216c582e1753f222f2d8c8a50bbb` |
| только 2.8.14 | `Swords_B/items/glass_sword.json` | `—` | `ae25a6492a95416b81465a8dfaf46b71bdbdd1e48e141c9688d03132f9bc921b` |
| изменён | `Swords_B/items/glowstone_sword.json` | `d842cef41c32551f6d446777238eeed87e8ff3446b72d6e640d537b6e9276909` | `60234df9cc8e8512b42329aa5ba3909f841bf7a011524e63c3d2fd53c8543b8e` |
| изменён | `Swords_B/items/grass_sword.json` | `5f45d8ed526d6b56d3476e8decc476e259d672bda74d8c8fd1a754fd1a662ce2` | `8c6168c595fca5ddebd7c2b87af28b42d672770902ef5d052b26f790a1e1f4c5` |
| изменён | `Swords_B/items/ice_sword.json` | `5ab1e4158f5615619f408bdd127cb33f76d2113dbf66f31a5ee1369cf9f301f3` | `809dd3dfe17e45a18475f58039395a57453c0cf8579394d1a6811e7578abbe4d` |
| изменён | `Swords_B/items/jungle_sword.json` | `7fd7669b9d3592f062facc4f76b930fa03171661175ba568ba9fe351f78e30a7` | `aff6656be773e68fea110dd113b4329023ead2b49d50b870689bf6722d5c3953` |
| изменён | `Swords_B/items/lapis_sword.json` | `2eefa35cd3e4795550d2b8ce5993d969bbba208143530b9894a6143883fe62b7` | `ad569e2e5fb3b0519a679139561bef7f4b6e92191fdd0523fc04fc78c6ec8798` |
| изменён | `Swords_B/items/lightning_sword.json` | `f9c6a78df9afa4d71ff4703f383be6069a5fcd7e3015cbdd049e43700912d17d` | `c9f2ef3b7f8c867b256d02311bc442c9d7fb38c08f7de6e91776e15b3ca91718` |
| изменён | `Swords_B/items/magma_sword.json` | `18176559789436b7a591d9a74519dfb0c8131f9e48e195899a84f844778d7ceb` | `fadeb7acf7bb5aec2b38332b46fdd35b9bbf11ac35d9ed1de41a1b768f973ab2` |
| только 2.8.14 | `Swords_B/items/nether_star_sword.json` | `—` | `4f3f7a93645eb4812da3bb8741cd0f21e6de65320e49c1c1ea4a30b6c90093bd` |
| изменён | `Swords_B/items/obsidian_sword.json` | `a2295776429edfbcce70d69784d6d5d3697167d9022b531a460ea4528c197277` | `40bd0b764e8a4f7b8de70a423c0974b731404b926e062db6883b05707ad2f5a2` |
| только 2.8.14 | `Swords_B/items/pumpkin_sword.json` | `—` | `a04c741f7a7714909d51014986af097fa8913dda093e9bd9e29d6ab406b308f1` |
| только 2.8.14 | `Swords_B/items/quartz_diamond.json` | `—` | `ff16936932b23965ca1cfd8ff78d0b7bc83c079444b91851110b65a285cf5032` |
| только 2.8.14 | `Swords_B/items/quartz_diamond_stick.json` | `—` | `213f6eb1298d0ac78d9586c272c3a84e8c351267a393bd4465c53426bc108724` |
| изменён | `Swords_B/items/quartz_sword.json` | `4141c3d2c4a85ed3e0dbfd338a16a8ff915a7ea577760e1bf8b5ecf4e14feaff` | `7bea756962f987bf109ee8647d72f64515556b6667780a0b59eaeae80ed7ace4` |
| изменён | `Swords_B/items/sea_sword.json` | `1b518f32c3c9ef658f5c17fbd58e173c10ecc5d683f2ae6417aae7721f730134` | `49fc78e882bb620e73487911c97d5111a04c58fbb99299d62a293ba4aeff6003` |
| изменён | `Swords_B/items/shulker_sword.json` | `13257472420959437943389f4da668b21229dc652b44a12fff34000730279988` | `084db74595975c07351e92309db5f6c175e5e4c7026a96f41d861f00bdc07cd3` |
| только 2.8.14 | `Swords_B/items/silver_ingot.json` | `—` | `aba76c12ec13fbfecaecc06eaf60016922b1e83eda4b4f6a5fd37632d638b83c` |
| только 2.8.14 | `Swords_B/items/silver_sword.json` | `—` | `106c52b49a6f7ec4e2ec9b57b652609f3ae17c31776e312b313f70fb82a6f55f` |
| изменён | `Swords_B/items/slime_sword.json` | `d961c121baa889eccff38774af4c243ddf5a53f7e25f91485f6638d8403a1cab` | `41c671649c7e20de61bdc8cb1dd29126e45d892b9fd12a5182f02a9f5bd9625e` |
| изменён | `Swords_B/items/spectral_sword.json` | `9e4889ed5608b7cdca29fa3cc5ca42691152511b1ae70d769fa33b392005bd33` | `51170151c3acb1e8eda5fd47bd23d2e7dc02c24e7304877500efe867006f9424` |
| изменён | `Swords_B/items/spider_sword.json` | `d0674a6986cd2374c5029a2173adf7749859d5ed98b55cad13f8652f45e82611` | `eb69b93549f10dffd8d1691b07eb65205081a40e13c6e291018b3736036027a3` |
| изменён | `Swords_B/items/sponge_sword.json` | `97af532d599397f0dc540e015ff6114b20abeb604f5093f6a65ea354185c45c1` | `b3bef1c1347eb355373624b129a21bb2e76acb4d0a078e48ee67440bf2aae434` |
| только 2.8.14 | `Swords_B/items/time_sword.json` | `—` | `1ef69771c6d2b5bf060871481f24b53de2aa7f60c7404084294b390c97294822` |
| изменён | `Swords_B/items/tnt_sword.json` | `5cb16bbd5d198a61541b9495540bf88856f53e0adfa1b388d85b387ea9529d73` | `206d1fcf4240b203e0adf2eeafd7a404da56bbd134f5ef74ad15fafca76dd51d` |
| только 2.8.14 | `Swords_B/items/ultra_instinct_sword.json` | `—` | `a033da705467f5ea9051ef7320ae9c9bd04432b42d2b831744e0473dc3189dea` |
| только 2.8.14 | `Swords_B/items/wet_sponge_sword.json` | `—` | `bc13721133e1b5dd4fee294f4e616ae615e918e052bed4c9644e62e486463c6b` |
| только 2.8.14 | `Swords_B/items/wither_skeleton_sword.json` | `—` | `2785b757ada081e3ee2e6bfabb38890a118d945dbf801ed6cace854aa17c143a` |
| изменён | `Swords_B/items/wither_sword.json` | `fed774cd8c3d74e0358c167b3240a908093c3e61c55c48c2d48591c0e4e8f056` | `7d0f14074dee6e1f2f9a1f9634cc5e9b9238458f030ada5fa87341542b689e7b` |
| только 2.8.14 | `Swords_B/items/wolf_sword.json` | `—` | `998b5902b7fde8b0ec23eff6c09bfabb1f3890ec545ec43b58b731332dcb8d08` |
| только 2.8.14 | `Swords_B/loot_tables/bee_sword.json` | `—` | `f3cd7ee19c8b21556df4ff1ccbb9f815472ac82f82ef9381a9b8dbf3dee65e09` |
| только 2.8.14 | `Swords_B/loot_tables/blocks/quartz_diamond_block.json` | `—` | `454e0a66c68a3b795db0a3e4508067ec078acd12ff8c1454d1548e3ef3a9a593` |
| только 2.8.14 | `Swords_B/loot_tables/blocks/quartz_diamond_ore.json` | `—` | `0eadb3c138068bab884ebcb69da55d2441c29650929c80c74e45b8b8a1367405` |
| только 2.8.14 | `Swords_B/loot_tables/blocks/silver_ore.json` | `—` | `4a4b479301a9e12054739395ab3b2d3774076274926cdc45011cc2a76c5972f3` |
| только 2.8.14 | `Swords_B/loot_tables/chests/abandoned_mineshaft.json` | `—` | `fdce88876b62f2ba9dce2e544df7bc0edad50f3793b357000416d536f0a6fa94` |
| только 2.8.14 | `Swords_B/loot_tables/chests/buriedtreasure.json` | `—` | `be6b5480ced6a762aaa553cd63361848a64c0e4e01ca85d16f1a57aa027ffb7f` |
| только 2.8.14 | `Swords_B/loot_tables/chests/desert_pyramid.json` | `—` | `62dbed4c7083aee0863fc97ded6fb00fc6510b69a75721cb9320be41e89b92a3` |
| только 2.8.14 | `Swords_B/loot_tables/chests/dispenser_trap.json` | `—` | `b00e80c580d726851b6f12b518115aabdbd6eefee95010aaa5b90f6acfc85ee9` |
| только 2.8.14 | `Swords_B/loot_tables/chests/end_city_treasure.json` | `—` | `923422e7d419edfd97abfb608ea0962671eb7d02529c32ba4a522904ad5f8bac` |
| только 2.8.14 | `Swords_B/loot_tables/chests/igloo_chest.json` | `—` | `0e4e2cc4f566213b80753df3aa62c16126a98952a6796181c12d6d291815856e` |
| только 2.8.14 | `Swords_B/loot_tables/chests/jungle_temple.json` | `—` | `457065c0f039f716836b183eb083ff9e11bbec9b4391845912f93d20bf01faa0` |
| только 2.8.14 | `Swords_B/loot_tables/chests/monster_room.json` | `—` | `0464e063612ee7c07b03af893aa1cd0185e2142438a8b7bdc9a05eb477f97d97` |
| только 2.8.14 | `Swords_B/loot_tables/chests/nether_bridge.json` | `—` | `df8f5bf18a1d250e005b6b50a1ead25ca910f77ef3a8718cc6e21091ccae6496` |
| только 2.8.14 | `Swords_B/loot_tables/chests/pillager_outpost.json` | `—` | `0f3d58e0cbef851cb3ab7b4c5d85155a377c0126a66e569b08d6bdddedc1a5ef` |
| только 2.8.14 | `Swords_B/loot_tables/chests/shipwreck.json` | `—` | `ecd31113fa81adb02ba7fa8fb8ad44dcfd054d7f62a221dd0fab4bd09bc06867` |
| только 2.8.14 | `Swords_B/loot_tables/chests/shipwrecksupply.json` | `—` | `f4feb668018a8fd2a822370b7a695368c501c1e037d5b50c7413864ea858d1ad` |
| только 2.8.14 | `Swords_B/loot_tables/chests/shipwrecktreasure.json` | `—` | `95a6849f1217fbfacf0e55b14450442a74c1a37246458d6cf1a5b8e6c69df577` |
| только 2.8.14 | `Swords_B/loot_tables/chests/simple_dungeon.json` | `—` | `75ccfd1f679f4559858cfe369edfd94ac3f7dd8a7a08e161c4f67cc131e15cd5` |
| только 2.8.14 | `Swords_B/loot_tables/chests/spawn_bonus_chest.json` | `—` | `5b722029757f4510eea6b6da7872aa1076c5d3e425b69a6e81b058cc37ca0d02` |
| только 2.8.14 | `Swords_B/loot_tables/chests/stronghold_corridor.json` | `—` | `436e02e55d15d846c3726cb9b705d88166621cfe9d2d2cad568aa0da705b7642` |
| только 2.8.14 | `Swords_B/loot_tables/chests/stronghold_crossing.json` | `—` | `242d4a3e0e7e1d2d468347d20c8d744724c0a85dc7ad4eca2c4d4c0893597c17` |
| только 2.8.14 | `Swords_B/loot_tables/chests/stronghold_library.json` | `—` | `e8e52b4b31861a806b666a0b34816c7f464dc1858262d9ebd744fcc8836f6d3d` |
| только 2.8.14 | `Swords_B/loot_tables/chests/underwater_ruin_big.json` | `—` | `113741262d5adc8cc4c3f1cef22e880181c732810a8f5b0a40bb42dc2a412cc6` |
| только 2.8.14 | `Swords_B/loot_tables/chests/underwater_ruin_small.json` | `—` | `a1d981aebd86ec13315023d5a784cdf829f53eef4093361ed59011d51040c483` |
| только 2.8.14 | `Swords_B/loot_tables/chests/village/village_armorer.json` | `—` | `91ca254202084298b3ecc4ba1d9c333c7d95550347b5290ac1ff1db0a7263a6f` |
| только 2.8.14 | `Swords_B/loot_tables/chests/village/village_butcher.json` | `—` | `14280461d0ddabc4839d13de13175734ea6d9930dfa87c8bbbcc24fd2186e383` |
| только 2.8.14 | `Swords_B/loot_tables/chests/village/village_cartographer.json` | `—` | `c358d7277ab80014ae97e3472011a6c739e6f7ce74cf7efe7560c06701935103` |
| только 2.8.14 | `Swords_B/loot_tables/chests/village/village_desert_house.json` | `—` | `871fdba4af6458549045fbb19896d27b1712bf2d6518a700ead484b8dc61d099` |
| только 2.8.14 | `Swords_B/loot_tables/chests/village/village_fletcher.json` | `—` | `98ee5d5370f4346dd69432858b3d5a3b59461f2f1019760f7968d96cc2b6acc4` |
| только 2.8.14 | `Swords_B/loot_tables/chests/village/village_mason.json` | `—` | `6fc7f1c2debee9c706ad1798256ea833d2aaed4d5dadc1b2d49383dcaaa004b8` |
| только 2.8.14 | `Swords_B/loot_tables/chests/village/village_plains_house.json` | `—` | `afca426280d77472ab8df1c61b08b7905092a0e1c7541fb74e795e0ce9ee7fbd` |
| только 2.8.14 | `Swords_B/loot_tables/chests/village/village_savanna_house.json` | `—` | `0b5931fdc6298383c89e1959e6b7c74088943f1c92a191c65a3729b2db51f9d5` |
| только 2.8.14 | `Swords_B/loot_tables/chests/village/village_shepherd.json` | `—` | `ba6d314f6abd18f5d03afdfec45a8aab0909655692b64e72a85018ff7d53f964` |
| только 2.8.14 | `Swords_B/loot_tables/chests/village/village_snowy_house.json` | `—` | `5f631d0acedc39681f943d6cbe6ed03a54c3a220af3554ab5545382775e93a4c` |
| только 2.8.14 | `Swords_B/loot_tables/chests/village/village_taiga_house.json` | `—` | `36229a16d760222deaabc52ff451c4970ae96737ec13597b233bc2331277af14` |
| только 2.8.14 | `Swords_B/loot_tables/chests/village/village_tannery.json` | `—` | `8b707fa58f8c02b75b8d57ee18a818acab514cf2774e61b6e956dee5274e3510` |
| только 2.8.14 | `Swords_B/loot_tables/chests/village/village_temple.json` | `—` | `feeca103da426924bef79ff65f4fe2ec8f206ff527a6e34854b8a8b657ec10cf` |
| только 2.8.14 | `Swords_B/loot_tables/chests/village/village_toolsmith.json` | `—` | `0701d9bbcae2b79c7e661462ba4cf3ab5b49395c17c2a5c62fa5f7d1e597328c` |
| только 2.8.14 | `Swords_B/loot_tables/chests/village/village_weaponsmith.json` | `—` | `b83c57c57a4b24bb2dd0ed3e8f9276aa5b69d19cd43f2afcbe2e25158b8e1e3c` |
| только 2.8.14 | `Swords_B/loot_tables/chests/village_blacksmith.json` | `—` | `6263ec2bfc90785fcb71e1581f2b3b2fd586085748f9daf400b4ade258b4665f` |
| только 2.8.14 | `Swords_B/loot_tables/chests/village_two_room_house.json` | `—` | `d9c279534371a7bd72f9749cac0b28f41c79146a625e9285fc68f917f7bdf88c` |
| только 2.8.14 | `Swords_B/loot_tables/chests/woodland_mansion.json` | `—` | `02a72468bdf568a92c857631940d78f467841a02bb3ea09868c0d99ef002eb63` |
| только 2.8.14 | `Swords_B/loot_tables/empty.json` | `—` | `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` |
| только 2.8.14 | `Swords_B/loot_tables/entities/blaze.json` | `—` | `4a3aa8badbc60aed981951f1d7580362a98bfe57fb02cf39e13bea913a4f4d38` |
| только 2.8.14 | `Swords_B/loot_tables/entities/creeper.json` | `—` | `8bf2f83cf7290a765ea31eb2bda560e3fb879e33d7b6c19847f6fb01861246aa` |
| только 2.8.14 | `Swords_B/loot_tables/entities/elder_guardian.json` | `—` | `d4c4c9380d598ce9c87f8b6e6006ca2856103bd450f34607c254470d781547a1` |
| только 2.8.14 | `Swords_B/loot_tables/entities/living_flame.json` | `—` | `4ff5433c132e0b031e91dfbf0bb198f1cd66228900fff213dd037936f2524071` |
| только 2.8.14 | `Swords_B/loot_tables/entities/red_enderman.json` | `—` | `6562e9062808f24425d711104cfb7f729c8224839b2f0d26f44b4bf8ac5b4098` |
| только 2.8.14 | `Swords_B/loot_tables/entities/shulker.json` | `—` | `f68cd2a30a473a605fd04aa4ec81c592f098a882e8a32eabe54feca78a6e7aae` |
| только 2.8.14 | `Swords_B/loot_tables/entities/slime_king.json` | `—` | `db0c31c48aa9b9f1978d9e89ad94370423ccbcd3d080df5635663399f4006c40` |
| только 2.8.14 | `Swords_B/loot_tables/entities/wither_skeleton.json` | `—` | `27e3a5a47848d48de7d72acfab193587d8886b47f087d6214f09c39eeb7526c6` |
| только 2.8.14 | `Swords_B/loot_tables/gameplay/entities/mooshroom_milking.json` | `—` | `ac6235b5017663111487fb45b9c0bf3e6fed109e8d53d0b242c3abc89c781d6b` |
| только 2.8.14 | `Swords_B/loot_tables/gameplay/fishing.json` | `—` | `a1e2c8c05cb7279d8965842060f6c84f067d72d63f72d5d03fd25c193e81203c` |
| только 2.8.14 | `Swords_B/loot_tables/gameplay/fishing/fish.json` | `—` | `0594621d6702c8bb78517b91f79334b79a2e0482efbe81339f044b9090baf568` |
| только 2.8.14 | `Swords_B/loot_tables/gameplay/fishing/jungle_fish.json` | `—` | `ffad35a982ac74cd08fa06c392266291de0d7ee3987676ee393897fedf32a39b` |
| только 2.8.14 | `Swords_B/loot_tables/gameplay/fishing/jungle_junk.json` | `—` | `24813f4d507f35ddc082725cf70c1c95f376c01849ffad2d9b94cec65dddacae` |
| только 2.8.14 | `Swords_B/loot_tables/gameplay/fishing/junk.json` | `—` | `0b51f94ee4ee46df16a6463767dbe957ef092bca138d33b5d0a74ebb7a760712` |
| только 2.8.14 | `Swords_B/loot_tables/gameplay/fishing/treasure.json` | `—` | `0459bb92fd47cab5f10e8c514d7b262854d8dab31c7b2efc1af13d839cae568e` |
| только 2.8.14 | `Swords_B/loot_tables/gameplay/jungle_fishing.json` | `—` | `296ef031d0f85409014f7c9908f0cf9368896313cfcac24ef91d108d6fcc8a72` |
| только 2.8.14 | `Swords_B/loot_tables/pumpkin_sword.json` | `—` | `d7ab4891c7151f23630ceb1cd03f9b82e842e2fece5b59c9d9fbe38dfa1a7c3a` |
| изменён | `Swords_B/manifest.json` | `37aa71529c2d64a381e1b056a526f9fcdc35e072df56b5d02e3370ecfdbab695` | `b85029ad07cd7c4b22ba6b80e4a63a2e27e7c86556bb8523119abd44e90f3491` |
| изменён | `Swords_B/pack_icon.png` | `434eacaaec8642bb534262bf727502b81d7bba1bc760ffa3baedf25bb17b2812` | `1d1faeae22cbb8db31db1380c25dfeb4b68ca649f6cc72bd974720823152bec3` |
| только 1.6 | `Swords_B/recipes/Sword_of_Time.json` | `74e551f158aad246f96ec39e194705a384e59a1944d21228a03e5d4acfc52020` | `—` |
| только 2.8.14 | `Swords_B/recipes/bedrock_stick.json` | `—` | `a3fbdeaf2ae02b6089e457ddee631d70ab463641a6914c93d9c869f5eab19168` |
| только 2.8.14 | `Swords_B/recipes/bedrock_sword.json` | `—` | `a6cf704f6ecc5300a9f7bf56e0c0a33aa70b0991083f5652a7e741b844ec47c3` |
| только 1.6 | `Swords_B/recipes/blaze_sword.json` | `fdbb3333b70d5b35570ea4d69f049687d0b1c8e9f5f57a41cbc77396de13bb47` | `—` |
| только 1.6 | `Swords_B/recipes/bone_sword.json` | `f071cf49ad71f7c1a793a1884c1678e9c1f2f0f4e173176f17b2ade33a36d03e` | `—` |
| только 2.8.14 | `Swords_B/recipes/clock_sword.json` | `—` | `9f6d3f2bf0ba1c89cb62da6ceb027fdacf92dc13572967c82d30d78e6fd62ec5` |
| только 1.6 | `Swords_B/recipes/creeper_sword.json` | `690b171622fd6545c630e1c104f43832d51f8db30c7b9ba1dad5aacaeb59ba89` | `—` |
| только 1.6 | `Swords_B/recipes/emerald sword.json` | `3eac878dfa531262cc12eebc82f10fd48fa48c09625a2c72677c381a551fc3de` | `—` |
| только 1.6 | `Swords_B/recipes/ender_sword.json` | `a387a9edb3ebc194ce2d49d4e3cfa63778d6fa8ac0a5583823786c144c59e597` | `—` |
| изменён | `Swords_B/recipes/fire_sword.json` | `40d31bf6b57e17bd4d18dc0494faa20c643283ed553cdbbe84a3dfce17b09dda` | `3272969d8234a2977de8a9f23a3536f487de6b7edef8e1040dad7813c64fc57a` |
| изменён | `Swords_B/recipes/glowstone_sword.json` | `3fb14439fba465ea17c63a8c6cc0e950e178d412df7ec71babe3493055b7d408` | `a1596ba72310a63b8bf100b12c818b43479fa88177b0e2677fd0e3b0b6620e62` |
| только 1.6 | `Swords_B/recipes/grass_sword.json` | `5dd0c93382fd713f847e344b6683e31ec226a39578c2998314fa2559036f3f5b` | `—` |
| только 1.6 | `Swords_B/recipes/ice_sword.json` | `863844eddf23319338c82087bf295e93ea9aac38d92cb0f374403d024c1f652e` | `—` |
| только 1.6 | `Swords_B/recipes/jungle_sword.json` | `c3fbce43dd7665dfde73be142b35a6e11064c2152aa9a8623e1013f95e84bb1d` | `—` |
| только 1.6 | `Swords_B/recipes/lapis_sword.json` | `e94beda185e6f1ff99d07b251f9f319845f4640977fffdf19436930f2c6ceae3` | `—` |
| только 1.6 | `Swords_B/recipes/lightning_sword.json` | `87ee8985909aa1851c6f506f4fd91a7b62355459c2bed5a90d8ae4ca38ac9716` | `—` |
| только 1.6 | `Swords_B/recipes/magma_sword.json` | `e2f67780759ff050cc4e7e0088c0fe89e121fcd6206b52de147b06c30e966c6a` | `—` |
| только 2.8.14 | `Swords_B/recipes/nether_star_sword.json` | `—` | `f09aab63bafb995f01d5d0687cc094f8f3d5f5940f7ba1182b25afe868be7f5b` |
| только 1.6 | `Swords_B/recipes/obsidian_sword.json` | `8f54907198f2799ff03817c56cf9a0958a8cc622162f0d093cf71afbe47e698f` | `—` |
| только 2.8.14 | `Swords_B/recipes/quartz_diamond_block.json` | `—` | `2c2d19d2433d8f8589d51f97e7604918c1555942222c7f03aa8bfdda06964b52` |
| только 2.8.14 | `Swords_B/recipes/quartz_diamond_stick.json` | `—` | `67eb173ad5bbf67c5918000d44e3d131ff43ee984dfdfeef430fdbab402daf1d` |
| только 2.8.14 | `Swords_B/recipes/quartz_diamond_sword.json` | `—` | `3a68d37b7572949ec23c0bf8ac3d5e05ddb3fed1c10d5c0cd2b20bfb85bffffd` |
| только 1.6 | `Swords_B/recipes/quartz_sword.json` | `7ce2c6e3a3443722188d28770467dc9bbb910dbfa5eac2c4faf7e27f28e55f03` | `—` |
| только 1.6 | `Swords_B/recipes/sea_sword.json` | `d769712aab0f0cb57a1f70f1602b19abdaae4a5bd7fe0b2aa635e32f416f1a74` | `—` |
| только 1.6 | `Swords_B/recipes/shulker_sword.json` | `06096203f9b00b7fad2bc5a69a2ebd4585b9fb29751bc65c05944d9aadc8e643` | `—` |
| только 2.8.14 | `Swords_B/recipes/silver_ingot.json` | `—` | `926e95c5167379ffd3664bddef7fa408e77a45217132e4a036ba816a8de6d588` |
| только 2.8.14 | `Swords_B/recipes/silver_sword.json` | `—` | `5b43faa8a1c063bb2dd87fc14414251aec35f276a562c42fdd75a77920dfb25b` |
| только 1.6 | `Swords_B/recipes/slime_sword.json` | `24b19ef73a5dc473b2b880bd5531e243b113277c884561176c79c0f8013a488c` | `—` |
| только 1.6 | `Swords_B/recipes/spectral_sword.json` | `badd3caa99b6e39de5685b25b1c4982d25c8689b43c32f6c031bd58320afdc5a` | `—` |
| только 1.6 | `Swords_B/recipes/spider_sword.json` | `4649f4bb4b07362aa56f8cd3769964a73235122e5a26b7cd047b0a60383380ec` | `—` |
| только 1.6 | `Swords_B/recipes/sponge_sword.json` | `bf095d6da33a323942fc8d619a56b4f513738330231f78ab1199426e94b427fd` | `—` |
| только 1.6 | `Swords_B/recipes/tnt_sword.json` | `10aa7c3438855e92011a8737cd211ae5c1324d9ba3f634aaddfd8d4516338163` | `—` |
| только 2.8.14 | `Swords_B/recipes/wet_sponge_sword.json` | `—` | `c98f9fad3ede6ea62682e733db139245ad3a350bd8ded6d854c093e68ab3c8de` |
| только 1.6 | `Swords_B/recipes/wither_sword.json` | `a0f19077b9f42931f8543fad850a0470f920d5a842144b065a47f812fe351cc0` | `—` |
| только 2.8.14 | `Swords_B/scripts/javascript.js` | `—` | `20ca25df1439d33395c80f697620b2eccac5dbed715c383d3ce05650ab93837b` |
| только 2.8.14 | `Swords_B/spawn_rules/alpha_wolf.json` | `—` | `0cbea71127b564fa0d6770a4607f2acb78aea59dcd457dbab182dfd30e7c09e6` |
| только 2.8.14 | `Swords_B/spawn_rules/ghost.json` | `—` | `112ccd21b6b834af038c08160ae0197b7564da665f7be1abd7cb56a5f671958b` |
| только 2.8.14 | `Swords_B/spawn_rules/living_flame.json` | `—` | `ce8ec59550ed8b9e0d4973ba7d04ff48c3bbab97eeae886378a796756ef89d03` |
| только 2.8.14 | `Swords_B/spawn_rules/slime_king.json` | `—` | `02125e6a2507a040cd7f76d3df5a6a037909bd4eeebdea0774c96d0503b6ccfe` |
| только 2.8.14 | `Swords_B/structures/armor stands swords.mcstructure` | `—` | `2738255459cb9f87abcd43d1f983050d0a3a46dddf699f428f5fdc563e62fe7a` |
| только 2.8.14 | `Swords_B/structures/bedrock_sword.mcstructure` | `—` | `14ae80aec8cbde5eeeb5802f77cae0e4cbf338d277af1510946bf11c079c3d97` |
| только 2.8.14 | `Swords_B/structures/bone_sword.mcstructure` | `—` | `f06d4150170ce46f09645260a2cc19865edebbb689d616102dc7ac8dc89592b3` |
| только 2.8.14 | `Swords_B/structures/creeper_sword.mcstructure` | `—` | `9e4f6a847837f92c24f3b9a9643b6254a7b1fee710d620dfe29dcf1f8d1eeb0a` |
| только 2.8.14 | `Swords_B/structures/fire_sword.mcstructure` | `—` | `be3526950e28b61ebe4814e880630478d8b8c6084d344eb8a107903681a78f89` |
| только 2.8.14 | `Swords_B/structures/ghost_sword.mcstructure` | `—` | `7bdb70032e43e8c4475c782da21ff6b60f9ef64d696aef5a1cf3efc8dc7591c7` |
| только 2.8.14 | `Swords_B/structures/glass_sword.mcstructure` | `—` | `a7b2145ffeda7605c71f117084ab11d52ab14d19f7cced4d21e4bfafcc7fb617` |
| только 2.8.14 | `Swords_B/structures/grass_sword.mcstructure` | `—` | `217d738c4a8f3071bd712bf35ba827e649e536e152278f8a5f00ebfbd7416a34` |
| только 2.8.14 | `Swords_B/structures/lightning_sword.mcstructure` | `—` | `632be5f2fa4dc526c9f73f8e53c831bfb2347bd812ef4e5bd6bb9f9b42733cee` |
| только 2.8.14 | `Swords_B/structures/obsidian_sword.mcstructure` | `—` | `77d1c64f704c07cef821b2059021248e0bb6c1ad8c5078663d94d16cf2d74f15` |
| только 2.8.14 | `Swords_B/structures/silver_ore.mcstructure` | `—` | `4a7a9f4c3f735431aa3c82d969d54ac03201c031c24799a16b6522c4e6e1f701` |
| только 2.8.14 | `Swords_B/structures/spectral_sword.mcstructure` | `—` | `77710d08327cdc2a14abe38ec14736f173b21e2223ea0716c6e44a7b3995c107` |
| только 2.8.14 | `Swords_B/structures/time_sword.mcstructure` | `—` | `c204e663c087940aaa9b05b097ac5386b5712d8bcbb349f4f4441a3687572d83` |
| только 2.8.14 | `Swords_B/structures/ultra_instinct_sword.mcstructure` | `—` | `e1aee9291e51f24fe965f12afbc8cd3685dcf5972268c23eb390e2064ce614e1` |
| только 2.8.14 | `Swords_B/structures/wet_sponge_sword.mcstructure` | `—` | `0176cf89b0ab3dfe3b8ff5a5ff148997e7467a788cdfa674d95e58ce7f1d6452` |
| только 2.8.14 | `Swords_B/structures/wither_sword.mcstructure` | `—` | `67ff65a8a1baf594519210244c89978a078b60911768b84e9568b5a6c7f985f2` |
| только 2.8.14 | `Swords_B/structures/wolf_sword.mcstructure` | `—` | `00361d97e4ab5190d45d9e6d7928dd78f018c0dd8ab2bbf7c72b683044469aeb` |
| только 2.8.14 | `Swords_R/animation_controllers/baby_slime.animation_controllers.json` | `—` | `410b806138f3f3bcbcb2f53e955c430bab5c22eb13ec82ab2fb80566f8342992` |
| только 2.8.14 | `Swords_R/animation_controllers/ghost.animation_controllers.json` | `—` | `76bcb560dd4c1deca4c82be7d82831275457c0397e2f1fa6facf9405016b6afe` |
| только 2.8.14 | `Swords_R/animation_controllers/grass.animation_controllers.json` | `—` | `921a672759fac15653073b92cf27ffbe24a9caa72a0d600d5dd05b332b5829d4` |
| только 2.8.14 | `Swords_R/animation_controllers/shulker_shield.animation_controllers.json` | `—` | `7b9bbd7305fe30545dfeda7178e82b06fa40ddef7fb0e4a5c72800d24ea728d9` |
| только 2.8.14 | `Swords_R/animation_controllers/ultra_instinct_projectile.animation_controllers.json` | `—` | `b351006f50b8ee5d8cc37f160b58a42c95aa1993f9bae7ce921acc3581dbf7e0` |
| только 2.8.14 | `Swords_R/animations/baby_slime.animation.json` | `—` | `2ff25c4c3e1cc11e634da947eea87aaf9f3f535570030f70497537e83f006084` |
| только 2.8.14 | `Swords_R/animations/blaze_rods.animation.json` | `—` | `25e5e97e44e19bfcaaf3666639f46aa8cbb26fce46ee20e277311f560c35b728` |
| только 2.8.14 | `Swords_R/animations/ghost.animation.json` | `—` | `d7da2dc5210566687929a27b2720938b7b0223d30e62fef45ffb299ad7b32e88` |
| только 2.8.14 | `Swords_R/animations/grass.animation.json` | `—` | `4649a576a7ef5d6191a41a3c736e6182c017ec9d5c0784f7161abfe1ab09a116` |
| только 2.8.14 | `Swords_R/animations/mermaid_player.animation.json` | `—` | `eb26e0a5bd9d5a94378c18b8c8172cd1adb6d91d054c724b4bb3aebf43ed8ed1` |
| только 2.8.14 | `Swords_R/animations/mobs.animation.json` | `—` | `fcd99e85c9b2ce1237325735a2f5400bbff3db6983cb32800d9c040c56fbff84` |
| только 2.8.14 | `Swords_R/animations/shulker_shield.animation.json` | `—` | `5676e31445e170b1812ee3935d8a92a79f37f0a0cac764a8c761340db80a6071` |
| только 2.8.14 | `Swords_R/animations/ultra_instinct_move.animation.json` | `—` | `802a9868471451dfab189254d2dceb580c9f6338bba3a636e911d521aa898460` |
| только 2.8.14 | `Swords_R/animations/ultra_instinct_projectile.animation.json` | `—` | `896f981aa6e68ef88c1fd0291ef24f447cb20319ccdf8419edf1c3a068368901` |
| только 2.8.14 | `Swords_R/blocks.json` | `—` | `5c2f6926da7475319dff6b590bee53a1119e3b8857a0d1f0a070c396637d0546` |
| только 2.8.14 | `Swords_R/entity/alpha_wolf.entity.json` | `—` | `264a901eea43a8b357b31b177a0d742d75343e33e483929370923557d6afe04f` |
| только 2.8.14 | `Swords_R/entity/bed_sword.entity.json` | `—` | `fd3b2844465544a30b1ffd5d6d5d0d1e90c06b4d1991fc0b33b71d27fd3e318f` |
| только 2.8.14 | `Swords_R/entity/bee_sword.json` | `—` | `496bb0ca7a167b5f8384d48868e5f9cb3305b13a1ad8d068e4ab43edde424304` |
| только 2.8.14 | `Swords_R/entity/enderman.entity.json` | `—` | `6225cc0d55bc01b03551ec6c265a75d528206479328057ab017e15d366a47238` |
| только 2.8.14 | `Swords_R/entity/fake_fireball.entity.json` | `—` | `8f5a1a54b224e88e009b074ad8137d5923ad2119d6cc323d46d510cb4d3fa71b` |
| только 2.8.14 | `Swords_R/entity/ghost.v1.0.json` | `—` | `29e704a89c0fec228e1ab684e44b2d692d22a82c2386e78dbe8ed2528b5d1133` |
| только 2.8.14 | `Swords_R/entity/grass.v1.0.json` | `—` | `e48f83132b2e425f9d6ec518b4c50c30f9a3b36297a2e8c7a8143d0d36d6fa00` |
| только 2.8.14 | `Swords_R/entity/mountable_slime.v1.0.json` | `—` | `07b23e973c411cfc176f9a289a5dec0fc0fa06854522fe003bd98e304d541f1c` |
| только 2.8.14 | `Swords_R/entity/nether_star.v1.0.json` | `—` | `db33d470fb3edf1407ec934c8761f427a1e3a2abc7a6e6179475eb51c8b62096` |
| только 2.8.14 | `Swords_R/entity/player.entity.json` | `—` | `05c0e53f5482dcae8f66be42e219a97934d32dcd6244f943c7fd4e1ae67f729b` |
| только 2.8.14 | `Swords_R/entity/pumpkin_projectile.entity.json` | `—` | `69f403303427cc8d2e75e877453149a93aaca5c51490ac9232e646f98f6d3084` |
| только 2.8.14 | `Swords_R/entity/shulker_shield.v1.0.json` | `—` | `425cf6f6b98cd428acc7b1164aadabc6e0a36f2ceb4a3ae2b4f004d342682b5d` |
| только 2.8.14 | `Swords_R/entity/slime_king.entity.json` | `—` | `ea65ab4758d2f61c372836f6f1f01746cf0ca560643473dda15751bb9e1422bf` |
| только 2.8.14 | `Swords_R/entity/ultra_instinct_projectile.json` | `—` | `d832d28f704b220105095592970d0586084853453e0d049c71c47c3bc77599a2` |
| только 2.8.14 | `Swords_R/entity/web.v1.0.json` | `—` | `6cd625976e2ebdc4082962db2f77480dcaa3066336fa55ee442f4f2b1eafcd40` |
| только 2.8.14 | `Swords_R/entity/witch.entity.json` | `—` | `fea1576d77bdeb113b945db339a0211e65705f70c40bfff9933557e3298f7f33` |
| только 2.8.14 | `Swords_R/entity/witch.v1.0.entity.json` | `—` | `d3a76a3b24d8b15090cf11c9cbdb9ab4faefa9d475ae139808dfc42c1319b298` |
| только 1.6 | `Swords_R/items/Sword_of_Time.json` | `132100c6bcfb9a230fadce5a84d166be777cd5c14cfc3911774dbcf4994f868c` | `—` |
| только 1.6 | `Swords_R/items/blaze_sword.json` | `68e88b7f1e42e0c9ab63f876f37b5fa9e988dda83b033fe0e3c4f7bb19823a00` | `—` |
| только 1.6 | `Swords_R/items/bone_sword.json` | `3be56e1440b296fb5c64487173b37fdda8a700c5afe23dd63d352910224b8780` | `—` |
| только 1.6 | `Swords_R/items/cactus_sword.json` | `491e49c8b2248ba4f5aa930370e8ff5adc328df43f9ba35f944c87a195bf248a` | `—` |
| только 1.6 | `Swords_R/items/coal_sword.json` | `147319467a8922cb560e2f79ea5afda4d7f806fcaa467c8d53fae6471336c53c` | `—` |
| только 1.6 | `Swords_R/items/creeper_sword.json` | `09a1848dbf6135921651a41646c0a72e917bf1801f85a792c24bc8b6a6cdcd22` | `—` |
| только 1.6 | `Swords_R/items/emerald_sword.json` | `a40e9d34ccb91120088d3ad9b80656b98246aa20b58554f953b2909fb92f959f` | `—` |
| только 1.6 | `Swords_R/items/ender_sword.json` | `5a0b4b71d942b79155e209b84a8487da3280a146acaba91a1f2aa11816d50644` | `—` |
| только 1.6 | `Swords_R/items/fire_sword.json` | `21fa4f5c7c4969ddee3e1ab3ce133fd368d62692e9b828dccaf63647c6a2ee3f` | `—` |
| только 1.6 | `Swords_R/items/glowstone_sword.json` | `694653dd22d75bc2c82b8966c0b91a20cdf602635e57f4832bb140c20e87fdc3` | `—` |
| только 1.6 | `Swords_R/items/grass_sword.json` | `d7190dece74e99e49e47e0d3eb70982e9a84e40ce9c24283a1fc91a6aeb000f7` | `—` |
| только 1.6 | `Swords_R/items/ice_sword.json` | `5cb3334b3d33cb33494dde6b4bebbed99e963d9ff3672f3424dd39d75c323b40` | `—` |
| только 1.6 | `Swords_R/items/jungle_sword.json` | `3174f26b2b2e791c15169e79546968092f769f179e0accd3509d165aaeb649c8` | `—` |
| только 1.6 | `Swords_R/items/lapis_sword.json` | `afc8e78bfb264faad94d24bd8142931fc64eb6d421314735293d02e50ac80143` | `—` |
| только 1.6 | `Swords_R/items/lightning_sword.json` | `50b53744b91dd5d68ba0a218e3e4212c6326c655178b8199819b6f9d99bf7169` | `—` |
| только 1.6 | `Swords_R/items/magma_sword.json` | `8c7ec10e0cb3b7b235576efd6bf1cb272b8bc4186b87f4498373155778542eca` | `—` |
| только 1.6 | `Swords_R/items/obsidian_sword.json` | `07603038ce92cca1a2f73a43c492264ed0ba82a09c34a4977b23f383dd1e1084` | `—` |
| только 1.6 | `Swords_R/items/quartz_sword.json` | `6a98078374626c66a5b59ceef214c492b3ddef40d6ef5d3cb011da0569505770` | `—` |
| только 1.6 | `Swords_R/items/sea_sword.json` | `270b869efcb1ae3607cfe60f3a8f37222096e988112127393e13ad66e36db960` | `—` |
| только 1.6 | `Swords_R/items/shulker_sword.json` | `adfd9933fcad89aff8e862231dfc7e15f0ceb3790d38adcb073ffb840386e4c4` | `—` |
| только 1.6 | `Swords_R/items/slime_sword.json` | `9265c0ab413baffd241ba34e5eb067bfe25e248881005fdb9a4fd453205a6e5c` | `—` |
| только 1.6 | `Swords_R/items/spectral_sword.json` | `4ae4e3109cd42cdb4fb95b59f965c9166cd39a4f1d4aee1dc0055727b052e007` | `—` |
| только 1.6 | `Swords_R/items/spider_sword.json` | `08b695a7ff05dc184108bc646c65f294d9bef180e586dce867267405ac4a0c8c` | `—` |
| только 1.6 | `Swords_R/items/sponge_sword.json` | `708759859508c10eeba8d8025b997ed4daf72d3ee47c9c90941cc944ae341f53` | `—` |
| только 1.6 | `Swords_R/items/tnt_sword.json` | `5fb091c21b1cd3e51d61bff7b527ace1001f7da382c7040638ad2d56e39f1d90` | `—` |
| только 1.6 | `Swords_R/items/wither_sword.json` | `cd4585e3708fdfd3274773b800197c77df7cb319e9249469c603b267eebe60ec` | `—` |
| изменён | `Swords_R/manifest.json` | `c644a706765e2c743d4f41064ee9f6877326baec93a91380a2f2a004112295ca` | `70f511ffa887bb51c00e9b538af281cdbcd7397604abcaac6f6dfb9486ddcadd` |
| только 2.8.14 | `Swords_R/materials/entity.material` | `—` | `a55ae77cbeec468298cc37688d3c73a3881aa9fa9fc69c235306a4ac33479e4c` |
| только 2.8.14 | `Swords_R/models/blocks/fake_ice.json` | `—` | `d5ff978680e3a0037a0a2cd555338353623bc85e7de66f826a4105c8aecadee0` |
| только 2.8.14 | `Swords_R/models/blocks/fake_ice2.json` | `—` | `3fa71f3de818d5f433eab5d38544d845426e29ca6776f35c4255a1b357aa29af` |
| только 2.8.14 | `Swords_R/models/blocks/fake_ice3.json` | `—` | `ff2e1e9b01893dd97c4c5c066b430b90a114c8151e53521c62098082a5098bfc` |
| только 2.8.14 | `Swords_R/models/blocks/fake_ice4.json` | `—` | `a99306467997fd4ebb803ac9fb0298ff0c010cc8a6d07b320b8d48ab94f38050` |
| только 2.8.14 | `Swords_R/models/blocks/null.geo.json` | `—` | `e0ae421ba8041b70ccd4581b967d32211a90f61eff33d1642cf542f7b5e044b9` |
| только 2.8.14 | `Swords_R/models/blocks/spectral_block.json` | `—` | `14b9545a4fa4125ff1a96bbd002c69818ae2fd2119473e320be5056edf36dc09` |
| только 2.8.14 | `Swords_R/models/entity/baby_slime.geo.json` | `—` | `4080689c9587f6743dd2e13ef7094d0d019b1a80456fbb314f65f75d72e93661` |
| только 2.8.14 | `Swords_R/models/entity/blaze_aura.geo.json` | `—` | `aed029e6747d55ddb91c741e8e471c5f5adc5392c38fb95f5493d021d56e04c5` |
| только 2.8.14 | `Swords_R/models/entity/blaze_rods.geo.json` | `—` | `d604a51c17059ee88dab22311302b263d3847cb47291425d861389b8da6fd3e0` |
| только 2.8.14 | `Swords_R/models/entity/ghost.geo.json` | `—` | `69e1b1f2cef2d387f47fe8134cbdf8c15abf51865e58eb6d945136e7008353da` |
| только 2.8.14 | `Swords_R/models/entity/grass.geo.json` | `—` | `990ae9323bc5cbb4632a4b8cb5ed9db640dd843bda76638f5f7adfc104185693` |
| только 2.8.14 | `Swords_R/models/entity/mermaid_player.geo.json` | `—` | `848d40095db8ef5fd6a3e8784c4b1b77e878619ecbf4d64caa6921e56a3575a4` |
| только 2.8.14 | `Swords_R/models/entity/mountable_slime.geo.json` | `—` | `394404abf568b1296b8c783013244d4941f18197bc6b422cc1fad534ef127318` |
| только 2.8.14 | `Swords_R/models/entity/player_ghost.geo.json` | `—` | `b6d667edbe2b7cfdfa8e77d487786646367580af3955076d866691301e250eec` |
| только 2.8.14 | `Swords_R/models/entity/pumpkin_projectile.geo.json` | `—` | `7e6dcb41e60c6618df175b2b690547bfde14c543d2c55df892367481f422e756` |
| только 2.8.14 | `Swords_R/models/entity/shulker_shield.geo.json` | `—` | `84e84885fd289da6f71ec46123cb551ca7fa6ecdbc657c6b3d55a94e19545633` |
| только 2.8.14 | `Swords_R/models/entity/slime_king_armor.geo.json` | `—` | `db0d4edd317f0acad14c4ba88c4680cc152a13ef982fa47b59a6ece733c1ef6b` |
| только 2.8.14 | `Swords_R/models/entity/ultra_instinct_aura.geo.json` | `—` | `8b2acf9fdf620b0355b114beb5b4c9307e946af271cf6aeea9ce4e81aaec4794` |
| только 2.8.14 | `Swords_R/models/entity/ultra_instinct_projectile.geo.json` | `—` | `e372473ed661970f1872bc449ff3aa28efeee15a90aee90ef6afa3102e2b0433` |
| только 2.8.14 | `Swords_R/models/entity/wolf_transformation.geo.json` | `—` | `904c513357bcba37b6c3e6f61832ea13b2c2452a83c09559a370eee83f74d73d` |
| только 2.8.14 | `Swords_R/models/entity/wolf_vision.geo.json` | `—` | `9149fe52f3fd5dd1fff6540afd1e0f5e43f0f1ed222ef02c3cca72848e879972` |
| изменён | `Swords_R/pack_icon.png` | `434eacaaec8642bb534262bf727502b81d7bba1bc760ffa3baedf25bb17b2812` | `1d1faeae22cbb8db31db1380c25dfeb4b68ca649f6cc72bd974720823152bec3` |
| только 2.8.14 | `Swords_R/particles/examples/example_bounce.json` | `—` | `fe7bf18d4c506de7f3078fbeb75d3b97b23a2c03cc0ba8129518264a93d14516` |
| только 2.8.14 | `Swords_R/particles/examples/example_directional_sphere.json` | `—` | `9171f253cd76356cdef65c817807ba452e3fb6fc2719a95ee432522ec148bd99` |
| только 2.8.14 | `Swords_R/particles/examples/example_directional_sphere_2.json` | `—` | `6a22353392c263e0b4471874382e110c4379c0758f2c0846c13f1c59486f28b0` |
| только 2.8.14 | `Swords_R/particles/examples/example_flipbook.json` | `—` | `c082f13ccbd6ef16f1ccdd3631f1be3afedb6c309ca953593bfe19ed0fb9b94d` |
| только 2.8.14 | `Swords_R/particles/examples/example_linearcurve.json` | `—` | `0e8779b63de7280bf1e0de933f1126082c17ceab09a4b92f8540e735d5f6719f` |
| только 2.8.14 | `Swords_R/particles/examples/ghost_spiral.json` | `—` | `6e4dbb039dccb23c53f8c7c0ab2224ca61399c297f6e45aa3357c15e3f39bf89` |
| только 2.8.14 | `Swords_R/particles/nether_star_hit.json` | `—` | `cea98a3a0700492d7ab320d042a9fed43c02cf75c86a5d3db5781a3b907a34fe` |
| только 2.8.14 | `Swords_R/render_controllers/blaze_aura.render_controllers.json` | `—` | `90e48feb1ca0bc1905e1556b709602f5af0520d2bf1b7a628ee5a1200b48ac34` |
| только 2.8.14 | `Swords_R/render_controllers/blaze_rods.render_controllers.json` | `—` | `165e89a6608f2030fe27c7f8dc3b05d91b377b72b2bee88c0a877d535cc401ef` |
| только 2.8.14 | `Swords_R/render_controllers/default.render_controllers.json` | `—` | `61f489b438ab7ed930ccf433247fd86114b1350e04a366641e2fef78a6e1c2ca` |
| только 2.8.14 | `Swords_R/render_controllers/enderman.render_controllers.json` | `—` | `375d940ffc9380df499b05c8f265d90d24ea96ed5b174aa31d39254c59d3a0c9` |
| только 2.8.14 | `Swords_R/render_controllers/ghost.render_controllers.json` | `—` | `ff2afb889a7b0cb49c130032776043724c0a9eb6a2e216ce5f9f2bf640066d3f` |
| только 2.8.14 | `Swords_R/render_controllers/grass.render_controllers.json` | `—` | `d716827edfdb8e2ff751b2a4e2a06e186d39f6bba1cf94a901de9e92ff9f78ff` |
| только 2.8.14 | `Swords_R/render_controllers/mermaid_player.render_controllers.json` | `—` | `01deeafbfaffed1f177461b17742b91b9c08cdc6964f8a8a1fca09f9e3f21441` |
| только 2.8.14 | `Swords_R/render_controllers/player_ghost.render_controllers.json` | `—` | `8aa60aa9fd452e1f28fe879d841d221f5b927097491cba71e4a6aabbe76c1d50` |
| только 2.8.14 | `Swords_R/render_controllers/pumpkin_projectile.render_controllers.json` | `—` | `1e0d2245ed096e5efef4934950e18597e2293143b8d8a77732d794d194075559` |
| только 2.8.14 | `Swords_R/render_controllers/shulker_shield.render_controllers.json` | `—` | `d9e2f9721f0a1b582f403eeb3e6442af9ccf446218eae132d70641dd13d07b3e` |
| только 2.8.14 | `Swords_R/render_controllers/ultra_instinct_aura.render_controllers.json` | `—` | `dcf9952d51faad5709ab1f7e992fa2fb2fd378189cd0cc7010a7484a12d5d65f` |
| только 2.8.14 | `Swords_R/render_controllers/ultra_instinct_projectile.render_controllers.json` | `—` | `2e8b0c601e0c76babc9f2b7cfbccddee5b849d06fd2be0167e34e4c3a0737f19` |
| только 2.8.14 | `Swords_R/render_controllers/witch.render_controllers.json` | `—` | `ea636495e315816b4f1f7f756f004491c7051b99bc3ffa163feacf32bba92bfe` |
| только 2.8.14 | `Swords_R/render_controllers/wolf_transformation.render_controllers.json` | `—` | `af424e0c4cd4e26a911cfeea379dc405cabf7e36d56831566be7b3ce409344e3` |
| только 2.8.14 | `Swords_R/render_controllers/wolf_vision.render_controllers.json` | `—` | `919c5a71b63703dd9a85a22929a9c83f6e0004f73d401f31b47c398b9145722c` |
| только 2.8.14 | `Swords_R/sounds.json` | `—` | `f2b5876e7121aab05e83a5d889a55a719bd525750a91eef42ec2877ea8d13f3f` |
| только 2.8.14 | `Swords_R/sounds/ghost_sword/wailing.ogg` | `—` | `7f2574957dfa0b3ec48295bd94073e22840ac3c7eedf6739923deccaabcc1348` |
| только 2.8.14 | `Swords_R/sounds/sound_definitions.json` | `—` | `f172f276d5bb20596a647fea880195df7198853d26f8f2a75025b422b1280330` |
| только 2.8.14 | `Swords_R/sounds/wolf_sword/distant_howl.ogg` | `—` | `5d6bdea2ba2183e7ab965c17d36cb66a54a93c634047ca3163cf69552e66c0e8` |
| только 2.8.14 | `Swords_R/sounds/wolf_sword/howl.ogg` | `—` | `db2b08a2103d38d3b32feebe187c7c38b153b46e9e44ac147936fc6941c76020` |
| изменён | `Swords_R/texts/en_US.lang` | `e49c82c7ccbb1fb5ac24ac86496a0f442f6268a180058c122b56d2cd59f534a6` | `37ee50014e83f21d8ee4621d51171f8a475f4bce2b3640fd027aca8f3ce90393` |
| только 2.8.14 | `Swords_R/textures/blocks/fake_ice.png` | `—` | `e31f1cb478052654d5699d232d9419b888dd0cfe3c9106a435552602e39bd17f` |
| только 2.8.14 | `Swords_R/textures/blocks/lightblock.png` | `—` | `8ff30cd9dc11cc06a7377bb427946861d492966ac3d4e4f663dd2ad9d1ad6941` |
| только 2.8.14 | `Swords_R/textures/blocks/lightblock2.png` | `—` | `8ff30cd9dc11cc06a7377bb427946861d492966ac3d4e4f663dd2ad9d1ad6941` |
| только 2.8.14 | `Swords_R/textures/blocks/quartz_diamond_block.png` | `—` | `70fb2e4f54bd24009c1f551cb56a85e31960dbe1f3094c13ad322d2b20e16716` |
| только 2.8.14 | `Swords_R/textures/blocks/quartz_diamond_ore.png` | `—` | `8eea7d0972a09c6a2a2b2eb2c61efe0d3e7fdd8c9c36e6a2a750874c72248636` |
| только 2.8.14 | `Swords_R/textures/blocks/silver_ore.png` | `—` | `7702d245fe117c87be86e053f33ffe76a23ec0d8cb03f9d5d848a3f826556f44` |
| только 2.8.14 | `Swords_R/textures/blocks/spectral_block.png` | `—` | `92a580a28da5631c6b2af03c3312b228545996ebf12683532c70acc48f84415e` |
| только 2.8.14 | `Swords_R/textures/entity/blaze_rods.png` | `—` | `900c49dbb88a0b070a69b7c44a5f769d9d3b6f11032953bfd25a7fb2bd1f0e13` |
| только 2.8.14 | `Swords_R/textures/entity/enderman/enderman.tga` | `—` | `a94d1e061aa62a01a9f8fdde09afcc2079af09cc796df6e94b70a2bcc1ec9c95` |
| только 2.8.14 | `Swords_R/textures/entity/enderman/red_enderman.tga` | `—` | `6343454292704fdc8058869a5d4ffd9cd9b809601f93a558a04bf3a3cc4a8820` |
| только 2.8.14 | `Swords_R/textures/entity/ghost.png` | `—` | `303f938f5c4dc69a12aacb03fc358fbf5ea0b297bf55734de8aea9d134f2febe` |
| только 2.8.14 | `Swords_R/textures/entity/grass.png` | `—` | `3375f62630ed50c085962131b5119aa071927dbae37f1777e5155ba525f43247` |
| только 2.8.14 | `Swords_R/textures/entity/grass_witch.png` | `—` | `1e9f744e4177825de9fb6f141a216348182e1fb15c63f0642eca61ea23dfaba7` |
| только 2.8.14 | `Swords_R/textures/entity/mermaid_player.png` | `—` | `c2189f171a816a6ee0eb6f856cfc3e4d5acbc02797911c32012f45590a80a3dd` |
| только 2.8.14 | `Swords_R/textures/entity/particles.png` | `—` | `955e7797a40eebcae6476279bfcd114ff3817a958c75d002ccd9c06b312017c9` |
| только 2.8.14 | `Swords_R/textures/entity/pumpkin_projectile.png` | `—` | `5e990f27e0757f610d7fdce6273d1e3934d537ae3d8c3c57f6a2a9041adf520f` |
| только 2.8.14 | `Swords_R/textures/entity/shulker_shield.png` | `—` | `312641c04dd9ed443815fd7c305c8a91fb33118ebb5ba8bb5c143623d7549ce2` |
| только 2.8.14 | `Swords_R/textures/entity/slime.png` | `—` | `48251f1a8a4ee083bfed0011c9457b50ffda68a9158d40379cb4c01150d7eba0` |
| только 2.8.14 | `Swords_R/textures/entity/slime/baby_slime.png` | `—` | `9d7bbd30f787de51a5ef38461d7d3e09496ae1a37eb25257b919560f62f34481` |
| только 2.8.14 | `Swords_R/textures/entity/slime/magmacube.tga` | `—` | `e9275615a3a6dddab130c3fa4f1a0f6bf44d1f45d9dd5728c30955afa4d6e59f` |
| только 2.8.14 | `Swords_R/textures/entity/slime/slime.png` | `—` | `48251f1a8a4ee083bfed0011c9457b50ffda68a9158d40379cb4c01150d7eba0` |
| только 2.8.14 | `Swords_R/textures/entity/slime/slime_king.png` | `—` | `5e75b92a375831d8a3a71ede3f2b0701f4ff55f3495615d6f6b369f717668bdd` |
| только 2.8.14 | `Swords_R/textures/entity/ultra_instinct_aura.png` | `—` | `76438c4073849ec8069a1ca525513026e8034b99fde47156f39970e447b778ac` |
| только 2.8.14 | `Swords_R/textures/entity/ultra_instinct_projectile.png` | `—` | `85507e324829992c7cce8a77d09ecad6e45501a30db1cf34a9c27e4fcb5c7741` |
| только 2.8.14 | `Swords_R/textures/entity/web.png` | `—` | `5d4f7313d3c8f84bbfc3e5b420604db34ffde520f3f6b4e58757ae10fe88cb37` |
| только 2.8.14 | `Swords_R/textures/entity/wolf_transformation.png` | `—` | `719a7679f035a2dfe3f21c736c67583dd4fcd0ed0cc8e0d86a83e9eaa13f24a2` |
| только 2.8.14 | `Swords_R/textures/entity/wolf_vision.png` | `—` | `1f240c2a07cdcf59dc32dbe479934e4f836ce0fa8b117d7d0097e5bc8936e558` |
| только 2.8.14 | `Swords_R/textures/flipbook_textures.json` | `—` | `224f536330eb815e17dcebc2485926a2c565957016ba5d708ecb2c2ce70813b1` |
| изменён | `Swords_R/textures/item_texture.json` | `c8badc6b81dbb4c18566ac85cba193c9afd395a40d21707a3f31b2c6c4767e69` | `b6b6ebbd91a3000c0115b9408d3968d962158d29b3ea1a86b92f3bf687e94266` |
| только 1.6 | `Swords_R/textures/items/Sword_of_Time.png` | `8613fd0f6cb0fb77d2455e96b9419e46f5163bf394da0eb8574d229f45fa34ee` | `—` |
| только 2.8.14 | `Swords_R/textures/items/bedrock_stick.png` | `—` | `72be8cf26b84d6a599bf2afea02bf95c28e0e78b038e222296381c51ec8481a4` |
| только 2.8.14 | `Swords_R/textures/items/bedrock_sword.png` | `—` | `52e028becdd098421e1b8c24e8dd2b42c278cc8d43e959463943ca8dd2dae4cb` |
| только 2.8.14 | `Swords_R/textures/items/bee_sword.png` | `—` | `a7a1f2bcb56ffbf8ed52c37c9dc0461f3f64f3322eebf1db8209f4f7faa567b5` |
| изменён | `Swords_R/textures/items/bone_sword.png` | `fe88df2adcedc08b38835336fddef86e124925e18be0bf7cab6280a4309345c1` | `863e3528e79706e43173fb56275fabc0f7813af6b354219159bd22b321b16343` |
| изменён | `Swords_R/textures/items/cactus_sword.png` | `30d45f098203f14ff714216dd540b77daf716c9e7cb73e66cafce24efe168464` | `df524ac680c19c71561de5ccbf76b9ddcc3edfab2e1502948c16bc73e488d228` |
| только 2.8.14 | `Swords_R/textures/items/clock_sword.png` | `—` | `6493d97bc9192e94984d2f1eaeb4bee695b63c2e1342bb565dd92d41ca17999a` |
| только 2.8.14 | `Swords_R/textures/items/cursed_pumpkin_sword.png` | `—` | `f301ee652b12ea0a52d3f1a2cc9bad76d3c8ecfc2d1239edf76e75d09dc96f07` |
| изменён | `Swords_R/textures/items/ender_sword.png` | `ebfec1b300f8c15c752225f1ca23c2b9e155551e0bc5b106f47fcd378063187e` | `eaf4f33d930a1f075c803dca5aaa8e608f1eb422d37dab20dc10ad9a7881a24d` |
| только 2.8.14 | `Swords_R/textures/items/ghost_sword.png` | `—` | `e7b59ed2c2c89035b93cdc34c7d7c816ee180db379a3335a951d7f5eff5d3ec0` |
| только 2.8.14 | `Swords_R/textures/items/glass_sword.png` | `—` | `9cbe175e0cdf04dc46953b97b2243ba967bd529c473a35a674d46fa1d1c76e97` |
| изменён | `Swords_R/textures/items/grass_sword.png` | `b02e0a177ad9491aaa6af4626cbe4c83dee1deaa011bbc7d00f75245012da38a` | `414f293674739c42179ddb809c9a0fb41c6fc20931106624358fe9b7fc79dfd1` |
| изменён | `Swords_R/textures/items/lightning_sword.png` | `647c6e005ce7e677558157fa253d3d10f2f90b19a071bcd9ad3869f2b663fb7c` | `3268d71fcf9dc4dc6ea5095be108d29503894e4d5b3fe041db66062faf0ca1f1` |
| только 2.8.14 | `Swords_R/textures/items/nether_star_sword.png` | `—` | `e3d608b8d6c590b99094fb2ffd16c45a8ab8098f8cc55562286e0625e79a04f8` |
| только 2.8.14 | `Swords_R/textures/items/pumpkin_face_off.png` | `—` | `8993e19661e39829ec6e126ea3fe97e5e63725c268d0776c3c71ff824087f1aa` |
| только 2.8.14 | `Swords_R/textures/items/pumpkin_face_on.png` | `—` | `8a68b2727006eaa8bda90f283723e75474bbe805973bd30b70b716bb8463c034` |
| только 2.8.14 | `Swords_R/textures/items/pumpkin_side.png` | `—` | `4794db787370fd96d9b767600e6b8a678e49683ce2be12b2668ee8e8c11b7cb0` |
| только 2.8.14 | `Swords_R/textures/items/pumpkin_top.png` | `—` | `d454f99259a049130e4be02ec3c7a59ccac2d6754c9f5fc1283259e200f05e41` |
| только 2.8.14 | `Swords_R/textures/items/quartz_diamond.png` | `—` | `eb79d9e236605948856f24e5f926a13800b861ed61c492b596f9d0127cc70cd3` |
| только 2.8.14 | `Swords_R/textures/items/quartz_diamond_block.png` | `—` | `ed4fb6f97aab41428a63566ae10145c7384d2f058c93c5bf1c5494a858eaaebe` |
| только 2.8.14 | `Swords_R/textures/items/quartz_diamond_stick.png` | `—` | `25e2cb5e50c3b5fafe704e73adb90e041e602e76c7c87682f92eb105a30612de` |
| изменён | `Swords_R/textures/items/quartz_sword.png` | `450337207d01a23f28cc4a7fcca5ddcf2a05d5a5e4f5b052346640794be1ff9d` | `5c7fd825f86ef9528d971253e47024df1f6fce7b569925bfc7612e3016129beb` |
| только 2.8.14 | `Swords_R/textures/items/silver_ingot.png` | `—` | `0fcfb476a35e3b9b3387c1d2ed374fc255005fe1ac3e3beda380a517fccea95c` |
| только 2.8.14 | `Swords_R/textures/items/silver_sword.png` | `—` | `f69e66b46bc6e572e7f2c8fa413790ee8897ff155f3f1410e452bd114dfbd389` |
| изменён | `Swords_R/textures/items/spectral_sword.png` | `09f8aa9d7457d635ac3831d857057525bb2aa48d0cc9d3e97ce1c2d2d8f08a41` | `c855d7c151b6e2f005d471c493fb6d9f077ef735921ccb3a2e7647b8acbed5e3` |
| только 2.8.14 | `Swords_R/textures/items/time_sword.png` | `—` | `50805410a3babc7cb414ace2cdc38f29a619087cf4715933649dd11225840b59` |
| только 2.8.14 | `Swords_R/textures/items/ultra_instinct_sword.png` | `—` | `fe84556e2aba4f502eacdf13806e65e923ccf240ee542e054fbdee56d6752dd0` |
| только 2.8.14 | `Swords_R/textures/items/wet_sponge_sword.png` | `—` | `b67a6c4157ff319553a47ed7d904e53c3906114d9c659308c544fc270199b00e` |
| только 2.8.14 | `Swords_R/textures/items/wither_skeleton_sword.png` | `—` | `d6e66480ed746a00937e98d385aec5f592ff9176ec6ff49a29d9bf2f236d0739` |
| изменён | `Swords_R/textures/items/wither_sword.png` | `81122b4771143b8614c3cc1ebb7b4fc35acd9599f83e55a0c142918e0690ada5` | `7978d1d7d7c9050875cc252513c48c962edcd06ac19c074b77d5fcda4621087d` |
| только 2.8.14 | `Swords_R/textures/items/wolf_sword.png` | `—` | `5f7cabfeeb15e918b3dc8adaf69d11929ad6e4e8145ec147372d108c6fb1a21b` |
| только 2.8.14 | `Swords_R/textures/particles.png` | `—` | `60ec9fe01780817a547ef2735075f131a9a061c32a5e787e1eaff65063541cd5` |
| только 2.8.14 | `Swords_R/textures/terrain_texture.json` | `—` | `6795b0800448f2bcfa9aef3404a0f6f5ac0c606ed32f713565fb9223804e46f9` |
| только 2.8.14 | `Swords_R/textures/ui/apha_wolf.jpeg` | `—` | `5ae27b8f2804c96f593256a24e8b13130baa7dc8ed9aba646216f8c51d3e7139` |
| только 2.8.14 | `Swords_R/textures/ui/centella.jpeg` | `—` | `42363e8c1f699a29a191750c9f372cc28cf0fcc3077300f49374267fd87317f3` |
| только 2.8.14 | `Swords_R/textures/ui/coal_sword_fuel.png` | `—` | `763efa4df77445750c716bb2fcbc60436f3acbe8eec085b05113fe97bd3046fa` |
| только 2.8.14 | `Swords_R/textures/ui/crafting_clock_sword.png` | `—` | `150cb979b9696174bbc490bb9f2df32f68883e5f2dc23a97609e12c3da326f95` |
| только 2.8.14 | `Swords_R/textures/ui/ghost.png` | `—` | `e19c749d85b8ace3428bec1062ae3d7bff1e961093d4919f89f604aff76f8f30` |
| только 2.8.14 | `Swords_R/textures/ui/ghost_.jpeg` | `—` | `e05522c603f53c8f2f63de4a13ffb858ee06bc04b2cd63ccad604c2c6d964691` |
| только 2.8.14 | `Swords_R/textures/ui/grass_witch.jpeg` | `—` | `44d632b111fcc7587491557e0151e5660f15abbdd7b13c94b249136f850c4c0a` |
| только 2.8.14 | `Swords_R/textures/ui/how_to_play_button_default.png` | `—` | `0f6923f6a3a87cab5a97bc71e8c6c3f9ae86927050a6b8141a1934dc1035b80d` |
| только 2.8.14 | `Swords_R/textures/ui/how_to_play_button_default_light.png` | `—` | `39ddc7d64afbeff0397a783f3fb935688c02112ac781bc2b016981d147f0d240` |
| только 2.8.14 | `Swords_R/textures/ui/how_to_play_button_hover.png` | `—` | `294cb7e6a8dcfddc6ec567333a1b8c58ae6dfdcf9496be4d46e2bbd1a4bd4eb6` |
| только 2.8.14 | `Swords_R/textures/ui/how_to_play_button_hover_light.png` | `—` | `215efc32dee80b9bbf7f2db21078c3bd7b41fee65b15f6f4919d1a4e0be70b1d` |
| только 2.8.14 | `Swords_R/textures/ui/how_to_play_button_pressed.png` | `—` | `9e21111c5b9f61844e892944a205bf8f3aaa3ccdcad7fb1aea31fad04edc6d31` |
| только 2.8.14 | `Swords_R/textures/ui/how_to_play_button_pressed_light.png` | `—` | `ce45b620f6a223bda758f0be16d92277bdb575cb48b15a22e24420ba72f54cdf` |
| только 2.8.14 | `Swords_R/textures/ui/lapis_sword_xp.png` | `—` | `ebdf758611869d88b247ba83bd8e85d06e2e053b2af2a488ba3ad5b7b38e6278` |
| только 2.8.14 | `Swords_R/textures/ui/red_enderman.png` | `—` | `324d4dac935dc541400f7007ddf134060ce2d765360ef42ef6065dab2f5e6f58` |
| только 2.8.14 | `Swords_R/textures/ui/red_enderman_.jpeg` | `—` | `81e2ff0d7f2ce2e773ae224556eb8c491b8d106109941e67a4f755d37522e2ea` |
| только 2.8.14 | `Swords_R/textures/ui/slime_baby.png` | `—` | `ee4dc47daeaf1636d0bab8ea172dceb2c8850e565e8f2d09c715b072263d7a97` |
| только 2.8.14 | `Swords_R/textures/ui/slime_king.jpeg` | `—` | `107364239559d0c250360186adb6191d82f267b86a543319a4ddc54e70e30be2` |
| только 2.8.14 | `Swords_R/textures/ui/swords_and_more_swords.jpeg` | `—` | `a40a7d488be41d46b6e8e6823882c0a4e3e8b4430974959845600673b021bb4d` |
| только 2.8.14 | `Swords_R/textures/ui/well.png` | `—` | `e915b68ca50aeb113add008f375dfd200d861ccb5b938fe654e5af381216e9a2` |
| только 2.8.14 | `Swords_R/textures/ui/werewolf.png` | `—` | `04af8970d047c406afe7089bf11acf5cf21293ecbc7ca018380a7b226d2ba907` |
| только 2.8.14 | `Swords_R/ui/how_to_play_screen.json` | `—` | `5048424cc16b4080268f96e3b1f6c1aa342c717e14b602a37c6dc079d6e9f3cf` |

Совпадают по нормализованному пути и байтам: 19.

## Построчные изменения совпадающих текстовых путей

### `Swords_B/animation_controllers/shulker_sword.json`

```diff
--- 1.6/Sword_B/animation_controllers/shulker_sword.json
+++ 2.8.14/Swords_B/animation_controllers/shulker_sword.json
@@ -1,41 +1,23 @@
 {
   "format_version": "1.10.0",
   "animation_controllers": {
-    "controller.animation.shulker": {
+    "controller.animation.shulker_sword": {
       "states": {
         "default": {
           "transitions": [
             {
-              "shulker": "(1.0)"
+              "shulker_sword": "q.get_equipped_item_name=='shulker_sword' && q.is_sneaking"
             }
-          ],
-          "on_entry": [
-          	"/effect @p levitation 0 0 true",
-          	"/execute @p ~ ~ ~ tp @e[type=entity:shulker2] ~ ~2.5 ~",
-            "/scoreboard objectives add sh dummy",
-            "/scoreboard players add @p sh 1",
-            "/execute @p[scores={sh=40}] ~ ~ ~ summon entity:shulker2",
-            "/execute @p[scores={sh=2400}] ~ ~ ~ scoreboard objectives remove sh",
-            "/execute @p[scores={sh=2390}] ~ ~ ~ kill @e[type=entity:shulker2,r=5] ~ 0 ~",
-            "/scoreboard players set @a swords 2"
           ]
         },
-        "shulker": {
+        "shulker_sword": {
+          "on_entry": [
+            "@s shulker_sword_skill"
+          ],
           "transitions": [
             {
-              "default": "(1.0)"
+              "default": "1.0"
             }
-          ],
-          "on_entry": [
-            "/effect @p levitation 0 0 true",
-            "/execute @p ~ ~ ~ tp @e[type=entity:shulker2] ~ ~2.5 ~",
-            "/scoreboard objectives add sh dummy",
-            "/scoreboard players add @p sh 1",
-            "/execute @p[scores={sh=40}] ~ ~ ~ summon entity:shulker2",
-            "/execute @p[scores={sh=2400}] ~ ~ ~ scoreboard objectives remove sh",
-            "/execute @p[scores={sh=2390}] ~ ~ ~ kill @e[type=entity:shulker2,r=5] ~ 0 ~",
-            "/scoreboard players set @a swords 2"
-
           ]
         }
       }
```

### `Swords_B/animation_controllers/wither_sword.json`

```diff
--- 1.6/Sword_B/animation_controllers/wither_sword.json
+++ 2.8.14/Swords_B/animation_controllers/wither_sword.json
@@ -1,71 +1,23 @@
 {
   "format_version": "1.10.0",
   "animation_controllers": {
-    "controller.animation.wither": {
+    "controller.animation.wither_sword": {
       "states": {
         "default": {
           "transitions": [
             {
-              "wither": "(1.0)"
+              "wither_sword": "q.get_equipped_item_name=='wither_sword'"
             }
-          ],
-          "on_entry": [
-            "/Effect99"
           ]
         },
-        "wither": {
+        "wither_sword": {
+          "on_entry": [
+            "/ride @s summon_rider entity:name minecraft:wither_sword"
+          ],
           "transitions": [
             {
-              "default": "(1.0)"
+              "default": "1.0"
             }
-          ],
-          "on_entry": [     	
-            "/effect @e[r=16,type=!player] poison 30 1 true",
-            "/execute @a ~~~ particle minecraft:falling_dust_concrete_powder_particle ~-0.1 ~0.2 ~-0.2",
-            "/fill ~5 ~5 ~5 ~-5 ~-5 ~-5 dirt 1 replace grass",
-            "/fill ~5 ~5 ~5 ~-5 ~-5 ~-5 air 0 replace leaves2",
-            "/fill ~5 ~5 ~5 ~-5 ~-5 ~-5 air 0 replace leaves",
-            "/fill ~5 ~5 ~5 ~-5 ~-5 ~-5 water 0 replace ice",
-            "/fill ~5 ~5 ~5 ~-5 ~-5 ~-5 dirt 0 replace farmland",
-            "/fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace red_flower",
-            "/fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace yellow_flower",
-            "/fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace red_mushroom",
-            "/fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace brown_mushroom",
-            "/fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace double_plant",
-          	"/scoreboard objectives add w dummy",
-          	"/scoreboard players add @e[r=16,type=!cow,type=!pig,type=!sheep,type=!horse,type=!rabbit,type=!villager,type=!wolf,type=!cat,type=!fox,type=!chicken] w 1",
-          	"/execute @p[scores={w=200}] ~ ~ ~ playsound mob.wither.death",
-          	"/execute @p[scores={w=500}] ~ ~ ~ playsound mob.wither.hurt",
-          	"/execute @e[scores={w=100},r=16,type=zombie] ~ ~ ~ summon entity:explode",
-            "/execute @e[scores={w=100},r=16,type=husk] ~ ~ ~ summon entity:explode",
-            "/execute @e[scores={w=100},r=16,type=drowned] ~ ~ ~ summon entity:explode",
-            "/execute @e[scores={w=100},r=16,type=creeper] ~ ~ ~ summon entity:explode",
-            "/execute @e[scores={w=100},r=16,type=enderman] ~ ~ ~ summon entity:explode",
-            "/execute @e[scores={w=100},r=16,type=slime] ~ ~ ~ summon entity:explode",
-            "/execute @e[scores={w=100},r=16,type=skeleton] ~ ~ ~ summon entity:explode",
-            "/execute @e[scores={w=100},r=16,type=stray] ~ ~ ~ summon entity:explode",
-            "/execute @e[scores={w=100},r=16,type=blaze] ~ ~ ~ summon entity:explode",
-            "/execute @e[scores={w=100},r=16,type=wither_skeleton] ~ ~ ~ summon entity:explode",
-            "/execute @e[scores={w=100},r=16,type=witch] ~ ~ ~ summon entity:explode",
-            "/execute @e[scores={w=100},r=16,type=magma_cube] ~ ~ ~ summon entity:explode",
-            "/execute @e[scores={w=100},r=16,type=ghast] ~ ~ ~ summon entity:explode",
-            "/execute @e[scores={w=100},r=16,type=zombie_pigman] ~ ~ ~ summon entity:explode",
-            "/execute @e[scores={w=100},r=16,type=spider] ~ ~ ~ summon entity:explode",
-            "/execute @e[scores={w=100},r=16,type=cave_spider] ~ ~ ~ summon entity:explode",
-            "/execute @e[scores={w=100},r=16,type=silverfish] ~ ~ ~ summon entity:explode",
-            "/execute @e[scores={w=100},r=16,type=evocation_fang] ~ ~ ~ summon entity:explode",
-            "/execute @e[scores={w=100},r=16,type=evocation_illager] ~ ~ ~ summon entity:explode",
-            "/execute @e[scores={w=100},r=16,type=vex] ~ ~ ~ summon entity:explode",
-            "/execute @e[scores={w=100},r=16,type=ravager] ~ ~ ~ summon entity:explode",
-            "/execute @e[scores={w=100},r=16,type=endermite] ~ ~ ~ summon entity:explode",
-            "/execute @e[scores={w=100},r=16,type=guardian] ~ ~ ~ summon entity:explode",
-            "/execute @e[scores={w=100},r=16,type=vindicator] ~ ~ ~ summon entity:explode",
-            "/execute @e[scores={w=100},r=16,type=phantom] ~ ~ ~ summon entity:explode",
-            "/execute @e[scores={w=100},r=16,type=tnt] ~ ~ ~ summon entity:explode",
-            "/execute @e[scores={w=100},r=16,type=zombie_villager] ~ ~ ~ summon entity:explode",
-            "/execute @e[scores={w=100},r=16,type=wither] ~ ~ ~ summon entity:explode",
-          	"/execute @p[scores={w=600}] ~ ~ ~ scoreboard objectives remove w",
-            "/scoreboard players set @a swords 2"
           ]
         }
       }
```

### `Swords_B/entities/blaze.json`

```diff
--- 1.6/Sword_B/entities/blaze.json
+++ 2.8.14/Swords_B/entities/blaze.json
@@ -1,46 +1,140 @@
 {
-  "format_version": "1.11.0",
+  "format_version": "1.13.0",
   "minecraft:entity": {
     "description": {
-      "identifier": "entity:blaze",
-      "is_spawnable": false,
+      "identifier": "minecraft:blaze",
+      "is_spawnable": true,
       "is_summonable": true,
-      "is_experimental": false,
-      "scripts": {
-        "animate": [
-          "blaze"
+      "is_experimental": false
+    },
+    "components": {
+      "minecraft:experience_reward": {
+        "on_death": "query.last_hit_by_player ? 10 : 0"
+      },
+      "minecraft:loot": {
+        "table": "loot_tables/entities/blaze.json"
+      },
+      "minecraft:collision_box": {
+        "width": 0.5,
+        "height": 1.8
+      },
+      "minecraft:attack": {
+        "damage": 6
+      },
+      "minecraft:damage_sensor": {
+        "triggers": [
+          {
+           "cause": "fall",
+           "deals_damage": false
+          } 
         ]
       },
-      "animations": {
-        "blaze": "controller.animation.blaze"
+      "minecraft:movement": {
+        "value": 0.23
+      },
+      "minecraft:navigation.walk": {
+        "can_path_over_water": true
+      },
+      "minecraft:movement.basic": {
+
+      },
+      "minecraft:jump.static": {
+      },
+      "minecraft:can_climb": {
+      },
+      "minecraft:can_fly": {
+      },
+      "minecraft:health": {
+        "value": 20,
+        "max": 20
+      },
+      "minecraft:hurt_on_condition": {
+        "damage_conditions": [
+          {
+            "filters": { "test": "in_water_or_rain", "operator": "==", "value": true },
+            "cause": "drowning",
+            "damage_per_tick": 1
+          }
+        ]
+      },
+      "minecraft:follow_range": {
+        "value": 48,
+        "max": 48
+      },
+      "minecraft:fire_immune": true,
+      "minecraft:nameable": {
+
+      },
+      "minecraft:behavior.float": {
+        "priority": 0
+      },
+      "minecraft:behavior.hurt_by_target": {
+        "priority": 1
+      },
+      "minecraft:behavior.nearest_attackable_target": {
+        "priority": 2,
+        "entity_types": [
+          {
+            "filters": {
+              "test": "is_family",
+              "subject": "other",
+              "value": "player"
+            },
+            "max_dist": 48
+          }
+        ],
+        "must_see": true
+      },
+      "minecraft:behavior.melee_attack": {
+        "priority": 3,
+        "max_dist": 3,
+        "speed_multiplier": 1,
+        "random_stop_interval": 2.0,
+        "track_target": true
+      },
+      "minecraft:shooter": {
+        "type": "smallfireball",
+        "def": "minecraft:small_fireball"
+      },
+      "minecraft:behavior.ranged_attack": {
+        "priority": 4,
+        "attack_interval_min": 3,
+        "attack_interval_max": 5,
+        "charge_charged_trigger": 0.0,
+        "charge_shoot_trigger": 4.0,
+        "attack_radius": 16,
+        "burst_shots": 3,
+        "burst_interval": 0.3
+      },
+      "minecraft:behavior.random_stroll": {
+        "priority": 5,
+        "speed_multiplier": 1.0
+      },
+      "minecraft:behavior.random_look_around": {
+        "priority": 6
+      },
+      "minecraft:type_family": {
+        "family": [ "blaze", "monster", "mob" ]
+      },
+      "minecraft:physics": {
+      },
+      "minecraft:pushable": {
+        "is_pushable": true,
+        "is_pushable_by_piston": true
       }
     },
-    "components": {
-      "minecraft:type_family": {
-        "family": [
-          "despawnear"
+    "events": {
+      "blaze_sword": {
+        "randomize": [
+          {
+            "weight": 995
+          },
+          {
+            "weight": 5,
+            "run_command": { "command": [ "structure load blaze_sword ~ ~ ~" ] }
+          }
         ]
-      },
-      "minecraft:despawn": {
-        "filters": {
-          "all_of": [
-            {
-              "test": "is_family",
-              "subject": "self",
-              "value": "despawnear"
-            }
-          ]
-        }
-      },
-      "minecraft:health": {
-        "value": 1
-      },
-      "minecraft:collision_box": {
-       "width": 0.0,
-       "height": 0.0
-     },
-      "minecraft:fire_immune": true,
-      "minecraft:physics": {}
+      }
     }
   }
 }
```

### `Swords_B/entities/creeper.json`

```diff
--- 1.6/Sword_B/entities/creeper.json
+++ 2.8.14/Swords_B/entities/creeper.json
@@ -1,46 +1,430 @@
 {
-  "format_version": "1.11.0",
+  "format_version": "1.13.0",
   "minecraft:entity": {
     "description": {
-      "identifier": "entity:creeper",
-      "is_spawnable": false,
+      "identifier": "minecraft:creeper",
+      "is_spawnable": true,
       "is_summonable": true,
-      "is_experimental": false,
-      "scripts": {
-        "animate": [
-          "creeper"
-        ]
-      },
-      "animations": {
-        "creeper": "controller.animation.creeper"
-      }
+      "is_experimental": false
     },
-    "components": {
-      "minecraft:type_family": {
-        "family": [
-          "despawnear"
-        ]
-      },
-      "minecraft:despawn": {
-        "filters": {
-          "all_of": [
-            {
-              "test": "is_family",
-              "subject": "self",
-              "value": "despawnear"
-            }
-          ]
+    "component_groups": {
+      "minecraft:minicreeper_projectile": {
+        "minecraft:projectile": {
+          "on_hit": {
+           "definition_event": {
+            "affect_projectile": true,
+            "event_trigger": {
+              "event": "minecraft:stop_projectile",
+              "target": "self"
+              }
+            },
+            "impact_damage": {
+              "damage": 1,
+              "knockback": true
+            }
+          },
+          "power": 1,
+          "gravity": 0.02,
+          "inertia": 1,
+          "liquid_inertia": 1
         }
       },
-      "minecraft:health": {
-        "value": 1
+      "minecraft:minicreeper": {
+        "minecraft:timer": { "time": [ 10, 10 ], "looping": true, "randomInterval": false,
+        "time_down_event": { "event": "start_minicreeper_exploding", "target": "self" }
+        },
+        "minecraft:scale": { "value": 0.3 },
+        "minecraft:behavior.nearest_attackable_target": {
+          "priority": 1,
+          "entity_types": [
+            {
+              "filters": {
+                "test": "is_family",
+                "subject": "other",
+                "value": "monster"
+              },
+              "max_dist": 16
+            }
+          ],
+          "must_see": true,
+          "must_see_forget_duration": 0.0
+          },
+          "minecraft:type_family": {
+          "family": [ "creeper", "player", "mob", "effect99_entities" ]
+          },
+          "minecraft:target_nearby_sensor": {
+            "inside_range": 2.5,
+            "must_see": true,
+            "on_inside_range": {
+              "event": "start_minicreeper_exploding",
+              "target": "self"
+            }
+          },
+          "minecraft:damage_sensor": {
+            "triggers": {
+              "on_damage": {
+                "filters": { "any_of": [ { "test": "has_damage", "subject": "self", "operator": "!=", "value": "void" } ] },
+                 "event": "start_minicreeper_exploding"
+              },
+              "deals_damage": true
+            }
+          }
+        },
+        "minecraft:minicreeper_exploding": {
+          "minecraft:damage_sensor": {
+            "triggers": {
+              "cause": "all",
+              "deals_damage": false
+            }
+          },
+          "minecraft:explode": {
+            "fuse_length": 1.5,
+            "fuse_lit": true,
+            "power": 1,
+            "causes_fire": false,
+            "destroy_affected_by_griefing": true
+          }
+        },
+        "minecraft:exploding": {
+          "minecraft:explode": {
+            "fuse_length": 1.5,
+            "fuse_lit": true,
+            "power": 3,
+            "causes_fire": false,
+            "destroy_affected_by_griefing": true
+          }
+        },
+        "minecraft:charged_creeper": {
+          "minecraft:is_charged": {
+          }
+        },
+        "minecraft:charged_exploding": {
+          "minecraft:explode": {
+            "fuse_length": 1.5,
+            "fuse_lit": true,
+            "power": 6,
+            "causes_fire": false,
+            "destroy_affected_by_griefing": true
+          }
+        },
+        "minecraft:forced_exploding": {
+          "minecraft:target_nearby_sensor": {
+          },
+          "minecraft:explode": {
+            "fuse_length": 1.5,
+            "fuse_lit": true,
+            "power": 3,
+            "causes_fire": false,
+            "destroy_affected_by_griefing": true
+          },
+          "minecraft:on_target_escape": {
+          }
+        },
+        "minecraft:forced_charged_exploding": {
+          "minecraft:timer": { "time": [ 1.4, 1.4 ], "looping": false,
+           "time_down_event": { "event": "creeper_sword", "target": "self" }
+          },
+          "minecraft:target_nearby_sensor": {
+          },
+          "minecraft:explode": {
+            "fuse_length": 1.5,
+            "fuse_lit": true,
+            "power": 6,
+            "causes_fire": false,
+            "destroy_affected_by_griefing": true
+          },
+          "minecraft:on_target_escape": {
+          }
+        }
       },
-      "minecraft:collision_box": {
-       "width": 0.0,
-       "height": 0.0
-     },
-      "minecraft:fire_immune": true,
-      "minecraft:physics": {}
+      "components": {
+        "minecraft:experience_reward": {
+          "on_death": "query.last_hit_by_player ? 5 : 0"
+        },
+        "minecraft:type_family": {
+          "family": [ "creeper", "monster", "mob" ]
+        },
+        "minecraft:breathable": {
+          "total_supply": 15,
+          "suffocate_time": 0
+        },
+        "minecraft:nameable": {
+        },
+        "minecraft:collision_box": {
+          "width": 0.6,
+          "height": 1.8
+        },
+        "minecraft:movement": {
+          "value": 0.2
+        },
+        "minecraft:navigation.walk": {
+        "can_path_over_water": true
+        },
+        "minecraft:movement.basic": {
+
+        },
+        "minecraft:jump.static": {
+        },
+        "minecraft:can_climb": {
+        },
+        "minecraft:loot": {
+          "table": "loot_tables/entities/creeper.json"
+        },
+        "minecraft:health": {
+          "value": 20,
+          "max": 20
+        },
+        "minecraft:hurt_on_condition": {
+          "damage_conditions": [
+            {
+              "filters": { "test": "in_lava", "subject": "self", "operator": "==", "value": true },
+              "cause": "lava",
+              "damage_per_tick": 4
+            }
+          ]
+        },
+        "minecraft:attack": {
+          "damage": 3
+        },
+        "minecraft:damage_sensor": {
+          "triggers": {
+            "on_damage": {
+              "filters": {
+                "test": "is_family",
+                "subject": "other",
+                "value": "lightning"
+              },
+              "event": "minecraft:become_charged"
+            },
+            "deals_damage": false
+          }
+        },
+        "minecraft:target_nearby_sensor": {
+          "inside_range": 2.5,
+          "outside_range": 6.0,
+          "must_see": true,
+          "on_inside_range": {
+            "event": "minecraft:start_exploding",
+            "target": "self"
+          },
+          "on_outside_range": {
+            "event": "minecraft:stop_exploding",
+            "target": "self"
+          },
+          "on_vision_lost_inside_range": {
+            "event": "minecraft:stop_exploding",
+            "target": "self"
+          }
+        },
+        "minecraft:interact": {
+          "interactions": {
+            "on_interact": {
+              "filters": {
+                "all_of": [
+                  {
+                    "test": "is_family",
+                    "subject": "other",
+                    "value": "player"
+                  },
+                  {
+                    "test": "has_equipment",
+                    "domain": "hand",
+                    "subject": "other",
+                    "value": "flint_and_steel"
+                  },
+                  {
+                    "test": "has_component",
+                    "operator": "!=",
+                    "value": "minecraft:explode"
+                  }
+                ]
+              },
+              "event": "minecraft:start_exploding_forced",
+              "target": "self"
+            },
+            "hurt_item": 1,
+            "swing": true,
+            "play_sounds": "ignite",
+            "interact_text": "action.interact.creeper"
+          }
+        },
+        "minecraft:behavior.float": {
+          "priority": 0
+        },
+        "minecraft:behavior.swell": {
+          "start_distance": 2.5,
+          "stop_distance": 6.0,
+          "priority": 2
+        },
+        "minecraft:behavior.melee_attack": {
+          "priority": 4,
+          "speed_multiplier": 1.25,
+          "track_target": false,
+          "reach_multiplier":  0.0
+        },
+        "minecraft:behavior.avoid_mob_type": {
+          "priority": 3,
+          "entity_types": [
+            {
+              "filters": {
+                "any_of": [
+                  { "test" :  "is_family", "subject" : "other", "value" :  "ocelot"},
+                  { "test" :  "is_family", "subject" : "other", "value" :  "cat"}
+                ]
+              },
+              "max_dist": 6,
+              "walk_speed_multiplier": 1,
+              "sprint_speed_multiplier": 1.2
+            }
+          ]
+        },
+        "minecraft:behavior.random_stroll": {
+          "priority": 5,
+          "speed_multiplier": 1
+        },
+        "minecraft:behavior.look_at_player": {
+          "priority": 6,
+          "look_distance": 8
+        },
+        "minecraft:behavior.random_look_around": {
+          "priority": 6
+        },
+        "minecraft:behavior.nearest_attackable_target": {
+          "priority": 1,
+          "entity_types": [
+            {
+              "filters": {
+                "test": "is_family",
+                "subject": "other",
+                "value": "player"
+              },
+              "max_dist": 16
+            }
+          ],
+          "must_see": true,
+          "must_see_forget_duration": 0.0
+        },
+        "minecraft:behavior.hurt_by_target": {
+          "priority": 2
+        },
+        "minecraft:physics": {
+        },
+        "minecraft:pushable": {
+          "is_pushable": true,
+          "is_pushable_by_piston": true
+        },
+        "minecraft:on_target_escape": {
+          "event": "minecraft:stop_exploding",
+          "target": "self"
+        }
+      },
+      "events": {
+        "minecraft:entity_spawned": {
+        "sequence": [
+          {
+            "filters": { "test": "has_equipment", "subject": "other", "domain": "hand", "value": "effect:creeper_sword" },
+            "add": {
+              "component_groups": [ "minecraft:minicreeper", "minecraft:minicreeper_projectile" ]
+              }
+            }
+          ]
+        },
+        "creeper_sword": {
+          "randomize": [
+            {
+              "weight": 95
+            },
+            {
+              "weight": 5,
+              "run_command": { "command": [ "structure load creeper_sword ~ ~ ~" ] }
+            }
+          ]
+        },
+        "minecraft:start_exploding_forced": {
+          "sequence": [
+            {
+              "filters": {
+                "test": "has_component",
+                "operator": "!=",
+                "value": "minecraft:is_charged"
+              },
+              "add": {
+                "component_groups": [
+                  "minecraft:forced_exploding"
+                ]
+              }
+            },
+            {
+              "filters": {
+                "test": "has_component",
+                "value": "minecraft:is_charged"
+              },
+              "add": {
+                "component_groups": [
+                  "minecraft:forced_charged_exploding"
+                ]
+              }
+            }
+          ]
+        },
+        "minecraft:start_exploding": {
+          "sequence": [
+            {
+              "filters": {
+                "test": "has_component",
+                "operator": "!=",
+                "value": "minecraft:is_charged"
+              },
+              "add": {
+                "component_groups": [
+                  "minecraft:exploding"
+                ]
+              }
+            },
+            {
+              "filters": {
+                "test": "has_component",
+                "value": "minecraft:is_charged"
+              },
+              "add": {
+                "component_groups": [
+                  "minecraft:charged_exploding"
+                ]
+              }
+            }
+          ]
+        },
+        "minecraft:stop_exploding": {
+          "remove": {
+            "component_groups": [
+              "minecraft:exploding"
+            ]
+          }
+        },
+        "minecraft:become_charged": {
+          "remove": {
+            "component_groups": [
+              "minecraft:exploding"
+            ]
+          },
+          "add": {
+            "component_groups": [
+              "minecraft:charged_creeper"
+            ]
+          }
+        },
+        "minecraft:minicreeper": { "add": { "component_groups": [ "minecraft:minicreeper" ] } 
+        },
+        "minecraft:stop_projectile": { "remove": { "component_groups": [ "minecraft:minicreeper_projectile" ] } 
+        },
+        "start_minicreeper_exploding": {
+          "add": {
+            "component_groups": [
+              "minecraft:minicreeper_exploding"
+              ]
+            }
+          }
+        }
+      }
     }
   }
-}
```

### `Swords_B/entities/fire.json`

```diff
--- 1.6/Sword_B/entities/fire.json
+++ 2.8.14/Swords_B/entities/fire.json
@@ -3,44 +3,58 @@
   "minecraft:entity": {
     "description": {
       "identifier": "entity:fire",
+      "runtime_identifier": "minecraft:snowball",
       "is_spawnable": false,
       "is_summonable": true,
-      "is_experimental": false,
-      "scripts": {
-        "animate": [
-          "fire"
-        ]
-      },
-      "animations": {
-        "fire": "controller.animation.fire"
+      "is_experimental": false
+    },
+    "component_groups": {
+      "fire_sword": {
+        "minecraft:projectile": {
+        "on_hit": {
+          "impact_damage": {
+            "damage": 1,
+            "knockback": false,
+            "catch_fire": true,
+            "semi_random_diff_damage": false
+          },
+          "catch_fire": {
+            "fire_affected_by_griefing": true
+          },
+          "remove_on_hit": {}
+        },
+        "power": 10,
+        "gravity": 0.1,
+        "inertia": 1,
+        "liquid_inertia": 1,
+        "reflect_on_hurt": true
+        }
       }
     },
     "components": {
-      "minecraft:type_family": {
-        "family": [
-          "despawnear"
+      "minecraft:type_family": { "family": [ "effect99_entities" ] },
+      "minecraft:despawn": {},
+      "minecraft:collision_box": { "width": 0.1, "height": 0.1 },
+      "minecraft:physics": {},
+      "minecraft:projectile": {
+       "on_hit": {
+         "impact_damage": { "damage": 0, "catch_fire": true },
+         "remove_on_hit": {}
+       },
+       "power": 1, "gravity": 0.01
+      }
+    },
+    "events": {
+      "minecraft:entity_spawned": {
+        "sequence": [
+         {
+          "filters": { "test": "has_equipment", "subject": "other", "domain": "hand", "value": "effect:fire_sword" },
+            "add": {
+             "component_groups": [ "fire_sword" ]
+            }
+          }
         ]
-      },
-      "minecraft:despawn": {
-        "filters": {
-          "all_of": [
-            {
-              "test": "is_family",
-              "subject": "self",
-              "value": "despawnear"
-            }
-          ]
-        }
-      },
-      "minecraft:health": {
-        "value": 1
-      },
-      "minecraft:collision_box": {
-       "width": 0.0,
-       "height": 0.0
-     },
-      "minecraft:fire_immune": true,
-      "minecraft:physics": {}
+      }
     }
   }
 }
```

### `Swords_B/entities/grass.json`

```diff
--- 1.6/Sword_B/entities/grass.json
+++ 2.8.14/Swords_B/entities/grass.json
@@ -5,42 +5,61 @@
       "identifier": "entity:grass",
       "is_spawnable": false,
       "is_summonable": true,
-      "is_experimental": false,
-      "scripts": {
-        "animate": [
-          "grass"
-        ]
+      "is_experimental": false
+    },
+    "component_groups": {
+      "despawn": { "minecraft:despawn": {} 
       },
-      "animations": {
-        "grass": "controller.animation.grass"
+      "start_despawn": {
+        "minecraft:timer": { "time": [ 0.52, 0.52 ], "looping": false,
+         "time_down_event": { "event": "despawn", "target": "self" }
+        }      
+      },
+      "grass_sword": {
+        "minecraft:timer": { "time": [ 1.08, 1.08 ], "looping": false,
+         "time_down_event": { "event": "grass_sword_skill", "target": "self" }
+        }      
       }
     },
     "components": {
-      "minecraft:type_family": {
-        "family": [
-          "despawnear"
+      "minecraft:type_family": { "family": [ "effect99_entities" ] },
+      "minecraft:collision_box": { "width": 0.0, "height": 0.0 },
+      "minecraft:damage_sensor": { "triggers": { "cause": "all", "deals_damage": false } },
+      "minecraft:physics": { "has_gravity": false, "has_collision": false },
+      "minecraft:pushable": { "is_pushable": false, "is_pushable_by_piston": false }
+    },
+    "events": {
+      "minecraft:entity_spawned": {
+        "sequence": [ {
+            "add": { "component_groups": [ "grass_sword" ] },
+              "run_command": { "command": [ 
+                "playsound dig.grass @a[r=12]", 
+                "effect @e[type=!entity:grass,r=1] slowness 2 15 true",
+                "execute @e[family=!grass_witch,type=!entity:grass,type=!xp_orb,type=!arrow,r=1,tag=!grass] ~ ~ ~ tag @s add grass"
+              ] 
+            }
+          }
         ]
       },
-      "minecraft:despawn": {
-        "filters": {
-          "all_of": [
-            {
-              "test": "is_family",
-              "subject": "self",
-              "value": "despawnear"
-            }
-          ]
-        }
+      "grass_sword_skill": { 
+        "run_command": { "command": [
+          "playsound dig.grass @a[r=12] ~ ~ ~ 1 0.4",
+          "execute @e[type=!entity:grass,c=1,r=1,tag=grass] ~ ~ ~ detect ~ ~-1 ~ grass 0 execute @s ~ ~ ~ detect ~ ~ ~ air 0 tp @s ~ ~-1 ~",
+          "execute @e[type=!entity:grass,c=1,r=1,tag=grass] ~ ~ ~ detect ~ ~-1 ~ grass 0 execute @s ~ ~ ~ detect ~ ~ ~ tallgrass 0 tp @s ~ ~-1 ~",
+          "tag @e[tag=grass,r=2] remove grass"
+          ] 
+        },
+        "add": { "component_groups": [ "start_despawn" ] } 
       },
-      "minecraft:health": {
-        "value": 1
-      },
-      "minecraft:collision_box": {
-       "width": 0.0,
-       "height": 0.0
-     },
-      "minecraft:fire_immune": true,
-      "minecraft:physics": {}
+      "despawn": {
+        "sequence": [ 
+          { "add": { "component_groups": [ "despawn" ] } },
+          { "randomize": [
+            { "weight": 50, "run_command": { "command": [ "fill ~ ~ ~ ~ ~ ~ tallgrass 0 replace air" ] } },
+            { "weight": 50 } ] 
+          }
+        ]
+      }
     }
   }
 }
```

### `Swords_B/entities/player.json`

```diff
--- 1.6/Sword_B/entities/player.json
+++ 2.8.14/Swords_B/entities/player.json
@@ -7,322 +7,479 @@
       "is_summonable": false,
       "is_experimental": false,
       "scripts": {
-        "animate": [
-          "normal"
-        ]
+        "animate": [ "shulker_sword", "wither_sword", "wolf_sword_0", "wolf_sword_1", "wolf_sword_2", "ghost_sword" ]
       },
       "animations": {
-        "normal": "controller.animation.normal"
+        "shulker_sword": "controller.animation.shulker_sword",
+        "wither_sword": "controller.animation.wither_sword",
+        "wolf_sword_1": "controller.animation.start_wolf_sword",
+        "wolf_sword_2": "controller.animation.end_wolf_sword",
+        "wolf_sword_0": "controller.animation.wolf_sword",
+        "ghost_sword": "controller.animation.ghost_sword"
       }
     },
     "component_groups": {
-      "minecraft:normal_player": {
-        "minecraft:spell_effects": {},
+      "minecraft:bee_sword": {
+        "minecraft:timer": { "time": [ 3, 8 ], "looping": true, "randomInterval": true,
+        "time_down_event": { "event": "bee_sword_flower", "target": "self" }
+        },
+        "minecraft:type_family": { "family": [ "player", "bee_sword" ] }
+      },
+      "minecraft:nether_star_sword": {
+        "minecraft:damage_sensor": { "triggers": { "on_damage": { "filters": { "all_of": [
+         { "test": "is_family", "subject": "other", "value": "nether_star_projectile" } ] } },
+           "deals_damage": false }
+        },
+        "minecraft:type_family": { "family": [ "player", "nether_star_sword" ] }
+      },
+      "minecraft:clock_sword": {
+        "minecraft:type_family": { "family": [ "player", "clock_sword" ] }
+      },
+      "clock_sword_skill": {
+        "minecraft:timer": { "time": [ 5, 5 ], "looping": true, "randomInterval": false,
+        "time_down_event": { "event": "stop_clock_sword_event", "target": "self" }
+        },
+        "minecraft:type_family": { "family": [ "player", "clock_sword", "clock_sword_skill" ] }
+      },
+      "clock_sword_movement": {
+        "minecraft:movement": { "value": 1 }
+      },
+      "minecraft:ghost_sword": {
+        "minecraft:scale": {
+          "value": 1.05
+        },
+        "minecraft:knockback_resistance": {
+          "value": 1.0
+        },
+        "minecraft:collision_box": {
+          "width": 0.0, "height": 0.0
+        },
+        "minecraft:breathable": { "total_supply": 15, "suffocate_time": 0, "inhale_time": 3.75, 
+         "generates_bubbles": false, "breathes_water": true, "breathes_air": true, "breathes_lava": true
+        },
+        "minecraft:damage_sensor": { "triggers": { "cause": "all", "deals_damage": false }
+      },
+      "minecraft:type_family": { "family": [ "ghost_sword" ] }
+      },
+      "ghost_movement": {
+        "minecraft:movement": { "value": 0.14 }
+      },
+      "minecraft:wolf_sword": {
+        "minecraft:type_family": { "family": [ "player", "wolf_sword" ] }
+      },
+      "wolf_transformation": {
+        "minecraft:type_family": { "family": [ "player", "wolf_sword", "wolf_transformation" ] }
+      },
+      "complete_wolf_transformation": {
+        "minecraft:damage_sensor": {
+          "triggers": [
+            {
+              "on_damage": {  "filters": { "all_of": [ { "test": "has_damage", "operator": "!=", "value": "void" } ] },
+                "event": "wolf_damage_sound"
+              },
+              "deals_damage": true
+            }
+          ]
+        },
+        "minecraft:timer": { "time": [ 3, 6 ], "looping": true, "randomInterval": true,
+          "time_down_event": { "event": "wolf_sword_sounds", "target": "self" }
+        },
         "minecraft:attack": {
-          "damage": 1
-        }
-      },
-      "minecraft:spectral_sword": {
-        "minecraft:spawn_entity": [
-          {
-            "min_wait_time": 0,
-            "max_wait_time": 0,
-            "spawn_entity": "entity:spectral",
-            "num_to_spawn": 1,
-            "single_use": true
-          }
-        ]
-      },
-      "minecraft:magma_sword": {
-        "minecraft:spawn_entity": [
-          {
-            "min_wait_time": 0,
-            "max_wait_time": 0,
-            "spawn_entity": "entity:magma",
-            "num_to_spawn": 1,
-            "single_use": true
-          }
-        ]
-      },
-      "minecraft:lightning_sword": {
-        "minecraft:spawn_entity": [
-          {
-            "min_wait_time": 0,
-            "max_wait_time": 0,
-            "spawn_entity": "entity:lightning",
-            "num_to_spawn": 1,
-            "single_use": true
-          }
-        ]
-      },
-      "minecraft:lapis_sword": {
-        "minecraft:spawn_entity": [
-          {
-            "min_wait_time": 0,
-            "max_wait_time": 0,
-            "spawn_entity": "entity:lapis",
-            "num_to_spawn": 1,
-            "single_use": true
-          }
-        ]
-      },
-      "minecraft:jungle_sword": {
-        "minecraft:spawn_entity": [
-          {
-            "min_wait_time": 0,
-            "max_wait_time": 0,
-            "spawn_entity": "entity:jungle",
-            "num_to_spawn": 1,
-            "single_use": true
-          }
-        ]
-      },
-      "minecraft:slime_sword": {
-        "minecraft:spawn_entity": [
-          {
-            "min_wait_time": 0,
-            "max_wait_time": 0,
-            "spawn_entity": "entity:slime",
-            "num_to_spawn": 1,
-            "single_use": true
-          }
-        ]
-      },
-      "minecraft:shulker_sword": {
-        "minecraft:spawn_entity": [
-          {
-            "min_wait_time": 0,
-            "max_wait_time": 0,
-            "spawn_entity": "entity:shulker",
-            "num_to_spawn": 1,
-            "single_use": true
-          }
-        ]
-      },
-      "minecraft:sea_sword": {
-        "minecraft:spawn_entity": [
-          {
-            "min_wait_time": 0,
-            "max_wait_time": 0,
-            "spawn_entity": "entity:sea",
-            "num_to_spawn": 1,
-            "single_use": true
-          }
-        ]
-      },
-      "minecraft:grass_sword": {
-        "minecraft:spawn_entity": [
-          {
-            "min_wait_time": 0,
-            "max_wait_time": 0,
-            "spawn_entity": "entity:grass",
-            "num_to_spawn": 1,
-            "single_use": true
-          }
-        ]
-      },
-      "minecraft:glowstone_sword": {
-        "minecraft:spawn_entity": [
-          {
-            "min_wait_time": 0,
-            "max_wait_time": 0,
-            "spawn_entity": "entity:glow",
-            "num_to_spawn": 1,
-            "single_use": true
-          }
-        ]
-      },
-      "minecraft:fire_sword": {
-        "minecraft:spawn_entity": [
-          {
-            "min_wait_time": 0,
-            "max_wait_time": 0,
-            "spawn_entity": "entity:fire",
-            "num_to_spawn": 1,
-            "single_use": true
-          }
-        ]
+          "damage": 15
+        },
+        "minecraft:type_family": { "family": [ "wolf", "wolf_sword", "complete_wolf_transformation", "monster" ] }
+      },
+      "wolf_movement": {
+        "minecraft:movement": { "value": 0.18 }
+      },
+      "minecraft:ultra_instinct_sword": {
+        "minecraft:knockback_resistance": { "value": 1.0 },
+        "minecraft:timer": { "time": [ 0.1, 0.2 ], "looping": true, "randomInterval": true,
+        "time_down_event": { "event": "ultra_instinct_sword_effects", "target": "self" }
+        },
+        "minecraft:damage_sensor": {
+          "triggers": [
+            {
+              "on_damage": {  "filters": { "all_of": [
+                { "test": "has_damage", "operator": "!=", "value": "lava" },
+                { "test": "has_damage", "operator": "!=", "value": "drowning" },
+                { "test": "has_damage", "operator": "!=", "value": "void" },
+                { "test": "has_damage", "operator": "!=", "value": "thorns" },
+                { "test": "has_damage", "operator": "!=", "value": "suicide" },
+                { "test": "has_damage", "operator": "!=", "value": "starve" },
+                { "test": "has_damage", "operator": "!=", "value": "fire" },
+                { "test": "has_damage", "operator": "!=", "value": "fire_tick" },
+                { "test": "has_damage", "operator": "!=", "value": "magic" } ] },
+                "event": "ultra_instinct_sword_skill"
+              },
+              "deals_damage": false
+            },
+            {
+              "on_damage": {  "filters": { "test": "has_damage", "value": "fire" }
+              },
+              "deals_damage": false
+            },
+            {
+              "on_damage": {  "filters": { "test": "has_damage", "value": "fire_tick" }
+              },
+              "deals_damage": false
+            },
+            {
+              "on_damage": {  "filters": { "any_of": [ 
+                { "test": "has_damage", "value": "block_explosion" },
+                { "test": "has_damage", "value": "entity_explosion" } ] }
+              },
+              "deals_damage": false
+            },
+            {
+              "on_damage": {  "filters": { "all_of": [ 
+                { "test": "has_damage", "value": "lava" } ] }
+              },
+              "deals_damage": true
+            }
+          ]
+        },
+        "minecraft:type_family": { "family": [ "player", "ultra_instinct_sword" ] }
+      },
+      "ultra_instinct_sword_movement": {
+        "minecraft:movement": { "value": 0.22 }
       },
       "minecraft:ender_sword": {
-        "minecraft:spawn_entity": [
-          {
-            "min_wait_time": 0,
-            "max_wait_time": 0,
-            "spawn_entity": "entity:ender",
-            "num_to_spawn": 1,
-            "single_use": true
-          }
-        ],
-        "minecraft:teleport": {
-          "random_teleports": true,
-          "max_random_teleport_time": 30,
-          "random_teleport_cube": [
-            32,
-            32,
-            32
-          ],
-          "target_distance": 16,
-          "target_teleport_chance": 0.05,
-          "light_teleport_chance": 0.05
+        "minecraft:damage_sensor": {
+          "triggers": [
+            {
+              "on_damage": {  "filters": { "all_of": [ { "test": "has_damage", "subject": "self", "operator": "!=", "value": "projectile" } ] },
+                "event": "ender_sword_skill"
+              },
+              "deals_damage": true
+            },
+            {
+              "on_damage": {  "filters": { "all_of": [ { "test": "has_damage", "subject": "self", "value": "projectile" } ] },
+                "event": "ender_sword_tp"
+              },
+              "deals_damage": false
+            },
+            {
+              "on_damage": {  "filters": { "all_of": [ { "test": "in_water_or_rain" } ] },
+                "event": "ender_sword_tp"
+              },
+              "deals_damage": true
+            }
+          ]
         },
         "minecraft:hurt_on_condition": {
           "damage_conditions": [
             {
-              "filters": {
-                "test": "in_water_or_rain",
-                "operator": "==",
-                "value": true
-              },
+              "filters": { "test": "in_water_or_rain" },
               "cause": "drowning",
               "damage_per_tick": 1
             }
           ]
-        }
+        },
+        "minecraft:type_family": { "family": [ "player", "ender_sword" ] },
+        "minecraft:timer": { "time": [ 6, 18 ], "looping": true, "randomInterval": true,
+        "time_down_event": { "event": "ender_sword_sound", "target": "self" }
+        }
+      },
+      "minecraft:lightning_sword": {
+        "minecraft:damage_sensor": { "triggers": { "on_damage": { "filters": { "all_of": [
+         { "test": "is_family", "subject": "other", "value": "lightning" } ] } },
+           "deals_damage": false }
+        },
+        "minecraft:type_family": { "family": [ "player", "lightning_sword" ] }
+      },
+      "minecraft:wither_sword": {
+        "minecraft:rideable": {
+          "seat_count": 1,
+          "family_types": [ "entity_name" ],
+          "seats": { "position": [ 0.0, 0.4, 0.0 ], "lock_rider_rotation": 0 }
+        },
+        "minecraft:damage_sensor": { "triggers": { "on_damage": { "filters": { "all_of": [
+         { "test": "has_damage", "subject": "self", "value": "wither" } ] } },
+           "deals_damage": false }
+        },
+        "minecraft:timer": { "time": [ 4, 18 ], "looping": true, "randomInterval": true,
+          "time_down_event": { "event": "wither_sword_effects", "target": "self" }
+        },
+        "minecraft:type_family": { "family": [ "player", "wither_sword" ] }
+      },
+      "minecraft:time_sword": {
+        "minecraft:movement": { "value": 1 },
+        "minecraft:type_family": { "family": [ "player", "time_sword" ] }
+      },
+      "time_sword_movement": {
+        "minecraft:movement": { "value": 1 }
+      },
+      "minecraft:sponge_sword": {
+        "minecraft:type_family": { "family": [ "player", "sponge_sword" ] }
+      },
+      "minecraft:spider_sword": {
+        "minecraft:type_family": { "family": [ "player", "spider_sword" ] }
+      },
+      "spider_sword_skill": {
+        "minecraft:spawn_entity": [
+          { "min_wait_time": 0, "max_wait_time": 0, "single_use": false, "spawn_entity": "entity:web", "num_to_spawn": 1 }
+        ],
+        "minecraft:timer": { "time": [ 2, 2 ], "looping": false,
+         "time_down_event": { "event": "stop_spider_skill_event", "target": "self" }
+        },
+        "minecraft:type_family": { "family": [ "player", "spider_sword", "spider_sword_skill" ] }
+      },
+      "minecraft:shulker_sword": {
+        "minecraft:scale": { "value": 1 },
+        "minecraft:type_family": { "family": [ "player", "shulker_sword" ] }
+      },
+      "shulker_sword_skill": {
+        "minecraft:damage_sensor": {
+          "triggers": [
+            { "cause": "all", "deals_damage": false }
+          ]
+        },
+        "minecraft:scale": { "value": 0.7 },
+        "minecraft:type_family": { "family": [ "player", "shulker_sword" ] }
+      },
+      "minecraft:slime_sword": {
+        "minecraft:type_family": { "family": [ "player", "slime_sword" ] },
+        "minecraft:timer": { "time": [ 0.4, 0.4 ], "looping": false,
+         "time_down_event": { "event": "slime_sword_skills", "target": "self" }
+        },
+        "minecraft:damage_sensor": { "triggers": { "on_damage": { "filters": { "all_of": [
+         { "test": "is_family", "subject": "other", "value": "tamed_slime" } ] } },
+           "deals_damage": false }
+        }
+      },
+      "minecraft:spectral_sword": {
+        "minecraft:timer": { "time": [ 0.4, 0.4 ], "looping": false,
+         "time_down_event": { "event": "spectral_sword_skills", "target": "self" }
+        },
+        "minecraft:rideable": {
+          "seat_count": 1,
+          "family_types": [ "ender_crystal", "spectral_sword" ],
+          "seats": { "position": [ 0.0, 0.4, 0.0 ], "lock_rider_rotation": 0 }
+        },
+        "minecraft:type_family": { "family": [ "player", "spectral_sword" ] }
+      },
+      "minecraft:sea_sword": {
+        "minecraft:collision_box": {
+          "width": 0.6,
+          "height": 0.9
+        },
+        "minecraft:timer": { "time": [ 0.5, 0.5 ], "looping": true,
+         "time_down_event": { "event": "sea_sword_sound", "target": "self" }
+        },
+        "minecraft:breathable": { "total_supply": 2, "suffocate_time": -1, "inhale_time": 3.75, 
+         "generates_bubbles": false, "breathes_water": true, "breathes_air": false, "breathes_lava": false
+        },
+        "minecraft:type_family": { "family": [ "player", "sea_sword" ] }
+      },
+      "mermaid_movement_out_water": {
+        "minecraft:movement": { "value": 0.06 }
+      },
+      "mermaid_movement_in_water": {
+        "minecraft:underwater_movement": {
+          "value": 0.07
+        }
+      },
+      "minecraft:quartz_sword": {
+        "minecraft:type_family": { "family": [ "player", "quartz_sword" ] }
+      },
+      "minecraft:obsidian_sword": {
+        "minecraft:damage_sensor": { "triggers": { "on_damage": { "filters": { "any_of": [
+         { "test": "has_damage", "subject": "self", "value": "block_explosion" },
+         { "test": "has_damage", "subject": "self", "value": "entity_explosion" } ] } },
+           "deals_damage": false }
+        },
+        "minecraft:type_family": { "family": [ "player", "obsidian_sword" ]
+        },
+        "minecraft:knockback_resistance": { "value": 1.0 }
+      },
+      "minecraft:lapis_sword": {
+        "minecraft:type_family": { "family": [ "player", "lapis_sword" ] },
+        "minecraft:timer": { "time": [ 2.5, 6.0 ], "looping": true,  "randomInterval": true,
+         "time_down_event": { "event": "lapis_sword_skills", "target": "self" }
+        }
+      },
+      "minecraft:ice_sword": {
+        "minecraft:type_family": { "family": [ "player", "ice_sword" ] }
+      },
+      "minecraft:magma_sword": {
+        "minecraft:damage_sensor": { "triggers": { "on_damage": { "filters": { "any_of": [
+         { "test": "has_damage", "subject": "self", "value": "fire_tick" },
+         { "test": "is_block", "subject": "block", "operator": "equals", "value": "magma" } ] } },
+           "deals_damage": false }
+        },
+        "minecraft:type_family": { "family": [ "player", "magma_sword" ] }
+      },
+      "minecraft:jungle_sword": {
+        "minecraft:type_family": { "family": [ "player", "jungle_sword" ] },
+        "minecraft:health": { "value": 8, "max": 8 }
+      },
+      "minecraft:grass_sword": {
+        "minecraft:type_family": { "family": [ "player", "grass_sword" ] },
+        "minecraft:timer": { "time": [ 0.2, 0.2 ], "looping": true,
+         "time_down_event": { "event": "grass_sword_skills", "target": "self" }
+        }
+      },
+      "minecraft:fire_sword": {
+        "minecraft:timer": { "time": [ 0.2, 0.7 ], "looping": true, "randomInterval": true,
+         "time_down_event": { "event": "fire_sword_sound", "target": "self" }
+        },
+        "minecraft:damage_sensor": { "triggers": { "on_damage": { "filters": { "any_of": [ 
+         { "test": "has_damage", "subject": "self", "value": "fire" },
+         { "test": "has_damage", "subject": "self", "value": "fire_tick" } ] } },
+           "deals_damage": false }
+        },
+        "minecraft:type_family": { "family": [ "player", "fire_sword" ] }
       },
       "minecraft:emerald_sword": {
-        "minecraft:spawn_entity": [
-          {
-            "min_wait_time": 0,
-            "max_wait_time": 0,
-            "spawn_entity": "entity:emerald",
-            "num_to_spawn": 1,
-            "single_use": true
-          }
-        ]
-      },
-      "minecraft:creeper_sword": {
-        "minecraft:spawn_entity": [
-          {
-            "min_wait_time": 0,
-            "max_wait_time": 0,
-            "spawn_entity": "entity:creeper",
-            "num_to_spawn": 1,
-            "single_use": true
-          }
-        ]
-      },
-      "minecraft:coal_sword": {
-        "minecraft:spawn_entity": [
-          {
-            "min_wait_time": 0,
-            "max_wait_time": 0,
-            "spawn_entity": "entity:coal",
-            "num_to_spawn": 1,
-            "single_use": true
-          }
-        ]
+        "minecraft:type_family": { "family": [ "player", "emerald_sword" ] }
+      },
+      "start_player_explode_event": {
+        "minecraft:movement": { "value": 0.0 },
+        "minecraft:timer": { "time": [ 1.5, 1.5 ], "looping": true,
+        "time_down_event": { "event": "start_player_explode", "target": "self" }
+        }
       },
       "minecraft:cactus_sword": {
-        "minecraft:spawn_entity": [
-          {
-            "min_wait_time": 0,
-            "max_wait_time": 0,
-            "spawn_entity": "entity:cactus",
-            "num_to_spawn": 1,
-            "single_use": true
-          }
-        ]
+        "minecraft:type_family": { "family": [ "player", "cactus_sword" ] },
+        "minecraft:timer": { "time": [ 0.5, 0.5 ], "looping": true,
+        "time_down_event": { "event": "cactus_sword_skills", "target": "self" }
+        }
+      },
+      "minecraft:bone_sword": {
+        "minecraft:type_family": { "family": [ "player", "bone_sword" ] },
+        "minecraft:timer": { "time": [ 1, 1 ], "looping": true,
+        "time_down_event": { "event": "bone_sword_skills", "target": "self" }
+        }
       },
       "minecraft:blaze_sword": {
-        "minecraft:spawn_entity": [
-          {
-            "min_wait_time": 0,
-            "max_wait_time": 0,
-            "spawn_entity": "entity:blaze",
-            "num_to_spawn": 1,
-            "single_use": true
-          }
-        ]
-      },
-      "minecraft:wither_sword": {
-        "minecraft:spawn_entity": [
-          {
-            "min_wait_time": 0,
-            "max_wait_time": 0,
-            "spawn_entity": "entity:wither",
-            "num_to_spawn": 1,
-            "single_use": true
-          }
-        ]
-      },
-      "minecraft:tnt_sword": {
-        "minecraft:spawn_entity": [
-          {
-            "min_wait_time": 0,
-            "max_wait_time": 0,
-            "spawn_entity": "entity:tnt_sword",
-            "num_to_spawn": 1,
-            "single_use": true
-          }
-        ]
-      },
-      "minecraft:sword_of_time": {
-        "minecraft:spawn_entity": [
-          {
-            "min_wait_time": 0,
-            "max_wait_time": 0,
-            "spawn_entity": "entity:time",
-            "num_to_spawn": 1,
-            "single_use": true
-          }
-        ]
-      },
-      "minecraft:sponge_sword": {
-        "minecraft:spawn_entity": [
-          {
-            "min_wait_time": 0,
-            "max_wait_time": 0,
-            "spawn_entity": "entity:sponge",
-            "num_to_spawn": 1,
-            "single_use": true
-          }
-        ]
-      },
-      "minecraft:spider_sword": {
-        "minecraft:spawn_entity": [
-          {
-            "min_wait_time": 0,
-            "max_wait_time": 0,
-            "spawn_entity": "entity:spider",
-            "num_to_spawn": 1,
-            "single_use": true
-          }
-        ]
-      },
-      "minecraft:ice_sword": {
-        "minecraft:spawn_entity": [
-          {
-            "min_wait_time": 0,
-            "max_wait_time": 0,
-            "spawn_entity": "entity:ice",
-            "num_to_spawn": 1,
-            "single_use": true
-          }
-        ]
-      },
-      "minecraft:obsidian_sword": {
-        "minecraft:spawn_entity": [
-          {
-            "min_wait_time": 0,
-            "max_wait_time": 0,
-            "spawn_entity": "entity:obsidian",
-            "num_to_spawn": 1,
-            "single_use": true
-          }
-        ]
-      },
-      "minecraft:bone_sword": {
-        "minecraft:spawn_entity": [
-          {
-            "min_wait_time": 0,
-            "max_wait_time": 0,
-            "spawn_entity": "entity:bone",
-            "num_to_spawn": 1,
-            "single_use": true
-          }
-        ]
-      },
-      "minecraft:quartz_sword": {},
+        "minecraft:damage_sensor": { "triggers": { "on_damage": { "filters": { "any_of": [ 
+         { "test": "has_damage", "subject": "self", "value": "fire" },
+         { "test": "has_damage", "subject": "self", "value": "fire_tick" } ] } },
+           "deals_damage": false }
+        },
+        "minecraft:hurt_on_condition": {
+          "damage_conditions": [
+            {
+              "filters": { "test": "in_water_or_rain" },
+              "cause": "drowning",
+              "damage_per_tick": 1
+            }
+          ]
+        },
+        "minecraft:type_family": { "family": [ "player", "blaze_sword" ] },
+        "minecraft:timer": { "time": [ 1, 1 ], "looping": true,
+        "time_down_event": { "event": "blaze_sword_effects", "target": "self" }
+        }
+      },
+      "blaze_sword_skill": {
+        "minecraft:type_family": { "family": [ "player", "blaze_sword", "blaze_sword_skill" ] },
+        "minecraft:timer": { "time": [ 6, 6 ], "looping": false,
+        "time_down_event": { "event": "blaze_sword_skill", "target": "self" }
+        }
+      },
+      "shoot_small_fireball": {
+        "minecraft:spawn_entity": [ 
+          {
+           "min_wait_time": 0,
+           "max_wait_time": 1, 
+           "single_use": true, 
+           "spawn_entity": "entity:fake_fireball",
+           "spawn_event": "set_sound",
+           "num_to_spawn": 1 
+          },
+          {
+           "min_wait_time": 0,
+           "max_wait_time": 1, 
+           "single_use": true, 
+           "spawn_entity": "entity:fake_fireball",
+           "spawn_event": "set_sound",
+           "num_to_spawn": 1 
+          },
+          {
+           "min_wait_time": 0,
+           "max_wait_time": 1,
+           "single_use": true,
+           "spawn_entity": "entity:fake_fireball",
+           "spawn_event": "set_sound",
+           "num_to_spawn": 1
+          },
+          {
+           "min_wait_time": 0,
+           "max_wait_time": 1,
+           "single_use": true,
+           "spawn_entity": "entity:fake_fireball",
+           "spawn_event": "set_sound",
+           "num_to_spawn": 1
+          }
+        ],
+        "minecraft:timer": { "time": [ 2, 2 ], "looping": false,
+        "time_down_event": { "event": "stop_blaze_sword_skill", "target": "self" }
+        }
+      },
+      "ultra_instinct_projectile": {
+        "minecraft:spawn_entity": [ { "min_wait_time": 0, "max_wait_time": 0, "single_use": true, "spawn_entity": "entity:ultra_instinct_projectile", "num_to_spawn": 1 } ]
+      },
+      "minecraft:default_player": {
+        "minecraft:damage_sensor": {},
+        "minecraft:timer": {},
+        "minecraft:physics": {
+        "has_gravity": true,
+        "has_collision": true
+        },
+        "minecraft:scale": { 
+          "value": 1 
+        },
+        "minecraft:attack": {
+          "damage": 1
+        },
+        "minecraft:collision_box": {
+          "width": 0.6,
+          "height": 1.8
+        },
+        "minecraft:type_family": {
+          "family": [ "player", "default_player" ]
+        },
+        "minecraft:movement": {
+          "value": 0.1
+        },
+        "minecraft:underwater_movement": {
+          "value": 0.02
+        },
+        "minecraft:health": {
+          "value": 20,
+          "max": 20
+        },
+        "minecraft:breathable": {
+        "total_supply": 15,
+        "suffocate_time": -1,
+        "inhale_time": 3.75,
+        "generates_bubbles": false
+        },
+        "minecraft:rideable": {
+        "seat_count": 2,
+        "family_types": [
+          "parrot_tame"
+        ],
+        "pull_in_entities": true,
+          "seats": [
+            {
+              "position": [ 0.4, -0.2, -0.1 ],
+              "min_rider_count": 0,
+              "max_rider_count": 0,
+              "lock_rider_rotation": 0
+            },
+            {
+              "position": [ -0.4, -0.2, -0.1 ],
+              "min_rider_count": 1,
+              "max_rider_count": 2,
+              "lock_rider_rotation": 0
+            }
+          ]
+        }
+      },
+      "despawn": { "minecraft:despawn": {}
+      },
       "minecraft:add_bad_omen": {
         "minecraft:spell_effects": {
           "add_effects": [
@@ -334,10 +491,7 @@
           ]
         },
         "minecraft:timer": {
-          "time": [
-            0,
-            0
-          ],
+          "time": [ 0.0, 0.0 ],
           "looping": false,
           "time_down_event": {
             "event": "minecraft:clear_add_bad_omen",
@@ -346,7 +500,8 @@
         }
       },
       "minecraft:clear_bad_omen_spell_effect": {
-        "minecraft:spell_effects": {}
+        "minecraft:spell_effects": {
+        }
       },
       "minecraft:raid_trigger": {
         "minecraft:raid_trigger": {
@@ -361,14 +516,13 @@
       }
     },
     "components": {
+      "minecraft:experience_reward": {
+        "on_death": "Math.Min(query.player_level * 7, 100)"
+      },
       "minecraft:type_family": {
-        "family": [
-          "player"
-        ]
-      },
-      "minecraft:is_hidden_when_invisible": {},
-      "minecraft:movement": {
-        "value": 0.1
+        "family": [ "player", "default_player" ]
+      },
+      "minecraft:is_hidden_when_invisible": {
       },
       "minecraft:loot": {
         "table": "loot_tables/empty.json"
@@ -377,7 +531,23 @@
         "width": 0.6,
         "height": 1.8
       },
-      "minecraft:can_climb": {},
+      "minecraft:can_climb": {
+      },
+      "minecraft:movement": {
+        "value": 0.1
+      },
+      "minecraft:hurt_on_condition": {
+        "damage_conditions": [
+          {
+            "filters": { "test": "in_lava", "subject": "self", "operator": "==", "value": true },
+            "cause": "lava",
+            "damage_per_tick": 4
+          }
+        ]
+      },
+      "minecraft:attack": {
+        "damage": 1
+      },
       "minecraft:player.saturation": {
         "value": 20
       },
@@ -394,16 +564,21 @@
         "max": 1
       },
       "minecraft:breathable": {
-        "totalSupply": 15,
-        "suffocateTime": -1,
-        "inhaleTime": 3.75,
-        "generatesBubbles": false
+        "total_supply": 15,
+        "suffocate_time": -1,
+        "inhale_time": 3.75,
+        "generates_bubbles": false
       },
       "minecraft:nameable": {
-        "alwaysShow": true,
-        "allowNameTagRenaming": false
-      },
-      "minecraft:physics": {},
+        "always_show": true,
+        "allow_name_tag_renaming": false
+      },
+      "minecraft:physics": {
+      },
+      "minecraft:pushable": {
+        "is_pushable": false,
+        "is_pushable_by_piston": true
+      },
       "minecraft:insomnia": {
         "days_until_insomnia": 3
       },
@@ -415,21 +590,13 @@
         "pull_in_entities": true,
         "seats": [
           {
-            "position": [
-              0.4,
-              -0.15,
-              0.04
-            ],
+            "position": [ 0.4, -0.2, -0.1 ],
             "min_rider_count": 0,
             "max_rider_count": 0,
             "lock_rider_rotation": 0
           },
           {
-            "position": [
-              -0.4,
-              -0.15,
-              0.04
-            ],
+            "position": [ -0.4, -0.2, -0.1 ],
             "min_rider_count": 1,
             "max_rider_count": 2,
             "lock_rider_rotation": 0
@@ -439,649 +606,1667 @@
       "minecraft:scaffolding_climber": {},
       "minecraft:environment_sensor": [
         {
-          "on_environment": {
-            "filters": {
-              "all_of": [
-                {
-                  "test": "has_mob_effect",
-                  "subject": "self",
-                  "value": "bad_omen"
-                },
-                {
-                  "test": "is_in_village",
-                  "subject": "self",
-                  "value": true
-                }
-              ]
-            },
-            "event": "minecraft:trigger_raid"
-          }
-        },
-        {
-          "on_environment": {
-            "filters": {
-              "all_of": [
-                {
-                  "test": "is_family",
-                  "subject": "self",
-                  "value": "player"
-                }
-              ]
-            },
-            "event": "minecraft:event_normal_player"
-          }
-        },
-        {
-          "on_environment": {
-            "filters": {
-              "all_of": [
-                {
-                  "test": "has_equipment",
-                  "subject": "self",
-                  "domain": "hand",
-                  "value": "effect:spectral_sword"
-                }
-              ]
+         "on_environment": {
+           "filters": {
+             "all_of": [
+               {
+                 "test": "has_mob_effect",
+                 "subject": "self",
+                 "value": "bad_omen"
+               },
+               {
+                 "test": "is_in_village",
+                 "subject": "self",
+                 "value": true
+               }
+             ]
+           },
+           "event": "minecraft:trigger_raid"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": {  "test": "is_family", "operator": "!=", "value": "null" },
+            "event": "minecraft:constant_events"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "any_of": [ { "test": "is_family", "subject": "self", "value": "default_player" }, { "test": "is_family", "subject": "self", "operator": "!=", "value": "spectral_sword" } ] 
+            },
+            "event": "minecraft:stop_sword_events"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "value": "effect:blaze_sword" } ] 
+            },
+            "event": "minecraft:blaze_sword"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "operator": "!=", "value": "effect:blaze_sword" } ] 
+            },
+            "event": "stop_blaze_sword_event"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "value": "effect:bone_sword" } ] 
+            },
+            "event": "minecraft:bone_sword"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "operator": "!=", "value": "effect:bone_sword" } ] 
+            },
+            "event": "stop_bone_sword_event"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "value": "effect:cactus_sword" } ] 
+            },
+            "event": "minecraft:cactus_sword"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "operator": "!=", "value": "effect:cactus_sword" } ] 
+            },
+            "event": "stop_cactus_sword_event"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "value": "effect:emerald_sword" } ] 
+            },
+            "event": "minecraft:emerald_sword"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "operator": "!=", "value": "effect:emerald_sword" } ] 
+            },
+            "event": "stop_emerald_sword_event"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "value": "effect:fire_sword" } ] 
+            },
+            "event": "minecraft:fire_sword"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "operator": "!=", "value": "effect:fire_sword" } ] 
+            },
+            "event": "stop_fire_sword_event"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "value": "effect:grass_sword" } ] 
+            },
+            "event": "minecraft:grass_sword"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "operator": "!=", "value": "effect:grass_sword" } ] 
+            },
+            "event": "stop_grass_sword_event"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "value": "effect:jungle_sword" } ] 
+            },
+            "event": "minecraft:jungle_sword"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "operator": "!=", "value": "effect:jungle_sword" } ] 
+            },
+            "event": "stop_jungle_sword_event"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "value": "effect:magma_sword" } ] 
+            },
+            "event": "minecraft:magma_sword"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "operator": "!=", "value": "effect:magma_sword" } ] 
+            },
+            "event": "stop_magma_sword_event"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "value": "effect:ice_sword" } ] 
+            },
+            "event": "minecraft:ice_sword"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "operator": "!=", "value": "effect:ice_sword" } ] 
+            },
+            "event": "stop_ice_sword_event"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "value": "effect:lapis_sword" } ] 
+            },
+            "event": "minecraft:lapis_sword"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "operator": "!=", "value": "effect:lapis_sword" } ] 
+            },
+            "event": "stop_lapis_sword_event"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "value": "effect:obsidian_sword" } ] 
+            },
+            "event": "minecraft:obsidian_sword"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "operator": "!=", "value": "effect:obsidian_sword" } ] 
+            },
+            "event": "stop_obsidian_sword_event"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "value": "effect:quartz_sword" } ] 
+            },
+            "event": "minecraft:quartz_sword"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "operator": "!=", "value": "effect:quartz_sword" } ] 
+            },
+            "event": "stop_quartz_sword_event"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "value": "effect:sea_sword" } ] 
+            },
+            "event": "minecraft:sea_sword"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "operator": "!=", "value": "effect:sea_sword" } ] 
+            },
+            "event": "stop_sea_sword_event"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "value": "effect:spectral_sword" } ] 
             },
             "event": "minecraft:spectral_sword"
           }
         },
         {
           "on_environment": {
-            "filters": {
-              "all_of": [
-                {
-                  "test": "has_equipment",
-                  "subject": "self",
-                  "domain": "hand",
-                  "value": "effect:blaze_sword"
-                }
-              ]
-            },
-            "event": "minecraft:blaze_sword"
-          }
-        },
-        {
-          "on_environment": {
-            "filters": {
-              "all_of": [
-                {
-                  "test": "has_equipment",
-                  "subject": "self",
-                  "domain": "hand",
-                  "value": "effect:cactus_sword"
-                }
-              ]
-            },
-            "event": "minecraft:cactus_sword"
-          }
-        },
-        {
-          "on_environment": {
-            "filters": {
-              "all_of": [
-                {
-                  "test": "has_equipment",
-                  "subject": "self",
-                  "domain": "hand",
-                  "value": "effect:coal_sword"
-                }
-              ]
-            },
-            "event": "minecraft:coal_sword"
-          }
-        },
-        {
-          "on_environment": {
-            "filters": {
-              "all_of": [
-                {
-                  "test": "has_equipment",
-                  "subject": "self",
-                  "domain": "hand",
-                  "value": "effect:creeper_sword"
-                }
-              ]
-            },
-            "event": "minecraft:creeper_sword"
-          }
-        },
-        {
-          "on_environment": {
-            "filters": {
-              "all_of": [
-                {
-                  "test": "has_equipment",
-                  "subject": "self",
-                  "domain": "hand",
-                  "value": "effect:emerald_sword"
-                }
-              ]
-            },
-            "event": "minecraft:emerald_sword"
-          }
-        },
-        {
-          "on_environment": {
-            "filters": {
-              "all_of": [
-                {
-                  "test": "has_equipment",
-                  "subject": "self",
-                  "domain": "hand",
-                  "value": "effect:ender_sword"
-                }
-              ]
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "operator": "!=", "value": "effect:spectral_sword" } ] 
+            },
+            "event": "stop_spectral_sword_event"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "value": "effect:slime_sword" } ] 
+            },
+            "event": "minecraft:slime_sword"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "operator": "!=", "value": "effect:slime_sword" } ] 
+            },
+            "event": "stop_slime_sword_event"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "value": "effect:shulker_sword" } ] 
+            },
+            "event": "minecraft:shulker_sword"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "operator": "!=", "value": "effect:shulker_sword" } ]
+            },
+            "event": "stop_shulker_sword_event"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "value": "effect:spider_sword" } ] 
+            },
+            "event": "minecraft:spider_sword"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "operator": "!=", "value": "effect:spider_sword" } ] 
+            },
+            "event": "stop_spider_sword_event"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "value": "effect:sponge_sword" } ] 
+            },
+            "event": "minecraft:sponge_sword"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "operator": "!=", "value": "effect:sponge_sword" } ] 
+            },
+            "event": "stop_sponge_sword_event"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "value": "effect:time_sword" } ] 
+            },
+            "event": "minecraft:time_sword"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "operator": "!=", "value": "effect:time_sword" } ] 
+            },
+            "event": "stop_time_sword_event"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "value": "effect:wither_sword" } ] 
+            },
+            "event": "minecraft:wither_sword"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "operator": "!=", "value": "effect:wither_sword" } ] 
+            },
+            "event": "stop_wither_sword_event"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "value": "effect:glowstone_sword" } ] 
+            },
+            "event": "minecraft:glowstone_sword"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "value": "effect:lightning_sword" } ] 
+            },
+            "event": "minecraft:lightning_sword"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "operator": "!=", "value": "effect:lightning_sword" } ] 
+            },
+            "event": "stop_lightning_sword_event"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "value": "effect:ender_sword" } ] 
             },
             "event": "minecraft:ender_sword"
           }
         },
         {
           "on_environment": {
-            "filters": {
-              "all_of": [
-                {
-                  "test": "has_equipment",
-                  "subject": "self",
-                  "domain": "hand",
-                  "value": "effect:fire_sword"
-                }
-              ]
-            },
-            "event": "minecraft:fire_sword"
-          }
-        },
-        {
-          "on_environment": {
-            "filters": {
-              "all_of": [
-                {
-                  "test": "has_equipment",
-                  "subject": "self",
-                  "domain": "hand",
-                  "value": "effect:glowstone_sword"
-                }
-              ]
-            },
-            "event": "minecraft:glowstone_sword"
-          }
-        },
-        {
-          "on_environment": {
-            "filters": {
-              "all_of": [
-                {
-                  "test": "has_equipment",
-                  "subject": "self",
-                  "domain": "hand",
-                  "value": "effect:grass_sword"
-                }
-              ]
-            },
-            "event": "minecraft:grass_sword"
-          }
-        },
-        {
-          "on_environment": {
-            "filters": {
-              "all_of": [
-                {
-                  "test": "has_equipment",
-                  "subject": "self",
-                  "domain": "hand",
-                  "value": "effect:ice_sword"
-                }
-              ]
-            },
-            "event": "minecraft:ice_sword"
-          }
-        },
-        {
-          "on_environment": {
-            "filters": {
-              "all_of": [
-                {
-                  "test": "has_equipment",
-                  "subject": "self",
-                  "domain": "hand",
-                  "value": "effect:jungle_sword"
-                }
-              ]
-            },
-            "event": "minecraft:jungle_sword"
-          }
-        },
-        {
-          "on_environment": {
-            "filters": {
-              "all_of": [
-                {
-                  "test": "has_equipment",
-                  "subject": "self",
-                  "domain": "hand",
-                  "value": "effect:lapis_sword"
-                }
-              ]
-            },
-            "event": "minecraft:lapis_sword"
-          }
-        },
-        {
-          "on_environment": {
-            "filters": {
-              "all_of": [
-                {
-                  "test": "has_equipment",
-                  "subject": "self",
-                  "domain": "hand",
-                  "value": "effect:lightning_sword"
-                }
-              ]
-            },
-            "event": "minecraft:lightning_sword"
-          }
-        },
-        {
-          "on_environment": {
-            "filters": {
-              "all_of": [
-                {
-                  "test": "has_equipment",
-                  "subject": "self",
-                  "domain": "hand",
-                  "value": "effect:magma_sword"
-                }
-              ]
-            },
-            "event": "minecraft:magma_sword"
-          }
-        },
-        {
-          "on_environment": {
-            "filters": {
-              "all_of": [
-                {
-                  "test": "has_equipment",
-                  "subject": "self",
-                  "domain": "hand",
-                  "value": "effect:obsidian_sword"
-                }
-              ]
-            },
-            "event": "minecraft:obsidian_sword"
-          }
-        },
-        {
-          "on_environment": {
-            "filters": {
-              "all_of": [
-                {
-                  "test": "has_equipment",
-                  "subject": "self",
-                  "domain": "hand",
-                  "value": "effect:sea_sword"
-                }
-              ]
-            },
-            "event": "minecraft:sea_sword"
-          }
-        },
-        {
-          "on_environment": {
-            "filters": {
-              "all_of": [
-                {
-                  "test": "has_equipment",
-                  "subject": "self",
-                  "domain": "hand",
-                  "value": "effect:shulker_sword"
-                }
-              ]
-            },
-            "event": "minecraft:shulker_sword"
-          }
-        },
-        {
-          "on_environment": {
-            "filters": {
-              "all_of": [
-                {
-                  "test": "has_equipment",
-                  "subject": "self",
-                  "domain": "hand",
-                  "value": "effect:slime_sword"
-                }
-              ]
-            },
-            "event": "minecraft:slime_sword"
-          }
-        },
-        {
-          "on_environment": {
-            "filters": {
-              "all_of": [
-                {
-                  "test": "has_equipment",
-                  "subject": "self",
-                  "domain": "hand",
-                  "value": "effect:spider_sword"
-                }
-              ]
-            },
-            "event": "minecraft:spider_sword"
-          }
-        },
-        {
-          "on_environment": {
-            "filters": {
-              "all_of": [
-                {
-                  "test": "has_equipment",
-                  "subject": "self",
-                  "domain": "hand",
-                  "value": "effect:sponge_sword"
-                }
-              ]
-            },
-            "event": "minecraft:sponge_sword"
-          }
-        },
-        {
-          "on_environment": {
-            "filters": {
-              "all_of": [
-                {
-                  "test": "has_equipment",
-                  "subject": "self",
-                  "domain": "hand",
-                  "value": "effect:sword_of_time"
-                }
-              ]
-            },
-            "event": "minecraft:sword_of_time"
-          }
-        },
-        {
-          "on_environment": {
-            "filters": {
-              "all_of": [
-                {
-                  "test": "has_equipment",
-                  "subject": "self",
-                  "domain": "hand",
-                  "value": "effect:tnt_sword"
-                }
-              ]
-            },
-            "event": "minecraft:tnt_sword"
-          }
-        },
-        {
-          "on_environment": {
-            "filters": {
-              "all_of": [
-                {
-                  "test": "has_equipment",
-                  "subject": "self",
-                  "domain": "hand",
-                  "value": "effect:wither_sword"
-                }
-              ]
-            },
-            "event": "minecraft:wither_sword"
-          }
-        },
-        {
-          "on_environment": {
-            "filters": {
-              "all_of": [
-                {
-                  "test": "has_equipment",
-                  "subject": "self",
-                  "domain": "hand",
-                  "value": "effect:bone_sword"
-                }
-              ]
-            },
-            "event": "minecraft:bone_sword"
-          }
-        },
-        {
-          "on_environment": {
-            "filters": {
-              "all_of": [
-                {
-                  "test": "has_equipment",
-                  "subject": "self",
-                  "domain": "hand",
-                  "value": "effect:quartz_sword"
-                }
-              ]
-            },
-            "event": "minecraft:quartz_sword"
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "operator": "!=", "value": "effect:ender_sword" } ] 
+            },
+            "event": "stop_ender_sword_event"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "value": "effect:ultra_instinct_sword" } ] 
+            },
+            "event": "minecraft:ultra_instinct_sword"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "operator": "!=", "value": "effect:ultra_instinct_sword" } ] 
+            },
+            "event": "stop_ultra_instinct_sword_event"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "value": "effect:wolf_sword" } ] 
+            },
+            "event": "minecraft:wolf_sword"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "operator": "!=", "value": "effect:wolf_sword" } ] 
+            },
+            "event": "stop_wolf_sword_event"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "is_family", "value": "wolf_transformation" } ]
+            },
+            "event": "starting_wolf_transformation"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "is_family", "value": "complete_wolf_transformation" } ]
+            },
+            "event": "wolf_movement"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "value": "effect:ghost_sword" } ] 
+            },
+            "event": "minecraft:ghost_sword"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "operator": "!=", "value": "effect:ghost_sword" } ] 
+            },
+            "event": "stop_ghost_sword_event"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "value": "effect:clock_sword" } ] 
+            },
+            "event": "minecraft:clock_sword"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "operator": "!=", "value": "effect:clock_sword" } ] 
+            },
+            "event": "stop_clock_sword_event"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "value": "effect:nether_star_sword" } ] 
+            },
+            "event": "minecraft:nether_star_sword"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "operator": "!=", "value": "effect:nether_star_sword" } ] 
+            },
+            "event": "stop_nether_star_sword_event"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "value": "effect:bee_sword" } ] 
+            },
+            "event": "minecraft:bee_sword"
+          }
+        },
+        {
+          "on_environment": {
+            "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "operator": "!=", "value": "effect:bee_sword" } ] 
+            },
+            "event": "stop_bee_sword_event"
           }
         }
       ]
     },
     "events": {
-      "minecraft:event_normal_player": {
+      "minecraft:constant_events": {
+        "sequence": [
+          {
+            "run_command": { "command": [
+              "function commands/swords_and_more_swords/swords_and_more_swords/tag_swords",
+              "gamerule sendcommandfeedback false",
+              "gamerule commandblockoutput false",
+              "scoreboard objectives add Effect99 dummy",
+              "scoreboard players add @s Effect99 1",
+              "title @s[scores={Effect99=12000}] actionbar §l§fCreated by §7Effect99",
+              "scoreboard players set @s[scores={Effect99=36001}] Effect99 1" ] }
+          }
+        ]
+      },
+      "minecraft:stop_sword_events": {
+        "sequence": [
+          {
+            "run_command": { "command": [ "execute @e[r=64,type=!player] ~ ~ ~ detect ~ ~ ~ ice 0 tp @s ~ ~ ~" ] }
+          },
+          {
+            "filters": { "all_of": [ 
+            { "test": "has_biome_tag", "operator":"!=", "value": "nether" },
+            { "test": "has_biome_tag", "operator":"!=", "value": "the_end" } ] },
+            "run_command": {
+              "command": [  
+                "fill ~6 ~6 ~6 ~-6 ~-6 ~-6 stone 0 replace effect99:spectral_block",
+                "fill ~7 ~8 ~8 ~8 ~-8 ~-8 stone 0 replace effect99:spectral_block",
+                "fill ~-7 ~-8 ~-8 ~-8 ~8 ~8 stone 0 replace effect99:spectral_block",
+                "fill ~-6 ~8 ~7 ~6 ~-8 ~8 stone 0 replace effect99:spectral_block",
+                "fill ~6 ~-8 ~-7 ~-6 ~8 ~-8 stone 0 replace effect99:spectral_block",
+                "fill ~8 ~-8 ~8 ~-8 ~-7 ~-8 stone 0 replace effect99:spectral_block",
+                "fill ~8 ~8 ~8 ~-8 ~7 ~-8 stone 0 replace effect99:spectral_block"
+              ] 
+            }
+          },
+          {
+            "filters": { "test": "has_biome_tag", "value": "nether" },
+            "run_command": {
+              "command": [  
+                "fill ~6 ~6 ~6 ~-6 ~-6 ~-6 netherrack 0 replace effect99:spectral_block",
+                "fill ~7 ~8 ~8 ~8 ~-8 ~-8 netherrack 0 replace effect99:spectral_block",
+                "fill ~-7 ~-8 ~-8 ~-8 ~8 ~8 netherrack 0 replace effect99:spectral_block",
+                "fill ~-6 ~8 ~7 ~6 ~-8 ~8 netherrack 0 replace effect99:spectral_block",
+                "fill ~6 ~-8 ~-7 ~-6 ~8 ~-8 netherrack 0 replace effect99:spectral_block",
+                "fill ~8 ~-8 ~8 ~-8 ~-7 ~-8 netherrack 0 replace effect99:spectral_block",
+                "fill ~8 ~8 ~8 ~-8 ~7 ~-8 netherrack 0 replace effect99:spectral_block"
+              ] 
+            }
+          },
+          {
+            "filters": { "test": "has_biome_tag", "value": "the_end" },
+            "run_command": {
+              "command": [  
+                "fill ~6 ~6 ~6 ~-6 ~-6 ~-6 end_stone 0 replace effect99:spectral_block",
+                "fill ~7 ~8 ~8 ~8 ~-8 ~-8 end_stone 0 replace effect99:spectral_block",
+                "fill ~-7 ~-8 ~-8 ~-8 ~8 ~8 end_stone 0 replace effect99:spectral_block",
+                "fill ~-6 ~8 ~7 ~6 ~-8 ~8 end_stone 0 replace effect99:spectral_block",
+                "fill ~6 ~-8 ~-7 ~-6 ~8 ~-8 end_stone 0 replace effect99:spectral_block",
+                "fill ~8 ~-8 ~8 ~-8 ~-7 ~-8 end_stone 0 replace effect99:spectral_block",
+                "fill ~8 ~8 ~8 ~-8 ~7 ~-8 end_stone 0 replace effect99:spectral_block"
+              ] 
+            }
+          },
+          {
+           "filters": { "all_of": [ { "test": "has_equipment", "subject": "self", "domain": "hand", "operator": "!=", "value": "effect:slime_sword" } ] },
+           "run_command": { "command": [ "ride @e[type=entity:mountable_slime,r=1,y=~-1] evict_riders" ] }
+          }
+        ]
+      },
+      "minecraft:bee_sword": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "!=", "value": "bee_sword" },
+            "add": { "component_groups": [ "minecraft:bee_sword" ] }
+          }
+        ]
+      },
+      "stop_bee_sword_event": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "==", "value": "bee_sword" },
+          "remove": { "component_groups": [ "minecraft:bee_sword" ] },
+          "add": { "component_groups": [ "minecraft:default_player" ] }
+          }
+        ]
+      },
+      "default_player": {
+        "add": { "component_groups": [ "minecraft:default_player" ] }
+      },
+      "bee_sword_flower": {
+        "randomize": [
+          { "weight": 1, "run_command": { "command": [ "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 0" ] } },
+          { "weight": 1, "run_command": { "command": [ "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 1" ] } },
+          { "weight": 1, "run_command": { "command": [ "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 2" ] } },
+          { "weight": 1, "run_command": { "command": [ "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 3" ] } },
+          { "weight": 1, "run_command": { "command": [ "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 4" ] } },
+          { "weight": 1, "run_command": { "command": [ "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 5" ] } },
+          { "weight": 1, "run_command": { "command": [ "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 6" ] } },
+          { "weight": 1, "run_command": { "command": [ "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 7" ] } },
+          { "weight": 1, "run_command": { "command": [ "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 8" ] } },
+          { "weight": 1, "run_command": { "command": [ "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 9" ] } },
+          { "weight": 1, "run_command": { "command": [ "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 10" ] } },
+          { "weight": 1, "run_command": { "command": [ "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ yellow_flower 0" ] } }
+        ]
+      },
+      "minecraft:nether_star_sword": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "!=", "value": "nether_star_sword" },
+            "add": { "component_groups": [ "minecraft:nether_star_sword" ] }
+          }
+        ]
+      },
+      "stop_nether_star_sword_event": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "==", "value": "nether_star_sword" },
+          "remove": { "component_groups": [ "minecraft:nether_star_sword" ] },
+          "add": { "component_groups": [ "minecraft:default_player" ] }
+          }
+        ]
+      },
+      "minecraft:clock_sword": {
+        "sequence": [
+          {
+            "filters": { "test": "is_family", "subject": "self", "operator": "!=", "value": "clock_sword" },
+            "add": { "component_groups": [ "minecraft:clock_sword" ] }
+          },
+          {
+            "filters": { "test": "is_family", "subject": "self", "operator": "==", "value": "clock_sword_skill" },
+            "add": { "component_groups": [ "clock_sword_movement" ] },
+            "run_command": { 
+              "command": [ 
+                "gamerule randomtickspeed 100", 
+                "effect @e[type=!player] speed 1 10 true", 
+                "time add 10", 
+                "event entity @a[family=default_player] clock_sword_movement" 
+              ] 
+            }
+          }
+        ]
+      },
+      "stop_clock_sword_event": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "==", "value": "clock_sword" },
+          "remove": { "component_groups": [ "minecraft:clock_sword" ] },
+          "run_command": { "command": [ "gamerule randomtickspeed 1", "effect @e[type=!player] speed 0 0", "event entity @a[family=default_player] default_player" ] },
+          "add": { "component_groups": [ "minecraft:default_player" ] }
+          }
+        ]
+      },
+      "clock_sword_skill_event": {
+        "add": {
+          "component_groups": [ "clock_sword_skill" ]
+        }
+      },
+      "clock_sword_movement": {
+        "add": { "component_groups": [ "clock_sword_movement" ] }
+      },
+      "minecraft:ghost_sword": {
+        "sequence": [
+          {
+          "filters": { "test": "is_family", "subject": "self", "operator": "!=", "value": "ghost_sword" },
+            "add": { "component_groups": [ "minecraft:ghost_sword" ] },
+            "run_command": { "command": [ 
+               "particle minecraft:egg_destroy_emitter ~ ~ ~",
+               "particle minecraft:egg_destroy_emitter ~ ~0.3 ~",
+               "particle minecraft:egg_destroy_emitter ~ ~0.6 ~",
+               "particle minecraft:egg_destroy_emitter ~ ~0.9 ~",
+               "particle minecraft:egg_destroy_emitter ~ ~1.2 ~",
+               "particle minecraft:egg_destroy_emitter ~ ~1.5 ~",
+               "playsound mob.wither.ambient @a[r=16] ~ ~1 ~ 2 0.3"
+              ] 
+            }
+          },
+          {
+            "run_command": { "command": [ "effect @s slow_falling 1 0 true", "effect @s saturation 1 1 true" ] },
+            "add": { "component_groups": [ "ghost_movement" ] }
+          },
+          {
+            "filters": { "test": "in_water" },
+            "run_command": { "command": [ "effect @s levitation 1 0 true" ] }
+          },
+          {
+            "filters": { "test": "in_lava" },
+            "run_command": { "command": [ "effect @s levitation 1 0 true", "effect @s fire_resistance 1 0 true" ] }
+          },
+          {
+            "filters": { "test": "in_lava", "operator": "!=" },
+            "run_command": { "command": [ "effect @s fire_resistance 0 0" ] }
+          },
+          {
+            "randomize": [
+              {
+                "weight": 90
+              },
+              {
+                "weight": 10,
+                "run_command": { "command": [ "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 0.15 0.2" ] }
+              }
+            ]
+          }
+        ]
+      },
+      "stop_ghost_sword_event": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "==", "value": "ghost_sword" },
+          "remove": { "component_groups": [ "minecraft:ghost_sword" ] },
+          "add": { "component_groups": [ "minecraft:default_player" ] },
+            "run_command": { "command": [
+               "effect @s slow_falling 0 0", 
+               "stopsound @a[r=18] mob.wither.spawn", 
+               "playsound mob.wither.ambient @a[r=16] ~ ~1 ~ 2 0.2",
+               "particle minecraft:egg_destroy_emitter ~ ~ ~",
+               "particle minecraft:egg_destroy_emitter ~ ~0.3 ~",
+               "particle minecraft:egg_destroy_emitter ~ ~0.6 ~",
+               "particle minecraft:egg_destroy_emitter ~ ~0.9 ~",
+               "particle minecraft:egg_destroy_emitter ~ ~1.2 ~",
+               "particle minecraft:egg_destroy_emitter ~ ~1.5 ~",
+               "particle minecraft:ghost_spiral ~~~"
+              ] 
+            }
+          }
+        ]
+      },
+      "minecraft:wolf_sword": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "!=", "value": "wolf_sword" },
+            "add": { "component_groups": [ "minecraft:wolf_sword" ] },
+            "run_command": { "command": [ "effect @s nausea 0 0", "effect @s blindness 0 0", "effect @s nausea 0 0" ] }
+          }
+        ]
+      },
+      "stop_wolf_sword_event": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "==", "value": "wolf_sword" },
+          "remove": { "component_groups": [ "minecraft:wolf_sword", "wolf_transformation", "wolf_movement" ] },
+          "run_command": { "command": [ "effect @s nausea 0 0" ] },
+          "add": { "component_groups": [ "minecraft:default_player" ] }
+          },
+          {
+            "filters": { "test": "is_family", "value": "complete_wolf_transformation" },
+            "remove": { "component_groups": [ "complete_wolf_transformation" ] },
+            "run_command": { "command": [ "effect @s nausea 9999 0 true", "effect @s blindness 9999 0 true" ] },
+            "add": { "component_groups": [ "minecraft:default_player" ] }
+          }
+        ]
+      },
+      "wolf_sword_start_events": {
+        "sequence": [
+          {
+           "filters": { "test": "is_family", "subject": "self", "operator": "!=", "value": "wolf_transformation" },
+           "add": { "component_groups": [ "wolf_transformation" ] },
+           "run_command": { "command": [ "function commands/swords_and_more_swords/swords_and_more_swords/tellraw1" ] }
+          }
+        ]
+      },
+      "starting_wolf_transformation": { "run_command": { "command": [ "effect @s nausea 5 0 true" ] }
+      },
+      "wolf_transformation": {
+        "sequence": [
+          {
+             "filters": { "test": "is_family", "subject": "self", "operator": "!=", "value": "complete_wolf_transformation" },
+             "run_command": { "command": [
+               "playsound random.fizz @a[r=16] ~~~", 
+               "playsound wolf_sword.howl @a[r=24] ~~~", 
+               "playsound wolf_sword.distant_howl @a[rm=25,r=100]", 
+               "particle minecraft:egg_destroy_emitter ~ ~ ~",
+               "particle minecraft:egg_destroy_emitter ~ ~0.5 ~",
+               "particle minecraft:egg_destroy_emitter ~ ~0.8 ~"
+              ] 
+            },
+            "add": { "component_groups": [ "complete_wolf_transformation" ] }
+          },
+          {
+           "filters": { "test": "is_family", "value": "wolf_transformation" },
+           "remove": { "component_groups": [ "wolf_transformation" ] }
+          }
+        ]
+      },
+      "wolf_movement": { "add": { "component_groups": [ "wolf_movement" ] } 
+      },
+      "wolf_damage_sound": { "run_command": { "command": [ "playsound mob.wolf.bark @a[r=16] ~ ~ ~ 1 0.55" ] } 
+      },
+      "wolf_sword_sounds": {
+        "randomize": [
+          { "weight": 1, "run_command": { "command": [ "playsound mob.wolf.growl @a[r=16] ~ ~ ~ 1 0.9 24" ] } }
+        ]
+      },
+      "stop_wolf_transformation": {
+        "sequence": [
+          {
+            "run_command": { "command": [ "effect @s nausea 0 0", "effect @s blindness 0 0", "stopsound @a wolf_sword.howl", "stopsound @a wolf_sword.distant_howl" ] }
+          },
+          {
+            "remove": { "component_groups": [ "wolf_transformation", "complete_wolf_transformation", "wolf_movement" ] },
+            "add": { "component_groups": [ "minecraft:wolf_sword" ] }
+          }
+        ]
+      },
+      "minecraft:ultra_instinct_sword": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "!=", "value": "ultra_instinct_sword" },
+            "add": { "component_groups": [ "minecraft:ultra_instinct_sword" ] },
+            "run_command": { "command": [ "particle minecraft:example_flipbook ~ ~ ~", "particle minecraft:example_flipbook ~ ~1.5 ~", "playsound mob.wither.ambient @a[r=16] ~ ~1 ~ 2 0.6" ] }
+          },
+          {
+            "run_command": { "command": [
+              "camerashake add @a[r=32] 0.1 0.016 positional", 
+              "fill ~1 ~2 ~1 ~-1 ~2 ~-1 effect99:lightblock 0 replace air", 
+              "fill ~1 ~2 ~1 ~-1 ~2 ~-1 effect99:lightblock 0 replace effect99:lightblock",
+              "effect @s hunger 0 0",
+              "effect @s blindness 0 0",
+              "effect @s slowness 0 0",
+              "effect @s weakness 0 0",
+              "effect @s mining_fatigue 0 0",
+              "effect @s nausea 0 0",
+              "effect @s instant_damage 0 0",
+              "effect @s wither 0 0" ] 
+             },
+            "add": { "component_groups": [ "ultra_instinct_sword_movement" ] }
+          }
+        ]
+      },
+      "stop_ultra_instinct_sword_event": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "==", "value": "ultra_instinct_sword" },
+          "remove": { "component_groups": [ "minecraft:ultra_instinct_sword", "ultra_instinct_sword_movement" ] },
+          "add": { "component_groups": [ "minecraft:default_player" ] },
+          "run_command": { "command": [ "particle minecraft:example_flipbook ~ ~ ~", "particle minecraft:example_flipbook ~ ~1.5 ~", "playsound mob.wither.ambient @a[r=16] ~ ~1 ~ 2 0.6" ] }
+          }
+        ]
+      },
+      "ultra_instinct_sword_skill": { "run_command": { "command": [ "spreadplayers ~ ~ 1 3 @s", "playsound mob.endermen.portal @a[r=17] ~ ~ ~ 1 0.6" ] } 
+      },
+      "ultra_instinct_sword_effects": {
+        "randomize": [
+          { "weight": 1, "run_command": { "command": [ "particle minecraft:balloon_gas_particle ~0.3 ~1 ~", "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3" ] } },
+          { "weight": 1, "run_command": { "command": [ "particle minecraft:balloon_gas_particle ~ ~2 ~0.3", "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3" ] } },
+          { "weight": 1, "run_command": { "command": [ "particle minecraft:balloon_gas_particle ~-0.3 ~ ~", "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3" ] } },
+          { "weight": 1, "run_command": { "command": [ "particle minecraft:balloon_gas_particle ~ ~0.3 ~-0.3", "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3" ] } },
+          { "weight": 1, "run_command": { "command": [ "particle minecraft:balloon_gas_particle ~0.3 ~1.5 ~0.3", "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3" ] } },
+          { "weight": 1, "run_command": { "command": [ "particle minecraft:balloon_gas_particle ~-0.3 ~0.8 ~-0.3", "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3" ] } },
+          { "weight": 1, "run_command": { "command": [ "particle minecraft:balloon_gas_particle ~-0.3 ~2 ~0.3", "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3" ] } },
+          { "weight": 1, "run_command": { "command": [ "particle minecraft:balloon_gas_particle ~0.2 ~1 ~0.3", "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3" ] } },
+          { "weight": 1, "run_command": { "command": [ "particle minecraft:balloon_gas_particle ~0.3 ~0.9 ~0.1", "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3" ] } },
+          { "weight": 1, "run_command": { "command": [ "particle minecraft:balloon_gas_particle ~0.2 ~2.3 ~-0.2", "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3" ] } },
+          { "weight": 1, "run_command": { "command": [ "particle minecraft:balloon_gas_particle ~-0.3 ~1.2 ~", "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3" ] } },
+          { "weight": 1, "run_command": { "command": [ "particle minecraft:balloon_gas_particle ~0.3 ~0.3 ~0.3", "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3" ] } },
+          { "weight": 1, "run_command": { "command": [ "particle minecraft:balloon_gas_particle ~0.3 ~0.6 ~0.1", "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3" ] } },
+          { "weight": 1, "run_command": { "command": [ "particle minecraft:balloon_gas_particle ~-0.3 ~0.2 ~0.3", "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3" ] } },
+          { "weight": 1, "run_command": { "command": [ "particle minecraft:balloon_gas_particle ~0.1 ~0.7 ~-0.3", "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3" ] } }
+        ]
+      },
+      "minecraft:ender_sword": {
+        "sequence": [
+        {
+        "filters": { "test": "is_family", "subject": "self", "operator": "!=", "value": "ender_sword" },
+          "add": { "component_groups": [ "minecraft:ender_sword" ] },
+          "run_command": { "command": [ "playsound mob.endermen.portal @a[r=8] ~ ~ ~" ] }
+          },
+          {
+            "run_command": { "command": [ "particle minecraft:end_chest ~ ~0.6 ~" ] }
+          }
+        ]
+      },
+      "stop_ender_sword_event": {
+        "sequence": [
+        {
+        "filters": { "test": "is_family", "subject": "self", "operator": "==", "value": "ender_sword" },
+        "remove": { "component_groups": [ "minecraft:ender_sword" ] },
+        "add": { "component_groups": [ "minecraft:default_player" ] }
+        }
+       ]
+      },
+      "ender_sword_sound": {
+        "randomize": [
+          { "weight": 1, "run_command": { "command": [ "playsound mob.endermen.scream @a[r=8] ~ ~ ~" ] } },
+          { "weight": 1, "run_command": { "command": [ "playsound mob.endermen.idle @a[r=8] ~ ~ ~" ] } },
+          { "weight": 1, "run_command": { "command": [ "playsound mob.endermen.stare @a[r=8] ~ ~ ~" ] } }
+        ]
+      },
+      "ender_sword_tp": { "run_command": { "command": [ "spreadplayers ~ ~ 0 16 @s", "playsound mob.endermen.portal @a[r=17]" ] }
+      },
+      "ender_sword_skill": {
+        "sequence": [
+          {
+           "run_command": { 
+             "command": [ 
+               "playsound mob.endermen.hit @a[r=8] ~ ~ ~"
+              ]
+            }
+          },
+          {
+            "randomize": [
+              {
+                "weight": 50
+              },
+              {
+                "weight": 50,
+                "run_command": { "command": [ "spreadplayers ~ ~ 0 16 @s", "playsound mob.endermen.portal @a[r=17]" ] }
+              }
+            ]
+          }
+        ]
+      },
+      "minecraft:lightning_sword": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "!=", "value": "lightning_sword" },
+            "add": { "component_groups": [ "minecraft:lightning_sword" ] },
+            "run_command": { "command": [ "summon lightning_bolt ~ 255 ~ default_lightning_bolt" ] }
+          },
+          {
+            "run_command": { "command": [ "fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace air", "fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace effect99:lightblock2" ] }
+          }
+        ]
+      },
+      "stop_lightning_sword_event": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "==", "value": "lightning_sword" },
+          "remove": { "component_groups": [ "minecraft:lightning_sword" ] },
+          "add": { "component_groups": [ "minecraft:default_player" ] }
+          }
+        ]
+      },
+      "minecraft:glowstone_sword": {
+        "run_command": { "command": [ "fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock 0 replace air", "fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock 0 replace effect99:lightblock" ] }
+      },
+      "minecraft:wither_sword": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "!=", "value": "wither_sword" },
+            "add": { "component_groups": [ "minecraft:wither_sword" ] },
+            "run_command": { "command": [ "playsound mob.wither.spawn @a[r=16]" ] }
+          },
+          {
+            "run_command": {
+              "command": [
+                "fill ~5 ~5 ~5 ~-5 ~-5 ~-5 dirt 1 replace grass",
+                "fill ~5 ~5 ~5 ~-5 ~-5 ~-5 air 0 replace leaves2",
+                "fill ~5 ~5 ~5 ~-5 ~-5 ~-5 air 0 replace leaves",
+                "fill ~5 ~5 ~5 ~-5 ~-5 ~-5 air 0 replace vine",
+                "fill ~5 ~5 ~5 ~-5 ~-5 ~-5 water 0 replace ice",
+                "fill ~5 ~5 ~5 ~-5 ~-5 ~-5 dirt 0 replace farmland",
+                "fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace red_flower",
+                "fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace yellow_flower",
+                "fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace red_mushroom",
+                "fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace brown_mushroom",
+                "fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace double_plant",
+                "effect @s wither 39960 1 true",
+                "fill ~1 ~2 ~1 ~-1 ~2 ~-1 effect99:lightblock2 0 replace air", 
+                "fill ~1 ~2 ~1 ~-1 ~2 ~-1 effect99:lightblock2 0 replace effect99:lightblock2"
+              ]
+            }
+          }
+        ]
+      },
+      "stop_wither_sword_event": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "==", "value": "wither_sword" },
+          "remove": { "component_groups": [ "minecraft:wither_sword" ] },
+          "add": { "component_groups": [ "minecraft:default_player" ] },
+          "run_command": { "command": [ "effect @s wither 0 0", "ride @s evict_riders" ] }
+          }
+        ]
+      },
+      "wither_sword_effects": {
+        "randomize": [
+          { "weight": 50, "run_command": { "command": [ "playsound mob.wither.death @a[r=16]" ] } },
+          { "weight": 50, "run_command": { "command": [ "playsound mob.wither.hurt @a[r=16]" ] } }
+        ]
+      },
+      "minecraft:time_sword": {
+        "sequence": [
+          {
+            "add": { "component_groups": [ "minecraft:time_sword" ] }
+          },
+          {
+            "run_command": { "command": [ "gamerule randomtickspeed 300", "effect @e[type=!player] speed 1 15 true", "time add 30", "event entity @a[family=default_player] time_sword_movement", "fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace air", "fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace effect99:lightblock2" ] }
+          }
+        ]
+      },
+      "stop_time_sword_event": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "==", "value": "time_sword" },
+          "remove": { "component_groups": [ "minecraft:time_sword" ] },
+          "add": { "component_groups": [ "minecraft:default_player" ] },
+          "run_command": { "command": [ "gamerule randomtickspeed 1", "effect @e[type=!player] speed 0 0", "event entity @a[family=default_player] default_player" ] }
+          }
+        ]
+      },
+      "time_sword_movement": {
+        "add": { "component_groups": [ "time_sword_movement" ] }
+      },
+      "minecraft:sponge_sword": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "!=", "value": "sponge_sword" },
+            "add": { "component_groups": [ "minecraft:sponge_sword" ] },
+            "run_command": { "command": [ "scoreboard objectives add sponge_sword dummy" ] }
+          },
+          {
+           "filters": { "test": "in_water_or_rain" },
+           "run_command": {
+             "command": [
+               "fill ~2 ~2 ~2 ~-2 ~-2 ~-2 sponge 0 replace water",
+               "playsound random.fizz @a[r=12] ~~~ 0.6",
+               "particle minecraft:cauldron_explosion_emitter ~ ~ ~",
+               "scoreboard players add @s sponge_sword 1"
+              ]
+            }
+          },
+          {
+            "run_command": {
+             "command": [
+               "fill ~2 ~2 ~2 ~-2 ~-2 ~-2 air 0 replace sponge",
+               "fill ~2 ~2 ~2 ~-2 ~-2 ~-2 air 0 replace seagrass",
+               "execute @s[scores={sponge_sword=150}] ~ ~ ~ event entity @s wet_sponge_sword",
+               "execute @s[scores={sponge_sword=155}] ~ ~ ~ event entity @s wet_sponge_sword",
+               "execute @s[scores={sponge_sword=160}] ~ ~ ~ event entity @s wet_sponge_sword"
+              ]
+            }
+          }
+        ]
+      },
+      "wet_sponge_sword": {
+        "sequence": [
+          {
+            "filters": { "test": "has_equipment", "subject": "self", "domain": "hand", "value": "effect:sponge_sword" },
+            "run_command": { "command": [ "replaceitem entity @s slot.weapon.mainhand 0 effect:wet_sponge_sword 1", "scoreboard players set @s sponge_sword 0", "title @s actionbar §l§gWet Sponge Sword" ] }
+          }
+        ]
+      },
+      "stop_sponge_sword_event": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "==", "value": "sponge_sword" },
+          "remove": { "component_groups": [ "minecraft:sponge_sword" ] },
+          "add": { "component_groups": [ "minecraft:default_player" ] }
+          }
+        ]
+      },
+      "minecraft:spider_sword": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "!=", "value": "spider_sword" },
+            "add": { "component_groups": [ "minecraft:spider_sword" ] },
+            "run_command": { "command": [ "ride @s summon_ride minecraft:spider no_ride_change minecraft:spider_sword", "particle minecraft:example_linearcurve ~ ~ ~" ] }
+          }
+        ]
+      },
+      "stop_spider_sword_event": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "==", "value": "spider_sword" },
+          "remove": { "component_groups": [ "minecraft:spider_sword", "spider_sword_skill" ] },
+          "add": { "component_groups": [ "minecraft:default_player" ] },
+          "run_command": { "command": [ "ride @s stop_riding" ] }
+          }
+        ]
+      },
+      "stop_spider_skill_event": {
+        "sequence": [
+          {
+          "filters": { "test": "is_family", "subject": "self", "value": "spider_sword_skill" },
+            "remove": { "component_groups": [ "spider_sword_skill" ] },
+            "add": { "component_groups": [ "minecraft:spider_sword" ] }
+          }
+        ]
+      },
+      "spider_sword_skill": {
+        "sequence": [
+          {
+           "filters": { "test": "is_family", "subject": "self", "operator": "!=", "value": "spider_sword_skill" },
+           "add": { "component_groups": [ "spider_sword_skill" ] }
+          } 
+        ]
+      },
+      "minecraft:shulker_sword": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "!=", "value": "shulker_sword" },
+            "add": { "component_groups": [ "minecraft:shulker_sword" ] }
+          },
+          {
+            "run_command": { "command": [ "effect @s levitation 0 0" ] }
+          }
+        ]
+      },
+      "stop_shulker_sword_event": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "==", "value": "shulker_sword" },
+          "remove": { "component_groups": [ "minecraft:shulker_sword" ] },
+          "add": { "component_groups": [ "minecraft:default_player" ] },
+          "run_command": { "command": [ "ride @s stop_riding" ] }
+          }
+        ]
+      },
+      "shulker_sword_skill": {
+        "add": { "component_groups": [ "shulker_sword_skill" ] },
+        "run_command": { "command": [ "ride @s summon_ride entity:shulker_shield no_ride_change" ] }
+      },
+      "minecraft:slime_sword": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "!=", "value": "slime_sword" },
+            "add": { "component_groups": [ "minecraft:slime_sword" ] }
+          },
+          {
+            "run_command": { "command": [ "scoreboard players set @e[type=entity:mountable_slime,c=1,r=12] slime_despawn 0" ] }
+          }
+        ]
+      },
+      "stop_slime_sword_event": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "==", "value": "slime_sword" },
+          "remove": { "component_groups": [ "minecraft:slime_sword" ] },
+          "add": { "component_groups": [ "minecraft:default_player" ] },
+          "run_command": { "command": [ "ride @s stop_riding", "event entity @e[type=entity:mountable_slime,c=1,r=32] despawn" ] }
+          }
+        ]
+      },
+      "slime_sword_skills": {
+        "run_command": { "command": [ "ride @s summon_ride entity:mountable_slime no_ride_change", "scoreboard objectives add slime_despawn dummy" ] }
+      },
+      "minecraft:spectral_sword": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "!=", "value": "spectral_sword" },
+            "add": { "component_groups": [ "minecraft:spectral_sword" ] }
+          },
+          {
+           "run_command": { 
+             "command": [
+               "fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace air", 
+               "fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace effect99:lightblock2",
+               "execute @s[y=8,dy=247] ~~~ event entity @s spectral_sword_function",
+               "execute @s[y=0,dy=7] ~~~ event entity @s spectral_sword_function_1"
+              ] 
+            }
+          }
+        ]
+      },
+      "spectral_sword_function_1": {
+        "sequence": [
+          {
+            "filters": { "all_of": [ 
+            { "test": "has_biome_tag", "operator":"!=", "value": "nether" },
+            { "test": "has_biome_tag", "operator":"!=", "value": "the_end" } ] },
+            "run_command": {
+              "command": [  
+                "fill ~8 ~8 ~8 ~-8 ~-6 ~-8 stone 0 replace effect99:spectral_block"
+              ] 
+            }
+          },
+          {
+            "filters": { "test": "has_biome_tag", "value": "nether" },
+            "run_command": {
+              "command": [  
+                "fill ~8 ~8 ~8 ~-8 ~-6 ~-8 netherrack 0 replace effect99:spectral_block"
+              ] 
+            }
+          },
+          {
+            "filters": { "test": "has_biome_tag", "value": "the_end" },
+            "run_command": {
+              "command": [  
+                "fill ~8 ~8 ~8 ~-8 ~-6 ~-8 end_stone 0 replace effect99:spectral_block"
+              ] 
+            }
+          }
+        ]
+      },
+      "spectral_sword_function": {
+        "sequence": [
+          {
+            "filters": { "all_of": [ 
+            { "test": "has_biome_tag", "operator":"!=", "value": "nether" },
+            { "test": "has_biome_tag", "operator":"!=", "value": "the_end" } ] },
+            "run_command": {
+              "command": [  
+                "fill ~6 ~6 ~6 ~-6 ~-6 ~-6 effect99:spectral_block 0 replace stone",
+                "fill ~7 ~8 ~8 ~8 ~-8 ~-8 stone 0 replace effect99:spectral_block",
+                "fill ~-7 ~-8 ~-8 ~-8 ~8 ~8 stone 0 replace effect99:spectral_block",
+                "fill ~-6 ~8 ~7 ~6 ~-8 ~8 stone 0 replace effect99:spectral_block",
+                "fill ~6 ~-8 ~-7 ~-6 ~8 ~-8 stone 0 replace effect99:spectral_block",
+                "fill ~8 ~-8 ~8 ~-8 ~-7 ~-8 stone 0 replace effect99:spectral_block",
+                "fill ~8 ~8 ~8 ~-8 ~7 ~-8 stone 0 replace effect99:spectral_block"
+              ] 
+            }
+          },
+          {
+            "filters": { "test": "has_biome_tag", "value": "nether" },
+            "run_command": {
+              "command": [  
+                "fill ~6 ~6 ~6 ~-6 ~-6 ~-6 effect99:spectral_block 0 replace netherrack",
+                "fill ~7 ~8 ~8 ~8 ~-8 ~-8 netherrack 0 replace effect99:spectral_block",
+                "fill ~-7 ~-8 ~-8 ~-8 ~8 ~8 netherrack 0 replace effect99:spectral_block",
+                "fill ~-6 ~8 ~7 ~6 ~-8 ~8 netherrack 0 replace effect99:spectral_block",
+                "fill ~6 ~-8 ~-7 ~-6 ~8 ~-8 netherrack 0 replace effect99:spectral_block",
+                "fill ~8 ~-8 ~8 ~-8 ~-7 ~-8 netherrack 0 replace effect99:spectral_block",
+                "fill ~8 ~8 ~8 ~-8 ~7 ~-8 netherrack 0 replace effect99:spectral_block"
+              ] 
+            }
+          },
+          {
+            "filters": { "test": "has_biome_tag", "value": "the_end" },
+            "run_command": {
+              "command": [  
+                "fill ~6 ~6 ~6 ~-6 ~-6 ~-6 effect99:spectral_block 0 replace end_stone",
+                "fill ~7 ~8 ~8 ~8 ~-8 ~-8 end_stone 0 replace effect99:spectral_block",
+                "fill ~-7 ~-8 ~-8 ~-8 ~8 ~8 end_stone 0 replace effect99:spectral_block",
+                "fill ~-6 ~8 ~7 ~6 ~-8 ~8 end_stone 0 replace effect99:spectral_block",
+                "fill ~6 ~-8 ~-7 ~-6 ~8 ~-8 end_stone 0 replace effect99:spectral_block",
+                "fill ~8 ~-8 ~8 ~-8 ~-7 ~-8 end_stone 0 replace effect99:spectral_block",
+                "fill ~8 ~8 ~8 ~-8 ~7 ~-8 end_stone 0 replace effect99:spectral_block"
+              ] 
+            }
+          }
+        ]
+      },
+      "stop_spectral_sword_event": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "==", "value": "spectral_sword" },
+          "remove": { "component_groups": [ "minecraft:spectral_sword" ] },
+          "run_command": { "command": [ "ride @s evict_riders" ] },
+          "add": { "component_groups": [ "minecraft:default_player" ] }
+          }
+        ]
+      },
+      "spectral_sword_skills": {
+        "sequence": [
+          {
+            "filters": { "test": "has_biome_tag", "operator": "!=", "value": "the_end" },
+            "run_command": { "command": [ 
+              "summon ender_crystal ~ ~1.8 ~ minecraft:detect_player"
+              ] 
+            }
+          },
+          {
+            "run_command": { "command": [
+              "playsound portal.travel @a[r=16] ~ ~ ~ 1 7",
+              "particle minecraft:example_flipbook ~ ~3 ~"
+              ] 
+            }
+          }
+        ]
+      },
+      "spectral_sword_reload_skill": { 
+        "sequence": [
+         {
+          "filters": { "test": "is_family", "subject": "self", "operator": "==", "value": "spectral_sword" },
+            "add": { "component_groups": [ "minecraft:spectral_sword" ] }
+          }
+        ]
+      },
+      "minecraft:sea_sword": {
+        "sequence": [
+          {
+            "filters": { "test": "in_water", "operator": "!=" },
+            "add": { "component_groups": [ "mermaid_movement_out_water" ] },
+            "run_command": { "command": [ "camerashake add @s 0.01 1 positional", "effect @s conduit_power 0 0" ] }
+          },
+          {
+          "filters": { "test": "is_family", "subject": "self", "operator": "!=", "value": "sea_sword" },
+            "add": { "component_groups": [ "minecraft:sea_sword" ] },
+            "run_command": { "command": [ "particle minecraft:example_bounce ~ ~ ~", "playsound random.splash @a[r=12] ~ ~ ~ 0.5" ] }
+          },
+          {
+            "filters": { "test": "in_water" },
+            "add": { "component_groups": [ "mermaid_movement_in_water" ] },
+            "run_command": { "command": [ "effect @s conduit_power 1 0 true" ] }
+          }
+        ]
+      },
+      "stop_sea_sword_event": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "==", "value": "sea_sword" },
+          "remove": { "component_groups": [ "minecraft:sea_sword", "mermaid_movement_in_water" ] },
+          "add": { "component_groups": [ "minecraft:default_player" ] },
+          "run_command": { "command": [ "particle minecraft:example_bounce ~ ~ ~", "playsound random.splash @a[r=12] ~ ~ ~ 0.5", "effect @s conduit_power 0 0" ] }
+          }
+        ]
+      },
+      "sea_sword_sound": {
+        "sequence": [
+          {
+            "filters": { "test": "in_water", "operator": "!=" },
+            "run_command": {
+              "command": [ "playsound mob.fish.flop @a[r=12] ~ ~ ~ 1 0.6" ]
+            }
+          }
+        ]
+      },
+      "minecraft:quartz_sword": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "!=", "value": "quartz_sword" },
+            "run_command": { "command": [ "damage @s 14 magic" ] },
+            "add": { "component_groups": [ "minecraft:quartz_sword" ] }
+          }
+        ]
+      },
+      "stop_quartz_sword_event": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "==", "value": "quartz_sword" },
+          "run_command": { "command": [ "damage @s 14 magic" ] },
+          "remove": { "component_groups": [ "minecraft:quartz_sword" ] },
+          "add": { "component_groups": [ "minecraft:default_player" ] }
+          }
+        ]
+      },
+      "minecraft:obsidian_sword": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "!=", "value": "obsidian_sword" },
+            "add": { "component_groups": [ "minecraft:obsidian_sword" ] }
+          }
+        ]
+      },
+      "stop_obsidian_sword_event": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "==", "value": "obsidian_sword" },
+          "remove": { "component_groups": [ "minecraft:obsidian_sword" ] },
+          "add": { "component_groups": [ "minecraft:default_player" ] }
+          }
+        ]
+      },
+      "minecraft:lapis_sword": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "!=", "value": "lapis_sword" },
+            "add": { "component_groups": [ "minecraft:lapis_sword" ] }
+          }
+        ]
+      },
+      "stop_lapis_sword_event": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "==", "value": "lapis_sword" },
+          "remove": { "component_groups": [ "minecraft:lapis_sword" ] },
+          "add": { "component_groups": [ "minecraft:default_player" ] }
+          }
+        ]
+      },
+      "lapis_sword_skills": {
+        "run_command": { "command": [ "xp 5 @s", "playsound random.orb @s ~ ~ ~ 0.3" ] }
+      },
+      "minecraft:ice_sword": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "!=", "value": "ice_sword" },
+            "add": { "component_groups": [ "minecraft:ice_sword" ] }
+          },
+          {
+            "filters": { "all_of": [ { "test": "in_lava" }, { "test": "has_biome_tag", "operator": "!=", "value": "nether" } ] },
+            "run_command": { "command": [ "playsound random.fizz @a[r=10] ~ ~ ~", "setblock ~ ~ ~ flowing_water", "replaceitem entity @s slot.weapon.mainhand 0 air 1 0", "particle minecraft:cauldron_explosion_emitter ~ ~ ~" ] }
+          },
+          {
+            "filters": { "all_of": [ { "test": "in_lava" }, { "test": "has_biome_tag", "value": "nether" } ] },
+            "run_command": { "command": [ "playsound random.fizz @a[r=10] ~ ~ ~", "replaceitem entity @s slot.weapon.mainhand 0 air 1 0", "particle minecraft:cauldron_explosion_emitter ~ ~ ~" ] }
+          },
+          {
+            "run_command": { "command": [ 
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
+              ] 
+            }
+          }
+        ]
+      },
+      "stop_ice_sword_event": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "==", "value": "ice_sword" },
+          "remove": { "component_groups": [ "minecraft:ice_sword" ] },
+          "add": { "component_groups": [ "minecraft:default_player" ] }
+          }
+        ]
+      },
+      "minecraft:magma_sword": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "!=", "value": "magma_sword" },
+            "add": { "component_groups": [ "minecraft:magma_sword" ] }
+          },
+          {
+            "run_command": { "command": [ 
+              "fill ~ ~-1 ~ ~ ~-1 ~ magma 0 replace lava",
+              "fill ~1 ~-1 ~1 ~ ~-1 ~ magma 0 replace lava",
+              "fill ~ ~-1 ~1 ~ ~-1 ~1 magma 0 replace lava",
+              "fill ~-1 ~-1 ~ ~-1 ~-1 ~ magma 0 replace lava",
+              "fill ~ ~-1 ~-1 ~ ~-1 ~-1 magma 0 replace lava",
+              "execute @s ~ ~1 ~ particle minecraft:guardian_attack_particle ^-0.4 ^ ^0.2"
+              ] 
+            }
+          },
+          {
+            "filters": { "test": "in_water", "operator": "==" },
+            "randomize": [
+              {
+                "weight": 99
+              },
+              {
+                "weight": 1,
+                "run_command": { "command": [ "playsound bubble.up @a ~ ~ ~ 1 0.9" ] }
+              }
+            ]
+          }
+        ]
+      },
+      "stop_magma_sword_event": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "==", "value": "magma_sword" },
+          "remove": { "component_groups": [ "minecraft:magma_sword" ] },
+          "add": { "component_groups": [ "minecraft:default_player" ] }
+          }
+        ]
+      },
+      "minecraft:jungle_sword": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "!=", "value": "jungle_sword" },
+            "add": { "component_groups": [ "minecraft:jungle_sword" ] }
+          },
+          {
+            "run_command": { "command": [ "effect @s absorption 1 2 true", "function commands/swords_and_more_swords/swords_and_more_swords/jungle_sword" ] }
+          }
+        ]
+      },
+      "stop_jungle_sword_event": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "==", "value": "jungle_sword" },
+          "remove": { "component_groups": [ "minecraft:jungle_sword" ] },
+          "add": { "component_groups": [ "minecraft:default_player" ] },
+          "run_command": { "command": [ "effect @s absorption 0" ] }
+          }
+        ]
+      },
+
+      "minecraft:grass_sword": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "!=", "value": "grass_sword" },
+            "add": { "component_groups": [ "minecraft:grass_sword" ] }
+          },
+          {
+            "run_command": { "command": [ 
+              "tag @e[tag=grass,rm=9,r=10] remove grass",
+              "fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 grass 0 replace dirt",
+              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 fill ~ ~ ~ ~ ~ ~ tallgrass 0 replace air"
+              ] 
+            }
+          }
+        ]
+      },
+      "stop_grass_sword_event": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "==", "value": "grass_sword" },
+          "remove": { "component_groups": [ "minecraft:grass_sword" ] },
+          "add": { "component_groups": [ "minecraft:default_player" ] }
+          }
+        ]
+      },
+      "grass_sword_skills": {
+        "run_command": { 
+          "command": [ 
+            "execute @e[type=!player,type=!item,type=!entity:grass,type=!xp_orb,type=!arrow,r=8,tag=!grass] ~ ~ ~ detect ~ ~-0.1 ~ grass 0 execute @s ~ ~ ~ detect ~ ~ ~ air 0 summon entity:grass",
+            "execute @e[type=!player,type=!item,type=!entity:grass,type=!xp_orb,type=!arrow,r=8,tag=!grass] ~ ~ ~ detect ~ ~-0.1 ~ grass 0 execute @s ~ ~ ~ detect ~ ~ ~ tallgrass 0 summon entity:grass" ] }
+      },
+      "minecraft:fire_sword": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "!=", "value": "fire_sword" },
+            "add": { "component_groups": [ "minecraft:fire_sword" ] }
+          },
+          {
+           "run_command": {
+             "command": [ 
+               "fill ~3 ~3 ~3 ~-3 ~-3 ~-3 air 0 replace snow_layer",
+               "fill ~3 ~3 ~3 ~-3 ~-3 ~-3 water 0 replace ice",
+               "fill ~3 ~3 ~3 ~-3 ~-3 ~-3 water 0 replace blue_ice",
+               "fill ~3 ~3 ~3 ~-3 ~-3 ~-3 water 0 replace packed_ice",
+               "execute @e[family=!player,type=!item,r=3] ~ ~ ~ summon entity:fire",
+               "fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock 0 replace air", 
+               "fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock 0 replace effect99:lightblock"
+              ] 
+            }
+          }
+        ]
+      },
+      "stop_fire_sword_event": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "==", "value": "fire_sword" },
+          "remove": { "component_groups": [ "minecraft:fire_sword" ] },
+          "add": { "component_groups": [ "minecraft:default_player" ] }
+          }
+        ]
+      },
+      "fire_sword_sound": { "run_command": { "command": [ "playsound fire.fire @a[r=8]" ] }
+      },
+      "minecraft:emerald_sword": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "!=", "value": "emerald_sword" },
+            "add": { "component_groups": [ "minecraft:emerald_sword" ] }
+          },
+          {
+          "filters": {  "all_of": [ { "test": "is_in_village", "subject": "self", "value": true } ] },
+            "run_command": { "command": [ "effect @s village_hero 1 0 true", "effect @e[family=villager,r=64] resistance 1 1 true" ] }
+          }
+        ]
+      },
+      "stop_emerald_sword_event": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "==", "value": "emerald_sword" },
+          "run_command": { "command": [ "effect @s village_hero 0 0 true" ] },
+          "remove": { "component_groups": [ "minecraft:emerald_sword" ] },
+          "add": { "component_groups": [ "minecraft:default_player" ] }
+          }
+        ]
+      },
+      "start_player_explode_event": { 
+        "add": { "component_groups": [ "start_player_explode_event" ] },
+        "run_command": { "command": [ "playanimation @s animation.player.explode", "playsound random.fuse" ] }
+      },
+      "start_player_explode": { 
+        "remove": { "component_groups": [ "start_player_explode_event" ] },
+        "add": { "component_groups": [ "minecraft:default_player" ] },
+        "run_command": { "command": [ "summon entity:instant_creeper_explode ~ ~1 ~", "kill @s" ] }
+      },
+      "minecraft:cactus_sword": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "!=", "value": "cactus_sword" },
+            "add": { "component_groups": [ "minecraft:cactus_sword" ] }
+          }
+        ]
+      },
+      "stop_cactus_sword_event": {
+        "sequence": [
+          {
+            "filters": { "test": "is_family", "subject": "self", "operator": "==", "value": "cactus_sword" },
+            "remove": { "component_groups": [ "minecraft:cactus_sword" ] },
+            "add": { "component_groups": [ "minecraft:default_player" ] }
+          }
+        ]
+      },
+      "cactus_sword_skills": { "run_command": { "command": [ "damage @e[r=1.4,type=!player] 1 contact entity @s", "damage @s 1 contact" ] }
+      },
+      "minecraft:bone_sword": {
+        "sequence": [
+        {
+          "filters": { "test": "is_family", "subject": "self", "operator": "!=", "value": "bone_sword" },
+            "add": { "component_groups": [ "minecraft:bone_sword" ] }
+          },
+          {
+          "run_command": {
+            "command": [ "event entity @e[family=arrow,r=8] minecraft:inertia_disable" ]
+            } 
+          }
+        ]
+      },
+      "stop_bone_sword_event": {
+        "sequence": [
+          {
+            "filters": { "test": "is_family", "subject": "self", "operator": "==", "value": "bone_sword" },
+            "remove": { "component_groups": [ "minecraft:bone_sword" ] },
+            "add": { "component_groups": [ "minecraft:default_player" ] }
+          }
+        ]
+      },
+      "bone_sword_skills": {
+        "run_command": {
+          "command": [ "summon entity:grows_crop ~ ~0.1 ~ grows_crop_event" ]
+        }
+      },
+      "minecraft:blaze_sword": {
+        "sequence": [
+        {
+        "filters": { "test": "is_family", "subject": "self", "operator": "!=", "value": "blaze_sword" },
+          "add": { "component_groups": [ "minecraft:blaze_sword" ] },
+          "run_command": {
+            "command": [ 
+              "particle minecraft:mobflame_single ~ ~ ~",
+              "particle minecraft:mobflame_single ~ ~1 ~",
+              "particle minecraft:mobflame_single ~ ~1.5 ~",
+              "particle minecraft:mobflame_single ~0.4 ~ ~",
+              "particle minecraft:mobflame_single ~ ~1 ~0.4",
+              "particle minecraft:mobflame_single ~-0.4 ~1.5 ~",
+              "particle minecraft:mobflame_single ~ ~ ~-0.4",
+              "particle minecraft:mobflame_single ~0.3 ~1 ~0.3",
+              "particle minecraft:mobflame_single ~-0.3 ~1.5 ~-0.3",
+              "particle minecraft:mobflame_single ~0.3 ~ ~-0.3",
+              "particle minecraft:mobflame_single ~-0.3 ~1 ~0.3",
+              "particle minecraft:example_linearcurve ~ ~1 ~", 
+              "playsound random.fizz @a[r=16]"
+            ] 
+          }
+        },
+        {
+          "run_command": {
+            "command": [ "event entity @e[family=shot_by_the_blaze,r=7] minecraft:inertia_disable", "fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace air", "fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace effect99:lightblock2" ]
+            }
+          },
+          {
+            "filters": { "test": "is_family", "subject": "self", "operator": "==", "value": "blaze_sword_skill" },
+            "randomize": [
+            { "weight": 5, "run_command": { "command": [ "particle minecraft:mobflame_single ~ ~0.2 ~" ] } },
+            { "weight": 5, "run_command": { "command": [ "particle minecraft:mobflame_single ~0.3 ~0.2 ~" ] } },
+            { "weight": 5, "run_command": { "command": [ "particle minecraft:mobflame_single ~ ~0.2 ~0.3" ] } },
+            { "weight": 5, "run_command": { "command": [ "particle minecraft:mobflame_single ~-0.3 ~0.2 ~" ] } },
+            { "weight": 5, "run_command": { "command": [ "particle minecraft:mobflame_single ~ ~0.2 ~-0.3" ] } },
+            { "weight": 5, "run_command": { "command": [ "playsound mob.blaze.breathe @a[r=12] ~ ~ ~ 0.5" ] } },
+            { "weight": 95 }
+            ]
+          }
+        ]
+      },
+      "stop_blaze_sword_event": {
+        "sequence": [
+        {
+        "filters": { "test": "is_family", "subject": "self", "operator": "==", "value": "blaze_sword" },
+        "remove": { "component_groups": [ "minecraft:blaze_sword", "shoot_small_fireball" ] },
+        "run_command": {
+          "command": [ 
+            "particle minecraft:mobflame_single ~ ~ ~",
+            "particle minecraft:mobflame_single ~ ~1 ~",
+            "particle minecraft:mobflame_single ~ ~1.5 ~",
+            "particle minecraft:mobflame_single ~0.4 ~ ~",
+            "particle minecraft:mobflame_single ~ ~1 ~0.4",
+            "particle minecraft:mobflame_single ~-0.4 ~1.5 ~",
+            "particle minecraft:mobflame_single ~ ~ ~-0.4",
+            "particle minecraft:mobflame_single ~0.3 ~1 ~0.3",
+            "particle minecraft:mobflame_single ~-0.3 ~1.5 ~-0.3",
+            "particle minecraft:mobflame_single ~0.3 ~ ~-0.3",
+            "particle minecraft:mobflame_single ~-0.3 ~1 ~0.3",
+            "particle minecraft:example_linearcurve ~ ~1 ~",
+            "playsound random.fizz @a[r=16]",
+            "effect @s levitation 0 0 true", 
+            "effect @s slow_falling 0 0 true"
+          ] 
+        },
+        "add": { "component_groups": [ "minecraft:default_player" ] }
+        }
+       ]
+      },
+      "stop_blaze_sword_skill": {
+        "sequence": [
+        {
+        "filters": { "test": "is_family", "subject": "self", "operator": "==", "value": "blaze_sword" },
+        "remove": { "component_groups": [ "shoot_small_fireball" ] },
+        "add": { "component_groups": [ "minecraft:blaze_sword" ] }
+        }
+       ]
+      },
+      "blaze_sword_skill_event": {
         "add": {
           "component_groups": [
-            "minecraft:normal_player"
+            "blaze_sword_skill"
           ]
-        },
-        "remove": {
-          "component_groups": [
-            "minecraft:spectral_sword",
-            "minecraft:blaze_sword",
-            "minecraft:cactus_sword",
-            "minecraft:coal_sword",
-            "minecraft:creeper_sword",
-            "minecraft:emerald_sword",
-            "minecraft:ender_sword",
-            "minecraft:fire_sword",
-            "minecraft:glowstone_sword",
-            "minecraft:grass_sword",
-            "minecraft:ice_sword",
-            "minecraft:jungle_sword",
-            "minecraft:lapis_sword",
-            "minecraft:lightning_sword",
-            "minecraft:magma_sword",
-            "minecraft:obsidian_sword",
-            "minecraft:sea_sword",
-            "minecraft:shulker_sword",
-            "minecraft:slime_sword",
-            "minecraft:spider_sword",
-            "minecraft:sponge_sword",
-            "minecraft:sword_of_time",
-            "minecraft:tnt_sword",
-            "minecraft:wither_sword",
-            "minecraft:bone_sword",
-            "minecraft:quartz_sword"
-          ]
-        }
-      },
-      "minecraft:spectral_sword": {
+        }
+      },
+      "blaze_sword_skill": {
         "add": {
           "component_groups": [
-            "minecraft:spectral_sword"
+            "shoot_small_fireball"
           ]
         }
       },
-      "minecraft:blaze_sword": {
-        "add": {
-          "component_groups": [
-            "minecraft:blaze_sword"
-          ]
-        }
-      },
-      "minecraft:cactus_sword": {
-        "add": {
-          "component_groups": [
-            "minecraft:cactus_sword"
-          ]
-        }
-      },
-      "minecraft:coal_sword": {
-        "add": {
-          "component_groups": [
-            "minecraft:coal_sword"
-          ]
-        }
-      },
-      "minecraft:creeper_sword": {
-        "add": {
-          "component_groups": [
-            "minecraft:creeper_sword"
-          ]
-        }
-      },
-      "minecraft:emerald_sword": {
-        "add": {
-          "component_groups": [
-            "minecraft:emerald_sword"
-          ]
-        }
-      },
-      "minecraft:ender_sword": {
-        "add": {
-          "component_groups": [
-            "minecraft:ender_sword"
-          ]
-        }
-      },
-      "minecraft:fire_sword": {
-        "add": {
-          "component_groups": [
-            "minecraft:fire_sword"
-          ]
-        }
-      },
-      "minecraft:glowstone_sword": {
-        "add": {
-          "component_groups": [
-            "minecraft:glowstone_sword"
-          ]
-        }
-      },
-      "minecraft:grass_sword": {
-        "add": {
-          "component_groups": [
-            "minecraft:grass_sword"
-          ]
-        }
-      },
-      "minecraft:ice_sword": {
-        "add": {
-          "component_groups": [
-            "minecraft:ice_sword"
-          ]
-        }
-      },
-      "minecraft:jungle_sword": {
-        "add": {
-          "component_groups": [
-            "minecraft:jungle_sword"
-          ]
-        }
-      },
-      "minecraft:lapis_sword": {
-        "add": {
-          "component_groups": [
-            "minecraft:lapis_sword"
-          ]
-        }
-      },
-      "minecraft:lightning_sword": {
-        "add": {
-          "component_groups": [
-            "minecraft:lightning_sword"
-          ]
-        }
-      },
-      "minecraft:magma_sword": {
-        "add": {
-          "component_groups": [
-            "minecraft:magma_sword"
-          ]
-        }
-      },
-      "minecraft:obsidian_sword": {
-        "add": {
-          "component_groups": [
-            "minecraft:obsidian_sword"
-          ]
-        }
-      },
-      "minecraft:sea_sword": {
-        "add": {
-          "component_groups": [
-            "minecraft:sea_sword"
-          ]
-        }
-      },
-      "minecraft:shulker_sword": {
-        "add": {
-          "component_groups": [
-            "minecraft:shulker_sword"
-          ]
-        }
-      },
-      "minecraft:slime_sword": {
-        "add": {
-          "component_groups": [
-            "minecraft:slime_sword"
-          ]
-        }
-      },
-      "minecraft:spider_sword": {
-        "add": {
-          "component_groups": [
-            "minecraft:spider_sword"
-          ]
-        }
-      },
-      "minecraft:sponge_sword": {
-        "add": {
-          "component_groups": [
-            "minecraft:sponge_sword"
-          ]
-        }
-      },
-      "minecraft:sword_of_time": {
-        "add": {
-          "component_groups": [
-            "minecraft:sword_of_time"
-          ]
-        }
-      },
-      "minecraft:tnt_sword": {
-        "add": {
-          "component_groups": [
-            "minecraft:tnt_sword"
-          ]
-        }
-      },
-      "minecraft:wither_sword": {
-        "add": {
-          "component_groups": [
-            "minecraft:wither_sword"
-          ]
-        }
-      },
-      "minecraft:bone_sword": {
-        "add": {
-          "component_groups": [
-            "minecraft:bone_sword"
-          ]
-        }
-      },
-      "minecraft:quartz_sword": {
-        "add": {
-          "component_groups": [
-            "minecraft:quartz_sword"
-          ]
-        }
+      "blaze_sword_effects": {
+        "randomize": [
+          { "weight": 1, "run_command": { "command": [ "particle minecraft:mobflame_single ~ ~0.2 ~" ] } },
+          { "weight": 1, "run_command": { "command": [ "particle minecraft:mobflame_single ~0.3 ~0.2 ~" ] } },
+          { "weight": 1, "run_command": { "command": [ "particle minecraft:mobflame_single ~ ~0.2 ~0.3" ] } },
+          { "weight": 1, "run_command": { "command": [ "particle minecraft:mobflame_single ~-0.3 ~0.2 ~" ] } },
+          { "weight": 1, "run_command": { "command": [ "particle minecraft:mobflame_single ~ ~0.2 ~-0.3" ] } },
+          { "weight": 1, "run_command": { "command": [ "playsound mob.blaze.breathe @a[r=12] ~ ~ ~ 0.5" ] } }
+        ]
+      },
+      "shoot_ultra_instinct_projectile": {
+        "run_command": { "command": [ "playsound mob.wither.ambient @s ~ ~1 ~ 2 0.6" ] },
+        "add": { "component_groups": [ "ultra_instinct_projectile" ] },
+        "remove": { "component_groups": [ "ultra_instinct_projectile" ] }
       },
       "minecraft:gain_bad_omen": {
         "add": {
@@ -1104,18 +2289,15 @@
       },
       "minecraft:trigger_raid": {
         "add": {
-          "component_groups": [
-            "minecraft:raid_trigger"
-          ]
+          "component_groups": [ "minecraft:raid_trigger" ]
         }
       },
       "minecraft:remove_raid_trigger": {
         "remove": {
-          "component_groups": [
-            "minecraft:raid_trigger"
-          ]
-        }
-      }
+          "component_groups": [ "minecraft:raid_trigger" ]
+        }
+      },
+      "despawn": {  "add": { "component_groups": [ "despawn" ] } }
     }
   }
 }
```

### `Swords_B/entities/spider.json`

```diff
--- 1.6/Sword_B/entities/spider.json
+++ 2.8.14/Swords_B/entities/spider.json
@@ -1,46 +1,416 @@
 {
-  "format_version": "1.11.0",
+  "format_version": "1.13.0",
   "minecraft:entity": {
     "description": {
-      "identifier": "entity:spider",
-      "is_spawnable": false,
+      "identifier": "minecraft:spider",
+      "is_spawnable": true,
       "is_summonable": true,
       "is_experimental": false,
       "scripts": {
-        "animate": [
-          "spider"
-        ]
+        "animate": [ "despawn", "climb_spider" ]
       },
       "animations": {
-        "spider": "controller.animation.spider"
+        "despawn": "controller.animation.despawn",
+        "climb_spider": "controller.animation.climb_spider"
+      }
+    },
+    "component_groups": {
+      "despawn": { "minecraft:despawn": {} 
+      },
+      "minecraft:spider_player_jockey": {
+        "minecraft:type_family": { "family": [ "spider", "monster", "mob", "arthropod", "spider_sword" ] },
+        "minecraft:input_ground_controlled": {},
+        "minecraft:behavior.controlled_by_player": { "priority": 0 },
+        "minecraft:can_power_jump": {},
+        "minecraft:horse.jump_strength": { "value": { "range_min": 0.4, "range_max": 0.7 } },
+        "minecraft:loot": { "table": "loot_tables/entities/empty.json" },
+        "minecraft:health": { "value": 20, "max": 20 },
+        "minecraft:rideable": {
+          "seat_count": 1,
+            "family_types": [
+            "player"
+          ],
+          "seats": {
+            "position": [ 0.0, 0.54, 0.0 ]
+          }
+        },
+        "minecraft:environment_sensor": {
+          "triggers": [
+            {
+              "filters": {},
+              "event": "not_climb"
+            }
+          ]
+        }
+      },
+      "minecraft:spider_jockey": {
+        "minecraft:addrider": {
+          "entity_type": "minecraft:skeleton"
+        },
+        "minecraft:rideable": {
+          "seat_count": 1,
+          "family_types": [
+            "skeleton"
+          ],
+          "seats": {
+            "position": [ 0.0, 0.54, 0.0 ]
+          }
+        }
+      },
+      "minecraft:spider_stray_jockey": {
+        "minecraft:addrider": {
+          "entity_type": "minecraft:skeleton.stray"
+        },
+        "minecraft:rideable": {
+          "seat_count": 1,
+          "family_types": [
+            "skeleton"
+          ],
+          "seats": {
+            "position": [ 0.0, 0.54, 0.0 ]
+          }
+        }
+      },
+      "minecraft:spider_wither_jockey": {
+        "minecraft:addrider": {
+          "entity_type": "minecraft:skeleton.wither"
+        },
+        "minecraft:rideable": {
+          "seat_count": 1,
+          "family_types": [
+            "skeleton"
+          ],
+          "seats": {
+            "position": [ 0.0, 0.54, 0.0 ]
+          }
+        }
+      },
+      "minecraft:spider_neutral": {
+        "minecraft:environment_sensor": {
+          "triggers": {
+            "filters": {
+              "test": "is_brightness",
+              "operator": "<",
+              "value": 0.49
+            },
+            "event": "minecraft:become_hostile"
+          }
+        },
+        "minecraft:on_target_acquired": {
+          "event": "minecraft:become_angry"
+        }
+      },
+      "minecraft:spider_hostile": {
+        "minecraft:environment_sensor": {
+          "triggers": {
+            "filters": {
+              "test": "is_brightness",
+              "operator": ">",
+              "value": 0.49
+            },
+            "event": "minecraft:become_neutral"
+          }
+        },
+        "minecraft:on_target_acquired": {
+          "event": "minecraft:become_angry"
+        },
+        "minecraft:behavior.nearest_attackable_target": {
+          "priority": 2,
+          "entity_types": [
+            {
+              "filters": {
+                "any_of": [
+                  {
+                    "test": "is_family",
+                    "subject": "other",
+                    "value": "player"
+                  },
+                  {
+                    "test": "is_family",
+                    "subject": "other",
+                    "value": "snowgolem"
+                  },
+                  {
+                    "test": "is_family",
+                    "subject": "other",
+                    "value": "irongolem"
+                  }
+                ]
+              },
+              "max_dist": 16
+            }
+          ],
+          "attack_interval": 5,
+          "must_see": true
+        }
+      },
+      "minecraft:spider_angry": {
+        "minecraft:angry": {
+          "duration": 10,
+          "duration_delta": 3,
+          "calm_event": {
+            "event": "minecraft:become_calm",
+            "target": "self"
+          }
+        },
+        "minecraft:behavior.leap_at_target": {
+          "priority": 4,
+          "yd": 0.4,
+          "must_be_on_ground": false
+        },
+        "minecraft:behavior.melee_attack": {
+          "priority": 3,
+          "speed_multiplier": 1.0,
+          "track_target": true,
+          "reach_multiplier": 0.8
+        }
+      },
+      "minecraft:default_spider": {
+        "minecraft:behavior.hurt_by_target": { 
+          "priority": 1 
+        },
+        "minecraft:behavior.random_stroll": {
+        "priority": 6,
+        "speed_multiplier": 0.8
+      },
+      "minecraft:behavior.look_at_player": {
+        "priority": 7,
+        "look_distance": 6.0,
+        "probability": 0.02
+      },
+      "minecraft:behavior.random_look_around": {
+        "priority": 7
+        }
       }
     },
     "components": {
+      "minecraft:experience_reward": {
+        "on_death": "query.last_hit_by_player ? 5 : 0"
+      },
+      "minecraft:nameable": {
+      },
       "minecraft:type_family": {
-        "family": [
-          "despawnear"
+        "family": [ "spider", "monster", "mob", "arthropod" ]
+      },
+      "minecraft:breathable": {
+        "total_supply": 15,
+        "suffocate_time": 0
+      },
+      "minecraft:loot": {
+        "table": "loot_tables/entities/spider.json"
+      },
+      "minecraft:collision_box": {
+        "width": 1.4,
+        "height": 0.9
+      },
+      "minecraft:health": {
+        "value": 16,
+        "max": 16
+      },
+      "minecraft:hurt_on_condition": {
+        "damage_conditions": [
+          {
+            "filters": { "test": "in_lava", "subject": "self", "operator": "==", "value": true },
+            "cause": "lava",
+            "damage_per_tick": 4
+          }
         ]
       },
+      "minecraft:movement": {
+        "value": 0.3
+      },
+      "minecraft:navigation.climb": {
+        "can_path_over_water": true
+      },
+      "minecraft:movement.basic": {
+      },
+      "minecraft:jump.static": {
+      },
+      "minecraft:can_climb": {
+      },
+      "minecraft:attack": {
+        "damage": 3
+      },
+      "minecraft:behavior.float": {
+        "priority": 1
+      },
+      "minecraft:behavior.mount_pathing": {
+        "priority": 5,
+        "speed_multiplier": 1.25,
+        "target_dist": 0.0,
+        "track_target": true
+      },
+      "minecraft:rideable": {
+        "seat_count": 1,
+        "family_types": [
+          "zombie"
+        ],
+        "seats": {
+          "position": [ 0.0, 0.54, -0.1 ]
+        }
+      },
+      "minecraft:physics": {
+      },
+      "minecraft:pushable": {
+        "is_pushable": true,
+        "is_pushable_by_piston": true
+      }
+    },
+
+    "events": {
+      "minecraft:entity_spawned": {
+        "sequence": [
+        {
+          "add": { "component_groups": [ "minecraft:default_spider" ] }
+        },
+        {
+        "randomize": [
+          {
+            "weight": 1,
+            "randomize": [
+              {
+                "weight": 80,
+                "filters": {
+                  "all_of": [
+                    {
+                      "test": "is_daytime",
+                      "value": false
+                    },
+                    {
+                      "test": "is_snow_covered",
+                      "value": true
+                    },
+                    {
+                      "test": "is_underground",
+                      "value": false
+                    }
+                  ]
+                },
+                "remove": {},
+                "add": {
+                  "component_groups": [
+                    "minecraft:spider_stray_jockey",
+                    "minecraft:spider_neutral"
+                  ]
+                }
+              },
+              {
+                "weight": 80,
+                "filters": {
+                  "test": "is_biome",
+                  "value": "the_nether"
+                },
+                "remove": {},
+                "add": {
+                  "component_groups": [
+                    "minecraft:spider_wither_jockey",
+                    "minecraft:spider_neutral"
+                  ]
+                }
+              },
+              {
+                "weight": 20,
+                "filters": {
+                  "any_of": [
+                    {
+                      "test": "is_daytime",
+                      "value": false
+                    },
+                    {
+                      "test": "is_underground",
+                      "value": true
+                    }
+                  ]
+                },
+                "remove": {},
+                "add": {
+                  "component_groups": [
+                    "minecraft:spider_jockey",
+                    "minecraft:spider_neutral"
+                  ]
+                }
+              }
+            ]
+          },
+          {
+            "weight": 99,
+            "remove": {},
+              "add": {
+                "component_groups": [
+                  "minecraft:spider_neutral"
+                  ]
+                }
+              }
+            ]
+          }
+        ]
+      },
+      "minecraft:become_hostile": {
+        "remove": {
+          "component_groups": [
+            "minecraft:spider_neutral"
+          ]
+        },
+        "add": {
+          "component_groups": [
+            "minecraft:spider_hostile"
+          ]
+        }
+      },
+      "minecraft:become_neutral": {
+        "remove": {
+          "component_groups": [
+            "minecraft:spider_hostile"
+          ]
+        },
+        "add": {
+          "component_groups": [
+            "minecraft:spider_neutral"
+          ]
+        }
+      },
+      "minecraft:become_angry": {
+        "add": {
+          "component_groups": [
+            "minecraft:spider_angry"
+          ]
+        }
+      },
+      "minecraft:become_calm": {
+        "remove": {
+          "component_groups": [
+            "minecraft:spider_angry"
+          ]
+        }
+      },
+      "minecraft:spider_sword": {
+        "remove": {
+          "component_groups": [
+            "minecraft:spider_hostile",
+            "minecraft:spider_neutral",
+            "minecraft:default_spider"
+          ]
+        },
+        "add": {
+          "component_groups": [
+            "minecraft:spider_player_jockey"
+          ]
+        }
+      },
       "minecraft:despawn": {
-        "filters": {
-          "all_of": [
-            {
-              "test": "is_family",
-              "subject": "self",
-              "value": "despawnear"
-            }
-          ]
-        }
-      },
-      "minecraft:health": {
-        "value": 1
-      },
-      "minecraft:collision_box": {
-       "width": 0.0,
-       "height": 0.0
-     },
-      "minecraft:fire_immune": true,
-      "minecraft:physics": {}
+        "sequence": [
+          {
+           "filters": { "test": "is_family", "subject": "self", "operator": "==", "value": "spider_sword" },
+           "add": { "component_groups": [ "despawn" ] },
+           "run_command": { "command": [ "particle minecraft:example_linearcurve ~ ~ ~", "playsound random.fizz @a[r=16]" ] }
+          }
+        ]
+      },
+      "not_climb": {
+        "run_command": {
+          "command": [ "execute @s ~~~ detect ~0.8 ~ ~ air 0 execute @s ~~~ detect ~-0.8 ~ ~ air 0 execute @s ~~~ detect ~ ~ ~0.8 air 0 execute @s ~~~ detect ~ ~ ~-0.8 air 0 effect @s levitation 0 0 true" ]
+        }
+      }
     }
   }
 }
```

### `Swords_B/functions/give.mcfunction`

```diff
--- 1.6/Sword_B/functions/give.mcfunction
+++ 2.8.14/Swords_B/functions/give.mcfunction
@@ -11,7 +11,7 @@
 give @p effect:ice_sword
 give @p effect:jungle_sword
 give @p effect:lapis_sword
-give @p effect:lightning_sword
+give @s effect:lightning_sword
 give @p effect:magma_sword
 give @p effect:obsidian_sword
 give @p effect:quartz_sword
@@ -21,6 +21,15 @@
 give @p effect:spectral_sword
 give @p effect:spider_sword
 give @p effect:sponge_sword
-give @p effect:sword_of_time
+give @p effect:time_sword
 give @p effect:tnt_sword
 give @p effect:wither_sword
+give @p effect:wolf_sword
+give @p effect:ultra_instinct_sword
+give @p effect:wither_skeleton_sword
+give @p effect:glass_sword
+give @p effect:clock_sword
+give @p effect:ghost_sword
+give @p effect:bedrock_sword
+give @p effect:nether_star_sword
+give @p effect:silver_sword
```

### `Swords_B/items/blaze_sword.json`

```diff
--- 1.6/Sword_B/items/blaze_sword.json
+++ 2.8.14/Swords_B/items/blaze_sword.json
@@ -1,41 +1,40 @@
 {
-  "format_version": "1.20.20",
+  "format_version": "1.16.100",
   "minecraft:item": {
-	"description": {
-   "identifier": "effect:blaze_sword",
-      "menu_category": {
-       	"category": "equipment"
-      }
-		},
-		"components": {
-      "minecraft:glint": false,
-			"minecraft:max_stack_size": 1,
-			"minecraft:enchantable": {
-				"value": 9,
-				"slot": "sword"
-			},
-
-   "minecraft:durability": {
+    "description": {
+      "identifier": "effect:blaze_sword",
+      "category": "equipment"
+    },
+    "components": {
+      "minecraft:foil": false,
+      "minecraft:max_stack_size": 1,
+      "minecraft:enchantable": {
+        "value": 9,
+        "slot": "sword"
+      },
+      "minecraft:durability": {
         "max_durability": 2300
       },
-			"minecraft:allow_off_hand": true,
-			"minecraft:hand_equipped": true,
-			
-			"minecraft:can_destroy_in_creative": false,
-			"minecraft:icon": {
-				"texture": "blaze_sword"
-			},
-						 "minecraft:repairable": {
-      "repair_items": [
+      "minecraft:allow_off_hand": false,
+      "minecraft:hand_equipped": true,
+      "minecraft:creative_category": {
+        "parent": "itemGroup.name.sword"
+      },
+      "minecraft:can_destroy_in_creative": false,
+      "minecraft:icon": {
+        "texture": "blaze_sword"
+      },
+      "minecraft:repairable": {
+        "repair_items": [
           {
-              "items":[
-                  "effect:blaze_sword"
-              ],
-              "repair_amount": 2300
+            "items": [
+              "effect:blaze_sword"
+            ],
+            "repair_amount": 2300
           }
-      ]
-  },
-			      "minecraft:digger": {
+        ]
+      },
+      "minecraft:digger": {
         "use_efficiency": true,
         "destroy_speeds": [
           {
@@ -48,8 +47,91 @@
           }
         ]
       },
-      "tag:minecraft:is_sword": {},
-			"minecraft:damage": 8
-		}
-	}
+      "minecraft:display_name": {},
+      "minecraft:cooldown": {
+        "category": "blaze_sword",
+        "duration": 20
+      },
+      "minecraft:on_use": {
+        "on_use": {
+          "event": "on_use"
+        }
+      },
+      "minecraft:damage": 6,
+      "minecraft:weapon": {
+        "on_hurt_entity": {
+          "event": "weapon"
+        },
+        "on_not_hurt_entity": {
+          "event": "weapon"
+        },
+        "on_hit_block": {
+          "event": "weapon"
+        }
+      }
+    },
+    "events": {
+      "on_use": {
+        "damage": {
+          "type": "durability",
+          "amount": 10,
+          "target": "self"
+        },
+        "run_command": {
+          "command": [
+            "event entity @s[family=blaze_sword] blaze_sword_skill_event",
+            "effect @s levitation 7 0 true",
+            "effect @s slow_falling 10 3 true"
+          ]
+        }
+      },
+      "weapon": {
+        "sequence": [
+          {
+            "damage": {
+              "type": "durability",
+              "amount": 1,
+              "target": "self"
+            }
+          },
+          {
+            "randomize": [
+              {
+                "weight": 14,
+                "run_command": {
+                  "command": [
+                    "effect @s fire_resistance 1 0 true"
+                  ]
+                },
+                "shoot": {
+                  "projectile": "minecraft:small_fireball",
+                  "launch_power": 1
+                }
+              },
+              {
+                "weight": 1,
+                "run_command": {
+                  "command": [
+                    "effect @s fire_resistance 1 0 true"
+                  ]
+                },
+                "shoot": {
+                  "projectile": "minecraft:fireball",
+                  "launch_power": 1
+                }
+              },
+              {
+                "weight": 85,
+                "damage": {
+                  "type": "durability",
+                  "amount": 1,
+                  "target": "self"
+                }
+              }
+            ]
+          }
+        ]
+      }
+    }
+  }
 }
```

### `Swords_B/items/bone_sword.json`

```diff
--- 1.6/Sword_B/items/bone_sword.json
+++ 2.8.14/Swords_B/items/bone_sword.json
@@ -1,41 +1,58 @@
 {
-  "format_version": "1.20.20",
+  "format_version": "1.16.100",
   "minecraft:item": {
-	"description": {
-   "identifier": "effect:bone_sword",
-			"menu_category": {
-        "category": "equipment"
-      }
-		},
-		"components": {
-            "minecraft:glint": false,
-			"minecraft:max_stack_size": 1,
-			"minecraft:enchantable": {
-				"value": 9,
-				"slot": "sword"
-			},
-
-   "minecraft:durability": {
+    "description": {
+      "identifier": "effect:bone_sword",
+      "category": "equipment"
+    },
+    "components": {
+      "minecraft:foil": false,
+      "minecraft:max_stack_size": 1,
+      "minecraft:enchantable": {
+        "value": 9,
+        "slot": "sword"
+      },
+      "minecraft:durability": {
         "max_durability": 820
       },
-			"minecraft:allow_off_hand": true,
-			"minecraft:hand_equipped": true,
-			
-			"minecraft:can_destroy_in_creative": false,
-			"minecraft:icon": {
-				"texture": "bone_sword"
-			},
-						 "minecraft:repairable": {
-      "repair_items": [
+      "minecraft:allow_off_hand": false,
+      "minecraft:hand_equipped": true,
+      "minecraft:creative_category": {
+        "parent": "itemGroup.name.sword"
+      },
+      "minecraft:can_destroy_in_creative": false,
+      "minecraft:icon": {
+        "texture": "bone_sword"
+      },
+      "minecraft:repairable": {
+        "repair_items": [
           {
-              "items":[
-                  "effect:bone_sword"
-              ],
-              "repair_amount": 820
+            "items": [
+              "effect:bone_sword"
+            ],
+            "repair_amount": 820
+          },
+          {
+            "items": [
+              "minecraft:bone"
+            ],
+            "repair_amount": 70
+          },
+          {
+            "items": [
+              "minecraft:bone_block"
+            ],
+            "repair_amount": 300
+          },
+          {
+            "items": [
+              "minecraft:bone_meal"
+            ],
+            "repair_amount": 18
           }
-      ]
-  },
-			      "minecraft:digger": {
+        ]
+      },
+      "minecraft:digger": {
         "use_efficiency": true,
         "destroy_speeds": [
           {
@@ -48,10 +65,51 @@
           }
         ]
       },
-      "tag:minecraft:is_sword": {},
-			
-			
-			"minecraft:damage": 7
-		}
-	}
+      "minecraft:display_name": {},
+      "minecraft:damage": 5,
+      "minecraft:weapon": {
+        "on_hurt_entity": {
+          "event": "weapon"
+        },
+        "on_not_hurt_entity": {
+          "event": "weapon"
+        },
+        "on_hit_block": {
+          "event": "weapon"
+        }
+      }
+    },
+    "events": {
+      "weapon": {
+        "sequence": [
+          {
+            "damage": {
+              "type": "durability",
+              "amount": 1,
+              "target": "self"
+            }
+          },
+          {
+            "randomize": [
+              {
+                "weight": 20,
+                "shoot": {
+                  "projectile": "minecraft:arrow",
+                  "launch_power": 1
+                }
+              },
+              {
+                "weight": 80,
+                "damage": {
+                  "type": "durability",
+                  "amount": 1,
+                  "target": "self"
+                }
+              }
+            ]
+          }
+        ]
+      }
+    }
+  }
 }
```

### `Swords_B/items/cactus_sword.json`

```diff
--- 1.6/Sword_B/items/cactus_sword.json
+++ 2.8.14/Swords_B/items/cactus_sword.json
@@ -1,41 +1,40 @@
 {
-  "format_version": "1.20.20",
+  "format_version": "1.16.100",
   "minecraft:item": {
-	"description": {
-   "identifier": "effect:cactus_sword",
-			"menu_category": {
-        "category": "equipment"
-      }
-		},
-		"components": {
-            "minecraft:glint": false,
-			"minecraft:max_stack_size": 1,
-			"minecraft:enchantable": {
-				"value": 9,
-				"slot": "sword"
-			},
-
-   "minecraft:durability": {
+    "description": {
+      "identifier": "effect:cactus_sword",
+      "category": "equipment"
+    },
+    "components": {
+      "minecraft:foil": false,
+      "minecraft:max_stack_size": 1,
+      "minecraft:enchantable": {
+        "value": 9,
+        "slot": "sword"
+      },
+      "minecraft:durability": {
         "max_durability": 125
       },
-			"minecraft:allow_off_hand": true,
-			"minecraft:hand_equipped": true,
-			
-			"minecraft:can_destroy_in_creative": false,
-			"minecraft:icon": {
-				"texture": "cactus_sword"
-			},
-						 "minecraft:repairable": {
-      "repair_items": [
+      "minecraft:allow_off_hand": false,
+      "minecraft:hand_equipped": true,
+      "minecraft:creative_category": {
+        "parent": "itemGroup.name.sword"
+      },
+      "minecraft:can_destroy_in_creative": false,
+      "minecraft:icon": {
+        "texture": "cactus_sword"
+      },
+      "minecraft:repairable": {
+        "repair_items": [
           {
-              "items":[
-                  "effect:cactus_sword"
-              ],
-              "repair_amount": 125
+            "items": [
+              "effect:cactus_sword"
+            ],
+            "repair_amount": 125
           }
-      ]
-  },
-			      "minecraft:digger": {
+        ]
+      },
+      "minecraft:digger": {
         "use_efficiency": true,
         "destroy_speeds": [
           {
@@ -48,10 +47,44 @@
           }
         ]
       },
-      "tag:minecraft:is_sword": {},
-			
-			
-			"minecraft:damage": 6
-		}
-	}
+      "minecraft:render_offsets": {
+        "main_hand": {
+          "first_person": {
+            "position": [ 
+              0.67, //x
+              0, //y = First person.
+              -1.24 //z
+            ]
+          },
+          "third_person": {
+            "position": [ 
+              0.36, //x
+              1.5, //z = Mirando la entidad desde al frente.
+              -0.66 //y
+            ]
+          }
+        }
+      },
+      "minecraft:display_name": {},
+      "minecraft:damage": 6,
+      "minecraft:weapon": {
+        "on_hurt_entity": {
+          "event": "weapon"
+        }
+      }
+    },
+    "events": {
+      "weapon": {
+        "sequence": [
+          {
+            "damage": {
+              "type": "durability",
+              "amount": 1,
+              "target": "self"
+            }
+          }
+        ]
+      }
+    }
+  }
 }
```

### `Swords_B/items/coal_sword.json`

```diff
--- 1.6/Sword_B/items/coal_sword.json
+++ 2.8.14/Swords_B/items/coal_sword.json
@@ -1,41 +1,55 @@
 {
-  "format_version": "1.20.20",
+  "format_version": "1.16.100",
   "minecraft:item": {
-	"description": {
-   "identifier": "effect:coal_sword",
-			"menu_category": {
-        "category": "equipment"
-      }
-		},
-		"components": {
-            "minecraft:glint": false,
-			"minecraft:max_stack_size": 1,
-			"minecraft:enchantable": {
-				"value": 9,
-				"slot": "sword"
-			},
-
-   "minecraft:durability": {
+    "description": {
+      "identifier": "effect:coal_sword",
+      "category": "equipment"
+    },
+    "components": {
+      "minecraft:foil": false,
+      "minecraft:max_stack_size": 1,
+      "minecraft:enchantable": {
+        "value": 9,
+        "slot": "sword"
+      },
+      "minecraft:durability": {
         "max_durability": 121
       },
-			"minecraft:allow_off_hand": true,
-			"minecraft:hand_equipped": true,
-			
-			"minecraft:can_destroy_in_creative": false,
-			"minecraft:icon": {
-				"texture": "coal_sword"
-			},
-						 "minecraft:repairable": {
-      "repair_items": [
+      "minecraft:allow_off_hand": false,
+      "minecraft:hand_equipped": true,
+      "minecraft:creative_category": {
+        "parent": "itemGroup.name.sword"
+      },
+      "minecraft:can_destroy_in_creative": false,
+      "minecraft:icon": {
+        "texture": "coal_sword"
+      },
+      "minecraft:fuel": {
+        "duration": 360.0
+      },
+      "minecraft:repairable": {
+        "repair_items": [
           {
-              "items":[
-                  "effect:coal_sword"
-              ],
-              "repair_amount": 121
+            "items": [
+              "effect:coal_sword"
+            ],
+            "repair_amount": 121
+          },
+          {
+            "items": [
+              "minecraft:coal"
+            ],
+            "repair_amount": 58
+          },
+          {
+            "items": [
+              "minecraft:stick"
+            ],
+            "repair_amount": 2
           }
-      ]
-  },
-			      "minecraft:digger": {
+        ]
+      },
+      "minecraft:digger": {
         "use_efficiency": true,
         "destroy_speeds": [
           {
@@ -48,10 +62,26 @@
           }
         ]
       },
-      "tag:minecraft:is_sword": {},
-			
-			
-			"minecraft:damage": 6
-		}
-	}
+      "minecraft:display_name": {},
+      "minecraft:damage": 4,
+      "minecraft:weapon": {
+        "on_hurt_entity": {
+          "event": "weapon"
+        }
+      }
+    },
+    "events": {
+      "weapon": {
+        "sequence": [
+          {
+            "damage": {
+              "type": "durability",
+              "amount": 1,
+              "target": "self"
+            }
+          }
+        ]
+      }
+    }
+  }
 }
```

### `Swords_B/items/creeper_sword.json`

```diff
--- 1.6/Sword_B/items/creeper_sword.json
+++ 2.8.14/Swords_B/items/creeper_sword.json
@@ -1,41 +1,51 @@
 {
-  "format_version": "1.20.20",
+  "format_version": "1.16.100",
   "minecraft:item": {
-	"description": {
-   "identifier": "effect:creeper_sword",
-			"menu_category": {
-        "category": "equipment"
-      }
-		},
-		"components": {
-            "minecraft:glint": false,
-			"minecraft:max_stack_size": 1,
-			"minecraft:enchantable": {
-				"value": 9,
-				"slot": "sword"
-			},
-
-   "minecraft:durability": {
+    "description": {
+      "identifier": "effect:creeper_sword",
+      "category": "equipment"
+    },
+    "components": {
+      
+      "minecraft:foil": false,
+      "minecraft:max_stack_size": 1,
+      "minecraft:enchantable": {
+        "value": 9,
+        "slot": "sword"
+      },
+      "minecraft:durability": {
         "max_durability": 1500
       },
-			"minecraft:allow_off_hand": true,
-			"minecraft:hand_equipped": true,
-			
-			"minecraft:can_destroy_in_creative": false,
-			"minecraft:icon": {
-				"texture": "creeper_sword"
-			},
-						 "minecraft:repairable": {
-      "repair_items": [
+      "minecraft:cooldown": {
+        "category": "creeper_sword",
+        "duration": 3
+      },
+      "minecraft:allow_off_hand": false,
+      "minecraft:hand_equipped": true,
+      "minecraft:creative_category": {
+        "parent": "itemGroup.name.sword"
+      },
+      "minecraft:can_destroy_in_creative": false,
+      "minecraft:icon": {
+        "texture": "creeper_sword"
+      },
+      "minecraft:repairable": {
+        "repair_items": [
           {
-              "items":[
-                  "effect:creeper_sword"
-              ],
-              "repair_amount": 1500
+            "items": [
+              "effect:creeper_sword"
+            ],
+            "repair_amount": 1500
+          },
+          {
+            "items": [
+              "minecraft:gunpowder"
+            ],
+            "repair_amount": 256
           }
-      ]
-  },
-			      "minecraft:digger": {
+        ]
+      },
+      "minecraft:digger": {
         "use_efficiency": true,
         "destroy_speeds": [
           {
@@ -48,10 +58,75 @@
           }
         ]
       },
-      "tag:minecraft:is_sword": {},
-			
-			
-			"minecraft:damage": 8
-		}
-	}
+      "minecraft:display_name": {},
+      "minecraft:damage": 6,
+      "minecraft:on_use": {
+        "on_use": {
+          "event": "on_use"
+        }
+      },
+      "minecraft:weapon": {
+        "on_hurt_entity": {
+          "event": "weapon"
+        },
+        "on_not_hurt_entity": {
+          "event": "weapon"
+        },
+        "on_hit_block": {
+          "event": "weapon"
+        }
+      }
+    },
+    "events": {
+      "on_use": {
+        "sequence": [
+          {
+            "run_command": {
+              "command": [
+                "event entity @s start_player_explode_event"
+              ],
+              "target": "holder"
+            }
+          },
+          {
+            "damage": {
+              "type": "durability",
+              "amount": 1,
+              "target": "self"
+            }
+          }
+        ]
+      },
+      "weapon": {
+        "sequence": [
+          {
+            "damage": {
+              "type": "durability",
+              "amount": 1,
+              "target": "self"
+            }
+          },
+          {
+            "randomize": [
+              {
+                "weight": 20,
+                "shoot": {
+                  "projectile": "minecraft:creeper",
+                  "launch_power": 1
+                }
+              },
+              {
+                "weight": 80,
+                "damage": {
+                  "type": "durability",
+                  "amount": 1,
+                  "target": "self"
+                }
+              }
+            ]
+          }
+        ]
+      }
+    }
+  }
 }
```

### `Swords_B/items/emerald_sword.json`

```diff
--- 1.6/Sword_B/items/emerald_sword.json
+++ 2.8.14/Swords_B/items/emerald_sword.json
@@ -1,41 +1,40 @@
 {
-  "format_version": "1.20.20",
+  "format_version": "1.16.100",
   "minecraft:item": {
-	"description": {
-   "identifier": "effect:emerald_sword",
-			"menu_category": {
-        "category": "equipment"
-      }
-		},
-		"components": {
-            "minecraft:glint": false,
-			"minecraft:max_stack_size": 1,
-			"minecraft:enchantable": {
-				"value": 9,
-				"slot": "sword"
-			},
-
-   "minecraft:durability": {
+    "description": {
+      "identifier": "effect:emerald_sword",
+      "category": "equipment"
+    },
+    "components": {
+      "minecraft:foil": false,
+      "minecraft:max_stack_size": 1,
+      "minecraft:enchantable": {
+        "value": 9,
+        "slot": "sword"
+      },
+      "minecraft:durability": {
         "max_durability": 2300
       },
-			"minecraft:allow_off_hand": true,
-			"minecraft:hand_equipped": true,
-			
-			"minecraft:can_destroy_in_creative": false,
-			"minecraft:icon": {
-				"texture": "emerald_sword"
-			},
-						 "minecraft:repairable": {
-      "repair_items": [
+      "minecraft:allow_off_hand": false,
+      "minecraft:hand_equipped": true,
+      "minecraft:creative_category": {
+        "parent": "itemGroup.name.sword"
+      },
+      "minecraft:can_destroy_in_creative": false,
+      "minecraft:icon": {
+        "texture": "emerald_sword"
+      },
+      "minecraft:repairable": {
+        "repair_items": [
           {
-              "items":[
-                  "effect:emerald_sword"
-              ],
-              "repair_amount": 2300
+            "items": [
+              "effect:emerald_sword"
+            ],
+            "repair_amount": 2300
           }
-      ]
-  },
-			      "minecraft:digger": {
+        ]
+      },
+      "minecraft:digger": {
         "use_efficiency": true,
         "destroy_speeds": [
           {
@@ -48,10 +47,32 @@
           }
         ]
       },
-      "tag:minecraft:is_sword": {},
-			
-			
-			"minecraft:damage": 7
-		}
-	}
+      "minecraft:display_name": {},
+      "minecraft:damage": 7,
+      "minecraft:weapon": {
+        "on_hurt_entity": {
+          "event": "weapon"
+        },
+        "on_not_hurt_entity": {
+          "event": "weapon"
+        },
+        "on_hit_block": {
+          "event": "weapon"
+        }
+      }
+    },
+    "events": {
+      "weapon": {
+        "sequence": [
+          {
+            "damage": {
+              "type": "durability",
+              "amount": 1,
+              "target": "self"
+            }
+          }
+        ]
+      }
+    }
+  }
 }
```

### `Swords_B/items/ender_sword.json`

```diff
--- 1.6/Sword_B/items/ender_sword.json
+++ 2.8.14/Swords_B/items/ender_sword.json
@@ -1,41 +1,52 @@
 {
-  "format_version": "1.20.20",
+  "format_version": "1.16.100",
   "minecraft:item": {
-	"description": {
-   "identifier": "effect:ender_sword",
-			"menu_category": {
-        "category": "equipment"
-      }
-		},
-		"components": {
-            "minecraft:glint": true,
-			"minecraft:max_stack_size": 1,
-			"minecraft:enchantable": {
-				"value": 9,
-				"slot": "sword"
-			},
-
-   "minecraft:durability": {
+    "description": {
+      "identifier": "effect:ender_sword",
+      "category": "equipment"
+    },
+    "components": {
+      "minecraft:foil": true,
+      "minecraft:max_stack_size": 1,
+      "minecraft:enchantable": {
+        "value": 9,
+        "slot": "sword"
+      },
+      "minecraft:durability": {
         "max_durability": 1256
       },
-			"minecraft:allow_off_hand": true,
-			"minecraft:hand_equipped": true,
-			
-			"minecraft:can_destroy_in_creative": false,
-			"minecraft:icon": {
-				"texture": "ender_sword"
-			},
-						 "minecraft:repairable": {
-      "repair_items": [
+      "minecraft:allow_off_hand": false,
+      "minecraft:hand_equipped": true,
+      "minecraft:creative_category": {
+        "parent": "itemGroup.name.sword"
+      },
+      "minecraft:can_destroy_in_creative": false,
+      "minecraft:icon": {
+        "texture": "ender_sword"
+      },
+      "minecraft:repairable": {
+        "repair_items": [
           {
-              "items":[
-                  "effect:ender_sword"
-              ],
-              "repair_amount": 1256
+            "items": [
+              "effect:ender_sword"
+            ],
+            "repair_amount": 1256
+          },
+          {
+            "items": [
+              "minecraft:ender_pearl"
+            ],
+            "repair_amount": 28
+          },
+          {
+            "items": [
+              "minecraft:ender_eye"
+            ],
+            "repair_amount": 32
           }
-      ]
-  },
-			      "minecraft:digger": {
+        ]
+      },
+      "minecraft:digger": {
         "use_efficiency": true,
         "destroy_speeds": [
           {
@@ -48,10 +59,67 @@
           }
         ]
       },
-      "tag:minecraft:is_sword": {},
-			
-			
-			"minecraft:damage": 9
-		}
-	}
+      "minecraft:render_offsets": {
+        "main_hand": {
+          "first_person": {
+            "position": [ 
+              1, //x
+              0.4, //y = First person.
+              -3 //z
+            ],
+            "scale": [
+              0.04,
+              0.04,
+              0.04
+            ]
+          },
+          "third_person": {
+            "position": [ 
+              0.5, //x
+              1.6, //z = Mirando la entidad desde al frente.
+              -0.8   //y
+            ],
+            "scale": [
+              0.038,
+              0.038,
+              0.038
+            ]
+          }
+        }
+      },
+      "minecraft:display_name": {},
+      "minecraft:damage": 9,
+      "minecraft:cooldown": {
+        "category": "ender_sword",
+        "duration": 2
+      },
+      "minecraft:on_use": {
+        "on_use": {
+          "event": "on_use"
+        }
+      },
+      "minecraft:weapon": {
+        "on_hurt_entity": {
+          "event": "weapon"
+        }
+      }
+    },
+    "events": {
+      "on_use": {
+        "run_command": { "command": [ "spreadplayers ~ ~ 16 32 @s", "playsound mob.endermen.portal @a[r=34]" ] },
+        "damage": { "type": "durability", "amount": 5, "target": "self"  }
+      },
+      "weapon": {
+        "sequence": [
+          {
+            "damage": {
+              "type": "durability",
+              "amount": 1,
+              "target": "self"
+            }
+          }
+        ]
+      }
+    }
+  }
 }
```

### `Swords_B/items/fire_sword.json`

```diff
--- 1.6/Sword_B/items/fire_sword.json
+++ 2.8.14/Swords_B/items/fire_sword.json
@@ -1,41 +1,50 @@
 {
-  "format_version": "1.20.20",
+  "format_version": "1.16.100",
   "minecraft:item": {
-	"description": {
-   "identifier": "effect:fire_sword",
-			"menu_category": {
-        "category": "equipment"
-      }
-		},
-		"components": {
-            "minecraft:glint": false,
-			"minecraft:max_stack_size": 1,
-			"minecraft:enchantable": {
-				"value": 9,
-				"slot": "sword"
-			},
-
-   "minecraft:durability": {
+    "description": {
+      "identifier": "effect:fire_sword",
+      "category": "equipment"
+    },
+    "components": {
+      "minecraft:foil": true,
+      "minecraft:max_stack_size": 1,
+      "minecraft:enchantable": {
+        "value": 9,
+        "slot": "sword"
+      },
+      "minecraft:durability": {
         "max_durability": 2000
       },
-			"minecraft:allow_off_hand": true,
-			"minecraft:hand_equipped": true,
-			
-			"minecraft:can_destroy_in_creative": false,
-			"minecraft:icon": {
-				"texture": "fire_sword"
-			},
-						 "minecraft:repairable": {
-      "repair_items": [
+      "minecraft:cooldown": {
+        "category": "fire_sword",
+        "duration": 25
+      },
+      "minecraft:allow_off_hand": false,
+      "minecraft:hand_equipped": true,
+      "minecraft:creative_category": {
+        "parent": "itemGroup.name.sword"
+      },
+      "minecraft:can_destroy_in_creative": false,
+      "minecraft:icon": {
+        "texture": "fire_sword"
+      },
+      "minecraft:repairable": {
+        "repair_items": [
           {
-              "items":[
-                  "effect:fire_sword"
-              ],
-              "repair_amount": 2000
+            "items": [
+              "effect:fire_sword"
+            ],
+            "repair_amount": 2000
+          },
+          {
+            "items": [
+              "minecraft:fire"
+            ],
+            "repair_amount": 1000
           }
-      ]
-  },
-			      "minecraft:digger": {
+        ]
+      },
+      "minecraft:digger": {
         "use_efficiency": true,
         "destroy_speeds": [
           {
@@ -48,10 +57,81 @@
           }
         ]
       },
-      "tag:minecraft:is_sword": {},
-			
-			
-			"minecraft:damage": 12
-		}
-	}
+      "minecraft:display_name": {},
+      "minecraft:damage": 6,
+      "minecraft:on_use": {
+        "on_use": {
+          "event": "on_use"
+        }
+      },
+      "minecraft:weapon": {
+        "on_hurt_entity": {
+          "event": "weapon"
+        },
+        "on_not_hurt_entity": {
+          "event": "weapon"
+        },
+        "on_hit_block": {
+          "event": "weapon"
+        }
+      }
+    },
+    "events": {
+      "on_use": {
+        "sequence": [
+          {
+            "run_command": {
+              "command": [
+                "summon entity:living_flame ~ ~14 ~ minecraft:target",
+                "summon entity:living_flame ~ ~4 ~ fire_sword_skill",
+                "summon entity:living_flame ~3 ~4 ~ fire_sword_skill",
+                "summon entity:living_flame ~ ~4 ~3 fire_sword_skill",
+                "summon entity:living_flame ~-3 ~4 ~ fire_sword_skill",
+                "summon entity:living_flame ~ ~4 ~-3 fire_sword_skill",
+                "particle minecraft:example_linearcurve ~ ~0.2 ~",
+                "title @s actionbar §l§6Fire rain"
+              ],
+              "target": "holder"
+            }
+          },
+          {
+            "damage": {
+              "type": "durability",
+              "amount": 20,
+              "target": "self"
+            }
+          }
+        ]
+      },
+      "weapon": {
+        "sequence": [
+          {
+            "damage": {
+              "type": "durability",
+              "amount": 1,
+              "target": "self"
+            }
+          },
+          {
+            "randomize": [
+              {
+                "weight": 85,
+                "shoot": {
+                  "projectile": "entity:fire",
+                  "launch_power": 1
+                }
+              },
+              {
+                "weight": 15,
+                "shoot": {
+                  "projectile": "entity:living_flame",
+                  "launch_power": 1
+                }
+              }
+            ]
+          }
+        ]
+      }
+    }
+  }
 }
```

### `Swords_B/items/glowstone_sword.json`

```diff
--- 1.6/Sword_B/items/glowstone_sword.json
+++ 2.8.14/Swords_B/items/glowstone_sword.json
@@ -1,41 +1,52 @@
 {
-  "format_version": "1.20.20",
+  "format_version": "1.16.100",
   "minecraft:item": {
-	"description": {
-   "identifier": "effect:glowstone_sword",
-			"menu_category": {
-        "category": "equipment"
-      }
-		},
-		"components": {
-            "minecraft:glint": true,
-			"minecraft:max_stack_size": 1,
-			"minecraft:enchantable": {
-				"value": 9,
-				"slot": "sword"
-			},
-
-   "minecraft:durability": {
+    "description": {
+      "identifier": "effect:glowstone_sword",
+      "category": "equipment"
+    },
+    "components": {
+      "minecraft:foil": true,
+      "minecraft:max_stack_size": 1,
+      "minecraft:enchantable": {
+        "value": 9,
+        "slot": "sword"
+      },
+      "minecraft:durability": {
         "max_durability": 128
       },
-			"minecraft:allow_off_hand": true,
-			"minecraft:hand_equipped": true,
-			
-			"minecraft:can_destroy_in_creative": false,
-			"minecraft:icon": {
-				"texture": "glowstone_sword"
-			},
-						 "minecraft:repairable": {
-      "repair_items": [
+      "minecraft:allow_off_hand": true,
+      "minecraft:hand_equipped": true,
+      "minecraft:creative_category": {
+        "parent": "itemGroup.name.sword"
+      },
+      "minecraft:can_destroy_in_creative": false,
+      "minecraft:icon": {
+        "texture": "glowstone_sword"
+      },
+      "minecraft:repairable": {
+        "repair_items": [
           {
-              "items":[
-                  "effect:glowstone_sword"
-              ],
-              "repair_amount": 128
+            "items": [
+              "effect:glowstone_sword"
+            ],
+            "repair_amount": 128
+          },
+          {
+            "items": [
+              "minecraft:glowstone"
+            ],
+            "repair_amount": 64
+          },
+          {
+            "items": [
+              "minecraft:glowstone_dust"
+            ],
+            "repair_amount": 16
           }
-      ]
-  },
-			      "minecraft:digger": {
+        ]
+      },
+      "minecraft:digger": {
         "use_efficiency": true,
         "destroy_speeds": [
           {
@@ -48,10 +59,26 @@
           }
         ]
       },
-      "tag:minecraft:is_sword": {},
-			
-			
-			"minecraft:damage": 6
-		}
-	}
+      "minecraft:display_name": {},
+      "minecraft:damage": 4,
+      "minecraft:weapon": {
+        "on_hurt_entity": {
+          "event": "weapon"
+        }
+      }
+    },
+    "events": {
+      "weapon": {
+        "sequence": [
+          {
+            "damage": {
+              "type": "durability",
+              "amount": 1,
+              "target": "self"
+            }
+          }
+        ]
+      }
+    }
+  }
 }
```

### `Swords_B/items/grass_sword.json`

```diff
--- 1.6/Sword_B/items/grass_sword.json
+++ 2.8.14/Swords_B/items/grass_sword.json
@@ -1,41 +1,40 @@
 {
-  "format_version": "1.20.20",
+  "format_version": "1.16.100",
   "minecraft:item": {
-	"description": {
-   "identifier": "effect:grass_sword",
-			"menu_category": {
-        "category": "equipment"
-      }
-		},
-		"components": {
-            "minecraft:glint": false,
-			"minecraft:max_stack_size": 1,
-			"minecraft:enchantable": {
-				"value": 9,
-				"slot": "sword"
-			},
-
-   "minecraft:durability": {
+    "description": {
+      "identifier": "effect:grass_sword",
+      "category": "equipment"
+    },
+    "components": {
+      "minecraft:foil": false,
+      "minecraft:max_stack_size": 1,
+      "minecraft:enchantable": {
+        "value": 9,
+        "slot": "sword"
+      },
+      "minecraft:durability": {
         "max_durability": 250
       },
-			"minecraft:allow_off_hand": true,
-			"minecraft:hand_equipped": true,
-			
-			"minecraft:can_destroy_in_creative": false,
-			"minecraft:icon": {
-				"texture": "grass_sword"
-			},
-						 "minecraft:repairable": {
-      "repair_items": [
+      "minecraft:allow_off_hand": false,
+      "minecraft:hand_equipped": true,
+      "minecraft:creative_category": {
+        "parent": "itemGroup.name.sword"
+      },
+      "minecraft:can_destroy_in_creative": false,
+      "minecraft:icon": {
+        "texture": "grass_sword"
+      },
+      "minecraft:repairable": {
+        "repair_items": [
           {
-              "items":[
-                  "effect:grass_sword"
-              ],
-              "repair_amount": 250
+            "items": [
+              "effect:grass_sword"
+            ],
+            "repair_amount": 250
           }
-      ]
-  },
-			      "minecraft:digger": {
+        ]
+      },
+      "minecraft:digger": {
         "use_efficiency": true,
         "destroy_speeds": [
           {
@@ -48,10 +47,44 @@
           }
         ]
       },
-      "tag:minecraft:is_sword": {},
-			
-			
-			"minecraft:damage": 8
-		}
-	}
+      "minecraft:render_offsets": {
+        "main_hand": {
+          "first_person": {
+            "position": [ 
+              0.8, //x
+              0.15, //y = First person.
+              -1.74 //z
+            ]
+          },
+          "third_person": {
+            "position": [ 
+              0.69, //x
+              2.5, //z = Mirando la entidad desde al frente.
+              -0.96 //y
+            ]
+          }
+        }
+      },
+      "minecraft:display_name": {},
+      "minecraft:damage": 8,
+      "minecraft:weapon": {
+        "on_hurt_entity": {
+          "event": "weapon"
+        }
+      }
+    },
+    "events": {
+      "weapon": {
+        "sequence": [
+          {
+            "damage": {
+              "type": "durability",
+              "amount": 1,
+              "target": "self"
+            }
+          }
+        ]
+      }
+    }
+  }
 }
```

### `Swords_B/items/ice_sword.json`

```diff
--- 1.6/Sword_B/items/ice_sword.json
+++ 2.8.14/Swords_B/items/ice_sword.json
@@ -1,40 +1,50 @@
 {
-  "format_version": "1.20.20",
+  "format_version": "1.16.100",
   "minecraft:item": {
-	"description": {
-   "identifier": "effect:ice_sword",
-			"menu_category": {
-        "category": "equipment"
-      }
-		},
-		"components": {
-			"minecraft:max_stack_size": 1,
-			"minecraft:enchantable": {
-				"value": 9,
-				"slot": "sword"
-			},
-
-   "minecraft:durability": {
+    "description": {
+      "identifier": "effect:ice_sword",
+      "category": "equipment"
+    },
+    "components": {
+      "minecraft:foil": true,
+      "minecraft:max_stack_size": 1,
+      "minecraft:enchantable": {
+        "value": 9,
+        "slot": "sword"
+      },
+      "minecraft:durability": {
         "max_durability": 500
       },
-			"minecraft:allow_off_hand": true,
-			"minecraft:hand_equipped": true,
-			
-			"minecraft:can_destroy_in_creative": false,
-			"minecraft:icon": {
-				"texture": "ice_sword"
-			},
-						 "minecraft:repairable": {
-      "repair_items": [
+      "minecraft:cooldown": {
+        "category": "ice_sword",
+        "duration": 5
+      },
+      "minecraft:allow_off_hand": false,
+      "minecraft:hand_equipped": true,
+      "minecraft:creative_category": {
+        "parent": "itemGroup.name.sword"
+      },
+      "minecraft:can_destroy_in_creative": false,
+      "minecraft:icon": {
+        "texture": "ice_sword"
+      },
+      "minecraft:repairable": {
+        "repair_items": [
           {
-              "items":[
-                  "effect:ice_sword"
-              ],
-              "repair_amount": 500
+            "items": [
+              "effect:ice_sword"
+            ],
+            "repair_amount": 500
+          },
+          {
+            "items": [
+              "minecraft:ice"
+            ],
+            "repair_amount": 55
           }
-      ]
-  },
-			      "minecraft:digger": {
+        ]
+      },
+      "minecraft:digger": {
         "use_efficiency": true,
         "destroy_speeds": [
           {
@@ -47,10 +57,117 @@
           }
         ]
       },
-      "tag:minecraft:is_sword": {},
-			
-			
-			"minecraft:damage": 11
-		}
-	}
+      "minecraft:display_name": {},
+      "minecraft:damage": 8.5,
+      "minecraft:on_use": {
+        "on_use": {
+          "event": "on_use"
+        }
+      },
+      "minecraft:weapon": {
+        "on_hurt_entity": {
+          "event": "weapon"
+        },
+        "on_not_hurt_entity": {
+          "event": "weapon"
+        },
+        "on_hit_block": {
+          "event": "weapon"
+        }
+      }
+    },
+    "events": {
+      "on_use": {
+        "sequence": [
+          {
+            "run_command": {
+              "command": [
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
+                "title @s actionbar §l§bIce Skill",
+                "playsound random.fizz @a[r=12] ~ ~ ~ 1 2.3",
+                "particle minecraft:knockback_roar_particle ~ ~1 ~"
+              ],
+              "target": "holder"
+            }
+          },
+          {
+            "damage": {
+              "type": "durability",
+              "amount": 6,
+              "target": "self"
+            }
+          }
+        ]
+      },
+      "weapon": {
+        "sequence": [
+          {
+            "damage": {
+              "type": "durability",
+              "amount": 1,
+              "target": "self"
+            }
+          },
+          {
+            "randomize": [
+              {
+                "weight": 70
+              },
+              {
+                "weight": 30,
+                "shoot": {
+                  "projectile": "minecraft:snowball",
+                  "launch_power": 1
+                },
+                "run_command": {
+                  "command": [
+                    "playsound random.bow @a[r=10] ~ ~ ~ 1 0.4"
+                  ]
+                }
+              }
+            ]
+          }
+        ]
+      }
+    }
+  }
 }
```

### `Swords_B/items/jungle_sword.json`

```diff
--- 1.6/Sword_B/items/jungle_sword.json
+++ 2.8.14/Swords_B/items/jungle_sword.json
@@ -1,41 +1,44 @@
 {
-  "format_version": "1.20.20",
+  "format_version": "1.16.100",
   "minecraft:item": {
-	"description": {
-   "identifier": "effect:jungle_sword",
-			"menu_category": {
-        "category": "equipment"
-      }    
-		},
-		"components": {
-            "minecraft:glint": false,
-			"minecraft:max_stack_size": 1,
-			"minecraft:enchantable": {
-				"value": 9,
-				"slot": "sword"
-			},
-
-   "minecraft:durability": {
+    "description": {
+      "identifier": "effect:jungle_sword",
+      "category": "equipment"
+    },
+    "components": {
+      "minecraft:foil": false,
+      "minecraft:max_stack_size": 1,
+      "minecraft:enchantable": {
+        "value": 9,
+        "slot": "sword"
+      },
+      "minecraft:durability": {
         "max_durability": 128
       },
-			"minecraft:allow_off_hand": true,
-			"minecraft:hand_equipped": true,
-			
-			"minecraft:can_destroy_in_creative": false,
-			"minecraft:icon": {
-				"texture": "jungle_sword"
-			},
-						 "minecraft:repairable": {
-      "repair_items": [
+      "minecraft:allow_off_hand": false,
+      "minecraft:hand_equipped": true,
+      "minecraft:creative_category": {
+        "parent": "itemGroup.name.sword"
+      },
+      "minecraft:block_placer": {
+        "block": "effect99:sapling3",
+        "use_on": [ "dirt", "grass" ]
+      },
+      "minecraft:can_destroy_in_creative": false,
+      "minecraft:icon": {
+        "texture": "jungle_sword"
+      },
+      "minecraft:repairable": {
+        "repair_items": [
           {
-              "items":[
-                  "effect:jungle_sword"
-              ],
-              "repair_amount": 128
+            "items": [
+              "effect:jungle_sword"
+            ],
+            "repair_amount": 128
           }
-      ]
-  },
-			      "minecraft:digger": {
+        ]
+      },
+      "minecraft:digger": {
         "use_efficiency": true,
         "destroy_speeds": [
           {
@@ -48,10 +51,26 @@
           }
         ]
       },
-      "tag:minecraft:is_sword": {},
-			
-			
-			"minecraft:damage": 4
-		}
-	}
+      "minecraft:display_name": {},
+      "minecraft:damage": 4,
+      "minecraft:weapon": {
+        "on_hurt_entity": {
+          "event": "weapon"
+        }
+      }
+    },
+    "events": {
+      "weapon": {
+        "sequence": [
+          {
+            "damage": {
+              "type": "durability",
+              "amount": 1,
+              "target": "self"
+            }
+          }
+        ]
+      }
+    }
+  }
 }
```

### `Swords_B/items/lapis_sword.json`

```diff
--- 1.6/Sword_B/items/lapis_sword.json
+++ 2.8.14/Swords_B/items/lapis_sword.json
@@ -1,41 +1,46 @@
 {
-  "format_version": "1.20.20",
+  "format_version": "1.16.100",
   "minecraft:item": {
-	"description": {
-   "identifier": "effect:lapis_sword",
-			"menu_category": {
-        "category": "equipment"
-      }
-		},
-		"components": {
-            "minecraft:glint": false,
-			"minecraft:max_stack_size": 1,
-			"minecraft:enchantable": {
-				"value": 9,
-				"slot": "sword"
-			},
-
-   "minecraft:durability": {
+    "description": {
+      "identifier": "effect:lapis_sword",
+      "category": "equipment"
+    },
+    "components": {
+      "minecraft:foil": false,
+      "minecraft:max_stack_size": 1,
+      "minecraft:enchantable": {
+        "value": 9,
+        "slot": "sword"
+      },
+      "minecraft:durability": {
         "max_durability": 528
       },
-			"minecraft:allow_off_hand": true,
-			"minecraft:hand_equipped": true,
-			
-			"minecraft:can_destroy_in_creative": false,
-			"minecraft:icon": {
-				"texture": "lapis_sword"
-			},
-						 "minecraft:repairable": {
-      "repair_items": [
+      "minecraft:allow_off_hand": false,
+      "minecraft:hand_equipped": true,
+      "minecraft:creative_category": {
+        "parent": "itemGroup.name.sword"
+      },
+      "minecraft:can_destroy_in_creative": false,
+      "minecraft:icon": {
+        "texture": "lapis_sword"
+      },
+      "minecraft:repairable": {
+        "repair_items": [
           {
-              "items":[
-                  "effect:lapis_sword"
-              ],
-              "repair_amount": 528
+            "items": [
+              "effect:lapis_sword"
+            ],
+            "repair_amount": 528
+          },
+          {
+            "items": [
+              "minecraft:lapis_lazuli"
+            ],
+            "repair_amount": 48
           }
-      ]
-  },
-			      "minecraft:digger": {
+        ]
+      },
+      "minecraft:digger": {
         "use_efficiency": true,
         "destroy_speeds": [
           {
@@ -48,10 +53,26 @@
           }
         ]
       },
-      "tag:minecraft:is_sword": {},
-			
-			
-			"minecraft:damage": 6
-		}
-	}
+      "minecraft:display_name": {},
+      "minecraft:damage": 5,
+      "minecraft:weapon": {
+        "on_hurt_entity": {
+          "event": "weapon"
+        }
+      }
+    },
+    "events": {
+      "weapon": {
+        "sequence": [
+          {
+            "damage": {
+              "type": "durability",
+              "amount": 1,
+              "target": "self"
+            }
+          }
+        ]
+      }
+    }
+  }
 }
```

### `Swords_B/items/lightning_sword.json`

```diff
--- 1.6/Sword_B/items/lightning_sword.json
+++ 2.8.14/Swords_B/items/lightning_sword.json
@@ -1,41 +1,40 @@
 {
-  "format_version": "1.20.20",
+  "format_version": "1.16.100",
   "minecraft:item": {
-	"description": {
-   "identifier": "effect:lightning_sword",
-			"menu_category": {
-        "category": "equipment"
-      }
-		},
-		"components": {
-            "minecraft:glint": true,
-			"minecraft:max_stack_size": 1,
-			"minecraft:enchantable": {
-				"value": 9,
-				"slot": "sword"
-			},
-
-   "minecraft:durability": {
-        "max_durability": 2000
+    "description": {
+      "identifier": "effect:lightning_sword",
+      "category": "equipment"
+    },
+    "components": {
+      "minecraft:foil": true,
+      "minecraft:max_stack_size": 1,
+      "minecraft:enchantable": {
+        "value": 9,
+        "slot": "sword"
       },
-			"minecraft:allow_off_hand": true,
-			"minecraft:hand_equipped": true,
-			
-			"minecraft:can_destroy_in_creative": false,
-			"minecraft:icon": {
-				"texture": "lightning_sword"
-			},
-						 "minecraft:repairable": {
-      "repair_items": [
+      "minecraft:durability": {
+        "max_durability": 2012
+      },
+      "minecraft:allow_off_hand": false,
+      "minecraft:hand_equipped": true,
+      "minecraft:creative_category": {
+        "parent": "itemGroup.name.sword"
+      },
+      "minecraft:can_destroy_in_creative": false,
+      "minecraft:icon": {
+        "texture": "lightning_sword"
+      },
+      "minecraft:repairable": {
+        "repair_items": [
           {
-              "items":[
-                  "effect:lightning_sword"
-              ],
-              "repair_amount": 2000
+            "items": [
+              "effect:lightning_sword"
+            ],
+            "repair_amount": 2012
           }
-      ]
-  },
-			      "minecraft:digger": {
+        ]
+      },
+      "minecraft:digger": {
         "use_efficiency": true,
         "destroy_speeds": [
           {
@@ -48,10 +47,136 @@
           }
         ]
       },
-      "tag:minecraft:is_sword": {},
-			
-			
-			"minecraft:damage": 8
-		}
-	}
+      "minecraft:render_offsets": {
+        "main_hand": {
+          "first_person": {
+            "position": [ 
+              1, //x
+              0.4, //y = First person.
+              -3 //z
+            ],
+            "scale": [
+              0.04,
+              0.04,
+              0.04
+            ]
+          },
+          "third_person": {
+            "position": [ 
+              0.7, //x
+              2.2, //z = Mirando la entidad desde al frente.
+              -1   //y
+            ],
+            "scale": [
+              0.05,
+              0.05,
+              0.05
+            ]
+          }
+        }
+      },
+      "minecraft:display_name": {},
+      "minecraft:damage": 8,
+      "minecraft:cooldown": {
+        "category": "lightning_sword",
+        "duration": 12
+      },
+      "minecraft:on_use": {
+        "on_use": {
+          "event": "on_use"
+        }
+      },
+      "minecraft:weapon": {
+        "on_hurt_entity": {
+          "event": "weapon"
+        },
+        "on_not_hurt_entity": {
+          "event": "weapon"
+        },
+        "on_hit_block": {
+          "event": "weapon"
+        }
+      }
+    },
+    "events": {
+      "on_use": {
+        "run_command": {
+          "command": [
+            "summon lightning_bolt ~ ~2 ~ default_lightning_bolt",
+            "summon lightning_bolt ~7 ~ ~ default_lightning_bolt",
+            "summon lightning_bolt ~ ~ ~7 default_lightning_bolt",
+            "summon lightning_bolt ~-7 ~ ~ default_lightning_bolt",
+            "summon lightning_bolt ~ ~ ~-7 default_lightning_bolt",
+            "summon lightning_bolt ~6 ~ ~6 default_lightning_bolt",
+            "summon lightning_bolt ~-6 ~ ~-6 default_lightning_bolt",
+            "summon lightning_bolt ~-6 ~ ~6 default_lightning_bolt",
+            "summon lightning_bolt ~6 ~ ~-6 default_lightning_bolt",
+            "summon lightning_bolt ~14 ~ ~ default_lightning_bolt",
+            "summon lightning_bolt ~ ~ ~14 default_lightning_bolt",
+            "summon lightning_bolt ~-14 ~ ~ default_lightning_bolt",
+            "summon lightning_bolt ~ ~ ~-14 default_lightning_bolt",
+            "summon lightning_bolt ~12 ~ ~12 default_lightning_bolt",
+            "summon lightning_bolt ~-12 ~ ~-12 default_lightning_bolt",
+            "summon lightning_bolt ~-12 ~ ~12 default_lightning_bolt",
+            "summon lightning_bolt ~12 ~ ~-12 default_lightning_bolt",
+            "summon lightning_bolt ~28 ~ ~ default_lightning_bolt",
+            "summon lightning_bolt ~ ~ ~28 default_lightning_bolt",
+            "summon lightning_bolt ~-28 ~ ~ default_lightning_bolt",
+            "summon lightning_bolt ~ ~ ~-28 default_lightning_bolt",
+            "summon lightning_bolt ~24 ~ ~24 default_lightning_bolt",
+            "summon lightning_bolt ~-24 ~ ~-24 default_lightning_bolt",
+            "summon lightning_bolt ~-24 ~ ~24 default_lightning_bolt",
+            "summon lightning_bolt ~24 ~ ~-24 default_lightning_bolt",
+            "summon lightning_bolt ~34 ~ ~ default_lightning_bolt",
+            "summon lightning_bolt ~ ~ ~34 default_lightning_bolt",
+            "summon lightning_bolt ~-34 ~ ~ default_lightning_bolt",
+            "summon lightning_bolt ~ ~ ~-34 default_lightning_bolt",
+            "summon lightning_bolt ~30 ~ ~30 default_lightning_bolt",
+            "summon lightning_bolt ~-30 ~ ~-30 default_lightning_bolt",
+            "summon lightning_bolt ~-30 ~ ~30 default_lightning_bolt",
+            "summon lightning_bolt ~30 ~ ~-30 default_lightning_bolt",
+            "summon lightning_bolt ~42 ~ ~ default_lightning_bolt",
+            "summon lightning_bolt ~ ~ ~42 default_lightning_bolt",
+            "summon lightning_bolt ~-42 ~ ~ default_lightning_bolt",
+            "summon lightning_bolt ~ ~ ~-42 default_lightning_bolt",
+            "summon lightning_bolt ~38 ~ ~38 default_lightning_bolt",
+            "summon lightning_bolt ~-38 ~ ~-38 default_lightning_bolt",
+            "summon lightning_bolt ~-38 ~ ~38 default_lightning_bolt",
+            "summon lightning_bolt ~38 ~ ~-38 default_lightning_bolt"
+
+          ]
+        },
+        "damage": {
+          "type": "durability",
+          "amount": 9,
+          "target": "self"
+        }
+      },
+      "weapon": {
+        "sequence": [
+          {
+            "damage": {
+              "type": "durability",
+              "amount": 1,
+              "target": "self"
+            }
+          },
+          {
+            "randomize": [
+              {
+                "weight": 15
+              },
+              {
+                "weight": 85,
+                "shoot": {
+                  "projectile": "entity:lightning_projectile",
+                  "launch_power": 1
+                }
+              }
+            ]
+          }
+        ]
+      }
+    }
+  }
 }
```

### `Swords_B/items/magma_sword.json`

```diff
--- 1.6/Sword_B/items/magma_sword.json
+++ 2.8.14/Swords_B/items/magma_sword.json
@@ -1,41 +1,46 @@
 {
-  "format_version": "1.20.20",
+  "format_version": "1.16.100",
   "minecraft:item": {
-	"description": {
-   "identifier": "effect:magma_sword",
-			"menu_category": {
-        "category": "equipment"
-      }
-		},
-		"components": {
-            "minecraft:glint": false,
-			"minecraft:max_stack_size": 1,
-			"minecraft:enchantable": {
-				"value": 9,
-				"slot": "sword"
-			},
-
-   "minecraft:durability": {
-        "max_durability": 1000
+    "description": {
+      "identifier": "effect:magma_sword",
+      "category": "equipment"
+    },
+    "components": {
+      "minecraft:foil": false,
+      "minecraft:max_stack_size": 1,
+      "minecraft:enchantable": {
+        "value": 9,
+        "slot": "sword"
       },
-			"minecraft:allow_off_hand": true,
-			"minecraft:hand_equipped": true,
-			
-			"minecraft:can_destroy_in_creative": false,
-			"minecraft:icon": {
-				"texture": "magma_sword"
-			},
-						 "minecraft:repairable": {
-      "repair_items": [
+      "minecraft:durability": {
+        "max_durability": 1316
+      },
+      "minecraft:allow_off_hand": false,
+      "minecraft:hand_equipped": true,
+      "minecraft:creative_category": {
+        "parent": "itemGroup.name.sword"
+      },
+      "minecraft:can_destroy_in_creative": false,
+      "minecraft:icon": {
+        "texture": "magma_sword"
+      },
+      "minecraft:repairable": {
+        "repair_items": [
           {
-              "items":[
-                  "effect:magma_sword"
-              ],
-              "repair_amount": 1000
+            "items": [
+              "effect:magma_sword"
+            ],
+            "repair_amount": 1316
+          },
+          {
+            "items": [
+              "minecraft:magma"
+            ],
+            "repair_amount": 100
           }
-      ]
-  },
-			      "minecraft:digger": {
+        ]
+      },
+      "minecraft:digger": {
         "use_efficiency": true,
         "destroy_speeds": [
           {
@@ -48,10 +53,26 @@
           }
         ]
       },
-      "tag:minecraft:is_sword": {},
-			
-			
-			"minecraft:damage": 7
-		}
-	}
+      "minecraft:display_name": {},
+      "minecraft:damage": 7.2,
+      "minecraft:weapon": {
+        "on_hurt_entity": {
+          "event": "weapon"
+        }
+      }
+    },
+    "events": {
+      "weapon": {
+        "sequence": [
+          {
+            "damage": {
+              "type": "durability",
+              "amount": 1,
+              "target": "self"
+            }
+          }
+        ]
+      }
+    }
+  }
 }
```

### `Swords_B/items/obsidian_sword.json`

```diff
--- 1.6/Sword_B/items/obsidian_sword.json
+++ 2.8.14/Swords_B/items/obsidian_sword.json
@@ -1,41 +1,47 @@
 {
-  "format_version": "1.20.20",
+  "format_version": "1.16.100",
   "minecraft:item": {
-	"description": {
-   "identifier": "effect:obsidian_sword",
-			"menu_category": {
-        "category": "equipment"
-      }
-		},
-		"components": {
-            "minecraft:glint": false,
-			"minecraft:max_stack_size": 1,
-			"minecraft:enchantable": {
-				"value": 9,
-				"slot": "sword"
-			},
-
-   "minecraft:durability": {
+    "description": {
+      "identifier": "effect:obsidian_sword",
+      "category": "equipment"
+    },
+    "components": {
+      
+      "minecraft:foil": false,
+      "minecraft:max_stack_size": 1,
+      "minecraft:enchantable": {
+        "value": 9,
+        "slot": "sword"
+      },
+      "minecraft:durability": {
         "max_durability": 3000
       },
-			"minecraft:allow_off_hand": true,
-			"minecraft:hand_equipped": true,
-			
-			"minecraft:can_destroy_in_creative": false,
-			"minecraft:icon": {
-				"texture": "obsidian_sword"
-			},
-						 "minecraft:repairable": {
-      "repair_items": [
+      "minecraft:allow_off_hand": false,
+      "minecraft:hand_equipped": true,
+      "minecraft:creative_category": {
+        "parent": "itemGroup.name.sword"
+      },
+      "minecraft:can_destroy_in_creative": false,
+      "minecraft:icon": {
+        "texture": "obsidian_sword"
+      },
+      "minecraft:repairable": {
+        "repair_items": [
           {
-              "items":[
-                  "effect:obsidian_sword"
-              ],
-              "repair_amount": 3000
+            "items": [
+              "effect:obsidian_sword"
+            ],
+            "repair_amount": 3000
+          },
+          {
+            "items": [
+              "minecraft:obsidian"
+            ],
+            "repair_amount": 120
           }
-      ]
-  },
-			      "minecraft:digger": {
+        ]
+      },
+      "minecraft:digger": {
         "use_efficiency": true,
         "destroy_speeds": [
           {
@@ -48,10 +54,43 @@
           }
         ]
       },
-      "tag:minecraft:is_sword": {},
-			
-			
-			"minecraft:damage": 12
-		}
-	}
+      "minecraft:display_name": {},
+      "minecraft:damage": 8,
+      "minecraft:weapon": {
+        "on_hurt_entity": {
+          "event": "weapon"
+        }
+      }
+    },
+    "events": {
+      "weapon": {
+        "randomize": [
+          {
+            "weight": 55,
+            "damage": {
+              "type": "durability",
+              "amount": 1,
+              "target": "self"
+            }
+          },
+          {
+            "weight": 30,
+            "damage": {
+              "type": "durability",
+              "amount": 2,
+              "target": "self"
+            }
+          },
+          {
+            "weight": 15,
+            "damage": {
+              "type": "durability",
+              "amount": 3,
+              "target": "self"
+            }
+          }
+        ]
+      }
+    }
+  }
 }
```

### `Swords_B/items/quartz_sword.json`

```diff
--- 1.6/Sword_B/items/quartz_sword.json
+++ 2.8.14/Swords_B/items/quartz_sword.json
@@ -1,36 +1,26 @@
 {
-  "format_version": "1.20.20",
+  "format_version": "1.16.100",
   "minecraft:item": {
     "description": {
       "identifier": "effect:quartz_sword",
-			"menu_category": {
-        "category": "equipment"
-      }
-		},
-		"components": {
-            "minecraft:glint": true,
-			"minecraft:max_stack_size": 1,
-            "minecraft:durability": {
-            "max_durability": 1
-            },
-			"minecraft:allow_off_hand": true,
-			"minecraft:hand_equipped": true,
-			
-			"minecraft:can_destroy_in_creative": false,
-			"minecraft:icon": {
-				"texture": "quartz_sword"
-			},
-						 "minecraft:repairable": {
-      "repair_items": [
-          {
-              "items":[
-                  "effect:quartz_sword"
-              ],
-              "repair_amount": 1
-          }
-      ]
-  },
-			      "minecraft:digger": {
+      "category": "equipment"
+    },
+    "components": {
+      "minecraft:foil": true,
+      "minecraft:max_stack_size": 1,
+      "minecraft:durability": {
+        "max_durability": 1
+      },
+      "minecraft:allow_off_hand": false,
+      "minecraft:hand_equipped": true,
+      "minecraft:creative_category": {
+        "parent": "itemGroup.name.sword"
+      },
+      "minecraft:can_destroy_in_creative": false,
+      "minecraft:icon": {
+        "texture": "quartz_sword"
+      },
+      "minecraft:digger": {
         "use_efficiency": true,
         "destroy_speeds": [
           {
@@ -43,10 +33,68 @@
           }
         ]
       },
-      "tag:minecraft:is_sword": {},
-			
-			
-			"minecraft:damage": 600
-		}
-	}
+      "minecraft:render_offsets": {
+        "main_hand": {
+          "first_person": {
+            "position": [ 
+              1.0, //x
+              0, //y = First person.
+              -2 //z
+            ],
+            "scale": [
+              0.07,
+              0.07,
+              0.07
+            ]
+          },
+          "third_person": {
+            "position": [ 
+              0.2, //x
+              1.1, //z = Mirando la entidad desde al frente.
+              -0.5 //y
+            ],
+            "scale": [
+              0.08,
+              0.08,
+              0.08
+            ]
+          }
+        }
+      },
+      "minecraft:display_name": {},
+      "minecraft:damage": 600,
+      "minecraft:weapon": {
+        "on_hurt_entity": {
+          "event": "weapon"
+        },
+        "on_not_hurt_entity": {
+          "event": "weapon"
+        },
+        "on_hit_block": {
+          "event": "weapon"
+        }
+      }
+    },
+    "events": {
+      "weapon": {
+        "sequence": [
+          {
+            "damage": {
+              "type": "durability",
+              "amount": 10,
+              "target": "self"
+            }
+          },
+          {
+            "run_command": {
+              "command": [ 
+                "effect @a[r=1] instant_damage 1 99 true",
+                "particle minecraft:knockback_roar_particle ~ ~1 ~"
+              ]
+            }
+          }
+        ]
+      }
+    }
+  }
 }
```

### `Swords_B/items/sea_sword.json`

```diff
--- 1.6/Sword_B/items/sea_sword.json
+++ 2.8.14/Swords_B/items/sea_sword.json
@@ -1,41 +1,46 @@
 {
-  "format_version": "1.20.20",
+  "format_version": "1.16.100",
   "minecraft:item": {
-	"description": {
-   "identifier": "effect:sea_sword",
-			"menu_category": {
-        "category": "equipment"
-      }
-		},
-		"components": {
-            "minecraft:glint": true,
-			"minecraft:max_stack_size": 1,
-			"minecraft:enchantable": {
-				"value": 9,
-				"slot": "sword"
-			},
-
-   "minecraft:durability": {
-        "max_durability": 1000
+    "description": {
+      "identifier": "effect:sea_sword",
+      "category": "equipment"
+    },
+    "components": {
+      "minecraft:foil": true,
+      "minecraft:max_stack_size": 1,
+      "minecraft:enchantable": {
+        "value": 9,
+        "slot": "sword"
       },
-			"minecraft:allow_off_hand": true,
-			"minecraft:hand_equipped": true,
-			
-			"minecraft:can_destroy_in_creative": false,
-			"minecraft:icon": {
-				"texture": "sea_sword"
-			},
-						 "minecraft:repairable": {
-      "repair_items": [
+      "minecraft:durability": {
+        "max_durability": 1356
+      },
+      "minecraft:allow_off_hand": false,
+      "minecraft:hand_equipped": true,
+      "minecraft:creative_category": {
+        "parent": "itemGroup.name.sword"
+      },
+      "minecraft:can_destroy_in_creative": false,
+      "minecraft:icon": {
+        "texture": "sea_sword"
+      },
+      "minecraft:repairable": {
+        "repair_items": [
           {
-              "items":[
-                  "effect:sea_sword"
-              ],
-              "repair_amount": 1000
+            "items": [
+              "effect:sea_sword"
+            ],
+            "repair_amount": 1356
+          },
+          {
+            "items": [
+              "minecraft:heart_of_the_sea"
+            ],
+            "repair_amount": 482
           }
-      ]
-  },
-			      "minecraft:digger": {
+        ]
+      },
+      "minecraft:digger": {
         "use_efficiency": true,
         "destroy_speeds": [
           {
@@ -48,10 +53,26 @@
           }
         ]
       },
-      "tag:minecraft:is_sword": {},
-			
-			
-			"minecraft:damage": 7
-		}
-	}
+      "minecraft:display_name": {},
+      "minecraft:damage": 7,
+      "minecraft:weapon": {
+        "on_hurt_entity": {
+          "event": "weapon"
+        }
+      }
+    },
+    "events": {
+      "weapon": {
+        "sequence": [
+          {
+            "damage": {
+              "type": "durability",
+              "amount": 1,
+              "target": "self"
+            }
+          }
+        ]
+      }
+    }
+  }
 }
```

### `Swords_B/items/shulker_sword.json`

```diff
--- 1.6/Sword_B/items/shulker_sword.json
+++ 2.8.14/Swords_B/items/shulker_sword.json
@@ -1,41 +1,44 @@
 {
-  "format_version": "1.20.20",
+  "format_version": "1.16.100",
   "minecraft:item": {
-	"description": {
-   "identifier": "effect:shulker_sword",
-			"menu_category": {
-        "category": "equipment"
-      }
-		},
-		"components": {
-            "minecraft:glint": false,
-			"minecraft:max_stack_size": 1,
-			"minecraft:enchantable": {
-				"value": 9,
-				"slot": "sword"
-			},
-
-   "minecraft:durability": {
-        "max_durability": 1000
+    "description": {
+      "identifier": "effect:shulker_sword",
+      "category": "equipment"
+    },
+    "components": {
+      "minecraft:foil": false,
+      "minecraft:max_stack_size": 1,
+      "minecraft:enchantable": {
+        "value": 9,
+        "slot": "sword"
       },
-			"minecraft:allow_off_hand": true,
-			"minecraft:hand_equipped": true,
-			
-			"minecraft:can_destroy_in_creative": false,
-			"minecraft:icon": {
-				"texture": "shulker_sword"
-			},
-						 "minecraft:repairable": {
-      "repair_items": [
+      "minecraft:cooldown": {
+        "category": "shulker_sword",
+        "duration": 8
+      },
+      "minecraft:durability": {
+        "max_durability": 2609
+      },
+      "minecraft:allow_off_hand": false,
+      "minecraft:hand_equipped": true,
+      "minecraft:creative_category": {
+        "parent": "itemGroup.name.sword"
+      },
+      "minecraft:can_destroy_in_creative": false,
+      "minecraft:icon": {
+        "texture": "shulker_sword"
+      },
+      "minecraft:repairable": {
+        "repair_items": [
           {
-              "items":[
-                  "effect:shulker_sword"
-              ],
-              "repair_amount": 1000
+            "items": [
+              "effect:shulker_sword"
+            ],
+            "repair_amount": 2609
           }
-      ]
-  },
-			      "minecraft:digger": {
+        ]
+      },
+      "minecraft:digger": {
         "use_efficiency": true,
         "destroy_speeds": [
           {
@@ -48,10 +51,76 @@
           }
         ]
       },
-      "tag:minecraft:is_sword": {},
-			
-			
-			"minecraft:damage": 7
-		}
-	}
+      "minecraft:display_name": {},
+      "minecraft:damage": 6,
+      "minecraft:on_use": {
+        "on_use": {
+          "event": "on_use"
+        }
+      },
+      "minecraft:weapon": {
+        "on_hurt_entity": {
+          "event": "weapon"
+        },
+        "on_not_hurt_entity": {
+          "event": "weapon"
+        },
+        "on_hit_block": {
+          "event": "weapon"
+        }
+      }
+    },
+    "events": {
+      "on_use": {
+        "run_command": {
+          "command": [
+            "particle minecraft:cauldron_explosion_emitter ~3 ~ ~",
+            "particle minecraft:cauldron_explosion_emitter ~ ~ ~3",
+            "particle minecraft:cauldron_explosion_emitter ~-3 ~ ~",
+            "particle minecraft:cauldron_explosion_emitter ~ ~ ~-3",
+            "particle minecraft:cauldron_explosion_emitter ~-2.5 ~ ~2.5",
+            "particle minecraft:cauldron_explosion_emitter ~2.5 ~ ~-2.5",
+            "particle minecraft:cauldron_explosion_emitter ~2.5 ~ ~2.5",
+            "particle minecraft:cauldron_explosion_emitter ~-2.5 ~ ~-2.5",
+            "effect @e[r=6,family=!shulker_sword] levitation 1 18 false"
+          ]
+        },
+        "damage": {
+          "type": "durability",
+          "amount": 8,
+          "target": "self"
+        }
+      },
+      "weapon": {
+        "sequence": [
+          {
+            "damage": {
+              "type": "durability",
+              "amount": 1,
+              "target": "self"
+            }
+          },
+          {
+            "randomize": [
+              {
+                "weight": 10,
+                "shoot": {
+                  "projectile": "minecraft:shulker_bullet",
+                  "launch_power": 1
+                },
+                "run_command": {
+                  "command": [
+                    "playsound random.bow @a[r=10] ~ ~ ~ 1 0.4"
+                  ]
+                }
+              },
+              {
+                "weight": 90
+              }
+            ]
+          }
+        ]
+      }
+    }
+  }
 }
```

### `Swords_B/items/slime_sword.json`

```diff
--- 1.6/Sword_B/items/slime_sword.json
+++ 2.8.14/Swords_B/items/slime_sword.json
@@ -1,41 +1,46 @@
 {
-  "format_version": "1.20.20",
+  "format_version": "1.16.100",
   "minecraft:item": {
-	"description": {
-   "identifier": "effect:slime_sword",
-			"menu_category": {
-        "category": "equipment"
-      }
-		},
-		"components": {
-            "minecraft:glint": false,
-			"minecraft:max_stack_size": 1,
-			"minecraft:enchantable": {
-				"value": 9,
-				"slot": "sword"
-			},
-
-   "minecraft:durability": {
+    "description": {
+      "identifier": "effect:slime_sword",
+      "category": "equipment"
+    },
+    "components": {
+      "minecraft:foil": false,
+      "minecraft:max_stack_size": 1,
+      "minecraft:enchantable": {
+        "value": 9,
+        "slot": "sword"
+      },
+      "minecraft:durability": {
         "max_durability": 675
       },
-			"minecraft:allow_off_hand": true,
-			"minecraft:hand_equipped": true,
-			
-			"minecraft:can_destroy_in_creative": false,
-			"minecraft:icon": {
-				"texture": "slime_sword"
-			},
-						 "minecraft:repairable": {
-      "repair_items": [
+      "minecraft:allow_off_hand": false,
+      "minecraft:hand_equipped": true,
+      "minecraft:creative_category": {
+        "parent": "itemGroup.name.sword"
+      },
+      "minecraft:can_destroy_in_creative": false,
+      "minecraft:icon": {
+        "texture": "slime_sword"
+      },
+      "minecraft:repairable": {
+        "repair_items": [
           {
-              "items":[
-                  "effect:slime_sword"
-              ],
-              "repair_amount": 675
+            "items": [
+              "effect:slime_sword"
+            ],
+            "repair_amount": 675
+          },
+          {
+            "items": [
+              "minecraft:slime"
+            ],
+            "repair_amount": 48
           }
-      ]
-  },
-			      "minecraft:digger": {
+        ]
+      },
+      "minecraft:digger": {
         "use_efficiency": true,
         "destroy_speeds": [
           {
@@ -48,10 +53,26 @@
           }
         ]
       },
-      "tag:minecraft:is_sword": {},
-			
-			
-			"minecraft:damage": 6
-		}
-	}
+      "minecraft:display_name": {},
+      "minecraft:damage": 6,
+      "minecraft:weapon": {
+        "on_hurt_entity": {
+          "event": "weapon"
+        }
+      }
+    },
+    "events": {
+      "weapon": {
+        "sequence": [
+          {
+            "damage": {
+              "type": "durability",
+              "amount": 1,
+              "target": "self"
+            }
+          }
+        ]
+      }
+    }
+  }
 }
```

### `Swords_B/items/spectral_sword.json`

```diff
--- 1.6/Sword_B/items/spectral_sword.json
+++ 2.8.14/Swords_B/items/spectral_sword.json
@@ -1,41 +1,76 @@
 {
-  "format_version": "1.20.20",
+  "format_version": "1.16.100",
   "minecraft:item": {
-	"description": {
-   "identifier": "effect:spectral_sword",
-			"menu_category": {
-        "category": "equipment"
-      }
-		},
-		"components": {
-            "minecraft:glint": true,
-			"minecraft:max_stack_size": 1,
-			"minecraft:enchantable": {
-				"value": 9,
-				"slot": "sword"
-			},
-
-   "minecraft:durability": {
+    "description": {
+      "identifier": "effect:spectral_sword",
+      "category": "equipment"
+    },
+    "components": {
+      
+      "minecraft:foil": true,
+      "minecraft:should_despawn": false,
+      "minecraft:max_stack_size": 1,
+      "minecraft:enchantable": {
+        "value": 9,
+        "slot": "sword"
+      },
+      "minecraft:cooldown": {
+        "category": "spectral_sword",
+        "duration": 18
+      },
+      "minecraft:durability": {
         "max_durability": 3256
       },
-			"minecraft:allow_off_hand": true,
-			"minecraft:hand_equipped": true,
-			
-			"minecraft:can_destroy_in_creative": false,
-			"minecraft:icon": {
-				"texture": "spectral_sword"
-			},
-						 "minecraft:repairable": {
-      "repair_items": [
+      "minecraft:allow_off_hand": false,
+      "minecraft:hand_equipped": true,
+      "minecraft:creative_category": {
+        "parent": "itemGroup.name.sword"
+      },
+      "minecraft:can_destroy_in_creative": false,
+      "minecraft:icon": {
+        "texture": "spectral_sword"
+      },
+      "minecraft:repairable": {
+        "repair_items": [
           {
-              "items":[
-                  "effect:spectral_sword"
-              ],
-              "repair_amount": 3256
+            "items": [
+              "effect:spectral_sword"
+            ],
+            "repair_amount": 3256
+          },
+          {
+            "items": [
+              "minecraft:end_crystal"
+            ],
+            "repair_amount": 620
+          },
+          {
+            "items": [
+              "minecraft:nether_star"
+            ],
+            "repair_amount": 2052
           }
-      ]
-  },
-			      "minecraft:digger": {
+        ]
+      },
+      "minecraft:render_offsets": {
+        "main_hand": {
+          "first_person": {
+            "position": [ 
+              0.57, //x
+              0.1, //y = First person.
+              -1.24 //z
+            ]
+          },
+          "third_person": {
+            "position": [ 
+              0.41, //x
+              1.7, //z = Mirando la entidad desde al frente.
+              -0.7 //y
+            ]
+          }
+        }
+      },
+      "minecraft:digger": {
         "use_efficiency": true,
         "destroy_speeds": [
           {
@@ -48,10 +83,63 @@
           }
         ]
       },
-      "tag:minecraft:is_sword": {},
-			
-			
-			"minecraft:damage": 9
-		}
-	}
+      "minecraft:display_name": {},
+      "minecraft:damage": 9,
+      "minecraft:on_use": {
+        "on_use": {
+          "event": "on_use"
+        }
+      },
+      "minecraft:weapon": {
+        "on_hurt_entity": {
+          "event": "weapon"
+        },
+        "on_not_hurt_entity": {
+          "event": "weapon"
+        },
+        "on_hit_block": {
+          "event": "weapon"
+        }
+      }
+    },
+    "events": {
+      "on_use": {
+        "damage": {
+          "type": "durability",
+          "amount": 15,
+          "target": "self"
+        },
+        "shoot": {
+          "projectile": "entity:ender_crystal_projectile",
+          "launch_power": 1
+        },
+        "run_command": {
+          "command": [ 
+            "playsound portal.travel @a[r=16] ~ ~ ~ 1 5",
+            "event entity @e[type=ender_crystal,family=!ender_crystal_default,family=!ender_crystal_scale,c=1,r=4] minecraft:ender_crystal_scale"
+          ]
+        }
+      },
+      "weapon": {
+        "randomize": [
+          {
+            "weight": 99,
+            "damage": {
+              "type": "durability",
+              "amount": 1,
+              "target": "self"
+            }
+          },
+          {
+            "weight": 1,
+            "run_command": { 
+              "command": [ 
+                "event entity @e[type=ender_crystal,family=!ender_crystal_default,family=!ender_crystal_scale,c=1] minecraft:crystal_explode"
+              ] 
+            }
+          }
+        ]
+      }
+    }
+  }
 }
```

### `Swords_B/items/spider_sword.json`

```diff
--- 1.6/Sword_B/items/spider_sword.json
+++ 2.8.14/Swords_B/items/spider_sword.json
@@ -1,46 +1,61 @@
 {
-  "format_version": "1.20.20",
+  "format_version": "1.16.100",
   "minecraft:item": {
-	"description": {
-   "identifier": "effect:spider_sword",
-			"menu_category": {
-        "category": "equipment"
-      }
-		},
-		"components": {
-            "minecraft:glint": false,
-			"minecraft:max_stack_size": 1,
-			"minecraft:enchantable": {
-				"value": 9,
-				"slot": "sword"
-			},
-
-   "minecraft:durability": {
+    "description": {
+      "identifier": "effect:spider_sword",
+      "category": "equipment"
+    },
+    "components": {
+      "minecraft:foil": false,
+      "minecraft:max_stack_size": 1,
+      "minecraft:enchantable": {
+        "value": 9,
+        "slot": "sword"
+      },
+      "minecraft:durability": {
         "max_durability": 628
       },
-			"minecraft:allow_off_hand": true,
-			"minecraft:hand_equipped": true,
-			
-			"minecraft:can_destroy_in_creative": false,
-			"minecraft:icon": {
-				"texture": "spider_sword"
-			},
-						 "minecraft:repairable": {
-      "repair_items": [
+      "minecraft:cooldown": {
+        "category": "spider_sword",
+        "duration": 28
+      },
+      "minecraft:allow_off_hand": false,
+      "minecraft:hand_equipped": true,
+      "minecraft:creative_category": {
+        "parent": "itemGroup.name.sword"
+      },
+      "minecraft:can_destroy_in_creative": false,
+      "minecraft:icon": {
+        "texture": "spider_sword"
+      },
+      "minecraft:repairable": {
+        "repair_items": [
           {
-              "items":[
-                  "effect:spider_sword"
-              ],
-              "repair_amount": 628
+            "items": [
+              "effect:spider_sword"
+            ],
+            "repair_amount": 628
+          },
+          {
+            "items": [
+              "minecraft:web"
+            ],
+            "repair_amount": 128
+          },
+          {
+            "items": [
+              "minecraft:spider_eye"
+            ],
+            "repair_amount": 48
           }
-      ]
-  },
-			      "minecraft:digger": {
+        ]
+      },
+      "minecraft:digger": {
         "use_efficiency": true,
         "destroy_speeds": [
           {
             "block": "minecraft:web",
-            "speed": 15
+            "speed": 100
           },
           {
             "block": "minecraft:bamboo",
@@ -48,10 +63,63 @@
           }
         ]
       },
-      "tag:minecraft:is_sword": {},
-			
-			
-			"minecraft:damage": 6
-		}
-	}
+      "minecraft:display_name": {},
+      "minecraft:damage": 5,
+      "minecraft:on_use": {
+        "on_use": {
+          "event": "on_use"
+        }
+      },
+      "minecraft:weapon": {
+        "on_hurt_entity": {
+          "event": "weapon"
+        },
+        "on_not_hurt_entity": {
+          "event": "weapon"
+        },
+        "on_hit_block": {
+          "event": "weapon"
+        }
+      }
+    },
+    "events": {
+      "on_use": {
+        "run_command": {
+          "command": [ "event entity @s spider_sword_skill" 
+          ],
+          "target": "holder"
+        },
+        "damage": {
+          "type": "durability",
+          "amount": 8,
+          "target": "self"
+        }
+      },
+      "weapon": {
+        "sequence": [
+          {
+            "damage": {
+              "type": "durability",
+              "amount": 1,
+              "target": "self"
+            }
+          },
+          {
+            "randomize": [
+              {
+                "weight": 95
+              },
+              {
+                "weight": 5,
+                "shoot": {
+                  "projectile": "entity:web",
+                  "launch_power": 1
+                }
+              }
+            ]
+          }
+        ]
+      }
+    }
+  }
 }
```

### `Swords_B/items/sponge_sword.json`

```diff
--- 1.6/Sword_B/items/sponge_sword.json
+++ 2.8.14/Swords_B/items/sponge_sword.json
@@ -1,41 +1,42 @@
 {
-  "format_version": "1.20.20",
+  "format_version": "1.16.100",
   "minecraft:item": {
-	"description": {
-   "identifier": "effect:sponge_sword",
-			"menu_category": {
-        "category": "equipment"
-      }
-		},
-		"components": {
-            "minecraft:glint": false,
-			"minecraft:max_stack_size": 1,
-			"minecraft:enchantable": {
-				"value": 9,
-				"slot": "sword"
-			},
-
-   "minecraft:durability": {
+    "description": {
+      "identifier": "effect:sponge_sword",
+      "category": "equipment"
+    },
+    "components": {
+      "minecraft:foil": false,
+      "minecraft:max_stack_size": 1,
+      "minecraft:durability": {
         "max_durability": 128
       },
-			"minecraft:allow_off_hand": true,
-			"minecraft:hand_equipped": true,
-			
-			"minecraft:can_destroy_in_creative": false,
-			"minecraft:icon": {
-				"texture": "sponge_sword"
-			},
-						 "minecraft:repairable": {
-      "repair_items": [
+      "minecraft:allow_off_hand": false,
+      "minecraft:hand_equipped": true,
+      "minecraft:creative_category": {
+        "parent": "itemGroup.name.sword"
+      },
+      "minecraft:can_destroy_in_creative": false,
+      "minecraft:icon": {
+        "texture": "sponge_sword"
+      },
+      "minecraft:repairable": {
+        "repair_items": [
           {
-              "items":[
-                  "effect:sponge_sword"
-              ],
-              "repair_amount": 128
+            "items": [
+              "effect:sponge_sword"
+            ],
+            "repair_amount": 128
+          },
+          {
+            "items": [
+              "minecraft:sponge"
+            ],
+            "repair_amount": 62
           }
-      ]
-  },
-			      "minecraft:digger": {
+        ]
+      },
+      "minecraft:digger": {
         "use_efficiency": true,
         "destroy_speeds": [
           {
@@ -48,10 +49,26 @@
           }
         ]
       },
-      "tag:minecraft:is_sword": {},
-			
-			
-			"minecraft:damage": 6
-		}
-	}
+      "minecraft:display_name": {},
+      "minecraft:damage": 5,
+      "minecraft:weapon": {
+        "on_hurt_entity": {
+          "event": "weapon"
+        }
+      }
+    },
+    "events": {
+      "weapon": {
+        "sequence": [
+          {
+            "damage": {
+              "type": "durability",
+              "amount": 1,
+              "target": "self"
+            }
+          }
+        ]
+      }
+    }
+  }
 }
```

### `Swords_B/items/tnt_sword.json`

```diff
--- 1.6/Sword_B/items/tnt_sword.json
+++ 2.8.14/Swords_B/items/tnt_sword.json
@@ -1,52 +1,104 @@
 {
-  "format_version": "1.20.20",
+  "format_version": "1.16.100",
   "minecraft:item": {
-	"description": {
-   "identifier": "effect:tnt_sword",
-			"menu_category": {
-        "category": "equipment"
-      }
-		},
-		"components": {
-            "minecraft:glint": false,
-			"minecraft:max_stack_size": 1,
-            "minecraft:durability": {
-            "max_durability": 1
-            },
-			"minecraft:allow_off_hand": true,
-			"minecraft:hand_equipped": true,
-			
-			"minecraft:can_destroy_in_creative": false,
-			"minecraft:icon": {
-				"texture": "tnt_sword"
-			},
-						 "minecraft:repairable": {
-      "repair_items": [
+    "description": {
+      "identifier": "effect:tnt_sword",
+      "category": "equipment"
+    },
+    "components": {
+      "minecraft:foil": false,
+      "minecraft:max_stack_size": 1,
+      "minecraft:durability": {
+        "max_durability": 64
+      },
+      "minecraft:enchantable": {
+        "value": 9,
+        "slot": "sword"
+      },
+      "minecraft:cooldown": {
+        "category": "tnt_sword",
+        "duration": 10
+      },
+      "minecraft:allow_off_hand": false,
+      "minecraft:hand_equipped": true,
+      "minecraft:creative_category": {
+        "parent": "itemGroup.name.sword"
+      },
+      "minecraft:can_destroy_in_creative": false,
+      "minecraft:icon": {
+        "texture": "tnt_sword"
+      },
+      "minecraft:repairable": {
+        "repair_items": [
           {
-              "items":[
-                  "effect:tnt_sword"
-              ],
-              "repair_amount": 1
-          }
-      ]
-  },
-			      "minecraft:digger": {
-        "use_efficiency": true,
-        "destroy_speeds": [
-          {
-            "block": "minecraft:web",
-            "speed": 15
+            "items": [
+              "effect:tnt_sword"
+            ],
+            "repair_amount": 64
           },
           {
-            "block": "minecraft:bamboo",
-            "speed": 10
+            "items": [
+              "minecraft:tnt"
+            ],
+            "repair_amount": 18
           }
         ]
       },
-      "tag:minecraft:is_sword": {},
-			
-			
-			"minecraft:damage": 7
-		}
-	}
+      "minecraft:display_name": {},
+      "minecraft:damage": 4,
+      "minecraft:on_use": {
+        "on_use": {
+          "event": "on_use"
+        }
+      },
+      "minecraft:weapon": {
+        "on_hurt_entity": {
+          "event": "weapon"
+        },
+        "on_not_hurt_entity": {
+          "event": "weapon"
+        },
+        "on_hit_block": {
+          "event": "weapon"
+        }
+      }
+    },
+    "events": {
+      "on_use": {
+        "run_command": {
+          "command": [ "summon minecraft:tnt ~~~ giant_tnt", "title @a[r=18] actionbar §fSuper§4TNT §f§lhas been activated.", "playsound random.fuse @a ~~~" ]
+        },
+        "damage": {
+          "type": "durability",
+          "amount": 18,
+          "target": "self"
+        }
+      },
+      "weapon": {
+        "sequence": [
+          {
+            "damage": {
+              "type": "durability",
+              "amount": 1,
+              "target": "self"
+            }
+          },
+          {
+            "randomize": [
+              {
+               "weight": 10
+              },
+              {
+                "weight": 90,
+                "shoot": {
+                  "projectile": "entity:tnt",
+                  "launch_power": 1
+                }
+              }
+            ]
+          }
+        ]
+      }
+    }
+  }
 }
```

### `Swords_B/items/wither_sword.json`

```diff
--- 1.6/Sword_B/items/wither_sword.json
+++ 2.8.14/Swords_B/items/wither_sword.json
@@ -1,41 +1,38 @@
 {
-  "format_version": "1.20.20",
+  "format_version": "1.16.100",
   "minecraft:item": {
-	"description": {
-   "identifier": "effect:wither_sword",
-			"menu_category": {
-        "category": "equipment"
-      }
-		},
-		"components": {
-            "minecraft:glint": true,
-			"minecraft:max_stack_size": 1,
-			"minecraft:enchantable": {
-				"value": 9,
-				"slot": "sword"
-			},
-
-   "minecraft:durability": {
-        "max_durability": 1256
+    "description": {
+      "identifier": "effect:wither_sword",
+      "category": "equipment"
+    },
+    "components": {
+      "minecraft:should_despawn": false,
+      
+      "minecraft:foil": true,
+      "minecraft:max_stack_size": 1,
+      "minecraft:durability": {
+        "max_durability": 3856
       },
-			"minecraft:allow_off_hand": true,
-			"minecraft:hand_equipped": true,
-			
-			"minecraft:can_destroy_in_creative": false,
-			"minecraft:icon": {
-				"texture": "wither_sword"
-			},
-						 "minecraft:repairable": {
-      "repair_items": [
+      "minecraft:allow_off_hand": false,
+      "minecraft:hand_equipped": true,
+      "minecraft:creative_category": {
+        "parent": "itemGroup.name.sword"
+      },
+      "minecraft:can_destroy_in_creative": false,
+      "minecraft:icon": {
+        "texture": "wither_sword"
+      },
+      "minecraft:repairable": {
+        "repair_items": [
           {
-              "items":[
-                  "effect:wither_sword"
-              ],
-              "repair_amount": 1256
+            "items": [
+              "effect:wither_sword"
+            ],
+            "repair_amount": 3856
           }
-      ]
-  },
-			      "minecraft:digger": {
+        ]
+      },
+      "minecraft:digger": {
         "use_efficiency": true,
         "destroy_speeds": [
           {
@@ -48,10 +45,100 @@
           }
         ]
       },
-      "tag:minecraft:is_sword": {},
-			
-			
-			"minecraft:damage": 10
-		}
-	}
+      "minecraft:render_offsets": {
+        "main_hand": {
+          "first_person": {
+            "position": [ 
+              0.8,  // X
+              0.1, // Y
+              -1.8  // Z
+            ],
+            "scale": [
+              0.01,
+              0.01,
+              0.01
+            ]
+          },
+          "third_person": {
+            "position": [ 
+              0.8, //x
+              2.5, //z = Mirando la entidad desde al frente.
+              -1.2 //y
+            ],
+            "scale": [
+              0.027,
+              0.027,
+              0.027
+            ]
+          }
+        }
+      },
+      "minecraft:display_name": {},
+      "minecraft:damage": 10,
+      "minecraft:cooldown": {
+        "category": "wither_sword",
+        "duration": 3
+      },
+      "minecraft:on_use": {
+        "on_use": {
+          "event": "on_use"
+        }
+      },
+      "minecraft:weapon": {
+        "on_hurt_entity": {
+          "event": "weapon"
+        },
+        "on_not_hurt_entity": {
+          "event": "weapon"
+        },
+        "on_hit_block": {
+          "event": "weapon"
+        }
+      }
+    },
+    "events": {
+      "on_use": {
+        "shoot": {
+          "projectile": "minecraft:wither_skull_dangerous",
+          "launch_power": 1
+        },
+        "run_command": {
+          "command": [ "playsound mob.wither.shoot @a[r=16] ~~~ 1 0.7" ]
+        },
+        "damage": {
+          "type": "durability",
+          "amount": 3,
+          "target": "self"
+        }
+      },
+      "weapon": {
+        "sequence": [
+          {
+            "damage": {
+              "type": "durability",
+              "amount": 1,
+              "target": "self"
+            }
+          },
+          {
+            "randomize": [
+              {
+                "weight": 90
+              },
+              {
+                "weight": 10,
+                "shoot": {
+                  "projectile": "minecraft:wither_skull",
+                  "launch_power": 1
+                },
+                "run_command": {
+                  "command": [ "playsound mob.wither.shoot @a[r=16]" ]
+                }
+              }
+            ]
+          }
+        ]
+      }
+    }
+  }
 }
```

### `Swords_B/manifest.json`

```diff
--- 1.6/Sword_B/manifest.json
+++ 2.8.14/Swords_B/manifest.json
@@ -1,26 +1,34 @@
 {
-    "format_version": 1,
+    "format_version": 2,
     "header": {
-        "description": "§l§fCreated by Effect99",
-        "name": "§l§fSwords and more swords V1.6",
-        "uuid": "1ecf4d4b-3a3c-1be3-bc21-9512946109b6",
-        "version": [1, 0, 0]
+        "name": "§l§fSwords and more swords §6V2.8.9.5 B",
+        "description": "§7By Effect99",
+        "uuid": "1acf4d4b-3a3c-1be3-bc21-9512946109b1",
+        "version": [1, 0, 0],
+        "min_engine_version": [ 1, 19, 40 ]
     },
     "modules": [
+       {
+           "type": "data",
+           "uuid": "ba10e35a-3b9c-3c0c-a9b9-fc4efa7309ea",
+           "version": [1, 0, 0]
+       },
+       {
+          "type": "script",
+          "uuid": "76310e1c-d881-46e6-eb3b-4fabfae56941",
+          "version": [1, 0, 0],
+          "entry": "scripts/javascript.js"
+       }
+    ],
+    "dependencies": [
         {
-            "type": "data",
-            "uuid": "bc00e35a-1b9c-3c0c-a9b9-fc4efa7309ac",
-            "version": [1, 0, 0]
+            "description": "@minecraft/server",
+            "uuid": "b26a4d4c-afdf-4690-88f8-931846312678",
+            "version": "1.12.0-beta"
+        },
+        {
+            "version": [1, 0, 0],
+            "uuid": "3f15ae41-a1c1-4111-aa1e-855a98a06316"
         }
-     ],
-    "dependencies": [
-     {
-      "version": [1, 0, 0],
-      "uuid": "2f15ae41-a1c1-4117-aa1e-855a98a06318"
-        }
-    ],
-    "metadata": {
-        "product_type": "addon",
-        "authors": [ "Effect99" ]
-  }
+    ]
 }
```

### `Swords_B/recipes/fire_sword.json`

```diff
--- 1.6/Sword_B/recipes/fire_sword.json
+++ 2.8.14/Swords_B/recipes/fire_sword.json
@@ -6,22 +6,16 @@
     },  
     "tags": [ "crafting_table" ],
     "pattern": [
-      "#SM",
-      "SBS",
-      "NS#"
+      "F",
+      "F",
+      "#"
     ],
     "key": {
-      "N": {
+      "#": {
         "item": "minecraft:blaze_rod"
       },
-      "S": {
-        "item": "minecraft:blaze_powder"
-      },
-      "B": {
-        "item": "minecraft:iron_sword"  
-      },
-      "M": {
-        "item": "minecraft:magma_cream"    
+      "F": {
+        "item": "minecraft:fire"
       }
     },
     "result": {
```

### `Swords_B/recipes/glowstone_sword.json`

```diff
--- 1.6/Sword_B/recipes/glowstone_sword.json
+++ 2.8.14/Swords_B/recipes/glowstone_sword.json
@@ -6,9 +6,9 @@
     },  
     "tags": [ "crafting_table" ],
     "pattern": [
-      "020",
-      "020",
-      "010"
+      "2",
+      "2",
+      "1"
     ],
     "key": {
       "1": {
```

### `Swords_R/manifest.json`

```diff
--- 1.6/Sword_R/manifest.json
+++ 2.8.14/Swords_R/manifest.json
@@ -1,22 +1,24 @@
 {
-    "format_version": 1,
+    "format_version": 2,
     "header": {
         "description": "§l§fCreated by Effect99",
-        "name": "§l§fSwords and more swords V1.6",
-        "uuid": "2f15ae41-a1c1-4117-aa1e-855a98a06318",
-        "version": [1, 0, 0]
+        "name": "§l§fSwords and more swords §6V2.8.9.5 R",
+        "uuid": "3f15ae41-a1c1-4111-aa1e-855a98a06316",
+        "version": [ 1, 0, 0 ],
+        "min_engine_version": [ 1, 19, 40 ]
     },
     "modules": [
         {
+            "description": "§l§fCreated by Effect99",
             "type": "resources",
-            "uuid": "e5447658-01ef-11e8-a1a0-ba2c34b08f13",
+            "uuid": "a6437658-11af-11e8-a1a0-be2c34b08f12",
             "version": [1, 0, 0]
         }
     ],
     "dependencies": [
      {
       "version": [1, 0, 0],
-      "uuid": "1ecf4d4b-3a3c-1be3-bc21-9512946109b6"
+      "uuid": "1acf4d4b-3a3c-1be3-bc21-9512946109b1"
         }
     ]
 }
```

### `Swords_R/texts/en_US.lang`

```diff
--- 1.6/Sword_R/texts/en_US.lang
+++ 2.8.14/Swords_R/texts/en_US.lang
@@ -1,3 +1,9 @@
+tile.effect99:sapling3.name=Jungle Sapling
+tile.effect99:silver_ore.name=Silver Ore
+tile.effect99:quartz_diamond_ore.name=Quartz Diamond Ore
+tile.effect99:quartz_diamond_block.name=Quartz Diamond block
+tile.effect99:fake_ice.name=Fake Ice
+
 item.effect:blaze_sword=§l§6Blaze Sword
 item.effect:coal_sword=§l§0Coal Sword
 item.effect:shulker_sword=§l§5Shulker sword
@@ -7,13 +13,13 @@
 item.effect:slime_sword=§l§aSlime Sword
 item.effect:emerald_sword=§l§aEmerald Sword
 item.effect:spectral_sword=§l§fSpectral Sword
-item.effect:lapis_sword=§1Lapis Sword
+item.effect:lapis_sword=§l§1Lapis Sword
 item.effect:sea_sword=§l§bSea Sword
 item.effect:grass_sword=§l§2Grass Sword
 item.effect:ice_sword=§l§bIce Sword
 item.effect:obsidian_sword=§l§8Obsidian Sword
 item.effect:glowstone_sword=§l§gGlowstone Sword
-item.effect:sword_of_time=§lTime Sword
+item.effect:time_sword=§lTime Sword
 item.effect:creeper_sword=§l§aCreeper§f Sword
 item.effect:fire_sword=§l§6Fire Sword
 item.effect:magma_sword=§l§6Magma Sword
@@ -22,5 +28,647 @@
 item.effect:lightning_sword=§g§lLightning Sword
 item.effect:ender_sword=§l§5Ender Sword
 item.effect:sponge_sword=§l§eSponge Sword
-item.effect:bone_sword=§lBone Sword
-item.effect:quartz_sword=§lQuartz Sword
+item.effect:wet_sponge_sword=§l§gWet Sponge Sword
+item.effect:bone_sword=§lSkeleton Bone Sword
+item.effect:quartz_sword=§lQuartz Diamond Sword
+item.effect:glass_sword=§l§bGlass Sword
+item.effect:wither_skeleton_sword=§l§7Wither Skeleton Sword
+item.effect:ultra_instinct_sword=§lUltra Instinct Sword
+item.effect:wolf_sword=§l§7Wolf Sword
+item.effect:silver_sword=§l§7Silver Sword
+item.effect:nether_star_sword=§l§fNether Star Sword
+item.effect:bedrock_sword=§l§7Bedrock Sword
+item.effect:ghost_sword=§l§fGhost Sword
+item.effect:clock_sword=§l§gClock Sword
+item.effect:bee_sword=§l§gBee Stinger
+item.effect:cursed_pumpkin_sword=§l§6Cursed pumpkin sword
+
+item.effect:bedrock_stick=§7Bedrock Stick
+item.effect:silver_ingot=Silver Ingot
+item.effect:quartz_diamond=Quartz Diamond
+item.effect:quartz_diamond_stick=Quartz Diamond Stick
+
+entity.entity:slime_king.name=§lSlime King
+entity.entity:ghost.name=§lGhost
+entity.entity:alpha_wolf.name=§l§7Alpha Wolf
+entity.entity:ghost.name=§l§fGhost
+entity.entity:mountable_slime.name=§l§aSlime Mount
+entity.entity:shulker_shield.name=§l§5Shulker Shield
+entity.entity:ultra_instinct_explode.name=§lUltra Instinct Projectile
+entity.entity:pumpkin_projectile.name=§l§6Pumpkin projectile
+entity.entity:nether_star_projectile.name=Nether Star
+
+item.spawn_egg.entity.entity:slime_king.name=Spawn §a§lSlime King
+item.spawn_egg.entity.entity:alpha_wolf.name=Spawn §7Alpha Wolf
+item.spawn_egg.entity.entity:ghost.name=Spawn §lGhost
+
+action.hint.exit.entity:mountable_slime=§l§aSlime mount
+action.hint.exit.entity:shulker_shield=§l§5Shulker Shield
+action.hint.exit.spider=§lSpider
+
+updates_changelog.header.title=§l§6Changelog §r§fV2.8.9                                                                                     
+basic_information.header.title=§l§6About                                                                                           
+howtoplay.updates_changelog.title=§lInformation
+howtoplay.basic_information.title=§lInformation
+howtoplay.basic_information=§lAbout..
+howtoplay.updates_changelog=§lUpdates Changelog
+howtoplay.category.basic_information=§lInformation
+howtoplay.category.swords=§lSwords and More Swords
+howtoplay.category.blocks_and_items=§lBlocks, Items and Mobs
+howtoplay.blocks_and_items=§lBlocks and Items
+howtoplay.sword_mobs=§lMobs
+howtoplay.blocks_and_items.title=§lBlocks, Items and Mobs
+blocks_and_items.header.title=§l§6Blocks, Items and more                                                                               
+howtoplay.sword_mobs.title=§lBlocks, Items and Mobs
+sword_mobs.header.title=§l§6Mobs                                                                                                      
+
+effect.updates_changelog.text_0=• Small changes
+effect.updates_changelog.text_1=• Bug fixes
+effect.updates_changelog.text_2=§r
+effect.updates_changelog.text_3=§r
+effect.updates_changelog.text_4=§r 
+effect.updates_changelog.text_5=§r
+effect.updates_changelog.text_6=§r
+
+blocks_and_items.header.title_1=§lQuartz diamond ore                                                                            
+effect.blocks_and_items.text_0= Spawns below height 16 (Rare) (will deal damage when sting if you're too close).  You will also find them in the lower layers of The End dimension.
+blocks_and_items.header.title_2=§lQuartz diamond                                                                            
+blocks_and_items.header.title_3=§lQuartz diamond stick                                                                            
+blocks_and_items.header.title_7=§lQuartz diamond block                                                                            
+effect.blocks_and_items.text_1= Durability: 20, Damage: 24, (Causes you damage when you attack entities) (It is crafted like a common stick)
+blocks_and_items.header.title_4=§lSilver ore                                                                            
+effect.blocks_and_items.text_2= Spawns below height 35 (common) (Place in the oven to get silver ingot)
+blocks_and_items.header.title_5=§lSilver ingot                                                                            
+blocks_and_items.header.title_6=§lBedrock stick                                                                            
+effect.blocks_and_items.text_3= Durability: Unbreakable, Damage: 6 (It is crafted like a common stick)
+effect.blocks_and_items.text_4= 
+effect.blocks_and_items.text_5= 
+effect.blocks_and_items.text_6= 
+
+sword_mobs.header.title.1=§lGhost                                                                                                      
+effect.sword_mobs.text_0=They will appear at night, these entities are not dangerous, they will not try to attack you and you will not be able to attack them either, but if you touch them as if you want to hurt them, the entity will drop the ghost sword with a probability of 0.3% so it can take you a while to get it. There will also be a 1% chance that the entity will randomly teleport so it can escape from you. This entity is also sensitive to light, so if it gets too close to the light, it will disappear. This entity only appears on grass or stone blocks. -Attack damage: Unknown Health: Unknown
+sword_mobs.header.title.2=§lGrass Witch                                                                                                      
+effect.sword_mobs.text_1=The grass witch will appear at night with little probability, when you try to attack it it will attack you with the same abilities as the grass sword, when you kill it it will drop the grass sword with a 20% chance. -Health: 32
+sword_mobs.header.title.3=§lAlpha Wold                                                                                                      
+effect.sword_mobs.text_2=These wolves spawn in the taiga biome only on a full moon and will be aggressive towards all animals and players, when you hear a distant howl it means one spawned nearby, the silver sword will be his weakness and he will drop the wolf sword with a 10% chance if you kill him with the silver sword. -Attack damage: 8 -Health: 480
+sword_mobs.header.title.4=§lRed-eyed Enderman                                                                                                      
+effect.sword_mobs.text_3=They will appear at night with low probability, they will be more aggressive and stronger than a normal Enderman. Killing him will drop the ender sword with a 2.5% chance. -Attack damage: 12 -Health: 120
+sword_mobs.header.title.5=§lKing Slime                                                                                                      
+effect.sword_mobs.text_4=The king slime appears in the swamp biome at night with a low probability, it will be very fast and aggressive with the player. Will drop the sword of slime with a 4% chance. -Attack damage: Unknown -Health: 300
+sword_mobs.header.title.6=§lCentella                                                                                                      
+effect.sword_mobs.text_5=Unknown entity, will appear when lightning strikes with a 20% chance. He will drop the lightning sword with a 2% chance. (It will be hard to kill since it has a lot of life, deals a lot of damage and will disappear in less than 60 seconds) (This entity is a reference to a strange real-life atmospheric phenomenon.) -Attack damage: Unknown -Health: 200
+sword_mobs.header.title.7=§lSlime baby                                                                                                      
+effect.sword_mobs.text_6=It appears when you have the slime sword in your hand, when you get off the slime it will try to attack all nearby enemies, you can ride the little slime again, but it will not obey you and will move in any direction, but it will increase its speed x3. -Attack damage: 1 -Health: Inmortal
+
+effect.basic_information.text_0=§c• Activate the option "Holiday Creator Features" and "Creation of Custom Biomes" for the correct functioning of the Add-On. 
+effect.basic_information.text_1=§c• If the add-on doesn't work properly, restart Minecraft and reactivate the packs 
+effect.basic_information.text_2= 
+effect.basic_information.text_3=§6• A pack of 39 swords with special powers.
+effect.basic_information.text_4=• Use the command "/function give" to get all the swords.
+effect.basic_information.text_5=• Swords can be found in the Creative Inventory under the Swords tab.
+effect.basic_information.text_6= 
+effect.basic_information.text_7=§c- Report error to my Twitter §l§b@Effectoo
+effect.basic_information.text_8=§c- Any suggestions to add in the addon are welcome as long as you send them to me on my Twitter.
+effect.basic_information.text_9= 
+basic_information.header.title_1=  §lCreated by Effect99
+
+howtoplay.coal_sword.title=§lSwords
+howtoplay.coal_sword=§lCoal Sword
+coal_sword.header.title=§lCoal Sword                                                                    
+effect.coal_sword.text.0=-Durability: 121
+effect.coal_sword.text.1=-Damage: 4
+effect.coal_sword.text.2=-Enchantable: true
+effect.coal_sword.text.3=-Repairable: true (With coal, sticks and the same sword.)
+effect.coal_sword.text.4=-Special skills: None (It only serves as fuel for the furnace.)
+effect.coal_sword.text.5=-How to create or get it:
+effect.coal_sword.text.6=  Two blocks of coal and a stick.
+
+howtoplay.silver_sword.title=§lSwords
+howtoplay.silver_sword=§lSilver Sword
+silver_sword.header.title=§lSilver Sword                                                                    
+effect.silver_sword.text.0=-Durability: 1800
+effect.silver_sword.text.1=-Damage: 6
+effect.silver_sword.text.2=-Enchantable: true
+effect.silver_sword.text.3=-Repairable: true (Only with the same sword.)
+effect.silver_sword.text.4=-Special skills: 
+effect.silver_sword.text.5=  Causes more damage than normal to "alpha wolves"
+effect.silver_sword.text.6=-How to create or get it:
+effect.silver_sword.text.7=  You must find the silver ore in the depths of the overworld (normal world) below height 15 and place it in the oven to obtain the silver ingot and be able to create the sword.
+
+howtoplay.lapis_sword.title=§lSwords
+howtoplay.lapis_sword=§lLapis Sword
+lapis_sword.header.title=§lLapis Sword                                                                    
+effect.lapis_sword.text.0=-Durability: 528
+effect.lapis_sword.text.1=-Damage: 5
+effect.lapis_sword.text.2=-Enchantable: true
+effect.lapis_sword.text.3=-Repairable: true (With lapis lazuli and the same sword.)
+effect.lapis_sword.text.4=-Special skills: 
+effect.lapis_sword.text.5=  You will be given 5 experience points in a random period of between 2.5 and 6 seconds.
+effect.lapis_sword.text.6=-How to create or get it:
+effect.lapis_sword.text.7=  Found in the chests of: Stronghold and Pillager Outpost.
+
+howtoplay.glowstone_sword.title=§lSwords
+howtoplay.glowstone_sword=§lGlowstone Sword
+glowstone_sword.header.title=§lGlowstone Sword                                                                    
+effect.glowstone_sword.text.0=-Durability: 128
+effect.glowstone_sword.text.1=-Damage: 4
+effect.glowstone_sword.text.2=-Enchantable: true
+effect.glowstone_sword.text.3=-Repairable: true (By glowstone, glowstone dust and the same sword.)
+effect.glowstone_sword.text.4=-Special skills: 
+effect.glowstone_sword.text.5=  This sword emits a lot of light and can be placed in the left hand.
+effect.glowstone_sword.text.6=-How to create or get it:
+effect.glowstone_sword.text.7=  Two glowstone blocks and a blaze rod
+
+howtoplay.glass_sword.title=§lSwords
+howtoplay.glass_sword=§lGlass Sword
+glass_sword.header.title=§lGlass Sword                                                                    
+effect.glass_sword.text.0=-Durability: 1
+effect.glass_sword.text.1=-Damage: 33
+effect.glass_sword.text.2=-Enchantable: true
+effect.glass_sword.text.3=-Repairable: false 
+effect.glass_sword.text.4=-Special skills: none
+effect.glass_sword.text.5=-How to create or get it:
+effect.glass_sword.text.6=  You will have to throw the fire sword into the water.
+
+howtoplay.jungle_sword.title=§lSwords
+howtoplay.jungle_sword=§lJungle Sword
+jungle_sword.header.title=§lJungle Sword                                                                    
+effect.jungle_sword.text.0=-Durability: 128
+effect.jungle_sword.text.1=-Damage: 4
+effect.jungle_sword.text.2=-Enchantable: true
+effect.jungle_sword.text.3=-Repairable: true (Only with the same sword.)
+effect.jungle_sword.text.4=-Special skills: 
+effect.jungle_sword.text.5=  Your health will be reduced to 4 hearts, but an absorption potion effect will be added.
+effect.jungle_sword.text.6=  Vines will be placed in nearby blocks. (Blocks: logs, grass, dirt, sand, cobblestone, stone, obsidian, endstone, gravel, ice, planks, leaves, netherrack, and nether bricks.)
+effect.jungle_sword.text.7=-How to create or get it:
+effect.jungle_sword.text.8=  Fishing in the jungle biome or jungle temple.
+
+howtoplay.cactus_sword.title=§lSwords
+howtoplay.cactus_sword=§lCactus Sword
+cactus_sword.header.title=§lCactus Sword                                                                    
+effect.cactus_sword.text.0=-Durability: 125
+effect.cactus_sword.text.1=-Damage: 6
+effect.cactus_sword.text.2=-Enchantable: true
+effect.cactus_sword.text.3=-Repairable: true (Only with the same sword.)
+effect.cactus_sword.text.4=-Special skills: 
+effect.cactus_sword.text.5=  You will receive damage when having the sword in hand, but you will also damage very close entities.
+effect.cactus_sword.text.6=-How to create or get it:
+effect.cactus_sword.text.7=  A stick and two cacti
+
+howtoplay.sponge_sword.title=§lSwords
+howtoplay.sponge_sword=§lSponge Swords
+sponge_sword.header.title.0=§lSponge Sword                                                                    
+effect.sponge_sword.text.0=-Durability: 128
+effect.sponge_sword.text.1=-Damage: 5
+effect.sponge_sword.text.2=-Enchantable: true
+effect.sponge_sword.text.3=-Repairable: true (By sponge and the same sword.)
+effect.sponge_sword.text.4=-Special skills: 
+effect.sponge_sword.text.5=  It will absorb water in a radius of 2 blocks, after several seconds absorbing water the sword will transform into a "wet sponge sword".
+effect.sponge_sword.text.6=-How to create or get it:
+effect.sponge_sword.text.7=  On killing the elder guardian with a 6.5% chance.
+effect.sponge_sword.text.8=  When putting the wet sponge sword in the oven.
+sponge_sword.header.title.1=§lWet Sponge Sword                                                                    
+effect.sponge_sword.text.9=-Durability: 64
+effect.sponge_sword.text.10=-Damage: 3
+effect.sponge_sword.text.11=-Enchantable: false
+effect.sponge_sword.text.12=-Repairable: true (Sponges and more sponges.)
+effect.sponge_sword.text.13=-Special skills: none
+effect.sponge_sword.text.14=-How to create or get it:
+effect.sponge_sword.text.15=  When wetting the sponge sword.
+
+howtoplay.emerald_sword.title=§lSwords
+howtoplay.emerald_sword=§lEmerald Sword
+emerald_sword.header.title=§lEmerald Sword                                                                    
+effect.emerald_sword.text.0=-Durability: 2300
+effect.emerald_sword.text.1=-Damage: 7
+effect.emerald_sword.text.2=-Enchantable: true
+effect.emerald_sword.text.3=-Repairable: true (Only with the same sword.)
+effect.emerald_sword.text.4=-Special skills: 
+effect.emerald_sword.text.5=  You'll get a village hero potion effect for being inside a village and it will give villagers a resistance effect within 64 radius.
+effect.emerald_sword.text.6=-How to create or get it:
+effect.emerald_sword.text.7=  Found in the chests of: Stronghold, Woodland Mansion, and Pillager Outpost.
+
+howtoplay.bone_sword.title=§lSwords
+howtoplay.bone_sword=§lSkeleton bone Sword
+bone_sword.header.title=§lSkeleton bone Sword                                                                  
+effect.bone_sword.text.0=-Durability: 820
+effect.bone_sword.text.1=-Damage: 5
+effect.bone_sword.text.2=-Enchantable: true
+effect.bone_sword.text.3=-Repairable: true (Everything that is made of: bone.)
+effect.bone_sword.text.4=-Special skills: 
+effect.bone_sword.text.5=  When attacking you will throw arrows with a 20% chance.
+effect.bone_sword.text.6=  Crops will grow much faster within a 2 block radius.
+effect.bone_sword.text.7=  Enemy arrows within 8 radius will slow down.
+effect.bone_sword.text.8=-How to create or get it:
+effect.bone_sword.text.9=  Killing skeletons at night in the desert biome with a 0.7% chance.
+
+howtoplay.wither_skeleton_sword.title=§lSwords
+howtoplay.wither_skeleton_sword=§lWither Skeleton Sword
+wither_skeleton_sword.header.title=§lWither Skeleton Sword                                                                    
+effect.wither_skeleton_sword.text.0=-Durability: 128
+effect.wither_skeleton_sword.text.1=-Damage: 4
+effect.wither_skeleton_sword.text.2=-Enchantable: true
+effect.wither_skeleton_sword.text.3=-Repairable: true (Coal, sticks and the same sword)
+effect.wither_skeleton_sword.text.4=-Special skills: 
+effect.wither_skeleton_sword.text.5=  Will give wither effect to the entities you attack
+effect.wither_skeleton_sword.text.6=-How to create or get it:
+effect.wither_skeleton_sword.text.7=  When killing wither skeletons with a 2.5% chance
+
+howtoplay.slime_sword.title=§lSwords
+howtoplay.slime_sword=§lSlime Sword
+slime_sword.header.title=§lSlime Sword                                                                    
+effect.slime_sword.text.0=-Durability: 675
+effect.slime_sword.text.1=-Damage: 6
+effect.slime_sword.text.2=-Enchantable: true
+effect.slime_sword.text.3=-Repairable: true (With slime and with the same sword.)
+effect.slime_sword.text.4=-Special skills: 
+effect.slime_sword.text.5=  By having the sword in hand you will get a baby slime mount.
+effect.slime_sword.text.6=  If you get off the slime mount, the slime will defend you from all nearby monsters. (The slime deals one point of damage and is immortal, plus it will teleport to its owner when it gets too far away.)
+effect.slime_sword.text.7=  Jumping with the slime mount and falling on an entity will damage it. (Jumping with the slime mount can be tricky.)
+effect.slime_sword.text.8=-How to create or get it:
+effect.slime_sword.text.9= Killing the slime king that appears at night in the swamp biome with a 4% chance.
+
+howtoplay.obsidian_sword.title=§lSwords
+howtoplay.obsidian_sword=§lObsidian Sword
+obsidian_sword.header.title=§lObsidian Sword                                                                    
+effect.obsidian_sword.text.0=-Durability: 3000
+effect.obsidian_sword.text.1=-Damage: 8
+effect.obsidian_sword.text.3=-Enchantable: true 
+effect.obsidian_sword.text.4=-Repairable: true (By obsidian and the same sword.)
+effect.obsidian_sword.text.5=-Special skills: 
+effect.obsidian_sword.text.6=  You will be immune to explosions and you will have knockback resistance.
+effect.obsidian_sword.text.7=-Description:
+effect.obsidian_sword.text.8=  When attacking, the durability points of the sword could lose 1 point with a probability of 55%, 2 points with a probability of 30% and 3 points with a probability of 15%.
+effect.obsidian_sword.text.9=-How to create or get it:
+effect.obsidian_sword.text.10=  You must throw the fire sword into the rain and wait a few seconds.
+
+howtoplay.magma_sword.title=§lSwords
+howtoplay.magma_sword=§lMagma Sword
+magma_sword.header.title=§lMagma Sword                                                                    
+effect.magma_sword.text.0=-Durability: 1316
+effect.magma_sword.text.1=-Damage: 7.2
+effect.magma_sword.text.2=-Enchantable: true
+effect.magma_sword.text.3=-Repairable: true (By magma blocks and the same sword.)
+effect.magma_sword.text.4=-Special skills: 
+effect.magma_sword.text.5=  Magma blocks won't hurt you.
+effect.magma_sword.text.6=  Fire will only hurt you if you are standing on it.
+effect.magma_sword.text.7=  The lava under your feet will turn into magma blocks.
+effect.magma_sword.text.8=-How to create or get it:
+effect.magma_sword.text.9=  In chests of great underwater ruins.
+
+howtoplay.clock_sword.title=§lSwords
+howtoplay.clock_sword=§lClock Sword
+clock_sword.header.title=§lClock Sword                                                                    
+effect.clock_sword.text.0=-Durability: 4800
+effect.clock_sword.text.1=-Damage: 7
+effect.clock_sword.text.2=-Enchantable: true
+effect.clock_sword.text.3=-Repairable: true (= Creation materials.)
+effect.clock_sword.text.4=-Special skills: 
+effect.clock_sword.text.5=  Right-clicking or pressing the screen will advance one hour (1000 ticks) into the game. (The game will go 10 times faster for 5 seconds)
+effect.clock_sword.text.6=-How to create or get it:
+
+howtoplay.grass_sword.title=§lSwords
+howtoplay.grass_sword=§lGrass Sword
+grass_sword.header.title=§lGrass Sword                                                                    
+effect.grass_sword.text.0=-Durability: 250
+effect.grass_sword.text.1=-Damage: 8
+effect.grass_sword.text.2=-Enchantable: true
+effect.grass_sword.text.3=-Repairable: true (Only with the same sword.)
+effect.grass_sword.text.4=-Special skills: 
+effect.grass_sword.text.5=  All nearby entities within a radius of 8 will be attacked by a strange grass entity that will bury them a bit underground or completely depending on the size of the entity.
+effect.grass_sword.text.6=  The dirt blocks will turn into grass.
+effect.grass_sword.text.7=-How to create or get it:
+effect.grass_sword.text.8=  You will have to kill a grass witch, these appear at night with a low probability and will drop the sword with a 20% probability.
+effect.grass_sword.text.9= 
+
+howtoplay.sea_sword.title=§lSwords
+howtoplay.sea_sword=§lSea Sword
+sea_sword.header.title=§lSea Sword                                                                    
+effect.sea_sword.text.0=-Durability: 1356
+effect.sea_sword.text.1=-Damage: 7
+effect.sea_sword.text.2=-Enchantable: true
+effect.sea_sword.text.3=-Repairable: true (By heart of the sea and the same sword.)
+effect.sea_sword.text.4=-Special skills: 
+effect.sea_sword.text.5= You can swim as fast as dolphins.
+effect.sea_sword.text.6= You will become a mermaid.
+effect.sea_sword.text.7=  You can breathe underwater but you cannot breathe air.
+effect.sea_sword.text.8=-Description:
+effect.sea_sword.text.9=  You will jump like a fish when you are out of the water.
+effect.sea_sword.text.10=-How to create or get it:
+effect.sea_sword.text.11=  In treasure chests.
+
+howtoplay.blaze_sword.title=§lSwords
+howtoplay.blaze_sword=§lBlaze Sword
+blaze_sword.header.title=§lBlaze Sword                                                                    
+effect.blaze_sword.text.0=-Durability: 2300
+effect.blaze_sword.text.1=-Damage: 6
+effect.blaze_sword.text.2=-Enchantable: true
+effect.blaze_sword.text.3=-Repairable: true (Only with the same sword.)
+effect.blaze_sword.text.4=-Special skills: 
+effect.blaze_sword.text.5=  By right-clicking or pressing the screen, your body will levitate for a few seconds and then launch several small fireballs in the direction you are looking.
+effect.blaze_sword.text.6=  The fire won't hurt you.
+effect.blaze_sword.text.7=  Sometimes you will throw fireballs when hitting entities.
+effect.blaze_sword.text.8=  Small fireballs will not be able to approach you within a radius of 7.
+effect.blaze_sword.text.9=-Description:
+effect.blaze_sword.text.10=  Blaze rods will surround you around your body.
+effect.blaze_sword.text.11=  Your body will turn somewhat orange.
+effect.blaze_sword.text.12=-How to create or get it:
+effect.blaze_sword.text.13=  A snow golem must kill a blaze this will release it with 0.5%
+
+howtoplay.nether_star_sword.title=§lSwords
+howtoplay.nether_star_sword=§lNether Star Sword
+nether_star_sword.header.title=§lNether Star Sword    
+effect.nether_star_sword.text.13=-Durability: 3256                                                                
+effect.nether_star_sword.text.0=-Damage: 7 (12= Her damage was reduced to 7 as her new power makes her too powerful in this Add-On update.)
+effect.nether_star_sword.text.2=-Should Despawn Item: false
+effect.nether_star_sword.text.3=-Enchantable: true
+effect.nether_star_sword.text.4=-Repairable: true (With a nether star and the same sword.)
+effect.nether_star_sword.text.5=-Special skills: 
+effect.nether_star_sword.text.6=  The stars of the nether will fall from the sky when you are attacking an entity, these stars will deal 6 damage per hit.
+effect.nether_star_sword.text.7=-Description:
+effect.nether_star_sword.text.8=  When using it to kill the Wither you may get the Wither sword.
+effect.nether_star_sword.text.9=  When thrown into the fire it explodes violently, this explosion is capable of breaking bedrock.
+effect.nether_star_sword.text.10=  This sword is slightly unstable and can explode with a 0.01% chance when attacking entities.
+effect.nether_star_sword.text.11=-How to create or get it:
+effect.nether_star_sword.text.12=  Crafting her with a diamond sword and a nether star.
+
+howtoplay.ice_sword.title=§lSwords
+howtoplay.ice_sword=§lIce Sword
+ice_sword.header.title=§lIce Sword                                                                    
+effect.ice_sword.text.0=-Durability: 500
+effect.ice_sword.text.1=-Damage: 8.5
+effect.ice_sword.text.2=-Enchantable: true
+effect.ice_sword.text.3=-Repairable: true (For ice and the same sword.)
+effect.ice_sword.text.4=-Special skills: 
+effect.ice_sword.text.5=  The ice that is placed when using this sword will disappear after approximately 8 seconds
+effect.ice_sword.text.6=  All the water under your feet will turn to ice.
+effect.ice_sword.text.7=  Sometimes you will throw snowballs at the entities you attack.
+effect.ice_sword.text.9=  Right-clicking or pressing the screen will cause entities within a radius of 8 to be encased in blocks of ice. (Sword durability: -6)
+effect.ice_sword.text.10=-Description:
+effect.ice_sword.text.11=  If the player is on fire the sword will turn into water.
+effect.ice_sword.text.12=-How to create or get it:
+effect.ice_sword.text.13=  In the chests of: Igloos and Villages in the snow.
+
+howtoplay.quartz_sword.title=§lSwords
+howtoplay.quartz_sword=§lQuartz Sword
+quartz_sword.header.title=§lQuartz Sword                                                                    
+effect.quartz_sword.text.0=-Durability: 1
+effect.quartz_sword.text.1=-Damage: 600
+effect.quartz_sword.text.2=-Enchantable: false
+effect.quartz_sword.text.3=-Repairable: false
+effect.quartz_sword.text.4=-Special skills: None
+effect.quartz_sword.text.5=-Description:
+effect.quartz_sword.text.6=  Putting the sword in your hand will cause you a lot of damage for a moment and taking it out of your hand will too.
+effect.quartz_sword.text.7=  The sword causes so much damage that when you attack an enemy you will die too. (everything has a price)
+effect.quartz_sword.text.8=-How to create or get it:
+effect.quartz_sword.text.9=  With two quartz diamond blocks and a quartz diamond stick that is created with the same material.
+effect.quartz_sword.text.10=  (You should look for quartz diamond ores below height 15 in small quantities. (they are rare to find))
+
+howtoplay.spider_sword.title=§lSwords
+howtoplay.spider_sword=§lSpider Sword
+spider_sword.header.title=§lSpider Sword                                                                    
+effect.spider_sword.text.0=-Durability: 628
+effect.spider_sword.text.1=-Damage: 5
+effect.spider_sword.text.2=-Enchantable: true
+effect.spider_sword.text.3=-Repairable: true (With cobwebs, spider eyes and the same sword.)
+effect.spider_sword.text.4=-Special skills: 
+effect.spider_sword.text.5=  The spider mount will be able to climb walls.
+effect.spider_sword.text.6=  You will throw cobwebs when attacking entities with a 5% chance.
+effect.spider_sword.text.7=  Holding the sword in your hand you will get a spider mount.
+effect.spider_sword.text.8=  Right-clicking or pressing the screen will fire cobweb projectiles for a few seconds. (Sword durability: -8)
+effect.spider_sword.text.9=-How to create or get it:
+effect.spider_sword.text.10=  In the chests of the abandoned mineshaft
+
+howtoplay.tnt_sword.title=§lSwords
+howtoplay.tnt_sword=§lTnt Sword
+tnt_sword.header.title=§lTnt Sword                                                                    
+effect.tnt_sword.text.0=-Durability: 64
+effect.tnt_sword.text.1=-Damage: 4
+effect.tnt_sword.text.2=-Enchantable: true
+effect.tnt_sword.text.3=-Repairable: true (By tnt and the same sword.)
+effect.tnt_sword.text.4=-Special skills: 
+effect.tnt_sword.text.5=  When attacking, you will throw small explosions.
+effect.tnt_sword.text.6= By right clicking or pressing the screen, a very powerful tnt will appear that will explode in 8 seconds. (Sword durability: -18)
+effect.tnt_sword.text.7=-Description:
+effect.tnt_sword.text.8=  When thrown into the fire it will explode violently.
+effect.tnt_sword.text.9=-How to create or get it:
+effect.tnt_sword.text.10=  In the chests of the desert temple.
+
+howtoplay.wolf_sword.title=§lSwords
+howtoplay.wolf_sword=§lWolf Sword
+wolf_sword.header.title=§lWolf Sword                                                                    
+effect.wolf_sword.text.0=-Damage: 5 (+15 points during the night of the full moon. (They will not be visible in the sword damage))
+effect.wolf_sword.text.1=-Enchantable: false
+effect.wolf_sword.text.2=-Repairable: true (Only with the same sword.)
+effect.wolf_sword.text.3=-Special skills: 
+effect.wolf_sword.text.4=  -During the night of the full moon:
+effect.wolf_sword.text.5=    The player will deal 15 points of damage per attack plus 5 points of sword attack for a total of 20.
+effect.wolf_sword.text.6=    The player will move faster.
+effect.wolf_sword.text.7=    The monsters will not attack you, you will be part of them.
+effect.wolf_sword.text.8=-Description:
+effect.wolf_sword.text.9=  -During the night of the full moon:
+effect.wolf_sword.text.10=    Your vision will look somewhat red
+effect.wolf_sword.text.11=    If you remove the sword from your hand before the end of the full moon night you will get negative potion effects. (They will disappear at dawn.)
+effect.wolf_sword.text.12=    If you have the sword in your hand during the sunset before the night of the full moon, you will feel dizzy.
+effect.wolf_sword.text.13=-How to create or get it:
+effect.wolf_sword.text.14=  You must kill an alpha wolf during the full moon with the silver sword and it will drop the sword with a 10% chance.
+effect.wolf_sword.text.15=  (Alpha wolves appear in the taiga biome during the night of the full moon, you will hear a distant howl when one appears nearby.)
+
+howtoplay.shulker_sword.title=§lSwords
+howtoplay.shulker_sword=§lShulker Sword
+shulker_sword.header.title=§lShulker Sword                                                                    
+effect.shulker_sword.text.0=-Durability: 2609
+effect.shulker_sword.text.1=-Damage: 6
+effect.shulker_sword.text.2=-Enchantable: true
+effect.shulker_sword.text.3=-Repairable: true (Only with the same sword.)
+effect.shulker_sword.text.4=-Special skills: 
+effect.shulker_sword.text.5=  Throw shulker projectiles with a 10% chance when attacking entities.
+effect.shulker_sword.text.6=  Right-clicking or pressing the screen will levitate entities within a radius of 6. (Sword durability: -8)
+effect.shulker_sword.text.7=  You will be immune to the effect of levitation.
+effect.shulker_sword.text.8=  When you duck you will get a shulker shell, which will protect you from enemy attacks but if they destroy the shell with you inside you will die too.
+effect.shulker_sword.text.9=-How to create or get it:
+effect.shulker_sword.text.10= When killing shulkers with a 4.5% chance
+
+howtoplay.bee_sword.title=§lSwords
+howtoplay.bee_sword=§lBee Sword
+bee_sword.header.title=§lBee Stinger                                                                   
+effect.bee_sword.text.0=-Durability: 1080
+effect.bee_sword.text.1=-Damage: 5
+effect.bee_sword.text.2=-Enchantable: true
+effect.bee_sword.text.3=-Repairable: true (bee sword, honeycomb, honey block)
+effect.bee_sword.text.4=-Special skills: 
+effect.bee_sword.text.5=   When attacking the enemies you will release from time to time small aggressive bees that will defend you.
+effect.bee_sword.text.6=-Description:
+effect.bee_sword.text.7=  Flowers will appear from time to time, when you walk through grass.
+effect.bee_sword.text.8=-How to create or get it:
+effect.bee_sword.text.9=  When a bee stings you, it will drop its stinger with a 2% percent chance.
+
+howtoplay.ghost_sword.title=§lSwords
+howtoplay.ghost_sword=§lGhost Sword
+ghost_sword.header.title=§lGhost Sword                                                                    
+effect.ghost_sword.text.0=-Durability: 3333
+effect.ghost_sword.text.1=-Damage: -666 (Being a negative number you cannot harm any entity)
+effect.ghost_sword.text.3=-Should Despawn Item: false
+effect.ghost_sword.text.4=-Enchantable: false
+effect.ghost_sword.text.5=-Repairable: false
+effect.ghost_sword.text.6=-Special skills: 
+effect.ghost_sword.text.7=  By holding the sword in hand, the player's legs will disappear and the player will turn into a ghost.
+effect.ghost_sword.text.8=  Nothing can harm the player, not fire, not lava, not explosions, basically nothing.
+effect.ghost_sword.text.9=  By right-clicking or pressing the screen the player will be able to teleport to any direction they are looking. (Sword durability: -6)
+effect.ghost_sword.text.10=  By getting very close to the walls, the player will be able to see nearby caves and will be able to teleport to any cave they are looking at.
+effect.ghost_sword.text.11=  By crouching, the player will levitate, he can basically fly.
+effect.ghost_sword.text.12=  You can move faster than normal.
+effect.ghost_sword.text.13=  The monsters will not attack you, now you are one of them.
+effect.ghost_sword.text.14=-Description:
+effect.ghost_sword.text.15=  The player's vision will look somewhat white.
+effect.ghost_sword.text.16=  The player will not be able to attack any entity.
+effect.ghost_sword.text.17=-How to create or get it:
+effect.ghost_sword.text.18=  At night ghosts will appear, these entities are not dangerous, they will not try to attack you and you will not be able to attack them either, but if you touch them as if you were trying to harm them, the entity will drop the sword with a probability of 0.3% so it could take you a while to get it. It will also be 1% likely that the entity will teleport randomly so it could escape you. This entity is also sensitive to light, so if it gets too close to the light it will disappear. This entity only appears in blocks of grass or stone.
+
+howtoplay.creeper_sword.title=§lSwords
+howtoplay.creeper_sword=§lCreeper Sword
+creeper_sword.header.title=§lCreeper Sword                                                                    
+effect.creeper_sword.text.0=-Durability: 1500
+effect.creeper_sword.text.1=-Damage: 6
+effect.creeper_sword.text.3=-Enchantable: true 
+effect.creeper_sword.text.4=-Repairable: true (For gunpowder and the same sword.)
+effect.creeper_sword.text.5=-Special skills: 
+effect.creeper_sword.text.6=  When attacking, it will launch small Creepers with a 20% chance that will explode in a few seconds with a small explosion.
+effect.creeper_sword.text.7=  By right-clicking or pressing the screen, the player will inflate like a Creeper and then the player will explode and die! (Sword durability: -1)
+effect.creeper_sword.text.8=-How to create or get it:
+effect.creeper_sword.text.9=  You will have to explode a Creeper loaded with a lighter and it will drop the sword with a 5% probability.
+
+howtoplay.fire_sword.title=§lSwords
+howtoplay.fire_sword=§lFire Sword
+fire_sword.header.title=§lFire Sword                                                                    
+effect.fire_sword.text.0=-Durability: 2000
+effect.fire_sword.text.1=-Damage: 6 (It will burn the enemies you attack.)
+effect.fire_sword.text.2=-Enchantable: true
+effect.fire_sword.text.3=-Repairable: true (By fire blocks(rare) and the same sword)
+effect.fire_sword.text.4=-Special skills: 
+effect.fire_sword.text.5=  You will be immune to fire.
+effect.fire_sword.text.6=  When you attack you will launch living flames with a 15% probability, these entities will attack the monsters and they will die after a few seconds.
+effect.fire_sword.text.7=  By right clicking or pressing the screen, you will activate the ability "rain of fire" this will create a shower of fireballs that will set fire all around. (Sword durability: -20)
+effect.fire_sword.text.8=  Entities very close to you will burn.
+effect.fire_sword.text.9=  The ice and snow will melt.
+effect.fire_sword.text.10=-Description: 
+effect.fire_sword.text.11=  It disappears if you enter the water.
+effect.fire_sword.text.12=  This sword emits light.
+effect.fire_sword.text.13=  By throwing the fire sword into the water it turns into an obsidian sword.
+effect.fire_sword.text.14=  Throwing the fire sword into the rain will cause it to turn into a crystal sword after a few seconds.
+effect.fire_sword.text.15=-How to create or get it:
+effect.fire_sword.text.16=  You must kill living flames, these appear in the Nether and some of them will attack you, to kill this entity correctly without the fire sword falling into the fire and vanishing, you will have to place blocks such as slabs, pressure plates or other types of I do not complete this to prevent the entity from setting fire. The entity will drop the sword with a 4.9% chance. This entity will disappear in a random period of between 25 and 60 seconds.
+
+howtoplay.spectral_sword.title=§lSwords
+howtoplay.spectral_sword=§lSpectral Sword
+spectral_sword.header.title=§lSpectral Sword                                                                    
+effect.spectral_sword.text.0=-Durability: 3256
+effect.spectral_sword.text.1=-Damage: 9
+effect.spectral_sword.text.3=-Should Despawn Item: false
+effect.spectral_sword.text.4=-Enchantable: false
+effect.spectral_sword.text.5=-Repairable: true (By ender crystal, nether star and by the same sword.)
+effect.spectral_sword.text.6=-Special skills: 
+effect.spectral_sword.text.7=  It will make the main block of each dimension transparent only in that dimension. (Overworld: stone, Nether: netherrack, End: endstone.)
+effect.spectral_sword.text.8=  Fire an explosive projectile. (Sword durability: -15)
+effect.spectral_sword.text.9=-Description:
+effect.spectral_sword.text.10=  This sword is somewhat unstable so it may explode when attacking entities with a 1% chance.
+effect.spectral_sword.text.11=  This sword will emit a slight light.
+effect.spectral_sword.text.12=  An ender crystal will appear above you and follow you everywhere.
+effect.spectral_sword.text.13=-How to create or get it:
+effect.spectral_sword.text.14=  When exploding ender crystals in the Nether with a 2% chance.
+effect.spectral_sword.text.15=  Kill a Ghast with his own projectile with a 6% chance.
+
+howtoplay.bedrock_sword.title=§lSwords
+howtoplay.bedrock_sword=§lBedrock Sword
+bedrock_sword.header.title=§lBedrock Sword                                                                    
+effect.bedrock_sword.text.0=-Durability: (Infinite)
+effect.bedrock_sword.text.1=-Damage: 18
+effect.bedrock_sword.text.3=-Should Despawn Item: false
+effect.bedrock_sword.text.4=-Enchantable: false
+effect.bedrock_sword.text.5=-Special skills: none
+effect.bedrock_sword.text.6=-Description: It works as an extremely powerful pickaxe.
+effect.bedrock_sword.text.7=-How to create or get it:
+effect.bedrock_sword.text.8=  It is created with two bedrock blocks and a bedrock stick that is created with the same material.
+effect.bedrock_sword.text.9=  (Bedrock can only be obtained by using the Ultra Instinct sword projectile or by throwing the Nether Star Sword into fire, which will cause a loud explosion that will shatter the bedrock.)
+
+howtoplay.ender_sword.title=§lSwords
+howtoplay.ender_sword=§lEnder Sword
+ender_sword.header.title=§lEnder Sword                                                                    
+effect.ender_sword.text.0=-Durability: 1256
+effect.ender_sword.text.1=-Damage: 9
+effect.ender_sword.text.2=-Enchantable: true
+effect.ender_sword.text.3=-Repairable: true (By ender pearl, ender eye or the same sword.)
+effect.ender_sword.text.4=-Special skills: 
+effect.ender_sword.text.5=  You will not take damage from any projectile and will randomly teleport within a radius of 16 when you are attacked with one.
+effect.ender_sword.text.6=  When they attack you, you will randomly teleport in a radius of 16 with a 50% chance.
+effect.ender_sword.text.7=  The water will cause you damage and you will teleport randomly.
+effect.ender_sword.text.8=  By right clicking or pressing the screen, you will randomly teleport in a radius of between 16 to 32 blocks. (Sword durability: -5) 
+effect.ender_sword.text.9=                                                                                             "Cooldown Duration": 2 = seconds                                                                                   
+effect.ender_sword.text.10=-How to create or get it:
+effect.ender_sword.text.11=  By killing the red-eyed enderman with a 2.5% chance, this enderman only appears in the overworld (normal world) with a low probability.
+
+howtoplay.lightning_sword.title=§lSwords
+howtoplay.lightning_sword=§lLightning Sword
+lightning_sword.header.title=§lLightning Sword                                                                    
+effect.lightning_sword.text.0=-Durability: 2012
+effect.lightning_sword.text.1=-Damage: 8
+effect.lightning_sword.text.2=-Enchantable: true
+effect.lightning_sword.text.3=-Repairable: true (Only with the same sword.)
+effect.lightning_sword.text.4=-Special skills: 
+effect.lightning_sword.text.5=  When attacking it will throw thunder.
+effect.lightning_sword.text.6=  By right clicking or pressing the screen, 41 rays will fall around you. (Sword durability: -9)
+effect.lightning_sword.text.7=  You will be immune to lightning damage but not fire.
+effect.lightning_sword.text.8=-Description:
+effect.lightning_sword.text.9=  This sword emits light.
+effect.lightning_sword.text.10=-How to create or get it:
+effect.lightning_sword.text.11=  You must kill an entity called "Centella in Spanish" or "spherical lightning or ball lightning in English", this entity will only appear with a 20% probability when lightning strikes during a storm, this entity will not try to harm you but if you get too close you will receive a lot damage, also this entity has 200 life points, that is, 100 hearts, it will not be easy to kill it, you must do it before it disappears since it only lives in a random period of between 10 to 60 seconds. (This entity is a reference to a strange real-life atmospheric phenomenon.)
+
+howtoplay.wither_sword.title=§lSwords
+howtoplay.wither_sword=§lWither Sword
+wither_sword.header.title=§lWither Sword                                                                    
+effect.wither_sword.text.0=-Durability: 3856
+effect.wither_sword.text.1=-Damage: 10
+effect.wither_sword.text.3=-Should Despawn Item: false
+effect.wither_sword.text.4=-Enchantable: false
+effect.wither_sword.text.5=-Repairable: true (Only with the same sword.)
+effect.wither_sword.text.6=-Special skills: 
+effect.wither_sword.text.7=  When attacking, it will drop wither skulls with a 10% chance.
+effect.wither_sword.text.8=  It will be immune to the wither effect.
+effect.wither_sword.text.9=  The leaves of the trees will wither, the flowers will turn into withered roses, the grass will turn to dirt.
+effect.wither_sword.text.10=  Right clicking or pressing the screen will launch a dangerous wither skull. (Sword durability: -3)
+effect.wither_sword.text.11=-Description:
+effect.wither_sword.text.12=  This sword emits light.
+effect.wither_sword.text.13=  By having the sword you will see a life bar on your screen with the name "Wither Sword" this is only decoration.
+effect.wither_sword.text.14=  You will have the effect of wither but it will not hurt you.
+effect.wither_sword.text.15=-How to create or get it:
+effect.wither_sword.text.16=  You will have to kill the wither with a "Nether star sword" and it will drop it with a 13% chance.
+
+howtoplay.time_sword.title=§lSwords
+howtoplay.time_sword=§lTime Sword
+time_sword.header.title=§lTime Sword                                                                    
+effect.time_sword.text.0=-Durability: 13770
+effect.time_sword.text.1=-Damage: 13
+effect.time_sword.text.2=-Enchantable: false
+effect.time_sword.text.3=-Repairable: false
+effect.time_sword.text.4=-Special skills: 
+effect.time_sword.text.5=  Time will advance faster, you and all entities will be able to move much faster, and the plants will grow much faster.
+effect.time_sword.text.6=-Description:
+effect.time_sword.text.7=  When attacking, the durability points of the sword could lose 1 point with a probability of 90%, 16 points with a probability of 6%, 32 points with a probability of 3% and 64 points with a probability of 1%.
+effect.time_sword.text.8=  This sword emits light.
+effect.time_sword.text.9=-How to create or get it:
+effect.time_sword.text.10=You must throw clock swords into the water of the well structure that is in the desert, this well will serve as a source of wishes and will give you the sword with a 2.5% chance.
+
+howtoplay.ultra_instinct_sword.title=§lSwords
+howtoplay.ultra_instinct_sword=§lUltra Instinct Sword
+ultra_instinct_sword.header.title=§lUltra Instinct Sword                                                                    
+effect.ultra_instinct_sword.text.0=-Durability: 9999
+effect.ultra_instinct_sword.text.1=-Damage: 16
+effect.ultra_instinct_sword.text.3=-Should Despawn Item: false
+effect.ultra_instinct_sword.text.4=-Enchantable: false
+effect.ultra_instinct_sword.text.5=-Repairable: false
+effect.ultra_instinct_sword.text.6=-Special skills: 
+effect.ultra_instinct_sword.text.7=  Melee attack, projectiles, fire, and explosions cannot harm you. (You can dodge the melee attack and the projectiles automatically)
+effect.ultra_instinct_sword.text.8=  Right clicking or pressing the screen will fire a powerful projectile capable of destroying everything in its path and the bedrock will not be a problem. (This ability recharges every 61 seconds) (Sword durability: -48) (The Ultra Instinct projectile can cause a lot of lag for a few seconds.)
+effect.ultra_instinct_sword.text.9=-How to create or get it:
+effect.ultra_instinct_sword.text.10=  You must throw quartz diamonds or quartz diamond blocks (new ore) into the water of the well structure that is in the desert, this well will serve as a source of wishes and will give you the sword with a 0.8% chance when throwing quartz diamonds or 2.5% chance with the quartz diamond block.
+effect.ultra_instinct_sword.text.11=  (Quartz diamond ores are spawned below height 15 in small quantities and are rare to find)
```

### `Swords_R/textures/item_texture.json`

```diff
--- 1.6/Sword_R/textures/item_texture.json
+++ 2.8.14/Swords_R/textures/item_texture.json
@@ -1,5 +1,5 @@
 {
-  "resource_pack_name": "vanilla",
+  "resource_pack_name": "swords",
   "texture_name": "atlas.items",
   "texture_data": {
     "blaze_sword": {
@@ -38,8 +38,8 @@
      "glowstone_sword": {
      "textures": "textures/items/glowstone_sword"
      },
-     "sword_of_time": {
-     "textures": "textures/items/Sword_of_Time"
+     "time_sword": {
+     "textures": "textures/items/time_sword"
      },
      "creeper_sword": {
      "textures": "textures/items/creeper_sword"
@@ -79,6 +79,55 @@
      },
      "quartz_sword": {
      "textures": "textures/items/quartz_sword"
+    },
+    "wither_skeleton_sword": {
+     "textures": "textures/items/wither_skeleton_sword"
+    },
+    "ultra_instinct_sword": {
+     "textures": "textures/items/ultra_instinct_sword"
+    },
+    "wolf_sword": {
+     "textures": "textures/items/wolf_sword"
+    },
+    "wet_sponge_sword": {
+     "textures": "textures/items/wet_sponge_sword"
+    },
+    "glass_sword": {
+     "textures": "textures/items/glass_sword"
+    },
+    "silver_sword": {
+     "textures": "textures/items/silver_sword"
+    },
+    "nether_star_sword": {
+     "textures": "textures/items/nether_star_sword"
+    },
+    "bedrock_sword": {
+     "textures": "textures/items/bedrock_sword"
+    },
+    "ghost_sword": {
+     "textures": "textures/items/ghost_sword"
+    },
+    "clock_sword": {
+     "textures": "textures/items/clock_sword"
+    },
+    "bee_sword": {
+     "textures": "textures/items/bee_sword"
+    },
+    "cursed_pumpkin_sword": {
+     "textures": "textures/items/cursed_pumpkin_sword"
+    },
+    //Materiales
+    "bedrock_stick": {
+     "textures": "textures/items/bedrock_stick"
+    },
+    "silver_ingot": {
+     "textures": "textures/items/silver_ingot"
+    },
+    "quartz_diamond": {
+     "textures": "textures/items/quartz_diamond"
+    },
+    "quartz_diamond_stick": {
+     "textures": "textures/items/quartz_diamond_stick"
     }
   }
 }
```
