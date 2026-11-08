# Блоки, рецепты, генерация, торговля и таблицы добычи — архив 1.6

Структурная выписка JSON файлов каталогов loot_tables, blocks, recipes, spawn_rules, features, feature_rules и trading behavior pack. Числа, условия, функции, веса, число бросков и порядок массивов приводятся как в JSON5. Это не ручное доказательство того, что файл загружен/вызывается, и не включает полный анализ структур и исполнения в игре.

Для loot приводятся **сырые относительные доли** по явно указанным целым weight только если у всех записей пула они есть и сумма > 0. Число бросков, условия пула/записи, типы записей, функции, удача и семантика движка могут изменить результат: доли не являются вероятностью получить предмет. При пропущенном весе доля не вычисляется. Все данные самого пула приведены целиком.

## `Sword_B/recipes/Sword_of_Time.json`

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
      "identifier": "effect:Sword_of_Time"
    },
    "tags": [
      "crafting_table"
    ],
    "pattern": [
      "#SS",
      "SBS",
      "NS#"
    ],
    "key": {
      "N": {
        "item": "minecraft:golden_sword"
      },
      "S": {
        "item": "minecraft:gold_block"
      },
      "B": {
        "item": "minecraft:clock"
      }
    },
    "result": {
      "item": "effect:Sword_of_Time"
    }
  }
}
```

## `Sword_B/recipes/blaze_sword.json`

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
      "identifier": "effect:blaze_sword"
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
        "item": "minecraft:blaze_rod"
      },
      "F": {
        "item": "minecraft:blaze_powder"
      }
    },
    "result": {
      "item": "effect:blaze_sword"
    }
  }
}
```

## `Sword_B/recipes/bone_sword.json`

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
      "identifier": "effect:bone_sword"
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
        "item": "minecraft:bone"
      },
      "F": {
        "item": "minecraft:bone_block"
      }
    },
    "result": {
      "item": "effect:bone_sword"
    }
  }
}
```

## `Sword_B/recipes/cactus_sword.json`

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

## `Sword_B/recipes/coal_sword.json`

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

## `Sword_B/recipes/creeper_sword.json`

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
      "identifier": "effect:creeper_sword"
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
        "item": "minecraft:skull",
        "data": 4
      }
    },
    "result": {
      "item": "effect:creeper_sword"
    }
  }
}
```

## `Sword_B/recipes/emerald sword.json`

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
      "identifier": "effect:emerald_sword"
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
        "item": "minecraft:emerald_block"
      }
    },
    "result": {
      "item": "effect:emerald_sword"
    }
  }
}
```

## `Sword_B/recipes/ender_sword.json`

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
      "identifier": "effect:ender_sword"
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
        "item": "minecraft:ender_pearl"
      },
      "F": {
        "item": "minecraft:ender_eye"
      }
    },
    "result": {
      "item": "effect:ender_sword"
    }
  }
}
```

## `Sword_B/recipes/fire_sword.json`

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
      "#SM",
      "SBS",
      "NS#"
    ],
    "key": {
      "N": {
        "item": "minecraft:blaze_rod"
      },
      "S": {
        "item": "minecraft:blaze_powder"
      },
      "B": {
        "item": "minecraft:iron_sword"
      },
      "M": {
        "item": "minecraft:magma_cream"
      }
    },
    "result": {
      "item": "effect:fire_sword"
    }
  }
}
```

## `Sword_B/recipes/glowstone_sword.json`

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
      "020",
      "020",
      "010"
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

## `Sword_B/recipes/grass_sword.json`

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
      "identifier": "effect:grass_sword"
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
        "item": "minecraft:grass"
      }
    },
    "result": {
      "item": "effect:grass_sword"
    }
  }
}
```

## `Sword_B/recipes/ice_sword.json`

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
      "identifier": "effect:ice_sword"
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
        "item": "minecraft:blue_ice"
      }
    },
    "result": {
      "item": "effect:ice_sword"
    }
  }
}
```

## `Sword_B/recipes/jungle_sword.json`

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
      "identifier": "effect:jungle_sword"
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
        "item": "minecraft:sapling",
        "data": 3
      },
      "F": {
        "item": "minecraft:leaves",
        "data": 3
      }
    },
    "result": {
      "item": "effect:jungle_sword"
    }
  }
}
```

## `Sword_B/recipes/lapis_sword.json`

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
      "identifier": "effect:lapis_sword"
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
        "item": "minecraft:lapis_block"
      }
    },
    "result": {
      "item": "effect:lapis_sword"
    }
  }
}
```

## `Sword_B/recipes/lightning_sword.json`

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
      "identifier": "effect:lightning_sword"
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
        "item": "minecraft:netherstar"
      },
      "F": {
        "item": "minecraft:gold_block"
      }
    },
    "result": {
      "item": "effect:lightning_sword"
    }
  }
}
```

## `Sword_B/recipes/magma_sword.json`

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
      "identifier": "effect:magma_sword"
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
        "item": "minecraft:blaze_rod"
      },
      "F": {
        "item": "minecraft:magma"
      }
    },
    "result": {
      "item": "effect:magma_sword"
    }
  }
}
```

## `Sword_B/recipes/obsidian_sword.json`

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
      "identifier": "effect:obsidian_sword"
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
        "item": "minecraft:blaze_rod"
      },
      "F": {
        "item": "minecraft:obsidian"
      }
    },
    "result": {
      "item": "effect:obsidian_sword"
    }
  }
}
```

## `Sword_B/recipes/quartz_sword.json`

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
      "#",
      "#",
      "0"
    ],
    "key": {
      "#": {
        "item": "minecraft:quartz_block",
        "data": 0
      },
      "0": {
        "item": "minecraft:stick",
        "data": 0
      }
    },
    "result": [
      {
        "item": "effect:quartz_sword",
        "data": 0,
        "count": 1
      }
    ]
  }
}
```

## `Sword_B/recipes/sea_sword.json`

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
      "identifier": "effect:sea_sword"
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
        "item": "minecraft:prismarine_shard"
      },
      "F": {
        "item": "minecraft:heart_of_the_sea"
      }
    },
    "result": {
      "item": "effect:sea_sword"
    }
  }
}
```

## `Sword_B/recipes/shulker_sword.json`

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
      "identifier": "effect:shulker_sword"
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
        "item": "minecraft:end_rod"
      },
      "F": {
        "item": "minecraft:shulker_shell"
      }
    },
    "result": {
      "item": "effect:shulker_sword"
    }
  }
}
```

## `Sword_B/recipes/slime_sword.json`

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
      "identifier": "effect:slime_sword"
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
        "item": "minecraft:slime"
      }
    },
    "result": {
      "item": "effect:slime_sword"
    }
  }
}
```

## `Sword_B/recipes/spectral_sword.json`

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
      "identifier": "effect:spectral_sword"
    },
    "tags": [
      "crafting_table"
    ],
    "pattern": [
      "#SS",
      "SBS",
      "NS#"
    ],
    "key": {
      "N": {
        "item": "minecraft:end_rod"
      },
      "S": {
        "item": "minecraft:end_crystal"
      },
      "B": {
        "item": "minecraft:netherstar"
      }
    },
    "result": {
      "item": "effect:spectral_sword"
    }
  }
}
```

## `Sword_B/recipes/spider_sword.json`

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
      "identifier": "effect:spider_sword"
    },
    "tags": [
      "crafting_table"
    ],
    "pattern": [
      "#SS",
      "SBS",
      "NS#"
    ],
    "key": {
      "N": {
        "item": "minecraft:stick"
      },
      "S": {
        "item": "minecraft:web"
      },
      "B": {
        "item": "minecraft:spider_eye"
      }
    },
    "result": {
      "item": "effect:spider_sword"
    }
  }
}
```

## `Sword_B/recipes/sponge_sword.json`

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
      "identifier": "effect:sponge_sword"
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
        "item": "minecraft:sponge"
      }
    },
    "result": {
      "item": "effect:sponge_sword"
    }
  }
}
```

## `Sword_B/recipes/tnt_sword.json`

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
      "identifier": "effect:tnt_sword"
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
        "item": "minecraft:tnt"
      }
    },
    "result": {
      "item": "effect:tnt_sword"
    }
  }
}
```

## `Sword_B/recipes/wither_sword.json`

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
      "identifier": "effect:wither_sword"
    },
    "tags": [
      "crafting_table"
    ],
    "pattern": [
      "#SS",
      "SBS",
      "NS#"
    ],
    "key": {
      "N": {
        "item": "minecraft:blaze_rod"
      },
      "S": {
        "item": "minecraft:skull",
        "data": 1
      },
      "B": {
        "item": "minecraft:netherstar"
      }
    },
    "result": {
      "item": "effect:wither_sword"
    }
  }
}
```

