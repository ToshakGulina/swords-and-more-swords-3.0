# Исходные карточки предметов — архив 2.8.8

Эта машинная выписка — точная отправная точка, не законченный семантический аудит. JSON ниже получен из JSON5, комментарии и оформление опущены; при повторяющихся ключах читать исходный файл. События и команды приведены без пересчёта вероятностей: веса являются относительными внутри конкретного `randomize`. Движковые значения по умолчанию и недокументированное поведение не угадываются.

Ссылки указывают путь и номера строк **внутри указанного архива**. Поиск упоминаний текстовый и не является полным графом вызовов: косвенные события, группы компонентов, снаряды, таблицы добычи, функции и модели необходимо проверить вручную.

## effect:bedrock_stick

- Название в en_US: `§7Bedrock Stick`
- Определение: `Swords_B/items/bedrock_stick.json`
- Урон (`minecraft:damage`): `6`
- Прочность (`minecraft:durability`): `"не указана"`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:bedrock_stick",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:should_despawn": true,
    "minecraft:max_stack_size": 1,
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:can_destroy_in_creative": true,
    "minecraft:icon": {
      "texture": "bedrock_stick"
    },
    "minecraft:display_name": {},
    "minecraft:damage": 6,
    "minecraft:weapon": {}
  },
  "events": {}
}
```

### Прямые текстовые упоминания

- `Swords_B/recipes/bedrock_stick.json`: строки 5, 18
- `Swords_B/recipes/bedrock_sword.json`: строки 15
- `Swords_R/texts/en_US.lang`: строки 46
- `Swords_R/textures/item_texture.json`: строки 120, 121
- `Swords_R/ui/how_to_play_screen.json`: строки 205

### Рецепты и таблицы добычи с точным ID

`Swords_B/recipes/bedrock_stick.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect:bedrock_stick"
    },  
    "tags": [ "crafting_table" ],
    "pattern": [
      "#",
      "#"
    ],
    "key": {
      "#": {
        "item": "minecraft:bedrock"
      }
    },
    "result": {
      "item": "effect:bedrock_stick"
    }
  }
}
```

`Swords_B/recipes/bedrock_sword.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect:bedrock_sword"
    },  
    "tags": [ "crafting_table" ],
    "pattern": [
      "B",
      "B",
      "#"
    ],
    "key": {
      "#": {
        "item": "effect:bedrock_stick"
      },
      "B": {
        "item": "minecraft:bedrock"
      }
    },
    "result": {
      "item": "effect:bedrock_sword"
    }
  }
}
```


## effect:bedrock_sword

- Название в en_US: `§l§7Bedrock Sword`
- Определение: `Swords_B/items/bedrock_sword.json`
- Урон (`minecraft:damage`): `18`
- Прочность (`minecraft:durability`): `"не указана"`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:bedrock_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:should_despawn": false,
    "minecraft:max_stack_size": 1,
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "bedrock_sword"
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": {
            "tags": "q.any_tag('stone', 'metal', 'diamond_pick_diggable', 'wood', 'pumpkin', 'plant', 'dirt', 'sand', 'gravel', 'grass', 'snow')"
          },
          "speed": 999
        },
        {
          "block": "effect99:quartz_diamond_block",
          "speed": 50
        },
        {
          "block": "effect99:quartz_diamond_ore",
          "speed": 100
        },
        {
          "block": "effect99:silver_ore",
          "speed": 999
        },
        {
          "block": "minecraft:warped_wart_block",
          "speed": 999
        },
        {
          "block": "minecraft:nether_wart_block",
          "speed": 999
        },
        {
          "block": "minecraft:leaves",
          "speed": 999
        },
        {
          "block": "minecraft:leaves2",
          "speed": 999
        },
        {
          "block": "minecraft:hay_block",
          "speed": 999
        },
        {
          "block": "minecraft:soul_soil",
          "speed": 999
        },
        {
          "block": "minecraft:soul_sand",
          "speed": 999
        },
        {
          "block": "minecraft:chest",
          "speed": 999
        },
        {
          "block": "minecraft:melon_block",
          "speed": 999
        },
        {
          "block": "minecraft:bookshelf",
          "speed": 999
        },
        {
          "block": "minecraft:lectern",
          "speed": 999
        },
        {
          "block": "minecraft:pumkin",
          "speed": 999
        },
        {
          "block": "minecraft:ice",
          "speed": 999
        },
        {
          "block": "minecraft:bone_block",
          "speed": 999
        },
        {
          "block": "minecraft:mob_spawner",
          "speed": 999
        },
        {
          "block": "minecraft:anvil",
          "speed": 999
        },
        {
          "block": "minecraft:netherite_block",
          "speed": 999
        },
        {
          "block": "minecraft:sandstone",
          "speed": 999
        },
        {
          "block": "minecraft:diamond_block",
          "speed": 999
        },
        {
          "block": "minecraft:lapis_block",
          "speed": 999
        },
        {
          "block": "minecraft:emerald_block",
          "speed": 999
        },
        {
          "block": "minecraft:ancient_debris",
          "speed": 999
        },
        {
          "block": "minecraft:cracked_polished_blackstone_bricks",
          "speed": 999
        },
        {
          "block": "minecraft:nether_brick",
          "speed": 999
        },
        {
          "block": "minecraft:cracked_nether_bricks",
          "speed": 999
        },
        {
          "block": "minecraft:quartz_ore",
          "speed": 999
        },
        {
          "block": "minecraft:netherrack",
          "speed": 999
        },
        {
          "block": "minecraft:basalt",
          "speed": 999
        },
        {
          "block": "minecraft:end_bricks",
          "speed": 999
        },
        {
          "block": "minecraft:purpur_block",
          "speed": 999
        },
        {
          "block": "minecraft:purpur_stairs",
          "speed": 999
        },
        {
          "block": "minecraft:end_brick_stairs",
          "speed": 999
        },
        {
          "block": "minecraft:stone_slab2",
          "speed": 999
        },
        {
          "block": "minecraft:stone_slab3",
          "speed": 999
        },
        {
          "block": "minecraft:polished_basalt",
          "speed": 999
        },
        {
          "block": "minecraft:warped_nylium",
          "speed": 999
        },
        {
          "block": "minecraft:crimson_nylium",
          "speed": 999
        },
        {
          "block": "minecraft:end_stone",
          "speed": 999
        },
        {
          "block": "minecraft:ender_chest",
          "speed": 999
        },
        {
          "block": "minecraft:quartz_block",
          "speed": 999
        },
        {
          "block": "minecraft:quartz_stairs",
          "speed": 999
        },
        {
          "block": "minecraft:quartz_bricks",
          "speed": 999
        },
        {
          "block": "minecraft:quartz_stairs",
          "speed": 999
        },
        {
          "block": "minecraft:nether_gold_ore",
          "speed": 999
        },
        {
          "block": "minecraft:blackstone",
          "speed": 999
        },
        {
          "block": "minecraft:furnace",
          "speed": 999
        },
        {
          "block": "minecraft:blast_furnace",
          "speed": 999
        },
        {
          "block": "minecraft:lit_furnace",
          "speed": 999
        },
        {
          "block": "minecraft:blast_furnace",
          "speed": 999
        },
        {
          "block": "minecraft:chain",
          "speed": 999
        },
        {
          "block": "minecraft:lantern",
          "speed": 999
        },
        {
          "block": "minecraft:soul_lantern",
          "speed": 999
        },
        {
          "block": "minecraft:grindstone",
          "speed": 999
        },
        {
          "block": "minecraft:brewing_stand",
          "speed": 999
        },
        {
          "block": "minecraft:smooth_stone",
          "speed": 999
        },
        {
          "block": "minecraft:stonebrick",
          "speed": 999
        },
        {
          "block": "minecraft:enchanting_table",
          "speed": 999
        },
        {
          "block": "minecraft:stone_brick_stairs",
          "speed": 999
        },
        {
          "block": "minecraft:mossy_stone_brick_stairs",
          "speed": 999
        },
        {
          "block": "minecraft:polished_blackstone_bricks",
          "speed": 999
        },
        {
          "block": "minecraft:polished_blackstone_stairs",
          "speed": 999
        },
        {
          "block": "minecraft:blackstone_wall",
          "speed": 999
        },
        {
          "block": "minecraft:blackstone_wall",
          "speed": 999
        },
        {
          "block": "minecraft:polished_blackstone_wall",
          "speed": 999
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 18,
    "minecraft:weapon": {}
  },
  "events": {}
}
```

### Прямые текстовые упоминания

- `Swords_B/animation_controllers/item_events.json`: строки 22
- `Swords_B/blocks/quartz_diamond_block.json`: строки 17
- `Swords_B/blocks/quartz_diamond_ore.json`: строки 13
- `Swords_B/blocks/silver_ore.json`: строки 13
- `Swords_B/entities/item.json`: строки 181
- `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/tag_swords.mcfunction`: строки 9
- `Swords_B/functions/give.mcfunction`: строки 33
- `Swords_B/recipes/bedrock_sword.json`: строки 5, 22
- `Swords_R/texts/en_US.lang`: строки 40, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592
- `Swords_R/textures/item_texture.json`: строки 104, 105
- `Swords_R/ui/how_to_play_screen.json`: строки 67, 126, 975, 977, 978, 981, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993

### Рецепты и таблицы добычи с точным ID

`Swords_B/recipes/bedrock_sword.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect:bedrock_sword"
    },  
    "tags": [ "crafting_table" ],
    "pattern": [
      "B",
      "B",
      "#"
    ],
    "key": {
      "#": {
        "item": "effect:bedrock_stick"
      },
      "B": {
        "item": "minecraft:bedrock"
      }
    },
    "result": {
      "item": "effect:bedrock_sword"
    }
  }
}
```


## effect:bee_sword

- Название в en_US: `§l§gBee Stinger`
- Определение: `Swords_B/items/bee_sword.json`
- Урон (`minecraft:damage`): `5`
- Прочность (`minecraft:durability`): `{"max_durability":1080}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:bee_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 1080
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "bee_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:bee_sword"
          ],
          "repair_amount": 1080
        },
        {
          "items": [
            "minecraft:honey_block"
          ],
          "repair_amount": 400
        },
        {
          "items": [
            "minecraft:honeycomb"
          ],
          "repair_amount": 150
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 5,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        },
        {
          "randomize": [
            {
              "weight": 30,
              "shoot": {
                "projectile": "entity:bee_sword",
                "launch_power": 1
              }
            },
            {
              "weight": 70,
              "damage": {
                "type": "durability",
                "amount": 1,
                "target": "self"
              }
            }
          ]
        }
      ]
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/entities/bee.json`: строки 848, 849
- `Swords_B/entities/bee_entity.json`: строки 5
- `Swords_B/entities/player.json`: строки 22, 24, 26, 1041, 1043, 1048, 1050, 1125, 1128, 1129, 1133, 1136, 1137, 1145
- `Swords_B/loot_tables/bee_sword.json`: строки 8
- `Swords_R/entity/bee_sword.json`: строки 5
- `Swords_R/texts/en_US.lang`: строки 43, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504
- `Swords_R/textures/item_texture.json`: строки 113, 114
- `Swords_R/ui/how_to_play_screen.json`: строки 62, 121, 837, 839, 840, 843, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855

### Рецепты и таблицы добычи с точным ID

`Swords_B/loot_tables/bee_sword.json`:

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "effect:bee_sword",
          "weight": 1
        }
      ]
    }
  ]
}
```


### Одноимённые группы и события игрока (`Swords_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:bee_sword": {
      "minecraft:timer": {
        "time": [
          3,
          8
        ],
        "looping": true,
        "randomInterval": true,
        "time_down_event": {
          "event": "bee_sword_flower",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "bee_sword"
        ]
      }
    }
  },
  "events": {
    "minecraft:bee_sword": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "!=",
            "value": "bee_sword"
          },
          "add": {
            "component_groups": [
              "minecraft:bee_sword"
            ]
          }
        }
      ]
    },
    "stop_bee_sword_event": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "==",
            "value": "bee_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:bee_sword"
            ]
          },
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          }
        }
      ]
    },
    "bee_sword_flower": {
      "randomize": [
        {
          "weight": 1,
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 0"
            ]
          }
        },
        {
          "weight": 1,
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 1"
            ]
          }
        },
        {
          "weight": 1,
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 2"
            ]
          }
        },
        {
          "weight": 1,
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 3"
            ]
          }
        },
        {
          "weight": 1,
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 4"
            ]
          }
        },
        {
          "weight": 1,
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 5"
            ]
          }
        },
        {
          "weight": 1,
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 6"
            ]
          }
        },
        {
          "weight": 1,
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 7"
            ]
          }
        },
        {
          "weight": 1,
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 8"
            ]
          }
        },
        {
          "weight": 1,
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 9"
            ]
          }
        },
        {
          "weight": 1,
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 10"
            ]
          }
        },
        {
          "weight": 1,
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ yellow_flower 0"
            ]
          }
        }
      ]
    }
  }
}
```

## effect:blaze_sword

- Название в en_US: `§l§6Blaze Sword`
- Определение: `Swords_B/items/blaze_sword.json`
- Урон (`minecraft:damage`): `6`
- Прочность (`minecraft:durability`): `{"max_durability":2300}`
- Кулдаун (`minecraft:cooldown`): `{"category":"blaze_sword","duration":20}`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:blaze_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 2300
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "blaze_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:blaze_sword"
          ],
          "repair_amount": 2300
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:cooldown": {
      "category": "blaze_sword",
      "duration": 20
    },
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:damage": 6,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "on_use": {
      "damage": {
        "type": "durability",
        "amount": 10,
        "target": "self"
      },
      "run_command": {
        "command": [
          "event entity @s[family=blaze_sword] blaze_sword_skill_event",
          "effect @s levitation 7 0 true",
          "effect @s slow_falling 10 3 true"
        ]
      }
    },
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        },
        {
          "randomize": [
            {
              "weight": 14,
              "run_command": {
                "command": [
                  "effect @s fire_resistance 1 0 true"
                ]
              },
              "shoot": {
                "projectile": "minecraft:small_fireball",
                "launch_power": 1
              }
            },
            {
              "weight": 1,
              "run_command": {
                "command": [
                  "effect @s fire_resistance 1 0 true"
                ]
              },
              "shoot": {
                "projectile": "minecraft:fireball",
                "launch_power": 1
              }
            },
            {
              "weight": 85,
              "damage": {
                "type": "durability",
                "amount": 1,
                "target": "self"
              }
            }
          ]
        }
      ]
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/entities/blaze.json`: строки 127, 134
- `Swords_B/entities/player.json`: строки 355, 370, 372, 375, 376, 378, 417, 642, 644, 649, 651, 2163, 2166, 2167, 2192, 2205, 2208, 2209, 2233, 2236, 2238, 2242, 2245, 2249, 2256
- `Swords_B/functions/give.mcfunction`: строки 1
- `Swords_B/loot_tables/entities/blaze.json`: строки 50
- `Swords_R/entity/player.entity.json`: строки 61
- `Swords_R/texts/en_US.lang`: строки 7, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376
- `Swords_R/textures/item_texture.json`: строки 5, 6
- `Swords_R/ui/how_to_play_screen.json`: строки 54, 113, 630, 632, 633, 636, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652

### Рецепты и таблицы добычи с точным ID

`Swords_B/loot_tables/entities/blaze.json`:

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:blaze_rod",
          "weight": 1,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 0,
                "max": 1
              }
            },
            {
              "function": "looting_enchant",
              "count": {
                "min": 0,
                "max": 1
              }
            }
          ]
        }
      ],
      "conditions": [
        {
          "condition": "killed_by_player_or_pets"
        }
      ]
    },
    {
      "conditions": [
        {
          "condition": "killed_by_entity",
          "entity_type": "minecraft:snow_golem"
        },
        {
          "condition": "random_chance_with_looting",
          "chance": 0.025,
          "looting_multiplier": 0.02
        }
      ],
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "effect:blaze_sword",
          "weight": 1,
          "functions": [
            {
              "function": "set_data",
              "data": 0
            }
          ]
        }
      ]
    }
  ]
}
```


### Одноимённые группы и события игрока (`Swords_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:blaze_sword": {
      "minecraft:damage_sensor": {
        "triggers": {
          "on_damage": {
            "filters": {
              "any_of": [
                {
                  "test": "has_damage",
                  "subject": "self",
                  "value": "fire"
                },
                {
                  "test": "has_damage",
                  "subject": "self",
                  "value": "fire_tick"
                }
              ]
            }
          },
          "deals_damage": false
        }
      },
      "minecraft:hurt_on_condition": {
        "damage_conditions": [
          {
            "filters": {
              "test": "in_water_or_rain"
            },
            "cause": "drowning",
            "damage_per_tick": 1
          }
        ]
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "blaze_sword"
        ]
      },
      "minecraft:timer": {
        "time": [
          1,
          1
        ],
        "looping": true,
        "time_down_event": {
          "event": "blaze_sword_effects",
          "target": "self"
        }
      }
    },
    "blaze_sword_skill": {
      "minecraft:type_family": {
        "family": [
          "player",
          "blaze_sword",
          "blaze_sword_skill"
        ]
      },
      "minecraft:timer": {
        "time": [
          6,
          6
        ],
        "looping": false,
        "time_down_event": {
          "event": "blaze_sword_skill",
          "target": "self"
        }
      }
    }
  },
  "events": {
    "minecraft:blaze_sword": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "!=",
            "value": "blaze_sword"
          },
          "add": {
            "component_groups": [
              "minecraft:blaze_sword"
            ]
          },
          "run_command": {
            "command": [
              "particle minecraft:mobflame_single ~ ~ ~",
              "particle minecraft:mobflame_single ~ ~1 ~",
              "particle minecraft:mobflame_single ~ ~1.5 ~",
              "particle minecraft:mobflame_single ~0.4 ~ ~",
              "particle minecraft:mobflame_single ~ ~1 ~0.4",
              "particle minecraft:mobflame_single ~-0.4 ~1.5 ~",
              "particle minecraft:mobflame_single ~ ~ ~-0.4",
              "particle minecraft:mobflame_single ~0.3 ~1 ~0.3",
              "particle minecraft:mobflame_single ~-0.3 ~1.5 ~-0.3",
              "particle minecraft:mobflame_single ~0.3 ~ ~-0.3",
              "particle minecraft:mobflame_single ~-0.3 ~1 ~0.3",
              "particle minecraft:example_linearcurve ~ ~1 ~",
              "playsound random.fizz @a[r=16]"
            ]
          }
        },
        {
          "run_command": {
            "command": [
              "event entity @e[family=shot_by_the_blaze,r=7] minecraft:inertia_disable",
              "fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace air",
              "fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace effect99:lightblock2"
            ]
          }
        },
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "==",
            "value": "blaze_sword_skill"
          },
          "randomize": [
            {
              "weight": 5,
              "run_command": {
                "command": [
                  "particle minecraft:mobflame_single ~ ~0.2 ~"
                ]
              }
            },
            {
              "weight": 5,
              "run_command": {
                "command": [
                  "particle minecraft:mobflame_single ~0.3 ~0.2 ~"
                ]
              }
            },
            {
              "weight": 5,
              "run_command": {
                "command": [
                  "particle minecraft:mobflame_single ~ ~0.2 ~0.3"
                ]
              }
            },
            {
              "weight": 5,
              "run_command": {
                "command": [
                  "particle minecraft:mobflame_single ~-0.3 ~0.2 ~"
                ]
              }
            },
            {
              "weight": 5,
              "run_command": {
                "command": [
                  "particle minecraft:mobflame_single ~ ~0.2 ~-0.3"
                ]
              }
            },
            {
              "weight": 5,
              "run_command": {
                "command": [
                  "playsound mob.blaze.breathe @a[r=12] ~ ~ ~ 0.5"
                ]
              }
            },
            {
              "weight": 95
            }
          ]
        }
      ]
    },
    "stop_blaze_sword_event": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "==",
            "value": "blaze_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:blaze_sword",
              "shoot_small_fireball"
            ]
          },
          "run_command": {
            "command": [
              "particle minecraft:mobflame_single ~ ~ ~",
              "particle minecraft:mobflame_single ~ ~1 ~",
              "particle minecraft:mobflame_single ~ ~1.5 ~",
              "particle minecraft:mobflame_single ~0.4 ~ ~",
              "particle minecraft:mobflame_single ~ ~1 ~0.4",
              "particle minecraft:mobflame_single ~-0.4 ~1.5 ~",
              "particle minecraft:mobflame_single ~ ~ ~-0.4",
              "particle minecraft:mobflame_single ~0.3 ~1 ~0.3",
              "particle minecraft:mobflame_single ~-0.3 ~1.5 ~-0.3",
              "particle minecraft:mobflame_single ~0.3 ~ ~-0.3",
              "particle minecraft:mobflame_single ~-0.3 ~1 ~0.3",
              "particle minecraft:example_linearcurve ~ ~1 ~",
              "playsound random.fizz @a[r=16]",
              "effect @s levitation 0 0 true",
              "effect @s slow_falling 0 0 true"
            ]
          },
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          }
        }
      ]
    },
    "stop_blaze_sword_skill": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "==",
            "value": "blaze_sword"
          },
          "remove": {
            "component_groups": [
              "shoot_small_fireball"
            ]
          },
          "add": {
            "component_groups": [
              "minecraft:blaze_sword"
            ]
          }
        }
      ]
    },
    "blaze_sword_skill_event": {
      "add": {
        "component_groups": [
          "blaze_sword_skill"
        ]
      }
    },
    "blaze_sword_skill": {
      "add": {
        "component_groups": [
          "shoot_small_fireball"
        ]
      }
    },
    "blaze_sword_effects": {
      "randomize": [
        {
          "weight": 1,
          "run_command": {
            "command": [
              "particle minecraft:mobflame_single ~ ~0.2 ~"
            ]
          }
        },
        {
          "weight": 1,
          "run_command": {
            "command": [
              "particle minecraft:mobflame_single ~0.3 ~0.2 ~"
            ]
          }
        },
        {
          "weight": 1,
          "run_command": {
            "command": [
              "particle minecraft:mobflame_single ~ ~0.2 ~0.3"
            ]
          }
        },
        {
          "weight": 1,
          "run_command": {
            "command": [
              "particle minecraft:mobflame_single ~-0.3 ~0.2 ~"
            ]
          }
        },
        {
          "weight": 1,
          "run_command": {
            "command": [
              "particle minecraft:mobflame_single ~ ~0.2 ~-0.3"
            ]
          }
        },
        {
          "weight": 1,
          "run_command": {
            "command": [
              "playsound mob.blaze.breathe @a[r=12] ~ ~ ~ 0.5"
            ]
          }
        }
      ]
    }
  }
}
```

## effect:bone_sword

- Название в en_US: `§lSkeleton Bone Sword`
- Определение: `Swords_B/items/bone_sword.json`
- Урон (`minecraft:damage`): `5`
- Прочность (`minecraft:durability`): `{"max_durability":820}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:bone_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 820
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "bone_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:bone_sword"
          ],
          "repair_amount": 820
        },
        {
          "items": [
            "minecraft:bone"
          ],
          "repair_amount": 70
        },
        {
          "items": [
            "minecraft:bone_block"
          ],
          "repair_amount": 300
        },
        {
          "items": [
            "minecraft:bone_meal"
          ],
          "repair_amount": 18
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 5,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        },
        {
          "randomize": [
            {
              "weight": 20,
              "shoot": {
                "projectile": "minecraft:arrow",
                "launch_power": 1
              }
            },
            {
              "weight": 80,
              "damage": {
                "type": "durability",
                "amount": 1,
                "target": "self"
              }
            }
          ]
        }
      ]
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/entities/arrow.json`: строки 15, 218
- `Swords_B/entities/player.json`: строки 349, 350, 352, 656, 658, 663, 665, 2136, 2139, 2140, 2149, 2152, 2153, 2158
- `Swords_B/entities/skeleton.json`: строки 25, 99, 265, 275
- `Swords_B/functions/give.mcfunction`: строки 2
- `Swords_R/texts/en_US.lang`: строки 32, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263
- `Swords_R/textures/item_texture.json`: строки 77, 78
- `Swords_R/ui/how_to_play_screen.json`: строки 46, 105, 446, 448, 449, 452, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464

### Одноимённые группы и события игрока (`Swords_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:bone_sword": {
      "minecraft:type_family": {
        "family": [
          "player",
          "bone_sword"
        ]
      },
      "minecraft:timer": {
        "time": [
          1,
          1
        ],
        "looping": true,
        "time_down_event": {
          "event": "bone_sword_skills",
          "target": "self"
        }
      }
    }
  },
  "events": {
    "minecraft:bone_sword": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "!=",
            "value": "bone_sword"
          },
          "add": {
            "component_groups": [
              "minecraft:bone_sword"
            ]
          }
        },
        {
          "run_command": {
            "command": [
              "event entity @e[family=arrow,r=8] minecraft:inertia_disable"
            ]
          }
        }
      ]
    },
    "stop_bone_sword_event": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "==",
            "value": "bone_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:bone_sword"
            ]
          },
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          }
        }
      ]
    },
    "bone_sword_skills": {
      "run_command": {
        "command": [
          "summon entity:grows_crop ~ ~0.1 ~ grows_crop_event"
        ]
      }
    }
  }
}
```

## effect:cactus_sword

- Название в en_US: `§l§2Cactus Sword`
- Определение: `Swords_B/items/cactus_sword.json`
- Урон (`minecraft:damage`): `6`
- Прочность (`minecraft:durability`): `{"max_durability":125}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:cactus_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 125
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "cactus_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:cactus_sword"
          ],
          "repair_amount": 125
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:render_offsets": {
      "main_hand": {
        "first_person": {
          "position": [
            0.67,
            0,
            -1.24
          ]
        },
        "third_person": {
          "position": [
            0.36,
            1.5,
            -0.66
          ]
        }
      }
    },
    "minecraft:display_name": {},
    "minecraft:damage": 6,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/entities/player.json`: строки 343, 344, 346, 670, 672, 677, 679, 2117, 2120, 2121, 2125, 2128, 2129, 2134
- `Swords_B/functions/give.mcfunction`: строки 3
- `Swords_B/recipes/cactus_sword.json`: строки 5, 22
- `Swords_R/texts/en_US.lang`: строки 12, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216
- `Swords_R/textures/item_texture.json`: строки 20, 21
- `Swords_R/ui/how_to_play_screen.json`: строки 43, 102, 374, 376, 377, 380, 382, 383, 384, 385, 386, 387, 388, 389, 390

### Рецепты и таблицы добычи с точным ID

`Swords_B/recipes/cactus_sword.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect:cactus_sword"
    },  
    "tags": [ "crafting_table" ],
    "pattern": [
      "F",
      "F",
      "E"
    ],
    "key": {
      "E": {
        "item": "minecraft:stick"
      },
      "F": {
        "item": "minecraft:cactus"
      }
    },
    "result": {
      "item": "effect:cactus_sword"
    }
  }
}
```


### Одноимённые группы и события игрока (`Swords_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:cactus_sword": {
      "minecraft:type_family": {
        "family": [
          "player",
          "cactus_sword"
        ]
      },
      "minecraft:timer": {
        "time": [
          0.5,
          0.5
        ],
        "looping": true,
        "time_down_event": {
          "event": "cactus_sword_skills",
          "target": "self"
        }
      }
    }
  },
  "events": {
    "minecraft:cactus_sword": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "!=",
            "value": "cactus_sword"
          },
          "add": {
            "component_groups": [
              "minecraft:cactus_sword"
            ]
          }
        }
      ]
    },
    "stop_cactus_sword_event": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "==",
            "value": "cactus_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:cactus_sword"
            ]
          },
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          }
        }
      ]
    },
    "cactus_sword_skills": {
      "run_command": {
        "command": [
          "damage @e[r=1.4,type=!player] 1 contact entity @s",
          "damage @s 1 contact"
        ]
      }
    }
  }
}
```

## effect:clock_sword

- Название в en_US: `§l§gClock Sword`
- Определение: `Swords_B/items/clock_sword.json`
- Урон (`minecraft:damage`): `7`
- Прочность (`minecraft:durability`): `{"max_durability":4800}`
- Кулдаун (`minecraft:cooldown`): `{"category":"clock_sword","duration":30}`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:clock_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": true,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 4800
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "clock_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:clock_sword"
          ],
          "repair_amount": 4800
        },
        {
          "items": [
            "minecraft:clock"
          ],
          "repair_amount": 900
        },
        {
          "items": [
            "minecraft:gold_block"
          ],
          "repair_amount": 780
        },
        {
          "items": [
            "minecraft:gold_ingot"
          ],
          "repair_amount": 87
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:cooldown": {
      "category": "clock_sword",
      "duration": 30
    },
    "minecraft:display_name": {},
    "minecraft:damage": 7,
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    },
    "on_use": {
      "damage": {
        "type": "durability",
        "amount": 10,
        "target": "self"
      },
      "run_command": {
        "command": [
          "event entity @s[family=clock_sword] clock_sword_skill_event"
        ]
      }
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/entities/player.json`: строки 35, 36, 38, 40, 42, 44, 1013, 1015, 1020, 1022, 1178, 1181, 1182, 1185, 1186, 1192, 1198, 1201, 1202, 1208, 1210, 1213, 1214
- `Swords_B/functions/give.mcfunction`: строки 31
- `Swords_B/recipes/clock_sword.json`: строки 5, 25
- `Swords_R/texts/en_US.lang`: строки 42, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328
- `Swords_R/textures/item_texture.json`: строки 110, 111
- `Swords_R/ui/how_to_play_screen.json`: строки 51, 110, 561, 563, 564, 567, 569, 570, 571, 572, 573, 574, 575, 576, 577

### Рецепты и таблицы добычи с точным ID

`Swords_B/recipes/clock_sword.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect:clock_sword"
    },  
    "tags": [ "crafting_table" ],
    "pattern": [
      "X##",
      "#C#",
      "I#X"
    ],
    "key": {
      "#": {
        "item": "minecraft:gold_block"
      },
      "C": {
        "item": "minecraft:clock"   
      },
      "I": {
        "item": "minecraft:gold_ingot"   
      }
    },
    "result": {
      "item": "effect:clock_sword"
    }
  }
}
```


### Одноимённые группы и события игрока (`Swords_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:clock_sword": {
      "minecraft:type_family": {
        "family": [
          "player",
          "clock_sword"
        ]
      }
    },
    "clock_sword_skill": {
      "minecraft:timer": {
        "time": [
          5,
          5
        ],
        "looping": true,
        "randomInterval": false,
        "time_down_event": {
          "event": "stop_clock_sword_event",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "clock_sword",
          "clock_sword_skill"
        ]
      }
    },
    "clock_sword_movement": {
      "minecraft:movement": {
        "value": 1
      }
    }
  },
  "events": {
    "minecraft:clock_sword": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "!=",
            "value": "clock_sword"
          },
          "add": {
            "component_groups": [
              "minecraft:clock_sword"
            ]
          }
        },
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "==",
            "value": "clock_sword_skill"
          },
          "add": {
            "component_groups": [
              "clock_sword_movement"
            ]
          },
          "run_command": {
            "command": [
              "gamerule randomtickspeed 100",
              "effect @e[type=!player] speed 1 10 true",
              "time add 10",
              "event entity @a[family=default_player] clock_sword_movement"
            ]
          }
        }
      ]
    },
    "stop_clock_sword_event": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "==",
            "value": "clock_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:clock_sword"
            ]
          },
          "run_command": {
            "command": [
              "gamerule randomtickspeed 1",
              "effect @e[type=!player] speed 0 0",
              "event entity @a[family=default_player] default_player"
            ]
          },
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          }
        }
      ]
    },
    "clock_sword_skill_event": {
      "add": {
        "component_groups": [
          "clock_sword_skill"
        ]
      }
    },
    "clock_sword_movement": {
      "add": {
        "component_groups": [
          "clock_sword_movement"
        ]
      }
    }
  }
}
```

## effect:coal_sword

- Название в en_US: `§l§0Coal Sword`
- Определение: `Swords_B/items/coal_sword.json`
- Урон (`minecraft:damage`): `4`
- Прочность (`minecraft:durability`): `{"max_durability":121}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:coal_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 121
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "coal_sword"
    },
    "minecraft:fuel": {
      "duration": 360.0
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:coal_sword"
          ],
          "repair_amount": 121
        },
        {
          "items": [
            "minecraft:coal"
          ],
          "repair_amount": 58
        },
        {
          "items": [
            "minecraft:stick"
          ],
          "repair_amount": 2
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 4,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/functions/give.mcfunction`: строки 4
- `Swords_B/loot_tables/chests/spawn_bonus_chest.json`: строки 8
- `Swords_B/recipes/coal_sword.json`: строки 5, 22
- `Swords_R/texts/en_US.lang`: строки 8, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144
- `Swords_R/textures/item_texture.json`: строки 11, 12
- `Swords_R/ui/how_to_play_screen.json`: строки 37, 96, 247, 249, 250, 253, 255, 256, 257, 258, 259, 260, 261, 262, 263

### Рецепты и таблицы добычи с точным ID

`Swords_B/loot_tables/chests/spawn_bonus_chest.json`:

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "effect:coal_sword",
          "weight": 1
        },
        {
          "type": "item",
          "name": "minecraft:stone_axe",
          "weight": 1
        },
        {
          "type": "item",
          "name": "minecraft:wooden_axe",
          "weight": 3
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:stone_pickaxe",
          "weight": 1
        },
        {
          "type": "item",
          "name": "minecraft:wooden_pickaxe",
          "weight": 3
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:apple",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        }
      ]
    },        
    {
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:bread",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:salmon",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:stick",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 12
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:planks",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 12
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:log2",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:log2",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_data",
              "data": 1
            },
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:log",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:log",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_data",
              "data": 1
            },
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:log",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_data",
              "data": 2
            },
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:log",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_data",
              "data": 3
            },
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        }
      ]
    },    
    {
      "rolls": 1,
      "entries": [    
        {
          "type": "item",
          "name": "minecraft:potato",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:carrot",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        }        
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:sapling",
          "weight": 2,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 4,
                "max": 4
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:sapling",
          "weight": 2,
          "functions": [
            {
              "function": "minecraft:set_data",
              "data": 1
            },
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 4,
                "max": 4
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:sapling",
          "weight": 2,
          "functions": [
            {
              "function": "minecraft:set_data",
              "data": 2
            },
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 4,
                "max": 4
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:sapling",
          "weight": 4,
          "functions": [
            {
              "function": "minecraft:set_data",
              "data": 3
            },
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 4,
                "max": 4
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:sapling",
          "weight": 2,
          "functions": [
            {
              "function": "minecraft:set_data",
              "data": 4
            },
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 4,
                "max": 4
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:sapling",
          "weight": 2,
          "functions": [
            {
              "function": "minecraft:set_data",
              "data": 5
            },
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 4,
                "max": 4
              }
            }
          ]
        }
      ]
    },    
    {
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:melon_seeds",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:pumpkin_seeds",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:beetroot_seeds",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        }        
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:cactus",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:dye",
          "weight": 2,
          "functions": [
            {
              "function": "set_data",
              "data": 3
            },
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:brown_mushroom",
          "weight": 2,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        }
      ]
    }
  ]
}
```

`Swords_B/recipes/coal_sword.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect:coal_sword"
    },  
    "tags": [ "crafting_table" ],
    "pattern": [
      "2",
      "2",
      "1"
    ],
    "key": {
      "2": {
        "item": "minecraft:coal_block"
      },
      "1": {
        "item": "minecraft:stick"      
      }
    },
    "result": {
      "item": "effect:coal_sword"
    }
  }
}
```


## effect:creeper_sword

- Название в en_US: `§l§aCreeper§f Sword`
- Определение: `Swords_B/items/creeper_sword.json`
- Урон (`minecraft:damage`): `6`
- Прочность (`minecraft:durability`): `{"max_durability":1500}`
- Кулдаун (`minecraft:cooldown`): `{"category":"creeper_sword","duration":3}`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:creeper_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 1500
    },
    "minecraft:cooldown": {
      "category": "creeper_sword",
      "duration": 3
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "creeper_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:creeper_sword"
          ],
          "repair_amount": 1500
        },
        {
          "items": [
            "minecraft:gunpowder"
          ],
          "repair_amount": 256
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 6,
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "on_use": {
      "sequence": [
        {
          "run_command": {
            "command": [
              "event entity @s start_player_explode_event"
            ],
            "target": "holder"
          }
        },
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    },
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        },
        {
          "randomize": [
            {
              "weight": 20,
              "shoot": {
                "projectile": "minecraft:creeper",
                "launch_power": 1
              }
            },
            {
              "weight": 80,
              "damage": {
                "type": "durability",
                "amount": 1,
                "target": "self"
              }
            }
          ]
        }
      ]
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/entities/creeper.json`: строки 125, 325, 332, 339
- `Swords_B/functions/give.mcfunction`: строки 5
- `Swords_R/texts/en_US.lang`: строки 23, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539
- `Swords_R/textures/item_texture.json`: строки 44, 45
- `Swords_R/ui/how_to_play_screen.json`: строки 64, 123, 893, 895, 896, 899, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911

## effect:emerald_sword

- Название в en_US: `§l§aEmerald Sword`
- Определение: `Swords_B/items/emerald_sword.json`
- Урон (`minecraft:damage`): `7`
- Прочность (`minecraft:durability`): `{"max_durability":2300}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:emerald_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 2300
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "emerald_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:emerald_sword"
          ],
          "repair_amount": 2300
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 7,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/entities/player.json`: строки 334, 335, 684, 686, 691, 693, 2086, 2089, 2090, 2098, 2101, 2103
- `Swords_B/functions/give.mcfunction`: строки 6
- `Swords_B/loot_tables/chests/pillager_outpost.json`: строки 170
- `Swords_B/loot_tables/chests/stronghold_corridor.json`: строки 154
- `Swords_B/loot_tables/chests/woodland_mansion.json`: строки 56
- `Swords_B/trading/economy_trades/weapon_smith_trades.json`: строки 277
- `Swords_B/trading/weapon_smith_trades.json`: строки 168
- `Swords_R/texts/en_US.lang`: строки 14, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249
- `Swords_R/textures/item_texture.json`: строки 26, 27
- `Swords_R/ui/how_to_play_screen.json`: строки 45, 104, 425, 427, 428, 431, 433, 434, 435, 436, 437, 438, 439, 440, 441

### Рецепты и таблицы добычи с точным ID

`Swords_B/loot_tables/chests/pillager_outpost.json`:

```json
{
  "pools": [
    {
      "rolls": {
        "min": 0,
        "max": 1
      },
      "entries": [
        {
          "type": "item",
          "name": "minecraft:crossbow"
        }
      ]
    },
    {
      "rolls": {
        "min": 2,
        "max": 3
      },
      "entries": [
        {
          "type": "item",
          "weight": 7,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 3,
                "max": 5
              }
            }
          ],
          "name": "minecraft:wheat"
        },
        {
          "type": "item",
          "weight": 5,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 2,
                "max": 5
              }
            }
          ],
          "name": "minecraft:potato"
        },
        {
          "type": "item",
          "weight": 5,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 3,
                "max": 5
              }
            }
          ],
          "name": "minecraft:carrot"
        }
      ]
    },
    {
      "rolls": {
        "min": 1,
        "max": 3
      },
      "entries": [
        {
          "type": "item",
          "name": "minecraft:log2",
          "weight": 1,
          "functions": [
            {
              "function": "set_data",
              "data": 1
            },
            {
              "function": "set_count",
              "count": {
                "min": 2,
                "max": 3
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": {
        "min": 2,
        "max": 3
      },
      "entries": [
        {
          "type": "item",
          "weight": 7,
          "name": "minecraft:experience_bottle"
        },
        {
          "type": "item",
          "weight": 4,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 6
              }
            }
          ],
          "name": "minecraft:string"
        },
        {
          "type": "item",
          "weight": 4,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 2,
                "max": 7
              }
            }
          ],
          "name": "minecraft:arrow"
        },
        {
          "type": "item",
          "weight": 3,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "name": "minecraft:tripwire_hook"
        },
        {
          "type": "item",
          "weight": 3,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "name": "minecraft:iron_ingot"
        },
        {
          "type": "item",
          "weight": 3,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 0,
                "max": 1
              }
            }
          ],
          "name": "effect:emerald_sword"
        },
        {
          "type": "item",
          "weight": 3,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 0,
                "max": 1
              }
            }
          ],
          "name": "effect:lapis_sword"
        },
        {
          "type": "item",
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:book"
        }
      ]
    }
  ]

}
```

`Swords_B/loot_tables/chests/stronghold_corridor.json`:

```json
{
  "pools": [
    {
      "rolls": {
        "min": 2,
        "max": 3
      },
      "entries": [
        {
          "type": "item",
          "name": "minecraft:ender_pearl",
          "weight": 50
        },
        {
          "type": "item",
          "name": "minecraft:emerald",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "weight": 15
        },
        {
          "type": "item",
          "name": "minecraft:diamond",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "weight": 15
        },
        {
          "type": "item",
          "name": "minecraft:iron_ingot",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 5
              }
            }
          ],
          "weight": 50
        },
        {
          "type": "item",
          "name": "minecraft:gold_ingot",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "weight": 25
        },
        {
          "type": "item",
          "name": "minecraft:redstone",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 4,
                "max": 9
              }
            }
          ],
          "weight": 25
        },
        {
          "type": "item",
          "name": "minecraft:bread",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "weight": 75
        },
        {
          "type": "item",
          "name": "minecraft:apple",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "weight": 75
        },
        {
          "type": "item",
          "name": "minecraft:iron_pickaxe",
          "weight": 25
        },
        {
          "type": "item",
          "name": "minecraft:iron_sword",
          "weight": 25
        },
        {
          "type": "item",
          "name": "minecraft:iron_chestplate",
          "weight": 25
        },
        {
          "type": "item",
          "name": "minecraft:iron_helmet",
          "weight": 25
        },
        {
          "type": "item",
          "name": "minecraft:iron_leggings",
          "weight": 25
        },
        {
          "type": "item",
          "name": "minecraft:iron_boots",
          "weight": 25
        },
        {
          "type": "item",
          "name": "minecraft:golden_apple",
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:saddle",
          "weight": 5
        },
        {
          "type": "item",
          "name": "effect:emerald_sword",
          "weight": 5
        },
        {
          "type": "item",
          "name": "effect:lapis_sword",
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:horsearmoriron",
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:horsearmorgold",
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:horsearmordiamond",
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:book",
          "weight": 6,
          "functions": [
            {
              "function": "enchant_with_levels",
              "levels": 30,
              "treasure": true
            }
          ]
        }
      ]
    }
  ]
}
```

`Swords_B/loot_tables/chests/woodland_mansion.json`:

```json
{
  "pools": [
    {
      "rolls": {
        "min": 1,
        "max": 3
      },
      "entries": [
        {
          "type": "item",
          "name": "minecraft:lead",
          "weight": 100
        },
        {
          "type": "item",
          "name": "minecraft:golden_apple",
          "weight": 75
        },
        {
          "type": "item",
          "name": "minecraft:appleEnchanted",
          "weight": 10
        },
        {
          "type": "item",
          "name": "minecraft:record_13",
          "weight": 75
        },
        {
          "type": "item",
          "name": "minecraft:record_cat",
          "weight": 75
        },
        {
          "type": "item",
          "name": "minecraft:name_tag",
          "weight": 100
        },
        {
          "type": "item",
          "name": "minecraft:chainmail_chestplate",
          "weight": 50
        },
        {
          "type": "item",
          "name": "minecraft:diamond_hoe",
          "weight": 75
        },
        {
          "type": "item",
          "name": "minecraft:diamond_chestplate",
          "weight": 25
        },
        {
          "type": "item",
          "name": "effect:emerald_sword",
          "weight": 25
        },
        {
          "type": "item",
          "name": "minecraft:book",
          "weight": 60,
          "functions": [
            {
              "function": "enchant_randomly",
              "treasure": true
            }
          ]
        }
      ]
    },
    {
      "rolls": {
        "min": 1,
        "max": 4
      },
      "entries": [
        {
          "type": "item",
          "name": "minecraft:iron_ingot",
          "weight": 50,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 4
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:gold_ingot",
          "weight": 25,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 4
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:bread",
          "weight": 100
        },
        {
          "type": "item",
          "name": "minecraft:wheat",
          "weight": 100,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 4
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:bucket",
          "weight": 50
        },
        {
          "type": "item",
          "name": "minecraft:redstone",
          "weight": 75,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 4
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:coal",
          "weight": 75,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 4
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:melon_seeds",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 2,
                "max": 4
              }
            }
          ],
          "weight": 50
        },
        {
          "type": "item",
          "name": "minecraft:pumpkin_seeds",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 2,
                "max": 4
              }
            }
          ],
          "weight": 50
        },
        {
          "type": "item",
          "name": "minecraft:beetroot_seeds",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 2,
                "max": 4
              }
            }
          ],
          "weight": 50
        }
      ]
    },
    {
      "rolls": 3,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:bone",
          "weight": 50,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 8
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:gunpowder",
          "weight": 50,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 8
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:rotten_flesh",
          "weight": 50,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 8
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:string",
          "weight": 50,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 8
              }
            }
          ]
        }
      ]
    }
  ]
}
```


### Одноимённые группы и события игрока (`Swords_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:emerald_sword": {
      "minecraft:type_family": {
        "family": [
          "player",
          "emerald_sword"
        ]
      }
    }
  },
  "events": {
    "minecraft:emerald_sword": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "!=",
            "value": "emerald_sword"
          },
          "add": {
            "component_groups": [
              "minecraft:emerald_sword"
            ]
          }
        },
        {
          "filters": {
            "all_of": [
              {
                "test": "is_in_village",
                "subject": "self",
                "value": true
              }
            ]
          },
          "run_command": {
            "command": [
              "effect @s village_hero 1 0 true",
              "effect @e[family=villager,r=64] resistance 1 1 true"
            ]
          }
        }
      ]
    },
    "stop_emerald_sword_event": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "==",
            "value": "emerald_sword"
          },
          "run_command": {
            "command": [
              "effect @s village_hero 0 0 true"
            ]
          },
          "remove": {
            "component_groups": [
              "minecraft:emerald_sword"
            ]
          },
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          }
        }
      ]
    }
  }
}
```

## effect:ender_sword

- Название в en_US: `§l§5Ender Sword`
- Определение: `Swords_B/items/ender_sword.json`
- Урон (`minecraft:damage`): `9`
- Прочность (`minecraft:durability`): `{"max_durability":1256}`
- Кулдаун (`minecraft:cooldown`): `{"category":"ender_sword","duration":2}`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:ender_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": true,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 1256
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "ender_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:ender_sword"
          ],
          "repair_amount": 1256
        },
        {
          "items": [
            "minecraft:ender_pearl"
          ],
          "repair_amount": 28
        },
        {
          "items": [
            "minecraft:ender_eye"
          ],
          "repair_amount": 32
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:render_offsets": {
      "main_hand": {
        "first_person": {
          "position": [
            1,
            0.4,
            -3
          ],
          "scale": [
            0.04,
            0.04,
            0.04
          ]
        },
        "third_person": {
          "position": [
            0.5,
            1.6,
            -0.8
          ],
          "scale": [
            0.038,
            0.038,
            0.038
          ]
        }
      }
    },
    "minecraft:display_name": {},
    "minecraft:damage": 9,
    "minecraft:cooldown": {
      "category": "ender_sword",
      "duration": 2
    },
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "on_use": {
      "run_command": {
        "command": [
          "spreadplayers ~ ~ 16 32 @s",
          "playsound mob.endermen.portal @a[r=34]"
        ]
      },
      "damage": {
        "type": "durability",
        "amount": 5,
        "target": "self"
      }
    },
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/animation_controllers/item_events.json`: строки 18
- `Swords_B/entities/player.json`: строки 147, 152, 158, 164, 179, 181, 943, 945, 950, 952, 1416, 1419, 1420, 1428, 1431, 1432, 1437, 1444, 1446
- `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/tag_swords.mcfunction`: строки 5
- `Swords_B/functions/give.mcfunction`: строки 7
- `Swords_B/loot_tables/entities/red_enderman.json`: строки 18
- `Swords_R/texts/en_US.lang`: строки 29, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608
- `Swords_R/textures/item_texture.json`: строки 62, 63
- `Swords_R/ui/how_to_play_screen.json`: строки 68, 127, 998, 1000, 1001, 1004, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018

### Рецепты и таблицы добычи с точным ID

`Swords_B/loot_tables/entities/red_enderman.json`:

```json
{
  "pools": [
    {
      "conditions": [
        {
          "condition": "killed_by_player"
        },
        {
          "condition": "random_chance_with_looting",
          "chance": 0.025,
          "looting_multiplier": 0.02
        }
      ],
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "effect:ender_sword",
          "weight": 1,
          "functions": [
            {
              "function": "set_data",
              "data": 0
            }
          ]
        }
      ]
    }
  ]
}
```


### Одноимённые группы и события игрока (`Swords_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:ender_sword": {
      "minecraft:damage_sensor": {
        "triggers": [
          {
            "on_damage": {
              "filters": {
                "all_of": [
                  {
                    "test": "has_damage",
                    "subject": "self",
                    "operator": "!=",
                    "value": "projectile"
                  }
                ]
              },
              "event": "ender_sword_skill"
            },
            "deals_damage": true
          },
          {
            "on_damage": {
              "filters": {
                "all_of": [
                  {
                    "test": "has_damage",
                    "subject": "self",
                    "value": "projectile"
                  }
                ]
              },
              "event": "ender_sword_tp"
            },
            "deals_damage": false
          },
          {
            "on_damage": {
              "filters": {
                "all_of": [
                  {
                    "test": "in_water_or_rain"
                  }
                ]
              },
              "event": "ender_sword_tp"
            },
            "deals_damage": true
          }
        ]
      },
      "minecraft:hurt_on_condition": {
        "damage_conditions": [
          {
            "filters": {
              "test": "in_water_or_rain"
            },
            "cause": "drowning",
            "damage_per_tick": 1
          }
        ]
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "ender_sword"
        ]
      },
      "minecraft:timer": {
        "time": [
          6,
          18
        ],
        "looping": true,
        "randomInterval": true,
        "time_down_event": {
          "event": "ender_sword_sound",
          "target": "self"
        }
      }
    }
  },
  "events": {
    "minecraft:ender_sword": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "!=",
            "value": "ender_sword"
          },
          "add": {
            "component_groups": [
              "minecraft:ender_sword"
            ]
          },
          "run_command": {
            "command": [
              "playsound mob.endermen.portal @a[r=8] ~ ~ ~"
            ]
          }
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:end_chest ~ ~0.6 ~"
            ]
          }
        }
      ]
    },
    "stop_ender_sword_event": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "==",
            "value": "ender_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:ender_sword"
            ]
          },
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          }
        }
      ]
    },
    "ender_sword_sound": {
      "randomize": [
        {
          "weight": 1,
          "run_command": {
            "command": [
              "playsound mob.endermen.scream @a[r=8] ~ ~ ~"
            ]
          }
        },
        {
          "weight": 1,
          "run_command": {
            "command": [
              "playsound mob.endermen.idle @a[r=8] ~ ~ ~"
            ]
          }
        },
        {
          "weight": 1,
          "run_command": {
            "command": [
              "playsound mob.endermen.stare @a[r=8] ~ ~ ~"
            ]
          }
        }
      ]
    },
    "ender_sword_tp": {
      "run_command": {
        "command": [
          "spreadplayers ~ ~ 0 16 @s",
          "playsound mob.endermen.portal @a[r=17]"
        ]
      }
    },
    "ender_sword_skill": {
      "sequence": [
        {
          "run_command": {
            "command": [
              "playsound mob.endermen.hit @a[r=8] ~ ~ ~"
            ]
          }
        },
        {
          "randomize": [
            {
              "weight": 50
            },
            {
              "weight": 50,
              "run_command": {
                "command": [
                  "spreadplayers ~ ~ 0 16 @s",
                  "playsound mob.endermen.portal @a[r=17]"
                ]
              }
            }
          ]
        }
      ]
    }
  }
}
```

## effect:fire_sword

- Название в en_US: `§l§6Fire Sword`
- Определение: `Swords_B/items/fire_sword.json`
- Урон (`minecraft:damage`): `6`
- Прочность (`minecraft:durability`): `{"max_durability":2000}`
- Кулдаун (`minecraft:cooldown`): `{"category":"fire_sword","duration":25}`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:fire_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": true,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 2000
    },
    "minecraft:cooldown": {
      "category": "fire_sword",
      "duration": 25
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "fire_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:fire_sword"
          ],
          "repair_amount": 2000
        },
        {
          "items": [
            "minecraft:fire"
          ],
          "repair_amount": 1000
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 6,
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "on_use": {
      "sequence": [
        {
          "run_command": {
            "command": [
              "summon entity:living_flame ~ ~14 ~ minecraft:target",
              "summon entity:living_flame ~ ~4 ~ fire_sword_skill",
              "summon entity:living_flame ~3 ~4 ~ fire_sword_skill",
              "summon entity:living_flame ~ ~4 ~3 fire_sword_skill",
              "summon entity:living_flame ~-3 ~4 ~ fire_sword_skill",
              "summon entity:living_flame ~ ~4 ~-3 fire_sword_skill",
              "particle minecraft:example_linearcurve ~ ~0.2 ~",
              "title @s actionbar §l§6Fire rain"
            ],
            "target": "holder"
          }
        },
        {
          "damage": {
            "type": "durability",
            "amount": 20,
            "target": "self"
          }
        }
      ]
    },
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        },
        {
          "randomize": [
            {
              "weight": 85,
              "shoot": {
                "projectile": "entity:fire",
                "launch_power": 1
              }
            },
            {
              "weight": 15,
              "shoot": {
                "projectile": "entity:living_flame",
                "launch_power": 1
              }
            }
          ]
        }
      ]
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/animation_controllers/item_events.json`: строки 15, 23
- `Swords_B/entities/fire.json`: строки 12, 51, 53
- `Swords_B/entities/item.json`: строки 25, 27, 29, 38, 42, 48, 51, 57, 60, 184, 216, 219, 220, 227, 228, 229, 230, 233
- `Swords_B/entities/living_flame.json`: строки 11, 15, 176, 187, 204, 270
- `Swords_B/entities/player.json`: строки 323, 325, 332, 698, 700, 705, 707, 2054, 2057, 2058, 2075, 2078, 2079, 2084
- `Swords_B/entities/small_fireball.json`: строки 122
- `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/tag_swords.mcfunction`: строки 1
- `Swords_B/functions/give.mcfunction`: строки 8
- `Swords_B/loot_tables/entities/living_flame.json`: строки 8
- `Swords_B/recipes/fire_sword.json`: строки 5, 22
- `Swords_R/texts/en_US.lang`: строки 24, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560
- `Swords_R/textures/item_texture.json`: строки 47, 48
- `Swords_R/ui/how_to_play_screen.json`: строки 65, 124, 916, 918, 919, 922, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941

### Рецепты и таблицы добычи с точным ID

`Swords_B/loot_tables/entities/living_flame.json`:

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "effect:fire_sword",
          "weight": 1,
          "functions": [
            {
              "function": "set_data",
              "data": 0
            }
          ]
        }
      ]
    }
  ]
}
```

`Swords_B/recipes/fire_sword.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect:fire_sword"
    },  
    "tags": [ "crafting_table" ],
    "pattern": [
      "F",
      "F",
      "#"
    ],
    "key": {
      "#": {
        "item": "minecraft:blaze_rod"
      },
      "F": {
        "item": "minecraft:fire"
      }
    },
    "result": {
      "item": "effect:fire_sword"
    }
  }
}
```


### Одноимённые группы и события игрока (`Swords_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:fire_sword": {
      "minecraft:timer": {
        "time": [
          0.2,
          0.7
        ],
        "looping": true,
        "randomInterval": true,
        "time_down_event": {
          "event": "fire_sword_sound",
          "target": "self"
        }
      },
      "minecraft:damage_sensor": {
        "triggers": {
          "on_damage": {
            "filters": {
              "any_of": [
                {
                  "test": "has_damage",
                  "subject": "self",
                  "value": "fire"
                },
                {
                  "test": "has_damage",
                  "subject": "self",
                  "value": "fire_tick"
                }
              ]
            }
          },
          "deals_damage": false
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "fire_sword"
        ]
      }
    }
  },
  "events": {
    "minecraft:fire_sword": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "!=",
            "value": "fire_sword"
          },
          "add": {
            "component_groups": [
              "minecraft:fire_sword"
            ]
          }
        },
        {
          "run_command": {
            "command": [
              "fill ~3 ~3 ~3 ~-3 ~-3 ~-3 air 0 replace snow_layer",
              "fill ~3 ~3 ~3 ~-3 ~-3 ~-3 water 0 replace ice",
              "fill ~3 ~3 ~3 ~-3 ~-3 ~-3 water 0 replace blue_ice",
              "fill ~3 ~3 ~3 ~-3 ~-3 ~-3 water 0 replace packed_ice",
              "execute @e[family=!player,type=!item,r=3] ~ ~ ~ summon entity:fire",
              "fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock 0 replace air",
              "fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock 0 replace effect99:lightblock"
            ]
          }
        }
      ]
    },
    "stop_fire_sword_event": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "==",
            "value": "fire_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:fire_sword"
            ]
          },
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          }
        }
      ]
    },
    "fire_sword_sound": {
      "run_command": {
        "command": [
          "playsound fire.fire @a[r=8]"
        ]
      }
    }
  }
}
```

## effect:ghost_sword

- Название в en_US: `§l§fGhost Sword`
- Определение: `Swords_B/items/ghost_sword.json`
- Урон (`minecraft:damage`): `-666`
- Прочность (`minecraft:durability`): `{"max_durability":3333}`
- Кулдаун (`minecraft:cooldown`): `{"category":"ghost_sword","duration":2}`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:ghost_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": true,
    "minecraft:should_despawn": false,
    "minecraft:max_stack_size": 1,
    "minecraft:durability": {
      "max_durability": 3333
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "ghost_sword"
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:render_offsets": {
      "main_hand": {
        "first_person": {
          "position": [
            0.67,
            0,
            -1.24
          ]
        },
        "third_person": {
          "position": [
            0.36,
            1.5,
            -0.66
          ]
        }
      }
    },
    "minecraft:cooldown": {
      "category": "ghost_sword",
      "duration": 2
    },
    "minecraft:display_name": {},
    "minecraft:damage": -666,
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "on_use": {
      "shoot": {
        "projectile": "entity:ghost_projectile",
        "launch_power": 1
      },
      "damage": {
        "type": "durability",
        "amount": 6,
        "target": "self"
      }
    },
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/animation_controllers/ghost_sword.json`: строки 4, 9, 12
- `Swords_B/entities/ghost.json`: строки 40, 122, 145, 148
- `Swords_B/entities/player.json`: строки 10, 18, 47, 62, 999, 1001, 1006, 1008, 1216, 1219, 1220, 1261, 1264, 1265
- `Swords_B/functions/give.mcfunction`: строки 32
- `Swords_R/entity/player.entity.json`: строки 59
- `Swords_R/sounds/sound_definitions.json`: строки 18, 22
- `Swords_R/texts/en_US.lang`: строки 41, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526
- `Swords_R/textures/item_texture.json`: строки 107, 108
- `Swords_R/ui/how_to_play_screen.json`: строки 63, 122, 860, 862, 863, 866, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887

### Одноимённые группы и события игрока (`Swords_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:ghost_sword": {
      "minecraft:scale": {
        "value": 1.05
      },
      "minecraft:knockback_resistance": {
        "value": 1.0
      },
      "minecraft:collision_box": {
        "width": 0.0,
        "height": 0.0
      },
      "minecraft:breathable": {
        "total_supply": 15,
        "suffocate_time": 0,
        "inhale_time": 3.75,
        "generates_bubbles": false,
        "breathes_water": true,
        "breathes_air": true,
        "breathes_lava": true
      },
      "minecraft:damage_sensor": {
        "triggers": {
          "cause": "all",
          "deals_damage": false
        }
      },
      "minecraft:type_family": {
        "family": [
          "ghost_sword"
        ]
      }
    }
  },
  "events": {
    "minecraft:ghost_sword": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "!=",
            "value": "ghost_sword"
          },
          "add": {
            "component_groups": [
              "minecraft:ghost_sword"
            ]
          },
          "run_command": {
            "command": [
              "particle minecraft:egg_destroy_emitter ~ ~ ~",
              "particle minecraft:egg_destroy_emitter ~ ~0.3 ~",
              "particle minecraft:egg_destroy_emitter ~ ~0.6 ~",
              "particle minecraft:egg_destroy_emitter ~ ~0.9 ~",
              "particle minecraft:egg_destroy_emitter ~ ~1.2 ~",
              "particle minecraft:egg_destroy_emitter ~ ~1.5 ~",
              "playsound mob.wither.ambient @a[r=16] ~ ~1 ~ 2 0.3"
            ]
          }
        },
        {
          "run_command": {
            "command": [
              "effect @s slow_falling 1 0 true",
              "effect @s saturation 1 1 true"
            ]
          },
          "add": {
            "component_groups": [
              "ghost_movement"
            ]
          }
        },
        {
          "filters": {
            "test": "in_water"
          },
          "run_command": {
            "command": [
              "effect @s levitation 1 0 true"
            ]
          }
        },
        {
          "filters": {
            "test": "in_lava"
          },
          "run_command": {
            "command": [
              "effect @s levitation 1 0 true",
              "effect @s fire_resistance 1 0 true"
            ]
          }
        },
        {
          "filters": {
            "test": "in_lava",
            "operator": "!="
          },
          "run_command": {
            "command": [
              "effect @s fire_resistance 0 0"
            ]
          }
        },
        {
          "randomize": [
            {
              "weight": 90
            },
            {
              "weight": 10,
              "run_command": {
                "command": [
                  "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 0.15 0.2"
                ]
              }
            }
          ]
        }
      ]
    },
    "stop_ghost_sword_event": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "==",
            "value": "ghost_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:ghost_sword"
            ]
          },
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "run_command": {
            "command": [
              "effect @s slow_falling 0 0",
              "stopsound @a[r=18] mob.wither.spawn",
              "playsound mob.wither.ambient @a[r=16] ~ ~1 ~ 2 0.2",
              "particle minecraft:egg_destroy_emitter ~ ~ ~",
              "particle minecraft:egg_destroy_emitter ~ ~0.3 ~",
              "particle minecraft:egg_destroy_emitter ~ ~0.6 ~",
              "particle minecraft:egg_destroy_emitter ~ ~0.9 ~",
              "particle minecraft:egg_destroy_emitter ~ ~1.2 ~",
              "particle minecraft:egg_destroy_emitter ~ ~1.5 ~",
              "particle minecraft:ghost_spiral ~~~"
            ]
          }
        }
      ]
    }
  }
}
```

## effect:glass_sword

- Название в en_US: `§l§bGlass Sword`
- Определение: `Swords_B/items/glass_sword.json`
- Урон (`minecraft:damage`): `33`
- Прочность (`minecraft:durability`): `{"max_durability":1}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:glass_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 1
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "glass_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:glass_sword"
          ],
          "repair_amount": 1
        },
        {
          "items": [
            "minecraft:glass"
          ],
          "repair_amount": 1
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 25,
          "on_dig": {
            "event": "weapon"
          }
        },
        {
          "block": "minecraft:bamboo",
          "speed": 15,
          "on_dig": {
            "event": "weapon"
          }
        }
      ],
      "on_dig": {
        "event": "weapon"
      }
    },
    "minecraft:display_name": {},
    "minecraft:damage": 33,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 10,
            "target": "self"
          },
          "run_command": {
            "command": [
              "playsound random.glass @a[r=8,m=0]"
            ]
          }
        }
      ]
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/entities/item.json`: строки 229
- `Swords_B/functions/give.mcfunction`: строки 30
- `Swords_R/texts/en_US.lang`: строки 34, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191
- `Swords_R/textures/item_texture.json`: строки 95, 96
- `Swords_R/ui/how_to_play_screen.json`: строки 41, 100, 332, 334, 335, 338, 340, 341, 342, 343, 344, 345, 346, 347

## effect:glowstone_sword

- Название в en_US: `§l§gGlowstone Sword`
- Определение: `Swords_B/items/glowstone_sword.json`
- Урон (`minecraft:damage`): `4`
- Прочность (`minecraft:durability`): `{"max_durability":128}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:glowstone_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": true,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 128
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "glowstone_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:glowstone_sword"
          ],
          "repair_amount": 128
        },
        {
          "items": [
            "minecraft:glowstone"
          ],
          "repair_amount": 64
        },
        {
          "items": [
            "minecraft:glowstone_dust"
          ],
          "repair_amount": 16
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 4,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/blocks/lightblock.json`: строки 22, 28
- `Swords_B/entities/player.json`: строки 922, 924, 1489
- `Swords_B/functions/give.mcfunction`: строки 9
- `Swords_B/recipes/glowstone_sword.json`: строки 5, 22
- `Swords_R/texts/en_US.lang`: строки 21, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180
- `Swords_R/textures/item_texture.json`: строки 38, 39
- `Swords_R/ui/how_to_play_screen.json`: строки 40, 99, 311, 313, 314, 317, 319, 320, 321, 322, 323, 324, 325, 326, 327

### Рецепты и таблицы добычи с точным ID

`Swords_B/recipes/glowstone_sword.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect:glowstone_sword"
    },  
    "tags": [ "crafting_table" ],
    "pattern": [
      "2",
      "2",
      "1"
    ],
    "key": {
      "1": {
        "item": "minecraft:blaze_rod"
      },
      "2": {
        "item": "minecraft:glowstone"   
      }
    },
    "result": {
      "item": "effect:glowstone_sword"
    }
  }
}
```


### Одноимённые группы и события игрока (`Swords_B/entities/player.json`)

```json
{
  "events": {
    "minecraft:glowstone_sword": {
      "run_command": {
        "command": [
          "fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock 0 replace air",
          "fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock 0 replace effect99:lightblock"
        ]
      }
    }
  }
}
```

## effect:grass_sword

- Название в en_US: `§l§2Grass Sword`
- Определение: `Swords_B/items/grass_sword.json`
- Урон (`minecraft:damage`): `8`
- Прочность (`minecraft:durability`): `{"max_durability":250}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:grass_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 250
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "grass_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:grass_sword"
          ],
          "repair_amount": 250
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:render_offsets": {
      "main_hand": {
        "first_person": {
          "position": [
            0.8,
            0.15,
            -1.74
          ]
        },
        "third_person": {
          "position": [
            0.69,
            2.5,
            -0.96
          ]
        }
      }
    },
    "minecraft:display_name": {},
    "minecraft:damage": 8,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/entities/grass.json`: строки 18, 20, 34, 44
- `Swords_B/entities/player.json`: строки 317, 318, 320, 712, 714, 719, 721, 2023, 2026, 2027, 2039, 2042, 2043, 2048
- `Swords_B/entities/witch.json`: строки 28, 213, 220
- `Swords_B/functions/give.mcfunction`: строки 10
- `Swords_R/texts/en_US.lang`: строки 18, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342
- `Swords_R/textures/item_texture.json`: строки 71, 72
- `Swords_R/ui/how_to_play_screen.json`: строки 52, 111, 582, 584, 585, 588, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600

### Одноимённые группы и события игрока (`Swords_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:grass_sword": {
      "minecraft:type_family": {
        "family": [
          "player",
          "grass_sword"
        ]
      },
      "minecraft:timer": {
        "time": [
          0.2,
          0.2
        ],
        "looping": true,
        "time_down_event": {
          "event": "grass_sword_skills",
          "target": "self"
        }
      }
    }
  },
  "events": {
    "minecraft:grass_sword": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "!=",
            "value": "grass_sword"
          },
          "add": {
            "component_groups": [
              "minecraft:grass_sword"
            ]
          }
        },
        {
          "run_command": {
            "command": [
              "tag @e[tag=grass,rm=9,r=10] remove grass",
              "fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 grass 0 replace dirt",
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 fill ~ ~ ~ ~ ~ ~ tallgrass 0 replace air"
            ]
          }
        }
      ]
    },
    "stop_grass_sword_event": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "==",
            "value": "grass_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:grass_sword"
            ]
          },
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          }
        }
      ]
    },
    "grass_sword_skills": {
      "run_command": {
        "command": [
          "execute @e[type=!player,type=!item,type=!entity:grass,type=!xp_orb,type=!arrow,r=8,tag=!grass] ~ ~ ~ detect ~ ~-0.1 ~ grass 0 execute @s ~ ~ ~ detect ~ ~ ~ air 0 summon entity:grass",
          "execute @e[type=!player,type=!item,type=!entity:grass,type=!xp_orb,type=!arrow,r=8,tag=!grass] ~ ~ ~ detect ~ ~-0.1 ~ grass 0 execute @s ~ ~ ~ detect ~ ~ ~ tallgrass 0 summon entity:grass"
        ]
      }
    }
  }
}
```

## effect:ice_sword

- Название в en_US: `§l§bIce Sword`
- Определение: `Swords_B/items/ice_sword.json`
- Урон (`minecraft:damage`): `8.5`
- Прочность (`minecraft:durability`): `{"max_durability":500}`
- Кулдаун (`minecraft:cooldown`): `{"category":"ice_sword","duration":5}`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:ice_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": true,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 500
    },
    "minecraft:cooldown": {
      "category": "ice_sword",
      "duration": 5
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "ice_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:ice_sword"
          ],
          "repair_amount": 500
        },
        {
          "items": [
            "minecraft:ice"
          ],
          "repair_amount": 55
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 8.5,
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "on_use": {
      "sequence": [
        {
          "run_command": {
            "command": [
              "execute @e[type=!enderman,type=!horse,type=!slime,type=!silverfish,type=!spider,type=!cave_spider,type=!tnt,type=!vex,type=!chicken,type=!pig,type=!wolf,type=!cat,type=!item,type=!xp_orb,type=!xp_bottle,type=!egg,type=!snowball,type=!fireball,type=!small_fireball,type=!eye_of_ender_signal,type=!ender_pearl,type=!fishing_hook,type=!falling_block,type=!lightning_bolt,type=!lingering_potion,type=!dragon_fireball,type=!ender_dragon,type=!endermite,type=!arrow,type=!thrown_trident,type=!leash_knot,type=!bat,type=!rabbit,type=!parrot,type=!ghast,type=!shulker,type=!elder_guardian,type=!guardian,type=!turtle,type=!fox,type=!squid,type=!ocelot,type=!phantom,type=!area_effect_cloud,family=!fish,family=!effect99_entities,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=enderman,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~3 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[family=slime_large,rm=2,r=12] ~ ~ ~ fill ~2 ~-1 ~2 ~-2 ~3 ~-2 effect99:fake_ice 0 replace air 0",
              "execute @e[family=slime_large,rm=2,r=12] ~ ~1 ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 air 0 replace effect99:fake_ice",
              "execute @e[family=slime_medium,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[family=slime_medium,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ air 0 replace effect99:fake_ice",
              "execute @e[family=slime_small,rm=2,r=12] ~ ~ ~ fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[family=slime_small,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ air 0 replace effect99:fake_ice",
              "execute @e[type=silverfish,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ effect99:fake_ice 0 replace air 0",
              "execute @e[type=spider,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=cave_spider,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=tnt,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=vex,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=chicken,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=pig,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=wolf,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=cat,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=small_fireball,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ effect99:fake_ice 0 replace air 0",
              "execute @e[type=fireball,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ effect99:fake_ice 0 replace air 0",
              "execute @e[type=arrow,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ effect99:fake_ice 0 replace air 0",
              "execute @e[type=lingering_potion,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ effect99:fake_ice 0 replace air 0",
              "execute @e[type=dragon_fireball,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ effect99:fake_ice 0 replace air 0",
              "execute @e[type=thrown_trident,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ effect99:fake_ice 0 replace air 0",
              "execute @e[type=endermite,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=rabbit,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=parrot,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=phantom,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=shulker,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=guardian,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=ocelot,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=turtle,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=fox,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=squid,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=elder_guardian,rm=2,r=12] ~ ~ ~ fill ~2 ~-1 ~2 ~-2 ~3 ~-2 effect99:fake_ice 0 replace air 0",
              "execute @e[type=bat,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=ghast,rm=2,r=12] ~ ~ ~ fill ~4 ~-3 ~4 ~-4 ~4 ~-4 effect99:fake_ice 0 replace air 0",
              "execute @e[type=ghast,rm=2,r=12] ~ ~ ~ fill ~3 ~-2 ~3 ~-3 ~3 ~-3 air 0 replace effect99:fake_ice",
              "execute @e[type=horse,rm=2,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 effect99:fake_ice 0 replace air 0",
              "execute @e[type=horse,rm=2,r=12] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ air 0 replace effect99:fake_ice 0",
              "execute @e[type=player,rm=3,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 effect99:fake_ice 0 replace air 0",
              "title @s actionbar §l§bIce Skill",
              "playsound random.fizz @a[r=12] ~ ~ ~ 1 2.3",
              "particle minecraft:knockback_roar_particle ~ ~1 ~"
            ],
            "target": "holder"
          }
        },
        {
          "damage": {
            "type": "durability",
            "amount": 6,
            "target": "self"
          }
        }
      ]
    },
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        },
        {
          "randomize": [
            {
              "weight": 70
            },
            {
              "weight": 30,
              "shoot": {
                "projectile": "minecraft:snowball",
                "launch_power": 1
              },
              "run_command": {
                "command": [
                  "playsound random.bow @a[r=10] ~ ~ ~ 1 0.4"
                ]
              }
            }
          ]
        }
      ]
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/animation_controllers/item_events.json`: строки 17
- `Swords_B/entities/player.json`: строки 302, 303, 754, 756, 761, 763, 1920, 1923, 1924, 1952, 1955, 1956
- `Swords_B/entities/snowball.json`: строки 11, 17, 74, 78, 79
- `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/tag_swords.mcfunction`: строки 3
- `Swords_B/functions/give.mcfunction`: строки 11
- `Swords_B/loot_tables/chests/igloo_chest.json`: строки 68
- `Swords_B/loot_tables/chests/village/village_snowy_house.json`: строки 108
- `Swords_R/texts/en_US.lang`: строки 19, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410
- `Swords_R/textures/item_texture.json`: строки 74, 75
- `Swords_R/ui/how_to_play_screen.json`: строки 56, 115, 684, 686, 687, 690, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706

### Рецепты и таблицы добычи с точным ID

`Swords_B/loot_tables/chests/igloo_chest.json`:

```json
{
  "pools": [
    {
      "rolls": {
        "min": 2,
        "max": 8
      },
      "entries": [
        {
          "type": "item",
          "name": "minecraft:apple",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:coal",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 4
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:gold_nugget",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:stone_axe",
          "weight": 2
        },
        {
          "type": "item",
          "name": "minecraft:rotten_flesh",
          "weight": 10
        },
        {
          "type": "item",
          "name": "minecraft:emerald",
          "weight": 1
        },
        {
          "type": "item",
          "name": "effect:ice_sword",
          "weight": 1
        },
        {
          "type": "item",
          "name": "minecraft:wheat",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 3
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:golden_apple",
          "weight": 1
        }
      ]
    }
  ]
}
```

`Swords_B/loot_tables/chests/village/village_snowy_house.json`:

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "min": 3,
        "max": 8
      },
      "entries": [
        {
          "type": "item",
          "name": "minecraft:blue_ice"
        },
        {
          "type": "item",
          "weight": 4,
          "name": "minecraft:snow"
        },
        {
          "type": "item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 7
              }
            }
          ],
          "name": "minecraft:potato"
        },
        {
          "type": "item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 4
              }
            }
          ],
          "name": "minecraft:bread"
        },
        {
          "type": "item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 5
              }
            }
          ],
          "name": "minecraft:beetroot_seeds"
        },
        {
          "type": "item",
          "name": "minecraft:beetroot_soup"
        },
        {
          "type": "item",
          "name": "minecraft:furnace"
        },
        {
          "type": "item",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 4
              }
            }
          ],
          "name": "minecraft:emerald"
        },
        {
          "type": "item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 7
              }
            }
          ],
          "name": "minecraft:snowball"
        },
        {
          "type": "item",
          "weight": 4,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 1
              }
            }
          ],
          "name": "effect:ice_sword"
        },
        {
          "type": "item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 4
              }
            }
          ],
          "name": "minecraft:coal"
        }
      ]
    }
  ]
}
```


### Одноимённые группы и события игрока (`Swords_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:ice_sword": {
      "minecraft:type_family": {
        "family": [
          "player",
          "ice_sword"
        ]
      }
    }
  },
  "events": {
    "minecraft:ice_sword": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "!=",
            "value": "ice_sword"
          },
          "add": {
            "component_groups": [
              "minecraft:ice_sword"
            ]
          }
        },
        {
          "filters": {
            "all_of": [
              {
                "test": "in_lava"
              },
              {
                "test": "has_biome_tag",
                "operator": "!=",
                "value": "nether"
              }
            ]
          },
          "run_command": {
            "command": [
              "playsound random.fizz @a[r=10] ~ ~ ~",
              "setblock ~ ~ ~ flowing_water",
              "replaceitem entity @s slot.weapon.mainhand 0 air 1 0",
              "particle minecraft:cauldron_explosion_emitter ~ ~ ~"
            ]
          }
        },
        {
          "filters": {
            "all_of": [
              {
                "test": "in_lava"
              },
              {
                "test": "has_biome_tag",
                "value": "nether"
              }
            ]
          },
          "run_command": {
            "command": [
              "playsound random.fizz @a[r=10] ~ ~ ~",
              "replaceitem entity @s slot.weapon.mainhand 0 air 1 0",
              "particle minecraft:cauldron_explosion_emitter ~ ~ ~"
            ]
          }
        },
        {
          "run_command": {
            "command": [
              "fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 effect99:fake_ice 0 replace water",
              "fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 effect99:fake_ice 0 replace flowing_water",
              "fill ~3 ~-1 ~ ~3 ~-1 ~ effect99:fake_ice 0 replace water",
              "fill ~3 ~-1 ~ ~3 ~-1 ~ effect99:fake_ice 0 replace flowing_water",
              "fill ~ ~-1 ~3 ~ ~-1 ~3 effect99:fake_ice 0 replace water",
              "fill ~ ~-1 ~3 ~ ~-1 ~3 effect99:fake_ice 0 replace flowing_water",
              "fill ~-3 ~-1 ~ ~-3 ~-1 ~ effect99:fake_ice 0 replace water",
              "fill ~-3 ~-1 ~ ~-3 ~-1 ~ effect99:fake_ice 0 replace flowing_water",
              "fill ~ ~-1 ~-3 ~ ~-1 ~-3 effect99:fake_ice 0 replace water",
              "fill ~ ~-1 ~-3 ~ ~-1 ~-3 effect99:fake_ice 0 replace flowing_water",
              "execute @e[r=64,type=!player] ~ ~ ~ detect ~ ~ ~ effect99:fake_ice 0 tp @s ~ ~ ~ ~1"
            ]
          }
        }
      ]
    },
    "stop_ice_sword_event": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "==",
            "value": "ice_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:ice_sword"
            ]
          },
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          }
        }
      ]
    }
  }
}
```

## effect:jungle_sword

- Название в en_US: `§l§2Jungle Sword`
- Определение: `Swords_B/items/jungle_sword.json`
- Урон (`minecraft:damage`): `4`
- Прочность (`minecraft:durability`): `{"max_durability":128}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:jungle_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 128
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:block_placer": {
      "block": "effect99:sapling3",
      "use_on": [
        "dirt",
        "grass"
      ]
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "jungle_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:jungle_sword"
          ],
          "repair_amount": 128
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 4,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/entities/parrot.json`: строки 103
- `Swords_B/entities/player.json`: строки 313, 314, 726, 728, 733, 735, 2001, 2004, 2005, 2008, 2012, 2015, 2016
- `Swords_B/functions/give.mcfunction`: строки 12
- `Swords_B/loot_tables/chests/jungle_temple.json`: строки 114
- `Swords_B/loot_tables/gameplay/fishing/treasure.json`: строки 28
- `Swords_R/texts/en_US.lang`: строки 11, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204
- `Swords_R/textures/item_texture.json`: строки 17, 18
- `Swords_R/ui/how_to_play_screen.json`: строки 42, 101, 352, 354, 355, 358, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369

### Рецепты и таблицы добычи с точным ID

`Swords_B/loot_tables/chests/jungle_temple.json`:

```json
{
  "pools": [
    {
      "rolls": {
        "min": 2,
        "max": 6
      },
      "entries": [
        {
          "type": "item",
          "name": "minecraft:diamond",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "weight": 15
        },
        {
          "type": "item",
          "name": "minecraft:iron_ingot",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 5
              }
            }
          ],
          "weight": 50
        },
        {
          "type": "item",
          "name": "minecraft:gold_ingot",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 2,
                "max": 7
              }
            }
          ],
          "weight": 75
        },
        {
          "type": "item",
          "name": "minecraft:emerald",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "weight": 10
        },
        {
          "type": "item",
          "name": "minecraft:bone",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 4,
                "max": 6
              }
            }
          ],
          "weight": 100
        },
        {
          "type": "item",
          "name": "minecraft:rotten_flesh",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 3,
                "max": 7
              }
            }
          ],
          "weight": 80
        },
        {
          "type": "item",
          "name": "minecraft:bamboo",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "weight": 75
        },
        {
          "type": "item",
          "name": "minecraft:saddle",
          "weight": 15
        },
        {
          "type": "item",
          "name": "effect:jungle_sword",
          "weight": 16
        },
        {
          "type": "item",
          "name": "minecraft:horsearmoriron",
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:horsearmorgold",
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:horsearmordiamond",
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:book",
          "weight": 6,
          "functions": [
            {
              "function": "enchant_with_levels",
              "levels": 30,
              "treasure": true
            }
          ]
        }
      ]
    }
  ]
}
```

`Swords_B/loot_tables/gameplay/fishing/treasure.json`:

```json
{
    "pools": [
        {
            "rolls": 1,
            "entries": [
                {
                    "type": "item",
                    "name": "minecraft:nautilus_shell",
                    "weight": 5
                },
                {
                    "type": "item",
                    "name": "minecraft:waterlily",
                    "weight": 5
                },
                {
                    "type": "item",
                    "name": "minecraft:name_tag",
                    "weight": 5
                },
                {
                    "type": "item",
                    "name": "minecraft:saddle",
                    "weight": 5
                },
                {
                    "type": "item",
                    "name": "effect:jungle_sword",
                    "weight": 5
                },
                {
                    "type": "item",
                    "name": "minecraft:bow",
                    "weight": 5,
                    "functions": [
                        {
                            "function": "set_damage",
                            "damage": {
                                "min": 0,
                                "max": 0.25
                            }
                        },
                        {
                            "function": "enchant_with_levels",
                            "levels": 30,
                            "treasure": true
                        }
                    ]
                },
                {
                    "type": "item",
                    "name": "minecraft:fishing_rod",
                    "weight": 5,
                    "functions": [
                        {
                            "function": "set_damage",
                            "damage": {
                                "min": 0,
                                "max": 0.25
                            }
                        },
                        {
                            "function": "enchant_with_levels",
                            "levels": 30,
                            "treasure": true
                        }
                    ]
                },
                {
                    "type": "item",
                    "name": "minecraft:book",
                    "weight": 6,
                    "functions": [
                        {
                            "function": "enchant_with_levels",
                            "levels": 30,
                            "treasure": true
                        }
                    ]
                }
            ]
        }
    ]
}
```


### Одноимённые группы и события игрока (`Swords_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:jungle_sword": {
      "minecraft:type_family": {
        "family": [
          "player",
          "jungle_sword"
        ]
      },
      "minecraft:health": {
        "value": 8,
        "max": 8
      }
    }
  },
  "events": {
    "minecraft:jungle_sword": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "!=",
            "value": "jungle_sword"
          },
          "add": {
            "component_groups": [
              "minecraft:jungle_sword"
            ]
          }
        },
        {
          "run_command": {
            "command": [
              "effect @s absorption 1 2 true",
              "function commands/swords_and_more_swords/swords_and_more_swords/jungle_sword"
            ]
          }
        }
      ]
    },
    "stop_jungle_sword_event": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "==",
            "value": "jungle_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:jungle_sword"
            ]
          },
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "run_command": {
            "command": [
              "effect @s absorption 0"
            ]
          }
        }
      ]
    }
  }
}
```

## effect:lapis_sword

- Название в en_US: `§l§1Lapis Sword`
- Определение: `Swords_B/items/lapis_sword.json`
- Урон (`minecraft:damage`): `5`
- Прочность (`minecraft:durability`): `{"max_durability":528}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:lapis_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 528
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "lapis_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:lapis_sword"
          ],
          "repair_amount": 528
        },
        {
          "items": [
            "minecraft:lapis_lazuli"
          ],
          "repair_amount": 48
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 5,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/entities/player.json`: строки 296, 297, 299, 768, 770, 775, 777, 1900, 1903, 1904, 1908, 1911, 1912, 1917
- `Swords_B/functions/give.mcfunction`: строки 13
- `Swords_B/loot_tables/chests/pillager_outpost.json`: строки 184
- `Swords_B/loot_tables/chests/stronghold_corridor.json`: строки 159
- `Swords_B/loot_tables/chests/stronghold_library.json`: строки 44
- `Swords_R/texts/en_US.lang`: строки 16, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168
- `Swords_R/textures/item_texture.json`: строки 29, 30
- `Swords_R/ui/how_to_play_screen.json`: строки 39, 98, 289, 291, 292, 295, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306

### Рецепты и таблицы добычи с точным ID

`Swords_B/loot_tables/chests/pillager_outpost.json`:

```json
{
  "pools": [
    {
      "rolls": {
        "min": 0,
        "max": 1
      },
      "entries": [
        {
          "type": "item",
          "name": "minecraft:crossbow"
        }
      ]
    },
    {
      "rolls": {
        "min": 2,
        "max": 3
      },
      "entries": [
        {
          "type": "item",
          "weight": 7,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 3,
                "max": 5
              }
            }
          ],
          "name": "minecraft:wheat"
        },
        {
          "type": "item",
          "weight": 5,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 2,
                "max": 5
              }
            }
          ],
          "name": "minecraft:potato"
        },
        {
          "type": "item",
          "weight": 5,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 3,
                "max": 5
              }
            }
          ],
          "name": "minecraft:carrot"
        }
      ]
    },
    {
      "rolls": {
        "min": 1,
        "max": 3
      },
      "entries": [
        {
          "type": "item",
          "name": "minecraft:log2",
          "weight": 1,
          "functions": [
            {
              "function": "set_data",
              "data": 1
            },
            {
              "function": "set_count",
              "count": {
                "min": 2,
                "max": 3
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": {
        "min": 2,
        "max": 3
      },
      "entries": [
        {
          "type": "item",
          "weight": 7,
          "name": "minecraft:experience_bottle"
        },
        {
          "type": "item",
          "weight": 4,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 6
              }
            }
          ],
          "name": "minecraft:string"
        },
        {
          "type": "item",
          "weight": 4,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 2,
                "max": 7
              }
            }
          ],
          "name": "minecraft:arrow"
        },
        {
          "type": "item",
          "weight": 3,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "name": "minecraft:tripwire_hook"
        },
        {
          "type": "item",
          "weight": 3,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "name": "minecraft:iron_ingot"
        },
        {
          "type": "item",
          "weight": 3,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 0,
                "max": 1
              }
            }
          ],
          "name": "effect:emerald_sword"
        },
        {
          "type": "item",
          "weight": 3,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 0,
                "max": 1
              }
            }
          ],
          "name": "effect:lapis_sword"
        },
        {
          "type": "item",
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:book"
        }
      ]
    }
  ]

}
```

`Swords_B/loot_tables/chests/stronghold_corridor.json`:

```json
{
  "pools": [
    {
      "rolls": {
        "min": 2,
        "max": 3
      },
      "entries": [
        {
          "type": "item",
          "name": "minecraft:ender_pearl",
          "weight": 50
        },
        {
          "type": "item",
          "name": "minecraft:emerald",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "weight": 15
        },
        {
          "type": "item",
          "name": "minecraft:diamond",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "weight": 15
        },
        {
          "type": "item",
          "name": "minecraft:iron_ingot",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 5
              }
            }
          ],
          "weight": 50
        },
        {
          "type": "item",
          "name": "minecraft:gold_ingot",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "weight": 25
        },
        {
          "type": "item",
          "name": "minecraft:redstone",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 4,
                "max": 9
              }
            }
          ],
          "weight": 25
        },
        {
          "type": "item",
          "name": "minecraft:bread",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "weight": 75
        },
        {
          "type": "item",
          "name": "minecraft:apple",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "weight": 75
        },
        {
          "type": "item",
          "name": "minecraft:iron_pickaxe",
          "weight": 25
        },
        {
          "type": "item",
          "name": "minecraft:iron_sword",
          "weight": 25
        },
        {
          "type": "item",
          "name": "minecraft:iron_chestplate",
          "weight": 25
        },
        {
          "type": "item",
          "name": "minecraft:iron_helmet",
          "weight": 25
        },
        {
          "type": "item",
          "name": "minecraft:iron_leggings",
          "weight": 25
        },
        {
          "type": "item",
          "name": "minecraft:iron_boots",
          "weight": 25
        },
        {
          "type": "item",
          "name": "minecraft:golden_apple",
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:saddle",
          "weight": 5
        },
        {
          "type": "item",
          "name": "effect:emerald_sword",
          "weight": 5
        },
        {
          "type": "item",
          "name": "effect:lapis_sword",
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:horsearmoriron",
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:horsearmorgold",
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:horsearmordiamond",
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:book",
          "weight": 6,
          "functions": [
            {
              "function": "enchant_with_levels",
              "levels": 30,
              "treasure": true
            }
          ]
        }
      ]
    }
  ]
}
```

`Swords_B/loot_tables/chests/stronghold_library.json`:

```json
{
  "pools": [
    {
      "rolls": {
        "min": 2,
        "max": 10
      },
      "entries": [
        {
          "type": "item",
          "name": "minecraft:book",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "weight": 100
        },
        {
          "type": "item",
          "name": "minecraft:paper",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 2,
                "max": 7
              }
            }
          ],
          "weight": 100
        },
        {
          "type": "item",
          "name": "minecraft:map",
          "weight": 5
        },
        {
          "type": "item",
          "name": "effect:lapis_sword",
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:compass",
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:book",
          "weight": 60,
          "functions": [
            {
              "function": "enchant_with_levels",
              "levels": 30,
              "treasure": true
            }
          ]
        }
      ]
    }
  ]
}
```


### Одноимённые группы и события игрока (`Swords_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:lapis_sword": {
      "minecraft:type_family": {
        "family": [
          "player",
          "lapis_sword"
        ]
      },
      "minecraft:timer": {
        "time": [
          2.5,
          6.0
        ],
        "looping": true,
        "randomInterval": true,
        "time_down_event": {
          "event": "lapis_sword_skills",
          "target": "self"
        }
      }
    }
  },
  "events": {
    "minecraft:lapis_sword": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "!=",
            "value": "lapis_sword"
          },
          "add": {
            "component_groups": [
              "minecraft:lapis_sword"
            ]
          }
        }
      ]
    },
    "stop_lapis_sword_event": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "==",
            "value": "lapis_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:lapis_sword"
            ]
          },
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          }
        }
      ]
    },
    "lapis_sword_skills": {
      "run_command": {
        "command": [
          "xp 5 @s",
          "playsound random.orb @s ~ ~ ~ 0.3"
        ]
      }
    }
  }
}
```

## effect:lightning_sword

- Название в en_US: `§g§lLightning Sword`
- Определение: `Swords_B/items/lightning_sword.json`
- Урон (`minecraft:damage`): `8`
- Прочность (`minecraft:durability`): `{"max_durability":2012}`
- Кулдаун (`minecraft:cooldown`): `{"category":"lightning_sword","duration":12}`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:lightning_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": true,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 2012
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "lightning_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:lightning_sword"
          ],
          "repair_amount": 2012
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:render_offsets": {
      "main_hand": {
        "first_person": {
          "position": [
            1,
            0.4,
            -3
          ],
          "scale": [
            0.04,
            0.04,
            0.04
          ]
        },
        "third_person": {
          "position": [
            0.7,
            2.2,
            -1
          ],
          "scale": [
            0.05,
            0.05,
            0.05
          ]
        }
      }
    },
    "minecraft:display_name": {},
    "minecraft:damage": 8,
    "minecraft:cooldown": {
      "category": "lightning_sword",
      "duration": 12
    },
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "on_use": {
      "run_command": {
        "command": [
          "summon lightning_bolt ~ ~2 ~ default_lightning_bolt",
          "summon lightning_bolt ~7 ~ ~ default_lightning_bolt",
          "summon lightning_bolt ~ ~ ~7 default_lightning_bolt",
          "summon lightning_bolt ~-7 ~ ~ default_lightning_bolt",
          "summon lightning_bolt ~ ~ ~-7 default_lightning_bolt",
          "summon lightning_bolt ~6 ~ ~6 default_lightning_bolt",
          "summon lightning_bolt ~-6 ~ ~-6 default_lightning_bolt",
          "summon lightning_bolt ~-6 ~ ~6 default_lightning_bolt",
          "summon lightning_bolt ~6 ~ ~-6 default_lightning_bolt",
          "summon lightning_bolt ~14 ~ ~ default_lightning_bolt",
          "summon lightning_bolt ~ ~ ~14 default_lightning_bolt",
          "summon lightning_bolt ~-14 ~ ~ default_lightning_bolt",
          "summon lightning_bolt ~ ~ ~-14 default_lightning_bolt",
          "summon lightning_bolt ~12 ~ ~12 default_lightning_bolt",
          "summon lightning_bolt ~-12 ~ ~-12 default_lightning_bolt",
          "summon lightning_bolt ~-12 ~ ~12 default_lightning_bolt",
          "summon lightning_bolt ~12 ~ ~-12 default_lightning_bolt",
          "summon lightning_bolt ~28 ~ ~ default_lightning_bolt",
          "summon lightning_bolt ~ ~ ~28 default_lightning_bolt",
          "summon lightning_bolt ~-28 ~ ~ default_lightning_bolt",
          "summon lightning_bolt ~ ~ ~-28 default_lightning_bolt",
          "summon lightning_bolt ~24 ~ ~24 default_lightning_bolt",
          "summon lightning_bolt ~-24 ~ ~-24 default_lightning_bolt",
          "summon lightning_bolt ~-24 ~ ~24 default_lightning_bolt",
          "summon lightning_bolt ~24 ~ ~-24 default_lightning_bolt",
          "summon lightning_bolt ~34 ~ ~ default_lightning_bolt",
          "summon lightning_bolt ~ ~ ~34 default_lightning_bolt",
          "summon lightning_bolt ~-34 ~ ~ default_lightning_bolt",
          "summon lightning_bolt ~ ~ ~-34 default_lightning_bolt",
          "summon lightning_bolt ~30 ~ ~30 default_lightning_bolt",
          "summon lightning_bolt ~-30 ~ ~-30 default_lightning_bolt",
          "summon lightning_bolt ~-30 ~ ~30 default_lightning_bolt",
          "summon lightning_bolt ~30 ~ ~-30 default_lightning_bolt",
          "summon lightning_bolt ~42 ~ ~ default_lightning_bolt",
          "summon lightning_bolt ~ ~ ~42 default_lightning_bolt",
          "summon lightning_bolt ~-42 ~ ~ default_lightning_bolt",
          "summon lightning_bolt ~ ~ ~-42 default_lightning_bolt",
          "summon lightning_bolt ~38 ~ ~38 default_lightning_bolt",
          "summon lightning_bolt ~-38 ~ ~-38 default_lightning_bolt",
          "summon lightning_bolt ~-38 ~ ~38 default_lightning_bolt",
          "summon lightning_bolt ~38 ~ ~-38 default_lightning_bolt"
        ]
      },
      "damage": {
        "type": "durability",
        "amount": 9,
        "target": "self"
      }
    },
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        },
        {
          "randomize": [
            {
              "weight": 15
            },
            {
              "weight": 85,
              "shoot": {
                "projectile": "entity:lightning_projectile",
                "launch_power": 1
              }
            }
          ]
        }
      ]
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/animation_controllers/item_events.json`: строки 20
- `Swords_B/entities/centella.json`: строки 107
- `Swords_B/entities/player.json`: строки 184, 189, 929, 931, 936, 938, 1468, 1471, 1472, 1480, 1483, 1484
- `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/tag_swords.mcfunction`: строки 6
- `Swords_B/functions/give.mcfunction`: строки 14
- `Swords_R/texts/en_US.lang`: строки 28, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624
- `Swords_R/textures/item_texture.json`: строки 59, 60
- `Swords_R/ui/how_to_play_screen.json`: строки 69, 128, 1024, 1026, 1027, 1030, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044

### Одноимённые группы и события игрока (`Swords_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:lightning_sword": {
      "minecraft:damage_sensor": {
        "triggers": {
          "on_damage": {
            "filters": {
              "all_of": [
                {
                  "test": "is_family",
                  "subject": "other",
                  "value": "lightning"
                }
              ]
            }
          },
          "deals_damage": false
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "lightning_sword"
        ]
      }
    }
  },
  "events": {
    "minecraft:lightning_sword": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "!=",
            "value": "lightning_sword"
          },
          "add": {
            "component_groups": [
              "minecraft:lightning_sword"
            ]
          },
          "run_command": {
            "command": [
              "summon lightning_bolt ~ 255 ~ default_lightning_bolt"
            ]
          }
        },
        {
          "run_command": {
            "command": [
              "fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace air",
              "fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace effect99:lightblock2"
            ]
          }
        }
      ]
    },
    "stop_lightning_sword_event": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "==",
            "value": "lightning_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:lightning_sword"
            ]
          },
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          }
        }
      ]
    }
  }
}
```

## effect:magma_sword

- Название в en_US: `§l§6Magma Sword`
- Определение: `Swords_B/items/magma_sword.json`
- Урон (`minecraft:damage`): `7.2`
- Прочность (`minecraft:durability`): `{"max_durability":1316}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:magma_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 1316
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "magma_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:magma_sword"
          ],
          "repair_amount": 1316
        },
        {
          "items": [
            "minecraft:magma"
          ],
          "repair_amount": 100
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 7.2,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/entities/player.json`: строки 305, 311, 740, 742, 747, 749, 1961, 1964, 1965, 1992, 1995, 1996
- `Swords_B/functions/give.mcfunction`: строки 15
- `Swords_B/loot_tables/chests/underwater_ruin_big.json`: строки 68
- `Swords_R/texts/en_US.lang`: строки 25, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317
- `Swords_R/textures/item_texture.json`: строки 50, 51
- `Swords_R/ui/how_to_play_screen.json`: строки 50, 109, 538, 540, 541, 544, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556

### Рецепты и таблицы добычи с точным ID

`Swords_B/loot_tables/chests/underwater_ruin_big.json`:

```json
{
    "pools": [
        {
            "rolls": {
                "min": 2,
                "max": 8
            },
            "entries": [
                {
                    "type": "item",
                    "name": "minecraft:coal",
                    "weight": 10,
                    "functions": [
                        {
                            "function": "minecraft:set_count",
                            "count": {
                                "min": 1,
                                "max": 4
                            }
                        }
                    ]
                },
                {
                    "type": "item",
                    "name": "minecraft:gold_nugget",
                    "weight": 10,
                    "functions": [
                        {
                            "function": "minecraft:set_count",
                            "count": {
                                "min": 1,
                                "max": 3
                            }
                        }
                    ]
                },
                {
                    "type": "item",
                    "name": "minecraft:emerald",
                    "weight": 1
                },
                {
                    "type": "item",
                    "name": "minecraft:wheat",
                    "weight": 10,
                    "functions": [
                        {
                            "function": "minecraft:set_count",
                            "count": {
                                "min": 2,
                                "max": 3
                            }
                        }
                    ]
                }
            ]
        },
        {
            "rolls": 1,
            "entries": [
                {
                    "type": "item",
                    "name": "minecraft:golden_apple",
                    "weight": 1
                },
                {
                    "type": "item",
                    "name": "effect:magma_sword",
                    "weight": 1
                },
                {
                    "type": "item",
                    "name": "minecraft:book",
                    "weight": 5,
                    "functions": [
                        {
                            "function": "enchant_randomly"
                        }
                    ]
                },
                {
                    "type": "item",
                    "name": "minecraft:leather_chestplate",
                    "weight": 1
                },
                {
                    "type": "item",
                    "name": "minecraft:golden_helmet",
                    "weight": 1
                },
                {
                    "type": "item",
                    "name": "minecraft:fishing_rod",
                    "weight": 5,
                    "functions": [
                        {
                            "function": "enchant_randomly"
                        }
                    ]
                },
                {
                    "type": "item",
                    "name": "minecraft:map",
                    "weight": 10,
                    "functions": [
                         {
                            "function": "exploration_map",
                            "destination": "buriedtreasure"
                         }
                    ]
                }
            ]
        }
    ]
}
```


### Одноимённые группы и события игрока (`Swords_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:magma_sword": {
      "minecraft:damage_sensor": {
        "triggers": {
          "on_damage": {
            "filters": {
              "any_of": [
                {
                  "test": "has_damage",
                  "subject": "self",
                  "value": "fire_tick"
                },
                {
                  "test": "is_block",
                  "subject": "block",
                  "operator": "equals",
                  "value": "magma"
                }
              ]
            }
          },
          "deals_damage": false
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "magma_sword"
        ]
      }
    }
  },
  "events": {
    "minecraft:magma_sword": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "!=",
            "value": "magma_sword"
          },
          "add": {
            "component_groups": [
              "minecraft:magma_sword"
            ]
          }
        },
        {
          "run_command": {
            "command": [
              "fill ~ ~-1 ~ ~ ~-1 ~ magma 0 replace lava",
              "fill ~1 ~-1 ~1 ~ ~-1 ~ magma 0 replace lava",
              "fill ~ ~-1 ~1 ~ ~-1 ~1 magma 0 replace lava",
              "fill ~-1 ~-1 ~ ~-1 ~-1 ~ magma 0 replace lava",
              "fill ~ ~-1 ~-1 ~ ~-1 ~-1 magma 0 replace lava",
              "execute @s ~ ~1 ~ particle minecraft:guardian_attack_particle ^-0.4 ^ ^0.2"
            ]
          }
        },
        {
          "filters": {
            "test": "in_water",
            "operator": "=="
          },
          "randomize": [
            {
              "weight": 99
            },
            {
              "weight": 1,
              "run_command": {
                "command": [
                  "playsound bubble.up @a ~ ~ ~ 1 0.9"
                ]
              }
            }
          ]
        }
      ]
    },
    "stop_magma_sword_event": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "==",
            "value": "magma_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:magma_sword"
            ]
          },
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          }
        }
      ]
    }
  }
}
```

## effect:nether_star_sword

- Название в en_US: `§l§fNether Star Sword`
- Определение: `Swords_B/items/nether_star_sword.json`
- Урон (`minecraft:damage`): `7`
- Прочность (`minecraft:durability`): `{"max_durability":3256}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:nether_star_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": true,
    "minecraft:should_despawn": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 3256
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "nether_star_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:nether_star_sword"
          ],
          "repair_amount": 3256
        },
        {
          "items": [
            "minecraft:nether_star"
          ],
          "repair_amount": 3000
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 7,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "shoot": {
            "projectile": "entity:nether_star_projectile",
            "launch_power": 1
          }
        },
        {
          "randomize": [
            {
              "weight": 80,
              "run_command": {
                "command": [
                  "summon entity:nether_star ^ ^20 ^-6"
                ]
              }
            },
            {
              "weight": 20,
              "run_command": {
                "command": [
                  "summon entity:nether_star ^ ^20 ^-6",
                  "summon entity:nether_star ^ ^18 ^-6"
                ]
              }
            }
          ]
        },
        {
          "randomize": [
            {
              "weight": 9999,
              "damage": {
                "type": "durability",
                "amount": 1,
                "target": "self"
              }
            },
            {
              "weight": 1,
              "run_command": {
                "command": [
                  "summon entity:ultra_instinct_explode"
                ]
              }
            }
          ]
        }
      ]
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/animation_controllers/item_events.json`: строки 21
- `Swords_B/entities/nether_star_projectile.json`: строки 12, 95, 96
- `Swords_B/entities/player.json`: строки 28, 33, 1027, 1029, 1034, 1036, 1161, 1164, 1165, 1169, 1172, 1173
- `Swords_B/entities/wither.json`: строки 38
- `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/tag_swords.mcfunction`: строки 8
- `Swords_B/functions/give.mcfunction`: строки 34
- `Swords_B/recipes/nether_star_sword.json`: строки 5, 19
- `Swords_R/texts/en_US.lang`: строки 39, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393
- `Swords_R/textures/item_texture.json`: строки 101, 102
- `Swords_R/ui/how_to_play_screen.json`: строки 55, 114, 657, 659, 660, 663, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679

### Рецепты и таблицы добычи с точным ID

`Swords_B/recipes/nether_star_sword.json`:

```json
{
  "format_version": "1.12",
  "minecraft:recipe_shapeless": {
    "description": {
    "identifier": "effect:nether_star_sword"
    },  
    "tags": [ "crafting_table" ],
    "ingredients": [
      {
        "item": "minecraft:nether_star",
        "data": 0
      },
      {
        "item": "minecraft:diamond_sword",
        "data": 0
      }
    ],
    "result": {
      "item": "effect:nether_star_sword",
      "count": 1
    }
  }
}
```


### Одноимённые группы и события игрока (`Swords_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:nether_star_sword": {
      "minecraft:damage_sensor": {
        "triggers": {
          "on_damage": {
            "filters": {
              "all_of": [
                {
                  "test": "is_family",
                  "subject": "other",
                  "value": "nether_star_projectile"
                }
              ]
            }
          },
          "deals_damage": false
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "nether_star_sword"
        ]
      }
    }
  },
  "events": {
    "minecraft:nether_star_sword": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "!=",
            "value": "nether_star_sword"
          },
          "add": {
            "component_groups": [
              "minecraft:nether_star_sword"
            ]
          }
        }
      ]
    },
    "stop_nether_star_sword_event": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "==",
            "value": "nether_star_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:nether_star_sword"
            ]
          },
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          }
        }
      ]
    }
  }
}
```

## effect:obsidian_sword

- Название в en_US: `§l§8Obsidian Sword`
- Определение: `Swords_B/items/obsidian_sword.json`
- Урон (`minecraft:damage`): `8`
- Прочность (`minecraft:durability`): `{"max_durability":3000}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:obsidian_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 3000
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "obsidian_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:obsidian_sword"
          ],
          "repair_amount": 3000
        },
        {
          "items": [
            "minecraft:obsidian"
          ],
          "repair_amount": 120
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 8,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "randomize": [
        {
          "weight": 55,
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        },
        {
          "weight": 30,
          "damage": {
            "type": "durability",
            "amount": 2,
            "target": "self"
          }
        },
        {
          "weight": 15,
          "damage": {
            "type": "durability",
            "amount": 3,
            "target": "self"
          }
        }
      ]
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/entities/item.json`: строки 228
- `Swords_B/entities/player.json`: строки 286, 292, 782, 784, 789, 791, 1883, 1886, 1887, 1891, 1894, 1895
- `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/tag_swords.mcfunction`: строки 10
- `Swords_B/functions/give.mcfunction`: строки 16
- `Swords_R/texts/en_US.lang`: строки 20, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303
- `Swords_R/textures/item_texture.json`: строки 35, 36
- `Swords_R/ui/how_to_play_screen.json`: строки 49, 108, 514, 516, 517, 520, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533

### Одноимённые группы и события игрока (`Swords_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:obsidian_sword": {
      "minecraft:damage_sensor": {
        "triggers": {
          "on_damage": {
            "filters": {
              "any_of": [
                {
                  "test": "has_damage",
                  "subject": "self",
                  "value": "block_explosion"
                },
                {
                  "test": "has_damage",
                  "subject": "self",
                  "value": "entity_explosion"
                }
              ]
            }
          },
          "deals_damage": false
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "obsidian_sword"
        ]
      },
      "minecraft:knockback_resistance": {
        "value": 1.0
      }
    }
  },
  "events": {
    "minecraft:obsidian_sword": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "!=",
            "value": "obsidian_sword"
          },
          "add": {
            "component_groups": [
              "minecraft:obsidian_sword"
            ]
          }
        }
      ]
    },
    "stop_obsidian_sword_event": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "==",
            "value": "obsidian_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:obsidian_sword"
            ]
          },
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          }
        }
      ]
    }
  }
}
```

## effect:cursed_pumpkin_sword

- Название в en_US: `§l§6Cursed pumpkin sword`
- Определение: `Swords_B/items/pumpkin_sword.json`
- Урон (`minecraft:damage`): `5`
- Прочность (`minecraft:durability`): `{"max_durability":606}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:cursed_pumpkin_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 606
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "cursed_pumpkin_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:cursed_pumpkin_sword"
          ],
          "repair_amount": 606
        },
        {
          "items": [
            "minecraft:honey_block"
          ],
          "repair_amount": 400
        },
        {
          "items": [
            "minecraft:honeycomb"
          ],
          "repair_amount": 150
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 5,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        },
        {
          "randomize": [
            {
              "weight": 80,
              "shoot": {
                "projectile": "entity:pumpkin_projectile",
                "launch_power": 1
              }
            },
            {
              "weight": 20
            }
          ]
        }
      ]
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/loot_tables/pumpkin_sword.json`: строки 8
- `Swords_B/scripts/javascript.js`: строки 6, 7, 8
- `Swords_R/texts/en_US.lang`: строки 44
- `Swords_R/textures/item_texture.json`: строки 116, 117

### Рецепты и таблицы добычи с точным ID

`Swords_B/loot_tables/pumpkin_sword.json`:

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "effect:cursed_pumpkin_sword",
          "weight": 1
        }
      ]
    }
  ]
}
```


## effect:quartz_diamond

- Название в en_US: `Quartz Diamond`
- Определение: `Swords_B/items/quartz_diamond.json`
- Урон (`minecraft:damage`): `"не указан"`
- Прочность (`minecraft:durability`): `"не указана"`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:quartz_diamond",
    "category": "items"
  },
  "components": {
    "minecraft:max_stack_size": 9,
    "minecraft:foil": true,
    "minecraft:hand_equipped": false,
    "minecraft:icon": {
      "texture": "quartz_diamond"
    },
    "minecraft:display_name": {}
  },
  "events": {}
}
```

### Прямые текстовые упоминания

- `Swords_B/blocks/quartz_diamond_block.json`: строки 5, 18, 24, 26
- `Swords_B/blocks/quartz_diamond_ore.json`: строки 5, 14, 20, 22
- `Swords_B/feature_rules/quartz_diamond_ore_feature.json`: строки 5, 6
- `Swords_B/features/quartz_diamond_ore.json`: строки 5, 7
- `Swords_B/items/bedrock_sword.json`: строки 32, 36
- `Swords_B/items/quartz_diamond_stick.json`: строки 5, 16
- `Swords_B/loot_tables/blocks/quartz_diamond_block.json`: строки 8
- `Swords_B/loot_tables/blocks/quartz_diamond_ore.json`: строки 8, 22, 36
- `Swords_B/recipes/quartz_diamond_block.json`: строки 5, 15, 19
- `Swords_B/recipes/quartz_diamond_stick.json`: строки 5, 14, 18
- `Swords_B/recipes/quartz_diamond_sword.json`: строки 15, 19
- `Swords_R/blocks.json`: строки 9, 10, 12, 13
- `Swords_R/texts/en_US.lang`: строки 3, 4, 48, 49
- `Swords_R/textures/flipbook_textures.json`: строки 3, 4
- `Swords_R/textures/item_texture.json`: строки 126, 127, 129, 130
- `Swords_R/textures/terrain_texture.json`: строки 9, 10
- `Swords_R/ui/how_to_play_screen.json`: строки 190, 193, 195, 197

### Рецепты и таблицы добычи с точным ID

`Swords_B/loot_tables/blocks/quartz_diamond_ore.json`:

```json
{
 "pools": [
  {
   "rolls": 1,
   "entries": [
    {
     "type": "item",
     "name": "effect:quartz_diamond",
     "weight": 89,
     "functions": [
      {
       "function": "set_count",
       "count": {
        "min": 1,
        "max": 1
       }
      }
     ]
    },
    {
     "type": "item",
     "name": "effect:quartz_diamond",
     "weight": 10,
     "functions": [
      {
       "function": "set_count",
       "count": {
        "min": 1,
        "max": 2
       }
      }
     ]
    },
    {
     "type": "item",
     "name": "effect:quartz_diamond",
     "weight": 1,
     "functions": [
      {
       "function": "set_count",
       "count": {
        "min": 2,
        "max": 4
       }
      }
     ]
    }
   ]
  }
 ]
}
```

`Swords_B/recipes/quartz_diamond_block.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect99:quartz_diamond_block"
    },  
    "tags": [ "crafting_table" ],
    "pattern": [
      "###",
      "###",
      "###"
    ],
    "key": {
      "#": {
        "item": "effect:quartz_diamond"
      }
    },
    "result": {
      "item": "effect99:quartz_diamond_block"
    }
  }
}
```

`Swords_B/recipes/quartz_diamond_stick.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect:quartz_diamond_stick"
    },  
    "tags": [ "crafting_table" ],
    "pattern": [
      "#",
      "#"
    ],
    "key": {
      "#": {
        "item": "effect:quartz_diamond"
      }
    },
    "result": {
      "item": "effect:quartz_diamond_stick"
    }
  }
}
```

`Swords_B/recipes/quartz_diamond_sword.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect:quartz_sword"
    },  
    "tags": [ "crafting_table" ],
    "pattern": [
      "Q",
      "Q",
      "#"
    ],
    "key": {
      "#": {
        "item": "effect:quartz_diamond_stick",
        "data": 0
      },
      "Q": {
        "item": "effect99:quartz_diamond_block"
      }
    },
    "result": {
      "item": "effect:quartz_sword"
    }
  }
}
```


## effect:quartz_diamond_stick

- Название в en_US: `Quartz Diamond Stick`
- Определение: `Swords_B/items/quartz_diamond_stick.json`
- Урон (`minecraft:damage`): `24`
- Прочность (`minecraft:durability`): `{"max_durability":20}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:quartz_diamond_stick",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": true,
    "minecraft:max_stack_size": 1,
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:can_destroy_in_creative": true,
    "minecraft:icon": {
      "texture": "quartz_diamond_stick"
    },
    "minecraft:durability": {
      "max_durability": 20
    },
    "minecraft:display_name": {},
    "minecraft:damage": 24,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "randomize": [
        {
          "weight": 10,
          "run_command": {
            "command": [
              "damage @s 1 magic"
            ]
          }
        },
        {
          "weight": 85,
          "run_command": {
            "command": [
              "damage @s 3 magic"
            ]
          }
        },
        {
          "weight": 5,
          "run_command": {
            "command": [
              "damage @s 6 magic"
            ]
          }
        }
      ]
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/recipes/quartz_diamond_stick.json`: строки 5, 18
- `Swords_B/recipes/quartz_diamond_sword.json`: строки 15
- `Swords_R/texts/en_US.lang`: строки 49
- `Swords_R/textures/item_texture.json`: строки 129, 130
- `Swords_R/ui/how_to_play_screen.json`: строки 197

### Рецепты и таблицы добычи с точным ID

`Swords_B/recipes/quartz_diamond_stick.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect:quartz_diamond_stick"
    },  
    "tags": [ "crafting_table" ],
    "pattern": [
      "#",
      "#"
    ],
    "key": {
      "#": {
        "item": "effect:quartz_diamond"
      }
    },
    "result": {
      "item": "effect:quartz_diamond_stick"
    }
  }
}
```

`Swords_B/recipes/quartz_diamond_sword.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect:quartz_sword"
    },  
    "tags": [ "crafting_table" ],
    "pattern": [
      "Q",
      "Q",
      "#"
    ],
    "key": {
      "#": {
        "item": "effect:quartz_diamond_stick",
        "data": 0
      },
      "Q": {
        "item": "effect99:quartz_diamond_block"
      }
    },
    "result": {
      "item": "effect:quartz_sword"
    }
  }
}
```


## effect:quartz_sword

- Название в en_US: `§lQuartz Diamond Sword`
- Определение: `Swords_B/items/quartz_sword.json`
- Урон (`minecraft:damage`): `600`
- Прочность (`minecraft:durability`): `{"max_durability":1}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:quartz_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": true,
    "minecraft:max_stack_size": 1,
    "minecraft:durability": {
      "max_durability": 1
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "quartz_sword"
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:render_offsets": {
      "main_hand": {
        "first_person": {
          "position": [
            1.0,
            0,
            -2
          ],
          "scale": [
            0.07,
            0.07,
            0.07
          ]
        },
        "third_person": {
          "position": [
            0.2,
            1.1,
            -0.5
          ],
          "scale": [
            0.08,
            0.08,
            0.08
          ]
        }
      }
    },
    "minecraft:display_name": {},
    "minecraft:damage": 600,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 10,
            "target": "self"
          }
        },
        {
          "run_command": {
            "command": [
              "effect @a[r=1] instant_damage 1 99 true",
              "particle minecraft:knockback_roar_particle ~ ~1 ~"
            ]
          }
        }
      ]
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/entities/player.json`: строки 283, 284, 796, 798, 803, 805, 1864, 1867, 1869, 1873, 1876, 1878
- `Swords_B/functions/give.mcfunction`: строки 17
- `Swords_B/recipes/quartz_diamond_sword.json`: строки 5, 23
- `Swords_R/texts/en_US.lang`: строки 33, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425
- `Swords_R/textures/item_texture.json`: строки 80, 81
- `Swords_R/ui/how_to_play_screen.json`: строки 57, 116, 711, 713, 714, 717, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730

### Рецепты и таблицы добычи с точным ID

`Swords_B/recipes/quartz_diamond_sword.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect:quartz_sword"
    },  
    "tags": [ "crafting_table" ],
    "pattern": [
      "Q",
      "Q",
      "#"
    ],
    "key": {
      "#": {
        "item": "effect:quartz_diamond_stick",
        "data": 0
      },
      "Q": {
        "item": "effect99:quartz_diamond_block"
      }
    },
    "result": {
      "item": "effect:quartz_sword"
    }
  }
}
```


### Одноимённые группы и события игрока (`Swords_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:quartz_sword": {
      "minecraft:type_family": {
        "family": [
          "player",
          "quartz_sword"
        ]
      }
    }
  },
  "events": {
    "minecraft:quartz_sword": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "!=",
            "value": "quartz_sword"
          },
          "run_command": {
            "command": [
              "damage @s 14 magic"
            ]
          },
          "add": {
            "component_groups": [
              "minecraft:quartz_sword"
            ]
          }
        }
      ]
    },
    "stop_quartz_sword_event": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "==",
            "value": "quartz_sword"
          },
          "run_command": {
            "command": [
              "damage @s 14 magic"
            ]
          },
          "remove": {
            "component_groups": [
              "minecraft:quartz_sword"
            ]
          },
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          }
        }
      ]
    }
  }
}
```

## effect:sea_sword

- Название в en_US: `§l§bSea Sword`
- Определение: `Swords_B/items/sea_sword.json`
- Урон (`minecraft:damage`): `7`
- Прочность (`minecraft:durability`): `{"max_durability":1356}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:sea_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": true,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 1356
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "sea_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:sea_sword"
          ],
          "repair_amount": 1356
        },
        {
          "items": [
            "minecraft:heart_of_the_sea"
          ],
          "repair_amount": 482
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 7,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/entities/player.json`: строки 262, 268, 273, 810, 812, 817, 819, 1825, 1833, 1834, 1844, 1847, 1848, 1854
- `Swords_B/functions/give.mcfunction`: строки 18
- `Swords_B/loot_tables/chests/buriedtreasure.json`: строки 96
- `Swords_R/entity/player.entity.json`: строки 60
- `Swords_R/texts/en_US.lang`: строки 17, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358
- `Swords_R/textures/item_texture.json`: строки 68, 69
- `Swords_R/ui/how_to_play_screen.json`: строки 53, 112, 605, 607, 608, 611, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625

### Рецепты и таблицы добычи с точным ID

`Swords_B/loot_tables/chests/buriedtreasure.json`:

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:heart_of_the_sea"
        }
      ]
    },
    {
      "rolls": {
        "min": 5,
        "max": 12
      },
      "entries": [
        {
          "type": "item",
          "name": "minecraft:prismarine_crystals",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 5
              }
            }
          ],
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:iron_ingot",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 3,
                "max": 5
              }
            }
          ],
          "weight": 20
        },
        {
          "type": "item",
          "name": "minecraft:gold_ingot",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 5
              }
            }
          ],
          "weight": 10
        },
        {
          "type": "item",
          "name": "minecraft:tnt",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ],
          "weight": 10
        },
        {
          "type": "item",
          "name": "minecraft:diamond",
          "weight": 15
        },
        {
          "type": "item",
          "name": "minecraft:record_wait",
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:record_mellohi",
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:name_tag",
          "weight": 10
        },
        {
          "type": "item",
          "name": "effect:sea_sword",
          "weight": 15
        },
        {
          "type": "item",
          "name": "minecraft:chainmail_chestplate",
          "weight": 20
        },
        {
          "type": "item",
          "name": "minecraft:chainmail_helmet",
          "weight": 20
        },
        {
          "type": "item",
          "name": "minecraft:chainmail_leggings",
          "weight": 20
        },
        {
          "type": "item",
          "name": "minecraft:chainmail_boots",
          "weight": 20
        },
        {
          "type": "item",
          "name": "minecraft:writable_book",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ],
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:lead",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "weight": 10
        },
        {
          "type": "item",
          "name": "minecraft:experience_bottle",
          "weight": 3
        },
        {
          "type": "item",
          "name": "minecraft:potion",
          "functions": [
            {
              "function": "set_data",
              "data": 19
            }
          ],
          "weight": 15
        },
        {
          "type": "item",
          "name": "minecraft:potion",
          "functions": [
            {
              "function": "set_data",
              "data": 28
            }
          ],
          "weight": 10
        },
        {
          "type": "item",
          "name": "minecraft:cake",
          "weight": 1
        }
      ]
    }
  ]
}
```


### Одноимённые группы и события игрока (`Swords_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:sea_sword": {
      "minecraft:collision_box": {
        "width": 0.6,
        "height": 0.9
      },
      "minecraft:timer": {
        "time": [
          0.5,
          0.5
        ],
        "looping": true,
        "time_down_event": {
          "event": "sea_sword_sound",
          "target": "self"
        }
      },
      "minecraft:breathable": {
        "total_supply": 2,
        "suffocate_time": -1,
        "inhale_time": 3.75,
        "generates_bubbles": false,
        "breathes_water": true,
        "breathes_air": false,
        "breathes_lava": false
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "sea_sword"
        ]
      }
    }
  },
  "events": {
    "minecraft:sea_sword": {
      "sequence": [
        {
          "filters": {
            "test": "in_water",
            "operator": "!="
          },
          "add": {
            "component_groups": [
              "mermaid_movement_out_water"
            ]
          },
          "run_command": {
            "command": [
              "camerashake add @s 0.01 1 positional",
              "effect @s conduit_power 0 0"
            ]
          }
        },
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "!=",
            "value": "sea_sword"
          },
          "add": {
            "component_groups": [
              "minecraft:sea_sword"
            ]
          },
          "run_command": {
            "command": [
              "particle minecraft:example_bounce ~ ~ ~",
              "playsound random.splash @a[r=12] ~ ~ ~ 0.5"
            ]
          }
        },
        {
          "filters": {
            "test": "in_water"
          },
          "add": {
            "component_groups": [
              "mermaid_movement_in_water"
            ]
          },
          "run_command": {
            "command": [
              "effect @s conduit_power 1 0 true"
            ]
          }
        }
      ]
    },
    "stop_sea_sword_event": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "==",
            "value": "sea_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:sea_sword",
              "mermaid_movement_in_water"
            ]
          },
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "run_command": {
            "command": [
              "particle minecraft:example_bounce ~ ~ ~",
              "playsound random.splash @a[r=12] ~ ~ ~ 0.5",
              "effect @s conduit_power 0 0"
            ]
          }
        }
      ]
    },
    "sea_sword_sound": {
      "sequence": [
        {
          "filters": {
            "test": "in_water",
            "operator": "!="
          },
          "run_command": {
            "command": [
              "playsound mob.fish.flop @a[r=12] ~ ~ ~ 1 0.6"
            ]
          }
        }
      ]
    }
  }
}
```

## effect:shulker_sword

- Название в en_US: `§l§5Shulker sword`
- Определение: `Swords_B/items/shulker_sword.json`
- Урон (`minecraft:damage`): `6`
- Прочность (`minecraft:durability`): `{"max_durability":2609}`
- Кулдаун (`minecraft:cooldown`): `{"category":"shulker_sword","duration":8}`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:shulker_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:cooldown": {
      "category": "shulker_sword",
      "duration": 8
    },
    "minecraft:durability": {
      "max_durability": 2609
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "shulker_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:shulker_sword"
          ],
          "repair_amount": 2609
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 6,
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "on_use": {
      "run_command": {
        "command": [
          "particle minecraft:cauldron_explosion_emitter ~3 ~ ~",
          "particle minecraft:cauldron_explosion_emitter ~ ~ ~3",
          "particle minecraft:cauldron_explosion_emitter ~-3 ~ ~",
          "particle minecraft:cauldron_explosion_emitter ~ ~ ~-3",
          "particle minecraft:cauldron_explosion_emitter ~-2.5 ~ ~2.5",
          "particle minecraft:cauldron_explosion_emitter ~2.5 ~ ~-2.5",
          "particle minecraft:cauldron_explosion_emitter ~2.5 ~ ~2.5",
          "particle minecraft:cauldron_explosion_emitter ~-2.5 ~ ~-2.5",
          "effect @e[r=6,family=!shulker_sword] levitation 1 18 false"
        ]
      },
      "damage": {
        "type": "durability",
        "amount": 8,
        "target": "self"
      }
    },
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        },
        {
          "randomize": [
            {
              "weight": 10,
              "shoot": {
                "projectile": "minecraft:shulker_bullet",
                "launch_power": 1
              },
              "run_command": {
                "command": [
                  "playsound random.bow @a[r=10] ~ ~ ~ 1 0.4"
                ]
              }
            },
            {
              "weight": 90
            }
          ]
        }
      ]
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/animation_controllers/shulker_sword.json`: строки 4, 9, 13, 15
- `Swords_B/entities/player.json`: строки 10, 13, 228, 230, 232, 239, 852, 854, 859, 861, 1644, 1647, 1648, 1655, 1658, 1659, 1665, 1666
- `Swords_B/entities/shulker_bullet.json`: строки 11, 91, 92
- `Swords_B/entities/shulker_shield.json`: строки 22, 47, 49
- `Swords_B/entities/witch.json`: строки 230, 231
- `Swords_B/functions/give.mcfunction`: строки 19
- `Swords_B/loot_tables/entities/shulker.json`: строки 44
- `Swords_R/texts/en_US.lang`: строки 9, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490
- `Swords_R/textures/item_texture.json`: строки 8, 9
- `Swords_R/ui/how_to_play_screen.json`: строки 61, 120, 813, 815, 816, 819, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832

### Рецепты и таблицы добычи с точным ID

`Swords_B/loot_tables/entities/shulker.json`:

```json
{
   "pools": [
     {
       "rolls": 1,
       "entries": [
         {
           "type": "item",
           "name": "minecraft:shulker_shell",
           "weight": 1,
           "functions": [
             {
               "function": "set_count",
               "count": {
                 "min": 0,
                 "max": 1
               }
             },
             {
               "function": "looting_enchant",
               "count": {
                 "min": 0,
                 "max": 1
               }
             }
           ]
         }
       ]
     },
     {
      "conditions": [
        {
          "condition": "killed_by_player"
        },
        {
          "condition": "random_chance_with_looting",
          "chance": 0.045,
          "looting_multiplier": 0.02
        }
      ],
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "effect:shulker_sword",
          "weight": 1,
          "functions": [
            {
               "function": "set_count",
               "count": {
                 "min": 1,
                 "max": 1
               }
             },
            {
              "function": "set_data",
              "data": 0
            }
          ]
        }
      ]
    }
  ]
}
```


### Одноимённые группы и события игрока (`Swords_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:shulker_sword": {
      "minecraft:scale": {
        "value": 1
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "shulker_sword"
        ]
      }
    },
    "shulker_sword_skill": {
      "minecraft:damage_sensor": {
        "triggers": [
          {
            "cause": "all",
            "deals_damage": false
          }
        ]
      },
      "minecraft:scale": {
        "value": 0.7
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "shulker_sword"
        ]
      }
    }
  },
  "events": {
    "minecraft:shulker_sword": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "!=",
            "value": "shulker_sword"
          },
          "add": {
            "component_groups": [
              "minecraft:shulker_sword"
            ]
          }
        },
        {
          "run_command": {
            "command": [
              "effect @s levitation 0 0"
            ]
          }
        }
      ]
    },
    "stop_shulker_sword_event": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "==",
            "value": "shulker_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:shulker_sword"
            ]
          },
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "run_command": {
            "command": [
              "ride @s stop_riding"
            ]
          }
        }
      ]
    },
    "shulker_sword_skill": {
      "add": {
        "component_groups": [
          "shulker_sword_skill"
        ]
      },
      "run_command": {
        "command": [
          "ride @s summon_ride entity:shulker_shield no_ride_change"
        ]
      }
    }
  }
}
```

## effect:silver_ingot

- Название в en_US: `Silver Ingot`
- Определение: `Swords_B/items/silver_ingot.json`
- Урон (`minecraft:damage`): `"не указан"`
- Прочность (`minecraft:durability`): `"не указана"`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:silver_ingot",
    "category": "items"
  },
  "components": {
    "minecraft:max_stack_size": 64,
    "minecraft:hand_equipped": false,
    "minecraft:icon": {
      "texture": "silver_ingot"
    },
    "minecraft:display_name": {}
  },
  "events": {}
}
```

### Прямые текстовые упоминания

- `Swords_B/recipes/silver_ingot.json`: строки 5, 12
- `Swords_B/recipes/silver_sword.json`: строки 15
- `Swords_R/texts/en_US.lang`: строки 47
- `Swords_R/textures/item_texture.json`: строки 123, 124
- `Swords_R/ui/how_to_play_screen.json`: строки 203

### Рецепты и таблицы добычи с точным ID

`Swords_B/recipes/silver_ingot.json`:

```json
{
  "format_version": "1.12",
  "minecraft:recipe_furnace": {
    "description": {
      "identifier": "effect:silver_ingot"
    },
    "tags": [
      "furnace",
      "blast_furnace"
    ],
    "input": "effect99:silver_ore",
    "output": "effect:silver_ingot"
  }
}
```

`Swords_B/recipes/silver_sword.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect:silver_sword"
    },  
    "tags": [ "crafting_table" ],
    "pattern": [
      "2",
      "2",
      "1"
    ],
    "key": {
      "2": {
        "item": "effect:silver_ingot"
      },
      "1": {
        "item": "minecraft:stick"      
      }
    },
    "result": {
      "item": "effect:silver_sword"
    }
  }
}
```


## effect:silver_sword

- Название в en_US: `§l§7Silver Sword`
- Определение: `Swords_B/items/silver_sword.json`
- Урон (`minecraft:damage`): `6`
- Прочность (`minecraft:durability`): `{"max_durability":1800}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:silver_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 1800
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "silver_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:silver_sword"
          ],
          "repair_amount": 1800
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:render_offsets": {
      "main_hand": {
        "first_person": {
          "position": [
            0.67,
            0,
            -1.19
          ]
        },
        "third_person": {
          "position": [
            0.36,
            1.5,
            -0.66
          ]
        }
      }
    },
    "minecraft:display_name": {},
    "minecraft:damage": 6,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/entities/alpha_wolf.json`: строки 110, 136, 157
- `Swords_B/functions/give.mcfunction`: строки 35
- `Swords_B/recipes/silver_sword.json`: строки 5, 22
- `Swords_R/texts/en_US.lang`: строки 38, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156
- `Swords_R/textures/item_texture.json`: строки 98, 99
- `Swords_R/ui/how_to_play_screen.json`: строки 38, 97, 268, 270, 271, 274, 276, 277, 278, 279, 280, 281, 282, 283, 284

### Рецепты и таблицы добычи с точным ID

`Swords_B/recipes/silver_sword.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect:silver_sword"
    },  
    "tags": [ "crafting_table" ],
    "pattern": [
      "2",
      "2",
      "1"
    ],
    "key": {
      "2": {
        "item": "effect:silver_ingot"
      },
      "1": {
        "item": "minecraft:stick"      
      }
    },
    "result": {
      "item": "effect:silver_sword"
    }
  }
}
```


## effect:slime_sword

- Название в en_US: `§l§aSlime Sword`
- Определение: `Swords_B/items/slime_sword.json`
- Урон (`minecraft:damage`): `6`
- Прочность (`minecraft:durability`): `{"max_durability":675}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:slime_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 675
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "slime_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:slime_sword"
          ],
          "repair_amount": 675
        },
        {
          "items": [
            "minecraft:slime"
          ],
          "repair_amount": 48
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 6,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/entities/mountable_slime.json`: строки 199, 214
- `Swords_B/entities/player.json`: строки 241, 242, 244, 838, 840, 845, 847, 1120, 1669, 1672, 1673, 1680, 1683, 1684, 1690
- `Swords_B/functions/give.mcfunction`: строки 20
- `Swords_B/loot_tables/entities/slime_king.json`: строки 18
- `Swords_R/texts/en_US.lang`: строки 13, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289
- `Swords_R/textures/item_texture.json`: строки 23, 24
- `Swords_R/ui/how_to_play_screen.json`: строки 48, 107, 490, 492, 493, 496, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508

### Рецепты и таблицы добычи с точным ID

`Swords_B/loot_tables/entities/slime_king.json`:

```json
{
  "pools": [
    {
      "conditions": [
        {
          "condition": "killed_by_player"
        },
        {
          "condition": "random_chance_with_looting",
          "chance": 0.040,
          "looting_multiplier": 0.02
        }
      ],
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "effect:slime_sword",
          "weight": 1,
          "functions": [
            {
              "function": "set_data",
              "data": 0
            }
          ]
        }
      ]
    }
  ]
}
```


### Одноимённые группы и события игрока (`Swords_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:slime_sword": {
      "minecraft:type_family": {
        "family": [
          "player",
          "slime_sword"
        ]
      },
      "minecraft:timer": {
        "time": [
          0.4,
          0.4
        ],
        "looping": false,
        "time_down_event": {
          "event": "slime_sword_skills",
          "target": "self"
        }
      },
      "minecraft:damage_sensor": {
        "triggers": {
          "on_damage": {
            "filters": {
              "all_of": [
                {
                  "test": "is_family",
                  "subject": "other",
                  "value": "tamed_slime"
                }
              ]
            }
          },
          "deals_damage": false
        }
      }
    }
  },
  "events": {
    "minecraft:slime_sword": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "!=",
            "value": "slime_sword"
          },
          "add": {
            "component_groups": [
              "minecraft:slime_sword"
            ]
          }
        },
        {
          "run_command": {
            "command": [
              "scoreboard players set @e[type=entity:mountable_slime,c=1,r=12] slime_despawn 0"
            ]
          }
        }
      ]
    },
    "stop_slime_sword_event": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "==",
            "value": "slime_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:slime_sword"
            ]
          },
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "run_command": {
            "command": [
              "ride @s stop_riding",
              "event entity @e[type=entity:mountable_slime,c=1,r=32] despawn"
            ]
          }
        }
      ]
    },
    "slime_sword_skills": {
      "run_command": {
        "command": [
          "ride @s summon_ride entity:mountable_slime no_ride_change",
          "scoreboard objectives add slime_despawn dummy"
        ]
      }
    }
  }
}
```

## effect:spectral_sword

- Название в en_US: `§l§fSpectral Sword`
- Определение: `Swords_B/items/spectral_sword.json`
- Урон (`minecraft:damage`): `9`
- Прочность (`minecraft:durability`): `{"max_durability":3256}`
- Кулдаун (`minecraft:cooldown`): `{"category":"spectral_sword","duration":18}`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:spectral_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": true,
    "minecraft:should_despawn": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:cooldown": {
      "category": "spectral_sword",
      "duration": 18
    },
    "minecraft:durability": {
      "max_durability": 3256
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "spectral_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:spectral_sword"
          ],
          "repair_amount": 3256
        },
        {
          "items": [
            "minecraft:end_crystal"
          ],
          "repair_amount": 620
        },
        {
          "items": [
            "minecraft:nether_star"
          ],
          "repair_amount": 2052
        }
      ]
    },
    "minecraft:render_offsets": {
      "main_hand": {
        "first_person": {
          "position": [
            0.57,
            0.1,
            -1.24
          ]
        },
        "third_person": {
          "position": [
            0.41,
            1.7,
            -0.7
          ]
        }
      }
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 9,
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "on_use": {
      "damage": {
        "type": "durability",
        "amount": 15,
        "target": "self"
      },
      "shoot": {
        "projectile": "entity:ender_crystal_projectile",
        "launch_power": 1
      },
      "run_command": {
        "command": [
          "playsound portal.travel @a[r=16] ~ ~ ~ 1 5",
          "event entity @e[type=ender_crystal,family=!ender_crystal_default,family=!ender_crystal_scale,c=1,r=4] minecraft:ender_crystal_scale"
        ]
      }
    },
    "weapon": {
      "randomize": [
        {
          "weight": 99,
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        },
        {
          "weight": 1,
          "run_command": {
            "command": [
              "event entity @e[type=ender_crystal,family=!ender_crystal_default,family=!ender_crystal_scale,c=1] minecraft:crystal_explode"
            ]
          }
        }
      ]
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/entities/ender_crystal.json`: строки 21, 34, 35, 41, 56, 89, 102, 116, 127, 133, 135, 142
- `Swords_B/entities/ghast.json`: строки 112
- `Swords_B/entities/player.json`: строки 251, 253, 257, 260, 635, 824, 826, 831, 833, 1693, 1696, 1697, 1704, 1705, 1711, 1741, 1789, 1792, 1793, 1799, 1817, 1820, 1821
- `Swords_B/functions/give.mcfunction`: строки 21
- `Swords_R/texts/en_US.lang`: строки 15, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579
- `Swords_R/textures/item_texture.json`: строки 32, 33
- `Swords_R/ui/how_to_play_screen.json`: строки 66, 125, 946, 948, 949, 952, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970

### Одноимённые группы и события игрока (`Swords_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:spectral_sword": {
      "minecraft:timer": {
        "time": [
          0.4,
          0.4
        ],
        "looping": false,
        "time_down_event": {
          "event": "spectral_sword_skills",
          "target": "self"
        }
      },
      "minecraft:rideable": {
        "seat_count": 1,
        "family_types": [
          "ender_crystal",
          "spectral_sword"
        ],
        "seats": {
          "position": [
            0.0,
            0.4,
            0.0
          ],
          "lock_rider_rotation": 0
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "spectral_sword"
        ]
      }
    }
  },
  "events": {
    "minecraft:spectral_sword": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "!=",
            "value": "spectral_sword"
          },
          "add": {
            "component_groups": [
              "minecraft:spectral_sword"
            ]
          }
        },
        {
          "run_command": {
            "command": [
              "fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace air",
              "fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace effect99:lightblock2",
              "execute @s[y=8,dy=247] ~~~ event entity @s spectral_sword_function",
              "execute @s[y=0,dy=7] ~~~ event entity @s spectral_sword_function_1"
            ]
          }
        }
      ]
    },
    "spectral_sword_function_1": {
      "sequence": [
        {
          "filters": {
            "all_of": [
              {
                "test": "has_biome_tag",
                "operator": "!=",
                "value": "nether"
              },
              {
                "test": "has_biome_tag",
                "operator": "!=",
                "value": "the_end"
              }
            ]
          },
          "run_command": {
            "command": [
              "fill ~8 ~8 ~8 ~-8 ~-6 ~-8 stone 0 replace effect99:spectral_block"
            ]
          }
        },
        {
          "filters": {
            "test": "has_biome_tag",
            "value": "nether"
          },
          "run_command": {
            "command": [
              "fill ~8 ~8 ~8 ~-8 ~-6 ~-8 netherrack 0 replace effect99:spectral_block"
            ]
          }
        },
        {
          "filters": {
            "test": "has_biome_tag",
            "value": "the_end"
          },
          "run_command": {
            "command": [
              "fill ~8 ~8 ~8 ~-8 ~-6 ~-8 end_stone 0 replace effect99:spectral_block"
            ]
          }
        }
      ]
    },
    "spectral_sword_function": {
      "sequence": [
        {
          "filters": {
            "all_of": [
              {
                "test": "has_biome_tag",
                "operator": "!=",
                "value": "nether"
              },
              {
                "test": "has_biome_tag",
                "operator": "!=",
                "value": "the_end"
              }
            ]
          },
          "run_command": {
            "command": [
              "fill ~6 ~6 ~6 ~-6 ~-6 ~-6 effect99:spectral_block 0 replace stone",
              "fill ~7 ~8 ~8 ~8 ~-8 ~-8 stone 0 replace effect99:spectral_block",
              "fill ~-7 ~-8 ~-8 ~-8 ~8 ~8 stone 0 replace effect99:spectral_block",
              "fill ~-6 ~8 ~7 ~6 ~-8 ~8 stone 0 replace effect99:spectral_block",
              "fill ~6 ~-8 ~-7 ~-6 ~8 ~-8 stone 0 replace effect99:spectral_block",
              "fill ~8 ~-8 ~8 ~-8 ~-7 ~-8 stone 0 replace effect99:spectral_block",
              "fill ~8 ~8 ~8 ~-8 ~7 ~-8 stone 0 replace effect99:spectral_block"
            ]
          }
        },
        {
          "filters": {
            "test": "has_biome_tag",
            "value": "nether"
          },
          "run_command": {
            "command": [
              "fill ~6 ~6 ~6 ~-6 ~-6 ~-6 effect99:spectral_block 0 replace netherrack",
              "fill ~7 ~8 ~8 ~8 ~-8 ~-8 netherrack 0 replace effect99:spectral_block",
              "fill ~-7 ~-8 ~-8 ~-8 ~8 ~8 netherrack 0 replace effect99:spectral_block",
              "fill ~-6 ~8 ~7 ~6 ~-8 ~8 netherrack 0 replace effect99:spectral_block",
              "fill ~6 ~-8 ~-7 ~-6 ~8 ~-8 netherrack 0 replace effect99:spectral_block",
              "fill ~8 ~-8 ~8 ~-8 ~-7 ~-8 netherrack 0 replace effect99:spectral_block",
              "fill ~8 ~8 ~8 ~-8 ~7 ~-8 netherrack 0 replace effect99:spectral_block"
            ]
          }
        },
        {
          "filters": {
            "test": "has_biome_tag",
            "value": "the_end"
          },
          "run_command": {
            "command": [
              "fill ~6 ~6 ~6 ~-6 ~-6 ~-6 effect99:spectral_block 0 replace end_stone",
              "fill ~7 ~8 ~8 ~8 ~-8 ~-8 end_stone 0 replace effect99:spectral_block",
              "fill ~-7 ~-8 ~-8 ~-8 ~8 ~8 end_stone 0 replace effect99:spectral_block",
              "fill ~-6 ~8 ~7 ~6 ~-8 ~8 end_stone 0 replace effect99:spectral_block",
              "fill ~6 ~-8 ~-7 ~-6 ~8 ~-8 end_stone 0 replace effect99:spectral_block",
              "fill ~8 ~-8 ~8 ~-8 ~-7 ~-8 end_stone 0 replace effect99:spectral_block",
              "fill ~8 ~8 ~8 ~-8 ~7 ~-8 end_stone 0 replace effect99:spectral_block"
            ]
          }
        }
      ]
    },
    "stop_spectral_sword_event": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "==",
            "value": "spectral_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:spectral_sword"
            ]
          },
          "run_command": {
            "command": [
              "ride @s evict_riders"
            ]
          },
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          }
        }
      ]
    },
    "spectral_sword_skills": {
      "sequence": [
        {
          "filters": {
            "test": "has_biome_tag",
            "operator": "!=",
            "value": "the_end"
          },
          "run_command": {
            "command": [
              "summon ender_crystal ~ ~1.8 ~ minecraft:detect_player"
            ]
          }
        },
        {
          "run_command": {
            "command": [
              "playsound portal.travel @a[r=16] ~ ~ ~ 1 7",
              "particle minecraft:example_flipbook ~ ~3 ~"
            ]
          }
        }
      ]
    },
    "spectral_sword_reload_skill": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "==",
            "value": "spectral_sword"
          },
          "add": {
            "component_groups": [
              "minecraft:spectral_sword"
            ]
          }
        }
      ]
    }
  }
}
```

## effect:spider_sword

- Название в en_US: `§l§cSpider Sword`
- Определение: `Swords_B/items/spider_sword.json`
- Урон (`minecraft:damage`): `5`
- Прочность (`minecraft:durability`): `{"max_durability":628}`
- Кулдаун (`minecraft:cooldown`): `{"category":"spider_sword","duration":28}`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:spider_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 628
    },
    "minecraft:cooldown": {
      "category": "spider_sword",
      "duration": 28
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "spider_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:spider_sword"
          ],
          "repair_amount": 628
        },
        {
          "items": [
            "minecraft:web"
          ],
          "repair_amount": 128
        },
        {
          "items": [
            "minecraft:spider_eye"
          ],
          "repair_amount": 48
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 100
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 5,
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "on_use": {
      "run_command": {
        "command": [
          "event entity @s spider_sword_skill"
        ],
        "target": "holder"
      },
      "damage": {
        "type": "durability",
        "amount": 8,
        "target": "self"
      }
    },
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        },
        {
          "randomize": [
            {
              "weight": 95
            },
            {
              "weight": 5,
              "shoot": {
                "projectile": "entity:web",
                "launch_power": 1
              }
            }
          ]
        }
      ]
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/entities/player.json`: строки 216, 217, 219, 226, 866, 868, 873, 875, 1608, 1611, 1612, 1613, 1617, 1620, 1621, 1630, 1631, 1632, 1636, 1639, 1640
- `Swords_B/entities/spider.json`: строки 21, 386, 403
- `Swords_B/functions/give.mcfunction`: строки 22
- `Swords_B/loot_tables/chests/abandoned_mineshaft.json`: строки 124
- `Swords_R/texts/en_US.lang`: строки 10, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440
- `Swords_R/textures/item_texture.json`: строки 14, 15
- `Swords_R/ui/how_to_play_screen.json`: строки 58, 117, 735, 737, 738, 741, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754

### Рецепты и таблицы добычи с точным ID

`Swords_B/loot_tables/chests/abandoned_mineshaft.json`:

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:golden_apple",
          "weight": 20
        },
        {
          "type": "item",
          "name": "minecraft:appleEnchanted",
          "weight": 1
        },
        {
          "type": "item",
          "name": "minecraft:name_tag",
          "weight": 30
        },
        {
          "type": "item",
          "name": "minecraft:book",
          "weight": 10,
          "functions": [
            {
              "function": "enchant_randomly"
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:iron_pickaxe",
          "weight": 5
        },
        {
          "type": "empty",
          "weight": 5
        }
      ]
    },
    {
      "rolls": {
        "min": 2,
        "max": 4
      },
      "entries": [
        {
          "type": "item",
          "name": "minecraft:iron_ingot",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 5
              }
            }
          ],
          "weight": 10
        },
        {
          "type": "item",
          "name": "minecraft:gold_ingot",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:redstone",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 4,
                "max": 9
              }
            }
          ],
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:dye",
          "functions": [
            {
              "function": "set_data",
              "data": 4
            },
            {
              "function": "set_count",
              "count": {
                "min": 4,
                "max": 9
              }
            }
          ],
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:diamond",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ],
          "weight": 3
        },
        {
          "type": "item",
          "name": "effect:spider_sword",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 1
              }
            }
          ],
          "weight": 3
        },
        {
          "type": "item",
          "name": "minecraft:coal",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 3,
                "max": 8
              }
            }
          ],
          "weight": 10
        },
        {
          "type": "item",
          "name": "minecraft:bread",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "weight": 15
        },
        {
          "type": "item",
          "name": "minecraft:melon_seeds",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 2,
                "max": 4
              }
            }
          ],
          "weight": 10
        },
        {
          "type": "item",
          "name": "minecraft:pumpkin_seeds",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 2,
                "max": 4
              }
            }
          ],
          "weight": 10
        },
        {
          "type": "item",
          "name": "minecraft:beetroot_seeds",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 2,
                "max": 4
              }
            }
          ],
          "weight": 10
        }
      ]
    },
    {
      "rolls": 3,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:rail",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 4,
                "max": 8
              }
            }
          ],
          "weight": 20
        },
        {
          "type": "item",
          "name": "minecraft:golden_rail",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 4
              }
            }
          ],
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:detector_rail",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 4
              }
            }
          ],
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:activator_rail",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 4
              }
            }
          ],
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:torch",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 16
              }
            }
          ],
          "weight": 15
        }
      ]
    }
  ]
}
```


### Одноимённые группы и события игрока (`Swords_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:spider_sword": {
      "minecraft:type_family": {
        "family": [
          "player",
          "spider_sword"
        ]
      }
    },
    "spider_sword_skill": {
      "minecraft:spawn_entity": [
        {
          "min_wait_time": 0,
          "max_wait_time": 0,
          "single_use": false,
          "spawn_entity": "entity:web",
          "num_to_spawn": 1
        }
      ],
      "minecraft:timer": {
        "time": [
          2,
          2
        ],
        "looping": false,
        "time_down_event": {
          "event": "stop_spider_skill_event",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "spider_sword",
          "spider_sword_skill"
        ]
      }
    }
  },
  "events": {
    "minecraft:spider_sword": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "!=",
            "value": "spider_sword"
          },
          "add": {
            "component_groups": [
              "minecraft:spider_sword"
            ]
          },
          "run_command": {
            "command": [
              "ride @s summon_ride minecraft:spider no_ride_change minecraft:spider_sword",
              "particle minecraft:example_linearcurve ~ ~ ~"
            ]
          }
        }
      ]
    },
    "stop_spider_sword_event": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "==",
            "value": "spider_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:spider_sword",
              "spider_sword_skill"
            ]
          },
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "run_command": {
            "command": [
              "ride @s stop_riding"
            ]
          }
        }
      ]
    },
    "spider_sword_skill": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "!=",
            "value": "spider_sword_skill"
          },
          "add": {
            "component_groups": [
              "spider_sword_skill"
            ]
          }
        }
      ]
    }
  }
}
```

## effect:sponge_sword

- Название в en_US: `§l§eSponge Sword`
- Определение: `Swords_B/items/sponge_sword.json`
- Урон (`minecraft:damage`): `5`
- Прочность (`minecraft:durability`): `{"max_durability":128}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:sponge_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:durability": {
      "max_durability": 128
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "sponge_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:sponge_sword"
          ],
          "repair_amount": 128
        },
        {
          "items": [
            "minecraft:sponge"
          ],
          "repair_amount": 62
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 5,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/entities/item.json`: строки 19, 21, 23, 66, 69, 75, 78, 115, 118, 119, 134, 136
- `Swords_B/entities/player.json`: строки 213, 214, 880, 882, 887, 889, 1560, 1563, 1564, 1565, 1574, 1583, 1584, 1585, 1591, 1594, 1595, 1599, 1602, 1603
- `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/tag_swords.mcfunction`: строки 7
- `Swords_B/functions/give.mcfunction`: строки 23
- `Swords_B/items/wet_sponge_sword.json`: строки 5, 21, 27, 39
- `Swords_B/loot_tables/entities/elder_guardian.json`: строки 44
- `Swords_B/recipes/wet_sponge_sword.json`: строки 5, 11, 12
- `Swords_R/texts/en_US.lang`: строки 30, 31, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237
- `Swords_R/textures/item_texture.json`: строки 65, 66, 92, 93
- `Swords_R/ui/how_to_play_screen.json`: строки 44, 103, 395, 397, 398, 401, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 414, 415, 416, 417, 418, 419, 420

### Рецепты и таблицы добычи с точным ID

`Swords_B/loot_tables/entities/elder_guardian.json`:

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:prismarine_shard",
          "weight": 1,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 0,
                "max": 2
              }
            },
            {
              "function": "looting_enchant",
              "count": {
                "min": 0,
                "max": 1
              }
            }
          ]
        }
      ]
    },
    {
      "conditions": [
        {
          "condition": "killed_by_player"
        },
        {
          "condition": "random_chance_with_looting",
          "chance": 0.065,
          "looting_multiplier": 0.02
        }
      ],
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "effect:sponge_sword",
          "weight": 1,
          "functions": [
            {
               "function": "set_count",
               "count": {
                 "min": 1,
                 "max": 1
               }
             },
            {
              "function": "set_data",
              "data": 0
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:fish",
          "weight": 3,
          "functions": [
            {
              "function": "looting_enchant",
              "count": {
                "min": 0,
                "max": 1
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:prismarine_crystals",
          "weight": 2,
          "functions": [
            {
              "function": "looting_enchant",
              "count": {
                "min": 0,
                "max": 1
              }
            }
          ]
        },
        {
          "type": "empty",
          "weight": 1
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:sponge",
          "weight": 1,
          "functions": [
            {
              "function": "set_data",
              "data": 1
            }
          ]
        }
      ],
      "conditions": [
        {
          "condition": "killed_by_player"
        }
      ]
    },
    {
      "conditions": [
        {
          "condition": "killed_by_player"
        },
        {
          "condition": "random_chance_with_looting",
          "chance": 0.025,
          "looting_multiplier": 0.01
        }
      ],
      "rolls": 1,
      "entries": [
        {
          "type": "loot_table",
          "name": "loot_tables/gameplay/fishing/fish",
          "weight": 1
        }
      ]
    }
  ]
}
```

`Swords_B/recipes/wet_sponge_sword.json`:

```json
{
  "format_version": "1.12",
  "minecraft:recipe_furnace": {
    "description": {
      "identifier": "effect:wet_sponge_sword"
    },
    "tags": [
      "furnace",
      "blast_furnace"
    ],
    "input": "effect:wet_sponge_sword",
    "output": "effect:sponge_sword"
  }
}
```


### Одноимённые группы и события игрока (`Swords_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:sponge_sword": {
      "minecraft:type_family": {
        "family": [
          "player",
          "sponge_sword"
        ]
      }
    }
  },
  "events": {
    "minecraft:sponge_sword": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "!=",
            "value": "sponge_sword"
          },
          "add": {
            "component_groups": [
              "minecraft:sponge_sword"
            ]
          },
          "run_command": {
            "command": [
              "scoreboard objectives add sponge_sword dummy"
            ]
          }
        },
        {
          "filters": {
            "test": "in_water_or_rain"
          },
          "run_command": {
            "command": [
              "fill ~2 ~2 ~2 ~-2 ~-2 ~-2 sponge 0 replace water",
              "playsound random.fizz @a[r=12] ~~~ 0.6",
              "particle minecraft:cauldron_explosion_emitter ~ ~ ~",
              "scoreboard players add @s sponge_sword 1"
            ]
          }
        },
        {
          "run_command": {
            "command": [
              "fill ~2 ~2 ~2 ~-2 ~-2 ~-2 air 0 replace sponge",
              "fill ~2 ~2 ~2 ~-2 ~-2 ~-2 air 0 replace seagrass",
              "execute @s[scores={sponge_sword=150}] ~ ~ ~ event entity @s wet_sponge_sword",
              "execute @s[scores={sponge_sword=155}] ~ ~ ~ event entity @s wet_sponge_sword",
              "execute @s[scores={sponge_sword=160}] ~ ~ ~ event entity @s wet_sponge_sword"
            ]
          }
        }
      ]
    },
    "wet_sponge_sword": {
      "sequence": [
        {
          "filters": {
            "test": "has_equipment",
            "subject": "self",
            "domain": "hand",
            "value": "effect:sponge_sword"
          },
          "run_command": {
            "command": [
              "replaceitem entity @s slot.weapon.mainhand 0 effect:wet_sponge_sword 1",
              "scoreboard players set @s sponge_sword 0",
              "title @s actionbar §l§gWet Sponge Sword"
            ]
          }
        }
      ]
    },
    "stop_sponge_sword_event": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "==",
            "value": "sponge_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:sponge_sword"
            ]
          },
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          }
        }
      ]
    }
  }
}
```

## effect:time_sword

- Название в en_US: `§lTime Sword`
- Определение: `Swords_B/items/time_sword.json`
- Урон (`minecraft:damage`): `13`
- Прочность (`minecraft:durability`): `{"max_durability":13770}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:time_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": true,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 13770
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "time_sword"
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:render_offsets": {
      "main_hand": {
        "first_person": {
          "position": [
            1,
            0.5,
            -3
          ],
          "scale": [
            0.04,
            0.04,
            0.04
          ]
        },
        "third_person": {
          "position": [
            0.95,
            3.3,
            -1.2
          ],
          "scale": [
            0.06,
            0.06,
            0.06
          ]
        }
      }
    },
    "minecraft:display_name": {},
    "minecraft:damage": 13,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "randomize": [
        {
          "weight": 90,
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        },
        {
          "weight": 6,
          "damage": {
            "type": "durability",
            "amount": 16,
            "target": "self"
          }
        },
        {
          "weight": 3,
          "damage": {
            "type": "durability",
            "amount": 32,
            "target": "self"
          }
        },
        {
          "weight": 1,
          "damage": {
            "type": "durability",
            "amount": 64,
            "target": "self"
          }
        }
      ]
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/entities/item.json`: строки 176
- `Swords_B/entities/player.json`: строки 206, 208, 210, 894, 896, 901, 903, 1537, 1540, 1543, 1547, 1550, 1551, 1557, 1558
- `Swords_B/functions/give.mcfunction`: строки 24
- `Swords_R/texts/en_US.lang`: строки 22, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659
- `Swords_R/textures/item_texture.json`: строки 41, 42
- `Swords_R/ui/how_to_play_screen.json`: строки 71, 130, 1079, 1081, 1082, 1085, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098

### Одноимённые группы и события игрока (`Swords_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:time_sword": {
      "minecraft:movement": {
        "value": 1
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "time_sword"
        ]
      }
    },
    "time_sword_movement": {
      "minecraft:movement": {
        "value": 1
      }
    }
  },
  "events": {
    "minecraft:time_sword": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:time_sword"
            ]
          }
        },
        {
          "run_command": {
            "command": [
              "gamerule randomtickspeed 300",
              "effect @e[type=!player] speed 1 15 true",
              "time add 30",
              "event entity @a[family=default_player] time_sword_movement",
              "fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace air",
              "fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock2 0 replace effect99:lightblock2"
            ]
          }
        }
      ]
    },
    "stop_time_sword_event": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "==",
            "value": "time_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:time_sword"
            ]
          },
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "run_command": {
            "command": [
              "gamerule randomtickspeed 1",
              "effect @e[type=!player] speed 0 0",
              "event entity @a[family=default_player] default_player"
            ]
          }
        }
      ]
    },
    "time_sword_movement": {
      "add": {
        "component_groups": [
          "time_sword_movement"
        ]
      }
    }
  }
}
```

## effect:tnt_sword

- Название в en_US: `§4TNT§f Sword`
- Определение: `Swords_B/items/tnt_sword.json`
- Урон (`minecraft:damage`): `4`
- Прочность (`minecraft:durability`): `{"max_durability":64}`
- Кулдаун (`minecraft:cooldown`): `{"category":"tnt_sword","duration":10}`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:tnt_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:durability": {
      "max_durability": 64
    },
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:cooldown": {
      "category": "tnt_sword",
      "duration": 10
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "tnt_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:tnt_sword"
          ],
          "repair_amount": 64
        },
        {
          "items": [
            "minecraft:tnt"
          ],
          "repair_amount": 18
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 4,
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "on_use": {
      "run_command": {
        "command": [
          "summon minecraft:tnt ~~~ giant_tnt",
          "title @a[r=18] actionbar §fSuper§4TNT §f§lhas been activated.",
          "playsound random.fuse @a ~~~"
        ]
      },
      "damage": {
        "type": "durability",
        "amount": 18,
        "target": "self"
      }
    },
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        },
        {
          "randomize": [
            {
              "weight": 10
            },
            {
              "weight": 90,
              "shoot": {
                "projectile": "entity:tnt",
                "launch_power": 1
              }
            }
          ]
        }
      ]
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/animation_controllers/item_events.json`: строки 16
- `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/tag_swords.mcfunction`: строки 2
- `Swords_B/functions/give.mcfunction`: строки 25
- `Swords_B/loot_tables/chests/desert_pyramid.json`: строки 114
- `Swords_R/texts/en_US.lang`: строки 27, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455
- `Swords_R/textures/item_texture.json`: строки 56, 57
- `Swords_R/ui/how_to_play_screen.json`: строки 59, 118, 759, 761, 762, 765, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778

### Рецепты и таблицы добычи с точным ID

`Swords_B/loot_tables/chests/desert_pyramid.json`:

```json
{
  "pools": [
    {
      "rolls": {
        "min": 2,
        "max": 4
      },
      "entries": [
        {
          "type": "item",
          "name": "minecraft:diamond",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:iron_ingot",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 5
              }
            }
          ],
          "weight": 15
        },
        {
          "type": "item",
          "name": "minecraft:gold_ingot",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 2,
                "max": 7
              }
            }
          ],
          "weight": 15
        },
        {
          "type": "item",
          "name": "minecraft:emerald",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "weight": 15
        },
        {
          "type": "item",
          "name": "minecraft:bone",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 4,
                "max": 6
              }
            }
          ],
          "weight": 25
        },
        {
          "type": "item",
          "name": "minecraft:spider_eye",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "weight": 25
        },
        {
          "type": "item",
          "name": "minecraft:rotten_flesh",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 3,
                "max": 7
              }
            }
          ],
          "weight": 25
        },
        {
          "type": "item",
          "name": "minecraft:saddle",
          "weight": 20
        },
        {
          "type": "item",
          "name": "effect:tnt_sword",
          "weight": 10
        },
        {
          "type": "item",
          "name": "minecraft:horsearmoriron",
          "weight": 15
        },
        {
          "type": "item",
          "name": "minecraft:horsearmorgold",
          "weight": 10
        },
        {
          "type": "item",
          "name": "minecraft:horsearmordiamond",
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:book",
          "weight": 20,
          "functions": [
            {
              "function": "enchant_randomly"
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:golden_apple",
          "weight": 20
        },
        {
          "type": "item",
          "name": "minecraft:appleEnchanted",
          "weight": 2
        },
        {
          "type": "empty",
          "weight": 15
        }
      ]
    },
    {
      "rolls": 4,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:bone",
          "weight": 10,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 8
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:gunpowder",
          "weight": 10,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 8
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:rotten_flesh",
          "weight": 10,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 8
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:string",
          "weight": 10,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 8
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:sand",
          "weight": 10,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 8
              }
            }
          ]
        }
      ]
    }
  ]
}
```


## effect:ultra_instinct_sword

- Название в en_US: `§lUltra Instinct Sword`
- Определение: `Swords_B/items/ultra_instinct_sword.json`
- Урон (`minecraft:damage`): `16`
- Прочность (`minecraft:durability`): `{"max_durability":9999}`
- Кулдаун (`minecraft:cooldown`): `{"category":"ultra_instinct_sword","duration":61}`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:ultra_instinct_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": true,
    "minecraft:should_despawn": false,
    "minecraft:max_stack_size": 1,
    "minecraft:durability": {
      "max_durability": 9999
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "ultra_instinct_sword"
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 999
        },
        {
          "block": "minecraft:bamboo",
          "speed": 999
        }
      ]
    },
    "minecraft:render_offsets": {
      "main_hand": {
        "first_person": {
          "rotation": [
            0,
            -5.0,
            95
          ],
          "position": [
            1.8,
            -1.4,
            -5.5
          ],
          "scale": [
            0.04,
            0.04,
            0.04
          ]
        },
        "third_person": {
          "position": [
            1.5,
            3.6,
            -1.8
          ],
          "scale": [
            0.04,
            0.04,
            0.04
          ]
        }
      }
    },
    "minecraft:display_name": {},
    "minecraft:damage": 16,
    "minecraft:cooldown": {
      "category": "ultra_instinct_sword",
      "duration": 61
    },
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "on_use": {
      "shoot": {
        "projectile": "entity:ultra_instinct_projectile",
        "launch_power": 1
      },
      "damage": {
        "type": "durability",
        "amount": 48,
        "target": "self"
      },
      "run_command": {
        "command": [
          "playsound mob.wither.ambient @s ~ ~1 ~ 2 0.6"
        ]
      }
    },
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/entities/item.json`: строки 152, 164
- `Swords_B/entities/player.json`: строки 95, 98, 113, 142, 144, 957, 959, 964, 966, 1360, 1363, 1364, 1381, 1385, 1388, 1389, 1395, 1397
- `Swords_B/entities/ultra_instinct_projectile.json`: строки 21, 50
- `Swords_B/functions/give.mcfunction`: строки 28
- `Swords_R/animations/mobs.animation.json`: строки 73
- `Swords_R/entity/player.entity.json`: строки 56, 65, 66, 85, 143
- `Swords_R/texts/en_US.lang`: строки 36, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674
- `Swords_R/textures/item_texture.json`: строки 86, 87
- `Swords_R/ui/how_to_play_screen.json`: строки 72, 131, 1104, 1106, 1107, 1110, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124

### Одноимённые группы и события игрока (`Swords_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:ultra_instinct_sword": {
      "minecraft:knockback_resistance": {
        "value": 1.0
      },
      "minecraft:timer": {
        "time": [
          0.1,
          0.2
        ],
        "looping": true,
        "randomInterval": true,
        "time_down_event": {
          "event": "ultra_instinct_sword_effects",
          "target": "self"
        }
      },
      "minecraft:damage_sensor": {
        "triggers": [
          {
            "on_damage": {
              "filters": {
                "all_of": [
                  {
                    "test": "has_damage",
                    "operator": "!=",
                    "value": "lava"
                  },
                  {
                    "test": "has_damage",
                    "operator": "!=",
                    "value": "drowning"
                  },
                  {
                    "test": "has_damage",
                    "operator": "!=",
                    "value": "void"
                  },
                  {
                    "test": "has_damage",
                    "operator": "!=",
                    "value": "thorns"
                  },
                  {
                    "test": "has_damage",
                    "operator": "!=",
                    "value": "suicide"
                  },
                  {
                    "test": "has_damage",
                    "operator": "!=",
                    "value": "starve"
                  },
                  {
                    "test": "has_damage",
                    "operator": "!=",
                    "value": "fire"
                  },
                  {
                    "test": "has_damage",
                    "operator": "!=",
                    "value": "fire_tick"
                  },
                  {
                    "test": "has_damage",
                    "operator": "!=",
                    "value": "magic"
                  }
                ]
              },
              "event": "ultra_instinct_sword_skill"
            },
            "deals_damage": false
          },
          {
            "on_damage": {
              "filters": {
                "test": "has_damage",
                "value": "fire"
              }
            },
            "deals_damage": false
          },
          {
            "on_damage": {
              "filters": {
                "test": "has_damage",
                "value": "fire_tick"
              }
            },
            "deals_damage": false
          },
          {
            "on_damage": {
              "filters": {
                "any_of": [
                  {
                    "test": "has_damage",
                    "value": "block_explosion"
                  },
                  {
                    "test": "has_damage",
                    "value": "entity_explosion"
                  }
                ]
              }
            },
            "deals_damage": false
          },
          {
            "on_damage": {
              "filters": {
                "all_of": [
                  {
                    "test": "has_damage",
                    "value": "lava"
                  }
                ]
              }
            },
            "deals_damage": true
          }
        ]
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "ultra_instinct_sword"
        ]
      }
    },
    "ultra_instinct_sword_movement": {
      "minecraft:movement": {
        "value": 0.22
      }
    }
  },
  "events": {
    "minecraft:ultra_instinct_sword": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "!=",
            "value": "ultra_instinct_sword"
          },
          "add": {
            "component_groups": [
              "minecraft:ultra_instinct_sword"
            ]
          },
          "run_command": {
            "command": [
              "particle minecraft:example_flipbook ~ ~ ~",
              "particle minecraft:example_flipbook ~ ~1.5 ~",
              "playsound mob.wither.ambient @a[r=16] ~ ~1 ~ 2 0.6"
            ]
          }
        },
        {
          "run_command": {
            "command": [
              "camerashake add @a[r=32] 0.1 0.016 positional",
              "fill ~1 ~2 ~1 ~-1 ~2 ~-1 effect99:lightblock 0 replace air",
              "fill ~1 ~2 ~1 ~-1 ~2 ~-1 effect99:lightblock 0 replace effect99:lightblock",
              "effect @s hunger 0 0",
              "effect @s blindness 0 0",
              "effect @s slowness 0 0",
              "effect @s weakness 0 0",
              "effect @s mining_fatigue 0 0",
              "effect @s nausea 0 0",
              "effect @s instant_damage 0 0",
              "effect @s wither 0 0"
            ]
          },
          "add": {
            "component_groups": [
              "ultra_instinct_sword_movement"
            ]
          }
        }
      ]
    },
    "stop_ultra_instinct_sword_event": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "==",
            "value": "ultra_instinct_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:ultra_instinct_sword",
              "ultra_instinct_sword_movement"
            ]
          },
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "run_command": {
            "command": [
              "particle minecraft:example_flipbook ~ ~ ~",
              "particle minecraft:example_flipbook ~ ~1.5 ~",
              "playsound mob.wither.ambient @a[r=16] ~ ~1 ~ 2 0.6"
            ]
          }
        }
      ]
    },
    "ultra_instinct_sword_skill": {
      "run_command": {
        "command": [
          "spreadplayers ~ ~ 1 3 @s",
          "playsound mob.endermen.portal @a[r=17] ~ ~ ~ 1 0.6"
        ]
      }
    },
    "ultra_instinct_sword_effects": {
      "randomize": [
        {
          "weight": 1,
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.3 ~1 ~",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          }
        },
        {
          "weight": 1,
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~ ~2 ~0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          }
        },
        {
          "weight": 1,
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~-0.3 ~ ~",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          }
        },
        {
          "weight": 1,
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~ ~0.3 ~-0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          }
        },
        {
          "weight": 1,
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.3 ~1.5 ~0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          }
        },
        {
          "weight": 1,
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~-0.3 ~0.8 ~-0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          }
        },
        {
          "weight": 1,
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~-0.3 ~2 ~0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          }
        },
        {
          "weight": 1,
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.2 ~1 ~0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          }
        },
        {
          "weight": 1,
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.3 ~0.9 ~0.1",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          }
        },
        {
          "weight": 1,
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.2 ~2.3 ~-0.2",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          }
        },
        {
          "weight": 1,
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~-0.3 ~1.2 ~",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          }
        },
        {
          "weight": 1,
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.3 ~0.3 ~0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          }
        },
        {
          "weight": 1,
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.3 ~0.6 ~0.1",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          }
        },
        {
          "weight": 1,
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~-0.3 ~0.2 ~0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          }
        },
        {
          "weight": 1,
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.1 ~0.7 ~-0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          }
        }
      ]
    }
  }
}
```

## effect:wet_sponge_sword

- Название в en_US: `§l§gWet Sponge Sword`
- Определение: `Swords_B/items/wet_sponge_sword.json`
- Урон (`minecraft:damage`): `3`
- Прочность (`minecraft:durability`): `{"max_durability":64}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:wet_sponge_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:durability": {
      "max_durability": 64
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "wet_sponge_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:sponge_sword"
          ],
          "repair_amount": 64
        },
        {
          "items": [
            "minecraft:sponge"
          ],
          "repair_amount": 32
        },
        {
          "items": [
            "effect:wet_sponge_sword"
          ],
          "repair_amount": 64
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 3,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/entities/item.json`: строки 21, 134
- `Swords_B/entities/player.json`: строки 1583, 1584, 1585, 1591, 1595
- `Swords_B/recipes/wet_sponge_sword.json`: строки 5, 11
- `Swords_R/texts/en_US.lang`: строки 31
- `Swords_R/textures/item_texture.json`: строки 92, 93
- `Swords_R/ui/how_to_play_screen.json`: строки 415

### Рецепты и таблицы добычи с точным ID

`Swords_B/recipes/wet_sponge_sword.json`:

```json
{
  "format_version": "1.12",
  "minecraft:recipe_furnace": {
    "description": {
      "identifier": "effect:wet_sponge_sword"
    },
    "tags": [
      "furnace",
      "blast_furnace"
    ],
    "input": "effect:wet_sponge_sword",
    "output": "effect:sponge_sword"
  }
}
```


### Одноимённые группы и события игрока (`Swords_B/entities/player.json`)

```json
{
  "events": {
    "wet_sponge_sword": {
      "sequence": [
        {
          "filters": {
            "test": "has_equipment",
            "subject": "self",
            "domain": "hand",
            "value": "effect:sponge_sword"
          },
          "run_command": {
            "command": [
              "replaceitem entity @s slot.weapon.mainhand 0 effect:wet_sponge_sword 1",
              "scoreboard players set @s sponge_sword 0",
              "title @s actionbar §l§gWet Sponge Sword"
            ]
          }
        }
      ]
    }
  }
}
```

## effect:wither_skeleton_sword

- Название в en_US: `§l§7Wither Skeleton Sword`
- Определение: `Swords_B/items/wither_skeleton_sword.json`
- Урон (`minecraft:damage`): `4`
- Прочность (`minecraft:durability`): `{"max_durability":128}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:wither_skeleton_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 128
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "wither_skeleton_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:wither_skeleton_sword"
          ],
          "repair_amount": 128
        },
        {
          "items": [
            "minecraft:coal"
          ],
          "repair_amount": 58
        },
        {
          "items": [
            "minecraft:stick"
          ],
          "repair_amount": 2
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:display_name": {},
    "minecraft:damage": 4,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          },
          "shoot": {
            "projectile": "entity:wither_effect",
            "launch_power": 1
          }
        }
      ]
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/functions/give.mcfunction`: строки 29
- `Swords_B/loot_tables/entities/wither_skeleton.json`: строки 96
- `Swords_R/texts/en_US.lang`: строки 35, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275
- `Swords_R/textures/item_texture.json`: строки 83, 84
- `Swords_R/ui/how_to_play_screen.json`: строки 47, 106, 469, 471, 472, 475, 477, 478, 479, 480, 481, 482, 483, 484, 485

### Рецепты и таблицы добычи с точным ID

`Swords_B/loot_tables/entities/wither_skeleton.json`:

```json
{
    "pools": [
        {
            "rolls": 1,
            "entries": [
                {
                    "type": "item",
                    "name": "minecraft:coal",
                    "weight": 1,
                    "functions": [
                        {
                            "function": "set_count",
                            "count": {
                                "min": 0,
                                "max": 1
                            }
                        },
                        {
                            "function": "looting_enchant",
                            "count": {
                                "min": 0,
                                "max": 1
                            }
                        }
                    ]
                }
            ]
        },
        {
            "rolls": 1,
            "entries": [
                {
                    "type": "item",
                    "name": "minecraft:bone",
                    "weight": 1,
                    "functions": [
                        {
                            "function": "set_count",
                            "count": {
                                "min": 0,
                                "max": 2
                            }
                        },
                        {
                            "function": "looting_enchant",
                            "count": {
                                "min": 0,
                                "max": 1
                            }
                        }
                    ]
                }
            ]
        },
        {
            "conditions": [
                {
                    "condition": "killed_by_player"
                },
                {
                    "condition": "random_chance_with_looting",
                    "chance": 0.025,
                    "looting_multiplier": 0.02
                }
            ],
            "rolls": 1,
            "entries": [
                {
                    "type": "item",
                    "name": "minecraft:skull",
                    "weight": 1,
                    "functions": [
                        {
                            "function": "set_data",
                            "data": 1
                        }
                    ]
                }
            ]
        },
        {
            "conditions": [
                {
                    "condition": "killed_by_player"
                },
                {
                    "condition": "random_chance_with_looting",
                    "chance": 0.025,
                    "looting_multiplier": 0.02
                }
            ],
            "rolls": 1,
            "entries": [
                {
                    "type": "item",
                    "name": "effect:wither_skeleton_sword",
                    "weight": 1,
                    "functions": [
                        {
                            "function": "set_data",
                            "data": 0
                        }
                    ]
                }
            ]
        }
    ]
}
```


## effect:wither_sword

- Название в en_US: `§l§7Wither Sword`
- Определение: `Swords_B/items/wither_sword.json`
- Урон (`minecraft:damage`): `10`
- Прочность (`minecraft:durability`): `{"max_durability":3856}`
- Кулдаун (`minecraft:cooldown`): `{"category":"wither_sword","duration":3}`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:wither_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:should_despawn": false,
    "minecraft:foil": true,
    "minecraft:max_stack_size": 1,
    "minecraft:durability": {
      "max_durability": 3856
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "wither_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:wither_sword"
          ],
          "repair_amount": 3856
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:render_offsets": {
      "main_hand": {
        "first_person": {
          "position": [
            0.8,
            0.1,
            -1.8
          ],
          "scale": [
            0.01,
            0.01,
            0.01
          ]
        },
        "third_person": {
          "position": [
            0.8,
            2.5,
            -1.2
          ],
          "scale": [
            0.027,
            0.027,
            0.027
          ]
        }
      }
    },
    "minecraft:display_name": {},
    "minecraft:damage": 10,
    "minecraft:cooldown": {
      "category": "wither_sword",
      "duration": 3
    },
    "minecraft:on_use": {
      "on_use": {
        "event": "on_use"
      }
    },
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      },
      "on_not_hurt_entity": {
        "event": "weapon"
      },
      "on_hit_block": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "on_use": {
      "shoot": {
        "projectile": "minecraft:wither_skull_dangerous",
        "launch_power": 1
      },
      "run_command": {
        "command": [
          "playsound mob.wither.shoot @a[r=16] ~~~ 1 0.7"
        ]
      },
      "damage": {
        "type": "durability",
        "amount": 3,
        "target": "self"
      }
    },
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        },
        {
          "randomize": [
            {
              "weight": 90
            },
            {
              "weight": 10,
              "shoot": {
                "projectile": "minecraft:wither_skull",
                "launch_power": 1
              },
              "run_command": {
                "command": [
                  "playsound mob.wither.shoot @a[r=16]"
                ]
              }
            }
          ]
        }
      ]
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/animation_controllers/item_events.json`: строки 19
- `Swords_B/animation_controllers/wither_sword.json`: строки 4, 9, 13, 15
- `Swords_B/entities/entity_name.json`: строки 19, 38
- `Swords_B/entities/player.json`: строки 10, 14, 191, 202, 204, 908, 910, 915, 917, 1492, 1495, 1496, 1521, 1524, 1525, 1531
- `Swords_B/entities/wither.json`: строки 48, 154, 163
- `Swords_B/entities/wither_skull.json`: строки 11, 101, 102
- `Swords_B/entities/wither_skull_dangerous.json`: строки 11, 106, 107
- `Swords_B/functions/commands/swords_and_more_swords/swords_and_more_swords/tag_swords.mcfunction`: строки 4
- `Swords_B/functions/give.mcfunction`: строки 26
- `Swords_R/texts/en_US.lang`: строки 26, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644
- `Swords_R/textures/item_texture.json`: строки 53, 54
- `Swords_R/ui/how_to_play_screen.json`: строки 70, 129, 1049, 1051, 1052, 1055, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074

### Одноимённые группы и события игрока (`Swords_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:wither_sword": {
      "minecraft:rideable": {
        "seat_count": 1,
        "family_types": [
          "entity_name"
        ],
        "seats": {
          "position": [
            0.0,
            0.4,
            0.0
          ],
          "lock_rider_rotation": 0
        }
      },
      "minecraft:damage_sensor": {
        "triggers": {
          "on_damage": {
            "filters": {
              "all_of": [
                {
                  "test": "has_damage",
                  "subject": "self",
                  "value": "wither"
                }
              ]
            }
          },
          "deals_damage": false
        }
      },
      "minecraft:timer": {
        "time": [
          4,
          18
        ],
        "looping": true,
        "randomInterval": true,
        "time_down_event": {
          "event": "wither_sword_effects",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "wither_sword"
        ]
      }
    }
  },
  "events": {
    "minecraft:wither_sword": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "!=",
            "value": "wither_sword"
          },
          "add": {
            "component_groups": [
              "minecraft:wither_sword"
            ]
          },
          "run_command": {
            "command": [
              "playsound mob.wither.spawn @a[r=16]"
            ]
          }
        },
        {
          "run_command": {
            "command": [
              "fill ~5 ~5 ~5 ~-5 ~-5 ~-5 dirt 1 replace grass",
              "fill ~5 ~5 ~5 ~-5 ~-5 ~-5 air 0 replace leaves2",
              "fill ~5 ~5 ~5 ~-5 ~-5 ~-5 air 0 replace leaves",
              "fill ~5 ~5 ~5 ~-5 ~-5 ~-5 air 0 replace vine",
              "fill ~5 ~5 ~5 ~-5 ~-5 ~-5 water 0 replace ice",
              "fill ~5 ~5 ~5 ~-5 ~-5 ~-5 dirt 0 replace farmland",
              "fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace red_flower",
              "fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace yellow_flower",
              "fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace red_mushroom",
              "fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace brown_mushroom",
              "fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace double_plant",
              "effect @s wither 39960 1 true",
              "fill ~1 ~2 ~1 ~-1 ~2 ~-1 effect99:lightblock2 0 replace air",
              "fill ~1 ~2 ~1 ~-1 ~2 ~-1 effect99:lightblock2 0 replace effect99:lightblock2"
            ]
          }
        }
      ]
    },
    "stop_wither_sword_event": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "==",
            "value": "wither_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:wither_sword"
            ]
          },
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "run_command": {
            "command": [
              "effect @s wither 0 0",
              "ride @s evict_riders"
            ]
          }
        }
      ]
    },
    "wither_sword_effects": {
      "randomize": [
        {
          "weight": 50,
          "run_command": {
            "command": [
              "playsound mob.wither.death @a[r=16]"
            ]
          }
        },
        {
          "weight": 50,
          "run_command": {
            "command": [
              "playsound mob.wither.hurt @a[r=16]"
            ]
          }
        }
      ]
    }
  }
}
```

## effect:wolf_sword

- Название в en_US: `§l§7Wolf Sword`
- Определение: `Swords_B/items/wolf_sword.json`
- Урон (`minecraft:damage`): `5`
- Прочность (`minecraft:durability`): `{"max_durability":2800}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:wolf_sword",
    "category": "equipment"
  },
  "components": {
    "minecraft:foil": false,
    "minecraft:max_stack_size": 1,
    "minecraft:durability": {
      "max_durability": 2800
    },
    "minecraft:allow_off_hand": false,
    "minecraft:hand_equipped": true,
    "minecraft:creative_category": {
      "parent": "itemGroup.name.sword"
    },
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "wolf_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:wolf_sword"
          ],
          "repair_amount": 2800
        }
      ]
    },
    "minecraft:digger": {
      "use_efficiency": true,
      "destroy_speeds": [
        {
          "block": "minecraft:web",
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "minecraft:render_offsets": {
      "main_hand": {
        "first_person": {
          "position": [
            0.67,
            0,
            -1.22
          ]
        },
        "third_person": {
          "position": [
            0.36,
            1.5,
            -0.66
          ]
        }
      }
    },
    "minecraft:display_name": {},
    "minecraft:damage": 5,
    "minecraft:weapon": {
      "on_hurt_entity": {
        "event": "weapon"
      }
    }
  },
  "events": {
    "weapon": {
      "sequence": [
        {
          "damage": {
            "type": "durability",
            "amount": 1,
            "target": "self"
          }
        }
      ]
    }
  }
}
```

### Прямые текстовые упоминания

- `Swords_B/animation_controllers/wolf_sword.json`: строки 4, 9, 13, 15, 25, 30, 34, 46, 51, 55
- `Swords_B/entities/alpha_wolf.json`: строки 103, 257, 264, 268, 278
- `Swords_B/entities/player.json`: строки 10, 15, 16, 17, 67, 68, 71, 85, 90, 971, 973, 978, 980, 1283, 1286, 1287, 1292, 1295, 1296, 1308, 1325, 1326, 1344, 1352, 1356
- `Swords_B/functions/give.mcfunction`: строки 27
- `Swords_R/entity/player.entity.json`: строки 57, 58
- `Swords_R/sounds/sound_definitions.json`: строки 4, 8, 11, 15
- `Swords_R/texts/en_US.lang`: строки 37, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475
- `Swords_R/textures/item_texture.json`: строки 89, 90
- `Swords_R/ui/how_to_play_screen.json`: строки 60, 119, 783, 785, 786, 789, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807

### Одноимённые группы и события игрока (`Swords_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:wolf_sword": {
      "minecraft:type_family": {
        "family": [
          "player",
          "wolf_sword"
        ]
      }
    }
  },
  "events": {
    "minecraft:wolf_sword": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "!=",
            "value": "wolf_sword"
          },
          "add": {
            "component_groups": [
              "minecraft:wolf_sword"
            ]
          },
          "run_command": {
            "command": [
              "effect @s nausea 0 0",
              "effect @s blindness 0 0",
              "effect @s nausea 0 0"
            ]
          }
        }
      ]
    },
    "stop_wolf_sword_event": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "==",
            "value": "wolf_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:wolf_sword",
              "wolf_transformation",
              "wolf_movement"
            ]
          },
          "run_command": {
            "command": [
              "effect @s nausea 0 0"
            ]
          },
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          }
        },
        {
          "filters": {
            "test": "is_family",
            "value": "complete_wolf_transformation"
          },
          "remove": {
            "component_groups": [
              "complete_wolf_transformation"
            ]
          },
          "run_command": {
            "command": [
              "effect @s nausea 9999 0 true",
              "effect @s blindness 9999 0 true"
            ]
          },
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          }
        }
      ]
    },
    "wolf_sword_start_events": {
      "sequence": [
        {
          "filters": {
            "test": "is_family",
            "subject": "self",
            "operator": "!=",
            "value": "wolf_transformation"
          },
          "add": {
            "component_groups": [
              "wolf_transformation"
            ]
          },
          "run_command": {
            "command": [
              "function commands/swords_and_more_swords/swords_and_more_swords/tellraw1"
            ]
          }
        }
      ]
    },
    "wolf_sword_sounds": {
      "randomize": [
        {
          "weight": 1,
          "run_command": {
            "command": [
              "playsound mob.wolf.growl @a[r=16] ~ ~ ~ 1 0.9 24"
            ]
          }
        }
      ]
    }
  }
}
```

