# Контроллеры поведения и прямые связи — 1.6

Автоматическая выписка из behavior pack: оригинальный текст каждого файла контроллеров и буквальные связи `description.animations` у разбираемых сущностей. Команды/условия, порядок состояний и пробелы сохранены в блоках ниже; ни фактический запуск контроллера, ни семантика команд не доказаны. Повторяющиеся JSON-ключи и неразобранные файлы требуют проверки оригинала. Не охвачены ресурсные контроллеры и вложенные/динамические вызовы. Списки ссылок не являются полным графом.

## Диагностика

- `Sword_B/entities/blaze2.json`: `<string>:78 Unexpected "}" at column 1`
- `Sword_B/entities/bone2.json`: `<string>:75 Unexpected "}" at column 1`
- `Sword_B/entities/shulker2.json`: `<string>:75 Unexpected "}" at column 1`

## Все файлы контроллеров

### `Sword_B/animation_controllers/blaze_sword.json`

Идентификаторы: `["controller.animation.blaze"]`.

Буквальные ссылки description.animations: `entity:blaze` `Sword_B/entities/blaze.json`: alias `blaze`, `scripts.animate` = `["blaze"]`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.blaze": {
      "states": {
        "default": {
          "transitions": [
            {
              "blaze": "(1.0)"
            }
          ],
          "on_entry": [
          	"/execute @p ~ ~ ~ tp @e[type=entity:blaze2] ~ ~2 ~",
            "/scoreboard objectives add b dummy",
            "/scoreboard players add @p b 1",
            "/execute @p[scores={b=10}] ~ ~ ~ summon entity:blaze2",
            "/execute @p[scores={b=5000}] ~ ~ ~ scoreboard objectives remove b",
            "/execute @p[scores={b=4990}] ~ ~ ~ kill @e[type=entity:blaze2,r=5] ~ 0 ~",
            "/scoreboard players set @a swords 2"
          ]
        },
        "blaze": {
          "transitions": [
            {
              "default": "(1.0)"
            }
          ],
          "on_entry": [
            "/execute @p ~ ~ ~ tp @e[type=entity:blaze2] ~ ~2 ~",
            "/scoreboard objectives add b dummy",
            "/scoreboard players add @p b 1",
            "/execute @p[scores={b=10}] ~ ~ ~ summon entity:blaze2",
            "/execute @p[scores={b=5000}] ~ ~ ~ scoreboard objectives remove b",
            "/execute @p[scores={b=4990}] ~ ~ ~ kill @e[type=entity:blaze2,r=5] ~ 0 ~",
            "/scoreboard players set @a swords 2"

          ]
        }
      }
    }
  }
}
```

### `Sword_B/animation_controllers/bone_sword.json`

Идентификаторы: `["controller.animation.bone"]`.

Буквальные ссылки description.animations: `entity:bone` `Sword_B/entities/bone.json`: alias `bone`, `scripts.animate` = `["bone"]`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.bone": {
      "states": {
        "default": {
          "transitions": [
            {
              "bone": "(1.0)"
            }
          ],
          "on_entry": [
          	"/execute @p ~ ~ ~ tp @e[type=entity:bone2] ~ ~2 ~",
            "/scoreboard objectives add bn dummy",
            "/scoreboard players add @p bn 1",
            "/execute @p[scores={bn=10}] ~ ~ ~ summon entity:bone2",
            "/execute @p[scores={bn=5000}] ~ ~ ~ scoreboard objectives remove bn",
            "/execute @p[scores={bn=4990}] ~ ~ ~ kill @e[type=entity:bone2,r=5] ~ 0 ~",
            "/scoreboard players set @a swords 2"
          ]
        },
        "bone": {
          "transitions": [
            {
              "default": "(1.0)"
            }
          ],
          "on_entry": [
            "/execute @p ~ ~ ~ tp @e[type=entity:bone2] ~ ~2 ~",
            "/scoreboard objectives add bn dummy",
            "/scoreboard players add @p bn 1",
            "/execute @p[scores={bn=10}] ~ ~ ~ summon entity:bone2",
            "/execute @p[scores={bn=5000}] ~ ~ ~ scoreboard objectives remove bn",
            "/execute @p[scores={bn=4990}] ~ ~ ~ kill @e[type=entity:bone2,r=5] ~ 0 ~",
            "/scoreboard players set @a swords 2"

          ]
        }
      }
    }
  }
}
```

### `Sword_B/animation_controllers/cactus_sword.json`

Идентификаторы: `["controller.animation.cactus"]`.

Буквальные ссылки description.animations: `entity:cactus` `Sword_B/entities/cactus.json`: alias `cactus`, `scripts.animate` = `["cactus"]`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.cactus": {
      "states": {
        "default": {
          "transitions": [
            {
              "cactus": "(1.0)"
            }
          ],
          "on_entry": [
          	"/scoreboard objectives add ct dummy",
            "/scoreboard players add @p ct 1",
            "/scoreboard players add @e[r=3,type=!entity:cactus,type=!player] ct 1",
            "/execute @p[scores={ct=1}] ~ ~ ~ effect @s poison 1 1 true",
            "/execute @e[scores={ct=1},r=2] ~ ~ ~ effect @s poison 1 1 true",
            "/execute @p[scores={ct=20}] ~ ~ ~ scoreboard objectives remove ct",
            "/scoreboard players set @a swords 2"
          ]
        },
        "cactus": {
          "transitions": [
            {
              "default": "(1.0)"
            }
          ],
          "on_entry": [
            "/scoreboard objectives add ct dummy",
            "/scoreboard players add @p ct 1",
            "/scoreboard players add @e[r=3,type=!entity:cactus,type=!player] ct 1",
            "/execute @p[scores={ct=1}] ~ ~ ~ effect @s poison 1 1 true",
            "/execute @e[scores={ct=1},r=2] ~ ~ ~ effect @s poison 1 1 true",
            "/execute @p[scores={ct=20}] ~ ~ ~ scoreboard objectives remove ct",
            "/scoreboard players set @a swords 2"
          ]
        }
      }
    }
  }
}
```

### `Sword_B/animation_controllers/coal_sword.json`

Идентификаторы: `["controller.animation.coal"]`.

Буквальные ссылки description.animations: `entity:coal` `Sword_B/entities/coal.json`: alias `coal`, `scripts.animate` = `["coal"]`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.coal": {
      "states": {
        "default": {
          "transitions": [
            {
              "coal": "(1.0)"
            }
          ],
          "on_entry": [
          	"/replaceitem block ~-1 ~ ~ slot.container 1 coal",
          	"/replaceitem block ~1 ~ ~ slot.container 1 coal",
          	"/replaceitem block ~ ~ ~-1 slot.container 1 coal",
          	"/replaceitem block ~ ~ ~1 slot.container 1 coal",
          	"/replaceitem block ~ ~-1 ~ slot.container 1 coal",
            "/replaceitem block ~-1 ~1 ~ slot.container 1 coal",
          	"/replaceitem block ~1 ~1 ~ slot.container 1 coal",
          	"/replaceitem block ~ ~1 ~-1 slot.container 1 coal",
          	"/replaceitem block ~ ~1 ~1 slot.container 1 coal",
          	"/replaceitem block ~-1 ~-1 ~ slot.container 1 coal",
          	"/replaceitem block ~1 ~-1 ~ slot.container 1 coal",
          	"/replaceitem block ~ ~-1 ~-1 slot.container 1 coal",
          	"/replaceitem block ~ ~-1 ~1 slot.container 1 coal",
            "/scoreboard players set @a swords 2"
          ]
        },
        "coal": {
          "transitions": [
            {
              "default": "(1.0)"
            }
          ],
          "on_entry": [
          	"/replaceitem block ~-1 ~ ~ slot.container 1 coal",
          	"/replaceitem block ~1 ~ ~ slot.container 1 coal",
          	"/replaceitem block ~ ~ ~-1 slot.container 1 coal",
          	"/replaceitem block ~ ~ ~1 slot.container 1 coal",
          	"/replaceitem block ~ ~-1 ~ slot.container 1 coal",
            "/replaceitem block ~-1 ~1 ~ slot.container 1 coal",
          	"/replaceitem block ~1 ~1 ~ slot.container 1 coal",
          	"/replaceitem block ~ ~1 ~-1 slot.container 1 coal",
          	"/replaceitem block ~ ~1 ~1 slot.container 1 coal",
          	"/replaceitem block ~-1 ~-1 ~ slot.container 1 coal",
          	"/replaceitem block ~1 ~-1 ~ slot.container 1 coal",
          	"/replaceitem block ~ ~-1 ~-1 slot.container 1 coal",
          	"/replaceitem block ~ ~-1 ~1 slot.container 1 coal",
            "/scoreboard players set @a swords 2"

          ]
        }
      }
    }
  }
}
```

### `Sword_B/animation_controllers/creeper_sword.json`

Идентификаторы: `["controller.animation.creeper"]`.

Буквальные ссылки description.animations: `entity:creeper` `Sword_B/entities/creeper.json`: alias `creeper`, `scripts.animate` = `["creeper"]`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.creeper": {
      "states": {
        "default": {
          "transitions": [
            {
              "creeper": "(1.0)"
            }
          ],
          "on_entry": [
            "/scoreboard objectives add c dummy",
            "/scoreboard players add @e[r=16] c 1",
            "/playsound mob.creeper.say @p[scores={c=90}]",
            "/execute @e[scores={c=100},r=16,type=zombie] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=husk] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=drowned] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=enderman] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=slime] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=skeleton] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=stray] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=blaze] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=wither_skeleton] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=witch] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=magma_cube] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=ghast] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=zombie_pigman] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=spider] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=cave_spider] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=silverfish] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=evocation_fang] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=evocation_illager] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=vex] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=ravager] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=endermite] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=guardian] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=vindicator] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=phantom] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=tnt] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=zombie_villager] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=wither] ~ ~ ~ summon entity:explode",
            "/execute @p[scores={c=300}] ~ ~ ~ scoreboard objectives remove c",
            "/scoreboard players set @a swords 2"
          ]
        },
        "creeper": {
          "transitions": [
            {
              "default": "(1.0)"
            }
          ],
          "on_entry": [
            "/scoreboard objectives add c dummy",
            "/scoreboard players add @e[r=16] c 1",
            "/playsound mob.creeper.say @p[scores={c=90}]",
            "/execute @e[scores={c=100},r=16,type=zombie] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=husk] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=drowned] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=enderman] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=slime] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=skeleton] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=stray] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=blaze] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=wither_skeleton] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=witch] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=magma_cube] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=ghast] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=zombie_pigman] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=spider] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=cave_spider] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=silverfish] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=evocation_fang] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=evocation_illager] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=vex] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=ravager] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=endermite] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=guardian] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=vindicator] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=phantom] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=tnt] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=zombie_villager] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={c=100},r=16,type=wither] ~ ~ ~ summon entity:explode",
            "/execute @p[scores={c=300}] ~ ~ ~ scoreboard objectives remove c",
            "/scoreboard players set @a swords 2"
          ]
        }
      }
    }
  }
}
```

### `Sword_B/animation_controllers/emerald_sword.json`

Идентификаторы: `["controller.animation.emerald"]`.

Буквальные ссылки description.animations: `entity:emerald` `Sword_B/entities/emerald.json`: alias `emerald`, `scripts.animate` = `["emerald"]`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.emerald": {
      "states": {
        "default": {
          "transitions": [
            {
              "emerald": "(1.0)"
            }
          ],
          "on_entry": [
          	"/effect @p village_hero 16 0 true",
            "/scoreboard players set @a swords 2"
          ]
        },
        "emerald": {
          "transitions": [
            {
              "default": "(1.0)"
            }
          ],
          "on_entry": [
          	"/effect @p village_hero 16 0 true",
            "/scoreboard players set @a swords 2"
          ]
        }
      }
    }
  }
}
```

### `Sword_B/animation_controllers/ender_sword.json`

Идентификаторы: `["controller.animation.ender"]`.

Буквальные ссылки description.animations: `entity:ender` `Sword_B/entities/ender.json`: alias `ender`, `scripts.animate` = `["ender"]`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.ender": {
      "states": {
        "default": {
          "transitions": [
            {
              "ender": "(1.0)"
            }
          ],
          "on_entry": [
          	"/execute @p ~ ~ ~ particle minecraft:basic_portal_particle ~ ~1 ~",
          	"/execute @p ~ ~ ~ particle minecraft:end_chest ~ ~1 ~",
          	"/scoreboard objectives add e dummy",
            "/scoreboard players add @e[r=16] e 1",
            "/playsound mob.endermen.scream @p[scores={e=10}]",
            "/playsound mob.endermen.portal @p[scores={e=90}]",
            "/playsound mob.endermen.hit @p[scores={e=140}]",
            "/playsound mob.endermen.idle @p[scores={e=300}]",
            "/playsound mob.endermen.stare @p[scores={e=500}]",
            "/execute @p[scores={e=700}] ~ ~ ~ scoreboard objectives remove e",
            "/execute @p[scores={e=750}] ~ ~ ~ scoreboard objectives remove e",
            "/execute @p[scores={e=85}] ~ ~ ~ spreadplayers ~ ~ 8 16 @s",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=zombie]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=husk]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=drowned]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=creeper]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=enderman]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=slime]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=skeleton]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=stray]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=blaze]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=wither_skeleton]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=witch]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=magma_cube]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=ghast]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=zombie_pigman]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=spider]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=cave_spider]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=silverfish]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=evocation_fang]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=evocation_illager]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=vex]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=ravager]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=endermite]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=guardian]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=vindicator]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=phantom]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=tnt]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=zombie_villager]",
            "/scoreboard players set @a swords 2"
          ]
        },
        "ender": {
          "transitions": [
            {
              "default": "(1.0)"
            }
          ],
          "on_entry": [
            "/execute @p ~ ~ ~ particle minecraft:basic_portal_particle ~ ~1 ~",
          	"/execute @p ~ ~ ~ particle minecraft:end_chest ~ ~1 ~",
          	"/scoreboard objectives add e dummy",
            "/scoreboard players add @e[r=16] e 1",
            "/playsound mob.endermen.scream @p[scores={e=10}]",
            "/playsound mob.endermen.portal @p[scores={e=90}]",
            "/playsound mob.endermen.hit @p[scores={e=140}]",
            "/playsound mob.endermen.idle @p[scores={e=300}]",
            "/playsound mob.endermen.stare @p[scores={e=500}]",
            "/execute @p[scores={e=700}] ~ ~ ~ scoreboard objectives remove e",
            "/execute @p[scores={e=750}] ~ ~ ~ scoreboard objectives remove e",
            "/execute @p[scores={e=85}] ~ ~ ~ spreadplayers ~ ~ 8 16 @s",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=zombie]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=husk]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=drowned]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=creeper]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=enderman]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=slime]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=skeleton]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=stray]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=blaze]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=wither_skeleton]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=witch]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=magma_cube]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=ghast]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=zombie_pigman]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=spider]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=cave_spider]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=silverfish]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=evocation_fang]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=evocation_illager]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=vex]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=ravager]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=endermite]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=guardian]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=vindicator]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=phantom]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=tnt]",
            "/execute @p ~ ~ ~ spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=zombie_villager]",
            "/scoreboard players set @a swords 2"
          ]
        }
      }
    }
  }
}
```

### `Sword_B/animation_controllers/fire_sword.json`

Идентификаторы: `["controller.animation.fire"]`.

Буквальные ссылки description.animations: `entity:fire` `Sword_B/entities/fire.json`: alias `fire`, `scripts.animate` = `["fire"]`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.fire": {
      "states": {
        "default": {
          "transitions": [
            {
              "fire": "(1.0)"
            }
          ],
          "on_entry": [
          	"/effect @p fire_resistance 10 0 true",
          	"/execute @p ~ ~ ~ detect ~ ~ ~ air 0 setblock ~ ~ ~ fire",
          	"/execute @p ~ ~ ~ fill ~3 ~3 ~3 ~-3 ~-3 ~-3 air 0 replace snow_layer",
          	"/execute @p ~ ~ ~ fill ~3 ~3 ~3 ~-3 ~-3 ~-3 water 0 replace ice",
          	"/execute @p ~ ~ ~ fill ~3 ~3 ~3 ~-3 ~-3 ~-3 water 0 replace blue_ice",
          	"/execute @p ~ ~ ~ fill ~3 ~3 ~3 ~-3 ~-3 ~-3 water 0 replace packed_ice",
          	"/execute @p ~ ~ ~ fill ~3 ~3 ~3 ~-3 ~-3 ~-3 grass 0 replace snow",
            "/execute @e[r=15,rm=2,type=zombie] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=husk] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=drowned] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=creeper] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=enderman] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=slime] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=skeleton] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=stray] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=witch] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=spider] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=cave_spider] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=silverfish] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=evocation_fang] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=evocation_illager] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=vex] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=ravager] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=endermite] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=guardian] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=vindicator] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=phantom] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=cow] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=pig] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=chicken] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=horse] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=rabbit] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=sheep] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=fox] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=bat] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=polar_bear] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=villager] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=zombie_villager] ~ ~ ~ setblock ~ ~ ~ fire",
            "/scoreboard players set @a swords 2"



          ]
        },
        "fire": {
          "transitions": [
            {
              "default": "(1.0)"
            }
          ],
          "on_entry": [
          	"/effect @p fire_resistance 10 0 true",
          	"/execute @p ~ ~ ~ detect ~ ~ ~ air 0 setblock ~ ~ ~ fire",
          	"/execute @p ~ ~ ~ fill ~3 ~3 ~3 ~-3 ~-3 ~-3 air 0 replace snow_layer",
          	"/execute @p ~ ~ ~ fill ~3 ~3 ~3 ~-3 ~-3 ~-3 water 0 replace ice",
          	"/execute @p ~ ~ ~ fill ~3 ~3 ~3 ~-3 ~-3 ~-3 water 0 replace blue_ice",
          	"/execute @p ~ ~ ~ fill ~3 ~3 ~3 ~-3 ~-3 ~-3 water 0 replace packed_ice",
          	"/execute @p ~ ~ ~ fill ~3 ~3 ~3 ~-3 ~-3 ~-3 grass 0 replace snow",
            "/execute @e[r=15,rm=2,type=zombie] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=husk] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=drowned] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=creeper] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=enderman] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=slime] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=skeleton] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=stray] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=witch] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=spider] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=cave_spider] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=silverfish] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=evocation_fang] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=evocation_illager] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=vex] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=ravager] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=endermite] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=guardian] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=vindicator] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=phantom] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=cow] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=pig] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=chicken] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=horse] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=rabbit] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=sheep] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=fox] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=bat] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=polar_bear] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=villager] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=zombie_villager] ~ ~ ~ setblock ~ ~ ~ fire",
            "/scoreboard players set @a swords 2"
          ]
        }
      }
    }
  }
}
```

### `Sword_B/animation_controllers/glowstone_sword.json`

Идентификаторы: `["controller.animation.glow"]`.

Буквальные ссылки description.animations: `entity:glow` `Sword_B/entities/glowstone_sword.json`: alias `glow`, `scripts.animate` = `["glow"]`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.glow": {
      "states": {
        "default": {
          "transitions": [
            {
              "glow": "(1.0)"
            }
          ],
          "on_entry": [
          	"/execute @p ~~~ fill ~ ~1 ~ ~ ~1 ~ light_block 15 replace air",
          	"/execute @p ~~~ fill ~5 ~5 ~5 ~-5 ~-5 ~-5 air 0 replace light_block 15",
          	"/execute @p ~~~ fill ~ ~1 ~ ~ ~1 ~ light_block 15 replace air",
            "/scoreboard players set @a swords 2"
          ]
        },
        "glow": {
          "transitions": [
            {
              "default": "(1.0)"
            }
          ],
          "on_entry": [
          	"/execute @p ~~~ fill ~ ~1 ~ ~ ~1 ~ light_block 15 replace air",
          	"/execute @p ~~~ fill ~5 ~5 ~5 ~-5 ~-5 ~-5 air 0 replace light_block 15",
          	"/execute @p ~~~ fill ~ ~1 ~ ~ ~1 ~ light_block 15 replace air",
            "/scoreboard players set @a swords 2"
          ]
        }
      }
    }
  }
}
```

### `Sword_B/animation_controllers/grass_sword.json`

Идентификаторы: `["controller.animation.grass"]`.

Буквальные ссылки description.animations: `entity:grass` `Sword_B/entities/grass.json`: alias `grass`, `scripts.animate` = `["grass"]`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.grass": {
      "states": {
        "default": {
          "transitions": [
            {
              "grass": "(1.0)"
            }
          ],
          "on_entry": [
            "/execute @a ~ ~ ~ detect ~ ~ ~ air 0 fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 grass 0 replace dirt",
            "/execute @a ~ ~ ~ detect ~ ~-1 ~ grass 0 fill ~ ~ ~ ~ ~ ~ tallgrass 0 replace air",
            "/execute @e[r=10] ~ ~ ~ detect ~ ~-1 ~ grass 0 fill ~ ~ ~ ~ ~ ~ tallgrass 0 replace air",
            "/scoreboard players set @a swords 2"
          ]
        },
        "grass": {
          "transitions": [
            {
              "default": "(1.0)"
            }
          ],
          "on_entry": [
            "/execute @a ~ ~ ~ detect ~ ~ ~ air 0 fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 grass 0 replace dirt",
            "/execute @a ~ ~ ~ detect ~ ~-1 ~ grass 0 fill ~ ~ ~ ~ ~ ~ tallgrass 0 replace air",
            "/execute @e[r=10] ~ ~ ~ detect ~ ~-1 ~ grass 0 fill ~ ~ ~ ~ ~ ~ tallgrass 0 replace air",
            "/scoreboard players set @a swords 2"
          ]
        }
      }
    }
  }
}
```

### `Sword_B/animation_controllers/ice_sword.json`

Идентификаторы: `["controller.animation.ice"]`.

Буквальные ссылки description.animations: `entity:ice` `Sword_B/entities/ice.json`: alias `ice`, `scripts.animate` = `["ice"]`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.ice": {
      "states": {
        "default": {
          "transitions": [
            {
              "ice": "(1.0)"
            }
          ],
          "on_entry": [
            "/Effect99"
          ]
        },
        "ice": {
          "transitions": [
            {
              "default": "(1.0)"
            }
          ],
          "on_entry": [
            "/execute @a ~ ~ ~ detect ~ ~ ~ air 0 fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 ice 0 replace water 0",
            "/execute @a ~ ~ ~ detect ~ ~ ~ air 0 fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 ice 0 replace flowing_water 0",
            "/execute @e[type=zombie,rm=5,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 ice 0 replace air 0",
            "/execute @e[type=creeper,rm=5,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 ice 0 replace air 0",
            "/execute @e[type=zombie_villager,rm=5,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 ice 0 replace air 0",
            "/execute @e[type=phantom,rm=5,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 ice 0 replace air 0",
            "/execute @e[type=witch,rm=5,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 ice 0 replace air 0",
            "/execute @e[type=skeleton,rm=5,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 ice 0 replace air 0",
            "/execute @e[type=stray,rm=5,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 ice 0 replace air 0",
            "/execute @e[type=husk,rm=5,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 ice 0 replace air 0",
            "/execute @e[type=drowned,rm=5,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 ice 0 replace air 0",
            "/execute @e[type=enderman,rm=5,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~3 ~-1 ice 0 replace air 0",
            "/execute @e[type=silverfish,rm=5,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 ice 0 replace air 0",
            "/execute @e[type=spider,rm=5,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 ice 0 replace air 0",
            "/execute @e[type=cave_spider,rm=5,r=12] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 ice 0 replace air 0",
            "/execute @e[r=12,rm=5,type=slime] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 ice 0 replace air 0",
            "/execute @e[r=12,rm=5,type=slime] ~ ~ ~ detect ~ ~ ~ ice 0 tp @s ~ ~ ~",
            "/execute @e[r=12,rm=5,type=evocation_fang] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 ice 0 replace air 0",
            "/execute @e[r=12,rm=5,type=evocation_illager] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 ice 0 replace air 0",
            "/execute @e[r=12,rm=5,type=vex] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 ice 0 replace air 0",
            "/execute @e[r=12,rm=5,type=ravager] ~ ~ ~ fill ~2 ~-1 ~2 ~-2 ~2 ~-2 ice 0 replace air 0",
            "/execute @e[r=12,rm=5,type=endermite] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 ice 0 replace air 0",
            "/execute @e[r=12,rm=5,type=guardian] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 ice 0 replace air 0",
            "/execute @e[r=12,rm=5,type=vindicator] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~2 ~-1 ice 0 replace air 0",
            "/execute @e[r=12,rm=5,type=tnt] ~ ~ ~ fill ~1 ~-1 ~1 ~-1 ~1 ~-1 ice 0 replace air 0",
            "/scoreboard players set @a swords 2"
          ]
        }
      }
    }
  }
}
```

### `Sword_B/animation_controllers/jungle_sword.json`

Идентификаторы: `["controller.animation.jungle"]`.

Буквальные ссылки description.animations: `entity:jungle` `Sword_B/entities/jungle.json`: alias `jungle`, `scripts.animate` = `["jungle"]`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.jungle": {
      "states": {
        "default": {
          "transitions": [
            {
              "jungle": "(1.0)"
            }
          ],
          "on_entry": [
          	"/commands"
          ]
        },
        "jungle": {
          "transitions": [
            {
              "default": "(1.0)"
            }
          ],
          "on_entry": [
          	"/execute @p ~~~ detect ~1 ~1 ~ log 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air",
          	"/execute @p ~~~ detect ~-1 ~1 ~ log 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~1 log 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~-1 log 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air",
          	"/execute @p ~~~ detect ~1 ~1 ~ log 1 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air",
          	"/execute @p ~~~ detect ~-1 ~1 ~ log 1 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~1 log 1 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~-1 log 1 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air",
          	"/execute @p ~~~ detect ~1 ~1 ~ log 2 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air",
          	"/execute @p ~~~ detect ~-1 ~1 ~ log 2 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~1 log 2 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~-1 log 2 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air",
          	"/execute @p ~~~ detect ~1 ~1 ~ log 3 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air",
          	"/execute @p ~~~ detect ~-1 ~1 ~ log 3 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~1 log 3 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~-1 log 3 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air",
          	"/execute @p ~~~ detect ~1 ~1 ~ log2 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air",
          	"/execute @p ~~~ detect ~-1 ~1 ~ log2 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~1 log2 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~-1 log2 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air",
          	"/execute @p ~~~ detect ~1 ~1 ~ log2 1 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air",
          	"/execute @p ~~~ detect ~-1 ~1 ~ log2 1 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~1 log2 1 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~-1 log2 1 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air",
          	"/execute @p ~~~ detect ~1 ~1 ~ stone 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air",
          	"/execute @p ~~~ detect ~-1 ~1 ~ stone 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~1 stone 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~-1 stone 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air",
          	"/execute @p ~~~ detect ~1 ~1 ~ cobblestone 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air",
          	"/execute @p ~~~ detect ~-1 ~1 ~ cobblestone 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~1 cobblestone 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~-1 cobblestone 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air",
          	"/execute @p ~~~ detect ~1 ~1 ~ dirt 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air",
          	"/execute @p ~~~ detect ~-1 ~1 ~ dirt 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~1 dirt 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~-1 dirt 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air",
          	"/execute @p ~~~ detect ~1 ~1 ~ leaves 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air",
          	"/execute @p ~~~ detect ~-1 ~1 ~ leaves 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~1 leaves 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~-1 leaves 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air",
          	"/execute @p ~~~ detect ~1 ~1 ~ leaves 1 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air",
          	"/execute @p ~~~ detect ~-1 ~1 ~ leaves 1 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~1 leaves 1 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~-1 leaves 1 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air",
          	"/execute @p ~~~ detect ~1 ~1 ~ leaves 2 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air",
          	"/execute @p ~~~ detect ~-1 ~1 ~ leaves 2 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~1 leaves 2 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~-1 leaves 2 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air",
          	"/execute @p ~~~ detect ~1 ~1 ~ leaves 3 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air",
          	"/execute @p ~~~ detect ~-1 ~1 ~ leaves 3 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~1 leaves 3 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~-1 leaves 3 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air",
          	"/execute @p ~~~ detect ~1 ~1 ~ leaves2 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air",
          	"/execute @p ~~~ detect ~-1 ~1 ~ leaves2 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~1 leaves2 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~-1 leaves2 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air",
          	"/execute @p ~~~ detect ~1 ~1 ~ leaves2 1 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air",
          	"/execute @p ~~~ detect ~-1 ~1 ~ leaves2 1 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~1 leaves2 1 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~-1 leaves2 1 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air",
          	"/execute @p ~~~ detect ~1 ~1 ~ planks 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air",
          	"/execute @p ~~~ detect ~-1 ~1 ~ planks 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~1 planks 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~-1 planks 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air",
          	"/execute @p ~~~ detect ~1 ~1 ~ planks 1 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air",
          	"/execute @p ~~~ detect ~-1 ~1 ~ planks 1 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~1 planks 1 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~-1 planks 1 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air",
          	"/execute @p ~~~ detect ~1 ~1 ~ planks 2 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air",
          	"/execute @p ~~~ detect ~-1 ~1 ~ planks 2 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~1 planks 2 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~-1 planks 2 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air",
          	"/execute @p ~~~ detect ~1 ~1 ~ planks 3 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air",
          	"/execute @p ~~~ detect ~-1 ~1 ~ planks 3 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~1 planks 3 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~-1 planks 3 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air",
          	"/execute @p ~~~ detect ~1 ~1 ~ planks 4 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air",
          	"/execute @p ~~~ detect ~-1 ~1 ~ planks 4 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~1 planks 4 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~-1 planks 4 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air",
          	"/execute @p ~~~ detect ~1 ~1 ~ planks 5 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air",
          	"/execute @p ~~~ detect ~-1 ~1 ~ planks 5 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~1 planks 5 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~-1 planks 5 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air",
          	"/execute @p ~~~ detect ~1 ~1 ~ grass 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air",
          	"/execute @p ~~~ detect ~-1 ~1 ~ grass 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~1 grass 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~-1 grass 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air",
          	"/execute @p ~~~ detect ~1 ~1 ~ netherrack 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air",
          	"/execute @p ~~~ detect ~-1 ~1 ~ netherrack 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~1 netherrack 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~-1 netherrack 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air",
          	"/execute @p ~~~ detect ~1 ~1 ~ nether_brick 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air",
          	"/execute @p ~~~ detect ~-1 ~1 ~ nether_brick 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~1 nether_brick 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~-1 nether_brick 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air",
          	"/execute @p ~~~ detect ~1 ~1 ~ sand 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air",
          	"/execute @p ~~~ detect ~-1 ~1 ~ sand 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~1 sand 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~-1 sand 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air",
          	"/execute @p ~~~ detect ~1 ~1 ~ glass 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air",
          	"/execute @p ~~~ detect ~-1 ~1 ~ glass 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~1 glass 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~-1 glass 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air",
          	"/execute @p ~~~ detect ~1 ~1 ~ obsidian 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air",
          	"/execute @p ~~~ detect ~-1 ~1 ~ obsidian 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~1 obsidian 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~-1 obsidian 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air",
          	"/execute @p ~~~ detect ~1 ~1 ~ end_stone 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air",
          	"/execute @p ~~~ detect ~-1 ~1 ~ end_stone 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~1 end_stone 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~-1 end_stone 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air",
          	"/execute @p ~~~ detect ~1 ~1 ~ sandstone 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air",
          	"/execute @p ~~~ detect ~-1 ~1 ~ sandstone 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~1 sandstone 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~-1 sandstone 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air",
          	"/execute @p ~~~ detect ~1 ~1 ~ gravel 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air",
          	"/execute @p ~~~ detect ~-1 ~1 ~ gravel 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~1 gravel 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~-1 gravel 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air",
          	"/execute @p ~~~ detect ~1 ~1 ~ stone 1 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air",
          	"/execute @p ~~~ detect ~-1 ~1 ~ stone 1 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~1 stone 1 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~-1 stone 1 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air",
          	"/execute @p ~~~ detect ~1 ~1 ~ stone 3 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air",
          	"/execute @p ~~~ detect ~-1 ~1 ~ stone 3 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~1 stone 3 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~-1 stone 3 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air",
          	"/execute @p ~~~ detect ~1 ~1 ~ stone 5 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air",
          	"/execute @p ~~~ detect ~-1 ~1 ~ stone 5 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~1 stone 5 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~-1 stone 5 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air",
          	"/execute @p ~~~ detect ~1 ~1 ~ snow 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air",
          	"/execute @p ~~~ detect ~-1 ~1 ~ snow 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~1 snow 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~-1 snow 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air",
          	"/execute @p ~~~ detect ~1 ~1 ~ packed_ice 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air",
          	"/execute @p ~~~ detect ~-1 ~1 ~ packed_ice 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~1 packed_ice 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~-1 packed_ice 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air",
          	"/execute @p ~~~ detect ~1 ~1 ~ ice 0 fill ~ ~1 ~ ~ ~1 ~ vine 8 replace air",
          	"/execute @p ~~~ detect ~-1 ~1 ~ ice 0 fill ~ ~1 ~ ~ ~1 ~ vine 2 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~1 ice 0 fill ~ ~1 ~ ~ ~1 ~ vine 1 replace air",
          	"/execute @p ~~~ detect ~ ~1 ~-1 ice 0 fill ~ ~1 ~ ~ ~1 ~ vine 4 replace air",
            "/scoreboard players set @a swords 2"

          ]
        }
      }
    }
  }
}
```

### `Sword_B/animation_controllers/lapis_sword.json`

Идентификаторы: `["controller.animation.lapis"]`.

Буквальные ссылки description.animations: `entity:lapis` `Sword_B/entities/lapis.json`: alias `lapis`, `scripts.animate` = `["lapis"]`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.lapis": {
      "states": {
        "default": {
          "transitions": [
            {
              "lapis": "(1.0)"
            }
          ],
          "on_entry": [
            "/scoreboard objectives add l dummy",
            "/scoreboard players add @p l 1",
            "/execute @p[scores={l=10}] ~ ~ ~ xp 5 @s",
            "/execute @p[scores={l=30}] ~ ~ ~ scoreboard objectives remove l",
            "/scoreboard players set @a swords 2"
          ]
        },
        "lapis": {
          "transitions": [
            {
              "default": "(1.0)"
            }
          ],
          "on_entry": [
            "/scoreboard objectives add l dummy",
            "/scoreboard players add @p l 1",
            "/execute @p[scores={l=10}] ~ ~ ~ xp 5 @s",
            "/execute @p[scores={l=30}] ~ ~ ~ scoreboard objectives remove l",
            "/scoreboard players set @a swords 2"
          ]
        }
      }
    }
  }
}
```

### `Sword_B/animation_controllers/lightning sword.json`

Идентификаторы: `["controller.animation.lightning"]`.

Буквальные ссылки description.animations: `entity:lightning` `Sword_B/entities/lightning.json`: alias `lightning`, `scripts.animate` = `["lightning"]`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.lightning": {
      "states": {
        "default": {
          "transitions": [
            {
              "lightning": "(1.0)"
            }
          ],
          "on_entry": [
            "/execute @e[type=zombie,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=husk,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=drowned,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=creeper,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=enderman,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=slime,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=skeleton,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=stray,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=blaze,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=wither_skeleton,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=witch,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=magma_cube,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=ghast,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=zombie_pigman,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=spider,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=cave_spider,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=silverfish,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=evocation_fang,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=evocation_illager,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=vex,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=ravager,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=endermite,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=guardian,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=vindicator,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=phantom,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=zombie_villager,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/scoreboard players set @a swords 2"
          ]
        },
        "lightning": {
          "transitions": [
            {
              "default": "(1.0)"
            }
          ],
          "on_entry": [
            "/execute @e[type=zombie,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=husk,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=drowned,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=creeper,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=enderman,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=slime,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=skeleton,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=stray,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=blaze,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=wither_skeleton,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=witch,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=magma_cube,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=ghast,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=zombie_pigman,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=spider,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=cave_spider,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=silverfish,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=evocation_fang,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=evocation_illager,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=vex,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=ravager,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=endermite,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=guardian,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=vindicator,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=phantom,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/execute @e[type=zombie_villager,r=16,rm=10] ~ ~ ~ summon lightning_bolt",
            "/scoreboard players set @a swords 2"
          ]
        }
      }
    }
  }
}
```

### `Sword_B/animation_controllers/magma_sword.json`

Идентификаторы: `["controller.animation.magma"]`.

Буквальные ссылки description.animations: `entity:magma` `Sword_B/entities/magma.json`: alias `magma`, `scripts.animate` = `["magma"]`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.magma": {
      "states": {
        "default": {
          "transitions": [
            {
              "magma": "(1.0)"
            }
          ],
          "on_entry": [
          	"/effect @p fire_resistance 10 0 true",
          	"/execute @p ~ ~ ~ fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 magma 0 replace lava",
            "/execute @e[r=15,rm=2,type=zombie] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=husk] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=drowned] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=creeper] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=enderman] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=slime] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=skeleton] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=stray] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=witch] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=spider] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=cave_spider] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=silverfish] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=evocation_fang] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=evocation_illager] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=vex] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=ravager] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=endermite] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=guardian] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=vindicator] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=phantom] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=zombie_villager] ~ ~ ~ setblock ~ ~ ~ fire",
            "/scoreboard players set @a swords 2"
          ]
        },
        "magma": {
          "transitions": [
            {
              "default": "(1.0)"
            }
          ],
          "on_entry": [
          	"/effect @p fire_resistance 10 0 true",
          	"/execute @p ~ ~ ~ fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 magma 0 replace lava",
            "/execute @e[r=15,rm=2,type=zombie] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=husk] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=drowned] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=creeper] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=enderman] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=slime] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=skeleton] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=stray] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=witch] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=spider] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=cave_spider] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=silverfish] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=evocation_fang] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=evocation_illager] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=vex] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=ravager] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=endermite] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=guardian] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=vindicator] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=phantom] ~ ~ ~ setblock ~ ~ ~ fire",
            "/execute @e[r=15,rm=2,type=zombie_villager] ~ ~ ~ setblock ~ ~ ~ fire",
            "/scoreboard players set @a swords 2"
          ]
        }
      }
    }
  }
}
```

### `Sword_B/animation_controllers/normal.json`

Идентификаторы: `["controller.animation.normal"]`.

Буквальные ссылки description.animations: `entity:normal` `Sword_B/entities/normal.json`: alias `normal`, `scripts.animate` = `["normal"]`; `minecraft:player` `Sword_B/entities/player.json`: alias `normal`, `scripts.animate` = `["normal"]`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.normal": {
      "states": {
        "default": {
          "transitions": [
            {
              "normal": "(1.0)"
            }
          ],
          "on_entry": [
            "/function normalft"

          ]
        },
        "normal": {
          "transitions": [
            {
              "default": "(1.0)"
            }
          ],
          "on_entry": [
            "/function normalft"
          ]
        }
      }
    }
  }
}
```

### `Sword_B/animation_controllers/obsidian_sword.json`

Идентификаторы: `["controller.animation.ob"]`.

Буквальные ссылки description.animations: `entity:obsidian` `Sword_B/entities/obsidian.json`: alias `ob`, `scripts.animate` = `["ob"]`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.ob": {
      "states": {
        "default": {
          "transitions": [
            {
              "ob": "(1.0)"
            }
          ],
          "on_entry": [
            "/execute @a ~ ~ ~ detect ~ ~ ~ air 0 fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 obsidian 0 replace lava 0",
            "/execute @a ~ ~ ~ detect ~ ~ ~ air 0 fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 obsidian 0 replace flowing_lava 0",
            "/execute @a ~ ~ ~ detect ~ ~ ~ lava 0 effect @s fire_resistance 10 0 true",
            "/execute @a ~ ~ ~ detect ~ ~ ~ lava 1 effect @s fire_resistance 10 0 true",
            "/execute @a ~ ~ ~ detect ~ ~ ~ lava 2 effect @s fire_resistance 10 0 true",
            "/execute @a ~ ~ ~ detect ~ ~ ~ lava 3 effect @s fire_resistance 10 0 true",
            "/execute @a ~ ~ ~ detect ~ ~ ~ lava 4 effect @s fire_resistance 10 0 true",
            "/execute @a ~ ~ ~ detect ~ ~ ~ lava 5 effect @s fire_resistance 10 0 true",
            "/execute @a ~ ~ ~ detect ~ ~ ~ lava 6 effect @s fire_resistance 10 0 true",
            "/execute @a ~ ~ ~ detect ~ ~ ~ lava 7 effect @s fire_resistance 10 0 true",
            "/execute @a ~ ~ ~ detect ~ ~ ~ lava 8 effect @s fire_resistance 10 0 true",
            "/execute @a ~ ~ ~ detect ~ ~ ~ flowing_lava 0 effect @s fire_resistance 10 0 true",
            "/scoreboard players set @a swords 2"
          ]
        },
        "ob": {
          "transitions": [
            {
              "default": "(1.0)"
            }
          ],
          "on_entry": [
            "/execute @a ~ ~ ~ detect ~ ~ ~ air 0 fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 obsidian 0 replace lava 0",
            "/execute @a ~ ~ ~ detect ~ ~ ~ air 0 fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 obsidian 0 replace flowing_lava 0",    
            "/execute @a ~ ~ ~ detect ~ ~ ~ lava 0 effect @s fire_resistance 10 0 true",
            "/execute @a ~ ~ ~ detect ~ ~ ~ lava 1 effect @s fire_resistance 10 0 true",
            "/execute @a ~ ~ ~ detect ~ ~ ~ lava 2 effect @s fire_resistance 10 0 true",
            "/execute @a ~ ~ ~ detect ~ ~ ~ lava 3 effect @s fire_resistance 10 0 true",
            "/execute @a ~ ~ ~ detect ~ ~ ~ lava 4 effect @s fire_resistance 10 0 true",
            "/execute @a ~ ~ ~ detect ~ ~ ~ lava 5 effect @s fire_resistance 10 0 true",
            "/execute @a ~ ~ ~ detect ~ ~ ~ lava 6 effect @s fire_resistance 10 0 true",
            "/execute @a ~ ~ ~ detect ~ ~ ~ lava 7 effect @s fire_resistance 10 0 true",
            "/execute @a ~ ~ ~ detect ~ ~ ~ lava 8 effect @s fire_resistance 10 0 true",            
            "/execute @a ~ ~ ~ detect ~ ~ ~ flowing_lava 0 effect @s fire_resistance 10 0 true",
            "/scoreboard players set @a swords 2"   
          ]
        }
      }
    }
  }
}
```

### `Sword_B/animation_controllers/sea_sword.json`

Идентификаторы: `["controller.animation.sea"]`.

Буквальные ссылки description.animations: `entity:sea` `Sword_B/entities/sea.json`: alias `sea`, `scripts.animate` = `["sea"]`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.sea": {
      "states": {
        "default": {
          "transitions": [
            {
              "sea": "(1.0)"
            }
          ],
          "on_entry": [
            "/effect @e[type=guardian,r=6] fatal_poison 5 0 true",
            "/effect @e[type=drowned,r=6] fatal_poison 5 0 true",
            "/effect @p conduit_power 16 0 true",
            "/scoreboard players set @a swords 2"

          ]
        },
        "sea": {
          "transitions": [
            {
              "default": "(1.0)"
            }
          ],
          "on_entry": [
            "/effect @e[type=guardian,r=6] fatal_poison 5 0 true",
            "/effect @e[type=drowned,r=6] fatal_poison 5 0 true",
            "/effect @p conduit_power 16 0 true",
            "/scoreboard players set @a swords 2"
          ]
        }
      }
    }
  }
}
```

### `Sword_B/animation_controllers/shulker_sword.json`

Идентификаторы: `["controller.animation.shulker"]`.

Буквальные ссылки description.animations: `entity:shulker` `Sword_B/entities/shulker.json`: alias `shulker`, `scripts.animate` = `["shulker"]`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.shulker": {
      "states": {
        "default": {
          "transitions": [
            {
              "shulker": "(1.0)"
            }
          ],
          "on_entry": [
          	"/effect @p levitation 0 0 true",
          	"/execute @p ~ ~ ~ tp @e[type=entity:shulker2] ~ ~2.5 ~",
            "/scoreboard objectives add sh dummy",
            "/scoreboard players add @p sh 1",
            "/execute @p[scores={sh=40}] ~ ~ ~ summon entity:shulker2",
            "/execute @p[scores={sh=2400}] ~ ~ ~ scoreboard objectives remove sh",
            "/execute @p[scores={sh=2390}] ~ ~ ~ kill @e[type=entity:shulker2,r=5] ~ 0 ~",
            "/scoreboard players set @a swords 2"
          ]
        },
        "shulker": {
          "transitions": [
            {
              "default": "(1.0)"
            }
          ],
          "on_entry": [
            "/effect @p levitation 0 0 true",
            "/execute @p ~ ~ ~ tp @e[type=entity:shulker2] ~ ~2.5 ~",
            "/scoreboard objectives add sh dummy",
            "/scoreboard players add @p sh 1",
            "/execute @p[scores={sh=40}] ~ ~ ~ summon entity:shulker2",
            "/execute @p[scores={sh=2400}] ~ ~ ~ scoreboard objectives remove sh",
            "/execute @p[scores={sh=2390}] ~ ~ ~ kill @e[type=entity:shulker2,r=5] ~ 0 ~",
            "/scoreboard players set @a swords 2"

          ]
        }
      }
    }
  }
}
```

### `Sword_B/animation_controllers/slime_sword.json`

Идентификаторы: `["controller.animation.slime"]`.

Буквальные ссылки description.animations: `entity:slime` `Sword_B/entities/slime.json`: alias `slime`, `scripts.animate` = `["slime"]`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.slime": {
      "states": {
        "default": {
          "transitions": [
            {
              "slime": "(1.0)"
            }
          ],
          "on_entry": [
          	"/scoreboard objectives add s dummy",
            "/scoreboard players add @p s 1",
            "/execute @p[scores={s=1}] ~ ~ ~ summon slime",
            "/effect @p jump_boost 1 5 true",
            "/execute @p[scores={s=600}] ~ ~ ~ scoreboard objectives remove s",
            "/scoreboard players set @a swords 2"




          ]
        },
        "slime": {
          "transitions": [
            {
              "default": "(1.0)"
            }
          ],
          "on_entry": [
            "/scoreboard objectives add s dummy",
            "/scoreboard players add @p s 1",
            "/execute @p[scores={s=1}] ~ ~ ~ summon slime",
            "/effect @p jump_boost 1 5 true",
            "/execute @p[scores={s=600}] ~ ~ ~ scoreboard objectives remove s",
            "/scoreboard players set @a swords 2"
          ]
        }
      }
    }
  }
}
```

### `Sword_B/animation_controllers/spectral_sword.json`

Идентификаторы: `["controller.animation.spectral"]`.

Буквальные ссылки description.animations: `entity:spectral` `Sword_B/entities/spectral.json`: alias `spectral`, `scripts.animate` = `["spectral"]`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.spectral": {
      "states": {
        "default": {
          "transitions": [
            {
              "spectral": "(1.0)"
            }
          ],
          "on_entry": [
            "/execute @p ~~~ fill ~6 ~6 ~6 ~-6 ~-6 ~-6 barrier 0 replace stone 0",
            "/fill ~7 ~8 ~8 ~8 ~-8 ~-8 stone 0 replace barrier",
            "/fill ~-7 ~-8 ~-8 ~-8 ~8 ~8 stone 0 replace barrier",
            "/fill ~-6 ~8 ~7 ~6 ~-8 ~8 stone 0 replace barrier",
            "/fill ~6 ~-8 ~-7 ~-6 ~8 ~-8 stone 0 replace barrier",
            "/fill ~8 ~-8 ~8 ~-8 ~-7 ~-8 stone 0 replace barrier",
            "/fill ~8 ~8 ~8 ~-8 ~7 ~-8 stone 0 replace barrier",
            "/scoreboard players set @a swords 2"
          ]
        },
        "spectral": {
          "transitions": [
            {
              "default": "(1.0)"
            }
          ],
          "on_entry": [     	
            "/execute @p ~~~ fill ~6 ~6 ~6 ~-6 ~-6 ~-6 barrier 0 replace stone 0",
            "/fill ~7 ~8 ~8 ~8 ~-8 ~-8 stone 0 replace barrier",
            "/fill ~-7 ~-8 ~-8 ~-8 ~8 ~8 stone 0 replace barrier",
            "/fill ~-6 ~8 ~7 ~6 ~-8 ~8 stone 0 replace barrier",
            "/fill ~6 ~-8 ~-7 ~-6 ~8 ~-8 stone 0 replace barrier",
            "/fill ~8 ~-8 ~8 ~-8 ~-7 ~-8 stone 0 replace barrier",
            "/fill ~8 ~8 ~8 ~-8 ~7 ~-8 stone 0 replace barrier",
            "/scoreboard players set @a swords 2"
          ]
        }
      }
    }
  }
}
```

### `Sword_B/animation_controllers/spider_sword.json`

Идентификаторы: `["controller.animation.spider"]`.

Буквальные ссылки description.animations: `entity:spider` `Sword_B/entities/spider.json`: alias `spider`, `scripts.animate` = `["spider"]`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.spider": {
      "states": {
        "default": {
          "transitions": [
            {
              "spider": "(1.0)"
            }
          ],
          "on_entry": [
          	"/effect @p poison 0 0 true",
          	"/execute @p ~ ~ ~ detect ~ ~ ~ web 0 fill ~ ~ ~ ~ ~ ~ air 0 replace web",
          	"/execute @p ~ ~ ~ detect ~ ~1 ~ web 0 fill ~ ~1 ~ ~ ~1 ~ air 0 replace web",
          	"/execute @p ~ ~ ~ effect @e[r=6,type=spider] slowness 1 128 true",
          	"/execute @p ~ ~ ~ effect @e[r=6,type=cave_spider] slowness 1 128 true",
            "/execute @e[r=5,type=zombie] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=creeper] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=husk] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=drowned] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=enderman] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=slime] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=skeleton] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=stray] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=blaze] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=wither_skeleton] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=witch] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=magma_cube] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=ghast] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=zombie_pigman] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=silverfish] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=evocation_fang] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=evocation_illager] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=vex] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=ravager] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=endermite] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=guardian] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=vindicator] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=phantom] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=tnt] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=zombie_villager] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/scoreboard players set @a swords 2"




          ]
        },
        "spider": {
          "transitions": [
            {
              "default": "(1.0)"
            }
          ],
          "on_entry": [
          	"/effect @p poison 0 0 true",
          	"/execute @p ~ ~ ~ detect ~ ~ ~ web 0 fill ~ ~ ~ ~ ~ ~ air 0 replace web",
          	"/execute @p ~ ~ ~ detect ~ ~1 ~ web 0 fill ~ ~1 ~ ~ ~1 ~ air 0 replace web",
          	"/execute @p ~ ~ ~ effect @e[r=6,type=spider] slowness 1 128 true",
          	"/execute @p ~ ~ ~ effect @e[r=6,type=cave_spider] slowness 1 128 true",
            "/execute @e[r=5,type=zombie] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=creeper] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=husk] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=drowned] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=enderman] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=slime] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=skeleton] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=stray] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=blaze] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=wither_skeleton] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=witch] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=magma_cube] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=ghast] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=zombie_pigman] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=silverfish] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=evocation_fang] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=evocation_illager] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=vex] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=ravager] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=endermite] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=guardian] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=vindicator] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=phantom] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=tnt] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/execute @e[r=5,type=zombie_villager] ~ ~ ~ fill ~ ~ ~ ~ ~ ~ web 0 replace air",
            "/scoreboard players set @a swords 2"

          ]
        }
      }
    }
  }
}
```

### `Sword_B/animation_controllers/sponge_sword.json`

Идентификаторы: `["controller.animation.sponge"]`.

Буквальные ссылки description.animations: `entity:sponge` `Sword_B/entities/sponge.json`: alias `sponge`, `scripts.animate` = `["sponge"]`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.sponge": {
      "states": {
        "default": {
          "transitions": [
            {
              "sponge": "(1.0)"
            }
          ],
          "on_entry": [
            "/execute @a ~ ~ ~ fill ~4 ~4 ~4 ~-4 ~-4 ~-4 sponge 0 replace water",
            "/execute @a ~ ~ ~ fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace sponge",
            "/execute @a ~ ~ ~ detect ~ ~ ~ water 0 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass",
            "/execute @a ~ ~ ~ detect ~ ~ ~ water 1 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass",
            "/execute @a ~ ~ ~ detect ~ ~ ~ water 2 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass",
            "/execute @a ~ ~ ~ detect ~ ~ ~ water 3 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass",
            "/execute @a ~ ~ ~ detect ~ ~ ~ water 4 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass",
            "/execute @a ~ ~ ~ detect ~ ~ ~ water 5 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass",
            "/execute @a ~ ~ ~ detect ~ ~ ~ water 6 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass",
            "/execute @a ~ ~ ~ detect ~ ~ ~ water 7 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass",
            "/execute @a ~ ~ ~ detect ~ ~ ~ water 8 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass",
            "/execute @a ~ ~ ~ detect ~ ~1 ~ air 0 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass",
            "/scoreboard players set @a swords 2"
          ]
        },
        "sponge": {
          "transitions": [
            {
              "default": "(1.0)"
            }
          ],
          "on_entry": [
            "/execute @a ~ ~ ~ fill ~4 ~4 ~4 ~-4 ~-4 ~-4 sponge 0 replace water",
            "/execute @a ~ ~ ~ fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace sponge",
            "/execute @a ~ ~ ~ detect ~ ~ ~ water 0 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass",
            "/execute @a ~ ~ ~ detect ~ ~ ~ water 1 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass",
            "/execute @a ~ ~ ~ detect ~ ~ ~ water 2 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass",
            "/execute @a ~ ~ ~ detect ~ ~ ~ water 3 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass",
            "/execute @a ~ ~ ~ detect ~ ~ ~ water 4 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass",
            "/execute @a ~ ~ ~ detect ~ ~ ~ water 5 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass",
            "/execute @a ~ ~ ~ detect ~ ~ ~ water 6 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass",
            "/execute @a ~ ~ ~ detect ~ ~ ~ water 7 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass",
            "/execute @a ~ ~ ~ detect ~ ~ ~ water 8 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass",
            "/execute @a ~ ~ ~ detect ~ ~1 ~ air 0 fill ~4 ~4 ~4 ~-4 ~-4 ~-4 air 0 replace seagrass",
            "/scoreboard players set @a swords 2"
          ]
        }
      }
    }
  }
}
```

### `Sword_B/animation_controllers/sword of time.json`

Идентификаторы: `["controller.animation.time"]`.

Буквальные ссылки description.animations: `entity:time` `Sword_B/entities/time.json`: alias `time`, `scripts.animate` = `["time"]`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.time": {
      "states": {
        "default": {
          "transitions": [
            {
              "time": "(1.0)"
            }
          ],
          "on_entry": [
            "/gamerule randomtickspeed 300",
            "/effect @e speed 1 15 true",
            "/time add 30",
            "/scoreboard players set @a swords 2"
          ]
        },
        "time": {
          "transitions": [
            {
              "default": "(1.0)"
            }
          ],
          "on_entry": [
            "/gamerule randomtickspeed 300",
            "/effect @e speed 1 15 true",
            "/time add 30",
            "/scoreboard players set @a swords 2"
          ]
        }
      }
    }
  }
}
```

### `Sword_B/animation_controllers/tnt_sword.json`

Идентификаторы: `["controller.animation.tnt"]`.

Буквальные ссылки description.animations: `entity:tnt_sword` `Sword_B/entities/tnt_sword.json`: alias `tnt`, `scripts.animate` = `["tnt"]`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.tnt": {
      "states": {
        "default": {
          "transitions": [
            {
              "tnt": "(1.0)"
            }
          ],
          "on_entry": [
            "/execute @e[r=15,rm=10,type=zombie] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=husk] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=drowned] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=creeper] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=enderman] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=slime] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=skeleton] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=stray] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=blaze] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=wither_skeleton] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=witch] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=magma_cube] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=ghast] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=zombie_pigman] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=spider] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=cave_spider] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=silverfish] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=evocation_fang] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=evocation_illager] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=vex] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=ravager] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=endermite] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=guardian] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=vindicator] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=phantom] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=zombie_villager] ~ ~ ~ summon entity:explode",
            "/scoreboard players set @a swords 2"
          ]
        },
        "tnt": {
          "transitions": [
            {
              "default": "(1.0)"
            }
          ],
          "on_entry": [
            "/execute @e[r=15,rm=10,type=zombie] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=husk] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=drowned] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=creeper] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=enderman] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=slime] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=skeleton] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=stray] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=blaze] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=wither_skeleton] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=witch] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=magma_cube] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=ghast] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=zombie_pigman] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=spider] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=cave_spider] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=silverfish] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=evocation_fang] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=evocation_illager] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=vex] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=ravager] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=endermite] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=guardian] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=vindicator] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=phantom] ~ ~ ~ summon entity:explode",
            "/execute @e[r=15,rm=10,type=zombie_villager] ~ ~ ~ summon entity:explode",
            "/scoreboard players set @a swords 2"
          ]
        }
      }
    }
  }
}
```

### `Sword_B/animation_controllers/wither_sword.json`

Идентификаторы: `["controller.animation.wither"]`.

Буквальные ссылки description.animations: `entity:wither` `Sword_B/entities/wither_s.json`: alias `wither`, `scripts.animate` = `["wither"]`.

```json
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.wither": {
      "states": {
        "default": {
          "transitions": [
            {
              "wither": "(1.0)"
            }
          ],
          "on_entry": [
            "/Effect99"
          ]
        },
        "wither": {
          "transitions": [
            {
              "default": "(1.0)"
            }
          ],
          "on_entry": [     	
            "/effect @e[r=16,type=!player] poison 30 1 true",
            "/execute @a ~~~ particle minecraft:falling_dust_concrete_powder_particle ~-0.1 ~0.2 ~-0.2",
            "/fill ~5 ~5 ~5 ~-5 ~-5 ~-5 dirt 1 replace grass",
            "/fill ~5 ~5 ~5 ~-5 ~-5 ~-5 air 0 replace leaves2",
            "/fill ~5 ~5 ~5 ~-5 ~-5 ~-5 air 0 replace leaves",
            "/fill ~5 ~5 ~5 ~-5 ~-5 ~-5 water 0 replace ice",
            "/fill ~5 ~5 ~5 ~-5 ~-5 ~-5 dirt 0 replace farmland",
            "/fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace red_flower",
            "/fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace yellow_flower",
            "/fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace red_mushroom",
            "/fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace brown_mushroom",
            "/fill ~5 ~5 ~5 ~-5 ~-5 ~-5 wither_rose 0 replace double_plant",
          	"/scoreboard objectives add w dummy",
          	"/scoreboard players add @e[r=16,type=!cow,type=!pig,type=!sheep,type=!horse,type=!rabbit,type=!villager,type=!wolf,type=!cat,type=!fox,type=!chicken] w 1",
          	"/execute @p[scores={w=200}] ~ ~ ~ playsound mob.wither.death",
          	"/execute @p[scores={w=500}] ~ ~ ~ playsound mob.wither.hurt",
          	"/execute @e[scores={w=100},r=16,type=zombie] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={w=100},r=16,type=husk] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={w=100},r=16,type=drowned] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={w=100},r=16,type=creeper] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={w=100},r=16,type=enderman] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={w=100},r=16,type=slime] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={w=100},r=16,type=skeleton] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={w=100},r=16,type=stray] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={w=100},r=16,type=blaze] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={w=100},r=16,type=wither_skeleton] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={w=100},r=16,type=witch] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={w=100},r=16,type=magma_cube] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={w=100},r=16,type=ghast] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={w=100},r=16,type=zombie_pigman] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={w=100},r=16,type=spider] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={w=100},r=16,type=cave_spider] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={w=100},r=16,type=silverfish] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={w=100},r=16,type=evocation_fang] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={w=100},r=16,type=evocation_illager] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={w=100},r=16,type=vex] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={w=100},r=16,type=ravager] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={w=100},r=16,type=endermite] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={w=100},r=16,type=guardian] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={w=100},r=16,type=vindicator] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={w=100},r=16,type=phantom] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={w=100},r=16,type=tnt] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={w=100},r=16,type=zombie_villager] ~ ~ ~ summon entity:explode",
            "/execute @e[scores={w=100},r=16,type=wither] ~ ~ ~ summon entity:explode",
          	"/execute @p[scores={w=600}] ~ ~ ~ scoreboard objectives remove w",
            "/scoreboard players set @a swords 2"
          ]
        }
      }
    }
  }
}
```

