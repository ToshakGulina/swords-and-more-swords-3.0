# Полные значения отличающихся ключей player 1.6/2.x и пяти ванильных мобов 2.x

Структурная машинная выписка без игры. [Источники, ограничения, воспроизведение и ручной разбор](manual-vanilla-override-review.md).
Выводятся полные значения каждого отличающегося ключа в выбранных разделах; одинаковые не выводятся.
`present:false` — ключ отсутствует, а не значение по умолчанию; массивы упорядочены, 1 и 1.0 равны.

## `minecraft:blaze`

### Аддон `2.8.14`

SHA-256 файла: `9918581c5584a38910b0db61df2bdab370d33567c16af32bbe1298fc7893e169`.

#### Образец `1.19.40.2`

SHA-256 файла образца: `8dff5acd676fef87a23ff37418318469eeab97628970b1d03cebb61bb6d1d242`.

##### `component_groups`

**`melee_mode`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:attack": {
        "damage": 6
      },
      "minecraft:behavior.melee_attack": {
        "priority": 3
      }
    }
  }
}
```

**`mode_switcher`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:target_nearby_sensor": {
        "inside_range": 2.0,
        "must_see": true,
        "on_inside_range": {
          "event": "switch_to_melee",
          "target": "self"
        },
        "on_outside_range": {
          "event": "switch_to_ranged",
          "target": "self"
        },
        "outside_range": 3.0
      }
    }
  }
}
```

**`ranged_mode`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:behavior.ranged_attack": {
        "attack_interval_max": 5.0,
        "attack_interval_min": 3.0,
        "attack_radius": 16.0,
        "burst_interval": 0.3,
        "burst_shots": 3,
        "charge_charged_trigger": 0.0,
        "charge_shoot_trigger": 4.0,
        "priority": 3
      },
      "minecraft:shooter": {
        "def": "minecraft:small_fireball"
      }
    }
  }
}
```

##### `components`

**`minecraft:attack`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "damage": 6
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:behavior.melee_attack`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "max_dist": 3,
      "priority": 3,
      "random_stop_interval": 2.0,
      "speed_multiplier": 1,
      "track_target": true
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:behavior.random_look_around`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "priority": 6
    }
  },
  "reference": {
    "present": true,
    "value": {
      "priority": 5
    }
  }
}
```

**`minecraft:behavior.random_stroll`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "priority": 5,
      "speed_multiplier": 1.0
    }
  },
  "reference": {
    "present": true,
    "value": {
      "priority": 4,
      "speed_multiplier": 1.0
    }
  }
}
```

**`minecraft:behavior.ranged_attack`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "attack_interval_max": 5,
      "attack_interval_min": 3,
      "attack_radius": 16,
      "burst_interval": 0.3,
      "burst_shots": 3,
      "charge_charged_trigger": 0.0,
      "charge_shoot_trigger": 4.0,
      "priority": 4
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:can_fly`**

```json
{
  "addon": {
    "present": true,
    "value": {}
  },
  "reference": {
    "present": false
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

**`minecraft:damage_sensor`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "triggers": [
        {
          "cause": "fall",
          "deals_damage": false
        }
      ]
    }
  },
  "reference": {
    "present": true,
    "value": {
      "triggers": {
        "cause": "fall",
        "deals_damage": false
      }
    }
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

**`minecraft:fire_immune`**

```json
{
  "addon": {
    "present": true,
    "value": true
  },
  "reference": {
    "present": true,
    "value": {}
  }
}
```

**`minecraft:hurt_on_condition`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "damage_conditions": [
        {
          "cause": "drowning",
          "damage_per_tick": 1,
          "filters": {
            "operator": "==",
            "test": "in_water_or_rain",
            "value": true
          }
        }
      ]
    }
  },
  "reference": {
    "present": true,
    "value": {
      "damage_conditions": [
        {
          "cause": "drowning",
          "damage_per_tick": 1,
          "filters": {
            "operator": "==",
            "test": "in_contact_with_water",
            "value": true
          }
        }
      ]
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

**`minecraft:navigation.walk`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "can_path_over_water": true
    }
  },
  "reference": {
    "present": true,
    "value": {
      "avoid_damage_blocks": true,
      "avoid_water": true,
      "can_path_over_water": true
    }
  }
}
```

**`minecraft:on_hurt`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "event": "minecraft:on_hurt_event",
      "target": "self"
    }
  }
}
```

**`minecraft:on_hurt_by_player`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "event": "minecraft:on_hurt_event",
      "target": "self"
    }
  }
}
```

**`minecraft:shooter`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "def": "minecraft:small_fireball",
      "type": "smallfireball"
    }
  },
  "reference": {
    "present": false
  }
}
```

##### `events`

**`blaze_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "randomize": [
        {
          "weight": 995
        },
        {
          "run_command": {
            "command": [
              "structure load blaze_sword ~ ~ ~"
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
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "mode_switcher"
        ]
      }
    }
  }
}
```

**`minecraft:on_hurt_event`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "mode_switcher"
        ]
      }
    }
  }
}
```

**`switch_to_melee`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "melee_mode"
        ]
      },
      "remove": {
        "component_groups": [
          "ranged_mode"
        ]
      }
    }
  }
}
```

**`switch_to_ranged`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "ranged_mode"
        ]
      },
      "remove": {
        "component_groups": [
          "melee_mode"
        ]
      }
    }
  }
}
```

##### `root`

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

#### Образец `1.20.30.1`

SHA-256 файла образца: `8dff5acd676fef87a23ff37418318469eeab97628970b1d03cebb61bb6d1d242`.

##### `component_groups`

**`melee_mode`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:attack": {
        "damage": 6
      },
      "minecraft:behavior.melee_attack": {
        "priority": 3
      }
    }
  }
}
```

**`mode_switcher`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:target_nearby_sensor": {
        "inside_range": 2.0,
        "must_see": true,
        "on_inside_range": {
          "event": "switch_to_melee",
          "target": "self"
        },
        "on_outside_range": {
          "event": "switch_to_ranged",
          "target": "self"
        },
        "outside_range": 3.0
      }
    }
  }
}
```

**`ranged_mode`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:behavior.ranged_attack": {
        "attack_interval_max": 5.0,
        "attack_interval_min": 3.0,
        "attack_radius": 16.0,
        "burst_interval": 0.3,
        "burst_shots": 3,
        "charge_charged_trigger": 0.0,
        "charge_shoot_trigger": 4.0,
        "priority": 3
      },
      "minecraft:shooter": {
        "def": "minecraft:small_fireball"
      }
    }
  }
}
```

##### `components`

**`minecraft:attack`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "damage": 6
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:behavior.melee_attack`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "max_dist": 3,
      "priority": 3,
      "random_stop_interval": 2.0,
      "speed_multiplier": 1,
      "track_target": true
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:behavior.random_look_around`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "priority": 6
    }
  },
  "reference": {
    "present": true,
    "value": {
      "priority": 5
    }
  }
}
```

**`minecraft:behavior.random_stroll`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "priority": 5,
      "speed_multiplier": 1.0
    }
  },
  "reference": {
    "present": true,
    "value": {
      "priority": 4,
      "speed_multiplier": 1.0
    }
  }
}
```

**`minecraft:behavior.ranged_attack`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "attack_interval_max": 5,
      "attack_interval_min": 3,
      "attack_radius": 16,
      "burst_interval": 0.3,
      "burst_shots": 3,
      "charge_charged_trigger": 0.0,
      "charge_shoot_trigger": 4.0,
      "priority": 4
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:can_fly`**

```json
{
  "addon": {
    "present": true,
    "value": {}
  },
  "reference": {
    "present": false
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

**`minecraft:damage_sensor`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "triggers": [
        {
          "cause": "fall",
          "deals_damage": false
        }
      ]
    }
  },
  "reference": {
    "present": true,
    "value": {
      "triggers": {
        "cause": "fall",
        "deals_damage": false
      }
    }
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

**`minecraft:fire_immune`**

```json
{
  "addon": {
    "present": true,
    "value": true
  },
  "reference": {
    "present": true,
    "value": {}
  }
}
```

**`minecraft:hurt_on_condition`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "damage_conditions": [
        {
          "cause": "drowning",
          "damage_per_tick": 1,
          "filters": {
            "operator": "==",
            "test": "in_water_or_rain",
            "value": true
          }
        }
      ]
    }
  },
  "reference": {
    "present": true,
    "value": {
      "damage_conditions": [
        {
          "cause": "drowning",
          "damage_per_tick": 1,
          "filters": {
            "operator": "==",
            "test": "in_contact_with_water",
            "value": true
          }
        }
      ]
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

**`minecraft:navigation.walk`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "can_path_over_water": true
    }
  },
  "reference": {
    "present": true,
    "value": {
      "avoid_damage_blocks": true,
      "avoid_water": true,
      "can_path_over_water": true
    }
  }
}
```

**`minecraft:on_hurt`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "event": "minecraft:on_hurt_event",
      "target": "self"
    }
  }
}
```

**`minecraft:on_hurt_by_player`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "event": "minecraft:on_hurt_event",
      "target": "self"
    }
  }
}
```

**`minecraft:shooter`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "def": "minecraft:small_fireball",
      "type": "smallfireball"
    }
  },
  "reference": {
    "present": false
  }
}
```

##### `events`

**`blaze_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "randomize": [
        {
          "weight": 995
        },
        {
          "run_command": {
            "command": [
              "structure load blaze_sword ~ ~ ~"
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
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "mode_switcher"
        ]
      }
    }
  }
}
```

**`minecraft:on_hurt_event`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "mode_switcher"
        ]
      }
    }
  }
}
```

**`switch_to_melee`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "melee_mode"
        ]
      },
      "remove": {
        "component_groups": [
          "ranged_mode"
        ]
      }
    }
  }
}
```

**`switch_to_ranged`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "ranged_mode"
        ]
      },
      "remove": {
        "component_groups": [
          "melee_mode"
        ]
      }
    }
  }
}
```

##### `root`

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

### Аддон `2.8.8`

SHA-256 файла: `9918581c5584a38910b0db61df2bdab370d33567c16af32bbe1298fc7893e169`.

#### Образец `1.19.40.2`

SHA-256 файла образца: `8dff5acd676fef87a23ff37418318469eeab97628970b1d03cebb61bb6d1d242`.

##### `component_groups`

**`melee_mode`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:attack": {
        "damage": 6
      },
      "minecraft:behavior.melee_attack": {
        "priority": 3
      }
    }
  }
}
```

**`mode_switcher`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:target_nearby_sensor": {
        "inside_range": 2.0,
        "must_see": true,
        "on_inside_range": {
          "event": "switch_to_melee",
          "target": "self"
        },
        "on_outside_range": {
          "event": "switch_to_ranged",
          "target": "self"
        },
        "outside_range": 3.0
      }
    }
  }
}
```

**`ranged_mode`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:behavior.ranged_attack": {
        "attack_interval_max": 5.0,
        "attack_interval_min": 3.0,
        "attack_radius": 16.0,
        "burst_interval": 0.3,
        "burst_shots": 3,
        "charge_charged_trigger": 0.0,
        "charge_shoot_trigger": 4.0,
        "priority": 3
      },
      "minecraft:shooter": {
        "def": "minecraft:small_fireball"
      }
    }
  }
}
```

##### `components`

**`minecraft:attack`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "damage": 6
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:behavior.melee_attack`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "max_dist": 3,
      "priority": 3,
      "random_stop_interval": 2.0,
      "speed_multiplier": 1,
      "track_target": true
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:behavior.random_look_around`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "priority": 6
    }
  },
  "reference": {
    "present": true,
    "value": {
      "priority": 5
    }
  }
}
```

**`minecraft:behavior.random_stroll`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "priority": 5,
      "speed_multiplier": 1.0
    }
  },
  "reference": {
    "present": true,
    "value": {
      "priority": 4,
      "speed_multiplier": 1.0
    }
  }
}
```

**`minecraft:behavior.ranged_attack`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "attack_interval_max": 5,
      "attack_interval_min": 3,
      "attack_radius": 16,
      "burst_interval": 0.3,
      "burst_shots": 3,
      "charge_charged_trigger": 0.0,
      "charge_shoot_trigger": 4.0,
      "priority": 4
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:can_fly`**

```json
{
  "addon": {
    "present": true,
    "value": {}
  },
  "reference": {
    "present": false
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

**`minecraft:damage_sensor`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "triggers": [
        {
          "cause": "fall",
          "deals_damage": false
        }
      ]
    }
  },
  "reference": {
    "present": true,
    "value": {
      "triggers": {
        "cause": "fall",
        "deals_damage": false
      }
    }
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

**`minecraft:fire_immune`**

```json
{
  "addon": {
    "present": true,
    "value": true
  },
  "reference": {
    "present": true,
    "value": {}
  }
}
```

**`minecraft:hurt_on_condition`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "damage_conditions": [
        {
          "cause": "drowning",
          "damage_per_tick": 1,
          "filters": {
            "operator": "==",
            "test": "in_water_or_rain",
            "value": true
          }
        }
      ]
    }
  },
  "reference": {
    "present": true,
    "value": {
      "damage_conditions": [
        {
          "cause": "drowning",
          "damage_per_tick": 1,
          "filters": {
            "operator": "==",
            "test": "in_contact_with_water",
            "value": true
          }
        }
      ]
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

**`minecraft:navigation.walk`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "can_path_over_water": true
    }
  },
  "reference": {
    "present": true,
    "value": {
      "avoid_damage_blocks": true,
      "avoid_water": true,
      "can_path_over_water": true
    }
  }
}
```

**`minecraft:on_hurt`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "event": "minecraft:on_hurt_event",
      "target": "self"
    }
  }
}
```

**`minecraft:on_hurt_by_player`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "event": "minecraft:on_hurt_event",
      "target": "self"
    }
  }
}
```

**`minecraft:shooter`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "def": "minecraft:small_fireball",
      "type": "smallfireball"
    }
  },
  "reference": {
    "present": false
  }
}
```

##### `events`

**`blaze_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "randomize": [
        {
          "weight": 995
        },
        {
          "run_command": {
            "command": [
              "structure load blaze_sword ~ ~ ~"
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
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "mode_switcher"
        ]
      }
    }
  }
}
```

**`minecraft:on_hurt_event`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "mode_switcher"
        ]
      }
    }
  }
}
```

**`switch_to_melee`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "melee_mode"
        ]
      },
      "remove": {
        "component_groups": [
          "ranged_mode"
        ]
      }
    }
  }
}
```

**`switch_to_ranged`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "ranged_mode"
        ]
      },
      "remove": {
        "component_groups": [
          "melee_mode"
        ]
      }
    }
  }
}
```

##### `root`

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

#### Образец `1.20.30.1`

SHA-256 файла образца: `8dff5acd676fef87a23ff37418318469eeab97628970b1d03cebb61bb6d1d242`.

##### `component_groups`

**`melee_mode`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:attack": {
        "damage": 6
      },
      "minecraft:behavior.melee_attack": {
        "priority": 3
      }
    }
  }
}
```

**`mode_switcher`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:target_nearby_sensor": {
        "inside_range": 2.0,
        "must_see": true,
        "on_inside_range": {
          "event": "switch_to_melee",
          "target": "self"
        },
        "on_outside_range": {
          "event": "switch_to_ranged",
          "target": "self"
        },
        "outside_range": 3.0
      }
    }
  }
}
```

**`ranged_mode`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:behavior.ranged_attack": {
        "attack_interval_max": 5.0,
        "attack_interval_min": 3.0,
        "attack_radius": 16.0,
        "burst_interval": 0.3,
        "burst_shots": 3,
        "charge_charged_trigger": 0.0,
        "charge_shoot_trigger": 4.0,
        "priority": 3
      },
      "minecraft:shooter": {
        "def": "minecraft:small_fireball"
      }
    }
  }
}
```

##### `components`

**`minecraft:attack`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "damage": 6
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:behavior.melee_attack`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "max_dist": 3,
      "priority": 3,
      "random_stop_interval": 2.0,
      "speed_multiplier": 1,
      "track_target": true
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:behavior.random_look_around`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "priority": 6
    }
  },
  "reference": {
    "present": true,
    "value": {
      "priority": 5
    }
  }
}
```

**`minecraft:behavior.random_stroll`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "priority": 5,
      "speed_multiplier": 1.0
    }
  },
  "reference": {
    "present": true,
    "value": {
      "priority": 4,
      "speed_multiplier": 1.0
    }
  }
}
```

**`minecraft:behavior.ranged_attack`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "attack_interval_max": 5,
      "attack_interval_min": 3,
      "attack_radius": 16,
      "burst_interval": 0.3,
      "burst_shots": 3,
      "charge_charged_trigger": 0.0,
      "charge_shoot_trigger": 4.0,
      "priority": 4
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:can_fly`**

```json
{
  "addon": {
    "present": true,
    "value": {}
  },
  "reference": {
    "present": false
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

**`minecraft:damage_sensor`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "triggers": [
        {
          "cause": "fall",
          "deals_damage": false
        }
      ]
    }
  },
  "reference": {
    "present": true,
    "value": {
      "triggers": {
        "cause": "fall",
        "deals_damage": false
      }
    }
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

**`minecraft:fire_immune`**

```json
{
  "addon": {
    "present": true,
    "value": true
  },
  "reference": {
    "present": true,
    "value": {}
  }
}
```

**`minecraft:hurt_on_condition`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "damage_conditions": [
        {
          "cause": "drowning",
          "damage_per_tick": 1,
          "filters": {
            "operator": "==",
            "test": "in_water_or_rain",
            "value": true
          }
        }
      ]
    }
  },
  "reference": {
    "present": true,
    "value": {
      "damage_conditions": [
        {
          "cause": "drowning",
          "damage_per_tick": 1,
          "filters": {
            "operator": "==",
            "test": "in_contact_with_water",
            "value": true
          }
        }
      ]
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

**`minecraft:navigation.walk`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "can_path_over_water": true
    }
  },
  "reference": {
    "present": true,
    "value": {
      "avoid_damage_blocks": true,
      "avoid_water": true,
      "can_path_over_water": true
    }
  }
}
```

**`minecraft:on_hurt`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "event": "minecraft:on_hurt_event",
      "target": "self"
    }
  }
}
```

**`minecraft:on_hurt_by_player`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "event": "minecraft:on_hurt_event",
      "target": "self"
    }
  }
}
```

**`minecraft:shooter`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "def": "minecraft:small_fireball",
      "type": "smallfireball"
    }
  },
  "reference": {
    "present": false
  }
}
```

##### `events`

**`blaze_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "randomize": [
        {
          "weight": 995
        },
        {
          "run_command": {
            "command": [
              "structure load blaze_sword ~ ~ ~"
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
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "mode_switcher"
        ]
      }
    }
  }
}
```

**`minecraft:on_hurt_event`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "mode_switcher"
        ]
      }
    }
  }
}
```

**`switch_to_melee`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "melee_mode"
        ]
      },
      "remove": {
        "component_groups": [
          "ranged_mode"
        ]
      }
    }
  }
}
```

**`switch_to_ranged`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "ranged_mode"
        ]
      },
      "remove": {
        "component_groups": [
          "melee_mode"
        ]
      }
    }
  }
}
```

##### `root`

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

## `minecraft:cat`

### Аддон `2.8.14`

SHA-256 файла: `d384969ec5f6f0c2280911b61c320801faba8354840c1764e8cece5dd3b6bd3f`.

#### Образец `1.19.40.2`

SHA-256 файла образца: `9836e61046294dc1bcd6fbd2d299c15ea2bbe13cf122fb9302ae9bb96cbbb521`.

##### `component_groups`

**`minecraft:cat_adult`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:behavior.breed": {
        "priority": 3,
        "speed_multiplier": 1.0
      },
      "minecraft:breedable": {
        "allow_sitting": true,
        "breed_items": [
          "fish",
          "salmon"
        ],
        "breeds_with": {
          "baby_type": "minecraft:cat",
          "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
          },
          "mate_type": "minecraft:cat"
        },
        "require_tame": true
      },
      "minecraft:experience_reward": {
        "on_bred": "Math.Random(1,7)",
        "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
      },
      "minecraft:loot": {
        "table": "loot_tables/entities/cat.json"
      },
      "minecraft:scale": {
        "value": 0.8
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:behavior.breed": {
        "priority": 3,
        "speed_multiplier": 1.0
      },
      "minecraft:breedable": {
        "allow_sitting": true,
        "breed_items": [
          "fish",
          "salmon"
        ],
        "breeds_with": {
          "baby_type": "minecraft:cat",
          "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
          },
          "mate_type": "minecraft:cat"
        },
        "require_full_health": true,
        "require_tame": true
      },
      "minecraft:experience_reward": {
        "on_bred": "Math.Random(1,7)",
        "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
      },
      "minecraft:loot": {
        "table": "loot_tables/entities/cat.json"
      },
      "minecraft:scale": {
        "value": 0.8
      }
    }
  }
}
```

**`minecraft:cat_gift_for_owner`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:behavior.drop_item_for": {
        "drop_item_chance": 0.7,
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "player"
            },
            "max_dist": 6
          }
        ],
        "goal_radius": 1.0,
        "loot_table": "loot_tables/entities/cat_gift.json",
        "max_dist": 5,
        "offering_distance": 5,
        "on_drop_attempt": {
          "event": "minecraft:cat_gifted_owner",
          "target": "self"
        },
        "priority": 1,
        "search_count": 0,
        "search_height": 2,
        "search_range": 5,
        "speed_multiplier": 1.0,
        "time_of_day_range": [
          0.74999,
          0.8
        ]
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:behavior.drop_item_for": {
        "cooldown": 0.25,
        "drop_item_chance": 0.7,
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "player"
            },
            "max_dist": 6
          }
        ],
        "goal_radius": 1.0,
        "loot_table": "loot_tables/entities/cat_gift.json",
        "max_head_look_at_height": 10.0,
        "minimum_teleport_distance": 2.0,
        "offering_distance": 5.0,
        "on_drop_attempt": {
          "event": "minecraft:cat_gifted_owner",
          "target": "self"
        },
        "priority": 1,
        "search_count": 0,
        "search_height": 2,
        "search_range": 5,
        "seconds_before_pickup": 0.0,
        "speed_multiplier": 1.0,
        "target_range": [
          5.0,
          5.0,
          5.0
        ],
        "teleport_offset": [
          0.0,
          1.0,
          0.0
        ],
        "time_of_day_range": [
          0.74999,
          0.8
        ]
      }
    }
  }
}
```

**`minecraft:cat_tame`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:behavior.follow_owner": {
        "priority": 4,
        "speed_multiplier": 1.0,
        "start_distance": 10,
        "stop_distance": 2
      },
      "minecraft:behavior.ocelot_sit_on_block": {
        "priority": 7,
        "speed_multiplier": 1.0
      },
      "minecraft:behavior.pet_sleep_with_owner": {
        "goal_radius": 1.0,
        "priority": 2,
        "search_height": 10,
        "search_radius": 10,
        "speed_multiplier": 1.2
      },
      "minecraft:behavior.stay_while_sitting": {
        "priority": 3
      },
      "minecraft:behavior.tempt": {
        "items": [
          "fish",
          "salmon"
        ],
        "priority": 5,
        "speed_multiplier": 0.5,
        "within_radius": 16
      },
      "minecraft:color": {
        "value": 14
      },
      "minecraft:health": {
        "max": 20,
        "value": 20
      },
      "minecraft:is_dyeable": {
        "interact_text": "action.interact.dye"
      },
      "minecraft:is_tamed": {},
      "minecraft:leashable": {
        "hard_distance": 6.0,
        "max_distance": 10.0,
        "soft_distance": 4.0
      },
      "minecraft:on_wake_with_owner": {
        "event": "minecraft:pet_slept_with_owner",
        "target": "self"
      },
      "minecraft:sittable": {},
      "minecraft:type_family": {
        "family": [
          "cat",
          "mob",
          "tamed"
        ]
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:behavior.follow_owner": {
        "priority": 4,
        "speed_multiplier": 1.0,
        "start_distance": 10,
        "stop_distance": 2
      },
      "minecraft:behavior.ocelot_sit_on_block": {
        "priority": 7,
        "speed_multiplier": 1.0
      },
      "minecraft:behavior.pet_sleep_with_owner": {
        "goal_radius": 1.0,
        "priority": 2,
        "search_height": 10,
        "search_radius": 10,
        "speed_multiplier": 1.2
      },
      "minecraft:behavior.stay_while_sitting": {
        "priority": 3
      },
      "minecraft:behavior.tempt": {
        "items": [
          "fish",
          "salmon"
        ],
        "priority": 5,
        "speed_multiplier": 0.5,
        "within_radius": 16
      },
      "minecraft:color": {
        "value": 14
      },
      "minecraft:health": {
        "max": 20,
        "value": 20
      },
      "minecraft:is_dyeable": {
        "interact_text": "action.interact.dye"
      },
      "minecraft:is_tamed": {},
      "minecraft:on_wake_with_owner": {
        "event": "minecraft:pet_slept_with_owner",
        "target": "self"
      },
      "minecraft:sittable": {}
    }
  }
}
```

**`minecraft:cat_wild`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:behavior.avoid_mob_type": {
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "player"
            },
            "max_dist": 10,
            "sprint_speed_multiplier": 1.33,
            "walk_speed_multiplier": 0.8
          }
        ],
        "priority": 6
      },
      "minecraft:behavior.move_towards_restriction": {
        "priority": 7
      },
      "minecraft:behavior.nearest_attackable_target": {
        "attack_interval": 10,
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "rabbit"
            },
            "max_dist": 8
          },
          {
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "baby_turtle"
                },
                {
                  "operator": "!=",
                  "subject": "other",
                  "test": "in_water",
                  "value": true
                }
              ]
            },
            "max_dist": 8
          }
        ],
        "priority": 1,
        "reselect_targets": true,
        "within_radius": 16.0
      },
      "minecraft:behavior.tempt": {
        "can_get_scared": true,
        "items": [
          "fish",
          "salmon"
        ],
        "priority": 5,
        "speed_multiplier": 0.5,
        "within_radius": 16
      },
      "minecraft:health": {
        "max": 10,
        "value": 10
      },
      "minecraft:rideable": {
        "family_types": [
          "zombie"
        ],
        "seat_count": 1,
        "seats": {
          "position": [
            0.0,
            0.35,
            0.0
          ]
        }
      },
      "minecraft:tameable": {
        "probability": 0.33,
        "tame_event": {
          "event": "minecraft:on_tame",
          "target": "self"
        },
        "tame_items": [
          "fish",
          "salmon"
        ]
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:behavior.avoid_mob_type": {
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "player"
            },
            "max_dist": 10,
            "sprint_speed_multiplier": 1.33,
            "walk_speed_multiplier": 0.8
          }
        ],
        "priority": 6
      },
      "minecraft:behavior.move_towards_dwelling_restriction": {
        "priority": 7
      },
      "minecraft:behavior.nearest_attackable_target": {
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "rabbit"
            },
            "max_dist": 8
          },
          {
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "baby_turtle"
                },
                {
                  "operator": "!=",
                  "subject": "other",
                  "test": "in_water",
                  "value": true
                }
              ]
            },
            "max_dist": 8
          }
        ],
        "priority": 1,
        "reselect_targets": true,
        "within_radius": 16.0
      },
      "minecraft:behavior.tempt": {
        "can_get_scared": true,
        "items": [
          "fish",
          "salmon"
        ],
        "priority": 5,
        "speed_multiplier": 0.5,
        "within_radius": 16
      },
      "minecraft:health": {
        "max": 10,
        "value": 10
      },
      "minecraft:rideable": {
        "family_types": [
          "zombie"
        ],
        "seat_count": 1,
        "seats": {
          "position": [
            0.0,
            0.35,
            0.0
          ]
        }
      },
      "minecraft:tameable": {
        "probability": 0.33,
        "tame_event": {
          "event": "minecraft:on_tame",
          "target": "self"
        },
        "tame_items": [
          "fish",
          "salmon"
        ]
      }
    }
  }
}
```

##### `components`

**`minecraft:balloonable`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "mass": 0.6
    }
  }
}
```

**`minecraft:behavior.ocelotattack`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "priority": 4,
      "sneak_speed_multiplier": 0.6,
      "sprint_speed_multiplier": 1.33,
      "walk_speed_multiplier": 0.8
    }
  },
  "reference": {
    "present": true,
    "value": {
      "cooldown_time": 1.0,
      "max_distance": 15.0,
      "max_sneak_range": 15.0,
      "max_sprint_range": 4.0,
      "priority": 4,
      "reach_multiplier": 2.0,
      "sneak_speed_multiplier": 0.6,
      "sprint_speed_multiplier": 1.33,
      "walk_speed_multiplier": 0.8,
      "x_max_rotation": 30.0,
      "y_max_head_rotation": 30.0
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

**`minecraft:leashable`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "hard_distance": 6.0,
      "max_distance": 10.0,
      "soft_distance": 4.0
    }
  }
}
```

##### `root`

**`format_version`**

```json
{
  "addon": {
    "present": true,
    "value": "1.13.0"
  },
  "reference": {
    "present": true,
    "value": "1.18.10"
  }
}
```

#### Образец `1.20.30.1`

SHA-256 файла образца: `9836e61046294dc1bcd6fbd2d299c15ea2bbe13cf122fb9302ae9bb96cbbb521`.

##### `component_groups`

**`minecraft:cat_adult`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:behavior.breed": {
        "priority": 3,
        "speed_multiplier": 1.0
      },
      "minecraft:breedable": {
        "allow_sitting": true,
        "breed_items": [
          "fish",
          "salmon"
        ],
        "breeds_with": {
          "baby_type": "minecraft:cat",
          "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
          },
          "mate_type": "minecraft:cat"
        },
        "require_tame": true
      },
      "minecraft:experience_reward": {
        "on_bred": "Math.Random(1,7)",
        "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
      },
      "minecraft:loot": {
        "table": "loot_tables/entities/cat.json"
      },
      "minecraft:scale": {
        "value": 0.8
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:behavior.breed": {
        "priority": 3,
        "speed_multiplier": 1.0
      },
      "minecraft:breedable": {
        "allow_sitting": true,
        "breed_items": [
          "fish",
          "salmon"
        ],
        "breeds_with": {
          "baby_type": "minecraft:cat",
          "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
          },
          "mate_type": "minecraft:cat"
        },
        "require_full_health": true,
        "require_tame": true
      },
      "minecraft:experience_reward": {
        "on_bred": "Math.Random(1,7)",
        "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
      },
      "minecraft:loot": {
        "table": "loot_tables/entities/cat.json"
      },
      "minecraft:scale": {
        "value": 0.8
      }
    }
  }
}
```

**`minecraft:cat_gift_for_owner`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:behavior.drop_item_for": {
        "drop_item_chance": 0.7,
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "player"
            },
            "max_dist": 6
          }
        ],
        "goal_radius": 1.0,
        "loot_table": "loot_tables/entities/cat_gift.json",
        "max_dist": 5,
        "offering_distance": 5,
        "on_drop_attempt": {
          "event": "minecraft:cat_gifted_owner",
          "target": "self"
        },
        "priority": 1,
        "search_count": 0,
        "search_height": 2,
        "search_range": 5,
        "speed_multiplier": 1.0,
        "time_of_day_range": [
          0.74999,
          0.8
        ]
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:behavior.drop_item_for": {
        "cooldown": 0.25,
        "drop_item_chance": 0.7,
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "player"
            },
            "max_dist": 6
          }
        ],
        "goal_radius": 1.0,
        "loot_table": "loot_tables/entities/cat_gift.json",
        "max_head_look_at_height": 10.0,
        "minimum_teleport_distance": 2.0,
        "offering_distance": 5.0,
        "on_drop_attempt": {
          "event": "minecraft:cat_gifted_owner",
          "target": "self"
        },
        "priority": 1,
        "search_count": 0,
        "search_height": 2,
        "search_range": 5,
        "seconds_before_pickup": 0.0,
        "speed_multiplier": 1.0,
        "target_range": [
          5.0,
          5.0,
          5.0
        ],
        "teleport_offset": [
          0.0,
          1.0,
          0.0
        ],
        "time_of_day_range": [
          0.74999,
          0.8
        ]
      }
    }
  }
}
```

**`minecraft:cat_tame`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:behavior.follow_owner": {
        "priority": 4,
        "speed_multiplier": 1.0,
        "start_distance": 10,
        "stop_distance": 2
      },
      "minecraft:behavior.ocelot_sit_on_block": {
        "priority": 7,
        "speed_multiplier": 1.0
      },
      "minecraft:behavior.pet_sleep_with_owner": {
        "goal_radius": 1.0,
        "priority": 2,
        "search_height": 10,
        "search_radius": 10,
        "speed_multiplier": 1.2
      },
      "minecraft:behavior.stay_while_sitting": {
        "priority": 3
      },
      "minecraft:behavior.tempt": {
        "items": [
          "fish",
          "salmon"
        ],
        "priority": 5,
        "speed_multiplier": 0.5,
        "within_radius": 16
      },
      "minecraft:color": {
        "value": 14
      },
      "minecraft:health": {
        "max": 20,
        "value": 20
      },
      "minecraft:is_dyeable": {
        "interact_text": "action.interact.dye"
      },
      "minecraft:is_tamed": {},
      "minecraft:leashable": {
        "hard_distance": 6.0,
        "max_distance": 10.0,
        "soft_distance": 4.0
      },
      "minecraft:on_wake_with_owner": {
        "event": "minecraft:pet_slept_with_owner",
        "target": "self"
      },
      "minecraft:sittable": {},
      "minecraft:type_family": {
        "family": [
          "cat",
          "mob",
          "tamed"
        ]
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:behavior.follow_owner": {
        "priority": 4,
        "speed_multiplier": 1.0,
        "start_distance": 10,
        "stop_distance": 2
      },
      "minecraft:behavior.ocelot_sit_on_block": {
        "priority": 7,
        "speed_multiplier": 1.0
      },
      "minecraft:behavior.pet_sleep_with_owner": {
        "goal_radius": 1.0,
        "priority": 2,
        "search_height": 10,
        "search_radius": 10,
        "speed_multiplier": 1.2
      },
      "minecraft:behavior.stay_while_sitting": {
        "priority": 3
      },
      "minecraft:behavior.tempt": {
        "items": [
          "fish",
          "salmon"
        ],
        "priority": 5,
        "speed_multiplier": 0.5,
        "within_radius": 16
      },
      "minecraft:color": {
        "value": 14
      },
      "minecraft:health": {
        "max": 20,
        "value": 20
      },
      "minecraft:is_dyeable": {
        "interact_text": "action.interact.dye"
      },
      "minecraft:is_tamed": {},
      "minecraft:on_wake_with_owner": {
        "event": "minecraft:pet_slept_with_owner",
        "target": "self"
      },
      "minecraft:sittable": {}
    }
  }
}
```

**`minecraft:cat_wild`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:behavior.avoid_mob_type": {
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "player"
            },
            "max_dist": 10,
            "sprint_speed_multiplier": 1.33,
            "walk_speed_multiplier": 0.8
          }
        ],
        "priority": 6
      },
      "minecraft:behavior.move_towards_restriction": {
        "priority": 7
      },
      "minecraft:behavior.nearest_attackable_target": {
        "attack_interval": 10,
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "rabbit"
            },
            "max_dist": 8
          },
          {
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "baby_turtle"
                },
                {
                  "operator": "!=",
                  "subject": "other",
                  "test": "in_water",
                  "value": true
                }
              ]
            },
            "max_dist": 8
          }
        ],
        "priority": 1,
        "reselect_targets": true,
        "within_radius": 16.0
      },
      "minecraft:behavior.tempt": {
        "can_get_scared": true,
        "items": [
          "fish",
          "salmon"
        ],
        "priority": 5,
        "speed_multiplier": 0.5,
        "within_radius": 16
      },
      "minecraft:health": {
        "max": 10,
        "value": 10
      },
      "minecraft:rideable": {
        "family_types": [
          "zombie"
        ],
        "seat_count": 1,
        "seats": {
          "position": [
            0.0,
            0.35,
            0.0
          ]
        }
      },
      "minecraft:tameable": {
        "probability": 0.33,
        "tame_event": {
          "event": "minecraft:on_tame",
          "target": "self"
        },
        "tame_items": [
          "fish",
          "salmon"
        ]
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:behavior.avoid_mob_type": {
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "player"
            },
            "max_dist": 10,
            "sprint_speed_multiplier": 1.33,
            "walk_speed_multiplier": 0.8
          }
        ],
        "priority": 6
      },
      "minecraft:behavior.move_towards_dwelling_restriction": {
        "priority": 7
      },
      "minecraft:behavior.nearest_attackable_target": {
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "rabbit"
            },
            "max_dist": 8
          },
          {
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "baby_turtle"
                },
                {
                  "operator": "!=",
                  "subject": "other",
                  "test": "in_water",
                  "value": true
                }
              ]
            },
            "max_dist": 8
          }
        ],
        "priority": 1,
        "reselect_targets": true,
        "within_radius": 16.0
      },
      "minecraft:behavior.tempt": {
        "can_get_scared": true,
        "items": [
          "fish",
          "salmon"
        ],
        "priority": 5,
        "speed_multiplier": 0.5,
        "within_radius": 16
      },
      "minecraft:health": {
        "max": 10,
        "value": 10
      },
      "minecraft:rideable": {
        "family_types": [
          "zombie"
        ],
        "seat_count": 1,
        "seats": {
          "position": [
            0.0,
            0.35,
            0.0
          ]
        }
      },
      "minecraft:tameable": {
        "probability": 0.33,
        "tame_event": {
          "event": "minecraft:on_tame",
          "target": "self"
        },
        "tame_items": [
          "fish",
          "salmon"
        ]
      }
    }
  }
}
```

##### `components`

**`minecraft:balloonable`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "mass": 0.6
    }
  }
}
```

**`minecraft:behavior.ocelotattack`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "priority": 4,
      "sneak_speed_multiplier": 0.6,
      "sprint_speed_multiplier": 1.33,
      "walk_speed_multiplier": 0.8
    }
  },
  "reference": {
    "present": true,
    "value": {
      "cooldown_time": 1.0,
      "max_distance": 15.0,
      "max_sneak_range": 15.0,
      "max_sprint_range": 4.0,
      "priority": 4,
      "reach_multiplier": 2.0,
      "sneak_speed_multiplier": 0.6,
      "sprint_speed_multiplier": 1.33,
      "walk_speed_multiplier": 0.8,
      "x_max_rotation": 30.0,
      "y_max_head_rotation": 30.0
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

**`minecraft:leashable`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "hard_distance": 6.0,
      "max_distance": 10.0,
      "soft_distance": 4.0
    }
  }
}
```

##### `root`

**`format_version`**

```json
{
  "addon": {
    "present": true,
    "value": "1.13.0"
  },
  "reference": {
    "present": true,
    "value": "1.18.10"
  }
}
```

### Аддон `2.8.8`

SHA-256 файла: `d384969ec5f6f0c2280911b61c320801faba8354840c1764e8cece5dd3b6bd3f`.

#### Образец `1.19.40.2`

SHA-256 файла образца: `9836e61046294dc1bcd6fbd2d299c15ea2bbe13cf122fb9302ae9bb96cbbb521`.

##### `component_groups`

**`minecraft:cat_adult`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:behavior.breed": {
        "priority": 3,
        "speed_multiplier": 1.0
      },
      "minecraft:breedable": {
        "allow_sitting": true,
        "breed_items": [
          "fish",
          "salmon"
        ],
        "breeds_with": {
          "baby_type": "minecraft:cat",
          "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
          },
          "mate_type": "minecraft:cat"
        },
        "require_tame": true
      },
      "minecraft:experience_reward": {
        "on_bred": "Math.Random(1,7)",
        "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
      },
      "minecraft:loot": {
        "table": "loot_tables/entities/cat.json"
      },
      "minecraft:scale": {
        "value": 0.8
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:behavior.breed": {
        "priority": 3,
        "speed_multiplier": 1.0
      },
      "minecraft:breedable": {
        "allow_sitting": true,
        "breed_items": [
          "fish",
          "salmon"
        ],
        "breeds_with": {
          "baby_type": "minecraft:cat",
          "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
          },
          "mate_type": "minecraft:cat"
        },
        "require_full_health": true,
        "require_tame": true
      },
      "minecraft:experience_reward": {
        "on_bred": "Math.Random(1,7)",
        "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
      },
      "minecraft:loot": {
        "table": "loot_tables/entities/cat.json"
      },
      "minecraft:scale": {
        "value": 0.8
      }
    }
  }
}
```

**`minecraft:cat_gift_for_owner`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:behavior.drop_item_for": {
        "drop_item_chance": 0.7,
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "player"
            },
            "max_dist": 6
          }
        ],
        "goal_radius": 1.0,
        "loot_table": "loot_tables/entities/cat_gift.json",
        "max_dist": 5,
        "offering_distance": 5,
        "on_drop_attempt": {
          "event": "minecraft:cat_gifted_owner",
          "target": "self"
        },
        "priority": 1,
        "search_count": 0,
        "search_height": 2,
        "search_range": 5,
        "speed_multiplier": 1.0,
        "time_of_day_range": [
          0.74999,
          0.8
        ]
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:behavior.drop_item_for": {
        "cooldown": 0.25,
        "drop_item_chance": 0.7,
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "player"
            },
            "max_dist": 6
          }
        ],
        "goal_radius": 1.0,
        "loot_table": "loot_tables/entities/cat_gift.json",
        "max_head_look_at_height": 10.0,
        "minimum_teleport_distance": 2.0,
        "offering_distance": 5.0,
        "on_drop_attempt": {
          "event": "minecraft:cat_gifted_owner",
          "target": "self"
        },
        "priority": 1,
        "search_count": 0,
        "search_height": 2,
        "search_range": 5,
        "seconds_before_pickup": 0.0,
        "speed_multiplier": 1.0,
        "target_range": [
          5.0,
          5.0,
          5.0
        ],
        "teleport_offset": [
          0.0,
          1.0,
          0.0
        ],
        "time_of_day_range": [
          0.74999,
          0.8
        ]
      }
    }
  }
}
```

**`minecraft:cat_tame`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:behavior.follow_owner": {
        "priority": 4,
        "speed_multiplier": 1.0,
        "start_distance": 10,
        "stop_distance": 2
      },
      "minecraft:behavior.ocelot_sit_on_block": {
        "priority": 7,
        "speed_multiplier": 1.0
      },
      "minecraft:behavior.pet_sleep_with_owner": {
        "goal_radius": 1.0,
        "priority": 2,
        "search_height": 10,
        "search_radius": 10,
        "speed_multiplier": 1.2
      },
      "minecraft:behavior.stay_while_sitting": {
        "priority": 3
      },
      "minecraft:behavior.tempt": {
        "items": [
          "fish",
          "salmon"
        ],
        "priority": 5,
        "speed_multiplier": 0.5,
        "within_radius": 16
      },
      "minecraft:color": {
        "value": 14
      },
      "minecraft:health": {
        "max": 20,
        "value": 20
      },
      "minecraft:is_dyeable": {
        "interact_text": "action.interact.dye"
      },
      "minecraft:is_tamed": {},
      "minecraft:leashable": {
        "hard_distance": 6.0,
        "max_distance": 10.0,
        "soft_distance": 4.0
      },
      "minecraft:on_wake_with_owner": {
        "event": "minecraft:pet_slept_with_owner",
        "target": "self"
      },
      "minecraft:sittable": {},
      "minecraft:type_family": {
        "family": [
          "cat",
          "mob",
          "tamed"
        ]
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:behavior.follow_owner": {
        "priority": 4,
        "speed_multiplier": 1.0,
        "start_distance": 10,
        "stop_distance": 2
      },
      "minecraft:behavior.ocelot_sit_on_block": {
        "priority": 7,
        "speed_multiplier": 1.0
      },
      "minecraft:behavior.pet_sleep_with_owner": {
        "goal_radius": 1.0,
        "priority": 2,
        "search_height": 10,
        "search_radius": 10,
        "speed_multiplier": 1.2
      },
      "minecraft:behavior.stay_while_sitting": {
        "priority": 3
      },
      "minecraft:behavior.tempt": {
        "items": [
          "fish",
          "salmon"
        ],
        "priority": 5,
        "speed_multiplier": 0.5,
        "within_radius": 16
      },
      "minecraft:color": {
        "value": 14
      },
      "minecraft:health": {
        "max": 20,
        "value": 20
      },
      "minecraft:is_dyeable": {
        "interact_text": "action.interact.dye"
      },
      "minecraft:is_tamed": {},
      "minecraft:on_wake_with_owner": {
        "event": "minecraft:pet_slept_with_owner",
        "target": "self"
      },
      "minecraft:sittable": {}
    }
  }
}
```

**`minecraft:cat_wild`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:behavior.avoid_mob_type": {
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "player"
            },
            "max_dist": 10,
            "sprint_speed_multiplier": 1.33,
            "walk_speed_multiplier": 0.8
          }
        ],
        "priority": 6
      },
      "minecraft:behavior.move_towards_restriction": {
        "priority": 7
      },
      "minecraft:behavior.nearest_attackable_target": {
        "attack_interval": 10,
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "rabbit"
            },
            "max_dist": 8
          },
          {
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "baby_turtle"
                },
                {
                  "operator": "!=",
                  "subject": "other",
                  "test": "in_water",
                  "value": true
                }
              ]
            },
            "max_dist": 8
          }
        ],
        "priority": 1,
        "reselect_targets": true,
        "within_radius": 16.0
      },
      "minecraft:behavior.tempt": {
        "can_get_scared": true,
        "items": [
          "fish",
          "salmon"
        ],
        "priority": 5,
        "speed_multiplier": 0.5,
        "within_radius": 16
      },
      "minecraft:health": {
        "max": 10,
        "value": 10
      },
      "minecraft:rideable": {
        "family_types": [
          "zombie"
        ],
        "seat_count": 1,
        "seats": {
          "position": [
            0.0,
            0.35,
            0.0
          ]
        }
      },
      "minecraft:tameable": {
        "probability": 0.33,
        "tame_event": {
          "event": "minecraft:on_tame",
          "target": "self"
        },
        "tame_items": [
          "fish",
          "salmon"
        ]
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:behavior.avoid_mob_type": {
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "player"
            },
            "max_dist": 10,
            "sprint_speed_multiplier": 1.33,
            "walk_speed_multiplier": 0.8
          }
        ],
        "priority": 6
      },
      "minecraft:behavior.move_towards_dwelling_restriction": {
        "priority": 7
      },
      "minecraft:behavior.nearest_attackable_target": {
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "rabbit"
            },
            "max_dist": 8
          },
          {
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "baby_turtle"
                },
                {
                  "operator": "!=",
                  "subject": "other",
                  "test": "in_water",
                  "value": true
                }
              ]
            },
            "max_dist": 8
          }
        ],
        "priority": 1,
        "reselect_targets": true,
        "within_radius": 16.0
      },
      "minecraft:behavior.tempt": {
        "can_get_scared": true,
        "items": [
          "fish",
          "salmon"
        ],
        "priority": 5,
        "speed_multiplier": 0.5,
        "within_radius": 16
      },
      "minecraft:health": {
        "max": 10,
        "value": 10
      },
      "minecraft:rideable": {
        "family_types": [
          "zombie"
        ],
        "seat_count": 1,
        "seats": {
          "position": [
            0.0,
            0.35,
            0.0
          ]
        }
      },
      "minecraft:tameable": {
        "probability": 0.33,
        "tame_event": {
          "event": "minecraft:on_tame",
          "target": "self"
        },
        "tame_items": [
          "fish",
          "salmon"
        ]
      }
    }
  }
}
```

##### `components`

**`minecraft:balloonable`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "mass": 0.6
    }
  }
}
```

**`minecraft:behavior.ocelotattack`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "priority": 4,
      "sneak_speed_multiplier": 0.6,
      "sprint_speed_multiplier": 1.33,
      "walk_speed_multiplier": 0.8
    }
  },
  "reference": {
    "present": true,
    "value": {
      "cooldown_time": 1.0,
      "max_distance": 15.0,
      "max_sneak_range": 15.0,
      "max_sprint_range": 4.0,
      "priority": 4,
      "reach_multiplier": 2.0,
      "sneak_speed_multiplier": 0.6,
      "sprint_speed_multiplier": 1.33,
      "walk_speed_multiplier": 0.8,
      "x_max_rotation": 30.0,
      "y_max_head_rotation": 30.0
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

**`minecraft:leashable`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "hard_distance": 6.0,
      "max_distance": 10.0,
      "soft_distance": 4.0
    }
  }
}
```

##### `root`

**`format_version`**

```json
{
  "addon": {
    "present": true,
    "value": "1.13.0"
  },
  "reference": {
    "present": true,
    "value": "1.18.10"
  }
}
```

#### Образец `1.20.30.1`

SHA-256 файла образца: `9836e61046294dc1bcd6fbd2d299c15ea2bbe13cf122fb9302ae9bb96cbbb521`.

##### `component_groups`

**`minecraft:cat_adult`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:behavior.breed": {
        "priority": 3,
        "speed_multiplier": 1.0
      },
      "minecraft:breedable": {
        "allow_sitting": true,
        "breed_items": [
          "fish",
          "salmon"
        ],
        "breeds_with": {
          "baby_type": "minecraft:cat",
          "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
          },
          "mate_type": "minecraft:cat"
        },
        "require_tame": true
      },
      "minecraft:experience_reward": {
        "on_bred": "Math.Random(1,7)",
        "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
      },
      "minecraft:loot": {
        "table": "loot_tables/entities/cat.json"
      },
      "minecraft:scale": {
        "value": 0.8
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:behavior.breed": {
        "priority": 3,
        "speed_multiplier": 1.0
      },
      "minecraft:breedable": {
        "allow_sitting": true,
        "breed_items": [
          "fish",
          "salmon"
        ],
        "breeds_with": {
          "baby_type": "minecraft:cat",
          "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
          },
          "mate_type": "minecraft:cat"
        },
        "require_full_health": true,
        "require_tame": true
      },
      "minecraft:experience_reward": {
        "on_bred": "Math.Random(1,7)",
        "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
      },
      "minecraft:loot": {
        "table": "loot_tables/entities/cat.json"
      },
      "minecraft:scale": {
        "value": 0.8
      }
    }
  }
}
```

**`minecraft:cat_gift_for_owner`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:behavior.drop_item_for": {
        "drop_item_chance": 0.7,
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "player"
            },
            "max_dist": 6
          }
        ],
        "goal_radius": 1.0,
        "loot_table": "loot_tables/entities/cat_gift.json",
        "max_dist": 5,
        "offering_distance": 5,
        "on_drop_attempt": {
          "event": "minecraft:cat_gifted_owner",
          "target": "self"
        },
        "priority": 1,
        "search_count": 0,
        "search_height": 2,
        "search_range": 5,
        "speed_multiplier": 1.0,
        "time_of_day_range": [
          0.74999,
          0.8
        ]
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:behavior.drop_item_for": {
        "cooldown": 0.25,
        "drop_item_chance": 0.7,
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "player"
            },
            "max_dist": 6
          }
        ],
        "goal_radius": 1.0,
        "loot_table": "loot_tables/entities/cat_gift.json",
        "max_head_look_at_height": 10.0,
        "minimum_teleport_distance": 2.0,
        "offering_distance": 5.0,
        "on_drop_attempt": {
          "event": "minecraft:cat_gifted_owner",
          "target": "self"
        },
        "priority": 1,
        "search_count": 0,
        "search_height": 2,
        "search_range": 5,
        "seconds_before_pickup": 0.0,
        "speed_multiplier": 1.0,
        "target_range": [
          5.0,
          5.0,
          5.0
        ],
        "teleport_offset": [
          0.0,
          1.0,
          0.0
        ],
        "time_of_day_range": [
          0.74999,
          0.8
        ]
      }
    }
  }
}
```

**`minecraft:cat_tame`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:behavior.follow_owner": {
        "priority": 4,
        "speed_multiplier": 1.0,
        "start_distance": 10,
        "stop_distance": 2
      },
      "minecraft:behavior.ocelot_sit_on_block": {
        "priority": 7,
        "speed_multiplier": 1.0
      },
      "minecraft:behavior.pet_sleep_with_owner": {
        "goal_radius": 1.0,
        "priority": 2,
        "search_height": 10,
        "search_radius": 10,
        "speed_multiplier": 1.2
      },
      "minecraft:behavior.stay_while_sitting": {
        "priority": 3
      },
      "minecraft:behavior.tempt": {
        "items": [
          "fish",
          "salmon"
        ],
        "priority": 5,
        "speed_multiplier": 0.5,
        "within_radius": 16
      },
      "minecraft:color": {
        "value": 14
      },
      "minecraft:health": {
        "max": 20,
        "value": 20
      },
      "minecraft:is_dyeable": {
        "interact_text": "action.interact.dye"
      },
      "minecraft:is_tamed": {},
      "minecraft:leashable": {
        "hard_distance": 6.0,
        "max_distance": 10.0,
        "soft_distance": 4.0
      },
      "minecraft:on_wake_with_owner": {
        "event": "minecraft:pet_slept_with_owner",
        "target": "self"
      },
      "minecraft:sittable": {},
      "minecraft:type_family": {
        "family": [
          "cat",
          "mob",
          "tamed"
        ]
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:behavior.follow_owner": {
        "priority": 4,
        "speed_multiplier": 1.0,
        "start_distance": 10,
        "stop_distance": 2
      },
      "minecraft:behavior.ocelot_sit_on_block": {
        "priority": 7,
        "speed_multiplier": 1.0
      },
      "minecraft:behavior.pet_sleep_with_owner": {
        "goal_radius": 1.0,
        "priority": 2,
        "search_height": 10,
        "search_radius": 10,
        "speed_multiplier": 1.2
      },
      "minecraft:behavior.stay_while_sitting": {
        "priority": 3
      },
      "minecraft:behavior.tempt": {
        "items": [
          "fish",
          "salmon"
        ],
        "priority": 5,
        "speed_multiplier": 0.5,
        "within_radius": 16
      },
      "minecraft:color": {
        "value": 14
      },
      "minecraft:health": {
        "max": 20,
        "value": 20
      },
      "minecraft:is_dyeable": {
        "interact_text": "action.interact.dye"
      },
      "minecraft:is_tamed": {},
      "minecraft:on_wake_with_owner": {
        "event": "minecraft:pet_slept_with_owner",
        "target": "self"
      },
      "minecraft:sittable": {}
    }
  }
}
```

**`minecraft:cat_wild`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:behavior.avoid_mob_type": {
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "player"
            },
            "max_dist": 10,
            "sprint_speed_multiplier": 1.33,
            "walk_speed_multiplier": 0.8
          }
        ],
        "priority": 6
      },
      "minecraft:behavior.move_towards_restriction": {
        "priority": 7
      },
      "minecraft:behavior.nearest_attackable_target": {
        "attack_interval": 10,
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "rabbit"
            },
            "max_dist": 8
          },
          {
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "baby_turtle"
                },
                {
                  "operator": "!=",
                  "subject": "other",
                  "test": "in_water",
                  "value": true
                }
              ]
            },
            "max_dist": 8
          }
        ],
        "priority": 1,
        "reselect_targets": true,
        "within_radius": 16.0
      },
      "minecraft:behavior.tempt": {
        "can_get_scared": true,
        "items": [
          "fish",
          "salmon"
        ],
        "priority": 5,
        "speed_multiplier": 0.5,
        "within_radius": 16
      },
      "minecraft:health": {
        "max": 10,
        "value": 10
      },
      "minecraft:rideable": {
        "family_types": [
          "zombie"
        ],
        "seat_count": 1,
        "seats": {
          "position": [
            0.0,
            0.35,
            0.0
          ]
        }
      },
      "minecraft:tameable": {
        "probability": 0.33,
        "tame_event": {
          "event": "minecraft:on_tame",
          "target": "self"
        },
        "tame_items": [
          "fish",
          "salmon"
        ]
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:behavior.avoid_mob_type": {
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "player"
            },
            "max_dist": 10,
            "sprint_speed_multiplier": 1.33,
            "walk_speed_multiplier": 0.8
          }
        ],
        "priority": 6
      },
      "minecraft:behavior.move_towards_dwelling_restriction": {
        "priority": 7
      },
      "minecraft:behavior.nearest_attackable_target": {
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "rabbit"
            },
            "max_dist": 8
          },
          {
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "baby_turtle"
                },
                {
                  "operator": "!=",
                  "subject": "other",
                  "test": "in_water",
                  "value": true
                }
              ]
            },
            "max_dist": 8
          }
        ],
        "priority": 1,
        "reselect_targets": true,
        "within_radius": 16.0
      },
      "minecraft:behavior.tempt": {
        "can_get_scared": true,
        "items": [
          "fish",
          "salmon"
        ],
        "priority": 5,
        "speed_multiplier": 0.5,
        "within_radius": 16
      },
      "minecraft:health": {
        "max": 10,
        "value": 10
      },
      "minecraft:rideable": {
        "family_types": [
          "zombie"
        ],
        "seat_count": 1,
        "seats": {
          "position": [
            0.0,
            0.35,
            0.0
          ]
        }
      },
      "minecraft:tameable": {
        "probability": 0.33,
        "tame_event": {
          "event": "minecraft:on_tame",
          "target": "self"
        },
        "tame_items": [
          "fish",
          "salmon"
        ]
      }
    }
  }
}
```

##### `components`

**`minecraft:balloonable`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "mass": 0.6
    }
  }
}
```

**`minecraft:behavior.ocelotattack`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "priority": 4,
      "sneak_speed_multiplier": 0.6,
      "sprint_speed_multiplier": 1.33,
      "walk_speed_multiplier": 0.8
    }
  },
  "reference": {
    "present": true,
    "value": {
      "cooldown_time": 1.0,
      "max_distance": 15.0,
      "max_sneak_range": 15.0,
      "max_sprint_range": 4.0,
      "priority": 4,
      "reach_multiplier": 2.0,
      "sneak_speed_multiplier": 0.6,
      "sprint_speed_multiplier": 1.33,
      "walk_speed_multiplier": 0.8,
      "x_max_rotation": 30.0,
      "y_max_head_rotation": 30.0
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

**`minecraft:leashable`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "hard_distance": 6.0,
      "max_distance": 10.0,
      "soft_distance": 4.0
    }
  }
}
```

##### `root`

**`format_version`**

```json
{
  "addon": {
    "present": true,
    "value": "1.13.0"
  },
  "reference": {
    "present": true,
    "value": "1.18.10"
  }
}
```

## `minecraft:parrot`

### Аддон `2.8.14`

SHA-256 файла: `92d8f706f3f853eb01913a34ade0ae588a9c24aa00bd50ce2c8c113d26585572`.

#### Образец `1.19.40.2`

SHA-256 файла образца: `acd06d3f4fed9366591b3390f6dfa4e3925b80beff3d8bcdb89a2c1465a354cd`.

##### `component_groups`

**`minecraft:parrot_not_riding_player`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:behavior.look_at_player": {
        "look_distance": 8.0,
        "priority": 1
      },
      "minecraft:entity_sensor": {
        "event": "minecraft:on_riding_player",
        "event_filters": {
          "all_of": [
            {
              "operator": "equals",
              "subject": "self",
              "test": "is_riding",
              "value": true
            },
            {
              "operator": "equals",
              "subject": "self",
              "test": "has_component",
              "value": "minecraft:behavior.look_at_player"
            }
          ]
        },
        "relative_range": false,
        "sensor_range": 2.0
      }
    }
  }
}
```

**`minecraft:parrot_riding_player`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:entity_sensor": {
        "event": "minecraft:on_not_riding_player",
        "event_filters": {
          "all_of": [
            {
              "operator": "equals",
              "subject": "self",
              "test": "is_riding",
              "value": false
            },
            {
              "operator": "not",
              "subject": "self",
              "test": "has_component",
              "value": "minecraft:behavior.look_at_player"
            }
          ]
        },
        "relative_range": false,
        "sensor_range": 2.0
      }
    }
  }
}
```

##### `components`

**`minecraft:balloonable`**

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

**`minecraft:behavior.look_at_player`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "look_distance": 8.0,
      "priority": 1
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:behavior.tempt`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "items": [
        "effect:jungle_sword"
      ],
      "speed_multiplier": 1.0
    }
  },
  "reference": {
    "present": false
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

**`minecraft:game_event_movement_tracking`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "emit_flap": true
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

**`minecraft:leashable`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "hard_distance": 6.0,
      "max_distance": 10.0,
      "soft_distance": 4.0
    }
  }
}
```

**`minecraft:navigation.fly`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "can_path_over_water": true
    }
  },
  "reference": {
    "present": true,
    "value": {
      "can_path_from_air": true,
      "can_path_over_water": true
    }
  }
}
```

##### `events`

**`minecraft:entity_spawned`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "randomize": [
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_red",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild"
            ]
          },
          "weight": 20
        },
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_blue",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild"
            ]
          },
          "weight": 20
        },
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_green",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild"
            ]
          },
          "weight": 20
        },
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_cyan",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild"
            ]
          },
          "weight": 20
        },
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_silver",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild"
            ]
          },
          "weight": 20
        }
      ]
    }
  },
  "reference": {
    "present": true,
    "value": {
      "randomize": [
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_red",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild",
              "minecraft:parrot_not_riding_player"
            ]
          },
          "weight": 20
        },
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_blue",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild",
              "minecraft:parrot_not_riding_player"
            ]
          },
          "weight": 20
        },
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_green",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild",
              "minecraft:parrot_not_riding_player"
            ]
          },
          "weight": 20
        },
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_cyan",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild",
              "minecraft:parrot_not_riding_player"
            ]
          },
          "weight": 20
        },
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_silver",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild",
              "minecraft:parrot_not_riding_player"
            ]
          },
          "weight": 20
        }
      ]
    }
  }
}
```

**`minecraft:on_not_riding_player`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:parrot_not_riding_player"
        ]
      },
      "remove": {
        "component_groups": [
          "minecraft:parrot_riding_player"
        ]
      }
    }
  }
}
```

**`minecraft:on_riding_player`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:parrot_riding_player"
        ]
      },
      "remove": {
        "component_groups": [
          "minecraft:parrot_not_riding_player"
        ]
      }
    }
  }
}
```

##### `root`

**`format_version`**

```json
{
  "addon": {
    "present": true,
    "value": "1.13.0"
  },
  "reference": {
    "present": true,
    "value": "1.19.0"
  }
}
```

#### Образец `1.20.30.1`

SHA-256 файла образца: `d2c98d8d76a91de95b791db5a629bc075f6faf5e246ec6a484c0c2b53948a80e`.

##### `component_groups`

**`minecraft:parrot_not_riding_player`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:behavior.look_at_player": {
        "look_distance": 8.0,
        "priority": 1
      },
      "minecraft:entity_sensor": {
        "event": "minecraft:on_riding_player",
        "event_filters": {
          "all_of": [
            {
              "operator": "equals",
              "subject": "self",
              "test": "is_riding",
              "value": true
            },
            {
              "operator": "equals",
              "subject": "self",
              "test": "has_component",
              "value": "minecraft:behavior.look_at_player"
            }
          ]
        },
        "relative_range": false,
        "sensor_range": 2.0
      }
    }
  }
}
```

**`minecraft:parrot_riding_player`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:entity_sensor": {
        "event": "minecraft:on_not_riding_player",
        "event_filters": {
          "all_of": [
            {
              "operator": "equals",
              "subject": "self",
              "test": "is_riding",
              "value": false
            },
            {
              "operator": "not",
              "subject": "self",
              "test": "has_component",
              "value": "minecraft:behavior.look_at_player"
            }
          ]
        },
        "relative_range": false,
        "sensor_range": 2.0
      }
    }
  }
}
```

**`minecraft:parrot_wild`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:behavior.follow_mob": {
        "priority": 3,
        "search_range": 20,
        "speed_multiplier": 1.0,
        "stop_distance": 3
      },
      "minecraft:behavior.random_fly": {
        "avoid_damage_blocks": true,
        "can_land_on_trees": true,
        "priority": 2,
        "speed_multiplier": 1.0,
        "xz_dist": 15,
        "y_dist": 1,
        "y_offset": 0
      },
      "minecraft:tameable": {
        "probability": 0.33,
        "tame_event": {
          "event": "minecraft:on_tame",
          "target": "self"
        },
        "tame_items": [
          "wheat_seeds",
          "pumpkin_seeds",
          "melon_seeds",
          "beetroot_seeds"
        ]
      },
      "minecraft:type_family": {
        "family": [
          "parrot_wild",
          "mob"
        ]
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:behavior.follow_mob": {
        "priority": 3,
        "search_range": 20,
        "speed_multiplier": 1.0,
        "stop_distance": 3
      },
      "minecraft:behavior.random_fly": {
        "avoid_damage_blocks": true,
        "can_land_on_trees": true,
        "priority": 2,
        "speed_multiplier": 1.0,
        "xz_dist": 15,
        "y_dist": 1,
        "y_offset": 0
      },
      "minecraft:tameable": {
        "probability": 0.33,
        "tame_event": {
          "event": "minecraft:on_tame",
          "target": "self"
        },
        "tame_items": [
          "wheat_seeds",
          "pumpkin_seeds",
          "melon_seeds",
          "beetroot_seeds",
          "pitcher_pod",
          "torchflower_seeds"
        ]
      },
      "minecraft:type_family": {
        "family": [
          "parrot_wild",
          "mob"
        ]
      }
    }
  }
}
```

##### `components`

**`minecraft:balloonable`**

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

**`minecraft:behavior.look_at_player`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "look_distance": 8.0,
      "priority": 1
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:behavior.tempt`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "items": [
        "effect:jungle_sword"
      ],
      "speed_multiplier": 1.0
    }
  },
  "reference": {
    "present": false
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

**`minecraft:game_event_movement_tracking`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "emit_flap": true
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

**`minecraft:leashable`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "hard_distance": 6.0,
      "max_distance": 10.0,
      "soft_distance": 4.0
    }
  }
}
```

**`minecraft:navigation.fly`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "can_path_over_water": true
    }
  },
  "reference": {
    "present": true,
    "value": {
      "can_path_from_air": true,
      "can_path_over_water": true
    }
  }
}
```

##### `events`

**`minecraft:entity_spawned`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "randomize": [
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_red",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild"
            ]
          },
          "weight": 20
        },
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_blue",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild"
            ]
          },
          "weight": 20
        },
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_green",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild"
            ]
          },
          "weight": 20
        },
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_cyan",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild"
            ]
          },
          "weight": 20
        },
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_silver",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild"
            ]
          },
          "weight": 20
        }
      ]
    }
  },
  "reference": {
    "present": true,
    "value": {
      "randomize": [
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_red",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild",
              "minecraft:parrot_not_riding_player"
            ]
          },
          "weight": 20
        },
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_blue",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild",
              "minecraft:parrot_not_riding_player"
            ]
          },
          "weight": 20
        },
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_green",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild",
              "minecraft:parrot_not_riding_player"
            ]
          },
          "weight": 20
        },
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_cyan",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild",
              "minecraft:parrot_not_riding_player"
            ]
          },
          "weight": 20
        },
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_silver",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild",
              "minecraft:parrot_not_riding_player"
            ]
          },
          "weight": 20
        }
      ]
    }
  }
}
```

**`minecraft:on_not_riding_player`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:parrot_not_riding_player"
        ]
      },
      "remove": {
        "component_groups": [
          "minecraft:parrot_riding_player"
        ]
      }
    }
  }
}
```

**`minecraft:on_riding_player`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:parrot_riding_player"
        ]
      },
      "remove": {
        "component_groups": [
          "minecraft:parrot_not_riding_player"
        ]
      }
    }
  }
}
```

##### `root`

**`format_version`**

```json
{
  "addon": {
    "present": true,
    "value": "1.13.0"
  },
  "reference": {
    "present": true,
    "value": "1.19.0"
  }
}
```

### Аддон `2.8.8`

SHA-256 файла: `92d8f706f3f853eb01913a34ade0ae588a9c24aa00bd50ce2c8c113d26585572`.

#### Образец `1.19.40.2`

SHA-256 файла образца: `acd06d3f4fed9366591b3390f6dfa4e3925b80beff3d8bcdb89a2c1465a354cd`.

##### `component_groups`

**`minecraft:parrot_not_riding_player`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:behavior.look_at_player": {
        "look_distance": 8.0,
        "priority": 1
      },
      "minecraft:entity_sensor": {
        "event": "minecraft:on_riding_player",
        "event_filters": {
          "all_of": [
            {
              "operator": "equals",
              "subject": "self",
              "test": "is_riding",
              "value": true
            },
            {
              "operator": "equals",
              "subject": "self",
              "test": "has_component",
              "value": "minecraft:behavior.look_at_player"
            }
          ]
        },
        "relative_range": false,
        "sensor_range": 2.0
      }
    }
  }
}
```

**`minecraft:parrot_riding_player`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:entity_sensor": {
        "event": "minecraft:on_not_riding_player",
        "event_filters": {
          "all_of": [
            {
              "operator": "equals",
              "subject": "self",
              "test": "is_riding",
              "value": false
            },
            {
              "operator": "not",
              "subject": "self",
              "test": "has_component",
              "value": "minecraft:behavior.look_at_player"
            }
          ]
        },
        "relative_range": false,
        "sensor_range": 2.0
      }
    }
  }
}
```

##### `components`

**`minecraft:balloonable`**

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

**`minecraft:behavior.look_at_player`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "look_distance": 8.0,
      "priority": 1
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:behavior.tempt`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "items": [
        "effect:jungle_sword"
      ],
      "speed_multiplier": 1.0
    }
  },
  "reference": {
    "present": false
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

**`minecraft:game_event_movement_tracking`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "emit_flap": true
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

**`minecraft:leashable`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "hard_distance": 6.0,
      "max_distance": 10.0,
      "soft_distance": 4.0
    }
  }
}
```

**`minecraft:navigation.fly`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "can_path_over_water": true
    }
  },
  "reference": {
    "present": true,
    "value": {
      "can_path_from_air": true,
      "can_path_over_water": true
    }
  }
}
```

##### `events`

**`minecraft:entity_spawned`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "randomize": [
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_red",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild"
            ]
          },
          "weight": 20
        },
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_blue",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild"
            ]
          },
          "weight": 20
        },
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_green",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild"
            ]
          },
          "weight": 20
        },
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_cyan",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild"
            ]
          },
          "weight": 20
        },
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_silver",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild"
            ]
          },
          "weight": 20
        }
      ]
    }
  },
  "reference": {
    "present": true,
    "value": {
      "randomize": [
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_red",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild",
              "minecraft:parrot_not_riding_player"
            ]
          },
          "weight": 20
        },
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_blue",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild",
              "minecraft:parrot_not_riding_player"
            ]
          },
          "weight": 20
        },
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_green",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild",
              "minecraft:parrot_not_riding_player"
            ]
          },
          "weight": 20
        },
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_cyan",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild",
              "minecraft:parrot_not_riding_player"
            ]
          },
          "weight": 20
        },
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_silver",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild",
              "minecraft:parrot_not_riding_player"
            ]
          },
          "weight": 20
        }
      ]
    }
  }
}
```

**`minecraft:on_not_riding_player`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:parrot_not_riding_player"
        ]
      },
      "remove": {
        "component_groups": [
          "minecraft:parrot_riding_player"
        ]
      }
    }
  }
}
```

**`minecraft:on_riding_player`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:parrot_riding_player"
        ]
      },
      "remove": {
        "component_groups": [
          "minecraft:parrot_not_riding_player"
        ]
      }
    }
  }
}
```

##### `root`

**`format_version`**

```json
{
  "addon": {
    "present": true,
    "value": "1.13.0"
  },
  "reference": {
    "present": true,
    "value": "1.19.0"
  }
}
```

#### Образец `1.20.30.1`

SHA-256 файла образца: `d2c98d8d76a91de95b791db5a629bc075f6faf5e246ec6a484c0c2b53948a80e`.

##### `component_groups`

**`minecraft:parrot_not_riding_player`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:behavior.look_at_player": {
        "look_distance": 8.0,
        "priority": 1
      },
      "minecraft:entity_sensor": {
        "event": "minecraft:on_riding_player",
        "event_filters": {
          "all_of": [
            {
              "operator": "equals",
              "subject": "self",
              "test": "is_riding",
              "value": true
            },
            {
              "operator": "equals",
              "subject": "self",
              "test": "has_component",
              "value": "minecraft:behavior.look_at_player"
            }
          ]
        },
        "relative_range": false,
        "sensor_range": 2.0
      }
    }
  }
}
```

**`minecraft:parrot_riding_player`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:entity_sensor": {
        "event": "minecraft:on_not_riding_player",
        "event_filters": {
          "all_of": [
            {
              "operator": "equals",
              "subject": "self",
              "test": "is_riding",
              "value": false
            },
            {
              "operator": "not",
              "subject": "self",
              "test": "has_component",
              "value": "minecraft:behavior.look_at_player"
            }
          ]
        },
        "relative_range": false,
        "sensor_range": 2.0
      }
    }
  }
}
```

**`minecraft:parrot_wild`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:behavior.follow_mob": {
        "priority": 3,
        "search_range": 20,
        "speed_multiplier": 1.0,
        "stop_distance": 3
      },
      "minecraft:behavior.random_fly": {
        "avoid_damage_blocks": true,
        "can_land_on_trees": true,
        "priority": 2,
        "speed_multiplier": 1.0,
        "xz_dist": 15,
        "y_dist": 1,
        "y_offset": 0
      },
      "minecraft:tameable": {
        "probability": 0.33,
        "tame_event": {
          "event": "minecraft:on_tame",
          "target": "self"
        },
        "tame_items": [
          "wheat_seeds",
          "pumpkin_seeds",
          "melon_seeds",
          "beetroot_seeds"
        ]
      },
      "minecraft:type_family": {
        "family": [
          "parrot_wild",
          "mob"
        ]
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:behavior.follow_mob": {
        "priority": 3,
        "search_range": 20,
        "speed_multiplier": 1.0,
        "stop_distance": 3
      },
      "minecraft:behavior.random_fly": {
        "avoid_damage_blocks": true,
        "can_land_on_trees": true,
        "priority": 2,
        "speed_multiplier": 1.0,
        "xz_dist": 15,
        "y_dist": 1,
        "y_offset": 0
      },
      "minecraft:tameable": {
        "probability": 0.33,
        "tame_event": {
          "event": "minecraft:on_tame",
          "target": "self"
        },
        "tame_items": [
          "wheat_seeds",
          "pumpkin_seeds",
          "melon_seeds",
          "beetroot_seeds",
          "pitcher_pod",
          "torchflower_seeds"
        ]
      },
      "minecraft:type_family": {
        "family": [
          "parrot_wild",
          "mob"
        ]
      }
    }
  }
}
```

##### `components`

**`minecraft:balloonable`**

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

**`minecraft:behavior.look_at_player`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "look_distance": 8.0,
      "priority": 1
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:behavior.tempt`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "items": [
        "effect:jungle_sword"
      ],
      "speed_multiplier": 1.0
    }
  },
  "reference": {
    "present": false
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

**`minecraft:game_event_movement_tracking`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "emit_flap": true
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

**`minecraft:leashable`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "hard_distance": 6.0,
      "max_distance": 10.0,
      "soft_distance": 4.0
    }
  }
}
```

**`minecraft:navigation.fly`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "can_path_over_water": true
    }
  },
  "reference": {
    "present": true,
    "value": {
      "can_path_from_air": true,
      "can_path_over_water": true
    }
  }
}
```

##### `events`

**`minecraft:entity_spawned`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "randomize": [
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_red",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild"
            ]
          },
          "weight": 20
        },
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_blue",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild"
            ]
          },
          "weight": 20
        },
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_green",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild"
            ]
          },
          "weight": 20
        },
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_cyan",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild"
            ]
          },
          "weight": 20
        },
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_silver",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild"
            ]
          },
          "weight": 20
        }
      ]
    }
  },
  "reference": {
    "present": true,
    "value": {
      "randomize": [
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_red",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild",
              "minecraft:parrot_not_riding_player"
            ]
          },
          "weight": 20
        },
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_blue",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild",
              "minecraft:parrot_not_riding_player"
            ]
          },
          "weight": 20
        },
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_green",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild",
              "minecraft:parrot_not_riding_player"
            ]
          },
          "weight": 20
        },
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_cyan",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild",
              "minecraft:parrot_not_riding_player"
            ]
          },
          "weight": 20
        },
        {
          "add": {
            "component_groups": [
              "minecraft:parrot_silver",
              "minecraft:parrot_adult",
              "minecraft:parrot_wild",
              "minecraft:parrot_not_riding_player"
            ]
          },
          "weight": 20
        }
      ]
    }
  }
}
```

**`minecraft:on_not_riding_player`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:parrot_not_riding_player"
        ]
      },
      "remove": {
        "component_groups": [
          "minecraft:parrot_riding_player"
        ]
      }
    }
  }
}
```

**`minecraft:on_riding_player`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:parrot_riding_player"
        ]
      },
      "remove": {
        "component_groups": [
          "minecraft:parrot_not_riding_player"
        ]
      }
    }
  }
}
```

##### `root`

**`format_version`**

```json
{
  "addon": {
    "present": true,
    "value": "1.13.0"
  },
  "reference": {
    "present": true,
    "value": "1.19.0"
  }
}
```

## `minecraft:player`

### Аддон `1.6`

SHA-256 файла: `ec003a118515a8ef9ae5fa3222fe9a618d06a887e24aee4467a0e0c5d908857f`.

#### Образец `1.19.40.2`

SHA-256 файла образца: `e6da0c426bfd839336c7f447101bf29af3d68e420dcab3a493b28ff84d31b8ad`.

##### `component_groups`

**`minecraft:add_bad_omen`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spell_effects": {
        "add_effects": [
          {
            "display_on_screen_animation": true,
            "duration": 6000,
            "effect": "bad_omen"
          }
        ]
      },
      "minecraft:timer": {
        "looping": false,
        "time": [
          0,
          0
        ],
        "time_down_event": {
          "event": "minecraft:clear_add_bad_omen",
          "target": "self"
        }
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:spell_effects": {
        "add_effects": [
          {
            "display_on_screen_animation": true,
            "duration": 6000,
            "effect": "bad_omen",
            "visible": false
          }
        ]
      },
      "minecraft:timer": {
        "looping": false,
        "time": [
          0.0,
          0.0
        ],
        "time_down_event": {
          "event": "minecraft:clear_add_bad_omen",
          "target": "self"
        }
      }
    }
  }
}
```

**`minecraft:blaze_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:blaze"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:bone_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:bone"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:cactus_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:cactus"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:coal_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:coal"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:creeper_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:creeper"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:emerald_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:emerald"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:ender_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:hurt_on_condition": {
        "damage_conditions": [
          {
            "cause": "drowning",
            "damage_per_tick": 1,
            "filters": {
              "operator": "==",
              "test": "in_water_or_rain",
              "value": true
            }
          }
        ]
      },
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:ender"
        }
      ],
      "minecraft:teleport": {
        "light_teleport_chance": 0.05,
        "max_random_teleport_time": 30,
        "random_teleport_cube": [
          32,
          32,
          32
        ],
        "random_teleports": true,
        "target_distance": 16,
        "target_teleport_chance": 0.05
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:fire_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:fire"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:glowstone_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:glow"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:grass_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:grass"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:ice_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:ice"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:jungle_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:jungle"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:lapis_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:lapis"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:lightning_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:lightning"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:magma_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:magma"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:normal_player`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:attack": {
        "damage": 1
      },
      "minecraft:spell_effects": {}
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:obsidian_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:obsidian"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:quartz_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {}
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:sea_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:sea"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:shulker_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:shulker"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:slime_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:slime"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:spectral_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:spectral"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:spider_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:spider"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:sponge_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:sponge"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:sword_of_time`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:time"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:tnt_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:tnt_sword"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:wither_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:wither"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

##### `components`

**`minecraft:attack`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "damage": 1
    }
  }
}
```

**`minecraft:block_climber`**

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

**`minecraft:breathable`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "generatesBubbles": false,
      "inhaleTime": 3.75,
      "suffocateTime": -1,
      "totalSupply": 15
    }
  },
  "reference": {
    "present": true,
    "value": {
      "generates_bubbles": false,
      "inhale_time": 3.75,
      "suffocate_time": -1,
      "total_supply": 15
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

**`minecraft:environment_sensor`**

```json
{
  "addon": {
    "present": true,
    "value": [
      {
        "on_environment": {
          "event": "minecraft:trigger_raid",
          "filters": {
            "all_of": [
              {
                "subject": "self",
                "test": "has_mob_effect",
                "value": "bad_omen"
              },
              {
                "subject": "self",
                "test": "is_in_village",
                "value": true
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:event_normal_player",
          "filters": {
            "all_of": [
              {
                "subject": "self",
                "test": "is_family",
                "value": "player"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:spectral_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:spectral_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:blaze_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:blaze_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:cactus_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:cactus_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:coal_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:coal_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:creeper_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:creeper_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:emerald_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:emerald_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:ender_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:ender_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:fire_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:fire_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:glowstone_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:glowstone_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:grass_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:grass_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:ice_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:ice_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:jungle_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:jungle_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:lapis_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:lapis_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:lightning_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:lightning_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:magma_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:magma_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:obsidian_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:obsidian_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:sea_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:sea_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:shulker_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:shulker_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:slime_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:slime_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:spider_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:spider_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:sponge_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:sponge_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:sword_of_time",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:sword_of_time"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:tnt_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:tnt_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:wither_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:wither_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:bone_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:bone_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:quartz_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:quartz_sword"
              }
            ]
          }
        }
      }
    ]
  },
  "reference": {
    "present": true,
    "value": {
      "triggers": {
        "event": "minecraft:trigger_raid",
        "filters": {
          "all_of": [
            {
              "subject": "self",
              "test": "has_mob_effect",
              "value": "bad_omen"
            },
            {
              "subject": "self",
              "test": "is_in_village",
              "value": true
            }
          ]
        }
      }
    }
  }
}
```

**`minecraft:exhaustion_values`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "attack": 0.1,
      "damage": 0.1,
      "heal": 6,
      "jump": 0.05,
      "mine": 0.005,
      "sprint": 0.1,
      "sprint_jump": 0.2,
      "swim": 0.01,
      "walk": 0.0
    }
  }
}
```

**`minecraft:experience_reward`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "on_death": "Math.Min(query.player_level * 7, 100)"
    }
  }
}
```

**`minecraft:hurt_on_condition`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "damage_conditions": [
        {
          "cause": "lava",
          "damage_per_tick": 4,
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "in_lava",
            "value": true
          }
        }
      ]
    }
  }
}
```

**`minecraft:nameable`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "allowNameTagRenaming": false,
      "alwaysShow": true
    }
  },
  "reference": {
    "present": true,
    "value": {
      "allow_name_tag_renaming": false,
      "always_show": true
    }
  }
}
```

**`minecraft:player.exhaustion`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "max": 4,
      "value": 0
    }
  },
  "reference": {
    "present": true,
    "value": {
      "max": 20,
      "value": 0
    }
  }
}
```

**`minecraft:player.saturation`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "value": 20
    }
  },
  "reference": {
    "present": true,
    "value": {
      "max": 20,
      "value": 5
    }
  }
}
```

**`minecraft:pushable`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "is_pushable": false,
      "is_pushable_by_piston": true
    }
  }
}
```

**`minecraft:rideable`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "family_types": [
        "parrot_tame"
      ],
      "pull_in_entities": true,
      "seat_count": 2,
      "seats": [
        {
          "lock_rider_rotation": 0,
          "max_rider_count": 0,
          "min_rider_count": 0,
          "position": [
            0.4,
            -0.15,
            0.04
          ]
        },
        {
          "lock_rider_rotation": 0,
          "max_rider_count": 2,
          "min_rider_count": 1,
          "position": [
            -0.4,
            -0.15,
            0.04
          ]
        }
      ]
    }
  },
  "reference": {
    "present": true,
    "value": {
      "family_types": [
        "parrot_tame"
      ],
      "pull_in_entities": true,
      "seat_count": 2,
      "seats": [
        {
          "lock_rider_rotation": 0,
          "max_rider_count": 0,
          "min_rider_count": 0,
          "position": [
            0.4,
            -0.2,
            -0.1
          ]
        },
        {
          "lock_rider_rotation": 0,
          "max_rider_count": 2,
          "min_rider_count": 1,
          "position": [
            -0.4,
            -0.2,
            -0.1
          ]
        }
      ]
    }
  }
}
```

**`minecraft:scaffolding_climber`**

```json
{
  "addon": {
    "present": true,
    "value": {}
  },
  "reference": {
    "present": false
  }
}
```

##### `description`

**`animations`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "normal": "controller.animation.normal"
    }
  },
  "reference": {
    "present": false
  }
}
```

**`scripts`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "animate": [
        "normal"
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

##### `events`

**`minecraft:blaze_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:blaze_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:bone_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:bone_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:cactus_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:cactus_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:coal_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:coal_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:creeper_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:creeper_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:emerald_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:emerald_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:ender_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:ender_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:event_normal_player`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:normal_player"
        ]
      },
      "remove": {
        "component_groups": [
          "minecraft:spectral_sword",
          "minecraft:blaze_sword",
          "minecraft:cactus_sword",
          "minecraft:coal_sword",
          "minecraft:creeper_sword",
          "minecraft:emerald_sword",
          "minecraft:ender_sword",
          "minecraft:fire_sword",
          "minecraft:glowstone_sword",
          "minecraft:grass_sword",
          "minecraft:ice_sword",
          "minecraft:jungle_sword",
          "minecraft:lapis_sword",
          "minecraft:lightning_sword",
          "minecraft:magma_sword",
          "minecraft:obsidian_sword",
          "minecraft:sea_sword",
          "minecraft:shulker_sword",
          "minecraft:slime_sword",
          "minecraft:spider_sword",
          "minecraft:sponge_sword",
          "minecraft:sword_of_time",
          "minecraft:tnt_sword",
          "minecraft:wither_sword",
          "minecraft:bone_sword",
          "minecraft:quartz_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:fire_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:fire_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:glowstone_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:glowstone_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:grass_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:grass_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:ice_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:ice_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:jungle_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:jungle_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:lapis_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:lapis_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:lightning_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:lightning_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:magma_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:magma_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:obsidian_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:obsidian_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:quartz_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:quartz_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:sea_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:sea_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:shulker_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:shulker_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:slime_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:slime_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:spectral_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:spectral_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:spider_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:spider_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:sponge_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:sponge_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:sword_of_time`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:sword_of_time"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:tnt_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:tnt_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:wither_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:wither_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

##### `root`

**`format_version`**

```json
{
  "addon": {
    "present": true,
    "value": "1.11.0"
  },
  "reference": {
    "present": true,
    "value": "1.18.20"
  }
}
```

#### Образец `1.20.30.1`

SHA-256 файла образца: `0ad825e9433490dda6fa9d51eb0eaf4aaf1e7e510559f7cb0ceded5822ebc155`.

##### `component_groups`

**`minecraft:add_bad_omen`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spell_effects": {
        "add_effects": [
          {
            "display_on_screen_animation": true,
            "duration": 6000,
            "effect": "bad_omen"
          }
        ]
      },
      "minecraft:timer": {
        "looping": false,
        "time": [
          0,
          0
        ],
        "time_down_event": {
          "event": "minecraft:clear_add_bad_omen",
          "target": "self"
        }
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:spell_effects": {
        "add_effects": [
          {
            "display_on_screen_animation": true,
            "duration": 6000,
            "effect": "bad_omen",
            "visible": false
          }
        ]
      },
      "minecraft:timer": {
        "looping": false,
        "time": [
          0.0,
          0.0
        ],
        "time_down_event": {
          "event": "minecraft:clear_add_bad_omen",
          "target": "self"
        }
      }
    }
  }
}
```

**`minecraft:blaze_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:blaze"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:bone_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:bone"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:cactus_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:cactus"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:coal_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:coal"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:creeper_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:creeper"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:emerald_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:emerald"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:ender_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:hurt_on_condition": {
        "damage_conditions": [
          {
            "cause": "drowning",
            "damage_per_tick": 1,
            "filters": {
              "operator": "==",
              "test": "in_water_or_rain",
              "value": true
            }
          }
        ]
      },
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:ender"
        }
      ],
      "minecraft:teleport": {
        "light_teleport_chance": 0.05,
        "max_random_teleport_time": 30,
        "random_teleport_cube": [
          32,
          32,
          32
        ],
        "random_teleports": true,
        "target_distance": 16,
        "target_teleport_chance": 0.05
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:fire_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:fire"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:glowstone_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:glow"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:grass_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:grass"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:ice_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:ice"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:jungle_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:jungle"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:lapis_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:lapis"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:lightning_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:lightning"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:magma_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:magma"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:normal_player`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:attack": {
        "damage": 1
      },
      "minecraft:spell_effects": {}
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:obsidian_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:obsidian"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:quartz_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {}
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:sea_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:sea"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:shulker_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:shulker"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:slime_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:slime"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:spectral_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:spectral"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:spider_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:spider"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:sponge_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:sponge"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:sword_of_time`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:time"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:tnt_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:tnt_sword"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:wither_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:wither"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

##### `components`

**`minecraft:attack`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "damage": 1
    }
  }
}
```

**`minecraft:block_climber`**

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

**`minecraft:breathable`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "generatesBubbles": false,
      "inhaleTime": 3.75,
      "suffocateTime": -1,
      "totalSupply": 15
    }
  },
  "reference": {
    "present": true,
    "value": {
      "generates_bubbles": false,
      "inhale_time": 3.75,
      "suffocate_time": -1,
      "total_supply": 15
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

**`minecraft:environment_sensor`**

```json
{
  "addon": {
    "present": true,
    "value": [
      {
        "on_environment": {
          "event": "minecraft:trigger_raid",
          "filters": {
            "all_of": [
              {
                "subject": "self",
                "test": "has_mob_effect",
                "value": "bad_omen"
              },
              {
                "subject": "self",
                "test": "is_in_village",
                "value": true
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:event_normal_player",
          "filters": {
            "all_of": [
              {
                "subject": "self",
                "test": "is_family",
                "value": "player"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:spectral_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:spectral_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:blaze_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:blaze_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:cactus_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:cactus_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:coal_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:coal_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:creeper_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:creeper_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:emerald_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:emerald_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:ender_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:ender_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:fire_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:fire_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:glowstone_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:glowstone_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:grass_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:grass_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:ice_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:ice_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:jungle_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:jungle_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:lapis_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:lapis_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:lightning_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:lightning_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:magma_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:magma_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:obsidian_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:obsidian_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:sea_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:sea_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:shulker_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:shulker_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:slime_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:slime_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:spider_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:spider_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:sponge_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:sponge_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:sword_of_time",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:sword_of_time"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:tnt_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:tnt_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:wither_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:wither_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:bone_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:bone_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:quartz_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:quartz_sword"
              }
            ]
          }
        }
      }
    ]
  },
  "reference": {
    "present": true,
    "value": {
      "triggers": {
        "event": "minecraft:trigger_raid",
        "filters": {
          "all_of": [
            {
              "subject": "self",
              "test": "has_mob_effect",
              "value": "bad_omen"
            },
            {
              "subject": "self",
              "test": "is_in_village",
              "value": true
            }
          ]
        }
      }
    }
  }
}
```

**`minecraft:exhaustion_values`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "attack": 0.1,
      "damage": 0.1,
      "heal": 6,
      "jump": 0.05,
      "mine": 0.005,
      "sprint": 0.1,
      "sprint_jump": 0.2,
      "swim": 0.01,
      "walk": 0.0
    }
  }
}
```

**`minecraft:experience_reward`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "on_death": "Math.Min(query.player_level * 7, 100)"
    }
  }
}
```

**`minecraft:hurt_on_condition`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "damage_conditions": [
        {
          "cause": "lava",
          "damage_per_tick": 4,
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "in_lava",
            "value": true
          }
        }
      ]
    }
  }
}
```

**`minecraft:nameable`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "allowNameTagRenaming": false,
      "alwaysShow": true
    }
  },
  "reference": {
    "present": true,
    "value": {
      "allow_name_tag_renaming": false,
      "always_show": true
    }
  }
}
```

**`minecraft:physics`**

```json
{
  "addon": {
    "present": true,
    "value": {}
  },
  "reference": {
    "present": true,
    "value": {
      "push_towards_closest_space": true
    }
  }
}
```

**`minecraft:player.exhaustion`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "max": 4,
      "value": 0
    }
  },
  "reference": {
    "present": true,
    "value": {
      "max": 20,
      "value": 0
    }
  }
}
```

**`minecraft:player.saturation`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "value": 20
    }
  },
  "reference": {
    "present": true,
    "value": {
      "max": 20,
      "value": 5
    }
  }
}
```

**`minecraft:pushable`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "is_pushable": false,
      "is_pushable_by_piston": true
    }
  }
}
```

**`minecraft:rideable`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "family_types": [
        "parrot_tame"
      ],
      "pull_in_entities": true,
      "seat_count": 2,
      "seats": [
        {
          "lock_rider_rotation": 0,
          "max_rider_count": 0,
          "min_rider_count": 0,
          "position": [
            0.4,
            -0.15,
            0.04
          ]
        },
        {
          "lock_rider_rotation": 0,
          "max_rider_count": 2,
          "min_rider_count": 1,
          "position": [
            -0.4,
            -0.15,
            0.04
          ]
        }
      ]
    }
  },
  "reference": {
    "present": true,
    "value": {
      "family_types": [
        "parrot_tame"
      ],
      "pull_in_entities": true,
      "seat_count": 2,
      "seats": [
        {
          "lock_rider_rotation": 0,
          "max_rider_count": 0,
          "min_rider_count": 0,
          "position": [
            0.4,
            -0.2,
            -0.1
          ]
        },
        {
          "lock_rider_rotation": 0,
          "max_rider_count": 2,
          "min_rider_count": 1,
          "position": [
            -0.4,
            -0.2,
            -0.1
          ]
        }
      ]
    }
  }
}
```

**`minecraft:scaffolding_climber`**

```json
{
  "addon": {
    "present": true,
    "value": {}
  },
  "reference": {
    "present": false
  }
}
```

##### `description`

**`animations`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "normal": "controller.animation.normal"
    }
  },
  "reference": {
    "present": false
  }
}
```

**`scripts`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "animate": [
        "normal"
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

##### `events`

**`minecraft:blaze_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:blaze_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:bone_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:bone_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:cactus_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:cactus_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:coal_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:coal_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:creeper_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:creeper_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:emerald_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:emerald_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:ender_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:ender_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:event_normal_player`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:normal_player"
        ]
      },
      "remove": {
        "component_groups": [
          "minecraft:spectral_sword",
          "minecraft:blaze_sword",
          "minecraft:cactus_sword",
          "minecraft:coal_sword",
          "minecraft:creeper_sword",
          "minecraft:emerald_sword",
          "minecraft:ender_sword",
          "minecraft:fire_sword",
          "minecraft:glowstone_sword",
          "minecraft:grass_sword",
          "minecraft:ice_sword",
          "minecraft:jungle_sword",
          "minecraft:lapis_sword",
          "minecraft:lightning_sword",
          "minecraft:magma_sword",
          "minecraft:obsidian_sword",
          "minecraft:sea_sword",
          "minecraft:shulker_sword",
          "minecraft:slime_sword",
          "minecraft:spider_sword",
          "minecraft:sponge_sword",
          "minecraft:sword_of_time",
          "minecraft:tnt_sword",
          "minecraft:wither_sword",
          "minecraft:bone_sword",
          "minecraft:quartz_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:fire_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:fire_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:glowstone_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:glowstone_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:grass_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:grass_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:ice_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:ice_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:jungle_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:jungle_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:lapis_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:lapis_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:lightning_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:lightning_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:magma_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:magma_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:obsidian_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:obsidian_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:quartz_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:quartz_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:sea_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:sea_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:shulker_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:shulker_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:slime_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:slime_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:spectral_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:spectral_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:spider_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:spider_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:sponge_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:sponge_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:sword_of_time`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:sword_of_time"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:tnt_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:tnt_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:wither_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:wither_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

##### `root`

**`format_version`**

```json
{
  "addon": {
    "present": true,
    "value": "1.11.0"
  },
  "reference": {
    "present": true,
    "value": "1.18.20"
  }
}
```

### Аддон `2.8.14`

SHA-256 файла: `d25d5fe1e885ef35c4027cc25290950b814b96e48a3a211b87bdabc77df2000f`.

#### Образец `1.19.40.2`

SHA-256 файла образца: `e6da0c426bfd839336c7f447101bf29af3d68e420dcab3a493b28ff84d31b8ad`.

##### `component_groups`

**`blaze_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:timer": {
        "looping": false,
        "time": [
          6,
          6
        ],
        "time_down_event": {
          "event": "blaze_sword_skill",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "blaze_sword",
          "blaze_sword_skill"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`clock_sword_movement`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:movement": {
        "value": 1
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`clock_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:timer": {
        "looping": true,
        "randomInterval": false,
        "time": [
          5,
          5
        ],
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`complete_wolf_transformation`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:attack": {
        "damage": 15
      },
      "minecraft:damage_sensor": {
        "triggers": [
          {
            "deals_damage": true,
            "on_damage": {
              "event": "wolf_damage_sound",
              "filters": {
                "all_of": [
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "void"
                  }
                ]
              }
            }
          }
        ]
      },
      "minecraft:timer": {
        "looping": true,
        "randomInterval": true,
        "time": [
          3,
          6
        ],
        "time_down_event": {
          "event": "wolf_sword_sounds",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "wolf",
          "wolf_sword",
          "complete_wolf_transformation",
          "monster"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`despawn`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:despawn": {}
    }
  },
  "reference": {
    "present": false
  }
}
```

**`ghost_movement`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:movement": {
        "value": 0.14
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`mermaid_movement_in_water`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:underwater_movement": {
        "value": 0.07
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`mermaid_movement_out_water`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:movement": {
        "value": 0.06
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:add_bad_omen`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spell_effects": {
        "add_effects": [
          {
            "display_on_screen_animation": true,
            "duration": 6000,
            "effect": "bad_omen"
          }
        ]
      },
      "minecraft:timer": {
        "looping": false,
        "time": [
          0.0,
          0.0
        ],
        "time_down_event": {
          "event": "minecraft:clear_add_bad_omen",
          "target": "self"
        }
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:spell_effects": {
        "add_effects": [
          {
            "display_on_screen_animation": true,
            "duration": 6000,
            "effect": "bad_omen",
            "visible": false
          }
        ]
      },
      "minecraft:timer": {
        "looping": false,
        "time": [
          0.0,
          0.0
        ],
        "time_down_event": {
          "event": "minecraft:clear_add_bad_omen",
          "target": "self"
        }
      }
    }
  }
}
```

**`minecraft:bee_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:timer": {
        "looping": true,
        "randomInterval": true,
        "time": [
          3,
          8
        ],
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
  "reference": {
    "present": false
  }
}
```

**`minecraft:blaze_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": false,
          "on_damage": {
            "filters": {
              "any_of": [
                {
                  "subject": "self",
                  "test": "has_damage",
                  "value": "fire"
                },
                {
                  "subject": "self",
                  "test": "has_damage",
                  "value": "fire_tick"
                }
              ]
            }
          }
        }
      },
      "minecraft:hurt_on_condition": {
        "damage_conditions": [
          {
            "cause": "drowning",
            "damage_per_tick": 1,
            "filters": {
              "test": "in_water_or_rain"
            }
          }
        ]
      },
      "minecraft:timer": {
        "looping": true,
        "time": [
          1,
          1
        ],
        "time_down_event": {
          "event": "blaze_sword_effects",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "blaze_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:bone_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:timer": {
        "looping": true,
        "time": [
          1,
          1
        ],
        "time_down_event": {
          "event": "bone_sword_skills",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "bone_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:cactus_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:timer": {
        "looping": true,
        "time": [
          0.5,
          0.5
        ],
        "time_down_event": {
          "event": "cactus_sword_skills",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "cactus_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:clock_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:type_family": {
        "family": [
          "player",
          "clock_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:default_player`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:attack": {
        "damage": 1
      },
      "minecraft:breathable": {
        "generates_bubbles": false,
        "inhale_time": 3.75,
        "suffocate_time": -1,
        "total_supply": 15
      },
      "minecraft:collision_box": {
        "height": 1.8,
        "width": 0.6
      },
      "minecraft:damage_sensor": {},
      "minecraft:health": {
        "max": 20,
        "value": 20
      },
      "minecraft:movement": {
        "value": 0.1
      },
      "minecraft:physics": {
        "has_collision": true,
        "has_gravity": true
      },
      "minecraft:rideable": {
        "family_types": [
          "parrot_tame"
        ],
        "pull_in_entities": true,
        "seat_count": 2,
        "seats": [
          {
            "lock_rider_rotation": 0,
            "max_rider_count": 0,
            "min_rider_count": 0,
            "position": [
              0.4,
              -0.2,
              -0.1
            ]
          },
          {
            "lock_rider_rotation": 0,
            "max_rider_count": 2,
            "min_rider_count": 1,
            "position": [
              -0.4,
              -0.2,
              -0.1
            ]
          }
        ]
      },
      "minecraft:scale": {
        "value": 1
      },
      "minecraft:timer": {},
      "minecraft:type_family": {
        "family": [
          "player",
          "default_player"
        ]
      },
      "minecraft:underwater_movement": {
        "value": 0.02
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:emerald_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:type_family": {
        "family": [
          "player",
          "emerald_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:ender_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": [
          {
            "deals_damage": true,
            "on_damage": {
              "event": "ender_sword_skill",
              "filters": {
                "all_of": [
                  {
                    "operator": "!=",
                    "subject": "self",
                    "test": "has_damage",
                    "value": "projectile"
                  }
                ]
              }
            }
          },
          {
            "deals_damage": false,
            "on_damage": {
              "event": "ender_sword_tp",
              "filters": {
                "all_of": [
                  {
                    "subject": "self",
                    "test": "has_damage",
                    "value": "projectile"
                  }
                ]
              }
            }
          },
          {
            "deals_damage": true,
            "on_damage": {
              "event": "ender_sword_tp",
              "filters": {
                "all_of": [
                  {
                    "test": "in_water_or_rain"
                  }
                ]
              }
            }
          }
        ]
      },
      "minecraft:hurt_on_condition": {
        "damage_conditions": [
          {
            "cause": "drowning",
            "damage_per_tick": 1,
            "filters": {
              "test": "in_water_or_rain"
            }
          }
        ]
      },
      "minecraft:timer": {
        "looping": true,
        "randomInterval": true,
        "time": [
          6,
          18
        ],
        "time_down_event": {
          "event": "ender_sword_sound",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "ender_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:fire_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": false,
          "on_damage": {
            "filters": {
              "any_of": [
                {
                  "subject": "self",
                  "test": "has_damage",
                  "value": "fire"
                },
                {
                  "subject": "self",
                  "test": "has_damage",
                  "value": "fire_tick"
                }
              ]
            }
          }
        }
      },
      "minecraft:timer": {
        "looping": true,
        "randomInterval": true,
        "time": [
          0.2,
          0.7
        ],
        "time_down_event": {
          "event": "fire_sword_sound",
          "target": "self"
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
  "reference": {
    "present": false
  }
}
```

**`minecraft:ghost_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:breathable": {
        "breathes_air": true,
        "breathes_lava": true,
        "breathes_water": true,
        "generates_bubbles": false,
        "inhale_time": 3.75,
        "suffocate_time": 0,
        "total_supply": 15
      },
      "minecraft:collision_box": {
        "height": 0.0,
        "width": 0.0
      },
      "minecraft:damage_sensor": {
        "triggers": {
          "cause": "all",
          "deals_damage": false
        }
      },
      "minecraft:knockback_resistance": {
        "value": 1.0
      },
      "minecraft:scale": {
        "value": 1.05
      },
      "minecraft:type_family": {
        "family": [
          "ghost_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:grass_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:timer": {
        "looping": true,
        "time": [
          0.2,
          0.2
        ],
        "time_down_event": {
          "event": "grass_sword_skills",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "grass_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:ice_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:type_family": {
        "family": [
          "player",
          "ice_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:jungle_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:health": {
        "max": 8,
        "value": 8
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "jungle_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:lapis_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:timer": {
        "looping": true,
        "randomInterval": true,
        "time": [
          2.5,
          6.0
        ],
        "time_down_event": {
          "event": "lapis_sword_skills",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "lapis_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:lightning_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": false,
          "on_damage": {
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "lightning"
                }
              ]
            }
          }
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
  "reference": {
    "present": false
  }
}
```

**`minecraft:magma_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": false,
          "on_damage": {
            "filters": {
              "any_of": [
                {
                  "subject": "self",
                  "test": "has_damage",
                  "value": "fire_tick"
                },
                {
                  "operator": "equals",
                  "subject": "block",
                  "test": "is_block",
                  "value": "magma"
                }
              ]
            }
          }
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
  "reference": {
    "present": false
  }
}
```

**`minecraft:nether_star_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": false,
          "on_damage": {
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "nether_star_projectile"
                }
              ]
            }
          }
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
  "reference": {
    "present": false
  }
}
```

**`minecraft:obsidian_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": false,
          "on_damage": {
            "filters": {
              "any_of": [
                {
                  "subject": "self",
                  "test": "has_damage",
                  "value": "block_explosion"
                },
                {
                  "subject": "self",
                  "test": "has_damage",
                  "value": "entity_explosion"
                }
              ]
            }
          }
        }
      },
      "minecraft:knockback_resistance": {
        "value": 1.0
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "obsidian_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:quartz_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:type_family": {
        "family": [
          "player",
          "quartz_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:sea_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:breathable": {
        "breathes_air": false,
        "breathes_lava": false,
        "breathes_water": true,
        "generates_bubbles": false,
        "inhale_time": 3.75,
        "suffocate_time": -1,
        "total_supply": 2
      },
      "minecraft:collision_box": {
        "height": 0.9,
        "width": 0.6
      },
      "minecraft:timer": {
        "looping": true,
        "time": [
          0.5,
          0.5
        ],
        "time_down_event": {
          "event": "sea_sword_sound",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "sea_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:shulker_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:scale": {
        "value": 1
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "shulker_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:slime_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": false,
          "on_damage": {
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "tamed_slime"
                }
              ]
            }
          }
        }
      },
      "minecraft:timer": {
        "looping": false,
        "time": [
          0.4,
          0.4
        ],
        "time_down_event": {
          "event": "slime_sword_skills",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "slime_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:spectral_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:rideable": {
        "family_types": [
          "ender_crystal",
          "spectral_sword"
        ],
        "seat_count": 1,
        "seats": {
          "lock_rider_rotation": 0,
          "position": [
            0.0,
            0.4,
            0.0
          ]
        }
      },
      "minecraft:timer": {
        "looping": false,
        "time": [
          0.4,
          0.4
        ],
        "time_down_event": {
          "event": "spectral_sword_skills",
          "target": "self"
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
  "reference": {
    "present": false
  }
}
```

**`minecraft:spider_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:type_family": {
        "family": [
          "player",
          "spider_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:sponge_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:type_family": {
        "family": [
          "player",
          "sponge_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:time_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:movement": {
        "value": 1
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "time_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:ultra_instinct_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": [
          {
            "deals_damage": false,
            "on_damage": {
              "event": "ultra_instinct_sword_skill",
              "filters": {
                "all_of": [
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "lava"
                  },
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "drowning"
                  },
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "void"
                  },
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "thorns"
                  },
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "suicide"
                  },
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "starve"
                  },
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "fire"
                  },
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "fire_tick"
                  },
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "magic"
                  }
                ]
              }
            }
          },
          {
            "deals_damage": false,
            "on_damage": {
              "filters": {
                "test": "has_damage",
                "value": "fire"
              }
            }
          },
          {
            "deals_damage": false,
            "on_damage": {
              "filters": {
                "test": "has_damage",
                "value": "fire_tick"
              }
            }
          },
          {
            "deals_damage": false,
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
            }
          },
          {
            "deals_damage": true,
            "on_damage": {
              "filters": {
                "all_of": [
                  {
                    "test": "has_damage",
                    "value": "lava"
                  }
                ]
              }
            }
          }
        ]
      },
      "minecraft:knockback_resistance": {
        "value": 1.0
      },
      "minecraft:timer": {
        "looping": true,
        "randomInterval": true,
        "time": [
          0.1,
          0.2
        ],
        "time_down_event": {
          "event": "ultra_instinct_sword_effects",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "ultra_instinct_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:wither_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": false,
          "on_damage": {
            "filters": {
              "all_of": [
                {
                  "subject": "self",
                  "test": "has_damage",
                  "value": "wither"
                }
              ]
            }
          }
        }
      },
      "minecraft:rideable": {
        "family_types": [
          "entity_name"
        ],
        "seat_count": 1,
        "seats": {
          "lock_rider_rotation": 0,
          "position": [
            0.0,
            0.4,
            0.0
          ]
        }
      },
      "minecraft:timer": {
        "looping": true,
        "randomInterval": true,
        "time": [
          4,
          18
        ],
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
  "reference": {
    "present": false
  }
}
```

**`minecraft:wolf_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:type_family": {
        "family": [
          "player",
          "wolf_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`shoot_small_fireball`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 1,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:fake_fireball",
          "spawn_event": "set_sound"
        },
        {
          "max_wait_time": 1,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:fake_fireball",
          "spawn_event": "set_sound"
        },
        {
          "max_wait_time": 1,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:fake_fireball",
          "spawn_event": "set_sound"
        },
        {
          "max_wait_time": 1,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:fake_fireball",
          "spawn_event": "set_sound"
        }
      ],
      "minecraft:timer": {
        "looping": false,
        "time": [
          2,
          2
        ],
        "time_down_event": {
          "event": "stop_blaze_sword_skill",
          "target": "self"
        }
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`shulker_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
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
  "reference": {
    "present": false
  }
}
```

**`spider_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": false,
          "spawn_entity": "entity:web"
        }
      ],
      "minecraft:timer": {
        "looping": false,
        "time": [
          2,
          2
        ],
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
  "reference": {
    "present": false
  }
}
```

**`start_player_explode_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:movement": {
        "value": 0.0
      },
      "minecraft:timer": {
        "looping": true,
        "time": [
          1.5,
          1.5
        ],
        "time_down_event": {
          "event": "start_player_explode",
          "target": "self"
        }
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`time_sword_movement`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:movement": {
        "value": 1
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`ultra_instinct_projectile`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:ultra_instinct_projectile"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`ultra_instinct_sword_movement`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:movement": {
        "value": 0.22
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`wolf_movement`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:movement": {
        "value": 0.18
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`wolf_transformation`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:type_family": {
        "family": [
          "player",
          "wolf_sword",
          "wolf_transformation"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

##### `components`

**`minecraft:block_climber`**

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

**`minecraft:environment_sensor`**

```json
{
  "addon": {
    "present": true,
    "value": [
      {
        "on_environment": {
          "event": "minecraft:trigger_raid",
          "filters": {
            "all_of": [
              {
                "subject": "self",
                "test": "has_mob_effect",
                "value": "bad_omen"
              },
              {
                "subject": "self",
                "test": "is_in_village",
                "value": true
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:constant_events",
          "filters": {
            "operator": "!=",
            "test": "is_family",
            "value": "null"
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:stop_sword_events",
          "filters": {
            "any_of": [
              {
                "subject": "self",
                "test": "is_family",
                "value": "default_player"
              },
              {
                "operator": "!=",
                "subject": "self",
                "test": "is_family",
                "value": "spectral_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:blaze_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:blaze_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_blaze_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:blaze_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:bone_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:bone_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_bone_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:bone_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:cactus_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:cactus_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_cactus_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:cactus_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:emerald_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:emerald_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_emerald_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:emerald_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:fire_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:fire_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_fire_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:fire_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:grass_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:grass_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_grass_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:grass_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:jungle_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:jungle_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_jungle_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:jungle_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:magma_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:magma_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_magma_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:magma_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:ice_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:ice_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_ice_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:ice_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:lapis_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:lapis_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_lapis_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:lapis_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:obsidian_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:obsidian_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_obsidian_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:obsidian_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:quartz_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:quartz_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_quartz_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:quartz_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:sea_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:sea_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_sea_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:sea_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:spectral_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:spectral_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_spectral_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:spectral_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:slime_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:slime_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_slime_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:slime_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:shulker_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:shulker_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_shulker_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:shulker_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:spider_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:spider_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_spider_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:spider_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:sponge_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:sponge_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_sponge_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:sponge_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:time_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:time_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_time_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:time_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:wither_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:wither_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_wither_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:wither_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:glowstone_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:glowstone_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:lightning_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:lightning_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_lightning_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:lightning_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:ender_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:ender_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_ender_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:ender_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:ultra_instinct_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:ultra_instinct_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_ultra_instinct_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:ultra_instinct_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:wolf_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:wolf_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_wolf_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:wolf_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "starting_wolf_transformation",
          "filters": {
            "all_of": [
              {
                "test": "is_family",
                "value": "wolf_transformation"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "wolf_movement",
          "filters": {
            "all_of": [
              {
                "test": "is_family",
                "value": "complete_wolf_transformation"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:ghost_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:ghost_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_ghost_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:ghost_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:clock_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:clock_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_clock_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:clock_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:nether_star_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:nether_star_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_nether_star_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:nether_star_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:bee_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:bee_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_bee_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:bee_sword"
              }
            ]
          }
        }
      }
    ]
  },
  "reference": {
    "present": true,
    "value": {
      "triggers": {
        "event": "minecraft:trigger_raid",
        "filters": {
          "all_of": [
            {
              "subject": "self",
              "test": "has_mob_effect",
              "value": "bad_omen"
            },
            {
              "subject": "self",
              "test": "is_in_village",
              "value": true
            }
          ]
        }
      }
    }
  }
}
```

**`minecraft:exhaustion_values`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "attack": 0.1,
      "damage": 0.1,
      "heal": 6,
      "jump": 0.05,
      "mine": 0.005,
      "sprint": 0.1,
      "sprint_jump": 0.2,
      "swim": 0.01,
      "walk": 0.0
    }
  }
}
```

**`minecraft:player.exhaustion`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "max": 4,
      "value": 0
    }
  },
  "reference": {
    "present": true,
    "value": {
      "max": 20,
      "value": 0
    }
  }
}
```

**`minecraft:player.saturation`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "value": 20
    }
  },
  "reference": {
    "present": true,
    "value": {
      "max": 20,
      "value": 5
    }
  }
}
```

**`minecraft:scaffolding_climber`**

```json
{
  "addon": {
    "present": true,
    "value": {}
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:type_family`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "family": [
        "player",
        "default_player"
      ]
    }
  },
  "reference": {
    "present": true,
    "value": {
      "family": [
        "player"
      ]
    }
  }
}
```

##### `description`

**`animations`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "ghost_sword": "controller.animation.ghost_sword",
      "shulker_sword": "controller.animation.shulker_sword",
      "wither_sword": "controller.animation.wither_sword",
      "wolf_sword_0": "controller.animation.wolf_sword",
      "wolf_sword_1": "controller.animation.start_wolf_sword",
      "wolf_sword_2": "controller.animation.end_wolf_sword"
    }
  },
  "reference": {
    "present": false
  }
}
```

**`scripts`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "animate": [
        "shulker_sword",
        "wither_sword",
        "wolf_sword_0",
        "wolf_sword_1",
        "wolf_sword_2",
        "ghost_sword"
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

##### `events`

**`bee_sword_flower`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "randomize": [
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 0"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 1"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 2"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 4"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 5"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 6"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 7"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 8"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 9"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 10"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ yellow_flower 0"
            ]
          },
          "weight": 1
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`blaze_sword_effects`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "randomize": [
        {
          "run_command": {
            "command": [
              "particle minecraft:mobflame_single ~ ~0.2 ~"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:mobflame_single ~0.3 ~0.2 ~"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:mobflame_single ~ ~0.2 ~0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:mobflame_single ~-0.3 ~0.2 ~"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:mobflame_single ~ ~0.2 ~-0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "playsound mob.blaze.breathe @a[r=12] ~ ~ ~ 0.5"
            ]
          },
          "weight": 1
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`blaze_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "shoot_small_fireball"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`blaze_sword_skill_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "blaze_sword_skill"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`bone_sword_skills`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "summon entity:grows_crop ~ ~0.1 ~ grows_crop_event"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`cactus_sword_skills`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "damage @e[r=1.4,type=!player] 1 contact entity @s",
          "damage @s 1 contact"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`clock_sword_movement`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "clock_sword_movement"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`clock_sword_skill_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "clock_sword_skill"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`default_player`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:default_player"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`despawn`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "despawn"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`ender_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
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
              "run_command": {
                "command": [
                  "spreadplayers ~ ~ 0 16 @s",
                  "playsound mob.endermen.portal @a[r=17]"
                ]
              },
              "weight": 50
            }
          ]
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`ender_sword_sound`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "randomize": [
        {
          "run_command": {
            "command": [
              "playsound mob.endermen.scream @a[r=8] ~ ~ ~"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "playsound mob.endermen.idle @a[r=8] ~ ~ ~"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "playsound mob.endermen.stare @a[r=8] ~ ~ ~"
            ]
          },
          "weight": 1
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`ender_sword_tp`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "spreadplayers ~ ~ 0 16 @s",
          "playsound mob.endermen.portal @a[r=17]"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`fire_sword_sound`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "playsound fire.fire @a[r=8]"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`grass_sword_skills`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "execute @e[type=!player,type=!item,type=!entity:grass,type=!xp_orb,type=!arrow,r=8,tag=!grass] ~ ~ ~ detect ~ ~-0.1 ~ grass 0 execute @s ~ ~ ~ detect ~ ~ ~ air 0 summon entity:grass",
          "execute @e[type=!player,type=!item,type=!entity:grass,type=!xp_orb,type=!arrow,r=8,tag=!grass] ~ ~ ~ detect ~ ~-0.1 ~ grass 0 execute @s ~ ~ ~ detect ~ ~ ~ tallgrass 0 summon entity:grass"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`lapis_sword_skills`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "xp 5 @s",
          "playsound random.orb @s ~ ~ ~ 0.3"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:bee_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:bee_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "bee_sword"
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

**`minecraft:blaze_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:blaze_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "blaze_sword"
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
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "blaze_sword_skill"
          },
          "randomize": [
            {
              "run_command": {
                "command": [
                  "particle minecraft:mobflame_single ~ ~0.2 ~"
                ]
              },
              "weight": 5
            },
            {
              "run_command": {
                "command": [
                  "particle minecraft:mobflame_single ~0.3 ~0.2 ~"
                ]
              },
              "weight": 5
            },
            {
              "run_command": {
                "command": [
                  "particle minecraft:mobflame_single ~ ~0.2 ~0.3"
                ]
              },
              "weight": 5
            },
            {
              "run_command": {
                "command": [
                  "particle minecraft:mobflame_single ~-0.3 ~0.2 ~"
                ]
              },
              "weight": 5
            },
            {
              "run_command": {
                "command": [
                  "particle minecraft:mobflame_single ~ ~0.2 ~-0.3"
                ]
              },
              "weight": 5
            },
            {
              "run_command": {
                "command": [
                  "playsound mob.blaze.breathe @a[r=12] ~ ~ ~ 0.5"
                ]
              },
              "weight": 5
            },
            {
              "weight": 95
            }
          ]
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:bone_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:bone_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "bone_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:cactus_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:cactus_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "cactus_sword"
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

**`minecraft:clock_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:clock_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "clock_sword"
          }
        },
        {
          "add": {
            "component_groups": [
              "clock_sword_movement"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "clock_sword_skill"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:constant_events`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "run_command": {
            "command": [
              "function commands/swords_and_more_swords/swords_and_more_swords/tag_swords",
              "gamerule sendcommandfeedback false",
              "gamerule commandblockoutput false",
              "scoreboard objectives add Effect99 dummy",
              "scoreboard players add @s Effect99 1",
              "title @s[scores={Effect99=12000}] actionbar §l§fCreated by §7Effect99",
              "scoreboard players set @s[scores={Effect99=36001}] Effect99 1"
            ]
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

**`minecraft:emerald_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:emerald_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "emerald_sword"
          }
        },
        {
          "filters": {
            "all_of": [
              {
                "subject": "self",
                "test": "is_in_village",
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:ender_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:ender_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "ender_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:fire_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:fire_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "fire_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:ghost_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:ghost_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "ghost_sword"
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
          "add": {
            "component_groups": [
              "ghost_movement"
            ]
          },
          "run_command": {
            "command": [
              "effect @s slow_falling 1 0 true",
              "effect @s saturation 1 1 true"
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
            "operator": "!=",
            "test": "in_lava"
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
              "run_command": {
                "command": [
                  "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 0.15 0.2"
                ]
              },
              "weight": 10
            }
          ]
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:glowstone_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock 0 replace air",
          "fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock 0 replace effect99:lightblock"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:grass_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:grass_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "grass_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:ice_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:ice_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "ice_sword"
          }
        },
        {
          "filters": {
            "all_of": [
              {
                "test": "in_lava"
              },
              {
                "operator": "!=",
                "test": "has_biome_tag",
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
              "fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 frosted_ice 0 replace water",
              "fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 frosted_ice 0 replace flowing_water",
              "fill ~3 ~-1 ~ ~3 ~-1 ~ frosted_ice 0 replace water",
              "fill ~3 ~-1 ~ ~3 ~-1 ~ frosted_ice 0 replace flowing_water",
              "fill ~ ~-1 ~3 ~ ~-1 ~3 frosted_ice 0 replace water",
              "fill ~ ~-1 ~3 ~ ~-1 ~3 frosted_ice 0 replace flowing_water",
              "fill ~-3 ~-1 ~ ~-3 ~-1 ~ frosted_ice 0 replace water",
              "fill ~-3 ~-1 ~ ~-3 ~-1 ~ frosted_ice 0 replace flowing_water",
              "fill ~ ~-1 ~-3 ~ ~-1 ~-3 frosted_ice 0 replace water",
              "fill ~ ~-1 ~-3 ~ ~-1 ~-3 frosted_ice 0 replace flowing_water",
              "execute @e[r=64,type=!player] ~ ~ ~ detect ~ ~ ~ frosted_ice 0 tp @s ~ ~ ~ ~1"
            ]
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

**`minecraft:jungle_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:jungle_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "jungle_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:lapis_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:lapis_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "lapis_sword"
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

**`minecraft:lightning_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:lightning_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "lightning_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:magma_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:magma_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "magma_sword"
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
            "operator": "==",
            "test": "in_water"
          },
          "randomize": [
            {
              "weight": 99
            },
            {
              "run_command": {
                "command": [
                  "playsound bubble.up @a ~ ~ ~ 1 0.9"
                ]
              },
              "weight": 1
            }
          ]
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:nether_star_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:nether_star_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "nether_star_sword"
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

**`minecraft:obsidian_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:obsidian_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "obsidian_sword"
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

**`minecraft:quartz_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:quartz_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "quartz_sword"
          },
          "run_command": {
            "command": [
              "damage @s 14 magic"
            ]
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

**`minecraft:sea_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "mermaid_movement_out_water"
            ]
          },
          "filters": {
            "operator": "!=",
            "test": "in_water"
          },
          "run_command": {
            "command": [
              "camerashake add @s 0.01 1 positional",
              "effect @s conduit_power 0 0"
            ]
          }
        },
        {
          "add": {
            "component_groups": [
              "minecraft:sea_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "sea_sword"
          },
          "run_command": {
            "command": [
              "particle minecraft:example_bounce ~ ~ ~",
              "playsound random.splash @a[r=12] ~ ~ ~ 0.5"
            ]
          }
        },
        {
          "add": {
            "component_groups": [
              "mermaid_movement_in_water"
            ]
          },
          "filters": {
            "test": "in_water"
          },
          "run_command": {
            "command": [
              "effect @s conduit_power 1 0 true"
            ]
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

**`minecraft:shulker_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:shulker_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "shulker_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:slime_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:slime_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "slime_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:spectral_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:spectral_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "spectral_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:spider_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:spider_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "spider_sword"
          },
          "run_command": {
            "command": [
              "ride @s summon_ride minecraft:spider no_ride_change minecraft:spider_sword",
              "particle minecraft:example_linearcurve ~ ~ ~"
            ]
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

**`minecraft:sponge_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:sponge_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "sponge_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:stop_sword_events`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "run_command": {
            "command": [
              "execute @e[r=64,type=!player] ~ ~ ~ detect ~ ~ ~ ice 0 tp @s ~ ~ ~"
            ]
          }
        },
        {
          "filters": {
            "all_of": [
              {
                "operator": "!=",
                "test": "has_biome_tag",
                "value": "nether"
              },
              {
                "operator": "!=",
                "test": "has_biome_tag",
                "value": "the_end"
              }
            ]
          },
          "run_command": {
            "command": [
              "fill ~6 ~6 ~6 ~-6 ~-6 ~-6 stone 0 replace effect99:spectral_block",
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
              "fill ~6 ~6 ~6 ~-6 ~-6 ~-6 netherrack 0 replace effect99:spectral_block",
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
              "fill ~6 ~6 ~6 ~-6 ~-6 ~-6 end_stone 0 replace effect99:spectral_block",
              "fill ~7 ~8 ~8 ~8 ~-8 ~-8 end_stone 0 replace effect99:spectral_block",
              "fill ~-7 ~-8 ~-8 ~-8 ~8 ~8 end_stone 0 replace effect99:spectral_block",
              "fill ~-6 ~8 ~7 ~6 ~-8 ~8 end_stone 0 replace effect99:spectral_block",
              "fill ~6 ~-8 ~-7 ~-6 ~8 ~-8 end_stone 0 replace effect99:spectral_block",
              "fill ~8 ~-8 ~8 ~-8 ~-7 ~-8 end_stone 0 replace effect99:spectral_block",
              "fill ~8 ~8 ~8 ~-8 ~7 ~-8 end_stone 0 replace effect99:spectral_block"
            ]
          }
        },
        {
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:slime_sword"
              }
            ]
          },
          "run_command": {
            "command": [
              "ride @e[type=entity:mountable_slime,r=1,y=~-1] evict_riders"
            ]
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

**`minecraft:time_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:ultra_instinct_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:ultra_instinct_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "ultra_instinct_sword"
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
          "add": {
            "component_groups": [
              "ultra_instinct_sword_movement"
            ]
          },
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

**`minecraft:wither_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:wither_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "wither_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:wolf_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:wolf_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "wolf_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`sea_sword_sound`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "filters": {
            "operator": "!=",
            "test": "in_water"
          },
          "run_command": {
            "command": [
              "playsound mob.fish.flop @a[r=12] ~ ~ ~ 1 0.6"
            ]
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

**`shoot_ultra_instinct_projectile`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "ultra_instinct_projectile"
        ]
      },
      "remove": {
        "component_groups": [
          "ultra_instinct_projectile"
        ]
      },
      "run_command": {
        "command": [
          "playsound mob.wither.ambient @s ~ ~1 ~ 2 0.6"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`shulker_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
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
  },
  "reference": {
    "present": false
  }
}
```

**`slime_sword_skills`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "ride @s summon_ride entity:mountable_slime no_ride_change",
          "scoreboard objectives add slime_despawn dummy"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`spectral_sword_function`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "filters": {
            "all_of": [
              {
                "operator": "!=",
                "test": "has_biome_tag",
                "value": "nether"
              },
              {
                "operator": "!=",
                "test": "has_biome_tag",
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`spectral_sword_function_1`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "filters": {
            "all_of": [
              {
                "operator": "!=",
                "test": "has_biome_tag",
                "value": "nether"
              },
              {
                "operator": "!=",
                "test": "has_biome_tag",
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`spectral_sword_reload_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:spectral_sword"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "spectral_sword"
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

**`spectral_sword_skills`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "filters": {
            "operator": "!=",
            "test": "has_biome_tag",
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`spider_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "spider_sword_skill"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "spider_sword_skill"
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

**`start_player_explode`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:default_player"
        ]
      },
      "remove": {
        "component_groups": [
          "start_player_explode_event"
        ]
      },
      "run_command": {
        "command": [
          "summon entity:instant_creeper_explode ~ ~1 ~",
          "kill @s"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`start_player_explode_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "start_player_explode_event"
        ]
      },
      "run_command": {
        "command": [
          "playanimation @s animation.player.explode",
          "playsound random.fuse"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`starting_wolf_transformation`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "effect @s nausea 5 0 true"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`stop_bee_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "bee_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:bee_sword"
            ]
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

**`stop_blaze_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
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

**`stop_blaze_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:blaze_sword"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "blaze_sword"
          },
          "remove": {
            "component_groups": [
              "shoot_small_fireball"
            ]
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

**`stop_bone_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "bone_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:bone_sword"
            ]
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

**`stop_cactus_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "cactus_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:cactus_sword"
            ]
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

**`stop_clock_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
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

**`stop_emerald_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "emerald_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:emerald_sword"
            ]
          },
          "run_command": {
            "command": [
              "effect @s village_hero 0 0 true"
            ]
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

**`stop_ender_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "ender_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:ender_sword"
            ]
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

**`stop_fire_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "fire_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:fire_sword"
            ]
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

**`stop_ghost_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "ghost_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:ghost_sword"
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
  },
  "reference": {
    "present": false
  }
}
```

**`stop_grass_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "grass_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:grass_sword"
            ]
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

**`stop_ice_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "ice_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:ice_sword"
            ]
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

**`stop_jungle_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "jungle_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:jungle_sword"
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
  },
  "reference": {
    "present": false
  }
}
```

**`stop_lapis_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "lapis_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:lapis_sword"
            ]
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

**`stop_lightning_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "lightning_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:lightning_sword"
            ]
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

**`stop_magma_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "magma_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:magma_sword"
            ]
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

**`stop_nether_star_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "nether_star_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:nether_star_sword"
            ]
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

**`stop_obsidian_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "obsidian_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:obsidian_sword"
            ]
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

**`stop_quartz_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "quartz_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:quartz_sword"
            ]
          },
          "run_command": {
            "command": [
              "damage @s 14 magic"
            ]
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

**`stop_sea_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "sea_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:sea_sword",
              "mermaid_movement_in_water"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`stop_shulker_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "shulker_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:shulker_sword"
            ]
          },
          "run_command": {
            "command": [
              "ride @s stop_riding"
            ]
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

**`stop_slime_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "slime_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:slime_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`stop_spectral_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
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

**`stop_spider_skill_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:spider_sword"
            ]
          },
          "filters": {
            "subject": "self",
            "test": "is_family",
            "value": "spider_sword_skill"
          },
          "remove": {
            "component_groups": [
              "spider_sword_skill"
            ]
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

**`stop_spider_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "spider_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:spider_sword",
              "spider_sword_skill"
            ]
          },
          "run_command": {
            "command": [
              "ride @s stop_riding"
            ]
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

**`stop_sponge_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "sponge_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:sponge_sword"
            ]
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

**`stop_time_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "time_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:time_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`stop_ultra_instinct_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "ultra_instinct_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:ultra_instinct_sword",
              "ultra_instinct_sword_movement"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`stop_wither_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "wither_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:wither_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`stop_wolf_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
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
          }
        },
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
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

**`stop_wolf_transformation`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "run_command": {
            "command": [
              "effect @s nausea 0 0",
              "effect @s blindness 0 0",
              "stopsound @a wolf_sword.howl",
              "stopsound @a wolf_sword.distant_howl"
            ]
          }
        },
        {
          "add": {
            "component_groups": [
              "minecraft:wolf_sword"
            ]
          },
          "remove": {
            "component_groups": [
              "wolf_transformation",
              "complete_wolf_transformation",
              "wolf_movement"
            ]
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

**`time_sword_movement`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "time_sword_movement"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`ultra_instinct_sword_effects`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "randomize": [
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.3 ~1 ~",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~ ~2 ~0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~-0.3 ~ ~",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~ ~0.3 ~-0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.3 ~1.5 ~0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~-0.3 ~0.8 ~-0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~-0.3 ~2 ~0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.2 ~1 ~0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.3 ~0.9 ~0.1",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.2 ~2.3 ~-0.2",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~-0.3 ~1.2 ~",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.3 ~0.3 ~0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.3 ~0.6 ~0.1",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~-0.3 ~0.2 ~0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.1 ~0.7 ~-0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`ultra_instinct_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "spreadplayers ~ ~ 1 3 @s",
          "playsound mob.endermen.portal @a[r=17] ~ ~ ~ 1 0.6"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`wet_sponge_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "filters": {
            "domain": "hand",
            "subject": "self",
            "test": "has_equipment",
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
  },
  "reference": {
    "present": false
  }
}
```

**`wither_sword_effects`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "randomize": [
        {
          "run_command": {
            "command": [
              "playsound mob.wither.death @a[r=16]"
            ]
          },
          "weight": 50
        },
        {
          "run_command": {
            "command": [
              "playsound mob.wither.hurt @a[r=16]"
            ]
          },
          "weight": 50
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`wolf_damage_sound`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "playsound mob.wolf.bark @a[r=16] ~ ~ ~ 1 0.55"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`wolf_movement`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "wolf_movement"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`wolf_sword_sounds`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "randomize": [
        {
          "run_command": {
            "command": [
              "playsound mob.wolf.growl @a[r=16] ~ ~ ~ 1 0.9 24"
            ]
          },
          "weight": 1
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`wolf_sword_start_events`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "wolf_transformation"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "wolf_transformation"
          },
          "run_command": {
            "command": [
              "function commands/swords_and_more_swords/swords_and_more_swords/tellraw1"
            ]
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

**`wolf_transformation`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "complete_wolf_transformation"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "complete_wolf_transformation"
          },
          "run_command": {
            "command": [
              "playsound random.fizz @a[r=16] ~~~",
              "playsound wolf_sword.howl @a[r=24] ~~~",
              "playsound wolf_sword.distant_howl @a[rm=25,r=100]",
              "particle minecraft:egg_destroy_emitter ~ ~ ~",
              "particle minecraft:egg_destroy_emitter ~ ~0.5 ~",
              "particle minecraft:egg_destroy_emitter ~ ~0.8 ~"
            ]
          }
        },
        {
          "filters": {
            "test": "is_family",
            "value": "wolf_transformation"
          },
          "remove": {
            "component_groups": [
              "wolf_transformation"
            ]
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

##### `root`

**`format_version`**

```json
{
  "addon": {
    "present": true,
    "value": "1.11.0"
  },
  "reference": {
    "present": true,
    "value": "1.18.20"
  }
}
```

#### Образец `1.20.30.1`

SHA-256 файла образца: `0ad825e9433490dda6fa9d51eb0eaf4aaf1e7e510559f7cb0ceded5822ebc155`.

##### `component_groups`

**`blaze_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:timer": {
        "looping": false,
        "time": [
          6,
          6
        ],
        "time_down_event": {
          "event": "blaze_sword_skill",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "blaze_sword",
          "blaze_sword_skill"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`clock_sword_movement`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:movement": {
        "value": 1
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`clock_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:timer": {
        "looping": true,
        "randomInterval": false,
        "time": [
          5,
          5
        ],
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`complete_wolf_transformation`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:attack": {
        "damage": 15
      },
      "minecraft:damage_sensor": {
        "triggers": [
          {
            "deals_damage": true,
            "on_damage": {
              "event": "wolf_damage_sound",
              "filters": {
                "all_of": [
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "void"
                  }
                ]
              }
            }
          }
        ]
      },
      "minecraft:timer": {
        "looping": true,
        "randomInterval": true,
        "time": [
          3,
          6
        ],
        "time_down_event": {
          "event": "wolf_sword_sounds",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "wolf",
          "wolf_sword",
          "complete_wolf_transformation",
          "monster"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`despawn`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:despawn": {}
    }
  },
  "reference": {
    "present": false
  }
}
```

**`ghost_movement`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:movement": {
        "value": 0.14
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`mermaid_movement_in_water`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:underwater_movement": {
        "value": 0.07
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`mermaid_movement_out_water`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:movement": {
        "value": 0.06
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:add_bad_omen`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spell_effects": {
        "add_effects": [
          {
            "display_on_screen_animation": true,
            "duration": 6000,
            "effect": "bad_omen"
          }
        ]
      },
      "minecraft:timer": {
        "looping": false,
        "time": [
          0.0,
          0.0
        ],
        "time_down_event": {
          "event": "minecraft:clear_add_bad_omen",
          "target": "self"
        }
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:spell_effects": {
        "add_effects": [
          {
            "display_on_screen_animation": true,
            "duration": 6000,
            "effect": "bad_omen",
            "visible": false
          }
        ]
      },
      "minecraft:timer": {
        "looping": false,
        "time": [
          0.0,
          0.0
        ],
        "time_down_event": {
          "event": "minecraft:clear_add_bad_omen",
          "target": "self"
        }
      }
    }
  }
}
```

**`minecraft:bee_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:timer": {
        "looping": true,
        "randomInterval": true,
        "time": [
          3,
          8
        ],
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
  "reference": {
    "present": false
  }
}
```

**`minecraft:blaze_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": false,
          "on_damage": {
            "filters": {
              "any_of": [
                {
                  "subject": "self",
                  "test": "has_damage",
                  "value": "fire"
                },
                {
                  "subject": "self",
                  "test": "has_damage",
                  "value": "fire_tick"
                }
              ]
            }
          }
        }
      },
      "minecraft:hurt_on_condition": {
        "damage_conditions": [
          {
            "cause": "drowning",
            "damage_per_tick": 1,
            "filters": {
              "test": "in_water_or_rain"
            }
          }
        ]
      },
      "minecraft:timer": {
        "looping": true,
        "time": [
          1,
          1
        ],
        "time_down_event": {
          "event": "blaze_sword_effects",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "blaze_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:bone_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:timer": {
        "looping": true,
        "time": [
          1,
          1
        ],
        "time_down_event": {
          "event": "bone_sword_skills",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "bone_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:cactus_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:timer": {
        "looping": true,
        "time": [
          0.5,
          0.5
        ],
        "time_down_event": {
          "event": "cactus_sword_skills",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "cactus_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:clock_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:type_family": {
        "family": [
          "player",
          "clock_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:default_player`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:attack": {
        "damage": 1
      },
      "minecraft:breathable": {
        "generates_bubbles": false,
        "inhale_time": 3.75,
        "suffocate_time": -1,
        "total_supply": 15
      },
      "minecraft:collision_box": {
        "height": 1.8,
        "width": 0.6
      },
      "minecraft:damage_sensor": {},
      "minecraft:health": {
        "max": 20,
        "value": 20
      },
      "minecraft:movement": {
        "value": 0.1
      },
      "minecraft:physics": {
        "has_collision": true,
        "has_gravity": true
      },
      "minecraft:rideable": {
        "family_types": [
          "parrot_tame"
        ],
        "pull_in_entities": true,
        "seat_count": 2,
        "seats": [
          {
            "lock_rider_rotation": 0,
            "max_rider_count": 0,
            "min_rider_count": 0,
            "position": [
              0.4,
              -0.2,
              -0.1
            ]
          },
          {
            "lock_rider_rotation": 0,
            "max_rider_count": 2,
            "min_rider_count": 1,
            "position": [
              -0.4,
              -0.2,
              -0.1
            ]
          }
        ]
      },
      "minecraft:scale": {
        "value": 1
      },
      "minecraft:timer": {},
      "minecraft:type_family": {
        "family": [
          "player",
          "default_player"
        ]
      },
      "minecraft:underwater_movement": {
        "value": 0.02
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:emerald_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:type_family": {
        "family": [
          "player",
          "emerald_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:ender_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": [
          {
            "deals_damage": true,
            "on_damage": {
              "event": "ender_sword_skill",
              "filters": {
                "all_of": [
                  {
                    "operator": "!=",
                    "subject": "self",
                    "test": "has_damage",
                    "value": "projectile"
                  }
                ]
              }
            }
          },
          {
            "deals_damage": false,
            "on_damage": {
              "event": "ender_sword_tp",
              "filters": {
                "all_of": [
                  {
                    "subject": "self",
                    "test": "has_damage",
                    "value": "projectile"
                  }
                ]
              }
            }
          },
          {
            "deals_damage": true,
            "on_damage": {
              "event": "ender_sword_tp",
              "filters": {
                "all_of": [
                  {
                    "test": "in_water_or_rain"
                  }
                ]
              }
            }
          }
        ]
      },
      "minecraft:hurt_on_condition": {
        "damage_conditions": [
          {
            "cause": "drowning",
            "damage_per_tick": 1,
            "filters": {
              "test": "in_water_or_rain"
            }
          }
        ]
      },
      "minecraft:timer": {
        "looping": true,
        "randomInterval": true,
        "time": [
          6,
          18
        ],
        "time_down_event": {
          "event": "ender_sword_sound",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "ender_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:fire_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": false,
          "on_damage": {
            "filters": {
              "any_of": [
                {
                  "subject": "self",
                  "test": "has_damage",
                  "value": "fire"
                },
                {
                  "subject": "self",
                  "test": "has_damage",
                  "value": "fire_tick"
                }
              ]
            }
          }
        }
      },
      "minecraft:timer": {
        "looping": true,
        "randomInterval": true,
        "time": [
          0.2,
          0.7
        ],
        "time_down_event": {
          "event": "fire_sword_sound",
          "target": "self"
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
  "reference": {
    "present": false
  }
}
```

**`minecraft:ghost_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:breathable": {
        "breathes_air": true,
        "breathes_lava": true,
        "breathes_water": true,
        "generates_bubbles": false,
        "inhale_time": 3.75,
        "suffocate_time": 0,
        "total_supply": 15
      },
      "minecraft:collision_box": {
        "height": 0.0,
        "width": 0.0
      },
      "minecraft:damage_sensor": {
        "triggers": {
          "cause": "all",
          "deals_damage": false
        }
      },
      "minecraft:knockback_resistance": {
        "value": 1.0
      },
      "minecraft:scale": {
        "value": 1.05
      },
      "minecraft:type_family": {
        "family": [
          "ghost_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:grass_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:timer": {
        "looping": true,
        "time": [
          0.2,
          0.2
        ],
        "time_down_event": {
          "event": "grass_sword_skills",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "grass_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:ice_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:type_family": {
        "family": [
          "player",
          "ice_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:jungle_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:health": {
        "max": 8,
        "value": 8
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "jungle_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:lapis_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:timer": {
        "looping": true,
        "randomInterval": true,
        "time": [
          2.5,
          6.0
        ],
        "time_down_event": {
          "event": "lapis_sword_skills",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "lapis_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:lightning_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": false,
          "on_damage": {
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "lightning"
                }
              ]
            }
          }
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
  "reference": {
    "present": false
  }
}
```

**`minecraft:magma_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": false,
          "on_damage": {
            "filters": {
              "any_of": [
                {
                  "subject": "self",
                  "test": "has_damage",
                  "value": "fire_tick"
                },
                {
                  "operator": "equals",
                  "subject": "block",
                  "test": "is_block",
                  "value": "magma"
                }
              ]
            }
          }
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
  "reference": {
    "present": false
  }
}
```

**`minecraft:nether_star_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": false,
          "on_damage": {
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "nether_star_projectile"
                }
              ]
            }
          }
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
  "reference": {
    "present": false
  }
}
```

**`minecraft:obsidian_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": false,
          "on_damage": {
            "filters": {
              "any_of": [
                {
                  "subject": "self",
                  "test": "has_damage",
                  "value": "block_explosion"
                },
                {
                  "subject": "self",
                  "test": "has_damage",
                  "value": "entity_explosion"
                }
              ]
            }
          }
        }
      },
      "minecraft:knockback_resistance": {
        "value": 1.0
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "obsidian_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:quartz_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:type_family": {
        "family": [
          "player",
          "quartz_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:sea_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:breathable": {
        "breathes_air": false,
        "breathes_lava": false,
        "breathes_water": true,
        "generates_bubbles": false,
        "inhale_time": 3.75,
        "suffocate_time": -1,
        "total_supply": 2
      },
      "minecraft:collision_box": {
        "height": 0.9,
        "width": 0.6
      },
      "minecraft:timer": {
        "looping": true,
        "time": [
          0.5,
          0.5
        ],
        "time_down_event": {
          "event": "sea_sword_sound",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "sea_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:shulker_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:scale": {
        "value": 1
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "shulker_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:slime_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": false,
          "on_damage": {
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "tamed_slime"
                }
              ]
            }
          }
        }
      },
      "minecraft:timer": {
        "looping": false,
        "time": [
          0.4,
          0.4
        ],
        "time_down_event": {
          "event": "slime_sword_skills",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "slime_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:spectral_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:rideable": {
        "family_types": [
          "ender_crystal",
          "spectral_sword"
        ],
        "seat_count": 1,
        "seats": {
          "lock_rider_rotation": 0,
          "position": [
            0.0,
            0.4,
            0.0
          ]
        }
      },
      "minecraft:timer": {
        "looping": false,
        "time": [
          0.4,
          0.4
        ],
        "time_down_event": {
          "event": "spectral_sword_skills",
          "target": "self"
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
  "reference": {
    "present": false
  }
}
```

**`minecraft:spider_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:type_family": {
        "family": [
          "player",
          "spider_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:sponge_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:type_family": {
        "family": [
          "player",
          "sponge_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:time_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:movement": {
        "value": 1
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "time_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:ultra_instinct_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": [
          {
            "deals_damage": false,
            "on_damage": {
              "event": "ultra_instinct_sword_skill",
              "filters": {
                "all_of": [
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "lava"
                  },
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "drowning"
                  },
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "void"
                  },
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "thorns"
                  },
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "suicide"
                  },
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "starve"
                  },
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "fire"
                  },
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "fire_tick"
                  },
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "magic"
                  }
                ]
              }
            }
          },
          {
            "deals_damage": false,
            "on_damage": {
              "filters": {
                "test": "has_damage",
                "value": "fire"
              }
            }
          },
          {
            "deals_damage": false,
            "on_damage": {
              "filters": {
                "test": "has_damage",
                "value": "fire_tick"
              }
            }
          },
          {
            "deals_damage": false,
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
            }
          },
          {
            "deals_damage": true,
            "on_damage": {
              "filters": {
                "all_of": [
                  {
                    "test": "has_damage",
                    "value": "lava"
                  }
                ]
              }
            }
          }
        ]
      },
      "minecraft:knockback_resistance": {
        "value": 1.0
      },
      "minecraft:timer": {
        "looping": true,
        "randomInterval": true,
        "time": [
          0.1,
          0.2
        ],
        "time_down_event": {
          "event": "ultra_instinct_sword_effects",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "ultra_instinct_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:wither_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": false,
          "on_damage": {
            "filters": {
              "all_of": [
                {
                  "subject": "self",
                  "test": "has_damage",
                  "value": "wither"
                }
              ]
            }
          }
        }
      },
      "minecraft:rideable": {
        "family_types": [
          "entity_name"
        ],
        "seat_count": 1,
        "seats": {
          "lock_rider_rotation": 0,
          "position": [
            0.0,
            0.4,
            0.0
          ]
        }
      },
      "minecraft:timer": {
        "looping": true,
        "randomInterval": true,
        "time": [
          4,
          18
        ],
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
  "reference": {
    "present": false
  }
}
```

**`minecraft:wolf_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:type_family": {
        "family": [
          "player",
          "wolf_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`shoot_small_fireball`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 1,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:fake_fireball",
          "spawn_event": "set_sound"
        },
        {
          "max_wait_time": 1,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:fake_fireball",
          "spawn_event": "set_sound"
        },
        {
          "max_wait_time": 1,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:fake_fireball",
          "spawn_event": "set_sound"
        },
        {
          "max_wait_time": 1,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:fake_fireball",
          "spawn_event": "set_sound"
        }
      ],
      "minecraft:timer": {
        "looping": false,
        "time": [
          2,
          2
        ],
        "time_down_event": {
          "event": "stop_blaze_sword_skill",
          "target": "self"
        }
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`shulker_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
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
  "reference": {
    "present": false
  }
}
```

**`spider_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": false,
          "spawn_entity": "entity:web"
        }
      ],
      "minecraft:timer": {
        "looping": false,
        "time": [
          2,
          2
        ],
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
  "reference": {
    "present": false
  }
}
```

**`start_player_explode_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:movement": {
        "value": 0.0
      },
      "minecraft:timer": {
        "looping": true,
        "time": [
          1.5,
          1.5
        ],
        "time_down_event": {
          "event": "start_player_explode",
          "target": "self"
        }
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`time_sword_movement`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:movement": {
        "value": 1
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`ultra_instinct_projectile`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:ultra_instinct_projectile"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`ultra_instinct_sword_movement`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:movement": {
        "value": 0.22
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`wolf_movement`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:movement": {
        "value": 0.18
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`wolf_transformation`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:type_family": {
        "family": [
          "player",
          "wolf_sword",
          "wolf_transformation"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

##### `components`

**`minecraft:block_climber`**

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

**`minecraft:environment_sensor`**

```json
{
  "addon": {
    "present": true,
    "value": [
      {
        "on_environment": {
          "event": "minecraft:trigger_raid",
          "filters": {
            "all_of": [
              {
                "subject": "self",
                "test": "has_mob_effect",
                "value": "bad_omen"
              },
              {
                "subject": "self",
                "test": "is_in_village",
                "value": true
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:constant_events",
          "filters": {
            "operator": "!=",
            "test": "is_family",
            "value": "null"
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:stop_sword_events",
          "filters": {
            "any_of": [
              {
                "subject": "self",
                "test": "is_family",
                "value": "default_player"
              },
              {
                "operator": "!=",
                "subject": "self",
                "test": "is_family",
                "value": "spectral_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:blaze_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:blaze_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_blaze_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:blaze_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:bone_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:bone_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_bone_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:bone_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:cactus_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:cactus_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_cactus_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:cactus_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:emerald_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:emerald_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_emerald_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:emerald_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:fire_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:fire_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_fire_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:fire_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:grass_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:grass_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_grass_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:grass_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:jungle_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:jungle_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_jungle_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:jungle_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:magma_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:magma_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_magma_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:magma_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:ice_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:ice_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_ice_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:ice_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:lapis_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:lapis_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_lapis_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:lapis_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:obsidian_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:obsidian_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_obsidian_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:obsidian_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:quartz_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:quartz_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_quartz_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:quartz_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:sea_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:sea_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_sea_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:sea_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:spectral_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:spectral_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_spectral_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:spectral_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:slime_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:slime_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_slime_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:slime_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:shulker_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:shulker_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_shulker_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:shulker_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:spider_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:spider_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_spider_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:spider_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:sponge_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:sponge_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_sponge_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:sponge_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:time_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:time_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_time_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:time_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:wither_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:wither_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_wither_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:wither_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:glowstone_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:glowstone_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:lightning_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:lightning_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_lightning_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:lightning_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:ender_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:ender_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_ender_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:ender_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:ultra_instinct_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:ultra_instinct_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_ultra_instinct_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:ultra_instinct_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:wolf_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:wolf_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_wolf_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:wolf_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "starting_wolf_transformation",
          "filters": {
            "all_of": [
              {
                "test": "is_family",
                "value": "wolf_transformation"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "wolf_movement",
          "filters": {
            "all_of": [
              {
                "test": "is_family",
                "value": "complete_wolf_transformation"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:ghost_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:ghost_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_ghost_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:ghost_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:clock_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:clock_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_clock_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:clock_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:nether_star_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:nether_star_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_nether_star_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:nether_star_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:bee_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:bee_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_bee_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:bee_sword"
              }
            ]
          }
        }
      }
    ]
  },
  "reference": {
    "present": true,
    "value": {
      "triggers": {
        "event": "minecraft:trigger_raid",
        "filters": {
          "all_of": [
            {
              "subject": "self",
              "test": "has_mob_effect",
              "value": "bad_omen"
            },
            {
              "subject": "self",
              "test": "is_in_village",
              "value": true
            }
          ]
        }
      }
    }
  }
}
```

**`minecraft:exhaustion_values`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "attack": 0.1,
      "damage": 0.1,
      "heal": 6,
      "jump": 0.05,
      "mine": 0.005,
      "sprint": 0.1,
      "sprint_jump": 0.2,
      "swim": 0.01,
      "walk": 0.0
    }
  }
}
```

**`minecraft:physics`**

```json
{
  "addon": {
    "present": true,
    "value": {}
  },
  "reference": {
    "present": true,
    "value": {
      "push_towards_closest_space": true
    }
  }
}
```

**`minecraft:player.exhaustion`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "max": 4,
      "value": 0
    }
  },
  "reference": {
    "present": true,
    "value": {
      "max": 20,
      "value": 0
    }
  }
}
```

**`minecraft:player.saturation`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "value": 20
    }
  },
  "reference": {
    "present": true,
    "value": {
      "max": 20,
      "value": 5
    }
  }
}
```

**`minecraft:scaffolding_climber`**

```json
{
  "addon": {
    "present": true,
    "value": {}
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:type_family`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "family": [
        "player",
        "default_player"
      ]
    }
  },
  "reference": {
    "present": true,
    "value": {
      "family": [
        "player"
      ]
    }
  }
}
```

##### `description`

**`animations`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "ghost_sword": "controller.animation.ghost_sword",
      "shulker_sword": "controller.animation.shulker_sword",
      "wither_sword": "controller.animation.wither_sword",
      "wolf_sword_0": "controller.animation.wolf_sword",
      "wolf_sword_1": "controller.animation.start_wolf_sword",
      "wolf_sword_2": "controller.animation.end_wolf_sword"
    }
  },
  "reference": {
    "present": false
  }
}
```

**`scripts`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "animate": [
        "shulker_sword",
        "wither_sword",
        "wolf_sword_0",
        "wolf_sword_1",
        "wolf_sword_2",
        "ghost_sword"
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

##### `events`

**`bee_sword_flower`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "randomize": [
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 0"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 1"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 2"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 4"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 5"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 6"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 7"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 8"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 9"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 10"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ yellow_flower 0"
            ]
          },
          "weight": 1
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`blaze_sword_effects`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "randomize": [
        {
          "run_command": {
            "command": [
              "particle minecraft:mobflame_single ~ ~0.2 ~"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:mobflame_single ~0.3 ~0.2 ~"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:mobflame_single ~ ~0.2 ~0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:mobflame_single ~-0.3 ~0.2 ~"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:mobflame_single ~ ~0.2 ~-0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "playsound mob.blaze.breathe @a[r=12] ~ ~ ~ 0.5"
            ]
          },
          "weight": 1
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`blaze_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "shoot_small_fireball"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`blaze_sword_skill_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "blaze_sword_skill"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`bone_sword_skills`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "summon entity:grows_crop ~ ~0.1 ~ grows_crop_event"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`cactus_sword_skills`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "damage @e[r=1.4,type=!player] 1 contact entity @s",
          "damage @s 1 contact"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`clock_sword_movement`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "clock_sword_movement"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`clock_sword_skill_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "clock_sword_skill"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`default_player`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:default_player"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`despawn`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "despawn"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`ender_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
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
              "run_command": {
                "command": [
                  "spreadplayers ~ ~ 0 16 @s",
                  "playsound mob.endermen.portal @a[r=17]"
                ]
              },
              "weight": 50
            }
          ]
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`ender_sword_sound`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "randomize": [
        {
          "run_command": {
            "command": [
              "playsound mob.endermen.scream @a[r=8] ~ ~ ~"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "playsound mob.endermen.idle @a[r=8] ~ ~ ~"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "playsound mob.endermen.stare @a[r=8] ~ ~ ~"
            ]
          },
          "weight": 1
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`ender_sword_tp`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "spreadplayers ~ ~ 0 16 @s",
          "playsound mob.endermen.portal @a[r=17]"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`fire_sword_sound`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "playsound fire.fire @a[r=8]"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`grass_sword_skills`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "execute @e[type=!player,type=!item,type=!entity:grass,type=!xp_orb,type=!arrow,r=8,tag=!grass] ~ ~ ~ detect ~ ~-0.1 ~ grass 0 execute @s ~ ~ ~ detect ~ ~ ~ air 0 summon entity:grass",
          "execute @e[type=!player,type=!item,type=!entity:grass,type=!xp_orb,type=!arrow,r=8,tag=!grass] ~ ~ ~ detect ~ ~-0.1 ~ grass 0 execute @s ~ ~ ~ detect ~ ~ ~ tallgrass 0 summon entity:grass"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`lapis_sword_skills`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "xp 5 @s",
          "playsound random.orb @s ~ ~ ~ 0.3"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:bee_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:bee_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "bee_sword"
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

**`minecraft:blaze_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:blaze_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "blaze_sword"
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
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "blaze_sword_skill"
          },
          "randomize": [
            {
              "run_command": {
                "command": [
                  "particle minecraft:mobflame_single ~ ~0.2 ~"
                ]
              },
              "weight": 5
            },
            {
              "run_command": {
                "command": [
                  "particle minecraft:mobflame_single ~0.3 ~0.2 ~"
                ]
              },
              "weight": 5
            },
            {
              "run_command": {
                "command": [
                  "particle minecraft:mobflame_single ~ ~0.2 ~0.3"
                ]
              },
              "weight": 5
            },
            {
              "run_command": {
                "command": [
                  "particle minecraft:mobflame_single ~-0.3 ~0.2 ~"
                ]
              },
              "weight": 5
            },
            {
              "run_command": {
                "command": [
                  "particle minecraft:mobflame_single ~ ~0.2 ~-0.3"
                ]
              },
              "weight": 5
            },
            {
              "run_command": {
                "command": [
                  "playsound mob.blaze.breathe @a[r=12] ~ ~ ~ 0.5"
                ]
              },
              "weight": 5
            },
            {
              "weight": 95
            }
          ]
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:bone_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:bone_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "bone_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:cactus_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:cactus_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "cactus_sword"
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

**`minecraft:clock_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:clock_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "clock_sword"
          }
        },
        {
          "add": {
            "component_groups": [
              "clock_sword_movement"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "clock_sword_skill"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:constant_events`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "run_command": {
            "command": [
              "function commands/swords_and_more_swords/swords_and_more_swords/tag_swords",
              "gamerule sendcommandfeedback false",
              "gamerule commandblockoutput false",
              "scoreboard objectives add Effect99 dummy",
              "scoreboard players add @s Effect99 1",
              "title @s[scores={Effect99=12000}] actionbar §l§fCreated by §7Effect99",
              "scoreboard players set @s[scores={Effect99=36001}] Effect99 1"
            ]
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

**`minecraft:emerald_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:emerald_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "emerald_sword"
          }
        },
        {
          "filters": {
            "all_of": [
              {
                "subject": "self",
                "test": "is_in_village",
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:ender_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:ender_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "ender_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:fire_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:fire_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "fire_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:ghost_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:ghost_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "ghost_sword"
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
          "add": {
            "component_groups": [
              "ghost_movement"
            ]
          },
          "run_command": {
            "command": [
              "effect @s slow_falling 1 0 true",
              "effect @s saturation 1 1 true"
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
            "operator": "!=",
            "test": "in_lava"
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
              "run_command": {
                "command": [
                  "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 0.15 0.2"
                ]
              },
              "weight": 10
            }
          ]
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:glowstone_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock 0 replace air",
          "fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock 0 replace effect99:lightblock"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:grass_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:grass_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "grass_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:ice_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:ice_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "ice_sword"
          }
        },
        {
          "filters": {
            "all_of": [
              {
                "test": "in_lava"
              },
              {
                "operator": "!=",
                "test": "has_biome_tag",
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
              "fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 frosted_ice 0 replace water",
              "fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 frosted_ice 0 replace flowing_water",
              "fill ~3 ~-1 ~ ~3 ~-1 ~ frosted_ice 0 replace water",
              "fill ~3 ~-1 ~ ~3 ~-1 ~ frosted_ice 0 replace flowing_water",
              "fill ~ ~-1 ~3 ~ ~-1 ~3 frosted_ice 0 replace water",
              "fill ~ ~-1 ~3 ~ ~-1 ~3 frosted_ice 0 replace flowing_water",
              "fill ~-3 ~-1 ~ ~-3 ~-1 ~ frosted_ice 0 replace water",
              "fill ~-3 ~-1 ~ ~-3 ~-1 ~ frosted_ice 0 replace flowing_water",
              "fill ~ ~-1 ~-3 ~ ~-1 ~-3 frosted_ice 0 replace water",
              "fill ~ ~-1 ~-3 ~ ~-1 ~-3 frosted_ice 0 replace flowing_water",
              "execute @e[r=64,type=!player] ~ ~ ~ detect ~ ~ ~ frosted_ice 0 tp @s ~ ~ ~ ~1"
            ]
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

**`minecraft:jungle_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:jungle_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "jungle_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:lapis_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:lapis_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "lapis_sword"
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

**`minecraft:lightning_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:lightning_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "lightning_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:magma_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:magma_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "magma_sword"
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
            "operator": "==",
            "test": "in_water"
          },
          "randomize": [
            {
              "weight": 99
            },
            {
              "run_command": {
                "command": [
                  "playsound bubble.up @a ~ ~ ~ 1 0.9"
                ]
              },
              "weight": 1
            }
          ]
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:nether_star_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:nether_star_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "nether_star_sword"
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

**`minecraft:obsidian_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:obsidian_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "obsidian_sword"
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

**`minecraft:quartz_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:quartz_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "quartz_sword"
          },
          "run_command": {
            "command": [
              "damage @s 14 magic"
            ]
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

**`minecraft:sea_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "mermaid_movement_out_water"
            ]
          },
          "filters": {
            "operator": "!=",
            "test": "in_water"
          },
          "run_command": {
            "command": [
              "camerashake add @s 0.01 1 positional",
              "effect @s conduit_power 0 0"
            ]
          }
        },
        {
          "add": {
            "component_groups": [
              "minecraft:sea_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "sea_sword"
          },
          "run_command": {
            "command": [
              "particle minecraft:example_bounce ~ ~ ~",
              "playsound random.splash @a[r=12] ~ ~ ~ 0.5"
            ]
          }
        },
        {
          "add": {
            "component_groups": [
              "mermaid_movement_in_water"
            ]
          },
          "filters": {
            "test": "in_water"
          },
          "run_command": {
            "command": [
              "effect @s conduit_power 1 0 true"
            ]
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

**`minecraft:shulker_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:shulker_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "shulker_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:slime_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:slime_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "slime_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:spectral_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:spectral_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "spectral_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:spider_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:spider_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "spider_sword"
          },
          "run_command": {
            "command": [
              "ride @s summon_ride minecraft:spider no_ride_change minecraft:spider_sword",
              "particle minecraft:example_linearcurve ~ ~ ~"
            ]
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

**`minecraft:sponge_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:sponge_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "sponge_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:stop_sword_events`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "run_command": {
            "command": [
              "execute @e[r=64,type=!player] ~ ~ ~ detect ~ ~ ~ ice 0 tp @s ~ ~ ~"
            ]
          }
        },
        {
          "filters": {
            "all_of": [
              {
                "operator": "!=",
                "test": "has_biome_tag",
                "value": "nether"
              },
              {
                "operator": "!=",
                "test": "has_biome_tag",
                "value": "the_end"
              }
            ]
          },
          "run_command": {
            "command": [
              "fill ~6 ~6 ~6 ~-6 ~-6 ~-6 stone 0 replace effect99:spectral_block",
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
              "fill ~6 ~6 ~6 ~-6 ~-6 ~-6 netherrack 0 replace effect99:spectral_block",
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
              "fill ~6 ~6 ~6 ~-6 ~-6 ~-6 end_stone 0 replace effect99:spectral_block",
              "fill ~7 ~8 ~8 ~8 ~-8 ~-8 end_stone 0 replace effect99:spectral_block",
              "fill ~-7 ~-8 ~-8 ~-8 ~8 ~8 end_stone 0 replace effect99:spectral_block",
              "fill ~-6 ~8 ~7 ~6 ~-8 ~8 end_stone 0 replace effect99:spectral_block",
              "fill ~6 ~-8 ~-7 ~-6 ~8 ~-8 end_stone 0 replace effect99:spectral_block",
              "fill ~8 ~-8 ~8 ~-8 ~-7 ~-8 end_stone 0 replace effect99:spectral_block",
              "fill ~8 ~8 ~8 ~-8 ~7 ~-8 end_stone 0 replace effect99:spectral_block"
            ]
          }
        },
        {
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:slime_sword"
              }
            ]
          },
          "run_command": {
            "command": [
              "ride @e[type=entity:mountable_slime,r=1,y=~-1] evict_riders"
            ]
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

**`minecraft:time_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:ultra_instinct_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:ultra_instinct_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "ultra_instinct_sword"
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
          "add": {
            "component_groups": [
              "ultra_instinct_sword_movement"
            ]
          },
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

**`minecraft:wither_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:wither_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "wither_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:wolf_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:wolf_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "wolf_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`sea_sword_sound`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "filters": {
            "operator": "!=",
            "test": "in_water"
          },
          "run_command": {
            "command": [
              "playsound mob.fish.flop @a[r=12] ~ ~ ~ 1 0.6"
            ]
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

**`shoot_ultra_instinct_projectile`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "ultra_instinct_projectile"
        ]
      },
      "remove": {
        "component_groups": [
          "ultra_instinct_projectile"
        ]
      },
      "run_command": {
        "command": [
          "playsound mob.wither.ambient @s ~ ~1 ~ 2 0.6"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`shulker_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
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
  },
  "reference": {
    "present": false
  }
}
```

**`slime_sword_skills`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "ride @s summon_ride entity:mountable_slime no_ride_change",
          "scoreboard objectives add slime_despawn dummy"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`spectral_sword_function`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "filters": {
            "all_of": [
              {
                "operator": "!=",
                "test": "has_biome_tag",
                "value": "nether"
              },
              {
                "operator": "!=",
                "test": "has_biome_tag",
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`spectral_sword_function_1`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "filters": {
            "all_of": [
              {
                "operator": "!=",
                "test": "has_biome_tag",
                "value": "nether"
              },
              {
                "operator": "!=",
                "test": "has_biome_tag",
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`spectral_sword_reload_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:spectral_sword"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "spectral_sword"
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

**`spectral_sword_skills`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "filters": {
            "operator": "!=",
            "test": "has_biome_tag",
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`spider_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "spider_sword_skill"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "spider_sword_skill"
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

**`start_player_explode`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:default_player"
        ]
      },
      "remove": {
        "component_groups": [
          "start_player_explode_event"
        ]
      },
      "run_command": {
        "command": [
          "summon entity:instant_creeper_explode ~ ~1 ~",
          "kill @s"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`start_player_explode_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "start_player_explode_event"
        ]
      },
      "run_command": {
        "command": [
          "playanimation @s animation.player.explode",
          "playsound random.fuse"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`starting_wolf_transformation`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "effect @s nausea 5 0 true"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`stop_bee_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "bee_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:bee_sword"
            ]
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

**`stop_blaze_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
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

**`stop_blaze_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:blaze_sword"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "blaze_sword"
          },
          "remove": {
            "component_groups": [
              "shoot_small_fireball"
            ]
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

**`stop_bone_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "bone_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:bone_sword"
            ]
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

**`stop_cactus_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "cactus_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:cactus_sword"
            ]
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

**`stop_clock_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
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

**`stop_emerald_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "emerald_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:emerald_sword"
            ]
          },
          "run_command": {
            "command": [
              "effect @s village_hero 0 0 true"
            ]
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

**`stop_ender_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "ender_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:ender_sword"
            ]
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

**`stop_fire_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "fire_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:fire_sword"
            ]
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

**`stop_ghost_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "ghost_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:ghost_sword"
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
  },
  "reference": {
    "present": false
  }
}
```

**`stop_grass_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "grass_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:grass_sword"
            ]
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

**`stop_ice_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "ice_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:ice_sword"
            ]
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

**`stop_jungle_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "jungle_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:jungle_sword"
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
  },
  "reference": {
    "present": false
  }
}
```

**`stop_lapis_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "lapis_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:lapis_sword"
            ]
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

**`stop_lightning_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "lightning_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:lightning_sword"
            ]
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

**`stop_magma_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "magma_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:magma_sword"
            ]
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

**`stop_nether_star_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "nether_star_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:nether_star_sword"
            ]
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

**`stop_obsidian_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "obsidian_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:obsidian_sword"
            ]
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

**`stop_quartz_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "quartz_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:quartz_sword"
            ]
          },
          "run_command": {
            "command": [
              "damage @s 14 magic"
            ]
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

**`stop_sea_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "sea_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:sea_sword",
              "mermaid_movement_in_water"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`stop_shulker_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "shulker_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:shulker_sword"
            ]
          },
          "run_command": {
            "command": [
              "ride @s stop_riding"
            ]
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

**`stop_slime_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "slime_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:slime_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`stop_spectral_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
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

**`stop_spider_skill_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:spider_sword"
            ]
          },
          "filters": {
            "subject": "self",
            "test": "is_family",
            "value": "spider_sword_skill"
          },
          "remove": {
            "component_groups": [
              "spider_sword_skill"
            ]
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

**`stop_spider_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "spider_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:spider_sword",
              "spider_sword_skill"
            ]
          },
          "run_command": {
            "command": [
              "ride @s stop_riding"
            ]
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

**`stop_sponge_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "sponge_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:sponge_sword"
            ]
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

**`stop_time_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "time_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:time_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`stop_ultra_instinct_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "ultra_instinct_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:ultra_instinct_sword",
              "ultra_instinct_sword_movement"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`stop_wither_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "wither_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:wither_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`stop_wolf_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
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
          }
        },
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
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

**`stop_wolf_transformation`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "run_command": {
            "command": [
              "effect @s nausea 0 0",
              "effect @s blindness 0 0",
              "stopsound @a wolf_sword.howl",
              "stopsound @a wolf_sword.distant_howl"
            ]
          }
        },
        {
          "add": {
            "component_groups": [
              "minecraft:wolf_sword"
            ]
          },
          "remove": {
            "component_groups": [
              "wolf_transformation",
              "complete_wolf_transformation",
              "wolf_movement"
            ]
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

**`time_sword_movement`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "time_sword_movement"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`ultra_instinct_sword_effects`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "randomize": [
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.3 ~1 ~",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~ ~2 ~0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~-0.3 ~ ~",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~ ~0.3 ~-0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.3 ~1.5 ~0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~-0.3 ~0.8 ~-0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~-0.3 ~2 ~0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.2 ~1 ~0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.3 ~0.9 ~0.1",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.2 ~2.3 ~-0.2",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~-0.3 ~1.2 ~",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.3 ~0.3 ~0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.3 ~0.6 ~0.1",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~-0.3 ~0.2 ~0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.1 ~0.7 ~-0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`ultra_instinct_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "spreadplayers ~ ~ 1 3 @s",
          "playsound mob.endermen.portal @a[r=17] ~ ~ ~ 1 0.6"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`wet_sponge_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "filters": {
            "domain": "hand",
            "subject": "self",
            "test": "has_equipment",
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
  },
  "reference": {
    "present": false
  }
}
```

**`wither_sword_effects`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "randomize": [
        {
          "run_command": {
            "command": [
              "playsound mob.wither.death @a[r=16]"
            ]
          },
          "weight": 50
        },
        {
          "run_command": {
            "command": [
              "playsound mob.wither.hurt @a[r=16]"
            ]
          },
          "weight": 50
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`wolf_damage_sound`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "playsound mob.wolf.bark @a[r=16] ~ ~ ~ 1 0.55"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`wolf_movement`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "wolf_movement"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`wolf_sword_sounds`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "randomize": [
        {
          "run_command": {
            "command": [
              "playsound mob.wolf.growl @a[r=16] ~ ~ ~ 1 0.9 24"
            ]
          },
          "weight": 1
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`wolf_sword_start_events`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "wolf_transformation"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "wolf_transformation"
          },
          "run_command": {
            "command": [
              "function commands/swords_and_more_swords/swords_and_more_swords/tellraw1"
            ]
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

**`wolf_transformation`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "complete_wolf_transformation"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "complete_wolf_transformation"
          },
          "run_command": {
            "command": [
              "playsound random.fizz @a[r=16] ~~~",
              "playsound wolf_sword.howl @a[r=24] ~~~",
              "playsound wolf_sword.distant_howl @a[rm=25,r=100]",
              "particle minecraft:egg_destroy_emitter ~ ~ ~",
              "particle minecraft:egg_destroy_emitter ~ ~0.5 ~",
              "particle minecraft:egg_destroy_emitter ~ ~0.8 ~"
            ]
          }
        },
        {
          "filters": {
            "test": "is_family",
            "value": "wolf_transformation"
          },
          "remove": {
            "component_groups": [
              "wolf_transformation"
            ]
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

##### `root`

**`format_version`**

```json
{
  "addon": {
    "present": true,
    "value": "1.11.0"
  },
  "reference": {
    "present": true,
    "value": "1.18.20"
  }
}
```

### Аддон `2.8.8`

SHA-256 файла: `2f499faf84dfc33f9ad0ad0d43ae18b3645ba4c15213b79a511ac7b6776972a3`.

#### Образец `1.19.40.2`

SHA-256 файла образца: `e6da0c426bfd839336c7f447101bf29af3d68e420dcab3a493b28ff84d31b8ad`.

##### `component_groups`

**`blaze_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:timer": {
        "looping": false,
        "time": [
          6,
          6
        ],
        "time_down_event": {
          "event": "blaze_sword_skill",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "blaze_sword",
          "blaze_sword_skill"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`clock_sword_movement`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:movement": {
        "value": 1
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`clock_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:timer": {
        "looping": true,
        "randomInterval": false,
        "time": [
          5,
          5
        ],
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`complete_wolf_transformation`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:attack": {
        "damage": 15
      },
      "minecraft:damage_sensor": {
        "triggers": [
          {
            "deals_damage": true,
            "on_damage": {
              "event": "wolf_damage_sound",
              "filters": {
                "all_of": [
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "void"
                  }
                ]
              }
            }
          }
        ]
      },
      "minecraft:timer": {
        "looping": true,
        "randomInterval": true,
        "time": [
          3,
          6
        ],
        "time_down_event": {
          "event": "wolf_sword_sounds",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "wolf",
          "wolf_sword",
          "complete_wolf_transformation",
          "monster"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`despawn`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:despawn": {}
    }
  },
  "reference": {
    "present": false
  }
}
```

**`ghost_movement`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:movement": {
        "value": 0.14
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`mermaid_movement_in_water`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:underwater_movement": {
        "value": 0.07
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`mermaid_movement_out_water`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:movement": {
        "value": 0.06
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:add_bad_omen`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spell_effects": {
        "add_effects": [
          {
            "display_on_screen_animation": true,
            "duration": 6000,
            "effect": "bad_omen"
          }
        ]
      },
      "minecraft:timer": {
        "looping": false,
        "time": [
          0.0,
          0.0
        ],
        "time_down_event": {
          "event": "minecraft:clear_add_bad_omen",
          "target": "self"
        }
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:spell_effects": {
        "add_effects": [
          {
            "display_on_screen_animation": true,
            "duration": 6000,
            "effect": "bad_omen",
            "visible": false
          }
        ]
      },
      "minecraft:timer": {
        "looping": false,
        "time": [
          0.0,
          0.0
        ],
        "time_down_event": {
          "event": "minecraft:clear_add_bad_omen",
          "target": "self"
        }
      }
    }
  }
}
```

**`minecraft:bee_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:timer": {
        "looping": true,
        "randomInterval": true,
        "time": [
          3,
          8
        ],
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
  "reference": {
    "present": false
  }
}
```

**`minecraft:blaze_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": false,
          "on_damage": {
            "filters": {
              "any_of": [
                {
                  "subject": "self",
                  "test": "has_damage",
                  "value": "fire"
                },
                {
                  "subject": "self",
                  "test": "has_damage",
                  "value": "fire_tick"
                }
              ]
            }
          }
        }
      },
      "minecraft:hurt_on_condition": {
        "damage_conditions": [
          {
            "cause": "drowning",
            "damage_per_tick": 1,
            "filters": {
              "test": "in_water_or_rain"
            }
          }
        ]
      },
      "minecraft:timer": {
        "looping": true,
        "time": [
          1,
          1
        ],
        "time_down_event": {
          "event": "blaze_sword_effects",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "blaze_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:bone_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:timer": {
        "looping": true,
        "time": [
          1,
          1
        ],
        "time_down_event": {
          "event": "bone_sword_skills",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "bone_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:cactus_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:timer": {
        "looping": true,
        "time": [
          0.5,
          0.5
        ],
        "time_down_event": {
          "event": "cactus_sword_skills",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "cactus_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:clock_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:type_family": {
        "family": [
          "player",
          "clock_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:default_player`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:attack": {
        "damage": 1
      },
      "minecraft:breathable": {
        "generates_bubbles": false,
        "inhale_time": 3.75,
        "suffocate_time": -1,
        "total_supply": 15
      },
      "minecraft:collision_box": {
        "height": 1.8,
        "width": 0.6
      },
      "minecraft:damage_sensor": {},
      "minecraft:health": {
        "max": 20,
        "value": 20
      },
      "minecraft:movement": {
        "value": 0.1
      },
      "minecraft:physics": {
        "has_collision": true,
        "has_gravity": true
      },
      "minecraft:rideable": {
        "family_types": [
          "parrot_tame"
        ],
        "pull_in_entities": true,
        "seat_count": 2,
        "seats": [
          {
            "lock_rider_rotation": 0,
            "max_rider_count": 0,
            "min_rider_count": 0,
            "position": [
              0.4,
              -0.2,
              -0.1
            ]
          },
          {
            "lock_rider_rotation": 0,
            "max_rider_count": 2,
            "min_rider_count": 1,
            "position": [
              -0.4,
              -0.2,
              -0.1
            ]
          }
        ]
      },
      "minecraft:scale": {
        "value": 1
      },
      "minecraft:timer": {},
      "minecraft:type_family": {
        "family": [
          "player",
          "default_player"
        ]
      },
      "minecraft:underwater_movement": {
        "value": 0.02
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:emerald_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:type_family": {
        "family": [
          "player",
          "emerald_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:ender_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": [
          {
            "deals_damage": true,
            "on_damage": {
              "event": "ender_sword_skill",
              "filters": {
                "all_of": [
                  {
                    "operator": "!=",
                    "subject": "self",
                    "test": "has_damage",
                    "value": "projectile"
                  }
                ]
              }
            }
          },
          {
            "deals_damage": false,
            "on_damage": {
              "event": "ender_sword_tp",
              "filters": {
                "all_of": [
                  {
                    "subject": "self",
                    "test": "has_damage",
                    "value": "projectile"
                  }
                ]
              }
            }
          },
          {
            "deals_damage": true,
            "on_damage": {
              "event": "ender_sword_tp",
              "filters": {
                "all_of": [
                  {
                    "test": "in_water_or_rain"
                  }
                ]
              }
            }
          }
        ]
      },
      "minecraft:hurt_on_condition": {
        "damage_conditions": [
          {
            "cause": "drowning",
            "damage_per_tick": 1,
            "filters": {
              "test": "in_water_or_rain"
            }
          }
        ]
      },
      "minecraft:timer": {
        "looping": true,
        "randomInterval": true,
        "time": [
          6,
          18
        ],
        "time_down_event": {
          "event": "ender_sword_sound",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "ender_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:fire_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": false,
          "on_damage": {
            "filters": {
              "any_of": [
                {
                  "subject": "self",
                  "test": "has_damage",
                  "value": "fire"
                },
                {
                  "subject": "self",
                  "test": "has_damage",
                  "value": "fire_tick"
                }
              ]
            }
          }
        }
      },
      "minecraft:timer": {
        "looping": true,
        "randomInterval": true,
        "time": [
          0.2,
          0.7
        ],
        "time_down_event": {
          "event": "fire_sword_sound",
          "target": "self"
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
  "reference": {
    "present": false
  }
}
```

**`minecraft:ghost_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:breathable": {
        "breathes_air": true,
        "breathes_lava": true,
        "breathes_water": true,
        "generates_bubbles": false,
        "inhale_time": 3.75,
        "suffocate_time": 0,
        "total_supply": 15
      },
      "minecraft:collision_box": {
        "height": 0.0,
        "width": 0.0
      },
      "minecraft:damage_sensor": {
        "triggers": {
          "cause": "all",
          "deals_damage": false
        }
      },
      "minecraft:knockback_resistance": {
        "value": 1.0
      },
      "minecraft:scale": {
        "value": 1.05
      },
      "minecraft:type_family": {
        "family": [
          "ghost_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:grass_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:timer": {
        "looping": true,
        "time": [
          0.2,
          0.2
        ],
        "time_down_event": {
          "event": "grass_sword_skills",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "grass_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:ice_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:type_family": {
        "family": [
          "player",
          "ice_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:jungle_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:health": {
        "max": 8,
        "value": 8
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "jungle_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:lapis_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:timer": {
        "looping": true,
        "randomInterval": true,
        "time": [
          2.5,
          6.0
        ],
        "time_down_event": {
          "event": "lapis_sword_skills",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "lapis_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:lightning_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": false,
          "on_damage": {
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "lightning"
                }
              ]
            }
          }
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
  "reference": {
    "present": false
  }
}
```

**`minecraft:magma_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": false,
          "on_damage": {
            "filters": {
              "any_of": [
                {
                  "subject": "self",
                  "test": "has_damage",
                  "value": "fire_tick"
                },
                {
                  "operator": "equals",
                  "subject": "block",
                  "test": "is_block",
                  "value": "magma"
                }
              ]
            }
          }
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
  "reference": {
    "present": false
  }
}
```

**`minecraft:nether_star_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": false,
          "on_damage": {
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "nether_star_projectile"
                }
              ]
            }
          }
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
  "reference": {
    "present": false
  }
}
```

**`minecraft:obsidian_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": false,
          "on_damage": {
            "filters": {
              "any_of": [
                {
                  "subject": "self",
                  "test": "has_damage",
                  "value": "block_explosion"
                },
                {
                  "subject": "self",
                  "test": "has_damage",
                  "value": "entity_explosion"
                }
              ]
            }
          }
        }
      },
      "minecraft:knockback_resistance": {
        "value": 1.0
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "obsidian_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:quartz_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:type_family": {
        "family": [
          "player",
          "quartz_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:sea_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:breathable": {
        "breathes_air": false,
        "breathes_lava": false,
        "breathes_water": true,
        "generates_bubbles": false,
        "inhale_time": 3.75,
        "suffocate_time": -1,
        "total_supply": 2
      },
      "minecraft:collision_box": {
        "height": 0.9,
        "width": 0.6
      },
      "minecraft:timer": {
        "looping": true,
        "time": [
          0.5,
          0.5
        ],
        "time_down_event": {
          "event": "sea_sword_sound",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "sea_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:shulker_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:scale": {
        "value": 1
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "shulker_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:slime_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": false,
          "on_damage": {
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "tamed_slime"
                }
              ]
            }
          }
        }
      },
      "minecraft:timer": {
        "looping": false,
        "time": [
          0.4,
          0.4
        ],
        "time_down_event": {
          "event": "slime_sword_skills",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "slime_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:spectral_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:rideable": {
        "family_types": [
          "ender_crystal",
          "spectral_sword"
        ],
        "seat_count": 1,
        "seats": {
          "lock_rider_rotation": 0,
          "position": [
            0.0,
            0.4,
            0.0
          ]
        }
      },
      "minecraft:timer": {
        "looping": false,
        "time": [
          0.4,
          0.4
        ],
        "time_down_event": {
          "event": "spectral_sword_skills",
          "target": "self"
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
  "reference": {
    "present": false
  }
}
```

**`minecraft:spider_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:type_family": {
        "family": [
          "player",
          "spider_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:sponge_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:type_family": {
        "family": [
          "player",
          "sponge_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:time_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:movement": {
        "value": 1
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "time_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:ultra_instinct_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": [
          {
            "deals_damage": false,
            "on_damage": {
              "event": "ultra_instinct_sword_skill",
              "filters": {
                "all_of": [
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "lava"
                  },
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "drowning"
                  },
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "void"
                  },
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "thorns"
                  },
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "suicide"
                  },
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "starve"
                  },
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "fire"
                  },
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "fire_tick"
                  },
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "magic"
                  }
                ]
              }
            }
          },
          {
            "deals_damage": false,
            "on_damage": {
              "filters": {
                "test": "has_damage",
                "value": "fire"
              }
            }
          },
          {
            "deals_damage": false,
            "on_damage": {
              "filters": {
                "test": "has_damage",
                "value": "fire_tick"
              }
            }
          },
          {
            "deals_damage": false,
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
            }
          },
          {
            "deals_damage": true,
            "on_damage": {
              "filters": {
                "all_of": [
                  {
                    "test": "has_damage",
                    "value": "lava"
                  }
                ]
              }
            }
          }
        ]
      },
      "minecraft:knockback_resistance": {
        "value": 1.0
      },
      "minecraft:timer": {
        "looping": true,
        "randomInterval": true,
        "time": [
          0.1,
          0.2
        ],
        "time_down_event": {
          "event": "ultra_instinct_sword_effects",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "ultra_instinct_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:wither_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": false,
          "on_damage": {
            "filters": {
              "all_of": [
                {
                  "subject": "self",
                  "test": "has_damage",
                  "value": "wither"
                }
              ]
            }
          }
        }
      },
      "minecraft:rideable": {
        "family_types": [
          "entity_name"
        ],
        "seat_count": 1,
        "seats": {
          "lock_rider_rotation": 0,
          "position": [
            0.0,
            0.4,
            0.0
          ]
        }
      },
      "minecraft:timer": {
        "looping": true,
        "randomInterval": true,
        "time": [
          4,
          18
        ],
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
  "reference": {
    "present": false
  }
}
```

**`minecraft:wolf_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:type_family": {
        "family": [
          "player",
          "wolf_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`shoot_small_fireball`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 1,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:fake_fireball",
          "spawn_event": "set_sound"
        },
        {
          "max_wait_time": 1,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:fake_fireball",
          "spawn_event": "set_sound"
        },
        {
          "max_wait_time": 1,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:fake_fireball",
          "spawn_event": "set_sound"
        },
        {
          "max_wait_time": 1,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:fake_fireball",
          "spawn_event": "set_sound"
        }
      ],
      "minecraft:timer": {
        "looping": false,
        "time": [
          2,
          2
        ],
        "time_down_event": {
          "event": "stop_blaze_sword_skill",
          "target": "self"
        }
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`shulker_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
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
  "reference": {
    "present": false
  }
}
```

**`spider_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": false,
          "spawn_entity": "entity:web"
        }
      ],
      "minecraft:timer": {
        "looping": false,
        "time": [
          2,
          2
        ],
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
  "reference": {
    "present": false
  }
}
```

**`start_player_explode_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:movement": {
        "value": 0.0
      },
      "minecraft:timer": {
        "looping": true,
        "time": [
          1.5,
          1.5
        ],
        "time_down_event": {
          "event": "start_player_explode",
          "target": "self"
        }
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`time_sword_movement`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:movement": {
        "value": 1
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`ultra_instinct_projectile`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:ultra_instinct_projectile"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`ultra_instinct_sword_movement`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:movement": {
        "value": 0.22
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`wolf_movement`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:movement": {
        "value": 0.18
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`wolf_transformation`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:type_family": {
        "family": [
          "player",
          "wolf_sword",
          "wolf_transformation"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

##### `components`

**`minecraft:block_climber`**

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

**`minecraft:environment_sensor`**

```json
{
  "addon": {
    "present": true,
    "value": [
      {
        "on_environment": {
          "event": "minecraft:trigger_raid",
          "filters": {
            "all_of": [
              {
                "subject": "self",
                "test": "has_mob_effect",
                "value": "bad_omen"
              },
              {
                "subject": "self",
                "test": "is_in_village",
                "value": true
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:constant_events",
          "filters": {
            "operator": "!=",
            "test": "is_family",
            "value": "null"
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:stop_sword_events",
          "filters": {
            "any_of": [
              {
                "subject": "self",
                "test": "is_family",
                "value": "default_player"
              },
              {
                "operator": "!=",
                "subject": "self",
                "test": "is_family",
                "value": "spectral_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:blaze_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:blaze_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_blaze_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:blaze_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:bone_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:bone_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_bone_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:bone_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:cactus_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:cactus_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_cactus_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:cactus_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:emerald_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:emerald_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_emerald_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:emerald_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:fire_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:fire_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_fire_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:fire_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:grass_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:grass_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_grass_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:grass_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:jungle_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:jungle_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_jungle_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:jungle_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:magma_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:magma_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_magma_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:magma_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:ice_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:ice_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_ice_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:ice_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:lapis_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:lapis_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_lapis_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:lapis_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:obsidian_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:obsidian_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_obsidian_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:obsidian_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:quartz_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:quartz_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_quartz_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:quartz_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:sea_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:sea_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_sea_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:sea_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:spectral_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:spectral_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_spectral_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:spectral_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:slime_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:slime_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_slime_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:slime_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:shulker_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:shulker_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_shulker_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:shulker_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:spider_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:spider_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_spider_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:spider_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:sponge_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:sponge_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_sponge_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:sponge_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:time_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:time_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_time_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:time_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:wither_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:wither_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_wither_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:wither_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:glowstone_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:glowstone_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:lightning_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:lightning_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_lightning_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:lightning_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:ender_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:ender_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_ender_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:ender_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:ultra_instinct_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:ultra_instinct_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_ultra_instinct_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:ultra_instinct_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:wolf_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:wolf_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_wolf_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:wolf_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "starting_wolf_transformation",
          "filters": {
            "all_of": [
              {
                "test": "is_family",
                "value": "wolf_transformation"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "wolf_movement",
          "filters": {
            "all_of": [
              {
                "test": "is_family",
                "value": "complete_wolf_transformation"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:ghost_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:ghost_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_ghost_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:ghost_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:clock_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:clock_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_clock_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:clock_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:nether_star_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:nether_star_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_nether_star_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:nether_star_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:bee_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:bee_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_bee_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:bee_sword"
              }
            ]
          }
        }
      }
    ]
  },
  "reference": {
    "present": true,
    "value": {
      "triggers": {
        "event": "minecraft:trigger_raid",
        "filters": {
          "all_of": [
            {
              "subject": "self",
              "test": "has_mob_effect",
              "value": "bad_omen"
            },
            {
              "subject": "self",
              "test": "is_in_village",
              "value": true
            }
          ]
        }
      }
    }
  }
}
```

**`minecraft:exhaustion_values`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "attack": 0.1,
      "damage": 0.1,
      "heal": 6,
      "jump": 0.05,
      "mine": 0.005,
      "sprint": 0.1,
      "sprint_jump": 0.2,
      "swim": 0.01,
      "walk": 0.0
    }
  }
}
```

**`minecraft:player.exhaustion`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "max": 4,
      "value": 0
    }
  },
  "reference": {
    "present": true,
    "value": {
      "max": 20,
      "value": 0
    }
  }
}
```

**`minecraft:player.saturation`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "value": 20
    }
  },
  "reference": {
    "present": true,
    "value": {
      "max": 20,
      "value": 5
    }
  }
}
```

**`minecraft:scaffolding_climber`**

```json
{
  "addon": {
    "present": true,
    "value": {}
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:type_family`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "family": [
        "player",
        "default_player"
      ]
    }
  },
  "reference": {
    "present": true,
    "value": {
      "family": [
        "player"
      ]
    }
  }
}
```

##### `description`

**`animations`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "ghost_sword": "controller.animation.ghost_sword",
      "shulker_sword": "controller.animation.shulker_sword",
      "wither_sword": "controller.animation.wither_sword",
      "wolf_sword_0": "controller.animation.wolf_sword",
      "wolf_sword_1": "controller.animation.start_wolf_sword",
      "wolf_sword_2": "controller.animation.end_wolf_sword"
    }
  },
  "reference": {
    "present": false
  }
}
```

**`scripts`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "animate": [
        "shulker_sword",
        "wither_sword",
        "wolf_sword_0",
        "wolf_sword_1",
        "wolf_sword_2",
        "ghost_sword"
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

##### `events`

**`bee_sword_flower`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "randomize": [
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 0"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 1"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 2"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 4"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 5"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 6"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 7"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 8"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 9"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 10"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ yellow_flower 0"
            ]
          },
          "weight": 1
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`blaze_sword_effects`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "randomize": [
        {
          "run_command": {
            "command": [
              "particle minecraft:mobflame_single ~ ~0.2 ~"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:mobflame_single ~0.3 ~0.2 ~"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:mobflame_single ~ ~0.2 ~0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:mobflame_single ~-0.3 ~0.2 ~"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:mobflame_single ~ ~0.2 ~-0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "playsound mob.blaze.breathe @a[r=12] ~ ~ ~ 0.5"
            ]
          },
          "weight": 1
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`blaze_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "shoot_small_fireball"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`blaze_sword_skill_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "blaze_sword_skill"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`bone_sword_skills`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "summon entity:grows_crop ~ ~0.1 ~ grows_crop_event"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`cactus_sword_skills`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "damage @e[r=1.4,type=!player] 1 contact entity @s",
          "damage @s 1 contact"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`clock_sword_movement`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "clock_sword_movement"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`clock_sword_skill_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "clock_sword_skill"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`default_player`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:default_player"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`despawn`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "despawn"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`ender_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
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
              "run_command": {
                "command": [
                  "spreadplayers ~ ~ 0 16 @s",
                  "playsound mob.endermen.portal @a[r=17]"
                ]
              },
              "weight": 50
            }
          ]
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`ender_sword_sound`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "randomize": [
        {
          "run_command": {
            "command": [
              "playsound mob.endermen.scream @a[r=8] ~ ~ ~"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "playsound mob.endermen.idle @a[r=8] ~ ~ ~"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "playsound mob.endermen.stare @a[r=8] ~ ~ ~"
            ]
          },
          "weight": 1
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`ender_sword_tp`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "spreadplayers ~ ~ 0 16 @s",
          "playsound mob.endermen.portal @a[r=17]"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`fire_sword_sound`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "playsound fire.fire @a[r=8]"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`grass_sword_skills`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "execute @e[type=!player,type=!item,type=!entity:grass,type=!xp_orb,type=!arrow,r=8,tag=!grass] ~ ~ ~ detect ~ ~-0.1 ~ grass 0 execute @s ~ ~ ~ detect ~ ~ ~ air 0 summon entity:grass",
          "execute @e[type=!player,type=!item,type=!entity:grass,type=!xp_orb,type=!arrow,r=8,tag=!grass] ~ ~ ~ detect ~ ~-0.1 ~ grass 0 execute @s ~ ~ ~ detect ~ ~ ~ tallgrass 0 summon entity:grass"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`lapis_sword_skills`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "xp 5 @s",
          "playsound random.orb @s ~ ~ ~ 0.3"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:bee_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:bee_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "bee_sword"
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

**`minecraft:blaze_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:blaze_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "blaze_sword"
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
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "blaze_sword_skill"
          },
          "randomize": [
            {
              "run_command": {
                "command": [
                  "particle minecraft:mobflame_single ~ ~0.2 ~"
                ]
              },
              "weight": 5
            },
            {
              "run_command": {
                "command": [
                  "particle minecraft:mobflame_single ~0.3 ~0.2 ~"
                ]
              },
              "weight": 5
            },
            {
              "run_command": {
                "command": [
                  "particle minecraft:mobflame_single ~ ~0.2 ~0.3"
                ]
              },
              "weight": 5
            },
            {
              "run_command": {
                "command": [
                  "particle minecraft:mobflame_single ~-0.3 ~0.2 ~"
                ]
              },
              "weight": 5
            },
            {
              "run_command": {
                "command": [
                  "particle minecraft:mobflame_single ~ ~0.2 ~-0.3"
                ]
              },
              "weight": 5
            },
            {
              "run_command": {
                "command": [
                  "playsound mob.blaze.breathe @a[r=12] ~ ~ ~ 0.5"
                ]
              },
              "weight": 5
            },
            {
              "weight": 95
            }
          ]
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:bone_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:bone_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "bone_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:cactus_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:cactus_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "cactus_sword"
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

**`minecraft:clock_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:clock_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "clock_sword"
          }
        },
        {
          "add": {
            "component_groups": [
              "clock_sword_movement"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "clock_sword_skill"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:constant_events`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "run_command": {
            "command": [
              "function commands/swords_and_more_swords/swords_and_more_swords/tag_swords",
              "gamerule sendcommandfeedback false",
              "gamerule commandblockoutput false",
              "scoreboard objectives add Effect99 dummy",
              "scoreboard players add @s Effect99 1",
              "title @s[scores={Effect99=12000}] actionbar §l§fCreated by §7Effect99",
              "scoreboard players set @s[scores={Effect99=36001}] Effect99 1"
            ]
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

**`minecraft:emerald_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:emerald_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "emerald_sword"
          }
        },
        {
          "filters": {
            "all_of": [
              {
                "subject": "self",
                "test": "is_in_village",
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:ender_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:ender_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "ender_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:fire_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:fire_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "fire_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:ghost_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:ghost_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "ghost_sword"
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
          "add": {
            "component_groups": [
              "ghost_movement"
            ]
          },
          "run_command": {
            "command": [
              "effect @s slow_falling 1 0 true",
              "effect @s saturation 1 1 true"
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
            "operator": "!=",
            "test": "in_lava"
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
              "run_command": {
                "command": [
                  "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 0.15 0.2"
                ]
              },
              "weight": 10
            }
          ]
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:glowstone_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock 0 replace air",
          "fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock 0 replace effect99:lightblock"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:grass_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:grass_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "grass_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:ice_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:ice_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "ice_sword"
          }
        },
        {
          "filters": {
            "all_of": [
              {
                "test": "in_lava"
              },
              {
                "operator": "!=",
                "test": "has_biome_tag",
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:jungle_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:jungle_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "jungle_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:lapis_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:lapis_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "lapis_sword"
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

**`minecraft:lightning_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:lightning_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "lightning_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:magma_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:magma_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "magma_sword"
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
            "operator": "==",
            "test": "in_water"
          },
          "randomize": [
            {
              "weight": 99
            },
            {
              "run_command": {
                "command": [
                  "playsound bubble.up @a ~ ~ ~ 1 0.9"
                ]
              },
              "weight": 1
            }
          ]
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:nether_star_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:nether_star_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "nether_star_sword"
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

**`minecraft:obsidian_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:obsidian_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "obsidian_sword"
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

**`minecraft:quartz_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:quartz_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "quartz_sword"
          },
          "run_command": {
            "command": [
              "damage @s 14 magic"
            ]
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

**`minecraft:sea_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "mermaid_movement_out_water"
            ]
          },
          "filters": {
            "operator": "!=",
            "test": "in_water"
          },
          "run_command": {
            "command": [
              "camerashake add @s 0.01 1 positional",
              "effect @s conduit_power 0 0"
            ]
          }
        },
        {
          "add": {
            "component_groups": [
              "minecraft:sea_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "sea_sword"
          },
          "run_command": {
            "command": [
              "particle minecraft:example_bounce ~ ~ ~",
              "playsound random.splash @a[r=12] ~ ~ ~ 0.5"
            ]
          }
        },
        {
          "add": {
            "component_groups": [
              "mermaid_movement_in_water"
            ]
          },
          "filters": {
            "test": "in_water"
          },
          "run_command": {
            "command": [
              "effect @s conduit_power 1 0 true"
            ]
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

**`minecraft:shulker_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:shulker_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "shulker_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:slime_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:slime_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "slime_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:spectral_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:spectral_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "spectral_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:spider_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:spider_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "spider_sword"
          },
          "run_command": {
            "command": [
              "ride @s summon_ride minecraft:spider no_ride_change minecraft:spider_sword",
              "particle minecraft:example_linearcurve ~ ~ ~"
            ]
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

**`minecraft:sponge_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:sponge_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "sponge_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:stop_sword_events`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "run_command": {
            "command": [
              "execute @e[r=64,type=!player] ~ ~ ~ detect ~ ~ ~ ice 0 tp @s ~ ~ ~"
            ]
          }
        },
        {
          "filters": {
            "all_of": [
              {
                "operator": "!=",
                "test": "has_biome_tag",
                "value": "nether"
              },
              {
                "operator": "!=",
                "test": "has_biome_tag",
                "value": "the_end"
              }
            ]
          },
          "run_command": {
            "command": [
              "fill ~6 ~6 ~6 ~-6 ~-6 ~-6 stone 0 replace effect99:spectral_block",
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
              "fill ~6 ~6 ~6 ~-6 ~-6 ~-6 netherrack 0 replace effect99:spectral_block",
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
              "fill ~6 ~6 ~6 ~-6 ~-6 ~-6 end_stone 0 replace effect99:spectral_block",
              "fill ~7 ~8 ~8 ~8 ~-8 ~-8 end_stone 0 replace effect99:spectral_block",
              "fill ~-7 ~-8 ~-8 ~-8 ~8 ~8 end_stone 0 replace effect99:spectral_block",
              "fill ~-6 ~8 ~7 ~6 ~-8 ~8 end_stone 0 replace effect99:spectral_block",
              "fill ~6 ~-8 ~-7 ~-6 ~8 ~-8 end_stone 0 replace effect99:spectral_block",
              "fill ~8 ~-8 ~8 ~-8 ~-7 ~-8 end_stone 0 replace effect99:spectral_block",
              "fill ~8 ~8 ~8 ~-8 ~7 ~-8 end_stone 0 replace effect99:spectral_block"
            ]
          }
        },
        {
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:slime_sword"
              }
            ]
          },
          "run_command": {
            "command": [
              "ride @e[type=entity:mountable_slime,r=1,y=~-1] evict_riders"
            ]
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

**`minecraft:time_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:ultra_instinct_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:ultra_instinct_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "ultra_instinct_sword"
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
          "add": {
            "component_groups": [
              "ultra_instinct_sword_movement"
            ]
          },
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

**`minecraft:wither_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:wither_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "wither_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:wolf_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:wolf_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "wolf_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`sea_sword_sound`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "filters": {
            "operator": "!=",
            "test": "in_water"
          },
          "run_command": {
            "command": [
              "playsound mob.fish.flop @a[r=12] ~ ~ ~ 1 0.6"
            ]
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

**`shoot_ultra_instinct_projectile`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "ultra_instinct_projectile"
        ]
      },
      "remove": {
        "component_groups": [
          "ultra_instinct_projectile"
        ]
      },
      "run_command": {
        "command": [
          "playsound mob.wither.ambient @s ~ ~1 ~ 2 0.6"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`shulker_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
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
  },
  "reference": {
    "present": false
  }
}
```

**`slime_sword_skills`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "ride @s summon_ride entity:mountable_slime no_ride_change",
          "scoreboard objectives add slime_despawn dummy"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`spectral_sword_function`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "filters": {
            "all_of": [
              {
                "operator": "!=",
                "test": "has_biome_tag",
                "value": "nether"
              },
              {
                "operator": "!=",
                "test": "has_biome_tag",
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`spectral_sword_function_1`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "filters": {
            "all_of": [
              {
                "operator": "!=",
                "test": "has_biome_tag",
                "value": "nether"
              },
              {
                "operator": "!=",
                "test": "has_biome_tag",
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`spectral_sword_reload_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:spectral_sword"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "spectral_sword"
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

**`spectral_sword_skills`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "filters": {
            "operator": "!=",
            "test": "has_biome_tag",
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`spider_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "spider_sword_skill"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "spider_sword_skill"
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

**`start_player_explode`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:default_player"
        ]
      },
      "remove": {
        "component_groups": [
          "start_player_explode_event"
        ]
      },
      "run_command": {
        "command": [
          "summon entity:instant_creeper_explode ~ ~1 ~",
          "kill @s"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`start_player_explode_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "start_player_explode_event"
        ]
      },
      "run_command": {
        "command": [
          "playanimation @s animation.player.explode",
          "playsound random.fuse"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`starting_wolf_transformation`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "effect @s nausea 5 0 true"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`stop_bee_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "bee_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:bee_sword"
            ]
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

**`stop_blaze_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
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

**`stop_blaze_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:blaze_sword"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "blaze_sword"
          },
          "remove": {
            "component_groups": [
              "shoot_small_fireball"
            ]
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

**`stop_bone_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "bone_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:bone_sword"
            ]
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

**`stop_cactus_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "cactus_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:cactus_sword"
            ]
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

**`stop_clock_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
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

**`stop_emerald_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "emerald_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:emerald_sword"
            ]
          },
          "run_command": {
            "command": [
              "effect @s village_hero 0 0 true"
            ]
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

**`stop_ender_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "ender_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:ender_sword"
            ]
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

**`stop_fire_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "fire_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:fire_sword"
            ]
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

**`stop_ghost_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "ghost_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:ghost_sword"
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
  },
  "reference": {
    "present": false
  }
}
```

**`stop_grass_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "grass_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:grass_sword"
            ]
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

**`stop_ice_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "ice_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:ice_sword"
            ]
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

**`stop_jungle_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "jungle_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:jungle_sword"
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
  },
  "reference": {
    "present": false
  }
}
```

**`stop_lapis_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "lapis_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:lapis_sword"
            ]
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

**`stop_lightning_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "lightning_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:lightning_sword"
            ]
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

**`stop_magma_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "magma_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:magma_sword"
            ]
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

**`stop_nether_star_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "nether_star_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:nether_star_sword"
            ]
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

**`stop_obsidian_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "obsidian_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:obsidian_sword"
            ]
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

**`stop_quartz_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "quartz_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:quartz_sword"
            ]
          },
          "run_command": {
            "command": [
              "damage @s 14 magic"
            ]
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

**`stop_sea_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "sea_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:sea_sword",
              "mermaid_movement_in_water"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`stop_shulker_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "shulker_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:shulker_sword"
            ]
          },
          "run_command": {
            "command": [
              "ride @s stop_riding"
            ]
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

**`stop_slime_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "slime_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:slime_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`stop_spectral_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
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

**`stop_spider_skill_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:spider_sword"
            ]
          },
          "filters": {
            "subject": "self",
            "test": "is_family",
            "value": "spider_sword_skill"
          },
          "remove": {
            "component_groups": [
              "spider_sword_skill"
            ]
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

**`stop_spider_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "spider_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:spider_sword",
              "spider_sword_skill"
            ]
          },
          "run_command": {
            "command": [
              "ride @s stop_riding"
            ]
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

**`stop_sponge_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "sponge_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:sponge_sword"
            ]
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

**`stop_time_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "time_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:time_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`stop_ultra_instinct_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "ultra_instinct_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:ultra_instinct_sword",
              "ultra_instinct_sword_movement"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`stop_wither_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "wither_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:wither_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`stop_wolf_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
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
          }
        },
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
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

**`stop_wolf_transformation`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "run_command": {
            "command": [
              "effect @s nausea 0 0",
              "effect @s blindness 0 0",
              "stopsound @a wolf_sword.howl",
              "stopsound @a wolf_sword.distant_howl"
            ]
          }
        },
        {
          "add": {
            "component_groups": [
              "minecraft:wolf_sword"
            ]
          },
          "remove": {
            "component_groups": [
              "wolf_transformation",
              "complete_wolf_transformation",
              "wolf_movement"
            ]
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

**`time_sword_movement`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "time_sword_movement"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`ultra_instinct_sword_effects`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "randomize": [
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.3 ~1 ~",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~ ~2 ~0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~-0.3 ~ ~",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~ ~0.3 ~-0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.3 ~1.5 ~0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~-0.3 ~0.8 ~-0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~-0.3 ~2 ~0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.2 ~1 ~0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.3 ~0.9 ~0.1",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.2 ~2.3 ~-0.2",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~-0.3 ~1.2 ~",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.3 ~0.3 ~0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.3 ~0.6 ~0.1",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~-0.3 ~0.2 ~0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.1 ~0.7 ~-0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`ultra_instinct_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "spreadplayers ~ ~ 1 3 @s",
          "playsound mob.endermen.portal @a[r=17] ~ ~ ~ 1 0.6"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`wet_sponge_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "filters": {
            "domain": "hand",
            "subject": "self",
            "test": "has_equipment",
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
  },
  "reference": {
    "present": false
  }
}
```

**`wither_sword_effects`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "randomize": [
        {
          "run_command": {
            "command": [
              "playsound mob.wither.death @a[r=16]"
            ]
          },
          "weight": 50
        },
        {
          "run_command": {
            "command": [
              "playsound mob.wither.hurt @a[r=16]"
            ]
          },
          "weight": 50
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`wolf_damage_sound`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "playsound mob.wolf.bark @a[r=16] ~ ~ ~ 1 0.55"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`wolf_movement`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "wolf_movement"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`wolf_sword_sounds`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "randomize": [
        {
          "run_command": {
            "command": [
              "playsound mob.wolf.growl @a[r=16] ~ ~ ~ 1 0.9 24"
            ]
          },
          "weight": 1
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`wolf_sword_start_events`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "wolf_transformation"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "wolf_transformation"
          },
          "run_command": {
            "command": [
              "function commands/swords_and_more_swords/swords_and_more_swords/tellraw1"
            ]
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

**`wolf_transformation`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "complete_wolf_transformation"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "complete_wolf_transformation"
          },
          "run_command": {
            "command": [
              "playsound random.fizz @a[r=16] ~~~",
              "playsound wolf_sword.howl @a[r=24] ~~~",
              "playsound wolf_sword.distant_howl @a[rm=25,r=100]",
              "particle minecraft:egg_destroy_emitter ~ ~ ~",
              "particle minecraft:egg_destroy_emitter ~ ~0.5 ~",
              "particle minecraft:egg_destroy_emitter ~ ~0.8 ~"
            ]
          }
        },
        {
          "filters": {
            "test": "is_family",
            "value": "wolf_transformation"
          },
          "remove": {
            "component_groups": [
              "wolf_transformation"
            ]
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

##### `root`

**`format_version`**

```json
{
  "addon": {
    "present": true,
    "value": "1.11.0"
  },
  "reference": {
    "present": true,
    "value": "1.18.20"
  }
}
```

#### Образец `1.20.30.1`

SHA-256 файла образца: `0ad825e9433490dda6fa9d51eb0eaf4aaf1e7e510559f7cb0ceded5822ebc155`.

##### `component_groups`

**`blaze_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:timer": {
        "looping": false,
        "time": [
          6,
          6
        ],
        "time_down_event": {
          "event": "blaze_sword_skill",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "blaze_sword",
          "blaze_sword_skill"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`clock_sword_movement`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:movement": {
        "value": 1
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`clock_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:timer": {
        "looping": true,
        "randomInterval": false,
        "time": [
          5,
          5
        ],
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`complete_wolf_transformation`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:attack": {
        "damage": 15
      },
      "minecraft:damage_sensor": {
        "triggers": [
          {
            "deals_damage": true,
            "on_damage": {
              "event": "wolf_damage_sound",
              "filters": {
                "all_of": [
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "void"
                  }
                ]
              }
            }
          }
        ]
      },
      "minecraft:timer": {
        "looping": true,
        "randomInterval": true,
        "time": [
          3,
          6
        ],
        "time_down_event": {
          "event": "wolf_sword_sounds",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "wolf",
          "wolf_sword",
          "complete_wolf_transformation",
          "monster"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`despawn`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:despawn": {}
    }
  },
  "reference": {
    "present": false
  }
}
```

**`ghost_movement`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:movement": {
        "value": 0.14
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`mermaid_movement_in_water`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:underwater_movement": {
        "value": 0.07
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`mermaid_movement_out_water`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:movement": {
        "value": 0.06
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:add_bad_omen`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spell_effects": {
        "add_effects": [
          {
            "display_on_screen_animation": true,
            "duration": 6000,
            "effect": "bad_omen"
          }
        ]
      },
      "minecraft:timer": {
        "looping": false,
        "time": [
          0.0,
          0.0
        ],
        "time_down_event": {
          "event": "minecraft:clear_add_bad_omen",
          "target": "self"
        }
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:spell_effects": {
        "add_effects": [
          {
            "display_on_screen_animation": true,
            "duration": 6000,
            "effect": "bad_omen",
            "visible": false
          }
        ]
      },
      "minecraft:timer": {
        "looping": false,
        "time": [
          0.0,
          0.0
        ],
        "time_down_event": {
          "event": "minecraft:clear_add_bad_omen",
          "target": "self"
        }
      }
    }
  }
}
```

**`minecraft:bee_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:timer": {
        "looping": true,
        "randomInterval": true,
        "time": [
          3,
          8
        ],
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
  "reference": {
    "present": false
  }
}
```

**`minecraft:blaze_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": false,
          "on_damage": {
            "filters": {
              "any_of": [
                {
                  "subject": "self",
                  "test": "has_damage",
                  "value": "fire"
                },
                {
                  "subject": "self",
                  "test": "has_damage",
                  "value": "fire_tick"
                }
              ]
            }
          }
        }
      },
      "minecraft:hurt_on_condition": {
        "damage_conditions": [
          {
            "cause": "drowning",
            "damage_per_tick": 1,
            "filters": {
              "test": "in_water_or_rain"
            }
          }
        ]
      },
      "minecraft:timer": {
        "looping": true,
        "time": [
          1,
          1
        ],
        "time_down_event": {
          "event": "blaze_sword_effects",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "blaze_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:bone_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:timer": {
        "looping": true,
        "time": [
          1,
          1
        ],
        "time_down_event": {
          "event": "bone_sword_skills",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "bone_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:cactus_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:timer": {
        "looping": true,
        "time": [
          0.5,
          0.5
        ],
        "time_down_event": {
          "event": "cactus_sword_skills",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "cactus_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:clock_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:type_family": {
        "family": [
          "player",
          "clock_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:default_player`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:attack": {
        "damage": 1
      },
      "minecraft:breathable": {
        "generates_bubbles": false,
        "inhale_time": 3.75,
        "suffocate_time": -1,
        "total_supply": 15
      },
      "minecraft:collision_box": {
        "height": 1.8,
        "width": 0.6
      },
      "minecraft:damage_sensor": {},
      "minecraft:health": {
        "max": 20,
        "value": 20
      },
      "minecraft:movement": {
        "value": 0.1
      },
      "minecraft:physics": {
        "has_collision": true,
        "has_gravity": true
      },
      "minecraft:rideable": {
        "family_types": [
          "parrot_tame"
        ],
        "pull_in_entities": true,
        "seat_count": 2,
        "seats": [
          {
            "lock_rider_rotation": 0,
            "max_rider_count": 0,
            "min_rider_count": 0,
            "position": [
              0.4,
              -0.2,
              -0.1
            ]
          },
          {
            "lock_rider_rotation": 0,
            "max_rider_count": 2,
            "min_rider_count": 1,
            "position": [
              -0.4,
              -0.2,
              -0.1
            ]
          }
        ]
      },
      "minecraft:scale": {
        "value": 1
      },
      "minecraft:timer": {},
      "minecraft:type_family": {
        "family": [
          "player",
          "default_player"
        ]
      },
      "minecraft:underwater_movement": {
        "value": 0.02
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:emerald_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:type_family": {
        "family": [
          "player",
          "emerald_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:ender_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": [
          {
            "deals_damage": true,
            "on_damage": {
              "event": "ender_sword_skill",
              "filters": {
                "all_of": [
                  {
                    "operator": "!=",
                    "subject": "self",
                    "test": "has_damage",
                    "value": "projectile"
                  }
                ]
              }
            }
          },
          {
            "deals_damage": false,
            "on_damage": {
              "event": "ender_sword_tp",
              "filters": {
                "all_of": [
                  {
                    "subject": "self",
                    "test": "has_damage",
                    "value": "projectile"
                  }
                ]
              }
            }
          },
          {
            "deals_damage": true,
            "on_damage": {
              "event": "ender_sword_tp",
              "filters": {
                "all_of": [
                  {
                    "test": "in_water_or_rain"
                  }
                ]
              }
            }
          }
        ]
      },
      "minecraft:hurt_on_condition": {
        "damage_conditions": [
          {
            "cause": "drowning",
            "damage_per_tick": 1,
            "filters": {
              "test": "in_water_or_rain"
            }
          }
        ]
      },
      "minecraft:timer": {
        "looping": true,
        "randomInterval": true,
        "time": [
          6,
          18
        ],
        "time_down_event": {
          "event": "ender_sword_sound",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "ender_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:fire_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": false,
          "on_damage": {
            "filters": {
              "any_of": [
                {
                  "subject": "self",
                  "test": "has_damage",
                  "value": "fire"
                },
                {
                  "subject": "self",
                  "test": "has_damage",
                  "value": "fire_tick"
                }
              ]
            }
          }
        }
      },
      "minecraft:timer": {
        "looping": true,
        "randomInterval": true,
        "time": [
          0.2,
          0.7
        ],
        "time_down_event": {
          "event": "fire_sword_sound",
          "target": "self"
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
  "reference": {
    "present": false
  }
}
```

**`minecraft:ghost_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:breathable": {
        "breathes_air": true,
        "breathes_lava": true,
        "breathes_water": true,
        "generates_bubbles": false,
        "inhale_time": 3.75,
        "suffocate_time": 0,
        "total_supply": 15
      },
      "minecraft:collision_box": {
        "height": 0.0,
        "width": 0.0
      },
      "minecraft:damage_sensor": {
        "triggers": {
          "cause": "all",
          "deals_damage": false
        }
      },
      "minecraft:knockback_resistance": {
        "value": 1.0
      },
      "minecraft:scale": {
        "value": 1.05
      },
      "minecraft:type_family": {
        "family": [
          "ghost_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:grass_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:timer": {
        "looping": true,
        "time": [
          0.2,
          0.2
        ],
        "time_down_event": {
          "event": "grass_sword_skills",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "grass_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:ice_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:type_family": {
        "family": [
          "player",
          "ice_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:jungle_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:health": {
        "max": 8,
        "value": 8
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "jungle_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:lapis_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:timer": {
        "looping": true,
        "randomInterval": true,
        "time": [
          2.5,
          6.0
        ],
        "time_down_event": {
          "event": "lapis_sword_skills",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "lapis_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:lightning_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": false,
          "on_damage": {
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "lightning"
                }
              ]
            }
          }
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
  "reference": {
    "present": false
  }
}
```

**`minecraft:magma_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": false,
          "on_damage": {
            "filters": {
              "any_of": [
                {
                  "subject": "self",
                  "test": "has_damage",
                  "value": "fire_tick"
                },
                {
                  "operator": "equals",
                  "subject": "block",
                  "test": "is_block",
                  "value": "magma"
                }
              ]
            }
          }
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
  "reference": {
    "present": false
  }
}
```

**`minecraft:nether_star_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": false,
          "on_damage": {
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "nether_star_projectile"
                }
              ]
            }
          }
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
  "reference": {
    "present": false
  }
}
```

**`minecraft:obsidian_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": false,
          "on_damage": {
            "filters": {
              "any_of": [
                {
                  "subject": "self",
                  "test": "has_damage",
                  "value": "block_explosion"
                },
                {
                  "subject": "self",
                  "test": "has_damage",
                  "value": "entity_explosion"
                }
              ]
            }
          }
        }
      },
      "minecraft:knockback_resistance": {
        "value": 1.0
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "obsidian_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:quartz_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:type_family": {
        "family": [
          "player",
          "quartz_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:sea_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:breathable": {
        "breathes_air": false,
        "breathes_lava": false,
        "breathes_water": true,
        "generates_bubbles": false,
        "inhale_time": 3.75,
        "suffocate_time": -1,
        "total_supply": 2
      },
      "minecraft:collision_box": {
        "height": 0.9,
        "width": 0.6
      },
      "minecraft:timer": {
        "looping": true,
        "time": [
          0.5,
          0.5
        ],
        "time_down_event": {
          "event": "sea_sword_sound",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "sea_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:shulker_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:scale": {
        "value": 1
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "shulker_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:slime_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": false,
          "on_damage": {
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "tamed_slime"
                }
              ]
            }
          }
        }
      },
      "minecraft:timer": {
        "looping": false,
        "time": [
          0.4,
          0.4
        ],
        "time_down_event": {
          "event": "slime_sword_skills",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "slime_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:spectral_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:rideable": {
        "family_types": [
          "ender_crystal",
          "spectral_sword"
        ],
        "seat_count": 1,
        "seats": {
          "lock_rider_rotation": 0,
          "position": [
            0.0,
            0.4,
            0.0
          ]
        }
      },
      "minecraft:timer": {
        "looping": false,
        "time": [
          0.4,
          0.4
        ],
        "time_down_event": {
          "event": "spectral_sword_skills",
          "target": "self"
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
  "reference": {
    "present": false
  }
}
```

**`minecraft:spider_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:type_family": {
        "family": [
          "player",
          "spider_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:sponge_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:type_family": {
        "family": [
          "player",
          "sponge_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:time_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:movement": {
        "value": 1
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "time_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:ultra_instinct_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": [
          {
            "deals_damage": false,
            "on_damage": {
              "event": "ultra_instinct_sword_skill",
              "filters": {
                "all_of": [
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "lava"
                  },
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "drowning"
                  },
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "void"
                  },
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "thorns"
                  },
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "suicide"
                  },
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "starve"
                  },
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "fire"
                  },
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "fire_tick"
                  },
                  {
                    "operator": "!=",
                    "test": "has_damage",
                    "value": "magic"
                  }
                ]
              }
            }
          },
          {
            "deals_damage": false,
            "on_damage": {
              "filters": {
                "test": "has_damage",
                "value": "fire"
              }
            }
          },
          {
            "deals_damage": false,
            "on_damage": {
              "filters": {
                "test": "has_damage",
                "value": "fire_tick"
              }
            }
          },
          {
            "deals_damage": false,
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
            }
          },
          {
            "deals_damage": true,
            "on_damage": {
              "filters": {
                "all_of": [
                  {
                    "test": "has_damage",
                    "value": "lava"
                  }
                ]
              }
            }
          }
        ]
      },
      "minecraft:knockback_resistance": {
        "value": 1.0
      },
      "minecraft:timer": {
        "looping": true,
        "randomInterval": true,
        "time": [
          0.1,
          0.2
        ],
        "time_down_event": {
          "event": "ultra_instinct_sword_effects",
          "target": "self"
        }
      },
      "minecraft:type_family": {
        "family": [
          "player",
          "ultra_instinct_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:wither_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": false,
          "on_damage": {
            "filters": {
              "all_of": [
                {
                  "subject": "self",
                  "test": "has_damage",
                  "value": "wither"
                }
              ]
            }
          }
        }
      },
      "minecraft:rideable": {
        "family_types": [
          "entity_name"
        ],
        "seat_count": 1,
        "seats": {
          "lock_rider_rotation": 0,
          "position": [
            0.0,
            0.4,
            0.0
          ]
        }
      },
      "minecraft:timer": {
        "looping": true,
        "randomInterval": true,
        "time": [
          4,
          18
        ],
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
  "reference": {
    "present": false
  }
}
```

**`minecraft:wolf_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:type_family": {
        "family": [
          "player",
          "wolf_sword"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`shoot_small_fireball`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 1,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:fake_fireball",
          "spawn_event": "set_sound"
        },
        {
          "max_wait_time": 1,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:fake_fireball",
          "spawn_event": "set_sound"
        },
        {
          "max_wait_time": 1,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:fake_fireball",
          "spawn_event": "set_sound"
        },
        {
          "max_wait_time": 1,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:fake_fireball",
          "spawn_event": "set_sound"
        }
      ],
      "minecraft:timer": {
        "looping": false,
        "time": [
          2,
          2
        ],
        "time_down_event": {
          "event": "stop_blaze_sword_skill",
          "target": "self"
        }
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`shulker_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
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
  "reference": {
    "present": false
  }
}
```

**`spider_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": false,
          "spawn_entity": "entity:web"
        }
      ],
      "minecraft:timer": {
        "looping": false,
        "time": [
          2,
          2
        ],
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
  "reference": {
    "present": false
  }
}
```

**`start_player_explode_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:movement": {
        "value": 0.0
      },
      "minecraft:timer": {
        "looping": true,
        "time": [
          1.5,
          1.5
        ],
        "time_down_event": {
          "event": "start_player_explode",
          "target": "self"
        }
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`time_sword_movement`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:movement": {
        "value": 1
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`ultra_instinct_projectile`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:spawn_entity": [
        {
          "max_wait_time": 0,
          "min_wait_time": 0,
          "num_to_spawn": 1,
          "single_use": true,
          "spawn_entity": "entity:ultra_instinct_projectile"
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`ultra_instinct_sword_movement`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:movement": {
        "value": 0.22
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`wolf_movement`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:movement": {
        "value": 0.18
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`wolf_transformation`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:type_family": {
        "family": [
          "player",
          "wolf_sword",
          "wolf_transformation"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

##### `components`

**`minecraft:block_climber`**

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

**`minecraft:environment_sensor`**

```json
{
  "addon": {
    "present": true,
    "value": [
      {
        "on_environment": {
          "event": "minecraft:trigger_raid",
          "filters": {
            "all_of": [
              {
                "subject": "self",
                "test": "has_mob_effect",
                "value": "bad_omen"
              },
              {
                "subject": "self",
                "test": "is_in_village",
                "value": true
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:constant_events",
          "filters": {
            "operator": "!=",
            "test": "is_family",
            "value": "null"
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:stop_sword_events",
          "filters": {
            "any_of": [
              {
                "subject": "self",
                "test": "is_family",
                "value": "default_player"
              },
              {
                "operator": "!=",
                "subject": "self",
                "test": "is_family",
                "value": "spectral_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:blaze_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:blaze_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_blaze_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:blaze_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:bone_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:bone_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_bone_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:bone_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:cactus_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:cactus_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_cactus_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:cactus_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:emerald_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:emerald_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_emerald_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:emerald_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:fire_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:fire_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_fire_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:fire_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:grass_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:grass_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_grass_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:grass_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:jungle_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:jungle_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_jungle_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:jungle_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:magma_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:magma_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_magma_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:magma_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:ice_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:ice_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_ice_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:ice_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:lapis_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:lapis_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_lapis_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:lapis_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:obsidian_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:obsidian_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_obsidian_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:obsidian_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:quartz_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:quartz_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_quartz_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:quartz_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:sea_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:sea_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_sea_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:sea_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:spectral_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:spectral_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_spectral_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:spectral_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:slime_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:slime_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_slime_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:slime_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:shulker_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:shulker_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_shulker_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:shulker_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:spider_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:spider_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_spider_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:spider_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:sponge_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:sponge_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_sponge_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:sponge_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:time_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:time_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_time_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:time_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:wither_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:wither_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_wither_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:wither_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:glowstone_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:glowstone_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:lightning_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:lightning_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_lightning_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:lightning_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:ender_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:ender_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_ender_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:ender_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:ultra_instinct_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:ultra_instinct_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_ultra_instinct_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:ultra_instinct_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:wolf_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:wolf_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_wolf_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:wolf_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "starting_wolf_transformation",
          "filters": {
            "all_of": [
              {
                "test": "is_family",
                "value": "wolf_transformation"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "wolf_movement",
          "filters": {
            "all_of": [
              {
                "test": "is_family",
                "value": "complete_wolf_transformation"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:ghost_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:ghost_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_ghost_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:ghost_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:clock_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:clock_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_clock_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:clock_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:nether_star_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:nether_star_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_nether_star_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:nether_star_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "minecraft:bee_sword",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:bee_sword"
              }
            ]
          }
        }
      },
      {
        "on_environment": {
          "event": "stop_bee_sword_event",
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:bee_sword"
              }
            ]
          }
        }
      }
    ]
  },
  "reference": {
    "present": true,
    "value": {
      "triggers": {
        "event": "minecraft:trigger_raid",
        "filters": {
          "all_of": [
            {
              "subject": "self",
              "test": "has_mob_effect",
              "value": "bad_omen"
            },
            {
              "subject": "self",
              "test": "is_in_village",
              "value": true
            }
          ]
        }
      }
    }
  }
}
```

**`minecraft:exhaustion_values`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "attack": 0.1,
      "damage": 0.1,
      "heal": 6,
      "jump": 0.05,
      "mine": 0.005,
      "sprint": 0.1,
      "sprint_jump": 0.2,
      "swim": 0.01,
      "walk": 0.0
    }
  }
}
```

**`minecraft:physics`**

```json
{
  "addon": {
    "present": true,
    "value": {}
  },
  "reference": {
    "present": true,
    "value": {
      "push_towards_closest_space": true
    }
  }
}
```

**`minecraft:player.exhaustion`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "max": 4,
      "value": 0
    }
  },
  "reference": {
    "present": true,
    "value": {
      "max": 20,
      "value": 0
    }
  }
}
```

**`minecraft:player.saturation`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "value": 20
    }
  },
  "reference": {
    "present": true,
    "value": {
      "max": 20,
      "value": 5
    }
  }
}
```

**`minecraft:scaffolding_climber`**

```json
{
  "addon": {
    "present": true,
    "value": {}
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:type_family`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "family": [
        "player",
        "default_player"
      ]
    }
  },
  "reference": {
    "present": true,
    "value": {
      "family": [
        "player"
      ]
    }
  }
}
```

##### `description`

**`animations`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "ghost_sword": "controller.animation.ghost_sword",
      "shulker_sword": "controller.animation.shulker_sword",
      "wither_sword": "controller.animation.wither_sword",
      "wolf_sword_0": "controller.animation.wolf_sword",
      "wolf_sword_1": "controller.animation.start_wolf_sword",
      "wolf_sword_2": "controller.animation.end_wolf_sword"
    }
  },
  "reference": {
    "present": false
  }
}
```

**`scripts`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "animate": [
        "shulker_sword",
        "wither_sword",
        "wolf_sword_0",
        "wolf_sword_1",
        "wolf_sword_2",
        "ghost_sword"
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

##### `events`

**`bee_sword_flower`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "randomize": [
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 0"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 1"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 2"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 4"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 5"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 6"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 7"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 8"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 9"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ red_flower 10"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "execute @s ~ ~ ~ detect ~ ~-1 ~ grass 0 setblock ~ ~ ~ yellow_flower 0"
            ]
          },
          "weight": 1
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`blaze_sword_effects`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "randomize": [
        {
          "run_command": {
            "command": [
              "particle minecraft:mobflame_single ~ ~0.2 ~"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:mobflame_single ~0.3 ~0.2 ~"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:mobflame_single ~ ~0.2 ~0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:mobflame_single ~-0.3 ~0.2 ~"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:mobflame_single ~ ~0.2 ~-0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "playsound mob.blaze.breathe @a[r=12] ~ ~ ~ 0.5"
            ]
          },
          "weight": 1
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`blaze_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "shoot_small_fireball"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`blaze_sword_skill_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "blaze_sword_skill"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`bone_sword_skills`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "summon entity:grows_crop ~ ~0.1 ~ grows_crop_event"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`cactus_sword_skills`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "damage @e[r=1.4,type=!player] 1 contact entity @s",
          "damage @s 1 contact"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`clock_sword_movement`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "clock_sword_movement"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`clock_sword_skill_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "clock_sword_skill"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`default_player`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:default_player"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`despawn`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "despawn"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`ender_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
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
              "run_command": {
                "command": [
                  "spreadplayers ~ ~ 0 16 @s",
                  "playsound mob.endermen.portal @a[r=17]"
                ]
              },
              "weight": 50
            }
          ]
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`ender_sword_sound`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "randomize": [
        {
          "run_command": {
            "command": [
              "playsound mob.endermen.scream @a[r=8] ~ ~ ~"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "playsound mob.endermen.idle @a[r=8] ~ ~ ~"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "playsound mob.endermen.stare @a[r=8] ~ ~ ~"
            ]
          },
          "weight": 1
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`ender_sword_tp`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "spreadplayers ~ ~ 0 16 @s",
          "playsound mob.endermen.portal @a[r=17]"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`fire_sword_sound`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "playsound fire.fire @a[r=8]"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`grass_sword_skills`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "execute @e[type=!player,type=!item,type=!entity:grass,type=!xp_orb,type=!arrow,r=8,tag=!grass] ~ ~ ~ detect ~ ~-0.1 ~ grass 0 execute @s ~ ~ ~ detect ~ ~ ~ air 0 summon entity:grass",
          "execute @e[type=!player,type=!item,type=!entity:grass,type=!xp_orb,type=!arrow,r=8,tag=!grass] ~ ~ ~ detect ~ ~-0.1 ~ grass 0 execute @s ~ ~ ~ detect ~ ~ ~ tallgrass 0 summon entity:grass"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`lapis_sword_skills`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "xp 5 @s",
          "playsound random.orb @s ~ ~ ~ 0.3"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:bee_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:bee_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "bee_sword"
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

**`minecraft:blaze_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:blaze_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "blaze_sword"
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
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "blaze_sword_skill"
          },
          "randomize": [
            {
              "run_command": {
                "command": [
                  "particle minecraft:mobflame_single ~ ~0.2 ~"
                ]
              },
              "weight": 5
            },
            {
              "run_command": {
                "command": [
                  "particle minecraft:mobflame_single ~0.3 ~0.2 ~"
                ]
              },
              "weight": 5
            },
            {
              "run_command": {
                "command": [
                  "particle minecraft:mobflame_single ~ ~0.2 ~0.3"
                ]
              },
              "weight": 5
            },
            {
              "run_command": {
                "command": [
                  "particle minecraft:mobflame_single ~-0.3 ~0.2 ~"
                ]
              },
              "weight": 5
            },
            {
              "run_command": {
                "command": [
                  "particle minecraft:mobflame_single ~ ~0.2 ~-0.3"
                ]
              },
              "weight": 5
            },
            {
              "run_command": {
                "command": [
                  "playsound mob.blaze.breathe @a[r=12] ~ ~ ~ 0.5"
                ]
              },
              "weight": 5
            },
            {
              "weight": 95
            }
          ]
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:bone_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:bone_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "bone_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:cactus_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:cactus_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "cactus_sword"
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

**`minecraft:clock_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:clock_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "clock_sword"
          }
        },
        {
          "add": {
            "component_groups": [
              "clock_sword_movement"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "clock_sword_skill"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:constant_events`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "run_command": {
            "command": [
              "function commands/swords_and_more_swords/swords_and_more_swords/tag_swords",
              "gamerule sendcommandfeedback false",
              "gamerule commandblockoutput false",
              "scoreboard objectives add Effect99 dummy",
              "scoreboard players add @s Effect99 1",
              "title @s[scores={Effect99=12000}] actionbar §l§fCreated by §7Effect99",
              "scoreboard players set @s[scores={Effect99=36001}] Effect99 1"
            ]
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

**`minecraft:emerald_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:emerald_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "emerald_sword"
          }
        },
        {
          "filters": {
            "all_of": [
              {
                "subject": "self",
                "test": "is_in_village",
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:ender_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:ender_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "ender_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:fire_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:fire_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "fire_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:ghost_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:ghost_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "ghost_sword"
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
          "add": {
            "component_groups": [
              "ghost_movement"
            ]
          },
          "run_command": {
            "command": [
              "effect @s slow_falling 1 0 true",
              "effect @s saturation 1 1 true"
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
            "operator": "!=",
            "test": "in_lava"
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
              "run_command": {
                "command": [
                  "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 0.15 0.2"
                ]
              },
              "weight": 10
            }
          ]
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:glowstone_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock 0 replace air",
          "fill ~1 ~1 ~1 ~-1 ~-1 ~-1 effect99:lightblock 0 replace effect99:lightblock"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:grass_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:grass_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "grass_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:ice_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:ice_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "ice_sword"
          }
        },
        {
          "filters": {
            "all_of": [
              {
                "test": "in_lava"
              },
              {
                "operator": "!=",
                "test": "has_biome_tag",
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:jungle_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:jungle_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "jungle_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:lapis_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:lapis_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "lapis_sword"
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

**`minecraft:lightning_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:lightning_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "lightning_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:magma_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:magma_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "magma_sword"
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
            "operator": "==",
            "test": "in_water"
          },
          "randomize": [
            {
              "weight": 99
            },
            {
              "run_command": {
                "command": [
                  "playsound bubble.up @a ~ ~ ~ 1 0.9"
                ]
              },
              "weight": 1
            }
          ]
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:nether_star_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:nether_star_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "nether_star_sword"
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

**`minecraft:obsidian_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:obsidian_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "obsidian_sword"
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

**`minecraft:quartz_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:quartz_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "quartz_sword"
          },
          "run_command": {
            "command": [
              "damage @s 14 magic"
            ]
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

**`minecraft:sea_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "mermaid_movement_out_water"
            ]
          },
          "filters": {
            "operator": "!=",
            "test": "in_water"
          },
          "run_command": {
            "command": [
              "camerashake add @s 0.01 1 positional",
              "effect @s conduit_power 0 0"
            ]
          }
        },
        {
          "add": {
            "component_groups": [
              "minecraft:sea_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "sea_sword"
          },
          "run_command": {
            "command": [
              "particle minecraft:example_bounce ~ ~ ~",
              "playsound random.splash @a[r=12] ~ ~ ~ 0.5"
            ]
          }
        },
        {
          "add": {
            "component_groups": [
              "mermaid_movement_in_water"
            ]
          },
          "filters": {
            "test": "in_water"
          },
          "run_command": {
            "command": [
              "effect @s conduit_power 1 0 true"
            ]
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

**`minecraft:shulker_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:shulker_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "shulker_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:slime_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:slime_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "slime_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:spectral_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:spectral_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "spectral_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:spider_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:spider_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "spider_sword"
          },
          "run_command": {
            "command": [
              "ride @s summon_ride minecraft:spider no_ride_change minecraft:spider_sword",
              "particle minecraft:example_linearcurve ~ ~ ~"
            ]
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

**`minecraft:sponge_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:sponge_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "sponge_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:stop_sword_events`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "run_command": {
            "command": [
              "execute @e[r=64,type=!player] ~ ~ ~ detect ~ ~ ~ ice 0 tp @s ~ ~ ~"
            ]
          }
        },
        {
          "filters": {
            "all_of": [
              {
                "operator": "!=",
                "test": "has_biome_tag",
                "value": "nether"
              },
              {
                "operator": "!=",
                "test": "has_biome_tag",
                "value": "the_end"
              }
            ]
          },
          "run_command": {
            "command": [
              "fill ~6 ~6 ~6 ~-6 ~-6 ~-6 stone 0 replace effect99:spectral_block",
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
              "fill ~6 ~6 ~6 ~-6 ~-6 ~-6 netherrack 0 replace effect99:spectral_block",
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
              "fill ~6 ~6 ~6 ~-6 ~-6 ~-6 end_stone 0 replace effect99:spectral_block",
              "fill ~7 ~8 ~8 ~8 ~-8 ~-8 end_stone 0 replace effect99:spectral_block",
              "fill ~-7 ~-8 ~-8 ~-8 ~8 ~8 end_stone 0 replace effect99:spectral_block",
              "fill ~-6 ~8 ~7 ~6 ~-8 ~8 end_stone 0 replace effect99:spectral_block",
              "fill ~6 ~-8 ~-7 ~-6 ~8 ~-8 end_stone 0 replace effect99:spectral_block",
              "fill ~8 ~-8 ~8 ~-8 ~-7 ~-8 end_stone 0 replace effect99:spectral_block",
              "fill ~8 ~8 ~8 ~-8 ~7 ~-8 end_stone 0 replace effect99:spectral_block"
            ]
          }
        },
        {
          "filters": {
            "all_of": [
              {
                "domain": "hand",
                "operator": "!=",
                "subject": "self",
                "test": "has_equipment",
                "value": "effect:slime_sword"
              }
            ]
          },
          "run_command": {
            "command": [
              "ride @e[type=entity:mountable_slime,r=1,y=~-1] evict_riders"
            ]
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

**`minecraft:time_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:ultra_instinct_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:ultra_instinct_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "ultra_instinct_sword"
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
          "add": {
            "component_groups": [
              "ultra_instinct_sword_movement"
            ]
          },
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

**`minecraft:wither_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:wither_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "wither_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`minecraft:wolf_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:wolf_sword"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "wolf_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`sea_sword_sound`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "filters": {
            "operator": "!=",
            "test": "in_water"
          },
          "run_command": {
            "command": [
              "playsound mob.fish.flop @a[r=12] ~ ~ ~ 1 0.6"
            ]
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

**`shoot_ultra_instinct_projectile`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "ultra_instinct_projectile"
        ]
      },
      "remove": {
        "component_groups": [
          "ultra_instinct_projectile"
        ]
      },
      "run_command": {
        "command": [
          "playsound mob.wither.ambient @s ~ ~1 ~ 2 0.6"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`shulker_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
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
  },
  "reference": {
    "present": false
  }
}
```

**`slime_sword_skills`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "ride @s summon_ride entity:mountable_slime no_ride_change",
          "scoreboard objectives add slime_despawn dummy"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`spectral_sword_function`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "filters": {
            "all_of": [
              {
                "operator": "!=",
                "test": "has_biome_tag",
                "value": "nether"
              },
              {
                "operator": "!=",
                "test": "has_biome_tag",
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`spectral_sword_function_1`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "filters": {
            "all_of": [
              {
                "operator": "!=",
                "test": "has_biome_tag",
                "value": "nether"
              },
              {
                "operator": "!=",
                "test": "has_biome_tag",
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`spectral_sword_reload_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:spectral_sword"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "spectral_sword"
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

**`spectral_sword_skills`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "filters": {
            "operator": "!=",
            "test": "has_biome_tag",
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`spider_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "spider_sword_skill"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "spider_sword_skill"
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

**`start_player_explode`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:default_player"
        ]
      },
      "remove": {
        "component_groups": [
          "start_player_explode_event"
        ]
      },
      "run_command": {
        "command": [
          "summon entity:instant_creeper_explode ~ ~1 ~",
          "kill @s"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`start_player_explode_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "start_player_explode_event"
        ]
      },
      "run_command": {
        "command": [
          "playanimation @s animation.player.explode",
          "playsound random.fuse"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`starting_wolf_transformation`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "effect @s nausea 5 0 true"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`stop_bee_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "bee_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:bee_sword"
            ]
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

**`stop_blaze_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
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

**`stop_blaze_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:blaze_sword"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "blaze_sword"
          },
          "remove": {
            "component_groups": [
              "shoot_small_fireball"
            ]
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

**`stop_bone_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "bone_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:bone_sword"
            ]
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

**`stop_cactus_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "cactus_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:cactus_sword"
            ]
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

**`stop_clock_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
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

**`stop_emerald_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "emerald_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:emerald_sword"
            ]
          },
          "run_command": {
            "command": [
              "effect @s village_hero 0 0 true"
            ]
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

**`stop_ender_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "ender_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:ender_sword"
            ]
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

**`stop_fire_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "fire_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:fire_sword"
            ]
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

**`stop_ghost_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "ghost_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:ghost_sword"
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
  },
  "reference": {
    "present": false
  }
}
```

**`stop_grass_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "grass_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:grass_sword"
            ]
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

**`stop_ice_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "ice_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:ice_sword"
            ]
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

**`stop_jungle_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "jungle_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:jungle_sword"
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
  },
  "reference": {
    "present": false
  }
}
```

**`stop_lapis_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "lapis_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:lapis_sword"
            ]
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

**`stop_lightning_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "lightning_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:lightning_sword"
            ]
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

**`stop_magma_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "magma_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:magma_sword"
            ]
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

**`stop_nether_star_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "nether_star_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:nether_star_sword"
            ]
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

**`stop_obsidian_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "obsidian_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:obsidian_sword"
            ]
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

**`stop_quartz_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "quartz_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:quartz_sword"
            ]
          },
          "run_command": {
            "command": [
              "damage @s 14 magic"
            ]
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

**`stop_sea_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "sea_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:sea_sword",
              "mermaid_movement_in_water"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`stop_shulker_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "shulker_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:shulker_sword"
            ]
          },
          "run_command": {
            "command": [
              "ride @s stop_riding"
            ]
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

**`stop_slime_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "slime_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:slime_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`stop_spectral_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
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

**`stop_spider_skill_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:spider_sword"
            ]
          },
          "filters": {
            "subject": "self",
            "test": "is_family",
            "value": "spider_sword_skill"
          },
          "remove": {
            "component_groups": [
              "spider_sword_skill"
            ]
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

**`stop_spider_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "spider_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:spider_sword",
              "spider_sword_skill"
            ]
          },
          "run_command": {
            "command": [
              "ride @s stop_riding"
            ]
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

**`stop_sponge_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "sponge_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:sponge_sword"
            ]
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

**`stop_time_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "time_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:time_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`stop_ultra_instinct_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "ultra_instinct_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:ultra_instinct_sword",
              "ultra_instinct_sword_movement"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`stop_wither_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
            "value": "wither_sword"
          },
          "remove": {
            "component_groups": [
              "minecraft:wither_sword"
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
    }
  },
  "reference": {
    "present": false
  }
}
```

**`stop_wolf_sword_event`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_family",
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
          }
        },
        {
          "add": {
            "component_groups": [
              "minecraft:default_player"
            ]
          },
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

**`stop_wolf_transformation`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "run_command": {
            "command": [
              "effect @s nausea 0 0",
              "effect @s blindness 0 0",
              "stopsound @a wolf_sword.howl",
              "stopsound @a wolf_sword.distant_howl"
            ]
          }
        },
        {
          "add": {
            "component_groups": [
              "minecraft:wolf_sword"
            ]
          },
          "remove": {
            "component_groups": [
              "wolf_transformation",
              "complete_wolf_transformation",
              "wolf_movement"
            ]
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

**`time_sword_movement`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "time_sword_movement"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`ultra_instinct_sword_effects`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "randomize": [
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.3 ~1 ~",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~ ~2 ~0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~-0.3 ~ ~",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~ ~0.3 ~-0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.3 ~1.5 ~0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~-0.3 ~0.8 ~-0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~-0.3 ~2 ~0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.2 ~1 ~0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.3 ~0.9 ~0.1",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.2 ~2.3 ~-0.2",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~-0.3 ~1.2 ~",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.3 ~0.3 ~0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.3 ~0.6 ~0.1",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~-0.3 ~0.2 ~0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        },
        {
          "run_command": {
            "command": [
              "particle minecraft:balloon_gas_particle ~0.1 ~0.7 ~-0.3",
              "playsound mob.wither.spawn @a[r=16] ~ ~ ~ 1 0.3"
            ]
          },
          "weight": 1
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`ultra_instinct_sword_skill`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "spreadplayers ~ ~ 1 3 @s",
          "playsound mob.endermen.portal @a[r=17] ~ ~ ~ 1 0.6"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`wet_sponge_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "filters": {
            "domain": "hand",
            "subject": "self",
            "test": "has_equipment",
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
  },
  "reference": {
    "present": false
  }
}
```

**`wither_sword_effects`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "randomize": [
        {
          "run_command": {
            "command": [
              "playsound mob.wither.death @a[r=16]"
            ]
          },
          "weight": 50
        },
        {
          "run_command": {
            "command": [
              "playsound mob.wither.hurt @a[r=16]"
            ]
          },
          "weight": 50
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`wolf_damage_sound`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "run_command": {
        "command": [
          "playsound mob.wolf.bark @a[r=16] ~ ~ ~ 1 0.55"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`wolf_movement`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "wolf_movement"
        ]
      }
    }
  },
  "reference": {
    "present": false
  }
}
```

**`wolf_sword_sounds`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "randomize": [
        {
          "run_command": {
            "command": [
              "playsound mob.wolf.growl @a[r=16] ~ ~ ~ 1 0.9 24"
            ]
          },
          "weight": 1
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`wolf_sword_start_events`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "wolf_transformation"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "wolf_transformation"
          },
          "run_command": {
            "command": [
              "function commands/swords_and_more_swords/swords_and_more_swords/tellraw1"
            ]
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

**`wolf_transformation`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "add": {
            "component_groups": [
              "complete_wolf_transformation"
            ]
          },
          "filters": {
            "operator": "!=",
            "subject": "self",
            "test": "is_family",
            "value": "complete_wolf_transformation"
          },
          "run_command": {
            "command": [
              "playsound random.fizz @a[r=16] ~~~",
              "playsound wolf_sword.howl @a[r=24] ~~~",
              "playsound wolf_sword.distant_howl @a[rm=25,r=100]",
              "particle minecraft:egg_destroy_emitter ~ ~ ~",
              "particle minecraft:egg_destroy_emitter ~ ~0.5 ~",
              "particle minecraft:egg_destroy_emitter ~ ~0.8 ~"
            ]
          }
        },
        {
          "filters": {
            "test": "is_family",
            "value": "wolf_transformation"
          },
          "remove": {
            "component_groups": [
              "wolf_transformation"
            ]
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

##### `root`

**`format_version`**

```json
{
  "addon": {
    "present": true,
    "value": "1.11.0"
  },
  "reference": {
    "present": true,
    "value": "1.18.20"
  }
}
```

## `minecraft:skeleton`

### Аддон `2.8.14`

SHA-256 файла: `b6640a992aac64bf1d99b42660196096ab6fb55c55f6f387cea3bdcd1c84ef06`.

#### Образец `1.19.40.2`

SHA-256 файла образца: `bf7fce9c7e82c897918c183eabc1ecfd9b2a16105483164a6150dd28a3132dd9`.

##### `component_groups`

**`become_stray`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:transformation": {
        "drop_inventory": true,
        "into": "minecraft:stray",
        "keep_level": true,
        "preserve_equipment": true,
        "transformation_sound": "convert_to_stray"
      }
    }
  }
}
```

**`got_out_of_powder_snow_environment_sensor`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:environment_sensor": {
        "triggers": [
          {
            "event": "minecraft:melee_mode",
            "filters": {
              "operator": "==",
              "subject": "self",
              "test": "is_underwater",
              "value": true
            }
          },
          {
            "event": "minecraft:melee_mode",
            "filters": {
              "operator": "==",
              "subject": "self",
              "test": "has_ranged_weapon",
              "value": false
            }
          },
          {
            "event": "minecraft:ranged_mode",
            "filters": {
              "all_of": [
                {
                  "operator": "==",
                  "subject": "self",
                  "test": "in_water",
                  "value": false
                },
                {
                  "operator": "==",
                  "subject": "self",
                  "test": "has_ranged_weapon",
                  "value": true
                }
              ]
            }
          }
        ]
      }
    }
  }
}
```

**`in_powder_snow`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:environment_sensor": {
        "triggers": [
          {
            "event": "got_out_of_powder_snow",
            "filters": {
              "operator": "!=",
              "subject": "self",
              "test": "in_block",
              "value": "minecraft:powder_snow"
            }
          }
        ]
      },
      "minecraft:is_shaking": {},
      "minecraft:timer": {
        "looping": false,
        "time": 20,
        "time_down_event": {
          "event": "become_stray_event"
        }
      }
    }
  }
}
```

**`minecraft:lightning_immune`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": [
          {
            "deals_damage": true,
            "on_damage": {
              "event": "bone_sword",
              "filters": {
                "all_of": [
                  {
                    "subject": "other",
                    "test": "is_family",
                    "value": "player"
                  },
                  {
                    "test": "has_damage",
                    "value": "fatal"
                  }
                ]
              }
            }
          },
          {
            "deals_damage": false,
            "on_damage": {
              "filters": {
                "other_with_families": "lightning"
              }
            }
          }
        ]
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": false,
          "on_damage": {
            "filters": {
              "other_with_families": "lightning"
            }
          }
        }
      }
    }
  }
}
```

**`minecraft:melee_attack`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:attack": {
        "damage": 3
      },
      "minecraft:behavior.melee_attack": {
        "priority": 4,
        "speed_multiplier": 1.25,
        "target_dist": 1.2,
        "track_target": true
      },
      "minecraft:environment_sensor": {
        "triggers": {
          "event": "minecraft:ranged_mode",
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "in_water",
            "value": false
          }
        }
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:attack": {
        "damage": 2
      },
      "minecraft:behavior.melee_attack": {
        "priority": 4,
        "speed_multiplier": 1.25,
        "track_target": true
      },
      "minecraft:environment_sensor": {
        "triggers": [
          {
            "event": "minecraft:ranged_mode",
            "filters": {
              "all_of": [
                {
                  "operator": "==",
                  "subject": "self",
                  "test": "in_water",
                  "value": false
                },
                {
                  "operator": "==",
                  "subject": "self",
                  "test": "has_ranged_weapon",
                  "value": true
                }
              ]
            }
          },
          {
            "event": "got_in_powder_snow",
            "filters": {
              "operator": "==",
              "subject": "self",
              "test": "in_block",
              "value": "minecraft:powder_snow"
            }
          }
        ]
      }
    }
  }
}
```

**`minecraft:ranged_attack`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:behavior.ranged_attack": {
        "attack_interval_max": 3,
        "attack_interval_min": 1,
        "attack_radius": 15
      },
      "minecraft:environment_sensor": {
        "triggers": {
          "event": "minecraft:melee_mode",
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_underwater",
            "value": true
          }
        }
      },
      "minecraft:shooter": {
        "def": "minecraft:arrow",
        "type": "Arrow"
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:behavior.ranged_attack": {
        "attack_interval_max": 3.0,
        "attack_interval_min": 1.0,
        "attack_radius": 15.0,
        "priority": 0
      },
      "minecraft:environment_sensor": {
        "triggers": [
          {
            "event": "minecraft:melee_mode",
            "filters": {
              "operator": "==",
              "subject": "self",
              "test": "is_underwater",
              "value": true
            }
          },
          {
            "event": "minecraft:melee_mode",
            "filters": {
              "operator": "==",
              "subject": "self",
              "test": "has_ranged_weapon",
              "value": false
            }
          },
          {
            "event": "got_in_powder_snow",
            "filters": {
              "operator": "==",
              "subject": "self",
              "test": "in_block",
              "value": "minecraft:powder_snow"
            }
          }
        ]
      },
      "minecraft:shooter": {
        "def": "minecraft:arrow"
      }
    }
  }
}
```

##### `components`

**`minecraft:behavior.equip_item`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "priority": 3
    }
  }
}
```

**`minecraft:behavior.look_at_player`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "look_distance": 8,
      "priority": 6
    }
  },
  "reference": {
    "present": true,
    "value": {
      "look_distance": 8,
      "priority": 7
    }
  }
}
```

**`minecraft:behavior.pickup_items`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "can_pickup_any_item": true,
      "goal_radius": 2,
      "max_dist": 3,
      "pickup_based_on_chance": true,
      "priority": 5,
      "speed_multiplier": 1.0
    }
  }
}
```

**`minecraft:behavior.random_look_around`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "priority": 6
    }
  },
  "reference": {
    "present": true,
    "value": {
      "priority": 8
    }
  }
}
```

**`minecraft:behavior.random_stroll`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "priority": 5,
      "speed_multiplier": 1
    }
  },
  "reference": {
    "present": true,
    "value": {
      "priority": 6,
      "speed_multiplier": 1
    }
  }
}
```

**`minecraft:behavior.ranged_attack`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "attack_interval_max": 3,
      "attack_interval_min": 1,
      "attack_radius": 15
    }
  },
  "reference": {
    "present": true,
    "value": {
      "attack_interval_max": 3.0,
      "attack_interval_min": 1.0,
      "attack_radius": 15.0,
      "priority": 0
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

**`minecraft:damage_sensor`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "triggers": [
        {
          "deals_damage": true,
          "on_damage": {
            "event": "bone_sword",
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "player"
                },
                {
                  "test": "has_damage",
                  "value": "fatal"
                }
              ]
            }
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

**`minecraft:environment_sensor`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "triggers": {
        "event": "minecraft:melee_mode",
        "filters": {
          "operator": "==",
          "subject": "self",
          "test": "is_underwater",
          "value": true
        }
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "triggers": [
        {
          "event": "minecraft:melee_mode",
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_underwater",
            "value": true
          }
        },
        {
          "event": "minecraft:melee_mode",
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "has_ranged_weapon",
            "value": false
          }
        },
        {
          "event": "got_in_powder_snow",
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "in_block",
            "value": "minecraft:powder_snow"
          }
        }
      ]
    }
  }
}
```

**`minecraft:equip_item`**

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

**`minecraft:shareables`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "items": [
        {
          "item": "minecraft:netherite_sword",
          "priority": 0,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:diamond_sword",
          "priority": 1,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:iron_sword",
          "priority": 2,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:stone_sword",
          "priority": 3,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:golden_sword",
          "priority": 4,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:wooden_sword",
          "priority": 5,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:bow",
          "priority": 6,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:netherite_helmet",
          "priority": 0,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:diamond_helmet",
          "priority": 1,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:iron_helmet",
          "priority": 2,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:chainmail_helmet",
          "priority": 3,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:golden_helmet",
          "priority": 4,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:leather_helmet",
          "priority": 5,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:turtle_helmet",
          "priority": 6,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:skull:0",
          "priority": 7,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:skull:1",
          "priority": 7,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:carved_pumpkin",
          "priority": 7,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:netherite_chestplate",
          "priority": 0,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:diamond_chestplate",
          "priority": 1,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:iron_chestplate",
          "priority": 2,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:chainmail_chestplate",
          "priority": 3,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:golden_chestplate",
          "priority": 4,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:leather_chestplate",
          "priority": 5,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:netherite_leggings",
          "priority": 0,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:diamond_leggings",
          "priority": 1,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:iron_leggings",
          "priority": 2,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:chainmail_leggings",
          "priority": 3,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:golden_leggings",
          "priority": 4,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:leather_leggings",
          "priority": 5,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:netherite_boots",
          "priority": 0,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:diamond_boots",
          "priority": 1,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:iron_boots",
          "priority": 2,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:chainmail_boots",
          "priority": 3,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:golden_boots",
          "priority": 4,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:leather_boots",
          "priority": 5,
          "surplus_amount": 1,
          "want_amount": 1
        }
      ]
    }
  }
}
```

**`minecraft:shooter`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "def": "minecraft:arrow",
      "type": "Arrow"
    }
  },
  "reference": {
    "present": true,
    "value": {
      "def": "minecraft:arrow"
    }
  }
}
```

##### `events`

**`become_stray_event`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "become_stray"
        ]
      }
    }
  }
}
```

**`bone_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "filters": {
            "all_of": [
              {
                "test": "has_biome_tag",
                "value": "desert"
              },
              {
                "operator": "<",
                "test": "is_brightness",
                "value": 0.49
              }
            ]
          },
          "randomize": [
            {
              "weight": 993
            },
            {
              "run_command": {
                "command": [
                  "structure load bone_sword ~ ~ ~"
                ]
              },
              "weight": 7
            }
          ]
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`got_in_powder_snow`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "in_powder_snow"
        ]
      }
    }
  }
}
```

**`got_out_of_powder_snow`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "got_out_of_powder_snow_environment_sensor"
        ]
      },
      "remove": {
        "component_groups": [
          "in_powder_snow"
        ]
      }
    }
  }
}
```

**`minecraft:melee_mode`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:melee_attack"
        ]
      },
      "remove": {
        "component_groups": [
          "minecraft:ranged_attack"
        ]
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:melee_attack"
        ]
      },
      "remove": {
        "component_groups": [
          "minecraft:ranged_attack",
          "got_out_of_powder_snow_environment_sensor"
        ]
      }
    }
  }
}
```

**`minecraft:ranged_mode`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:ranged_attack"
        ]
      },
      "remove": {
        "component_groups": [
          "minecraft:melee_attack"
        ]
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:ranged_attack"
        ]
      },
      "remove": {
        "component_groups": [
          "minecraft:melee_attack",
          "got_out_of_powder_snow_environment_sensor"
        ]
      }
    }
  }
}
```

##### `root`

**`format_version`**

```json
{
  "addon": {
    "present": true,
    "value": "1.13.0"
  },
  "reference": {
    "present": true,
    "value": "1.18.20"
  }
}
```

#### Образец `1.20.30.1`

SHA-256 файла образца: `2af6271b7d4bbe239aa5fb4f14a2b16f56cb02d7f8260f9358e14efda4056773`.

##### `component_groups`

**`become_stray`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:transformation": {
        "drop_inventory": true,
        "into": "minecraft:stray",
        "keep_level": true,
        "preserve_equipment": true,
        "transformation_sound": "convert_to_stray"
      }
    }
  }
}
```

**`got_out_of_powder_snow_environment_sensor`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:environment_sensor": {
        "triggers": [
          {
            "event": "minecraft:melee_mode",
            "filters": {
              "operator": "==",
              "subject": "self",
              "test": "is_underwater",
              "value": true
            }
          },
          {
            "event": "minecraft:melee_mode",
            "filters": {
              "operator": "==",
              "subject": "self",
              "test": "has_ranged_weapon",
              "value": false
            }
          },
          {
            "event": "minecraft:ranged_mode",
            "filters": {
              "all_of": [
                {
                  "operator": "==",
                  "subject": "self",
                  "test": "in_water",
                  "value": false
                },
                {
                  "operator": "==",
                  "subject": "self",
                  "test": "has_ranged_weapon",
                  "value": true
                }
              ]
            }
          }
        ]
      }
    }
  }
}
```

**`in_powder_snow`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:environment_sensor": {
        "triggers": [
          {
            "event": "got_out_of_powder_snow",
            "filters": {
              "operator": "!=",
              "subject": "self",
              "test": "in_block",
              "value": "minecraft:powder_snow"
            }
          }
        ]
      },
      "minecraft:is_shaking": {},
      "minecraft:timer": {
        "looping": false,
        "time": 20,
        "time_down_event": {
          "event": "become_stray_event"
        }
      }
    }
  }
}
```

**`minecraft:lightning_immune`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": [
          {
            "deals_damage": true,
            "on_damage": {
              "event": "bone_sword",
              "filters": {
                "all_of": [
                  {
                    "subject": "other",
                    "test": "is_family",
                    "value": "player"
                  },
                  {
                    "test": "has_damage",
                    "value": "fatal"
                  }
                ]
              }
            }
          },
          {
            "deals_damage": false,
            "on_damage": {
              "filters": {
                "other_with_families": "lightning"
              }
            }
          }
        ]
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": false,
          "on_damage": {
            "filters": {
              "other_with_families": "lightning"
            }
          }
        }
      }
    }
  }
}
```

**`minecraft:melee_attack`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:attack": {
        "damage": 3
      },
      "minecraft:behavior.melee_attack": {
        "priority": 4,
        "speed_multiplier": 1.25,
        "target_dist": 1.2,
        "track_target": true
      },
      "minecraft:environment_sensor": {
        "triggers": {
          "event": "minecraft:ranged_mode",
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "in_water",
            "value": false
          }
        }
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:attack": {
        "damage": 2
      },
      "minecraft:behavior.melee_attack": {
        "priority": 4,
        "speed_multiplier": 1.25,
        "track_target": true
      },
      "minecraft:environment_sensor": {
        "triggers": [
          {
            "event": "minecraft:ranged_mode",
            "filters": {
              "all_of": [
                {
                  "operator": "==",
                  "subject": "self",
                  "test": "in_water",
                  "value": false
                },
                {
                  "operator": "==",
                  "subject": "self",
                  "test": "has_ranged_weapon",
                  "value": true
                }
              ]
            }
          },
          {
            "event": "got_in_powder_snow",
            "filters": {
              "operator": "==",
              "subject": "self",
              "test": "in_block",
              "value": "minecraft:powder_snow"
            }
          }
        ]
      }
    }
  }
}
```

**`minecraft:ranged_attack`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:behavior.ranged_attack": {
        "attack_interval_max": 3,
        "attack_interval_min": 1,
        "attack_radius": 15
      },
      "minecraft:environment_sensor": {
        "triggers": {
          "event": "minecraft:melee_mode",
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_underwater",
            "value": true
          }
        }
      },
      "minecraft:shooter": {
        "def": "minecraft:arrow",
        "type": "Arrow"
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:behavior.ranged_attack": {
        "attack_interval_max": 3.0,
        "attack_interval_min": 1.0,
        "attack_radius": 15.0,
        "priority": 0
      },
      "minecraft:environment_sensor": {
        "triggers": [
          {
            "event": "minecraft:melee_mode",
            "filters": {
              "operator": "==",
              "subject": "self",
              "test": "is_underwater",
              "value": true
            }
          },
          {
            "event": "minecraft:melee_mode",
            "filters": {
              "operator": "==",
              "subject": "self",
              "test": "has_ranged_weapon",
              "value": false
            }
          },
          {
            "event": "got_in_powder_snow",
            "filters": {
              "operator": "==",
              "subject": "self",
              "test": "in_block",
              "value": "minecraft:powder_snow"
            }
          }
        ]
      },
      "minecraft:shooter": {
        "def": "minecraft:arrow",
        "sound": "bow"
      }
    }
  }
}
```

##### `components`

**`minecraft:behavior.equip_item`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "priority": 3
    }
  }
}
```

**`minecraft:behavior.look_at_player`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "look_distance": 8,
      "priority": 6
    }
  },
  "reference": {
    "present": true,
    "value": {
      "look_distance": 8,
      "priority": 7
    }
  }
}
```

**`minecraft:behavior.pickup_items`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "can_pickup_any_item": true,
      "goal_radius": 2,
      "max_dist": 3,
      "pickup_based_on_chance": true,
      "priority": 5,
      "speed_multiplier": 1.0
    }
  }
}
```

**`minecraft:behavior.random_look_around`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "priority": 6
    }
  },
  "reference": {
    "present": true,
    "value": {
      "priority": 8
    }
  }
}
```

**`minecraft:behavior.random_stroll`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "priority": 5,
      "speed_multiplier": 1
    }
  },
  "reference": {
    "present": true,
    "value": {
      "priority": 6,
      "speed_multiplier": 1
    }
  }
}
```

**`minecraft:behavior.ranged_attack`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "attack_interval_max": 3,
      "attack_interval_min": 1,
      "attack_radius": 15
    }
  },
  "reference": {
    "present": true,
    "value": {
      "attack_interval_max": 3.0,
      "attack_interval_min": 1.0,
      "attack_radius": 15.0,
      "priority": 0
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

**`minecraft:damage_sensor`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "triggers": [
        {
          "deals_damage": true,
          "on_damage": {
            "event": "bone_sword",
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "player"
                },
                {
                  "test": "has_damage",
                  "value": "fatal"
                }
              ]
            }
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

**`minecraft:environment_sensor`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "triggers": {
        "event": "minecraft:melee_mode",
        "filters": {
          "operator": "==",
          "subject": "self",
          "test": "is_underwater",
          "value": true
        }
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "triggers": [
        {
          "event": "minecraft:melee_mode",
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_underwater",
            "value": true
          }
        },
        {
          "event": "minecraft:melee_mode",
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "has_ranged_weapon",
            "value": false
          }
        },
        {
          "event": "got_in_powder_snow",
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "in_block",
            "value": "minecraft:powder_snow"
          }
        }
      ]
    }
  }
}
```

**`minecraft:equip_item`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "excluded_items": [
        {
          "item": "minecraft:banner:15"
        }
      ]
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

**`minecraft:shareables`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "items": [
        {
          "item": "minecraft:netherite_sword",
          "priority": 0,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:diamond_sword",
          "priority": 1,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:iron_sword",
          "priority": 2,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:stone_sword",
          "priority": 3,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:golden_sword",
          "priority": 4,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:wooden_sword",
          "priority": 5,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:bow",
          "priority": 6,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:netherite_helmet",
          "priority": 0,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:diamond_helmet",
          "priority": 1,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:iron_helmet",
          "priority": 2,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:chainmail_helmet",
          "priority": 3,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:golden_helmet",
          "priority": 4,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:leather_helmet",
          "priority": 5,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:turtle_helmet",
          "priority": 6,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:skull:0",
          "priority": 7,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:skull:1",
          "priority": 7,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:carved_pumpkin",
          "priority": 7,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:netherite_chestplate",
          "priority": 0,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:diamond_chestplate",
          "priority": 1,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:iron_chestplate",
          "priority": 2,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:chainmail_chestplate",
          "priority": 3,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:golden_chestplate",
          "priority": 4,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:leather_chestplate",
          "priority": 5,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:netherite_leggings",
          "priority": 0,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:diamond_leggings",
          "priority": 1,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:iron_leggings",
          "priority": 2,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:chainmail_leggings",
          "priority": 3,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:golden_leggings",
          "priority": 4,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:leather_leggings",
          "priority": 5,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:netherite_boots",
          "priority": 0,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:diamond_boots",
          "priority": 1,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:iron_boots",
          "priority": 2,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:chainmail_boots",
          "priority": 3,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:golden_boots",
          "priority": 4,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:leather_boots",
          "priority": 5,
          "surplus_amount": 1,
          "want_amount": 1
        }
      ],
      "singular_pickup": true
    }
  }
}
```

**`minecraft:shooter`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "def": "minecraft:arrow",
      "type": "Arrow"
    }
  },
  "reference": {
    "present": true,
    "value": {
      "def": "minecraft:arrow"
    }
  }
}
```

##### `events`

**`become_stray_event`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "become_stray"
        ]
      }
    }
  }
}
```

**`bone_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "filters": {
            "all_of": [
              {
                "test": "has_biome_tag",
                "value": "desert"
              },
              {
                "operator": "<",
                "test": "is_brightness",
                "value": 0.49
              }
            ]
          },
          "randomize": [
            {
              "weight": 993
            },
            {
              "run_command": {
                "command": [
                  "structure load bone_sword ~ ~ ~"
                ]
              },
              "weight": 7
            }
          ]
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`got_in_powder_snow`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "in_powder_snow"
        ]
      }
    }
  }
}
```

**`got_out_of_powder_snow`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "got_out_of_powder_snow_environment_sensor"
        ]
      },
      "remove": {
        "component_groups": [
          "in_powder_snow"
        ]
      }
    }
  }
}
```

**`minecraft:melee_mode`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:melee_attack"
        ]
      },
      "remove": {
        "component_groups": [
          "minecraft:ranged_attack"
        ]
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:melee_attack"
        ]
      },
      "remove": {
        "component_groups": [
          "minecraft:ranged_attack",
          "got_out_of_powder_snow_environment_sensor"
        ]
      }
    }
  }
}
```

**`minecraft:ranged_mode`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:ranged_attack"
        ]
      },
      "remove": {
        "component_groups": [
          "minecraft:melee_attack"
        ]
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:ranged_attack"
        ]
      },
      "remove": {
        "component_groups": [
          "minecraft:melee_attack",
          "got_out_of_powder_snow_environment_sensor"
        ]
      }
    }
  }
}
```

##### `root`

**`format_version`**

```json
{
  "addon": {
    "present": true,
    "value": "1.13.0"
  },
  "reference": {
    "present": true,
    "value": "1.18.20"
  }
}
```

### Аддон `2.8.8`

SHA-256 файла: `b6640a992aac64bf1d99b42660196096ab6fb55c55f6f387cea3bdcd1c84ef06`.

#### Образец `1.19.40.2`

SHA-256 файла образца: `bf7fce9c7e82c897918c183eabc1ecfd9b2a16105483164a6150dd28a3132dd9`.

##### `component_groups`

**`become_stray`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:transformation": {
        "drop_inventory": true,
        "into": "minecraft:stray",
        "keep_level": true,
        "preserve_equipment": true,
        "transformation_sound": "convert_to_stray"
      }
    }
  }
}
```

**`got_out_of_powder_snow_environment_sensor`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:environment_sensor": {
        "triggers": [
          {
            "event": "minecraft:melee_mode",
            "filters": {
              "operator": "==",
              "subject": "self",
              "test": "is_underwater",
              "value": true
            }
          },
          {
            "event": "minecraft:melee_mode",
            "filters": {
              "operator": "==",
              "subject": "self",
              "test": "has_ranged_weapon",
              "value": false
            }
          },
          {
            "event": "minecraft:ranged_mode",
            "filters": {
              "all_of": [
                {
                  "operator": "==",
                  "subject": "self",
                  "test": "in_water",
                  "value": false
                },
                {
                  "operator": "==",
                  "subject": "self",
                  "test": "has_ranged_weapon",
                  "value": true
                }
              ]
            }
          }
        ]
      }
    }
  }
}
```

**`in_powder_snow`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:environment_sensor": {
        "triggers": [
          {
            "event": "got_out_of_powder_snow",
            "filters": {
              "operator": "!=",
              "subject": "self",
              "test": "in_block",
              "value": "minecraft:powder_snow"
            }
          }
        ]
      },
      "minecraft:is_shaking": {},
      "minecraft:timer": {
        "looping": false,
        "time": 20,
        "time_down_event": {
          "event": "become_stray_event"
        }
      }
    }
  }
}
```

**`minecraft:lightning_immune`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": [
          {
            "deals_damage": true,
            "on_damage": {
              "event": "bone_sword",
              "filters": {
                "all_of": [
                  {
                    "subject": "other",
                    "test": "is_family",
                    "value": "player"
                  },
                  {
                    "test": "has_damage",
                    "value": "fatal"
                  }
                ]
              }
            }
          },
          {
            "deals_damage": false,
            "on_damage": {
              "filters": {
                "other_with_families": "lightning"
              }
            }
          }
        ]
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": false,
          "on_damage": {
            "filters": {
              "other_with_families": "lightning"
            }
          }
        }
      }
    }
  }
}
```

**`minecraft:melee_attack`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:attack": {
        "damage": 3
      },
      "minecraft:behavior.melee_attack": {
        "priority": 4,
        "speed_multiplier": 1.25,
        "target_dist": 1.2,
        "track_target": true
      },
      "minecraft:environment_sensor": {
        "triggers": {
          "event": "minecraft:ranged_mode",
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "in_water",
            "value": false
          }
        }
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:attack": {
        "damage": 2
      },
      "minecraft:behavior.melee_attack": {
        "priority": 4,
        "speed_multiplier": 1.25,
        "track_target": true
      },
      "minecraft:environment_sensor": {
        "triggers": [
          {
            "event": "minecraft:ranged_mode",
            "filters": {
              "all_of": [
                {
                  "operator": "==",
                  "subject": "self",
                  "test": "in_water",
                  "value": false
                },
                {
                  "operator": "==",
                  "subject": "self",
                  "test": "has_ranged_weapon",
                  "value": true
                }
              ]
            }
          },
          {
            "event": "got_in_powder_snow",
            "filters": {
              "operator": "==",
              "subject": "self",
              "test": "in_block",
              "value": "minecraft:powder_snow"
            }
          }
        ]
      }
    }
  }
}
```

**`minecraft:ranged_attack`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:behavior.ranged_attack": {
        "attack_interval_max": 3,
        "attack_interval_min": 1,
        "attack_radius": 15
      },
      "minecraft:environment_sensor": {
        "triggers": {
          "event": "minecraft:melee_mode",
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_underwater",
            "value": true
          }
        }
      },
      "minecraft:shooter": {
        "def": "minecraft:arrow",
        "type": "Arrow"
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:behavior.ranged_attack": {
        "attack_interval_max": 3.0,
        "attack_interval_min": 1.0,
        "attack_radius": 15.0,
        "priority": 0
      },
      "minecraft:environment_sensor": {
        "triggers": [
          {
            "event": "minecraft:melee_mode",
            "filters": {
              "operator": "==",
              "subject": "self",
              "test": "is_underwater",
              "value": true
            }
          },
          {
            "event": "minecraft:melee_mode",
            "filters": {
              "operator": "==",
              "subject": "self",
              "test": "has_ranged_weapon",
              "value": false
            }
          },
          {
            "event": "got_in_powder_snow",
            "filters": {
              "operator": "==",
              "subject": "self",
              "test": "in_block",
              "value": "minecraft:powder_snow"
            }
          }
        ]
      },
      "minecraft:shooter": {
        "def": "minecraft:arrow"
      }
    }
  }
}
```

##### `components`

**`minecraft:behavior.equip_item`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "priority": 3
    }
  }
}
```

**`minecraft:behavior.look_at_player`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "look_distance": 8,
      "priority": 6
    }
  },
  "reference": {
    "present": true,
    "value": {
      "look_distance": 8,
      "priority": 7
    }
  }
}
```

**`minecraft:behavior.pickup_items`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "can_pickup_any_item": true,
      "goal_radius": 2,
      "max_dist": 3,
      "pickup_based_on_chance": true,
      "priority": 5,
      "speed_multiplier": 1.0
    }
  }
}
```

**`minecraft:behavior.random_look_around`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "priority": 6
    }
  },
  "reference": {
    "present": true,
    "value": {
      "priority": 8
    }
  }
}
```

**`minecraft:behavior.random_stroll`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "priority": 5,
      "speed_multiplier": 1
    }
  },
  "reference": {
    "present": true,
    "value": {
      "priority": 6,
      "speed_multiplier": 1
    }
  }
}
```

**`minecraft:behavior.ranged_attack`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "attack_interval_max": 3,
      "attack_interval_min": 1,
      "attack_radius": 15
    }
  },
  "reference": {
    "present": true,
    "value": {
      "attack_interval_max": 3.0,
      "attack_interval_min": 1.0,
      "attack_radius": 15.0,
      "priority": 0
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

**`minecraft:damage_sensor`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "triggers": [
        {
          "deals_damage": true,
          "on_damage": {
            "event": "bone_sword",
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "player"
                },
                {
                  "test": "has_damage",
                  "value": "fatal"
                }
              ]
            }
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

**`minecraft:environment_sensor`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "triggers": {
        "event": "minecraft:melee_mode",
        "filters": {
          "operator": "==",
          "subject": "self",
          "test": "is_underwater",
          "value": true
        }
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "triggers": [
        {
          "event": "minecraft:melee_mode",
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_underwater",
            "value": true
          }
        },
        {
          "event": "minecraft:melee_mode",
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "has_ranged_weapon",
            "value": false
          }
        },
        {
          "event": "got_in_powder_snow",
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "in_block",
            "value": "minecraft:powder_snow"
          }
        }
      ]
    }
  }
}
```

**`minecraft:equip_item`**

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

**`minecraft:shareables`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "items": [
        {
          "item": "minecraft:netherite_sword",
          "priority": 0,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:diamond_sword",
          "priority": 1,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:iron_sword",
          "priority": 2,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:stone_sword",
          "priority": 3,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:golden_sword",
          "priority": 4,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:wooden_sword",
          "priority": 5,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:bow",
          "priority": 6,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:netherite_helmet",
          "priority": 0,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:diamond_helmet",
          "priority": 1,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:iron_helmet",
          "priority": 2,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:chainmail_helmet",
          "priority": 3,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:golden_helmet",
          "priority": 4,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:leather_helmet",
          "priority": 5,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:turtle_helmet",
          "priority": 6,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:skull:0",
          "priority": 7,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:skull:1",
          "priority": 7,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:carved_pumpkin",
          "priority": 7,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:netherite_chestplate",
          "priority": 0,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:diamond_chestplate",
          "priority": 1,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:iron_chestplate",
          "priority": 2,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:chainmail_chestplate",
          "priority": 3,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:golden_chestplate",
          "priority": 4,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:leather_chestplate",
          "priority": 5,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:netherite_leggings",
          "priority": 0,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:diamond_leggings",
          "priority": 1,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:iron_leggings",
          "priority": 2,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:chainmail_leggings",
          "priority": 3,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:golden_leggings",
          "priority": 4,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:leather_leggings",
          "priority": 5,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:netherite_boots",
          "priority": 0,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:diamond_boots",
          "priority": 1,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:iron_boots",
          "priority": 2,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:chainmail_boots",
          "priority": 3,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:golden_boots",
          "priority": 4,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:leather_boots",
          "priority": 5,
          "surplus_amount": 1,
          "want_amount": 1
        }
      ]
    }
  }
}
```

**`minecraft:shooter`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "def": "minecraft:arrow",
      "type": "Arrow"
    }
  },
  "reference": {
    "present": true,
    "value": {
      "def": "minecraft:arrow"
    }
  }
}
```

##### `events`

**`become_stray_event`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "become_stray"
        ]
      }
    }
  }
}
```

**`bone_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "filters": {
            "all_of": [
              {
                "test": "has_biome_tag",
                "value": "desert"
              },
              {
                "operator": "<",
                "test": "is_brightness",
                "value": 0.49
              }
            ]
          },
          "randomize": [
            {
              "weight": 993
            },
            {
              "run_command": {
                "command": [
                  "structure load bone_sword ~ ~ ~"
                ]
              },
              "weight": 7
            }
          ]
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`got_in_powder_snow`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "in_powder_snow"
        ]
      }
    }
  }
}
```

**`got_out_of_powder_snow`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "got_out_of_powder_snow_environment_sensor"
        ]
      },
      "remove": {
        "component_groups": [
          "in_powder_snow"
        ]
      }
    }
  }
}
```

**`minecraft:melee_mode`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:melee_attack"
        ]
      },
      "remove": {
        "component_groups": [
          "minecraft:ranged_attack"
        ]
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:melee_attack"
        ]
      },
      "remove": {
        "component_groups": [
          "minecraft:ranged_attack",
          "got_out_of_powder_snow_environment_sensor"
        ]
      }
    }
  }
}
```

**`minecraft:ranged_mode`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:ranged_attack"
        ]
      },
      "remove": {
        "component_groups": [
          "minecraft:melee_attack"
        ]
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:ranged_attack"
        ]
      },
      "remove": {
        "component_groups": [
          "minecraft:melee_attack",
          "got_out_of_powder_snow_environment_sensor"
        ]
      }
    }
  }
}
```

##### `root`

**`format_version`**

```json
{
  "addon": {
    "present": true,
    "value": "1.13.0"
  },
  "reference": {
    "present": true,
    "value": "1.18.20"
  }
}
```

#### Образец `1.20.30.1`

SHA-256 файла образца: `2af6271b7d4bbe239aa5fb4f14a2b16f56cb02d7f8260f9358e14efda4056773`.

##### `component_groups`

**`become_stray`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:transformation": {
        "drop_inventory": true,
        "into": "minecraft:stray",
        "keep_level": true,
        "preserve_equipment": true,
        "transformation_sound": "convert_to_stray"
      }
    }
  }
}
```

**`got_out_of_powder_snow_environment_sensor`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:environment_sensor": {
        "triggers": [
          {
            "event": "minecraft:melee_mode",
            "filters": {
              "operator": "==",
              "subject": "self",
              "test": "is_underwater",
              "value": true
            }
          },
          {
            "event": "minecraft:melee_mode",
            "filters": {
              "operator": "==",
              "subject": "self",
              "test": "has_ranged_weapon",
              "value": false
            }
          },
          {
            "event": "minecraft:ranged_mode",
            "filters": {
              "all_of": [
                {
                  "operator": "==",
                  "subject": "self",
                  "test": "in_water",
                  "value": false
                },
                {
                  "operator": "==",
                  "subject": "self",
                  "test": "has_ranged_weapon",
                  "value": true
                }
              ]
            }
          }
        ]
      }
    }
  }
}
```

**`in_powder_snow`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:environment_sensor": {
        "triggers": [
          {
            "event": "got_out_of_powder_snow",
            "filters": {
              "operator": "!=",
              "subject": "self",
              "test": "in_block",
              "value": "minecraft:powder_snow"
            }
          }
        ]
      },
      "minecraft:is_shaking": {},
      "minecraft:timer": {
        "looping": false,
        "time": 20,
        "time_down_event": {
          "event": "become_stray_event"
        }
      }
    }
  }
}
```

**`minecraft:lightning_immune`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": [
          {
            "deals_damage": true,
            "on_damage": {
              "event": "bone_sword",
              "filters": {
                "all_of": [
                  {
                    "subject": "other",
                    "test": "is_family",
                    "value": "player"
                  },
                  {
                    "test": "has_damage",
                    "value": "fatal"
                  }
                ]
              }
            }
          },
          {
            "deals_damage": false,
            "on_damage": {
              "filters": {
                "other_with_families": "lightning"
              }
            }
          }
        ]
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:damage_sensor": {
        "triggers": {
          "deals_damage": false,
          "on_damage": {
            "filters": {
              "other_with_families": "lightning"
            }
          }
        }
      }
    }
  }
}
```

**`minecraft:melee_attack`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:attack": {
        "damage": 3
      },
      "minecraft:behavior.melee_attack": {
        "priority": 4,
        "speed_multiplier": 1.25,
        "target_dist": 1.2,
        "track_target": true
      },
      "minecraft:environment_sensor": {
        "triggers": {
          "event": "minecraft:ranged_mode",
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "in_water",
            "value": false
          }
        }
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:attack": {
        "damage": 2
      },
      "minecraft:behavior.melee_attack": {
        "priority": 4,
        "speed_multiplier": 1.25,
        "track_target": true
      },
      "minecraft:environment_sensor": {
        "triggers": [
          {
            "event": "minecraft:ranged_mode",
            "filters": {
              "all_of": [
                {
                  "operator": "==",
                  "subject": "self",
                  "test": "in_water",
                  "value": false
                },
                {
                  "operator": "==",
                  "subject": "self",
                  "test": "has_ranged_weapon",
                  "value": true
                }
              ]
            }
          },
          {
            "event": "got_in_powder_snow",
            "filters": {
              "operator": "==",
              "subject": "self",
              "test": "in_block",
              "value": "minecraft:powder_snow"
            }
          }
        ]
      }
    }
  }
}
```

**`minecraft:ranged_attack`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:behavior.ranged_attack": {
        "attack_interval_max": 3,
        "attack_interval_min": 1,
        "attack_radius": 15
      },
      "minecraft:environment_sensor": {
        "triggers": {
          "event": "minecraft:melee_mode",
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_underwater",
            "value": true
          }
        }
      },
      "minecraft:shooter": {
        "def": "minecraft:arrow",
        "type": "Arrow"
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:behavior.ranged_attack": {
        "attack_interval_max": 3.0,
        "attack_interval_min": 1.0,
        "attack_radius": 15.0,
        "priority": 0
      },
      "minecraft:environment_sensor": {
        "triggers": [
          {
            "event": "minecraft:melee_mode",
            "filters": {
              "operator": "==",
              "subject": "self",
              "test": "is_underwater",
              "value": true
            }
          },
          {
            "event": "minecraft:melee_mode",
            "filters": {
              "operator": "==",
              "subject": "self",
              "test": "has_ranged_weapon",
              "value": false
            }
          },
          {
            "event": "got_in_powder_snow",
            "filters": {
              "operator": "==",
              "subject": "self",
              "test": "in_block",
              "value": "minecraft:powder_snow"
            }
          }
        ]
      },
      "minecraft:shooter": {
        "def": "minecraft:arrow",
        "sound": "bow"
      }
    }
  }
}
```

##### `components`

**`minecraft:behavior.equip_item`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "priority": 3
    }
  }
}
```

**`minecraft:behavior.look_at_player`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "look_distance": 8,
      "priority": 6
    }
  },
  "reference": {
    "present": true,
    "value": {
      "look_distance": 8,
      "priority": 7
    }
  }
}
```

**`minecraft:behavior.pickup_items`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "can_pickup_any_item": true,
      "goal_radius": 2,
      "max_dist": 3,
      "pickup_based_on_chance": true,
      "priority": 5,
      "speed_multiplier": 1.0
    }
  }
}
```

**`minecraft:behavior.random_look_around`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "priority": 6
    }
  },
  "reference": {
    "present": true,
    "value": {
      "priority": 8
    }
  }
}
```

**`minecraft:behavior.random_stroll`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "priority": 5,
      "speed_multiplier": 1
    }
  },
  "reference": {
    "present": true,
    "value": {
      "priority": 6,
      "speed_multiplier": 1
    }
  }
}
```

**`minecraft:behavior.ranged_attack`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "attack_interval_max": 3,
      "attack_interval_min": 1,
      "attack_radius": 15
    }
  },
  "reference": {
    "present": true,
    "value": {
      "attack_interval_max": 3.0,
      "attack_interval_min": 1.0,
      "attack_radius": 15.0,
      "priority": 0
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

**`minecraft:damage_sensor`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "triggers": [
        {
          "deals_damage": true,
          "on_damage": {
            "event": "bone_sword",
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "player"
                },
                {
                  "test": "has_damage",
                  "value": "fatal"
                }
              ]
            }
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

**`minecraft:environment_sensor`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "triggers": {
        "event": "minecraft:melee_mode",
        "filters": {
          "operator": "==",
          "subject": "self",
          "test": "is_underwater",
          "value": true
        }
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "triggers": [
        {
          "event": "minecraft:melee_mode",
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "is_underwater",
            "value": true
          }
        },
        {
          "event": "minecraft:melee_mode",
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "has_ranged_weapon",
            "value": false
          }
        },
        {
          "event": "got_in_powder_snow",
          "filters": {
            "operator": "==",
            "subject": "self",
            "test": "in_block",
            "value": "minecraft:powder_snow"
          }
        }
      ]
    }
  }
}
```

**`minecraft:equip_item`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "excluded_items": [
        {
          "item": "minecraft:banner:15"
        }
      ]
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

**`minecraft:shareables`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "items": [
        {
          "item": "minecraft:netherite_sword",
          "priority": 0,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:diamond_sword",
          "priority": 1,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:iron_sword",
          "priority": 2,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:stone_sword",
          "priority": 3,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:golden_sword",
          "priority": 4,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:wooden_sword",
          "priority": 5,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:bow",
          "priority": 6,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:netherite_helmet",
          "priority": 0,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:diamond_helmet",
          "priority": 1,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:iron_helmet",
          "priority": 2,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:chainmail_helmet",
          "priority": 3,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:golden_helmet",
          "priority": 4,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:leather_helmet",
          "priority": 5,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:turtle_helmet",
          "priority": 6,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:skull:0",
          "priority": 7,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:skull:1",
          "priority": 7,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:carved_pumpkin",
          "priority": 7,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:netherite_chestplate",
          "priority": 0,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:diamond_chestplate",
          "priority": 1,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:iron_chestplate",
          "priority": 2,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:chainmail_chestplate",
          "priority": 3,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:golden_chestplate",
          "priority": 4,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:leather_chestplate",
          "priority": 5,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:netherite_leggings",
          "priority": 0,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:diamond_leggings",
          "priority": 1,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:iron_leggings",
          "priority": 2,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:chainmail_leggings",
          "priority": 3,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:golden_leggings",
          "priority": 4,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:leather_leggings",
          "priority": 5,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:netherite_boots",
          "priority": 0,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:diamond_boots",
          "priority": 1,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:iron_boots",
          "priority": 2,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:chainmail_boots",
          "priority": 3,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:golden_boots",
          "priority": 4,
          "surplus_amount": 1,
          "want_amount": 1
        },
        {
          "item": "minecraft:leather_boots",
          "priority": 5,
          "surplus_amount": 1,
          "want_amount": 1
        }
      ],
      "singular_pickup": true
    }
  }
}
```

**`minecraft:shooter`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "def": "minecraft:arrow",
      "type": "Arrow"
    }
  },
  "reference": {
    "present": true,
    "value": {
      "def": "minecraft:arrow"
    }
  }
}
```

##### `events`

**`become_stray_event`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "become_stray"
        ]
      }
    }
  }
}
```

**`bone_sword`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "sequence": [
        {
          "filters": {
            "all_of": [
              {
                "test": "has_biome_tag",
                "value": "desert"
              },
              {
                "operator": "<",
                "test": "is_brightness",
                "value": 0.49
              }
            ]
          },
          "randomize": [
            {
              "weight": 993
            },
            {
              "run_command": {
                "command": [
                  "structure load bone_sword ~ ~ ~"
                ]
              },
              "weight": 7
            }
          ]
        }
      ]
    }
  },
  "reference": {
    "present": false
  }
}
```

**`got_in_powder_snow`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "in_powder_snow"
        ]
      }
    }
  }
}
```

**`got_out_of_powder_snow`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "got_out_of_powder_snow_environment_sensor"
        ]
      },
      "remove": {
        "component_groups": [
          "in_powder_snow"
        ]
      }
    }
  }
}
```

**`minecraft:melee_mode`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:melee_attack"
        ]
      },
      "remove": {
        "component_groups": [
          "minecraft:ranged_attack"
        ]
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:melee_attack"
        ]
      },
      "remove": {
        "component_groups": [
          "minecraft:ranged_attack",
          "got_out_of_powder_snow_environment_sensor"
        ]
      }
    }
  }
}
```

**`minecraft:ranged_mode`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:ranged_attack"
        ]
      },
      "remove": {
        "component_groups": [
          "minecraft:melee_attack"
        ]
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "add": {
        "component_groups": [
          "minecraft:ranged_attack"
        ]
      },
      "remove": {
        "component_groups": [
          "minecraft:melee_attack",
          "got_out_of_powder_snow_environment_sensor"
        ]
      }
    }
  }
}
```

##### `root`

**`format_version`**

```json
{
  "addon": {
    "present": true,
    "value": "1.13.0"
  },
  "reference": {
    "present": true,
    "value": "1.18.20"
  }
}
```

## `minecraft:wolf`

### Аддон `2.8.14`

SHA-256 файла: `03caf1ef629458d090f9517820bf3218cf43694289782394e51dcbe13ee4d060`.

#### Образец `1.19.40.2`

SHA-256 файла образца: `5754ff9d0058c5e514c3a5bab19415bc8bf4889d5d5222454de7bef3b23f6c6f`.

##### `component_groups`

**`minecraft:wolf_adult`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:breedable": {
        "breed_items": [
          "chicken",
          "cooked_chicken",
          "beef",
          "cooked_beef",
          "muttonRaw",
          "muttonCooked",
          "porkchop",
          "cooked_porkchop",
          "rabbit",
          "cooked_rabbit",
          "rotten_flesh"
        ],
        "breeds_with": {
          "baby_type": "minecraft:wolf",
          "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
          },
          "mate_type": "minecraft:wolf"
        },
        "require_tame": true
      },
      "minecraft:experience_reward": {
        "on_bred": "Math.Random(1,7)",
        "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
      },
      "minecraft:loot": {
        "table": "loot_tables/entities/wolf.json"
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:breedable": {
        "breed_items": [
          "chicken",
          "cooked_chicken",
          "beef",
          "cooked_beef",
          "muttonRaw",
          "muttonCooked",
          "porkchop",
          "cooked_porkchop",
          "rabbit",
          "cooked_rabbit",
          "rotten_flesh"
        ],
        "breeds_with": {
          "baby_type": "minecraft:wolf",
          "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
          },
          "mate_type": "minecraft:wolf"
        },
        "require_full_health": true,
        "require_tame": true
      },
      "minecraft:experience_reward": {
        "on_bred": "Math.Random(1,7)",
        "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
      },
      "minecraft:loot": {
        "table": "loot_tables/entities/wolf.json"
      }
    }
  }
}
```

**`minecraft:wolf_angry`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:angry": {
        "broadcast_anger": true,
        "broadcast_range": 20,
        "calm_event": {
          "event": "minecraft:on_calm",
          "target": "self"
        },
        "duration": 25
      },
      "minecraft:on_target_acquired": {}
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:angry": {
        "broadcast_anger": true,
        "broadcast_range": 20,
        "calm_event": {
          "event": "minecraft:on_calm",
          "target": "self"
        },
        "duration": 25
      },
      "minecraft:on_target_acquired": {},
      "minecraft:rideable": {
        "family_types": [
          "zombie"
        ],
        "seat_count": 1,
        "seats": {
          "position": [
            0.0,
            0.675,
            -0.1
          ]
        }
      }
    }
  }
}
```

**`minecraft:wolf_tame`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:attack": {
        "damage": 4
      },
      "minecraft:behavior.breed": {
        "priority": 7
      },
      "minecraft:behavior.follow_owner": {
        "priority": 6,
        "speed_multiplier": 1.0,
        "start_distance": 10,
        "stop_distance": 2
      },
      "minecraft:behavior.nearest_attackable_target": {
        "attack_interval": 10,
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "skeleton"
            },
            "max_dist": 16
          }
        ],
        "must_see": true,
        "priority": 5
      },
      "minecraft:behavior.owner_hurt_by_target": {
        "priority": 1
      },
      "minecraft:behavior.owner_hurt_target": {
        "priority": 2
      },
      "minecraft:color": {
        "value": 14
      },
      "minecraft:health": {
        "max": 20,
        "value": 20
      },
      "minecraft:is_dyeable": {
        "interact_text": "action.interact.dye"
      },
      "minecraft:is_tamed": {},
      "minecraft:leashable": {
        "hard_distance": 6.0,
        "max_distance": 10.0,
        "on_leash": {
          "event": "minecraft:on_leash",
          "target": "self"
        },
        "on_unleash": {
          "event": "minecraft:on_unleash",
          "target": "self"
        },
        "soft_distance": 4.0
      },
      "minecraft:sittable": {},
      "minecraft:type_family": {
        "family": [
          "wolf",
          "mob",
          "tamed"
        ]
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:attack": {
        "damage": 4
      },
      "minecraft:behavior.breed": {
        "priority": 2,
        "speed_multiplier": 1.0
      },
      "minecraft:behavior.follow_owner": {
        "priority": 6,
        "speed_multiplier": 1.0,
        "start_distance": 10,
        "stop_distance": 2
      },
      "minecraft:behavior.nearest_attackable_target": {
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "skeleton"
            },
            "max_dist": 16
          }
        ],
        "must_see": true,
        "priority": 5
      },
      "minecraft:behavior.owner_hurt_by_target": {
        "priority": 1
      },
      "minecraft:behavior.owner_hurt_target": {
        "priority": 2
      },
      "minecraft:color": {
        "value": 14
      },
      "minecraft:health": {
        "max": 20,
        "value": 20
      },
      "minecraft:is_dyeable": {
        "interact_text": "action.interact.dye"
      },
      "minecraft:is_tamed": {},
      "minecraft:sittable": {}
    }
  }
}
```

**`minecraft:wolf_wild`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:behavior.avoid_mob_type": {
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "llama"
            },
            "max_dist": 24,
            "sprint_speed_multiplier": 1.5,
            "walk_speed_multiplier": 1.5
          }
        ],
        "priority": 3,
        "probability_per_strength": 0.14
      },
      "minecraft:behavior.nearest_attackable_target": {
        "attack_interval": 10,
        "entity_types": [
          {
            "filters": {
              "any_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "skeleton"
                },
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "sheep"
                },
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "rabbit"
                },
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "fox"
                }
              ]
            },
            "max_dist": 16
          },
          {
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "baby_turtle"
                },
                {
                  "operator": "!=",
                  "subject": "other",
                  "test": "in_water",
                  "value": true
                }
              ]
            },
            "max_dist": 16
          },
          {
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "skeleton"
                },
                {
                  "operator": "!=",
                  "subject": "other",
                  "test": "is_underwater",
                  "value": true
                }
              ]
            },
            "max_dist": 16
          }
        ],
        "must_see": true,
        "priority": 4,
        "reselect_targets": true
      },
      "minecraft:on_target_acquired": {
        "event": "minecraft:become_angry",
        "target": "self"
      },
      "minecraft:rideable": {
        "family_types": [
          "zombie"
        ],
        "seat_count": 1,
        "seats": {
          "position": [
            0.0,
            0.675,
            -0.1
          ]
        }
      },
      "minecraft:tameable": {
        "probability": 0.33,
        "tame_event": {
          "event": "minecraft:on_tame",
          "target": "self"
        },
        "tame_items": "bone"
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:behavior.avoid_mob_type": {
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "llama"
            },
            "max_dist": 24,
            "sprint_speed_multiplier": 1.5,
            "walk_speed_multiplier": 1.5
          }
        ],
        "priority": 3,
        "probability_per_strength": 0.14
      },
      "minecraft:behavior.nearest_attackable_target": {
        "entity_types": [
          {
            "filters": {
              "any_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "skeleton"
                },
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "sheep"
                },
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "rabbit"
                },
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "fox"
                }
              ]
            },
            "max_dist": 16
          },
          {
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "baby_turtle"
                },
                {
                  "operator": "!=",
                  "subject": "other",
                  "test": "in_water",
                  "value": true
                }
              ]
            },
            "max_dist": 16
          },
          {
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "skeleton"
                },
                {
                  "operator": "!=",
                  "subject": "other",
                  "test": "is_underwater",
                  "value": true
                }
              ]
            },
            "max_dist": 16
          }
        ],
        "must_see": true,
        "priority": 4,
        "reselect_targets": true
      },
      "minecraft:on_target_acquired": {
        "event": "minecraft:become_angry",
        "target": "self"
      },
      "minecraft:rideable": {
        "family_types": [
          "zombie"
        ],
        "seat_count": 1,
        "seats": {
          "position": [
            0.0,
            0.675,
            -0.1
          ]
        }
      },
      "minecraft:tameable": {
        "probability": 0.33,
        "tame_event": {
          "event": "minecraft:on_tame",
          "target": "self"
        },
        "tame_items": "bone"
      }
    }
  }
}
```

##### `components`

**`minecraft:balloonable`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "mass": 0.8
    }
  }
}
```

**`minecraft:behavior.melee_attack`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "priority": 5,
      "reach_multiplier": 1.0,
      "target_dist": 1.2,
      "track_target": true
    }
  },
  "reference": {
    "present": true,
    "value": {
      "priority": 5
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

**`minecraft:leashable`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "hard_distance": 6.0,
      "max_distance": 10.0,
      "on_leash": {
        "event": "minecraft:on_leash",
        "target": "self"
      },
      "on_unleash": {
        "event": "minecraft:on_unleash",
        "target": "self"
      },
      "soft_distance": 4.0
    }
  }
}
```

##### `root`

**`format_version`**

```json
{
  "addon": {
    "present": true,
    "value": "1.13.0"
  },
  "reference": {
    "present": true,
    "value": "1.18.10"
  }
}
```

#### Образец `1.20.30.1`

SHA-256 файла образца: `5754ff9d0058c5e514c3a5bab19415bc8bf4889d5d5222454de7bef3b23f6c6f`.

##### `component_groups`

**`minecraft:wolf_adult`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:breedable": {
        "breed_items": [
          "chicken",
          "cooked_chicken",
          "beef",
          "cooked_beef",
          "muttonRaw",
          "muttonCooked",
          "porkchop",
          "cooked_porkchop",
          "rabbit",
          "cooked_rabbit",
          "rotten_flesh"
        ],
        "breeds_with": {
          "baby_type": "minecraft:wolf",
          "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
          },
          "mate_type": "minecraft:wolf"
        },
        "require_tame": true
      },
      "minecraft:experience_reward": {
        "on_bred": "Math.Random(1,7)",
        "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
      },
      "minecraft:loot": {
        "table": "loot_tables/entities/wolf.json"
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:breedable": {
        "breed_items": [
          "chicken",
          "cooked_chicken",
          "beef",
          "cooked_beef",
          "muttonRaw",
          "muttonCooked",
          "porkchop",
          "cooked_porkchop",
          "rabbit",
          "cooked_rabbit",
          "rotten_flesh"
        ],
        "breeds_with": {
          "baby_type": "minecraft:wolf",
          "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
          },
          "mate_type": "minecraft:wolf"
        },
        "require_full_health": true,
        "require_tame": true
      },
      "minecraft:experience_reward": {
        "on_bred": "Math.Random(1,7)",
        "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
      },
      "minecraft:loot": {
        "table": "loot_tables/entities/wolf.json"
      }
    }
  }
}
```

**`minecraft:wolf_angry`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:angry": {
        "broadcast_anger": true,
        "broadcast_range": 20,
        "calm_event": {
          "event": "minecraft:on_calm",
          "target": "self"
        },
        "duration": 25
      },
      "minecraft:on_target_acquired": {}
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:angry": {
        "broadcast_anger": true,
        "broadcast_range": 20,
        "calm_event": {
          "event": "minecraft:on_calm",
          "target": "self"
        },
        "duration": 25
      },
      "minecraft:on_target_acquired": {},
      "minecraft:rideable": {
        "family_types": [
          "zombie"
        ],
        "seat_count": 1,
        "seats": {
          "position": [
            0.0,
            0.675,
            -0.1
          ]
        }
      }
    }
  }
}
```

**`minecraft:wolf_tame`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:attack": {
        "damage": 4
      },
      "minecraft:behavior.breed": {
        "priority": 7
      },
      "minecraft:behavior.follow_owner": {
        "priority": 6,
        "speed_multiplier": 1.0,
        "start_distance": 10,
        "stop_distance": 2
      },
      "minecraft:behavior.nearest_attackable_target": {
        "attack_interval": 10,
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "skeleton"
            },
            "max_dist": 16
          }
        ],
        "must_see": true,
        "priority": 5
      },
      "minecraft:behavior.owner_hurt_by_target": {
        "priority": 1
      },
      "minecraft:behavior.owner_hurt_target": {
        "priority": 2
      },
      "minecraft:color": {
        "value": 14
      },
      "minecraft:health": {
        "max": 20,
        "value": 20
      },
      "minecraft:is_dyeable": {
        "interact_text": "action.interact.dye"
      },
      "minecraft:is_tamed": {},
      "minecraft:leashable": {
        "hard_distance": 6.0,
        "max_distance": 10.0,
        "on_leash": {
          "event": "minecraft:on_leash",
          "target": "self"
        },
        "on_unleash": {
          "event": "minecraft:on_unleash",
          "target": "self"
        },
        "soft_distance": 4.0
      },
      "minecraft:sittable": {},
      "minecraft:type_family": {
        "family": [
          "wolf",
          "mob",
          "tamed"
        ]
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:attack": {
        "damage": 4
      },
      "minecraft:behavior.breed": {
        "priority": 2,
        "speed_multiplier": 1.0
      },
      "minecraft:behavior.follow_owner": {
        "priority": 6,
        "speed_multiplier": 1.0,
        "start_distance": 10,
        "stop_distance": 2
      },
      "minecraft:behavior.nearest_attackable_target": {
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "skeleton"
            },
            "max_dist": 16
          }
        ],
        "must_see": true,
        "priority": 5
      },
      "minecraft:behavior.owner_hurt_by_target": {
        "priority": 1
      },
      "minecraft:behavior.owner_hurt_target": {
        "priority": 2
      },
      "minecraft:color": {
        "value": 14
      },
      "minecraft:health": {
        "max": 20,
        "value": 20
      },
      "minecraft:is_dyeable": {
        "interact_text": "action.interact.dye"
      },
      "minecraft:is_tamed": {},
      "minecraft:sittable": {}
    }
  }
}
```

**`minecraft:wolf_wild`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:behavior.avoid_mob_type": {
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "llama"
            },
            "max_dist": 24,
            "sprint_speed_multiplier": 1.5,
            "walk_speed_multiplier": 1.5
          }
        ],
        "priority": 3,
        "probability_per_strength": 0.14
      },
      "minecraft:behavior.nearest_attackable_target": {
        "attack_interval": 10,
        "entity_types": [
          {
            "filters": {
              "any_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "skeleton"
                },
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "sheep"
                },
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "rabbit"
                },
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "fox"
                }
              ]
            },
            "max_dist": 16
          },
          {
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "baby_turtle"
                },
                {
                  "operator": "!=",
                  "subject": "other",
                  "test": "in_water",
                  "value": true
                }
              ]
            },
            "max_dist": 16
          },
          {
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "skeleton"
                },
                {
                  "operator": "!=",
                  "subject": "other",
                  "test": "is_underwater",
                  "value": true
                }
              ]
            },
            "max_dist": 16
          }
        ],
        "must_see": true,
        "priority": 4,
        "reselect_targets": true
      },
      "minecraft:on_target_acquired": {
        "event": "minecraft:become_angry",
        "target": "self"
      },
      "minecraft:rideable": {
        "family_types": [
          "zombie"
        ],
        "seat_count": 1,
        "seats": {
          "position": [
            0.0,
            0.675,
            -0.1
          ]
        }
      },
      "minecraft:tameable": {
        "probability": 0.33,
        "tame_event": {
          "event": "minecraft:on_tame",
          "target": "self"
        },
        "tame_items": "bone"
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:behavior.avoid_mob_type": {
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "llama"
            },
            "max_dist": 24,
            "sprint_speed_multiplier": 1.5,
            "walk_speed_multiplier": 1.5
          }
        ],
        "priority": 3,
        "probability_per_strength": 0.14
      },
      "minecraft:behavior.nearest_attackable_target": {
        "entity_types": [
          {
            "filters": {
              "any_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "skeleton"
                },
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "sheep"
                },
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "rabbit"
                },
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "fox"
                }
              ]
            },
            "max_dist": 16
          },
          {
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "baby_turtle"
                },
                {
                  "operator": "!=",
                  "subject": "other",
                  "test": "in_water",
                  "value": true
                }
              ]
            },
            "max_dist": 16
          },
          {
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "skeleton"
                },
                {
                  "operator": "!=",
                  "subject": "other",
                  "test": "is_underwater",
                  "value": true
                }
              ]
            },
            "max_dist": 16
          }
        ],
        "must_see": true,
        "priority": 4,
        "reselect_targets": true
      },
      "minecraft:on_target_acquired": {
        "event": "minecraft:become_angry",
        "target": "self"
      },
      "minecraft:rideable": {
        "family_types": [
          "zombie"
        ],
        "seat_count": 1,
        "seats": {
          "position": [
            0.0,
            0.675,
            -0.1
          ]
        }
      },
      "minecraft:tameable": {
        "probability": 0.33,
        "tame_event": {
          "event": "minecraft:on_tame",
          "target": "self"
        },
        "tame_items": "bone"
      }
    }
  }
}
```

##### `components`

**`minecraft:balloonable`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "mass": 0.8
    }
  }
}
```

**`minecraft:behavior.melee_attack`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "priority": 5,
      "reach_multiplier": 1.0,
      "target_dist": 1.2,
      "track_target": true
    }
  },
  "reference": {
    "present": true,
    "value": {
      "priority": 5
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

**`minecraft:leashable`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "hard_distance": 6.0,
      "max_distance": 10.0,
      "on_leash": {
        "event": "minecraft:on_leash",
        "target": "self"
      },
      "on_unleash": {
        "event": "minecraft:on_unleash",
        "target": "self"
      },
      "soft_distance": 4.0
    }
  }
}
```

##### `root`

**`format_version`**

```json
{
  "addon": {
    "present": true,
    "value": "1.13.0"
  },
  "reference": {
    "present": true,
    "value": "1.18.10"
  }
}
```

### Аддон `2.8.8`

SHA-256 файла: `03caf1ef629458d090f9517820bf3218cf43694289782394e51dcbe13ee4d060`.

#### Образец `1.19.40.2`

SHA-256 файла образца: `5754ff9d0058c5e514c3a5bab19415bc8bf4889d5d5222454de7bef3b23f6c6f`.

##### `component_groups`

**`minecraft:wolf_adult`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:breedable": {
        "breed_items": [
          "chicken",
          "cooked_chicken",
          "beef",
          "cooked_beef",
          "muttonRaw",
          "muttonCooked",
          "porkchop",
          "cooked_porkchop",
          "rabbit",
          "cooked_rabbit",
          "rotten_flesh"
        ],
        "breeds_with": {
          "baby_type": "minecraft:wolf",
          "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
          },
          "mate_type": "minecraft:wolf"
        },
        "require_tame": true
      },
      "minecraft:experience_reward": {
        "on_bred": "Math.Random(1,7)",
        "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
      },
      "minecraft:loot": {
        "table": "loot_tables/entities/wolf.json"
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:breedable": {
        "breed_items": [
          "chicken",
          "cooked_chicken",
          "beef",
          "cooked_beef",
          "muttonRaw",
          "muttonCooked",
          "porkchop",
          "cooked_porkchop",
          "rabbit",
          "cooked_rabbit",
          "rotten_flesh"
        ],
        "breeds_with": {
          "baby_type": "minecraft:wolf",
          "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
          },
          "mate_type": "minecraft:wolf"
        },
        "require_full_health": true,
        "require_tame": true
      },
      "minecraft:experience_reward": {
        "on_bred": "Math.Random(1,7)",
        "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
      },
      "minecraft:loot": {
        "table": "loot_tables/entities/wolf.json"
      }
    }
  }
}
```

**`minecraft:wolf_angry`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:angry": {
        "broadcast_anger": true,
        "broadcast_range": 20,
        "calm_event": {
          "event": "minecraft:on_calm",
          "target": "self"
        },
        "duration": 25
      },
      "minecraft:on_target_acquired": {}
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:angry": {
        "broadcast_anger": true,
        "broadcast_range": 20,
        "calm_event": {
          "event": "minecraft:on_calm",
          "target": "self"
        },
        "duration": 25
      },
      "minecraft:on_target_acquired": {},
      "minecraft:rideable": {
        "family_types": [
          "zombie"
        ],
        "seat_count": 1,
        "seats": {
          "position": [
            0.0,
            0.675,
            -0.1
          ]
        }
      }
    }
  }
}
```

**`minecraft:wolf_tame`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:attack": {
        "damage": 4
      },
      "minecraft:behavior.breed": {
        "priority": 7
      },
      "minecraft:behavior.follow_owner": {
        "priority": 6,
        "speed_multiplier": 1.0,
        "start_distance": 10,
        "stop_distance": 2
      },
      "minecraft:behavior.nearest_attackable_target": {
        "attack_interval": 10,
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "skeleton"
            },
            "max_dist": 16
          }
        ],
        "must_see": true,
        "priority": 5
      },
      "minecraft:behavior.owner_hurt_by_target": {
        "priority": 1
      },
      "minecraft:behavior.owner_hurt_target": {
        "priority": 2
      },
      "minecraft:color": {
        "value": 14
      },
      "minecraft:health": {
        "max": 20,
        "value": 20
      },
      "minecraft:is_dyeable": {
        "interact_text": "action.interact.dye"
      },
      "minecraft:is_tamed": {},
      "minecraft:leashable": {
        "hard_distance": 6.0,
        "max_distance": 10.0,
        "on_leash": {
          "event": "minecraft:on_leash",
          "target": "self"
        },
        "on_unleash": {
          "event": "minecraft:on_unleash",
          "target": "self"
        },
        "soft_distance": 4.0
      },
      "minecraft:sittable": {},
      "minecraft:type_family": {
        "family": [
          "wolf",
          "mob",
          "tamed"
        ]
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:attack": {
        "damage": 4
      },
      "minecraft:behavior.breed": {
        "priority": 2,
        "speed_multiplier": 1.0
      },
      "minecraft:behavior.follow_owner": {
        "priority": 6,
        "speed_multiplier": 1.0,
        "start_distance": 10,
        "stop_distance": 2
      },
      "minecraft:behavior.nearest_attackable_target": {
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "skeleton"
            },
            "max_dist": 16
          }
        ],
        "must_see": true,
        "priority": 5
      },
      "minecraft:behavior.owner_hurt_by_target": {
        "priority": 1
      },
      "minecraft:behavior.owner_hurt_target": {
        "priority": 2
      },
      "minecraft:color": {
        "value": 14
      },
      "minecraft:health": {
        "max": 20,
        "value": 20
      },
      "minecraft:is_dyeable": {
        "interact_text": "action.interact.dye"
      },
      "minecraft:is_tamed": {},
      "minecraft:sittable": {}
    }
  }
}
```

**`minecraft:wolf_wild`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:behavior.avoid_mob_type": {
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "llama"
            },
            "max_dist": 24,
            "sprint_speed_multiplier": 1.5,
            "walk_speed_multiplier": 1.5
          }
        ],
        "priority": 3,
        "probability_per_strength": 0.14
      },
      "minecraft:behavior.nearest_attackable_target": {
        "attack_interval": 10,
        "entity_types": [
          {
            "filters": {
              "any_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "skeleton"
                },
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "sheep"
                },
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "rabbit"
                },
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "fox"
                }
              ]
            },
            "max_dist": 16
          },
          {
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "baby_turtle"
                },
                {
                  "operator": "!=",
                  "subject": "other",
                  "test": "in_water",
                  "value": true
                }
              ]
            },
            "max_dist": 16
          },
          {
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "skeleton"
                },
                {
                  "operator": "!=",
                  "subject": "other",
                  "test": "is_underwater",
                  "value": true
                }
              ]
            },
            "max_dist": 16
          }
        ],
        "must_see": true,
        "priority": 4,
        "reselect_targets": true
      },
      "minecraft:on_target_acquired": {
        "event": "minecraft:become_angry",
        "target": "self"
      },
      "minecraft:rideable": {
        "family_types": [
          "zombie"
        ],
        "seat_count": 1,
        "seats": {
          "position": [
            0.0,
            0.675,
            -0.1
          ]
        }
      },
      "minecraft:tameable": {
        "probability": 0.33,
        "tame_event": {
          "event": "minecraft:on_tame",
          "target": "self"
        },
        "tame_items": "bone"
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:behavior.avoid_mob_type": {
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "llama"
            },
            "max_dist": 24,
            "sprint_speed_multiplier": 1.5,
            "walk_speed_multiplier": 1.5
          }
        ],
        "priority": 3,
        "probability_per_strength": 0.14
      },
      "minecraft:behavior.nearest_attackable_target": {
        "entity_types": [
          {
            "filters": {
              "any_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "skeleton"
                },
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "sheep"
                },
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "rabbit"
                },
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "fox"
                }
              ]
            },
            "max_dist": 16
          },
          {
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "baby_turtle"
                },
                {
                  "operator": "!=",
                  "subject": "other",
                  "test": "in_water",
                  "value": true
                }
              ]
            },
            "max_dist": 16
          },
          {
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "skeleton"
                },
                {
                  "operator": "!=",
                  "subject": "other",
                  "test": "is_underwater",
                  "value": true
                }
              ]
            },
            "max_dist": 16
          }
        ],
        "must_see": true,
        "priority": 4,
        "reselect_targets": true
      },
      "minecraft:on_target_acquired": {
        "event": "minecraft:become_angry",
        "target": "self"
      },
      "minecraft:rideable": {
        "family_types": [
          "zombie"
        ],
        "seat_count": 1,
        "seats": {
          "position": [
            0.0,
            0.675,
            -0.1
          ]
        }
      },
      "minecraft:tameable": {
        "probability": 0.33,
        "tame_event": {
          "event": "minecraft:on_tame",
          "target": "self"
        },
        "tame_items": "bone"
      }
    }
  }
}
```

##### `components`

**`minecraft:balloonable`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "mass": 0.8
    }
  }
}
```

**`minecraft:behavior.melee_attack`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "priority": 5,
      "reach_multiplier": 1.0,
      "target_dist": 1.2,
      "track_target": true
    }
  },
  "reference": {
    "present": true,
    "value": {
      "priority": 5
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

**`minecraft:leashable`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "hard_distance": 6.0,
      "max_distance": 10.0,
      "on_leash": {
        "event": "minecraft:on_leash",
        "target": "self"
      },
      "on_unleash": {
        "event": "minecraft:on_unleash",
        "target": "self"
      },
      "soft_distance": 4.0
    }
  }
}
```

##### `root`

**`format_version`**

```json
{
  "addon": {
    "present": true,
    "value": "1.13.0"
  },
  "reference": {
    "present": true,
    "value": "1.18.10"
  }
}
```

#### Образец `1.20.30.1`

SHA-256 файла образца: `5754ff9d0058c5e514c3a5bab19415bc8bf4889d5d5222454de7bef3b23f6c6f`.

##### `component_groups`

**`minecraft:wolf_adult`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:breedable": {
        "breed_items": [
          "chicken",
          "cooked_chicken",
          "beef",
          "cooked_beef",
          "muttonRaw",
          "muttonCooked",
          "porkchop",
          "cooked_porkchop",
          "rabbit",
          "cooked_rabbit",
          "rotten_flesh"
        ],
        "breeds_with": {
          "baby_type": "minecraft:wolf",
          "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
          },
          "mate_type": "minecraft:wolf"
        },
        "require_tame": true
      },
      "minecraft:experience_reward": {
        "on_bred": "Math.Random(1,7)",
        "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
      },
      "minecraft:loot": {
        "table": "loot_tables/entities/wolf.json"
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:breedable": {
        "breed_items": [
          "chicken",
          "cooked_chicken",
          "beef",
          "cooked_beef",
          "muttonRaw",
          "muttonCooked",
          "porkchop",
          "cooked_porkchop",
          "rabbit",
          "cooked_rabbit",
          "rotten_flesh"
        ],
        "breeds_with": {
          "baby_type": "minecraft:wolf",
          "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
          },
          "mate_type": "minecraft:wolf"
        },
        "require_full_health": true,
        "require_tame": true
      },
      "minecraft:experience_reward": {
        "on_bred": "Math.Random(1,7)",
        "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
      },
      "minecraft:loot": {
        "table": "loot_tables/entities/wolf.json"
      }
    }
  }
}
```

**`minecraft:wolf_angry`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:angry": {
        "broadcast_anger": true,
        "broadcast_range": 20,
        "calm_event": {
          "event": "minecraft:on_calm",
          "target": "self"
        },
        "duration": 25
      },
      "minecraft:on_target_acquired": {}
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:angry": {
        "broadcast_anger": true,
        "broadcast_range": 20,
        "calm_event": {
          "event": "minecraft:on_calm",
          "target": "self"
        },
        "duration": 25
      },
      "minecraft:on_target_acquired": {},
      "minecraft:rideable": {
        "family_types": [
          "zombie"
        ],
        "seat_count": 1,
        "seats": {
          "position": [
            0.0,
            0.675,
            -0.1
          ]
        }
      }
    }
  }
}
```

**`minecraft:wolf_tame`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:attack": {
        "damage": 4
      },
      "minecraft:behavior.breed": {
        "priority": 7
      },
      "minecraft:behavior.follow_owner": {
        "priority": 6,
        "speed_multiplier": 1.0,
        "start_distance": 10,
        "stop_distance": 2
      },
      "minecraft:behavior.nearest_attackable_target": {
        "attack_interval": 10,
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "skeleton"
            },
            "max_dist": 16
          }
        ],
        "must_see": true,
        "priority": 5
      },
      "minecraft:behavior.owner_hurt_by_target": {
        "priority": 1
      },
      "minecraft:behavior.owner_hurt_target": {
        "priority": 2
      },
      "minecraft:color": {
        "value": 14
      },
      "minecraft:health": {
        "max": 20,
        "value": 20
      },
      "minecraft:is_dyeable": {
        "interact_text": "action.interact.dye"
      },
      "minecraft:is_tamed": {},
      "minecraft:leashable": {
        "hard_distance": 6.0,
        "max_distance": 10.0,
        "on_leash": {
          "event": "minecraft:on_leash",
          "target": "self"
        },
        "on_unleash": {
          "event": "minecraft:on_unleash",
          "target": "self"
        },
        "soft_distance": 4.0
      },
      "minecraft:sittable": {},
      "minecraft:type_family": {
        "family": [
          "wolf",
          "mob",
          "tamed"
        ]
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:attack": {
        "damage": 4
      },
      "minecraft:behavior.breed": {
        "priority": 2,
        "speed_multiplier": 1.0
      },
      "minecraft:behavior.follow_owner": {
        "priority": 6,
        "speed_multiplier": 1.0,
        "start_distance": 10,
        "stop_distance": 2
      },
      "minecraft:behavior.nearest_attackable_target": {
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "skeleton"
            },
            "max_dist": 16
          }
        ],
        "must_see": true,
        "priority": 5
      },
      "minecraft:behavior.owner_hurt_by_target": {
        "priority": 1
      },
      "minecraft:behavior.owner_hurt_target": {
        "priority": 2
      },
      "minecraft:color": {
        "value": 14
      },
      "minecraft:health": {
        "max": 20,
        "value": 20
      },
      "minecraft:is_dyeable": {
        "interact_text": "action.interact.dye"
      },
      "minecraft:is_tamed": {},
      "minecraft:sittable": {}
    }
  }
}
```

**`minecraft:wolf_wild`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "minecraft:behavior.avoid_mob_type": {
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "llama"
            },
            "max_dist": 24,
            "sprint_speed_multiplier": 1.5,
            "walk_speed_multiplier": 1.5
          }
        ],
        "priority": 3,
        "probability_per_strength": 0.14
      },
      "minecraft:behavior.nearest_attackable_target": {
        "attack_interval": 10,
        "entity_types": [
          {
            "filters": {
              "any_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "skeleton"
                },
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "sheep"
                },
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "rabbit"
                },
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "fox"
                }
              ]
            },
            "max_dist": 16
          },
          {
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "baby_turtle"
                },
                {
                  "operator": "!=",
                  "subject": "other",
                  "test": "in_water",
                  "value": true
                }
              ]
            },
            "max_dist": 16
          },
          {
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "skeleton"
                },
                {
                  "operator": "!=",
                  "subject": "other",
                  "test": "is_underwater",
                  "value": true
                }
              ]
            },
            "max_dist": 16
          }
        ],
        "must_see": true,
        "priority": 4,
        "reselect_targets": true
      },
      "minecraft:on_target_acquired": {
        "event": "minecraft:become_angry",
        "target": "self"
      },
      "minecraft:rideable": {
        "family_types": [
          "zombie"
        ],
        "seat_count": 1,
        "seats": {
          "position": [
            0.0,
            0.675,
            -0.1
          ]
        }
      },
      "minecraft:tameable": {
        "probability": 0.33,
        "tame_event": {
          "event": "minecraft:on_tame",
          "target": "self"
        },
        "tame_items": "bone"
      }
    }
  },
  "reference": {
    "present": true,
    "value": {
      "minecraft:behavior.avoid_mob_type": {
        "entity_types": [
          {
            "filters": {
              "subject": "other",
              "test": "is_family",
              "value": "llama"
            },
            "max_dist": 24,
            "sprint_speed_multiplier": 1.5,
            "walk_speed_multiplier": 1.5
          }
        ],
        "priority": 3,
        "probability_per_strength": 0.14
      },
      "minecraft:behavior.nearest_attackable_target": {
        "entity_types": [
          {
            "filters": {
              "any_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "skeleton"
                },
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "sheep"
                },
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "rabbit"
                },
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "fox"
                }
              ]
            },
            "max_dist": 16
          },
          {
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "baby_turtle"
                },
                {
                  "operator": "!=",
                  "subject": "other",
                  "test": "in_water",
                  "value": true
                }
              ]
            },
            "max_dist": 16
          },
          {
            "filters": {
              "all_of": [
                {
                  "subject": "other",
                  "test": "is_family",
                  "value": "skeleton"
                },
                {
                  "operator": "!=",
                  "subject": "other",
                  "test": "is_underwater",
                  "value": true
                }
              ]
            },
            "max_dist": 16
          }
        ],
        "must_see": true,
        "priority": 4,
        "reselect_targets": true
      },
      "minecraft:on_target_acquired": {
        "event": "minecraft:become_angry",
        "target": "self"
      },
      "minecraft:rideable": {
        "family_types": [
          "zombie"
        ],
        "seat_count": 1,
        "seats": {
          "position": [
            0.0,
            0.675,
            -0.1
          ]
        }
      },
      "minecraft:tameable": {
        "probability": 0.33,
        "tame_event": {
          "event": "minecraft:on_tame",
          "target": "self"
        },
        "tame_items": "bone"
      }
    }
  }
}
```

##### `components`

**`minecraft:balloonable`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "mass": 0.8
    }
  }
}
```

**`minecraft:behavior.melee_attack`**

```json
{
  "addon": {
    "present": true,
    "value": {
      "priority": 5,
      "reach_multiplier": 1.0,
      "target_dist": 1.2,
      "track_target": true
    }
  },
  "reference": {
    "present": true,
    "value": {
      "priority": 5
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

**`minecraft:leashable`**

```json
{
  "addon": {
    "present": false
  },
  "reference": {
    "present": true,
    "value": {
      "hard_distance": 6.0,
      "max_distance": 10.0,
      "on_leash": {
        "event": "minecraft:on_leash",
        "target": "self"
      },
      "on_unleash": {
        "event": "minecraft:on_unleash",
        "target": "self"
      },
      "soft_distance": 4.0
    }
  }
}
```

##### `root`

**`format_version`**

```json
{
  "addon": {
    "present": true,
    "value": "1.13.0"
  },
  "reference": {
    "present": true,
    "value": "1.18.10"
  }
}
```
