# Контроллеры поведения и прямые связи — 2.8.14

Автоматическая выписка из behavior pack: оригинальный текст каждого файла контроллеров и буквальные связи `description.animations` у разбираемых сущностей. Команды/условия, порядок состояний и пробелы сохранены в блоках ниже; ни фактический запуск контроллера, ни семантика команд не доказаны. Повторяющиеся JSON-ключи и неразобранные файлы требуют проверки оригинала. Не охвачены ресурсные контроллеры и вложенные/динамические вызовы. Списки ссылок не являются полным графом.

## Диагностика

- `Swords_B/entities/creeper.json`: `<string>:430 Unexpected "}" at column 3`

## Все файлы контроллеров

### `Swords_B/animation_controllers/climb_spider.json`

Идентификаторы: `["controller.animation.climb_spider"]`.

Буквальные ссылки description.animations: `minecraft:spider` `Swords_B/entities/spider.json`: alias `climb_spider`, `scripts.animate` = `["despawn","climb_spider"]`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.climb_spider": {
      "states": {
        "default": {
          "transitions": [
            {
              "climb_spider": "q.has_rider"
            }
          ]
        },
        "climb_spider": {
          "on_entry": [
            "/effect @s levitation 10 3 true"
          ],
          "transitions": [
            {
              "default": "1.0"
            }
          ]
        }
      }
    }
  }
}
```

### `Swords_B/animation_controllers/despawn.json`

Идентификаторы: `["controller.animation.despawn","controller.animation.despawn_crystal","controller.animation.mount_crystal","controller.animation.despawn_wolf","controller.animation.despawn2"]`.

Буквальные ссылки description.animations: `entity:alpha_wolf` `Swords_B/entities/alpha_wolf.json`: alias `despawn_wolf`, `scripts.animate` = `["despawn_wolf"]`; `entity:mountable_slime` `Swords_B/entities/mountable_slime.json`: alias `despawn`, `scripts.animate` = `["despawn","mountable_slime"]`; `entity:name` `Swords_B/entities/entity_name.json`: alias `despawn2`, `scripts.animate` = `["despawn2"]`; `entity:shulker_shield` `Swords_B/entities/shulker_shield.json`: alias `despawn`, `scripts.animate` = `["despawn"]`; `minecraft:ender_crystal` `Swords_B/entities/ender_crystal.json`: alias `despawn_crystal`, `scripts.animate` = `["despawn_crystal","mount_crystal"]`; `minecraft:ender_crystal` `Swords_B/entities/ender_crystal.json`: alias `mount_crystal`, `scripts.animate` = `["despawn_crystal","mount_crystal"]`; `minecraft:spider` `Swords_B/entities/spider.json`: alias `despawn`, `scripts.animate` = `["despawn","climb_spider"]`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.despawn": {
      "states": {
        "default": {
          "transitions": [
            {
              "despawn": "!q.has_rider"
            }
          ]
        },
        "despawn": {
          "on_entry": [
            "@s minecraft:despawn"
          ],
          "transitions": [
            {
              "default": "1.0"
            }
          ]
        }
      }
    },
    "controller.animation.despawn_crystal": {
      "states": {
        "default": {
          "transitions": [
            {
              "despawn_crystal": "!q.is_riding"
            }
          ]
        },
        "despawn_crystal": {
          "on_entry": [
            "@s minecraft:despawn"
          ],
          "transitions": [
            {
              "default": "1.0"
            }
          ]
        }
      }
    },
    "controller.animation.mount_crystal": {
      "states": {
        "default": {
          "transitions": [
            {
              "mount_crystal": "q.is_riding"
            }
          ]
        },
        "mount_crystal": {
          "on_entry": [
            "@s minecraft:mount_crystal"
          ],
          "transitions": [
            {
              "default": "1.0"
            }
          ]
        }
      }
    },
    "controller.animation.despawn_wolf": {
      "states": {
        "default": {
          "transitions": [
            {
              "despawn": "(!q.moon_phase == 0 && !q.time_of_day <= 0.20 || !q.time_of_day >= 0.80)"
            }
          ]
        },
        "despawn": {
          "on_entry": [
            "@s despawn"
          ],
          "transitions": [
            {
              "default": "1.0"
            }
          ]
        }
      }
    },
    "controller.animation.despawn2": {
      "states": {
        "default": {
          "transitions": [
            {
              "despawn2": "!q.is_riding"
            }
          ]
        },
        "despawn2": {
          "on_entry": [
            "@s minecraft:despawn"
          ],
          "transitions": [
            {
              "default": "1.0"
            }
          ]
        }
      }
    }
  }
}
```

### `Swords_B/animation_controllers/ghost_sword.json`

Идентификаторы: `["controller.animation.ghost_sword"]`.

Буквальные ссылки description.animations: `minecraft:player` `Swords_B/entities/player.json`: alias `ghost_sword`, `scripts.animate` = `["shulker_sword","wither_sword","wolf_sword_0","wolf_sword_1","wolf_sword_2","ghost_sword"]`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.ghost_sword": {
      "states": {
        "default": {
          "transitions": [
            {
              "levitation_ghost": "q.get_equipped_item_name=='ghost_sword' && q.is_sneaking"
            },
            {
              "default_ghost": "q.get_equipped_item_name=='ghost_sword' && !q.is_sneaking"
            }
          ]
        },
        "levitation_ghost": {
          "on_entry": [
            "/effect @s levitation 1 3 true"
          ],
          "transitions": [
            {
              "default": "1.0"
            }
          ]
        },
        "default_ghost": {
          "on_entry": [
            "/effect @s levitation 0 0"
          ],
          "transitions": [
            {
              "default": "1.0"
            }
          ]
        }
      }
    }
  }
}
```

### `Swords_B/animation_controllers/item_events.json`

Идентификаторы: `["controller.animation.item_events"]`.

Буквальные ссылки description.animations: `minecraft:item` `Swords_B/entities/item.json`: alias `on_fire_swords`, `scripts.animate` = `["on_fire_swords"]`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.item_events": {
      "states": {
        "default": {
          "transitions": [
            {
              "on_fire_swords": "q.is_on_fire"
            }
          ]
        },
        "on_fire_swords": {
          "on_entry": [
            "/event entity @s[tag=fire_sword,tag=!fire_sword_respawn] fire_sword_event_3",
            "/event entity @s[tag=tnt_sword] despawn_event_5",
            "/event entity @s[tag=ice_sword] despawn_event_4",
            "/event entity @s[tag=ender_sword] despawn_event_1",
            "/event entity @s[tag=wither_sword] despawn_event_2",
            "/event entity @s[tag=lightning_sword] despawn_event_3",
            "/event entity @s[tag=nether_star_sword] despawn_event_6",
            "/event entity @s[tag=bedrock_sword] respawn_event_1",
            "/event entity @s[tag=fire_sword_respawn] respawn_event_2"
          ],
          "transitions": [
            {
              "default": "1.0"
            }
          ]
        }
      }
    }
  }
}
```

### `Swords_B/animation_controllers/mountable_slime.json`

Идентификаторы: `["controller.animation.mountable_slime"]`.

Буквальные ссылки description.animations: `entity:mountable_slime` `Swords_B/entities/mountable_slime.json`: alias `mountable_slime`, `scripts.animate` = `["despawn","mountable_slime"]`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.mountable_slime": {
      "states": {
        "default": {
          "transitions": [
            {
              "mountable_slime": "q.has_rider"
            }
          ]
        },
        "mountable_slime": {
          "on_entry": [
            "@s default_slime"
          ],
          "transitions": [
            {
              "default": "1.0"
            }
          ]
        }
      }
    }
  }
}
```

### `Swords_B/animation_controllers/shulker_sword.json`

Идентификаторы: `["controller.animation.shulker_sword"]`.

Буквальные ссылки description.animations: `minecraft:player` `Swords_B/entities/player.json`: alias `shulker_sword`, `scripts.animate` = `["shulker_sword","wither_sword","wolf_sword_0","wolf_sword_1","wolf_sword_2","ghost_sword"]`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.shulker_sword": {
      "states": {
        "default": {
          "transitions": [
            {
              "shulker_sword": "q.get_equipped_item_name=='shulker_sword' && q.is_sneaking"
            }
          ]
        },
        "shulker_sword": {
          "on_entry": [
            "@s shulker_sword_skill"
          ],
          "transitions": [
            {
              "default": "1.0"
            }
          ]
        }
      }
    }
  }
}
```

### `Swords_B/animation_controllers/wither_sword.json`

Идентификаторы: `["controller.animation.wither_sword"]`.

Буквальные ссылки description.animations: `minecraft:player` `Swords_B/entities/player.json`: alias `wither_sword`, `scripts.animate` = `["shulker_sword","wither_sword","wolf_sword_0","wolf_sword_1","wolf_sword_2","ghost_sword"]`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.wither_sword": {
      "states": {
        "default": {
          "transitions": [
            {
              "wither_sword": "q.get_equipped_item_name=='wither_sword'"
            }
          ]
        },
        "wither_sword": {
          "on_entry": [
            "/ride @s summon_rider entity:name minecraft:wither_sword"
          ],
          "transitions": [
            {
              "default": "1.0"
            }
          ]
        }
      }
    }
  }
}
```

### `Swords_B/animation_controllers/wolf_sword.json`

Идентификаторы: `["controller.animation.wolf_sword","controller.animation.start_wolf_sword","controller.animation.end_wolf_sword"]`.

Буквальные ссылки description.animations: `minecraft:player` `Swords_B/entities/player.json`: alias `wolf_sword_1`, `scripts.animate` = `["shulker_sword","wither_sword","wolf_sword_0","wolf_sword_1","wolf_sword_2","ghost_sword"]`; `minecraft:player` `Swords_B/entities/player.json`: alias `wolf_sword_2`, `scripts.animate` = `["shulker_sword","wither_sword","wolf_sword_0","wolf_sword_1","wolf_sword_2","ghost_sword"]`; `minecraft:player` `Swords_B/entities/player.json`: alias `wolf_sword_0`, `scripts.animate` = `["shulker_sword","wither_sword","wolf_sword_0","wolf_sword_1","wolf_sword_2","ghost_sword"]`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.wolf_sword": {
      "states": {
        "wolf_transformation": {
          "transitions": [
            {
              "wolf_sword": "q.get_equipped_item_name('main_hand') == 'wolf_sword' && q.moon_phase == 0 && (q.time_of_day >= 0.77 && q.time_of_day <= 0.78)"
            }
          ]
        },
        "wolf_sword": {
          "on_entry": [
            "@s wolf_sword_start_events"
          ],
          "transitions": [
            {
              "wolf_transformation": "1.0"
            }
          ]
        }
      }
    },
    "controller.animation.start_wolf_sword": {
      "states": {
        "start_wolf_transformation": {
          "transitions": [
            {
              "wolf_sword_start": "q.get_equipped_item_name('main_hand') == 'wolf_sword' && q.moon_phase == 0 && (q.time_of_day <= 0.20 || q.time_of_day >= 0.80)"
            }
          ]
        },
        "wolf_sword_start": {
          "on_entry": [
            "@s wolf_transformation"
          ],
          "transitions": [
            {
              "start_wolf_transformation": "1.0"
            }
          ]
        }
      }
    },
    "controller.animation.end_wolf_sword": {
      "states": {
        "end_wolf_transformation": {
          "transitions": [
            {
              "wolf_sword_end": "q.get_equipped_item_name('main_hand') == 'wolf_sword' || q.get_equipped_item_name('main_hand') != 'wolf_sword' && q.moon_phase == 0 && q.time_of_day == 0.20"
            }
          ]
        },
        "wolf_sword_end": {
          "on_entry": [
            "@s stop_wolf_transformation"
          ],
          "transitions": [
            {
              "end_wolf_transformation": "1.0"
            }
          ]
        }
      }
    }
  }
}
```

