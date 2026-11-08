# Клиентские анимации: определения и прямые aliases

В `Sword_R/animations/` 1.6 не обнаружено локальных JSON-анимаций; это не означает отсутствия ванильной анимации или ресурсов за пределами этого пути. В 2.x найдено **18** определений в **9** JSON-файлах. Сравнение исходных SHA-256 файлов анимаций и структурное сравнение извлечённых aliases показывает совпадение двух архивов 2.x; остальной resource pack может отличаться.

Таблица сохраняет буквальные `loop`, `animation_length`, `override_previous_animation` и список bones; `—` означает отсутствие поля, не false и не ноль. Имена references ищутся только в `description.animations` разобранных client entity JSON и обозначают объявленный alias, а не установленное применение. Отсутствие alias **не** означает неиспользуемость: например, `animation.player.explode` прямо назван в `playanimation` у Creeper Sword. Контроллеры, `scripts.animate`, команды и Molang не интерпретируются.

Ниже каждый animation-объект приведён целиком, в том числе все временные ключи, значения, Molang-выражения, пустые объекты и порядок списков; JSON5-комментарии и форматирование не сохраняются. Если ключи повторяются, JSON5 оставляет последнее значение; исходный архив остаётся эталоном. Время/единицы и поведение interpolation не выводятся из этого индекса.

- Ошибки разбора: нет.
- Повторные ключи: нет.

| Animation ID | loop | animation_length | override_previous_animation | bones | Локальные client aliases |
|---|---|---|---|---|---|
| [`animation.baby_slime.wing`](#animationbaby_slimewing) | `true` | — | — | не задано | не найдено в client entity |
| [`animation.baby_slime.normal_speed_wing`](#animationbaby_slimenormal_speed_wing) | `true` | `0.79167` | — | `wings`, `wings2` | `Swords_R/entity/mountable_slime.v1.0.json` · `entity:mountable_slime` · `not_jump` |
| [`animation.baby_slime.speed_wing`](#animationbaby_slimespeed_wing) | `true` | `0.45833` | — | `wings`, `wings2` | `Swords_R/entity/mountable_slime.v1.0.json` · `entity:mountable_slime` · `is_jump` |
| [`animation.blaze_rods`](#animationblaze_rods) | `true` | — | — | `upperbodyparts0`, `upperbodyparts1`, `upperbodyparts10`, `upperbodyparts11`, `upperbodyparts2`, `upperbodyparts3`, `upperbodyparts4`, `upperbodyparts5`, `upperbodyparts6`, `upperbodyparts7`, `upperbodyparts8`, `upperbodyparts9` | `Swords_R/entity/player.entity.json` · `minecraft:player` · `blaze_rods.move` |
| [`animation.ghost.move`](#animationghostmove) | `true` | `2.0833` | — | `body`, `ghost_tail`, `leftArm`, `rightArm` | `Swords_R/entity/ghost.v1.0.json` · `entity:ghost` · `move` |
| [`animation.ghost.look_at_target`](#animationghostlook_at_target) | `true` | — | — | `ghost_head` | `Swords_R/entity/ghost.v1.0.json` · `entity:ghost` · `look_at_target` |
| [`animation.grass.attack`](#animationgrassattack) | — | `2` | — | `bone`, `bone2`, `bone3`, `bone4`, `bone5` | `Swords_R/entity/grass.v1.0.json` · `entity:grass` · `move` |
| [`animation.mermaid_player.tail`](#animationmermaid_playertail) | `true` | `0.01` | `true` | `rightLeg`, `leftLeg` | `Swords_R/entity/player.entity.json` · `minecraft:player` · `mermaid_player.tail` |
| [`animation.mermaid_player.swimming`](#animationmermaid_playerswimming) | `true` | `4` | — | `Mermaidtail`, `Mermaidtail4`, `Mermaidtail5`, `Mermaidtail6`, `Mermaidtail7` | `Swords_R/entity/player.entity.json` · `minecraft:player` · `mermaid_player.swimming` |
| [`animation.mermaid_player.drowning`](#animationmermaid_playerdrowning) | `true` | `2` | — | `root`, `Mermaidtail`, `Mermaidtail4`, `Mermaidtail5`, `Mermaidtail6` | `Swords_R/entity/player.entity.json` · `minecraft:player` · `mermaid_player.drowning` |
| [`animation.mermaid_player.default_pose`](#animationmermaid_playerdefault_pose) | `true` | `4` | — | `root`, `Mermaidtail`, `Mermaidtail4`, `Mermaidtail5`, `Mermaidtail6` | `Swords_R/entity/player.entity.json` · `minecraft:player` · `mermaid_player.default_pose` |
| [`animation.player.explode`](#animationplayerexplode) | — | `1.52` | — | `body`, `head`, `leftArm`, `rightArm`, `rightItem`, `leftLeg`, `rightLeg` | не найдено в client entity |
| [`animation.ultra_instinct_sword.attack`](#animationultra_instinct_swordattack) | `true` | `0.32` | `true` | `rightArm` | `Swords_R/entity/player.entity.json` · `minecraft:player` · `attack.ultra_instinct_sword` |
| [`animation.player_ghost.move`](#animationplayer_ghostmove) | `true` | `2.0833` | — | `root`, `rightItem`, `leftLeg`, `rightLeg`, `ghost_cola`, `leftArm`, `rightArm` | `Swords_R/entity/player.entity.json` · `minecraft:player` · `move.player_ghost` |
| [`animation.player_ghost.vision`](#animationplayer_ghostvision) | `true` | `0.01667` | — | `ghost_hat`, `leftArm`, `jacket` | `Swords_R/entity/player.entity.json` · `minecraft:player` · `vision.player_ghost` |
| [`animation.shulker_shield.closed`](#animationshulker_shieldclosed) | `true` | `10000` | — | `lid` | `Swords_R/entity/shulker_shield.v1.0.json` · `entity:shulker_shield` · `move` |
| [`animation.ultra_instinct.move`](#animationultra_instinctmove) | `true` | `4` | — | `root`, `rightLeg`, `leftLeg` | `Swords_R/entity/player.entity.json` · `minecraft:player` · `ultra_instinct.move` |
| [`animation.move`](#animationmove) | `true` | `3.08` | — | `bone` | `Swords_R/entity/ultra_instinct_projectile.json` · `entity:ultra_instinct_projectile` · `move` |

## Полные объекты анимаций

### `animation.baby_slime.wing`

- `Swords_R/animations/baby_slime.animation.json`; исходный SHA-256 `2ff25c4c3e1cc11e634da947eea87aaf9f3f535570030f70497537e83f006084`; format_version `1.8.0`.

```json
{
  "loop": true
}
```

### `animation.baby_slime.normal_speed_wing`

- `Swords_R/animations/baby_slime.animation.json`; исходный SHA-256 `2ff25c4c3e1cc11e634da947eea87aaf9f3f535570030f70497537e83f006084`; format_version `1.8.0`.

```json
{
  "loop": true,
  "animation_length": 0.79167,
  "bones": {
    "wings": {
      "rotation": {
        "0.0": [
          0,
          0,
          0
        ],
        "0.1667": [
          0,
          0,
          -22.5
        ],
        "0.375": [
          0,
          0,
          22.5
        ],
        "0.5417": [
          0,
          0,
          55
        ],
        "0.75": [
          0,
          0,
          12.5
        ]
      },
      "position": [
        0,
        0,
        0
      ]
    },
    "wings2": {
      "rotation": {
        "0.0": [
          0,
          0,
          0
        ],
        "0.1667": [
          0,
          0,
          12.5
        ],
        "0.3333": [
          0,
          0,
          -22.5
        ],
        "0.5417": [
          0,
          0,
          -50
        ],
        "0.75": [
          0,
          0,
          -17.5
        ]
      },
      "position": [
        0,
        0,
        0
      ]
    }
  }
}
```

### `animation.baby_slime.speed_wing`

- `Swords_R/animations/baby_slime.animation.json`; исходный SHA-256 `2ff25c4c3e1cc11e634da947eea87aaf9f3f535570030f70497537e83f006084`; format_version `1.8.0`.

```json
{
  "loop": true,
  "animation_length": 0.45833,
  "bones": {
    "wings": {
      "rotation": {
        "0.0": [
          0,
          0,
          0
        ],
        "0.125": [
          2.5,
          0,
          -92.5
        ],
        "0.2917": [
          2.5,
          0,
          110
        ],
        "0.4583": [
          0,
          0,
          0
        ]
      },
      "position": [
        0,
        0,
        0
      ]
    },
    "wings2": {
      "rotation": {
        "0.0": [
          0,
          0,
          0
        ],
        "0.125": [
          0,
          0,
          97.5
        ],
        "0.2917": [
          0,
          0,
          -92.5
        ],
        "0.4583": [
          0,
          0,
          0
        ]
      },
      "position": [
        0,
        0,
        0
      ]
    }
  }
}
```

### `animation.blaze_rods`

- `Swords_R/animations/blaze_rods.animation.json`; исходный SHA-256 `25e5e97e44e19bfcaaf3666639f46aa8cbb26fce46ee20e277311f560c35b728`; format_version `1.8.0`.

```json
{
  "loop": true,
  "bones": {
    "upperbodyparts0": {
      "position": [
        "math.cos(query.life_time * -360.0        ) * 9.0",
        "2.0 + math.cos((0 * 2 + query.life_time * 20.0) * 14.32)",
        "math.sin(query.life_time * -360.0        ) * 9.0"
      ]
    },
    "upperbodyparts1": {
      "position": [
        "math.cos(query.life_time * -360.0 +  90.0) * 9.0",
        "2.0 + math.cos((1 * 2 + query.life_time * 20.0) * 14.32)",
        "math.sin(query.life_time * -360.0 +  90.0) * 9.0"
      ]
    },
    "upperbodyparts10": {
      "position": [
        "math.cos(query.life_time * -180.0 + 207.0) * 5.0",
        "-11.0 + math.cos((10 * 1.5 + query.life_time * 20.0) * 14.32)",
        "math.sin(query.life_time * -180.0 + 207.0) * 5.0"
      ]
    },
    "upperbodyparts11": {
      "position": [
        "math.cos(query.life_time * -180.0 + 297.0) * 5.0",
        "-11.0 + math.cos((11 * 1.5 + query.life_time * 20.0) * 14.32)",
        "math.sin(query.life_time * -180.0 + 297.0) * 5.0"
      ]
    },
    "upperbodyparts2": {
      "position": [
        "math.cos(query.life_time * -360.0 + 180.0) * 9.0",
        "2.0 + math.cos((2 * 2 + query.life_time * 20.0) * 14.32)",
        "math.sin(query.life_time * -360.0 + 180.0) * 9.0"
      ]
    },
    "upperbodyparts3": {
      "position": [
        "math.cos(query.life_time * -360.0 + 270.0) * 9.0",
        "2.0 + math.cos((3 * 2 + query.life_time * 20.0) * 14.32)",
        "math.sin(query.life_time * -360.0 + 270.0) * 9.0"
      ]
    },
    "upperbodyparts4": {
      "position": [
        "math.cos(query.life_time * 108.0 +  45.0) * 7.0",
        "-2.0 + math.cos((4 * 2 + query.life_time * 20.0) * 14.32)",
        "math.sin(query.life_time * 108.0 +  45.0) * 7.0"
      ]
    },
    "upperbodyparts5": {
      "position": [
        "math.cos(query.life_time * 108.0 + 135.0) * 7.0",
        "-2.0 + math.cos((5 * 2 + query.life_time * 20.0) * 14.32)",
        "math.sin(query.life_time * 108.0 + 135.0) * 7.0"
      ]
    },
    "upperbodyparts6": {
      "position": [
        "math.cos(query.life_time * 108.0 + 225.0) * 7.0",
        "-2.0 + math.cos((6 * 2 + query.life_time * 20.0) * 14.32)",
        "math.sin(query.life_time * 108.0 + 225.0) * 7.0"
      ]
    },
    "upperbodyparts7": {
      "position": [
        "math.cos(query.life_time * 108.0 + 315.0) * 7.0",
        "-2.0 + math.cos((7 * 2 + query.life_time * 20.0) * 14.32)",
        "math.sin(query.life_time * 108.0 + 315.0) * 7.0"
      ]
    },
    "upperbodyparts8": {
      "position": [
        "math.cos(query.life_time * -180.0 +  27.0) * 5.0",
        "-11.0 + math.cos((8 * 1.5 + query.life_time * 20.0) * 14.32)",
        "math.sin(query.life_time * -180.0 +  27.0) * 5.0"
      ]
    },
    "upperbodyparts9": {
      "position": [
        "math.cos(query.life_time * -180.0 + 117.0) * 5.0",
        "-11.0 + math.cos((9 * 1.5 + query.life_time * 20.0) * 14.32)",
        "math.sin(query.life_time * -180.0 + 117.0) * 5.0"
      ]
    }
  }
}
```

### `animation.ghost.move`

- `Swords_R/animations/ghost.animation.json`; исходный SHA-256 `d7da2dc5210566687929a27b2720938b7b0223d30e62fef45ffb299ad7b32e88`; format_version `1.8.0`.

```json
{
  "loop": true,
  "animation_length": 2.0833,
  "bones": {
    "body": {
      "position": {
        "0.0": [
          0,
          0,
          0
        ],
        "1.0333": [
          0,
          2,
          0
        ],
        "2.0833": [
          0,
          0,
          0
        ]
      }
    },
    "ghost_tail": {
      "rotation": {
        "0.0": [
          0,
          0,
          0
        ],
        "0.7167": [
          5,
          0,
          0
        ],
        "1.4333": [
          10,
          0,
          0
        ],
        "2.0833": [
          0,
          0,
          0
        ]
      },
      "position": {
        "0.0": [
          0,
          0,
          0
        ],
        "1.2": [
          0,
          0.5,
          0
        ],
        "2.0833": [
          0,
          0,
          0
        ]
      }
    },
    "leftArm": {
      "rotation": {
        "0.0": [
          0,
          0,
          0
        ],
        "1.0": [
          0,
          0,
          -5
        ],
        "2.0333": [
          0,
          0,
          0
        ]
      },
      "position": [
        0,
        0,
        0
      ]
    },
    "rightArm": {
      "rotation": {
        "0.0": [
          0,
          0,
          0
        ],
        "0.9667": [
          0,
          0,
          5
        ],
        "2.0833": [
          0,
          0,
          0
        ]
      },
      "position": [
        0,
        0,
        0
      ]
    }
  }
}
```

### `animation.ghost.look_at_target`

- `Swords_R/animations/ghost.animation.json`; исходный SHA-256 `d7da2dc5210566687929a27b2720938b7b0223d30e62fef45ffb299ad7b32e88`; format_version `1.8.0`.

```json
{
  "loop": true,
  "bones": {
    "ghost_head": {
      "rotation": [
        "query.target_x_rotation",
        "query.target_y_rotation",
        0
      ]
    }
  }
}
```

### `animation.grass.attack`

- `Swords_R/animations/grass.animation.json`; исходный SHA-256 `4649a576a7ef5d6191a41a3c736e6182c017ec9d5c0784f7161abfe1ab09a116`; format_version `1.8.0`.

```json
{
  "animation_length": 2,
  "bones": {
    "bone": {
      "rotation": {
        "0.0": [
          0,
          0,
          0
        ],
        "0.9167": [
          -18,
          0,
          18
        ]
      },
      "position": {
        "0.0": [
          0,
          0,
          0
        ],
        "0.5167": [
          0,
          7,
          0
        ],
        "0.7667": [
          0,
          11,
          0
        ],
        "1.0333": [
          0,
          15,
          0
        ],
        "1.2333": [
          0,
          11,
          0
        ],
        "1.6": [
          0,
          0,
          0
        ]
      }
    },
    "bone2": {
      "rotation": {
        "0.0": [
          0,
          0,
          0
        ],
        "0.9167": [
          18,
          0,
          18
        ]
      },
      "position": {
        "0.0": [
          0,
          0,
          0
        ],
        "0.5167": [
          0,
          8,
          0
        ],
        "0.7667": [
          0,
          12,
          0
        ],
        "1.0333": [
          0,
          15,
          0
        ],
        "1.2333": [
          0,
          12,
          0
        ],
        "1.6": [
          0,
          0,
          0
        ]
      }
    },
    "bone3": {
      "rotation": {
        "0.0": [
          0,
          0,
          0
        ],
        "0.9167": [
          18,
          0,
          -18
        ]
      },
      "position": {
        "0.0": [
          0,
          0,
          0
        ],
        "0.5167": [
          0,
          9,
          0
        ],
        "0.7667": [
          0,
          12,
          0
        ],
        "1.0333": [
          0,
          15,
          0
        ],
        "1.2333": [
          0,
          12,
          0
        ],
        "1.6": [
          0,
          0,
          0
        ]
      }
    },
    "bone4": {
      "rotation": {
        "0.0": [
          0,
          0,
          0
        ],
        "0.9167": [
          -18,
          0,
          -18
        ]
      },
      "position": {
        "0.0": [
          0,
          0,
          0
        ],
        "0.5167": [
          0,
          8,
          0
        ],
        "0.7667": [
          0,
          12,
          0
        ],
        "1.0333": [
          0,
          15,
          0
        ],
        "1.2333": [
          0,
          12,
          0
        ],
        "1.6": [
          0,
          0,
          0
        ]
      }
    },
    "bone5": {
      "position": {
        "0.0": [
          0,
          0,
          0
        ],
        "0.2833": [
          0,
          2,
          0
        ],
        "1.0333": [
          0,
          12,
          0
        ],
        "1.6": [
          0,
          -2,
          0
        ]
      }
    }
  }
}
```

### `animation.mermaid_player.tail`

- `Swords_R/animations/mermaid_player.animation.json`; исходный SHA-256 `eb26e0a5bd9d5a94378c18b8c8172cd1adb6d91d054c724b4bb3aebf43ed8ed1`; format_version `1.8.0`.

```json
{
  "loop": true,
  "animation_length": 0.01,
  "override_previous_animation": true,
  "bones": {
    "rightLeg": {
      "rotation": [
        0,
        0,
        0
      ],
      "position": [
        0,
        0,
        0
      ],
      "scale": 0
    },
    "leftLeg": {
      "rotation": [
        0,
        0,
        0
      ],
      "position": [
        0,
        0,
        0
      ],
      "scale": 0
    }
  }
}
```

### `animation.mermaid_player.swimming`

- `Swords_R/animations/mermaid_player.animation.json`; исходный SHA-256 `eb26e0a5bd9d5a94378c18b8c8172cd1adb6d91d054c724b4bb3aebf43ed8ed1`; format_version `1.8.0`.

```json
{
  "loop": true,
  "animation_length": 4,
  "bones": {
    "Mermaidtail": {
      "rotation": {
        "0.0": [
          0,
          0,
          0
        ],
        "1.0": [
          -42.5,
          0,
          0
        ],
        "2.0": [
          0,
          0,
          0
        ],
        "2.6667": [
          -42.5,
          0,
          0
        ],
        "3.6667": [
          0,
          0,
          0
        ],
        "3.8333": [
          6,
          0,
          0
        ],
        "4.0": [
          0,
          0,
          0
        ]
      },
      "position": {
        "0.0": [
          0,
          0,
          0
        ],
        "2.0": [
          0,
          0,
          0
        ],
        "3.6667": [
          0,
          0,
          0
        ],
        "4.0": [
          0,
          0,
          0
        ]
      }
    },
    "Mermaidtail4": {
      "rotation": {
        "0.0": [
          0,
          0,
          0
        ],
        "1.2083": [
          -10,
          0,
          0
        ],
        "2.875": [
          -10,
          0,
          0
        ],
        "4.0": [
          0,
          0,
          0
        ]
      },
      "position": {
        "0.0": [
          0,
          0,
          0
        ],
        "4.0": [
          0,
          0,
          0
        ]
      }
    },
    "Mermaidtail5": {
      "rotation": {
        "0.0": [
          0,
          0,
          0
        ],
        "1.0": [
          -20,
          0,
          0
        ],
        "1.5": [
          -50,
          0,
          0
        ],
        "2.6667": [
          -20,
          0,
          0
        ],
        "3.1667": [
          -50,
          0,
          0
        ],
        "4.0": [
          0,
          0,
          0
        ]
      },
      "position": {
        "0.0": [
          0,
          0,
          0
        ],
        "1.5": [
          0,
          -0.7,
          0.6
        ],
        "3.1667": [
          0,
          -0.7,
          0.6
        ],
        "4.0": [
          0,
          0,
          0
        ]
      }
    },
    "Mermaidtail6": {
      "rotation": {
        "0.0": [
          0,
          0,
          0
        ],
        "1.0": [
          -30,
          0,
          0
        ],
        "1.5": [
          -105,
          0,
          0
        ],
        "2.25": [
          -36.79,
          0,
          0
        ],
        "2.6667": [
          -30,
          0,
          0
        ],
        "3.1667": [
          -105,
          0,
          0
        ],
        "4.0": [
          0,
          0,
          0
        ]
      },
      "position": {
        "0.0": [
          0,
          0,
          0
        ],
        "0.8333": [
          0,
          -0.08,
          0.19
        ],
        "1.0": [
          0,
          -0.33,
          0.85
        ],
        "1.2083": [
          0,
          -0.45,
          1.59
        ],
        "1.5": [
          0,
          -1.5,
          2.3
        ],
        "1.6667": [
          0,
          -1.18,
          2.23
        ],
        "1.8333": [
          0,
          -0.83,
          1.87
        ],
        "2.25": [
          0,
          -0.68,
          0.99
        ],
        "2.6667": [
          0,
          -0.33,
          0.85
        ],
        "2.875": [
          0,
          -0.45,
          1.59
        ],
        "3.1667": [
          0,
          -1.5,
          2.3
        ],
        "3.3333": [
          0,
          -0.56,
          1.98
        ],
        "4.0": [
          0,
          0,
          0
        ]
      }
    },
    "Mermaidtail7": {
      "rotation": {
        "0.0": [
          0,
          0,
          0
        ],
        "0.5": [
          7.5,
          0,
          0
        ],
        "1.0": [
          21.32,
          0,
          0
        ],
        "1.8333": [
          0.4,
          0,
          0
        ],
        "2.8333": [
          23.25,
          0,
          0
        ],
        "4.0": [
          0,
          0,
          0
        ]
      },
      "position": {
        "0.0": [
          0,
          0,
          0
        ],
        "1.0": [
          0,
          -0.3,
          -0.2
        ],
        "4.0": [
          0,
          0,
          0
        ]
      }
    }
  }
}
```

### `animation.mermaid_player.drowning`

- `Swords_R/animations/mermaid_player.animation.json`; исходный SHA-256 `eb26e0a5bd9d5a94378c18b8c8172cd1adb6d91d054c724b4bb3aebf43ed8ed1`; format_version `1.8.0`.

```json
{
  "loop": true,
  "animation_length": 2,
  "bones": {
    "root": {
      "rotation": {
        "0.0": [
          80,
          0,
          0
        ],
        "0.5": [
          80,
          0,
          -90
        ],
        "1.0": [
          80,
          0,
          90
        ],
        "1.5": [
          80,
          0,
          -90
        ],
        "2.0": [
          80,
          0,
          0
        ]
      },
      "position": {
        "0.0": [
          0,
          0,
          10
        ],
        "0.25": [
          0,
          5,
          10
        ],
        "0.5": [
          0,
          0,
          10
        ],
        "0.75": [
          0,
          5,
          10
        ],
        "1.0": [
          0,
          0,
          10
        ],
        "1.25": [
          0,
          5,
          10
        ],
        "1.5": [
          0,
          0,
          10
        ],
        "1.75": [
          0,
          5,
          10
        ],
        "2.0": [
          0,
          0.3,
          10
        ]
      }
    },
    "Mermaidtail": {
      "rotation": {
        "0.0": [
          0,
          0,
          0
        ],
        "0.5": [
          -12.5,
          0,
          0
        ],
        "1.0": [
          0,
          0,
          0
        ],
        "1.5": [
          -12.5,
          0,
          0
        ],
        "2.0": [
          0,
          0,
          0
        ]
      },
      "position": {
        "0.0": [
          0,
          0,
          0
        ],
        "1.0": [
          0,
          0,
          0
        ],
        "2.0": [
          0,
          0,
          0
        ]
      }
    },
    "Mermaidtail4": {
      "rotation": {
        "0.0": [
          0,
          0,
          0
        ],
        "0.5": [
          -17.5,
          0,
          0
        ],
        "1.0": [
          0,
          0,
          0
        ],
        "1.5": [
          -17.5,
          0,
          0
        ],
        "2.0": [
          0,
          0,
          0
        ]
      },
      "position": {
        "0.0": [
          0,
          0,
          0
        ],
        "0.5": [
          0,
          -0.5,
          -0.4
        ],
        "1.0": [
          0,
          0,
          0
        ],
        "1.5": [
          0,
          -0.5,
          -0.4
        ],
        "2.0": [
          0,
          0,
          0
        ]
      }
    },
    "Mermaidtail5": {
      "rotation": {
        "0.0": [
          0,
          0,
          0
        ],
        "0.5": [
          -52.5,
          0,
          0
        ],
        "1.0": [
          0,
          0,
          0
        ],
        "1.5": [
          -52.5,
          0,
          0
        ],
        "2.0": [
          0,
          0,
          0
        ]
      },
      "position": {
        "0.0": [
          0,
          0,
          0
        ],
        "0.5": [
          0,
          -1,
          0
        ],
        "1.0": [
          0,
          0,
          0
        ],
        "1.5": [
          0,
          -1,
          0
        ],
        "2.0": [
          0,
          0,
          0
        ]
      }
    },
    "Mermaidtail6": {
      "rotation": {
        "0.0": [
          0,
          0,
          0
        ],
        "0.5": [
          -80,
          0,
          0
        ],
        "1.0": [
          0,
          0,
          0
        ],
        "1.5": [
          -80,
          0,
          0
        ],
        "2.0": [
          0,
          0,
          0
        ]
      },
      "position": {
        "0.0": [
          0,
          0,
          0
        ],
        "0.5": [
          0,
          -1,
          1
        ],
        "1.0": [
          0,
          0,
          0
        ],
        "1.5": [
          0,
          -1,
          1
        ],
        "2.0": [
          0,
          0,
          0
        ]
      }
    }
  }
}
```

### `animation.mermaid_player.default_pose`

- `Swords_R/animations/mermaid_player.animation.json`; исходный SHA-256 `eb26e0a5bd9d5a94378c18b8c8172cd1adb6d91d054c724b4bb3aebf43ed8ed1`; format_version `1.8.0`.

```json
{
  "loop": true,
  "animation_length": 4,
  "bones": {
    "root": {
      "position": [
        0,
        4.5,
        0
      ]
    },
    "Mermaidtail": {
      "rotation": {
        "0.0": [
          0,
          0,
          0
        ],
        "1.0": [
          -12.5,
          0,
          0
        ],
        "2.0": [
          0,
          0,
          0
        ],
        "3.0": [
          -12.5,
          0,
          0
        ],
        "4.0": [
          0,
          0,
          0
        ]
      },
      "position": {
        "0.0": [
          0,
          0,
          0
        ],
        "2.0": [
          0,
          0,
          0
        ],
        "4.0": [
          0,
          0,
          0
        ]
      }
    },
    "Mermaidtail4": {
      "rotation": {
        "0.0": [
          0,
          0,
          0
        ],
        "1.0": [
          -17.5,
          0,
          0
        ],
        "2.0": [
          0,
          0,
          0
        ],
        "3.0": [
          -17.5,
          0,
          0
        ],
        "4.0": [
          0,
          0,
          0
        ]
      },
      "position": {
        "0.0": [
          0,
          0,
          0
        ],
        "1.0": [
          0,
          -0.5,
          -0.4
        ],
        "2.0": [
          0,
          0,
          0
        ],
        "3.0": [
          0,
          -0.5,
          -0.4
        ],
        "4.0": [
          0,
          0,
          0
        ]
      }
    },
    "Mermaidtail5": {
      "rotation": {
        "0.0": [
          0,
          0,
          0
        ],
        "1.0": [
          -52.5,
          0,
          0
        ],
        "2.0": [
          0,
          0,
          0
        ],
        "3.0": [
          -52.5,
          0,
          0
        ],
        "4.0": [
          0,
          0,
          0
        ]
      },
      "position": {
        "0.0": [
          0,
          0,
          0
        ],
        "1.0": [
          0,
          -1,
          0
        ],
        "2.0": [
          0,
          0,
          0
        ],
        "3.0": [
          0,
          -1,
          0
        ],
        "4.0": [
          0,
          0,
          0
        ]
      }
    },
    "Mermaidtail6": {
      "rotation": {
        "0.0": [
          0,
          0,
          0
        ],
        "1.0": [
          -80,
          0,
          0
        ],
        "2.0": [
          0,
          0,
          0
        ],
        "3.0": [
          -80,
          0,
          0
        ],
        "4.0": [
          0,
          0,
          0
        ]
      },
      "position": {
        "0.0": [
          0,
          0,
          0
        ],
        "1.0": [
          0,
          -1,
          1
        ],
        "2.0": [
          0,
          0,
          0
        ],
        "3.0": [
          0,
          -1,
          1
        ],
        "4.0": [
          0,
          0,
          0
        ]
      }
    }
  }
}
```

### `animation.player.explode`

- `Swords_R/animations/mobs.animation.json`; исходный SHA-256 `fcd99e85c9b2ce1237325735a2f5400bbff3db6983cb32800d9c040c56fbff84`; format_version `1.8.0`.

```json
{
  "animation_length": 1.52,
  "bones": {
    "body": {
      "position": {
        "0.0": [
          0,
          0,
          0
        ],
        "0.8": [
          0,
          2,
          0
        ]
      },
      "scale": {
        "0.0": [
          1,
          1,
          1
        ],
        "0.8": [
          1.3,
          1.2,
          1.3
        ]
      }
    },
    "head": {
      "position": {
        "0.0": [
          0,
          0,
          0
        ],
        "0.8": [
          0,
          0,
          0
        ]
      },
      "scale": {
        "0.0": [
          1,
          1,
          1
        ],
        "0.8": [
          1.2,
          1,
          1.2
        ]
      }
    },
    "leftArm": {
      "position": {
        "0.0": [
          0,
          0,
          0
        ],
        "0.8": [
          -1,
          0,
          0
        ]
      },
      "scale": {
        "0.0": [
          1,
          1,
          0.8
        ],
        "0.8": [
          1,
          1,
          1
        ]
      }
    },
    "rightArm": {
      "position": {
        "0.0": [
          0,
          0,
          0
        ],
        "0.8": [
          1,
          0,
          0
        ]
      },
      "scale": {
        "0.0": [
          1,
          1,
          1
        ],
        "0.8": [
          1,
          1,
          1
        ]
      }
    },
    "rightItem": {
      "position": [
        0,
        0,
        0
      ],
      "scale": 1
    },
    "leftLeg": {
      "position": {
        "0.0": [
          0,
          0,
          0
        ],
        "0.8": [
          0.5,
          0,
          0
        ]
      },
      "scale": {
        "0.0": [
          1,
          1,
          1
        ],
        "0.8": [
          1.33,
          1,
          1.13
        ]
      }
    },
    "rightLeg": {
      "position": {
        "0.0": [
          0,
          0,
          0
        ],
        "0.8": [
          -0.5,
          0,
          0
        ]
      },
      "scale": {
        "0.0": [
          1,
          1,
          1
        ],
        "0.8": [
          1.33,
          1,
          1.13
        ]
      }
    }
  }
}
```

### `animation.ultra_instinct_sword.attack`

- `Swords_R/animations/mobs.animation.json`; исходный SHA-256 `fcd99e85c9b2ce1237325735a2f5400bbff3db6983cb32800d9c040c56fbff84`; format_version `1.8.0`.

```json
{
  "loop": true,
  "animation_length": 0.32,
  "override_previous_animation": true,
  "bones": {
    "rightArm": {
      "rotation": {
        "0.0": [
          0,
          0,
          0
        ],
        "0.1167": [
          -110,
          15,
          -90
        ],
        "0.2333": [
          52,
          0,
          -92
        ],
        "0.3167": [
          0,
          0,
          0
        ]
      },
      "position": {
        "0.0": [
          0,
          0,
          0
        ],
        "0.2333": [
          1,
          0,
          -2
        ],
        "0.3167": [
          0,
          0,
          0
        ]
      }
    }
  }
}
```

### `animation.player_ghost.move`

- `Swords_R/animations/mobs.animation.json`; исходный SHA-256 `fcd99e85c9b2ce1237325735a2f5400bbff3db6983cb32800d9c040c56fbff84`; format_version `1.8.0`.

```json
{
  "loop": true,
  "animation_length": 2.0833,
  "bones": {
    "root": {
      "position": {
        "0.0": [
          0,
          0,
          0
        ],
        "1.0": [
          0,
          2,
          0
        ],
        "2.0833": [
          0,
          0,
          0
        ]
      }
    },
    "rightItem": {
      "rotation": [
        50.5,
        0,
        0
      ]
    },
    "leftLeg": {
      "position": [
        0,
        0,
        0
      ],
      "scale": 0
    },
    "rightLeg": {
      "position": [
        0,
        0,
        0
      ],
      "scale": 0
    },
    "ghost_cola": {
      "rotation": {
        "0.0": [
          0,
          0,
          0
        ],
        "0.7167": [
          5,
          0,
          0
        ],
        "1.4333": [
          10,
          0,
          0
        ],
        "2.0833": [
          0,
          0,
          0
        ]
      },
      "position": {
        "0.0": [
          0,
          0,
          0
        ],
        "1.2": [
          0,
          0.5,
          0
        ],
        "2.0833": [
          0,
          0,
          0
        ]
      }
    },
    "leftArm": {
      "rotation": {
        "0.0": [
          0,
          0,
          0
        ],
        "1.0": [
          0,
          0,
          -5
        ],
        "2.0333": [
          0,
          0,
          0
        ]
      },
      "position": [
        0,
        0,
        0
      ]
    },
    "rightArm": {
      "rotation": {
        "0.0": [
          0,
          0,
          0
        ],
        "0.9667": [
          0,
          0,
          5
        ],
        "2.0833": [
          0,
          0,
          0
        ]
      },
      "position": [
        0,
        0,
        0
      ]
    }
  }
}
```

### `animation.player_ghost.vision`

- `Swords_R/animations/mobs.animation.json`; исходный SHA-256 `fcd99e85c9b2ce1237325735a2f5400bbff3db6983cb32800d9c040c56fbff84`; format_version `1.8.0`.

```json
{
  "loop": true,
  "animation_length": 0.01667,
  "bones": {
    "ghost_hat": {
      "rotation": [
        0,
        0,
        0
      ],
      "position": [
        0,
        -39,
        1
      ],
      "scale": [
        2.5,
        2.5,
        1
      ]
    },
    "leftArm": {
      "position": [
        0,
        0,
        -5
      ]
    },
    "jacket": {
      "position": [
        0,
        0,
        -5
      ]
    }
  }
}
```

### `animation.shulker_shield.closed`

- `Swords_R/animations/shulker_shield.animation.json`; исходный SHA-256 `5676e31445e170b1812ee3935d8a92a79f37f0a0cac764a8c761340db80a6071`; format_version `1.8.0`.

```json
{
  "loop": true,
  "animation_length": 10000,
  "bones": {
    "lid": {
      "position": {
        "0.0": [
          0,
          0,
          0
        ],
        "0.4833": [
          0,
          -7.95,
          0
        ],
        "0.7667": [
          0,
          -13,
          0
        ],
        "1.0333": [
          0,
          -17,
          0
        ]
      }
    }
  }
}
```

### `animation.ultra_instinct.move`

- `Swords_R/animations/ultra_instinct_move.animation.json`; исходный SHA-256 `802a9868471451dfab189254d2dceb580c9f6338bba3a636e911d521aa898460`; format_version `1.8.0`.

```json
{
  "loop": true,
  "animation_length": 4,
  "bones": {
    "root": {
      "rotation": [
        0,
        0,
        0
      ],
      "position": {
        "0.0": [
          0,
          1,
          0
        ],
        "2.0": [
          0,
          3.5,
          0
        ],
        "4.0": [
          0,
          1,
          0
        ]
      }
    },
    "rightLeg": {
      "rotation": {
        "0.0": [
          0,
          0,
          0
        ],
        "1.3": [
          5,
          0,
          0
        ],
        "2.8": [
          -5,
          0,
          0
        ],
        "4.0": [
          0,
          0,
          0
        ]
      },
      "position": [
        0,
        0,
        0
      ]
    },
    "leftLeg": {
      "rotation": {
        "0.0": [
          0,
          0,
          0
        ],
        "1.3": [
          -5,
          0,
          0
        ],
        "2.8": [
          5,
          0,
          0
        ],
        "4.0": [
          0,
          0,
          0
        ]
      },
      "position": [
        0,
        0,
        0
      ]
    }
  }
}
```

### `animation.move`

- `Swords_R/animations/ultra_instinct_projectile.animation.json`; исходный SHA-256 `896f981aa6e68ef88c1fd0291ef24f447cb20319ccdf8419edf1c3a068368901`; format_version `1.8.0`.

```json
{
  "loop": true,
  "animation_length": 3.08,
  "bones": {
    "bone": {
      "rotation": {
        "0.0": [
          0,
          -50,
          -45
        ],
        "0.8": [
          0,
          -140,
          -45
        ],
        "1.6": [
          0,
          -230,
          -45
        ],
        "2.3167": [
          0,
          -320,
          -45
        ],
        "3.0833": [
          0,
          -410,
          -45
        ]
      },
      "position": [
        6,
        0,
        0
      ]
    }
  }
}
```

Сопоставление прочих моделей, геометрии и render controllers — в [графе ресурсов](resource-graph-2.8.14.md); оригинальные аудиофайлы и изображения — в [реестре ассетов](assets-2.8.14.md).
