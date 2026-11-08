# Клиентские ресурсы и буквальные связи — 2.8.14

Автоматическое сопоставление определённых в resource pack идентификаторов и путей. «Не найдено локально» не означает ошибки: многие модели, анимации, текстуры и контроллеры являются ванильными или могут поступать из других пакетов. Списки не доказывают работающий рендер, не интерпретируют условия Molang и не обрабатывают динамические ссылки. JSON5 сохраняет только последнее значение повторённого ключа: при диагностике сверять оригинал. Полные исходные файлы и имена компонентов остаются в архиве.

## Ошибки и повторные ключи

- Не обнаружены парсером JSON5.

## Локальные определения и совпадения ID

### geometry

| ID | Определения в пакете |
|---|---|
| `geometry.baby_slime` | `Swords_R/models/entity/baby_slime.geo.json` |
| `geometry.blaze_aura` | `Swords_R/models/entity/blaze_aura.geo.json` |
| `geometry.blaze_rods` | `Swords_R/models/entity/blaze_rods.geo.json` |
| `geometry.fake_ice` | `Swords_R/models/blocks/fake_ice.json` |
| `geometry.fake_ice2` | `Swords_R/models/blocks/fake_ice2.json` |
| `geometry.fake_ice3` | `Swords_R/models/blocks/fake_ice3.json` |
| `geometry.fake_ice4` | `Swords_R/models/blocks/fake_ice4.json` |
| `geometry.ghost` | `Swords_R/models/entity/ghost.geo.json` |
| `geometry.grass` | `Swords_R/models/entity/grass.geo.json` |
| `geometry.mermaid_player.tail` | `Swords_R/models/entity/mermaid_player.geo.json` |
| `geometry.mountable_slime` | `Swords_R/models/entity/mountable_slime.geo.json` |
| `geometry.null` | `Swords_R/models/blocks/null.geo.json` |
| `geometry.player_ghost` | `Swords_R/models/entity/player_ghost.geo.json` |
| `geometry.pumpkin_projectile` | `Swords_R/models/entity/pumpkin_projectile.geo.json` |
| `geometry.shulker_shield` | `Swords_R/models/entity/shulker_shield.geo.json` |
| `geometry.slime_king.armor` | `Swords_R/models/entity/slime_king_armor.geo.json` |
| `geometry.spectral_block` | `Swords_R/models/blocks/spectral_block.json` |
| `geometry.ultra_instinct_aura` | `Swords_R/models/entity/ultra_instinct_aura.geo.json` |
| `geometry.ultra_instinct_projectile` | `Swords_R/models/entity/ultra_instinct_projectile.geo.json` |
| `geometry.wolf_transformation` | `Swords_R/models/entity/wolf_transformation.geo.json` |
| `geometry.wolf_vision` | `Swords_R/models/entity/wolf_vision.geo.json` |

### animation

| ID | Определения в пакете |
|---|---|
| `animation.baby_slime.normal_speed_wing` | `Swords_R/animations/baby_slime.animation.json` |
| `animation.baby_slime.speed_wing` | `Swords_R/animations/baby_slime.animation.json` |
| `animation.baby_slime.wing` | `Swords_R/animations/baby_slime.animation.json` |
| `animation.blaze_rods` | `Swords_R/animations/blaze_rods.animation.json` |
| `animation.ghost.look_at_target` | `Swords_R/animations/ghost.animation.json` |
| `animation.ghost.move` | `Swords_R/animations/ghost.animation.json` |
| `animation.grass.attack` | `Swords_R/animations/grass.animation.json` |
| `animation.mermaid_player.default_pose` | `Swords_R/animations/mermaid_player.animation.json` |
| `animation.mermaid_player.drowning` | `Swords_R/animations/mermaid_player.animation.json` |
| `animation.mermaid_player.swimming` | `Swords_R/animations/mermaid_player.animation.json` |
| `animation.mermaid_player.tail` | `Swords_R/animations/mermaid_player.animation.json` |
| `animation.move` | `Swords_R/animations/ultra_instinct_projectile.animation.json` |
| `animation.player.explode` | `Swords_R/animations/mobs.animation.json` |
| `animation.player_ghost.move` | `Swords_R/animations/mobs.animation.json` |
| `animation.player_ghost.vision` | `Swords_R/animations/mobs.animation.json` |
| `animation.shulker_shield.closed` | `Swords_R/animations/shulker_shield.animation.json` |
| `animation.ultra_instinct.move` | `Swords_R/animations/ultra_instinct_move.animation.json` |
| `animation.ultra_instinct_sword.attack` | `Swords_R/animations/mobs.animation.json` |

### animation_controller

| ID | Определения в пакете |
|---|---|
| `controller.animation.baby_slime.move` | `Swords_R/animation_controllers/baby_slime.animation_controllers.json` |
| `controller.animation.ghost.move` | `Swords_R/animation_controllers/ghost.animation_controllers.json` |
| `controller.animation.grass.move` | `Swords_R/animation_controllers/grass.animation_controllers.json` |
| `controller.animation.shulker_shield.move` | `Swords_R/animation_controllers/shulker_shield.animation_controllers.json` |
| `controller.animation.ultra_instinct_projectile.move` | `Swords_R/animation_controllers/ultra_instinct_projectile.animation_controllers.json` |

### render_controller

| ID | Определения в пакете |
|---|---|
| `controller.render.blaze_aura` | `Swords_R/render_controllers/blaze_aura.render_controllers.json` |
| `controller.render.blaze_rods` | `Swords_R/render_controllers/blaze_rods.render_controllers.json` |
| `controller.render.default` | `Swords_R/render_controllers/default.render_controllers.json` |
| `controller.render.enderman` | `Swords_R/render_controllers/enderman.render_controllers.json` |
| `controller.render.ghost` | `Swords_R/render_controllers/ghost.render_controllers.json` |
| `controller.render.grass` | `Swords_R/render_controllers/grass.render_controllers.json` |
| `controller.render.mermaid_player` | `Swords_R/render_controllers/mermaid_player.render_controllers.json` |
| `controller.render.player_ghost` | `Swords_R/render_controllers/player_ghost.render_controllers.json` |
| `controller.render.pumpkin_projectile` | `Swords_R/render_controllers/pumpkin_projectile.render_controllers.json` |
| `controller.render.shulker_shield` | `Swords_R/render_controllers/shulker_shield.render_controllers.json` |
| `controller.render.ultra_instinct_aura` | `Swords_R/render_controllers/ultra_instinct_aura.render_controllers.json` |
| `controller.render.ultra_instinct_projectile` | `Swords_R/render_controllers/ultra_instinct_projectile.render_controllers.json` |
| `controller.render.witch` | `Swords_R/render_controllers/witch.render_controllers.json` |
| `controller.render.witch.v1.0` | `Swords_R/render_controllers/witch.render_controllers.json` |
| `controller.render.wolf_transformation` | `Swords_R/render_controllers/wolf_transformation.render_controllers.json` |
| `controller.render.wolf_vision` | `Swords_R/render_controllers/wolf_vision.render_controllers.json` |

### particle

| ID | Определения в пакете |
|---|---|
| `minecraft:example_bounce` | `Swords_R/particles/examples/example_bounce.json` |
| `minecraft:example_directional_sphere` | `Swords_R/particles/examples/example_directional_sphere.json` |
| `minecraft:example_directional_sphere_2` | `Swords_R/particles/examples/example_directional_sphere_2.json` |
| `minecraft:example_flipbook` | `Swords_R/particles/examples/example_flipbook.json` |
| `minecraft:example_linearcurve` | `Swords_R/particles/examples/example_linearcurve.json` |
| `minecraft:ghost_spiral` | `Swords_R/particles/examples/ghost_spiral.json` |
| `minecraft:nether_star_hit` | `Swords_R/particles/nether_star_hit.json` |

### client_entity

| ID | Определения в пакете |
|---|---|
| `entity:alpha_wolf` | `Swords_R/entity/alpha_wolf.entity.json` |
| `entity:bee_sword` | `Swords_R/entity/bee_sword.json` |
| `entity:fake_fireball` | `Swords_R/entity/fake_fireball.entity.json` |
| `entity:ghost` | `Swords_R/entity/ghost.v1.0.json` |
| `entity:grass` | `Swords_R/entity/grass.v1.0.json` |
| `entity:mountable_slime` | `Swords_R/entity/mountable_slime.v1.0.json` |
| `entity:nether_star_projectile` | `Swords_R/entity/nether_star.v1.0.json` |
| `entity:pumpkin_projectile` | `Swords_R/entity/pumpkin_projectile.entity.json` |
| `entity:shulker_shield` | `Swords_R/entity/shulker_shield.v1.0.json` |
| `entity:slime_king` | `Swords_R/entity/slime_king.entity.json` |
| `entity:ultra_instinct_projectile` | `Swords_R/entity/ultra_instinct_projectile.json` |
| `entity:web` | `Swords_R/entity/web.v1.0.json` |
| `minecraft:bed` | `Swords_R/entity/bed_sword.entity.json` |
| `minecraft:enderman` | `Swords_R/entity/enderman.entity.json` |
| `minecraft:player` | `Swords_R/entity/player.entity.json` |
| `minecraft:witch` | `Swords_R/entity/witch.entity.json`, `Swords_R/entity/witch.v1.0.entity.json` |

## Описания клиентских сущностей и ссылки

### `entity:alpha_wolf` — `Swords_R/entity/alpha_wolf.entity.json`

- Полный `description`: `{"identifier":"entity:alpha_wolf","materials":{"default":"wolf"},"textures":{"default":"textures/entity/wolf_transformation","angry":"textures/entity/wolf/wolf_angry","tame":"textures/entity/wolf/wolf_tame"},"geometry":{"default":"geometry.wolf"},"scripts":{"pre_animation":["variable.body_shake_angle = 0.05 * query.frame_alpha + query.shake_angle;","variable.body_roll_progress = Math.clamp((variable.body_shake_angle - 0.16) / 1.8, 0, 1);","variable.body_rot_z = Math.sin(variable.body_roll_progress * 180) * Math.sin(variable.body_roll_progress * 1980) * 27;","variable.upper_body_roll_progress = Math.clamp((variable.body_shake_angle - 0.08) / 1.8, 0, 1);","variable.upper_body_rot_z = (Math.sin(variable.upper_body_roll_progress * 180) * Math.sin(variable.upper_body_roll_progress * 1980) * 27) - variable.body_rot_z;","variable.tail_roll_progress = Math.clamp((variable.body_shake_angle - 0.2) / 1.8, 0, 1);","variable.tail_rot_z = (Math.sin(variable.tail_roll_progress * 180) * Math.sin(variable.tail_roll_progress * 1980) * 27) - variable.body_rot_z;","variable.head_roll_progress = Math.clamp(variable.body_shake_angle / 1.8, 0, 1);","variable.head_rot_z = (Math.sin(variable.head_roll_progress * 180) * Math.sin(variable.head_roll_progress * 1980) * 27) - variable.body_rot_z;"]},"animations":{"wolf_setup":"animation.wolf.setup","wolf_baby_scaling":"animation.wolf.baby_scaling","wolf_look_at":"animation.common.look_at_target","wolf_head_rot_z":"animation.wolf.head_rot_z","wolf_tail_default":"animation.wolf.tail_default","wolf_angry":"animation.wolf.angry","wolf_sitting":"animation.wolf.sitting","wolf_shaking":"animation.wolf.shaking","wolf_leg_default":"animation.wolf.leg_default"},"animation_controllers":[{"wolf_setup":"controller.animation.wolf.setup"},{"wolf_look_at":"controller.animation.wolf.look_at"},{"wolf_baby_scaling":"controller.animation.wolf.baby_scaling"},{"wolf_head_rot_z":"controller.animation.wolf.head_rot_z"},{"wolf_tail_default":"controller.animation.wolf.tail_default"},{"wolf_angry":"controller.animation.wolf.angry"},{"wolf_sitting":"controller.animation.wolf.sitting"},{"wolf_shaking":"controller.animation.wolf.shaking"}],"render_controllers":["controller.render.wolf"],"spawn_egg":{"texture":"spawn_egg","texture_index":4}}`

- texture `default` → `textures/entity/wolf_transformation` → `Swords_R/textures/entity/wolf_transformation.png`
- texture `angry` → `textures/entity/wolf/wolf_angry` → не найдено локально (возможно ванильный ресурс)
- texture `tame` → `textures/entity/wolf/wolf_tame` → не найдено локально (возможно ванильный ресурс)
- geometry `default` → `geometry.wolf` → не найдено локально (возможно ванильный ресурс)
- animation `wolf_setup` → `animation.wolf.setup` → не найдено локально (возможно ванильный ресурс)
- animation `wolf_baby_scaling` → `animation.wolf.baby_scaling` → не найдено локально (возможно ванильный ресурс)
- animation `wolf_look_at` → `animation.common.look_at_target` → не найдено локально (возможно ванильный ресурс)
- animation `wolf_head_rot_z` → `animation.wolf.head_rot_z` → не найдено локально (возможно ванильный ресурс)
- animation `wolf_tail_default` → `animation.wolf.tail_default` → не найдено локально (возможно ванильный ресурс)
- animation `wolf_angry` → `animation.wolf.angry` → не найдено локально (возможно ванильный ресурс)
- animation `wolf_sitting` → `animation.wolf.sitting` → не найдено локально (возможно ванильный ресурс)
- animation `wolf_shaking` → `animation.wolf.shaking` → не найдено локально (возможно ванильный ресурс)
- animation `wolf_leg_default` → `animation.wolf.leg_default` → не найдено локально (возможно ванильный ресурс)
- render controller `controller.render.wolf` → не найдено локально (возможно ванильный ресурс)

### `entity:bee_sword` — `Swords_R/entity/bee_sword.json`

- Полный `description`: `{"identifier":"entity:bee_sword","materials":{"default":"bee"},"textures":{"default":"textures/entity/bee/bee_angry"},"geometry":{"default":"geometry.bee"},"animations":{"flying":"animation.bee.flying"},"scripts":{"animate":["flying"]},"render_controllers":["controller.render.default"]}`

- texture `default` → `textures/entity/bee/bee_angry` → не найдено локально (возможно ванильный ресурс)
- geometry `default` → `geometry.bee` → не найдено локально (возможно ванильный ресурс)
- animation `flying` → `animation.bee.flying` → не найдено локально (возможно ванильный ресурс)
- render controller `controller.render.default` → `Swords_R/render_controllers/default.render_controllers.json`

### `entity:fake_fireball` — `Swords_R/entity/fake_fireball.entity.json`

- Полный `description`: `{"identifier":"entity:fake_fireball","materials":{"default":"fireball"},"textures":{"default":"textures/items/fireball"},"geometry":{"default":"geometry.fireball"},"animations":{"face_player":"animation.actor.billboard"},"scripts":{"scale":"0.5","animate":["face_player"]},"render_controllers":["controller.render.fireball"]}`

- texture `default` → `textures/items/fireball` → не найдено локально (возможно ванильный ресурс)
- geometry `default` → `geometry.fireball` → не найдено локально (возможно ванильный ресурс)
- animation `face_player` → `animation.actor.billboard` → не найдено локально (возможно ванильный ресурс)
- render controller `controller.render.fireball` → не найдено локально (возможно ванильный ресурс)

### `entity:ghost` — `Swords_R/entity/ghost.v1.0.json`

- Полный `description`: `{"identifier":"entity:ghost","materials":{"ghost":"ghost"},"textures":{"ghost":"textures/entity/ghost"},"geometry":{"ghost":"geometry.ghost"},"animations":{"look_at_target":"animation.ghost.look_at_target","move":"animation.ghost.move"},"animation_controllers":[{"move":"controller.animation.ghost.move"}],"render_controllers":["controller.render.ghost"],"spawn_egg":{"base_color":"#ffffff","overlay_color":"#ffffff"}}`

- texture `ghost` → `textures/entity/ghost` → `Swords_R/textures/entity/ghost.png`
- geometry `ghost` → `geometry.ghost` → `Swords_R/models/entity/ghost.geo.json`
- animation `look_at_target` → `animation.ghost.look_at_target` → `Swords_R/animations/ghost.animation.json`
- animation `move` → `animation.ghost.move` → `Swords_R/animations/ghost.animation.json`
- render controller `controller.render.ghost` → `Swords_R/render_controllers/ghost.render_controllers.json`

### `entity:grass` — `Swords_R/entity/grass.v1.0.json`

- Полный `description`: `{"identifier":"entity:grass","materials":{"default":"grass"},"textures":{"default":"textures/entity/grass"},"geometry":{"default":"geometry.grass"},"animations":{"move":"animation.grass.attack"},"animation_controllers":[{"move":"controller.animation.grass.move"}],"render_controllers":["controller.render.grass"]}`

- texture `default` → `textures/entity/grass` → `Swords_R/textures/entity/grass.png`
- geometry `default` → `geometry.grass` → `Swords_R/models/entity/grass.geo.json`
- animation `move` → `animation.grass.attack` → `Swords_R/animations/grass.animation.json`
- render controller `controller.render.grass` → `Swords_R/render_controllers/grass.render_controllers.json`

### `entity:mountable_slime` — `Swords_R/entity/mountable_slime.v1.0.json`

- Полный `description`: `{"identifier":"entity:mountable_slime","materials":{"default":"slime","outer":"slime_outer"},"textures":{"default":"textures/entity/slime/baby_slime"},"geometry":{"default":"geometry.mountable_slime","armor":"geometry.baby_slime"},"animations":{"not_jump":"animation.baby_slime.normal_speed_wing","is_jump":"animation.baby_slime.speed_wing"},"animation_controllers":[{"move":"controller.animation.baby_slime.move"}],"scripts":{"pre_animation":["variable.squish_factor = (query.previous_squish_value + (query.current_squish_value - query.previous_squish_value) * query.frame_alpha);","variable.bounce = 1 / ((variable.squish_factor / (query.variant * 0.5 + 1)) + 1);","variable.horizontal_scale_amount = variable.bounce * query.variant;","variable.vertical_scale_amount = (1 / variable.bounce) * query.variant;"],"scaleX":"variable.horizontal_scale_amount","scaleY":"variable.vertical_scale_amount","scaleZ":"variable.horizontal_scale_amount"},"render_controllers":["controller.render.slime","controller.render.slime_armor"]}`

- texture `default` → `textures/entity/slime/baby_slime` → `Swords_R/textures/entity/slime/baby_slime.png`
- geometry `default` → `geometry.mountable_slime` → `Swords_R/models/entity/mountable_slime.geo.json`
- geometry `armor` → `geometry.baby_slime` → `Swords_R/models/entity/baby_slime.geo.json`
- animation `not_jump` → `animation.baby_slime.normal_speed_wing` → `Swords_R/animations/baby_slime.animation.json`
- animation `is_jump` → `animation.baby_slime.speed_wing` → `Swords_R/animations/baby_slime.animation.json`
- render controller `controller.render.slime` → не найдено локально (возможно ванильный ресурс)
- render controller `controller.render.slime_armor` → не найдено локально (возможно ванильный ресурс)

### `entity:nether_star_projectile` — `Swords_R/entity/nether_star.v1.0.json`

- Полный `description`: `{"identifier":"entity:nether_star_projectile","materials":{"default":"snowball"},"textures":{"default":"textures/items/nether_star"},"geometry":{"default":"geometry.item_sprite"},"render_controllers":["controller.render.item_sprite"],"animations":{"flying":"animation.actor.billboard"},"scripts":{"animate":["flying"]}}`

- texture `default` → `textures/items/nether_star` → не найдено локально (возможно ванильный ресурс)
- geometry `default` → `geometry.item_sprite` → не найдено локально (возможно ванильный ресурс)
- animation `flying` → `animation.actor.billboard` → не найдено локально (возможно ванильный ресурс)
- render controller `controller.render.item_sprite` → не найдено локально (возможно ванильный ресурс)

### `entity:pumpkin_projectile` — `Swords_R/entity/pumpkin_projectile.entity.json`

- Полный `description`: `{"identifier":"entity:pumpkin_projectile","materials":{"default":"shulker_bullet"},"textures":{"default":"textures/entity/pumpkin_projectile"},"geometry":{"default":"geometry.pumpkin_projectile"},"animations":{"move":"animation.wither_skull.move"},"scripts":{"animate":["move"]},"render_controllers":["controller.render.pumpkin_projectile"]}`

- texture `default` → `textures/entity/pumpkin_projectile` → `Swords_R/textures/entity/pumpkin_projectile.png`
- geometry `default` → `geometry.pumpkin_projectile` → `Swords_R/models/entity/pumpkin_projectile.geo.json`
- animation `move` → `animation.wither_skull.move` → не найдено локально (возможно ванильный ресурс)
- render controller `controller.render.pumpkin_projectile` → `Swords_R/render_controllers/pumpkin_projectile.render_controllers.json`

### `entity:shulker_shield` — `Swords_R/entity/shulker_shield.v1.0.json`

- Полный `description`: `{"identifier":"entity:shulker_shield","materials":{"default":"shulker_shield"},"textures":{"default":"textures/entity/shulker_shield"},"geometry":{"default":"geometry.shulker_shield"},"animations":{"move":"animation.shulker_shield.closed"},"animation_controllers":[{"move":"controller.animation.shulker_shield.move"}],"render_controllers":["controller.render.shulker_shield"]}`

- texture `default` → `textures/entity/shulker_shield` → `Swords_R/textures/entity/shulker_shield.png`
- geometry `default` → `geometry.shulker_shield` → `Swords_R/models/entity/shulker_shield.geo.json`
- animation `move` → `animation.shulker_shield.closed` → `Swords_R/animations/shulker_shield.animation.json`
- render controller `controller.render.shulker_shield` → `Swords_R/render_controllers/shulker_shield.render_controllers.json`

### `entity:slime_king` — `Swords_R/entity/slime_king.entity.json`

- Полный `description`: `{"identifier":"entity:slime_king","materials":{"default":"slime","outer":"slime_outer"},"textures":{"default":"textures/entity/slime/slime_king"},"geometry":{"default":"geometry.slime","armor":"geometry.slime_king.armor"},"scripts":{"pre_animation":["variable.squish_factor = (query.previous_squish_value + (query.current_squish_value - query.previous_squish_value) * query.frame_alpha);","variable.bounce = 1 / ((variable.squish_factor / (query.variant * 0.5 + 1)) + 1);","variable.horizontal_scale_amount = variable.bounce * query.variant;","variable.vertical_scale_amount = (1 / variable.bounce) * query.variant;"],"scaleX":"variable.horizontal_scale_amount","scaleY":"variable.vertical_scale_amount","scaleZ":"variable.horizontal_scale_amount"},"render_controllers":["controller.render.slime","controller.render.slime_armor"],"spawn_egg":{"base_color":"#577fba","overlay_color":"#577fba"}}`

- texture `default` → `textures/entity/slime/slime_king` → `Swords_R/textures/entity/slime/slime_king.png`
- geometry `default` → `geometry.slime` → не найдено локально (возможно ванильный ресурс)
- geometry `armor` → `geometry.slime_king.armor` → `Swords_R/models/entity/slime_king_armor.geo.json`
- render controller `controller.render.slime` → не найдено локально (возможно ванильный ресурс)
- render controller `controller.render.slime_armor` → не найдено локально (возможно ванильный ресурс)

### `entity:ultra_instinct_projectile` — `Swords_R/entity/ultra_instinct_projectile.json`

- Полный `description`: `{"identifier":"entity:ultra_instinct_projectile","materials":{"default":"ultra_instinct_projectile"},"textures":{"default":"textures/entity/ultra_instinct_projectile"},"geometry":{"default":"geometry.ultra_instinct_projectile"},"animation_controllers":[{"move":"controller.animation.ultra_instinct_projectile.move"}],"render_controllers":["controller.render.ultra_instinct_projectile"],"animations":{"move":"animation.move"}}`

- texture `default` → `textures/entity/ultra_instinct_projectile` → `Swords_R/textures/entity/ultra_instinct_projectile.png`
- geometry `default` → `geometry.ultra_instinct_projectile` → `Swords_R/models/entity/ultra_instinct_projectile.geo.json`
- animation `move` → `animation.move` → `Swords_R/animations/ultra_instinct_projectile.animation.json`
- render controller `controller.render.ultra_instinct_projectile` → `Swords_R/render_controllers/ultra_instinct_projectile.render_controllers.json`

### `entity:web` — `Swords_R/entity/web.v1.0.json`

- Полный `description`: `{"identifier":"entity:web","materials":{"default":"snowball"},"textures":{"default":"textures/entity/web"},"geometry":{"default":"geometry.item_sprite"},"render_controllers":["controller.render.item_sprite"],"animations":{"flying":"animation.actor.billboard"},"scripts":{"animate":["flying"]}}`

- texture `default` → `textures/entity/web` → `Swords_R/textures/entity/web.png`
- geometry `default` → `geometry.item_sprite` → не найдено локально (возможно ванильный ресурс)
- animation `flying` → `animation.actor.billboard` → не найдено локально (возможно ванильный ресурс)
- render controller `controller.render.item_sprite` → не найдено локально (возможно ванильный ресурс)

### `minecraft:bed` — `Swords_R/entity/bed_sword.entity.json`

- Полный `description`: `{"identifier":"minecraft:bed","textures":{"default":"textures/entity/bed/white","white":"textures/entity/bed/white","orange":"textures/entity/bed/orange","magenta":"textures/entity/bed/magenta","light_blue":"textures/entity/bed/light_blue","yellow":"textures/entity/bed/yellow","lime":"textures/entity/bed/lime","pink":"textures/entity/bed/pink","gray":"textures/entity/bed/gray","silver":"textures/entity/bed/silver","cyan":"textures/entity/bed/cyan","purple":"textures/entity/bed/purple","blue":"textures/entity/bed/blue","brown":"textures/entity/bed/brown","green":"textures/entity/bed/green","red":"textures/entity/bed/red","black":"textures/entity/bed/black"},"geometry":{"default":"geometry.bed"}}`

- texture `default` → `textures/entity/bed/white` → не найдено локально (возможно ванильный ресурс)
- texture `white` → `textures/entity/bed/white` → не найдено локально (возможно ванильный ресурс)
- texture `orange` → `textures/entity/bed/orange` → не найдено локально (возможно ванильный ресурс)
- texture `magenta` → `textures/entity/bed/magenta` → не найдено локально (возможно ванильный ресурс)
- texture `light_blue` → `textures/entity/bed/light_blue` → не найдено локально (возможно ванильный ресурс)
- texture `yellow` → `textures/entity/bed/yellow` → не найдено локально (возможно ванильный ресурс)
- texture `lime` → `textures/entity/bed/lime` → не найдено локально (возможно ванильный ресурс)
- texture `pink` → `textures/entity/bed/pink` → не найдено локально (возможно ванильный ресурс)
- texture `gray` → `textures/entity/bed/gray` → не найдено локально (возможно ванильный ресурс)
- texture `silver` → `textures/entity/bed/silver` → не найдено локально (возможно ванильный ресурс)
- texture `cyan` → `textures/entity/bed/cyan` → не найдено локально (возможно ванильный ресурс)
- texture `purple` → `textures/entity/bed/purple` → не найдено локально (возможно ванильный ресурс)
- texture `blue` → `textures/entity/bed/blue` → не найдено локально (возможно ванильный ресурс)
- texture `brown` → `textures/entity/bed/brown` → не найдено локально (возможно ванильный ресурс)
- texture `green` → `textures/entity/bed/green` → не найдено локально (возможно ванильный ресурс)
- texture `red` → `textures/entity/bed/red` → не найдено локально (возможно ванильный ресурс)
- texture `black` → `textures/entity/bed/black` → не найдено локально (возможно ванильный ресурс)
- geometry `default` → `geometry.bed` → не найдено локально (возможно ванильный ресурс)

### `minecraft:enderman` — `Swords_R/entity/enderman.entity.json`

- Полный `description`: `{"identifier":"minecraft:enderman","min_engine_version":"1.8.0","materials":{"default":"enderman","invisible":"enderman_invisible"},"textures":{"default":"textures/entity/enderman/enderman","red_enderman":"textures/entity/enderman/red_enderman"},"geometry":{"default":"geometry.enderman.v1.8"},"scripts":{"pre_animation":["variable.tcos0 = (Math.cos(query.modified_distance_moved * 38.17) * query.modified_move_speed / variable.gliding_speed_value) * 28.65;"]},"animations":{"look_at_target_default":"animation.humanoid.look_at_target.default","look_at_target_gliding":"animation.humanoid.look_at_target.gliding","look_at_target_swimming":"animation.humanoid.look_at_target.swimming","move":"animation.humanoid.move","attack.rotations":"animation.humanoid.attack.rotations","bob":"animation.humanoid.bob","base_pose":"animation.enderman.base_pose","arms_legs":"animation.enderman.arms_legs","carrying":"animation.enderman.carrying","scary_face":"animation.enderman.scary_face"},"animation_controllers":[{"look_at_target":"controller.animation.humanoid.look_at_target"},{"move":"controller.animation.humanoid.move"},{"attack":"controller.animation.humanoid.attack"},{"bob":"controller.animation.humanoid.bob"},{"base_pose":"controller.animation.enderman.base_pose"},{"carrying":"controller.animation.enderman.carrying"},{"scary_face":"controller.animation.enderman.scary_face"}],"render_controllers":["controller.render.enderman"],"spawn_egg":{"texture":"spawn_egg","texture_index":7}}`

- texture `default` → `textures/entity/enderman/enderman` → `Swords_R/textures/entity/enderman/enderman.tga`
- texture `red_enderman` → `textures/entity/enderman/red_enderman` → `Swords_R/textures/entity/enderman/red_enderman.tga`
- geometry `default` → `geometry.enderman.v1.8` → не найдено локально (возможно ванильный ресурс)
- animation `look_at_target_default` → `animation.humanoid.look_at_target.default` → не найдено локально (возможно ванильный ресурс)
- animation `look_at_target_gliding` → `animation.humanoid.look_at_target.gliding` → не найдено локально (возможно ванильный ресурс)
- animation `look_at_target_swimming` → `animation.humanoid.look_at_target.swimming` → не найдено локально (возможно ванильный ресурс)
- animation `move` → `animation.humanoid.move` → не найдено локально (возможно ванильный ресурс)
- animation `attack.rotations` → `animation.humanoid.attack.rotations` → не найдено локально (возможно ванильный ресурс)
- animation `bob` → `animation.humanoid.bob` → не найдено локально (возможно ванильный ресурс)
- animation `base_pose` → `animation.enderman.base_pose` → не найдено локально (возможно ванильный ресурс)
- animation `arms_legs` → `animation.enderman.arms_legs` → не найдено локально (возможно ванильный ресурс)
- animation `carrying` → `animation.enderman.carrying` → не найдено локально (возможно ванильный ресурс)
- animation `scary_face` → `animation.enderman.scary_face` → не найдено локально (возможно ванильный ресурс)
- render controller `controller.render.enderman` → `Swords_R/render_controllers/enderman.render_controllers.json`

### `minecraft:player` — `Swords_R/entity/player.entity.json`

- Полный `description`: `{"identifier":"minecraft:player","materials":{"default":"entity_alphatest","cape":"entity_alphatest","animated":"player_animated","ultra_instinct_aura":"ultra_instinct_aura","player_ghost":"player_ghost","wolf_vision":"wolf_vision","blaze_aura":"blaze_aura"},"textures":{"default":"textures/entity/steve","cape":"textures/entity/cape_invisible","ultra_instinct_aura":"textures/entity/ultra_instinct_aura","wolf_transformation":"textures/entity/wolf_transformation","wolf_vision":"textures/entity/wolf_vision","ghost":"textures/entity/ghost","mermaid_player":"textures/entity/mermaid_player","blaze_rods":"textures/entity/blaze_rods","blaze_aura":"textures/entity/blaze_rods"},"geometry":{"default":"geometry.humanoid.custom","cape":"geometry.cape","ultra_instinct_aura":"geometry.ultra_instinct_aura","wolf_transformation":"geometry.wolf_transformation","player_ghost":"geometry.player_ghost","wolf_vision":"geometry.wolf_vision","mermaid_player":"geometry.mermaid_player.tail","blaze_rods":"geometry.blaze_rods","blaze_aura":"geometry.blaze_aura"},"scripts":{"scale":"0.9375","initialize":["variable.is_holding_right = 0.0;","variable.is_blinking = 0.0;","variable.last_blink_time = 0.0;","variable.hand_bob = 0.0;"],"pre_animation":["variable.helmet_layer_visible = 1.0;","variable.leg_layer_visible = 1.0;","variable.boot_layer_visible = 1.0;","variable.chest_layer_visible = 1.0;","variable.attack_body_rot_y = Math.sin(360*Math.sqrt(variable.attack_time)) * 5.0;","variable.tcos0 = (math.cos(query.modified_distance_moved * 38.17) * query.modified_move_speed / variable.gliding_speed_value) * 57.3;","variable.first_person_rotation_factor = math.sin((1 - variable.attack_time) * 180.0);","variable.hand_bob = query.life_time < 0.01 ? 0.0 : variable.hand_bob + ((query.is_on_ground && query.is_alive ? math.clamp(math.sqrt(math.pow(query.position_delta(0), 2.0) + math.pow(query.position_delta(2), 2.0)), 0.0, 0.1) : 0.0) - variable.hand_bob) * 0.02;","variable.map_angle = math.clamp(1 - variable.player_x_rotation / 45.1, 0.0, 1.0);","variable.item_use_normalized = query.main_hand_item_use_duration / query.main_hand_item_max_duration;","variable.ultra_instinct_sword = query.get_equipped_item_name('main_hand') == 'ultra_instinct_sword';","variable.wolf_transformation = (!variable.is_first_person && query.get_equipped_item_name('main_hand') == 'wolf_sword' && query.moon_phase == 0 && (query.time_of_day <= 0.20 || query.time_of_day >= 0.80));","variable.wolf_vision = (variable.is_first_person && query.get_equipped_item_name('main_hand') == 'wolf_sword' && query.moon_phase == 0 && (query.time_of_day <= 0.20 || query.time_of_day >= 0.80));","variable.player_ghost = query.get_equipped_item_name('main_hand') == 'ghost_sword';","variable.mermaid_player = !variable.is_first_person && query.get_equipped_item_name('main_hand') == 'sea_sword';","variable.blaze_rods = query.get_equipped_item_name('main_hand') == 'blaze_sword';"],"animate":["root",{"attack.ultra_instinct_sword":"variable.ultra_instinct_sword && variable.attack_body_rot_y"},{"ultra_instinct.move":"variable.ultra_instinct_sword"},{"move.player_ghost":"variable.player_ghost && !variable.is_first_person"},{"vision.player_ghost":"variable.player_ghost && variable.is_first_person"},{"mermaid_player.tail":"variable.mermaid_player && !variable.is_first_person"},{"mermaid_player.swimming":"variable.mermaid_player && query.is_swimming"},{"mermaid_player.drowning":"variable.mermaid_player && !query.is_in_water"},{"mermaid_player.default_pose":"variable.mermaid_player && !query.is_swimming && query.is_in_water"},{"blaze_rods.move":"variable.blaze_rods"}]},"animations":{"blaze_rods.move":"animation.blaze_rods","mermaid_player.default_pose":"animation.mermaid_player.default_pose","mermaid_player.tail":"animation.mermaid_player.tail","mermaid_player.swimming":"animation.mermaid_player.swimming","mermaid_player.drowning":"animation.mermaid_player.drowning","ultra_instinct.move":"animation.ultra_instinct.move","vision.player_ghost":"animation.player_ghost.vision","move.player_ghost":"animation.player_ghost.move","attack.ultra_instinct_sword":"animation.ultra_instinct_sword.attack","root":"controller.animation.player.root","base_controller":"controller.animation.player.base","hudplayer":"controller.animation.player.hudplayer","humanoid_base_pose":"animation.humanoid.base_pose","look_at_target":"controller.animation.humanoid.look_at_target","look_at_target_ui":"animation.player.look_at_target.ui","look_at_target_default":"animation.humanoid.look_at_target.default","look_at_target_gliding":"animation.humanoid.look_at_target.gliding","look_at_target_swimming":"animation.humanoid.look_at_target.swimming","look_at_target_inverted":"animation.player.look_at_target.inverted","cape":"animation.player.cape","move.arms":"animation.player.move.arms","move.legs":"animation.player.move.legs","swimming":"animation.player.swim","swimming.legs":"animation.player.swim.legs","riding.arms":"animation.player.riding.arms","riding.legs":"animation.player.riding.legs","holding":"animation.player.holding","brandish_spear":"animation.humanoid.brandish_spear","charging":"animation.humanoid.charging","attack.positions":"animation.player.attack.positions","attack.rotations":"animation.player.attack.rotations","sneaking":"animation.player.sneaking","bob":"animation.player.bob","damage_nearby_mobs":"animation.humanoid.damage_nearby_mobs","bow_and_arrow":"animation.humanoid.bow_and_arrow","use_item_progress":"animation.humanoid.use_item_progress","skeleton_attack":"animation.skeleton.attack","sleeping":"animation.player.sleeping","first_person_base_pose":"animation.player.first_person.base_pose","first_person_empty_hand":"animation.player.first_person.empty_hand","first_person_swap_item":"animation.player.first_person.swap_item","first_person_attack_controller":"controller.animation.player.first_person_attack","first_person_attack_rotation":"animation.player.first_person.attack_rotation","first_person_attack_rotation_item":"animation.player.first_person.attack_rotation_item","first_person_vr_attack_rotation":"animation.player.first_person.vr_attack_rotation","first_person_walk":"animation.player.first_person.walk","first_person_map_controller":"controller.animation.player.first_person_map","first_person_map_hold":"animation.player.first_person.map_hold","first_person_map_hold_attack":"animation.player.first_person.map_hold_attack","first_person_map_hold_off_hand":"animation.player.first_person.map_hold_off_hand","first_person_map_hold_main_hand":"animation.player.first_person.map_hold_main_hand","first_person_crossbow_equipped":"animation.player.first_person.crossbow_equipped","first_person_crossbow_hold":"animation.player.first_person.crossbow_hold","first_person_breathing_bob":"animation.player.first_person.breathing_bob","third_person_crossbow_equipped":"animation.player.crossbow_equipped","third_person_bow_equipped":"animation.player.bow_equipped","crossbow_hold":"animation.player.crossbow_hold","crossbow_controller":"controller.animation.player.crossbow","shield_block_main_hand":"animation.player.shield_block_main_hand","shield_block_off_hand":"animation.player.shield_block_off_hand","blink":"controller.animation.persona.blink"},"render_controllers":[{"controller.render.player.first_person":"variable.is_first_person"},{"controller.render.player.third_person":"!variable.is_first_person && !variable.map_face_icon"},{"controller.render.player.map":"variable.map_face_icon"},{"controller.render.ultra_instinct_aura":"variable.ultra_instinct_sword"},{"controller.render.wolf_transformation":"variable.wolf_transformation"},{"controller.render.wolf_vision":"variable.wolf_vision"},{"controller.render.player_ghost":"variable.player_ghost"},{"controller.render.mermaid_player":"variable.mermaid_player"},{"controller.render.blaze_rods":"variable.blaze_rods"},{"controller.render.blaze_aura":"variable.blaze_rods && !variable.is_first_person"}],"enable_attachables":true}`

- texture `default` → `textures/entity/steve` → не найдено локально (возможно ванильный ресурс)
- texture `cape` → `textures/entity/cape_invisible` → не найдено локально (возможно ванильный ресурс)
- texture `ultra_instinct_aura` → `textures/entity/ultra_instinct_aura` → `Swords_R/textures/entity/ultra_instinct_aura.png`
- texture `wolf_transformation` → `textures/entity/wolf_transformation` → `Swords_R/textures/entity/wolf_transformation.png`
- texture `wolf_vision` → `textures/entity/wolf_vision` → `Swords_R/textures/entity/wolf_vision.png`
- texture `ghost` → `textures/entity/ghost` → `Swords_R/textures/entity/ghost.png`
- texture `mermaid_player` → `textures/entity/mermaid_player` → `Swords_R/textures/entity/mermaid_player.png`
- texture `blaze_rods` → `textures/entity/blaze_rods` → `Swords_R/textures/entity/blaze_rods.png`
- texture `blaze_aura` → `textures/entity/blaze_rods` → `Swords_R/textures/entity/blaze_rods.png`
- geometry `default` → `geometry.humanoid.custom` → не найдено локально (возможно ванильный ресурс)
- geometry `cape` → `geometry.cape` → не найдено локально (возможно ванильный ресурс)
- geometry `ultra_instinct_aura` → `geometry.ultra_instinct_aura` → `Swords_R/models/entity/ultra_instinct_aura.geo.json`
- geometry `wolf_transformation` → `geometry.wolf_transformation` → `Swords_R/models/entity/wolf_transformation.geo.json`
- geometry `player_ghost` → `geometry.player_ghost` → `Swords_R/models/entity/player_ghost.geo.json`
- geometry `wolf_vision` → `geometry.wolf_vision` → `Swords_R/models/entity/wolf_vision.geo.json`
- geometry `mermaid_player` → `geometry.mermaid_player.tail` → `Swords_R/models/entity/mermaid_player.geo.json`
- geometry `blaze_rods` → `geometry.blaze_rods` → `Swords_R/models/entity/blaze_rods.geo.json`
- geometry `blaze_aura` → `geometry.blaze_aura` → `Swords_R/models/entity/blaze_aura.geo.json`
- animation `blaze_rods.move` → `animation.blaze_rods` → `Swords_R/animations/blaze_rods.animation.json`
- animation `mermaid_player.default_pose` → `animation.mermaid_player.default_pose` → `Swords_R/animations/mermaid_player.animation.json`
- animation `mermaid_player.tail` → `animation.mermaid_player.tail` → `Swords_R/animations/mermaid_player.animation.json`
- animation `mermaid_player.swimming` → `animation.mermaid_player.swimming` → `Swords_R/animations/mermaid_player.animation.json`
- animation `mermaid_player.drowning` → `animation.mermaid_player.drowning` → `Swords_R/animations/mermaid_player.animation.json`
- animation `ultra_instinct.move` → `animation.ultra_instinct.move` → `Swords_R/animations/ultra_instinct_move.animation.json`
- animation `vision.player_ghost` → `animation.player_ghost.vision` → `Swords_R/animations/mobs.animation.json`
- animation `move.player_ghost` → `animation.player_ghost.move` → `Swords_R/animations/mobs.animation.json`
- animation `attack.ultra_instinct_sword` → `animation.ultra_instinct_sword.attack` → `Swords_R/animations/mobs.animation.json`
- animation `root` → `controller.animation.player.root` → не найдено локально (возможно ванильный ресурс)
- animation `base_controller` → `controller.animation.player.base` → не найдено локально (возможно ванильный ресурс)
- animation `hudplayer` → `controller.animation.player.hudplayer` → не найдено локально (возможно ванильный ресурс)
- animation `humanoid_base_pose` → `animation.humanoid.base_pose` → не найдено локально (возможно ванильный ресурс)
- animation `look_at_target` → `controller.animation.humanoid.look_at_target` → не найдено локально (возможно ванильный ресурс)
- animation `look_at_target_ui` → `animation.player.look_at_target.ui` → не найдено локально (возможно ванильный ресурс)
- animation `look_at_target_default` → `animation.humanoid.look_at_target.default` → не найдено локально (возможно ванильный ресурс)
- animation `look_at_target_gliding` → `animation.humanoid.look_at_target.gliding` → не найдено локально (возможно ванильный ресурс)
- animation `look_at_target_swimming` → `animation.humanoid.look_at_target.swimming` → не найдено локально (возможно ванильный ресурс)
- animation `look_at_target_inverted` → `animation.player.look_at_target.inverted` → не найдено локально (возможно ванильный ресурс)
- animation `cape` → `animation.player.cape` → не найдено локально (возможно ванильный ресурс)
- animation `move.arms` → `animation.player.move.arms` → не найдено локально (возможно ванильный ресурс)
- animation `move.legs` → `animation.player.move.legs` → не найдено локально (возможно ванильный ресурс)
- animation `swimming` → `animation.player.swim` → не найдено локально (возможно ванильный ресурс)
- animation `swimming.legs` → `animation.player.swim.legs` → не найдено локально (возможно ванильный ресурс)
- animation `riding.arms` → `animation.player.riding.arms` → не найдено локально (возможно ванильный ресурс)
- animation `riding.legs` → `animation.player.riding.legs` → не найдено локально (возможно ванильный ресурс)
- animation `holding` → `animation.player.holding` → не найдено локально (возможно ванильный ресурс)
- animation `brandish_spear` → `animation.humanoid.brandish_spear` → не найдено локально (возможно ванильный ресурс)
- animation `charging` → `animation.humanoid.charging` → не найдено локально (возможно ванильный ресурс)
- animation `attack.positions` → `animation.player.attack.positions` → не найдено локально (возможно ванильный ресурс)
- animation `attack.rotations` → `animation.player.attack.rotations` → не найдено локально (возможно ванильный ресурс)
- animation `sneaking` → `animation.player.sneaking` → не найдено локально (возможно ванильный ресурс)
- animation `bob` → `animation.player.bob` → не найдено локально (возможно ванильный ресурс)
- animation `damage_nearby_mobs` → `animation.humanoid.damage_nearby_mobs` → не найдено локально (возможно ванильный ресурс)
- animation `bow_and_arrow` → `animation.humanoid.bow_and_arrow` → не найдено локально (возможно ванильный ресурс)
- animation `use_item_progress` → `animation.humanoid.use_item_progress` → не найдено локально (возможно ванильный ресурс)
- animation `skeleton_attack` → `animation.skeleton.attack` → не найдено локально (возможно ванильный ресурс)
- animation `sleeping` → `animation.player.sleeping` → не найдено локально (возможно ванильный ресурс)
- animation `first_person_base_pose` → `animation.player.first_person.base_pose` → не найдено локально (возможно ванильный ресурс)
- animation `first_person_empty_hand` → `animation.player.first_person.empty_hand` → не найдено локально (возможно ванильный ресурс)
- animation `first_person_swap_item` → `animation.player.first_person.swap_item` → не найдено локально (возможно ванильный ресурс)
- animation `first_person_attack_controller` → `controller.animation.player.first_person_attack` → не найдено локально (возможно ванильный ресурс)
- animation `first_person_attack_rotation` → `animation.player.first_person.attack_rotation` → не найдено локально (возможно ванильный ресурс)
- animation `first_person_attack_rotation_item` → `animation.player.first_person.attack_rotation_item` → не найдено локально (возможно ванильный ресурс)
- animation `first_person_vr_attack_rotation` → `animation.player.first_person.vr_attack_rotation` → не найдено локально (возможно ванильный ресурс)
- animation `first_person_walk` → `animation.player.first_person.walk` → не найдено локально (возможно ванильный ресурс)
- animation `first_person_map_controller` → `controller.animation.player.first_person_map` → не найдено локально (возможно ванильный ресурс)
- animation `first_person_map_hold` → `animation.player.first_person.map_hold` → не найдено локально (возможно ванильный ресурс)
- animation `first_person_map_hold_attack` → `animation.player.first_person.map_hold_attack` → не найдено локально (возможно ванильный ресурс)
- animation `first_person_map_hold_off_hand` → `animation.player.first_person.map_hold_off_hand` → не найдено локально (возможно ванильный ресурс)
- animation `first_person_map_hold_main_hand` → `animation.player.first_person.map_hold_main_hand` → не найдено локально (возможно ванильный ресурс)
- animation `first_person_crossbow_equipped` → `animation.player.first_person.crossbow_equipped` → не найдено локально (возможно ванильный ресурс)
- animation `first_person_crossbow_hold` → `animation.player.first_person.crossbow_hold` → не найдено локально (возможно ванильный ресурс)
- animation `first_person_breathing_bob` → `animation.player.first_person.breathing_bob` → не найдено локально (возможно ванильный ресурс)
- animation `third_person_crossbow_equipped` → `animation.player.crossbow_equipped` → не найдено локально (возможно ванильный ресурс)
- animation `third_person_bow_equipped` → `animation.player.bow_equipped` → не найдено локально (возможно ванильный ресурс)
- animation `crossbow_hold` → `animation.player.crossbow_hold` → не найдено локально (возможно ванильный ресурс)
- animation `crossbow_controller` → `controller.animation.player.crossbow` → не найдено локально (возможно ванильный ресурс)
- animation `shield_block_main_hand` → `animation.player.shield_block_main_hand` → не найдено локально (возможно ванильный ресурс)
- animation `shield_block_off_hand` → `animation.player.shield_block_off_hand` → не найдено локально (возможно ванильный ресурс)
- animation `blink` → `controller.animation.persona.blink` → не найдено локально (возможно ванильный ресурс)
- render controller `controller.render.player.first_person` → не найдено локально (возможно ванильный ресурс)
- render controller `controller.render.player.third_person` → не найдено локально (возможно ванильный ресурс)
- render controller `controller.render.player.map` → не найдено локально (возможно ванильный ресурс)
- render controller `controller.render.ultra_instinct_aura` → `Swords_R/render_controllers/ultra_instinct_aura.render_controllers.json`
- render controller `controller.render.wolf_transformation` → `Swords_R/render_controllers/wolf_transformation.render_controllers.json`
- render controller `controller.render.wolf_vision` → `Swords_R/render_controllers/wolf_vision.render_controllers.json`
- render controller `controller.render.player_ghost` → `Swords_R/render_controllers/player_ghost.render_controllers.json`
- render controller `controller.render.mermaid_player` → `Swords_R/render_controllers/mermaid_player.render_controllers.json`
- render controller `controller.render.blaze_rods` → `Swords_R/render_controllers/blaze_rods.render_controllers.json`
- render controller `controller.render.blaze_aura` → `Swords_R/render_controllers/blaze_aura.render_controllers.json`

### `minecraft:witch` — `Swords_R/entity/witch.entity.json`

- Полный `description`: `{"identifier":"minecraft:witch","min_engine_version":"1.8.0","materials":{"default":"witch"},"textures":{"default":"textures/entity/witch","grass_witch":"textures/entity/grass_witch"},"geometry":{"default":"geometry.villager.witch.v1.8"},"scripts":{"scale":"0.9375"},"animations":{"villager_general":"animation.villager.general","look_at_target":"animation.common.look_at_target","move":"animation.villager.move","general":"animation.witch.general"},"animation_controllers":[{"general":"controller.animation.witch.general"},{"move":"controller.animation.villager.move"}],"render_controllers":["controller.render.witch"],"spawn_egg":{"texture":"spawn_egg","texture_index":17}}`

- texture `default` → `textures/entity/witch` → не найдено локально (возможно ванильный ресурс)
- texture `grass_witch` → `textures/entity/grass_witch` → `Swords_R/textures/entity/grass_witch.png`
- geometry `default` → `geometry.villager.witch.v1.8` → не найдено локально (возможно ванильный ресурс)
- animation `villager_general` → `animation.villager.general` → не найдено локально (возможно ванильный ресурс)
- animation `look_at_target` → `animation.common.look_at_target` → не найдено локально (возможно ванильный ресурс)
- animation `move` → `animation.villager.move` → не найдено локально (возможно ванильный ресурс)
- animation `general` → `animation.witch.general` → не найдено локально (возможно ванильный ресурс)
- render controller `controller.render.witch` → `Swords_R/render_controllers/witch.render_controllers.json`

### `minecraft:witch` — `Swords_R/entity/witch.v1.0.entity.json`

- Полный `description`: `{"identifier":"minecraft:witch","materials":{"default":"witch"},"textures":{"default":"textures/entity/witch","grass_witch":"textures/entity/grass_witch"},"geometry":{"default":"geometry.villager.witch"},"scripts":{"scale":"0.9375"},"animations":{"villager_general":"animation.villager.general.v1.0","look_at_target":"animation.common.look_at_target","move":"animation.villager.move","general":"animation.witch.general"},"animation_controllers":[{"general":"controller.animation.witch.general"},{"move":"controller.animation.villager.move"}],"render_controllers":["controller.render.witch.v1.0"],"spawn_egg":{"texture":"spawn_egg","texture_index":17}}`

- texture `default` → `textures/entity/witch` → не найдено локально (возможно ванильный ресурс)
- texture `grass_witch` → `textures/entity/grass_witch` → `Swords_R/textures/entity/grass_witch.png`
- geometry `default` → `geometry.villager.witch` → не найдено локально (возможно ванильный ресурс)
- animation `villager_general` → `animation.villager.general.v1.0` → не найдено локально (возможно ванильный ресурс)
- animation `look_at_target` → `animation.common.look_at_target` → не найдено локально (возможно ванильный ресурс)
- animation `move` → `animation.villager.move` → не найдено локально (возможно ванильный ресурс)
- animation `general` → `animation.witch.general` → не найдено локально (возможно ванильный ресурс)
- render controller `controller.render.witch.v1.0` → `Swords_R/render_controllers/witch.render_controllers.json`

## Объявления звуков и текстуры flipbook

### `Swords_R/sounds.json`

```json
{
  "entity_sounds": {
    "entities": {
      "entity:mountable_slime": {
        "volume": 1.0,
        "pitch": [
          0.8,
          1.2
        ],
        "events": {
          "ambient": "",
          "hurt": "mob.slime.small",
          "death": "mob.slime.small",
          "squish.big": {
            "sound": "mob.slime.big",
            "pitch": [
              0.64,
              0.96
            ]
          },
          "squish.small": {
            "sound": "mob.slime.small",
            "pitch": [
              0.64,
              0.96
            ]
          },
          "attack": {
            "sound": "mob.attack",
            "pitch": [
              0.8,
              1.2
            ]
          }
        }
      },
      "entity:centella": {
        "volume": 1.0,
        "events": {
          "ambient": {
            "sound": "mob.wither.spawn",
            "pitch": 0.6
          },
          "hurt": "",
          "death": ""
        }
      },
      "entity:alpha_wolf": {
        "volume": 1.0,
        "events": {
          "ambient": {
            "sound": "mob.wolf.growl",
            "volume": 1,
            "pitch": 0.9
          },
          "hurt": {
            "sound": "mob.wolf.bark",
            "volume": 1,
            "pitch": 0.7
          },
          "death": "",
          "step": {
            "sound": "mob.wolf.step",
            "volume": 0.65,
            "pitch": 0.8
          },
          "shake": {
            "sound": "mob.wolf.shake",
            "pitch": [
              0.8,
              1.2
            ]
          },
          "growl": "mob.wolf.growl"
        }
      },
      "entity:slime_king": {
        "volume": 1.0,
        "pitch": [
          0.8,
          1.0
        ],
        "events": {
          "ambient": "",
          "hurt": "mob.slime.small",
          "death": "mob.slime.small",
          "squish.big": {
            "sound": "mob.slime.big",
            "pitch": [
              0.64,
              0.96
            ]
          },
          "squish.small": {
            "sound": "mob.slime.big",
            "pitch": [
              0.64,
              0.96
            ]
          },
          "attack": {
            "sound": "mob.attack",
            "pitch": [
              0.8,
              1.2
            ]
          }
        }
      }
    }
  }
}
```

### `Swords_R/sounds/sound_definitions.json`

```json
{
  "format_version": "1.14.0",
  "sound_definitions": {
    "wolf_sword.howl": {
      "category": "neutral",
      "min_distance": 32.0,
      "sounds": [
        "sounds/wolf_sword/howl"
      ]
    },
    "wolf_sword.distant_howl": {
      "category": "neutral",
      "min_distance": 100.0,
      "sounds": [
        "sounds/wolf_sword/distant_howl"
      ]
    },
    "ghost_sword.wailing": {
      "category": "neutral",
      "min_distance": 60.0,
      "sounds": [
        "sounds/ghost_sword/wailing"
      ]
    }
  }
}
```

### `Swords_R/textures/flipbook_textures.json`

```json
[
  {
    "flipbook_texture": "textures/blocks/quartz_diamond_block",
    "atlas_tile": "quartz_diamond_block",
    "ticks_per_frame": 2,
    "frames": [
      0,
      1,
      2,
      3,
      4,
      5,
      6,
      7
    ],
    "blend_frames": false
  }
]
```

