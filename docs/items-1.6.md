# Исходные карточки предметов — архив 1.6

Эта машинная выписка — точная отправная точка, не законченный семантический аудит. JSON ниже получен из JSON5, комментарии и оформление опущены; при повторяющихся ключах читать исходный файл. События и команды приведены без пересчёта вероятностей: веса являются относительными внутри конкретного `randomize`. Движковые значения по умолчанию и недокументированное поведение не угадываются.

Ссылки указывают путь и номера строк **внутри указанного архива**. Поиск упоминаний текстовый и не является полным графом вызовов: косвенные события, группы компонентов, снаряды, таблицы добычи, функции и модели необходимо проверить вручную.

## effect:sword_of_time

- Название в en_US: `§lTime Sword`
- Определение: `Sword_B/items/Sword of Time.json`
- Урон (`minecraft:damage`): `7`
- Прочность (`minecraft:durability`): `{"max_durability":128}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:sword_of_time",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": true,
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
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "sword_of_time"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:sword_of_time"
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
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 7
  }
}
```

### Прямые текстовые упоминания

- `Sword_B/entities/player.json`: строки 259, 797, 801, 896, 1051, 1054
- `Sword_B/functions/give.mcfunction`: строки 24
- `Sword_B/recipes/Sword_of_Time.json`: строки 5, 25
- `Sword_R/items/Sword_of_Time.json`: строки 5, 9
- `Sword_R/texts/en_US.lang`: строки 16
- `Sword_R/textures/item_texture.json`: строки 41, 42

### Одноимённые группы и события игрока (`Sword_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:sword_of_time": {
      "minecraft:spawn_entity": [
        {
          "min_wait_time": 0,
          "max_wait_time": 0,
          "spawn_entity": "entity:time",
          "num_to_spawn": 1,
          "single_use": true
        }
      ]
    }
  },
  "events": {
    "minecraft:sword_of_time": {
      "add": {
        "component_groups": [
          "minecraft:sword_of_time"
        ]
      }
    }
  }
}
```

## effect:blaze_sword

- Название в en_US: `§l§6Blaze Sword`
- Определение: `Sword_B/items/blaze_sword.json`
- Урон (`minecraft:damage`): `8`
- Прочность (`minecraft:durability`): `{"max_durability":2300}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:blaze_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 2300
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
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
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 8
  }
}
```

### Прямые текстовые упоминания

- `Sword_B/entities/player.json`: строки 226, 497, 501, 876, 911, 914
- `Sword_B/functions/give.mcfunction`: строки 1
- `Sword_B/recipes/blaze_sword.json`: строки 5, 22
- `Sword_R/items/blaze_sword.json`: строки 5, 9
- `Sword_R/texts/en_US.lang`: строки 1
- `Sword_R/textures/item_texture.json`: строки 5, 6

### Рецепты и таблицы добычи с точным ID

`Sword_B/recipes/blaze_sword.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect:blaze_sword"
    },  
    "tags": [ "crafting_table" ],
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


### Одноимённые группы и события игрока (`Sword_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:blaze_sword": {
      "minecraft:spawn_entity": [
        {
          "min_wait_time": 0,
          "max_wait_time": 0,
          "spawn_entity": "entity:blaze",
          "num_to_spawn": 1,
          "single_use": true
        }
      ]
    }
  },
  "events": {
    "minecraft:blaze_sword": {
      "add": {
        "component_groups": [
          "minecraft:blaze_sword"
        ]
      }
    }
  }
}
```

## effect:bone_sword

- Название в en_US: `§lBone Sword`
- Определение: `Sword_B/items/bone_sword.json`
- Урон (`minecraft:damage`): `7`
- Прочность (`minecraft:durability`): `{"max_durability":820}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:bone_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 820
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
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
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 7
  }
}
```

### Прямые текстовые упоминания

- `Sword_B/entities/player.json`: строки 314, 842, 846, 899, 1072, 1075
- `Sword_B/functions/give.mcfunction`: строки 2
- `Sword_B/recipes/bone_sword.json`: строки 5, 22
- `Sword_R/items/bone_sword.json`: строки 5, 9
- `Sword_R/texts/en_US.lang`: строки 25
- `Sword_R/textures/item_texture.json`: строки 77, 78

### Рецепты и таблицы добычи с точным ID

`Sword_B/recipes/bone_sword.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect:bone_sword"
    },  
    "tags": [ "crafting_table" ],
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


### Одноимённые группы и события игрока (`Sword_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:bone_sword": {
      "minecraft:spawn_entity": [
        {
          "min_wait_time": 0,
          "max_wait_time": 0,
          "spawn_entity": "entity:bone",
          "num_to_spawn": 1,
          "single_use": true
        }
      ]
    }
  },
  "events": {
    "minecraft:bone_sword": {
      "add": {
        "component_groups": [
          "minecraft:bone_sword"
        ]
      }
    }
  }
}
```

## effect:cactus_sword

- Название в en_US: `§l§2Cactus Sword`
- Определение: `Sword_B/items/cactus_sword.json`
- Урон (`minecraft:damage`): `6`
- Прочность (`minecraft:durability`): `{"max_durability":125}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:cactus_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 125
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
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
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 6
  }
}
```

### Прямые текстовые упоминания

- `Sword_B/entities/player.json`: строки 215, 512, 516, 877, 918, 921
- `Sword_B/functions/give.mcfunction`: строки 3
- `Sword_B/recipes/cactus_sword.json`: строки 5, 22
- `Sword_R/items/cactus_sword.json`: строки 5, 9
- `Sword_R/texts/en_US.lang`: строки 6
- `Sword_R/textures/item_texture.json`: строки 20, 21

### Рецепты и таблицы добычи с точным ID

`Sword_B/recipes/cactus_sword.json`:

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


### Одноимённые группы и события игрока (`Sword_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:cactus_sword": {
      "minecraft:spawn_entity": [
        {
          "min_wait_time": 0,
          "max_wait_time": 0,
          "spawn_entity": "entity:cactus",
          "num_to_spawn": 1,
          "single_use": true
        }
      ]
    }
  },
  "events": {
    "minecraft:cactus_sword": {
      "add": {
        "component_groups": [
          "minecraft:cactus_sword"
        ]
      }
    }
  }
}
```

## effect:coal_sword

- Название в en_US: `§l§0Coal Sword`
- Определение: `Sword_B/items/coal_sword.json`
- Урон (`minecraft:damage`): `6`
- Прочность (`minecraft:durability`): `{"max_durability":121}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:coal_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 121
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "coal_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:coal_sword"
          ],
          "repair_amount": 121
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
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 6
  }
}
```

### Прямые текстовые упоминания

- `Sword_B/entities/player.json`: строки 204, 527, 531, 878, 925, 928
- `Sword_B/functions/give.mcfunction`: строки 4
- `Sword_B/recipes/coal_sword.json`: строки 5, 22
- `Sword_R/items/coal_sword.json`: строки 5, 9
- `Sword_R/texts/en_US.lang`: строки 2
- `Sword_R/textures/item_texture.json`: строки 11, 12

### Рецепты и таблицы добычи с точным ID

`Sword_B/recipes/coal_sword.json`:

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


### Одноимённые группы и события игрока (`Sword_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:coal_sword": {
      "minecraft:spawn_entity": [
        {
          "min_wait_time": 0,
          "max_wait_time": 0,
          "spawn_entity": "entity:coal",
          "num_to_spawn": 1,
          "single_use": true
        }
      ]
    }
  },
  "events": {
    "minecraft:coal_sword": {
      "add": {
        "component_groups": [
          "minecraft:coal_sword"
        ]
      }
    }
  }
}
```

## effect:creeper_sword

- Название в en_US: `§l§aCreeper§f Sword`
- Определение: `Sword_B/items/creeper_sword.json`
- Урон (`minecraft:damage`): `8`
- Прочность (`minecraft:durability`): `{"max_durability":1500}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:creeper_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 1500
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
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
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 8
  }
}
```

### Прямые текстовые упоминания

- `Sword_B/entities/player.json`: строки 193, 542, 546, 879, 932, 935
- `Sword_B/functions/give.mcfunction`: строки 5
- `Sword_B/recipes/creeper_sword.json`: строки 5, 23
- `Sword_R/items/creeper_sword.json`: строки 5, 9
- `Sword_R/texts/en_US.lang`: строки 17
- `Sword_R/textures/item_texture.json`: строки 44, 45

### Рецепты и таблицы добычи с точным ID

`Sword_B/recipes/creeper_sword.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect:creeper_sword"
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


### Одноимённые группы и события игрока (`Sword_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:creeper_sword": {
      "minecraft:spawn_entity": [
        {
          "min_wait_time": 0,
          "max_wait_time": 0,
          "spawn_entity": "entity:creeper",
          "num_to_spawn": 1,
          "single_use": true
        }
      ]
    }
  },
  "events": {
    "minecraft:creeper_sword": {
      "add": {
        "component_groups": [
          "minecraft:creeper_sword"
        ]
      }
    }
  }
}
```

## effect:emerald_sword

- Название в en_US: `§l§aEmerald Sword`
- Определение: `Sword_B/items/emerald_sword.json`
- Урон (`minecraft:damage`): `7`
- Прочность (`minecraft:durability`): `{"max_durability":2300}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:emerald_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 2300
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
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
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 7
  }
}
```

### Прямые текстовые упоминания

- `Sword_B/entities/player.json`: строки 182, 557, 561, 880, 939, 942
- `Sword_B/functions/give.mcfunction`: строки 6
- `Sword_B/recipes/emerald sword.json`: строки 5, 22
- `Sword_R/items/emerald_sword.json`: строки 5, 9
- `Sword_R/texts/en_US.lang`: строки 8
- `Sword_R/textures/item_texture.json`: строки 26, 27

### Рецепты и таблицы добычи с точным ID

`Sword_B/recipes/emerald sword.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect:emerald_sword"
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
        "item": "minecraft:emerald_block"
      }
    },
    "result": {
      "item": "effect:emerald_sword"
    }
  }
}
```


### Одноимённые группы и события игрока (`Sword_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:emerald_sword": {
      "minecraft:spawn_entity": [
        {
          "min_wait_time": 0,
          "max_wait_time": 0,
          "spawn_entity": "entity:emerald",
          "num_to_spawn": 1,
          "single_use": true
        }
      ]
    }
  },
  "events": {
    "minecraft:emerald_sword": {
      "add": {
        "component_groups": [
          "minecraft:emerald_sword"
        ]
      }
    }
  }
}
```

## effect:ender_sword

- Название в en_US: `§l§5Ender Sword`
- Определение: `Sword_B/items/ender_sword.json`
- Урон (`minecraft:damage`): `9`
- Прочность (`minecraft:durability`): `{"max_durability":1256}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:ender_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": true,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 1256
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
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
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 9
  }
}
```

### Прямые текстовые упоминания

- `Sword_B/entities/player.json`: строки 146, 572, 576, 881, 946, 949
- `Sword_B/functions/give.mcfunction`: строки 7
- `Sword_B/recipes/ender_sword.json`: строки 5, 22
- `Sword_R/items/ender_sword.json`: строки 5, 9
- `Sword_R/texts/en_US.lang`: строки 23
- `Sword_R/textures/item_texture.json`: строки 62, 63

### Рецепты и таблицы добычи с точным ID

`Sword_B/recipes/ender_sword.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect:ender_sword"
    },  
    "tags": [ "crafting_table" ],
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


### Одноимённые группы и события игрока (`Sword_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:ender_sword": {
      "minecraft:spawn_entity": [
        {
          "min_wait_time": 0,
          "max_wait_time": 0,
          "spawn_entity": "entity:ender",
          "num_to_spawn": 1,
          "single_use": true
        }
      ],
      "minecraft:teleport": {
        "random_teleports": true,
        "max_random_teleport_time": 30,
        "random_teleport_cube": [
          32,
          32,
          32
        ],
        "target_distance": 16,
        "target_teleport_chance": 0.05,
        "light_teleport_chance": 0.05
      },
      "minecraft:hurt_on_condition": {
        "damage_conditions": [
          {
            "filters": {
              "test": "in_water_or_rain",
              "operator": "==",
              "value": true
            },
            "cause": "drowning",
            "damage_per_tick": 1
          }
        ]
      }
    }
  },
  "events": {
    "minecraft:ender_sword": {
      "add": {
        "component_groups": [
          "minecraft:ender_sword"
        ]
      }
    }
  }
}
```

## effect:fire_sword

- Название в en_US: `§l§6Fire Sword`
- Определение: `Sword_B/items/fire_sword.json`
- Урон (`minecraft:damage`): `12`
- Прочность (`minecraft:durability`): `{"max_durability":2000}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:fire_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 2000
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
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
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 12
  }
}
```

### Прямые текстовые упоминания

- `Sword_B/entities/player.json`: строки 135, 587, 591, 882, 953, 956
- `Sword_B/functions/give.mcfunction`: строки 8
- `Sword_B/recipes/fire_sword.json`: строки 5, 28
- `Sword_R/items/fire_sword.json`: строки 5, 9
- `Sword_R/texts/en_US.lang`: строки 18
- `Sword_R/textures/item_texture.json`: строки 47, 48

### Рецепты и таблицы добычи с точным ID

`Sword_B/recipes/fire_sword.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect:fire_sword"
    },  
    "tags": [ "crafting_table" ],
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


### Одноимённые группы и события игрока (`Sword_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:fire_sword": {
      "minecraft:spawn_entity": [
        {
          "min_wait_time": 0,
          "max_wait_time": 0,
          "spawn_entity": "entity:fire",
          "num_to_spawn": 1,
          "single_use": true
        }
      ]
    }
  },
  "events": {
    "minecraft:fire_sword": {
      "add": {
        "component_groups": [
          "minecraft:fire_sword"
        ]
      }
    }
  }
}
```

## effect:glowstone_sword

- Название в en_US: `§l§gGlowstone Sword`
- Определение: `Sword_B/items/glowstone_sword.json`
- Урон (`minecraft:damage`): `6`
- Прочность (`minecraft:durability`): `{"max_durability":128}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:glowstone_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": true,
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
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 6
  }
}
```

### Прямые текстовые упоминания

- `Sword_B/entities/player.json`: строки 124, 602, 606, 883, 960, 963
- `Sword_B/functions/give.mcfunction`: строки 9
- `Sword_B/recipes/glowstone_sword.json`: строки 5, 22
- `Sword_R/items/glowstone_sword.json`: строки 5, 9
- `Sword_R/texts/en_US.lang`: строки 15
- `Sword_R/textures/item_texture.json`: строки 38, 39

### Рецепты и таблицы добычи с точным ID

`Sword_B/recipes/glowstone_sword.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect:glowstone_sword"
    },  
    "tags": [ "crafting_table" ],
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


### Одноимённые группы и события игрока (`Sword_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:glowstone_sword": {
      "minecraft:spawn_entity": [
        {
          "min_wait_time": 0,
          "max_wait_time": 0,
          "spawn_entity": "entity:glow",
          "num_to_spawn": 1,
          "single_use": true
        }
      ]
    }
  },
  "events": {
    "minecraft:glowstone_sword": {
      "add": {
        "component_groups": [
          "minecraft:glowstone_sword"
        ]
      }
    }
  }
}
```

## effect:grass_sword

- Название в en_US: `§l§2Grass Sword`
- Определение: `Sword_B/items/grass_sword.json`
- Урон (`minecraft:damage`): `8`
- Прочность (`minecraft:durability`): `{"max_durability":250}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:grass_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 250
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
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
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 8
  }
}
```

### Прямые текстовые упоминания

- `Sword_B/entities/player.json`: строки 113, 617, 621, 884, 967, 970
- `Sword_B/functions/give.mcfunction`: строки 10
- `Sword_B/recipes/grass_sword.json`: строки 5, 22
- `Sword_R/items/grass_sword.json`: строки 5, 9
- `Sword_R/texts/en_US.lang`: строки 12
- `Sword_R/textures/item_texture.json`: строки 71, 72

### Рецепты и таблицы добычи с точным ID

`Sword_B/recipes/grass_sword.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect:grass_sword"
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
        "item": "minecraft:grass"
      }
    },
    "result": {
      "item": "effect:grass_sword"
    }
  }
}
```


### Одноимённые группы и события игрока (`Sword_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:grass_sword": {
      "minecraft:spawn_entity": [
        {
          "min_wait_time": 0,
          "max_wait_time": 0,
          "spawn_entity": "entity:grass",
          "num_to_spawn": 1,
          "single_use": true
        }
      ]
    }
  },
  "events": {
    "minecraft:grass_sword": {
      "add": {
        "component_groups": [
          "minecraft:grass_sword"
        ]
      }
    }
  }
}
```

## effect:ice_sword

- Название в en_US: `§l§bIce Sword`
- Определение: `Sword_B/items/ice_sword.json`
- Урон (`minecraft:damage`): `11`
- Прочность (`minecraft:durability`): `{"max_durability":500}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:ice_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 500
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
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
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 11
  }
}
```

### Прямые текстовые упоминания

- `Sword_B/entities/player.json`: строки 292, 632, 636, 885, 974, 977
- `Sword_B/functions/give.mcfunction`: строки 11
- `Sword_B/recipes/ice_sword.json`: строки 5, 22
- `Sword_R/items/ice_sword.json`: строки 5, 9
- `Sword_R/texts/en_US.lang`: строки 13
- `Sword_R/textures/item_texture.json`: строки 74, 75

### Рецепты и таблицы добычи с точным ID

`Sword_B/recipes/ice_sword.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect:ice_sword"
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
        "item": "minecraft:blue_ice"
      }
    },
    "result": {
      "item": "effect:ice_sword"
    }
  }
}
```


### Одноимённые группы и события игрока (`Sword_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:ice_sword": {
      "minecraft:spawn_entity": [
        {
          "min_wait_time": 0,
          "max_wait_time": 0,
          "spawn_entity": "entity:ice",
          "num_to_spawn": 1,
          "single_use": true
        }
      ]
    }
  },
  "events": {
    "minecraft:ice_sword": {
      "add": {
        "component_groups": [
          "minecraft:ice_sword"
        ]
      }
    }
  }
}
```

## effect:jungle_sword

- Название в en_US: `§l§2Jungle Sword`
- Определение: `Sword_B/items/jungle_sword.json`
- Урон (`minecraft:damage`): `4`
- Прочность (`minecraft:durability`): `{"max_durability":128}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:jungle_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": false,
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
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 4
  }
}
```

### Прямые текстовые упоминания

- `Sword_B/entities/player.json`: строки 69, 647, 651, 886, 981, 984
- `Sword_B/functions/give.mcfunction`: строки 12
- `Sword_B/recipes/jungle_sword.json`: строки 5, 24
- `Sword_R/items/jungle_sword.json`: строки 5, 9
- `Sword_R/texts/en_US.lang`: строки 5
- `Sword_R/textures/item_texture.json`: строки 17, 18

### Рецепты и таблицы добычи с точным ID

`Sword_B/recipes/jungle_sword.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect:jungle_sword"
    },  
    "tags": [ "crafting_table" ],
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


### Одноимённые группы и события игрока (`Sword_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:jungle_sword": {
      "minecraft:spawn_entity": [
        {
          "min_wait_time": 0,
          "max_wait_time": 0,
          "spawn_entity": "entity:jungle",
          "num_to_spawn": 1,
          "single_use": true
        }
      ]
    }
  },
  "events": {
    "minecraft:jungle_sword": {
      "add": {
        "component_groups": [
          "minecraft:jungle_sword"
        ]
      }
    }
  }
}
```

## effect:lapis_sword

- Название в en_US: `§1Lapis Sword`
- Определение: `Sword_B/items/lapis_sword.json`
- Урон (`minecraft:damage`): `6`
- Прочность (`minecraft:durability`): `{"max_durability":528}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:lapis_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 528
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
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
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 6
  }
}
```

### Прямые текстовые упоминания

- `Sword_B/entities/player.json`: строки 58, 662, 666, 887, 988, 991
- `Sword_B/functions/give.mcfunction`: строки 13
- `Sword_B/recipes/lapis_sword.json`: строки 5, 22
- `Sword_R/items/lapis_sword.json`: строки 5, 9
- `Sword_R/texts/en_US.lang`: строки 10
- `Sword_R/textures/item_texture.json`: строки 29, 30

### Рецепты и таблицы добычи с точным ID

`Sword_B/recipes/lapis_sword.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect:lapis_sword"
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
        "item": "minecraft:lapis_block"
      }
    },
    "result": {
      "item": "effect:lapis_sword"
    }
  }
}
```


### Одноимённые группы и события игрока (`Sword_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:lapis_sword": {
      "minecraft:spawn_entity": [
        {
          "min_wait_time": 0,
          "max_wait_time": 0,
          "spawn_entity": "entity:lapis",
          "num_to_spawn": 1,
          "single_use": true
        }
      ]
    }
  },
  "events": {
    "minecraft:lapis_sword": {
      "add": {
        "component_groups": [
          "minecraft:lapis_sword"
        ]
      }
    }
  }
}
```

## effect:lightning_sword

- Название в en_US: `§g§lLightning Sword`
- Определение: `Sword_B/items/lightning_sword.json`
- Урон (`minecraft:damage`): `8`
- Прочность (`minecraft:durability`): `{"max_durability":2000}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:lightning_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": true,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 2000
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
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
          "repair_amount": 2000
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
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 8
  }
}
```

### Прямые текстовые упоминания

- `Sword_B/entities/player.json`: строки 47, 677, 681, 888, 995, 998
- `Sword_B/functions/give.mcfunction`: строки 14
- `Sword_B/recipes/lightning_sword.json`: строки 5, 22
- `Sword_R/items/lightning_sword.json`: строки 5, 9
- `Sword_R/texts/en_US.lang`: строки 22
- `Sword_R/textures/item_texture.json`: строки 59, 60

### Рецепты и таблицы добычи с точным ID

`Sword_B/recipes/lightning_sword.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect:lightning_sword"
    },  
    "tags": [ "crafting_table" ],
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


### Одноимённые группы и события игрока (`Sword_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:lightning_sword": {
      "minecraft:spawn_entity": [
        {
          "min_wait_time": 0,
          "max_wait_time": 0,
          "spawn_entity": "entity:lightning",
          "num_to_spawn": 1,
          "single_use": true
        }
      ]
    }
  },
  "events": {
    "minecraft:lightning_sword": {
      "add": {
        "component_groups": [
          "minecraft:lightning_sword"
        ]
      }
    }
  }
}
```

## effect:magma_sword

- Название в en_US: `§l§6Magma Sword`
- Определение: `Sword_B/items/magma_sword.json`
- Урон (`minecraft:damage`): `7`
- Прочность (`minecraft:durability`): `{"max_durability":1000}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:magma_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 1000
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
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
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 7
  }
}
```

### Прямые текстовые упоминания

- `Sword_B/entities/player.json`: строки 36, 692, 696, 889, 1002, 1005
- `Sword_B/functions/give.mcfunction`: строки 15
- `Sword_B/recipes/magma_sword.json`: строки 5, 22
- `Sword_R/items/magma_sword.json`: строки 5, 9
- `Sword_R/texts/en_US.lang`: строки 19
- `Sword_R/textures/item_texture.json`: строки 50, 51

### Рецепты и таблицы добычи с точным ID

`Sword_B/recipes/magma_sword.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect:magma_sword"
    },  
    "tags": [ "crafting_table" ],
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


### Одноимённые группы и события игрока (`Sword_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:magma_sword": {
      "minecraft:spawn_entity": [
        {
          "min_wait_time": 0,
          "max_wait_time": 0,
          "spawn_entity": "entity:magma",
          "num_to_spawn": 1,
          "single_use": true
        }
      ]
    }
  },
  "events": {
    "minecraft:magma_sword": {
      "add": {
        "component_groups": [
          "minecraft:magma_sword"
        ]
      }
    }
  }
}
```

## effect:obsidian_sword

- Название в en_US: `§l§8Obsidian Sword`
- Определение: `Sword_B/items/obsidian_sword.json`
- Урон (`minecraft:damage`): `12`
- Прочность (`minecraft:durability`): `{"max_durability":3000}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:obsidian_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 3000
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
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
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 12
  }
}
```

### Прямые текстовые упоминания

- `Sword_B/entities/player.json`: строки 303, 707, 711, 890, 1009, 1012
- `Sword_B/functions/give.mcfunction`: строки 16
- `Sword_B/recipes/obsidian_sword.json`: строки 5, 22
- `Sword_R/items/obsidian_sword.json`: строки 5, 9
- `Sword_R/texts/en_US.lang`: строки 14
- `Sword_R/textures/item_texture.json`: строки 35, 36

### Рецепты и таблицы добычи с точным ID

`Sword_B/recipes/obsidian_sword.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect:obsidian_sword"
    },  
    "tags": [ "crafting_table" ],
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


### Одноимённые группы и события игрока (`Sword_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:obsidian_sword": {
      "minecraft:spawn_entity": [
        {
          "min_wait_time": 0,
          "max_wait_time": 0,
          "spawn_entity": "entity:obsidian",
          "num_to_spawn": 1,
          "single_use": true
        }
      ]
    }
  },
  "events": {
    "minecraft:obsidian_sword": {
      "add": {
        "component_groups": [
          "minecraft:obsidian_sword"
        ]
      }
    }
  }
}
```

## effect:quartz_sword

- Название в en_US: `§lQuartz Sword`
- Определение: `Sword_B/items/quartz_sword.json`
- Урон (`minecraft:damage`): `600`
- Прочность (`minecraft:durability`): `{"max_durability":1}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:quartz_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": true,
    "minecraft:max_stack_size": 1,
    "minecraft:durability": {
      "max_durability": 1
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
    "minecraft:can_destroy_in_creative": false,
    "minecraft:icon": {
      "texture": "quartz_sword"
    },
    "minecraft:repairable": {
      "repair_items": [
        {
          "items": [
            "effect:quartz_sword"
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
          "speed": 15
        },
        {
          "block": "minecraft:bamboo",
          "speed": 10
        }
      ]
    },
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 600
  }
}
```

### Прямые текстовые упоминания

- `Sword_B/entities/player.json`: строки 325, 857, 861, 900, 1079, 1082
- `Sword_B/functions/give.mcfunction`: строки 17
- `Sword_B/recipes/quartz_sword.json`: строки 5, 27
- `Sword_R/items/quartz_sword.json`: строки 5, 9
- `Sword_R/texts/en_US.lang`: строки 26
- `Sword_R/textures/item_texture.json`: строки 80, 81

### Рецепты и таблицы добычи с точным ID

`Sword_B/recipes/quartz_sword.json`:

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


### Одноимённые группы и события игрока (`Sword_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:quartz_sword": {}
  },
  "events": {
    "minecraft:quartz_sword": {
      "add": {
        "component_groups": [
          "minecraft:quartz_sword"
        ]
      }
    }
  }
}
```

## effect:sea_sword

- Название в en_US: `§l§bSea Sword`
- Определение: `Sword_B/items/sea_sword.json`
- Урон (`minecraft:damage`): `7`
- Прочность (`minecraft:durability`): `{"max_durability":1000}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:sea_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": true,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 1000
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
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
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 7
  }
}
```

### Прямые текстовые упоминания

- `Sword_B/entities/player.json`: строки 102, 722, 726, 891, 1016, 1019
- `Sword_B/functions/give.mcfunction`: строки 18
- `Sword_B/recipes/sea_sword.json`: строки 5, 22
- `Sword_R/items/sea_sword.json`: строки 5, 9
- `Sword_R/texts/en_US.lang`: строки 11
- `Sword_R/textures/item_texture.json`: строки 68, 69

### Рецепты и таблицы добычи с точным ID

`Sword_B/recipes/sea_sword.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect:sea_sword"
    },  
    "tags": [ "crafting_table" ],
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


### Одноимённые группы и события игрока (`Sword_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:sea_sword": {
      "minecraft:spawn_entity": [
        {
          "min_wait_time": 0,
          "max_wait_time": 0,
          "spawn_entity": "entity:sea",
          "num_to_spawn": 1,
          "single_use": true
        }
      ]
    }
  },
  "events": {
    "minecraft:sea_sword": {
      "add": {
        "component_groups": [
          "minecraft:sea_sword"
        ]
      }
    }
  }
}
```

## effect:shulker_sword

- Название в en_US: `§l§5Shulker sword`
- Определение: `Sword_B/items/shulker_sword.json`
- Урон (`minecraft:damage`): `7`
- Прочность (`minecraft:durability`): `{"max_durability":1000}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:shulker_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 1000
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
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
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 7
  }
}
```

### Прямые текстовые упоминания

- `Sword_B/entities/player.json`: строки 91, 737, 741, 892, 1023, 1026
- `Sword_B/functions/give.mcfunction`: строки 19
- `Sword_B/recipes/shulker_sword.json`: строки 5, 22
- `Sword_R/items/shulker_sword.json`: строки 5, 9
- `Sword_R/texts/en_US.lang`: строки 3
- `Sword_R/textures/item_texture.json`: строки 8, 9

### Рецепты и таблицы добычи с точным ID

`Sword_B/recipes/shulker_sword.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect:shulker_sword"
    },  
    "tags": [ "crafting_table" ],
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


### Одноимённые группы и события игрока (`Sword_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:shulker_sword": {
      "minecraft:spawn_entity": [
        {
          "min_wait_time": 0,
          "max_wait_time": 0,
          "spawn_entity": "entity:shulker",
          "num_to_spawn": 1,
          "single_use": true
        }
      ]
    }
  },
  "events": {
    "minecraft:shulker_sword": {
      "add": {
        "component_groups": [
          "minecraft:shulker_sword"
        ]
      }
    }
  }
}
```

## effect:slime_sword

- Название в en_US: `§l§aSlime Sword`
- Определение: `Sword_B/items/slime_sword.json`
- Урон (`minecraft:damage`): `6`
- Прочность (`minecraft:durability`): `{"max_durability":675}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:slime_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 675
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
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
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 6
  }
}
```

### Прямые текстовые упоминания

- `Sword_B/entities/player.json`: строки 80, 752, 756, 893, 1030, 1033
- `Sword_B/functions/give.mcfunction`: строки 20
- `Sword_B/recipes/slime_sword.json`: строки 5, 22
- `Sword_R/items/slime_sword.json`: строки 5, 9
- `Sword_R/texts/en_US.lang`: строки 7
- `Sword_R/textures/item_texture.json`: строки 23, 24

### Рецепты и таблицы добычи с точным ID

`Sword_B/recipes/slime_sword.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect:slime_sword"
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
        "item": "minecraft:slime"
      }
    },
    "result": {
      "item": "effect:slime_sword"
    }
  }
}
```


### Одноимённые группы и события игрока (`Sword_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:slime_sword": {
      "minecraft:spawn_entity": [
        {
          "min_wait_time": 0,
          "max_wait_time": 0,
          "spawn_entity": "entity:slime",
          "num_to_spawn": 1,
          "single_use": true
        }
      ]
    }
  },
  "events": {
    "minecraft:slime_sword": {
      "add": {
        "component_groups": [
          "minecraft:slime_sword"
        ]
      }
    }
  }
}
```

## effect:spectral_sword

- Название в en_US: `§l§fSpectral Sword`
- Определение: `Sword_B/items/spectral_sword.json`
- Урон (`minecraft:damage`): `9`
- Прочность (`minecraft:durability`): `{"max_durability":3256}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:spectral_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": true,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 3256
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
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
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 9
  }
}
```

### Прямые текстовые упоминания

- `Sword_B/entities/player.json`: строки 25, 482, 486, 875, 904, 907
- `Sword_B/functions/give.mcfunction`: строки 21
- `Sword_B/recipes/spectral_sword.json`: строки 5, 25
- `Sword_R/items/spectral_sword.json`: строки 5, 9
- `Sword_R/texts/en_US.lang`: строки 9
- `Sword_R/textures/item_texture.json`: строки 32, 33

### Рецепты и таблицы добычи с точным ID

`Sword_B/recipes/spectral_sword.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect:spectral_sword"
    },  
    "tags": [ "crafting_table" ],
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


### Одноимённые группы и события игрока (`Sword_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:spectral_sword": {
      "minecraft:spawn_entity": [
        {
          "min_wait_time": 0,
          "max_wait_time": 0,
          "spawn_entity": "entity:spectral",
          "num_to_spawn": 1,
          "single_use": true
        }
      ]
    }
  },
  "events": {
    "minecraft:spectral_sword": {
      "add": {
        "component_groups": [
          "minecraft:spectral_sword"
        ]
      }
    }
  }
}
```

## effect:spider_sword

- Название в en_US: `§l§cSpider Sword`
- Определение: `Sword_B/items/spider_sword.json`
- Урон (`minecraft:damage`): `6`
- Прочность (`minecraft:durability`): `{"max_durability":628}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:spider_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": false,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 628
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
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
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 6
  }
}
```

### Прямые текстовые упоминания

- `Sword_B/entities/player.json`: строки 281, 767, 771, 894, 1037, 1040
- `Sword_B/functions/give.mcfunction`: строки 22
- `Sword_B/recipes/spider_sword.json`: строки 5, 25
- `Sword_R/items/spider_sword.json`: строки 5, 9
- `Sword_R/texts/en_US.lang`: строки 4
- `Sword_R/textures/item_texture.json`: строки 14, 15

### Рецепты и таблицы добычи с точным ID

`Sword_B/recipes/spider_sword.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect:spider_sword"
    },  
    "tags": [ "crafting_table" ],
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


### Одноимённые группы и события игрока (`Sword_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:spider_sword": {
      "minecraft:spawn_entity": [
        {
          "min_wait_time": 0,
          "max_wait_time": 0,
          "spawn_entity": "entity:spider",
          "num_to_spawn": 1,
          "single_use": true
        }
      ]
    }
  },
  "events": {
    "minecraft:spider_sword": {
      "add": {
        "component_groups": [
          "minecraft:spider_sword"
        ]
      }
    }
  }
}
```

## effect:sponge_sword

- Название в en_US: `§l§eSponge Sword`
- Определение: `Sword_B/items/sponge_sword.json`
- Урон (`minecraft:damage`): `6`
- Прочность (`minecraft:durability`): `{"max_durability":128}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:sponge_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": false,
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
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 6
  }
}
```

### Прямые текстовые упоминания

- `Sword_B/entities/player.json`: строки 270, 782, 786, 895, 1044, 1047
- `Sword_B/functions/give.mcfunction`: строки 23
- `Sword_B/recipes/sponge_sword.json`: строки 5, 22
- `Sword_R/items/sponge_sword.json`: строки 5, 9
- `Sword_R/texts/en_US.lang`: строки 24
- `Sword_R/textures/item_texture.json`: строки 65, 66

### Рецепты и таблицы добычи с точным ID

`Sword_B/recipes/sponge_sword.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect:sponge_sword"
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
        "item": "minecraft:sponge"
      }
    },
    "result": {
      "item": "effect:sponge_sword"
    }
  }
}
```


### Одноимённые группы и события игрока (`Sword_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:sponge_sword": {
      "minecraft:spawn_entity": [
        {
          "min_wait_time": 0,
          "max_wait_time": 0,
          "spawn_entity": "entity:sponge",
          "num_to_spawn": 1,
          "single_use": true
        }
      ]
    }
  },
  "events": {
    "minecraft:sponge_sword": {
      "add": {
        "component_groups": [
          "minecraft:sponge_sword"
        ]
      }
    }
  }
}
```

## effect:tnt_sword

- Название в en_US: `§4TNT§f Sword`
- Определение: `Sword_B/items/tnt_sword.json`
- Урон (`minecraft:damage`): `7`
- Прочность (`minecraft:durability`): `{"max_durability":1}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:tnt_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": false,
    "minecraft:max_stack_size": 1,
    "minecraft:durability": {
      "max_durability": 1
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
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
          "repair_amount": 1
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
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 7
  }
}
```

### Прямые текстовые упоминания

- `Sword_B/entities/player.json`: строки 248, 253, 812, 816, 897, 1058, 1061
- `Sword_B/entities/tnt_sword.json`: строки 5
- `Sword_B/functions/give.mcfunction`: строки 25
- `Sword_B/recipes/tnt_sword.json`: строки 5, 22
- `Sword_R/items/tnt_sword.json`: строки 5, 9
- `Sword_R/texts/en_US.lang`: строки 21
- `Sword_R/textures/item_texture.json`: строки 56, 57

### Рецепты и таблицы добычи с точным ID

`Sword_B/recipes/tnt_sword.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect:tnt_sword"
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
        "item": "minecraft:tnt"
      }
    },
    "result": {
      "item": "effect:tnt_sword"
    }
  }
}
```


### Одноимённые группы и события игрока (`Sword_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:tnt_sword": {
      "minecraft:spawn_entity": [
        {
          "min_wait_time": 0,
          "max_wait_time": 0,
          "spawn_entity": "entity:tnt_sword",
          "num_to_spawn": 1,
          "single_use": true
        }
      ]
    }
  },
  "events": {
    "minecraft:tnt_sword": {
      "add": {
        "component_groups": [
          "minecraft:tnt_sword"
        ]
      }
    }
  }
}
```

## effect:wither_sword

- Название в en_US: `§l§7Wither Sword`
- Определение: `Sword_B/items/wither_sword.json`
- Урон (`minecraft:damage`): `10`
- Прочность (`minecraft:durability`): `{"max_durability":1256}`
- Кулдаун (`minecraft:cooldown`): `"не указан"`

### Полное определение предмета

```json
{
  "description": {
    "identifier": "effect:wither_sword",
    "menu_category": {
      "category": "equipment"
    }
  },
  "components": {
    "minecraft:glint": true,
    "minecraft:max_stack_size": 1,
    "minecraft:enchantable": {
      "value": 9,
      "slot": "sword"
    },
    "minecraft:durability": {
      "max_durability": 1256
    },
    "minecraft:allow_off_hand": true,
    "minecraft:hand_equipped": true,
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
          "repair_amount": 1256
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
    "tag:minecraft:is_sword": {},
    "minecraft:damage": 10
  }
}
```

### Прямые текстовые упоминания

- `Sword_B/entities/player.json`: строки 237, 827, 831, 898, 1065, 1068
- `Sword_B/functions/give.mcfunction`: строки 26
- `Sword_B/recipes/wither_sword.json`: строки 5, 26
- `Sword_R/items/wither_sword.json`: строки 5, 9
- `Sword_R/texts/en_US.lang`: строки 20
- `Sword_R/textures/item_texture.json`: строки 53, 54

### Рецепты и таблицы добычи с точным ID

`Sword_B/recipes/wither_sword.json`:

```json
{
  "format_version": "1.11.0",
  "minecraft:recipe_shaped": {
    "description": {
    "identifier": "effect:wither_sword"
    },  
    "tags": [ "crafting_table" ],
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


### Одноимённые группы и события игрока (`Sword_B/entities/player.json`)

```json
{
  "component_groups": {
    "minecraft:wither_sword": {
      "minecraft:spawn_entity": [
        {
          "min_wait_time": 0,
          "max_wait_time": 0,
          "spawn_entity": "entity:wither",
          "num_to_spawn": 1,
          "single_use": true
        }
      ]
    }
  },
  "events": {
    "minecraft:wither_sword": {
      "add": {
        "component_groups": [
          "minecraft:wither_sword"
        ]
      }
    }
  }
}
```

