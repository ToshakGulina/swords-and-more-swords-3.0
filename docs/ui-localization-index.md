# Встроенная справка 2.x: поля текста и локализация

Источник UI: `Swords_R/ui/how_to_play_screen.json` (файл побайтово одинаков в 2.8.8 и 2.8.14); источник строк — `Swords_R/texts/en_US.lang` каждого архива. В 1.6 такого локального UI-файла нет. Разбор следует порядку полей JSON и списков, а не предполагаемому порядку отрисовки. Здесь сохранены все прямые строковые поля `$text`, без вычисления наследования, видимости, управления или шаблонов Bedrock.

Всего 490 полей `$text`, 490 различных ссылок, 9 ссылок без точного ключа в локальном en_US 2.8.14. Из 40 секций 36 точно соответствуют ID предмета по имени; локального одноимённого раздела для остальных 6 ID нет: `effect:bedrock_stick`, `effect:cursed_pumpkin_sword`, `effect:quartz_diamond`, `effect:quartz_diamond_stick`, `effect:silver_ingot`, `effect:wet_sponge_sword`. Отсутствие раздела или строки в пакете не доказывает отсутствия fallback, фактической видимости либо иной локализации.

Значения приведены без изменения как JSON-строки: пробелы внутри кавычек, коды `§` и английский текст сохранены. Числа и обещания справки — заявления автора, а не подтверждение кода или поведения. Если ключ повторяется, перечислены все исходные строки; приоритет повторов и fallback не определяются. [Полные исходные строки en_US всех версий](localization-source-index.md); [сверка чисел UI с компонентами](ui-stat-comparison.md) · [сравнение скриншотов с компонентами](screenshot-stat-comparison.md).

Пять ID без одноимённой секции всё же названы во вложенных заголовках: Wet Sponge Sword — в `sponge_sword_section`, четыре материала — в `blocks_and_items_section`. В секции Sponge под заголовком Wet Sponge заявлены прочность 64 и damage 3; локализованные строки `effect.sponge_sword.text.14` и `.15` присутствуют в en_US, но ни одно прямое `$text` поля UI не ссылается на них.

Справка сама даёт два разных описания глубины серебряной руды: `effect.blocks_and_items.text_2` — ниже 35, `effect.silver_sword.text.7` — ниже 15. В 2.8.8 декларирован gaussian extent `[10,35]`, а в 2.8.14 локальных правил генерации этих руд нет; см. [анализ генерации](manual-version-2.8.8.md). Это разные типы данных, и утверждения UI не доказывают границы реальной генерации.

## Локально отсутствующие ключи en_US

| Путь поля UI | Ключ |
|---|---|
| `"$.obsidian_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.obsidian_sword.text.2"` |
| `"$.nether_star_sword_section@how_to_play_common.main_sections.controls[5].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.nether_star_sword.text.1"` |
| `"$.ice_sword_section@how_to_play_common.main_sections.controls[11].paragraph_8@how_to_play_common.paragraph.$text"` | `"effect.ice_sword.text.8"` |
| `"$.ghost_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.ghost_sword.text.2"` |
| `"$.creeper_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.creeper_sword.text.2"` |
| `"$.spectral_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.spectral_sword.text.2"` |
| `"$.bedrock_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.bedrock_sword.text.2"` |
| `"$.wither_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.wither_sword.text.2"` |
| `"$.ultra_instinct_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.ultra_instinct_sword.text.2"` |

## Полный порядок прямых полей $text

### basic_information_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.basic_information_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"basic_information.header.title"` | стр. 70: `"§l§6About                                                                                           "` |
| `"$.basic_information_section@how_to_play_common.main_sections.controls[2].paragraph_text_0@how_to_play_common.paragraph.$text"` | `"effect.basic_information.text_0"` | стр. 123: `"§c• Activate the option \"Holiday Creator Features\" and \"Creation of Custom Biomes\" for the correct functioning of the Add-On. "` |
| `"$.basic_information_section@how_to_play_common.main_sections.controls[3].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.basic_information.text_1"` | стр. 124: `"§c• If the add-on doesn't work properly, restart Minecraft and reactivate the packs "` |
| `"$.basic_information_section@how_to_play_common.main_sections.controls[4].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.basic_information.text_2"` | стр. 125: `" "` |
| `"$.basic_information_section@how_to_play_common.main_sections.controls[5].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.basic_information.text_3"` | стр. 126: `"§6• A pack of 39 swords with special powers."` |
| `"$.basic_information_section@how_to_play_common.main_sections.controls[6].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.basic_information.text_4"` | стр. 127: `"• Use the command \"/function give\" to get all the swords."` |
| `"$.basic_information_section@how_to_play_common.main_sections.controls[7].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.basic_information.text_5"` | стр. 128: `"• Swords can be found in the Creative Inventory under the Swords tab."` |
| `"$.basic_information_section@how_to_play_common.main_sections.controls[8].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.basic_information.text_6"` | стр. 129: `" "` |
| `"$.basic_information_section@how_to_play_common.main_sections.controls[9].paragraph_7@how_to_play_common.paragraph.$text"` | `"effect.basic_information.text_7"` | стр. 130: `"§c- Report error to my Twitter §l§b@Effectoo"` |
| `"$.basic_information_section@how_to_play_common.main_sections.controls[10].paragraph_8@how_to_play_common.paragraph.$text"` | `"effect.basic_information.text_8"` | стр. 131: `"§c- Any suggestions to add in the addon are welcome as long as you send them to me on my Twitter."` |
| `"$.basic_information_section@how_to_play_common.main_sections.controls[11].paragraph_9@how_to_play_common.paragraph.$text"` | `"effect.basic_information.text_9"` | стр. 132: `" "` |
| `"$.basic_information_section@how_to_play_common.main_sections.controls[12].header_1@how_to_play_common.header.$text"` | `"basic_information.header.title_1"` | стр. 133: `"  §lCreated by Effect99"` |

### updates_changelog_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.updates_changelog_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"updates_changelog.header.title"` | 2.8.8: стр. 69: `"§l§6Changelog §r§fV2.8.8                                                                                     "`<br>2.8.14: стр. 69: `"§l§6Changelog §r§fV2.8.9                                                                                     "` |
| `"$.updates_changelog_section@how_to_play_common.main_sections.controls[2].paragraph_text_0@how_to_play_common.paragraph.$text"` | `"effect.updates_changelog.text_0"` | 2.8.8: стр. 85: `"• Updated for minecraft 1.20.50+"`<br>2.8.14: стр. 85: `"• Small changes"` |
| `"$.updates_changelog_section@how_to_play_common.main_sections.controls[3].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.updates_changelog.text_1"` | стр. 86: `"• Bug fixes"` |
| `"$.updates_changelog_section@how_to_play_common.main_sections.controls[4].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.updates_changelog.text_2"` | 2.8.8: стр. 87: `"• Small changes"`<br>2.8.14: стр. 87: `"§r"` |
| `"$.updates_changelog_section@how_to_play_common.main_sections.controls[5].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.updates_changelog.text_3"` | стр. 88: `"§r"` |
| `"$.updates_changelog_section@how_to_play_common.main_sections.controls[6].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.updates_changelog.text_4"` | стр. 89: `"§r "` |
| `"$.updates_changelog_section@how_to_play_common.main_sections.controls[7].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.updates_changelog.text_5"` | стр. 90: `"§r"` |
| `"$.updates_changelog_section@how_to_play_common.main_sections.controls[8].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.updates_changelog.text_6"` | стр. 91: `"§r"` |

### blocks_and_items_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.blocks_and_items_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"blocks_and_items.header.title"` | стр. 81: `"§l§6Blocks, Items and more                                                                               "` |
| `"$.blocks_and_items_section@how_to_play_common.main_sections.controls[2].header_1@how_to_play_common.header.$text"` | `"blocks_and_items.header.title_1"` | стр. 93: `"§lQuartz diamond ore                                                                            "` |
| `"$.blocks_and_items_section@how_to_play_common.main_sections.controls[4].paragraph_text_0@how_to_play_common.paragraph.$text"` | `"effect.blocks_and_items.text_0"` | стр. 94: `" Spawns below height 16 (Rare) (will deal damage when sting if you're too close).  You will also find them in the lower layers of The End dimension."` |
| `"$.blocks_and_items_section@how_to_play_common.main_sections.controls[5].header_2@how_to_play_common.header.$text"` | `"blocks_and_items.header.title_2"` | стр. 95: `"§lQuartz diamond                                                                            "` |
| `"$.blocks_and_items_section@how_to_play_common.main_sections.controls[7].header_7@how_to_play_common.header.$text"` | `"blocks_and_items.header.title_7"` | стр. 97: `"§lQuartz diamond block                                                                            "` |
| `"$.blocks_and_items_section@how_to_play_common.main_sections.controls[9].header_3@how_to_play_common.header.$text"` | `"blocks_and_items.header.title_3"` | стр. 96: `"§lQuartz diamond stick                                                                            "` |
| `"$.blocks_and_items_section@how_to_play_common.main_sections.controls[11].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.blocks_and_items.text_1"` | стр. 98: `" Durability: 20, Damage: 24, (Causes you damage when you attack entities) (It is crafted like a common stick)"` |
| `"$.blocks_and_items_section@how_to_play_common.main_sections.controls[12].header_4@how_to_play_common.header.$text"` | `"blocks_and_items.header.title_4"` | стр. 99: `"§lSilver ore                                                                            "` |
| `"$.blocks_and_items_section@how_to_play_common.main_sections.controls[14].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.blocks_and_items.text_2"` | стр. 100: `" Spawns below height 35 (common) (Place in the oven to get silver ingot)"` |
| `"$.blocks_and_items_section@how_to_play_common.main_sections.controls[15].header_5@how_to_play_common.header.$text"` | `"blocks_and_items.header.title_5"` | стр. 101: `"§lSilver ingot                                                                            "` |
| `"$.blocks_and_items_section@how_to_play_common.main_sections.controls[17].header_6@how_to_play_common.header.$text"` | `"blocks_and_items.header.title_6"` | стр. 102: `"§lBedrock stick                                                                            "` |
| `"$.blocks_and_items_section@how_to_play_common.main_sections.controls[19].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.blocks_and_items.text_3"` | стр. 103: `" Durability: Unbreakable, Damage: 6 (It is crafted like a common stick)"` |
| `"$.blocks_and_items_section@how_to_play_common.main_sections.controls[20].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.blocks_and_items.text_4"` | стр. 104: `" "` |
| `"$.blocks_and_items_section@how_to_play_common.main_sections.controls[21].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.blocks_and_items.text_5"` | стр. 105: `" "` |
| `"$.blocks_and_items_section@how_to_play_common.main_sections.controls[22].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.blocks_and_items.text_6"` | стр. 106: `" "` |

### sword_mobs_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.sword_mobs_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"sword_mobs.header.title"` | стр. 83: `"§l§6Mobs                                                                                                      "` |
| `"$.sword_mobs_section@how_to_play_common.main_sections.controls[2].header_1@how_to_play_common.header.$text"` | `"sword_mobs.header.title.1"` | стр. 108: `"§lGhost                                                                                                      "` |
| `"$.sword_mobs_section@how_to_play_common.main_sections.controls[4].paragraph_text_0@how_to_play_common.paragraph.$text"` | `"effect.sword_mobs.text_0"` | стр. 109: `"They will appear at night, these entities are not dangerous, they will not try to attack you and you will not be able to attack them either, but if you touch them as if you want to hurt them, the entity will drop the ghost sword with a probability of 0.3% so it can take you a while to get it. There will also be a 1% chance that the entity will randomly teleport so it can escape from you. This entity is also sensitive to light, so if it gets too close to the light, it will disappear. This entity only appears on grass or stone blocks. -Attack damage: Unknown Health: Unknown"` |
| `"$.sword_mobs_section@how_to_play_common.main_sections.controls[5].header_2@how_to_play_common.header.$text"` | `"sword_mobs.header.title.2"` | стр. 110: `"§lGrass Witch                                                                                                      "` |
| `"$.sword_mobs_section@how_to_play_common.main_sections.controls[7].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.sword_mobs.text_1"` | стр. 111: `"The grass witch will appear at night with little probability, when you try to attack it it will attack you with the same abilities as the grass sword, when you kill it it will drop the grass sword with a 20% chance. -Health: 32"` |
| `"$.sword_mobs_section@how_to_play_common.main_sections.controls[8].header_3@how_to_play_common.header.$text"` | `"sword_mobs.header.title.3"` | стр. 112: `"§lAlpha Wold                                                                                                      "` |
| `"$.sword_mobs_section@how_to_play_common.main_sections.controls[10].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.sword_mobs.text_2"` | стр. 113: `"These wolves spawn in the taiga biome only on a full moon and will be aggressive towards all animals and players, when you hear a distant howl it means one spawned nearby, the silver sword will be his weakness and he will drop the wolf sword with a 10% chance if you kill him with the silver sword. -Attack damage: 8 -Health: 480"` |
| `"$.sword_mobs_section@how_to_play_common.main_sections.controls[11].header_4@how_to_play_common.header.$text"` | `"sword_mobs.header.title.4"` | стр. 114: `"§lRed-eyed Enderman                                                                                                      "` |
| `"$.sword_mobs_section@how_to_play_common.main_sections.controls[13].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.sword_mobs.text_3"` | стр. 115: `"They will appear at night with low probability, they will be more aggressive and stronger than a normal Enderman. Killing him will drop the ender sword with a 2.5% chance. -Attack damage: 12 -Health: 120"` |
| `"$.sword_mobs_section@how_to_play_common.main_sections.controls[14].header_5@how_to_play_common.header.$text"` | `"sword_mobs.header.title.5"` | стр. 116: `"§lKing Slime                                                                                                      "` |
| `"$.sword_mobs_section@how_to_play_common.main_sections.controls[16].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.sword_mobs.text_4"` | стр. 117: `"The king slime appears in the swamp biome at night with a low probability, it will be very fast and aggressive with the player. Will drop the sword of slime with a 4% chance. -Attack damage: Unknown -Health: 300"` |
| `"$.sword_mobs_section@how_to_play_common.main_sections.controls[17].header_6@how_to_play_common.header.$text"` | `"sword_mobs.header.title.6"` | стр. 118: `"§lCentella                                                                                                      "` |
| `"$.sword_mobs_section@how_to_play_common.main_sections.controls[19].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.sword_mobs.text_5"` | стр. 119: `"Unknown entity, will appear when lightning strikes with a 20% chance. He will drop the lightning sword with a 2% chance. (It will be hard to kill since it has a lot of life, deals a lot of damage and will disappear in less than 60 seconds) (This entity is a reference to a strange real-life atmospheric phenomenon.) -Attack damage: Unknown -Health: 200"` |
| `"$.sword_mobs_section@how_to_play_common.main_sections.controls[20].header_7@how_to_play_common.header.$text"` | `"sword_mobs.header.title.7"` | стр. 120: `"§lSlime baby                                                                                                      "` |
| `"$.sword_mobs_section@how_to_play_common.main_sections.controls[22].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.sword_mobs.text_6"` | стр. 121: `"It appears when you have the slime sword in your hand, when you get off the slime it will try to attack all nearby enemies, you can ride the little slime again, but it will not obey you and will move in any direction, but it will increase its speed x3. -Attack damage: 1 -Health: Inmortal"` |

### coal_sword_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.coal_sword_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"coal_sword.header.title"` | стр. 137: `"§lCoal Sword                                                                    "` |
| `"$.coal_sword_section@how_to_play_common.main_sections.controls[3].paragraph_0@how_to_play_common.paragraph.$text"` | `"effect.coal_sword.text.0"` | стр. 138: `"-Durability: 121"` |
| `"$.coal_sword_section@how_to_play_common.main_sections.controls[4].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.coal_sword.text.1"` | стр. 139: `"-Damage: 4"` |
| `"$.coal_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.coal_sword.text.2"` | стр. 140: `"-Enchantable: true"` |
| `"$.coal_sword_section@how_to_play_common.main_sections.controls[6].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.coal_sword.text.3"` | стр. 141: `"-Repairable: true (With coal, sticks and the same sword.)"` |
| `"$.coal_sword_section@how_to_play_common.main_sections.controls[7].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.coal_sword.text.4"` | стр. 142: `"-Special skills: None (It only serves as fuel for the furnace.)"` |
| `"$.coal_sword_section@how_to_play_common.main_sections.controls[8].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.coal_sword.text.5"` | стр. 143: `"-How to create or get it:"` |
| `"$.coal_sword_section@how_to_play_common.main_sections.controls[9].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.coal_sword.text.6"` | стр. 144: `"  Two blocks of coal and a stick."` |

### silver_sword_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.silver_sword_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"silver_sword.header.title"` | стр. 148: `"§lSilver Sword                                                                    "` |
| `"$.silver_sword_section@how_to_play_common.main_sections.controls[3].paragraph_0@how_to_play_common.paragraph.$text"` | `"effect.silver_sword.text.0"` | стр. 149: `"-Durability: 1800"` |
| `"$.silver_sword_section@how_to_play_common.main_sections.controls[4].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.silver_sword.text.1"` | стр. 150: `"-Damage: 6"` |
| `"$.silver_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.silver_sword.text.2"` | стр. 151: `"-Enchantable: true"` |
| `"$.silver_sword_section@how_to_play_common.main_sections.controls[6].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.silver_sword.text.3"` | стр. 152: `"-Repairable: true (Only with the same sword.)"` |
| `"$.silver_sword_section@how_to_play_common.main_sections.controls[7].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.silver_sword.text.4"` | стр. 153: `"-Special skills: "` |
| `"$.silver_sword_section@how_to_play_common.main_sections.controls[8].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.silver_sword.text.5"` | стр. 154: `"  Causes more damage than normal to \"alpha wolves\""` |
| `"$.silver_sword_section@how_to_play_common.main_sections.controls[9].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.silver_sword.text.6"` | стр. 155: `"-How to create or get it:"` |
| `"$.silver_sword_section@how_to_play_common.main_sections.controls[10].paragraph_7@how_to_play_common.paragraph.$text"` | `"effect.silver_sword.text.7"` | стр. 156: `"  You must find the silver ore in the depths of the overworld (normal world) below height 15 and place it in the oven to obtain the silver ingot and be able to create the sword."` |

### lapis_sword_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.lapis_sword_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"lapis_sword.header.title"` | стр. 160: `"§lLapis Sword                                                                    "` |
| `"$.lapis_sword_section@how_to_play_common.main_sections.controls[3].paragraph_0@how_to_play_common.paragraph.$text"` | `"effect.lapis_sword.text.0"` | стр. 161: `"-Durability: 528"` |
| `"$.lapis_sword_section@how_to_play_common.main_sections.controls[4].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.lapis_sword.text.1"` | стр. 162: `"-Damage: 5"` |
| `"$.lapis_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.lapis_sword.text.2"` | стр. 163: `"-Enchantable: true"` |
| `"$.lapis_sword_section@how_to_play_common.main_sections.controls[6].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.lapis_sword.text.3"` | стр. 164: `"-Repairable: true (With lapis lazuli and the same sword.)"` |
| `"$.lapis_sword_section@how_to_play_common.main_sections.controls[7].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.lapis_sword.text.4"` | стр. 165: `"-Special skills: "` |
| `"$.lapis_sword_section@how_to_play_common.main_sections.controls[8].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.lapis_sword.text.5"` | стр. 166: `"  You will be given 5 experience points in a random period of between 2.5 and 6 seconds."` |
| `"$.lapis_sword_section@how_to_play_common.main_sections.controls[9].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.lapis_sword.text.6"` | стр. 167: `"-How to create or get it:"` |
| `"$.lapis_sword_section@how_to_play_common.main_sections.controls[10].paragraph_7@how_to_play_common.paragraph.$text"` | `"effect.lapis_sword.text.7"` | стр. 168: `"  Found in the chests of: Stronghold and Pillager Outpost."` |

### glowstone_sword_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.glowstone_sword_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"glowstone_sword.header.title"` | стр. 172: `"§lGlowstone Sword                                                                    "` |
| `"$.glowstone_sword_section@how_to_play_common.main_sections.controls[3].paragraph_0@how_to_play_common.paragraph.$text"` | `"effect.glowstone_sword.text.0"` | стр. 173: `"-Durability: 128"` |
| `"$.glowstone_sword_section@how_to_play_common.main_sections.controls[4].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.glowstone_sword.text.1"` | стр. 174: `"-Damage: 4"` |
| `"$.glowstone_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.glowstone_sword.text.2"` | стр. 175: `"-Enchantable: true"` |
| `"$.glowstone_sword_section@how_to_play_common.main_sections.controls[6].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.glowstone_sword.text.3"` | стр. 176: `"-Repairable: true (By glowstone, glowstone dust and the same sword.)"` |
| `"$.glowstone_sword_section@how_to_play_common.main_sections.controls[7].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.glowstone_sword.text.4"` | стр. 177: `"-Special skills: "` |
| `"$.glowstone_sword_section@how_to_play_common.main_sections.controls[8].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.glowstone_sword.text.5"` | стр. 178: `"  This sword emits a lot of light and can be placed in the left hand."` |
| `"$.glowstone_sword_section@how_to_play_common.main_sections.controls[9].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.glowstone_sword.text.6"` | стр. 179: `"-How to create or get it:"` |
| `"$.glowstone_sword_section@how_to_play_common.main_sections.controls[10].paragraph_7@how_to_play_common.paragraph.$text"` | `"effect.glowstone_sword.text.7"` | стр. 180: `"  Two glowstone blocks and a blaze rod"` |

### glass_sword_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.glass_sword_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"glass_sword.header.title"` | стр. 184: `"§lGlass Sword                                                                    "` |
| `"$.glass_sword_section@how_to_play_common.main_sections.controls[3].paragraph_0@how_to_play_common.paragraph.$text"` | `"effect.glass_sword.text.0"` | стр. 185: `"-Durability: 1"` |
| `"$.glass_sword_section@how_to_play_common.main_sections.controls[4].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.glass_sword.text.1"` | стр. 186: `"-Damage: 33"` |
| `"$.glass_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.glass_sword.text.2"` | стр. 187: `"-Enchantable: true"` |
| `"$.glass_sword_section@how_to_play_common.main_sections.controls[6].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.glass_sword.text.3"` | стр. 188: `"-Repairable: false "` |
| `"$.glass_sword_section@how_to_play_common.main_sections.controls[7].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.glass_sword.text.4"` | стр. 189: `"-Special skills: none"` |
| `"$.glass_sword_section@how_to_play_common.main_sections.controls[8].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.glass_sword.text.5"` | стр. 190: `"-How to create or get it:"` |
| `"$.glass_sword_section@how_to_play_common.main_sections.controls[9].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.glass_sword.text.6"` | стр. 191: `"  You will have to throw the fire sword into the water."` |

### jungle_sword_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.jungle_sword_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"jungle_sword.header.title"` | стр. 195: `"§lJungle Sword                                                                    "` |
| `"$.jungle_sword_section@how_to_play_common.main_sections.controls[3].paragraph_0@how_to_play_common.paragraph.$text"` | `"effect.jungle_sword.text.0"` | стр. 196: `"-Durability: 128"` |
| `"$.jungle_sword_section@how_to_play_common.main_sections.controls[4].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.jungle_sword.text.1"` | стр. 197: `"-Damage: 4"` |
| `"$.jungle_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.jungle_sword.text.2"` | стр. 198: `"-Enchantable: true"` |
| `"$.jungle_sword_section@how_to_play_common.main_sections.controls[6].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.jungle_sword.text.3"` | стр. 199: `"-Repairable: true (Only with the same sword.)"` |
| `"$.jungle_sword_section@how_to_play_common.main_sections.controls[7].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.jungle_sword.text.4"` | стр. 200: `"-Special skills: "` |
| `"$.jungle_sword_section@how_to_play_common.main_sections.controls[8].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.jungle_sword.text.5"` | стр. 201: `"  Your health will be reduced to 4 hearts, but an absorption potion effect will be added."` |
| `"$.jungle_sword_section@how_to_play_common.main_sections.controls[9].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.jungle_sword.text.6"` | стр. 202: `"  Vines will be placed in nearby blocks. (Blocks: logs, grass, dirt, sand, cobblestone, stone, obsidian, endstone, gravel, ice, planks, leaves, netherrack, and nether bricks.)"` |
| `"$.jungle_sword_section@how_to_play_common.main_sections.controls[10].paragraph_7@how_to_play_common.paragraph.$text"` | `"effect.jungle_sword.text.7"` | стр. 203: `"-How to create or get it:"` |
| `"$.jungle_sword_section@how_to_play_common.main_sections.controls[11].paragraph_8@how_to_play_common.paragraph.$text"` | `"effect.jungle_sword.text.8"` | стр. 204: `"  Fishing in the jungle biome or jungle temple."` |

### cactus_sword_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.cactus_sword_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"cactus_sword.header.title"` | стр. 208: `"§lCactus Sword                                                                    "` |
| `"$.cactus_sword_section@how_to_play_common.main_sections.controls[3].paragraph_0@how_to_play_common.paragraph.$text"` | `"effect.cactus_sword.text.0"` | стр. 209: `"-Durability: 125"` |
| `"$.cactus_sword_section@how_to_play_common.main_sections.controls[4].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.cactus_sword.text.1"` | стр. 210: `"-Damage: 6"` |
| `"$.cactus_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.cactus_sword.text.2"` | стр. 211: `"-Enchantable: true"` |
| `"$.cactus_sword_section@how_to_play_common.main_sections.controls[6].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.cactus_sword.text.3"` | стр. 212: `"-Repairable: true (Only with the same sword.)"` |
| `"$.cactus_sword_section@how_to_play_common.main_sections.controls[7].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.cactus_sword.text.4"` | стр. 213: `"-Special skills: "` |
| `"$.cactus_sword_section@how_to_play_common.main_sections.controls[8].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.cactus_sword.text.5"` | стр. 214: `"  You will receive damage when having the sword in hand, but you will also damage very close entities."` |
| `"$.cactus_sword_section@how_to_play_common.main_sections.controls[9].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.cactus_sword.text.6"` | стр. 215: `"-How to create or get it:"` |
| `"$.cactus_sword_section@how_to_play_common.main_sections.controls[10].paragraph_7@how_to_play_common.paragraph.$text"` | `"effect.cactus_sword.text.7"` | стр. 216: `"  A stick and two cacti"` |

### sponge_sword_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.sponge_sword_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"sponge_sword.header.title.0"` | стр. 220: `"§lSponge Sword                                                                    "` |
| `"$.sponge_sword_section@how_to_play_common.main_sections.controls[3].paragraph_0@how_to_play_common.paragraph.$text"` | `"effect.sponge_sword.text.0"` | стр. 221: `"-Durability: 128"` |
| `"$.sponge_sword_section@how_to_play_common.main_sections.controls[4].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.sponge_sword.text.1"` | стр. 222: `"-Damage: 5"` |
| `"$.sponge_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.sponge_sword.text.2"` | стр. 223: `"-Enchantable: true"` |
| `"$.sponge_sword_section@how_to_play_common.main_sections.controls[6].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.sponge_sword.text.3"` | стр. 224: `"-Repairable: true (By sponge and the same sword.)"` |
| `"$.sponge_sword_section@how_to_play_common.main_sections.controls[7].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.sponge_sword.text.4"` | стр. 225: `"-Special skills: "` |
| `"$.sponge_sword_section@how_to_play_common.main_sections.controls[8].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.sponge_sword.text.5"` | стр. 226: `"  It will absorb water in a radius of 2 blocks, after several seconds absorbing water the sword will transform into a \"wet sponge sword\"."` |
| `"$.sponge_sword_section@how_to_play_common.main_sections.controls[9].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.sponge_sword.text.6"` | стр. 227: `"-How to create or get it:"` |
| `"$.sponge_sword_section@how_to_play_common.main_sections.controls[10].paragraph_7@how_to_play_common.paragraph.$text"` | `"effect.sponge_sword.text.7"` | стр. 228: `"  On killing the elder guardian with a 6.5% chance."` |
| `"$.sponge_sword_section@how_to_play_common.main_sections.controls[11].paragraph_8@how_to_play_common.paragraph.$text"` | `"effect.sponge_sword.text.8"` | стр. 229: `"  When putting the wet sponge sword in the oven."` |
| `"$.sponge_sword_section@how_to_play_common.main_sections.controls[13].header_1@how_to_play_common.header.$text"` | `"sponge_sword.header.title.1"` | стр. 230: `"§lWet Sponge Sword                                                                    "` |
| `"$.sponge_sword_section@how_to_play_common.main_sections.controls[15].paragraph_9@how_to_play_common.paragraph.$text"` | `"effect.sponge_sword.text.9"` | стр. 231: `"-Durability: 64"` |
| `"$.sponge_sword_section@how_to_play_common.main_sections.controls[16].paragraph_10@how_to_play_common.paragraph.$text"` | `"effect.sponge_sword.text.10"` | стр. 232: `"-Damage: 3"` |
| `"$.sponge_sword_section@how_to_play_common.main_sections.controls[17].paragraph_11@how_to_play_common.paragraph.$text"` | `"effect.sponge_sword.text.11"` | стр. 233: `"-Enchantable: false"` |
| `"$.sponge_sword_section@how_to_play_common.main_sections.controls[18].paragraph_12@how_to_play_common.paragraph.$text"` | `"effect.sponge_sword.text.12"` | стр. 234: `"-Repairable: true (Sponges and more sponges.)"` |
| `"$.sponge_sword_section@how_to_play_common.main_sections.controls[19].paragraph_13@how_to_play_common.paragraph.$text"` | `"effect.sponge_sword.text.13"` | стр. 235: `"-Special skills: none"` |

### emerald_sword_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.emerald_sword_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"emerald_sword.header.title"` | стр. 241: `"§lEmerald Sword                                                                    "` |
| `"$.emerald_sword_section@how_to_play_common.main_sections.controls[3].paragraph_0@how_to_play_common.paragraph.$text"` | `"effect.emerald_sword.text.0"` | стр. 242: `"-Durability: 2300"` |
| `"$.emerald_sword_section@how_to_play_common.main_sections.controls[4].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.emerald_sword.text.1"` | стр. 243: `"-Damage: 7"` |
| `"$.emerald_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.emerald_sword.text.2"` | стр. 244: `"-Enchantable: true"` |
| `"$.emerald_sword_section@how_to_play_common.main_sections.controls[6].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.emerald_sword.text.3"` | стр. 245: `"-Repairable: true (Only with the same sword.)"` |
| `"$.emerald_sword_section@how_to_play_common.main_sections.controls[7].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.emerald_sword.text.4"` | стр. 246: `"-Special skills: "` |
| `"$.emerald_sword_section@how_to_play_common.main_sections.controls[8].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.emerald_sword.text.5"` | стр. 247: `"  You'll get a village hero potion effect for being inside a village and it will give villagers a resistance effect within 64 radius."` |
| `"$.emerald_sword_section@how_to_play_common.main_sections.controls[9].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.emerald_sword.text.6"` | стр. 248: `"-How to create or get it:"` |
| `"$.emerald_sword_section@how_to_play_common.main_sections.controls[10].paragraph_7@how_to_play_common.paragraph.$text"` | `"effect.emerald_sword.text.7"` | стр. 249: `"  Found in the chests of: Stronghold, Woodland Mansion, and Pillager Outpost."` |

### bone_sword_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.bone_sword_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"bone_sword.header.title"` | стр. 253: `"§lSkeleton bone Sword                                                                  "` |
| `"$.bone_sword_section@how_to_play_common.main_sections.controls[3].paragraph_0@how_to_play_common.paragraph.$text"` | `"effect.bone_sword.text.0"` | стр. 254: `"-Durability: 820"` |
| `"$.bone_sword_section@how_to_play_common.main_sections.controls[4].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.bone_sword.text.1"` | стр. 255: `"-Damage: 5"` |
| `"$.bone_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.bone_sword.text.2"` | стр. 256: `"-Enchantable: true"` |
| `"$.bone_sword_section@how_to_play_common.main_sections.controls[6].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.bone_sword.text.3"` | стр. 257: `"-Repairable: true (Everything that is made of: bone.)"` |
| `"$.bone_sword_section@how_to_play_common.main_sections.controls[7].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.bone_sword.text.4"` | стр. 258: `"-Special skills: "` |
| `"$.bone_sword_section@how_to_play_common.main_sections.controls[8].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.bone_sword.text.5"` | стр. 259: `"  When attacking you will throw arrows with a 20% chance."` |
| `"$.bone_sword_section@how_to_play_common.main_sections.controls[9].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.bone_sword.text.6"` | стр. 260: `"  Crops will grow much faster within a 2 block radius."` |
| `"$.bone_sword_section@how_to_play_common.main_sections.controls[10].paragraph_7@how_to_play_common.paragraph.$text"` | `"effect.bone_sword.text.7"` | стр. 261: `"  Enemy arrows within 8 radius will slow down."` |
| `"$.bone_sword_section@how_to_play_common.main_sections.controls[11].paragraph_8@how_to_play_common.paragraph.$text"` | `"effect.bone_sword.text.8"` | стр. 262: `"-How to create or get it:"` |
| `"$.bone_sword_section@how_to_play_common.main_sections.controls[12].paragraph_9@how_to_play_common.paragraph.$text"` | `"effect.bone_sword.text.9"` | стр. 263: `"  Killing skeletons at night in the desert biome with a 0.7% chance."` |

### wither_skeleton_sword_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.wither_skeleton_sword_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"wither_skeleton_sword.header.title"` | стр. 267: `"§lWither Skeleton Sword                                                                    "` |
| `"$.wither_skeleton_sword_section@how_to_play_common.main_sections.controls[3].paragraph_0@how_to_play_common.paragraph.$text"` | `"effect.wither_skeleton_sword.text.0"` | стр. 268: `"-Durability: 128"` |
| `"$.wither_skeleton_sword_section@how_to_play_common.main_sections.controls[4].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.wither_skeleton_sword.text.1"` | стр. 269: `"-Damage: 4"` |
| `"$.wither_skeleton_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.wither_skeleton_sword.text.2"` | стр. 270: `"-Enchantable: true"` |
| `"$.wither_skeleton_sword_section@how_to_play_common.main_sections.controls[6].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.wither_skeleton_sword.text.3"` | стр. 271: `"-Repairable: true (Coal, sticks and the same sword)"` |
| `"$.wither_skeleton_sword_section@how_to_play_common.main_sections.controls[7].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.wither_skeleton_sword.text.4"` | стр. 272: `"-Special skills: "` |
| `"$.wither_skeleton_sword_section@how_to_play_common.main_sections.controls[8].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.wither_skeleton_sword.text.5"` | стр. 273: `"  Will give wither effect to the entities you attack"` |
| `"$.wither_skeleton_sword_section@how_to_play_common.main_sections.controls[9].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.wither_skeleton_sword.text.6"` | стр. 274: `"-How to create or get it:"` |
| `"$.wither_skeleton_sword_section@how_to_play_common.main_sections.controls[10].paragraph_7@how_to_play_common.paragraph.$text"` | `"effect.wither_skeleton_sword.text.7"` | стр. 275: `"  When killing wither skeletons with a 2.5% chance"` |

### slime_sword_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.slime_sword_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"slime_sword.header.title"` | стр. 279: `"§lSlime Sword                                                                    "` |
| `"$.slime_sword_section@how_to_play_common.main_sections.controls[3].paragraph_0@how_to_play_common.paragraph.$text"` | `"effect.slime_sword.text.0"` | стр. 280: `"-Durability: 675"` |
| `"$.slime_sword_section@how_to_play_common.main_sections.controls[4].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.slime_sword.text.1"` | стр. 281: `"-Damage: 6"` |
| `"$.slime_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.slime_sword.text.2"` | стр. 282: `"-Enchantable: true"` |
| `"$.slime_sword_section@how_to_play_common.main_sections.controls[6].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.slime_sword.text.3"` | стр. 283: `"-Repairable: true (With slime and with the same sword.)"` |
| `"$.slime_sword_section@how_to_play_common.main_sections.controls[7].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.slime_sword.text.4"` | стр. 284: `"-Special skills: "` |
| `"$.slime_sword_section@how_to_play_common.main_sections.controls[8].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.slime_sword.text.5"` | стр. 285: `"  By having the sword in hand you will get a baby slime mount."` |
| `"$.slime_sword_section@how_to_play_common.main_sections.controls[9].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.slime_sword.text.6"` | стр. 286: `"  If you get off the slime mount, the slime will defend you from all nearby monsters. (The slime deals one point of damage and is immortal, plus it will teleport to its owner when it gets too far away.)"` |
| `"$.slime_sword_section@how_to_play_common.main_sections.controls[10].paragraph_7@how_to_play_common.paragraph.$text"` | `"effect.slime_sword.text.7"` | стр. 287: `"  Jumping with the slime mount and falling on an entity will damage it. (Jumping with the slime mount can be tricky.)"` |
| `"$.slime_sword_section@how_to_play_common.main_sections.controls[11].paragraph_8@how_to_play_common.paragraph.$text"` | `"effect.slime_sword.text.8"` | стр. 288: `"-How to create or get it:"` |
| `"$.slime_sword_section@how_to_play_common.main_sections.controls[12].paragraph_9@how_to_play_common.paragraph.$text"` | `"effect.slime_sword.text.9"` | стр. 289: `" Killing the slime king that appears at night in the swamp biome with a 4% chance."` |

### obsidian_sword_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.obsidian_sword_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"obsidian_sword.header.title"` | стр. 293: `"§lObsidian Sword                                                                    "` |
| `"$.obsidian_sword_section@how_to_play_common.main_sections.controls[3].paragraph_0@how_to_play_common.paragraph.$text"` | `"effect.obsidian_sword.text.0"` | стр. 294: `"-Durability: 3000"` |
| `"$.obsidian_sword_section@how_to_play_common.main_sections.controls[4].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.obsidian_sword.text.1"` | стр. 295: `"-Damage: 8"` |
| `"$.obsidian_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.obsidian_sword.text.2"` | **нет точного ключа** |
| `"$.obsidian_sword_section@how_to_play_common.main_sections.controls[6].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.obsidian_sword.text.3"` | стр. 296: `"-Enchantable: true "` |
| `"$.obsidian_sword_section@how_to_play_common.main_sections.controls[7].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.obsidian_sword.text.4"` | стр. 297: `"-Repairable: true (By obsidian and the same sword.)"` |
| `"$.obsidian_sword_section@how_to_play_common.main_sections.controls[8].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.obsidian_sword.text.5"` | стр. 298: `"-Special skills: "` |
| `"$.obsidian_sword_section@how_to_play_common.main_sections.controls[9].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.obsidian_sword.text.6"` | стр. 299: `"  You will be immune to explosions and you will have knockback resistance."` |
| `"$.obsidian_sword_section@how_to_play_common.main_sections.controls[10].paragraph_7@how_to_play_common.paragraph.$text"` | `"effect.obsidian_sword.text.7"` | стр. 300: `"-Description:"` |
| `"$.obsidian_sword_section@how_to_play_common.main_sections.controls[11].paragraph_8@how_to_play_common.paragraph.$text"` | `"effect.obsidian_sword.text.8"` | стр. 301: `"  When attacking, the durability points of the sword could lose 1 point with a probability of 55%, 2 points with a probability of 30% and 3 points with a probability of 15%."` |
| `"$.obsidian_sword_section@how_to_play_common.main_sections.controls[12].paragraph_9@how_to_play_common.paragraph.$text"` | `"effect.obsidian_sword.text.9"` | стр. 302: `"-How to create or get it:"` |
| `"$.obsidian_sword_section@how_to_play_common.main_sections.controls[13].paragraph_10@how_to_play_common.paragraph.$text"` | `"effect.obsidian_sword.text.10"` | стр. 303: `"  You must throw the fire sword into the rain and wait a few seconds."` |

### magma_sword_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.magma_sword_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"magma_sword.header.title"` | стр. 307: `"§lMagma Sword                                                                    "` |
| `"$.magma_sword_section@how_to_play_common.main_sections.controls[3].paragraph_0@how_to_play_common.paragraph.$text"` | `"effect.magma_sword.text.0"` | стр. 308: `"-Durability: 1316"` |
| `"$.magma_sword_section@how_to_play_common.main_sections.controls[4].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.magma_sword.text.1"` | стр. 309: `"-Damage: 7.2"` |
| `"$.magma_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.magma_sword.text.2"` | стр. 310: `"-Enchantable: true"` |
| `"$.magma_sword_section@how_to_play_common.main_sections.controls[6].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.magma_sword.text.3"` | стр. 311: `"-Repairable: true (By magma blocks and the same sword.)"` |
| `"$.magma_sword_section@how_to_play_common.main_sections.controls[7].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.magma_sword.text.4"` | стр. 312: `"-Special skills: "` |
| `"$.magma_sword_section@how_to_play_common.main_sections.controls[8].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.magma_sword.text.5"` | стр. 313: `"  Magma blocks won't hurt you."` |
| `"$.magma_sword_section@how_to_play_common.main_sections.controls[9].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.magma_sword.text.6"` | стр. 314: `"  Fire will only hurt you if you are standing on it."` |
| `"$.magma_sword_section@how_to_play_common.main_sections.controls[10].paragraph_7@how_to_play_common.paragraph.$text"` | `"effect.magma_sword.text.7"` | стр. 315: `"  The lava under your feet will turn into magma blocks."` |
| `"$.magma_sword_section@how_to_play_common.main_sections.controls[11].paragraph_8@how_to_play_common.paragraph.$text"` | `"effect.magma_sword.text.8"` | стр. 316: `"-How to create or get it:"` |
| `"$.magma_sword_section@how_to_play_common.main_sections.controls[12].paragraph_9@how_to_play_common.paragraph.$text"` | `"effect.magma_sword.text.9"` | стр. 317: `"  In chests of great underwater ruins."` |

### clock_sword_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.clock_sword_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"clock_sword.header.title"` | стр. 321: `"§lClock Sword                                                                    "` |
| `"$.clock_sword_section@how_to_play_common.main_sections.controls[3].paragraph_0@how_to_play_common.paragraph.$text"` | `"effect.clock_sword.text.0"` | стр. 322: `"-Durability: 4800"` |
| `"$.clock_sword_section@how_to_play_common.main_sections.controls[4].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.clock_sword.text.1"` | стр. 323: `"-Damage: 7"` |
| `"$.clock_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.clock_sword.text.2"` | стр. 324: `"-Enchantable: true"` |
| `"$.clock_sword_section@how_to_play_common.main_sections.controls[6].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.clock_sword.text.3"` | стр. 325: `"-Repairable: true (= Creation materials.)"` |
| `"$.clock_sword_section@how_to_play_common.main_sections.controls[7].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.clock_sword.text.4"` | стр. 326: `"-Special skills: "` |
| `"$.clock_sword_section@how_to_play_common.main_sections.controls[8].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.clock_sword.text.5"` | стр. 327: `"  Right-clicking or pressing the screen will advance one hour (1000 ticks) into the game. (The game will go 10 times faster for 5 seconds)"` |
| `"$.clock_sword_section@how_to_play_common.main_sections.controls[9].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.clock_sword.text.6"` | стр. 328: `"-How to create or get it:"` |

### grass_sword_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.grass_sword_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"grass_sword.header.title"` | стр. 332: `"§lGrass Sword                                                                    "` |
| `"$.grass_sword_section@how_to_play_common.main_sections.controls[3].paragraph_0@how_to_play_common.paragraph.$text"` | `"effect.grass_sword.text.0"` | стр. 333: `"-Durability: 250"` |
| `"$.grass_sword_section@how_to_play_common.main_sections.controls[4].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.grass_sword.text.1"` | стр. 334: `"-Damage: 8"` |
| `"$.grass_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.grass_sword.text.2"` | стр. 335: `"-Enchantable: true"` |
| `"$.grass_sword_section@how_to_play_common.main_sections.controls[6].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.grass_sword.text.3"` | стр. 336: `"-Repairable: true (Only with the same sword.)"` |
| `"$.grass_sword_section@how_to_play_common.main_sections.controls[7].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.grass_sword.text.4"` | стр. 337: `"-Special skills: "` |
| `"$.grass_sword_section@how_to_play_common.main_sections.controls[8].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.grass_sword.text.5"` | стр. 338: `"  All nearby entities within a radius of 8 will be attacked by a strange grass entity that will bury them a bit underground or completely depending on the size of the entity."` |
| `"$.grass_sword_section@how_to_play_common.main_sections.controls[9].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.grass_sword.text.6"` | стр. 339: `"  The dirt blocks will turn into grass."` |
| `"$.grass_sword_section@how_to_play_common.main_sections.controls[10].paragraph_7@how_to_play_common.paragraph.$text"` | `"effect.grass_sword.text.7"` | стр. 340: `"-How to create or get it:"` |
| `"$.grass_sword_section@how_to_play_common.main_sections.controls[11].paragraph_8@how_to_play_common.paragraph.$text"` | `"effect.grass_sword.text.8"` | стр. 341: `"  You will have to kill a grass witch, these appear at night with a low probability and will drop the sword with a 20% probability."` |
| `"$.grass_sword_section@how_to_play_common.main_sections.controls[12].paragraph_9@how_to_play_common.paragraph.$text"` | `"effect.grass_sword.text.9"` | стр. 342: `" "` |

### sea_sword_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.sea_sword_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"sea_sword.header.title"` | стр. 346: `"§lSea Sword                                                                    "` |
| `"$.sea_sword_section@how_to_play_common.main_sections.controls[3].paragraph_0@how_to_play_common.paragraph.$text"` | `"effect.sea_sword.text.0"` | стр. 347: `"-Durability: 1356"` |
| `"$.sea_sword_section@how_to_play_common.main_sections.controls[4].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.sea_sword.text.1"` | стр. 348: `"-Damage: 7"` |
| `"$.sea_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.sea_sword.text.2"` | стр. 349: `"-Enchantable: true"` |
| `"$.sea_sword_section@how_to_play_common.main_sections.controls[6].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.sea_sword.text.3"` | стр. 350: `"-Repairable: true (By heart of the sea and the same sword.)"` |
| `"$.sea_sword_section@how_to_play_common.main_sections.controls[7].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.sea_sword.text.4"` | стр. 351: `"-Special skills: "` |
| `"$.sea_sword_section@how_to_play_common.main_sections.controls[8].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.sea_sword.text.5"` | стр. 352: `" You can swim as fast as dolphins."` |
| `"$.sea_sword_section@how_to_play_common.main_sections.controls[9].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.sea_sword.text.6"` | стр. 353: `" You will become a mermaid."` |
| `"$.sea_sword_section@how_to_play_common.main_sections.controls[10].paragraph_7@how_to_play_common.paragraph.$text"` | `"effect.sea_sword.text.7"` | стр. 354: `"  You can breathe underwater but you cannot breathe air."` |
| `"$.sea_sword_section@how_to_play_common.main_sections.controls[11].paragraph_8@how_to_play_common.paragraph.$text"` | `"effect.sea_sword.text.8"` | стр. 355: `"-Description:"` |
| `"$.sea_sword_section@how_to_play_common.main_sections.controls[12].paragraph_9@how_to_play_common.paragraph.$text"` | `"effect.sea_sword.text.9"` | стр. 356: `"  You will jump like a fish when you are out of the water."` |
| `"$.sea_sword_section@how_to_play_common.main_sections.controls[13].paragraph_10@how_to_play_common.paragraph.$text"` | `"effect.sea_sword.text.10"` | стр. 357: `"-How to create or get it:"` |
| `"$.sea_sword_section@how_to_play_common.main_sections.controls[14].paragraph_11@how_to_play_common.paragraph.$text"` | `"effect.sea_sword.text.11"` | стр. 358: `"  In treasure chests."` |

### blaze_sword_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.blaze_sword_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"blaze_sword.header.title"` | стр. 362: `"§lBlaze Sword                                                                    "` |
| `"$.blaze_sword_section@how_to_play_common.main_sections.controls[3].paragraph_0@how_to_play_common.paragraph.$text"` | `"effect.blaze_sword.text.0"` | стр. 363: `"-Durability: 2300"` |
| `"$.blaze_sword_section@how_to_play_common.main_sections.controls[4].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.blaze_sword.text.1"` | стр. 364: `"-Damage: 6"` |
| `"$.blaze_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.blaze_sword.text.2"` | стр. 365: `"-Enchantable: true"` |
| `"$.blaze_sword_section@how_to_play_common.main_sections.controls[6].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.blaze_sword.text.3"` | стр. 366: `"-Repairable: true (Only with the same sword.)"` |
| `"$.blaze_sword_section@how_to_play_common.main_sections.controls[7].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.blaze_sword.text.4"` | стр. 367: `"-Special skills: "` |
| `"$.blaze_sword_section@how_to_play_common.main_sections.controls[8].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.blaze_sword.text.5"` | стр. 368: `"  By right-clicking or pressing the screen, your body will levitate for a few seconds and then launch several small fireballs in the direction you are looking."` |
| `"$.blaze_sword_section@how_to_play_common.main_sections.controls[9].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.blaze_sword.text.6"` | стр. 369: `"  The fire won't hurt you."` |
| `"$.blaze_sword_section@how_to_play_common.main_sections.controls[10].paragraph_7@how_to_play_common.paragraph.$text"` | `"effect.blaze_sword.text.7"` | стр. 370: `"  Sometimes you will throw fireballs when hitting entities."` |
| `"$.blaze_sword_section@how_to_play_common.main_sections.controls[11].paragraph_8@how_to_play_common.paragraph.$text"` | `"effect.blaze_sword.text.8"` | стр. 371: `"  Small fireballs will not be able to approach you within a radius of 7."` |
| `"$.blaze_sword_section@how_to_play_common.main_sections.controls[12].paragraph_9@how_to_play_common.paragraph.$text"` | `"effect.blaze_sword.text.9"` | стр. 372: `"-Description:"` |
| `"$.blaze_sword_section@how_to_play_common.main_sections.controls[13].paragraph_10@how_to_play_common.paragraph.$text"` | `"effect.blaze_sword.text.10"` | стр. 373: `"  Blaze rods will surround you around your body."` |
| `"$.blaze_sword_section@how_to_play_common.main_sections.controls[14].paragraph_11@how_to_play_common.paragraph.$text"` | `"effect.blaze_sword.text.11"` | стр. 374: `"  Your body will turn somewhat orange."` |
| `"$.blaze_sword_section@how_to_play_common.main_sections.controls[15].paragraph_12@how_to_play_common.paragraph.$text"` | `"effect.blaze_sword.text.12"` | стр. 375: `"-How to create or get it:"` |
| `"$.blaze_sword_section@how_to_play_common.main_sections.controls[16].paragraph_13@how_to_play_common.paragraph.$text"` | `"effect.blaze_sword.text.13"` | стр. 376: `"  A snow golem must kill a blaze this will release it with 0.5%"` |

### nether_star_sword_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.nether_star_sword_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"nether_star_sword.header.title"` | стр. 380: `"§lNether Star Sword    "` |
| `"$.nether_star_sword_section@how_to_play_common.main_sections.controls[3].paragraph_13@how_to_play_common.paragraph.$text"` | `"effect.nether_star_sword.text.13"` | стр. 381: `"-Durability: 3256                                                                "` |
| `"$.nether_star_sword_section@how_to_play_common.main_sections.controls[4].paragraph_0@how_to_play_common.paragraph.$text"` | `"effect.nether_star_sword.text.0"` | стр. 382: `"-Damage: 7 (12= Her damage was reduced to 7 as her new power makes her too powerful in this Add-On update.)"` |
| `"$.nether_star_sword_section@how_to_play_common.main_sections.controls[5].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.nether_star_sword.text.1"` | **нет точного ключа** |
| `"$.nether_star_sword_section@how_to_play_common.main_sections.controls[6].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.nether_star_sword.text.2"` | стр. 383: `"-Should Despawn Item: false"` |
| `"$.nether_star_sword_section@how_to_play_common.main_sections.controls[7].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.nether_star_sword.text.3"` | стр. 384: `"-Enchantable: true"` |
| `"$.nether_star_sword_section@how_to_play_common.main_sections.controls[8].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.nether_star_sword.text.4"` | стр. 385: `"-Repairable: true (With a nether star and the same sword.)"` |
| `"$.nether_star_sword_section@how_to_play_common.main_sections.controls[9].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.nether_star_sword.text.5"` | стр. 386: `"-Special skills: "` |
| `"$.nether_star_sword_section@how_to_play_common.main_sections.controls[10].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.nether_star_sword.text.6"` | стр. 387: `"  The stars of the nether will fall from the sky when you are attacking an entity, these stars will deal 6 damage per hit."` |
| `"$.nether_star_sword_section@how_to_play_common.main_sections.controls[11].paragraph_7@how_to_play_common.paragraph.$text"` | `"effect.nether_star_sword.text.7"` | стр. 388: `"-Description:"` |
| `"$.nether_star_sword_section@how_to_play_common.main_sections.controls[12].paragraph_8@how_to_play_common.paragraph.$text"` | `"effect.nether_star_sword.text.8"` | стр. 389: `"  When using it to kill the Wither you may get the Wither sword."` |
| `"$.nether_star_sword_section@how_to_play_common.main_sections.controls[13].paragraph_9@how_to_play_common.paragraph.$text"` | `"effect.nether_star_sword.text.9"` | стр. 390: `"  When thrown into the fire it explodes violently, this explosion is capable of breaking bedrock."` |
| `"$.nether_star_sword_section@how_to_play_common.main_sections.controls[14].paragraph_10@how_to_play_common.paragraph.$text"` | `"effect.nether_star_sword.text.10"` | стр. 391: `"  This sword is slightly unstable and can explode with a 0.01% chance when attacking entities."` |
| `"$.nether_star_sword_section@how_to_play_common.main_sections.controls[15].paragraph_11@how_to_play_common.paragraph.$text"` | `"effect.nether_star_sword.text.11"` | стр. 392: `"-How to create or get it:"` |
| `"$.nether_star_sword_section@how_to_play_common.main_sections.controls[16].paragraph_12@how_to_play_common.paragraph.$text"` | `"effect.nether_star_sword.text.12"` | стр. 393: `"  Crafting her with a diamond sword and a nether star."` |

### ice_sword_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.ice_sword_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"ice_sword.header.title"` | стр. 397: `"§lIce Sword                                                                    "` |
| `"$.ice_sword_section@how_to_play_common.main_sections.controls[3].paragraph_0@how_to_play_common.paragraph.$text"` | `"effect.ice_sword.text.0"` | стр. 398: `"-Durability: 500"` |
| `"$.ice_sword_section@how_to_play_common.main_sections.controls[4].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.ice_sword.text.1"` | стр. 399: `"-Damage: 8.5"` |
| `"$.ice_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.ice_sword.text.2"` | стр. 400: `"-Enchantable: true"` |
| `"$.ice_sword_section@how_to_play_common.main_sections.controls[6].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.ice_sword.text.3"` | стр. 401: `"-Repairable: true (For ice and the same sword.)"` |
| `"$.ice_sword_section@how_to_play_common.main_sections.controls[7].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.ice_sword.text.4"` | стр. 402: `"-Special skills: "` |
| `"$.ice_sword_section@how_to_play_common.main_sections.controls[8].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.ice_sword.text.5"` | стр. 403: `"  The ice that is placed when using this sword will disappear after approximately 8 seconds"` |
| `"$.ice_sword_section@how_to_play_common.main_sections.controls[9].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.ice_sword.text.6"` | стр. 404: `"  All the water under your feet will turn to ice."` |
| `"$.ice_sword_section@how_to_play_common.main_sections.controls[10].paragraph_7@how_to_play_common.paragraph.$text"` | `"effect.ice_sword.text.7"` | стр. 405: `"  Sometimes you will throw snowballs at the entities you attack."` |
| `"$.ice_sword_section@how_to_play_common.main_sections.controls[11].paragraph_8@how_to_play_common.paragraph.$text"` | `"effect.ice_sword.text.8"` | **нет точного ключа** |
| `"$.ice_sword_section@how_to_play_common.main_sections.controls[12].paragraph_9@how_to_play_common.paragraph.$text"` | `"effect.ice_sword.text.9"` | стр. 406: `"  Right-clicking or pressing the screen will cause entities within a radius of 8 to be encased in blocks of ice. (Sword durability: -6)"` |
| `"$.ice_sword_section@how_to_play_common.main_sections.controls[13].paragraph_10@how_to_play_common.paragraph.$text"` | `"effect.ice_sword.text.10"` | стр. 407: `"-Description:"` |
| `"$.ice_sword_section@how_to_play_common.main_sections.controls[14].paragraph_11@how_to_play_common.paragraph.$text"` | `"effect.ice_sword.text.11"` | стр. 408: `"  If the player is on fire the sword will turn into water."` |
| `"$.ice_sword_section@how_to_play_common.main_sections.controls[15].paragraph_12@how_to_play_common.paragraph.$text"` | `"effect.ice_sword.text.12"` | стр. 409: `"-How to create or get it:"` |
| `"$.ice_sword_section@how_to_play_common.main_sections.controls[16].paragraph_13@how_to_play_common.paragraph.$text"` | `"effect.ice_sword.text.13"` | стр. 410: `"  In the chests of: Igloos and Villages in the snow."` |

### quartz_sword_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.quartz_sword_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"quartz_sword.header.title"` | стр. 414: `"§lQuartz Sword                                                                    "` |
| `"$.quartz_sword_section@how_to_play_common.main_sections.controls[3].paragraph_0@how_to_play_common.paragraph.$text"` | `"effect.quartz_sword.text.0"` | стр. 415: `"-Durability: 1"` |
| `"$.quartz_sword_section@how_to_play_common.main_sections.controls[4].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.quartz_sword.text.1"` | стр. 416: `"-Damage: 600"` |
| `"$.quartz_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.quartz_sword.text.2"` | стр. 417: `"-Enchantable: false"` |
| `"$.quartz_sword_section@how_to_play_common.main_sections.controls[6].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.quartz_sword.text.3"` | стр. 418: `"-Repairable: false"` |
| `"$.quartz_sword_section@how_to_play_common.main_sections.controls[7].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.quartz_sword.text.4"` | стр. 419: `"-Special skills: None"` |
| `"$.quartz_sword_section@how_to_play_common.main_sections.controls[8].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.quartz_sword.text.5"` | стр. 420: `"-Description:"` |
| `"$.quartz_sword_section@how_to_play_common.main_sections.controls[9].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.quartz_sword.text.6"` | стр. 421: `"  Putting the sword in your hand will cause you a lot of damage for a moment and taking it out of your hand will too."` |
| `"$.quartz_sword_section@how_to_play_common.main_sections.controls[10].paragraph_7@how_to_play_common.paragraph.$text"` | `"effect.quartz_sword.text.7"` | стр. 422: `"  The sword causes so much damage that when you attack an enemy you will die too. (everything has a price)"` |
| `"$.quartz_sword_section@how_to_play_common.main_sections.controls[11].paragraph_8@how_to_play_common.paragraph.$text"` | `"effect.quartz_sword.text.8"` | стр. 423: `"-How to create or get it:"` |
| `"$.quartz_sword_section@how_to_play_common.main_sections.controls[12].paragraph_9@how_to_play_common.paragraph.$text"` | `"effect.quartz_sword.text.9"` | стр. 424: `"  With two quartz diamond blocks and a quartz diamond stick that is created with the same material."` |
| `"$.quartz_sword_section@how_to_play_common.main_sections.controls[13].paragraph_10@how_to_play_common.paragraph.$text"` | `"effect.quartz_sword.text.10"` | стр. 425: `"  (You should look for quartz diamond ores below height 15 in small quantities. (they are rare to find))"` |

### spider_sword_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.spider_sword_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"spider_sword.header.title"` | стр. 429: `"§lSpider Sword                                                                    "` |
| `"$.spider_sword_section@how_to_play_common.main_sections.controls[3].paragraph_0@how_to_play_common.paragraph.$text"` | `"effect.spider_sword.text.0"` | стр. 430: `"-Durability: 628"` |
| `"$.spider_sword_section@how_to_play_common.main_sections.controls[4].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.spider_sword.text.1"` | стр. 431: `"-Damage: 5"` |
| `"$.spider_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.spider_sword.text.2"` | стр. 432: `"-Enchantable: true"` |
| `"$.spider_sword_section@how_to_play_common.main_sections.controls[6].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.spider_sword.text.3"` | стр. 433: `"-Repairable: true (With cobwebs, spider eyes and the same sword.)"` |
| `"$.spider_sword_section@how_to_play_common.main_sections.controls[7].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.spider_sword.text.4"` | стр. 434: `"-Special skills: "` |
| `"$.spider_sword_section@how_to_play_common.main_sections.controls[8].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.spider_sword.text.5"` | стр. 435: `"  The spider mount will be able to climb walls."` |
| `"$.spider_sword_section@how_to_play_common.main_sections.controls[9].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.spider_sword.text.6"` | стр. 436: `"  You will throw cobwebs when attacking entities with a 5% chance."` |
| `"$.spider_sword_section@how_to_play_common.main_sections.controls[10].paragraph_7@how_to_play_common.paragraph.$text"` | `"effect.spider_sword.text.7"` | стр. 437: `"  Holding the sword in your hand you will get a spider mount."` |
| `"$.spider_sword_section@how_to_play_common.main_sections.controls[11].paragraph_8@how_to_play_common.paragraph.$text"` | `"effect.spider_sword.text.8"` | стр. 438: `"  Right-clicking or pressing the screen will fire cobweb projectiles for a few seconds. (Sword durability: -8)"` |
| `"$.spider_sword_section@how_to_play_common.main_sections.controls[12].paragraph_9@how_to_play_common.paragraph.$text"` | `"effect.spider_sword.text.9"` | стр. 439: `"-How to create or get it:"` |
| `"$.spider_sword_section@how_to_play_common.main_sections.controls[13].paragraph_10@how_to_play_common.paragraph.$text"` | `"effect.spider_sword.text.10"` | стр. 440: `"  In the chests of the abandoned mineshaft"` |

### tnt_sword_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.tnt_sword_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"tnt_sword.header.title"` | стр. 444: `"§lTnt Sword                                                                    "` |
| `"$.tnt_sword_section@how_to_play_common.main_sections.controls[3].paragraph_0@how_to_play_common.paragraph.$text"` | `"effect.tnt_sword.text.0"` | стр. 445: `"-Durability: 64"` |
| `"$.tnt_sword_section@how_to_play_common.main_sections.controls[4].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.tnt_sword.text.1"` | стр. 446: `"-Damage: 4"` |
| `"$.tnt_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.tnt_sword.text.2"` | стр. 447: `"-Enchantable: true"` |
| `"$.tnt_sword_section@how_to_play_common.main_sections.controls[6].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.tnt_sword.text.3"` | стр. 448: `"-Repairable: true (By tnt and the same sword.)"` |
| `"$.tnt_sword_section@how_to_play_common.main_sections.controls[7].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.tnt_sword.text.4"` | стр. 449: `"-Special skills: "` |
| `"$.tnt_sword_section@how_to_play_common.main_sections.controls[8].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.tnt_sword.text.5"` | стр. 450: `"  When attacking, you will throw small explosions."` |
| `"$.tnt_sword_section@how_to_play_common.main_sections.controls[9].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.tnt_sword.text.6"` | стр. 451: `" By right clicking or pressing the screen, a very powerful tnt will appear that will explode in 8 seconds. (Sword durability: -18)"` |
| `"$.tnt_sword_section@how_to_play_common.main_sections.controls[10].paragraph_7@how_to_play_common.paragraph.$text"` | `"effect.tnt_sword.text.7"` | стр. 452: `"-Description:"` |
| `"$.tnt_sword_section@how_to_play_common.main_sections.controls[11].paragraph_8@how_to_play_common.paragraph.$text"` | `"effect.tnt_sword.text.8"` | стр. 453: `"  When thrown into the fire it will explode violently."` |
| `"$.tnt_sword_section@how_to_play_common.main_sections.controls[12].paragraph_9@how_to_play_common.paragraph.$text"` | `"effect.tnt_sword.text.9"` | стр. 454: `"-How to create or get it:"` |
| `"$.tnt_sword_section@how_to_play_common.main_sections.controls[13].paragraph_10@how_to_play_common.paragraph.$text"` | `"effect.tnt_sword.text.10"` | стр. 455: `"  In the chests of the desert temple."` |

### wolf_sword_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.wolf_sword_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"wolf_sword.header.title"` | стр. 459: `"§lWolf Sword                                                                    "` |
| `"$.wolf_sword_section@how_to_play_common.main_sections.controls[3].paragraph_0@how_to_play_common.paragraph.$text"` | `"effect.wolf_sword.text.0"` | стр. 460: `"-Damage: 5 (+15 points during the night of the full moon. (They will not be visible in the sword damage))"` |
| `"$.wolf_sword_section@how_to_play_common.main_sections.controls[4].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.wolf_sword.text.1"` | стр. 461: `"-Enchantable: false"` |
| `"$.wolf_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.wolf_sword.text.2"` | стр. 462: `"-Repairable: true (Only with the same sword.)"` |
| `"$.wolf_sword_section@how_to_play_common.main_sections.controls[6].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.wolf_sword.text.3"` | стр. 463: `"-Special skills: "` |
| `"$.wolf_sword_section@how_to_play_common.main_sections.controls[7].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.wolf_sword.text.4"` | стр. 464: `"  -During the night of the full moon:"` |
| `"$.wolf_sword_section@how_to_play_common.main_sections.controls[8].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.wolf_sword.text.5"` | стр. 465: `"    The player will deal 15 points of damage per attack plus 5 points of sword attack for a total of 20."` |
| `"$.wolf_sword_section@how_to_play_common.main_sections.controls[9].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.wolf_sword.text.6"` | стр. 466: `"    The player will move faster."` |
| `"$.wolf_sword_section@how_to_play_common.main_sections.controls[10].paragraph_7@how_to_play_common.paragraph.$text"` | `"effect.wolf_sword.text.7"` | стр. 467: `"    The monsters will not attack you, you will be part of them."` |
| `"$.wolf_sword_section@how_to_play_common.main_sections.controls[11].paragraph_8@how_to_play_common.paragraph.$text"` | `"effect.wolf_sword.text.8"` | стр. 468: `"-Description:"` |
| `"$.wolf_sword_section@how_to_play_common.main_sections.controls[12].paragraph_9@how_to_play_common.paragraph.$text"` | `"effect.wolf_sword.text.9"` | стр. 469: `"  -During the night of the full moon:"` |
| `"$.wolf_sword_section@how_to_play_common.main_sections.controls[13].paragraph_10@how_to_play_common.paragraph.$text"` | `"effect.wolf_sword.text.10"` | стр. 470: `"    Your vision will look somewhat red"` |
| `"$.wolf_sword_section@how_to_play_common.main_sections.controls[14].paragraph_11@how_to_play_common.paragraph.$text"` | `"effect.wolf_sword.text.11"` | стр. 471: `"    If you remove the sword from your hand before the end of the full moon night you will get negative potion effects. (They will disappear at dawn.)"` |
| `"$.wolf_sword_section@how_to_play_common.main_sections.controls[15].paragraph_12@how_to_play_common.paragraph.$text"` | `"effect.wolf_sword.text.12"` | стр. 472: `"    If you have the sword in your hand during the sunset before the night of the full moon, you will feel dizzy."` |
| `"$.wolf_sword_section@how_to_play_common.main_sections.controls[16].paragraph_13@how_to_play_common.paragraph.$text"` | `"effect.wolf_sword.text.13"` | стр. 473: `"-How to create or get it:"` |
| `"$.wolf_sword_section@how_to_play_common.main_sections.controls[17].paragraph_14@how_to_play_common.paragraph.$text"` | `"effect.wolf_sword.text.14"` | стр. 474: `"  You must kill an alpha wolf during the full moon with the silver sword and it will drop the sword with a 10% chance."` |
| `"$.wolf_sword_section@how_to_play_common.main_sections.controls[18].paragraph_15@how_to_play_common.paragraph.$text"` | `"effect.wolf_sword.text.15"` | стр. 475: `"  (Alpha wolves appear in the taiga biome during the night of the full moon, you will hear a distant howl when one appears nearby.)"` |

### shulker_sword_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.shulker_sword_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"shulker_sword.header.title"` | стр. 479: `"§lShulker Sword                                                                    "` |
| `"$.shulker_sword_section@how_to_play_common.main_sections.controls[3].paragraph_0@how_to_play_common.paragraph.$text"` | `"effect.shulker_sword.text.0"` | стр. 480: `"-Durability: 2609"` |
| `"$.shulker_sword_section@how_to_play_common.main_sections.controls[4].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.shulker_sword.text.1"` | стр. 481: `"-Damage: 6"` |
| `"$.shulker_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.shulker_sword.text.2"` | стр. 482: `"-Enchantable: true"` |
| `"$.shulker_sword_section@how_to_play_common.main_sections.controls[6].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.shulker_sword.text.3"` | стр. 483: `"-Repairable: true (Only with the same sword.)"` |
| `"$.shulker_sword_section@how_to_play_common.main_sections.controls[7].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.shulker_sword.text.4"` | стр. 484: `"-Special skills: "` |
| `"$.shulker_sword_section@how_to_play_common.main_sections.controls[8].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.shulker_sword.text.5"` | стр. 485: `"  Throw shulker projectiles with a 10% chance when attacking entities."` |
| `"$.shulker_sword_section@how_to_play_common.main_sections.controls[9].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.shulker_sword.text.6"` | стр. 486: `"  Right-clicking or pressing the screen will levitate entities within a radius of 6. (Sword durability: -8)"` |
| `"$.shulker_sword_section@how_to_play_common.main_sections.controls[10].paragraph_7@how_to_play_common.paragraph.$text"` | `"effect.shulker_sword.text.7"` | стр. 487: `"  You will be immune to the effect of levitation."` |
| `"$.shulker_sword_section@how_to_play_common.main_sections.controls[11].paragraph_8@how_to_play_common.paragraph.$text"` | `"effect.shulker_sword.text.8"` | стр. 488: `"  When you duck you will get a shulker shell, which will protect you from enemy attacks but if they destroy the shell with you inside you will die too."` |
| `"$.shulker_sword_section@how_to_play_common.main_sections.controls[12].paragraph_9@how_to_play_common.paragraph.$text"` | `"effect.shulker_sword.text.9"` | стр. 489: `"-How to create or get it:"` |
| `"$.shulker_sword_section@how_to_play_common.main_sections.controls[13].paragraph_10@how_to_play_common.paragraph.$text"` | `"effect.shulker_sword.text.10"` | стр. 490: `" When killing shulkers with a 4.5% chance"` |

### bee_sword_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.bee_sword_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"bee_sword.header.title"` | стр. 494: `"§lBee Stinger                                                                   "` |
| `"$.bee_sword_section@how_to_play_common.main_sections.controls[3].paragraph_0@how_to_play_common.paragraph.$text"` | `"effect.bee_sword.text.0"` | стр. 495: `"-Durability: 1080"` |
| `"$.bee_sword_section@how_to_play_common.main_sections.controls[4].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.bee_sword.text.1"` | стр. 496: `"-Damage: 5"` |
| `"$.bee_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.bee_sword.text.2"` | стр. 497: `"-Enchantable: true"` |
| `"$.bee_sword_section@how_to_play_common.main_sections.controls[6].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.bee_sword.text.3"` | стр. 498: `"-Repairable: true (bee sword, honeycomb, honey block)"` |
| `"$.bee_sword_section@how_to_play_common.main_sections.controls[7].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.bee_sword.text.4"` | стр. 499: `"-Special skills: "` |
| `"$.bee_sword_section@how_to_play_common.main_sections.controls[8].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.bee_sword.text.5"` | стр. 500: `"   When attacking the enemies you will release from time to time small aggressive bees that will defend you."` |
| `"$.bee_sword_section@how_to_play_common.main_sections.controls[9].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.bee_sword.text.6"` | стр. 501: `"-Description:"` |
| `"$.bee_sword_section@how_to_play_common.main_sections.controls[10].paragraph_7@how_to_play_common.paragraph.$text"` | `"effect.bee_sword.text.7"` | стр. 502: `"  Flowers will appear from time to time, when you walk through grass."` |
| `"$.bee_sword_section@how_to_play_common.main_sections.controls[11].paragraph_8@how_to_play_common.paragraph.$text"` | `"effect.bee_sword.text.8"` | стр. 503: `"-How to create or get it:"` |
| `"$.bee_sword_section@how_to_play_common.main_sections.controls[12].paragraph_9@how_to_play_common.paragraph.$text"` | `"effect.bee_sword.text.9"` | стр. 504: `"  When a bee stings you, it will drop its stinger with a 2% percent chance."` |

### ghost_sword_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.ghost_sword_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"ghost_sword.header.title"` | стр. 508: `"§lGhost Sword                                                                    "` |
| `"$.ghost_sword_section@how_to_play_common.main_sections.controls[3].paragraph_0@how_to_play_common.paragraph.$text"` | `"effect.ghost_sword.text.0"` | стр. 509: `"-Durability: 3333"` |
| `"$.ghost_sword_section@how_to_play_common.main_sections.controls[4].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.ghost_sword.text.1"` | стр. 510: `"-Damage: -666 (Being a negative number you cannot harm any entity)"` |
| `"$.ghost_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.ghost_sword.text.2"` | **нет точного ключа** |
| `"$.ghost_sword_section@how_to_play_common.main_sections.controls[6].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.ghost_sword.text.3"` | стр. 511: `"-Should Despawn Item: false"` |
| `"$.ghost_sword_section@how_to_play_common.main_sections.controls[7].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.ghost_sword.text.4"` | стр. 512: `"-Enchantable: false"` |
| `"$.ghost_sword_section@how_to_play_common.main_sections.controls[8].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.ghost_sword.text.5"` | стр. 513: `"-Repairable: false"` |
| `"$.ghost_sword_section@how_to_play_common.main_sections.controls[9].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.ghost_sword.text.6"` | стр. 514: `"-Special skills: "` |
| `"$.ghost_sword_section@how_to_play_common.main_sections.controls[10].paragraph_7@how_to_play_common.paragraph.$text"` | `"effect.ghost_sword.text.7"` | стр. 515: `"  By holding the sword in hand, the player's legs will disappear and the player will turn into a ghost."` |
| `"$.ghost_sword_section@how_to_play_common.main_sections.controls[11].paragraph_8@how_to_play_common.paragraph.$text"` | `"effect.ghost_sword.text.8"` | стр. 516: `"  Nothing can harm the player, not fire, not lava, not explosions, basically nothing."` |
| `"$.ghost_sword_section@how_to_play_common.main_sections.controls[12].paragraph_9@how_to_play_common.paragraph.$text"` | `"effect.ghost_sword.text.9"` | стр. 517: `"  By right-clicking or pressing the screen the player will be able to teleport to any direction they are looking. (Sword durability: -6)"` |
| `"$.ghost_sword_section@how_to_play_common.main_sections.controls[13].paragraph_10@how_to_play_common.paragraph.$text"` | `"effect.ghost_sword.text.10"` | стр. 518: `"  By getting very close to the walls, the player will be able to see nearby caves and will be able to teleport to any cave they are looking at."` |
| `"$.ghost_sword_section@how_to_play_common.main_sections.controls[14].paragraph_11@how_to_play_common.paragraph.$text"` | `"effect.ghost_sword.text.11"` | стр. 519: `"  By crouching, the player will levitate, he can basically fly."` |
| `"$.ghost_sword_section@how_to_play_common.main_sections.controls[15].paragraph_12@how_to_play_common.paragraph.$text"` | `"effect.ghost_sword.text.12"` | стр. 520: `"  You can move faster than normal."` |
| `"$.ghost_sword_section@how_to_play_common.main_sections.controls[16].paragraph_13@how_to_play_common.paragraph.$text"` | `"effect.ghost_sword.text.13"` | стр. 521: `"  The monsters will not attack you, now you are one of them."` |
| `"$.ghost_sword_section@how_to_play_common.main_sections.controls[17].paragraph_14@how_to_play_common.paragraph.$text"` | `"effect.ghost_sword.text.14"` | стр. 522: `"-Description:"` |
| `"$.ghost_sword_section@how_to_play_common.main_sections.controls[18].paragraph_15@how_to_play_common.paragraph.$text"` | `"effect.ghost_sword.text.15"` | стр. 523: `"  The player's vision will look somewhat white."` |
| `"$.ghost_sword_section@how_to_play_common.main_sections.controls[19].paragraph_16@how_to_play_common.paragraph.$text"` | `"effect.ghost_sword.text.16"` | стр. 524: `"  The player will not be able to attack any entity."` |
| `"$.ghost_sword_section@how_to_play_common.main_sections.controls[20].paragraph_17@how_to_play_common.paragraph.$text"` | `"effect.ghost_sword.text.17"` | стр. 525: `"-How to create or get it:"` |
| `"$.ghost_sword_section@how_to_play_common.main_sections.controls[21].paragraph_18@how_to_play_common.paragraph.$text"` | `"effect.ghost_sword.text.18"` | стр. 526: `"  At night ghosts will appear, these entities are not dangerous, they will not try to attack you and you will not be able to attack them either, but if you touch them as if you were trying to harm them, the entity will drop the sword with a probability of 0.3% so it could take you a while to get it. It will also be 1% likely that the entity will teleport randomly so it could escape you. This entity is also sensitive to light, so if it gets too close to the light it will disappear. This entity only appears in blocks of grass or stone."` |

### creeper_sword_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.creeper_sword_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"creeper_sword.header.title"` | стр. 530: `"§lCreeper Sword                                                                    "` |
| `"$.creeper_sword_section@how_to_play_common.main_sections.controls[3].paragraph_0@how_to_play_common.paragraph.$text"` | `"effect.creeper_sword.text.0"` | стр. 531: `"-Durability: 1500"` |
| `"$.creeper_sword_section@how_to_play_common.main_sections.controls[4].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.creeper_sword.text.1"` | стр. 532: `"-Damage: 6"` |
| `"$.creeper_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.creeper_sword.text.2"` | **нет точного ключа** |
| `"$.creeper_sword_section@how_to_play_common.main_sections.controls[6].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.creeper_sword.text.3"` | стр. 533: `"-Enchantable: true "` |
| `"$.creeper_sword_section@how_to_play_common.main_sections.controls[7].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.creeper_sword.text.4"` | стр. 534: `"-Repairable: true (For gunpowder and the same sword.)"` |
| `"$.creeper_sword_section@how_to_play_common.main_sections.controls[8].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.creeper_sword.text.5"` | стр. 535: `"-Special skills: "` |
| `"$.creeper_sword_section@how_to_play_common.main_sections.controls[9].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.creeper_sword.text.6"` | стр. 536: `"  When attacking, it will launch small Creepers with a 20% chance that will explode in a few seconds with a small explosion."` |
| `"$.creeper_sword_section@how_to_play_common.main_sections.controls[10].paragraph_7@how_to_play_common.paragraph.$text"` | `"effect.creeper_sword.text.7"` | стр. 537: `"  By right-clicking or pressing the screen, the player will inflate like a Creeper and then the player will explode and die! (Sword durability: -1)"` |
| `"$.creeper_sword_section@how_to_play_common.main_sections.controls[11].paragraph_8@how_to_play_common.paragraph.$text"` | `"effect.creeper_sword.text.8"` | стр. 538: `"-How to create or get it:"` |
| `"$.creeper_sword_section@how_to_play_common.main_sections.controls[12].paragraph_9@how_to_play_common.paragraph.$text"` | `"effect.creeper_sword.text.9"` | стр. 539: `"  You will have to explode a Creeper loaded with a lighter and it will drop the sword with a 5% probability."` |

### fire_sword_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.fire_sword_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"fire_sword.header.title"` | стр. 543: `"§lFire Sword                                                                    "` |
| `"$.fire_sword_section@how_to_play_common.main_sections.controls[3].paragraph_0@how_to_play_common.paragraph.$text"` | `"effect.fire_sword.text.0"` | стр. 544: `"-Durability: 2000"` |
| `"$.fire_sword_section@how_to_play_common.main_sections.controls[4].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.fire_sword.text.1"` | стр. 545: `"-Damage: 6 (It will burn the enemies you attack.)"` |
| `"$.fire_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.fire_sword.text.2"` | стр. 546: `"-Enchantable: true"` |
| `"$.fire_sword_section@how_to_play_common.main_sections.controls[6].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.fire_sword.text.3"` | стр. 547: `"-Repairable: true (By fire blocks(rare) and the same sword)"` |
| `"$.fire_sword_section@how_to_play_common.main_sections.controls[7].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.fire_sword.text.4"` | стр. 548: `"-Special skills: "` |
| `"$.fire_sword_section@how_to_play_common.main_sections.controls[8].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.fire_sword.text.5"` | стр. 549: `"  You will be immune to fire."` |
| `"$.fire_sword_section@how_to_play_common.main_sections.controls[9].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.fire_sword.text.6"` | стр. 550: `"  When you attack you will launch living flames with a 15% probability, these entities will attack the monsters and they will die after a few seconds."` |
| `"$.fire_sword_section@how_to_play_common.main_sections.controls[10].paragraph_7@how_to_play_common.paragraph.$text"` | `"effect.fire_sword.text.7"` | стр. 551: `"  By right clicking or pressing the screen, you will activate the ability \"rain of fire\" this will create a shower of fireballs that will set fire all around. (Sword durability: -20)"` |
| `"$.fire_sword_section@how_to_play_common.main_sections.controls[11].paragraph_8@how_to_play_common.paragraph.$text"` | `"effect.fire_sword.text.8"` | стр. 552: `"  Entities very close to you will burn."` |
| `"$.fire_sword_section@how_to_play_common.main_sections.controls[12].paragraph_9@how_to_play_common.paragraph.$text"` | `"effect.fire_sword.text.9"` | стр. 553: `"  The ice and snow will melt."` |
| `"$.fire_sword_section@how_to_play_common.main_sections.controls[13].paragraph_10@how_to_play_common.paragraph.$text"` | `"effect.fire_sword.text.10"` | стр. 554: `"-Description: "` |
| `"$.fire_sword_section@how_to_play_common.main_sections.controls[14].paragraph_11@how_to_play_common.paragraph.$text"` | `"effect.fire_sword.text.11"` | стр. 555: `"  It disappears if you enter the water."` |
| `"$.fire_sword_section@how_to_play_common.main_sections.controls[15].paragraph_12@how_to_play_common.paragraph.$text"` | `"effect.fire_sword.text.12"` | стр. 556: `"  This sword emits light."` |
| `"$.fire_sword_section@how_to_play_common.main_sections.controls[16].paragraph_13@how_to_play_common.paragraph.$text"` | `"effect.fire_sword.text.13"` | стр. 557: `"  By throwing the fire sword into the water it turns into an obsidian sword."` |
| `"$.fire_sword_section@how_to_play_common.main_sections.controls[17].paragraph_14@how_to_play_common.paragraph.$text"` | `"effect.fire_sword.text.14"` | стр. 558: `"  Throwing the fire sword into the rain will cause it to turn into a crystal sword after a few seconds."` |
| `"$.fire_sword_section@how_to_play_common.main_sections.controls[18].paragraph_15@how_to_play_common.paragraph.$text"` | `"effect.fire_sword.text.15"` | стр. 559: `"-How to create or get it:"` |
| `"$.fire_sword_section@how_to_play_common.main_sections.controls[19].paragraph_16@how_to_play_common.paragraph.$text"` | `"effect.fire_sword.text.16"` | стр. 560: `"  You must kill living flames, these appear in the Nether and some of them will attack you, to kill this entity correctly without the fire sword falling into the fire and vanishing, you will have to place blocks such as slabs, pressure plates or other types of I do not complete this to prevent the entity from setting fire. The entity will drop the sword with a 4.9% chance. This entity will disappear in a random period of between 25 and 60 seconds."` |

### spectral_sword_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.spectral_sword_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"spectral_sword.header.title"` | стр. 564: `"§lSpectral Sword                                                                    "` |
| `"$.spectral_sword_section@how_to_play_common.main_sections.controls[3].paragraph_0@how_to_play_common.paragraph.$text"` | `"effect.spectral_sword.text.0"` | стр. 565: `"-Durability: 3256"` |
| `"$.spectral_sword_section@how_to_play_common.main_sections.controls[4].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.spectral_sword.text.1"` | стр. 566: `"-Damage: 9"` |
| `"$.spectral_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.spectral_sword.text.2"` | **нет точного ключа** |
| `"$.spectral_sword_section@how_to_play_common.main_sections.controls[6].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.spectral_sword.text.3"` | стр. 567: `"-Should Despawn Item: false"` |
| `"$.spectral_sword_section@how_to_play_common.main_sections.controls[7].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.spectral_sword.text.4"` | стр. 568: `"-Enchantable: false"` |
| `"$.spectral_sword_section@how_to_play_common.main_sections.controls[8].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.spectral_sword.text.5"` | стр. 569: `"-Repairable: true (By ender crystal, nether star and by the same sword.)"` |
| `"$.spectral_sword_section@how_to_play_common.main_sections.controls[9].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.spectral_sword.text.6"` | стр. 570: `"-Special skills: "` |
| `"$.spectral_sword_section@how_to_play_common.main_sections.controls[10].paragraph_7@how_to_play_common.paragraph.$text"` | `"effect.spectral_sword.text.7"` | стр. 571: `"  It will make the main block of each dimension transparent only in that dimension. (Overworld: stone, Nether: netherrack, End: endstone.)"` |
| `"$.spectral_sword_section@how_to_play_common.main_sections.controls[11].paragraph_8@how_to_play_common.paragraph.$text"` | `"effect.spectral_sword.text.8"` | стр. 572: `"  Fire an explosive projectile. (Sword durability: -15)"` |
| `"$.spectral_sword_section@how_to_play_common.main_sections.controls[12].paragraph_9@how_to_play_common.paragraph.$text"` | `"effect.spectral_sword.text.9"` | стр. 573: `"-Description:"` |
| `"$.spectral_sword_section@how_to_play_common.main_sections.controls[13].paragraph_10@how_to_play_common.paragraph.$text"` | `"effect.spectral_sword.text.10"` | стр. 574: `"  This sword is somewhat unstable so it may explode when attacking entities with a 1% chance."` |
| `"$.spectral_sword_section@how_to_play_common.main_sections.controls[14].paragraph_11@how_to_play_common.paragraph.$text"` | `"effect.spectral_sword.text.11"` | стр. 575: `"  This sword will emit a slight light."` |
| `"$.spectral_sword_section@how_to_play_common.main_sections.controls[15].paragraph_12@how_to_play_common.paragraph.$text"` | `"effect.spectral_sword.text.12"` | стр. 576: `"  An ender crystal will appear above you and follow you everywhere."` |
| `"$.spectral_sword_section@how_to_play_common.main_sections.controls[16].paragraph_13@how_to_play_common.paragraph.$text"` | `"effect.spectral_sword.text.13"` | стр. 577: `"-How to create or get it:"` |
| `"$.spectral_sword_section@how_to_play_common.main_sections.controls[17].paragraph_14@how_to_play_common.paragraph.$text"` | `"effect.spectral_sword.text.14"` | стр. 578: `"  When exploding ender crystals in the Nether with a 2% chance."` |
| `"$.spectral_sword_section@how_to_play_common.main_sections.controls[18].paragraph_15@how_to_play_common.paragraph.$text"` | `"effect.spectral_sword.text.15"` | стр. 579: `"  Kill a Ghast with his own projectile with a 6% chance."` |

### bedrock_sword_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.bedrock_sword_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"bedrock_sword.header.title"` | стр. 583: `"§lBedrock Sword                                                                    "` |
| `"$.bedrock_sword_section@how_to_play_common.main_sections.controls[3].paragraph_0@how_to_play_common.paragraph.$text"` | `"effect.bedrock_sword.text.0"` | стр. 584: `"-Durability: (Infinite)"` |
| `"$.bedrock_sword_section@how_to_play_common.main_sections.controls[4].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.bedrock_sword.text.1"` | стр. 585: `"-Damage: 18"` |
| `"$.bedrock_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.bedrock_sword.text.2"` | **нет точного ключа** |
| `"$.bedrock_sword_section@how_to_play_common.main_sections.controls[6].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.bedrock_sword.text.3"` | стр. 586: `"-Should Despawn Item: false"` |
| `"$.bedrock_sword_section@how_to_play_common.main_sections.controls[7].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.bedrock_sword.text.4"` | стр. 587: `"-Enchantable: false"` |
| `"$.bedrock_sword_section@how_to_play_common.main_sections.controls[8].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.bedrock_sword.text.5"` | стр. 588: `"-Special skills: none"` |
| `"$.bedrock_sword_section@how_to_play_common.main_sections.controls[9].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.bedrock_sword.text.6"` | стр. 589: `"-Description: It works as an extremely powerful pickaxe."` |
| `"$.bedrock_sword_section@how_to_play_common.main_sections.controls[10].paragraph_7@how_to_play_common.paragraph.$text"` | `"effect.bedrock_sword.text.7"` | стр. 590: `"-How to create or get it:"` |
| `"$.bedrock_sword_section@how_to_play_common.main_sections.controls[11].paragraph_8@how_to_play_common.paragraph.$text"` | `"effect.bedrock_sword.text.8"` | стр. 591: `"  It is created with two bedrock blocks and a bedrock stick that is created with the same material."` |
| `"$.bedrock_sword_section@how_to_play_common.main_sections.controls[12].paragraph_9@how_to_play_common.paragraph.$text"` | `"effect.bedrock_sword.text.9"` | стр. 592: `"  (Bedrock can only be obtained by using the Ultra Instinct sword projectile or by throwing the Nether Star Sword into fire, which will cause a loud explosion that will shatter the bedrock.)"` |

### ender_sword_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.ender_sword_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"ender_sword.header.title"` | стр. 596: `"§lEnder Sword                                                                    "` |
| `"$.ender_sword_section@how_to_play_common.main_sections.controls[3].paragraph_0@how_to_play_common.paragraph.$text"` | `"effect.ender_sword.text.0"` | стр. 597: `"-Durability: 1256"` |
| `"$.ender_sword_section@how_to_play_common.main_sections.controls[4].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.ender_sword.text.1"` | стр. 598: `"-Damage: 9"` |
| `"$.ender_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.ender_sword.text.2"` | стр. 599: `"-Enchantable: true"` |
| `"$.ender_sword_section@how_to_play_common.main_sections.controls[6].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.ender_sword.text.3"` | стр. 600: `"-Repairable: true (By ender pearl, ender eye or the same sword.)"` |
| `"$.ender_sword_section@how_to_play_common.main_sections.controls[7].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.ender_sword.text.4"` | стр. 601: `"-Special skills: "` |
| `"$.ender_sword_section@how_to_play_common.main_sections.controls[8].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.ender_sword.text.5"` | стр. 602: `"  You will not take damage from any projectile and will randomly teleport within a radius of 16 when you are attacked with one."` |
| `"$.ender_sword_section@how_to_play_common.main_sections.controls[9].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.ender_sword.text.6"` | стр. 603: `"  When they attack you, you will randomly teleport in a radius of 16 with a 50% chance."` |
| `"$.ender_sword_section@how_to_play_common.main_sections.controls[10].paragraph_7@how_to_play_common.paragraph.$text"` | `"effect.ender_sword.text.7"` | стр. 604: `"  The water will cause you damage and you will teleport randomly."` |
| `"$.ender_sword_section@how_to_play_common.main_sections.controls[11].paragraph_8@how_to_play_common.paragraph.$text"` | `"effect.ender_sword.text.8"` | стр. 605: `"  By right clicking or pressing the screen, you will randomly teleport in a radius of between 16 to 32 blocks. (Sword durability: -5) "` |
| `"$.ender_sword_section@how_to_play_common.main_sections.controls[12].paragraph_9@how_to_play_common.paragraph.$text"` | `"effect.ender_sword.text.9"` | стр. 606: `"                                                                                             \"Cooldown Duration\": 2 = seconds                                                                                   "` |
| `"$.ender_sword_section@how_to_play_common.main_sections.controls[13].paragraph_10@how_to_play_common.paragraph.$text"` | `"effect.ender_sword.text.10"` | стр. 607: `"-How to create or get it:"` |
| `"$.ender_sword_section@how_to_play_common.main_sections.controls[14].paragraph_11@how_to_play_common.paragraph.$text"` | `"effect.ender_sword.text.11"` | стр. 608: `"  By killing the red-eyed enderman with a 2.5% chance, this enderman only appears in the overworld (normal world) with a low probability."` |

### lightning_sword_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.lightning_sword_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"lightning_sword.header.title"` | стр. 612: `"§lLightning Sword                                                                    "` |
| `"$.lightning_sword_section@how_to_play_common.main_sections.controls[3].paragraph_0@how_to_play_common.paragraph.$text"` | `"effect.lightning_sword.text.0"` | стр. 613: `"-Durability: 2012"` |
| `"$.lightning_sword_section@how_to_play_common.main_sections.controls[4].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.lightning_sword.text.1"` | стр. 614: `"-Damage: 8"` |
| `"$.lightning_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.lightning_sword.text.2"` | стр. 615: `"-Enchantable: true"` |
| `"$.lightning_sword_section@how_to_play_common.main_sections.controls[6].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.lightning_sword.text.3"` | стр. 616: `"-Repairable: true (Only with the same sword.)"` |
| `"$.lightning_sword_section@how_to_play_common.main_sections.controls[7].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.lightning_sword.text.4"` | стр. 617: `"-Special skills: "` |
| `"$.lightning_sword_section@how_to_play_common.main_sections.controls[8].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.lightning_sword.text.5"` | стр. 618: `"  When attacking it will throw thunder."` |
| `"$.lightning_sword_section@how_to_play_common.main_sections.controls[9].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.lightning_sword.text.6"` | стр. 619: `"  By right clicking or pressing the screen, 41 rays will fall around you. (Sword durability: -9)"` |
| `"$.lightning_sword_section@how_to_play_common.main_sections.controls[10].paragraph_7@how_to_play_common.paragraph.$text"` | `"effect.lightning_sword.text.7"` | стр. 620: `"  You will be immune to lightning damage but not fire."` |
| `"$.lightning_sword_section@how_to_play_common.main_sections.controls[11].paragraph_8@how_to_play_common.paragraph.$text"` | `"effect.lightning_sword.text.8"` | стр. 621: `"-Description:"` |
| `"$.lightning_sword_section@how_to_play_common.main_sections.controls[12].paragraph_9@how_to_play_common.paragraph.$text"` | `"effect.lightning_sword.text.9"` | стр. 622: `"  This sword emits light."` |
| `"$.lightning_sword_section@how_to_play_common.main_sections.controls[13].paragraph_10@how_to_play_common.paragraph.$text"` | `"effect.lightning_sword.text.10"` | стр. 623: `"-How to create or get it:"` |
| `"$.lightning_sword_section@how_to_play_common.main_sections.controls[14].paragraph_11@how_to_play_common.paragraph.$text"` | `"effect.lightning_sword.text.11"` | стр. 624: `"  You must kill an entity called \"Centella in Spanish\" or \"spherical lightning or ball lightning in English\", this entity will only appear with a 20% probability when lightning strikes during a storm, this entity will not try to harm you but if you get too close you will receive a lot damage, also this entity has 200 life points, that is, 100 hearts, it will not be easy to kill it, you must do it before it disappears since it only lives in a random period of between 10 to 60 seconds. (This entity is a reference to a strange real-life atmospheric phenomenon.)"` |

### wither_sword_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.wither_sword_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"wither_sword.header.title"` | стр. 628: `"§lWither Sword                                                                    "` |
| `"$.wither_sword_section@how_to_play_common.main_sections.controls[3].paragraph_0@how_to_play_common.paragraph.$text"` | `"effect.wither_sword.text.0"` | стр. 629: `"-Durability: 3856"` |
| `"$.wither_sword_section@how_to_play_common.main_sections.controls[4].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.wither_sword.text.1"` | стр. 630: `"-Damage: 10"` |
| `"$.wither_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.wither_sword.text.2"` | **нет точного ключа** |
| `"$.wither_sword_section@how_to_play_common.main_sections.controls[6].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.wither_sword.text.3"` | стр. 631: `"-Should Despawn Item: false"` |
| `"$.wither_sword_section@how_to_play_common.main_sections.controls[7].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.wither_sword.text.4"` | стр. 632: `"-Enchantable: false"` |
| `"$.wither_sword_section@how_to_play_common.main_sections.controls[8].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.wither_sword.text.5"` | стр. 633: `"-Repairable: true (Only with the same sword.)"` |
| `"$.wither_sword_section@how_to_play_common.main_sections.controls[9].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.wither_sword.text.6"` | стр. 634: `"-Special skills: "` |
| `"$.wither_sword_section@how_to_play_common.main_sections.controls[10].paragraph_7@how_to_play_common.paragraph.$text"` | `"effect.wither_sword.text.7"` | стр. 635: `"  When attacking, it will drop wither skulls with a 10% chance."` |
| `"$.wither_sword_section@how_to_play_common.main_sections.controls[11].paragraph_8@how_to_play_common.paragraph.$text"` | `"effect.wither_sword.text.8"` | стр. 636: `"  It will be immune to the wither effect."` |
| `"$.wither_sword_section@how_to_play_common.main_sections.controls[12].paragraph_9@how_to_play_common.paragraph.$text"` | `"effect.wither_sword.text.9"` | стр. 637: `"  The leaves of the trees will wither, the flowers will turn into withered roses, the grass will turn to dirt."` |
| `"$.wither_sword_section@how_to_play_common.main_sections.controls[13].paragraph_10@how_to_play_common.paragraph.$text"` | `"effect.wither_sword.text.10"` | стр. 638: `"  Right clicking or pressing the screen will launch a dangerous wither skull. (Sword durability: -3)"` |
| `"$.wither_sword_section@how_to_play_common.main_sections.controls[14].paragraph_11@how_to_play_common.paragraph.$text"` | `"effect.wither_sword.text.11"` | стр. 639: `"-Description:"` |
| `"$.wither_sword_section@how_to_play_common.main_sections.controls[15].paragraph_12@how_to_play_common.paragraph.$text"` | `"effect.wither_sword.text.12"` | стр. 640: `"  This sword emits light."` |
| `"$.wither_sword_section@how_to_play_common.main_sections.controls[16].paragraph_13@how_to_play_common.paragraph.$text"` | `"effect.wither_sword.text.13"` | стр. 641: `"  By having the sword you will see a life bar on your screen with the name \"Wither Sword\" this is only decoration."` |
| `"$.wither_sword_section@how_to_play_common.main_sections.controls[17].paragraph_14@how_to_play_common.paragraph.$text"` | `"effect.wither_sword.text.14"` | стр. 642: `"  You will have the effect of wither but it will not hurt you."` |
| `"$.wither_sword_section@how_to_play_common.main_sections.controls[18].paragraph_15@how_to_play_common.paragraph.$text"` | `"effect.wither_sword.text.15"` | стр. 643: `"-How to create or get it:"` |
| `"$.wither_sword_section@how_to_play_common.main_sections.controls[19].paragraph_16@how_to_play_common.paragraph.$text"` | `"effect.wither_sword.text.16"` | стр. 644: `"  You will have to kill the wither with a \"Nether star sword\" and it will drop it with a 13% chance."` |

### time_sword_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.time_sword_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"time_sword.header.title"` | стр. 648: `"§lTime Sword                                                                    "` |
| `"$.time_sword_section@how_to_play_common.main_sections.controls[3].paragraph_0@how_to_play_common.paragraph.$text"` | `"effect.time_sword.text.0"` | стр. 649: `"-Durability: 13770"` |
| `"$.time_sword_section@how_to_play_common.main_sections.controls[4].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.time_sword.text.1"` | стр. 650: `"-Damage: 13"` |
| `"$.time_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.time_sword.text.2"` | стр. 651: `"-Enchantable: false"` |
| `"$.time_sword_section@how_to_play_common.main_sections.controls[6].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.time_sword.text.3"` | стр. 652: `"-Repairable: false"` |
| `"$.time_sword_section@how_to_play_common.main_sections.controls[7].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.time_sword.text.4"` | стр. 653: `"-Special skills: "` |
| `"$.time_sword_section@how_to_play_common.main_sections.controls[8].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.time_sword.text.5"` | стр. 654: `"  Time will advance faster, you and all entities will be able to move much faster, and the plants will grow much faster."` |
| `"$.time_sword_section@how_to_play_common.main_sections.controls[9].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.time_sword.text.6"` | стр. 655: `"-Description:"` |
| `"$.time_sword_section@how_to_play_common.main_sections.controls[10].paragraph_7@how_to_play_common.paragraph.$text"` | `"effect.time_sword.text.7"` | стр. 656: `"  When attacking, the durability points of the sword could lose 1 point with a probability of 90%, 16 points with a probability of 6%, 32 points with a probability of 3% and 64 points with a probability of 1%."` |
| `"$.time_sword_section@how_to_play_common.main_sections.controls[11].paragraph_8@how_to_play_common.paragraph.$text"` | `"effect.time_sword.text.8"` | стр. 657: `"  This sword emits light."` |
| `"$.time_sword_section@how_to_play_common.main_sections.controls[12].paragraph_9@how_to_play_common.paragraph.$text"` | `"effect.time_sword.text.9"` | стр. 658: `"-How to create or get it:"` |
| `"$.time_sword_section@how_to_play_common.main_sections.controls[13].paragraph_10@how_to_play_common.paragraph.$text"` | `"effect.time_sword.text.10"` | стр. 659: `"You must throw clock swords into the water of the well structure that is in the desert, this well will serve as a source of wishes and will give you the sword with a 2.5% chance."` |

### ultra_instinct_sword_section@how_to_play_common.main_sections

| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |
|---|---|---|
| `"$.ultra_instinct_sword_section@how_to_play_common.main_sections.controls[0].header_0@how_to_play_common.header.$text"` | `"ultra_instinct_sword.header.title"` | стр. 663: `"§lUltra Instinct Sword                                                                    "` |
| `"$.ultra_instinct_sword_section@how_to_play_common.main_sections.controls[3].paragraph_0@how_to_play_common.paragraph.$text"` | `"effect.ultra_instinct_sword.text.0"` | стр. 664: `"-Durability: 9999"` |
| `"$.ultra_instinct_sword_section@how_to_play_common.main_sections.controls[4].paragraph_1@how_to_play_common.paragraph.$text"` | `"effect.ultra_instinct_sword.text.1"` | стр. 665: `"-Damage: 16"` |
| `"$.ultra_instinct_sword_section@how_to_play_common.main_sections.controls[5].paragraph_2@how_to_play_common.paragraph.$text"` | `"effect.ultra_instinct_sword.text.2"` | **нет точного ключа** |
| `"$.ultra_instinct_sword_section@how_to_play_common.main_sections.controls[6].paragraph_3@how_to_play_common.paragraph.$text"` | `"effect.ultra_instinct_sword.text.3"` | стр. 666: `"-Should Despawn Item: false"` |
| `"$.ultra_instinct_sword_section@how_to_play_common.main_sections.controls[7].paragraph_4@how_to_play_common.paragraph.$text"` | `"effect.ultra_instinct_sword.text.4"` | стр. 667: `"-Enchantable: false"` |
| `"$.ultra_instinct_sword_section@how_to_play_common.main_sections.controls[8].paragraph_5@how_to_play_common.paragraph.$text"` | `"effect.ultra_instinct_sword.text.5"` | стр. 668: `"-Repairable: false"` |
| `"$.ultra_instinct_sword_section@how_to_play_common.main_sections.controls[9].paragraph_6@how_to_play_common.paragraph.$text"` | `"effect.ultra_instinct_sword.text.6"` | стр. 669: `"-Special skills: "` |
| `"$.ultra_instinct_sword_section@how_to_play_common.main_sections.controls[10].paragraph_7@how_to_play_common.paragraph.$text"` | `"effect.ultra_instinct_sword.text.7"` | стр. 670: `"  Melee attack, projectiles, fire, and explosions cannot harm you. (You can dodge the melee attack and the projectiles automatically)"` |
| `"$.ultra_instinct_sword_section@how_to_play_common.main_sections.controls[11].paragraph_8@how_to_play_common.paragraph.$text"` | `"effect.ultra_instinct_sword.text.8"` | стр. 671: `"  Right clicking or pressing the screen will fire a powerful projectile capable of destroying everything in its path and the bedrock will not be a problem. (This ability recharges every 61 seconds) (Sword durability: -48) (The Ultra Instinct projectile can cause a lot of lag for a few seconds.)"` |
| `"$.ultra_instinct_sword_section@how_to_play_common.main_sections.controls[12].paragraph_9@how_to_play_common.paragraph.$text"` | `"effect.ultra_instinct_sword.text.9"` | стр. 672: `"-How to create or get it:"` |
| `"$.ultra_instinct_sword_section@how_to_play_common.main_sections.controls[13].paragraph_10@how_to_play_common.paragraph.$text"` | `"effect.ultra_instinct_sword.text.10"` | стр. 673: `"  You must throw quartz diamonds or quartz diamond blocks (new ore) into the water of the well structure that is in the desert, this well will serve as a source of wishes and will give you the sword with a 0.8% chance when throwing quartz diamonds or 2.5% chance with the quartz diamond block."` |
| `"$.ultra_instinct_sword_section@how_to_play_common.main_sections.controls[14].paragraph_11@how_to_play_common.paragraph.$text"` | `"effect.ultra_instinct_sword.text.11"` | стр. 674: `"  (Quartz diamond ores are spawned below height 15 in small quantities and are rare to find)"` |
