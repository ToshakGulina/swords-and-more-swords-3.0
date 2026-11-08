# Двоичные структуры — архив 2.8.14

Источник: `swordsandmoreswords-2-8-14.mcaddon`. Каждая структура ниже прочитана как little-endian NBT и выведена в типизированном SNBT. Преобразование SNBT → NBT проверено побайтово для каждого файла; оригинал архива остаётся основным источником.

Список вызовов ищется только по буквальному тексту `structure load` в JSON, JS и mcfunction. Синтаксис и успешность команд, динамические имена, другие пакеты и структуры из мира не проверяются. Пустой список вызовов не доказывает, что структура не используется.

## Буквальные ссылки без одноимённого файла в архиве

- `blaze_sword`: в архиве нет `*/structures/blaze_sword.mcstructure`; возможна внешняя структура или другой способ разрешения имени.
  - `Swords_B/entities/blaze.json:134` — `"run_command": { "command": [ "structure load blaze_sword ~ ~ ~" ] }`

## `armor stands swords`

- Путь `Swords_B/structures/armor stands swords.mcstructure`; MD5 `e9c63bb4c3130d0a6268b3735667a41c`; NBT round-trip: побайтово совпал.
- Размер `[1, 4, 36]`; structure_world_origin `[-11, 59, -12]`; сущностей 36.
- Сущности: `minecraft:armor_stand`, `minecraft:armor_stand`, `minecraft:armor_stand`, `minecraft:armor_stand`, `minecraft:armor_stand`, `minecraft:armor_stand`, `minecraft:armor_stand`, `minecraft:armor_stand`, `minecraft:armor_stand`, `minecraft:armor_stand`, `minecraft:armor_stand`, `minecraft:armor_stand`, `minecraft:armor_stand`, `minecraft:armor_stand`, `minecraft:armor_stand`, `minecraft:armor_stand`, `minecraft:armor_stand`, `minecraft:armor_stand`, `minecraft:armor_stand`, `minecraft:armor_stand`, `minecraft:armor_stand`, `minecraft:armor_stand`, `minecraft:armor_stand`, `minecraft:armor_stand`, `minecraft:armor_stand`, `minecraft:armor_stand`, `minecraft:armor_stand`, `minecraft:armor_stand`, `minecraft:armor_stand`, `minecraft:armor_stand`, `minecraft:armor_stand`, `minecraft:armor_stand`, `minecraft:armor_stand`, `minecraft:armor_stand`, `minecraft:armor_stand`, `minecraft:armor_stand`.
- Предметы с `Name` в пространствах `effect:` / `effect99:`:
  - `$.entities[0].Mainhand[0].Name`: `effect:time_sword`
  - `$.entities[1].Mainhand[0].Name`: `effect:sponge_sword`
  - `$.entities[2].Mainhand[0].Name`: `effect:spider_sword`
  - `$.entities[3].Mainhand[0].Name`: `effect:shulker_sword`
  - `$.entities[4].Mainhand[0].Name`: `effect:slime_sword`
  - `$.entities[5].Mainhand[0].Name`: `effect:spectral_sword`
  - `$.entities[6].Mainhand[0].Name`: `effect:sea_sword`
  - `$.entities[7].Mainhand[0].Name`: `effect:ender_sword`
  - `$.entities[8].Mainhand[0].Name`: `effect:wither_sword`
  - `$.entities[9].Mainhand[0].Name`: `effect:lightning_sword`
  - `$.entities[10].Mainhand[0].Name`: `effect:glowstone_sword`
  - `$.entities[11].Mainhand[0].Name`: `effect:tnt_sword`
  - `$.entities[12].Mainhand[0].Name`: `effect:lapis_sword`
  - `$.entities[13].Mainhand[0].Name`: `effect:bone_sword`
  - `$.entities[14].Mainhand[0].Name`: `effect:emerald_sword`
  - `$.entities[15].Mainhand[0].Name`: `effect:fire_sword`
  - `$.entities[16].Mainhand[0].Name`: `effect:blaze_sword`
  - `$.entities[17].Mainhand[0].Name`: `effect:creeper_sword`
  - `$.entities[18].Mainhand[0].Name`: `effect:wet_sponge_sword`
  - `$.entities[19].Mainhand[0].Name`: `effect:coal_sword`
  - `$.entities[20].Mainhand[0].Name`: `effect:ultra_instinct_sword`
  - `$.entities[21].Mainhand[0].Name`: `effect:quartz_sword`
  - `$.entities[22].Mainhand[0].Name`: `effect:obsidian_sword`
  - `$.entities[23].Mainhand[0].Name`: `effect:grass_sword`
  - `$.entities[24].Mainhand[0].Name`: `effect:cactus_sword`
  - `$.entities[25].Mainhand[0].Name`: `effect:jungle_sword`
  - `$.entities[26].Mainhand[0].Name`: `effect:ice_sword`
  - `$.entities[27].Mainhand[0].Name`: `effect:magma_sword`
  - `$.entities[28].Mainhand[0].Name`: `effect:wither_skeleton_sword`
  - `$.entities[29].Mainhand[0].Name`: `effect:glass_sword`
  - `$.entities[30].Mainhand[0].Name`: `effect:silver_sword`
  - `$.entities[31].Mainhand[0].Name`: `effect:wolf_sword`
  - `$.entities[32].Mainhand[0].Name`: `effect:nether_star_sword`
  - `$.entities[33].Mainhand[0].Name`: `effect:ghost_sword`
  - `$.entities[34].Mainhand[0].Name`: `effect:clock_sword`
  - `$.entities[35].Mainhand[0].Name`: `effect:bedrock_sword`
- Буквальные вызовы:
  - Не найдены.

### Полный типизированный SNBT

```snbt
{
  format_version: 1, 
  size: [1, 4, 36], 
  structure: {
    block_indices: [
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 
      [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    ], 
    entities: [
      {
        ActiveEffects: [
          {
            Ambient: 0b, 
            Amplifier: 10b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 16853724, 
            DurationEasy: 19973752, 
            DurationHard: 19973752, 
            DurationNormal: 19973752, 
            Id: 11b, 
            ShowParticles: 0b
          }, 
          {
            Ambient: 0b, 
            Amplifier: 0b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 17527140, 
            DurationEasy: 19969810, 
            DurationHard: 19969810, 
            DurationNormal: 19969810, 
            Id: 12b, 
            ShowParticles: 0b
          }
        ], 
        Armor: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        AttackTime: 0s, 
        Attributes: [
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 1024.0f, 
            DefaultMin: -1024.0f, 
            Max: 1024.0f, 
            Min: -1024.0f, 
            Name: "minecraft:luck"
          }, 
          {
            Base: 6.0f, 
            Current: 1.0f, 
            DefaultMax: 6.0f, 
            DefaultMin: 0.0f, 
            Max: 6.0f, 
            Min: 0.0f, 
            Name: "minecraft:health"
          }, 
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 16.0f, 
            DefaultMin: 0.0f, 
            Max: 16.0f, 
            Min: 0.0f, 
            Name: "minecraft:absorption"
          }, 
          {
            Base: 1.0f, 
            Current: 1.0f, 
            DefaultMax: 1.0f, 
            DefaultMin: 0.0f, 
            Max: 1.0f, 
            Min: 0.0f, 
            Name: "minecraft:knockback_resistance"
          }, 
          {
            Base: 0.699999988079071f, 
            Current: 0.699999988079071f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:underwater_movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:lava_movement"
          }, 
          {
            Base: 16.0f, 
            Current: 16.0f, 
            DefaultMax: 2048.0f, 
            DefaultMin: 0.0f, 
            Max: 2048.0f, 
            Min: 0.0f, 
            Name: "minecraft:follow_range"
          }
        ], 
        BodyRot: -90.0f, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        Dead: 0b, 
        DeathTime: 0s, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        HurtTime: 0s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsPregnant: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        LastDimensionId: 0, 
        LeasherID: -1L, 
        LootDropped: 0b, 
        Mainhand: [
          {
            Count: 1b, 
            Damage: 0s, 
            Name: "effect:time_sword", 
            WasPickedUp: 0b, 
            tag: {
              Damage: 0
            }
          }
        ], 
        MarkVariant: 0, 
        NaturalSpawn: 0b, 
        Offhand: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        OnGround: 1b, 
        OwnerNew: -1L, 
        Persistent: 1b, 
        PortalCooldown: 0, 
        Pos: [-10.5f, 59.0f, -6.5f], 
        Pose: {
          LastSignal: 0, 
          PoseIndex: 0
        }, 
        Rotation: [-90.0f, 0.0f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Surface: 0b, 
        Tags: [], 
        TargetID: -1L, 
        TradeExperience: 0, 
        TradeTier: 0, 
        UniqueID: -9225589751768L, 
        Variant: 0, 
        boundX: -7, 
        boundY: 3, 
        boundZ: 1, 
        canPickupItems: 0b, 
        definitions: ["+minecraft:armor_stand", "+"], 
        hasBoundOrigin: 0b, 
        hasSetCanPickupItems: 1b, 
        identifier: "minecraft:armor_stand", 
        limitedLife: 0
      }, 
      {
        ActiveEffects: [
          {
            Ambient: 0b, 
            Amplifier: 10b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 16853724, 
            DurationEasy: 19973752, 
            DurationHard: 19973752, 
            DurationNormal: 19973752, 
            Id: 11b, 
            ShowParticles: 0b
          }, 
          {
            Ambient: 0b, 
            Amplifier: 0b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 17527140, 
            DurationEasy: 19969810, 
            DurationHard: 19969810, 
            DurationNormal: 19969810, 
            Id: 12b, 
            ShowParticles: 0b
          }
        ], 
        Armor: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        AttackTime: 0s, 
        Attributes: [
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 1024.0f, 
            DefaultMin: -1024.0f, 
            Max: 1024.0f, 
            Min: -1024.0f, 
            Name: "minecraft:luck"
          }, 
          {
            Base: 6.0f, 
            Current: 1.0f, 
            DefaultMax: 6.0f, 
            DefaultMin: 0.0f, 
            Max: 6.0f, 
            Min: 0.0f, 
            Name: "minecraft:health"
          }, 
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 16.0f, 
            DefaultMin: 0.0f, 
            Max: 16.0f, 
            Min: 0.0f, 
            Name: "minecraft:absorption"
          }, 
          {
            Base: 1.0f, 
            Current: 1.0f, 
            DefaultMax: 1.0f, 
            DefaultMin: 0.0f, 
            Max: 1.0f, 
            Min: 0.0f, 
            Name: "minecraft:knockback_resistance"
          }, 
          {
            Base: 0.699999988079071f, 
            Current: 0.699999988079071f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:underwater_movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:lava_movement"
          }, 
          {
            Base: 16.0f, 
            Current: 16.0f, 
            DefaultMax: 2048.0f, 
            DefaultMin: 0.0f, 
            Max: 2048.0f, 
            Min: 0.0f, 
            Name: "minecraft:follow_range"
          }
        ], 
        BodyRot: -90.0f, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        Dead: 0b, 
        DeathTime: 0s, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        HurtTime: 0s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsPregnant: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        LastDimensionId: 0, 
        LeasherID: -1L, 
        LootDropped: 0b, 
        Mainhand: [
          {
            Count: 1b, 
            Damage: 0s, 
            Name: "effect:sponge_sword", 
            WasPickedUp: 0b, 
            tag: {
              Damage: 0
            }
          }
        ], 
        MarkVariant: 0, 
        NaturalSpawn: 0b, 
        Offhand: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        OnGround: 1b, 
        OwnerNew: -1L, 
        Persistent: 1b, 
        PortalCooldown: 0, 
        Pos: [-10.5f, 59.0f, -5.5f], 
        Pose: {
          LastSignal: 0, 
          PoseIndex: 0
        }, 
        Rotation: [-90.0f, 0.0f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Surface: 0b, 
        Tags: [], 
        TargetID: -1L, 
        TradeExperience: 0, 
        TradeTier: 0, 
        UniqueID: -9225589751769L, 
        Variant: 0, 
        boundX: -7, 
        boundY: 3, 
        boundZ: 1, 
        canPickupItems: 0b, 
        definitions: ["+minecraft:armor_stand", "+"], 
        hasBoundOrigin: 0b, 
        hasSetCanPickupItems: 1b, 
        identifier: "minecraft:armor_stand", 
        limitedLife: 0
      }, 
      {
        ActiveEffects: [
          {
            Ambient: 0b, 
            Amplifier: 10b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 16853724, 
            DurationEasy: 19973752, 
            DurationHard: 19973752, 
            DurationNormal: 19973752, 
            Id: 11b, 
            ShowParticles: 0b
          }, 
          {
            Ambient: 0b, 
            Amplifier: 0b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 17527140, 
            DurationEasy: 19969810, 
            DurationHard: 19969810, 
            DurationNormal: 19969810, 
            Id: 12b, 
            ShowParticles: 0b
          }
        ], 
        Armor: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        AttackTime: 0s, 
        Attributes: [
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 1024.0f, 
            DefaultMin: -1024.0f, 
            Max: 1024.0f, 
            Min: -1024.0f, 
            Name: "minecraft:luck"
          }, 
          {
            Base: 6.0f, 
            Current: 1.0f, 
            DefaultMax: 6.0f, 
            DefaultMin: 0.0f, 
            Max: 6.0f, 
            Min: 0.0f, 
            Name: "minecraft:health"
          }, 
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 16.0f, 
            DefaultMin: 0.0f, 
            Max: 16.0f, 
            Min: 0.0f, 
            Name: "minecraft:absorption"
          }, 
          {
            Base: 1.0f, 
            Current: 1.0f, 
            DefaultMax: 1.0f, 
            DefaultMin: 0.0f, 
            Max: 1.0f, 
            Min: 0.0f, 
            Name: "minecraft:knockback_resistance"
          }, 
          {
            Base: 0.699999988079071f, 
            Current: 0.699999988079071f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:underwater_movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:lava_movement"
          }, 
          {
            Base: 16.0f, 
            Current: 16.0f, 
            DefaultMax: 2048.0f, 
            DefaultMin: 0.0f, 
            Max: 2048.0f, 
            Min: 0.0f, 
            Name: "minecraft:follow_range"
          }
        ], 
        BodyRot: -90.0f, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        Dead: 0b, 
        DeathTime: 0s, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        HurtTime: 0s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsPregnant: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        LastDimensionId: 0, 
        LeasherID: -1L, 
        LootDropped: 0b, 
        Mainhand: [
          {
            Count: 1b, 
            Damage: 0s, 
            Name: "effect:spider_sword", 
            WasPickedUp: 0b, 
            tag: {
              Damage: 0
            }
          }
        ], 
        MarkVariant: 0, 
        NaturalSpawn: 0b, 
        Offhand: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        OnGround: 1b, 
        OwnerNew: -1L, 
        Persistent: 1b, 
        PortalCooldown: 0, 
        Pos: [-10.5f, 59.0f, -4.5f], 
        Pose: {
          LastSignal: 0, 
          PoseIndex: 0
        }, 
        Rotation: [-90.0f, 0.0f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Surface: 0b, 
        Tags: [], 
        TargetID: -1L, 
        TradeExperience: 0, 
        TradeTier: 0, 
        UniqueID: -9225589751770L, 
        Variant: 0, 
        boundX: -7, 
        boundY: 3, 
        boundZ: 1, 
        canPickupItems: 1b, 
        definitions: ["+minecraft:armor_stand", "+"], 
        hasBoundOrigin: 0b, 
        hasSetCanPickupItems: 1b, 
        identifier: "minecraft:armor_stand", 
        limitedLife: 0
      }, 
      {
        ActiveEffects: [
          {
            Ambient: 0b, 
            Amplifier: 0b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 17527140, 
            DurationEasy: 19999574, 
            DurationHard: 19999574, 
            DurationNormal: 19999574, 
            Id: 12b, 
            ShowParticles: 0b
          }
        ], 
        Armor: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        AttackTime: 0s, 
        Attributes: [
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 1024.0f, 
            DefaultMin: -1024.0f, 
            Max: 1024.0f, 
            Min: -1024.0f, 
            Name: "minecraft:luck"
          }, 
          {
            Base: 6.0f, 
            Current: 6.0f, 
            DefaultMax: 6.0f, 
            DefaultMin: 0.0f, 
            Max: 6.0f, 
            Min: 0.0f, 
            Name: "minecraft:health"
          }, 
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 16.0f, 
            DefaultMin: 0.0f, 
            Max: 16.0f, 
            Min: 0.0f, 
            Name: "minecraft:absorption"
          }, 
          {
            Base: 1.0f, 
            Current: 1.0f, 
            DefaultMax: 1.0f, 
            DefaultMin: 0.0f, 
            Max: 1.0f, 
            Min: 0.0f, 
            Name: "minecraft:knockback_resistance"
          }, 
          {
            Base: 0.699999988079071f, 
            Current: 0.699999988079071f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:underwater_movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:lava_movement"
          }, 
          {
            Base: 16.0f, 
            Current: 16.0f, 
            DefaultMax: 2048.0f, 
            DefaultMin: 0.0f, 
            Max: 2048.0f, 
            Min: 0.0f, 
            Name: "minecraft:follow_range"
          }
        ], 
        BodyRot: -90.0f, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        Dead: 0b, 
        DeathTime: 0s, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        HurtTime: 0s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsPregnant: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        LastDimensionId: 0, 
        LeasherID: -1L, 
        LootDropped: 0b, 
        Mainhand: [
          {
            Count: 1b, 
            Damage: 0s, 
            Name: "effect:shulker_sword", 
            WasPickedUp: 0b, 
            tag: {
              Damage: 0
            }
          }
        ], 
        MarkVariant: 0, 
        NaturalSpawn: 0b, 
        Offhand: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        OnGround: 1b, 
        OwnerNew: -1L, 
        Persistent: 1b, 
        PortalCooldown: 0, 
        Pos: [-10.5f, 59.0f, -3.5f], 
        Pose: {
          LastSignal: 0, 
          PoseIndex: 0
        }, 
        Rotation: [-90.0f, 0.0f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Surface: 0b, 
        Tags: [], 
        TargetID: -1L, 
        TradeExperience: 0, 
        TradeTier: 0, 
        UniqueID: -9225589751771L, 
        Variant: 0, 
        boundX: -7, 
        boundY: 3, 
        boundZ: 1, 
        canPickupItems: 1b, 
        definitions: ["+minecraft:armor_stand", "+"], 
        hasBoundOrigin: 0b, 
        hasSetCanPickupItems: 1b, 
        identifier: "minecraft:armor_stand", 
        limitedLife: 0
      }, 
      {
        Armor: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        AttackTime: 0s, 
        Attributes: [
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 1024.0f, 
            DefaultMin: -1024.0f, 
            Max: 1024.0f, 
            Min: -1024.0f, 
            Name: "minecraft:luck"
          }, 
          {
            Base: 6.0f, 
            Current: 6.0f, 
            DefaultMax: 6.0f, 
            DefaultMin: 0.0f, 
            Max: 6.0f, 
            Min: 0.0f, 
            Name: "minecraft:health"
          }, 
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 16.0f, 
            DefaultMin: 0.0f, 
            Max: 16.0f, 
            Min: 0.0f, 
            Name: "minecraft:absorption"
          }, 
          {
            Base: 1.0f, 
            Current: 1.0f, 
            DefaultMax: 1.0f, 
            DefaultMin: 0.0f, 
            Max: 1.0f, 
            Min: 0.0f, 
            Name: "minecraft:knockback_resistance"
          }, 
          {
            Base: 0.699999988079071f, 
            Current: 0.699999988079071f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:underwater_movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:lava_movement"
          }, 
          {
            Base: 16.0f, 
            Current: 16.0f, 
            DefaultMax: 2048.0f, 
            DefaultMin: 0.0f, 
            Max: 2048.0f, 
            Min: 0.0f, 
            Name: "minecraft:follow_range"
          }
        ], 
        BodyRot: -90.0f, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        Dead: 0b, 
        DeathTime: 0s, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        HurtTime: 0s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsPregnant: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        LastDimensionId: 0, 
        LeasherID: -1L, 
        LootDropped: 0b, 
        Mainhand: [
          {
            Count: 1b, 
            Damage: 0s, 
            Name: "effect:slime_sword", 
            WasPickedUp: 0b, 
            tag: {
              Damage: 0
            }
          }
        ], 
        MarkVariant: 0, 
        NaturalSpawn: 0b, 
        Offhand: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        OnGround: 1b, 
        OwnerNew: -1L, 
        Persistent: 1b, 
        PortalCooldown: 0, 
        Pos: [-10.5f, 59.0f, -2.5f], 
        Pose: {
          LastSignal: 0, 
          PoseIndex: 0
        }, 
        Rotation: [-90.0f, 0.0f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Surface: 0b, 
        Tags: [], 
        TargetID: -1L, 
        TradeExperience: 0, 
        TradeTier: 0, 
        UniqueID: -9225589751772L, 
        Variant: 0, 
        boundX: -7, 
        boundY: 3, 
        boundZ: 1, 
        canPickupItems: 1b, 
        definitions: ["+minecraft:armor_stand", "+"], 
        hasBoundOrigin: 0b, 
        hasSetCanPickupItems: 1b, 
        identifier: "minecraft:armor_stand", 
        limitedLife: 0
      }, 
      {
        ActiveEffects: [
          {
            Ambient: 0b, 
            Amplifier: 0b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 17527140, 
            DurationEasy: 19999574, 
            DurationHard: 19999574, 
            DurationNormal: 19999574, 
            Id: 12b, 
            ShowParticles: 0b
          }
        ], 
        Armor: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        AttackTime: 0s, 
        Attributes: [
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 1024.0f, 
            DefaultMin: -1024.0f, 
            Max: 1024.0f, 
            Min: -1024.0f, 
            Name: "minecraft:luck"
          }, 
          {
            Base: 6.0f, 
            Current: 6.0f, 
            DefaultMax: 6.0f, 
            DefaultMin: 0.0f, 
            Max: 6.0f, 
            Min: 0.0f, 
            Name: "minecraft:health"
          }, 
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 16.0f, 
            DefaultMin: 0.0f, 
            Max: 16.0f, 
            Min: 0.0f, 
            Name: "minecraft:absorption"
          }, 
          {
            Base: 1.0f, 
            Current: 1.0f, 
            DefaultMax: 1.0f, 
            DefaultMin: 0.0f, 
            Max: 1.0f, 
            Min: 0.0f, 
            Name: "minecraft:knockback_resistance"
          }, 
          {
            Base: 0.699999988079071f, 
            Current: 0.699999988079071f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:underwater_movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:lava_movement"
          }, 
          {
            Base: 16.0f, 
            Current: 16.0f, 
            DefaultMax: 2048.0f, 
            DefaultMin: 0.0f, 
            Max: 2048.0f, 
            Min: 0.0f, 
            Name: "minecraft:follow_range"
          }
        ], 
        BodyRot: -90.0f, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        Dead: 0b, 
        DeathTime: 0s, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        HurtTime: 0s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsPregnant: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        LastDimensionId: 0, 
        LeasherID: -1L, 
        LootDropped: 0b, 
        Mainhand: [
          {
            Count: 1b, 
            Damage: 0s, 
            Name: "effect:spectral_sword", 
            WasPickedUp: 0b, 
            tag: {
              Damage: 0
            }
          }
        ], 
        MarkVariant: 0, 
        NaturalSpawn: 0b, 
        Offhand: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        OnGround: 1b, 
        OwnerNew: -1L, 
        Persistent: 1b, 
        PortalCooldown: 0, 
        Pos: [-10.5f, 59.0f, -1.5f], 
        Pose: {
          LastSignal: 0, 
          PoseIndex: 0
        }, 
        Rotation: [-90.0f, 0.0f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Surface: 0b, 
        Tags: [], 
        TargetID: -1L, 
        TradeExperience: 0, 
        TradeTier: 0, 
        UniqueID: -9225589751773L, 
        Variant: 0, 
        boundX: -7, 
        boundY: 3, 
        boundZ: 1, 
        canPickupItems: 0b, 
        definitions: ["+minecraft:armor_stand", "+"], 
        hasBoundOrigin: 0b, 
        hasSetCanPickupItems: 1b, 
        identifier: "minecraft:armor_stand", 
        limitedLife: 0
      }, 
      {
        Armor: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        AttackTime: 0s, 
        Attributes: [
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 1024.0f, 
            DefaultMin: -1024.0f, 
            Max: 1024.0f, 
            Min: -1024.0f, 
            Name: "minecraft:luck"
          }, 
          {
            Base: 6.0f, 
            Current: 6.0f, 
            DefaultMax: 6.0f, 
            DefaultMin: 0.0f, 
            Max: 6.0f, 
            Min: 0.0f, 
            Name: "minecraft:health"
          }, 
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 16.0f, 
            DefaultMin: 0.0f, 
            Max: 16.0f, 
            Min: 0.0f, 
            Name: "minecraft:absorption"
          }, 
          {
            Base: 1.0f, 
            Current: 1.0f, 
            DefaultMax: 1.0f, 
            DefaultMin: 0.0f, 
            Max: 1.0f, 
            Min: 0.0f, 
            Name: "minecraft:knockback_resistance"
          }, 
          {
            Base: 0.699999988079071f, 
            Current: 0.699999988079071f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:underwater_movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:lava_movement"
          }, 
          {
            Base: 16.0f, 
            Current: 16.0f, 
            DefaultMax: 2048.0f, 
            DefaultMin: 0.0f, 
            Max: 2048.0f, 
            Min: 0.0f, 
            Name: "minecraft:follow_range"
          }
        ], 
        BodyRot: -90.0f, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        Dead: 0b, 
        DeathTime: 0s, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        HurtTime: 0s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsPregnant: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        LastDimensionId: 0, 
        LeasherID: -1L, 
        LootDropped: 0b, 
        Mainhand: [
          {
            Count: 1b, 
            Damage: 0s, 
            Name: "effect:sea_sword", 
            WasPickedUp: 0b, 
            tag: {
              Damage: 0
            }
          }
        ], 
        MarkVariant: 0, 
        NaturalSpawn: 0b, 
        Offhand: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        OnGround: 1b, 
        OwnerNew: -1L, 
        Persistent: 1b, 
        PortalCooldown: 0, 
        Pos: [-10.5f, 59.0f, -0.5f], 
        Pose: {
          LastSignal: 0, 
          PoseIndex: 0
        }, 
        Rotation: [-90.0f, 0.0f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Surface: 0b, 
        Tags: [], 
        TargetID: -1L, 
        TradeExperience: 0, 
        TradeTier: 0, 
        UniqueID: -9225589751774L, 
        Variant: 0, 
        boundX: -7, 
        boundY: 3, 
        boundZ: 1, 
        canPickupItems: 0b, 
        definitions: ["+minecraft:armor_stand", "+"], 
        hasBoundOrigin: 0b, 
        hasSetCanPickupItems: 1b, 
        identifier: "minecraft:armor_stand", 
        limitedLife: 0
      }, 
      {
        ActiveEffects: [
          {
            Ambient: 0b, 
            Amplifier: 10b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 16853724, 
            DurationEasy: 19973752, 
            DurationHard: 19973752, 
            DurationNormal: 19973752, 
            Id: 11b, 
            ShowParticles: 0b
          }, 
          {
            Ambient: 0b, 
            Amplifier: 0b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 17527140, 
            DurationEasy: 19969810, 
            DurationHard: 19969810, 
            DurationNormal: 19969810, 
            Id: 12b, 
            ShowParticles: 0b
          }
        ], 
        Armor: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        AttackTime: 0s, 
        Attributes: [
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 1024.0f, 
            DefaultMin: -1024.0f, 
            Max: 1024.0f, 
            Min: -1024.0f, 
            Name: "minecraft:luck"
          }, 
          {
            Base: 6.0f, 
            Current: 1.0f, 
            DefaultMax: 6.0f, 
            DefaultMin: 0.0f, 
            Max: 6.0f, 
            Min: 0.0f, 
            Name: "minecraft:health"
          }, 
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 16.0f, 
            DefaultMin: 0.0f, 
            Max: 16.0f, 
            Min: 0.0f, 
            Name: "minecraft:absorption"
          }, 
          {
            Base: 1.0f, 
            Current: 1.0f, 
            DefaultMax: 1.0f, 
            DefaultMin: 0.0f, 
            Max: 1.0f, 
            Min: 0.0f, 
            Name: "minecraft:knockback_resistance"
          }, 
          {
            Base: 0.699999988079071f, 
            Current: 0.699999988079071f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:underwater_movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:lava_movement"
          }, 
          {
            Base: 16.0f, 
            Current: 16.0f, 
            DefaultMax: 2048.0f, 
            DefaultMin: 0.0f, 
            Max: 2048.0f, 
            Min: 0.0f, 
            Name: "minecraft:follow_range"
          }
        ], 
        BodyRot: -90.0f, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        Dead: 0b, 
        DeathTime: 0s, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        HurtTime: 0s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsPregnant: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        LastDimensionId: 0, 
        LeasherID: -1L, 
        LootDropped: 0b, 
        Mainhand: [
          {
            Count: 1b, 
            Damage: 0s, 
            Name: "effect:ender_sword", 
            WasPickedUp: 0b, 
            tag: {
              Damage: 0
            }
          }
        ], 
        MarkVariant: 0, 
        NaturalSpawn: 0b, 
        Offhand: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        OnGround: 1b, 
        OwnerNew: -1L, 
        Persistent: 1b, 
        PortalCooldown: 0, 
        Pos: [-10.5f, 59.0f, -11.5f], 
        Pose: {
          LastSignal: 0, 
          PoseIndex: 0
        }, 
        Rotation: [-90.0f, 0.0f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Surface: 0b, 
        Tags: [], 
        TargetID: -1L, 
        TradeExperience: 0, 
        TradeTier: 0, 
        UniqueID: -9225589751775L, 
        Variant: 0, 
        boundX: -7, 
        boundY: 3, 
        boundZ: 1, 
        canPickupItems: 0b, 
        definitions: ["+minecraft:armor_stand", "+"], 
        hasBoundOrigin: 0b, 
        hasSetCanPickupItems: 1b, 
        identifier: "minecraft:armor_stand", 
        limitedLife: 0
      }, 
      {
        ActiveEffects: [
          {
            Ambient: 0b, 
            Amplifier: 10b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 16853724, 
            DurationEasy: 19973752, 
            DurationHard: 19973752, 
            DurationNormal: 19973752, 
            Id: 11b, 
            ShowParticles: 0b
          }, 
          {
            Ambient: 0b, 
            Amplifier: 0b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 17527140, 
            DurationEasy: 19969810, 
            DurationHard: 19969810, 
            DurationNormal: 19969810, 
            Id: 12b, 
            ShowParticles: 0b
          }
        ], 
        Armor: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        AttackTime: 0s, 
        Attributes: [
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 1024.0f, 
            DefaultMin: -1024.0f, 
            Max: 1024.0f, 
            Min: -1024.0f, 
            Name: "minecraft:luck"
          }, 
          {
            Base: 6.0f, 
            Current: 1.0f, 
            DefaultMax: 6.0f, 
            DefaultMin: 0.0f, 
            Max: 6.0f, 
            Min: 0.0f, 
            Name: "minecraft:health"
          }, 
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 16.0f, 
            DefaultMin: 0.0f, 
            Max: 16.0f, 
            Min: 0.0f, 
            Name: "minecraft:absorption"
          }, 
          {
            Base: 1.0f, 
            Current: 1.0f, 
            DefaultMax: 1.0f, 
            DefaultMin: 0.0f, 
            Max: 1.0f, 
            Min: 0.0f, 
            Name: "minecraft:knockback_resistance"
          }, 
          {
            Base: 0.699999988079071f, 
            Current: 0.699999988079071f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:underwater_movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:lava_movement"
          }, 
          {
            Base: 16.0f, 
            Current: 16.0f, 
            DefaultMax: 2048.0f, 
            DefaultMin: 0.0f, 
            Max: 2048.0f, 
            Min: 0.0f, 
            Name: "minecraft:follow_range"
          }
        ], 
        BodyRot: -90.0f, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        Dead: 0b, 
        DeathTime: 0s, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        HurtTime: 0s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsPregnant: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        LastDimensionId: 0, 
        LeasherID: -1L, 
        LootDropped: 0b, 
        Mainhand: [
          {
            Count: 1b, 
            Damage: 0s, 
            Name: "effect:wither_sword", 
            WasPickedUp: 0b, 
            tag: {
              Damage: 0
            }
          }
        ], 
        MarkVariant: 0, 
        NaturalSpawn: 0b, 
        Offhand: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        OnGround: 1b, 
        OwnerNew: -1L, 
        Persistent: 1b, 
        PortalCooldown: 0, 
        Pos: [-10.5f, 59.0f, -8.5f], 
        Pose: {
          LastSignal: 0, 
          PoseIndex: 0
        }, 
        Rotation: [-90.0f, 0.0f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Surface: 0b, 
        Tags: [], 
        TargetID: -1L, 
        TradeExperience: 0, 
        TradeTier: 0, 
        UniqueID: -9225589751766L, 
        Variant: 0, 
        boundX: -7, 
        boundY: 3, 
        boundZ: 1, 
        canPickupItems: 1b, 
        definitions: ["+minecraft:armor_stand", "+"], 
        hasBoundOrigin: 0b, 
        hasSetCanPickupItems: 1b, 
        identifier: "minecraft:armor_stand", 
        limitedLife: 0
      }, 
      {
        ActiveEffects: [
          {
            Ambient: 0b, 
            Amplifier: 10b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 16853724, 
            DurationEasy: 19973752, 
            DurationHard: 19973752, 
            DurationNormal: 19973752, 
            Id: 11b, 
            ShowParticles: 0b
          }, 
          {
            Ambient: 0b, 
            Amplifier: 0b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 17527140, 
            DurationEasy: 19969810, 
            DurationHard: 19969810, 
            DurationNormal: 19969810, 
            Id: 12b, 
            ShowParticles: 0b
          }
        ], 
        Armor: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        AttackTime: 0s, 
        Attributes: [
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 1024.0f, 
            DefaultMin: -1024.0f, 
            Max: 1024.0f, 
            Min: -1024.0f, 
            Name: "minecraft:luck"
          }, 
          {
            Base: 6.0f, 
            Current: 1.0f, 
            DefaultMax: 6.0f, 
            DefaultMin: 0.0f, 
            Max: 6.0f, 
            Min: 0.0f, 
            Name: "minecraft:health"
          }, 
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 16.0f, 
            DefaultMin: 0.0f, 
            Max: 16.0f, 
            Min: 0.0f, 
            Name: "minecraft:absorption"
          }, 
          {
            Base: 1.0f, 
            Current: 1.0f, 
            DefaultMax: 1.0f, 
            DefaultMin: 0.0f, 
            Max: 1.0f, 
            Min: 0.0f, 
            Name: "minecraft:knockback_resistance"
          }, 
          {
            Base: 0.699999988079071f, 
            Current: 0.699999988079071f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:underwater_movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:lava_movement"
          }, 
          {
            Base: 16.0f, 
            Current: 16.0f, 
            DefaultMax: 2048.0f, 
            DefaultMin: 0.0f, 
            Max: 2048.0f, 
            Min: 0.0f, 
            Name: "minecraft:follow_range"
          }
        ], 
        BodyRot: -90.0f, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        Dead: 0b, 
        DeathTime: 0s, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        HurtTime: 0s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsPregnant: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        LastDimensionId: 0, 
        LeasherID: -1L, 
        LootDropped: 0b, 
        Mainhand: [
          {
            Count: 1b, 
            Damage: 0s, 
            Name: "effect:lightning_sword", 
            WasPickedUp: 0b, 
            tag: {
              Damage: 0
            }
          }
        ], 
        MarkVariant: 0, 
        NaturalSpawn: 0b, 
        Offhand: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        OnGround: 1b, 
        OwnerNew: -1L, 
        Persistent: 1b, 
        PortalCooldown: 0, 
        Pos: [-10.5f, 59.0f, -10.5f], 
        Pose: {
          LastSignal: 0, 
          PoseIndex: 0
        }, 
        Rotation: [-90.0f, 0.0f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Surface: 0b, 
        Tags: [], 
        TargetID: -1L, 
        TradeExperience: 0, 
        TradeTier: 0, 
        UniqueID: -9225589751777L, 
        Variant: 0, 
        boundX: -7, 
        boundY: 3, 
        boundZ: 1, 
        canPickupItems: 0b, 
        definitions: ["+minecraft:armor_stand", "+"], 
        hasBoundOrigin: 0b, 
        hasSetCanPickupItems: 1b, 
        identifier: "minecraft:armor_stand", 
        limitedLife: 0
      }, 
      {
        ActiveEffects: [
          {
            Ambient: 0b, 
            Amplifier: 10b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 16853724, 
            DurationEasy: 19973752, 
            DurationHard: 19973752, 
            DurationNormal: 19973752, 
            Id: 11b, 
            ShowParticles: 0b
          }, 
          {
            Ambient: 0b, 
            Amplifier: 0b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 17527140, 
            DurationEasy: 19969810, 
            DurationHard: 19969810, 
            DurationNormal: 19969810, 
            Id: 12b, 
            ShowParticles: 0b
          }
        ], 
        Armor: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        AttackTime: 0s, 
        Attributes: [
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 1024.0f, 
            DefaultMin: -1024.0f, 
            Max: 1024.0f, 
            Min: -1024.0f, 
            Name: "minecraft:luck"
          }, 
          {
            Base: 6.0f, 
            Current: 1.0f, 
            DefaultMax: 6.0f, 
            DefaultMin: 0.0f, 
            Max: 6.0f, 
            Min: 0.0f, 
            Name: "minecraft:health"
          }, 
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 16.0f, 
            DefaultMin: 0.0f, 
            Max: 16.0f, 
            Min: 0.0f, 
            Name: "minecraft:absorption"
          }, 
          {
            Base: 1.0f, 
            Current: 1.0f, 
            DefaultMax: 1.0f, 
            DefaultMin: 0.0f, 
            Max: 1.0f, 
            Min: 0.0f, 
            Name: "minecraft:knockback_resistance"
          }, 
          {
            Base: 0.699999988079071f, 
            Current: 0.699999988079071f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:underwater_movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:lava_movement"
          }, 
          {
            Base: 16.0f, 
            Current: 16.0f, 
            DefaultMax: 2048.0f, 
            DefaultMin: 0.0f, 
            Max: 2048.0f, 
            Min: 0.0f, 
            Name: "minecraft:follow_range"
          }
        ], 
        BodyRot: -90.0f, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        Dead: 0b, 
        DeathTime: 0s, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        HurtTime: 0s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsPregnant: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        LastDimensionId: 0, 
        LeasherID: -1L, 
        LootDropped: 0b, 
        Mainhand: [
          {
            Count: 1b, 
            Damage: 0s, 
            Name: "effect:glowstone_sword", 
            WasPickedUp: 0b, 
            tag: {
              Damage: 0
            }
          }
        ], 
        MarkVariant: 0, 
        NaturalSpawn: 0b, 
        Offhand: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        OnGround: 1b, 
        OwnerNew: -1L, 
        Persistent: 1b, 
        PortalCooldown: 0, 
        Pos: [-10.5f, 59.0f, -9.5f], 
        Pose: {
          LastSignal: 0, 
          PoseIndex: 0
        }, 
        Rotation: [-90.0f, 0.0f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Surface: 0b, 
        Tags: [], 
        TargetID: -1L, 
        TradeExperience: 0, 
        TradeTier: 0, 
        UniqueID: -9225589751776L, 
        Variant: 0, 
        boundX: -7, 
        boundY: 3, 
        boundZ: 1, 
        canPickupItems: 1b, 
        definitions: ["+minecraft:armor_stand", "+"], 
        hasBoundOrigin: 0b, 
        hasSetCanPickupItems: 1b, 
        identifier: "minecraft:armor_stand", 
        limitedLife: 0
      }, 
      {
        ActiveEffects: [
          {
            Ambient: 0b, 
            Amplifier: 10b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 16853724, 
            DurationEasy: 19973752, 
            DurationHard: 19973752, 
            DurationNormal: 19973752, 
            Id: 11b, 
            ShowParticles: 0b
          }, 
          {
            Ambient: 0b, 
            Amplifier: 0b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 17527140, 
            DurationEasy: 19969810, 
            DurationHard: 19969810, 
            DurationNormal: 19969810, 
            Id: 12b, 
            ShowParticles: 0b
          }
        ], 
        Armor: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        AttackTime: 0s, 
        Attributes: [
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 1024.0f, 
            DefaultMin: -1024.0f, 
            Max: 1024.0f, 
            Min: -1024.0f, 
            Name: "minecraft:luck"
          }, 
          {
            Base: 6.0f, 
            Current: 1.0f, 
            DefaultMax: 6.0f, 
            DefaultMin: 0.0f, 
            Max: 6.0f, 
            Min: 0.0f, 
            Name: "minecraft:health"
          }, 
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 16.0f, 
            DefaultMin: 0.0f, 
            Max: 16.0f, 
            Min: 0.0f, 
            Name: "minecraft:absorption"
          }, 
          {
            Base: 1.0f, 
            Current: 1.0f, 
            DefaultMax: 1.0f, 
            DefaultMin: 0.0f, 
            Max: 1.0f, 
            Min: 0.0f, 
            Name: "minecraft:knockback_resistance"
          }, 
          {
            Base: 0.699999988079071f, 
            Current: 0.699999988079071f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:underwater_movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:lava_movement"
          }, 
          {
            Base: 16.0f, 
            Current: 16.0f, 
            DefaultMax: 2048.0f, 
            DefaultMin: 0.0f, 
            Max: 2048.0f, 
            Min: 0.0f, 
            Name: "minecraft:follow_range"
          }
        ], 
        BodyRot: -90.0f, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        Dead: 0b, 
        DeathTime: 0s, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        HurtTime: 0s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsPregnant: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        LastDimensionId: 0, 
        LeasherID: -1L, 
        LootDropped: 0b, 
        Mainhand: [
          {
            Count: 1b, 
            Damage: 0s, 
            Name: "effect:tnt_sword", 
            WasPickedUp: 0b, 
            tag: {
              Damage: 0
            }
          }
        ], 
        MarkVariant: 0, 
        NaturalSpawn: 0b, 
        Offhand: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        OnGround: 1b, 
        OwnerNew: -1L, 
        Persistent: 1b, 
        PortalCooldown: 0, 
        Pos: [-10.5f, 59.0f, -7.5f], 
        Pose: {
          LastSignal: 0, 
          PoseIndex: 0
        }, 
        Rotation: [-90.0f, 0.0f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Surface: 0b, 
        Tags: [], 
        TargetID: -1L, 
        TradeExperience: 0, 
        TradeTier: 0, 
        UniqueID: -9225589751767L, 
        Variant: 0, 
        boundX: -7, 
        boundY: 3, 
        boundZ: 1, 
        canPickupItems: 1b, 
        definitions: ["+minecraft:armor_stand", "+"], 
        hasBoundOrigin: 0b, 
        hasSetCanPickupItems: 1b, 
        identifier: "minecraft:armor_stand", 
        limitedLife: 0
      }, 
      {
        ActiveEffects: [
          {
            Ambient: 0b, 
            Amplifier: 0b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 17528446, 
            DurationEasy: 19999574, 
            DurationHard: 19999574, 
            DurationNormal: 19999574, 
            Id: 12b, 
            ShowParticles: 0b
          }
        ], 
        Armor: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        AttackTime: 0s, 
        Attributes: [
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 1024.0f, 
            DefaultMin: -1024.0f, 
            Max: 1024.0f, 
            Min: -1024.0f, 
            Name: "minecraft:luck"
          }, 
          {
            Base: 6.0f, 
            Current: 6.0f, 
            DefaultMax: 6.0f, 
            DefaultMin: 0.0f, 
            Max: 6.0f, 
            Min: 0.0f, 
            Name: "minecraft:health"
          }, 
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 16.0f, 
            DefaultMin: 0.0f, 
            Max: 16.0f, 
            Min: 0.0f, 
            Name: "minecraft:absorption"
          }, 
          {
            Base: 1.0f, 
            Current: 1.0f, 
            DefaultMax: 1.0f, 
            DefaultMin: 0.0f, 
            Max: 1.0f, 
            Min: 0.0f, 
            Name: "minecraft:knockback_resistance"
          }, 
          {
            Base: 0.699999988079071f, 
            Current: 0.699999988079071f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:underwater_movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:lava_movement"
          }, 
          {
            Base: 16.0f, 
            Current: 16.0f, 
            DefaultMax: 2048.0f, 
            DefaultMin: 0.0f, 
            Max: 2048.0f, 
            Min: 0.0f, 
            Name: "minecraft:follow_range"
          }
        ], 
        BodyRot: -90.0f, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        Dead: 0b, 
        DeathTime: 0s, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        HurtTime: 0s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsPregnant: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        LastDimensionId: 0, 
        LeasherID: -1L, 
        LootDropped: 0b, 
        Mainhand: [
          {
            Count: 1b, 
            Damage: 0s, 
            Name: "effect:lapis_sword", 
            WasPickedUp: 0b, 
            tag: {
              Damage: 0
            }
          }
        ], 
        MarkVariant: 0, 
        NaturalSpawn: 0b, 
        Offhand: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        OnGround: 1b, 
        OwnerNew: -1L, 
        Persistent: 1b, 
        PortalCooldown: 0, 
        Pos: [-10.5f, 59.0f, 2.5f], 
        Pose: {
          LastSignal: 0, 
          PoseIndex: 0
        }, 
        Rotation: [-90.0f, 0.0f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Surface: 0b, 
        Tags: [], 
        TargetID: -1L, 
        TradeExperience: 0, 
        TradeTier: 0, 
        UniqueID: -9225589751750L, 
        Variant: 0, 
        boundX: -7, 
        boundY: 3, 
        boundZ: 1, 
        canPickupItems: 0b, 
        definitions: ["+minecraft:armor_stand", "+"], 
        hasBoundOrigin: 0b, 
        hasSetCanPickupItems: 1b, 
        identifier: "minecraft:armor_stand", 
        limitedLife: 0
      }, 
      {
        ActiveEffects: [
          {
            Ambient: 0b, 
            Amplifier: 10b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 16855050, 
            DurationEasy: 19973752, 
            DurationHard: 19973752, 
            DurationNormal: 19973752, 
            Id: 11b, 
            ShowParticles: 0b
          }, 
          {
            Ambient: 0b, 
            Amplifier: 0b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 17528446, 
            DurationEasy: 19969810, 
            DurationHard: 19969810, 
            DurationNormal: 19969810, 
            Id: 12b, 
            ShowParticles: 0b
          }
        ], 
        Armor: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        AttackTime: 0s, 
        Attributes: [
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 1024.0f, 
            DefaultMin: -1024.0f, 
            Max: 1024.0f, 
            Min: -1024.0f, 
            Name: "minecraft:luck"
          }, 
          {
            Base: 6.0f, 
            Current: 6.0f, 
            DefaultMax: 6.0f, 
            DefaultMin: 0.0f, 
            Max: 6.0f, 
            Min: 0.0f, 
            Name: "minecraft:health"
          }, 
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 16.0f, 
            DefaultMin: 0.0f, 
            Max: 16.0f, 
            Min: 0.0f, 
            Name: "minecraft:absorption"
          }, 
          {
            Base: 1.0f, 
            Current: 1.0f, 
            DefaultMax: 1.0f, 
            DefaultMin: 0.0f, 
            Max: 1.0f, 
            Min: 0.0f, 
            Name: "minecraft:knockback_resistance"
          }, 
          {
            Base: 0.699999988079071f, 
            Current: 0.699999988079071f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:underwater_movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:lava_movement"
          }, 
          {
            Base: 16.0f, 
            Current: 16.0f, 
            DefaultMax: 2048.0f, 
            DefaultMin: 0.0f, 
            Max: 2048.0f, 
            Min: 0.0f, 
            Name: "minecraft:follow_range"
          }
        ], 
        BodyRot: -90.0f, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        Dead: 0b, 
        DeathTime: 0s, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        HurtTime: 0s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsPregnant: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        LastDimensionId: 0, 
        LeasherID: -1L, 
        LootDropped: 0b, 
        Mainhand: [
          {
            Count: 1b, 
            Damage: 0s, 
            Name: "effect:bone_sword", 
            WasPickedUp: 0b, 
            tag: {
              Damage: 0
            }
          }
        ], 
        MarkVariant: 0, 
        NaturalSpawn: 0b, 
        Offhand: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        OnGround: 1b, 
        OwnerNew: -1L, 
        Persistent: 1b, 
        PortalCooldown: 0, 
        Pos: [-10.5f, 59.0f, 12.5f], 
        Pose: {
          LastSignal: 0, 
          PoseIndex: 0
        }, 
        Rotation: [-90.0f, 0.0f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Surface: 0b, 
        Tags: [], 
        TargetID: -1L, 
        TradeExperience: 0, 
        TradeTier: 0, 
        UniqueID: -9225589751765L, 
        Variant: 0, 
        boundX: -7, 
        boundY: 3, 
        boundZ: 1, 
        canPickupItems: 0b, 
        definitions: ["+minecraft:armor_stand", "+"], 
        hasBoundOrigin: 0b, 
        hasSetCanPickupItems: 1b, 
        identifier: "minecraft:armor_stand", 
        limitedLife: 0
      }, 
      {
        ActiveEffects: [
          {
            Ambient: 0b, 
            Amplifier: 10b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 16855050, 
            DurationEasy: 19973752, 
            DurationHard: 19973752, 
            DurationNormal: 19973752, 
            Id: 11b, 
            ShowParticles: 0b
          }, 
          {
            Ambient: 0b, 
            Amplifier: 0b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 17528446, 
            DurationEasy: 19969810, 
            DurationHard: 19969810, 
            DurationNormal: 19969810, 
            Id: 12b, 
            ShowParticles: 0b
          }
        ], 
        Armor: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        AttackTime: 0s, 
        Attributes: [
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 1024.0f, 
            DefaultMin: -1024.0f, 
            Max: 1024.0f, 
            Min: -1024.0f, 
            Name: "minecraft:luck"
          }, 
          {
            Base: 6.0f, 
            Current: 6.0f, 
            DefaultMax: 6.0f, 
            DefaultMin: 0.0f, 
            Max: 6.0f, 
            Min: 0.0f, 
            Name: "minecraft:health"
          }, 
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 16.0f, 
            DefaultMin: 0.0f, 
            Max: 16.0f, 
            Min: 0.0f, 
            Name: "minecraft:absorption"
          }, 
          {
            Base: 1.0f, 
            Current: 1.0f, 
            DefaultMax: 1.0f, 
            DefaultMin: 0.0f, 
            Max: 1.0f, 
            Min: 0.0f, 
            Name: "minecraft:knockback_resistance"
          }, 
          {
            Base: 0.699999988079071f, 
            Current: 0.699999988079071f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:underwater_movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:lava_movement"
          }, 
          {
            Base: 16.0f, 
            Current: 16.0f, 
            DefaultMax: 2048.0f, 
            DefaultMin: 0.0f, 
            Max: 2048.0f, 
            Min: 0.0f, 
            Name: "minecraft:follow_range"
          }
        ], 
        BodyRot: -90.0f, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        Dead: 0b, 
        DeathTime: 0s, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        HurtTime: 0s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsPregnant: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        LastDimensionId: 0, 
        LeasherID: -1L, 
        LootDropped: 0b, 
        Mainhand: [
          {
            Count: 1b, 
            Damage: 0s, 
            Name: "effect:emerald_sword", 
            WasPickedUp: 0b, 
            tag: {
              Damage: 0
            }
          }
        ], 
        MarkVariant: 0, 
        NaturalSpawn: 0b, 
        Offhand: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        OnGround: 1b, 
        OwnerNew: -1L, 
        Persistent: 1b, 
        PortalCooldown: 0, 
        Pos: [-10.5f, 59.0f, 8.5f], 
        Pose: {
          LastSignal: 0, 
          PoseIndex: 0
        }, 
        Rotation: [-90.0f, 0.0f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Surface: 0b, 
        Tags: [], 
        TargetID: -1L, 
        TradeExperience: 0, 
        TradeTier: 0, 
        UniqueID: -9225589751764L, 
        Variant: 0, 
        boundX: -7, 
        boundY: 3, 
        boundZ: 1, 
        canPickupItems: 1b, 
        definitions: ["+minecraft:armor_stand", "+"], 
        hasBoundOrigin: 0b, 
        hasSetCanPickupItems: 1b, 
        identifier: "minecraft:armor_stand", 
        limitedLife: 0
      }, 
      {
        ActiveEffects: [
          {
            Ambient: 0b, 
            Amplifier: 10b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 16855050, 
            DurationEasy: 19973752, 
            DurationHard: 19973752, 
            DurationNormal: 19973752, 
            Id: 11b, 
            ShowParticles: 0b
          }, 
          {
            Ambient: 0b, 
            Amplifier: 0b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 17528446, 
            DurationEasy: 19969810, 
            DurationHard: 19969810, 
            DurationNormal: 19969810, 
            Id: 12b, 
            ShowParticles: 0b
          }
        ], 
        Armor: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        AttackTime: 0s, 
        Attributes: [
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 1024.0f, 
            DefaultMin: -1024.0f, 
            Max: 1024.0f, 
            Min: -1024.0f, 
            Name: "minecraft:luck"
          }, 
          {
            Base: 6.0f, 
            Current: 6.0f, 
            DefaultMax: 6.0f, 
            DefaultMin: 0.0f, 
            Max: 6.0f, 
            Min: 0.0f, 
            Name: "minecraft:health"
          }, 
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 16.0f, 
            DefaultMin: 0.0f, 
            Max: 16.0f, 
            Min: 0.0f, 
            Name: "minecraft:absorption"
          }, 
          {
            Base: 1.0f, 
            Current: 1.0f, 
            DefaultMax: 1.0f, 
            DefaultMin: 0.0f, 
            Max: 1.0f, 
            Min: 0.0f, 
            Name: "minecraft:knockback_resistance"
          }, 
          {
            Base: 0.699999988079071f, 
            Current: 0.699999988079071f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:underwater_movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:lava_movement"
          }, 
          {
            Base: 16.0f, 
            Current: 16.0f, 
            DefaultMax: 2048.0f, 
            DefaultMin: 0.0f, 
            Max: 2048.0f, 
            Min: 0.0f, 
            Name: "minecraft:follow_range"
          }
        ], 
        BodyRot: -90.0f, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        Dead: 0b, 
        DeathTime: 0s, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        HurtTime: 0s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsPregnant: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        LastDimensionId: 0, 
        LeasherID: -1L, 
        LootDropped: 0b, 
        Mainhand: [
          {
            Count: 1b, 
            Damage: 0s, 
            Name: "effect:fire_sword", 
            WasPickedUp: 0b, 
            tag: {
              Damage: 0
            }
          }
        ], 
        MarkVariant: 0, 
        NaturalSpawn: 0b, 
        Offhand: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        OnGround: 1b, 
        OwnerNew: -1L, 
        Persistent: 1b, 
        PortalCooldown: 0, 
        Pos: [-10.5f, 59.0f, 7.5f], 
        Pose: {
          LastSignal: 0, 
          PoseIndex: 0
        }, 
        Rotation: [-90.0f, 0.0f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Surface: 0b, 
        Tags: [], 
        TargetID: -1L, 
        TradeExperience: 0, 
        TradeTier: 0, 
        UniqueID: -9225589751763L, 
        Variant: 0, 
        boundX: -7, 
        boundY: 3, 
        boundZ: 1, 
        canPickupItems: 1b, 
        definitions: ["+minecraft:armor_stand", "+"], 
        hasBoundOrigin: 0b, 
        hasSetCanPickupItems: 1b, 
        identifier: "minecraft:armor_stand", 
        limitedLife: 0
      }, 
      {
        ActiveEffects: [
          {
            Ambient: 0b, 
            Amplifier: 10b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 16855050, 
            DurationEasy: 19973752, 
            DurationHard: 19973752, 
            DurationNormal: 19973752, 
            Id: 11b, 
            ShowParticles: 0b
          }, 
          {
            Ambient: 0b, 
            Amplifier: 0b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 17528446, 
            DurationEasy: 19969810, 
            DurationHard: 19969810, 
            DurationNormal: 19969810, 
            Id: 12b, 
            ShowParticles: 0b
          }
        ], 
        Armor: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        AttackTime: 0s, 
        Attributes: [
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 1024.0f, 
            DefaultMin: -1024.0f, 
            Max: 1024.0f, 
            Min: -1024.0f, 
            Name: "minecraft:luck"
          }, 
          {
            Base: 6.0f, 
            Current: 6.0f, 
            DefaultMax: 6.0f, 
            DefaultMin: 0.0f, 
            Max: 6.0f, 
            Min: 0.0f, 
            Name: "minecraft:health"
          }, 
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 16.0f, 
            DefaultMin: 0.0f, 
            Max: 16.0f, 
            Min: 0.0f, 
            Name: "minecraft:absorption"
          }, 
          {
            Base: 1.0f, 
            Current: 1.0f, 
            DefaultMax: 1.0f, 
            DefaultMin: 0.0f, 
            Max: 1.0f, 
            Min: 0.0f, 
            Name: "minecraft:knockback_resistance"
          }, 
          {
            Base: 0.699999988079071f, 
            Current: 0.699999988079071f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:underwater_movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:lava_movement"
          }, 
          {
            Base: 16.0f, 
            Current: 16.0f, 
            DefaultMax: 2048.0f, 
            DefaultMin: 0.0f, 
            Max: 2048.0f, 
            Min: 0.0f, 
            Name: "minecraft:follow_range"
          }
        ], 
        BodyRot: -90.0f, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        Dead: 0b, 
        DeathTime: 0s, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        HurtTime: 0s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsPregnant: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        LastDimensionId: 0, 
        LeasherID: -1L, 
        LootDropped: 0b, 
        Mainhand: [
          {
            Count: 1b, 
            Damage: 0s, 
            Name: "effect:blaze_sword", 
            WasPickedUp: 0b, 
            tag: {
              Damage: 0
            }
          }
        ], 
        MarkVariant: 0, 
        NaturalSpawn: 0b, 
        Offhand: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        OnGround: 1b, 
        OwnerNew: -1L, 
        Persistent: 1b, 
        PortalCooldown: 0, 
        Pos: [-10.5f, 59.0f, 13.5f], 
        Pose: {
          LastSignal: 0, 
          PoseIndex: 0
        }, 
        Rotation: [-90.0f, 0.0f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Surface: 0b, 
        Tags: [], 
        TargetID: -1L, 
        TradeExperience: 0, 
        TradeTier: 0, 
        UniqueID: -9225589751762L, 
        Variant: 0, 
        boundX: -7, 
        boundY: 3, 
        boundZ: 1, 
        canPickupItems: 1b, 
        definitions: ["+minecraft:armor_stand", "+"], 
        hasBoundOrigin: 0b, 
        hasSetCanPickupItems: 1b, 
        identifier: "minecraft:armor_stand", 
        limitedLife: 0
      }, 
      {
        ActiveEffects: [
          {
            Ambient: 0b, 
            Amplifier: 10b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 16855050, 
            DurationEasy: 19973752, 
            DurationHard: 19973752, 
            DurationNormal: 19973752, 
            Id: 11b, 
            ShowParticles: 0b
          }, 
          {
            Ambient: 0b, 
            Amplifier: 0b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 17528446, 
            DurationEasy: 19969810, 
            DurationHard: 19969810, 
            DurationNormal: 19969810, 
            Id: 12b, 
            ShowParticles: 0b
          }
        ], 
        Armor: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        AttackTime: 0s, 
        Attributes: [
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 1024.0f, 
            DefaultMin: -1024.0f, 
            Max: 1024.0f, 
            Min: -1024.0f, 
            Name: "minecraft:luck"
          }, 
          {
            Base: 6.0f, 
            Current: 6.0f, 
            DefaultMax: 6.0f, 
            DefaultMin: 0.0f, 
            Max: 6.0f, 
            Min: 0.0f, 
            Name: "minecraft:health"
          }, 
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 16.0f, 
            DefaultMin: 0.0f, 
            Max: 16.0f, 
            Min: 0.0f, 
            Name: "minecraft:absorption"
          }, 
          {
            Base: 1.0f, 
            Current: 1.0f, 
            DefaultMax: 1.0f, 
            DefaultMin: 0.0f, 
            Max: 1.0f, 
            Min: 0.0f, 
            Name: "minecraft:knockback_resistance"
          }, 
          {
            Base: 0.699999988079071f, 
            Current: 0.699999988079071f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:underwater_movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:lava_movement"
          }, 
          {
            Base: 16.0f, 
            Current: 16.0f, 
            DefaultMax: 2048.0f, 
            DefaultMin: 0.0f, 
            Max: 2048.0f, 
            Min: 0.0f, 
            Name: "minecraft:follow_range"
          }
        ], 
        BodyRot: -90.0f, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        Dead: 0b, 
        DeathTime: 0s, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        HurtTime: 0s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsPregnant: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        LastDimensionId: 0, 
        LeasherID: -1L, 
        LootDropped: 0b, 
        Mainhand: [
          {
            Count: 1b, 
            Damage: 0s, 
            Name: "effect:creeper_sword", 
            WasPickedUp: 0b, 
            tag: {
              Damage: 0
            }
          }
        ], 
        MarkVariant: 0, 
        NaturalSpawn: 0b, 
        Offhand: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        OnGround: 1b, 
        OwnerNew: -1L, 
        Persistent: 1b, 
        PortalCooldown: 0, 
        Pos: [-10.5f, 59.0f, 9.5f], 
        Pose: {
          LastSignal: 0, 
          PoseIndex: 0
        }, 
        Rotation: [-90.0f, 0.0f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Surface: 0b, 
        Tags: [], 
        TargetID: -1L, 
        TradeExperience: 0, 
        TradeTier: 0, 
        UniqueID: -9225589751761L, 
        Variant: 0, 
        boundX: -7, 
        boundY: 3, 
        boundZ: 1, 
        canPickupItems: 1b, 
        definitions: ["+minecraft:armor_stand", "+"], 
        hasBoundOrigin: 0b, 
        hasSetCanPickupItems: 1b, 
        identifier: "minecraft:armor_stand", 
        limitedLife: 0
      }, 
      {
        Armor: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        AttackTime: 0s, 
        Attributes: [
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 1024.0f, 
            DefaultMin: -1024.0f, 
            Max: 1024.0f, 
            Min: -1024.0f, 
            Name: "minecraft:luck"
          }, 
          {
            Base: 6.0f, 
            Current: 6.0f, 
            DefaultMax: 6.0f, 
            DefaultMin: 0.0f, 
            Max: 6.0f, 
            Min: 0.0f, 
            Name: "minecraft:health"
          }, 
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 16.0f, 
            DefaultMin: 0.0f, 
            Max: 16.0f, 
            Min: 0.0f, 
            Name: "minecraft:absorption"
          }, 
          {
            Base: 1.0f, 
            Current: 1.0f, 
            DefaultMax: 1.0f, 
            DefaultMin: 0.0f, 
            Max: 1.0f, 
            Min: 0.0f, 
            Name: "minecraft:knockback_resistance"
          }, 
          {
            Base: 0.699999988079071f, 
            Current: 0.699999988079071f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:underwater_movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:lava_movement"
          }, 
          {
            Base: 16.0f, 
            Current: 16.0f, 
            DefaultMax: 2048.0f, 
            DefaultMin: 0.0f, 
            Max: 2048.0f, 
            Min: 0.0f, 
            Name: "minecraft:follow_range"
          }
        ], 
        BodyRot: -90.0f, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        Dead: 0b, 
        DeathTime: 0s, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        HurtTime: 0s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsPregnant: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        LastDimensionId: 0, 
        LeasherID: -1L, 
        LootDropped: 0b, 
        Mainhand: [
          {
            Count: 1b, 
            Damage: 0s, 
            Name: "effect:wet_sponge_sword", 
            WasPickedUp: 0b, 
            tag: {
              Damage: 0
            }
          }
        ], 
        MarkVariant: 0, 
        NaturalSpawn: 0b, 
        Offhand: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        OnGround: 1b, 
        OwnerNew: -1L, 
        Persistent: 1b, 
        PortalCooldown: 0, 
        Pos: [-10.5f, 59.0f, 14.5f], 
        Pose: {
          LastSignal: 0, 
          PoseIndex: 0
        }, 
        Rotation: [-90.0f, 0.0f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Surface: 0b, 
        Tags: [], 
        TargetID: -1L, 
        TradeExperience: 0, 
        TradeTier: 0, 
        UniqueID: -9225589751760L, 
        Variant: 0, 
        boundX: 0, 
        boundY: 0, 
        boundZ: 0, 
        canPickupItems: 0b, 
        definitions: ["+minecraft:armor_stand", "+"], 
        hasBoundOrigin: 0b, 
        hasSetCanPickupItems: 1b, 
        identifier: "minecraft:armor_stand", 
        limitedLife: 0
      }, 
      {
        ActiveEffects: [
          {
            Ambient: 0b, 
            Amplifier: 10b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 16855050, 
            DurationEasy: 19973752, 
            DurationHard: 19973752, 
            DurationNormal: 19973752, 
            Id: 11b, 
            ShowParticles: 0b
          }, 
          {
            Ambient: 0b, 
            Amplifier: 0b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 17528446, 
            DurationEasy: 19969810, 
            DurationHard: 19969810, 
            DurationNormal: 19969810, 
            Id: 12b, 
            ShowParticles: 0b
          }
        ], 
        Armor: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        AttackTime: 0s, 
        Attributes: [
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 1024.0f, 
            DefaultMin: -1024.0f, 
            Max: 1024.0f, 
            Min: -1024.0f, 
            Name: "minecraft:luck"
          }, 
          {
            Base: 6.0f, 
            Current: 6.0f, 
            DefaultMax: 6.0f, 
            DefaultMin: 0.0f, 
            Max: 6.0f, 
            Min: 0.0f, 
            Name: "minecraft:health"
          }, 
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 16.0f, 
            DefaultMin: 0.0f, 
            Max: 16.0f, 
            Min: 0.0f, 
            Name: "minecraft:absorption"
          }, 
          {
            Base: 1.0f, 
            Current: 1.0f, 
            DefaultMax: 1.0f, 
            DefaultMin: 0.0f, 
            Max: 1.0f, 
            Min: 0.0f, 
            Name: "minecraft:knockback_resistance"
          }, 
          {
            Base: 0.699999988079071f, 
            Current: 0.699999988079071f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:underwater_movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:lava_movement"
          }, 
          {
            Base: 16.0f, 
            Current: 16.0f, 
            DefaultMax: 2048.0f, 
            DefaultMin: 0.0f, 
            Max: 2048.0f, 
            Min: 0.0f, 
            Name: "minecraft:follow_range"
          }
        ], 
        BodyRot: -90.0f, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        Dead: 0b, 
        DeathTime: 0s, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        HurtTime: 0s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsPregnant: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        LastDimensionId: 0, 
        LeasherID: -1L, 
        LootDropped: 0b, 
        Mainhand: [
          {
            Count: 1b, 
            Damage: 0s, 
            Name: "effect:coal_sword", 
            WasPickedUp: 0b, 
            tag: {
              Damage: 0
            }
          }
        ], 
        MarkVariant: 0, 
        NaturalSpawn: 0b, 
        Offhand: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        OnGround: 1b, 
        OwnerNew: -1L, 
        Persistent: 1b, 
        PortalCooldown: 0, 
        Pos: [-10.5f, 59.0f, 10.5f], 
        Pose: {
          LastSignal: 0, 
          PoseIndex: 0
        }, 
        Rotation: [-90.0f, 0.0f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Surface: 0b, 
        Tags: [], 
        TargetID: -1L, 
        TradeExperience: 0, 
        TradeTier: 0, 
        UniqueID: -9225589751759L, 
        Variant: 0, 
        boundX: -7, 
        boundY: 3, 
        boundZ: 1, 
        canPickupItems: 0b, 
        definitions: ["+minecraft:armor_stand", "+"], 
        hasBoundOrigin: 0b, 
        hasSetCanPickupItems: 1b, 
        identifier: "minecraft:armor_stand", 
        limitedLife: 0
      }, 
      {
        Armor: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        AttackTime: 0s, 
        Attributes: [
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 1024.0f, 
            DefaultMin: -1024.0f, 
            Max: 1024.0f, 
            Min: -1024.0f, 
            Name: "minecraft:luck"
          }, 
          {
            Base: 6.0f, 
            Current: 6.0f, 
            DefaultMax: 6.0f, 
            DefaultMin: 0.0f, 
            Max: 6.0f, 
            Min: 0.0f, 
            Name: "minecraft:health"
          }, 
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 16.0f, 
            DefaultMin: 0.0f, 
            Max: 16.0f, 
            Min: 0.0f, 
            Name: "minecraft:absorption"
          }, 
          {
            Base: 1.0f, 
            Current: 1.0f, 
            DefaultMax: 1.0f, 
            DefaultMin: 0.0f, 
            Max: 1.0f, 
            Min: 0.0f, 
            Name: "minecraft:knockback_resistance"
          }, 
          {
            Base: 0.699999988079071f, 
            Current: 0.699999988079071f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:underwater_movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:lava_movement"
          }, 
          {
            Base: 16.0f, 
            Current: 16.0f, 
            DefaultMax: 2048.0f, 
            DefaultMin: 0.0f, 
            Max: 2048.0f, 
            Min: 0.0f, 
            Name: "minecraft:follow_range"
          }
        ], 
        BodyRot: -90.0f, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        Dead: 0b, 
        DeathTime: 0s, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        HurtTime: 0s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsPregnant: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        LastDimensionId: 0, 
        LeasherID: -1L, 
        LootDropped: 0b, 
        Mainhand: [
          {
            Count: 1b, 
            Damage: 0s, 
            Name: "effect:ultra_instinct_sword", 
            WasPickedUp: 0b, 
            tag: {
              Damage: 20
            }
          }
        ], 
        MarkVariant: 0, 
        NaturalSpawn: 0b, 
        Offhand: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        OnGround: 1b, 
        OwnerNew: -1L, 
        Persistent: 1b, 
        PortalCooldown: 0, 
        Pos: [-10.5f, 59.0f, 15.5f], 
        Pose: {
          LastSignal: 0, 
          PoseIndex: 0
        }, 
        Rotation: [-90.0f, 0.0f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Surface: 0b, 
        Tags: [], 
        TargetID: -1L, 
        TradeExperience: 0, 
        TradeTier: 0, 
        UniqueID: -9225589751758L, 
        Variant: 0, 
        boundX: 0, 
        boundY: 0, 
        boundZ: 0, 
        canPickupItems: 0b, 
        definitions: ["+minecraft:armor_stand", "+"], 
        hasBoundOrigin: 0b, 
        hasSetCanPickupItems: 1b, 
        identifier: "minecraft:armor_stand", 
        limitedLife: 0
      }, 
      {
        ActiveEffects: [
          {
            Ambient: 0b, 
            Amplifier: 0b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 17524536, 
            DurationEasy: 19999574, 
            DurationHard: 19999574, 
            DurationNormal: 19999574, 
            Id: 12b, 
            ShowParticles: 0b
          }
        ], 
        Armor: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        AttackTime: 0s, 
        Attributes: [
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 1024.0f, 
            DefaultMin: -1024.0f, 
            Max: 1024.0f, 
            Min: -1024.0f, 
            Name: "minecraft:luck"
          }, 
          {
            Base: 6.0f, 
            Current: 6.0f, 
            DefaultMax: 6.0f, 
            DefaultMin: 0.0f, 
            Max: 6.0f, 
            Min: 0.0f, 
            Name: "minecraft:health"
          }, 
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 16.0f, 
            DefaultMin: 0.0f, 
            Max: 16.0f, 
            Min: 0.0f, 
            Name: "minecraft:absorption"
          }, 
          {
            Base: 1.0f, 
            Current: 1.0f, 
            DefaultMax: 1.0f, 
            DefaultMin: 0.0f, 
            Max: 1.0f, 
            Min: 0.0f, 
            Name: "minecraft:knockback_resistance"
          }, 
          {
            Base: 0.699999988079071f, 
            Current: 0.699999988079071f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:underwater_movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:lava_movement"
          }, 
          {
            Base: 16.0f, 
            Current: 16.0f, 
            DefaultMax: 2048.0f, 
            DefaultMin: 0.0f, 
            Max: 2048.0f, 
            Min: 0.0f, 
            Name: "minecraft:follow_range"
          }
        ], 
        BodyRot: -90.0f, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        Dead: 0b, 
        DeathTime: 0s, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        HurtTime: 0s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsPregnant: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        LastDimensionId: 0, 
        LeasherID: -1L, 
        LootDropped: 0b, 
        Mainhand: [
          {
            Count: 1b, 
            Damage: 0s, 
            Name: "effect:quartz_sword", 
            WasPickedUp: 0b, 
            tag: {
              Damage: 0
            }
          }
        ], 
        MarkVariant: 0, 
        NaturalSpawn: 0b, 
        Offhand: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        OnGround: 1b, 
        OwnerNew: -1L, 
        Persistent: 1b, 
        PortalCooldown: 0, 
        Pos: [-10.5f, 59.0f, 0.5f], 
        Pose: {
          LastSignal: 0, 
          PoseIndex: 0
        }, 
        Rotation: [-90.0f, 0.0f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Surface: 0b, 
        Tags: [], 
        TargetID: -1L, 
        TradeExperience: 0, 
        TradeTier: 0, 
        UniqueID: -9225589751757L, 
        Variant: 0, 
        boundX: -7, 
        boundY: 3, 
        boundZ: 1, 
        canPickupItems: 0b, 
        definitions: ["+minecraft:armor_stand", "+"], 
        hasBoundOrigin: 0b, 
        hasSetCanPickupItems: 1b, 
        identifier: "minecraft:armor_stand", 
        limitedLife: 0
      }, 
      {
        ActiveEffects: [
          {
            Ambient: 0b, 
            Amplifier: 0b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 17524536, 
            DurationEasy: 19999574, 
            DurationHard: 19999574, 
            DurationNormal: 19999574, 
            Id: 12b, 
            ShowParticles: 0b
          }
        ], 
        Armor: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        AttackTime: 0s, 
        Attributes: [
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 1024.0f, 
            DefaultMin: -1024.0f, 
            Max: 1024.0f, 
            Min: -1024.0f, 
            Name: "minecraft:luck"
          }, 
          {
            Base: 6.0f, 
            Current: 6.0f, 
            DefaultMax: 6.0f, 
            DefaultMin: 0.0f, 
            Max: 6.0f, 
            Min: 0.0f, 
            Name: "minecraft:health"
          }, 
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 16.0f, 
            DefaultMin: 0.0f, 
            Max: 16.0f, 
            Min: 0.0f, 
            Name: "minecraft:absorption"
          }, 
          {
            Base: 1.0f, 
            Current: 1.0f, 
            DefaultMax: 1.0f, 
            DefaultMin: 0.0f, 
            Max: 1.0f, 
            Min: 0.0f, 
            Name: "minecraft:knockback_resistance"
          }, 
          {
            Base: 0.699999988079071f, 
            Current: 0.699999988079071f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:underwater_movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:lava_movement"
          }, 
          {
            Base: 16.0f, 
            Current: 16.0f, 
            DefaultMax: 2048.0f, 
            DefaultMin: 0.0f, 
            Max: 2048.0f, 
            Min: 0.0f, 
            Name: "minecraft:follow_range"
          }
        ], 
        BodyRot: -90.0f, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        Dead: 0b, 
        DeathTime: 0s, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        HurtTime: 0s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsPregnant: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        LastDimensionId: 0, 
        LeasherID: -1L, 
        LootDropped: 0b, 
        Mainhand: [
          {
            Count: 1b, 
            Damage: 0s, 
            Name: "effect:obsidian_sword", 
            WasPickedUp: 0b, 
            tag: {
              Damage: 0
            }
          }
        ], 
        MarkVariant: 0, 
        NaturalSpawn: 0b, 
        Offhand: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        OnGround: 1b, 
        OwnerNew: -1L, 
        Persistent: 1b, 
        PortalCooldown: 0, 
        Pos: [-10.5f, 59.0f, 1.5f], 
        Pose: {
          LastSignal: 0, 
          PoseIndex: 0
        }, 
        Rotation: [-90.0f, 0.0f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Surface: 0b, 
        Tags: [], 
        TargetID: -1L, 
        TradeExperience: 0, 
        TradeTier: 0, 
        UniqueID: -9225589751756L, 
        Variant: 0, 
        boundX: -7, 
        boundY: 3, 
        boundZ: 1, 
        canPickupItems: 0b, 
        definitions: ["+minecraft:armor_stand", "+"], 
        hasBoundOrigin: 0b, 
        hasSetCanPickupItems: 1b, 
        identifier: "minecraft:armor_stand", 
        limitedLife: 0
      }, 
      {
        ActiveEffects: [
          {
            Ambient: 0b, 
            Amplifier: 10b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 16855050, 
            DurationEasy: 19973752, 
            DurationHard: 19973752, 
            DurationNormal: 19973752, 
            Id: 11b, 
            ShowParticles: 0b
          }, 
          {
            Ambient: 0b, 
            Amplifier: 0b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 17528446, 
            DurationEasy: 19969810, 
            DurationHard: 19969810, 
            DurationNormal: 19969810, 
            Id: 12b, 
            ShowParticles: 0b
          }
        ], 
        Armor: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        AttackTime: 0s, 
        Attributes: [
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 1024.0f, 
            DefaultMin: -1024.0f, 
            Max: 1024.0f, 
            Min: -1024.0f, 
            Name: "minecraft:luck"
          }, 
          {
            Base: 6.0f, 
            Current: 1.0f, 
            DefaultMax: 6.0f, 
            DefaultMin: 0.0f, 
            Max: 6.0f, 
            Min: 0.0f, 
            Name: "minecraft:health"
          }, 
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 16.0f, 
            DefaultMin: 0.0f, 
            Max: 16.0f, 
            Min: 0.0f, 
            Name: "minecraft:absorption"
          }, 
          {
            Base: 1.0f, 
            Current: 1.0f, 
            DefaultMax: 1.0f, 
            DefaultMin: 0.0f, 
            Max: 1.0f, 
            Min: 0.0f, 
            Name: "minecraft:knockback_resistance"
          }, 
          {
            Base: 0.699999988079071f, 
            Current: 0.699999988079071f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:underwater_movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:lava_movement"
          }, 
          {
            Base: 16.0f, 
            Current: 16.0f, 
            DefaultMax: 2048.0f, 
            DefaultMin: 0.0f, 
            Max: 2048.0f, 
            Min: 0.0f, 
            Name: "minecraft:follow_range"
          }
        ], 
        BodyRot: -90.0f, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        Dead: 0b, 
        DeathTime: 0s, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        HurtTime: 0s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsPregnant: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        LastDimensionId: 0, 
        LeasherID: -1L, 
        LootDropped: 0b, 
        Mainhand: [
          {
            Count: 1b, 
            Damage: 0s, 
            Name: "effect:grass_sword", 
            WasPickedUp: 0b, 
            tag: {
              Damage: 0
            }
          }
        ], 
        MarkVariant: 0, 
        NaturalSpawn: 0b, 
        Offhand: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        OnGround: 1b, 
        OwnerNew: -1L, 
        Persistent: 1b, 
        PortalCooldown: 0, 
        Pos: [-10.5f, 59.0f, 6.5f], 
        Pose: {
          LastSignal: 0, 
          PoseIndex: 0
        }, 
        Rotation: [-90.0f, 0.0f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Surface: 0b, 
        Tags: [], 
        TargetID: -1L, 
        TradeExperience: 0, 
        TradeTier: 0, 
        UniqueID: -9225589751755L, 
        Variant: 0, 
        boundX: -7, 
        boundY: 3, 
        boundZ: 1, 
        canPickupItems: 1b, 
        definitions: ["+minecraft:armor_stand", "+"], 
        hasBoundOrigin: 0b, 
        hasSetCanPickupItems: 1b, 
        identifier: "minecraft:armor_stand", 
        limitedLife: 0
      }, 
      {
        ActiveEffects: [
          {
            Ambient: 0b, 
            Amplifier: 10b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 16855050, 
            DurationEasy: 19973752, 
            DurationHard: 19973752, 
            DurationNormal: 19973752, 
            Id: 11b, 
            ShowParticles: 0b
          }, 
          {
            Ambient: 0b, 
            Amplifier: 0b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 17528446, 
            DurationEasy: 19969810, 
            DurationHard: 19969810, 
            DurationNormal: 19969810, 
            Id: 12b, 
            ShowParticles: 0b
          }
        ], 
        Armor: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        AttackTime: 0s, 
        Attributes: [
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 1024.0f, 
            DefaultMin: -1024.0f, 
            Max: 1024.0f, 
            Min: -1024.0f, 
            Name: "minecraft:luck"
          }, 
          {
            Base: 6.0f, 
            Current: 6.0f, 
            DefaultMax: 6.0f, 
            DefaultMin: 0.0f, 
            Max: 6.0f, 
            Min: 0.0f, 
            Name: "minecraft:health"
          }, 
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 16.0f, 
            DefaultMin: 0.0f, 
            Max: 16.0f, 
            Min: 0.0f, 
            Name: "minecraft:absorption"
          }, 
          {
            Base: 1.0f, 
            Current: 1.0f, 
            DefaultMax: 1.0f, 
            DefaultMin: 0.0f, 
            Max: 1.0f, 
            Min: 0.0f, 
            Name: "minecraft:knockback_resistance"
          }, 
          {
            Base: 0.699999988079071f, 
            Current: 0.699999988079071f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:underwater_movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:lava_movement"
          }, 
          {
            Base: 16.0f, 
            Current: 16.0f, 
            DefaultMax: 2048.0f, 
            DefaultMin: 0.0f, 
            Max: 2048.0f, 
            Min: 0.0f, 
            Name: "minecraft:follow_range"
          }
        ], 
        BodyRot: -90.0f, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        Dead: 0b, 
        DeathTime: 0s, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        HurtTime: 0s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsPregnant: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        LastDimensionId: 0, 
        LeasherID: -1L, 
        LootDropped: 0b, 
        Mainhand: [
          {
            Count: 1b, 
            Damage: 0s, 
            Name: "effect:cactus_sword", 
            WasPickedUp: 0b, 
            tag: {
              Damage: 0
            }
          }
        ], 
        MarkVariant: 0, 
        NaturalSpawn: 0b, 
        Offhand: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        OnGround: 1b, 
        OwnerNew: -1L, 
        Persistent: 1b, 
        PortalCooldown: 0, 
        Pos: [-10.5f, 59.0f, 11.5f], 
        Pose: {
          LastSignal: 0, 
          PoseIndex: 0
        }, 
        Rotation: [-90.0f, 0.0f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Surface: 0b, 
        Tags: [], 
        TargetID: -1L, 
        TradeExperience: 0, 
        TradeTier: 0, 
        UniqueID: -9225589751754L, 
        Variant: 0, 
        boundX: -7, 
        boundY: 3, 
        boundZ: 1, 
        canPickupItems: 0b, 
        definitions: ["+minecraft:armor_stand", "+"], 
        hasBoundOrigin: 0b, 
        hasSetCanPickupItems: 1b, 
        identifier: "minecraft:armor_stand", 
        limitedLife: 0
      }, 
      {
        ActiveEffects: [
          {
            Ambient: 0b, 
            Amplifier: 0b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 17528446, 
            DurationEasy: 19999574, 
            DurationHard: 19999574, 
            DurationNormal: 19999574, 
            Id: 12b, 
            ShowParticles: 0b
          }
        ], 
        Armor: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        AttackTime: 0s, 
        Attributes: [
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 1024.0f, 
            DefaultMin: -1024.0f, 
            Max: 1024.0f, 
            Min: -1024.0f, 
            Name: "minecraft:luck"
          }, 
          {
            Base: 6.0f, 
            Current: 6.0f, 
            DefaultMax: 6.0f, 
            DefaultMin: 0.0f, 
            Max: 6.0f, 
            Min: 0.0f, 
            Name: "minecraft:health"
          }, 
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 16.0f, 
            DefaultMin: 0.0f, 
            Max: 16.0f, 
            Min: 0.0f, 
            Name: "minecraft:absorption"
          }, 
          {
            Base: 1.0f, 
            Current: 1.0f, 
            DefaultMax: 1.0f, 
            DefaultMin: 0.0f, 
            Max: 1.0f, 
            Min: 0.0f, 
            Name: "minecraft:knockback_resistance"
          }, 
          {
            Base: 0.699999988079071f, 
            Current: 0.699999988079071f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:underwater_movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:lava_movement"
          }, 
          {
            Base: 16.0f, 
            Current: 16.0f, 
            DefaultMax: 2048.0f, 
            DefaultMin: 0.0f, 
            Max: 2048.0f, 
            Min: 0.0f, 
            Name: "minecraft:follow_range"
          }
        ], 
        BodyRot: -90.0f, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        Dead: 0b, 
        DeathTime: 0s, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        HurtTime: 0s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsPregnant: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        LastDimensionId: 0, 
        LeasherID: -1L, 
        LootDropped: 0b, 
        Mainhand: [
          {
            Count: 1b, 
            Damage: 0s, 
            Name: "effect:jungle_sword", 
            WasPickedUp: 0b, 
            tag: {
              Damage: 0
            }
          }
        ], 
        MarkVariant: 0, 
        NaturalSpawn: 0b, 
        Offhand: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        OnGround: 1b, 
        OwnerNew: -1L, 
        Persistent: 1b, 
        PortalCooldown: 0, 
        Pos: [-10.5f, 59.0f, 5.5f], 
        Pose: {
          LastSignal: 0, 
          PoseIndex: 0
        }, 
        Rotation: [-90.0f, 0.0f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Surface: 0b, 
        Tags: [], 
        TargetID: -1L, 
        TradeExperience: 0, 
        TradeTier: 0, 
        UniqueID: -9225589751753L, 
        Variant: 0, 
        boundX: -7, 
        boundY: 3, 
        boundZ: 1, 
        canPickupItems: 0b, 
        definitions: ["+minecraft:armor_stand", "+"], 
        hasBoundOrigin: 0b, 
        hasSetCanPickupItems: 1b, 
        identifier: "minecraft:armor_stand", 
        limitedLife: 0
      }, 
      {
        ActiveEffects: [
          {
            Ambient: 0b, 
            Amplifier: 0b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 17528446, 
            DurationEasy: 19999574, 
            DurationHard: 19999574, 
            DurationNormal: 19999574, 
            Id: 12b, 
            ShowParticles: 0b
          }
        ], 
        Armor: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        AttackTime: 0s, 
        Attributes: [
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 1024.0f, 
            DefaultMin: -1024.0f, 
            Max: 1024.0f, 
            Min: -1024.0f, 
            Name: "minecraft:luck"
          }, 
          {
            Base: 6.0f, 
            Current: 6.0f, 
            DefaultMax: 6.0f, 
            DefaultMin: 0.0f, 
            Max: 6.0f, 
            Min: 0.0f, 
            Name: "minecraft:health"
          }, 
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 16.0f, 
            DefaultMin: 0.0f, 
            Max: 16.0f, 
            Min: 0.0f, 
            Name: "minecraft:absorption"
          }, 
          {
            Base: 1.0f, 
            Current: 1.0f, 
            DefaultMax: 1.0f, 
            DefaultMin: 0.0f, 
            Max: 1.0f, 
            Min: 0.0f, 
            Name: "minecraft:knockback_resistance"
          }, 
          {
            Base: 0.699999988079071f, 
            Current: 0.699999988079071f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:underwater_movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:lava_movement"
          }, 
          {
            Base: 16.0f, 
            Current: 16.0f, 
            DefaultMax: 2048.0f, 
            DefaultMin: 0.0f, 
            Max: 2048.0f, 
            Min: 0.0f, 
            Name: "minecraft:follow_range"
          }
        ], 
        BodyRot: -90.0f, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        Dead: 0b, 
        DeathTime: 0s, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        HurtTime: 0s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsPregnant: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        LastDimensionId: 0, 
        LeasherID: -1L, 
        LootDropped: 0b, 
        Mainhand: [
          {
            Count: 1b, 
            Damage: 0s, 
            Name: "effect:ice_sword", 
            WasPickedUp: 0b, 
            tag: {
              Damage: 0
            }
          }
        ], 
        MarkVariant: 0, 
        NaturalSpawn: 0b, 
        Offhand: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        OnGround: 1b, 
        OwnerNew: -1L, 
        Persistent: 1b, 
        PortalCooldown: 0, 
        Pos: [-10.5f, 59.0f, 3.5f], 
        Pose: {
          LastSignal: 0, 
          PoseIndex: 0
        }, 
        Rotation: [-90.0f, 0.0f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Surface: 0b, 
        Tags: [], 
        TargetID: -1L, 
        TradeExperience: 0, 
        TradeTier: 0, 
        UniqueID: -9225589751752L, 
        Variant: 0, 
        boundX: -7, 
        boundY: 3, 
        boundZ: 1, 
        canPickupItems: 0b, 
        definitions: ["+minecraft:armor_stand", "+"], 
        hasBoundOrigin: 0b, 
        hasSetCanPickupItems: 1b, 
        identifier: "minecraft:armor_stand", 
        limitedLife: 0
      }, 
      {
        ActiveEffects: [
          {
            Ambient: 0b, 
            Amplifier: 0b, 
            DisplayOnScreenTextureAnimation: 0b, 
            Duration: 17528446, 
            DurationEasy: 19999574, 
            DurationHard: 19999574, 
            DurationNormal: 19999574, 
            Id: 12b, 
            ShowParticles: 0b
          }
        ], 
        Armor: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        AttackTime: 0s, 
        Attributes: [
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 1024.0f, 
            DefaultMin: -1024.0f, 
            Max: 1024.0f, 
            Min: -1024.0f, 
            Name: "minecraft:luck"
          }, 
          {
            Base: 6.0f, 
            Current: 6.0f, 
            DefaultMax: 6.0f, 
            DefaultMin: 0.0f, 
            Max: 6.0f, 
            Min: 0.0f, 
            Name: "minecraft:health"
          }, 
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 16.0f, 
            DefaultMin: 0.0f, 
            Max: 16.0f, 
            Min: 0.0f, 
            Name: "minecraft:absorption"
          }, 
          {
            Base: 1.0f, 
            Current: 1.0f, 
            DefaultMax: 1.0f, 
            DefaultMin: 0.0f, 
            Max: 1.0f, 
            Min: 0.0f, 
            Name: "minecraft:knockback_resistance"
          }, 
          {
            Base: 0.699999988079071f, 
            Current: 0.699999988079071f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:underwater_movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:lava_movement"
          }, 
          {
            Base: 16.0f, 
            Current: 16.0f, 
            DefaultMax: 2048.0f, 
            DefaultMin: 0.0f, 
            Max: 2048.0f, 
            Min: 0.0f, 
            Name: "minecraft:follow_range"
          }
        ], 
        BodyRot: -90.0f, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        Dead: 0b, 
        DeathTime: 0s, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        HurtTime: 0s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsPregnant: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        LastDimensionId: 0, 
        LeasherID: -1L, 
        LootDropped: 0b, 
        Mainhand: [
          {
            Count: 1b, 
            Damage: 0s, 
            Name: "effect:magma_sword", 
            WasPickedUp: 0b, 
            tag: {
              Damage: 0
            }
          }
        ], 
        MarkVariant: 0, 
        NaturalSpawn: 0b, 
        Offhand: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        OnGround: 1b, 
        OwnerNew: -1L, 
        Persistent: 1b, 
        PortalCooldown: 0, 
        Pos: [-10.5f, 59.0f, 4.5f], 
        Pose: {
          LastSignal: 0, 
          PoseIndex: 0
        }, 
        Rotation: [-90.0f, 0.0f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Surface: 0b, 
        Tags: [], 
        TargetID: -1L, 
        TradeExperience: 0, 
        TradeTier: 0, 
        UniqueID: -9225589751751L, 
        Variant: 0, 
        boundX: -7, 
        boundY: 3, 
        boundZ: 1, 
        canPickupItems: 0b, 
        definitions: ["+minecraft:armor_stand", "+"], 
        hasBoundOrigin: 0b, 
        hasSetCanPickupItems: 1b, 
        identifier: "minecraft:armor_stand", 
        limitedLife: 0
      }, 
      {
        Armor: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        AttackTime: 0s, 
        Attributes: [
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 1024.0f, 
            DefaultMin: -1024.0f, 
            Max: 1024.0f, 
            Min: -1024.0f, 
            Name: "minecraft:luck"
          }, 
          {
            Base: 6.0f, 
            Current: 6.0f, 
            DefaultMax: 6.0f, 
            DefaultMin: 0.0f, 
            Max: 6.0f, 
            Min: 0.0f, 
            Name: "minecraft:health"
          }, 
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 16.0f, 
            DefaultMin: 0.0f, 
            Max: 16.0f, 
            Min: 0.0f, 
            Name: "minecraft:absorption"
          }, 
          {
            Base: 1.0f, 
            Current: 1.0f, 
            DefaultMax: 1.0f, 
            DefaultMin: 0.0f, 
            Max: 1.0f, 
            Min: 0.0f, 
            Name: "minecraft:knockback_resistance"
          }, 
          {
            Base: 0.699999988079071f, 
            Current: 0.699999988079071f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:underwater_movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:lava_movement"
          }, 
          {
            Base: 16.0f, 
            Current: 16.0f, 
            DefaultMax: 2048.0f, 
            DefaultMin: 0.0f, 
            Max: 2048.0f, 
            Min: 0.0f, 
            Name: "minecraft:follow_range"
          }
        ], 
        BodyRot: -90.0f, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        Dead: 0b, 
        DeathTime: 0s, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        HurtTime: 0s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsPregnant: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        LastDimensionId: 0, 
        LeasherID: -1L, 
        LootDropped: 0b, 
        Mainhand: [
          {
            Count: 1b, 
            Damage: 0s, 
            Name: "effect:wither_skeleton_sword", 
            WasPickedUp: 0b, 
            tag: {
              Damage: 0
            }
          }
        ], 
        MarkVariant: 0, 
        NaturalSpawn: 0b, 
        Offhand: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        OnGround: 1b, 
        OwnerNew: -1L, 
        Persistent: 1b, 
        PortalCooldown: 0, 
        Pos: [-10.5f, 59.0f, 21.5f], 
        Pose: {
          LastSignal: 0, 
          PoseIndex: 0
        }, 
        Rotation: [-90.0f, 0.0f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Surface: 0b, 
        Tags: [], 
        TargetID: -1L, 
        TradeExperience: 0, 
        TradeTier: 0, 
        UniqueID: -9225589751749L, 
        Variant: 0, 
        boundX: 0, 
        boundY: 0, 
        boundZ: 0, 
        canPickupItems: 0b, 
        definitions: ["+minecraft:armor_stand", "+"], 
        hasBoundOrigin: 0b, 
        hasSetCanPickupItems: 1b, 
        identifier: "minecraft:armor_stand", 
        limitedLife: 0
      }, 
      {
        Armor: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        AttackTime: 0s, 
        Attributes: [
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 1024.0f, 
            DefaultMin: -1024.0f, 
            Max: 1024.0f, 
            Min: -1024.0f, 
            Name: "minecraft:luck"
          }, 
          {
            Base: 6.0f, 
            Current: 6.0f, 
            DefaultMax: 6.0f, 
            DefaultMin: 0.0f, 
            Max: 6.0f, 
            Min: 0.0f, 
            Name: "minecraft:health"
          }, 
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 16.0f, 
            DefaultMin: 0.0f, 
            Max: 16.0f, 
            Min: 0.0f, 
            Name: "minecraft:absorption"
          }, 
          {
            Base: 1.0f, 
            Current: 1.0f, 
            DefaultMax: 1.0f, 
            DefaultMin: 0.0f, 
            Max: 1.0f, 
            Min: 0.0f, 
            Name: "minecraft:knockback_resistance"
          }, 
          {
            Base: 0.699999988079071f, 
            Current: 0.699999988079071f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:underwater_movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:lava_movement"
          }, 
          {
            Base: 16.0f, 
            Current: 16.0f, 
            DefaultMax: 2048.0f, 
            DefaultMin: 0.0f, 
            Max: 2048.0f, 
            Min: 0.0f, 
            Name: "minecraft:follow_range"
          }
        ], 
        BodyRot: -90.0f, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        Dead: 0b, 
        DeathTime: 0s, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        HurtTime: 0s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsPregnant: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        LastDimensionId: 0, 
        LeasherID: -1L, 
        LootDropped: 0b, 
        Mainhand: [
          {
            Count: 1b, 
            Damage: 0s, 
            Name: "effect:glass_sword", 
            WasPickedUp: 0b, 
            tag: {
              Damage: 0
            }
          }
        ], 
        MarkVariant: 0, 
        NaturalSpawn: 0b, 
        Offhand: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        OnGround: 1b, 
        OwnerNew: -1L, 
        Persistent: 1b, 
        PortalCooldown: 0, 
        Pos: [-10.5f, 59.0f, 20.5f], 
        Pose: {
          LastSignal: 0, 
          PoseIndex: 0
        }, 
        Rotation: [-90.0f, 0.0f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Surface: 0b, 
        Tags: [], 
        TargetID: -1L, 
        TradeExperience: 0, 
        TradeTier: 0, 
        UniqueID: -9225589751748L, 
        Variant: 0, 
        boundX: 0, 
        boundY: 0, 
        boundZ: 0, 
        canPickupItems: 0b, 
        definitions: ["+minecraft:armor_stand", "+"], 
        hasBoundOrigin: 0b, 
        hasSetCanPickupItems: 1b, 
        identifier: "minecraft:armor_stand", 
        limitedLife: 0
      }, 
      {
        Armor: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        AttackTime: 0s, 
        Attributes: [
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 1024.0f, 
            DefaultMin: -1024.0f, 
            Max: 1024.0f, 
            Min: -1024.0f, 
            Name: "minecraft:luck"
          }, 
          {
            Base: 6.0f, 
            Current: 6.0f, 
            DefaultMax: 6.0f, 
            DefaultMin: 0.0f, 
            Max: 6.0f, 
            Min: 0.0f, 
            Name: "minecraft:health"
          }, 
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 16.0f, 
            DefaultMin: 0.0f, 
            Max: 16.0f, 
            Min: 0.0f, 
            Name: "minecraft:absorption"
          }, 
          {
            Base: 1.0f, 
            Current: 1.0f, 
            DefaultMax: 1.0f, 
            DefaultMin: 0.0f, 
            Max: 1.0f, 
            Min: 0.0f, 
            Name: "minecraft:knockback_resistance"
          }, 
          {
            Base: 0.699999988079071f, 
            Current: 0.699999988079071f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:underwater_movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:lava_movement"
          }, 
          {
            Base: 16.0f, 
            Current: 16.0f, 
            DefaultMax: 2048.0f, 
            DefaultMin: 0.0f, 
            Max: 2048.0f, 
            Min: 0.0f, 
            Name: "minecraft:follow_range"
          }
        ], 
        BodyRot: -90.0f, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        Dead: 0b, 
        DeathTime: 0s, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        HurtTime: 0s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsPregnant: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        LastDimensionId: 0, 
        LeasherID: -1L, 
        LootDropped: 0b, 
        Mainhand: [
          {
            Count: 1b, 
            Damage: 0s, 
            Name: "effect:silver_sword", 
            WasPickedUp: 0b, 
            tag: {
              Damage: 0
            }
          }
        ], 
        MarkVariant: 0, 
        NaturalSpawn: 0b, 
        Offhand: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        OnGround: 1b, 
        OwnerNew: -1L, 
        Persistent: 1b, 
        PortalCooldown: 0, 
        Pos: [-10.5f, 59.0f, 19.5f], 
        Pose: {
          LastSignal: 0, 
          PoseIndex: 0
        }, 
        Rotation: [-90.0f, 0.0f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Surface: 0b, 
        Tags: [], 
        TargetID: -1L, 
        TradeExperience: 0, 
        TradeTier: 0, 
        UniqueID: -9225589751747L, 
        Variant: 0, 
        boundX: 0, 
        boundY: 0, 
        boundZ: 0, 
        canPickupItems: 0b, 
        definitions: ["+minecraft:armor_stand", "+"], 
        hasBoundOrigin: 0b, 
        hasSetCanPickupItems: 1b, 
        identifier: "minecraft:armor_stand", 
        limitedLife: 0
      }, 
      {
        Armor: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        AttackTime: 0s, 
        Attributes: [
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 1024.0f, 
            DefaultMin: -1024.0f, 
            Max: 1024.0f, 
            Min: -1024.0f, 
            Name: "minecraft:luck"
          }, 
          {
            Base: 6.0f, 
            Current: 6.0f, 
            DefaultMax: 6.0f, 
            DefaultMin: 0.0f, 
            Max: 6.0f, 
            Min: 0.0f, 
            Name: "minecraft:health"
          }, 
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 16.0f, 
            DefaultMin: 0.0f, 
            Max: 16.0f, 
            Min: 0.0f, 
            Name: "minecraft:absorption"
          }, 
          {
            Base: 1.0f, 
            Current: 1.0f, 
            DefaultMax: 1.0f, 
            DefaultMin: 0.0f, 
            Max: 1.0f, 
            Min: 0.0f, 
            Name: "minecraft:knockback_resistance"
          }, 
          {
            Base: 0.699999988079071f, 
            Current: 0.699999988079071f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:underwater_movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:lava_movement"
          }, 
          {
            Base: 16.0f, 
            Current: 16.0f, 
            DefaultMax: 2048.0f, 
            DefaultMin: 0.0f, 
            Max: 2048.0f, 
            Min: 0.0f, 
            Name: "minecraft:follow_range"
          }
        ], 
        BodyRot: -90.0f, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        Dead: 0b, 
        DeathTime: 0s, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        HurtTime: 0s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsPregnant: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        LastDimensionId: 0, 
        LeasherID: -1L, 
        LootDropped: 0b, 
        Mainhand: [
          {
            Count: 1b, 
            Damage: 0s, 
            Name: "effect:wolf_sword", 
            WasPickedUp: 0b, 
            tag: {
              Damage: 0
            }
          }
        ], 
        MarkVariant: 0, 
        NaturalSpawn: 0b, 
        Offhand: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        OnGround: 1b, 
        OwnerNew: -1L, 
        Persistent: 1b, 
        PortalCooldown: 0, 
        Pos: [-10.5f, 59.0f, 18.5f], 
        Pose: {
          LastSignal: 0, 
          PoseIndex: 0
        }, 
        Rotation: [-90.0f, 0.0f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Surface: 0b, 
        Tags: [], 
        TargetID: -1L, 
        TradeExperience: 0, 
        TradeTier: 0, 
        UniqueID: -9225589751746L, 
        Variant: 0, 
        boundX: 0, 
        boundY: 0, 
        boundZ: 0, 
        canPickupItems: 0b, 
        definitions: ["+minecraft:armor_stand", "+"], 
        hasBoundOrigin: 0b, 
        hasSetCanPickupItems: 1b, 
        identifier: "minecraft:armor_stand", 
        limitedLife: 0
      }, 
      {
        Armor: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        AttackTime: 0s, 
        Attributes: [
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 1024.0f, 
            DefaultMin: -1024.0f, 
            Max: 1024.0f, 
            Min: -1024.0f, 
            Name: "minecraft:luck"
          }, 
          {
            Base: 6.0f, 
            Current: 6.0f, 
            DefaultMax: 6.0f, 
            DefaultMin: 0.0f, 
            Max: 6.0f, 
            Min: 0.0f, 
            Name: "minecraft:health"
          }, 
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 16.0f, 
            DefaultMin: 0.0f, 
            Max: 16.0f, 
            Min: 0.0f, 
            Name: "minecraft:absorption"
          }, 
          {
            Base: 1.0f, 
            Current: 1.0f, 
            DefaultMax: 1.0f, 
            DefaultMin: 0.0f, 
            Max: 1.0f, 
            Min: 0.0f, 
            Name: "minecraft:knockback_resistance"
          }, 
          {
            Base: 0.699999988079071f, 
            Current: 0.699999988079071f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:underwater_movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:lava_movement"
          }, 
          {
            Base: 16.0f, 
            Current: 16.0f, 
            DefaultMax: 2048.0f, 
            DefaultMin: 0.0f, 
            Max: 2048.0f, 
            Min: 0.0f, 
            Name: "minecraft:follow_range"
          }
        ], 
        BodyRot: -90.0f, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        Dead: 0b, 
        DeathTime: 0s, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        HurtTime: 0s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsPregnant: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        LastDimensionId: 0, 
        LeasherID: -1L, 
        LootDropped: 0b, 
        Mainhand: [
          {
            Count: 1b, 
            Damage: 0s, 
            Name: "effect:nether_star_sword", 
            WasPickedUp: 0b, 
            tag: {
              Damage: 0
            }
          }
        ], 
        MarkVariant: 0, 
        NaturalSpawn: 0b, 
        Offhand: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        OnGround: 1b, 
        OwnerNew: -1L, 
        Persistent: 1b, 
        PortalCooldown: 0, 
        Pos: [-10.5f, 59.0f, 17.5f], 
        Pose: {
          LastSignal: 0, 
          PoseIndex: 0
        }, 
        Rotation: [-90.0f, 0.0f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Surface: 0b, 
        Tags: [], 
        TargetID: -1L, 
        TradeExperience: 0, 
        TradeTier: 0, 
        UniqueID: -9225589751745L, 
        Variant: 0, 
        boundX: 0, 
        boundY: 0, 
        boundZ: 0, 
        canPickupItems: 0b, 
        definitions: ["+minecraft:armor_stand", "+"], 
        hasBoundOrigin: 0b, 
        hasSetCanPickupItems: 1b, 
        identifier: "minecraft:armor_stand", 
        limitedLife: 0
      }, 
      {
        Armor: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        AttackTime: 0s, 
        Attributes: [
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 1024.0f, 
            DefaultMin: -1024.0f, 
            Max: 1024.0f, 
            Min: -1024.0f, 
            Name: "minecraft:luck"
          }, 
          {
            Base: 6.0f, 
            Current: 6.0f, 
            DefaultMax: 6.0f, 
            DefaultMin: 0.0f, 
            Max: 6.0f, 
            Min: 0.0f, 
            Name: "minecraft:health"
          }, 
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 16.0f, 
            DefaultMin: 0.0f, 
            Max: 16.0f, 
            Min: 0.0f, 
            Name: "minecraft:absorption"
          }, 
          {
            Base: 1.0f, 
            Current: 1.0f, 
            DefaultMax: 1.0f, 
            DefaultMin: 0.0f, 
            Max: 1.0f, 
            Min: 0.0f, 
            Name: "minecraft:knockback_resistance"
          }, 
          {
            Base: 0.699999988079071f, 
            Current: 0.699999988079071f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:underwater_movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:lava_movement"
          }, 
          {
            Base: 16.0f, 
            Current: 16.0f, 
            DefaultMax: 2048.0f, 
            DefaultMin: 0.0f, 
            Max: 2048.0f, 
            Min: 0.0f, 
            Name: "minecraft:follow_range"
          }
        ], 
        BodyRot: -90.0f, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        Dead: 0b, 
        DeathTime: 0s, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        HurtTime: 0s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsPregnant: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        LastDimensionId: 0, 
        LeasherID: -1L, 
        LootDropped: 0b, 
        Mainhand: [
          {
            Count: 1b, 
            Damage: 0s, 
            Name: "effect:ghost_sword", 
            WasPickedUp: 0b, 
            tag: {
              Damage: 0
            }
          }
        ], 
        MarkVariant: 0, 
        NaturalSpawn: 0b, 
        Offhand: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        OnGround: 1b, 
        OwnerNew: -1L, 
        Persistent: 1b, 
        PortalCooldown: 0, 
        Pos: [-10.5f, 59.0f, 16.5f], 
        Pose: {
          LastSignal: 0, 
          PoseIndex: 0
        }, 
        Rotation: [-90.0f, 0.0f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Surface: 0b, 
        Tags: [], 
        TargetID: -1L, 
        TradeExperience: 0, 
        TradeTier: 0, 
        UniqueID: -9225589751744L, 
        Variant: 0, 
        boundX: 0, 
        boundY: 0, 
        boundZ: 0, 
        canPickupItems: 1b, 
        definitions: ["+minecraft:armor_stand", "+"], 
        hasBoundOrigin: 0b, 
        hasSetCanPickupItems: 1b, 
        identifier: "minecraft:armor_stand", 
        limitedLife: 0
      }, 
      {
        Armor: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        AttackTime: 0s, 
        Attributes: [
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 1024.0f, 
            DefaultMin: -1024.0f, 
            Max: 1024.0f, 
            Min: -1024.0f, 
            Name: "minecraft:luck"
          }, 
          {
            Base: 6.0f, 
            Current: 6.0f, 
            DefaultMax: 6.0f, 
            DefaultMin: 0.0f, 
            Max: 6.0f, 
            Min: 0.0f, 
            Name: "minecraft:health"
          }, 
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 16.0f, 
            DefaultMin: 0.0f, 
            Max: 16.0f, 
            Min: 0.0f, 
            Name: "minecraft:absorption"
          }, 
          {
            Base: 1.0f, 
            Current: 1.0f, 
            DefaultMax: 1.0f, 
            DefaultMin: 0.0f, 
            Max: 1.0f, 
            Min: 0.0f, 
            Name: "minecraft:knockback_resistance"
          }, 
          {
            Base: 0.699999988079071f, 
            Current: 0.699999988079071f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:underwater_movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:lava_movement"
          }, 
          {
            Base: 16.0f, 
            Current: 16.0f, 
            DefaultMax: 2048.0f, 
            DefaultMin: 0.0f, 
            Max: 2048.0f, 
            Min: 0.0f, 
            Name: "minecraft:follow_range"
          }
        ], 
        BodyRot: -90.0f, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        Dead: 0b, 
        DeathTime: 0s, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        HurtTime: 0s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsPregnant: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        LastDimensionId: 0, 
        LeasherID: -1L, 
        LootDropped: 0b, 
        Mainhand: [
          {
            Count: 1b, 
            Damage: 0s, 
            Name: "effect:clock_sword", 
            WasPickedUp: 0b, 
            tag: {
              Damage: 0
            }
          }
        ], 
        MarkVariant: 0, 
        NaturalSpawn: 0b, 
        Offhand: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        OnGround: 1b, 
        OwnerNew: -1L, 
        Persistent: 1b, 
        PortalCooldown: 0, 
        Pos: [-10.5f, 59.0f, 23.5f], 
        Pose: {
          LastSignal: 0, 
          PoseIndex: 0
        }, 
        Rotation: [-90.0f, 0.0f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Surface: 0b, 
        Tags: [], 
        TargetID: -1L, 
        TradeExperience: 0, 
        TradeTier: 0, 
        UniqueID: -9225589751743L, 
        Variant: 0, 
        boundX: 0, 
        boundY: 0, 
        boundZ: 0, 
        canPickupItems: 1b, 
        definitions: ["+minecraft:armor_stand", "+"], 
        hasBoundOrigin: 0b, 
        hasSetCanPickupItems: 1b, 
        identifier: "minecraft:armor_stand", 
        limitedLife: 0
      }, 
      {
        Armor: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }, 
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        AttackTime: 0s, 
        Attributes: [
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 1024.0f, 
            DefaultMin: -1024.0f, 
            Max: 1024.0f, 
            Min: -1024.0f, 
            Name: "minecraft:luck"
          }, 
          {
            Base: 6.0f, 
            Current: 6.0f, 
            DefaultMax: 6.0f, 
            DefaultMin: 0.0f, 
            Max: 6.0f, 
            Min: 0.0f, 
            Name: "minecraft:health"
          }, 
          {
            Base: 0.0f, 
            Current: 0.0f, 
            DefaultMax: 16.0f, 
            DefaultMin: 0.0f, 
            Max: 16.0f, 
            Min: 0.0f, 
            Name: "minecraft:absorption"
          }, 
          {
            Base: 1.0f, 
            Current: 1.0f, 
            DefaultMax: 1.0f, 
            DefaultMin: 0.0f, 
            Max: 1.0f, 
            Min: 0.0f, 
            Name: "minecraft:knockback_resistance"
          }, 
          {
            Base: 0.699999988079071f, 
            Current: 0.699999988079071f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:underwater_movement"
          }, 
          {
            Base: 0.019999999552965164f, 
            Current: 0.019999999552965164f, 
            DefaultMax: 3.4028234663852886e+38f, 
            DefaultMin: 0.0f, 
            Max: 3.4028234663852886e+38f, 
            Min: 0.0f, 
            Name: "minecraft:lava_movement"
          }, 
          {
            Base: 16.0f, 
            Current: 16.0f, 
            DefaultMax: 2048.0f, 
            DefaultMin: 0.0f, 
            Max: 2048.0f, 
            Min: 0.0f, 
            Name: "minecraft:follow_range"
          }
        ], 
        BodyRot: -90.0f, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        Dead: 0b, 
        DeathTime: 0s, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        HurtTime: 0s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsPregnant: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        LastDimensionId: 0, 
        LeasherID: -1L, 
        LootDropped: 0b, 
        Mainhand: [
          {
            Count: 1b, 
            Damage: 0s, 
            Name: "effect:bedrock_sword", 
            WasPickedUp: 0b
          }
        ], 
        MarkVariant: 0, 
        NaturalSpawn: 0b, 
        Offhand: [
          {
            Count: 0b, 
            Damage: 0s, 
            Name: "", 
            WasPickedUp: 0b
          }
        ], 
        OnGround: 1b, 
        OwnerNew: -1L, 
        Persistent: 1b, 
        PortalCooldown: 0, 
        Pos: [-10.5f, 59.0f, 22.5f], 
        Pose: {
          LastSignal: 0, 
          PoseIndex: 0
        }, 
        Rotation: [-90.0f, 0.0f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Surface: 0b, 
        Tags: [], 
        TargetID: -1L, 
        TradeExperience: 0, 
        TradeTier: 0, 
        UniqueID: -9225589751742L, 
        Variant: 0, 
        boundX: 0, 
        boundY: 0, 
        boundZ: 0, 
        canPickupItems: 1b, 
        definitions: ["+minecraft:armor_stand", "+"], 
        hasBoundOrigin: 0b, 
        hasSetCanPickupItems: 1b, 
        identifier: "minecraft:armor_stand", 
        limitedLife: 0
      }
    ], 
    palette: {
      default: {
        block_palette: [
          {
            name: "minecraft:air", 
            states: {}, 
            version: 17879555
          }, 
          {
            name: "minecraft:concrete", 
            states: {
              color: "lime"
            }, 
            version: 17879555
          }, 
          {
            name: "minecraft:lectern", 
            states: {
              direction: 3, 
              powered_bit: 0b
            }, 
            version: 17879555
          }
        ], 
        block_position_data: {
          108: {
            block_entity_data: {
              book: {
                Count: 1b, 
                Damage: 0s, 
                Name: "minecraft:writable_book", 
                WasPickedUp: 0b, 
                tag: {
                  pages: [
                    {
                      photoname: "", 
                      text: "Matando endermans de ojos rojos en el overworld"
                    }, 
                    {
                      photoname: "", 
                      text: ""
                    }
                  ]
                }
              }, 
              hasBook: 1b, 
              id: "Lectern", 
              isMovable: 1b, 
              page: 0, 
              totalPages: 2, 
              x: -11, 
              y: 62, 
              z: -12
            }
          }, 
          109: {
            block_entity_data: {
              book: {
                Count: 1b, 
                Damage: 0s, 
                Name: "minecraft:writable_book", 
                WasPickedUp: 0b, 
                tag: {
                  pages: [
                    {
                      photoname: "", 
                      text: "Matando centellas"
                    }, 
                    {
                      photoname: "", 
                      text: ""
                    }
                  ]
                }
              }, 
              hasBook: 1b, 
              id: "Lectern", 
              isMovable: 1b, 
              page: 0, 
              totalPages: 2, 
              x: -11, 
              y: 62, 
              z: -11
            }
          }, 
          110: {
            block_entity_data: {
              book: {
                Count: 1b, 
                Damage: 0s, 
                Name: "minecraft:writable_book", 
                WasPickedUp: 0b, 
                tag: {
                  pages: [
                    {
                      photoname: "", 
                      text: "Se craftea"
                    }, 
                    {
                      photoname: "", 
                      text: ""
                    }
                  ]
                }
              }, 
              hasBook: 1b, 
              id: "Lectern", 
              isMovable: 1b, 
              page: 0, 
              totalPages: 2, 
              x: -11, 
              y: 62, 
              z: -10
            }
          }, 
          111: {
            block_entity_data: {
              book: {
                Count: 1b, 
                Damage: 0s, 
                Name: "minecraft:writable_book", 
                WasPickedUp: 0b, 
                tag: {
                  pages: [
                    {
                      photoname: "", 
                      text: "Matando al wither con la nether star sword"
                    }, 
                    {
                      photoname: "", 
                      text: ""
                    }
                  ]
                }
              }, 
              hasBook: 1b, 
              id: "Lectern", 
              isMovable: 1b, 
              page: 0, 
              totalPages: 2, 
              x: -11, 
              y: 62, 
              z: -9
            }
          }, 
          112: {
            block_entity_data: {
              book: {
                Count: 1b, 
                Damage: 0s, 
                Name: "minecraft:writable_book", 
                WasPickedUp: 0b, 
                tag: {
                  pages: [
                    {
                      photoname: "", 
                      text: "-Se consigue en templo del desierto

"
                    }, 
                    {
                      photoname: "", 
                      text: ""
                    }
                  ]
                }
              }, 
              hasBook: 1b, 
              id: "Lectern", 
              isMovable: 1b, 
              page: 0, 
              totalPages: 2, 
              x: -11, 
              y: 62, 
              z: -8
            }
          }, 
          113: {
            block_entity_data: {
              book: {
                Count: 1b, 
                Damage: 0s, 
                Name: "minecraft:writable_book", 
                WasPickedUp: 0b, 
                tag: {
                  pages: [
                    {
                      photoname: "", 
                      text: "En la fuente de los deseos del desierto"
                    }, 
                    {
                      photoname: "", 
                      text: ""
                    }
                  ]
                }
              }, 
              hasBook: 1b, 
              id: "Lectern", 
              isMovable: 1b, 
              page: 0, 
              totalPages: 2, 
              x: -11, 
              y: 62, 
              z: -7
            }
          }, 
          114: {
            block_entity_data: {
              book: {
                Count: 1b, 
                Damage: 0s, 
                Name: "minecraft:writable_book", 
                WasPickedUp: 0b, 
                tag: {
                  pages: [
                    {
                      photoname: "", 
                      text: "Matando al elder guardian"
                    }, 
                    {
                      photoname: "", 
                      text: ""
                    }
                  ]
                }
              }, 
              hasBook: 1b, 
              id: "Lectern", 
              isMovable: 1b, 
              page: 0, 
              totalPages: 2, 
              x: -11, 
              y: 62, 
              z: -6
            }
          }, 
          115: {
            block_entity_data: {
              book: {
                Count: 1b, 
                Damage: 0s, 
                Name: "minecraft:writable_book", 
                WasPickedUp: 0b, 
                tag: {
                  pages: [
                    {
                      photoname: "", 
                      text: "En las mineshaft"
                    }, 
                    {
                      photoname: "", 
                      text: ""
                    }
                  ]
                }
              }, 
              hasBook: 1b, 
              id: "Lectern", 
              isMovable: 1b, 
              page: 0, 
              totalPages: 2, 
              x: -11, 
              y: 62, 
              z: -5
            }
          }, 
          116: {
            block_entity_data: {
              book: {
                Count: 1b, 
                Damage: 0s, 
                Name: "minecraft:writable_book", 
                WasPickedUp: 0b, 
                tag: {
                  pages: [
                    {
                      photoname: "", 
                      text: "Matando shulkers"
                    }, 
                    {
                      photoname: "", 
                      text: ""
                    }
                  ]
                }
              }, 
              hasBook: 1b, 
              id: "Lectern", 
              isMovable: 1b, 
              page: 0, 
              totalPages: 2, 
              x: -11, 
              y: 62, 
              z: -4
            }
          }, 
          117: {
            block_entity_data: {
              book: {
                Count: 1b, 
                Damage: 0s, 
                Name: "minecraft:writable_book", 
                WasPickedUp: 0b, 
                tag: {
                  pages: [
                    {
                      photoname: "", 
                      text: "Matando al rey slime en el pantano de noche"
                    }, 
                    {
                      photoname: "", 
                      text: ""
                    }
                  ]
                }
              }, 
              hasBook: 1b, 
              id: "Lectern", 
              isMovable: 1b, 
              page: 0, 
              totalPages: 2, 
              x: -11, 
              y: 62, 
              z: -3
            }
          }, 
          118: {
            block_entity_data: {
              book: {
                Count: 1b, 
                Damage: 0s, 
                Name: "minecraft:writable_book", 
                WasPickedUp: 0b, 
                tag: {
                  pages: [
                    {
                      photoname: "", 
                      text: "-Matando ghast con su propio proyectil

-Explotando ender crystal en el nether"
                    }, 
                    {
                      photoname: "", 
                      text: ""
                    }
                  ]
                }
              }, 
              hasBook: 1b, 
              id: "Lectern", 
              isMovable: 1b, 
              page: 0, 
              totalPages: 2, 
              x: -11, 
              y: 62, 
              z: -2
            }
          }, 
          119: {
            block_entity_data: {
              book: {
                Count: 1b, 
                Damage: 0s, 
                Name: "minecraft:writable_book", 
                WasPickedUp: 0b, 
                tag: {
                  pages: [
                    {
                      photoname: "", 
                      text: "En cofres del tesoro"
                    }, 
                    {
                      photoname: "", 
                      text: ""
                    }
                  ]
                }
              }, 
              hasBook: 1b, 
              id: "Lectern", 
              isMovable: 1b, 
              page: 0, 
              totalPages: 2, 
              x: -11, 
              y: 62, 
              z: -1
            }
          }, 
          120: {
            block_entity_data: {
              book: {
                Count: 1b, 
                Damage: 0s, 
                Name: "minecraft:writable_book", 
                WasPickedUp: 0b, 
                tag: {
                  pages: [
                    {
                      photoname: "", 
                      text: "Se craftea (quarzo de diamante y palos del mismo material)"
                    }, 
                    {
                      photoname: "", 
                      text: ""
                    }
                  ]
                }
              }, 
              hasBook: 1b, 
              id: "Lectern", 
              isMovable: 1b, 
              page: 0, 
              totalPages: 2, 
              x: -11, 
              y: 62, 
              z: 0
            }
          }, 
          121: {
            block_entity_data: {
              book: {
                Count: 1b, 
                Damage: 0s, 
                Name: "minecraft:writable_book", 
                WasPickedUp: 0b, 
                tag: {
                  pages: [
                    {
                      photoname: "", 
                      text: "-Tirando la espada de fuego a la lluvia

-"
                    }, 
                    {
                      photoname: "", 
                      text: ""
                    }
                  ]
                }
              }, 
              hasBook: 1b, 
              id: "Lectern", 
              isMovable: 1b, 
              page: 0, 
              totalPages: 2, 
              x: -11, 
              y: 62, 
              z: 1
            }
          }, 
          122: {
            block_entity_data: {
              book: {
                Count: 1b, 
                Damage: 0s, 
                Name: "minecraft:writable_book", 
                WasPickedUp: 0b, 
                tag: {
                  pages: [
                    {
                      photoname: "", 
                      text: "-En stronghold library

-En los pillager outpost

-En los corredores del stronghold"
                    }, 
                    {
                      photoname: "", 
                      text: ""
                    }
                  ]
                }
              }, 
              hasBook: 1b, 
              id: "Lectern", 
              isMovable: 1b, 
              page: 0, 
              totalPages: 2, 
              x: -11, 
              y: 62, 
              z: 2
            }
          }, 
          123: {
            block_entity_data: {
              book: {
                Count: 1b, 
                Damage: 0s, 
                Name: "minecraft:writable_book", 
                WasPickedUp: 0b, 
                tag: {
                  pages: [
                    {
                      photoname: "", 
                      text: "-Se consigue en iglú

-En las aldeas en la nieve"
                    }, 
                    {
                      photoname: "", 
                      text: ""
                    }
                  ]
                }
              }, 
              hasBook: 1b, 
              id: "Lectern", 
              isMovable: 1b, 
              page: 0, 
              totalPages: 2, 
              x: -11, 
              y: 62, 
              z: 3
            }
          }, 
          124: {
            block_entity_data: {
              book: {
                Count: 1b, 
                Damage: 0s, 
                Name: "minecraft:writable_book", 
                WasPickedUp: 0b, 
                tag: {
                  pages: [
                    {
                      photoname: "", 
                      text: "En ruinas submarinas grandes"
                    }, 
                    {
                      photoname: "", 
                      text: ""
                    }
                  ]
                }
              }, 
              hasBook: 1b, 
              id: "Lectern", 
              isMovable: 1b, 
              page: 0, 
              totalPages: 2, 
              x: -11, 
              y: 62, 
              z: 4
            }
          }, 
          125: {
            block_entity_data: {
              book: {
                Count: 1b, 
                Damage: 0s, 
                Name: "minecraft:writable_book", 
                WasPickedUp: 0b, 
                tag: {
                  pages: [
                    {
                      photoname: "", 
                      text: "-Pescando en la jungla

-En el cofre del templo de la jungla"
                    }, 
                    {
                      photoname: "", 
                      text: ""
                    }
                  ]
                }
              }, 
              hasBook: 1b, 
              id: "Lectern", 
              isMovable: 1b, 
              page: 0, 
              totalPages: 2, 
              x: -11, 
              y: 62, 
              z: 5
            }
          }, 
          126: {
            block_entity_data: {
              book: {
                Count: 1b, 
                Damage: 0s, 
                Name: "minecraft:writable_book", 
                WasPickedUp: 0b, 
                tag: {
                  pages: [
                    {
                      photoname: "", 
                      text: "Matando una bruja de pasto con baja probabilidad"
                    }, 
                    {
                      photoname: "", 
                      text: ""
                    }
                  ]
                }
              }, 
              hasBook: 1b, 
              id: "Lectern", 
              isMovable: 1b, 
              page: 0, 
              totalPages: 2, 
              x: -11, 
              y: 62, 
              z: 6
            }
          }, 
          127: {
            block_entity_data: {
              book: {
                Count: 1b, 
                Damage: 0s, 
                Name: "minecraft:writable_book", 
                WasPickedUp: 0b, 
                tag: {
                  pages: [
                    {
                      photoname: "", 
                      text: "-Se consigue matando llamas vivientes.

-Crafteandola con bloques de fuego(raro)"
                    }, 
                    {
                      photoname: "", 
                      text: ""
                    }
                  ]
                }
              }, 
              hasBook: 1b, 
              id: "Lectern", 
              isMovable: 1b, 
              page: 0, 
              totalPages: 2, 
              x: -11, 
              y: 62, 
              z: 7
            }
          }, 
          128: {
            block_entity_data: {
              book: {
                Count: 1b, 
                Damage: 0s, 
                Name: "minecraft:writable_book", 
                WasPickedUp: 0b, 
                tag: {
                  pages: [
                    {
                      photoname: "", 
                      text: "-Se encuentra en Woodland mansión

-En la biblioteca del stronghold

-En los corredores del stronghold

-En los pillager outpost"
                    }, 
                    {
                      photoname: "", 
                      text: ""
                    }
                  ]
                }
              }, 
              hasBook: 1b, 
              id: "Lectern", 
              isMovable: 1b, 
              page: 0, 
              totalPages: 2, 
              x: -11, 
              y: 62, 
              z: 8
            }
          }, 
          129: {
            block_entity_data: {
              book: {
                Count: 1b, 
                Damage: 0s, 
                Name: "minecraft:writable_book", 
                WasPickedUp: 0b, 
                tag: {
                  pages: [
                    {
                      photoname: "", 
                      text: "Haciendo explotar creepers cargados"
                    }
                  ]
                }
              }, 
              hasBook: 1b, 
              id: "Lectern", 
              isMovable: 1b, 
              page: 0, 
              totalPages: 1, 
              x: -11, 
              y: 62, 
              z: 9
            }
          }, 
          130: {
            block_entity_data: {
              book: {
                Count: 1b, 
                Damage: 0s, 
                Name: "minecraft:writable_book", 
                WasPickedUp: 0b, 
                tag: {
                  pages: [
                    {
                      photoname: "", 
                      text: "Se craftea (bloques de carbón y palo)"
                    }, 
                    {
                      photoname: "", 
                      text: ""
                    }
                  ]
                }
              }, 
              hasBook: 1b, 
              id: "Lectern", 
              isMovable: 1b, 
              page: 0, 
              totalPages: 2, 
              x: -11, 
              y: 62, 
              z: 10
            }
          }, 
          131: {
            block_entity_data: {
              book: {
                Count: 1b, 
                Damage: 0s, 
                Name: "minecraft:writable_book", 
                WasPickedUp: 0b, 
                tag: {
                  pages: [
                    {
                      photoname: "", 
                      text: "Se craftea (cactus y palo)"
                    }, 
                    {
                      photoname: "", 
                      text: ""
                    }
                  ]
                }
              }, 
              hasBook: 1b, 
              id: "Lectern", 
              isMovable: 1b, 
              page: 0, 
              totalPages: 2, 
              x: -11, 
              y: 62, 
              z: 11
            }
          }, 
          132: {
            block_entity_data: {
              book: {
                Count: 1b, 
                Damage: 0s, 
                Name: "minecraft:writable_book", 
                WasPickedUp: 0b, 
                tag: {
                  pages: [
                    {
                      photoname: "", 
                      text: "Se consigue matando skeletons en el desierto durante la noche con baja probabilidad"
                    }, 
                    {
                      photoname: "", 
                      text: ""
                    }
                  ]
                }
              }, 
              hasBook: 1b, 
              id: "Lectern", 
              isMovable: 1b, 
              page: 0, 
              totalPages: 2, 
              x: -11, 
              y: 62, 
              z: 12
            }
          }, 
          133: {
            block_entity_data: {
              book: {
                Count: 1b, 
                Damage: 0s, 
                Name: "minecraft:writable_book", 
                WasPickedUp: 0b, 
                tag: {
                  pages: [
                    {
                      photoname: "", 
                      text: "Se consigue matando blaze con bolas de nieve con baja probabilidad"
                    }, 
                    {
                      photoname: "", 
                      text: ""
                    }
                  ]
                }
              }, 
              hasBook: 1b, 
              id: "Lectern", 
              isMovable: 1b, 
              page: 0, 
              totalPages: 2, 
              x: -11, 
              y: 62, 
              z: 13
            }
          }, 
          134: {
            block_entity_data: {
              book: {
                Count: 1b, 
                Damage: 0s, 
                Name: "minecraft:writable_book", 
                WasPickedUp: 0b, 
                tag: {
                  pages: [
                    {
                      photoname: "", 
                      text: "Se consigue mojando una espada de sponja"
                    }, 
                    {
                      photoname: "", 
                      text: ""
                    }
                  ]
                }
              }, 
              hasBook: 1b, 
              id: "Lectern", 
              isMovable: 1b, 
              page: 0, 
              totalPages: 2, 
              x: -11, 
              y: 62, 
              z: 14
            }
          }, 
          135: {
            block_entity_data: {
              book: {
                Count: 1b, 
                Damage: 0s, 
                Name: "minecraft:writable_book", 
                WasPickedUp: 0b, 
                tag: {
                  pages: [
                    {
                      photoname: "", 
                      text: "Usando diamantes o bloques de diamante,  como monedas de la suerte en la fuente del desierto (muy baja probabilidad)"
                    }, 
                    {
                      photoname: "", 
                      text: ""
                    }
                  ]
                }
              }, 
              hasBook: 1b, 
              id: "Lectern", 
              isMovable: 1b, 
              page: 0, 
              totalPages: 2, 
              x: -11, 
              y: 62, 
              z: 15
            }
          }, 
          136: {
            block_entity_data: {
              book: {
                Count: 1b, 
                Damage: 0s, 
                Name: "minecraft:writable_book", 
                WasPickedUp: 0b, 
                tag: {
                  pages: [
                    {
                      photoname: "", 
                      text: "Haciendo desaparecer fantasmas"
                    }, 
                    {
                      photoname: "", 
                      text: ""
                    }
                  ]
                }
              }, 
              hasBook: 1b, 
              id: "Lectern", 
              isMovable: 1b, 
              page: 0, 
              totalPages: 2, 
              x: -11, 
              y: 62, 
              z: 16
            }
          }, 
          137: {
            block_entity_data: {
              book: {
                Count: 1b, 
                Damage: 0s, 
                Name: "minecraft:writable_book", 
                WasPickedUp: 0b, 
                tag: {
                  pages: [
                    {
                      photoname: "", 
                      text: "Se craftea (espada de diamond y netherStar)"
                    }, 
                    {
                      photoname: "", 
                      text: ""
                    }
                  ]
                }
              }, 
              hasBook: 1b, 
              id: "Lectern", 
              isMovable: 1b, 
              page: 0, 
              totalPages: 2, 
              x: -11, 
              y: 62, 
              z: 17
            }
          }, 
          138: {
            block_entity_data: {
              book: {
                Count: 1b, 
                Damage: 0s, 
                Name: "minecraft:writable_book", 
                WasPickedUp: 0b, 
                tag: {
                  pages: [
                    {
                      photoname: "", 
                      text: "Se consigue matando a un lobo alfa con una espada de plata durante la luna llena"
                    }, 
                    {
                      photoname: "", 
                      text: ""
                    }
                  ]
                }
              }, 
              hasBook: 1b, 
              id: "Lectern", 
              isMovable: 1b, 
              page: 0, 
              totalPages: 2, 
              x: -11, 
              y: 62, 
              z: 18
            }
          }, 
          139: {
            block_entity_data: {
              book: {
                Count: 1b, 
                Damage: 0s, 
                Name: "minecraft:writable_book", 
                WasPickedUp: 0b, 
                tag: {
                  pages: [
                    {
                      photoname: "", 
                      text: "Se consigue picando el mineral de plata (silver)"
                    }, 
                    {
                      photoname: "", 
                      text: ""
                    }
                  ]
                }
              }, 
              hasBook: 1b, 
              id: "Lectern", 
              isMovable: 1b, 
              page: 0, 
              totalPages: 2, 
              x: -11, 
              y: 62, 
              z: 19
            }
          }, 
          140: {
            block_entity_data: {
              book: {
                Count: 1b, 
                Damage: 0s, 
                Name: "minecraft:writable_book", 
                WasPickedUp: 0b, 
                tag: {
                  pages: [
                    {
                      photoname: "", 
                      text: "Se consigue arrojando la espada de fuego al agua"
                    }, 
                    {
                      photoname: "", 
                      text: ""
                    }
                  ]
                }
              }, 
              hasBook: 1b, 
              id: "Lectern", 
              isMovable: 1b, 
              page: 0, 
              totalPages: 2, 
              x: -11, 
              y: 62, 
              z: 20
            }
          }, 
          141: {
            block_entity_data: {
              book: {
                Count: 1b, 
                Damage: 0s, 
                Name: "minecraft:writable_book", 
                WasPickedUp: 0b, 
                tag: {
                  pages: [
                    {
                      photoname: "", 
                      text: "Se consigue matando wither skeletons con baja probabilidad"
                    }, 
                    {
                      photoname: "", 
                      text: ""
                    }
                  ]
                }
              }, 
              hasBook: 1b, 
              id: "Lectern", 
              isMovable: 1b, 
              page: 0, 
              totalPages: 2, 
              x: -11, 
              y: 62, 
              z: 21
            }
          }, 
          142: {
            block_entity_data: {
              book: {
                Count: 1b, 
                Damage: 0s, 
                Name: "minecraft:writable_book", 
                WasPickedUp: 0b, 
                tag: {
                  pages: [
                    {
                      photoname: "", 
                      text: "Se craftea (bedrock y palos del mismo material)"
                    }, 
                    {
                      photoname: "", 
                      text: ""
                    }
                  ]
                }
              }, 
              hasBook: 1b, 
              id: "Lectern", 
              isMovable: 1b, 
              page: 0, 
              totalPages: 2, 
              x: -11, 
              y: 62, 
              z: 22
            }
          }, 
          143: {
            block_entity_data: {
              book: {
                Count: 1b, 
                Damage: 0s, 
                Name: "minecraft:writable_book", 
                WasPickedUp: 0b, 
                tag: {
                  pages: [
                    {
                      photoname: "", 
                      text: "Se craftea"
                    }, 
                    {
                      photoname: "", 
                      text: ""
                    }
                  ]
                }
              }, 
              hasBook: 1b, 
              id: "Lectern", 
              isMovable: 1b, 
              page: 0, 
              totalPages: 2, 
              x: -11, 
              y: 62, 
              z: 23
            }
          }
        }
      }
    }
  }, 
  structure_world_origin: [-11, 59, -12]
}
```

## `bedrock_sword`

- Путь `Swords_B/structures/bedrock_sword.mcstructure`; MD5 `499a7f62e375426c70b42bf678a64e35`; NBT round-trip: побайтово совпал.
- Размер `[1, 1, 1]`; structure_world_origin `[-6, 56, 0]`; сущностей 1.
- Сущности: `minecraft:item`.
- Предметы с `Name` в пространствах `effect:` / `effect99:`:
  - `$.entities[0].Item.Name`: `effect:bedrock_sword`
- Буквальные вызовы:
  - `Swords_B/entities/item.json:181` — `"run_command": { "command": [ "structure load bedrock_sword ~ ~1 ~", "kill @s" ] }`

### Полный типизированный SNBT

```snbt
{
  format_version: 1, 
  size: [1, 1, 1], 
  structure: {
    block_indices: [
      [], 
      []
    ], 
    entities: [
      {
        Age: 279s, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        Health: 5s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        Item: {
          Count: 1b, 
          Damage: 0s, 
          Name: "effect:bedrock_sword", 
          WasPickedUp: 0b
        }, 
        LastDimensionId: 0, 
        LootDropped: 0b, 
        MarkVariant: 0, 
        Motion: [-3.072577377976824e-19f, 0.0f, 6.046041974957544e-19f], 
        OnGround: 1b, 
        OwnerID: -8589934591L, 
        OwnerNew: -8589934591L, 
        PortalCooldown: 0, 
        Pos: [-5.4790873527526855f, 56.125f, 0.5096691250801086f], 
        Rotation: [45.390838623046875f, 89.89163208007812f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Tags: [], 
        UniqueID: -6824703033343L, 
        Variant: 0, 
        definitions: ["+minecraft:item"], 
        identifier: "minecraft:item"
      }
    ], 
    palette: {}
  }, 
  structure_world_origin: [-6, 56, 0]
}
```

## `bone_sword`

- Путь `Swords_B/structures/bone_sword.mcstructure`; MD5 `2e43a7578a4bd492b63e3cee00651af1`; NBT round-trip: побайтово совпал.
- Размер `[1, 1, 1]`; structure_world_origin `[-6, 56, 0]`; сущностей 1.
- Сущности: `minecraft:item`.
- Предметы с `Name` в пространствах `effect:` / `effect99:`:
  - `$.entities[0].Item.Name`: `effect:bone_sword`
- Буквальные вызовы:
  - `Swords_B/entities/skeleton.json:275` — `"run_command": { "command": [ "structure load bone_sword ~ ~ ~" ] }`

### Полный типизированный SNBT

```snbt
{
  format_version: 1, 
  size: [1, 1, 1], 
  structure: {
    block_indices: [
      [], 
      []
    ], 
    entities: [
      {
        Age: 321s, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        Health: 5s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        Item: {
          Count: 1b, 
          Damage: 0s, 
          Name: "effect:bone_sword", 
          WasPickedUp: 0b, 
          tag: {
            Damage: 0
          }
        }, 
        LastDimensionId: 0, 
        LootDropped: 0b, 
        MarkVariant: 0, 
        Motion: [-6.615646297560317e-23f, 0.0f, 5.973677452317406e-21f], 
        OnGround: 1b, 
        OwnerID: -8589934591L, 
        OwnerNew: -8589934591L, 
        PortalCooldown: 0, 
        Pos: [-5.496306419372559f, 56.125f, 0.6903467774391174f], 
        Rotation: [89.11557006835938f, 89.89532470703125f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Tags: [], 
        UniqueID: -8448200670638L, 
        Variant: 0, 
        definitions: ["+minecraft:item"], 
        identifier: "minecraft:item"
      }
    ], 
    palette: {}
  }, 
  structure_world_origin: [-6, 56, 0]
}
```

## `creeper_sword`

- Путь `Swords_B/structures/creeper_sword.mcstructure`; MD5 `aac6103d455ee6ab8738c67fbb39125d`; NBT round-trip: побайтово совпал.
- Размер `[1, 1, 1]`; structure_world_origin `[-6, 56, 0]`; сущностей 1.
- Сущности: `minecraft:item`.
- Предметы с `Name` в пространствах `effect:` / `effect99:`:
  - `$.entities[0].Item.Name`: `effect:creeper_sword`
- Буквальные вызовы:
  - `Swords_B/entities/creeper.json:339` — `"run_command": { "command": [ "structure load creeper_sword ~ ~ ~" ] }`

### Полный типизированный SNBT

```snbt
{
  format_version: 1, 
  size: [1, 1, 1], 
  structure: {
    block_indices: [
      [], 
      []
    ], 
    entities: [
      {
        Age: 159s, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        Health: 5s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        Item: {
          Count: 1b, 
          Damage: 0s, 
          Name: "effect:creeper_sword", 
          WasPickedUp: 0b
        }, 
        LastDimensionId: 0, 
        LootDropped: 0b, 
        MarkVariant: 0, 
        Motion: [-8.171767949816111e-12f, 0.0f, -3.724649495079335e-12f], 
        OnGround: 1b, 
        OwnerID: -8589934591L, 
        OwnerNew: -8589934591L, 
        PortalCooldown: 0, 
        Pos: [-5.393953323364258f, 56.125f, 0.5855494737625122f], 
        Rotation: [125.4683837890625f, 85.29449462890625f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Tags: [], 
        UniqueID: -8478265442264L, 
        Variant: 0, 
        definitions: ["+minecraft:item"], 
        identifier: "minecraft:item"
      }
    ], 
    palette: {}
  }, 
  structure_world_origin: [-6, 56, 0]
}
```

## `fire_sword`

- Путь `Swords_B/structures/fire_sword.mcstructure`; MD5 `373fac643e0540117dfa6d3ea42d4d9a`; NBT round-trip: побайтово совпал.
- Размер `[1, 1, 1]`; structure_world_origin `[-343, 32, -11]`; сущностей 1.
- Сущности: `minecraft:item`.
- Предметы с `Name` в пространствах `effect:` / `effect99:`:
  - `$.entities[0].Item.Name`: `effect:fire_sword`
- Буквальные вызовы:
  - `Swords_B/entities/item.json:184` — `"run_command": { "command": [ "structure load fire_sword ~ ~1 ~", "kill @s" ] }`

### Полный типизированный SNBT

```snbt
{
  format_version: 1, 
  size: [1, 1, 1], 
  structure: {
    block_indices: [
      [], 
      []
    ], 
    entities: [
      {
        Age: 1612s, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        Health: 5s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        Item: {
          Count: 1b, 
          Damage: 0s, 
          Name: "effect:fire_sword", 
          WasPickedUp: 0b, 
          tag: {
            Damage: 0
          }
        }, 
        LastDimensionId: 1, 
        LootDropped: 0b, 
        MarkVariant: 0, 
        Motion: [-1.401298464324817e-45f, 0.0f, -1.401298464324817e-45f], 
        OnGround: 1b, 
        OwnerID: -8589934591L, 
        OwnerNew: -8589934591L, 
        PortalCooldown: 0, 
        Pos: [-342.4423828125f, 32.125f, -10.583288192749023f], 
        Rotation: [85.60189819335938f, 86.8297119140625f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Tags: ["fire_sword", "fire_sword_respawn"], 
        UniqueID: -8516920147952L, 
        Variant: 0, 
        definitions: ["+minecraft:item"], 
        identifier: "minecraft:item"
      }
    ], 
    palette: {}
  }, 
  structure_world_origin: [-343, 32, -11]
}
```

## `ghost_sword`

- Путь `Swords_B/structures/ghost_sword.mcstructure`; MD5 `69dd53e4ff9a4bc549dab162c143c8a6`; NBT round-trip: побайтово совпал.
- Размер `[1, 1, 1]`; structure_world_origin `[-6, 56, 0]`; сущностей 1.
- Сущности: `minecraft:item`.
- Предметы с `Name` в пространствах `effect:` / `effect99:`:
  - `$.entities[0].Item.Name`: `effect:ghost_sword`
- Буквальные вызовы:
  - `Swords_B/entities/ghost.json:122` — `"structure load ghost_sword ~~~",`

### Полный типизированный SNBT

```snbt
{
  format_version: 1, 
  size: [1, 1, 1], 
  structure: {
    block_indices: [
      [], 
      []
    ], 
    entities: [
      {
        Age: 403s, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        Health: 5s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        Item: {
          Count: 1b, 
          Damage: 0s, 
          Name: "effect:ghost_sword", 
          WasPickedUp: 0b
        }, 
        LastDimensionId: 0, 
        LootDropped: 0b, 
        MarkVariant: 0, 
        Motion: [-1.448165581603863e-26f, 0.0f, -3.709671947654262e-27f], 
        OnGround: 1b, 
        OwnerID: -8589934591L, 
        OwnerNew: -8589934591L, 
        PortalCooldown: 0, 
        Pos: [-5.4909749031066895f, 56.125f, 0.523998498916626f], 
        Rotation: [92.73812866210938f, 89.89163208007812f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Tags: [], 
        UniqueID: -8194797600538L, 
        Variant: 0, 
        definitions: ["+minecraft:item"], 
        identifier: "minecraft:item"
      }
    ], 
    palette: {}
  }, 
  structure_world_origin: [-6, 56, 0]
}
```

## `glass_sword`

- Путь `Swords_B/structures/glass_sword.mcstructure`; MD5 `da7e04299501244f9c0762defa81c587`; NBT round-trip: побайтово совпал.
- Размер `[1, 1, 1]`; structure_world_origin `[-6, 56, 0]`; сущностей 1.
- Сущности: `minecraft:item`.
- Предметы с `Name` в пространствах `effect:` / `effect99:`:
  - `$.entities[0].Item.Name`: `effect:glass_sword`
- Буквальные вызовы:
  - `Swords_B/entities/item.json:229` — `"fire_sword_event_2": { "run_command": { "command": [ "playsound random.fizz @a[r=12] ~ ~ ~ 0.6", "particle minecraft:cauldron_explosion_emitter ~ ~ ~", "structure load glass_sword ~ ~ ~", "kill @s" ] } },`

### Полный типизированный SNBT

```snbt
{
  format_version: 1, 
  size: [1, 1, 1], 
  structure: {
    block_indices: [
      [], 
      []
    ], 
    entities: [
      {
        Age: 277s, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        Health: 5s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        Item: {
          Count: 1b, 
          Damage: 0s, 
          Name: "effect:glass_sword", 
          WasPickedUp: 0b
        }, 
        LastDimensionId: 0, 
        LootDropped: 0b, 
        MarkVariant: 0, 
        Motion: [-1.9737061913034571e-19f, 0.0f, 1.3312233773061565e-19f], 
        OnGround: 1b, 
        OwnerID: -8589934591L, 
        OwnerNew: -8589934591L, 
        PortalCooldown: 0, 
        Pos: [-5.481268882751465f, 56.125f, 0.5345791578292847f], 
        Rotation: [108.59393310546875f, 89.88809204101562f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Tags: [], 
        UniqueID: -4896262717438L, 
        Variant: 0, 
        definitions: [], 
        identifier: "minecraft:item"
      }
    ], 
    palette: {}
  }, 
  structure_world_origin: [-6, 56, 0]
}
```

## `grass_sword`

- Путь `Swords_B/structures/grass_sword.mcstructure`; MD5 `d678cd531a0dfc64297c9ad410c0e25d`; NBT round-trip: побайтово совпал.
- Размер `[1, 1, 1]`; structure_world_origin `[-6, 56, 0]`; сущностей 1.
- Сущности: `minecraft:item`.
- Предметы с `Name` в пространствах `effect:` / `effect99:`:
  - `$.entities[0].Item.Name`: `effect:grass_sword`
- Буквальные вызовы:
  - `Swords_B/entities/witch.json:220` — `"run_command": { "command": [ "structure load grass_sword ~~~", "setblock ~ ~ ~ double_plant 2", "playsound dig.grass @a[r=12] ~~~" ] }`

### Полный типизированный SNBT

```snbt
{
  format_version: 1, 
  size: [1, 1, 1], 
  structure: {
    block_indices: [
      [], 
      []
    ], 
    entities: [
      {
        Age: 196s, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        Health: 5s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        Item: {
          Count: 1b, 
          Damage: 0s, 
          Name: "effect:grass_sword", 
          WasPickedUp: 0b
        }, 
        LastDimensionId: 0, 
        LootDropped: 0b, 
        MarkVariant: 0, 
        Motion: [-1.4176435361983736e-13f, 0.0f, -1.5896311366834712e-14f], 
        OnGround: 1b, 
        OwnerID: -8589934591L, 
        OwnerNew: -8589934591L, 
        PortalCooldown: 0, 
        Pos: [-5.480177879333496f, 56.125f, 0.4274146556854248f], 
        Rotation: [82.17916870117188f, 79.15447998046875f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Tags: [], 
        UniqueID: -8551279886219L, 
        Variant: 0, 
        definitions: ["+minecraft:item"], 
        identifier: "minecraft:item"
      }
    ], 
    palette: {}
  }, 
  structure_world_origin: [-6, 56, 0]
}
```

## `lightning_sword`

- Путь `Swords_B/structures/lightning_sword.mcstructure`; MD5 `731bb447e7e7416686d521a5242f8899`; NBT round-trip: побайтово совпал.
- Размер `[1, 1, 1]`; structure_world_origin `[488, 56, -18]`; сущностей 1.
- Сущности: `minecraft:item`.
- Предметы с `Name` в пространствах `effect:` / `effect99:`:
  - `$.entities[0].Item.Name`: `effect:lightning_sword`
- Буквальные вызовы:
  - `Swords_B/entities/centella.json:107` — `"run_command": { "command": [ "structure load lightning_sword ~ ~10 ~" ] }`

### Полный типизированный SNBT

```snbt
{
  format_version: 1, 
  size: [1, 1, 1], 
  structure: {
    block_indices: [
      [0], 
      [-1]
    ], 
    entities: [
      {
        Age: 133s, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        Health: 5s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        Item: {
          Count: 1b, 
          Damage: 0s, 
          Name: "effect:lightning_sword", 
          WasPickedUp: 0b
        }, 
        LastDimensionId: 0, 
        LootDropped: 0b, 
        MarkVariant: 0, 
        Motion: [-3.325447209268084e-11f, 0.0f, -7.837638177354833e-11f], 
        OnGround: 1b, 
        OwnerID: -8589934591L, 
        OwnerNew: -8589934591L, 
        PortalCooldown: 0, 
        Pos: [488.4828186035156f, 56.125f, -17.52618980407715f], 
        Rotation: [-87.01223754882812f, 89.89532470703125f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Tags: ["lightning_sword"], 
        UniqueID: -9062380994558L, 
        Variant: 0, 
        definitions: ["+minecraft:item", "+"], 
        identifier: "minecraft:item"
      }
    ], 
    palette: {
      default: {
        block_palette: [
          {
            name: "minecraft:air", 
            states: {}, 
            version: 17879555
          }
        ], 
        block_position_data: {}
      }
    }
  }, 
  structure_world_origin: [488, 56, -18]
}
```

## `obsidian_sword`

- Путь `Swords_B/structures/obsidian_sword.mcstructure`; MD5 `864f95fcdefae9b5295fdbd4300f922d`; NBT round-trip: побайтово совпал.
- Размер `[1, 1, 1]`; structure_world_origin `[-6, 56, 0]`; сущностей 1.
- Сущности: `minecraft:item`.
- Предметы с `Name` в пространствах `effect:` / `effect99:`:
  - `$.entities[0].Item.Name`: `effect:obsidian_sword`
- Буквальные вызовы:
  - `Swords_B/entities/item.json:228` — `"fire_sword_event_1": { "run_command": { "command": [ "structure load obsidian_sword ~ ~ ~", "playsound random.fizz @a[r=12] ~ ~ ~", "kill @s" ] } },`

### Полный типизированный SNBT

```snbt
{
  format_version: 1, 
  size: [1, 1, 1], 
  structure: {
    block_indices: [
      [], 
      []
    ], 
    entities: [
      {
        Age: 763s, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        Health: 5s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        Item: {
          Count: 1b, 
          Damage: 0s, 
          Name: "effect:obsidian_sword", 
          WasPickedUp: 0b, 
          tag: {
            Damage: 1000
          }
        }, 
        LastDimensionId: 0, 
        LootDropped: 0b, 
        MarkVariant: 0, 
        Motion: [-1.401298464324817e-45f, 0.0f, -1.401298464324817e-45f], 
        OnGround: 1b, 
        OwnerID: -8589934591L, 
        OwnerNew: -8589934591L, 
        PortalCooldown: 0, 
        Pos: [-5.457834243774414f, 56.125f, 0.45711666345596313f], 
        Rotation: [86.64590454101562f, 89.65509033203125f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Tags: [], 
        UniqueID: -4896262717439L, 
        Variant: 0, 
        definitions: [], 
        identifier: "minecraft:item"
      }
    ], 
    palette: {}
  }, 
  structure_world_origin: [-6, 56, 0]
}
```

## `silver_ore`

- Путь `Swords_B/structures/silver_ore.mcstructure`; MD5 `65799fad79d902a906b25454793992c7`; NBT round-trip: побайтово совпал.
- Размер `[1, 1, 1]`; structure_world_origin `[440, 9, 2416]`; сущностей 0.
- Сущности: нет.
- Предметы с `Name` в пространствах `effect:` / `effect99:`:
  - Не найдены.
- Буквальные вызовы:
  - Не найдены.

### Полный типизированный SNBT

```snbt
{
  format_version: 1, 
  size: [1, 1, 1], 
  structure: {
    block_indices: [
      [0], 
      [-1]
    ], 
    entities: [], 
    palette: {
      default: {
        block_palette: [
          {
            name: "effect99:silver_ore", 
            states: {}, 
            version: 17879555
          }
        ], 
        block_position_data: {}
      }
    }
  }, 
  structure_world_origin: [440, 9, 2416]
}
```

## `spectral_sword`

- Путь `Swords_B/structures/spectral_sword.mcstructure`; MD5 `a8c3b576c9c23272dfe868ad3029ed23`; NBT round-trip: побайтово совпал.
- Размер `[1, 1, 1]`; structure_world_origin `[-183, 43, -41]`; сущностей 1.
- Сущности: `minecraft:item`.
- Предметы с `Name` в пространствах `effect:` / `effect99:`:
  - `$.entities[0].Item.Name`: `effect:spectral_sword`
- Буквальные вызовы:
  - `Swords_B/entities/ender_crystal.json:102` — `"run_command": { "command": [ "structure load spectral_sword ~~~" ] }`
  - `Swords_B/entities/ghast.json:112` — `"run_command": { "command": [ "structure load spectral_sword ~~~" ] }`

### Полный типизированный SNBT

```snbt
{
  format_version: 1, 
  size: [1, 1, 1], 
  structure: {
    block_indices: [
      [], 
      []
    ], 
    entities: [
      {
        Age: 360s, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        Health: 5s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        Item: {
          Count: 1b, 
          Damage: 0s, 
          Name: "effect:spectral_sword", 
          WasPickedUp: 0b, 
          tag: {
            Damage: 0
          }
        }, 
        LastDimensionId: 1, 
        LootDropped: 0b, 
        MarkVariant: 0, 
        Motion: [3.410988800243152e-23f, 0.0f, 4.666815287221018e-23f], 
        OnGround: 1b, 
        OwnerID: -8589934591L, 
        OwnerNew: -8589934591L, 
        PortalCooldown: 0, 
        Pos: [-182.5467987060547f, 43.125f, -40.5103874206543f], 
        Rotation: [-46.1982421875f, 87.25848388671875f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Tags: [], 
        UniqueID: -8598524526572L, 
        Variant: 0, 
        definitions: ["+minecraft:item"], 
        identifier: "minecraft:item"
      }
    ], 
    palette: {}
  }, 
  structure_world_origin: [-183, 43, -41]
}
```

## `time_sword`

- Путь `Swords_B/structures/time_sword.mcstructure`; MD5 `37f3b438f675d386da96768d1d6d757a`; NBT round-trip: побайтово совпал.
- Размер `[1, 1, 1]`; structure_world_origin `[-6, 56, 0]`; сущностей 1.
- Сущности: `minecraft:item`.
- Предметы с `Name` в пространствах `effect:` / `effect99:`:
  - `$.entities[0].Item.Name`: `effect:time_sword`
- Буквальные вызовы:
  - `Swords_B/entities/item.json:176` — `"run_command": { "command": [ "structure load time_sword ~ ~1 ~", "time add 6000", "fill ~15 ~10 ~15 ~-15 ~-15 ~-15 concretepowder 4 replace sand", "particle minecraft:knockback_roar_particle ~ ~0.3 ~", "playsound random.levelup @a[r=16] ~ ~ ~ 1 0.5", "kill @s" ] }`

### Полный типизированный SNBT

```snbt
{
  format_version: 1, 
  size: [1, 1, 1], 
  structure: {
    block_indices: [
      [], 
      []
    ], 
    entities: [
      {
        Age: 373s, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        Health: 5s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        Item: {
          Count: 1b, 
          Damage: 0s, 
          Name: "effect:time_sword", 
          WasPickedUp: 0b
        }, 
        LastDimensionId: 0, 
        LootDropped: 0b, 
        MarkVariant: 0, 
        Motion: [4.873882045168942e-24f, 0.0f, -8.028344421694508e-25f], 
        OnGround: 1b, 
        OwnerID: -8589934591L, 
        OwnerNew: -8589934591L, 
        PortalCooldown: 0, 
        Pos: [-5.389373779296875f, 56.125f, 0.49385306239128113f], 
        Rotation: [98.1478271484375f, 89.8846435546875f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Tags: [], 
        UniqueID: -9161165242367L, 
        Variant: 0, 
        definitions: ["+minecraft:item", "+"], 
        identifier: "minecraft:item"
      }
    ], 
    palette: {}
  }, 
  structure_world_origin: [-6, 56, 0]
}
```

## `ultra_instinct_sword`

- Путь `Swords_B/structures/ultra_instinct_sword.mcstructure`; MD5 `cb8f1fe8ca52528c8f5ff901b0fd5a3a`; NBT round-trip: побайтово совпал.
- Размер `[1, 1, 1]`; structure_world_origin `[-6, 56, 0]`; сущностей 1.
- Сущности: `minecraft:item`.
- Предметы с `Name` в пространствах `effect:` / `effect99:`:
  - `$.entities[0].Item.Name`: `effect:ultra_instinct_sword`
- Буквальные вызовы:
  - `Swords_B/entities/item.json:152` — `"run_command": { "command": [ "structure load ultra_instinct_sword ~ ~1 ~", "fill ~15 ~10 ~15 ~-15 ~-15 ~-15 concretepowder 0 replace sand", "particle minecraft:example_flipbook ~ ~ ~", "particle minecraft:example_flipbook ~ ~1.5 ~", "playsound mob.wither.ambient @a[r=16] ~ ~1 ~ 2 0.6", "kill @s" ] }`
  - `Swords_B/entities/item.json:164` — `"run_command": { "command": [ "structure load ultra_instinct_sword ~ ~1 ~", "fill ~15 ~10 ~15 ~-15 ~-15 ~-15 concretepowder 0 replace sand", "particle minecraft:example_flipbook ~ ~ ~", "particle minecraft:example_flipbook ~ ~1.5 ~", "playsound mob.wither.ambient @a[r=16] ~ ~1 ~ 2 0.6", "kill @s" ] }`

### Полный типизированный SNBT

```snbt
{
  format_version: 1, 
  size: [1, 1, 1], 
  structure: {
    block_indices: [
      [], 
      []
    ], 
    entities: [
      {
        Age: 247s, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        Health: 5s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        Item: {
          Count: 1b, 
          Damage: 0s, 
          Name: "effect:ultra_instinct_sword", 
          WasPickedUp: 0b
        }, 
        LastDimensionId: 0, 
        LootDropped: 0b, 
        MarkVariant: 0, 
        Motion: [-5.359029557384434e-17f, 0.0f, -1.0730947085020811e-17f], 
        OnGround: 1b, 
        OwnerID: -8589934591L, 
        OwnerNew: -8589934591L, 
        PortalCooldown: 0, 
        Pos: [-5.573231220245361f, 56.125f, 0.5588690042495728f], 
        Rotation: [152.71014404296875f, 88.58389282226562f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Tags: [], 
        UniqueID: -8297876808966L, 
        Variant: 0, 
        definitions: ["+minecraft:item"], 
        identifier: "minecraft:item"
      }
    ], 
    palette: {}
  }, 
  structure_world_origin: [-6, 56, 0]
}
```

## `wet_sponge_sword`

- Путь `Swords_B/structures/wet_sponge_sword.mcstructure`; MD5 `faab8d6e22710c541a6f1f2f79741636`; NBT round-trip: побайтово совпал.
- Размер `[1, 1, 1]`; structure_world_origin `[-6, 56, 0]`; сущностей 1.
- Сущности: `minecraft:item`.
- Предметы с `Name` в пространствах `effect:` / `effect99:`:
  - `$.entities[0].Item.Name`: `effect:wet_sponge_sword`
- Буквальные вызовы:
  - `Swords_B/entities/item.json:134` — `"wet_sponge_sword": { "run_command": { "command": [ "structure load wet_sponge_sword ~ ~ ~", "kill @s" ] }`

### Полный типизированный SNBT

```snbt
{
  format_version: 1, 
  size: [1, 1, 1], 
  structure: {
    block_indices: [
      [], 
      []
    ], 
    entities: [
      {
        Age: 340s, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        Health: 5s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        Item: {
          Count: 1b, 
          Damage: 0s, 
          Name: "effect:wet_sponge_sword", 
          WasPickedUp: 0b
        }, 
        LastDimensionId: 0, 
        LootDropped: 0b, 
        MarkVariant: 0, 
        Motion: [5.918024413548444e-23f, 0.0f, 5.886522483921455e-22f], 
        OnGround: 1b, 
        OwnerID: -8589934591L, 
        OwnerNew: -8589934591L, 
        PortalCooldown: 0, 
        Pos: [-5.427984237670898f, 56.125f, 0.595425009727478f], 
        Rotation: [97.978759765625f, 89.8863525390625f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Tags: [], 
        UniqueID: -5695126634494L, 
        Variant: 0, 
        definitions: ["+minecraft:item"], 
        identifier: "minecraft:item"
      }
    ], 
    palette: {}
  }, 
  structure_world_origin: [-6, 56, 0]
}
```

## `wither_sword`

- Путь `Swords_B/structures/wither_sword.mcstructure`; MD5 `cab19628aded11b46ad944ae45f02b5e`; NBT round-trip: побайтово совпал.
- Размер `[1, 1, 1]`; structure_world_origin `[-6, 56, 0]`; сущностей 1.
- Сущности: `minecraft:item`.
- Предметы с `Name` в пространствах `effect:` / `effect99:`:
  - `$.entities[0].Item.Name`: `effect:wither_sword`
- Буквальные вызовы:
  - `Swords_B/entities/wither.json:163` — `"run_command": { "command": [ "structure load wither_sword ~ ~ ~" ] }`

### Полный типизированный SNBT

```snbt
{
  format_version: 1, 
  size: [1, 1, 1], 
  structure: {
    block_indices: [
      [], 
      []
    ], 
    entities: [
      {
        Age: 401s, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        Health: 5s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        Item: {
          Count: 1b, 
          Damage: 0s, 
          Name: "effect:wither_sword", 
          WasPickedUp: 0b
        }, 
        LastDimensionId: 0, 
        LootDropped: 0b, 
        MarkVariant: 0, 
        Motion: [3.81403000243484e-26f, 0.0f, -6.0865976774906346e-27f], 
        OnGround: 1b, 
        OwnerID: -8589934591L, 
        OwnerNew: -8589934591L, 
        PortalCooldown: 0, 
        Pos: [-5.417070388793945f, 56.125f, 0.5252560377120972f], 
        Rotation: [95.7054443359375f, 89.89163208007812f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Tags: ["wither_sword"], 
        UniqueID: -9032316223484L, 
        Variant: 0, 
        definitions: ["+minecraft:item", "+"], 
        identifier: "minecraft:item"
      }
    ], 
    palette: {}
  }, 
  structure_world_origin: [-6, 56, 0]
}
```

## `wolf_sword`

- Путь `Swords_B/structures/wolf_sword.mcstructure`; MD5 `2a705baa91249bc0355277e76511302a`; NBT round-trip: побайтово совпал.
- Размер `[1, 1, 1]`; structure_world_origin `[-6, 56, 0]`; сущностей 1.
- Сущности: `minecraft:item`.
- Предметы с `Name` в пространствах `effect:` / `effect99:`:
  - `$.entities[0].Item.Name`: `effect:wolf_sword`
- Буквальные вызовы:
  - `Swords_B/entities/alpha_wolf.json:278` — `"structure load wolf_sword ~ ~ ~"`

### Полный типизированный SNBT

```snbt
{
  format_version: 1, 
  size: [1, 1, 1], 
  structure: {
    block_indices: [
      [], 
      []
    ], 
    entities: [
      {
        Age: 295s, 
        Chested: 0b, 
        Color: 0b, 
        Color2: 0b, 
        FallDistance: 0.0f, 
        Fire: 0s, 
        Health: 5s, 
        Invulnerable: 0b, 
        IsAngry: 0b, 
        IsAutonomous: 0b, 
        IsBaby: 0b, 
        IsEating: 0b, 
        IsGliding: 0b, 
        IsGlobal: 0b, 
        IsIllagerCaptain: 0b, 
        IsOrphaned: 0b, 
        IsOutOfControl: 0b, 
        IsRoaring: 0b, 
        IsScared: 0b, 
        IsStunned: 0b, 
        IsSwimming: 0b, 
        IsTamed: 0b, 
        IsTrusting: 0b, 
        Item: {
          Count: 1b, 
          Damage: 0s, 
          Name: "effect:wolf_sword", 
          WasPickedUp: 0b
        }, 
        LastDimensionId: 0, 
        LootDropped: 0b, 
        MarkVariant: 0, 
        Motion: [-2.0608805103943046e-21f, 0.0f, -4.398546639741363e-21f], 
        OnGround: 1b, 
        OwnerID: -8589934591L, 
        OwnerNew: -8589934591L, 
        PortalCooldown: 0, 
        Pos: [-5.47147798538208f, 56.125f, 0.44039663672447205f], 
        Rotation: [103.64788818359375f, 89.88983154296875f], 
        Saddled: 0b, 
        Sheared: 0b, 
        ShowBottom: 0b, 
        Sitting: 0b, 
        SkinID: 0, 
        Strength: 0, 
        StrengthMax: 0, 
        Tags: [], 
        UniqueID: -7748121001707L, 
        Variant: 0, 
        definitions: ["+minecraft:item"], 
        identifier: "minecraft:item"
      }
    ], 
    palette: {}
  }, 
  structure_world_origin: [-6, 56, 0]
}
```

