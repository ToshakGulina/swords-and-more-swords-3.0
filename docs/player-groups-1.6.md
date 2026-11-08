# Добавление и удаление групп игрока — 1.6

Автоматический индекс для `Sword_B/entities/player.json`: все упоминания `add.component_groups` и `remove.component_groups` внутри событий этого файла, включая вложенные sequence/randomize. Ссылки — пути внутри разобранного объекта `minecraft:entity`; индекс показывает объявления, не вызовы и не последовательность исполнения.

«Нет» значит только, что такой операции не найдено среди событий данного файла: другие события, команды, внешние пакеты, дефолты и правила разрешения наложенных компонентов могут влиять на результат. Не следует считать отсутствие remove доказательством постоянно действующего эффекта. Фильтры на ветвях и в вызывающих сенсорах смотреть в [реестре сущностей](entity-ledger-1.6.md), [прямых цепочках](chain-index-1.6.md) или [ручных цепочках 1.6](manual-traces-1.6.md).

Объявлено групп: 30. У групп с add без локального remove: 2. Ссылки на группы, не объявленные в player: 0.

| Группа | Есть определение | Добавление | Удаление |
|---|---|---|---|
| `minecraft:add_bad_omen` | да | `$.events.minecraft:gain_bad_omen.add.component_groups` | `$.events.minecraft:clear_add_bad_omen.remove.component_groups` |
| `minecraft:blaze_sword` | да | `$.events.minecraft:blaze_sword.add.component_groups` | `$.events.minecraft:event_normal_player.remove.component_groups` |
| `minecraft:bone_sword` | да | `$.events.minecraft:bone_sword.add.component_groups` | `$.events.minecraft:event_normal_player.remove.component_groups` |
| `minecraft:cactus_sword` | да | `$.events.minecraft:cactus_sword.add.component_groups` | `$.events.minecraft:event_normal_player.remove.component_groups` |
| `minecraft:clear_bad_omen_spell_effect` | да | `$.events.minecraft:clear_add_bad_omen.add.component_groups` | нет |
| `minecraft:coal_sword` | да | `$.events.minecraft:coal_sword.add.component_groups` | `$.events.minecraft:event_normal_player.remove.component_groups` |
| `minecraft:creeper_sword` | да | `$.events.minecraft:creeper_sword.add.component_groups` | `$.events.minecraft:event_normal_player.remove.component_groups` |
| `minecraft:emerald_sword` | да | `$.events.minecraft:emerald_sword.add.component_groups` | `$.events.minecraft:event_normal_player.remove.component_groups` |
| `minecraft:ender_sword` | да | `$.events.minecraft:ender_sword.add.component_groups` | `$.events.minecraft:event_normal_player.remove.component_groups` |
| `minecraft:fire_sword` | да | `$.events.minecraft:fire_sword.add.component_groups` | `$.events.minecraft:event_normal_player.remove.component_groups` |
| `minecraft:glowstone_sword` | да | `$.events.minecraft:glowstone_sword.add.component_groups` | `$.events.minecraft:event_normal_player.remove.component_groups` |
| `minecraft:grass_sword` | да | `$.events.minecraft:grass_sword.add.component_groups` | `$.events.minecraft:event_normal_player.remove.component_groups` |
| `minecraft:ice_sword` | да | `$.events.minecraft:ice_sword.add.component_groups` | `$.events.minecraft:event_normal_player.remove.component_groups` |
| `minecraft:jungle_sword` | да | `$.events.minecraft:jungle_sword.add.component_groups` | `$.events.minecraft:event_normal_player.remove.component_groups` |
| `minecraft:lapis_sword` | да | `$.events.minecraft:lapis_sword.add.component_groups` | `$.events.minecraft:event_normal_player.remove.component_groups` |
| `minecraft:lightning_sword` | да | `$.events.minecraft:lightning_sword.add.component_groups` | `$.events.minecraft:event_normal_player.remove.component_groups` |
| `minecraft:magma_sword` | да | `$.events.minecraft:magma_sword.add.component_groups` | `$.events.minecraft:event_normal_player.remove.component_groups` |
| `minecraft:normal_player` | да | `$.events.minecraft:event_normal_player.add.component_groups` | нет |
| `minecraft:obsidian_sword` | да | `$.events.minecraft:obsidian_sword.add.component_groups` | `$.events.minecraft:event_normal_player.remove.component_groups` |
| `minecraft:quartz_sword` | да | `$.events.minecraft:quartz_sword.add.component_groups` | `$.events.minecraft:event_normal_player.remove.component_groups` |
| `minecraft:raid_trigger` | да | `$.events.minecraft:trigger_raid.add.component_groups` | `$.events.minecraft:remove_raid_trigger.remove.component_groups` |
| `minecraft:sea_sword` | да | `$.events.minecraft:sea_sword.add.component_groups` | `$.events.minecraft:event_normal_player.remove.component_groups` |
| `minecraft:shulker_sword` | да | `$.events.minecraft:shulker_sword.add.component_groups` | `$.events.minecraft:event_normal_player.remove.component_groups` |
| `minecraft:slime_sword` | да | `$.events.minecraft:slime_sword.add.component_groups` | `$.events.minecraft:event_normal_player.remove.component_groups` |
| `minecraft:spectral_sword` | да | `$.events.minecraft:spectral_sword.add.component_groups` | `$.events.minecraft:event_normal_player.remove.component_groups` |
| `minecraft:spider_sword` | да | `$.events.minecraft:spider_sword.add.component_groups` | `$.events.minecraft:event_normal_player.remove.component_groups` |
| `minecraft:sponge_sword` | да | `$.events.minecraft:sponge_sword.add.component_groups` | `$.events.minecraft:event_normal_player.remove.component_groups` |
| `minecraft:sword_of_time` | да | `$.events.minecraft:sword_of_time.add.component_groups` | `$.events.minecraft:event_normal_player.remove.component_groups` |
| `minecraft:tnt_sword` | да | `$.events.minecraft:tnt_sword.add.component_groups` | `$.events.minecraft:event_normal_player.remove.component_groups` |
| `minecraft:wither_sword` | да | `$.events.minecraft:wither_sword.add.component_groups` | `$.events.minecraft:event_normal_player.remove.component_groups` |
