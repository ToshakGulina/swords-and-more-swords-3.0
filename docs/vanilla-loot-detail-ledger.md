# Полная сравнительная выписка таблиц добычи 2.x и образцов Mojang

[Метод, результаты и ограничения](manual-vanilla-loot-2.8.md). Идентичные пул-объекты сопоставлены по равенству без учёта положения; пары индексов сохранены. Несовпадающие пулы приведены целиком с исходными индексами. Изменение индекса само по себе не доказывает изменения механики. Отсутствие файла образца — не отсутствие в игре.

## Образец `1.19.40.2`

### `chests/abandoned_mineshaft.json`

SHA-256 add-on `fdce88876b62f2ba9dce2e544df7bc0edad50f3793b357000416d536f0a6fa94`; образца `398d7f6449985594cc2464186773b5720d008024d013e3ea3ae99ed62634a324`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [
      [
        0,
        0
      ],
      [
        2,
        2
      ]
    ],
    "only_addon": [
      {
        "index": 1,
        "value": {
          "entries": [
            {
              "functions": [
                {
                  "count": {
                    "max": 5,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:iron_ingot",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:gold_ingot",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 9,
                    "min": 4
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:redstone",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "data": 4,
                  "function": "set_data"
                },
                {
                  "count": {
                    "max": 9,
                    "min": 4
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:dye",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 2,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:diamond",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 1,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "effect:spider_sword",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 8,
                    "min": 3
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:coal",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:bread",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 4,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:melon_seeds",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 4,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:pumpkin_seeds",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 4,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:beetroot_seeds",
              "type": "item",
              "weight": 10
            }
          ],
          "rolls": {
            "max": 4,
            "min": 2
          }
        }
      }
    ],
    "only_reference": [
      {
        "index": 1,
        "value": {
          "entries": [
            {
              "functions": [
                {
                  "count": {
                    "max": 5,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:iron_ingot",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:gold_ingot",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 9,
                    "min": 4
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:redstone",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "data": 4,
                  "function": "set_data"
                },
                {
                  "count": {
                    "max": 9,
                    "min": 4
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:dye",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 2,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:diamond",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 8,
                    "min": 3
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:coal",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:bread",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 4,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:melon_seeds",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 4,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:pumpkin_seeds",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 4,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:beetroot_seeds",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 6,
                    "min": 3
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:glow_berries",
              "type": "item",
              "weight": 15
            }
          ],
          "rolls": {
            "max": 4,
            "min": 2
          }
        }
      }
    ]
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `chests/buriedtreasure.json`

SHA-256 add-on `be6b5480ced6a762aaa553cd63361848a64c0e4e01ca85d16f1a57aa027ffb7f`; образца `f335246c8ebf7a6d9113b4d9d74e195b8b960f0c6ea3f1da533f0a7ed2873285`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [
      [
        0,
        0
      ]
    ],
    "only_addon": [
      {
        "index": 1,
        "value": {
          "entries": [
            {
              "functions": [
                {
                  "count": {
                    "max": 5,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:prismarine_crystals",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 5,
                    "min": 3
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:iron_ingot",
              "type": "item",
              "weight": 20
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 5,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:gold_ingot",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 2,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:tnt",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:diamond",
              "type": "item",
              "weight": 15
            },
            {
              "name": "minecraft:record_wait",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:record_mellohi",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:name_tag",
              "type": "item",
              "weight": 10
            },
            {
              "name": "effect:sea_sword",
              "type": "item",
              "weight": 15
            },
            {
              "name": "minecraft:chainmail_chestplate",
              "type": "item",
              "weight": 20
            },
            {
              "name": "minecraft:chainmail_helmet",
              "type": "item",
              "weight": 20
            },
            {
              "name": "minecraft:chainmail_leggings",
              "type": "item",
              "weight": 20
            },
            {
              "name": "minecraft:chainmail_boots",
              "type": "item",
              "weight": 20
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 2,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:writable_book",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:lead",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:experience_bottle",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "data": 19,
                  "function": "set_data"
                }
              ],
              "name": "minecraft:potion",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "data": 28,
                  "function": "set_data"
                }
              ],
              "name": "minecraft:potion",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:cake",
              "type": "item",
              "weight": 1
            }
          ],
          "rolls": {
            "max": 12,
            "min": 5
          }
        }
      }
    ],
    "only_reference": [
      {
        "index": 1,
        "value": {
          "entries": [
            {
              "functions": [
                {
                  "count": {
                    "max": 5,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:prismarine_crystals",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 5,
                    "min": 3
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:iron_ingot",
              "type": "item",
              "weight": 20
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 5,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:gold_ingot",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 2,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:tnt",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:diamond",
              "type": "item",
              "weight": 15
            },
            {
              "name": "minecraft:record_wait",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:record_mellohi",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:name_tag",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:chainmail_chestplate",
              "type": "item",
              "weight": 20
            },
            {
              "name": "minecraft:chainmail_helmet",
              "type": "item",
              "weight": 20
            },
            {
              "name": "minecraft:chainmail_leggings",
              "type": "item",
              "weight": 20
            },
            {
              "name": "minecraft:chainmail_boots",
              "type": "item",
              "weight": 20
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 2,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:writable_book",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:lead",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:experience_bottle",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "data": 19,
                  "function": "set_data"
                }
              ],
              "name": "minecraft:potion",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "data": 28,
                  "function": "set_data"
                }
              ],
              "name": "minecraft:potion",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:cake",
              "type": "item",
              "weight": 1
            }
          ],
          "rolls": {
            "max": 12,
            "min": 5
          }
        }
      }
    ]
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `chests/desert_pyramid.json`

SHA-256 add-on `62dbed4c7083aee0863fc97ded6fb00fc6510b69a75721cb9320be41e89b92a3`; образца `8d48b181b84961668041851cabc6d7f804af11c56730559e61a16a80fc1e94e1`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [
      [
        1,
        1
      ]
    ],
    "only_addon": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:diamond",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 5,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:iron_ingot",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 7,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:gold_ingot",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:emerald",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 6,
                    "min": 4
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:bone",
              "type": "item",
              "weight": 25
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:spider_eye",
              "type": "item",
              "weight": 25
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 7,
                    "min": 3
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:rotten_flesh",
              "type": "item",
              "weight": 25
            },
            {
              "name": "minecraft:saddle",
              "type": "item",
              "weight": 20
            },
            {
              "name": "effect:tnt_sword",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:horsearmoriron",
              "type": "item",
              "weight": 15
            },
            {
              "name": "minecraft:horsearmorgold",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:horsearmordiamond",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "function": "enchant_randomly"
                }
              ],
              "name": "minecraft:book",
              "type": "item",
              "weight": 20
            },
            {
              "name": "minecraft:golden_apple",
              "type": "item",
              "weight": 20
            },
            {
              "name": "minecraft:appleEnchanted",
              "type": "item",
              "weight": 2
            },
            {
              "type": "empty",
              "weight": 15
            }
          ],
          "rolls": {
            "max": 4,
            "min": 2
          }
        }
      }
    ],
    "only_reference": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:diamond",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 5,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:iron_ingot",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 7,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:gold_ingot",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:emerald",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 6,
                    "min": 4
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:bone",
              "type": "item",
              "weight": 25
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:spider_eye",
              "type": "item",
              "weight": 25
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 7,
                    "min": 3
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:rotten_flesh",
              "type": "item",
              "weight": 25
            },
            {
              "name": "minecraft:saddle",
              "type": "item",
              "weight": 20
            },
            {
              "name": "minecraft:horsearmoriron",
              "type": "item",
              "weight": 15
            },
            {
              "name": "minecraft:horsearmorgold",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:horsearmordiamond",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "function": "enchant_randomly"
                }
              ],
              "name": "minecraft:book",
              "type": "item",
              "weight": 20
            },
            {
              "name": "minecraft:golden_apple",
              "type": "item",
              "weight": 20
            },
            {
              "name": "minecraft:appleEnchanted",
              "type": "item",
              "weight": 2
            },
            {
              "type": "empty",
              "weight": 15
            }
          ],
          "rolls": {
            "max": 4,
            "min": 2
          }
        }
      }
    ]
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `chests/igloo_chest.json`

SHA-256 add-on `0e4e2cc4f566213b80753df3aa62c16126a98952a6796181c12d6d291815856e`; образца `9b48c4c250b0d3c5889f476a2f109499c5734adfe604d561cade5011e22b93f1`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [
      [
        1,
        1
      ]
    ],
    "only_addon": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:apple",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 4,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:coal",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:gold_nugget",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:stone_axe",
              "type": "item",
              "weight": 2
            },
            {
              "name": "minecraft:rotten_flesh",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:emerald",
              "type": "item",
              "weight": 1
            },
            {
              "name": "effect:ice_sword",
              "type": "item",
              "weight": 1
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 2
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:wheat",
              "type": "item",
              "weight": 10
            }
          ],
          "rolls": {
            "max": 8,
            "min": 2
          }
        }
      }
    ],
    "only_reference": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:apple",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 4,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:coal",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:gold_nugget",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:stone_axe",
              "type": "item",
              "weight": 2
            },
            {
              "name": "minecraft:rotten_flesh",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:emerald",
              "type": "item",
              "weight": 1
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 2
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:wheat",
              "type": "item",
              "weight": 10
            }
          ],
          "rolls": {
            "max": 8,
            "min": 2
          }
        }
      }
    ]
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `chests/jungle_temple.json`

SHA-256 add-on `457065c0f039f716836b183eb083ff9e11bbec9b4391845912f93d20bf01faa0`; образца `52d6b7345a1d89108efecd43c748a4f7c12ee7073a4c2626d3afe6111c1842e6`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [],
    "only_addon": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:diamond",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 5,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:iron_ingot",
              "type": "item",
              "weight": 50
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 7,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:gold_ingot",
              "type": "item",
              "weight": 75
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:emerald",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 6,
                    "min": 4
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:bone",
              "type": "item",
              "weight": 100
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 7,
                    "min": 3
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:rotten_flesh",
              "type": "item",
              "weight": 80
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:bamboo",
              "type": "item",
              "weight": 75
            },
            {
              "name": "minecraft:saddle",
              "type": "item",
              "weight": 15
            },
            {
              "name": "effect:jungle_sword",
              "type": "item",
              "weight": 16
            },
            {
              "name": "minecraft:horsearmoriron",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:horsearmorgold",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:horsearmordiamond",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "function": "enchant_with_levels",
                  "levels": 30,
                  "treasure": true
                }
              ],
              "name": "minecraft:book",
              "type": "item",
              "weight": 6
            }
          ],
          "rolls": {
            "max": 6,
            "min": 2
          }
        }
      }
    ],
    "only_reference": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:diamond",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 5,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:iron_ingot",
              "type": "item",
              "weight": 50
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 7,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:gold_ingot",
              "type": "item",
              "weight": 75
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:emerald",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 6,
                    "min": 4
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:bone",
              "type": "item",
              "weight": 100
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 7,
                    "min": 3
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:rotten_flesh",
              "type": "item",
              "weight": 80
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:bamboo",
              "type": "item",
              "weight": 75
            },
            {
              "name": "minecraft:saddle",
              "type": "item",
              "weight": 15
            },
            {
              "name": "minecraft:horsearmoriron",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:horsearmorgold",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:horsearmordiamond",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "function": "enchant_with_levels",
                  "levels": 30,
                  "treasure": true
                }
              ],
              "name": "minecraft:book",
              "type": "item",
              "weight": 6
            }
          ],
          "rolls": {
            "max": 6,
            "min": 2
          }
        }
      }
    ]
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `chests/pillager_outpost.json`

SHA-256 add-on `0f3d58e0cbef851cb3ab7b4c5d85155a377c0126a66e569b08d6bdddedc1a5ef`; образца `34a58e7d29e586a14523e34fa128ac378dd7d32d1a02c7dd6e4198bc328e3729`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [
      [
        0,
        0
      ],
      [
        1,
        1
      ],
      [
        2,
        2
      ]
    ],
    "only_addon": [
      {
        "index": 3,
        "value": {
          "entries": [
            {
              "name": "minecraft:experience_bottle",
              "type": "item",
              "weight": 7
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 6,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:string",
              "type": "item",
              "weight": 4
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 7,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:arrow",
              "type": "item",
              "weight": 4
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:tripwire_hook",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:iron_ingot",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 1,
                    "min": 0
                  },
                  "function": "set_count"
                }
              ],
              "name": "effect:emerald_sword",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 1,
                    "min": 0
                  },
                  "function": "set_count"
                }
              ],
              "name": "effect:lapis_sword",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "function": "minecraft:enchant_randomly"
                }
              ],
              "name": "minecraft:book",
              "type": "item"
            }
          ],
          "rolls": {
            "max": 3,
            "min": 2
          }
        }
      }
    ],
    "only_reference": [
      {
        "index": 3,
        "value": {
          "entries": [
            {
              "name": "minecraft:experience_bottle",
              "type": "item",
              "weight": 7
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 6,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:string",
              "type": "item",
              "weight": 4
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 7,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:arrow",
              "type": "item",
              "weight": 4
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:tripwire_hook",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:iron_ingot",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "function": "minecraft:enchant_randomly"
                }
              ],
              "name": "minecraft:book",
              "type": "item"
            }
          ],
          "rolls": {
            "max": 3,
            "min": 2
          }
        }
      },
      {
        "index": 4,
        "value": {
          "entries": [
            {
              "functions": [
                {
                  "data": {
                    "max": 3,
                    "min": 0
                  },
                  "function": "set_data"
                }
              ],
              "name": "minecraft:goat_horn",
              "type": "item"
            }
          ],
          "rolls": {
            "max": 1,
            "min": 0
          }
        }
      }
    ]
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `chests/shipwrecksupply.json`

SHA-256 add-on `f4feb668018a8fd2a822370b7a695368c501c1e037d5b50c7413864ea858d1ad`; образца `a4d972cfec06d3b5951ae32f4049c02e378a109e16a3de7990eb648a97a83bef`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [],
    "only_addon": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "functions": [
                {
                  "count": {
                    "max": 12,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:paper",
              "type": "item",
              "weight": 8
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 6,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:potato",
              "type": "item",
              "weight": 7
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 6,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:poisonous_potato",
              "type": "item",
              "weight": 7
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 8,
                    "min": 4
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:carrot",
              "type": "item",
              "weight": 7
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 21,
                    "min": 8
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:wheat",
              "type": "item",
              "weight": 7
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 8,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:coal",
              "type": "item",
              "weight": 6
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 24,
                    "min": 5
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:rotten_flesh",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:bamboo",
              "type": "item",
              "weight": 2
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:pumpkin",
              "type": "item",
              "weight": 2
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 5,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:gunpowder",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 2,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:tnt",
              "type": "item",
              "weight": 1
            },
            {
              "functions": [
                {
                  "function": "enchant_randomly"
                }
              ],
              "name": "minecraft:leather_helmet",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "function": "enchant_randomly"
                }
              ],
              "name": "minecraft:leather_chestplate",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "function": "enchant_randomly"
                }
              ],
              "name": "minecraft:leather_leggings",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "function": "enchant_randomly"
                }
              ],
              "name": "minecraft:leather_boots",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "function": "random_aux_value",
                  "values": {
                    "max": 6,
                    "min": 0
                  }
                }
              ],
              "name": "minecraft:suspicious_stew",
              "type": "item",
              "weight": 10
            }
          ],
          "rolls": {
            "max": 10,
            "min": 3
          }
        }
      }
    ],
    "only_reference": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "functions": [
                {
                  "count": {
                    "max": 12,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:paper",
              "type": "item",
              "weight": 8
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 6,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:potato",
              "type": "item",
              "weight": 7
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 4,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:moss_block",
              "type": "item",
              "weight": 7
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 6,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:poisonous_potato",
              "type": "item",
              "weight": 7
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 8,
                    "min": 4
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:carrot",
              "type": "item",
              "weight": 7
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 21,
                    "min": 8
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:wheat",
              "type": "item",
              "weight": 7
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 8,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:coal",
              "type": "item",
              "weight": 6
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 24,
                    "min": 5
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:rotten_flesh",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:bamboo",
              "type": "item",
              "weight": 2
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:pumpkin",
              "type": "item",
              "weight": 2
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 5,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:gunpowder",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 2,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:tnt",
              "type": "item",
              "weight": 1
            },
            {
              "functions": [
                {
                  "function": "enchant_randomly"
                }
              ],
              "name": "minecraft:leather_helmet",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "function": "enchant_randomly"
                }
              ],
              "name": "minecraft:leather_chestplate",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "function": "enchant_randomly"
                }
              ],
              "name": "minecraft:leather_leggings",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "function": "enchant_randomly"
                }
              ],
              "name": "minecraft:leather_boots",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "function": "random_aux_value",
                  "values": {
                    "max": 6,
                    "min": 0
                  }
                }
              ],
              "name": "minecraft:suspicious_stew",
              "type": "item",
              "weight": 10
            }
          ],
          "rolls": {
            "max": 10,
            "min": 3
          }
        }
      }
    ]
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `chests/simple_dungeon.json`

SHA-256 add-on `75ccfd1f679f4559858cfe369edfd94ac3f7dd8a7a08e161c4f67cc131e15cd5`; образца `5d704a9cbb490a90bbdc4f1125c8672a6c9c2c4609c9e1f5e06353c76458265f`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [
      [
        1,
        1
      ],
      [
        2,
        2
      ]
    ],
    "only_addon": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "name": "minecraft:saddle",
              "type": "item",
              "weight": 20
            },
            {
              "name": "minecraft:golden_apple",
              "type": "item",
              "weight": 15
            },
            {
              "name": "minecraft:appleEnchanted",
              "type": "item",
              "weight": 2
            },
            {
              "name": "minecraft:record_13",
              "type": "item",
              "weight": 15
            },
            {
              "name": "minecraft:record_cat",
              "type": "item",
              "weight": 15
            },
            {
              "name": "minecraft:name_tag",
              "type": "item",
              "weight": 20
            },
            {
              "name": "minecraft:horsearmorgold",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:horsearmoriron",
              "type": "item",
              "weight": 15
            },
            {
              "name": "minecraft:horsearmordiamond",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "function": "enchant_randomly"
                }
              ],
              "name": "minecraft:book",
              "type": "item",
              "weight": 10
            }
          ],
          "rolls": {
            "max": 3,
            "min": 1
          }
        }
      }
    ],
    "only_reference": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "name": "minecraft:saddle",
              "type": "item",
              "weight": 20
            },
            {
              "name": "minecraft:golden_apple",
              "type": "item",
              "weight": 15
            },
            {
              "name": "minecraft:appleEnchanted",
              "type": "item",
              "weight": 2
            },
            {
              "name": "minecraft:record_13",
              "type": "item",
              "weight": 15
            },
            {
              "name": "minecraft:record_cat",
              "type": "item",
              "weight": 15
            },
            {
              "name": "minecraft:record_otherside",
              "type": "item",
              "weight": 2
            },
            {
              "name": "minecraft:name_tag",
              "type": "item",
              "weight": 20
            },
            {
              "name": "minecraft:horsearmorgold",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:horsearmoriron",
              "type": "item",
              "weight": 15
            },
            {
              "name": "minecraft:horsearmordiamond",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "function": "enchant_randomly"
                }
              ],
              "name": "minecraft:book",
              "type": "item",
              "weight": 10
            }
          ],
          "rolls": {
            "max": 3,
            "min": 1
          }
        }
      }
    ]
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `chests/spawn_bonus_chest.json`

SHA-256 add-on `5b722029757f4510eea6b6da7872aa1076c5d3e425b69a6e81b058cc37ca0d02`; образца `c1b5a32d66c4a7c1099852f77dfb32fd7dad949f12fcbaa7e12c0c4b1e43d784`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [
      [
        1,
        1
      ],
      [
        2,
        2
      ],
      [
        3,
        3
      ],
      [
        4,
        4
      ],
      [
        5,
        5
      ],
      [
        6,
        6
      ],
      [
        8,
        8
      ],
      [
        9,
        9
      ],
      [
        10,
        10
      ],
      [
        11,
        11
      ],
      [
        12,
        12
      ],
      [
        13,
        13
      ]
    ],
    "only_addon": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "name": "effect:coal_sword",
              "type": "item",
              "weight": 1
            },
            {
              "name": "minecraft:stone_axe",
              "type": "item",
              "weight": 1
            },
            {
              "name": "minecraft:wooden_axe",
              "type": "item",
              "weight": 3
            }
          ],
          "rolls": 1
        }
      },
      {
        "index": 7,
        "value": {
          "entries": [
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:log2",
              "type": "item",
              "weight": 1
            },
            {
              "functions": [
                {
                  "data": 1,
                  "function": "minecraft:set_data"
                },
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:log2",
              "type": "item",
              "weight": 1
            }
          ],
          "rolls": 1
        }
      }
    ],
    "only_reference": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "name": "minecraft:stone_axe",
              "type": "item",
              "weight": 1
            },
            {
              "name": "minecraft:wooden_axe",
              "type": "item",
              "weight": 3
            }
          ],
          "rolls": 1
        }
      },
      {
        "index": 7,
        "value": {
          "entries": [
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:log2",
              "type": "item",
              "weight": 1
            },
            {
              "functions": [
                {
                  "data": 1,
                  "function": "minecraft:set_data"
                },
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:log2",
              "type": "item",
              "weight": 1
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:mangrove_log",
              "type": "item",
              "weight": 1
            }
          ],
          "rolls": 1
        }
      }
    ]
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `chests/stronghold_corridor.json`

SHA-256 add-on `436e02e55d15d846c3726cb9b705d88166621cfe9d2d2cad568aa0da705b7642`; образца `f6a164d154b34de5a13effe4dc52f443ad9b2691c444a4724c86f7fd96d995e9`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [],
    "only_addon": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "name": "minecraft:ender_pearl",
              "type": "item",
              "weight": 50
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:emerald",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:diamond",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 5,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:iron_ingot",
              "type": "item",
              "weight": 50
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:gold_ingot",
              "type": "item",
              "weight": 25
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 9,
                    "min": 4
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:redstone",
              "type": "item",
              "weight": 25
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:bread",
              "type": "item",
              "weight": 75
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:apple",
              "type": "item",
              "weight": 75
            },
            {
              "name": "minecraft:iron_pickaxe",
              "type": "item",
              "weight": 25
            },
            {
              "name": "minecraft:iron_sword",
              "type": "item",
              "weight": 25
            },
            {
              "name": "minecraft:iron_chestplate",
              "type": "item",
              "weight": 25
            },
            {
              "name": "minecraft:iron_helmet",
              "type": "item",
              "weight": 25
            },
            {
              "name": "minecraft:iron_leggings",
              "type": "item",
              "weight": 25
            },
            {
              "name": "minecraft:iron_boots",
              "type": "item",
              "weight": 25
            },
            {
              "name": "minecraft:golden_apple",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:saddle",
              "type": "item",
              "weight": 5
            },
            {
              "name": "effect:emerald_sword",
              "type": "item",
              "weight": 5
            },
            {
              "name": "effect:lapis_sword",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:horsearmoriron",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:horsearmorgold",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:horsearmordiamond",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "function": "enchant_with_levels",
                  "levels": 30,
                  "treasure": true
                }
              ],
              "name": "minecraft:book",
              "type": "item",
              "weight": 6
            }
          ],
          "rolls": {
            "max": 3,
            "min": 2
          }
        }
      }
    ],
    "only_reference": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "name": "minecraft:ender_pearl",
              "type": "item",
              "weight": 50
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:emerald",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:diamond",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 5,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:iron_ingot",
              "type": "item",
              "weight": 50
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:gold_ingot",
              "type": "item",
              "weight": 25
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 9,
                    "min": 4
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:redstone",
              "type": "item",
              "weight": 25
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:bread",
              "type": "item",
              "weight": 75
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:apple",
              "type": "item",
              "weight": 75
            },
            {
              "name": "minecraft:iron_pickaxe",
              "type": "item",
              "weight": 25
            },
            {
              "name": "minecraft:iron_sword",
              "type": "item",
              "weight": 25
            },
            {
              "name": "minecraft:iron_chestplate",
              "type": "item",
              "weight": 25
            },
            {
              "name": "minecraft:iron_helmet",
              "type": "item",
              "weight": 25
            },
            {
              "name": "minecraft:iron_leggings",
              "type": "item",
              "weight": 25
            },
            {
              "name": "minecraft:iron_boots",
              "type": "item",
              "weight": 25
            },
            {
              "name": "minecraft:golden_apple",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:saddle",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:horsearmoriron",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:horsearmorgold",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:horsearmordiamond",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:record_otherside",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "function": "enchant_with_levels",
                  "levels": 30,
                  "treasure": true
                }
              ],
              "name": "minecraft:book",
              "type": "item",
              "weight": 6
            }
          ],
          "rolls": {
            "max": 3,
            "min": 2
          }
        }
      }
    ]
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `chests/stronghold_library.json`

SHA-256 add-on `e8e52b4b31861a806b666a0b34816c7f464dc1858262d9ebd744fcc8836f6d3d`; образца `2babed7aaca1b1536c3ab494d3589b37d13a4da8354f1b2019fb115b3d63ee4e`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [],
    "only_addon": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:book",
              "type": "item",
              "weight": 100
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 7,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:paper",
              "type": "item",
              "weight": 100
            },
            {
              "name": "minecraft:map",
              "type": "item",
              "weight": 5
            },
            {
              "name": "effect:lapis_sword",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:compass",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "function": "enchant_with_levels",
                  "levels": 30,
                  "treasure": true
                }
              ],
              "name": "minecraft:book",
              "type": "item",
              "weight": 60
            }
          ],
          "rolls": {
            "max": 10,
            "min": 2
          }
        }
      }
    ],
    "only_reference": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:book",
              "type": "item",
              "weight": 100
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 7,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:paper",
              "type": "item",
              "weight": 100
            },
            {
              "name": "minecraft:map",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:compass",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "function": "enchant_with_levels",
                  "levels": 30,
                  "treasure": true
                }
              ],
              "name": "minecraft:book",
              "type": "item",
              "weight": 60
            }
          ],
          "rolls": {
            "max": 10,
            "min": 2
          }
        }
      }
    ]
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `chests/underwater_ruin_big.json`

SHA-256 add-on `113741262d5adc8cc4c3f1cef22e880181c732810a8f5b0a40bb42dc2a412cc6`; образца `e33c5889bb2b0b001a25dc15075cce523fad96211d798aaace58ce982039a3e6`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [
      [
        0,
        0
      ]
    ],
    "only_addon": [
      {
        "index": 1,
        "value": {
          "entries": [
            {
              "name": "minecraft:golden_apple",
              "type": "item",
              "weight": 1
            },
            {
              "name": "effect:magma_sword",
              "type": "item",
              "weight": 1
            },
            {
              "functions": [
                {
                  "function": "enchant_randomly"
                }
              ],
              "name": "minecraft:book",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:leather_chestplate",
              "type": "item",
              "weight": 1
            },
            {
              "name": "minecraft:golden_helmet",
              "type": "item",
              "weight": 1
            },
            {
              "functions": [
                {
                  "function": "enchant_randomly"
                }
              ],
              "name": "minecraft:fishing_rod",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "destination": "buriedtreasure",
                  "function": "exploration_map"
                }
              ],
              "name": "minecraft:map",
              "type": "item",
              "weight": 10
            }
          ],
          "rolls": 1
        }
      }
    ],
    "only_reference": [
      {
        "index": 1,
        "value": {
          "entries": [
            {
              "name": "minecraft:golden_apple",
              "type": "item",
              "weight": 1
            },
            {
              "functions": [
                {
                  "function": "enchant_randomly"
                }
              ],
              "name": "minecraft:book",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:leather_chestplate",
              "type": "item",
              "weight": 1
            },
            {
              "name": "minecraft:golden_helmet",
              "type": "item",
              "weight": 1
            },
            {
              "functions": [
                {
                  "function": "enchant_randomly"
                }
              ],
              "name": "minecraft:fishing_rod",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "destination": "buriedtreasure",
                  "function": "exploration_map"
                }
              ],
              "name": "minecraft:map",
              "type": "item",
              "weight": 10
            }
          ],
          "rolls": 1
        }
      }
    ]
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `chests/village/village_snowy_house.json`

SHA-256 add-on `5f631d0acedc39681f943d6cbe6ed03a54c3a220af3554ab5545382775e93a4c`; образца `dbaad2883cda2284082e771afddb234752475ff93fb52600a3a67d90fe4ac2f5`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [],
    "only_addon": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "name": "minecraft:blue_ice",
              "type": "item"
            },
            {
              "name": "minecraft:snow",
              "type": "item",
              "weight": 4
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 7,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:potato",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 4,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:bread",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 5,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:beetroot_seeds",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:beetroot_soup",
              "type": "item"
            },
            {
              "name": "minecraft:furnace",
              "type": "item"
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 4,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:emerald",
              "type": "item"
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 7,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:snowball",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 1,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "effect:ice_sword",
              "type": "item",
              "weight": 4
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 4,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:coal",
              "type": "item",
              "weight": 5
            }
          ],
          "rolls": {
            "max": 8,
            "min": 3
          }
        }
      }
    ],
    "only_reference": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "name": "minecraft:blue_ice",
              "type": "item"
            },
            {
              "name": "minecraft:snow",
              "type": "item",
              "weight": 4
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 7,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:potato",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 4,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:bread",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 5,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:beetroot_seeds",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:beetroot_soup",
              "type": "item"
            },
            {
              "name": "minecraft:furnace",
              "type": "item"
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 4,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:emerald",
              "type": "item"
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 7,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:snowball",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 4,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:coal",
              "type": "item",
              "weight": 5
            }
          ],
          "rolls": {
            "max": 8,
            "min": 3
          }
        }
      }
    ]
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `chests/woodland_mansion.json`

SHA-256 add-on `02a72468bdf568a92c857631940d78f467841a02bb3ea09868c0d99ef002eb63`; образца `09f1a1afaf014f5b94ded6de037bdd875847a1fcc8b76ed22a6c0d554d563b6e`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [
      [
        1,
        1
      ],
      [
        2,
        2
      ]
    ],
    "only_addon": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "name": "minecraft:lead",
              "type": "item",
              "weight": 100
            },
            {
              "name": "minecraft:golden_apple",
              "type": "item",
              "weight": 75
            },
            {
              "name": "minecraft:appleEnchanted",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:record_13",
              "type": "item",
              "weight": 75
            },
            {
              "name": "minecraft:record_cat",
              "type": "item",
              "weight": 75
            },
            {
              "name": "minecraft:name_tag",
              "type": "item",
              "weight": 100
            },
            {
              "name": "minecraft:chainmail_chestplate",
              "type": "item",
              "weight": 50
            },
            {
              "name": "minecraft:diamond_hoe",
              "type": "item",
              "weight": 75
            },
            {
              "name": "minecraft:diamond_chestplate",
              "type": "item",
              "weight": 25
            },
            {
              "name": "effect:emerald_sword",
              "type": "item",
              "weight": 25
            },
            {
              "functions": [
                {
                  "function": "enchant_randomly",
                  "treasure": true
                }
              ],
              "name": "minecraft:book",
              "type": "item",
              "weight": 60
            }
          ],
          "rolls": {
            "max": 3,
            "min": 1
          }
        }
      }
    ],
    "only_reference": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "name": "minecraft:lead",
              "type": "item",
              "weight": 100
            },
            {
              "name": "minecraft:golden_apple",
              "type": "item",
              "weight": 75
            },
            {
              "name": "minecraft:appleEnchanted",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:record_13",
              "type": "item",
              "weight": 75
            },
            {
              "name": "minecraft:record_cat",
              "type": "item",
              "weight": 75
            },
            {
              "name": "minecraft:name_tag",
              "type": "item",
              "weight": 100
            },
            {
              "name": "minecraft:chainmail_chestplate",
              "type": "item",
              "weight": 50
            },
            {
              "name": "minecraft:diamond_hoe",
              "type": "item",
              "weight": 75
            },
            {
              "name": "minecraft:diamond_chestplate",
              "type": "item",
              "weight": 25
            },
            {
              "functions": [
                {
                  "function": "enchant_randomly",
                  "treasure": true
                }
              ],
              "name": "minecraft:book",
              "type": "item",
              "weight": 60
            }
          ],
          "rolls": {
            "max": 3,
            "min": 1
          }
        }
      }
    ]
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `entities/blaze.json`

SHA-256 add-on `4a3aa8badbc60aed981951f1d7580362a98bfe57fb02cf39e13bea913a4f4d38`; образца `0c14613b63c3b564d14ce332d17f169e97a1ad2174f724aa36242220cd29a359`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [
      [
        0,
        0
      ]
    ],
    "only_addon": [
      {
        "index": 1,
        "value": {
          "conditions": [
            {
              "condition": "killed_by_entity",
              "entity_type": "minecraft:snow_golem"
            },
            {
              "chance": 0.025,
              "condition": "random_chance_with_looting",
              "looting_multiplier": 0.02
            }
          ],
          "entries": [
            {
              "functions": [
                {
                  "data": 0,
                  "function": "set_data"
                }
              ],
              "name": "effect:blaze_sword",
              "type": "item",
              "weight": 1
            }
          ],
          "rolls": 1
        }
      }
    ],
    "only_reference": []
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `entities/elder_guardian.json`

SHA-256 add-on `d4c4c9380d598ce9c87f8b6e6006ca2856103bd450f34607c254470d781547a1`; образца `625e1ac6f465ba38723c9d9d67d2c68b6655827963b39ea15c07da50c98eb02e`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [
      [
        0,
        0
      ],
      [
        1,
        2
      ],
      [
        2,
        3
      ],
      [
        3,
        4
      ]
    ],
    "only_addon": [
      {
        "index": 1,
        "value": {
          "conditions": [
            {
              "condition": "killed_by_player"
            },
            {
              "chance": 0.065,
              "condition": "random_chance_with_looting",
              "looting_multiplier": 0.02
            }
          ],
          "entries": [
            {
              "functions": [
                {
                  "count": {
                    "max": 1,
                    "min": 1
                  },
                  "function": "set_count"
                },
                {
                  "data": 0,
                  "function": "set_data"
                }
              ],
              "name": "effect:sponge_sword",
              "type": "item",
              "weight": 1
            }
          ],
          "rolls": 1
        }
      }
    ],
    "only_reference": []
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `entities/shulker.json`

SHA-256 add-on `f68cd2a30a473a605fd04aa4ec81c592f098a882e8a32eabe54feca78a6e7aae`; образца `e83bc240e031698b372c98af93918f78e965d1228f4b1e6685fdc8c7888ff9c2`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [
      [
        0,
        0
      ]
    ],
    "only_addon": [
      {
        "index": 1,
        "value": {
          "conditions": [
            {
              "condition": "killed_by_player"
            },
            {
              "chance": 0.045,
              "condition": "random_chance_with_looting",
              "looting_multiplier": 0.02
            }
          ],
          "entries": [
            {
              "functions": [
                {
                  "count": {
                    "max": 1,
                    "min": 1
                  },
                  "function": "set_count"
                },
                {
                  "data": 0,
                  "function": "set_data"
                }
              ],
              "name": "effect:shulker_sword",
              "type": "item",
              "weight": 1
            }
          ],
          "rolls": 1
        }
      }
    ],
    "only_reference": []
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `entities/wither_skeleton.json`

SHA-256 add-on `27e3a5a47848d48de7d72acfab193587d8886b47f087d6214f09c39eeb7526c6`; образца `cebf3750c7dc2a254648a773a4895bafe57628a3d2aa7be242951e658ad2eeaf`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [
      [
        0,
        0
      ],
      [
        1,
        1
      ],
      [
        2,
        2
      ]
    ],
    "only_addon": [
      {
        "index": 3,
        "value": {
          "conditions": [
            {
              "condition": "killed_by_player"
            },
            {
              "chance": 0.025,
              "condition": "random_chance_with_looting",
              "looting_multiplier": 0.02
            }
          ],
          "entries": [
            {
              "functions": [
                {
                  "data": 0,
                  "function": "set_data"
                }
              ],
              "name": "effect:wither_skeleton_sword",
              "type": "item",
              "weight": 1
            }
          ],
          "rolls": 1
        }
      }
    ],
    "only_reference": []
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `gameplay/fishing/treasure.json`

SHA-256 add-on `0459bb92fd47cab5f10e8c514d7b262854d8dab31c7b2efc1af13d839cae568e`; образца `5ac79eeb3122e9f2459c6f0087e55f83c49f292e5b2fb67bf589e1aaa1e02f0d`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [],
    "only_addon": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "name": "minecraft:nautilus_shell",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:waterlily",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:name_tag",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:saddle",
              "type": "item",
              "weight": 5
            },
            {
              "name": "effect:jungle_sword",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "damage": {
                    "max": 0.25,
                    "min": 0
                  },
                  "function": "set_damage"
                },
                {
                  "function": "enchant_with_levels",
                  "levels": 30,
                  "treasure": true
                }
              ],
              "name": "minecraft:bow",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "damage": {
                    "max": 0.25,
                    "min": 0
                  },
                  "function": "set_damage"
                },
                {
                  "function": "enchant_with_levels",
                  "levels": 30,
                  "treasure": true
                }
              ],
              "name": "minecraft:fishing_rod",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "function": "enchant_with_levels",
                  "levels": 30,
                  "treasure": true
                }
              ],
              "name": "minecraft:book",
              "type": "item",
              "weight": 6
            }
          ],
          "rolls": 1
        }
      }
    ],
    "only_reference": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "name": "minecraft:nautilus_shell",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:waterlily",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:name_tag",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:saddle",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "damage": {
                    "max": 0.25,
                    "min": 0
                  },
                  "function": "set_damage"
                },
                {
                  "function": "enchant_with_levels",
                  "levels": 30,
                  "treasure": true
                }
              ],
              "name": "minecraft:bow",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "damage": {
                    "max": 0.25,
                    "min": 0
                  },
                  "function": "set_damage"
                },
                {
                  "function": "enchant_with_levels",
                  "levels": 30,
                  "treasure": true
                }
              ],
              "name": "minecraft:fishing_rod",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "function": "enchant_with_levels",
                  "levels": 30,
                  "treasure": true
                }
              ],
              "name": "minecraft:book",
              "type": "item",
              "weight": 6
            }
          ],
          "rolls": 1
        }
      }
    ]
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

## Образец `1.20.30.1`

### `chests/abandoned_mineshaft.json`

SHA-256 add-on `fdce88876b62f2ba9dce2e544df7bc0edad50f3793b357000416d536f0a6fa94`; образца `398d7f6449985594cc2464186773b5720d008024d013e3ea3ae99ed62634a324`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [
      [
        0,
        0
      ],
      [
        2,
        2
      ]
    ],
    "only_addon": [
      {
        "index": 1,
        "value": {
          "entries": [
            {
              "functions": [
                {
                  "count": {
                    "max": 5,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:iron_ingot",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:gold_ingot",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 9,
                    "min": 4
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:redstone",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "data": 4,
                  "function": "set_data"
                },
                {
                  "count": {
                    "max": 9,
                    "min": 4
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:dye",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 2,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:diamond",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 1,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "effect:spider_sword",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 8,
                    "min": 3
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:coal",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:bread",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 4,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:melon_seeds",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 4,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:pumpkin_seeds",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 4,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:beetroot_seeds",
              "type": "item",
              "weight": 10
            }
          ],
          "rolls": {
            "max": 4,
            "min": 2
          }
        }
      }
    ],
    "only_reference": [
      {
        "index": 1,
        "value": {
          "entries": [
            {
              "functions": [
                {
                  "count": {
                    "max": 5,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:iron_ingot",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:gold_ingot",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 9,
                    "min": 4
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:redstone",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "data": 4,
                  "function": "set_data"
                },
                {
                  "count": {
                    "max": 9,
                    "min": 4
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:dye",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 2,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:diamond",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 8,
                    "min": 3
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:coal",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:bread",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 4,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:melon_seeds",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 4,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:pumpkin_seeds",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 4,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:beetroot_seeds",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 6,
                    "min": 3
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:glow_berries",
              "type": "item",
              "weight": 15
            }
          ],
          "rolls": {
            "max": 4,
            "min": 2
          }
        }
      }
    ]
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `chests/buriedtreasure.json`

SHA-256 add-on `be6b5480ced6a762aaa553cd63361848a64c0e4e01ca85d16f1a57aa027ffb7f`; образца `f335246c8ebf7a6d9113b4d9d74e195b8b960f0c6ea3f1da533f0a7ed2873285`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [
      [
        0,
        0
      ]
    ],
    "only_addon": [
      {
        "index": 1,
        "value": {
          "entries": [
            {
              "functions": [
                {
                  "count": {
                    "max": 5,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:prismarine_crystals",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 5,
                    "min": 3
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:iron_ingot",
              "type": "item",
              "weight": 20
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 5,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:gold_ingot",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 2,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:tnt",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:diamond",
              "type": "item",
              "weight": 15
            },
            {
              "name": "minecraft:record_wait",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:record_mellohi",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:name_tag",
              "type": "item",
              "weight": 10
            },
            {
              "name": "effect:sea_sword",
              "type": "item",
              "weight": 15
            },
            {
              "name": "minecraft:chainmail_chestplate",
              "type": "item",
              "weight": 20
            },
            {
              "name": "minecraft:chainmail_helmet",
              "type": "item",
              "weight": 20
            },
            {
              "name": "minecraft:chainmail_leggings",
              "type": "item",
              "weight": 20
            },
            {
              "name": "minecraft:chainmail_boots",
              "type": "item",
              "weight": 20
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 2,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:writable_book",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:lead",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:experience_bottle",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "data": 19,
                  "function": "set_data"
                }
              ],
              "name": "minecraft:potion",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "data": 28,
                  "function": "set_data"
                }
              ],
              "name": "minecraft:potion",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:cake",
              "type": "item",
              "weight": 1
            }
          ],
          "rolls": {
            "max": 12,
            "min": 5
          }
        }
      }
    ],
    "only_reference": [
      {
        "index": 1,
        "value": {
          "entries": [
            {
              "functions": [
                {
                  "count": {
                    "max": 5,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:prismarine_crystals",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 5,
                    "min": 3
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:iron_ingot",
              "type": "item",
              "weight": 20
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 5,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:gold_ingot",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 2,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:tnt",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:diamond",
              "type": "item",
              "weight": 15
            },
            {
              "name": "minecraft:record_wait",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:record_mellohi",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:name_tag",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:chainmail_chestplate",
              "type": "item",
              "weight": 20
            },
            {
              "name": "minecraft:chainmail_helmet",
              "type": "item",
              "weight": 20
            },
            {
              "name": "minecraft:chainmail_leggings",
              "type": "item",
              "weight": 20
            },
            {
              "name": "minecraft:chainmail_boots",
              "type": "item",
              "weight": 20
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 2,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:writable_book",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:lead",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:experience_bottle",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "data": 19,
                  "function": "set_data"
                }
              ],
              "name": "minecraft:potion",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "data": 28,
                  "function": "set_data"
                }
              ],
              "name": "minecraft:potion",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:cake",
              "type": "item",
              "weight": 1
            }
          ],
          "rolls": {
            "max": 12,
            "min": 5
          }
        }
      }
    ]
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `chests/desert_pyramid.json`

SHA-256 add-on `62dbed4c7083aee0863fc97ded6fb00fc6510b69a75721cb9320be41e89b92a3`; образца `d76adda3efc2300db7a875bcbc7a380760a8e77431f034ee0944446555ce7ddf`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [
      [
        1,
        1
      ]
    ],
    "only_addon": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:diamond",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 5,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:iron_ingot",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 7,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:gold_ingot",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:emerald",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 6,
                    "min": 4
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:bone",
              "type": "item",
              "weight": 25
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:spider_eye",
              "type": "item",
              "weight": 25
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 7,
                    "min": 3
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:rotten_flesh",
              "type": "item",
              "weight": 25
            },
            {
              "name": "minecraft:saddle",
              "type": "item",
              "weight": 20
            },
            {
              "name": "effect:tnt_sword",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:horsearmoriron",
              "type": "item",
              "weight": 15
            },
            {
              "name": "minecraft:horsearmorgold",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:horsearmordiamond",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "function": "enchant_randomly"
                }
              ],
              "name": "minecraft:book",
              "type": "item",
              "weight": 20
            },
            {
              "name": "minecraft:golden_apple",
              "type": "item",
              "weight": 20
            },
            {
              "name": "minecraft:appleEnchanted",
              "type": "item",
              "weight": 2
            },
            {
              "type": "empty",
              "weight": 15
            }
          ],
          "rolls": {
            "max": 4,
            "min": 2
          }
        }
      }
    ],
    "only_reference": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:diamond",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 5,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:iron_ingot",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 7,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:gold_ingot",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:emerald",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 6,
                    "min": 4
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:bone",
              "type": "item",
              "weight": 25
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:spider_eye",
              "type": "item",
              "weight": 25
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 7,
                    "min": 3
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:rotten_flesh",
              "type": "item",
              "weight": 25
            },
            {
              "name": "minecraft:saddle",
              "type": "item",
              "weight": 20
            },
            {
              "name": "minecraft:horsearmoriron",
              "type": "item",
              "weight": 15
            },
            {
              "name": "minecraft:horsearmorgold",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:horsearmordiamond",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "function": "enchant_randomly"
                }
              ],
              "name": "minecraft:book",
              "type": "item",
              "weight": 20
            },
            {
              "name": "minecraft:golden_apple",
              "type": "item",
              "weight": 20
            },
            {
              "name": "minecraft:appleEnchanted",
              "type": "item",
              "weight": 2
            },
            {
              "type": "empty",
              "weight": 15
            }
          ],
          "rolls": {
            "max": 4,
            "min": 2
          }
        }
      },
      {
        "index": 2,
        "value": {
          "entries": [
            {
              "type": "empty",
              "weight": 6
            },
            {
              "functions": [
                {
                  "count": 2,
                  "function": "set_count"
                }
              ],
              "name": "minecraft:dune_armor_trim_smithing_template",
              "type": "item",
              "weight": 1
            }
          ],
          "rolls": 1
        }
      }
    ]
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `chests/end_city_treasure.json`

SHA-256 add-on `923422e7d419edfd97abfb608ea0962671eb7d02529c32ba4a522904ad5f8bac`; образца `0a61c7da63e18325df520c09bc4b8b0b40bc3f4c5ca27166f0348ecd44aa4681`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [
      [
        0,
        0
      ]
    ],
    "only_addon": [],
    "only_reference": [
      {
        "index": 1,
        "value": {
          "entries": [
            {
              "type": "empty",
              "weight": 14
            },
            {
              "name": "minecraft:spire_armor_trim_smithing_template",
              "type": "item",
              "weight": 1
            }
          ],
          "rolls": 1
        }
      }
    ]
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `chests/igloo_chest.json`

SHA-256 add-on `0e4e2cc4f566213b80753df3aa62c16126a98952a6796181c12d6d291815856e`; образца `9b48c4c250b0d3c5889f476a2f109499c5734adfe604d561cade5011e22b93f1`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [
      [
        1,
        1
      ]
    ],
    "only_addon": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:apple",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 4,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:coal",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:gold_nugget",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:stone_axe",
              "type": "item",
              "weight": 2
            },
            {
              "name": "minecraft:rotten_flesh",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:emerald",
              "type": "item",
              "weight": 1
            },
            {
              "name": "effect:ice_sword",
              "type": "item",
              "weight": 1
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 2
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:wheat",
              "type": "item",
              "weight": 10
            }
          ],
          "rolls": {
            "max": 8,
            "min": 2
          }
        }
      }
    ],
    "only_reference": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:apple",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 4,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:coal",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:gold_nugget",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:stone_axe",
              "type": "item",
              "weight": 2
            },
            {
              "name": "minecraft:rotten_flesh",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:emerald",
              "type": "item",
              "weight": 1
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 2
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:wheat",
              "type": "item",
              "weight": 10
            }
          ],
          "rolls": {
            "max": 8,
            "min": 2
          }
        }
      }
    ]
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `chests/jungle_temple.json`

SHA-256 add-on `457065c0f039f716836b183eb083ff9e11bbec9b4391845912f93d20bf01faa0`; образца `9ef5c20d0d1bd5c4a6855888e66c15724535c51d2f05372f0f9827da791edbdd`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [],
    "only_addon": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:diamond",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 5,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:iron_ingot",
              "type": "item",
              "weight": 50
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 7,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:gold_ingot",
              "type": "item",
              "weight": 75
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:emerald",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 6,
                    "min": 4
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:bone",
              "type": "item",
              "weight": 100
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 7,
                    "min": 3
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:rotten_flesh",
              "type": "item",
              "weight": 80
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:bamboo",
              "type": "item",
              "weight": 75
            },
            {
              "name": "minecraft:saddle",
              "type": "item",
              "weight": 15
            },
            {
              "name": "effect:jungle_sword",
              "type": "item",
              "weight": 16
            },
            {
              "name": "minecraft:horsearmoriron",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:horsearmorgold",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:horsearmordiamond",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "function": "enchant_with_levels",
                  "levels": 30,
                  "treasure": true
                }
              ],
              "name": "minecraft:book",
              "type": "item",
              "weight": 6
            }
          ],
          "rolls": {
            "max": 6,
            "min": 2
          }
        }
      }
    ],
    "only_reference": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:diamond",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 5,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:iron_ingot",
              "type": "item",
              "weight": 50
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 7,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:gold_ingot",
              "type": "item",
              "weight": 75
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:emerald",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 6,
                    "min": 4
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:bone",
              "type": "item",
              "weight": 100
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 7,
                    "min": 3
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:rotten_flesh",
              "type": "item",
              "weight": 80
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:bamboo",
              "type": "item",
              "weight": 75
            },
            {
              "name": "minecraft:saddle",
              "type": "item",
              "weight": 15
            },
            {
              "name": "minecraft:horsearmoriron",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:horsearmorgold",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:horsearmordiamond",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "function": "enchant_with_levels",
                  "levels": 30,
                  "treasure": true
                }
              ],
              "name": "minecraft:book",
              "type": "item",
              "weight": 6
            }
          ],
          "rolls": {
            "max": 6,
            "min": 2
          }
        }
      },
      {
        "index": 1,
        "value": {
          "entries": [
            {
              "type": "empty",
              "weight": 2
            },
            {
              "functions": [
                {
                  "count": 2,
                  "function": "set_count"
                }
              ],
              "name": "minecraft:wild_armor_trim_smithing_template",
              "type": "item",
              "weight": 1
            }
          ],
          "rolls": 1
        }
      }
    ]
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `chests/nether_bridge.json`

SHA-256 add-on `df8f5bf18a1d250e005b6b50a1ead25ca910f77ef3a8718cc6e21091ccae6496`; образца `7832de65e2e747bb5146b70a8b1f0c65a70574d21e2f66fd01f3635971704405`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [
      [
        0,
        0
      ]
    ],
    "only_addon": [],
    "only_reference": [
      {
        "index": 1,
        "value": {
          "entries": [
            {
              "type": "empty",
              "weight": 14
            },
            {
              "name": "minecraft:rib_armor_trim_smithing_template",
              "type": "item",
              "weight": 1
            }
          ],
          "rolls": 1
        }
      }
    ]
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `chests/pillager_outpost.json`

SHA-256 add-on `0f3d58e0cbef851cb3ab7b4c5d85155a377c0126a66e569b08d6bdddedc1a5ef`; образца `aedbb1d4530dd9859c8e9aa3188c6c03d01e2d42ec6c261589a5f8e257da733e`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [
      [
        0,
        0
      ],
      [
        1,
        1
      ],
      [
        2,
        2
      ]
    ],
    "only_addon": [
      {
        "index": 3,
        "value": {
          "entries": [
            {
              "name": "minecraft:experience_bottle",
              "type": "item",
              "weight": 7
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 6,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:string",
              "type": "item",
              "weight": 4
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 7,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:arrow",
              "type": "item",
              "weight": 4
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:tripwire_hook",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:iron_ingot",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 1,
                    "min": 0
                  },
                  "function": "set_count"
                }
              ],
              "name": "effect:emerald_sword",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 1,
                    "min": 0
                  },
                  "function": "set_count"
                }
              ],
              "name": "effect:lapis_sword",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "function": "minecraft:enchant_randomly"
                }
              ],
              "name": "minecraft:book",
              "type": "item"
            }
          ],
          "rolls": {
            "max": 3,
            "min": 2
          }
        }
      }
    ],
    "only_reference": [
      {
        "index": 3,
        "value": {
          "entries": [
            {
              "name": "minecraft:experience_bottle",
              "type": "item",
              "weight": 7
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 6,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:string",
              "type": "item",
              "weight": 4
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 7,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:arrow",
              "type": "item",
              "weight": 4
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:tripwire_hook",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:iron_ingot",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "function": "minecraft:enchant_randomly"
                }
              ],
              "name": "minecraft:book",
              "type": "item"
            }
          ],
          "rolls": {
            "max": 3,
            "min": 2
          }
        }
      },
      {
        "index": 4,
        "value": {
          "entries": [
            {
              "functions": [
                {
                  "data": {
                    "max": 3,
                    "min": 0
                  },
                  "function": "set_data"
                }
              ],
              "name": "minecraft:goat_horn",
              "type": "item"
            }
          ],
          "rolls": {
            "max": 1,
            "min": 0
          }
        }
      },
      {
        "index": 5,
        "value": {
          "entries": [
            {
              "type": "empty",
              "weight": 3
            },
            {
              "functions": [
                {
                  "count": 2,
                  "function": "set_count"
                }
              ],
              "name": "minecraft:sentry_armor_trim_smithing_template",
              "type": "item",
              "weight": 1
            }
          ],
          "rolls": 1
        }
      }
    ]
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `chests/shipwreck.json`

SHA-256 add-on `ecd31113fa81adb02ba7fa8fb8ad44dcfd054d7f62a221dd0fab4bd09bc06867`; образца `5f1ada0ebaf359fd1b208692cff1dbfaee6755e8c27188d4141d5f1e0fadd6a9`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [
      [
        0,
        0
      ],
      [
        1,
        1
      ]
    ],
    "only_addon": [],
    "only_reference": [
      {
        "index": 2,
        "value": {
          "entries": [
            {
              "type": "empty",
              "weight": 5
            },
            {
              "functions": [
                {
                  "count": 2,
                  "function": "set_count"
                }
              ],
              "name": "minecraft:coast_armor_trim_smithing_template",
              "type": "item",
              "weight": 1
            }
          ],
          "rolls": 1
        }
      }
    ]
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `chests/shipwrecksupply.json`

SHA-256 add-on `f4feb668018a8fd2a822370b7a695368c501c1e037d5b50c7413864ea858d1ad`; образца `fb7eb594719e231d2ccb6a26feade0f83674456b462c48a70d16c609d9116077`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [],
    "only_addon": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "functions": [
                {
                  "count": {
                    "max": 12,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:paper",
              "type": "item",
              "weight": 8
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 6,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:potato",
              "type": "item",
              "weight": 7
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 6,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:poisonous_potato",
              "type": "item",
              "weight": 7
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 8,
                    "min": 4
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:carrot",
              "type": "item",
              "weight": 7
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 21,
                    "min": 8
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:wheat",
              "type": "item",
              "weight": 7
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 8,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:coal",
              "type": "item",
              "weight": 6
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 24,
                    "min": 5
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:rotten_flesh",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:bamboo",
              "type": "item",
              "weight": 2
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:pumpkin",
              "type": "item",
              "weight": 2
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 5,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:gunpowder",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 2,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:tnt",
              "type": "item",
              "weight": 1
            },
            {
              "functions": [
                {
                  "function": "enchant_randomly"
                }
              ],
              "name": "minecraft:leather_helmet",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "function": "enchant_randomly"
                }
              ],
              "name": "minecraft:leather_chestplate",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "function": "enchant_randomly"
                }
              ],
              "name": "minecraft:leather_leggings",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "function": "enchant_randomly"
                }
              ],
              "name": "minecraft:leather_boots",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "function": "random_aux_value",
                  "values": {
                    "max": 6,
                    "min": 0
                  }
                }
              ],
              "name": "minecraft:suspicious_stew",
              "type": "item",
              "weight": 10
            }
          ],
          "rolls": {
            "max": 10,
            "min": 3
          }
        }
      }
    ],
    "only_reference": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "functions": [
                {
                  "count": {
                    "max": 12,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:paper",
              "type": "item",
              "weight": 8
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 6,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:potato",
              "type": "item",
              "weight": 7
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 4,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:moss_block",
              "type": "item",
              "weight": 7
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 6,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:poisonous_potato",
              "type": "item",
              "weight": 7
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 8,
                    "min": 4
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:carrot",
              "type": "item",
              "weight": 7
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 21,
                    "min": 8
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:wheat",
              "type": "item",
              "weight": 7
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 8,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:coal",
              "type": "item",
              "weight": 6
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 24,
                    "min": 5
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:rotten_flesh",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:bamboo",
              "type": "item",
              "weight": 2
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:pumpkin",
              "type": "item",
              "weight": 2
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 5,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:gunpowder",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 2,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:tnt",
              "type": "item",
              "weight": 1
            },
            {
              "functions": [
                {
                  "function": "enchant_randomly"
                }
              ],
              "name": "minecraft:leather_helmet",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "function": "enchant_randomly"
                }
              ],
              "name": "minecraft:leather_chestplate",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "function": "enchant_randomly"
                }
              ],
              "name": "minecraft:leather_leggings",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "function": "enchant_randomly"
                }
              ],
              "name": "minecraft:leather_boots",
              "type": "item",
              "weight": 3
            },
            {
              "functions": [
                {
                  "function": "random_aux_value",
                  "values": {
                    "max": 6,
                    "min": 0
                  }
                }
              ],
              "name": "minecraft:suspicious_stew",
              "type": "item",
              "weight": 10
            }
          ],
          "rolls": {
            "max": 10,
            "min": 3
          }
        }
      },
      {
        "index": 1,
        "value": {
          "entries": [
            {
              "type": "empty",
              "weight": 5
            },
            {
              "functions": [
                {
                  "count": 2,
                  "function": "set_count"
                }
              ],
              "name": "minecraft:coast_armor_trim_smithing_template",
              "type": "item",
              "weight": 1
            }
          ],
          "rolls": 1
        }
      }
    ]
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `chests/shipwrecktreasure.json`

SHA-256 add-on `95a6849f1217fbfacf0e55b14450442a74c1a37246458d6cf1a5b8e6c69df577`; образца `9fab18487300a028730a8b140f7e10ef0d9ef52ef93e14569c1c0ef66c7b9b85`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [
      [
        0,
        0
      ],
      [
        1,
        1
      ]
    ],
    "only_addon": [],
    "only_reference": [
      {
        "index": 2,
        "value": {
          "entries": [
            {
              "type": "empty",
              "weight": 5
            },
            {
              "functions": [
                {
                  "count": 2,
                  "function": "set_count"
                }
              ],
              "name": "minecraft:coast_armor_trim_smithing_template",
              "type": "item",
              "weight": 1
            }
          ],
          "rolls": 1
        }
      }
    ]
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `chests/simple_dungeon.json`

SHA-256 add-on `75ccfd1f679f4559858cfe369edfd94ac3f7dd8a7a08e161c4f67cc131e15cd5`; образца `5d704a9cbb490a90bbdc4f1125c8672a6c9c2c4609c9e1f5e06353c76458265f`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [
      [
        1,
        1
      ],
      [
        2,
        2
      ]
    ],
    "only_addon": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "name": "minecraft:saddle",
              "type": "item",
              "weight": 20
            },
            {
              "name": "minecraft:golden_apple",
              "type": "item",
              "weight": 15
            },
            {
              "name": "minecraft:appleEnchanted",
              "type": "item",
              "weight": 2
            },
            {
              "name": "minecraft:record_13",
              "type": "item",
              "weight": 15
            },
            {
              "name": "minecraft:record_cat",
              "type": "item",
              "weight": 15
            },
            {
              "name": "minecraft:name_tag",
              "type": "item",
              "weight": 20
            },
            {
              "name": "minecraft:horsearmorgold",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:horsearmoriron",
              "type": "item",
              "weight": 15
            },
            {
              "name": "minecraft:horsearmordiamond",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "function": "enchant_randomly"
                }
              ],
              "name": "minecraft:book",
              "type": "item",
              "weight": 10
            }
          ],
          "rolls": {
            "max": 3,
            "min": 1
          }
        }
      }
    ],
    "only_reference": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "name": "minecraft:saddle",
              "type": "item",
              "weight": 20
            },
            {
              "name": "minecraft:golden_apple",
              "type": "item",
              "weight": 15
            },
            {
              "name": "minecraft:appleEnchanted",
              "type": "item",
              "weight": 2
            },
            {
              "name": "minecraft:record_13",
              "type": "item",
              "weight": 15
            },
            {
              "name": "minecraft:record_cat",
              "type": "item",
              "weight": 15
            },
            {
              "name": "minecraft:record_otherside",
              "type": "item",
              "weight": 2
            },
            {
              "name": "minecraft:name_tag",
              "type": "item",
              "weight": 20
            },
            {
              "name": "minecraft:horsearmorgold",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:horsearmoriron",
              "type": "item",
              "weight": 15
            },
            {
              "name": "minecraft:horsearmordiamond",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "function": "enchant_randomly"
                }
              ],
              "name": "minecraft:book",
              "type": "item",
              "weight": 10
            }
          ],
          "rolls": {
            "max": 3,
            "min": 1
          }
        }
      }
    ]
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `chests/spawn_bonus_chest.json`

SHA-256 add-on `5b722029757f4510eea6b6da7872aa1076c5d3e425b69a6e81b058cc37ca0d02`; образца `c1b5a32d66c4a7c1099852f77dfb32fd7dad949f12fcbaa7e12c0c4b1e43d784`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [
      [
        1,
        1
      ],
      [
        2,
        2
      ],
      [
        3,
        3
      ],
      [
        4,
        4
      ],
      [
        5,
        5
      ],
      [
        6,
        6
      ],
      [
        8,
        8
      ],
      [
        9,
        9
      ],
      [
        10,
        10
      ],
      [
        11,
        11
      ],
      [
        12,
        12
      ],
      [
        13,
        13
      ]
    ],
    "only_addon": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "name": "effect:coal_sword",
              "type": "item",
              "weight": 1
            },
            {
              "name": "minecraft:stone_axe",
              "type": "item",
              "weight": 1
            },
            {
              "name": "minecraft:wooden_axe",
              "type": "item",
              "weight": 3
            }
          ],
          "rolls": 1
        }
      },
      {
        "index": 7,
        "value": {
          "entries": [
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:log2",
              "type": "item",
              "weight": 1
            },
            {
              "functions": [
                {
                  "data": 1,
                  "function": "minecraft:set_data"
                },
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:log2",
              "type": "item",
              "weight": 1
            }
          ],
          "rolls": 1
        }
      }
    ],
    "only_reference": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "name": "minecraft:stone_axe",
              "type": "item",
              "weight": 1
            },
            {
              "name": "minecraft:wooden_axe",
              "type": "item",
              "weight": 3
            }
          ],
          "rolls": 1
        }
      },
      {
        "index": 7,
        "value": {
          "entries": [
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:log2",
              "type": "item",
              "weight": 1
            },
            {
              "functions": [
                {
                  "data": 1,
                  "function": "minecraft:set_data"
                },
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:log2",
              "type": "item",
              "weight": 1
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:mangrove_log",
              "type": "item",
              "weight": 1
            }
          ],
          "rolls": 1
        }
      }
    ]
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `chests/stronghold_corridor.json`

SHA-256 add-on `436e02e55d15d846c3726cb9b705d88166621cfe9d2d2cad568aa0da705b7642`; образца `9fb36a00441aa951466e5425a367a8e579b88d54fe55f6cc741c86632c6c721b`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [],
    "only_addon": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "name": "minecraft:ender_pearl",
              "type": "item",
              "weight": 50
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:emerald",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:diamond",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 5,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:iron_ingot",
              "type": "item",
              "weight": 50
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:gold_ingot",
              "type": "item",
              "weight": 25
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 9,
                    "min": 4
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:redstone",
              "type": "item",
              "weight": 25
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:bread",
              "type": "item",
              "weight": 75
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:apple",
              "type": "item",
              "weight": 75
            },
            {
              "name": "minecraft:iron_pickaxe",
              "type": "item",
              "weight": 25
            },
            {
              "name": "minecraft:iron_sword",
              "type": "item",
              "weight": 25
            },
            {
              "name": "minecraft:iron_chestplate",
              "type": "item",
              "weight": 25
            },
            {
              "name": "minecraft:iron_helmet",
              "type": "item",
              "weight": 25
            },
            {
              "name": "minecraft:iron_leggings",
              "type": "item",
              "weight": 25
            },
            {
              "name": "minecraft:iron_boots",
              "type": "item",
              "weight": 25
            },
            {
              "name": "minecraft:golden_apple",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:saddle",
              "type": "item",
              "weight": 5
            },
            {
              "name": "effect:emerald_sword",
              "type": "item",
              "weight": 5
            },
            {
              "name": "effect:lapis_sword",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:horsearmoriron",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:horsearmorgold",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:horsearmordiamond",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "function": "enchant_with_levels",
                  "levels": 30,
                  "treasure": true
                }
              ],
              "name": "minecraft:book",
              "type": "item",
              "weight": 6
            }
          ],
          "rolls": {
            "max": 3,
            "min": 2
          }
        }
      }
    ],
    "only_reference": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "name": "minecraft:ender_pearl",
              "type": "item",
              "weight": 50
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:emerald",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:diamond",
              "type": "item",
              "weight": 15
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 5,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:iron_ingot",
              "type": "item",
              "weight": 50
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:gold_ingot",
              "type": "item",
              "weight": 25
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 9,
                    "min": 4
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:redstone",
              "type": "item",
              "weight": 25
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:bread",
              "type": "item",
              "weight": 75
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:apple",
              "type": "item",
              "weight": 75
            },
            {
              "name": "minecraft:iron_pickaxe",
              "type": "item",
              "weight": 25
            },
            {
              "name": "minecraft:iron_sword",
              "type": "item",
              "weight": 25
            },
            {
              "name": "minecraft:iron_chestplate",
              "type": "item",
              "weight": 25
            },
            {
              "name": "minecraft:iron_helmet",
              "type": "item",
              "weight": 25
            },
            {
              "name": "minecraft:iron_leggings",
              "type": "item",
              "weight": 25
            },
            {
              "name": "minecraft:iron_boots",
              "type": "item",
              "weight": 25
            },
            {
              "name": "minecraft:golden_apple",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:saddle",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:horsearmoriron",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:horsearmorgold",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:horsearmordiamond",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:record_otherside",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "function": "enchant_with_levels",
                  "levels": 30,
                  "treasure": true
                }
              ],
              "name": "minecraft:book",
              "type": "item",
              "weight": 6
            }
          ],
          "rolls": {
            "max": 3,
            "min": 2
          }
        }
      },
      {
        "index": 1,
        "value": {
          "entries": [
            {
              "type": "empty",
              "weight": 9
            },
            {
              "name": "minecraft:eye_armor_trim_smithing_template",
              "type": "item",
              "weight": 1
            }
          ],
          "rolls": 1
        }
      }
    ]
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `chests/stronghold_library.json`

SHA-256 add-on `e8e52b4b31861a806b666a0b34816c7f464dc1858262d9ebd744fcc8836f6d3d`; образца `ea0475eb680f324d87b3c5ef8677575701c93b0704b07b11f2ef39b3c0fc0955`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [],
    "only_addon": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:book",
              "type": "item",
              "weight": 100
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 7,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:paper",
              "type": "item",
              "weight": 100
            },
            {
              "name": "minecraft:map",
              "type": "item",
              "weight": 5
            },
            {
              "name": "effect:lapis_sword",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:compass",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "function": "enchant_with_levels",
                  "levels": 30,
                  "treasure": true
                }
              ],
              "name": "minecraft:book",
              "type": "item",
              "weight": 60
            }
          ],
          "rolls": {
            "max": 10,
            "min": 2
          }
        }
      }
    ],
    "only_reference": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "functions": [
                {
                  "count": {
                    "max": 3,
                    "min": 1
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:book",
              "type": "item",
              "weight": 100
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 7,
                    "min": 2
                  },
                  "function": "set_count"
                }
              ],
              "name": "minecraft:paper",
              "type": "item",
              "weight": 100
            },
            {
              "name": "minecraft:map",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:compass",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "function": "enchant_with_levels",
                  "levels": 30,
                  "treasure": true
                }
              ],
              "name": "minecraft:book",
              "type": "item",
              "weight": 60
            }
          ],
          "rolls": {
            "max": 10,
            "min": 2
          }
        }
      },
      {
        "index": 1,
        "value": {
          "entries": [
            {
              "name": "minecraft:eye_armor_trim_smithing_template",
              "type": "item",
              "weight": 1
            }
          ],
          "rolls": 1
        }
      }
    ]
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `chests/underwater_ruin_big.json`

SHA-256 add-on `113741262d5adc8cc4c3f1cef22e880181c732810a8f5b0a40bb42dc2a412cc6`; образца `e33c5889bb2b0b001a25dc15075cce523fad96211d798aaace58ce982039a3e6`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [
      [
        0,
        0
      ]
    ],
    "only_addon": [
      {
        "index": 1,
        "value": {
          "entries": [
            {
              "name": "minecraft:golden_apple",
              "type": "item",
              "weight": 1
            },
            {
              "name": "effect:magma_sword",
              "type": "item",
              "weight": 1
            },
            {
              "functions": [
                {
                  "function": "enchant_randomly"
                }
              ],
              "name": "minecraft:book",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:leather_chestplate",
              "type": "item",
              "weight": 1
            },
            {
              "name": "minecraft:golden_helmet",
              "type": "item",
              "weight": 1
            },
            {
              "functions": [
                {
                  "function": "enchant_randomly"
                }
              ],
              "name": "minecraft:fishing_rod",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "destination": "buriedtreasure",
                  "function": "exploration_map"
                }
              ],
              "name": "minecraft:map",
              "type": "item",
              "weight": 10
            }
          ],
          "rolls": 1
        }
      }
    ],
    "only_reference": [
      {
        "index": 1,
        "value": {
          "entries": [
            {
              "name": "minecraft:golden_apple",
              "type": "item",
              "weight": 1
            },
            {
              "functions": [
                {
                  "function": "enchant_randomly"
                }
              ],
              "name": "minecraft:book",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:leather_chestplate",
              "type": "item",
              "weight": 1
            },
            {
              "name": "minecraft:golden_helmet",
              "type": "item",
              "weight": 1
            },
            {
              "functions": [
                {
                  "function": "enchant_randomly"
                }
              ],
              "name": "minecraft:fishing_rod",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "destination": "buriedtreasure",
                  "function": "exploration_map"
                }
              ],
              "name": "minecraft:map",
              "type": "item",
              "weight": 10
            }
          ],
          "rolls": 1
        }
      }
    ]
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `chests/village/village_snowy_house.json`

SHA-256 add-on `5f631d0acedc39681f943d6cbe6ed03a54c3a220af3554ab5545382775e93a4c`; образца `dbaad2883cda2284082e771afddb234752475ff93fb52600a3a67d90fe4ac2f5`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [],
    "only_addon": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "name": "minecraft:blue_ice",
              "type": "item"
            },
            {
              "name": "minecraft:snow",
              "type": "item",
              "weight": 4
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 7,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:potato",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 4,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:bread",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 5,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:beetroot_seeds",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:beetroot_soup",
              "type": "item"
            },
            {
              "name": "minecraft:furnace",
              "type": "item"
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 4,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:emerald",
              "type": "item"
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 7,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:snowball",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 1,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "effect:ice_sword",
              "type": "item",
              "weight": 4
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 4,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:coal",
              "type": "item",
              "weight": 5
            }
          ],
          "rolls": {
            "max": 8,
            "min": 3
          }
        }
      }
    ],
    "only_reference": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "name": "minecraft:blue_ice",
              "type": "item"
            },
            {
              "name": "minecraft:snow",
              "type": "item",
              "weight": 4
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 7,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:potato",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 4,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:bread",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 5,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:beetroot_seeds",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:beetroot_soup",
              "type": "item"
            },
            {
              "name": "minecraft:furnace",
              "type": "item"
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 4,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:emerald",
              "type": "item"
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 7,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:snowball",
              "type": "item",
              "weight": 10
            },
            {
              "functions": [
                {
                  "count": {
                    "max": 4,
                    "min": 1
                  },
                  "function": "minecraft:set_count"
                }
              ],
              "name": "minecraft:coal",
              "type": "item",
              "weight": 5
            }
          ],
          "rolls": {
            "max": 8,
            "min": 3
          }
        }
      }
    ]
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `chests/woodland_mansion.json`

SHA-256 add-on `02a72468bdf568a92c857631940d78f467841a02bb3ea09868c0d99ef002eb63`; образца `21ca7c61161ad9b283a840c177ced0cfbf8bd276b78ec6dd75003dcd32cb23b9`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [
      [
        1,
        1
      ],
      [
        2,
        2
      ]
    ],
    "only_addon": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "name": "minecraft:lead",
              "type": "item",
              "weight": 100
            },
            {
              "name": "minecraft:golden_apple",
              "type": "item",
              "weight": 75
            },
            {
              "name": "minecraft:appleEnchanted",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:record_13",
              "type": "item",
              "weight": 75
            },
            {
              "name": "minecraft:record_cat",
              "type": "item",
              "weight": 75
            },
            {
              "name": "minecraft:name_tag",
              "type": "item",
              "weight": 100
            },
            {
              "name": "minecraft:chainmail_chestplate",
              "type": "item",
              "weight": 50
            },
            {
              "name": "minecraft:diamond_hoe",
              "type": "item",
              "weight": 75
            },
            {
              "name": "minecraft:diamond_chestplate",
              "type": "item",
              "weight": 25
            },
            {
              "name": "effect:emerald_sword",
              "type": "item",
              "weight": 25
            },
            {
              "functions": [
                {
                  "function": "enchant_randomly",
                  "treasure": true
                }
              ],
              "name": "minecraft:book",
              "type": "item",
              "weight": 60
            }
          ],
          "rolls": {
            "max": 3,
            "min": 1
          }
        }
      }
    ],
    "only_reference": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "name": "minecraft:lead",
              "type": "item",
              "weight": 100
            },
            {
              "name": "minecraft:golden_apple",
              "type": "item",
              "weight": 75
            },
            {
              "name": "minecraft:appleEnchanted",
              "type": "item",
              "weight": 10
            },
            {
              "name": "minecraft:record_13",
              "type": "item",
              "weight": 75
            },
            {
              "name": "minecraft:record_cat",
              "type": "item",
              "weight": 75
            },
            {
              "name": "minecraft:name_tag",
              "type": "item",
              "weight": 100
            },
            {
              "name": "minecraft:chainmail_chestplate",
              "type": "item",
              "weight": 50
            },
            {
              "name": "minecraft:diamond_hoe",
              "type": "item",
              "weight": 75
            },
            {
              "name": "minecraft:diamond_chestplate",
              "type": "item",
              "weight": 25
            },
            {
              "functions": [
                {
                  "function": "enchant_randomly",
                  "treasure": true
                }
              ],
              "name": "minecraft:book",
              "type": "item",
              "weight": 60
            }
          ],
          "rolls": {
            "max": 3,
            "min": 1
          }
        }
      },
      {
        "index": 3,
        "value": {
          "entries": [
            {
              "type": "empty",
              "weight": 1
            },
            {
              "name": "minecraft:vex_armor_trim_smithing_template",
              "type": "item",
              "weight": 1
            }
          ],
          "rolls": 1
        }
      }
    ]
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `entities/blaze.json`

SHA-256 add-on `4a3aa8badbc60aed981951f1d7580362a98bfe57fb02cf39e13bea913a4f4d38`; образца `0c14613b63c3b564d14ce332d17f169e97a1ad2174f724aa36242220cd29a359`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [
      [
        0,
        0
      ]
    ],
    "only_addon": [
      {
        "index": 1,
        "value": {
          "conditions": [
            {
              "condition": "killed_by_entity",
              "entity_type": "minecraft:snow_golem"
            },
            {
              "chance": 0.025,
              "condition": "random_chance_with_looting",
              "looting_multiplier": 0.02
            }
          ],
          "entries": [
            {
              "functions": [
                {
                  "data": 0,
                  "function": "set_data"
                }
              ],
              "name": "effect:blaze_sword",
              "type": "item",
              "weight": 1
            }
          ],
          "rolls": 1
        }
      }
    ],
    "only_reference": []
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `entities/elder_guardian.json`

SHA-256 add-on `d4c4c9380d598ce9c87f8b6e6006ca2856103bd450f34607c254470d781547a1`; образца `8080edb9064abf581df782b46092c01e3805b3e9dc53a336d279da9845db57e4`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [
      [
        0,
        0
      ],
      [
        1,
        2
      ],
      [
        2,
        3
      ],
      [
        3,
        4
      ]
    ],
    "only_addon": [
      {
        "index": 1,
        "value": {
          "conditions": [
            {
              "condition": "killed_by_player"
            },
            {
              "chance": 0.065,
              "condition": "random_chance_with_looting",
              "looting_multiplier": 0.02
            }
          ],
          "entries": [
            {
              "functions": [
                {
                  "count": {
                    "max": 1,
                    "min": 1
                  },
                  "function": "set_count"
                },
                {
                  "data": 0,
                  "function": "set_data"
                }
              ],
              "name": "effect:sponge_sword",
              "type": "item",
              "weight": 1
            }
          ],
          "rolls": 1
        }
      }
    ],
    "only_reference": [
      {
        "index": 4,
        "value": {
          "entries": [
            {
              "type": "empty",
              "weight": 4
            },
            {
              "name": "minecraft:tide_armor_trim_smithing_template",
              "type": "item",
              "weight": 1
            }
          ],
          "rolls": 1
        }
      }
    ]
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `entities/shulker.json`

SHA-256 add-on `f68cd2a30a473a605fd04aa4ec81c592f098a882e8a32eabe54feca78a6e7aae`; образца `e83bc240e031698b372c98af93918f78e965d1228f4b1e6685fdc8c7888ff9c2`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [
      [
        0,
        0
      ]
    ],
    "only_addon": [
      {
        "index": 1,
        "value": {
          "conditions": [
            {
              "condition": "killed_by_player"
            },
            {
              "chance": 0.045,
              "condition": "random_chance_with_looting",
              "looting_multiplier": 0.02
            }
          ],
          "entries": [
            {
              "functions": [
                {
                  "count": {
                    "max": 1,
                    "min": 1
                  },
                  "function": "set_count"
                },
                {
                  "data": 0,
                  "function": "set_data"
                }
              ],
              "name": "effect:shulker_sword",
              "type": "item",
              "weight": 1
            }
          ],
          "rolls": 1
        }
      }
    ],
    "only_reference": []
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `entities/wither_skeleton.json`

SHA-256 add-on `27e3a5a47848d48de7d72acfab193587d8886b47f087d6214f09c39eeb7526c6`; образца `cebf3750c7dc2a254648a773a4895bafe57628a3d2aa7be242951e658ad2eeaf`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [
      [
        0,
        0
      ],
      [
        1,
        1
      ],
      [
        2,
        2
      ]
    ],
    "only_addon": [
      {
        "index": 3,
        "value": {
          "conditions": [
            {
              "condition": "killed_by_player"
            },
            {
              "chance": 0.025,
              "condition": "random_chance_with_looting",
              "looting_multiplier": 0.02
            }
          ],
          "entries": [
            {
              "functions": [
                {
                  "data": 0,
                  "function": "set_data"
                }
              ],
              "name": "effect:wither_skeleton_sword",
              "type": "item",
              "weight": 1
            }
          ],
          "rolls": 1
        }
      }
    ],
    "only_reference": []
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `gameplay/entities/mooshroom_milking.json`

SHA-256 add-on `ac6235b5017663111487fb45b9c0bf3e6fed109e8d53d0b242c3abc89c781d6b`; образца `63aff4bafe24e740bdd3fad0395fe54c96825413d5449873def7448d71f3ddcd`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [
      [
        0,
        0
      ],
      [
        1,
        1
      ],
      [
        2,
        2
      ],
      [
        3,
        3
      ],
      [
        4,
        4
      ],
      [
        5,
        5
      ],
      [
        6,
        6
      ],
      [
        7,
        7
      ],
      [
        8,
        8
      ],
      [
        9,
        9
      ],
      [
        10,
        10
      ]
    ],
    "only_addon": [],
    "only_reference": [
      {
        "index": 11,
        "value": {
          "conditions": [
            {
              "condition": "has_mark_variant",
              "value": 10
            }
          ],
          "entries": [
            {
              "functions": [
                {
                  "data": 10,
                  "function": "set_data"
                }
              ],
              "name": "minecraft:suspicious_stew",
              "type": "item",
              "weight": 1
            }
          ],
          "rolls": 1
        }
      }
    ]
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```

### `gameplay/fishing/treasure.json`

SHA-256 add-on `0459bb92fd47cab5f10e8c514d7b262854d8dab31c7b2efc1af13d839cae568e`; образца `5ac79eeb3122e9f2459c6f0087e55f83c49f292e5b2fb67bf589e1aaa1e02f0d`.

```json
{
  "other_fields": {},
  "pool_comparison": {
    "equal_pairs_reference_addon": [],
    "only_addon": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "name": "minecraft:nautilus_shell",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:waterlily",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:name_tag",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:saddle",
              "type": "item",
              "weight": 5
            },
            {
              "name": "effect:jungle_sword",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "damage": {
                    "max": 0.25,
                    "min": 0
                  },
                  "function": "set_damage"
                },
                {
                  "function": "enchant_with_levels",
                  "levels": 30,
                  "treasure": true
                }
              ],
              "name": "minecraft:bow",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "damage": {
                    "max": 0.25,
                    "min": 0
                  },
                  "function": "set_damage"
                },
                {
                  "function": "enchant_with_levels",
                  "levels": 30,
                  "treasure": true
                }
              ],
              "name": "minecraft:fishing_rod",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "function": "enchant_with_levels",
                  "levels": 30,
                  "treasure": true
                }
              ],
              "name": "minecraft:book",
              "type": "item",
              "weight": 6
            }
          ],
          "rolls": 1
        }
      }
    ],
    "only_reference": [
      {
        "index": 0,
        "value": {
          "entries": [
            {
              "name": "minecraft:nautilus_shell",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:waterlily",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:name_tag",
              "type": "item",
              "weight": 5
            },
            {
              "name": "minecraft:saddle",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "damage": {
                    "max": 0.25,
                    "min": 0
                  },
                  "function": "set_damage"
                },
                {
                  "function": "enchant_with_levels",
                  "levels": 30,
                  "treasure": true
                }
              ],
              "name": "minecraft:bow",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "damage": {
                    "max": 0.25,
                    "min": 0
                  },
                  "function": "set_damage"
                },
                {
                  "function": "enchant_with_levels",
                  "levels": 30,
                  "treasure": true
                }
              ],
              "name": "minecraft:fishing_rod",
              "type": "item",
              "weight": 5
            },
            {
              "functions": [
                {
                  "function": "enchant_with_levels",
                  "levels": 30,
                  "treasure": true
                }
              ],
              "name": "minecraft:book",
              "type": "item",
              "weight": 6
            }
          ],
          "rolls": 1
        }
      }
    ]
  },
  "pools_field": null,
  "pools_present": {
    "addon": true,
    "reference": true
  }
}
```
