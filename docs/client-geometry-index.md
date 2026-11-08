# Клиентская геометрия: модели, кости и полные определения

В `Sword_R/models/` 1.6 не обнаружено локальных JSON-моделей: это не исключает ванильную или внешнюю геометрию. В 2.x JSON-файлов: **21**, объявлений geometry: **21**. Сопоставлены оригинальные SHA-256 файлов и разобранные client aliases 2.8.8/2.8.14: эти данные совпадают; остальные файлы пакетов могут различаться.

Таблица показывает исходный format_version, расположение, прямо записанные размеры текстуры, количество элементов массива `bones` и количество прямо записанных `cubes`. `—` означает отсутствие поля; число кубов не включает прочие возможные формы геометрии. Это размеры разметки модели, не проверка размера присоединяемой PNG. Столбец aliases ищет точные ID только в `description.geometry` разобранных client entities: отсутствие там не означает отсутствие ссылок из блоков, render controllers, иных файлов или ванильных ресурсов.

Ниже полностью сохранён разобранный JSON каждого локального model-файла, включая имена/иерархию костей, pivot, origin, size, rotation, inflate, UV и все остальные поля как в исходной структуре. Оба синтаксиса `minecraft:geometry` и legacy-корня `geometry.*` сохраняются раздельно. Комментарии и форматирование JSON5 не сохраняются; исходные файлы архивов остаются эталоном.

- Ошибки разбора: нет.
- Повторные ключи: нет. JSON5 сохраняет последнее значение.

| ID / файл | Расположение / format_version | Размеры текстуры | bones / объявленные cubes | Прямые client aliases |
|---|---|---|---|---|
| `geometry.fake_ice`<br>`Swords_R/models/blocks/fake_ice.json` | `minecraft:geometry[0]`<br>`1.12.0` | `16` × `16` | 1 / 1 | не найдено в client entity |
| `geometry.fake_ice2`<br>`Swords_R/models/blocks/fake_ice2.json` | `minecraft:geometry[0]`<br>`1.12.0` | `16` × `16` | 1 / 1 | не найдено в client entity |
| `geometry.fake_ice3`<br>`Swords_R/models/blocks/fake_ice3.json` | `minecraft:geometry[0]`<br>`1.12.0` | `16` × `16` | 1 / 1 | не найдено в client entity |
| `geometry.fake_ice4`<br>`Swords_R/models/blocks/fake_ice4.json` | `minecraft:geometry[0]`<br>`1.12.0` | `16` × `16` | 1 / 1 | не найдено в client entity |
| `geometry.null`<br>`Swords_R/models/blocks/null.geo.json` | `minecraft:geometry[0]`<br>`1.12.0` | `1` × `1` | — / — | не найдено в client entity |
| `geometry.spectral_block`<br>`Swords_R/models/blocks/spectral_block.json` | `minecraft:geometry[0]`<br>`1.12.0` | `16` × `16` | 1 / 1 | не найдено в client entity |
| `geometry.baby_slime`<br>`Swords_R/models/entity/baby_slime.geo.json` | `minecraft:geometry[0]`<br>`1.12.0` | `64` × `32` | 7 / 11 | `Swords_R/entity/mountable_slime.v1.0.json` · `entity:mountable_slime` · `armor` |
| `geometry.blaze_aura`<br>`Swords_R/models/entity/blaze_aura.geo.json` | `minecraft:geometry[0]`<br>`1.12.0` | `64` × `64` | 23 / 6 | `Swords_R/entity/player.entity.json` · `minecraft:player` · `blaze_aura` |
| `geometry.blaze_rods`<br>`Swords_R/models/entity/blaze_rods.geo.json` | `geometry.blaze_rods`<br>`1.8.0` | `64` × `32` | 12 / 12 | `Swords_R/entity/player.entity.json` · `minecraft:player` · `blaze_rods` |
| `geometry.ghost`<br>`Swords_R/models/entity/ghost.geo.json` | `minecraft:geometry[0]`<br>`1.12.0` | `64` × `64` | 6 / 7 | `Swords_R/entity/ghost.v1.0.json` · `entity:ghost` · `ghost` |
| `geometry.grass`<br>`Swords_R/models/entity/grass.geo.json` | `minecraft:geometry[0]`<br>`1.12.0` | `16` × `16` | 6 / 5 | `Swords_R/entity/grass.v1.0.json` · `entity:grass` · `default` |
| `geometry.mermaid_player.tail`<br>`Swords_R/models/entity/mermaid_player.geo.json` | `minecraft:geometry[0]`<br>`1.12.0` | `64` × `64` | 16 / 12 | `Swords_R/entity/player.entity.json` · `minecraft:player` · `mermaid_player` |
| `geometry.mountable_slime`<br>`Swords_R/models/entity/mountable_slime.geo.json` | `geometry.mountable_slime`<br>`1.8.0` | `64` × `32` | 4 / 4 | `Swords_R/entity/mountable_slime.v1.0.json` · `entity:mountable_slime` · `default` |
| `geometry.player_ghost`<br>`Swords_R/models/entity/player_ghost.geo.json` | `minecraft:geometry[0]`<br>`1.12.0` | `64` × `64` | 22 / 15 | `Swords_R/entity/player.entity.json` · `minecraft:player` · `player_ghost` |
| `geometry.pumpkin_projectile`<br>`Swords_R/models/entity/pumpkin_projectile.geo.json` | `minecraft:geometry[0]`<br>`1.12.0` | `48` × `48` | 1 / 1 | `Swords_R/entity/pumpkin_projectile.entity.json` · `entity:pumpkin_projectile` · `default` |
| `geometry.shulker_shield`<br>`Swords_R/models/entity/shulker_shield.geo.json` | `geometry.shulker_shield`<br>`1.8.0` | `64` × `64` | 3 / 2 | `Swords_R/entity/shulker_shield.v1.0.json` · `entity:shulker_shield` · `default` |
| `geometry.slime_king.armor`<br>`Swords_R/models/entity/slime_king_armor.geo.json` | `minecraft:geometry[0]`<br>`1.12.0` | `64` × `32` | 5 / 8 | `Swords_R/entity/slime_king.entity.json` · `entity:slime_king` · `armor` |
| `geometry.ultra_instinct_aura`<br>`Swords_R/models/entity/ultra_instinct_aura.geo.json` | `minecraft:geometry[0]`<br>`1.12.0` | `64` × `64` | 23 / 6 | `Swords_R/entity/player.entity.json` · `minecraft:player` · `ultra_instinct_aura` |
| `geometry.ultra_instinct_projectile`<br>`Swords_R/models/entity/ultra_instinct_projectile.geo.json` | `minecraft:geometry[0]`<br>`1.12.0` | `64` × `64` | 1 / 1 | `Swords_R/entity/ultra_instinct_projectile.json` · `entity:ultra_instinct_projectile` · `default` |
| `geometry.wolf_transformation`<br>`Swords_R/models/entity/wolf_transformation.geo.json` | `minecraft:geometry[0]`<br>`1.12.0` | `64` × `64` | 25 / 10 | `Swords_R/entity/player.entity.json` · `minecraft:player` · `wolf_transformation` |
| `geometry.wolf_vision`<br>`Swords_R/models/entity/wolf_vision.geo.json` | `minecraft:geometry[0]`<br>`1.12.0` | `64` × `64` | 19 / 1 | `Swords_R/entity/player.entity.json` · `minecraft:player` · `wolf_vision` |

## Полные файлы моделей

### `Swords_R/models/blocks/fake_ice.json`

- SHA-256 исходного файла: `d5ff978680e3a0037a0a2cd555338353623bc85e7de66f826a4105c8aecadee0`.

```json
{
  "format_version": "1.12.0",
  "minecraft:geometry": [
    {
      "description": {
        "identifier": "geometry.fake_ice",
        "texture_width": 16,
        "texture_height": 16,
        "visible_bounds_width": 2,
        "visible_bounds_height": 3,
        "visible_bounds_offset": [
          0,
          0.5,
          0
        ]
      },
      "bones": [
        {
          "name": "fake_ice",
          "pivot": [
            0,
            0,
            0
          ],
          "cubes": [
            {
              "origin": [
                -8,
                0,
                -8
              ],
              "size": [
                16,
                16,
                16
              ],
              "uv": {
                "north": {
                  "uv": [
                    0,
                    0
                  ],
                  "uv_size": [
                    4,
                    8
                  ]
                },
                "east": {
                  "uv": [
                    0,
                    0
                  ],
                  "uv_size": [
                    4,
                    8
                  ]
                },
                "south": {
                  "uv": [
                    0,
                    0
                  ],
                  "uv_size": [
                    4,
                    8
                  ]
                },
                "west": {
                  "uv": [
                    0,
                    0
                  ],
                  "uv_size": [
                    4,
                    8
                  ]
                },
                "up": {
                  "uv": [
                    4,
                    8
                  ],
                  "uv_size": [
                    -4,
                    -8
                  ]
                },
                "down": {
                  "uv": [
                    4,
                    8
                  ],
                  "uv_size": [
                    -4,
                    -8
                  ]
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

### `Swords_R/models/blocks/fake_ice2.json`

- SHA-256 исходного файла: `3fa71f3de818d5f433eab5d38544d845426e29ca6776f35c4255a1b357aa29af`.

```json
{
  "format_version": "1.12.0",
  "minecraft:geometry": [
    {
      "description": {
        "identifier": "geometry.fake_ice2",
        "texture_width": 16,
        "texture_height": 16,
        "visible_bounds_width": 2,
        "visible_bounds_height": 3,
        "visible_bounds_offset": [
          0,
          0.5,
          0
        ]
      },
      "bones": [
        {
          "name": "fake_ice",
          "pivot": [
            0,
            0,
            0
          ],
          "cubes": [
            {
              "origin": [
                -8,
                0,
                -8
              ],
              "size": [
                16,
                16,
                16
              ],
              "uv": {
                "north": {
                  "uv": [
                    4,
                    8
                  ],
                  "uv_size": [
                    4,
                    8
                  ]
                },
                "east": {
                  "uv": [
                    4,
                    8
                  ],
                  "uv_size": [
                    4,
                    8
                  ]
                },
                "south": {
                  "uv": [
                    4,
                    8
                  ],
                  "uv_size": [
                    4,
                    8
                  ]
                },
                "west": {
                  "uv": [
                    4,
                    8
                  ],
                  "uv_size": [
                    4,
                    8
                  ]
                },
                "up": {
                  "uv": [
                    8,
                    16
                  ],
                  "uv_size": [
                    -4,
                    -8
                  ]
                },
                "down": {
                  "uv": [
                    8,
                    16
                  ],
                  "uv_size": [
                    -4,
                    -8
                  ]
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

### `Swords_R/models/blocks/fake_ice3.json`

- SHA-256 исходного файла: `ff2e1e9b01893dd97c4c5c066b430b90a114c8151e53521c62098082a5098bfc`.

```json
{
  "format_version": "1.12.0",
  "minecraft:geometry": [
    {
      "description": {
        "identifier": "geometry.fake_ice3",
        "texture_width": 16,
        "texture_height": 16,
        "visible_bounds_width": 2,
        "visible_bounds_height": 3,
        "visible_bounds_offset": [
          0,
          0.5,
          0
        ]
      },
      "bones": [
        {
          "name": "fake_ice",
          "pivot": [
            0,
            0,
            0
          ],
          "cubes": [
            {
              "origin": [
                -8,
                0,
                -8
              ],
              "size": [
                16,
                16,
                16
              ],
              "uv": {
                "north": {
                  "uv": [
                    8,
                    0
                  ],
                  "uv_size": [
                    4,
                    8
                  ]
                },
                "east": {
                  "uv": [
                    8,
                    0
                  ],
                  "uv_size": [
                    4,
                    8
                  ]
                },
                "south": {
                  "uv": [
                    8,
                    0
                  ],
                  "uv_size": [
                    4,
                    8
                  ]
                },
                "west": {
                  "uv": [
                    8,
                    0
                  ],
                  "uv_size": [
                    4,
                    8
                  ]
                },
                "up": {
                  "uv": [
                    12,
                    8
                  ],
                  "uv_size": [
                    -4,
                    -8
                  ]
                },
                "down": {
                  "uv": [
                    12,
                    8
                  ],
                  "uv_size": [
                    -4,
                    -8
                  ]
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

### `Swords_R/models/blocks/fake_ice4.json`

- SHA-256 исходного файла: `a99306467997fd4ebb803ac9fb0298ff0c010cc8a6d07b320b8d48ab94f38050`.

```json
{
  "format_version": "1.12.0",
  "minecraft:geometry": [
    {
      "description": {
        "identifier": "geometry.fake_ice4",
        "texture_width": 16,
        "texture_height": 16,
        "visible_bounds_width": 2,
        "visible_bounds_height": 3,
        "visible_bounds_offset": [
          0,
          0.5,
          0
        ]
      },
      "bones": [
        {
          "name": "fake_ice",
          "pivot": [
            0,
            0,
            0
          ],
          "cubes": [
            {
              "origin": [
                -8,
                0,
                -8
              ],
              "size": [
                16,
                16,
                16
              ],
              "uv": {
                "north": {
                  "uv": [
                    12,
                    8
                  ],
                  "uv_size": [
                    4,
                    8
                  ]
                },
                "east": {
                  "uv": [
                    12,
                    8
                  ],
                  "uv_size": [
                    4,
                    8
                  ]
                },
                "south": {
                  "uv": [
                    12,
                    8
                  ],
                  "uv_size": [
                    4,
                    8
                  ]
                },
                "west": {
                  "uv": [
                    12,
                    8
                  ],
                  "uv_size": [
                    4,
                    8
                  ]
                },
                "up": {
                  "uv": [
                    16,
                    16
                  ],
                  "uv_size": [
                    -4,
                    -8
                  ]
                },
                "down": {
                  "uv": [
                    16,
                    16
                  ],
                  "uv_size": [
                    -4,
                    -8
                  ]
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

### `Swords_R/models/blocks/null.geo.json`

- SHA-256 исходного файла: `e0ae421ba8041b70ccd4581b967d32211a90f61eff33d1642cf542f7b5e044b9`.

```json
{
  "format_version": "1.12.0",
  "minecraft:geometry": [
    {
      "description": {
        "identifier": "geometry.null",
        "texture_width": 1,
        "texture_height": 1
      }
    }
  ]
}
```

### `Swords_R/models/blocks/spectral_block.json`

- SHA-256 исходного файла: `14b9545a4fa4125ff1a96bbd002c69818ae2fd2119473e320be5056edf36dc09`.

```json
{
  "format_version": "1.12.0",
  "minecraft:geometry": [
    {
      "description": {
        "identifier": "geometry.spectral_block",
        "texture_width": 16,
        "texture_height": 16,
        "visible_bounds_width": 2,
        "visible_bounds_height": 2,
        "visible_bounds_offset": [
          0,
          0,
          0
        ]
      },
      "bones": [
        {
          "name": "stone",
          "pivot": [
            0,
            0,
            0
          ],
          "cubes": [
            {
              "origin": [
                -8,
                0,
                -8
              ],
              "size": [
                16,
                16,
                16
              ],
              "uv": {
                "north": {
                  "uv": [
                    0,
                    0
                  ],
                  "uv_size": [
                    16,
                    16
                  ]
                },
                "east": {
                  "uv": [
                    0,
                    0
                  ],
                  "uv_size": [
                    16,
                    16
                  ]
                },
                "south": {
                  "uv": [
                    0,
                    0
                  ],
                  "uv_size": [
                    16,
                    16
                  ]
                },
                "west": {
                  "uv": [
                    0,
                    0
                  ],
                  "uv_size": [
                    16,
                    16
                  ]
                },
                "up": {
                  "uv": [
                    16,
                    16
                  ],
                  "uv_size": [
                    -16,
                    -16
                  ]
                },
                "down": {
                  "uv": [
                    0,
                    16
                  ],
                  "uv_size": [
                    16,
                    -16
                  ]
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

### `Swords_R/models/entity/baby_slime.geo.json`

- SHA-256 исходного файла: `4080689c9587f6743dd2e13ef7094d0d019b1a80456fbb314f65f75d72e93661`.

```json
{
  "format_version": "1.12.0",
  "minecraft:geometry": [
    {
      "description": {
        "identifier": "geometry.baby_slime",
        "texture_width": 64,
        "texture_height": 32,
        "visible_bounds_width": 3,
        "visible_bounds_height": 2,
        "visible_bounds_offset": [
          0,
          1,
          0
        ]
      },
      "bones": [
        {
          "name": "cube",
          "pivot": [
            0,
            24,
            0
          ],
          "cubes": [
            {
              "origin": [
                -4.5,
                -0.2,
                -4
              ],
              "size": [
                8.9,
                8.2,
                8.9
              ],
              "uv": {
                "north": {
                  "uv": [
                    8,
                    8
                  ],
                  "uv_size": [
                    8,
                    8
                  ]
                },
                "east": {
                  "uv": [
                    0,
                    8
                  ],
                  "uv_size": [
                    8,
                    8
                  ]
                },
                "south": {
                  "uv": [
                    24,
                    8
                  ],
                  "uv_size": [
                    8,
                    8
                  ]
                },
                "west": {
                  "uv": [
                    16,
                    8
                  ],
                  "uv_size": [
                    8,
                    8
                  ]
                },
                "up": {
                  "uv": [
                    8,
                    0
                  ],
                  "uv_size": [
                    8,
                    8
                  ]
                },
                "down": {
                  "uv": [
                    16,
                    8
                  ],
                  "uv_size": [
                    8,
                    -8
                  ]
                }
              }
            }
          ]
        },
        {
          "name": "eye0",
          "parent": "cube",
          "pivot": [
            0,
            24,
            0
          ],
          "cubes": [
            {
              "origin": [
                -3.3,
                4,
                -3.5
              ],
              "size": [
                2,
                2,
                2
              ],
              "uv": {
                "north": {
                  "uv": [
                    34,
                    2
                  ],
                  "uv_size": [
                    2,
                    2
                  ]
                },
                "east": {
                  "uv": [
                    32,
                    2
                  ],
                  "uv_size": [
                    2,
                    2
                  ]
                },
                "south": {
                  "uv": [
                    38,
                    2
                  ],
                  "uv_size": [
                    2,
                    2
                  ]
                },
                "west": {
                  "uv": [
                    36,
                    2
                  ],
                  "uv_size": [
                    2,
                    2
                  ]
                },
                "up": {
                  "uv": [
                    34,
                    0
                  ],
                  "uv_size": [
                    2,
                    2
                  ]
                },
                "down": {
                  "uv": [
                    36,
                    2
                  ],
                  "uv_size": [
                    2,
                    -2
                  ]
                }
              }
            }
          ]
        },
        {
          "name": "eye1",
          "parent": "cube",
          "pivot": [
            0,
            24,
            0
          ],
          "cubes": [
            {
              "origin": [
                1.3,
                4,
                -3.5
              ],
              "size": [
                2,
                2,
                2
              ],
              "uv": {
                "north": {
                  "uv": [
                    34,
                    6
                  ],
                  "uv_size": [
                    2,
                    2
                  ]
                },
                "east": {
                  "uv": [
                    32,
                    6
                  ],
                  "uv_size": [
                    2,
                    2
                  ]
                },
                "south": {
                  "uv": [
                    38,
                    6
                  ],
                  "uv_size": [
                    2,
                    2
                  ]
                },
                "west": {
                  "uv": [
                    36,
                    6
                  ],
                  "uv_size": [
                    2,
                    2
                  ]
                },
                "up": {
                  "uv": [
                    34,
                    4
                  ],
                  "uv_size": [
                    2,
                    2
                  ]
                },
                "down": {
                  "uv": [
                    36,
                    6
                  ],
                  "uv_size": [
                    2,
                    -2
                  ]
                }
              }
            }
          ]
        },
        {
          "name": "mouth",
          "parent": "cube",
          "pivot": [
            0,
            24,
            0
          ],
          "cubes": [
            {
              "origin": [
                0,
                2,
                -3.5
              ],
              "size": [
                1,
                1,
                1
              ],
              "uv": {
                "north": {
                  "uv": [
                    33,
                    9
                  ],
                  "uv_size": [
                    1,
                    1
                  ]
                },
                "east": {
                  "uv": [
                    32,
                    9
                  ],
                  "uv_size": [
                    1,
                    1
                  ]
                },
                "south": {
                  "uv": [
                    35,
                    9
                  ],
                  "uv_size": [
                    1,
                    1
                  ]
                },
                "west": {
                  "uv": [
                    34,
                    9
                  ],
                  "uv_size": [
                    1,
                    1
                  ]
                },
                "up": {
                  "uv": [
                    33,
                    8
                  ],
                  "uv_size": [
                    1,
                    1
                  ]
                },
                "down": {
                  "uv": [
                    34,
                    9
                  ],
                  "uv_size": [
                    1,
                    -1
                  ]
                }
              }
            }
          ]
        },
        {
          "name": "baby",
          "pivot": [
            0,
            -0.7,
            0.4
          ],
          "cubes": [
            {
              "origin": [
                -1,
                1.3,
                -4.6
              ],
              "size": [
                2,
                2,
                1
              ],
              "uv": {
                "north": {
                  "uv": [
                    35,
                    25
                  ],
                  "uv_size": [
                    2,
                    2
                  ]
                },
                "east": {
                  "uv": [
                    34,
                    25
                  ],
                  "uv_size": [
                    1,
                    2
                  ]
                },
                "south": {
                  "uv": [
                    38,
                    25
                  ],
                  "uv_size": [
                    2,
                    2
                  ]
                },
                "west": {
                  "uv": [
                    37,
                    25
                  ],
                  "uv_size": [
                    1,
                    2
                  ]
                },
                "up": {
                  "uv": [
                    35,
                    24
                  ],
                  "uv_size": [
                    2,
                    1
                  ]
                },
                "down": {
                  "uv": [
                    37,
                    25
                  ],
                  "uv_size": [
                    2,
                    -1
                  ]
                }
              }
            },
            {
              "origin": [
                1,
                1.3,
                -4.6
              ],
              "size": [
                1,
                2,
                1
              ],
              "uv": {
                "north": {
                  "uv": [
                    26,
                    26
                  ],
                  "uv_size": [
                    1,
                    2
                  ]
                },
                "east": {
                  "uv": [
                    25,
                    26
                  ],
                  "uv_size": [
                    1,
                    2
                  ]
                },
                "south": {
                  "uv": [
                    28,
                    26
                  ],
                  "uv_size": [
                    1,
                    2
                  ]
                },
                "west": {
                  "uv": [
                    27,
                    26
                  ],
                  "uv_size": [
                    1,
                    2
                  ]
                },
                "up": {
                  "uv": [
                    26,
                    25
                  ],
                  "uv_size": [
                    1,
                    1
                  ]
                },
                "down": {
                  "uv": [
                    27,
                    26
                  ],
                  "uv_size": [
                    1,
                    -1
                  ]
                }
              }
            },
            {
              "origin": [
                -2,
                1.3,
                -4.6
              ],
              "size": [
                1,
                2,
                1
              ],
              "uv": {
                "north": {
                  "uv": [
                    1,
                    1
                  ],
                  "uv_size": [
                    1,
                    2
                  ]
                },
                "east": {
                  "uv": [
                    0,
                    1
                  ],
                  "uv_size": [
                    1,
                    2
                  ]
                },
                "south": {
                  "uv": [
                    3,
                    1
                  ],
                  "uv_size": [
                    1,
                    2
                  ]
                },
                "west": {
                  "uv": [
                    2,
                    1
                  ],
                  "uv_size": [
                    1,
                    2
                  ]
                },
                "up": {
                  "uv": [
                    1,
                    0
                  ],
                  "uv_size": [
                    1,
                    1
                  ]
                },
                "down": {
                  "uv": [
                    2,
                    1
                  ],
                  "uv_size": [
                    1,
                    -1
                  ]
                }
              }
            },
            {
              "origin": [
                -1,
                3.3,
                -4.6
              ],
              "size": [
                2,
                1,
                1
              ],
              "uv": {
                "north": {
                  "uv": [
                    26,
                    23
                  ],
                  "uv_size": [
                    2,
                    1
                  ]
                },
                "east": {
                  "uv": [
                    25,
                    23
                  ],
                  "uv_size": [
                    1,
                    1
                  ]
                },
                "south": {
                  "uv": [
                    29,
                    23
                  ],
                  "uv_size": [
                    2,
                    1
                  ]
                },
                "west": {
                  "uv": [
                    28,
                    23
                  ],
                  "uv_size": [
                    1,
                    1
                  ]
                },
                "up": {
                  "uv": [
                    26,
                    22
                  ],
                  "uv_size": [
                    2,
                    1
                  ]
                },
                "down": {
                  "uv": [
                    28,
                    23
                  ],
                  "uv_size": [
                    2,
                    -1
                  ]
                }
              }
            },
            {
              "origin": [
                -1,
                0.3,
                -4.6
              ],
              "size": [
                2,
                1,
                1
              ],
              "uv": {
                "north": {
                  "uv": [
                    1,
                    6
                  ],
                  "uv_size": [
                    2,
                    1
                  ]
                },
                "east": {
                  "uv": [
                    0,
                    6
                  ],
                  "uv_size": [
                    1,
                    1
                  ]
                },
                "south": {
                  "uv": [
                    4,
                    6
                  ],
                  "uv_size": [
                    2,
                    1
                  ]
                },
                "west": {
                  "uv": [
                    3,
                    6
                  ],
                  "uv_size": [
                    1,
                    1
                  ]
                },
                "up": {
                  "uv": [
                    1,
                    5
                  ],
                  "uv_size": [
                    2,
                    1
                  ]
                },
                "down": {
                  "uv": [
                    3,
                    6
                  ],
                  "uv_size": [
                    2,
                    -1
                  ]
                }
              }
            }
          ]
        },
        {
          "name": "wings",
          "pivot": [
            3.8,
            6.5,
            0
          ],
          "rotation": [
            9.83601,
            14.76689,
            -10.34527
          ],
          "cubes": [
            {
              "origin": [
                4.14867,
                7.15887,
                -0.53904
              ],
              "size": [
                9,
                0,
                6
              ],
              "uv": {
                "north": {
                  "uv": [
                    40,
                    23
                  ],
                  "uv_size": [
                    9,
                    0
                  ]
                },
                "east": {
                  "uv": [
                    34,
                    23
                  ],
                  "uv_size": [
                    6,
                    0
                  ]
                },
                "south": {
                  "uv": [
                    55,
                    23
                  ],
                  "uv_size": [
                    9,
                    0
                  ]
                },
                "west": {
                  "uv": [
                    49,
                    23
                  ],
                  "uv_size": [
                    6,
                    0
                  ]
                },
                "up": {
                  "uv": [
                    40,
                    17
                  ],
                  "uv_size": [
                    9,
                    6
                  ]
                },
                "down": {
                  "uv": [
                    40,
                    23
                  ],
                  "uv_size": [
                    9,
                    -6
                  ]
                }
              }
            }
          ]
        },
        {
          "name": "wings2",
          "pivot": [
            -3.8,
            7,
            1
          ],
          "rotation": [
            164.11935,
            -33.04568,
            -156.11033
          ],
          "cubes": [
            {
              "origin": [
                -3.81854,
                7.1962,
                0.54098
              ],
              "size": [
                9,
                0,
                6
              ],
              "uv": {
                "north": {
                  "uv": [
                    40,
                    23
                  ],
                  "uv_size": [
                    9,
                    0
                  ]
                },
                "east": {
                  "uv": [
                    34,
                    23
                  ],
                  "uv_size": [
                    6,
                    0
                  ]
                },
                "south": {
                  "uv": [
                    55,
                    23
                  ],
                  "uv_size": [
                    9,
                    0
                  ]
                },
                "west": {
                  "uv": [
                    49,
                    23
                  ],
                  "uv_size": [
                    6,
                    0
                  ]
                },
                "up": {
                  "uv": [
                    40,
                    17
                  ],
                  "uv_size": [
                    9,
                    6
                  ]
                },
                "down": {
                  "uv": [
                    40,
                    23
                  ],
                  "uv_size": [
                    9,
                    -6
                  ]
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

### `Swords_R/models/entity/blaze_aura.geo.json`

- SHA-256 исходного файла: `aed029e6747d55ddb91c741e8e471c5f5adc5392c38fb95f5493d021d56e04c5`.

```json
{
  "format_version": "1.12.0",
  "minecraft:geometry": [
    {
      "description": {
        "identifier": "geometry.blaze_aura",
        "texture_width": 64,
        "texture_height": 64,
        "visible_bounds_width": 3,
        "visible_bounds_height": 4.5,
        "visible_bounds_offset": [
          0,
          0.75,
          0
        ]
      },
      "bones": [
        {
          "name": "root",
          "pivot": [
            0,
            0,
            0
          ]
        },
        {
          "name": "waist",
          "parent": "root",
          "pivot": [
            0,
            12,
            0
          ]
        },
        {
          "name": "body",
          "parent": "waist",
          "pivot": [
            0,
            24,
            0
          ]
        },
        {
          "name": "head",
          "parent": "body",
          "pivot": [
            0,
            24,
            0
          ]
        },
        {
          "name": "hat",
          "parent": "head",
          "pivot": [
            0,
            24,
            0
          ]
        },
        {
          "name": "hat_aura",
          "parent": "hat",
          "pivot": [
            0,
            0,
            0
          ],
          "cubes": [
            {
              "origin": [
                -4.2432,
                24.50667,
                -4.2432
              ],
              "size": [
                8.4864,
                8.4864,
                8.4864
              ],
              "inflate": 0.5,
              "uv": {
                "north": {
                  "uv": [
                    32,
                    32
                  ],
                  "uv_size": [
                    32,
                    32
                  ]
                },
                "east": {
                  "uv": [
                    32,
                    32
                  ],
                  "uv_size": [
                    32,
                    32
                  ]
                },
                "south": {
                  "uv": [
                    32,
                    32
                  ],
                  "uv_size": [
                    32,
                    32
                  ]
                },
                "west": {
                  "uv": [
                    32,
                    32
                  ],
                  "uv_size": [
                    32,
                    32
                  ]
                },
                "up": {
                  "uv": [
                    64,
                    64
                  ],
                  "uv_size": [
                    -32,
                    -32
                  ]
                },
                "down": {
                  "uv": [
                    64,
                    64
                  ],
                  "uv_size": [
                    -32,
                    -32
                  ]
                }
              }
            }
          ]
        },
        {
          "name": "cape",
          "parent": "body",
          "pivot": [
            0,
            24,
            3
          ]
        },
        {
          "name": "leftArm",
          "parent": "body",
          "pivot": [
            5,
            22,
            0
          ]
        },
        {
          "name": "leftSleeve",
          "parent": "leftArm",
          "pivot": [
            5,
            22,
            0
          ]
        },
        {
          "name": "leftSleeve_aura",
          "parent": "leftSleeve",
          "pivot": [
            0,
            0,
            0
          ],
          "cubes": [
            {
              "origin": [
                4.2432,
                11.77707,
                -2.1216
              ],
              "size": [
                4.2432,
                12.7296,
                4.2432
              ],
              "inflate": 0.25,
              "uv": {
                "north": {
                  "uv": [
                    32,
                    32
                  ],
                  "uv_size": [
                    32,
                    32
                  ]
                },
                "east": {
                  "uv": [
                    32,
                    32
                  ],
                  "uv_size": [
                    32,
                    32
                  ]
                },
                "south": {
                  "uv": [
                    32,
                    32
                  ],
                  "uv_size": [
                    32,
                    32
                  ]
                },
                "west": {
                  "uv": [
                    32,
                    32
                  ],
                  "uv_size": [
                    32,
                    32
                  ]
                },
                "up": {
                  "uv": [
                    64,
                    64
                  ],
                  "uv_size": [
                    -32,
                    -32
                  ]
                },
                "down": {
                  "uv": [
                    64,
                    64
                  ],
                  "uv_size": [
                    -32,
                    -32
                  ]
                }
              }
            }
          ]
        },
        {
          "name": "leftItem",
          "parent": "leftArm",
          "pivot": [
            6,
            15,
            1
          ]
        },
        {
          "name": "rightArm",
          "parent": "body",
          "pivot": [
            -5,
            22,
            0
          ]
        },
        {
          "name": "rightSleeve",
          "parent": "rightArm",
          "pivot": [
            -5,
            22,
            0
          ]
        },
        {
          "name": "rightSleeve_aura",
          "parent": "rightSleeve",
          "pivot": [
            0,
            0,
            0
          ],
          "cubes": [
            {
              "origin": [
                -8.4864,
                11.77707,
                -2.1216
              ],
              "size": [
                4.2432,
                12.7296,
                4.2432
              ],
              "inflate": 0.25,
              "uv": {
                "north": {
                  "uv": [
                    40,
                    40
                  ],
                  "uv_size": [
                    4,
                    12
                  ]
                },
                "east": {
                  "uv": [
                    36,
                    40
                  ],
                  "uv_size": [
                    4,
                    12
                  ]
                },
                "south": {
                  "uv": [
                    48,
                    40
                  ],
                  "uv_size": [
                    4,
                    12
                  ]
                },
                "west": {
                  "uv": [
                    44,
                    40
                  ],
                  "uv_size": [
                    4,
                    12
                  ]
                },
                "up": {
                  "uv": [
                    40,
                    36
                  ],
                  "uv_size": [
                    4,
                    4
                  ]
                },
                "down": {
                  "uv": [
                    44,
                    40
                  ],
                  "uv_size": [
                    4,
                    -4
                  ]
                }
              }
            }
          ]
        },
        {
          "name": "rightItem",
          "parent": "rightArm",
          "pivot": [
            -6,
            15,
            1
          ]
        },
        {
          "name": "jacket",
          "parent": "body",
          "pivot": [
            0,
            24,
            0
          ]
        },
        {
          "name": "jacket_aura",
          "parent": "jacket",
          "pivot": [
            0,
            0,
            0
          ],
          "cubes": [
            {
              "origin": [
                -4.2432,
                11.77707,
                -2.1216
              ],
              "size": [
                8.4864,
                12.7296,
                4.2432
              ],
              "inflate": 0.25,
              "uv": {
                "north": {
                  "uv": [
                    32,
                    32
                  ],
                  "uv_size": [
                    32,
                    32
                  ]
                },
                "east": {
                  "uv": [
                    32,
                    32
                  ],
                  "uv_size": [
                    32,
                    32
                  ]
                },
                "south": {
                  "uv": [
                    32,
                    32
                  ],
                  "uv_size": [
                    32,
                    32
                  ]
                },
                "west": {
                  "uv": [
                    32,
                    32
                  ],
                  "uv_size": [
                    32,
                    32
                  ]
                },
                "up": {
                  "uv": [
                    64,
                    64
                  ],
                  "uv_size": [
                    -32,
                    -32
                  ]
                },
                "down": {
                  "uv": [
                    64,
                    64
                  ],
                  "uv_size": [
                    -32,
                    -32
                  ]
                }
              }
            }
          ]
        },
        {
          "name": "leftLeg",
          "parent": "root",
          "pivot": [
            1.9,
            12,
            0
          ]
        },
        {
          "name": "leftPants",
          "parent": "leftLeg",
          "pivot": [
            1.9,
            12,
            0
          ]
        },
        {
          "name": "leftPants_aura",
          "parent": "leftPants",
          "pivot": [
            0,
            0,
            0
          ],
          "cubes": [
            {
              "origin": [
                -0.10608,
                -0.95253,
                -2.1216
              ],
              "size": [
                4.2432,
                12.7296,
                4.2432
              ],
              "inflate": 0.25,
              "uv": {
                "north": {
                  "uv": [
                    32,
                    32
                  ],
                  "uv_size": [
                    32,
                    32
                  ]
                },
                "east": {
                  "uv": [
                    32,
                    32
                  ],
                  "uv_size": [
                    32,
                    32
                  ]
                },
                "south": {
                  "uv": [
                    32,
                    32
                  ],
                  "uv_size": [
                    32,
                    32
                  ]
                },
                "west": {
                  "uv": [
                    32,
                    32
                  ],
                  "uv_size": [
                    32,
                    32
                  ]
                },
                "up": {
                  "uv": [
                    64,
                    64
                  ],
                  "uv_size": [
                    -32,
                    -32
                  ]
                },
                "down": {
                  "uv": [
                    64,
                    64
                  ],
                  "uv_size": [
                    -32,
                    -32
                  ]
                }
              }
            }
          ]
        },
        {
          "name": "rightLeg",
          "parent": "root",
          "pivot": [
            -1.9,
            12,
            0
          ]
        },
        {
          "name": "rightPants",
          "parent": "rightLeg",
          "pivot": [
            -1.9,
            12,
            0
          ]
        },
        {
          "name": "rightPants_aura",
          "parent": "rightPants",
          "pivot": [
            0,
            0,
            0
          ],
          "cubes": [
            {
              "origin": [
                -4.13712,
                -0.95253,
                -2.1216
              ],
              "size": [
                4.2432,
                12.7296,
                4.2432
              ],
              "inflate": 0.25,
              "uv": {
                "north": {
                  "uv": [
                    32,
                    32
                  ],
                  "uv_size": [
                    32,
                    32
                  ]
                },
                "east": {
                  "uv": [
                    32,
                    32
                  ],
                  "uv_size": [
                    32,
                    32
                  ]
                },
                "south": {
                  "uv": [
                    32,
                    32
                  ],
                  "uv_size": [
                    32,
                    32
                  ]
                },
                "west": {
                  "uv": [
                    32,
                    32
                  ],
                  "uv_size": [
                    32,
                    32
                  ]
                },
                "up": {
                  "uv": [
                    64,
                    64
                  ],
                  "uv_size": [
                    -32,
                    -32
                  ]
                },
                "down": {
                  "uv": [
                    64,
                    64
                  ],
                  "uv_size": [
                    -32,
                    -32
                  ]
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

### `Swords_R/models/entity/blaze_rods.geo.json`

- SHA-256 исходного файла: `d604a51c17059ee88dab22311302b263d3847cb47291425d861389b8da6fd3e0`.

```json
{
  "format_version": "1.8.0",
  "geometry.blaze_rods": {
    "texturewidth": 64,
    "textureheight": 32,
    "visible_bounds_width": 2,
    "visible_bounds_height": 2,
    "visible_bounds_offset": [
      0,
      1,
      0
    ],
    "bones": [
      {
        "name": "upperBodyParts0",
        "pivot": [
          0,
          24,
          0
        ],
        "cubes": [
          {
            "origin": [
              0,
              16,
              0
            ],
            "size": [
              2,
              8,
              2
            ],
            "uv": [
              0,
              16
            ]
          }
        ]
      },
      {
        "name": "upperBodyParts1",
        "pivot": [
          0,
          24,
          0
        ],
        "cubes": [
          {
            "origin": [
              0,
              16,
              0
            ],
            "size": [
              2,
              8,
              2
            ],
            "uv": [
              0,
              16
            ]
          }
        ]
      },
      {
        "name": "upperBodyParts2",
        "pivot": [
          0,
          24,
          0
        ],
        "cubes": [
          {
            "origin": [
              0,
              16,
              0
            ],
            "size": [
              2,
              8,
              2
            ],
            "uv": [
              0,
              16
            ]
          }
        ]
      },
      {
        "name": "upperBodyParts3",
        "pivot": [
          0,
          24,
          0
        ],
        "cubes": [
          {
            "origin": [
              0,
              16,
              0
            ],
            "size": [
              2,
              8,
              2
            ],
            "uv": [
              0,
              16
            ]
          }
        ]
      },
      {
        "name": "upperBodyParts4",
        "pivot": [
          0,
          24,
          0
        ],
        "cubes": [
          {
            "origin": [
              0,
              16,
              0
            ],
            "size": [
              2,
              8,
              2
            ],
            "uv": [
              0,
              16
            ]
          }
        ]
      },
      {
        "name": "upperBodyParts5",
        "pivot": [
          0,
          24,
          0
        ],
        "cubes": [
          {
            "origin": [
              0,
              16,
              0
            ],
            "size": [
              2,
              8,
              2
            ],
            "uv": [
              0,
              16
            ]
          }
        ]
      },
      {
        "name": "upperBodyParts6",
        "pivot": [
          0,
          24,
          0
        ],
        "cubes": [
          {
            "origin": [
              0,
              16,
              0
            ],
            "size": [
              2,
              8,
              2
            ],
            "uv": [
              0,
              16
            ]
          }
        ]
      },
      {
        "name": "upperBodyParts7",
        "pivot": [
          0,
          24,
          0
        ],
        "cubes": [
          {
            "origin": [
              0,
              16,
              0
            ],
            "size": [
              2,
              8,
              2
            ],
            "uv": [
              0,
              16
            ]
          }
        ]
      },
      {
        "name": "upperBodyParts8",
        "pivot": [
          0,
          24,
          0
        ],
        "cubes": [
          {
            "origin": [
              0,
              16,
              0
            ],
            "size": [
              2,
              8,
              2
            ],
            "uv": [
              0,
              16
            ]
          }
        ]
      },
      {
        "name": "upperBodyParts9",
        "pivot": [
          0,
          24,
          0
        ],
        "cubes": [
          {
            "origin": [
              0,
              16,
              0
            ],
            "size": [
              2,
              8,
              2
            ],
            "uv": [
              0,
              16
            ]
          }
        ]
      },
      {
        "name": "upperBodyParts10",
        "pivot": [
          0,
          24,
          0
        ],
        "cubes": [
          {
            "origin": [
              0,
              16,
              0
            ],
            "size": [
              2,
              8,
              2
            ],
            "uv": [
              0,
              16
            ]
          }
        ]
      },
      {
        "name": "upperBodyParts11",
        "pivot": [
          0,
          24,
          0
        ],
        "cubes": [
          {
            "origin": [
              0,
              16,
              0
            ],
            "size": [
              2,
              8,
              2
            ],
            "uv": [
              0,
              16
            ]
          }
        ]
      }
    ]
  }
}
```

### `Swords_R/models/entity/ghost.geo.json`

- SHA-256 исходного файла: `69e1b1f2cef2d387f47fe8134cbdf8c15abf51865e58eb6d945136e7008353da`.

```json
{
  "format_version": "1.12.0",
  "minecraft:geometry": [
    {
      "description": {
        "identifier": "geometry.ghost",
        "texture_width": 64,
        "texture_height": 64,
        "visible_bounds_width": 3,
        "visible_bounds_height": 3,
        "visible_bounds_offset": [
          0,
          0,
          0
        ]
      },
      "bones": [
        {
          "name": "body",
          "pivot": [
            0,
            0,
            0
          ]
        },
        {
          "name": "ghost_head",
          "parent": "body",
          "pivot": [
            0,
            28.45,
            0
          ],
          "cubes": [
            {
              "origin": [
                -4.24,
                24.21,
                -4.24
              ],
              "size": [
                8.48,
                8.48,
                8.48
              ],
              "inflate": 0.5,
              "uv": [
                32,
                0
              ]
            }
          ]
        },
        {
          "name": "chest",
          "parent": "body",
          "pivot": [
            0,
            17.85,
            0
          ],
          "cubes": [
            {
              "origin": [
                -4.24,
                11.49,
                -2.12
              ],
              "size": [
                8.48,
                12.72,
                4.24
              ],
              "inflate": 0.25,
              "uv": [
                16,
                32
              ]
            }
          ]
        },
        {
          "name": "leftArm",
          "parent": "body",
          "pivot": [
            6.36,
            23.85,
            0
          ],
          "cubes": [
            {
              "origin": [
                4.24,
                11.49,
                -2.12
              ],
              "size": [
                4.24,
                12.72,
                4.24
              ],
              "inflate": 0.25,
              "uv": [
                48,
                48
              ]
            }
          ]
        },
        {
          "name": "rightArm",
          "parent": "body",
          "pivot": [
            -6.36,
            23.85,
            0
          ],
          "cubes": [
            {
              "origin": [
                -8.48,
                11.49,
                -2.12
              ],
              "size": [
                4.24,
                12.72,
                4.24
              ],
              "inflate": 0.25,
              "uv": [
                40,
                32
              ]
            }
          ]
        },
        {
          "name": "ghost_tail",
          "parent": "body",
          "pivot": [
            0,
            11.0673,
            -0.56378
          ],
          "cubes": [
            {
              "origin": [
                -1.24,
                4.37397,
                7.48289
              ],
              "size": [
                2.48,
                2.72,
                1.24
              ],
              "inflate": 0.25,
              "pivot": [
                0,
                4.23397,
                7.60289
              ],
              "rotation": [
                55,
                0,
                0
              ],
              "uv": [
                16,
                32
              ]
            },
            {
              "origin": [
                -2.24,
                5.37397,
                2.48289
              ],
              "size": [
                4.48,
                4.72,
                3.24
              ],
              "inflate": 0.25,
              "pivot": [
                0,
                7.23397,
                4.60289
              ],
              "rotation": [
                55,
                0,
                0
              ],
              "uv": [
                16,
                32
              ]
            },
            {
              "origin": [
                -4.24,
                8.37397,
                -0.51711
              ],
              "size": [
                8.48,
                4.72,
                3.24
              ],
              "inflate": 0.25,
              "pivot": [
                0,
                10.23397,
                1.60289
              ],
              "rotation": [
                40,
                0,
                0
              ],
              "uv": [
                16,
                32
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

### `Swords_R/models/entity/grass.geo.json`

- SHA-256 исходного файла: `990ae9323bc5cbb4632a4b8cb5ed9db640dd843bda76638f5f7adfc104185693`.

```json
{
  "format_version": "1.12.0",
  "minecraft:geometry": [
    {
      "description": {
        "identifier": "geometry.grass",
        "texture_width": 16,
        "texture_height": 16,
        "visible_bounds_width": 3,
        "visible_bounds_height": 2,
        "visible_bounds_offset": [
          0,
          0,
          0
        ]
      },
      "bones": [
        {
          "name": "grass",
          "pivot": [
            -0.8,
            -7.6,
            0.4
          ]
        },
        {
          "name": "bone",
          "parent": "grass",
          "pivot": [
            -4,
            -16,
            -5
          ],
          "cubes": [
            {
              "origin": [
                -13,
                -16,
                -4
              ],
              "size": [
                17,
                16,
                0
              ],
              "pivot": [
                -4,
                -16,
                -5
              ],
              "rotation": [
                15,
                45,
                0
              ],
              "uv": {
                "north": {
                  "uv": [
                    0,
                    8
                  ],
                  "uv_size": [
                    8,
                    8
                  ]
                },
                "east": {
                  "uv": [
                    4,
                    0
                  ],
                  "uv_size": [
                    0,
                    16
                  ]
                },
                "south": {
                  "uv": [
                    8,
                    0
                  ],
                  "uv_size": [
                    -8,
                    8
                  ]
                },
                "west": {
                  "uv": [
                    21,
                    0
                  ],
                  "uv_size": [
                    0,
                    16
                  ]
                },
                "up": {
                  "uv": [
                    4,
                    0
                  ],
                  "uv_size": [
                    17,
                    0
                  ]
                },
                "down": {
                  "uv": [
                    38,
                    0
                  ],
                  "uv_size": [
                    -17,
                    0
                  ]
                }
              }
            }
          ]
        },
        {
          "name": "bone2",
          "parent": "grass",
          "pivot": [
            -4,
            -16,
            3
          ],
          "cubes": [
            {
              "origin": [
                -13,
                -16,
                4
              ],
              "size": [
                17,
                16,
                0
              ],
              "pivot": [
                -4,
                -16,
                3
              ],
              "rotation": [
                15,
                135,
                0
              ],
              "uv": {
                "north": {
                  "uv": [
                    0,
                    8
                  ],
                  "uv_size": [
                    8,
                    8
                  ]
                },
                "east": {
                  "uv": [
                    4,
                    0
                  ],
                  "uv_size": [
                    0,
                    16
                  ]
                },
                "south": {
                  "uv": [
                    8,
                    0
                  ],
                  "uv_size": [
                    -8,
                    8
                  ]
                },
                "west": {
                  "uv": [
                    21,
                    0
                  ],
                  "uv_size": [
                    0,
                    16
                  ]
                },
                "up": {
                  "uv": [
                    4,
                    0
                  ],
                  "uv_size": [
                    17,
                    0
                  ]
                },
                "down": {
                  "uv": [
                    38,
                    0
                  ],
                  "uv_size": [
                    -17,
                    0
                  ]
                }
              }
            }
          ]
        },
        {
          "name": "bone3",
          "parent": "grass",
          "pivot": [
            3,
            -16,
            3
          ],
          "cubes": [
            {
              "origin": [
                -6,
                -16,
                4
              ],
              "size": [
                17,
                16,
                0
              ],
              "pivot": [
                3,
                -16,
                3
              ],
              "rotation": [
                -15,
                45,
                0
              ],
              "uv": {
                "north": {
                  "uv": [
                    8,
                    0
                  ],
                  "uv_size": [
                    -8,
                    8
                  ]
                },
                "east": {
                  "uv": [
                    4,
                    0
                  ],
                  "uv_size": [
                    0,
                    16
                  ]
                },
                "south": {
                  "uv": [
                    0,
                    8
                  ],
                  "uv_size": [
                    8,
                    8
                  ]
                },
                "west": {
                  "uv": [
                    21,
                    0
                  ],
                  "uv_size": [
                    0,
                    16
                  ]
                },
                "up": {
                  "uv": [
                    4,
                    0
                  ],
                  "uv_size": [
                    17,
                    0
                  ]
                },
                "down": {
                  "uv": [
                    38,
                    0
                  ],
                  "uv_size": [
                    -17,
                    0
                  ]
                }
              }
            }
          ]
        },
        {
          "name": "bone4",
          "parent": "grass",
          "pivot": [
            3,
            -16,
            -3
          ],
          "cubes": [
            {
              "origin": [
                -6,
                -16,
                -2
              ],
              "size": [
                17,
                16,
                0
              ],
              "pivot": [
                3,
                -16,
                -3
              ],
              "rotation": [
                -15,
                135,
                0
              ],
              "uv": {
                "north": {
                  "uv": [
                    8,
                    0
                  ],
                  "uv_size": [
                    -8,
                    8
                  ]
                },
                "east": {
                  "uv": [
                    4,
                    0
                  ],
                  "uv_size": [
                    0,
                    16
                  ]
                },
                "south": {
                  "uv": [
                    0,
                    8
                  ],
                  "uv_size": [
                    8,
                    8
                  ]
                },
                "west": {
                  "uv": [
                    21,
                    0
                  ],
                  "uv_size": [
                    0,
                    16
                  ]
                },
                "up": {
                  "uv": [
                    4,
                    0
                  ],
                  "uv_size": [
                    17,
                    0
                  ]
                },
                "down": {
                  "uv": [
                    38,
                    0
                  ],
                  "uv_size": [
                    -17,
                    0
                  ]
                }
              }
            }
          ]
        },
        {
          "name": "bone5",
          "parent": "grass",
          "pivot": [
            0,
            -14,
            0
          ],
          "cubes": [
            {
              "origin": [
                0,
                -14,
                -6
              ],
              "size": [
                0,
                16,
                12
              ],
              "uv": {
                "north": {
                  "uv": [
                    0,
                    0
                  ],
                  "uv_size": [
                    0,
                    8
                  ]
                },
                "east": {
                  "uv": [
                    8,
                    0
                  ],
                  "uv_size": [
                    8,
                    8
                  ]
                },
                "south": {
                  "uv": [
                    0,
                    0
                  ],
                  "uv_size": [
                    0,
                    8
                  ]
                },
                "west": {
                  "uv": [
                    16,
                    8
                  ],
                  "uv_size": [
                    -8,
                    8
                  ]
                },
                "up": {
                  "uv": [
                    0,
                    7
                  ],
                  "uv_size": [
                    0,
                    -7
                  ]
                },
                "down": {
                  "uv": [
                    0,
                    7
                  ],
                  "uv_size": [
                    0,
                    -7
                  ]
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

### `Swords_R/models/entity/mermaid_player.geo.json`

- SHA-256 исходного файла: `848d40095db8ef5fd6a3e8784c4b1b77e878619ecbf4d64caa6921e56a3575a4`.

```json
{
  "format_version": "1.12.0",
  "minecraft:geometry": [
    {
      "description": {
        "identifier": "geometry.mermaid_player.tail",
        "texture_width": 64,
        "texture_height": 64,
        "visible_bounds_width": 3,
        "visible_bounds_height": 3,
        "visible_bounds_offset": [
          0,
          1.5,
          0
        ]
      },
      "bones": [
        {
          "name": "root",
          "pivot": [
            0,
            0,
            0
          ]
        },
        {
          "name": "waist",
          "parent": "root",
          "pivot": [
            0,
            12,
            0
          ]
        },
        {
          "name": "body",
          "parent": "waist",
          "pivot": [
            0,
            24,
            0
          ],
          "cubes": [
            {
              "origin": [
                -4,
                12,
                -2
              ],
              "size": [
                8,
                12,
                4
              ],
              "uv": {
                "north": {
                  "uv": [
                    0,
                    0
                  ],
                  "uv_size": [
                    8,
                    12
                  ]
                },
                "east": {
                  "uv": [
                    18,
                    0
                  ],
                  "uv_size": [
                    4,
                    12
                  ]
                },
                "south": {
                  "uv": [
                    9,
                    0
                  ],
                  "uv_size": [
                    8,
                    12
                  ]
                },
                "west": {
                  "uv": [
                    18,
                    13
                  ],
                  "uv_size": [
                    4,
                    12
                  ]
                },
                "up": {
                  "uv": [
                    56,
                    60
                  ],
                  "uv_size": [
                    8,
                    4
                  ]
                },
                "down": {
                  "uv": [
                    56,
                    64
                  ],
                  "uv_size": [
                    8,
                    -4
                  ]
                }
              }
            }
          ]
        },
        {
          "name": "jacket",
          "parent": "body",
          "pivot": [
            0,
            24,
            0
          ],
          "cubes": [
            {
              "origin": [
                -4,
                12,
                -2
              ],
              "size": [
                8,
                12,
                4
              ],
              "inflate": 0.25,
              "uv": {
                "north": {
                  "uv": [
                    0,
                    13
                  ],
                  "uv_size": [
                    8,
                    12
                  ]
                },
                "east": {
                  "uv": [
                    23,
                    0
                  ],
                  "uv_size": [
                    4,
                    12
                  ]
                },
                "south": {
                  "uv": [
                    9,
                    13
                  ],
                  "uv_size": [
                    8,
                    12
                  ]
                },
                "west": {
                  "uv": [
                    23,
                    13
                  ],
                  "uv_size": [
                    4,
                    12
                  ]
                },
                "up": {
                  "uv": [
                    28,
                    0
                  ],
                  "uv_size": [
                    8,
                    4
                  ]
                },
                "down": {
                  "uv": [
                    28,
                    9
                  ],
                  "uv_size": [
                    8,
                    -4
                  ]
                }
              }
            }
          ]
        },
        {
          "name": "Mermaidtail",
          "parent": "jacket",
          "pivot": [
            0,
            9.63397,
            0.90289
          ],
          "rotation": [
            -24,
            0,
            0
          ]
        },
        {
          "name": "Mermaidtail7",
          "parent": "Mermaidtail",
          "pivot": [
            0,
            9.63397,
            0.90289
          ],
          "cubes": [
            {
              "origin": [
                -4.24,
                7.77397,
                -1.41711
              ],
              "size": [
                8.48,
                4.72,
                3.24
              ],
              "inflate": 0.25,
              "pivot": [
                0,
                9.63397,
                0.90289
              ],
              "rotation": [
                35,
                0,
                0
              ],
              "uv": {
                "north": {
                  "uv": [
                    0,
                    26
                  ],
                  "uv_size": [
                    8,
                    5
                  ]
                },
                "east": {
                  "uv": [
                    14,
                    32
                  ],
                  "uv_size": [
                    3,
                    5
                  ]
                },
                "south": {
                  "uv": [
                    9,
                    26
                  ],
                  "uv_size": [
                    8,
                    5
                  ]
                },
                "west": {
                  "uv": [
                    18,
                    35
                  ],
                  "uv_size": [
                    3,
                    5
                  ]
                },
                "up": {
                  "uv": [
                    18,
                    31
                  ],
                  "uv_size": [
                    8,
                    3
                  ]
                },
                "down": {
                  "uv": [
                    27,
                    34
                  ],
                  "uv_size": [
                    8,
                    -3
                  ]
                }
              }
            }
          ]
        },
        {
          "name": "Mermaidtail3",
          "parent": "Mermaidtail",
          "pivot": [
            0,
            6.63397,
            3.90289
          ],
          "cubes": [
            {
              "origin": [
                -3.24,
                6.87397,
                1.28289
              ],
              "size": [
                6.48,
                1.72,
                2.94
              ],
              "inflate": 0.25,
              "pivot": [
                0,
                6.63397,
                3.90289
              ],
              "rotation": [
                40,
                0,
                0
              ],
              "uv": {
                "north": {
                  "uv": [
                    32,
                    35
                  ],
                  "uv_size": [
                    6,
                    2
                  ]
                },
                "east": {
                  "uv": [
                    37,
                    6
                  ],
                  "uv_size": [
                    3,
                    2
                  ]
                },
                "south": {
                  "uv": [
                    0,
                    36
                  ],
                  "uv_size": [
                    6,
                    2
                  ]
                },
                "west": {
                  "uv": [
                    37,
                    18
                  ],
                  "uv_size": [
                    3,
                    2
                  ]
                },
                "up": {
                  "uv": [
                    0,
                    32
                  ],
                  "uv_size": [
                    6,
                    3
                  ]
                },
                "down": {
                  "uv": [
                    7,
                    35
                  ],
                  "uv_size": [
                    6,
                    -3
                  ]
                }
              }
            }
          ]
        },
        {
          "name": "Mermaidtail2",
          "parent": "Mermaidtail",
          "pivot": [
            0,
            6.63397,
            3.90289
          ],
          "cubes": [
            {
              "origin": [
                -2.24,
                4.77397,
                1.38289
              ],
              "size": [
                4.48,
                1.72,
                2.94
              ],
              "inflate": 0.25,
              "pivot": [
                0,
                6.63397,
                3.90289
              ],
              "rotation": [
                45,
                0,
                0
              ],
              "uv": {
                "north": {
                  "uv": [
                    7,
                    36
                  ],
                  "uv_size": [
                    4,
                    2
                  ]
                },
                "east": {
                  "uv": [
                    37,
                    0
                  ],
                  "uv_size": [
                    3,
                    2
                  ]
                },
                "south": {
                  "uv": [
                    36,
                    26
                  ],
                  "uv_size": [
                    4,
                    2
                  ]
                },
                "west": {
                  "uv": [
                    37,
                    3
                  ],
                  "uv_size": [
                    3,
                    2
                  ]
                },
                "up": {
                  "uv": [
                    22,
                    35
                  ],
                  "uv_size": [
                    4,
                    3
                  ]
                },
                "down": {
                  "uv": [
                    27,
                    38
                  ],
                  "uv_size": [
                    4,
                    -3
                  ]
                }
              }
            }
          ]
        },
        {
          "name": "Mermaidtail4",
          "parent": "Mermaidtail",
          "pivot": [
            0,
            3.63397,
            6.90289
          ],
          "cubes": [
            {
              "origin": [
                -1.24,
                3.77397,
                5.78289
              ],
              "size": [
                2.48,
                2.72,
                1.24
              ],
              "inflate": 0.25,
              "pivot": [
                0,
                3.63397,
                6.90289
              ],
              "rotation": [
                55,
                0,
                0
              ],
              "uv": {
                "north": {
                  "uv": [
                    37,
                    21
                  ],
                  "uv_size": [
                    2,
                    3
                  ]
                },
                "east": {
                  "uv": [
                    15,
                    38
                  ],
                  "uv_size": [
                    1,
                    3
                  ]
                },
                "south": {
                  "uv": [
                    12,
                    38
                  ],
                  "uv_size": [
                    2,
                    3
                  ]
                },
                "west": {
                  "uv": [
                    32,
                    38
                  ],
                  "uv_size": [
                    1,
                    3
                  ]
                },
                "up": {
                  "uv": [
                    36,
                    33
                  ],
                  "uv_size": [
                    2,
                    1
                  ]
                },
                "down": {
                  "uv": [
                    38,
                    39
                  ],
                  "uv_size": [
                    2,
                    -1
                  ]
                }
              }
            }
          ]
        },
        {
          "name": "Mermaidtail5",
          "parent": "Mermaidtail",
          "pivot": [
            0,
            3.63397,
            6.90289
          ],
          "cubes": [
            {
              "origin": [
                -4.24,
                1.77397,
                6.28289
              ],
              "size": [
                8.48,
                2.72,
                0.14
              ],
              "inflate": 0.25,
              "pivot": [
                0,
                3.63397,
                6.90289
              ],
              "rotation": [
                79,
                0,
                0
              ],
              "uv": {
                "north": {
                  "uv": [
                    28,
                    18
                  ],
                  "uv_size": [
                    8,
                    3
                  ]
                },
                "east": {
                  "uv": [
                    34,
                    38
                  ],
                  "uv_size": [
                    1,
                    3
                  ]
                },
                "south": {
                  "uv": [
                    28,
                    22
                  ],
                  "uv_size": [
                    8,
                    3
                  ]
                },
                "west": {
                  "uv": [
                    36,
                    38
                  ],
                  "uv_size": [
                    1,
                    3
                  ]
                },
                "up": {
                  "uv": [
                    36,
                    29
                  ],
                  "uv_size": [
                    8,
                    1
                  ]
                },
                "down": {
                  "uv": [
                    36,
                    32
                  ],
                  "uv_size": [
                    8,
                    -1
                  ]
                }
              }
            }
          ]
        },
        {
          "name": "Mermaidtail6",
          "parent": "Mermaidtail",
          "pivot": [
            0,
            3.63397,
            6.90289
          ],
          "cubes": [
            {
              "origin": [
                -5.24,
                -0.62603,
                5.72289
              ],
              "size": [
                10.48,
                2.72,
                0
              ],
              "inflate": 0.25,
              "pivot": [
                0,
                3.63397,
                6.90289
              ],
              "rotation": [
                100,
                0,
                0
              ],
              "uv": {
                "north": {
                  "uv": [
                    28,
                    10
                  ],
                  "uv_size": [
                    10,
                    3
                  ]
                },
                "east": {
                  "uv": [
                    20,
                    27
                  ],
                  "uv_size": [
                    1,
                    3
                  ]
                },
                "south": {
                  "uv": [
                    28,
                    14
                  ],
                  "uv_size": [
                    10,
                    3
                  ]
                },
                "west": {
                  "uv": [
                    18,
                    27
                  ],
                  "uv_size": [
                    1,
                    3
                  ]
                },
                "up": {
                  "uv": [
                    25,
                    28
                  ],
                  "uv_size": [
                    10,
                    -1
                  ]
                },
                "down": {
                  "uv": [
                    25,
                    30
                  ],
                  "uv_size": [
                    10,
                    -1
                  ]
                }
              }
            }
          ]
        },
        {
          "name": "cape",
          "parent": "body",
          "pivot": [
            0,
            24,
            -3
          ]
        },
        {
          "name": "rightLeg",
          "parent": "root",
          "pivot": [
            -1.9,
            12,
            0
          ],
          "cubes": [
            {
              "origin": [
                0.1,
                12,
                2
              ],
              "size": [
                0,
                0,
                0
              ],
              "uv": {
                "north": {
                  "uv": [
                    12,
                    36
                  ],
                  "uv_size": [
                    0,
                    0
                  ]
                },
                "east": {
                  "uv": [
                    13,
                    36
                  ],
                  "uv_size": [
                    0,
                    0
                  ]
                },
                "south": {
                  "uv": [
                    12,
                    37
                  ],
                  "uv_size": [
                    0,
                    0
                  ]
                },
                "west": {
                  "uv": [
                    13,
                    37
                  ],
                  "uv_size": [
                    0,
                    0
                  ]
                },
                "up": {
                  "uv": [
                    1,
                    39
                  ],
                  "uv_size": [
                    0,
                    0
                  ]
                },
                "down": {
                  "uv": [
                    2,
                    39
                  ],
                  "uv_size": [
                    0,
                    0
                  ]
                }
              }
            }
          ]
        },
        {
          "name": "rightPants",
          "parent": "rightLeg",
          "pivot": [
            -1.9,
            12,
            0
          ],
          "cubes": [
            {
              "origin": [
                0.1,
                12,
                2
              ],
              "size": [
                0,
                0,
                0
              ],
              "inflate": 0.25,
              "uv": {
                "north": {
                  "uv": [
                    3,
                    39
                  ],
                  "uv_size": [
                    0,
                    0
                  ]
                },
                "east": {
                  "uv": [
                    4,
                    39
                  ],
                  "uv_size": [
                    0,
                    0
                  ]
                },
                "south": {
                  "uv": [
                    5,
                    39
                  ],
                  "uv_size": [
                    0,
                    0
                  ]
                },
                "west": {
                  "uv": [
                    6,
                    39
                  ],
                  "uv_size": [
                    0,
                    0
                  ]
                },
                "up": {
                  "uv": [
                    7,
                    39
                  ],
                  "uv_size": [
                    0,
                    0
                  ]
                },
                "down": {
                  "uv": [
                    8,
                    39
                  ],
                  "uv_size": [
                    0,
                    0
                  ]
                }
              }
            }
          ]
        },
        {
          "name": "leftLeg",
          "parent": "root",
          "pivot": [
            1.9,
            12,
            0
          ],
          "cubes": [
            {
              "origin": [
                -0.1,
                12,
                2
              ],
              "size": [
                0,
                0,
                0
              ],
              "uv": {
                "north": {
                  "uv": [
                    9,
                    39
                  ],
                  "uv_size": [
                    0,
                    0
                  ]
                },
                "east": {
                  "uv": [
                    10,
                    39
                  ],
                  "uv_size": [
                    0,
                    0
                  ]
                },
                "south": {
                  "uv": [
                    39,
                    10
                  ],
                  "uv_size": [
                    0,
                    0
                  ]
                },
                "west": {
                  "uv": [
                    11,
                    39
                  ],
                  "uv_size": [
                    0,
                    0
                  ]
                },
                "up": {
                  "uv": [
                    39,
                    11
                  ],
                  "uv_size": [
                    0,
                    0
                  ]
                },
                "down": {
                  "uv": [
                    39,
                    12
                  ],
                  "uv_size": [
                    0,
                    0
                  ]
                }
              }
            }
          ]
        },
        {
          "name": "leftPants",
          "parent": "leftLeg",
          "pivot": [
            1.9,
            12,
            0
          ],
          "cubes": [
            {
              "origin": [
                -0.1,
                12,
                2
              ],
              "size": [
                0,
                0,
                0
              ],
              "uv": {
                "north": {
                  "uv": [
                    39,
                    13
                  ],
                  "uv_size": [
                    0,
                    0
                  ]
                },
                "east": {
                  "uv": [
                    39,
                    14
                  ],
                  "uv_size": [
                    0,
                    0
                  ]
                },
                "south": {
                  "uv": [
                    39,
                    15
                  ],
                  "uv_size": [
                    0,
                    0
                  ]
                },
                "west": {
                  "uv": [
                    39,
                    16
                  ],
                  "uv_size": [
                    0,
                    0
                  ]
                },
                "up": {
                  "uv": [
                    39,
                    17
                  ],
                  "uv_size": [
                    0,
                    0
                  ]
                },
                "down": {
                  "uv": [
                    22,
                    39
                  ],
                  "uv_size": [
                    0,
                    0
                  ]
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

### `Swords_R/models/entity/mountable_slime.geo.json`

- SHA-256 исходного файла: `394404abf568b1296b8c783013244d4941f18197bc6b422cc1fad534ef127318`.

```json
{
  "format_version": "1.8.0",
  "geometry.mountable_slime": {
    "texturewidth": 64,
    "textureheight": 32,
    "visible_bounds_width": 5,
    "visible_bounds_height": 2,
    "visible_bounds_offset": [
      0,
      1,
      0
    ],
    "bones": [
      {
        "name": "cube",
        "pivot": [
          0,
          24,
          0
        ],
        "cubes": [
          {
            "origin": [
              -3,
              1,
              -3
            ],
            "size": [
              6,
              6,
              6
            ],
            "uv": [
              0,
              16
            ]
          }
        ]
      },
      {
        "name": "eye0",
        "parent": "cube",
        "pivot": [
          0,
          24,
          0
        ],
        "cubes": [
          {
            "origin": [
              -2.5,
              4.3,
              -4.1
            ],
            "size": [
              1.4,
              2.3,
              2.6
            ],
            "uv": [
              32,
              0
            ]
          }
        ]
      },
      {
        "name": "eye1",
        "parent": "cube",
        "pivot": [
          0,
          24,
          0
        ],
        "cubes": [
          {
            "origin": [
              1.1,
              4.3,
              -4.1
            ],
            "size": [
              1.4,
              2.3,
              2.6
            ],
            "uv": [
              32,
              4
            ]
          }
        ]
      },
      {
        "name": "mouth",
        "parent": "cube",
        "pivot": [
          0,
          24,
          0
        ],
        "cubes": [
          {
            "origin": [
              0,
              2,
              -3.5
            ],
            "size": [
              1,
              1,
              1
            ],
            "uv": [
              32,
              8
            ]
          }
        ]
      }
    ]
  }
}
```

### `Swords_R/models/entity/player_ghost.geo.json`

- SHA-256 исходного файла: `b6d667edbe2b7cfdfa8e77d487786646367580af3955076d866691301e250eec`.

```json
{
  "format_version": "1.12.0",
  "minecraft:geometry": [
    {
      "description": {
        "identifier": "geometry.player_ghost",
        "texture_width": 64,
        "texture_height": 64,
        "visible_bounds_width": 3,
        "visible_bounds_height": 4.5,
        "visible_bounds_offset": [
          0,
          0.75,
          0
        ]
      },
      "bones": [
        {
          "name": "root",
          "pivot": [
            0,
            0,
            0
          ]
        },
        {
          "name": "waist",
          "parent": "root",
          "pivot": [
            0,
            12,
            0
          ]
        },
        {
          "name": "body",
          "parent": "waist",
          "pivot": [
            0,
            24,
            0
          ],
          "cubes": [
            {
              "origin": [
                -4,
                12,
                -2
              ],
              "size": [
                8,
                12,
                4
              ],
              "uv": [
                16,
                16
              ]
            }
          ]
        },
        {
          "name": "head",
          "parent": "body",
          "pivot": [
            0,
            24,
            0
          ]
        },
        {
          "name": "hat",
          "parent": "head",
          "pivot": [
            0,
            24,
            0
          ]
        },
        {
          "name": "ghost_hat",
          "parent": "hat",
          "pivot": [
            0,
            0,
            0
          ],
          "cubes": [
            {
              "origin": [
                -4.24,
                24.21,
                -4.24
              ],
              "size": [
                8.48,
                8.48,
                8.48
              ],
              "inflate": 0.5,
              "uv": [
                32,
                0
              ]
            }
          ]
        },
        {
          "name": "cape",
          "parent": "body",
          "pivot": [
            0,
            24,
            3
          ]
        },
        {
          "name": "leftArm",
          "parent": "body",
          "pivot": [
            5,
            22,
            0
          ]
        },
        {
          "name": "ghost_leftArm",
          "parent": "leftArm",
          "pivot": [
            0,
            0,
            0
          ],
          "cubes": [
            {
              "origin": [
                4.24,
                11.49,
                -2.12
              ],
              "size": [
                4.24,
                12.72,
                4.24
              ],
              "inflate": 0.25,
              "uv": [
                48,
                48
              ]
            }
          ]
        },
        {
          "name": "leftSleeve",
          "parent": "leftArm",
          "pivot": [
            5,
            22,
            0
          ],
          "cubes": [
            {
              "origin": [
                4,
                12,
                -2
              ],
              "size": [
                4,
                12,
                4
              ],
              "inflate": 0.25,
              "uv": [
                48,
                48
              ]
            }
          ]
        },
        {
          "name": "leftItem",
          "parent": "leftArm",
          "pivot": [
            6,
            15,
            1
          ]
        },
        {
          "name": "rightArm",
          "parent": "body",
          "pivot": [
            -5,
            22,
            0
          ],
          "cubes": [
            {
              "origin": [
                -8,
                12,
                -2
              ],
              "size": [
                4,
                12,
                4
              ],
              "uv": [
                40,
                16
              ]
            }
          ]
        },
        {
          "name": "ghost_rightArm",
          "parent": "rightArm",
          "pivot": [
            -5,
            22,
            0
          ],
          "cubes": [
            {
              "origin": [
                -8.48,
                11.49,
                -2.12
              ],
              "size": [
                4.24,
                12.72,
                4.24
              ],
              "inflate": 0.25,
              "uv": [
                40,
                32
              ]
            }
          ]
        },
        {
          "name": "rightSleeve",
          "parent": "rightArm",
          "pivot": [
            -5,
            22,
            0
          ],
          "cubes": [
            {
              "origin": [
                -8,
                12,
                -2
              ],
              "size": [
                4,
                12,
                4
              ],
              "inflate": 0.25,
              "uv": [
                40,
                32
              ]
            }
          ]
        },
        {
          "name": "rightItem",
          "parent": "rightArm",
          "pivot": [
            -6,
            15,
            1
          ],
          "locators": {
            "lead_hold": [
              -6,
              15,
              1
            ]
          }
        },
        {
          "name": "jacket",
          "parent": "body",
          "pivot": [
            0,
            24,
            0
          ]
        },
        {
          "name": "ghost_jacket",
          "parent": "jacket",
          "pivot": [
            0,
            0,
            0
          ],
          "cubes": [
            {
              "origin": [
                -4.24,
                11.49,
                -2.12
              ],
              "size": [
                8.48,
                12.72,
                4.24
              ],
              "inflate": 0.25,
              "uv": [
                16,
                32
              ]
            }
          ]
        },
        {
          "name": "ghost_cola",
          "parent": "ghost_jacket",
          "pivot": [
            0,
            10.23397,
            1.60289
          ],
          "cubes": [
            {
              "origin": [
                -2.24,
                5.37397,
                2.48289
              ],
              "size": [
                4.48,
                4.72,
                3.24
              ],
              "inflate": 0.25,
              "pivot": [
                0,
                7.23397,
                4.60289
              ],
              "rotation": [
                55,
                0,
                0
              ],
              "uv": [
                16,
                32
              ]
            },
            {
              "origin": [
                -1.24,
                4.37397,
                7.48289
              ],
              "size": [
                2.48,
                2.72,
                1.24
              ],
              "inflate": 0.25,
              "pivot": [
                0,
                4.23397,
                7.60289
              ],
              "rotation": [
                55,
                0,
                0
              ],
              "uv": [
                16,
                32
              ]
            },
            {
              "origin": [
                -4.24,
                8.37397,
                -0.51711
              ],
              "size": [
                8.48,
                4.72,
                3.24
              ],
              "inflate": 0.25,
              "pivot": [
                0,
                10.23397,
                1.60289
              ],
              "rotation": [
                40,
                0,
                0
              ],
              "uv": [
                16,
                32
              ]
            }
          ]
        },
        {
          "name": "leftLeg",
          "parent": "root",
          "pivot": [
            1.9,
            12,
            0
          ],
          "cubes": [
            {
              "origin": [
                -0.1,
                12,
                -2
              ],
              "size": [
                4,
                0,
                4
              ],
              "uv": [
                16,
                48
              ]
            }
          ]
        },
        {
          "name": "leftPants",
          "parent": "leftLeg",
          "pivot": [
            1.9,
            12,
            0
          ],
          "cubes": [
            {
              "origin": [
                -0.1,
                12,
                -2
              ],
              "size": [
                4,
                0,
                4
              ],
              "inflate": 0.25,
              "uv": [
                0,
                48
              ]
            }
          ]
        },
        {
          "name": "rightLeg",
          "parent": "root",
          "pivot": [
            -1.9,
            12,
            0
          ],
          "cubes": [
            {
              "origin": [
                -3.9,
                12,
                -2
              ],
              "size": [
                4,
                0,
                4
              ],
              "uv": [
                0,
                16
              ]
            }
          ]
        },
        {
          "name": "rightPants",
          "parent": "rightLeg",
          "pivot": [
            -1.9,
            12,
            0
          ],
          "cubes": [
            {
              "origin": [
                -3.9,
                12,
                -2
              ],
              "size": [
                4,
                0,
                4
              ],
              "inflate": 0.25,
              "uv": [
                0,
                32
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

### `Swords_R/models/entity/pumpkin_projectile.geo.json`

- SHA-256 исходного файла: `7e6dcb41e60c6618df175b2b690547bfde14c543d2c55df892367481f422e756`.

```json
{
  "format_version": "1.12.0",
  "minecraft:geometry": [
    {
      "description": {
        "identifier": "geometry.pumpkin_projectile",
        "texture_width": 48,
        "texture_height": 48,
        "visible_bounds_width": 3,
        "visible_bounds_height": 3,
        "visible_bounds_offset": [
          0,
          0.5,
          0
        ]
      },
      "bones": [
        {
          "name": "head",
          "pivot": [
            0,
            0,
            0
          ],
          "cubes": [
            {
              "origin": [
                -4,
                4,
                -4
              ],
              "size": [
                8,
                8,
                8
              ],
              "uv": {
                "north": {
                  "uv": [
                    0,
                    0
                  ],
                  "uv_size": [
                    16,
                    16
                  ]
                },
                "east": {
                  "uv": [
                    0,
                    16
                  ],
                  "uv_size": [
                    16,
                    16
                  ]
                },
                "south": {
                  "uv": [
                    16,
                    0
                  ],
                  "uv_size": [
                    16,
                    16
                  ]
                },
                "west": {
                  "uv": [
                    16,
                    16
                  ],
                  "uv_size": [
                    16,
                    16
                  ]
                },
                "up": {
                  "uv": [
                    0,
                    32
                  ],
                  "uv_size": [
                    16,
                    16
                  ]
                },
                "down": {
                  "uv": [
                    32,
                    16
                  ],
                  "uv_size": [
                    16,
                    -16
                  ]
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

### `Swords_R/models/entity/shulker_shield.geo.json`

- SHA-256 исходного файла: `84e84885fd289da6f71ec46123cb551ca7fa6ecdbc657c6b3d55a94e19545633`.

```json
{
  "format_version": "1.8.0",
  "geometry.shulker_shield": {
    "texturewidth": 64,
    "textureheight": 64,
    "visible_bounds_width": 3,
    "visible_bounds_height": 3,
    "visible_bounds_offset": [
      0,
      0,
      0
    ],
    "bones": [
      {
        "name": "shulker_shield",
        "pivot": [
          0,
          0,
          0
        ]
      },
      {
        "name": "base",
        "parent": "shulker_shield",
        "pivot": [
          0,
          0,
          0
        ],
        "cubes": [
          {
            "origin": [
              -8,
              0,
              -8
            ],
            "size": [
              16,
              8,
              16
            ],
            "uv": [
              0,
              28
            ]
          }
        ]
      },
      {
        "name": "lid",
        "parent": "shulker_shield",
        "pivot": [
          0,
          27,
          0
        ],
        "cubes": [
          {
            "origin": [
              -8,
              21,
              -8
            ],
            "size": [
              16,
              12,
              16
            ],
            "uv": [
              0,
              0
            ]
          }
        ]
      }
    ]
  }
}
```

### `Swords_R/models/entity/slime_king_armor.geo.json`

- SHA-256 исходного файла: `db0d4edd317f0acad14c4ba88c4680cc152a13ef982fa47b59a6ece733c1ef6b`.

```json
{
  "format_version": "1.12.0",
  "minecraft:geometry": [
    {
      "description": {
        "identifier": "geometry.slime_king.armor",
        "texture_width": 64,
        "texture_height": 32,
        "visible_bounds_width": 2,
        "visible_bounds_height": 1,
        "visible_bounds_offset": [
          0,
          0,
          0
        ]
      },
      "bones": [
        {
          "name": "cube",
          "pivot": [
            0,
            24,
            0
          ],
          "cubes": [
            {
              "origin": [
                -4,
                0,
                -4
              ],
              "size": [
                8,
                8,
                8
              ],
              "uv": {
                "north": {
                  "uv": [
                    8,
                    8
                  ],
                  "uv_size": [
                    8,
                    8
                  ]
                },
                "east": {
                  "uv": [
                    0,
                    8
                  ],
                  "uv_size": [
                    8,
                    8
                  ]
                },
                "south": {
                  "uv": [
                    24,
                    8
                  ],
                  "uv_size": [
                    8,
                    8
                  ]
                },
                "west": {
                  "uv": [
                    16,
                    8
                  ],
                  "uv_size": [
                    8,
                    8
                  ]
                },
                "up": {
                  "uv": [
                    8,
                    0
                  ],
                  "uv_size": [
                    8,
                    8
                  ]
                },
                "down": {
                  "uv": [
                    24,
                    8
                  ],
                  "uv_size": [
                    -8,
                    -8
                  ]
                }
              }
            }
          ]
        },
        {
          "name": "eye0",
          "parent": "cube",
          "pivot": [
            0,
            24,
            0
          ],
          "cubes": [
            {
              "origin": [
                -3.3,
                4,
                -3.5
              ],
              "size": [
                2,
                2,
                2
              ],
              "uv": {
                "north": {
                  "uv": [
                    34,
                    2
                  ],
                  "uv_size": [
                    2,
                    2
                  ]
                },
                "east": {
                  "uv": [
                    32,
                    2
                  ],
                  "uv_size": [
                    2,
                    2
                  ]
                },
                "south": {
                  "uv": [
                    38,
                    2
                  ],
                  "uv_size": [
                    2,
                    2
                  ]
                },
                "west": {
                  "uv": [
                    36,
                    2
                  ],
                  "uv_size": [
                    2,
                    2
                  ]
                },
                "up": {
                  "uv": [
                    34,
                    0
                  ],
                  "uv_size": [
                    2,
                    2
                  ]
                },
                "down": {
                  "uv": [
                    38,
                    2
                  ],
                  "uv_size": [
                    -2,
                    -2
                  ]
                }
              }
            }
          ]
        },
        {
          "name": "eye1",
          "parent": "cube",
          "pivot": [
            0,
            24,
            0
          ],
          "cubes": [
            {
              "origin": [
                1.3,
                4,
                -3.5
              ],
              "size": [
                2,
                2,
                2
              ],
              "uv": {
                "north": {
                  "uv": [
                    34,
                    6
                  ],
                  "uv_size": [
                    2,
                    2
                  ]
                },
                "east": {
                  "uv": [
                    32,
                    6
                  ],
                  "uv_size": [
                    2,
                    2
                  ]
                },
                "south": {
                  "uv": [
                    38,
                    6
                  ],
                  "uv_size": [
                    2,
                    2
                  ]
                },
                "west": {
                  "uv": [
                    36,
                    6
                  ],
                  "uv_size": [
                    2,
                    2
                  ]
                },
                "up": {
                  "uv": [
                    34,
                    4
                  ],
                  "uv_size": [
                    2,
                    2
                  ]
                },
                "down": {
                  "uv": [
                    38,
                    6
                  ],
                  "uv_size": [
                    -2,
                    -2
                  ]
                }
              }
            }
          ]
        },
        {
          "name": "mouth",
          "parent": "cube",
          "pivot": [
            0,
            24,
            0
          ],
          "cubes": [
            {
              "origin": [
                0,
                2,
                -3.5
              ],
              "size": [
                1,
                1,
                1
              ],
              "uv": {
                "north": {
                  "uv": [
                    33,
                    9
                  ],
                  "uv_size": [
                    1,
                    1
                  ]
                },
                "east": {
                  "uv": [
                    32,
                    9
                  ],
                  "uv_size": [
                    1,
                    1
                  ]
                },
                "south": {
                  "uv": [
                    35,
                    9
                  ],
                  "uv_size": [
                    1,
                    1
                  ]
                },
                "west": {
                  "uv": [
                    34,
                    9
                  ],
                  "uv_size": [
                    1,
                    1
                  ]
                },
                "up": {
                  "uv": [
                    33,
                    8
                  ],
                  "uv_size": [
                    1,
                    1
                  ]
                },
                "down": {
                  "uv": [
                    35,
                    9
                  ],
                  "uv_size": [
                    -1,
                    -1
                  ]
                }
              }
            }
          ]
        },
        {
          "name": "crown",
          "pivot": [
            0,
            0,
            0
          ],
          "cubes": [
            {
              "origin": [
                -2,
                8,
                -2
              ],
              "size": [
                4,
                2,
                0
              ],
              "uv": {
                "north": {
                  "uv": [
                    36,
                    23
                  ],
                  "uv_size": [
                    4,
                    2
                  ]
                },
                "east": {
                  "uv": [
                    0,
                    0
                  ],
                  "uv_size": [
                    0,
                    2
                  ]
                },
                "south": {
                  "uv": [
                    40,
                    23
                  ],
                  "uv_size": [
                    -4,
                    2
                  ]
                },
                "west": {
                  "uv": [
                    0,
                    0
                  ],
                  "uv_size": [
                    0,
                    2
                  ]
                },
                "up": {
                  "uv": [
                    4,
                    0
                  ],
                  "uv_size": [
                    -4,
                    0
                  ]
                },
                "down": {
                  "uv": [
                    0,
                    0
                  ],
                  "uv_size": [
                    4,
                    0
                  ]
                }
              }
            },
            {
              "origin": [
                -2,
                8,
                2
              ],
              "size": [
                4,
                2,
                0
              ],
              "uv": {
                "north": {
                  "uv": [
                    30,
                    22
                  ],
                  "uv_size": [
                    -4,
                    2
                  ]
                },
                "east": {
                  "uv": [
                    0,
                    0
                  ],
                  "uv_size": [
                    0,
                    2
                  ]
                },
                "south": {
                  "uv": [
                    26,
                    22
                  ],
                  "uv_size": [
                    4,
                    2
                  ]
                },
                "west": {
                  "uv": [
                    0,
                    0
                  ],
                  "uv_size": [
                    0,
                    2
                  ]
                },
                "up": {
                  "uv": [
                    4,
                    0
                  ],
                  "uv_size": [
                    -4,
                    0
                  ]
                },
                "down": {
                  "uv": [
                    0,
                    0
                  ],
                  "uv_size": [
                    4,
                    0
                  ]
                }
              }
            },
            {
              "origin": [
                -3,
                8,
                1
              ],
              "size": [
                4,
                2,
                0
              ],
              "pivot": [
                -2,
                8,
                1
              ],
              "rotation": [
                0,
                90,
                0
              ],
              "uv": {
                "north": {
                  "uv": [
                    26,
                    25
                  ],
                  "uv_size": [
                    4,
                    2
                  ]
                },
                "east": {
                  "uv": [
                    0,
                    0
                  ],
                  "uv_size": [
                    0,
                    2
                  ]
                },
                "south": {
                  "uv": [
                    30,
                    25
                  ],
                  "uv_size": [
                    -4,
                    2
                  ]
                },
                "west": {
                  "uv": [
                    0,
                    0
                  ],
                  "uv_size": [
                    0,
                    2
                  ]
                },
                "up": {
                  "uv": [
                    4,
                    0
                  ],
                  "uv_size": [
                    -4,
                    0
                  ]
                },
                "down": {
                  "uv": [
                    0,
                    0
                  ],
                  "uv_size": [
                    4,
                    0
                  ]
                }
              }
            },
            {
              "origin": [
                1,
                8,
                1
              ],
              "size": [
                4,
                2,
                0
              ],
              "pivot": [
                2,
                8,
                1
              ],
              "rotation": [
                0,
                90,
                0
              ],
              "uv": {
                "north": {
                  "uv": [
                    40,
                    26
                  ],
                  "uv_size": [
                    -4,
                    2
                  ]
                },
                "east": {
                  "uv": [
                    0,
                    0
                  ],
                  "uv_size": [
                    0,
                    2
                  ]
                },
                "south": {
                  "uv": [
                    36,
                    26
                  ],
                  "uv_size": [
                    4,
                    2
                  ]
                },
                "west": {
                  "uv": [
                    0,
                    0
                  ],
                  "uv_size": [
                    0,
                    2
                  ]
                },
                "up": {
                  "uv": [
                    4,
                    0
                  ],
                  "uv_size": [
                    -4,
                    0
                  ]
                },
                "down": {
                  "uv": [
                    0,
                    0
                  ],
                  "uv_size": [
                    4,
                    0
                  ]
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

### `Swords_R/models/entity/ultra_instinct_aura.geo.json`

- SHA-256 исходного файла: `8b2acf9fdf620b0355b114beb5b4c9307e946af271cf6aeea9ce4e81aaec4794`.

```json
{
  "format_version": "1.12.0",
  "minecraft:geometry": [
    {
      "description": {
        "identifier": "geometry.ultra_instinct_aura",
        "texture_width": 64,
        "texture_height": 64,
        "visible_bounds_width": 3,
        "visible_bounds_height": 3,
        "visible_bounds_offset": [
          0,
          0,
          0
        ]
      },
      "bones": [
        {
          "name": "root",
          "pivot": [
            0,
            0,
            0
          ]
        },
        {
          "name": "waist",
          "parent": "root",
          "pivot": [
            0,
            12,
            0
          ]
        },
        {
          "name": "body",
          "parent": "waist",
          "pivot": [
            0,
            24,
            0
          ]
        },
        {
          "name": "head",
          "parent": "body",
          "pivot": [
            0,
            24,
            0
          ]
        },
        {
          "name": "hat",
          "parent": "head",
          "pivot": [
            0,
            24,
            0
          ]
        },
        {
          "name": "hat_aura",
          "parent": "hat",
          "pivot": [
            0,
            0,
            0
          ],
          "cubes": [
            {
              "origin": [
                -4.2432,
                24.50667,
                -4.2432
              ],
              "size": [
                8.4864,
                8.4864,
                8.4864
              ],
              "inflate": 0.5,
              "uv": [
                0,
                0
              ]
            }
          ]
        },
        {
          "name": "cape",
          "parent": "body",
          "pivot": [
            0,
            24,
            3
          ]
        },
        {
          "name": "leftArm",
          "parent": "body",
          "pivot": [
            5,
            22,
            0
          ]
        },
        {
          "name": "leftSleeve",
          "parent": "leftArm",
          "pivot": [
            5,
            22,
            0
          ]
        },
        {
          "name": "leftSleeve_aura",
          "parent": "leftSleeve",
          "pivot": [
            0,
            0,
            0
          ],
          "cubes": [
            {
              "origin": [
                4.2432,
                11.77707,
                -2.1216
              ],
              "size": [
                4.2432,
                12.7296,
                4.2432
              ],
              "inflate": 0.25,
              "uv": [
                32,
                0
              ]
            }
          ]
        },
        {
          "name": "leftItem",
          "parent": "leftArm",
          "pivot": [
            6,
            15,
            1
          ]
        },
        {
          "name": "rightArm",
          "parent": "body",
          "pivot": [
            -5,
            22,
            0
          ]
        },
        {
          "name": "rightSleeve",
          "parent": "rightArm",
          "pivot": [
            -5,
            22,
            0
          ]
        },
        {
          "name": "rightSleeve_aura",
          "parent": "rightSleeve",
          "pivot": [
            0,
            0,
            0
          ],
          "cubes": [
            {
              "origin": [
                -8.4864,
                11.77707,
                -2.1216
              ],
              "size": [
                4.2432,
                12.7296,
                4.2432
              ],
              "inflate": 0.25,
              "uv": [
                36,
                36
              ]
            }
          ]
        },
        {
          "name": "rightItem",
          "parent": "rightArm",
          "pivot": [
            -6,
            15,
            1
          ]
        },
        {
          "name": "jacket",
          "parent": "body",
          "pivot": [
            0,
            24,
            0
          ]
        },
        {
          "name": "jacket_aura",
          "parent": "jacket",
          "pivot": [
            0,
            0,
            0
          ],
          "cubes": [
            {
              "origin": [
                -4.2432,
                11.77707,
                -2.1216
              ],
              "size": [
                8.4864,
                12.7296,
                4.2432
              ],
              "inflate": 0.25,
              "uv": [
                0,
                16
              ]
            }
          ]
        },
        {
          "name": "leftLeg",
          "parent": "root",
          "pivot": [
            1.9,
            12,
            0
          ]
        },
        {
          "name": "leftPants",
          "parent": "leftLeg",
          "pivot": [
            1.9,
            12,
            0
          ]
        },
        {
          "name": "leftPants_aura",
          "parent": "leftPants",
          "pivot": [
            0,
            0,
            0
          ],
          "cubes": [
            {
              "origin": [
                -0.10608,
                -0.95253,
                -2.1216
              ],
              "size": [
                4.2432,
                12.7296,
                4.2432
              ],
              "inflate": 0.25,
              "uv": [
                0,
                32
              ]
            }
          ]
        },
        {
          "name": "rightLeg",
          "parent": "root",
          "pivot": [
            -1.9,
            12,
            0
          ]
        },
        {
          "name": "rightPants",
          "parent": "rightLeg",
          "pivot": [
            -1.9,
            12,
            0
          ]
        },
        {
          "name": "rightPants_aura",
          "parent": "rightPants",
          "pivot": [
            0,
            0,
            0
          ],
          "cubes": [
            {
              "origin": [
                -4.13712,
                -0.95253,
                -2.1216
              ],
              "size": [
                4.2432,
                12.7296,
                4.2432
              ],
              "inflate": 0.25,
              "uv": [
                24,
                24
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

### `Swords_R/models/entity/ultra_instinct_projectile.geo.json`

- SHA-256 исходного файла: `e372473ed661970f1872bc449ff3aa28efeee15a90aee90ef6afa3102e2b0433`.

```json
{
  "format_version": "1.12.0",
  "minecraft:geometry": [
    {
      "description": {
        "identifier": "geometry.ultra_instinct_projectile",
        "texture_width": 64,
        "texture_height": 64,
        "visible_bounds_width": 2,
        "visible_bounds_height": 2,
        "visible_bounds_offset": [
          0,
          0,
          0
        ]
      },
      "bones": [
        {
          "name": "bone",
          "pivot": [
            0,
            0,
            0
          ],
          "cubes": [
            {
              "origin": [
                -8,
                0,
                -8
              ],
              "size": [
                16,
                16,
                16
              ],
              "uv": {
                "north": {
                  "uv": [
                    0,
                    0
                  ],
                  "uv_size": [
                    16,
                    16
                  ]
                },
                "east": {
                  "uv": [
                    0,
                    16
                  ],
                  "uv_size": [
                    16,
                    16
                  ]
                },
                "south": {
                  "uv": [
                    16,
                    16
                  ],
                  "uv_size": [
                    16,
                    16
                  ]
                },
                "west": {
                  "uv": [
                    16,
                    0
                  ],
                  "uv_size": [
                    16,
                    16
                  ]
                },
                "up": {
                  "uv": [
                    0,
                    32
                  ],
                  "uv_size": [
                    16,
                    16
                  ]
                },
                "down": {
                  "uv": [
                    32,
                    48
                  ],
                  "uv_size": [
                    -16,
                    -16
                  ]
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

### `Swords_R/models/entity/wolf_transformation.geo.json`

- SHA-256 исходного файла: `904c513357bcba37b6c3e6f61832ea13b2c2452a83c09559a370eee83f74d73d`.

```json
{
  "format_version": "1.12.0",
  "minecraft:geometry": [
    {
      "description": {
        "identifier": "geometry.wolf_transformation",
        "texture_width": 64,
        "texture_height": 64,
        "visible_bounds_width": 7,
        "visible_bounds_height": 11,
        "visible_bounds_offset": [
          0,
          0,
          0
        ]
      },
      "bones": [
        {
          "name": "root",
          "pivot": [
            0,
            0,
            0
          ]
        },
        {
          "name": "waist",
          "parent": "root",
          "pivot": [
            0,
            12,
            0
          ]
        },
        {
          "name": "body",
          "parent": "waist",
          "pivot": [
            0,
            24,
            0
          ]
        },
        {
          "name": "head",
          "parent": "body",
          "pivot": [
            0,
            24,
            0
          ]
        },
        {
          "name": "hat",
          "parent": "head",
          "pivot": [
            0,
            24,
            0
          ]
        },
        {
          "name": "hat_wolf",
          "parent": "hat",
          "pivot": [
            0,
            0,
            0
          ]
        },
        {
          "name": "head2",
          "parent": "hat_wolf",
          "pivot": [
            0,
            24.10313,
            -2.4
          ],
          "cubes": [
            {
              "origin": [
                -6.23818,
                23.26651,
                -5.79013
              ],
              "size": [
                12.48,
                13.52,
                11.4
              ],
              "uv": {
                "north": {
                  "uv": [
                    4,
                    8
                  ],
                  "uv_size": [
                    6,
                    12
                  ]
                },
                "east": {
                  "uv": [
                    0,
                    8
                  ],
                  "uv_size": [
                    4,
                    12
                  ]
                },
                "south": {
                  "uv": [
                    14,
                    8
                  ],
                  "uv_size": [
                    6,
                    12
                  ]
                },
                "west": {
                  "uv": [
                    10,
                    8
                  ],
                  "uv_size": [
                    4,
                    12
                  ]
                },
                "up": {
                  "uv": [
                    4,
                    0
                  ],
                  "uv_size": [
                    6,
                    8
                  ]
                },
                "down": {
                  "uv": [
                    16,
                    8
                  ],
                  "uv_size": [
                    -6,
                    -8
                  ]
                }
              }
            },
            {
              "origin": [
                -5.71818,
                35.74651,
                -1.63013
              ],
              "size": [
                4.16,
                5.2,
                3.12
              ],
              "uv": {
                "north": {
                  "uv": [
                    20,
                    30
                  ],
                  "uv_size": [
                    2,
                    4
                  ]
                },
                "east": {
                  "uv": [
                    17,
                    28
                  ],
                  "uv_size": [
                    4,
                    2
                  ]
                },
                "south": {
                  "uv": [
                    20,
                    30
                  ],
                  "uv_size": [
                    2,
                    4
                  ]
                },
                "west": {
                  "uv": [
                    17,
                    28
                  ],
                  "uv_size": [
                    4,
                    2
                  ]
                },
                "up": {
                  "uv": [
                    21,
                    30
                  ],
                  "uv_size": [
                    -4,
                    -2
                  ]
                },
                "down": {
                  "uv": [
                    28,
                    18
                  ],
                  "uv_size": [
                    -4,
                    -4
                  ]
                }
              }
            },
            {
              "origin": [
                1.56182,
                35.74651,
                -0.63013
              ],
              "size": [
                4.16,
                5.2,
                3.12
              ],
              "uv": {
                "north": {
                  "uv": [
                    20,
                    30
                  ],
                  "uv_size": [
                    2,
                    4
                  ]
                },
                "east": {
                  "uv": [
                    17,
                    28
                  ],
                  "uv_size": [
                    4,
                    2
                  ]
                },
                "south": {
                  "uv": [
                    20,
                    30
                  ],
                  "uv_size": [
                    2,
                    4
                  ]
                },
                "west": {
                  "uv": [
                    17,
                    28
                  ],
                  "uv_size": [
                    4,
                    2
                  ]
                },
                "up": {
                  "uv": [
                    21,
                    30
                  ],
                  "uv_size": [
                    -4,
                    -2
                  ]
                },
                "down": {
                  "uv": [
                    28,
                    18
                  ],
                  "uv_size": [
                    -4,
                    -4
                  ]
                }
              }
            },
            {
              "origin": [
                -3.11818,
                23.29901,
                -11.03013
              ],
              "size": [
                6.24,
                7.28,
                10.4
              ],
              "uv": {
                "north": {
                  "uv": [
                    4,
                    28
                  ],
                  "uv_size": [
                    3,
                    6
                  ]
                },
                "east": {
                  "uv": [
                    0,
                    28
                  ],
                  "uv_size": [
                    3,
                    6
                  ]
                },
                "south": {
                  "uv": [
                    26,
                    20
                  ],
                  "uv_size": [
                    6,
                    7
                  ]
                },
                "west": {
                  "uv": [
                    8,
                    28
                  ],
                  "uv_size": [
                    3,
                    6
                  ]
                },
                "up": {
                  "uv": [
                    4,
                    20
                  ],
                  "uv_size": [
                    3,
                    8
                  ]
                },
                "down": {
                  "uv": [
                    10,
                    28
                  ],
                  "uv_size": [
                    -3,
                    -8
                  ]
                }
              }
            }
          ],
          "locators": {
            "lead": [
              0.00182,
              29.50651,
              0.40987
            ]
          }
        },
        {
          "name": "cape",
          "parent": "body",
          "pivot": [
            0,
            24,
            3
          ]
        },
        {
          "name": "leftArm",
          "parent": "body",
          "pivot": [
            5,
            22,
            0
          ]
        },
        {
          "name": "leftSleeve",
          "parent": "leftArm",
          "pivot": [
            5,
            22,
            0
          ]
        },
        {
          "name": "leftSleeve_wolf",
          "parent": "leftSleeve",
          "pivot": [
            0,
            0,
            0
          ],
          "cubes": [
            {
              "origin": [
                4.41475,
                10.34991,
                -3.25259
              ],
              "size": [
                5.45293,
                15.27878,
                6.45293
              ],
              "inflate": 0.25,
              "uv": {
                "north": {
                  "uv": [
                    4,
                    40
                  ],
                  "uv_size": [
                    2,
                    16
                  ]
                },
                "east": {
                  "uv": [
                    32,
                    4
                  ],
                  "uv_size": [
                    4,
                    12
                  ]
                },
                "south": {
                  "uv": [
                    5,
                    40
                  ],
                  "uv_size": [
                    2,
                    16
                  ]
                },
                "west": {
                  "uv": [
                    1,
                    40
                  ],
                  "uv_size": [
                    2,
                    16
                  ]
                },
                "up": {
                  "uv": [
                    14,
                    13
                  ],
                  "uv_size": [
                    4,
                    4
                  ]
                },
                "down": {
                  "uv": [
                    44,
                    4
                  ],
                  "uv_size": [
                    -4,
                    -4
                  ]
                }
              }
            }
          ]
        },
        {
          "name": "leftItem",
          "parent": "leftArm",
          "pivot": [
            6,
            15,
            1
          ]
        },
        {
          "name": "rightArm",
          "parent": "body",
          "pivot": [
            -5,
            22,
            0
          ]
        },
        {
          "name": "rightSleeve",
          "parent": "rightArm",
          "pivot": [
            -5,
            22,
            0
          ]
        },
        {
          "name": "rightSleeve_wolf",
          "parent": "rightSleeve",
          "pivot": [
            0,
            0,
            0
          ],
          "cubes": [
            {
              "origin": [
                -9.86404,
                10.34991,
                -3.25259
              ],
              "size": [
                5.45293,
                15.27878,
                6.45293
              ],
              "inflate": 0.25,
              "uv": {
                "north": {
                  "uv": [
                    4,
                    40
                  ],
                  "uv_size": [
                    2,
                    16
                  ]
                },
                "east": {
                  "uv": [
                    5,
                    40
                  ],
                  "uv_size": [
                    2,
                    16
                  ]
                },
                "south": {
                  "uv": [
                    1,
                    40
                  ],
                  "uv_size": [
                    2,
                    16
                  ]
                },
                "west": {
                  "uv": [
                    32,
                    43
                  ],
                  "uv_size": [
                    4,
                    12
                  ]
                },
                "up": {
                  "uv": [
                    16,
                    9
                  ],
                  "uv_size": [
                    4,
                    4
                  ]
                },
                "down": {
                  "uv": [
                    44,
                    4
                  ],
                  "uv_size": [
                    -4,
                    -4
                  ]
                }
              }
            }
          ]
        },
        {
          "name": "rightItem",
          "parent": "rightArm",
          "pivot": [
            -6,
            15,
            1
          ]
        },
        {
          "name": "jacket",
          "parent": "body",
          "pivot": [
            0,
            24,
            0
          ]
        },
        {
          "name": "jacket_wolf",
          "parent": "jacket",
          "pivot": [
            0,
            0,
            0
          ],
          "cubes": [
            {
              "origin": [
                -5.41111,
                11.38991,
                -3.25259
              ],
              "size": [
                10.82586,
                13.23878,
                7.49293
              ],
              "inflate": 0.25,
              "uv": {
                "north": {
                  "uv": [
                    24,
                    40
                  ],
                  "uv_size": [
                    5,
                    18
                  ]
                },
                "east": {
                  "uv": [
                    18,
                    40
                  ],
                  "uv_size": [
                    6,
                    18
                  ]
                },
                "south": {
                  "uv": [
                    37,
                    40
                  ],
                  "uv_size": [
                    5,
                    18
                  ]
                },
                "west": {
                  "uv": [
                    30,
                    40
                  ],
                  "uv_size": [
                    6,
                    18
                  ]
                },
                "up": {
                  "uv": [
                    4,
                    16
                  ],
                  "uv_size": [
                    8,
                    4
                  ]
                },
                "down": {
                  "uv": [
                    20,
                    20
                  ],
                  "uv_size": [
                    -8,
                    -4
                  ]
                }
              }
            }
          ]
        },
        {
          "name": "cola",
          "parent": "jacket_wolf",
          "pivot": [
            0,
            0,
            0
          ],
          "cubes": [
            {
              "origin": [
                -2.07818,
                13.70176,
                1.03387
              ],
              "size": [
                3.12,
                3.12,
                11.44
              ],
              "pivot": [
                0.00182,
                13.70176,
                1.03387
              ],
              "rotation": [
                -40,
                0,
                0
              ],
              "uv": {
                "north": {
                  "uv": [
                    0,
                    0
                  ],
                  "uv_size": [
                    2,
                    2
                  ]
                },
                "east": {
                  "uv": [
                    30,
                    28
                  ],
                  "uv_size": [
                    6,
                    12
                  ]
                },
                "south": {
                  "uv": [
                    32,
                    35
                  ],
                  "uv_size": [
                    4,
                    4
                  ]
                },
                "west": {
                  "uv": [
                    32,
                    28
                  ],
                  "uv_size": [
                    1,
                    12
                  ]
                },
                "up": {
                  "uv": [
                    34,
                    40
                  ],
                  "uv_size": [
                    -2,
                    -12
                  ]
                },
                "down": {
                  "uv": [
                    34,
                    40
                  ],
                  "uv_size": [
                    2,
                    -12
                  ]
                }
              }
            }
          ]
        },
        {
          "name": "leftLeg",
          "parent": "root",
          "pivot": [
            1.9,
            12,
            0
          ]
        },
        {
          "name": "leftPants",
          "parent": "leftLeg",
          "pivot": [
            1.9,
            12,
            0
          ]
        },
        {
          "name": "leftPants_wolf",
          "parent": "leftPants",
          "pivot": [
            0,
            0,
            0
          ],
          "cubes": [
            {
              "origin": [
                -1.10851,
                -1.84887,
                -3.21259
              ],
              "size": [
                6.45293,
                14.23878,
                6.41293
              ],
              "inflate": 0.25,
              "uv": {
                "north": {
                  "uv": [
                    2,
                    40
                  ],
                  "uv_size": [
                    2,
                    16
                  ]
                },
                "east": {
                  "uv": [
                    0,
                    36
                  ],
                  "uv_size": [
                    4,
                    12
                  ]
                },
                "south": {
                  "uv": [
                    3,
                    40
                  ],
                  "uv_size": [
                    2,
                    16
                  ]
                },
                "west": {
                  "uv": [
                    2,
                    40
                  ],
                  "uv_size": [
                    2,
                    16
                  ]
                },
                "up": {
                  "uv": [
                    29,
                    49
                  ],
                  "uv_size": [
                    4,
                    4
                  ]
                },
                "down": {
                  "uv": [
                    44,
                    4
                  ],
                  "uv_size": [
                    -4,
                    -4
                  ]
                }
              }
            }
          ]
        },
        {
          "name": "rightLeg",
          "parent": "root",
          "pivot": [
            -1.9,
            12,
            0
          ]
        },
        {
          "name": "rightPants",
          "parent": "rightLeg",
          "pivot": [
            -1.9,
            12,
            0
          ]
        },
        {
          "name": "rightPants_wolf",
          "parent": "rightPants",
          "pivot": [
            0,
            0,
            0
          ],
          "cubes": [
            {
              "origin": [
                -5.34079,
                -1.84887,
                -3.21259
              ],
              "size": [
                6.45293,
                14.23878,
                6.41293
              ],
              "inflate": 0.25,
              "uv": {
                "north": {
                  "uv": [
                    0,
                    40
                  ],
                  "uv_size": [
                    2,
                    16
                  ]
                },
                "east": {
                  "uv": [
                    0,
                    40
                  ],
                  "uv_size": [
                    2,
                    16
                  ]
                },
                "south": {
                  "uv": [
                    0,
                    40
                  ],
                  "uv_size": [
                    2,
                    16
                  ]
                },
                "west": {
                  "uv": [
                    32,
                    28
                  ],
                  "uv_size": [
                    4,
                    12
                  ]
                },
                "up": {
                  "uv": [
                    31,
                    48
                  ],
                  "uv_size": [
                    4,
                    4
                  ]
                },
                "down": {
                  "uv": [
                    35,
                    4
                  ],
                  "uv_size": [
                    -4,
                    -4
                  ]
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

### `Swords_R/models/entity/wolf_vision.geo.json`

- SHA-256 исходного файла: `9149fe52f3fd5dd1fff6540afd1e0f5e43f0f1ed222ef02c3cca72848e879972`.

```json
{
  "format_version": "1.12.0",
  "minecraft:geometry": [
    {
      "description": {
        "identifier": "geometry.wolf_vision",
        "texture_width": 64,
        "texture_height": 64,
        "visible_bounds_width": 3,
        "visible_bounds_height": 3,
        "visible_bounds_offset": [
          0,
          0,
          0
        ]
      },
      "bones": [
        {
          "name": "root",
          "pivot": [
            0,
            0,
            0
          ]
        },
        {
          "name": "waist",
          "parent": "root",
          "pivot": [
            0,
            12,
            0
          ]
        },
        {
          "name": "body",
          "parent": "waist",
          "pivot": [
            0,
            24,
            0
          ]
        },
        {
          "name": "head",
          "parent": "body",
          "pivot": [
            0,
            24,
            0
          ]
        },
        {
          "name": "hat",
          "parent": "head",
          "pivot": [
            0,
            24,
            0
          ]
        },
        {
          "name": "wolf_vision",
          "parent": "hat",
          "pivot": [
            0,
            0,
            0
          ],
          "cubes": [
            {
              "origin": [
                -9.24,
                19.21,
                -4.24
              ],
              "size": [
                20.48,
                20.48,
                8.48
              ],
              "inflate": 0.5,
              "uv": {
                "north": {
                  "uv": [
                    0,
                    0
                  ],
                  "uv_size": [
                    64,
                    64
                  ]
                },
                "east": {
                  "uv": [
                    0,
                    0
                  ],
                  "uv_size": [
                    64,
                    64
                  ]
                },
                "south": {
                  "uv": [
                    0,
                    0
                  ],
                  "uv_size": [
                    64,
                    64
                  ]
                },
                "west": {
                  "uv": [
                    0,
                    0
                  ],
                  "uv_size": [
                    64,
                    64
                  ]
                },
                "up": {
                  "uv": [
                    64,
                    64
                  ],
                  "uv_size": [
                    -64,
                    -64
                  ]
                },
                "down": {
                  "uv": [
                    0,
                    64
                  ],
                  "uv_size": [
                    64,
                    -64
                  ]
                }
              }
            }
          ]
        },
        {
          "name": "cape",
          "parent": "body",
          "pivot": [
            0,
            24,
            3
          ]
        },
        {
          "name": "leftArm",
          "parent": "body",
          "pivot": [
            5,
            22,
            0
          ]
        },
        {
          "name": "leftSleeve",
          "parent": "leftArm",
          "pivot": [
            5,
            22,
            0
          ]
        },
        {
          "name": "leftItem",
          "parent": "leftArm",
          "pivot": [
            6,
            15,
            1
          ]
        },
        {
          "name": "rightArm",
          "parent": "body",
          "pivot": [
            -5,
            22,
            0
          ]
        },
        {
          "name": "rightSleeve",
          "parent": "rightArm",
          "pivot": [
            -5,
            22,
            0
          ]
        },
        {
          "name": "rightItem",
          "parent": "rightArm",
          "pivot": [
            -6,
            15,
            1
          ],
          "locators": {
            "lead_hold": [
              -6,
              15,
              1
            ]
          }
        },
        {
          "name": "jacket",
          "parent": "body",
          "pivot": [
            0,
            24,
            0
          ]
        },
        {
          "name": "ghost_jacket",
          "parent": "jacket",
          "pivot": [
            0,
            0,
            0
          ]
        },
        {
          "name": "leftLeg",
          "parent": "root",
          "pivot": [
            1.9,
            12,
            0
          ]
        },
        {
          "name": "leftPants",
          "parent": "leftLeg",
          "pivot": [
            1.9,
            12,
            0
          ]
        },
        {
          "name": "rightLeg",
          "parent": "root",
          "pivot": [
            -1.9,
            12,
            0
          ]
        },
        {
          "name": "rightPants",
          "parent": "rightLeg",
          "pivot": [
            -1.9,
            12,
            0
          ]
        }
      ]
    }
  ]
}
```

Текстуры, ID и прочие связи: [граф ресурсов](resource-graph-2.8.14.md) · [медиа и хэши](assets-2.8.14.md) · [локальные анимации](client-animation-index.md).
