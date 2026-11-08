# Клиентские контроллеры, частицы и материалы: полные исходные объекты

Это справочный архив для описаний из resource pack. Проверены только локальные JSON и `.material` в папках `animation_controllers`, `render_controllers`, `particles`, `materials`. В 1.6 таких файлов по указанным путям нет; это не означает, что ванильные или внешние ресурсы не используются. Все перечисленные файлы 2.8.8 и 2.8.14 побайтово совпадают по SHA-256 и дают одинаковые разобранные объекты.

Порядок массивов, численные значения, поля контроллеров, условия, частицы и Molang ниже сохранены; исходные комментарии и форматирование JSON5 не сохраняются. В случае повторных ключей JSON5 оставляет последнее значение; архивы — эталон. Таблица ключей материалов — буквальные имена внутри `materials`, включая возможные метаданные, не утверждение о регистрации каждого ключа как отдельного материала.

Сводка файлов: `animation_controllers` — 5, `render_controllers` — 15, `particles` — 7, `materials` — 1; всего 28.

- Ошибки разбора: нет.
- Повторные ключи: нет.

| Категория | Исходный файл | Объявленные имена / ключи |
|---|---|---|
| `animation_controllers` | `Swords_R/animation_controllers/baby_slime.animation_controllers.json` | `controller.animation.baby_slime.move` |
| `animation_controllers` | `Swords_R/animation_controllers/ghost.animation_controllers.json` | `controller.animation.ghost.move` |
| `animation_controllers` | `Swords_R/animation_controllers/grass.animation_controllers.json` | `controller.animation.grass.move` |
| `animation_controllers` | `Swords_R/animation_controllers/shulker_shield.animation_controllers.json` | `controller.animation.shulker_shield.move` |
| `animation_controllers` | `Swords_R/animation_controllers/ultra_instinct_projectile.animation_controllers.json` | `controller.animation.ultra_instinct_projectile.move` |
| `materials` | `Swords_R/materials/entity.material` | `version`, `grass:entity_alphatest`, `shulker_shield:entity_alphatest`, `ultra_instinct_projectile:charged_creeper`, `ultra_instinct_aura:charged_creeper`, `player_ghost:charged_creeper`, `ghost:charged_creeper`, `wolf_vision:charged_creeper`, `blaze_aura:charged_creeper` |
| `particles` | `Swords_R/particles/examples/example_bounce.json` | `minecraft:example_bounce` |
| `particles` | `Swords_R/particles/examples/example_directional_sphere.json` | `minecraft:example_directional_sphere` |
| `particles` | `Swords_R/particles/examples/example_directional_sphere_2.json` | `minecraft:example_directional_sphere_2` |
| `particles` | `Swords_R/particles/examples/example_flipbook.json` | `minecraft:example_flipbook` |
| `particles` | `Swords_R/particles/examples/example_linearcurve.json` | `minecraft:example_linearcurve` |
| `particles` | `Swords_R/particles/examples/ghost_spiral.json` | `minecraft:ghost_spiral` |
| `particles` | `Swords_R/particles/nether_star_hit.json` | `minecraft:nether_star_hit` |
| `render_controllers` | `Swords_R/render_controllers/blaze_aura.render_controllers.json` | `controller.render.blaze_aura` |
| `render_controllers` | `Swords_R/render_controllers/blaze_rods.render_controllers.json` | `controller.render.blaze_rods` |
| `render_controllers` | `Swords_R/render_controllers/default.render_controllers.json` | `controller.render.default` |
| `render_controllers` | `Swords_R/render_controllers/enderman.render_controllers.json` | `controller.render.enderman` |
| `render_controllers` | `Swords_R/render_controllers/ghost.render_controllers.json` | `controller.render.ghost` |
| `render_controllers` | `Swords_R/render_controllers/grass.render_controllers.json` | `controller.render.grass` |
| `render_controllers` | `Swords_R/render_controllers/mermaid_player.render_controllers.json` | `controller.render.mermaid_player` |
| `render_controllers` | `Swords_R/render_controllers/player_ghost.render_controllers.json` | `controller.render.player_ghost` |
| `render_controllers` | `Swords_R/render_controllers/pumpkin_projectile.render_controllers.json` | `controller.render.pumpkin_projectile` |
| `render_controllers` | `Swords_R/render_controllers/shulker_shield.render_controllers.json` | `controller.render.shulker_shield` |
| `render_controllers` | `Swords_R/render_controllers/ultra_instinct_aura.render_controllers.json` | `controller.render.ultra_instinct_aura` |
| `render_controllers` | `Swords_R/render_controllers/ultra_instinct_projectile.render_controllers.json` | `controller.render.ultra_instinct_projectile` |
| `render_controllers` | `Swords_R/render_controllers/witch.render_controllers.json` | `controller.render.witch`, `controller.render.witch.v1.0` |
| `render_controllers` | `Swords_R/render_controllers/wolf_transformation.render_controllers.json` | `controller.render.wolf_transformation` |
| `render_controllers` | `Swords_R/render_controllers/wolf_vision.render_controllers.json` | `controller.render.wolf_vision` |

## Полные файлы

### `Swords_R/animation_controllers/baby_slime.animation_controllers.json`

- SHA-256 исходного файла: `410b806138f3f3bcbcb2f53e955c430bab5c22eb13ec82ab2fb80566f8342992`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.baby_slime.move": {
      "initial_state": "is_jump",
      "states": {
        "is_jump": {
          "animations": [
            "is_jump"
          ],
          "transitions": [
            {
              "not_jump": "!q.is_baby"
            }
          ]
        },
        "not_jump": {
          "animations": [
            "not_jump"
          ],
          "transitions": [
            {
              "is_jump": "q.is_baby"
            }
          ]
        }
      }
    }
  }
}
```

### `Swords_R/animation_controllers/ghost.animation_controllers.json`

- SHA-256 исходного файла: `76bcb560dd4c1deca4c82be7d82831275457c0397e2f1fa6facf9405016b6afe`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.ghost.move": {
      "initial_state": "default",
      "states": {
        "default": {
          "animations": [
            "move",
            "look_at_target"
          ]
        }
      }
    }
  }
}
```

### `Swords_R/animation_controllers/grass.animation_controllers.json`

- SHA-256 исходного файла: `921a672759fac15653073b92cf27ffbe24a9caa72a0d600d5dd05b332b5829d4`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.grass.move": {
      "initial_state": "default",
      "states": {
        "default": {
          "animations": [
            "move"
          ]
        }
      }
    }
  }
}
```

### `Swords_R/animation_controllers/shulker_shield.animation_controllers.json`

- SHA-256 исходного файла: `7b9bbd7305fe30545dfeda7178e82b06fa40ddef7fb0e4a5c72800d24ea728d9`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.shulker_shield.move": {
      "initial_state": "default",
      "states": {
        "default": {
          "animations": [
            "move"
          ]
        }
      }
    }
  }
}
```

### `Swords_R/animation_controllers/ultra_instinct_projectile.animation_controllers.json`

- SHA-256 исходного файла: `b351006f50b8ee5d8cc37f160b58a42c95aa1993f9bae7ce921acc3581dbf7e0`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.ultra_instinct_projectile.move": {
      "initial_state": "default",
      "states": {
        "default": {
          "animations": [
            "move"
          ]
        }
      }
    }
  }
}
```

### `Swords_R/materials/entity.material`

- SHA-256 исходного файла: `a55ae77cbeec468298cc37688d3c73a3881aa9fa9fc69c235306a4ac33479e4c`.

```json
{
  "materials": {
    "version": "1.0.0",
    "grass:entity_alphatest": {},
    "shulker_shield:entity_alphatest": {},
    "ultra_instinct_projectile:charged_creeper": {},
    "ultra_instinct_aura:charged_creeper": {},
    "player_ghost:charged_creeper": {},
    "ghost:charged_creeper": {},
    "wolf_vision:charged_creeper": {
      "+states": [
        "DisableDepthWrite",
        "DisableAlphaWrite"
      ]
    },
    "blaze_aura:charged_creeper": {}
  }
}
```

### `Swords_R/particles/examples/example_bounce.json`

- SHA-256 исходного файла: `fe7bf18d4c506de7f3078fbeb75d3b97b23a2c03cc0ba8129518264a93d14516`.

```json
{
  "format_version": "1.10.0",
  "particle_effect": {
    "description": {
      "identifier": "minecraft:example_bounce",
      "basic_render_parameters": {
        "material": "particles_alpha",
        "texture": "textures/particle/particles"
      }
    },
    "components": {
      "minecraft:emitter_rate_instant": {
        "num_particles": 100
      },
      "minecraft:emitter_lifetime_once": {
        "active_time": 2
      },
      "minecraft:emitter_shape_sphere": {
        "offset": [
          "Math.random(-0.5, 0.5)",
          "Math.random(-0.5, 0.5)",
          "Math.random(-0.5, 0.5)"
        ],
        "direction": "outwards",
        "radius": 1
      },
      "minecraft:particle_initial_speed": 5.0,
      "minecraft:particle_initial_spin": {
        "rotation": "Math.random(0, 360)",
        "rotation_rate": 0
      },
      "minecraft:particle_lifetime_expression": {
        "max_lifetime": "5"
      },
      "minecraft:particle_motion_dynamic": {
        "linear_acceleration": [
          0,
          -9.8,
          0
        ]
      },
      "minecraft:particle_motion_collision": {
        "coefficient_of_restitution": 0.5,
        "collision_drag": 4,
        "collision_radius": 0.1
      },
      "minecraft:particle_appearance_billboard": {
        "size": [
          "0.1",
          "0.1"
        ],
        "facing_camera_mode": "lookat_xyz",
        "uv": {
          "texture_width": 128,
          "texture_height": 128,
          "uv": [
            0,
            16
          ],
          "uv_size": [
            8,
            8
          ]
        }
      },
      "minecraft:particle_appearance_lighting": {}
    }
  }
}
```

### `Swords_R/particles/examples/example_directional_sphere.json`

- SHA-256 исходного файла: `9171f253cd76356cdef65c817807ba452e3fb6fc2719a95ee432522ec148bd99`.

```json
{
  "format_version": "1.10.0",
  "particle_effect": {
    "description": {
      "identifier": "minecraft:example_directional_sphere",
      "basic_render_parameters": {
        "material": "particles_alpha",
        "texture": "textures/ui/RTX_Sparkle"
      }
    },
    "components": {
      "minecraft:emitter_rate_instant": {
        "num_particles": 5
      },
      "minecraft:emitter_lifetime_once": {
        "active_time": 0
      },
      "minecraft:emitter_shape_sphere": {
        "radius": 0.8,
        "direction": "outwards",
        "surface_only": true
      },
      "minecraft:particle_lifetime_expression": {
        "max_lifetime": 1
      },
      "minecraft:particle_motion_parametric": {
        "rotation": "variable.particle_random_1 * 360 + variable.particle_age * 500"
      },
      "minecraft:particle_appearance_billboard": {
        "size": [
          0.3,
          0.3
        ],
        "facing_camera_mode": "lookat_xyz"
      },
      "minecraft:particle_appearance_lighting": {}
    }
  }
}
```

### `Swords_R/particles/examples/example_directional_sphere_2.json`

- SHA-256 исходного файла: `6a22353392c263e0b4471874382e110c4379c0758f2c0846c13f1c59486f28b0`.

```json
{
  "format_version": "1.10.0",
  "particle_effect": {
    "description": {
      "identifier": "minecraft:example_directional_sphere_2",
      "basic_render_parameters": {
        "material": "particles_alpha",
        "texture": "textures/entity/particles"
      }
    },
    "components": {
      "minecraft:emitter_rate_instant": {
        "num_particles": 5
      },
      "minecraft:emitter_lifetime_once": {
        "active_time": 0
      },
      "minecraft:emitter_shape_sphere": {
        "radius": 1,
        "direction": "outwards",
        "surface_only": true
      },
      "minecraft:particle_lifetime_expression": {
        "max_lifetime": 1
      },
      "minecraft:particle_motion_parametric": {
        "rotation": "variable.particle_random_1 * 360 + variable.particle_age * 500"
      },
      "minecraft:particle_appearance_billboard": {
        "size": [
          0.3,
          0.3
        ],
        "facing_camera_mode": "lookat_xyz"
      },
      "minecraft:particle_appearance_lighting": {}
    }
  }
}
```

### `Swords_R/particles/examples/example_flipbook.json`

- SHA-256 исходного файла: `c082f13ccbd6ef16f1ccdd3631f1be3afedb6c309ca953593bfe19ed0fb9b94d`.

```json
{
  "format_version": "1.10.0",
  "particle_effect": {
    "description": {
      "identifier": "minecraft:example_flipbook",
      "basic_render_parameters": {
        "material": "particles_alpha",
        "texture": "textures/particle/particles"
      }
    },
    "components": {
      "minecraft:emitter_rate_instant": {
        "num_particles": 100
      },
      "minecraft:emitter_lifetime_once": {
        "active_time": 0
      },
      "minecraft:emitter_shape_sphere": {
        "radius": 0.1,
        "direction": "outwards"
      },
      "minecraft:particle_initial_speed": "Math.random(0.0, 15.0)",
      "minecraft:particle_lifetime_expression": {
        "max_lifetime": "Math.random(1.0, 4.0)"
      },
      "minecraft:particle_motion_dynamic": {
        "linear_acceleration": [
          0,
          2.0,
          0
        ],
        "linear_drag_coefficient": 5
      },
      "minecraft:particle_appearance_billboard": {
        "size": [
          "0.1",
          "0.1"
        ],
        "facing_camera_mode": "lookat_xyz",
        "uv": {
          "texture_width": 16,
          "texture_height": 16,
          "flipbook": {
            "base_UV": [
              7,
              "8 + math.floor(variable.particle_random_1 * 5.999)"
            ],
            "size_UV": [
              1,
              1
            ],
            "step_UV": [
              -1,
              0
            ],
            "frames_per_second": 8,
            "max_frame": "8 - math.floor(variable.particle_random_2*4)",
            "stretch_to_lifetime": true,
            "loop": false
          }
        }
      },
      "minecraft:particle_appearance_tinting": {
        "color": [
          1,
          1,
          1,
          1
        ]
      },
      "minecraft:particle_appearance_lighting": {}
    }
  }
}
```

### `Swords_R/particles/examples/example_linearcurve.json`

- SHA-256 исходного файла: `0e8779b63de7280bf1e0de933f1126082c17ceab09a4b92f8540e735d5f6719f`.

```json
{
  "format_version": "1.10.0",
  "particle_effect": {
    "description": {
      "identifier": "minecraft:example_linearcurve",
      "basic_render_parameters": {
        "material": "particles_alpha",
        "texture": "textures/particle/particles"
      }
    },
    "curves": {
      "variable.rotation_acceleration": {
        "type": "linear",
        "nodes": [
          1000.0,
          -2000.0,
          4000.0,
          -8000.0,
          16000.0,
          -32000.0
        ],
        "input": "variable.particle_age",
        "horizontal_range": "variable.particle_lifetime"
      }
    },
    "components": {
      "minecraft:emitter_rate_instant": {
        "num_particles": 100
      },
      "minecraft:emitter_lifetime_once": {
        "active_time": 0
      },
      "minecraft:emitter_shape_sphere": {
        "radius": 0.1,
        "direction": "outwards"
      },
      "minecraft:particle_initial_speed": "Math.random(0.0, 15.0)",
      "minecraft:particle_initial_spin": {
        "rotation": "Math.random(0, 360)"
      },
      "minecraft:particle_lifetime_expression": {
        "max_lifetime": "math.random(1.0, 3.0)"
      },
      "minecraft:particle_motion_dynamic": {
        "linear_acceleration": [
          0,
          2.0,
          0
        ],
        "linear_drag_coefficient": 5,
        "rotation_acceleration": "variable.rotation_acceleration"
      },
      "minecraft:particle_appearance_billboard": {
        "size": [
          0.2,
          0.2
        ],
        "facing_camera_mode": "lookat_xyz",
        "uv": {
          "texture_width": 128,
          "texture_height": 128,
          "flipbook": {
            "base_UV": [
              56,
              0
            ],
            "size_UV": [
              8,
              8
            ],
            "step_UV": [
              -8,
              0
            ],
            "frames_per_second": 8,
            "max_frame": 8,
            "stretch_to_lifetime": true,
            "loop": false
          }
        }
      },
      "minecraft:particle_appearance_tinting": {
        "color": [
          "variable.particle_random_1*0.5",
          "variable.particle_random_1*0.5",
          "variable.particle_random_1*0.5",
          1.0
        ]
      },
      "minecraft:particle_appearance_lighting": {}
    }
  }
}
```

### `Swords_R/particles/examples/ghost_spiral.json`

- SHA-256 исходного файла: `6e4dbb039dccb23c53f8c7c0ab2224ca61399c297f6e45aa3357c15e3f39bf89`.

```json
{
  "format_version": "1.10.0",
  "particle_effect": {
    "description": {
      "identifier": "minecraft:ghost_spiral",
      "basic_render_parameters": {
        "material": "particles_alpha",
        "texture": "textures/particles"
      }
    },
    "components": {
      "minecraft:emitter_rate_steady": {
        "spawn_rate": "Math.random(100, 100)",
        "max_particles": 500
      },
      "minecraft:emitter_lifetime_once": {
        "active_time": 1
      },
      "minecraft:emitter_shape_point": {},
      "minecraft:particle_lifetime_expression": {
        "max_lifetime": "Math.random(1.0, 6.0)"
      },
      "minecraft:particle_motion_parametric": {
        "relative_position": [
          "Math.cos((variable.particle_age * 360) + (variable.particle_random_1 * 360))",
          "variable.particle_age*3",
          "Math.sin((variable.particle_age * 360) + (variable.particle_random_1 * 360))"
        ]
      },
      "minecraft:particle_appearance_billboard": {
        "size": [
          0.1,
          0.1
        ],
        "facing_camera_mode": "lookat_xyz",
        "uv": {
          "texture_width": 128,
          "texture_height": 128,
          "flipbook": {
            "base_UV": [
              0,
              80
            ],
            "size_UV": [
              8,
              8
            ],
            "step_UV": [
              8,
              0
            ],
            "frames_per_second": 1,
            "max_frame": 16,
            "stretch_to_lifetime": true,
            "loop": false
          }
        }
      }
    }
  }
}
```

### `Swords_R/particles/nether_star_hit.json`

- SHA-256 исходного файла: `cea98a3a0700492d7ab320d042a9fed43c02cf75c86a5d3db5781a3b907a34fe`.

```json
{
  "format_version": "1.10.0",
  "particle_effect": {
    "description": {
      "identifier": "minecraft:nether_star_hit",
      "basic_render_parameters": {
        "material": "particles_alpha",
        "texture": "textures/particle/particles"
      }
    },
    "components": {
      "minecraft:emitter_rate_steady": {
        "spawn_rate": 520,
        "max_particles": 12
      },
      "minecraft:emitter_lifetime_once": {
        "active_time": 0.15
      },
      "minecraft:emitter_shape_point": {
        "offset": [
          0.0,
          "Math.random(-0.9, -0.5)",
          0.0
        ],
        "direction": [
          "Math.random(-0.75, 0.75)",
          "Math.random(-1.0, 1.0)",
          "Math.random(-0.75, 0.75)"
        ]
      },
      "minecraft:particle_initial_speed": "Math.random(10.0, 20.0)",
      "minecraft:particle_lifetime_expression": {
        "max_lifetime": "6.0 / (Math.random(0.0, 16.0) + 12.0)"
      },
      "minecraft:particle_motion_dynamic": {
        "linear_acceleration": [
          0,
          -6.0,
          0
        ],
        "linear_drag_coefficient": 10
      },
      "minecraft:particle_appearance_billboard": {
        "size": [
          "0.10 + variable.particle_random_1*0.05",
          "0.10 + variable.particle_random_1*0.05"
        ],
        "facing_camera_mode": "lookat_xyz",
        "uv": {
          "texture_width": 128,
          "texture_height": 128,
          "flipbook": {
            "base_UV": [
              0,
              72
            ],
            "size_UV": [
              8,
              8
            ],
            "step_UV": [
              8,
              0
            ],
            "frames_per_second": 8,
            "max_frame": 8,
            "stretch_to_lifetime": true,
            "loop": false
          }
        }
      },
      "minecraft:particle_appearance_tinting": {
        "color": {
          "gradient": [
            [
              "variable.particle_random_1*0.3 + 0.6",
              "variable.particle_random_2*0.3+ 0.6",
              "variable.particle_random_2*0.3+ 0.6",
              1.0
            ],
            [
              "variable.particle_random_1*0.3 + 0.6",
              0.5,
              0.3,
              1.0
            ]
          ],
          "interpolant": "variable.particle_age/variable.particle_lifetime"
        }
      },
      "minecraft:particle_appearance_lighting": {}
    }
  }
}
```

### `Swords_R/render_controllers/blaze_aura.render_controllers.json`

- SHA-256 исходного файла: `90e48feb1ca0bc1905e1556b709602f5af0520d2bf1b7a628ee5a1200b48ac34`.

```json
{
  "format_version": "1.8.0",
  "render_controllers": {
    "controller.render.blaze_aura": {
      "textures": [
        "Texture.blaze_rods"
      ],
      "geometry": "Geometry.blaze_aura",
      "materials": [
        {
          "*": "Material.blaze_aura"
        }
      ],
      "overlay_color": {
        "r": 1.0,
        "g": 1.0,
        "b": 1.0,
        "a": 1.0
      },
      "light_color_multiplier": 0.4,
      "filter_lighting": true,
      "ignore_lighting": true
    }
  }
}
```

### `Swords_R/render_controllers/blaze_rods.render_controllers.json`

- SHA-256 исходного файла: `165e89a6608f2030fe27c7f8dc3b05d91b377b72b2bee88c0a877d535cc401ef`.

```json
{
  "format_version": "1.8.0",
  "render_controllers": {
    "controller.render.blaze_rods": {
      "geometry": "Geometry.blaze_rods",
      "materials": [
        {
          "*": "Material.default"
        }
      ],
      "textures": [
        "Texture.blaze_rods"
      ]
    }
  }
}
```

### `Swords_R/render_controllers/default.render_controllers.json`

- SHA-256 исходного файла: `61f489b438ab7ed930ccf433247fd86114b1350e04a366641e2fef78a6e1c2ca`.

```json
{
  "format_version": "1.8.0",
  "render_controllers": {
    "controller.render.default": {
      "geometry": "Geometry.default",
      "materials": [
        {
          "*": "Material.default"
        }
      ],
      "textures": [
        "Texture.default"
      ]
    }
  }
}
```

### `Swords_R/render_controllers/enderman.render_controllers.json`

- SHA-256 исходного файла: `375d940ffc9380df499b05c8f265d90d24ea96ed5b174aa31d39254c59d3a0c9`.

```json
{
  "format_version": "1.8.0",
  "render_controllers": {
    "controller.render.enderman": {
      "arrays": {
        "materials": {
          "Array.materials": [
            "Material.default",
            "Material.invisible"
          ]
        },
        "textures": {
          "Array.textures": [
            "Texture.default",
            "Texture.red_enderman"
          ]
        }
      },
      "geometry": "Geometry.default",
      "materials": [
        {
          "*": "Array.materials[query.is_invisible]"
        }
      ],
      "textures": [
        "Array.textures[query.variant]"
      ]
    }
  }
}
```

### `Swords_R/render_controllers/ghost.render_controllers.json`

- SHA-256 исходного файла: `ff2afb889a7b0cb49c130032776043724c0a9eb6a2e216ce5f9f2bf640066d3f`.

```json
{
  "format_version": "1.8.0",
  "render_controllers": {
    "controller.render.ghost": {
      "textures": [
        "Texture.ghost"
      ],
      "geometry": "Geometry.ghost",
      "materials": [
        {
          "*": "Material.ghost"
        }
      ],
      "overlay_color": {
        "r": 1.0,
        "g": 1.0,
        "b": 1.0,
        "a": 1.0
      },
      "light_color_multiplier": 0.2,
      "filter_lighting": true,
      "ignore_lighting": true
    }
  }
}
```

### `Swords_R/render_controllers/grass.render_controllers.json`

- SHA-256 исходного файла: `d716827edfdb8e2ff751b2a4e2a06e186d39f6bba1cf94a901de9e92ff9f78ff`.

```json
{
  "format_version": "1.8.0",
  "render_controllers": {
    "controller.render.grass": {
      "geometry": "Geometry.default",
      "materials": [
        {
          "*": "Material.default"
        }
      ],
      "textures": [
        "Texture.default"
      ]
    }
  }
}
```

### `Swords_R/render_controllers/mermaid_player.render_controllers.json`

- SHA-256 исходного файла: `01deeafbfaffed1f177461b17742b91b9c08cdc6964f8a8a1fca09f9e3f21441`.

```json
{
  "format_version": "1.8.0",
  "render_controllers": {
    "controller.render.mermaid_player": {
      "geometry": "Geometry.mermaid_player",
      "materials": [
        {
          "*": "Material.default"
        }
      ],
      "textures": [
        "Texture.mermaid_player"
      ]
    }
  }
}
```

### `Swords_R/render_controllers/player_ghost.render_controllers.json`

- SHA-256 исходного файла: `8aa60aa9fd452e1f28fe879d841d221f5b927097491cba71e4a6aabbe76c1d50`.

```json
{
  "format_version": "1.8.0",
  "render_controllers": {
    "controller.render.player_ghost": {
      "textures": [
        "Texture.ghost"
      ],
      "geometry": "Geometry.player_ghost",
      "materials": [
        {
          "*": "Material.player_ghost"
        }
      ],
      "overlay_color": {
        "r": 1.0,
        "g": 1.0,
        "b": 1.0,
        "a": 1.0
      },
      "light_color_multiplier": 0.2,
      "filter_lighting": true,
      "ignore_lighting": true
    }
  }
}
```

### `Swords_R/render_controllers/pumpkin_projectile.render_controllers.json`

- SHA-256 исходного файла: `1e0d2245ed096e5efef4934950e18597e2293143b8d8a77732d794d194075559`.

```json
{
  "format_version": "1.10.0",
  "render_controllers": {
    "controller.render.pumpkin_projectile": {
      "geometry": "Geometry.default",
      "materials": [
        {
          "*": "Material.default"
        }
      ],
      "textures": [
        "Texture.default"
      ],
      "overlay_color": {
        "r": "1",
        "g": "(Math.sin(q.life_time * 500.0) + 1.0) * 0.5",
        "b": "0",
        "a": "0.5"
      },
      "light_color_multiplier": 0.5,
      "ignore_lighting": true,
      "filter_lighting": true
    }
  }
}
```

### `Swords_R/render_controllers/shulker_shield.render_controllers.json`

- SHA-256 исходного файла: `d9e2f9721f0a1b582f403eeb3e6442af9ccf446218eae132d70641dd13d07b3e`.

```json
{
  "format_version": "1.8.0",
  "render_controllers": {
    "controller.render.shulker_shield": {
      "geometry": "Geometry.default",
      "materials": [
        {
          "*": "Material.default"
        }
      ],
      "textures": [
        "Texture.default"
      ]
    }
  }
}
```

### `Swords_R/render_controllers/ultra_instinct_aura.render_controllers.json`

- SHA-256 исходного файла: `dcf9952d51faad5709ab1f7e992fa2fb2fd378189cd0cc7010a7484a12d5d65f`.

```json
{
  "format_version": "1.8.0",
  "render_controllers": {
    "controller.render.ultra_instinct_aura": {
      "textures": [
        "Texture.ultra_instinct_aura"
      ],
      "geometry": "Geometry.ultra_instinct_aura",
      "materials": [
        {
          "*": "Material.ultra_instinct_aura"
        }
      ],
      "overlay_color": {
        "r": 1.0,
        "g": 1.0,
        "b": 1.0,
        "a": 1.0
      },
      "light_color_multiplier": 0.2,
      "filter_lighting": true,
      "ignore_lighting": true
    }
  }
}
```

### `Swords_R/render_controllers/ultra_instinct_projectile.render_controllers.json`

- SHA-256 исходного файла: `2e8b0c601e0c76babc9f2b7cfbccddee5b849d06fd2be0167e34e4c3a0737f19`.

```json
{
  "format_version": "1.8.0",
  "render_controllers": {
    "controller.render.ultra_instinct_projectile": {
      "geometry": "Geometry.default",
      "materials": [
        {
          "*": "Material.default"
        }
      ],
      "textures": [
        "Texture.default"
      ],
      "filter_lighting": true
    }
  }
}
```

### `Swords_R/render_controllers/witch.render_controllers.json`

- SHA-256 исходного файла: `ea636495e315816b4f1f7f756f004491c7051b99bc3ffa163feacf32bba92bfe`.

```json
{
  "format_version": "1.8.0",
  "render_controllers": {
    "controller.render.witch": {
      "geometry": "Geometry.default",
      "materials": [
        {
          "*": "Material.default"
        }
      ],
      "arrays": {
        "textures": {
          "Array.variants": [
            "Texture.default",
            "Texture.grass_witch"
          ]
        }
      },
      "textures": [
        "Array.variants[query.variant]"
      ]
    },
    "controller.render.witch.v1.0": {
      "geometry": "Geometry.default",
      "materials": [
        {
          "*": "Material.default"
        }
      ],
      "part_visibility": [
        {
          "*": false,
          "head": true,
          "nose": true,
          "body": true,
          "arms": true,
          "leg0": true,
          "leg1": true,
          "hat": true,
          "hat2": true,
          "hat3": true,
          "hat4": true
        }
      ],
      "arrays": {
        "textures": {
          "Array.variants": [
            "Texture.default",
            "Texture.grass_witch"
          ]
        }
      },
      "textures": [
        "Array.variants[query.variant]"
      ]
    }
  }
}
```

### `Swords_R/render_controllers/wolf_transformation.render_controllers.json`

- SHA-256 исходного файла: `af424e0c4cd4e26a911cfeea379dc405cabf7e36d56831566be7b3ce409344e3`.

```json
{
  "format_version": "1.8.0",
  "render_controllers": {
    "controller.render.wolf_transformation": {
      "geometry": "Geometry.wolf_transformation",
      "materials": [
        {
          "*": "Material.default"
        }
      ],
      "textures": [
        "Texture.wolf_transformation"
      ]
    }
  }
}
```

### `Swords_R/render_controllers/wolf_vision.render_controllers.json`

- SHA-256 исходного файла: `919c5a71b63703dd9a85a22929a9c83f6e0004f73d401f31b47c398b9145722c`.

```json
{
  "format_version": "1.8.0",
  "render_controllers": {
    "controller.render.wolf_vision": {
      "textures": [
        "Texture.wolf_vision"
      ],
      "geometry": "Geometry.wolf_vision",
      "materials": [
        {
          "*": "Material.wolf_vision"
        }
      ],
      "overlay_color": {
        "r": 1.0,
        "g": 1.0,
        "b": 1.0,
        "a": 1.0
      },
      "light_color_multiplier": 0.2,
      "filter_lighting": true,
      "ignore_lighting": true
    }
  }
}
```

Связи client entity, местные/ванильные определения — [граф ресурсов](resource-graph-2.8.14.md). Сами модели — [реестр геометрии](client-geometry-index.md); keyframes — [реестр анимаций](client-animation-index.md); аудио и изображения — [реестр ассетов](assets-2.8.14.md).
