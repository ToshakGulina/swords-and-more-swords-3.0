# Блоки, рецепты, генерация, торговля и таблицы добычи — архив 2.8.14

Структурная выписка JSON файлов каталогов loot_tables, blocks, recipes, spawn_rules, features, feature_rules и trading behavior pack. Числа, условия, функции, веса, число бросков и порядок массивов приводятся как в JSON5. Это не ручное доказательство того, что файл загружен/вызывается, и не включает полный анализ структур и исполнения в игре.

Для loot приводятся **сырые относительные доли** по явно указанным целым weight только если у всех записей пула они есть и сумма > 0. Число бросков, условия пула/записи, типы записей, функции, удача и семантика движка могут изменить результат: доли не являются вероятностью получить предмет. При пропущенном весе доля не вычисляется. Все данные самого пула приведены целиком.

## `Swords_B/blocks/lightblock.json`

```json
{
  "format_version": "1.16.100",
  "minecraft:block": {
    "description": {
      "identifier": "effect99:lightblock"
    },
    "components": {
      "minecraft:loot": "loot_tables/empty.json",
      "minecraft:destroy_time": 0.1,
      "minecraft:material_instances": {
        "*": {
          "texture": "lightblock",
          "render_method": "blend"
        }
      },
      "minecraft:geometry": "geometry.null",
      "minecraft:entity_collision": {
        "origin": [
          -8,
          0,
          -8
        ],
        "size": [
          0,
          0,
          0
        ]
      },
      "minecraft:pick_collision": {
        "origin": [
          -8,
          0,
          -8
        ],
        "size": [
          0,
          0,
          0
        ]
      },
      "minecraft:explosion_resistance": 999,
      "minecraft:block_light_emission": 1,
      "minecraft:block_light_absorption": 0,
      "minecraft:map_color": "#000000",
      "minecraft:ticking": {
        "looping": true,
        "range": [
          0.2,
          0.2
        ],
        "on_tick": {
          "event": "glowstone_sword",
          "target": "self"
        }
      }
    },
    "events": {
      "glowstone_sword": {
        "sequence": [
          {
            "run_command": {
              "command": [
                "setblock ~ ~ ~ air 0"
              ]
            }
          }
        ]
      }
    }
  }
}
```

## `Swords_B/blocks/lightblock2.json`

```json
{
  "format_version": "1.16.100",
  "minecraft:block": {
    "description": {
      "identifier": "effect99:lightblock2"
    },
    "components": {
      "minecraft:loot": "loot_tables/empty.json",
      "minecraft:destroy_time": 0.1,
      "minecraft:material_instances": {
        "*": {
          "texture": "lightblock2",
          "render_method": "blend"
        }
      },
      "minecraft:geometry": "geometry.null",
      "minecraft:entity_collision": {
        "origin": [
          -8,
          0,
          -8
        ],
        "size": [
          0,
          0,
          0
        ]
      },
      "minecraft:pick_collision": {
        "origin": [
          -8,
          0,
          -8
        ],
        "size": [
          0,
          0,
          0
        ]
      },
      "minecraft:explosion_resistance": 999,
      "minecraft:block_light_emission": 0.5,
      "minecraft:block_light_absorption": 0,
      "minecraft:map_color": "#000000",
      "minecraft:ticking": {
        "looping": true,
        "range": [
          0.2,
          0.2
        ],
        "on_tick": {
          "event": "block_light_emission",
          "target": "self"
        }
      }
    },
    "events": {
      "block_light_emission": {
        "sequence": [
          {
            "run_command": {
              "command": [
                "setblock ~ ~ ~ air 0"
              ]
            }
          }
        ]
      }
    }
  }
}
```

## `Swords_B/blocks/quartz_diamond_block.json`

```json
{
  "format_version": "1.10.0",
  "minecraft:block": {
    "description": {
      "identifier": "effect99:quartz_diamond_block"
    },
    "components": {
      "minecraft:loot": "loot_tables/blocks/null.json",
      "minecraft:destroy_time": 20,
      "minecraft:explosion_resistance": 999,
      "minecraft:block_light_emission": 0,
      "minecraft:flammable": {
        "flame_odds": 0,
        "burn_odds": 0
      },
      "minecraft:on_player_destroyed": {
        "condition": "q.get_equipped_item_name == 'iron_pickaxe' || q.get_equipped_item_name == 'diamond_pickaxe'|| q.get_equipped_item_name == 'netherite_pickaxe' || q.get_equipped_item_name == 'bedrock_sword'",
        "event": "quartz_diamond_block"
      },
      "minecraft:block_light_absorption": 15,
      "minecraft:map_color": "#000000"
    },
    "events": {
      "quartz_diamond_block": {
        "spawn_loot": {
          "table": "loot_tables/blocks/quartz_diamond_block.json"
        },
        "run_command": {
          "command": [
            "particle minecraft:knockback_roar_particle ~ ~1 ~",
            "effect @p[r=6] instant_damage 1 0 true"
          ]
        }
      }
    }
  }
}
```

## `Swords_B/blocks/quartz_diamond_ore.json`

```json
{
  "format_version": "1.10.0",
  "minecraft:block": {
    "description": {
      "identifier": "effect99:quartz_diamond_ore"
    },
    "components": {
      "minecraft:loot": "loot_tables/blocks/null.json",
      "minecraft:destroy_time": 10,
      "minecraft:explosion_resistance": 999,
      "minecraft:light_emission": 0,
      "minecraft:on_player_destroyed": {
        "condition": "q.get_equipped_item_name == 'iron_pickaxe' || q.get_equipped_item_name == 'diamond_pickaxe'|| q.get_equipped_item_name == 'netherite_pickaxe' || q.get_equipped_item_name == 'bedrock_sword'",
        "event": "quartz_diamond_ore"
      },
      "minecraft:block_light_absorption": 15,
      "minecraft:map_color": "#000000"
    },
    "events": {
      "quartz_diamond_ore": {
        "spawn_loot": {
          "table": "loot_tables/blocks/quartz_diamond_ore.json"
        },
        "run_command": {
          "command": [
            "summon xp_orb",
            "summon xp_orb",
            "summon xp_orb",
            "summon xp_orb",
            "summon xp_orb",
            "summon xp_orb",
            "particle minecraft:knockback_roar_particle ~ ~1 ~",
            "effect @p[r=6] instant_damage 1 0 true"
          ]
        }
      }
    }
  }
}
```

## `Swords_B/blocks/sapling3.json`

```json
{
  "format_version": "1.16.100",
  "minecraft:block": {
    "description": {
      "identifier": "effect99:sapling3",
      "is_experimental": false,
      "register_to_creative_menu": true
    },
    "components": {
      "minecraft:destroy_time": 0.1,
      "minecraft:material_instances": {
        "*": {
          "texture": "null",
          "render_method": "blend"
        }
      },
      "minecraft:geometry": "geometry.null",
      "minecraft:entity_collision": {
        "origin": [
          -8,
          0,
          -8
        ],
        "size": [
          0,
          0,
          0
        ]
      },
      "minecraft:pick_collision": {
        "origin": [
          -8,
          0,
          -8
        ],
        "size": [
          0,
          0,
          0
        ]
      },
      "minecraft:explosion_resistance": 1,
      "minecraft:block_light_absorption": 0,
      "minecraft:map_color": "#000000",
      "minecraft:on_placed": {
        "event": "on_placed",
        "target": "self"
      }
    },
    "events": {
      "on_placed": {
        "sequence": [
          {
            "run_command": {
              "command": [
                "playsound dig.grass @a[r=12] ~ ~ ~",
                "fill ~ ~ ~ ~ ~ ~ sapling 3"
              ]
            }
          }
        ]
      }
    }
  }
}
```

## `Swords_B/blocks/silver_ore.json`

```json
{
  "format_version": "1.10.0",
  "minecraft:block": {
    "description": {
      "identifier": "effect99:silver_ore"
    },
    "components": {
      "minecraft:loot": "loot_tables/blocks/null.json",
      "minecraft:destroy_time": 8,
      "minecraft:explosion_resistance": 1,
      "minecraft:block_light_emission": 0,
      "minecraft:on_player_destroyed": {
        "condition": "q.get_equipped_item_name == 'iron_pickaxe' || q.get_equipped_item_name == 'diamond_pickaxe'|| q.get_equipped_item_name == 'netherite_pickaxe' || q.get_equipped_item_name == 'bedrock_sword'",
        "event": "silver_ore"
      },
      "minecraft:block_light_absorption": 15,
      "minecraft:map_color": "#000000"
    },
    "events": {
      "silver_ore": {
        "spawn_loot": {
          "table": "loot_tables/blocks/silver_ore.json"
        }
      }
    }
  }
}
```

## `Swords_B/blocks/spectral_block.json`

```json
{
  "format_version": "1.16.100",
  "minecraft:block": {
    "description": {
      "identifier": "effect99:spectral_block"
    },
    "components": {
      "minecraft:loot": "loot_tables/empty.json",
      "minecraft:destroy_time": 9999,
      "minecraft:geometry": "geometry.spectral_block",
      "minecraft:material_instances": {
        "*": {
          "texture": "spectral_block",
          "render_method": "blend"
        }
      },
      "minecraft:block_light_emission": 0,
      "minecraft:flammable": {
        "flame_odds": 0,
        "burn_odds": 0
      },
      "minecraft:explosion_resistance": 999,
      "minecraft:block_light_absorption": 0,
      "minecraft:map_color": "#000000"
    }
  }
}
```

## `Swords_B/loot_tables/bee_sword.json`

- Пул 0, rolls `1`, weights `[1]`, сумма 1.
  - Запись 0: `"effect:bee_sword"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.

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

## `Swords_B/loot_tables/blocks/quartz_diamond_block.json`

- Пул 0, rolls `1`, weights `[1]`, сумма 1.
  - Запись 0: `"effect99:quartz_diamond_block"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "effect99:quartz_diamond_block",
          "weight": 1,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 1
              }
            }
          ]
        }
      ]
    }
  ]
}
```

## `Swords_B/loot_tables/blocks/quartz_diamond_ore.json`

- Пул 0, rolls `1`, weights `[89,10,1]`, сумма 100.
  - Запись 0: `"effect:quartz_diamond"` — 89/100 (89%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"effect:quartz_diamond"` — 1/10 (10%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"effect:quartz_diamond"` — 1/100 (1%) от суммы явно указанных весов, до учёта условий и функций.

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

## `Swords_B/loot_tables/blocks/silver_ore.json`

- Пул 0, rolls `1`, weights `[1]`, сумма 1.
  - Запись 0: `"effect99:silver_ore"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "effect99:silver_ore",
          "weight": 1,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 1
              }
            }
          ]
        }
      ]
    }
  ]
}
```

## `Swords_B/loot_tables/chests/abandoned_mineshaft.json`

- Пул 0, rolls `1`, weights `[20,1,30,10,5,5]`, сумма 71.
  - Запись 0: `"minecraft:golden_apple"` — 20/71 (28.169%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:appleEnchanted"` — 1/71 (1.40845%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:name_tag"` — 30/71 (42.2535%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 3: `"minecraft:book"` — 10/71 (14.0845%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 4: `"minecraft:iron_pickaxe"` — 5/71 (7.04225%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 5: `"empty"` — 5/71 (7.04225%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 1, rolls `{"min":2,"max":4}`, weights `[10,5,5,5,3,3,10,15,10,10,10]`, сумма 86.
  - Запись 0: `"minecraft:iron_ingot"` — 5/43 (11.6279%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:gold_ingot"` — 5/86 (5.81395%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:redstone"` — 5/86 (5.81395%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 3: `"minecraft:dye"` — 5/86 (5.81395%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 4: `"minecraft:diamond"` — 3/86 (3.48837%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 5: `"effect:spider_sword"` — 3/86 (3.48837%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 6: `"minecraft:coal"` — 5/43 (11.6279%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 7: `"minecraft:bread"` — 15/86 (17.4419%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 8: `"minecraft:melon_seeds"` — 5/43 (11.6279%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 9: `"minecraft:pumpkin_seeds"` — 5/43 (11.6279%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 10: `"minecraft:beetroot_seeds"` — 5/43 (11.6279%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 2, rolls `3`, weights `[20,5,5,5,15]`, сумма 50.
  - Запись 0: `"minecraft:rail"` — 2/5 (40%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:golden_rail"` — 1/10 (10%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:detector_rail"` — 1/10 (10%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 3: `"minecraft:activator_rail"` — 1/10 (10%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 4: `"minecraft:torch"` — 3/10 (30%) от суммы явно указанных весов, до учёта условий и функций.

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

## `Swords_B/loot_tables/chests/buriedtreasure.json`

- Пул 0, rolls `1`, weights `[null]`; доли не вычислены.
- Пул 1, rolls `{"min":5,"max":12}`, weights `[5,20,10,10,15,5,5,10,15,20,20,20,20,5,10,3,15,10,1]`, сумма 219.
  - Запись 0: `"minecraft:prismarine_crystals"` — 5/219 (2.28311%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:iron_ingot"` — 20/219 (9.13242%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:gold_ingot"` — 10/219 (4.56621%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 3: `"minecraft:tnt"` — 10/219 (4.56621%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 4: `"minecraft:diamond"` — 5/73 (6.84932%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 5: `"minecraft:record_wait"` — 5/219 (2.28311%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 6: `"minecraft:record_mellohi"` — 5/219 (2.28311%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 7: `"minecraft:name_tag"` — 10/219 (4.56621%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 8: `"effect:sea_sword"` — 5/73 (6.84932%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 9: `"minecraft:chainmail_chestplate"` — 20/219 (9.13242%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 10: `"minecraft:chainmail_helmet"` — 20/219 (9.13242%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 11: `"minecraft:chainmail_leggings"` — 20/219 (9.13242%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 12: `"minecraft:chainmail_boots"` — 20/219 (9.13242%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 13: `"minecraft:writable_book"` — 5/219 (2.28311%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 14: `"minecraft:lead"` — 10/219 (4.56621%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 15: `"minecraft:experience_bottle"` — 1/73 (1.36986%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 16: `"minecraft:potion"` — 5/73 (6.84932%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 17: `"minecraft:potion"` — 10/219 (4.56621%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 18: `"minecraft:cake"` — 1/219 (0.456621%) от суммы явно указанных весов, до учёта условий и функций.

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

## `Swords_B/loot_tables/chests/desert_pyramid.json`

- Пул 0, rolls `{"min":2,"max":4}`, weights `[5,15,15,15,25,25,25,20,10,15,10,5,20,20,2,15]`, сумма 242.
  - Запись 0: `"minecraft:diamond"` — 5/242 (2.06612%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:iron_ingot"` — 15/242 (6.19835%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:gold_ingot"` — 15/242 (6.19835%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 3: `"minecraft:emerald"` — 15/242 (6.19835%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 4: `"minecraft:bone"` — 25/242 (10.3306%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 5: `"minecraft:spider_eye"` — 25/242 (10.3306%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 6: `"minecraft:rotten_flesh"` — 25/242 (10.3306%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 7: `"minecraft:saddle"` — 10/121 (8.26446%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 8: `"effect:tnt_sword"` — 5/121 (4.13223%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 9: `"minecraft:horsearmoriron"` — 15/242 (6.19835%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 10: `"minecraft:horsearmorgold"` — 5/121 (4.13223%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 11: `"minecraft:horsearmordiamond"` — 5/242 (2.06612%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 12: `"minecraft:book"` — 10/121 (8.26446%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 13: `"minecraft:golden_apple"` — 10/121 (8.26446%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 14: `"minecraft:appleEnchanted"` — 1/121 (0.826446%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 15: `"empty"` — 15/242 (6.19835%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 1, rolls `4`, weights `[10,10,10,10,10]`, сумма 50.
  - Запись 0: `"minecraft:bone"` — 1/5 (20%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:gunpowder"` — 1/5 (20%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:rotten_flesh"` — 1/5 (20%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 3: `"minecraft:string"` — 1/5 (20%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 4: `"minecraft:sand"` — 1/5 (20%) от суммы явно указанных весов, до учёта условий и функций.

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

## `Swords_B/loot_tables/chests/dispenser_trap.json`

- Пул 0, rolls `{"min":2,"max":2}`, weights `[30]`, сумма 30.
  - Запись 0: `"minecraft:arrow"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.

```json
{
  "pools": [
    {
      "rolls": {
        "min": 2,
        "max": 2
      },
      "entries": [
        {
          "type": "item",
          "name": "minecraft:arrow",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 2,
                "max": 7
              }
            }
          ],
          "weight": 30
        }
      ]
    }
  ]
}
```

## `Swords_B/loot_tables/chests/end_city_treasure.json`

- Пул 0, rolls `{"min":2,"max":6}`, weights `[5,10,15,2,5,3,1,1,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3]`, сумма 85.
  - Запись 0: `"minecraft:diamond"` — 1/17 (5.88235%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:iron_ingot"` — 2/17 (11.7647%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:gold_ingot"` — 3/17 (17.6471%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 3: `"minecraft:emerald"` — 2/85 (2.35294%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 4: `"minecraft:beetroot_seeds"` — 1/17 (5.88235%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 5: `"minecraft:saddle"` — 3/85 (3.52941%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 6: `"minecraft:horsearmoriron"` — 1/85 (1.17647%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 7: `"minecraft:horsearmorgold"` — 1/85 (1.17647%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 8: `"minecraft:horsearmordiamond"` — 1/85 (1.17647%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 9: `"minecraft:diamond_sword"` — 3/85 (3.52941%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 10: `"minecraft:diamond_boots"` — 3/85 (3.52941%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 11: `"minecraft:diamond_chestplate"` — 3/85 (3.52941%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 12: `"minecraft:diamond_leggings"` — 3/85 (3.52941%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 13: `"minecraft:diamond_helmet"` — 3/85 (3.52941%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 14: `"minecraft:diamond_pickaxe"` — 3/85 (3.52941%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 15: `"minecraft:diamond_shovel"` — 3/85 (3.52941%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 16: `"minecraft:iron_sword"` — 3/85 (3.52941%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 17: `"minecraft:iron_boots"` — 3/85 (3.52941%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 18: `"minecraft:iron_chestplate"` — 3/85 (3.52941%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 19: `"minecraft:iron_leggings"` — 3/85 (3.52941%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 20: `"minecraft:iron_helmet"` — 3/85 (3.52941%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 21: `"minecraft:iron_pickaxe"` — 3/85 (3.52941%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 22: `"minecraft:iron_shovel"` — 3/85 (3.52941%) от суммы явно указанных весов, до учёта условий и функций.

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
          "weight": 5,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 2,
                "max": 7
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:iron_ingot",
          "weight": 10,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 4,
                "max": 8
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:gold_ingot",
          "weight": 15,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 2,
                "max": 7
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:emerald",
          "weight": 2,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 2,
                "max": 6
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:beetroot_seeds",
          "weight": 5,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 10
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:saddle",
          "weight": 3
        },
        {
          "type": "item",
          "name": "minecraft:horsearmoriron",
          "weight": 1
        },
        {
          "type": "item",
          "name": "minecraft:horsearmorgold",
          "weight": 1
        },
        {
          "type": "item",
          "name": "minecraft:horsearmordiamond",
          "weight": 1
        },
        {
          "type": "item",
          "name": "minecraft:diamond_sword",
          "weight": 3,
          "functions": [
            {
              "function": "enchant_with_levels",
              "treasure": true,
              "levels": {
                "min": 20,
                "max": 39
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:diamond_boots",
          "weight": 3,
          "functions": [
            {
              "function": "enchant_with_levels",
              "treasure": true,
              "levels": {
                "min": 20,
                "max": 39
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:diamond_chestplate",
          "weight": 3,
          "functions": [
            {
              "function": "enchant_with_levels",
              "treasure": true,
              "levels": {
                "min": 20,
                "max": 39
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:diamond_leggings",
          "weight": 3,
          "functions": [
            {
              "function": "enchant_with_levels",
              "treasure": true,
              "levels": {
                "min": 20,
                "max": 39
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:diamond_helmet",
          "weight": 3,
          "functions": [
            {
              "function": "enchant_with_levels",
              "treasure": true,
              "levels": {
                "min": 20,
                "max": 39
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:diamond_pickaxe",
          "weight": 3,
          "functions": [
            {
              "function": "enchant_with_levels",
              "treasure": true,
              "levels": {
                "min": 20,
                "max": 39
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:diamond_shovel",
          "weight": 3,
          "functions": [
            {
              "function": "enchant_with_levels",
              "treasure": true,
              "levels": {
                "min": 20,
                "max": 39
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:iron_sword",
          "weight": 3,
          "functions": [
            {
              "function": "enchant_with_levels",
              "treasure": true,
              "levels": {
                "min": 20,
                "max": 39
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:iron_boots",
          "weight": 3,
          "functions": [
            {
              "function": "enchant_with_levels",
              "treasure": true,
              "levels": {
                "min": 20,
                "max": 39
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:iron_chestplate",
          "weight": 3,
          "functions": [
            {
              "function": "enchant_with_levels",
              "treasure": true,
              "levels": {
                "min": 20,
                "max": 39
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:iron_leggings",
          "weight": 3,
          "functions": [
            {
              "function": "enchant_with_levels",
              "treasure": true,
              "levels": {
                "min": 20,
                "max": 39
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:iron_helmet",
          "weight": 3,
          "functions": [
            {
              "function": "enchant_with_levels",
              "treasure": true,
              "levels": {
                "min": 20,
                "max": 39
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:iron_pickaxe",
          "weight": 3,
          "functions": [
            {
              "function": "enchant_with_levels",
              "treasure": true,
              "levels": {
                "min": 20,
                "max": 39
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:iron_shovel",
          "weight": 3,
          "functions": [
            {
              "function": "enchant_with_levels",
              "treasure": true,
              "levels": {
                "min": 20,
                "max": 39
              }
            }
          ]
        }
      ]
    }
  ]
}
```

## `Swords_B/loot_tables/chests/igloo_chest.json`

- Пул 0, rolls `{"min":2,"max":8}`, weights `[15,15,10,2,10,1,1,10]`, сумма 64.
  - Запись 0: `"minecraft:apple"` — 15/64 (23.4375%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:coal"` — 15/64 (23.4375%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:gold_nugget"` — 5/32 (15.625%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 3: `"minecraft:stone_axe"` — 1/32 (3.125%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 4: `"minecraft:rotten_flesh"` — 5/32 (15.625%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 5: `"minecraft:emerald"` — 1/64 (1.5625%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 6: `"effect:ice_sword"` — 1/64 (1.5625%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 7: `"minecraft:wheat"` — 5/32 (15.625%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 1, rolls `1`, weights `[1]`, сумма 1.
  - Запись 0: `"minecraft:golden_apple"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.

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

## `Swords_B/loot_tables/chests/jungle_temple.json`

- Пул 0, rolls `{"min":2,"max":6}`, weights `[15,50,75,10,100,80,75,15,16,5,5,5,6]`, сумма 457.
  - Запись 0: `"minecraft:diamond"` — 15/457 (3.28228%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:iron_ingot"` — 50/457 (10.9409%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:gold_ingot"` — 75/457 (16.4114%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 3: `"minecraft:emerald"` — 10/457 (2.18818%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 4: `"minecraft:bone"` — 100/457 (21.8818%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 5: `"minecraft:rotten_flesh"` — 80/457 (17.5055%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 6: `"minecraft:bamboo"` — 75/457 (16.4114%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 7: `"minecraft:saddle"` — 15/457 (3.28228%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 8: `"effect:jungle_sword"` — 16/457 (3.50109%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 9: `"minecraft:horsearmoriron"` — 5/457 (1.09409%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 10: `"minecraft:horsearmorgold"` — 5/457 (1.09409%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 11: `"minecraft:horsearmordiamond"` — 5/457 (1.09409%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 12: `"minecraft:book"` — 6/457 (1.31291%) от суммы явно указанных весов, до учёта условий и функций.

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

## `Swords_B/loot_tables/chests/monster_room.json`

- Пул 0, rolls `1`, weights `[10,10,10,10,10,10,10,10,5,5,2,1]`, сумма 93.
  - Запись 0: `"minecraft:iron_ingot"` — 10/93 (10.7527%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:redstone"` — 10/93 (10.7527%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:bread"` — 10/93 (10.7527%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 3: `"minecraft:golden_apple"` — 10/93 (10.7527%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 4: `"minecraft:wheat"` — 10/93 (10.7527%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 5: `"minecraft:gunpowder"` — 10/93 (10.7527%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 6: `"minecraft:string"` — 10/93 (10.7527%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 7: `"minecraft:name_tag"` — 10/93 (10.7527%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 8: `"minecraft:bucket"` — 5/93 (5.37634%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 9: `"minecraft:horsearmoriron"` — 5/93 (5.37634%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 10: `"minecraft:horsearmorgold"` — 2/93 (2.15054%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 11: `"minecraft:book"` — 1/93 (1.07527%) от суммы явно указанных весов, до учёта условий и функций.

```json
{
  "pools": [
    {
      "rolls": 1,
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
          "name": "minecraft:redstone",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 4
              }
            }
          ],
          "weight": 10
        },
        {
          "type": "item",
          "name": "minecraft:bread",
          "weight": 10
        },
        {
          "type": "item",
          "name": "minecraft:golden_apple",
          "weight": 10
        },
        {
          "type": "item",
          "name": "minecraft:wheat",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 4
              }
            }
          ],
          "weight": 10
        },
        {
          "type": "item",
          "name": "minecraft:gunpowder",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 4
              }
            }
          ],
          "weight": 10
        },
        {
          "type": "item",
          "name": "minecraft:string",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 4
              }
            }
          ],
          "weight": 10
        },
        {
          "type": "item",
          "name": "minecraft:name_tag",
          "weight": 10
        },
        {
          "type": "item",
          "name": "minecraft:bucket",
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
          "weight": 2
        },
        {
          "type": "item",
          "name": "minecraft:book",
          "weight": 1,
          "functions": [
            {
              "function": "enchant_randomly"
            }
          ]
        }
      ]
    }
  ]
}
```

## `Swords_B/loot_tables/chests/nether_bridge.json`

- Пул 0, rolls `{"min":2,"max":4}`, weights `[5,5,15,5,5,5,5,10,8,5,3,2]`, сумма 73.
  - Запись 0: `"minecraft:diamond"` — 5/73 (6.84932%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:iron_ingot"` — 5/73 (6.84932%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:gold_ingot"` — 15/73 (20.5479%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 3: `"minecraft:golden_sword"` — 5/73 (6.84932%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 4: `"minecraft:golden_chestplate"` — 5/73 (6.84932%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 5: `"minecraft:flint_and_steel"` — 5/73 (6.84932%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 6: `"minecraft:nether_wart"` — 5/73 (6.84932%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 7: `"minecraft:saddle"` — 10/73 (13.6986%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 8: `"minecraft:horsearmorgold"` — 8/73 (10.9589%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 9: `"minecraft:horsearmoriron"` — 5/73 (6.84932%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 10: `"minecraft:horsearmordiamond"` — 3/73 (4.10959%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 11: `"minecraft:obsidian"` — 2/73 (2.73973%) от суммы явно указанных весов, до учёта условий и функций.

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
          "weight": 5
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
          "weight": 15
        },
        {
          "type": "item",
          "name": "minecraft:golden_sword",
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:golden_chestplate",
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:flint_and_steel",
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:nether_wart",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 3,
                "max": 7
              }
            }
          ],
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:saddle",
          "weight": 10
        },
        {
          "type": "item",
          "name": "minecraft:horsearmorgold",
          "weight": 8
        },
        {
          "type": "item",
          "name": "minecraft:horsearmoriron",
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:horsearmordiamond",
          "weight": 3
        },
        {
          "type": "item",
          "name": "minecraft:obsidian",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 2,
                "max": 4
              }
            }
          ],
          "weight": 2
        }
      ]
    }
  ]
}
```

## `Swords_B/loot_tables/chests/pillager_outpost.json`

- Пул 0, rolls `{"min":0,"max":1}`, weights `[null]`; доли не вычислены.
- Пул 1, rolls `{"min":2,"max":3}`, weights `[7,5,5]`, сумма 17.
  - Запись 0: `"minecraft:wheat"` — 7/17 (41.1765%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:potato"` — 5/17 (29.4118%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:carrot"` — 5/17 (29.4118%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 2, rolls `{"min":1,"max":3}`, weights `[1]`, сумма 1.
  - Запись 0: `"minecraft:log2"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 3, rolls `{"min":2,"max":3}`, weights `[7,4,4,3,3,3,3,null]`; доли не вычислены.

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

## `Swords_B/loot_tables/chests/shipwreck.json`

- Пул 0, rolls `1`, weights `[null]`; доли не вычислены.
- Пул 1, rolls `3`, weights `[1,1,1,20,10,5]`, сумма 38.
  - Запись 0: `"minecraft:compass"` — 1/38 (2.63158%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:map"` — 1/38 (2.63158%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:clock"` — 1/38 (2.63158%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 3: `"minecraft:paper"` — 10/19 (52.6316%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 4: `"minecraft:feather"` — 5/19 (26.3158%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 5: `"minecraft:book"` — 5/38 (13.1579%) от суммы явно указанных весов, до учёта условий и функций.

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:map",
          "functions": [
            {
              "function": "exploration_map",
              "destination": "buriedtreasure"
            }
          ]
        }
      ]
    },
    {
      "rolls": 3,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:compass",
          "weight": 1
        },
        {
          "type": "item",
          "name": "minecraft:map",
          "weight": 1
        },
        {
          "type": "item",
          "name": "minecraft:clock",
          "weight": 1
        },
        {
          "type": "item",
          "name": "minecraft:paper",
          "weight": 20,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 10
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:feather",
          "weight": 10,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 5
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:book",
          "weight": 5,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 5
              }
            }
          ]
        }
      ]
    }
  ]
}
```

## `Swords_B/loot_tables/chests/shipwrecksupply.json`

- Пул 0, rolls `{"min":3,"max":10}`, weights `[8,7,7,7,7,6,5,2,2,3,1,3,3,3,3,10]`, сумма 77.
  - Запись 0: `"minecraft:paper"` — 8/77 (10.3896%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:potato"` — 1/11 (9.09091%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:poisonous_potato"` — 1/11 (9.09091%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 3: `"minecraft:carrot"` — 1/11 (9.09091%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 4: `"minecraft:wheat"` — 1/11 (9.09091%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 5: `"minecraft:coal"` — 6/77 (7.79221%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 6: `"minecraft:rotten_flesh"` — 5/77 (6.49351%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 7: `"minecraft:bamboo"` — 2/77 (2.5974%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 8: `"minecraft:pumpkin"` — 2/77 (2.5974%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 9: `"minecraft:gunpowder"` — 3/77 (3.8961%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 10: `"minecraft:tnt"` — 1/77 (1.2987%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 11: `"minecraft:leather_helmet"` — 3/77 (3.8961%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 12: `"minecraft:leather_chestplate"` — 3/77 (3.8961%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 13: `"minecraft:leather_leggings"` — 3/77 (3.8961%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 14: `"minecraft:leather_boots"` — 3/77 (3.8961%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 15: `"minecraft:suspicious_stew"` — 10/77 (12.987%) от суммы явно указанных весов, до учёта условий и функций.

```json
{
  "pools": [
    {
      "rolls": {
        "min": 3,
        "max": 10
      },
      "entries": [
        {
          "type": "item",
          "name": "minecraft:paper",
          "weight": 8,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 12
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:potato",
          "weight": 7,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 2,
                "max": 6
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:poisonous_potato",
          "weight": 7,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 2,
                "max": 6
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:carrot",
          "weight": 7,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 4,
                "max": 8
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:wheat",
          "weight": 7,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 8,
                "max": 21
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:coal",
          "weight": 6,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 2,
                "max": 8
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:rotten_flesh",
          "weight": 5,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 5,
                "max": 24
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:bamboo",
          "weight": 2,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:pumpkin",
          "weight": 2,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:gunpowder",
          "weight": 3,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 5
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:tnt",
          "weight": 1,
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
          "name": "minecraft:leather_helmet",
          "weight": 3,
          "functions": [
            {
              "function": "enchant_randomly"
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:leather_chestplate",
          "weight": 3,
          "functions": [
            {
              "function": "enchant_randomly"
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:leather_leggings",
          "weight": 3,
          "functions": [
            {
              "function": "enchant_randomly"
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:leather_boots",
          "weight": 3,
          "functions": [
            {
              "function": "enchant_randomly"
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:suspicious_stew",
          "weight": 10,
          "functions": [
            {
              "function": "random_aux_value",
              "values": {
                "min": 0,
                "max": 6
              }
            }
          ]
        }
      ]
    }
  ]
}
```

## `Swords_B/loot_tables/chests/shipwrecktreasure.json`

- Пул 0, rolls `{"min":3,"max":6}`, weights `[90,10,40,5,5]`, сумма 150.
  - Запись 0: `"minecraft:iron_ingot"` — 3/5 (60%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:gold_ingot"` — 1/15 (6.66667%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:emerald"` — 4/15 (26.6667%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 3: `"minecraft:diamond"` — 1/30 (3.33333%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 4: `"minecraft:experience_bottle"` — 1/30 (3.33333%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 1, rolls `{"min":2,"max":5}`, weights `[50,10,20]`, сумма 80.
  - Запись 0: `"minecraft:iron_nugget"` — 5/8 (62.5%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:gold_nugget"` — 1/8 (12.5%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:dye"` — 1/4 (25%) от суммы явно указанных весов, до учёта условий и функций.

```json
{
  "pools": [
    {
      "rolls": {
        "min": 3,
        "max": 6
      },
      "entries": [
        {
          "type": "item",
          "name": "minecraft:iron_ingot",
          "weight": 90,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 5
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:gold_ingot",
          "weight": 10,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 5
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:emerald",
          "weight": 40,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 5
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:diamond",
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:experience_bottle",
          "weight": 5
        }
      ]
    },
    {
      "rolls": {
        "min": 2,
        "max": 5
      },
      "entries": [
        {
          "type": "item",
          "name": "minecraft:iron_nugget",
          "weight": 50,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 10
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
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 10
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:dye",
          "weight": 20,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 10
              }
            },
            {
              "function": "set_data",
              "data": 4
            }
          ]
        }
      ]
    }
  ]
}
```

## `Swords_B/loot_tables/chests/simple_dungeon.json`

- Пул 0, rolls `{"min":1,"max":3}`, weights `[20,15,2,15,15,20,10,15,5,10]`, сумма 127.
  - Запись 0: `"minecraft:saddle"` — 20/127 (15.748%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:golden_apple"` — 15/127 (11.811%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:appleEnchanted"` — 2/127 (1.5748%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 3: `"minecraft:record_13"` — 15/127 (11.811%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 4: `"minecraft:record_cat"` — 15/127 (11.811%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 5: `"minecraft:name_tag"` — 20/127 (15.748%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 6: `"minecraft:horsearmorgold"` — 10/127 (7.87402%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 7: `"minecraft:horsearmoriron"` — 15/127 (11.811%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 8: `"minecraft:horsearmordiamond"` — 5/127 (3.93701%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 9: `"minecraft:book"` — 10/127 (7.87402%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 1, rolls `{"min":1,"max":4}`, weights `[10,5,20,20,10,15,15,10,10,10]`, сумма 125.
  - Запись 0: `"minecraft:iron_ingot"` — 2/25 (8%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:gold_ingot"` — 1/25 (4%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:bread"` — 4/25 (16%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 3: `"minecraft:wheat"` — 4/25 (16%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 4: `"minecraft:bucket"` — 2/25 (8%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 5: `"minecraft:redstone"` — 3/25 (12%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 6: `"minecraft:coal"` — 3/25 (12%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 7: `"minecraft:melon_seeds"` — 2/25 (8%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 8: `"minecraft:pumpkin_seeds"` — 2/25 (8%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 9: `"minecraft:beetroot_seeds"` — 2/25 (8%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 2, rolls `3`, weights `[10,10,10,10]`, сумма 40.
  - Запись 0: `"minecraft:bone"` — 1/4 (25%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:gunpowder"` — 1/4 (25%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:rotten_flesh"` — 1/4 (25%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 3: `"minecraft:string"` — 1/4 (25%) от суммы явно указанных весов, до учёта условий и функций.

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
          "name": "minecraft:saddle",
          "weight": 20
        },
        {
          "type": "item",
          "name": "minecraft:golden_apple",
          "weight": 15
        },
        {
          "type": "item",
          "name": "minecraft:appleEnchanted",
          "weight": 2
        },
        {
          "type": "item",
          "name": "minecraft:record_13",
          "weight": 15
        },
        {
          "type": "item",
          "name": "minecraft:record_cat",
          "weight": 15
        },
        {
          "type": "item",
          "name": "minecraft:name_tag",
          "weight": 20
        },
        {
          "type": "item",
          "name": "minecraft:horsearmorgold",
          "weight": 10
        },
        {
          "type": "item",
          "name": "minecraft:horsearmoriron",
          "weight": 15
        },
        {
          "type": "item",
          "name": "minecraft:horsearmordiamond",
          "weight": 5
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
          "weight": 10,
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
          "weight": 5,
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
          "weight": 20
        },
        {
          "type": "item",
          "name": "minecraft:wheat",
          "weight": 20,
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
          "weight": 10
        },
        {
          "type": "item",
          "name": "minecraft:redstone",
          "weight": 15,
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
          "weight": 15,
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
        }
      ]
    }
  ]
}
```

## `Swords_B/loot_tables/chests/spawn_bonus_chest.json`

- Пул 0, rolls `1`, weights `[1,1,3]`, сумма 5.
  - Запись 0: `"effect:coal_sword"` — 1/5 (20%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:stone_axe"` — 1/5 (20%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:wooden_axe"` — 3/5 (60%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 1, rolls `1`, weights `[1,3]`, сумма 4.
  - Запись 0: `"minecraft:stone_pickaxe"` — 1/4 (25%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:wooden_pickaxe"` — 3/4 (75%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 2, rolls `1`, weights `[1]`, сумма 1.
  - Запись 0: `"minecraft:apple"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 3, rolls `1`, weights `[1]`, сумма 1.
  - Запись 0: `"minecraft:bread"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 4, rolls `1`, weights `[1]`, сумма 1.
  - Запись 0: `"minecraft:salmon"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 5, rolls `1`, weights `[1]`, сумма 1.
  - Запись 0: `"minecraft:stick"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 6, rolls `1`, weights `[1]`, сумма 1.
  - Запись 0: `"minecraft:planks"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 7, rolls `1`, weights `[1,1]`, сумма 2.
  - Запись 0: `"minecraft:log2"` — 1/2 (50%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:log2"` — 1/2 (50%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 8, rolls `1`, weights `[1,1,1,1]`, сумма 4.
  - Запись 0: `"minecraft:log"` — 1/4 (25%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:log"` — 1/4 (25%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:log"` — 1/4 (25%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 3: `"minecraft:log"` — 1/4 (25%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 9, rolls `1`, weights `[3,3]`, сумма 6.
  - Запись 0: `"minecraft:potato"` — 1/2 (50%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:carrot"` — 1/2 (50%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 10, rolls `1`, weights `[2,2,2,4,2,2]`, сумма 14.
  - Запись 0: `"minecraft:sapling"` — 1/7 (14.2857%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:sapling"` — 1/7 (14.2857%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:sapling"` — 1/7 (14.2857%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 3: `"minecraft:sapling"` — 2/7 (28.5714%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 4: `"minecraft:sapling"` — 1/7 (14.2857%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 5: `"minecraft:sapling"` — 1/7 (14.2857%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 11, rolls `1`, weights `[3,3,3]`, сумма 9.
  - Запись 0: `"minecraft:melon_seeds"` — 1/3 (33.3333%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:pumpkin_seeds"` — 1/3 (33.3333%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:beetroot_seeds"` — 1/3 (33.3333%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 12, rolls `1`, weights `[3,2]`, сумма 5.
  - Запись 0: `"minecraft:cactus"` — 3/5 (60%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:dye"` — 2/5 (40%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 13, rolls `1`, weights `[2]`, сумма 2.
  - Запись 0: `"minecraft:brown_mushroom"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.

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

## `Swords_B/loot_tables/chests/stronghold_corridor.json`

- Пул 0, rolls `{"min":2,"max":3}`, weights `[50,15,15,50,25,25,75,75,25,25,25,25,25,25,5,5,5,5,5,5,5,6]`, сумма 521.
  - Запись 0: `"minecraft:ender_pearl"` — 50/521 (9.59693%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:emerald"` — 15/521 (2.87908%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:diamond"` — 15/521 (2.87908%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 3: `"minecraft:iron_ingot"` — 50/521 (9.59693%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 4: `"minecraft:gold_ingot"` — 25/521 (4.79846%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 5: `"minecraft:redstone"` — 25/521 (4.79846%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 6: `"minecraft:bread"` — 75/521 (14.3954%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 7: `"minecraft:apple"` — 75/521 (14.3954%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 8: `"minecraft:iron_pickaxe"` — 25/521 (4.79846%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 9: `"minecraft:iron_sword"` — 25/521 (4.79846%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 10: `"minecraft:iron_chestplate"` — 25/521 (4.79846%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 11: `"minecraft:iron_helmet"` — 25/521 (4.79846%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 12: `"minecraft:iron_leggings"` — 25/521 (4.79846%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 13: `"minecraft:iron_boots"` — 25/521 (4.79846%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 14: `"minecraft:golden_apple"` — 5/521 (0.959693%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 15: `"minecraft:saddle"` — 5/521 (0.959693%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 16: `"effect:emerald_sword"` — 5/521 (0.959693%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 17: `"effect:lapis_sword"` — 5/521 (0.959693%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 18: `"minecraft:horsearmoriron"` — 5/521 (0.959693%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 19: `"minecraft:horsearmorgold"` — 5/521 (0.959693%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 20: `"minecraft:horsearmordiamond"` — 5/521 (0.959693%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 21: `"minecraft:book"` — 6/521 (1.15163%) от суммы явно указанных весов, до учёта условий и функций.

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

## `Swords_B/loot_tables/chests/stronghold_crossing.json`

- Пул 0, rolls `{"min":1,"max":4}`, weights `[50,25,25,50,75,75,5,6,75]`, сумма 386.
  - Запись 0: `"minecraft:iron_ingot"` — 25/193 (12.9534%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:gold_ingot"` — 25/386 (6.47668%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:redstone"` — 25/386 (6.47668%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 3: `"minecraft:coal"` — 25/193 (12.9534%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 4: `"minecraft:bread"` — 75/386 (19.4301%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 5: `"minecraft:apple"` — 75/386 (19.4301%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 6: `"minecraft:iron_pickaxe"` — 5/386 (1.29534%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 7: `"minecraft:book"` — 3/193 (1.5544%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 8: `"minecraft:dye"` — 75/386 (19.4301%) от суммы явно указанных весов, до учёта условий и функций.

```json
{
  "pools": [
    {
      "rolls": {
        "min": 1,
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
          "weight": 50
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
        },
        {
          "type": "item",
          "name": "minecraft:dye",
          "weight": 75,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
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

## `Swords_B/loot_tables/chests/stronghold_library.json`

- Пул 0, rolls `{"min":2,"max":10}`, weights `[100,100,5,5,5,60]`, сумма 275.
  - Запись 0: `"minecraft:book"` — 4/11 (36.3636%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:paper"` — 4/11 (36.3636%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:map"` — 1/55 (1.81818%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 3: `"effect:lapis_sword"` — 1/55 (1.81818%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 4: `"minecraft:compass"` — 1/55 (1.81818%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 5: `"minecraft:book"` — 12/55 (21.8182%) от суммы явно указанных весов, до учёта условий и функций.

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

## `Swords_B/loot_tables/chests/underwater_ruin_big.json`

- Пул 0, rolls `{"min":2,"max":8}`, weights `[10,10,1,10]`, сумма 31.
  - Запись 0: `"minecraft:coal"` — 10/31 (32.2581%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:gold_nugget"` — 10/31 (32.2581%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:emerald"` — 1/31 (3.22581%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 3: `"minecraft:wheat"` — 10/31 (32.2581%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 1, rolls `1`, weights `[1,1,5,1,1,5,10]`, сумма 24.
  - Запись 0: `"minecraft:golden_apple"` — 1/24 (4.16667%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"effect:magma_sword"` — 1/24 (4.16667%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:book"` — 5/24 (20.8333%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 3: `"minecraft:leather_chestplate"` — 1/24 (4.16667%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 4: `"minecraft:golden_helmet"` — 1/24 (4.16667%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 5: `"minecraft:fishing_rod"` — 5/24 (20.8333%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 6: `"minecraft:map"` — 5/12 (41.6667%) от суммы явно указанных весов, до учёта условий и функций.

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

## `Swords_B/loot_tables/chests/underwater_ruin_small.json`

- Пул 0, rolls `{"min":2,"max":8}`, weights `[10,2,5,1,10]`, сумма 28.
  - Запись 0: `"minecraft:coal"` — 5/14 (35.7143%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:stone_axe"` — 1/14 (7.14286%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:rotten_flesh"` — 5/28 (17.8571%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 3: `"minecraft:emerald"` — 1/28 (3.57143%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 4: `"minecraft:wheat"` — 5/14 (35.7143%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 1, rolls `1`, weights `[1,1,5,5]`, сумма 12.
  - Запись 0: `"minecraft:leather_chestplate"` — 1/12 (8.33333%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:golden_helmet"` — 1/12 (8.33333%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:fishing_rod"` — 5/12 (41.6667%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 3: `"minecraft:map"` — 5/12 (41.6667%) от суммы явно указанных весов, до учёта условий и функций.

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
          "name": "minecraft:stone_axe",
          "weight": 2
        },
        {
          "type": "item",
          "name": "minecraft:rotten_flesh",
          "weight": 5
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
          "weight": 5,
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

## `Swords_B/loot_tables/chests/village/village_armorer.json`

- Пул 0, rolls `{"min":1,"max":5}`, weights `[2,4,null,null]`; доли не вычислены.

```json
{
  "pools": [
    {
      "rolls": {
        "min": 1,
        "max": 5
      },
      "entries": [
        {
          "type": "item",
          "weight": 2,
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
          "weight": 4,
          "functions": [
            {
              "function": "set_count",
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
          "name": "minecraft:iron_helmet"
        },
        {
          "type": "item",
          "name": "minecraft:emerald"
        }
      ]
    }
  ]
}
```

## `Swords_B/loot_tables/chests/village/village_butcher.json`

- Пул 0, rolls `{"min":1,"max":5}`, weights `[null,6,6,6,6,3]`; доли не вычислены.

```json
{
  "pools": [
    {
      "rolls": {
        "min": 1,
        "max": 5
      },
      "entries": [
        {
          "type": "item",
          "name": "minecraft:emerald"
        },
        {
          "type": "item",
          "weight": 6,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "name": "minecraft:porkchop"
        },
        {
          "type": "item",
          "weight": 6,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "name": "minecraft:wheat"
        },
        {
          "type": "item",
          "weight": 6,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "name": "minecraft:beef"
        },
        {
          "type": "item",
          "weight": 6,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "name": "minecraft:muttonRaw"
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
          "name": "minecraft:coal"
        }
      ]
    }
  ]
}
```

## `Swords_B/loot_tables/chests/village/village_cartographer.json`

- Пул 0, rolls `{"min":1,"max":5}`, weights `[10,15,5,15,5]`, сумма 50.
  - Запись 0: `"minecraft:map"` — 1/5 (20%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:paper"` — 3/10 (30%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:compass"` — 1/10 (10%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 3: `"minecraft:bread"` — 3/10 (30%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 4: `"minecraft:sapling"` — 1/10 (10%) от суммы явно указанных весов, до учёта условий и функций.

```json
{
  "pools": [
    {
      "rolls": {
        "min": 1,
        "max": 5
      },
      "entries": [
        {
          "type": "item",
          "weight": 10,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "name": "minecraft:map"
        },
        {
          "type": "item",
          "weight": 15,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 5
              }
            }
          ],
          "name": "minecraft:paper"
        },
        {
          "type": "item",
          "weight": 5,
          "name": "minecraft:compass"
        },
        {
          "type": "item",
          "weight": 15,
          "functions": [
            {
              "function": "set_count",
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
          "weight": 5,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            },
            {
              "function": "set_data",
              "data": 0
            }
          ],
          "name": "minecraft:sapling"
        }
      ]
    }
  ]
}
```

## `Swords_B/loot_tables/chests/village/village_desert_house.json`

- Пул 0, rolls `{"min":3,"max":8}`, weights `[null,null,10,10,10,null,2,null]`; доли не вычислены.

```json
{
  "pools": [
    {
      "rolls": {
        "min": 3,
        "max": 8
      },
      "entries": [
        {
          "type": "item",
          "name": "minecraft:clay_ball"
        },
        {
          "type": "item",
          "functions": [
            {
              "function": "set_data",
              "data": 2
            }
          ],
          "name": "minecraft:dye"
        },
        {
          "type": "item",
          "weight": 10,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 4
              }
            }
          ],
          "name": "minecraft:cactus"
        },
        {
          "type": "item",
          "weight": 10,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 7
              }
            }
          ],
          "name": "minecraft:wheat"
        },
        {
          "type": "item",
          "weight": 10,
          "functions": [
            {
              "function": "set_count",
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
          "name": "minecraft:book"
        },
        {
          "type": "item",
          "weight": 2,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "name": "minecraft:deadbush"
        },
        {
          "type": "item",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "name": "minecraft:emerald"
        }
      ]
    }
  ]
}
```

## `Swords_B/loot_tables/chests/village/village_fletcher.json`

- Пул 0, rolls `{"min":1.0,"max":5.0}`, weights `[null,2,6,2,6,6]`; доли не вычислены.

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "min": 1.0,
        "max": 5.0
      },
      "entries": [
        {
          "type": "item",
          "name": "minecraft:emerald"
        },
        {
          "type": "item",
          "weight": 2,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1.0,
                "max": 3.0
              }
            }
          ],
          "name": "minecraft:arrow"
        },
        {
          "type": "item",
          "weight": 6,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1.0,
                "max": 3.0
              }
            }
          ],
          "name": "minecraft:feather"
        },
        {
          "type": "item",
          "weight": 2,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1.0,
                "max": 3.0
              }
            }
          ],
          "name": "minecraft:egg"
        },
        {
          "type": "item",
          "weight": 6,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1.0,
                "max": 3.0
              }
            }
          ],
          "name": "minecraft:flint"
        },
        {
          "type": "item",
          "weight": 6,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1.0,
                "max": 3.0
              }
            }
          ],
          "name": "minecraft:stick"
        }
      ]
    }
  ]
}
```

## `Swords_B/loot_tables/chests/village/village_mason.json`

- Пул 0, rolls `{"min":1,"max":5}`, weights `[null,null,2,2,4,null,null,null]`; доли не вычислены.

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "min": 1,
        "max": 5
      },
      "entries": [
        {
          "type": "item",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "name": "minecraft:clay_ball"
        },
        {
          "type": "item",
          "name": "minecraft:flower_pot"
        },
        {
          "type": "item",
          "weight": 2,
          "name": "minecraft:stone"
        },
        {
          "type": "item",
          "weight": 2,
          "name": "minecraft:stonebrick"
        },
        {
          "type": "item",
          "weight": 4,
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
          "functions": [
            {
              "function": "minecraft:set_data",
              "data": 11
            }
          ],
          "name": "minecraft:dye"
        },
        {
          "type": "item",
          "name": "minecraft:smooth_stone"
        },
        {
          "type": "item",
          "name": "minecraft:emerald"
        }
      ]
    }
  ]
}
```

## `Swords_B/loot_tables/chests/village/village_plains_house.json`

- Пул 0, rolls `{"min":3,"max":8}`, weights `[null,2,null,10,10,10,null,null,2,5]`; доли не вычислены.

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
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "name": "minecraft:gold_nugget"
        },
        {
          "type": "item",
          "weight": 2,
          "name": "minecraft:yellow_flower"
        },
        {
          "type": "item",
          "functions": [
            {
              "function": "minecraft:set_data",
              "data": 0
            }
          ],
          "name": "minecraft:red_flower"
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
          "name": "minecraft:apple"
        },
        {
          "type": "item",
          "name": "minecraft:book"
        },
        {
          "type": "item",
          "name": "minecraft:feather"
        },
        {
          "type": "item",
          "weight": 2,
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
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            },
            {
              "function": "minecraft:set_data",
              "data": 0
            }
          ],
          "name": "minecraft:sapling"
        }
      ]
    }
  ]
}
```

## `Swords_B/loot_tables/chests/village/village_savanna_house.json`

- Пул 0, rolls `{"min":3,"max":8}`, weights `[null,5,5,10,10,2,10,null,null,null]`; доли не вычислены.

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
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "name": "minecraft:gold_nugget"
        },
        {
          "type": "item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_data",
              "data": 1
            }
          ],
          "name": "minecraft:tallgrass"
        },
        {
          "type": "item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_data",
              "data": 2
            }
          ],
          "name": "minecraft:double_plant"
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
          "name": "minecraft:wheat_seeds"
        },
        {
          "type": "item",
          "weight": 2,
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
                "max": 2
              }
            },
            {
              "function": "minecraft:set_data",
              "data": 4
            }
          ],
          "name": "minecraft:sapling"
        },
        {
          "type": "item",
          "name": "minecraft:saddle"
        },
        {
          "type": "item",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ],
          "name": "minecraft:torch"
        },
        {
          "type": "item",
          "name": "minecraft:bucket"
        }
      ]
    }
  ]
}
```

## `Swords_B/loot_tables/chests/village/village_shepherd.json`

- Пул 0, rolls `{"min":1,"max":5}`, weights `[6,3,2,2,2,null,null,6]`; доли не вычислены.

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "min": 1,
        "max": 5
      },
      "entries": [
        {
          "type": "item",
          "weight": 6,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 8
              }
            },
            {
              "function": "set_data",
              "data": 0
            }
          ],
          "name": "minecraft:wool"
        },
        {
          "type": "item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            },
            {
              "function": "set_data",
              "data": 15
            }
          ],
          "name": "minecraft:wool"
        },
        {
          "type": "item",
          "weight": 2,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            },
            {
              "function": "set_data",
              "data": 7
            }
          ],
          "name": "minecraft:wool"
        },
        {
          "type": "item",
          "weight": 2,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            },
            {
              "function": "set_data",
              "data": 12
            }
          ],
          "name": "minecraft:wool"
        },
        {
          "type": "item",
          "weight": 2,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            },
            {
              "function": "set_data",
              "data": 8
            }
          ],
          "name": "minecraft:wool"
        },
        {
          "type": "item",
          "name": "minecraft:emerald"
        },
        {
          "type": "item",
          "name": "minecraft:shears"
        },
        {
          "type": "item",
          "weight": 6,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 6
              }
            }
          ],
          "name": "minecraft:wheat"
        }
      ]
    }
  ]
}
```

## `Swords_B/loot_tables/chests/village/village_snowy_house.json`

- Пул 0, rolls `{"min":3,"max":8}`, weights `[null,4,10,10,10,null,null,null,10,4,5]`; доли не вычислены.

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

## `Swords_B/loot_tables/chests/village/village_taiga_house.json`

- Пул 0, rolls `{"min":3,"max":8}`, weights `[null,2,2,10,10,5,null,2,5,null,10]`; доли не вычислены.

```json
{
  "pools": [
    {
      "rolls": {
        "min": 3,
        "max": 8
      },
      "entries": [
        {
          "type": "item",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 5
              }
            }
          ],
          "name": "minecraft:iron_nugget"
        },
        {
          "type": "item",
          "weight": 2,
          "functions": [
            {
              "function": "set_data",
              "data": 2
            }
          ],
          "name": "minecraft:tallgrass"
        },
        {
          "type": "item",
          "weight": 2,
          "functions": [
            {
              "function": "set_data",
              "data": 3
            }
          ],
          "name": "minecraft:double_plant"
        },
        {
          "type": "item",
          "weight": 10,
          "functions": [
            {
              "function": "set_count",
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
              "function": "set_count",
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
          "weight": 5,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 5
              }
            }
          ],
          "name": "minecraft:pumpkin_seeds"
        },
        {
          "type": "item",
          "name": "minecraft:pumpkin_pie"
        },
        {
          "type": "item",
          "weight": 2,
          "functions": [
            {
              "function": "set_count",
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
          "weight": 5,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 5
              }
            },
            {
              "function": "set_data",
              "data": 1
            }
          ],
          "name": "minecraft:sapling"
        },
        {
          "type": "item",
          "functions": [
            {
              "function": "set_data",
              "data": 1
            }
          ],
          "name": "minecraft:sign"
        },
        {
          "type": "item",
          "weight": 10,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 5
              }
            },
            {
              "function": "set_data",
              "data": 1
            }
          ],
          "name": "minecraft:log"
        }
      ]
    }
  ]
}
```

## `Swords_B/loot_tables/chests/village/village_tannery.json`

- Пул 0, rolls `{"min":1,"max":5}`, weights `[null,2,2,2,5,2,null,null]`; доли не вычислены.

```json
{
  "pools": [
    {
      "rolls": {
        "min": 1,
        "max": 5
      },
      "entries": [
        {
          "type": "item",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "name": "minecraft:leather"
        },
        {
          "type": "item",
          "weight": 2,
          "name": "minecraft:leather_chestplate"
        },
        {
          "type": "item",
          "weight": 2,
          "name": "minecraft:leather_boots"
        },
        {
          "type": "item",
          "weight": 2,
          "name": "minecraft:leather_helmet"
        },
        {
          "type": "item",
          "weight": 5,
          "functions": [
            {
              "function": "set_count",
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
          "weight": 2,
          "name": "minecraft:leather_leggings"
        },
        {
          "type": "item",
          "name": "minecraft:saddle"
        },
        {
          "type": "item",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 4
              }
            }
          ],
          "name": "minecraft:emerald"
        }
      ]
    }
  ]
}
```

## `Swords_B/loot_tables/chests/village/village_temple.json`

- Пул 0, rolls `{"min":3,"max":8}`, weights `[2,7,7,null,null,null]`; доли не вычислены.

```json
{
  "pools": [
    {
      "rolls": {
        "min": 3,
        "max": 8
      },
      "entries": [
        {
          "type": "item",
          "weight": 2,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 4
              }
            }
          ],
          "name": "minecraft:redstone"
        },
        {
          "type": "item",
          "weight": 7,
          "functions": [
            {
              "function": "set_count",
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
          "weight": 7,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 4
              }
            }
          ],
          "name": "minecraft:rotten_flesh"
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
            },
            {
              "function": "set_data",
              "data": 4
            }
          ],
          "name": "minecraft:dye"
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
          "name": "minecraft:gold_ingot"
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
        }
      ]
    }
  ]
}
```

## `Swords_B/loot_tables/chests/village/village_toolsmith.json`

- Пул 0, rolls `{"min":3,"max":8}`, weights `[null,5,null,15,5,null,20,5]`; доли не вычислены.

```json
{
  "pools": [
    {
      "rolls": {
        "min": 3,
        "max": 8
      },
      "entries": [
        {
          "type": "item",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "name": "minecraft:diamond"
        },
        {
          "type": "item",
          "weight": 5,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 5
              }
            }
          ],
          "name": "minecraft:iron_ingot"
        },
        {
          "type": "item",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "name": "minecraft:gold_ingot"
        },
        {
          "type": "item",
          "weight": 15,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "name": "minecraft:bread"
        },
        {
          "type": "item",
          "weight": 5,
          "name": "minecraft:iron_pickaxe"
        },
        {
          "type": "item",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "name": "minecraft:coal"
        },
        {
          "type": "item",
          "weight": 20,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "name": "minecraft:stick"
        },
        {
          "type": "item",
          "weight": 5,
          "name": "minecraft:iron_shovel"
        }
      ]
    }
  ]
}
```

## `Swords_B/loot_tables/chests/village/village_weaponsmith.json`

- Пул 0, rolls `{"min":3,"max":8}`, weights `[3,10,5,15,15,5,5,5,5,5,5,5,5,3,null,null,null]`; доли не вычислены.

```json
{
  "pools": [
    {
      "rolls": {
        "min": 3,
        "max": 8
      },
      "entries": [
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
          "name": "minecraft:diamond"
        },
        {
          "type": "item",
          "weight": 10,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 5
              }
            }
          ],
          "name": "minecraft:iron_ingot"
        },
        {
          "type": "item",
          "weight": 5,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "name": "minecraft:gold_ingot"
        },
        {
          "type": "item",
          "weight": 15,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "name": "minecraft:bread"
        },
        {
          "type": "item",
          "weight": 15,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ],
          "name": "minecraft:apple"
        },
        {
          "type": "item",
          "weight": 5,
          "name": "minecraft:iron_pickaxe"
        },
        {
          "type": "item",
          "weight": 5,
          "name": "minecraft:iron_sword"
        },
        {
          "type": "item",
          "weight": 5,
          "name": "minecraft:iron_chestplate"
        },
        {
          "type": "item",
          "weight": 5,
          "name": "minecraft:iron_helmet"
        },
        {
          "type": "item",
          "weight": 5,
          "name": "minecraft:iron_leggings"
        },
        {
          "type": "item",
          "weight": 5,
          "name": "minecraft:iron_boots"
        },
        {
          "type": "item",
          "weight": 5,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 3,
                "max": 7
              }
            }
          ],
          "name": "minecraft:obsidian"
        },
        {
          "type": "item",
          "weight": 5,
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 3,
                "max": 7
              }
            },
            {
              "function": "set_data",
              "data": 0
            }
          ],
          "name": "minecraft:sapling"
        },
        {
          "type": "item",
          "weight": 3,
          "name": "minecraft:saddle"
        },
        {
          "type": "item",
          "name": "minecraft:horsearmoriron"
        },
        {
          "type": "item",
          "name": "minecraft:horsearmorgold"
        },
        {
          "type": "item",
          "name": "minecraft:horsearmordiamond"
        }
      ]
    }
  ]
}
```

## `Swords_B/loot_tables/chests/village_blacksmith.json`

- Пул 0, rolls `{"min":3,"max":8}`, weights `[3,10,5,15,15,5,5,5,5,5,5,5,5,3,1,1,1]`, сумма 94.
  - Запись 0: `"minecraft:diamond"` — 3/94 (3.19149%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:iron_ingot"` — 5/47 (10.6383%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:gold_ingot"` — 5/94 (5.31915%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 3: `"minecraft:bread"` — 15/94 (15.9574%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 4: `"minecraft:apple"` — 15/94 (15.9574%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 5: `"minecraft:iron_pickaxe"` — 5/94 (5.31915%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 6: `"minecraft:iron_sword"` — 5/94 (5.31915%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 7: `"minecraft:iron_chestplate"` — 5/94 (5.31915%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 8: `"minecraft:iron_helmet"` — 5/94 (5.31915%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 9: `"minecraft:iron_leggings"` — 5/94 (5.31915%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 10: `"minecraft:iron_boots"` — 5/94 (5.31915%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 11: `"minecraft:obsidian"` — 5/94 (5.31915%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 12: `"minecraft:sapling"` — 5/94 (5.31915%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 13: `"minecraft:saddle"` — 3/94 (3.19149%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 14: `"minecraft:horsearmoriron"` — 1/94 (1.06383%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 15: `"minecraft:horsearmorgold"` — 1/94 (1.06383%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 16: `"minecraft:horsearmordiamond"` — 1/94 (1.06383%) от суммы явно указанных весов, до учёта условий и функций.

```json
{
  "pools": [
    {
      "rolls": {
        "min": 3,
        "max": 8
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
          "weight": 3
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
          "weight": 15
        },
        {
          "type": "item",
          "name": "minecraft:iron_pickaxe",
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:iron_sword",
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:iron_chestplate",
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:iron_helmet",
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:iron_leggings",
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:iron_boots",
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:obsidian",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 3,
                "max": 7
              }
            }
          ],
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:sapling",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 3,
                "max": 7
              }
            }
          ],
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:saddle",
          "weight": 3
        },
        {
          "type": "item",
          "name": "minecraft:horsearmoriron",
          "weight": 1
        },
        {
          "type": "item",
          "name": "minecraft:horsearmorgold",
          "weight": 1
        },
        {
          "type": "item",
          "name": "minecraft:horsearmordiamond",
          "weight": 1
        }
      ]
    }
  ]
}
```

## `Swords_B/loot_tables/chests/village_two_room_house.json`

- Пул 0, rolls `{"min":6,"max":8}`, weights `[10,10,15,5,5,1]`, сумма 46.
  - Запись 0: `"minecraft:potato"` — 5/23 (21.7391%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:carrot"` — 5/23 (21.7391%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:wheat"` — 15/46 (32.6087%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 3: `"minecraft:wheat_seeds"` — 5/46 (10.8696%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 4: `"minecraft:beetroot"` — 5/46 (10.8696%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 5: `"minecraft:wooden_hoe"` — 1/46 (2.17391%) от суммы явно указанных весов, до учёта условий и функций.

```json
{
  "pools": [
    {
      "rolls": {
        "min": 6,
        "max": 8
      },
      "entries": [
        {
          "type": "item",
          "name": "minecraft:potato",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 5,
                "max": 8
              }
            }
          ],
          "weight": 10
        },
        {
          "type": "item",
          "name": "minecraft:carrot",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 4,
                "max": 8
              }
            }
          ],
          "weight": 10
        },
        {
          "type": "item",
          "name": "minecraft:wheat",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 8,
                "max": 12
              }
            }
          ],
          "weight": 15
        },
        {
          "type": "item",
          "name": "minecraft:wheat_seeds",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 2,
                "max": 4
              }
            }
          ],
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:beetroot",
          "functions": [
            {
              "function": "set_count",
              "count": {
                "min": 5,
                "max": 8
              }
            }
          ],
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:wooden_hoe",
          "functions": [
            {
              "function": "set_count",
              "count": 1
            }
          ],
          "weight": 1
        }
      ]
    }
  ]
}
```

## `Swords_B/loot_tables/chests/woodland_mansion.json`

- Пул 0, rolls `{"min":1,"max":3}`, weights `[100,75,10,75,75,100,50,75,25,25,60]`, сумма 670.
  - Запись 0: `"minecraft:lead"` — 10/67 (14.9254%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:golden_apple"` — 15/134 (11.194%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:appleEnchanted"` — 1/67 (1.49254%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 3: `"minecraft:record_13"` — 15/134 (11.194%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 4: `"minecraft:record_cat"` — 15/134 (11.194%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 5: `"minecraft:name_tag"` — 10/67 (14.9254%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 6: `"minecraft:chainmail_chestplate"` — 5/67 (7.46269%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 7: `"minecraft:diamond_hoe"` — 15/134 (11.194%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 8: `"minecraft:diamond_chestplate"` — 5/134 (3.73134%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 9: `"effect:emerald_sword"` — 5/134 (3.73134%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 10: `"minecraft:book"` — 6/67 (8.95522%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 1, rolls `{"min":1,"max":4}`, weights `[50,25,100,100,50,75,75,50,50,50]`, сумма 625.
  - Запись 0: `"minecraft:iron_ingot"` — 2/25 (8%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:gold_ingot"` — 1/25 (4%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:bread"` — 4/25 (16%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 3: `"minecraft:wheat"` — 4/25 (16%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 4: `"minecraft:bucket"` — 2/25 (8%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 5: `"minecraft:redstone"` — 3/25 (12%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 6: `"minecraft:coal"` — 3/25 (12%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 7: `"minecraft:melon_seeds"` — 2/25 (8%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 8: `"minecraft:pumpkin_seeds"` — 2/25 (8%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 9: `"minecraft:beetroot_seeds"` — 2/25 (8%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 2, rolls `3`, weights `[50,50,50,50]`, сумма 200.
  - Запись 0: `"minecraft:bone"` — 1/4 (25%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:gunpowder"` — 1/4 (25%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:rotten_flesh"` — 1/4 (25%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 3: `"minecraft:string"` — 1/4 (25%) от суммы явно указанных весов, до учёта условий и функций.

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

## `Swords_B/loot_tables/empty.json`


```json
{}
```

## `Swords_B/loot_tables/entities/blaze.json`

- Пул 0, rolls `1`, weights `[1]`, сумма 1.
  - Запись 0: `"minecraft:blaze_rod"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 1, rolls `1`, weights `[1]`, сумма 1.
  - Запись 0: `"effect:blaze_sword"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.

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

## `Swords_B/loot_tables/entities/creeper.json`

- Пул 0, rolls `1`, weights `[1]`, сумма 1.
  - Запись 0: `"minecraft:gunpowder"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 1, rolls `1`, weights `[null,null,null,null,null,null,null,null,null,null,null,null]`; доли не вычислены.
- Пул 2, rolls `1`, weights `[null,null,null,null,null,null,null,null,null,null,null,null]`; доли не вычислены.

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:gunpowder",
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
          "condition": "killed_by_entity",
          "entity_type": "minecraft:skeleton"
        }
      ],
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:record_13"
        },
        {
          "type": "item",
          "name": "minecraft:record_cat"
        },
        {
          "type": "item",
          "name": "minecraft:record_blocks"
        },
        {
          "type": "item",
          "name": "minecraft:record_chirp"
        },
        {
          "type": "item",
          "name": "minecraft:record_far"
        },
        {
          "type": "item",
          "name": "minecraft:record_mall"
        },
        {
          "type": "item",
          "name": "minecraft:record_mellohi"
        },
        {
          "type": "item",
          "name": "minecraft:record_stal"
        },
        {
          "type": "item",
          "name": "minecraft:record_strad"
        },
        {
          "type": "item",
          "name": "minecraft:record_ward"
        },
        {
          "type": "item",
          "name": "minecraft:record_11"
        },
        {
          "type": "item",
          "name": "minecraft:record_wait"
        }
      ]
    },
    {
      "conditions": [
        {
          "condition": "killed_by_entity",
          "entity_type": "minecraft:stray"
        }
      ],
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:record_13"
        },
        {
          "type": "item",
          "name": "minecraft:record_cat"
        },
        {
          "type": "item",
          "name": "minecraft:record_blocks"
        },
        {
          "type": "item",
          "name": "minecraft:record_chirp"
        },
        {
          "type": "item",
          "name": "minecraft:record_far"
        },
        {
          "type": "item",
          "name": "minecraft:record_mall"
        },
        {
          "type": "item",
          "name": "minecraft:record_mellohi"
        },
        {
          "type": "item",
          "name": "minecraft:record_stal"
        },
        {
          "type": "item",
          "name": "minecraft:record_strad"
        },
        {
          "type": "item",
          "name": "minecraft:record_ward"
        },
        {
          "type": "item",
          "name": "minecraft:record_11"
        },
        {
          "type": "item",
          "name": "minecraft:record_wait"
        }
      ]
    }
  ]
}
```

## `Swords_B/loot_tables/entities/elder_guardian.json`

- Пул 0, rolls `1`, weights `[1]`, сумма 1.
  - Запись 0: `"minecraft:prismarine_shard"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 1, rolls `1`, weights `[1]`, сумма 1.
  - Запись 0: `"effect:sponge_sword"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 2, rolls `1`, weights `[3,2,1]`, сумма 6.
  - Запись 0: `"minecraft:fish"` — 1/2 (50%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:prismarine_crystals"` — 1/3 (33.3333%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"empty"` — 1/6 (16.6667%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 3, rolls `1`, weights `[1]`, сумма 1.
  - Запись 0: `"minecraft:sponge"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 4, rolls `1`, weights `[1]`, сумма 1.
  - Запись 0: `"loot_tables/gameplay/fishing/fish"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.

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

## `Swords_B/loot_tables/entities/living_flame.json`

- Пул 0, rolls `1`, weights `[1]`, сумма 1.
  - Запись 0: `"effect:fire_sword"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.

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

## `Swords_B/loot_tables/entities/red_enderman.json`

- Пул 0, rolls `1`, weights `[1]`, сумма 1.
  - Запись 0: `"effect:ender_sword"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.

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

## `Swords_B/loot_tables/entities/shulker.json`

- Пул 0, rolls `1`, weights `[1]`, сумма 1.
  - Запись 0: `"minecraft:shulker_shell"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 1, rolls `1`, weights `[1]`, сумма 1.
  - Запись 0: `"effect:shulker_sword"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.

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

## `Swords_B/loot_tables/entities/slime_king.json`

- Пул 0, rolls `1`, weights `[1]`, сумма 1.
  - Запись 0: `"effect:slime_sword"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.

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
          "chance": 0.04,
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

## `Swords_B/loot_tables/entities/wither_skeleton.json`

- Пул 0, rolls `1`, weights `[1]`, сумма 1.
  - Запись 0: `"minecraft:coal"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 1, rolls `1`, weights `[1]`, сумма 1.
  - Запись 0: `"minecraft:bone"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 2, rolls `1`, weights `[1]`, сумма 1.
  - Запись 0: `"minecraft:skull"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 3, rolls `1`, weights `[1]`, сумма 1.
  - Запись 0: `"effect:wither_skeleton_sword"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.

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

## `Swords_B/loot_tables/gameplay/entities/mooshroom_milking.json`

- Пул 0, rolls `1`, weights `[1]`, сумма 1.
  - Запись 0: `"minecraft:mushroom_stew"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 1, rolls `1`, weights `[1]`, сумма 1.
  - Запись 0: `"minecraft:suspicious_stew"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 2, rolls `1`, weights `[1]`, сумма 1.
  - Запись 0: `"minecraft:suspicious_stew"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 3, rolls `1`, weights `[1]`, сумма 1.
  - Запись 0: `"minecraft:suspicious_stew"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 4, rolls `1`, weights `[1]`, сумма 1.
  - Запись 0: `"minecraft:suspicious_stew"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 5, rolls `1`, weights `[1]`, сумма 1.
  - Запись 0: `"minecraft:suspicious_stew"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 6, rolls `1`, weights `[1]`, сумма 1.
  - Запись 0: `"minecraft:suspicious_stew"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 7, rolls `1`, weights `[1]`, сумма 1.
  - Запись 0: `"minecraft:suspicious_stew"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 8, rolls `1`, weights `[1]`, сумма 1.
  - Запись 0: `"minecraft:suspicious_stew"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 9, rolls `1`, weights `[1]`, сумма 1.
  - Запись 0: `"minecraft:suspicious_stew"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.
- Пул 10, rolls `1`, weights `[1]`, сумма 1.
  - Запись 0: `"minecraft:suspicious_stew"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.

```json
{
  "pools": [
    {
      "conditions": [
        {
          "condition": "has_mark_variant",
          "value": -1
        }
      ],
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:mushroom_stew",
          "weight": 1
        }
      ]
    },
    {
      "conditions": [
        {
          "condition": "has_mark_variant",
          "value": 0
        }
      ],
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:suspicious_stew",
          "weight": 1,
          "functions": [
            {
              "function": "set_data",
              "data": 0
            }
          ]
        }
      ]
    },
    {
      "conditions": [
        {
          "condition": "has_mark_variant",
          "value": 1
        }
      ],
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:suspicious_stew",
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
          "condition": "has_mark_variant",
          "value": 2
        }
      ],
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:suspicious_stew",
          "weight": 1,
          "functions": [
            {
              "function": "set_data",
              "data": 2
            }
          ]
        }
      ]
    },
    {
      "conditions": [
        {
          "condition": "has_mark_variant",
          "value": 3
        }
      ],
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:suspicious_stew",
          "weight": 1,
          "functions": [
            {
              "function": "set_data",
              "data": 3
            }
          ]
        }
      ]
    },
    {
      "conditions": [
        {
          "condition": "has_mark_variant",
          "value": 4
        }
      ],
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:suspicious_stew",
          "weight": 1,
          "functions": [
            {
              "function": "set_data",
              "data": 4
            }
          ]
        }
      ]
    },
    {
      "conditions": [
        {
          "condition": "has_mark_variant",
          "value": 5
        }
      ],
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:suspicious_stew",
          "weight": 1,
          "functions": [
            {
              "function": "set_data",
              "data": 5
            }
          ]
        }
      ]
    },
    {
      "conditions": [
        {
          "condition": "has_mark_variant",
          "value": 6
        }
      ],
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:suspicious_stew",
          "weight": 1,
          "functions": [
            {
              "function": "set_data",
              "data": 6
            }
          ]
        }
      ]
    },
    {
      "conditions": [
        {
          "condition": "has_mark_variant",
          "value": 7
        }
      ],
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:suspicious_stew",
          "weight": 1,
          "functions": [
            {
              "function": "set_data",
              "data": 7
            }
          ]
        }
      ]
    },
    {
      "conditions": [
        {
          "condition": "has_mark_variant",
          "value": 8
        }
      ],
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:suspicious_stew",
          "weight": 1,
          "functions": [
            {
              "function": "set_data",
              "data": 8
            }
          ]
        }
      ]
    },
    {
      "conditions": [
        {
          "condition": "has_mark_variant",
          "value": 9
        }
      ],
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:suspicious_stew",
          "weight": 1,
          "functions": [
            {
              "function": "set_data",
              "data": 9
            }
          ]
        }
      ]
    }
  ]
}
```

## `Swords_B/loot_tables/gameplay/fishing.json`

- Пул 0, rolls `1`, weights `[10,5,85]`, сумма 100.
  - Запись 0: `"loot_tables/gameplay/fishing/junk.json"` — 1/10 (10%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"loot_tables/gameplay/fishing/treasure.json"` — 1/20 (5%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"loot_tables/gameplay/fishing/fish.json"` — 17/20 (85%) от суммы явно указанных весов, до учёта условий и функций.

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "loot_table",
          "name": "loot_tables/gameplay/fishing/junk.json",
          "weight": 10,
          "quality": -2
        },
        {
          "type": "loot_table",
          "name": "loot_tables/gameplay/fishing/treasure.json",
          "weight": 5,
          "quality": 2
        },
        {
          "type": "loot_table",
          "name": "loot_tables/gameplay/fishing/fish.json",
          "weight": 85,
          "quality": -1
        }
      ]
    }
  ]
}
```

## `Swords_B/loot_tables/gameplay/fishing/fish.json`

- Пул 0, rolls `1`, weights `[60,25,2,13]`, сумма 100.
  - Запись 0: `"minecraft:fish"` — 3/5 (60%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:salmon"` — 1/4 (25%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:clownfish"` — 1/50 (2%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 3: `"minecraft:pufferfish"` — 13/100 (13%) от суммы явно указанных весов, до учёта условий и функций.

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:fish",
          "weight": 60
        },
        {
          "type": "item",
          "name": "minecraft:salmon",
          "weight": 25
        },
        {
          "type": "item",
          "name": "minecraft:clownfish",
          "weight": 2
        },
        {
          "type": "item",
          "name": "minecraft:pufferfish",
          "weight": 13
        }
      ]
    }
  ]
}
```

## `Swords_B/loot_tables/gameplay/fishing/jungle_fish.json`

- Пул 0, rolls `1`, weights `[60,40]`, сумма 100.
  - Запись 0: `"minecraft:fish"` — 3/5 (60%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:salmon"` — 2/5 (40%) от суммы явно указанных весов, до учёта условий и функций.

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:fish",
          "weight": 60
        },
        {
          "type": "item",
          "name": "minecraft:salmon",
          "weight": 40
        }
      ]
    }
  ]
}
```

## `Swords_B/loot_tables/gameplay/fishing/jungle_junk.json`

- Пул 0, rolls `1`, weights `[10,10,10,10,5,2,10,5,1,10,10,10,10]`, сумма 103.
  - Запись 0: `"minecraft:leather_boots"` — 10/103 (9.70874%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:leather"` — 10/103 (9.70874%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:bone"` — 10/103 (9.70874%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 3: `"minecraft:potion"` — 10/103 (9.70874%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 4: `"minecraft:string"` — 5/103 (4.85437%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 5: `"minecraft:fishing_rod"` — 2/103 (1.94175%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 6: `"minecraft:bowl"` — 10/103 (9.70874%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 7: `"minecraft:stick"` — 5/103 (4.85437%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 8: `"minecraft:dye"` — 1/103 (0.970874%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 9: `"minecraft:dye"` — 10/103 (9.70874%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 10: `"minecraft:tripwire_hook"` — 10/103 (9.70874%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 11: `"minecraft:rotten_flesh"` — 10/103 (9.70874%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 12: `"minecraft:bamboo"` — 10/103 (9.70874%) от суммы явно указанных весов, до учёта условий и функций.

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:leather_boots",
          "weight": 10,
          "functions": [
            {
              "function": "set_damage",
              "damage": {
                "min": 0,
                "max": 0.9
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:leather",
          "weight": 10
        },
        {
          "type": "item",
          "name": "minecraft:bone",
          "weight": 10
        },
        {
          "type": "item",
          "name": "minecraft:potion",
          "weight": 10
        },
        {
          "type": "item",
          "name": "minecraft:string",
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:fishing_rod",
          "weight": 2,
          "functions": [
            {
              "function": "set_damage",
              "damage": {
                "min": 0,
                "max": 0.9
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:bowl",
          "weight": 10
        },
        {
          "type": "item",
          "name": "minecraft:stick",
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:dye",
          "weight": 1,
          "functions": [
            {
              "function": "set_data",
              "data": 0
            },
            {
              "function": "set_count",
              "count": 10
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:dye",
          "weight": 10,
          "functions": [
            {
              "function": "set_data",
              "data": 3
            },
            {
              "function": "set_count",
              "count": 1
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:tripwire_hook",
          "weight": 10
        },
        {
          "type": "item",
          "name": "minecraft:rotten_flesh",
          "weight": 10
        },
        {
          "type": "item",
          "name": "minecraft:bamboo",
          "weight": 10
        }
      ]
    }
  ]
}
```

## `Swords_B/loot_tables/gameplay/fishing/junk.json`

- Пул 0, rolls `1`, weights `[10,10,10,10,5,2,10,5,1,10,10]`, сумма 83.
  - Запись 0: `"minecraft:leather_boots"` — 10/83 (12.0482%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:leather"` — 10/83 (12.0482%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:bone"` — 10/83 (12.0482%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 3: `"minecraft:potion"` — 10/83 (12.0482%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 4: `"minecraft:string"` — 5/83 (6.0241%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 5: `"minecraft:fishing_rod"` — 2/83 (2.40964%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 6: `"minecraft:bowl"` — 10/83 (12.0482%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 7: `"minecraft:stick"` — 5/83 (6.0241%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 8: `"minecraft:dye"` — 1/83 (1.20482%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 9: `"minecraft:tripwire_hook"` — 10/83 (12.0482%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 10: `"minecraft:rotten_flesh"` — 10/83 (12.0482%) от суммы явно указанных весов, до учёта условий и функций.

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:leather_boots",
          "weight": 10,
          "functions": [
            {
              "function": "set_damage",
              "damage": {
                "min": 0,
                "max": 0.9
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:leather",
          "weight": 10
        },
        {
          "type": "item",
          "name": "minecraft:bone",
          "weight": 10
        },
        {
          "type": "item",
          "name": "minecraft:potion",
          "weight": 10
        },
        {
          "type": "item",
          "name": "minecraft:string",
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:fishing_rod",
          "weight": 2,
          "functions": [
            {
              "function": "set_damage",
              "damage": {
                "min": 0,
                "max": 0.9
              }
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:bowl",
          "weight": 10
        },
        {
          "type": "item",
          "name": "minecraft:stick",
          "weight": 5
        },
        {
          "type": "item",
          "name": "minecraft:dye",
          "weight": 1,
          "functions": [
            {
              "function": "set_data",
              "data": 0
            },
            {
              "function": "set_count",
              "count": 10
            }
          ]
        },
        {
          "type": "item",
          "name": "minecraft:tripwire_hook",
          "weight": 10
        },
        {
          "type": "item",
          "name": "minecraft:rotten_flesh",
          "weight": 10
        }
      ]
    }
  ]
}
```

## `Swords_B/loot_tables/gameplay/fishing/treasure.json`

- Пул 0, rolls `1`, weights `[5,5,5,5,5,5,5,6]`, сумма 41.
  - Запись 0: `"minecraft:nautilus_shell"` — 5/41 (12.1951%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"minecraft:waterlily"` — 5/41 (12.1951%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"minecraft:name_tag"` — 5/41 (12.1951%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 3: `"minecraft:saddle"` — 5/41 (12.1951%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 4: `"effect:jungle_sword"` — 5/41 (12.1951%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 5: `"minecraft:bow"` — 5/41 (12.1951%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 6: `"minecraft:fishing_rod"` — 5/41 (12.1951%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 7: `"minecraft:book"` — 6/41 (14.6341%) от суммы явно указанных весов, до учёта условий и функций.

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

## `Swords_B/loot_tables/gameplay/jungle_fishing.json`

- Пул 0, rolls `1`, weights `[10,5,85]`, сумма 100.
  - Запись 0: `"loot_tables/gameplay/fishing/jungle_junk.json"` — 1/10 (10%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 1: `"loot_tables/gameplay/fishing/treasure.json"` — 1/20 (5%) от суммы явно указанных весов, до учёта условий и функций.
  - Запись 2: `"loot_tables/gameplay/fishing/jungle_fish.json"` — 17/20 (85%) от суммы явно указанных весов, до учёта условий и функций.

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "loot_table",
          "name": "loot_tables/gameplay/fishing/jungle_junk.json",
          "weight": 10,
          "quality": -2
        },
        {
          "type": "loot_table",
          "name": "loot_tables/gameplay/fishing/treasure.json",
          "weight": 5,
          "quality": 2
        },
        {
          "type": "loot_table",
          "name": "loot_tables/gameplay/fishing/jungle_fish.json",
          "weight": 85,
          "quality": -1
        }
      ]
    }
  ]
}
```

## `Swords_B/loot_tables/pumpkin_sword.json`

- Пул 0, rolls `1`, weights `[1]`, сумма 1.
  - Запись 0: `"effect:cursed_pumpkin_sword"` — 1/1 (100%) от суммы явно указанных весов, до учёта условий и функций.

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

## `Swords_B/recipes/bedrock_stick.json`

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
      "identifier": "effect:bedrock_stick"
    },
    "tags": [
      "crafting_table"
    ],
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

## `Swords_B/recipes/bedrock_sword.json`

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
      "identifier": "effect:bedrock_sword"
    },
    "tags": [
      "crafting_table"
    ],
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

## `Swords_B/recipes/cactus_sword.json`

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
      "identifier": "effect:cactus_sword"
    },
    "tags": [
      "crafting_table"
    ],
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

## `Swords_B/recipes/clock_sword.json`

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
      "identifier": "effect:clock_sword"
    },
    "tags": [
      "crafting_table"
    ],
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

## `Swords_B/recipes/coal_sword.json`

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
      "identifier": "effect:coal_sword"
    },
    "tags": [
      "crafting_table"
    ],
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

## `Swords_B/recipes/fire_sword.json`

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
      "identifier": "effect:fire_sword"
    },
    "tags": [
      "crafting_table"
    ],
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

## `Swords_B/recipes/glowstone_sword.json`

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
      "identifier": "effect:glowstone_sword"
    },
    "tags": [
      "crafting_table"
    ],
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

## `Swords_B/recipes/nether_star_sword.json`

```json
{
  "format_version": "1.12",
  "minecraft:recipe_shapeless": {
    "description": {
      "identifier": "effect:nether_star_sword"
    },
    "tags": [
      "crafting_table"
    ],
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

## `Swords_B/recipes/quartz_diamond_block.json`

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
      "identifier": "effect99:quartz_diamond_block"
    },
    "tags": [
      "crafting_table"
    ],
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

## `Swords_B/recipes/quartz_diamond_stick.json`

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
      "identifier": "effect:quartz_diamond_stick"
    },
    "tags": [
      "crafting_table"
    ],
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

## `Swords_B/recipes/quartz_diamond_sword.json`

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
      "identifier": "effect:quartz_sword"
    },
    "tags": [
      "crafting_table"
    ],
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

## `Swords_B/recipes/silver_ingot.json`

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

## `Swords_B/recipes/silver_sword.json`

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
      "identifier": "effect:silver_sword"
    },
    "tags": [
      "crafting_table"
    ],
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

## `Swords_B/recipes/wet_sponge_sword.json`

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

## `Swords_B/spawn_rules/alpha_wolf.json`

```json
{
  "format_version": "1.8.0",
  "minecraft:spawn_rules": {
    "description": {
      "identifier": "entity:alpha_wolf",
      "population_control": "monster"
    },
    "conditions": [
      {
        "minecraft:spawns_on_surface": {},
        "minecraft:spawns_on_block_filter": "minecraft:grass",
        "minecraft:brightness_filter": {
          "min": 0,
          "max": 7,
          "adjust_for_weather": true
        },
        "minecraft:difficulty_filter": {
          "min": "easy",
          "max": "hard"
        },
        "minecraft:weight": {
          "default": 10
        },
        "minecraft:herd": {
          "min_size": 1,
          "max_size": 1
        },
        "minecraft:biome_filter": {
          "all_of": [
            {
              "test": "has_biome_tag",
              "operator": "==",
              "value": "taiga"
            },
            {
              "test": "has_biome_tag",
              "operator": "!=",
              "value": "mega"
            }
          ]
        }
      }
    ]
  }
}
```

## `Swords_B/spawn_rules/ghost.json`

```json
{
  "format_version": "1.8.0",
  "minecraft:spawn_rules": {
    "description": {
      "identifier": "entity:ghost",
      "population_control": "monster"
    },
    "conditions": [
      {
        "minecraft:spawns_underground": {},
        "minecraft:spawns_on_block_filter": "minecraft:stone",
        "minecraft:brightness_filter": {
          "min": 0,
          "max": 7,
          "adjust_for_weather": true
        },
        "minecraft:spawn_event": {
          "event": "ghost_wailing"
        },
        "minecraft:difficulty_filter": {
          "min": "easy",
          "max": "hard"
        },
        "minecraft:weight": {
          "default": 100
        },
        "minecraft:herd": {
          "min_size": 1,
          "max_size": 2
        },
        "minecraft:biome_filter": {
          "test": "has_biome_tag",
          "operator": "==",
          "value": "monster"
        }
      },
      {
        "minecraft:spawns_on_surface": {},
        "minecraft:spawns_on_block_filter": "minecraft:grass",
        "minecraft:brightness_filter": {
          "min": 0,
          "max": 7,
          "adjust_for_weather": true
        },
        "minecraft:difficulty_filter": {
          "min": "easy",
          "max": "hard"
        },
        "minecraft:weight": {
          "default": 50
        },
        "minecraft:density_limit": {
          "surface": 3
        },
        "minecraft:biome_filter": {
          "test": "has_biome_tag",
          "operator": "==",
          "value": "monster"
        }
      }
    ]
  }
}
```

## `Swords_B/spawn_rules/living_flame.json`

```json
{
  "format_version": "1.8.0",
  "minecraft:spawn_rules": {
    "description": {
      "identifier": "entity:living_flame",
      "population_control": "monster"
    },
    "conditions": [
      {
        "minecraft:spawns_underground": {},
        "minecraft:difficulty_filter": {
          "min": "easy",
          "max": "hard"
        },
        "minecraft:weight": {
          "default": 20
        },
        "minecraft:herd": {
          "min_size": 1,
          "max_size": 4
        },
        "minecraft:biome_filter": {
          "test": "has_biome_tag",
          "operator": "==",
          "value": "nether"
        }
      }
    ]
  }
}
```

## `Swords_B/spawn_rules/slime_king.json`

```json
{
  "format_version": "1.8.0",
  "minecraft:spawn_rules": {
    "description": {
      "identifier": "entity:slime_king",
      "population_control": "monster"
    },
    "conditions": [
      {
        "minecraft:spawns_on_surface": {},
        "minecraft:difficulty_filter": {
          "min": "easy",
          "max": "hard"
        },
        "minecraft:weight": {
          "default": 10
        },
        "minecraft:biome_filter": {
          "test": "has_biome_tag",
          "operator": "==",
          "value": "swamp"
        }
      }
    ]
  }
}
```

