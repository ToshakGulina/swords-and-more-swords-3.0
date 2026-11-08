# Диагностическое сравнение повреждённого creeper.json

**Не исправление и не поведение игры:** исходный файл JSON5 не разбирается; для этих гипотетических данных в памяти удалена только последняя закрывающая скобка после удаления конечных пробелов. Авторская задумка и поведение Bedrock не установлены.

[Интерпретация и источники](manual-creeper-sword.md) · [метод внешних сравнений](manual-vanilla-override-review.md).

Оригинальный SHA-256: `8c8f169be60ee52a224928d57575cb3b47f19bf41c03e8dd5326f8440d6c33c2`; преобразованный UTF-8 SHA-256: `d666f1d0d7b91b5edfae1df375f06dde98e4e6ab577981822fa1bc4538d62917`.

## Образец `1.19.40.2`

SHA-256 файла образца: `6f8a46400a440580a9f450404476c17132e448f010cc7c81c9dd9984ffab8bce`.

### `component_groups`

**`minecraft:forced_charged_exploding`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:explode": {
        "causes_fire": false,
        "destroy_affected_by_griefing": true,
        "fuse_length": 1.5,
        "fuse_lit": true,
        "power": 6
      },
      "minecraft:on_target_escape": {},
      "minecraft:target_nearby_sensor": {},
      "minecraft:timer": {
        "looping": false,
        "time": [
          1.4,
          1.4
        ],
        "time_down_event": {
          "event": "creeper_sword",
          "target": "self"
        }
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:explode": {
        "causes_fire": false,
        "destroy_affected_by_griefing": true,
        "fuse_length": 1.5,
        "fuse_lit": true,
        "power": 6
      },
      "minecraft:on_target_escape": {},
      "minecraft:target_nearby_sensor": {}
    }
  }
}
```

**`minecraft:minicreeper`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:behavior.nearest_attackable_target": {
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "monster"
            },
            "max_dist": 16
          }
        ],
        "must_see": true,
        "must_see_forget_duration": 0.0,
        "priority": 1
      },
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": true,
          "on_damage": {
            "event": "start_minicreeper_exploding",
            "filters": {
              "any_of": [
                {
                  "operator": "!=",
                  "subject": "self",
                  "test": "has_damage",
                  "value": "void"
                }
              ]
            }
          }
        }
      },
      "minecraft:scale": {
        "value": 0.3
      },
      "minecraft:target_nearby_sensor": {
        "inside_range": 2.5,
        "must_see": true,
        "on_inside_range": {
          "event": "start_minicreeper_exploding",
          "target": "self"
        }
      },
      "minecraft:timer": {
        "looping": true,
        "randomInterval": false,
        "time": [
          10,
          10
        ],
        "time_down_event": {
          "event": "start_minicreeper_exploding",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "creeper",
          "player",
          "mob",
          "effect99_entities"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:minicreeper_exploding`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "cause": "all",
          "deals_damage": false
        }
      },
      "minecraft:explode": {
        "causes_fire": false,
        "destroy_affected_by_griefing": true,
        "fuse_length": 1.5,
        "fuse_lit": true,
        "power": 1
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:minicreeper_projectile`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:projectile": {
        "gravity": 0.02,
        "inertia": 1,
        "liquid_inertia": 1,
        "on_hit": {
          "definition_event": {
            "affect_projectile": true,
            "event_trigger": {
              "event": "minecraft:stop_projectile",
              "target": "self"
            }
          },
          "impact_damage": {
            "damage": 1,
            "knockback": true
          }
        },
        "power": 1
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

### `components`

**`minecraft:behavior.avoid_mob_type`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "entity_types": [
        {
          "filters": {
            "any_of": [
              {
                "subject": "other",
                "test": "is_family",
                "value": "ocelot"
              },
              {
                "subject": "other",
                "test": "is_family",
                "value": "cat"
              }
            ]
          },
          "max_dist": 6,
          "sprint_speed_multiplier": 1.2,
          "walk_speed_multiplier": 1
        }
      ],
      "priority": 3
    }
  },
  "reference": {
    "present": true,
    "value": {
      "entity_types": [
        {
          "filters": {
            "any_of": [
              {
                "subject": "other",
                "test": "is_family",
                "value": "ocelot"
              },
              {
                "subject": "other",
                "test": "is_family",
                "value": "cat"
              }
            ]
          },
          "max_dist": 6,
          "sprint_speed_multiplier": 1.2
        }
      ],
      "priority": 3
    }
  }
}
```

**`minecraft:behavior.nearest_attackable_target`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "entity_types": [
        {
          "filters": {
            "subject": "other",
            "test": "is_family",
            "value": "player"
          },
          "max_dist": 16
        }
      ],
      "must_see": true,
      "must_see_forget_duration": 0.0,
      "priority": 1
    }
  },
  "reference": {
    "present": true,
    "value": {
      "entity_types": [
        {
          "filters": {
            "subject": "other",
            "test": "is_family",
            "value": "player"
          },
          "max_dist": 16
        }
      ],
      "must_see": true,
      "must_see_forget_duration": 3.0,
      "priority": 1
    }
  }
}
```

**`minecraft:conditional_bandwidth_optimization`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {}
  }
}
```

**`minecraft:despawn`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "despawn_from_distance": {}
    }
  }
}
```

**`minecraft:is_hidden_when_invisible`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {}
  }
}
```

### `events`

**`creeper_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "randomize": [
        {
          "weight": 95
        },
        {
          "run_command": {
            "command": [
              "structure load creeper_sword ~ ~ ~"
            ]
          },
          "weight": 5
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:entity_spawned`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:minicreeper",
              "minecraft:minicreeper_projectile"
            ]
          },
          "filters": {
            "domain": "hand",
            "subject": "other",
            "test": "has_equipment",
            "value": "effect:creeper_sword"
          }
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:minicreeper`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:minicreeper"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:stop_projectile`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "remove": {
        "component_groups": [
          "minecraft:minicreeper_projectile"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`start_minicreeper_exploding`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:minicreeper_exploding"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

### `root`

**`format_version`**

```json
{
  "addon": {
    "present": true,
    "value": "1.13.0"
  },
  "reference": {
    "present": true,
    "value": "1.16.0"
  }
}
```

## Образец `1.20.30.1`

SHA-256 файла образца: `6f8a46400a440580a9f450404476c17132e448f010cc7c81c9dd9984ffab8bce`.

### `component_groups`

**`minecraft:forced_charged_exploding`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:explode": {
        "causes_fire": false,
        "destroy_affected_by_griefing": true,
        "fuse_length": 1.5,
        "fuse_lit": true,
        "power": 6
      },
      "minecraft:on_target_escape": {},
      "minecraft:target_nearby_sensor": {},
      "minecraft:timer": {
        "looping": false,
        "time": [
          1.4,
          1.4
        ],
        "time_down_event": {
          "event": "creeper_sword",
          "target": "self"
        }
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:explode": {
        "causes_fire": false,
        "destroy_affected_by_griefing": true,
        "fuse_length": 1.5,
        "fuse_lit": true,
        "power": 6
      },
      "minecraft:on_target_escape": {},
      "minecraft:target_nearby_sensor": {}
    }
  }
}
```

**`minecraft:minicreeper`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:behavior.nearest_attackable_target": {
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "monster"
            },
            "max_dist": 16
          }
        ],
        "must_see": true,
        "must_see_forget_duration": 0.0,
        "priority": 1
      },
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": true,
          "on_damage": {
            "event": "start_minicreeper_exploding",
            "filters": {
              "any_of": [
                {
                  "operator": "!=",
                  "subject": "self",
                  "test": "has_damage",
                  "value": "void"
                }
              ]
            }
          }
        }
      },
      "minecraft:scale": {
        "value": 0.3
      },
      "minecraft:target_nearby_sensor": {
        "inside_range": 2.5,
        "must_see": true,
        "on_inside_range": {
          "event": "start_minicreeper_exploding",
          "target": "self"
        }
      },
      "minecraft:timer": {
        "looping": true,
        "randomInterval": false,
        "time": [
          10,
          10
        ],
        "time_down_event": {
          "event": "start_minicreeper_exploding",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "creeper",
          "player",
          "mob",
          "effect99_entities"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:minicreeper_exploding`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "cause": "all",
          "deals_damage": false
        }
      },
      "minecraft:explode": {
        "causes_fire": false,
        "destroy_affected_by_griefing": true,
        "fuse_length": 1.5,
        "fuse_lit": true,
        "power": 1
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:minicreeper_projectile`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:projectile": {
        "gravity": 0.02,
        "inertia": 1,
        "liquid_inertia": 1,
        "on_hit": {
          "definition_event": {
            "affect_projectile": true,
            "event_trigger": {
              "event": "minecraft:stop_projectile",
              "target": "self"
            }
          },
          "impact_damage": {
            "damage": 1,
            "knockback": true
          }
        },
        "power": 1
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

### `components`

**`minecraft:behavior.avoid_mob_type`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "entity_types": [
        {
          "filters": {
            "any_of": [
              {
                "subject": "other",
                "test": "is_family",
                "value": "ocelot"
              },
              {
                "subject": "other",
                "test": "is_family",
                "value": "cat"
              }
            ]
          },
          "max_dist": 6,
          "sprint_speed_multiplier": 1.2,
          "walk_speed_multiplier": 1
        }
      ],
      "priority": 3
    }
  },
  "reference": {
    "present": true,
    "value": {
      "entity_types": [
        {
          "filters": {
            "any_of": [
              {
                "subject": "other",
                "test": "is_family",
                "value": "ocelot"
              },
              {
                "subject": "other",
                "test": "is_family",
                "value": "cat"
              }
            ]
          },
          "max_dist": 6,
          "sprint_speed_multiplier": 1.2
        }
      ],
      "priority": 3
    }
  }
}
```

**`minecraft:behavior.nearest_attackable_target`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "entity_types": [
        {
          "filters": {
            "subject": "other",
            "test": "is_family",
            "value": "player"
          },
          "max_dist": 16
        }
      ],
      "must_see": true,
      "must_see_forget_duration": 0.0,
      "priority": 1
    }
  },
  "reference": {
    "present": true,
    "value": {
      "entity_types": [
        {
          "filters": {
            "subject": "other",
            "test": "is_family",
            "value": "player"
          },
          "max_dist": 16
        }
      ],
      "must_see": true,
      "must_see_forget_duration": 3.0,
      "priority": 1
    }
  }
}
```

**`minecraft:conditional_bandwidth_optimization`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {}
  }
}
```

**`minecraft:despawn`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "despawn_from_distance": {}
    }
  }
}
```

**`minecraft:is_hidden_when_invisible`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {}
  }
}
```

### `events`

**`creeper_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "randomize": [
        {
          "weight": 95
        },
        {
          "run_command": {
            "command": [
              "structure load creeper_sword ~ ~ ~"
            ]
          },
          "weight": 5
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:entity_spawned`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:minicreeper",
              "minecraft:minicreeper_projectile"
            ]
          },
          "filters": {
            "domain": "hand",
            "subject": "other",
            "test": "has_equipment",
            "value": "effect:creeper_sword"
          }
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:minicreeper`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:minicreeper"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:stop_projectile`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "remove": {
        "component_groups": [
          "minecraft:minicreeper_projectile"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`start_minicreeper_exploding`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:minicreeper_exploding"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

### `root`

**`format_version`**

```json
{
  "addon": {
    "present": true,
    "value": "1.13.0"
  },
  "reference": {
    "present": true,
    "value": "1.16.0"
  }
}
```
