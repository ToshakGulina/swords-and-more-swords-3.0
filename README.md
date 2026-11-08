# Swords and more swords 3.0 — исследование исходного аддона

**Актуальная точка входа:** [основа подготовки](docs/remake-working-basis-ru.md), [план разработки](docs/remake-full-development-plan-ru.md), [памятка](docs/remake-master-brief-ru.md) и [проверка документации](docs/remake-preparation-audit-ru.md). Ремейк не начат; разрешение пользователя необходимо отдельно.

**Важно:** по решению пользователя версия 2.8.14 не используется как источник. Далее сохранены исторические исследования и старые инструкции; некоторые старые генераторы и тесты могут обращаться к 2.8.14. Не запускать их или полный `unittest discover` без предварительной проверки зависимостей. Профильные проверки актуальной подготовки перечислены в отчёте.

Начните с [подробной памятки по каждому предмету](docs/detailed-item-guide-ru.md); есть также [краткий обзор](docs/guide-ru.md). Для проверки источников — [пофайловая повторная проверка и её границы](docs/file-review-status.md), [краткого указателя предметов](docs/quick-reference.md), [сводки статического аудита](docs/static-audit-summary.md) и [статуса анализа](docs/analysis-status.md). Ремейк ещё не реализован; автоматические выписки предметов — не завершённый ручной аудит. [Разбор серверных контейнеров и его ограничения](docs/server-archive.md) · [сравнение player с серверными определениями](docs/server-player-comparison.md).

[Сравнение ванильных ID с двумя официальными образцами Mojang](docs/manual-vanilla-override-review.md): игрок и 22 сущности 2.x, границы выводов и воспроизведение. [Вложенные различия остальных 16 сущностей](docs/manual-vanilla-entities-2.8.md) и [полная выписка](docs/vanilla-entity-detail-ledger.md).

[Ванильная добыча и таблицы аддона](docs/manual-vanilla-loot-2.8.md): сравнение всех 60 путей, потерянные относительно образцов записи и условия мечей.

[Клиентские ресурсы против официальных образцов](docs/manual-vanilla-resources.md): совпадения путей, атласы, UI и клиентские сущности без предположений о слиянии пакетов.

Ручные межверсионные карточки: [Coal/Cactus/Emerald/Lapis/Glass](docs/manual-basic-swords.md), [Obsidian/Magma/Glowstone/Wither Skeleton](docs/manual-heat-light-swords.md), [Blaze/Bone/Shulker](docs/manual-companion-projectile-swords.md), [Ender/Wither/TNT/Slime](docs/manual-ender-wither-tnt-slime.md), [Quartz/Bedrock](docs/manual-quartz-bedrock-progression.md), [Fire/Spider/Sponge](docs/manual-fire-spider-sponge.md), [Spectral/Time](docs/manual-spectral-time-comparison.md), [Ghost/Nether Star/Ultra](docs/manual-ghost-nether-ultra.md), [Silver/Wolf](docs/manual-silver-wolf-path.md). Это статическое чтение, не проверка в игре.

Исходные архивы из пользовательской папки Google Диска сохранены без изменений в `sources/`. Чтобы воспроизвести инвентаризацию и карточки:

```sh
python -m pip install json5==0.17.3 nbtlib==2.0.4 Pillow==11.3.0 mutagen==1.47.0
python tools/build_dossiers.py
python tools/build_mechanics.py
python tools/build_entities.py
python tools/build_world_ledger.py
python tools/build_structures.py
python tools/build_version_comparison.py
python tools/build_assets.py
python tools/build_literal_references.py
python tools/build_animation_ledger.py
python tools/build_resource_graph.py
python tools/build_client_animation_index.py
python tools/build_client_geometry_index.py
python tools/build_client_effects_ledger.py
python tools/build_acquisition_index.py
python tools/build_quick_reference.py
python tools/build_randomize_index.py
python tools/build_loot_context.py
python tools/build_loot_selection_model.py
python tools/build_player_group_index.py
python tools/build_player_sensor_index.py
python tools/build_entity_group_index.py
python tools/build_entity_combat_index.py
python tools/build_entity_trigger_index.py
python tools/build_entity_event_index.py
python tools/build_spawn_shoot_index.py
python tools/build_projectile_component_index.py
python tools/build_command_risk_index.py
python tools/build_effect_index.py
python tools/build_scoreboard_index.py
python tools/build_command_entity_calls.py
python tools/build_function_ledger.py
python tools/build_world_command_index.py
python tools/build_screenshot_stats.py
python tools/build_sound_audit.py
python tools/build_legacy_target_matrix.py
python tools/build_wolf_conditions.py
python tools/build_digger_index.py
python tools/build_definition_audit.py
python tools/build_icon_comparison.py
python tools/build_item_version_matrix.py
python tools/build_item_repair_index.py
python tools/build_item_visual_index.py
python tools/build_ui_localization.py
python tools/build_ui_stats.py
python tools/build_ice_geometry.py
python tools/build_legacy_ice_matrix.py
python tools/build_lightning_patterns.py
python tools/build_legacy_fire_web_matrix.py
python tools/build_jungle_vine_index.py
python tools/build_grass_selector_samples.py
python tools/build_weapon_event_index.py
python tools/build_on_use_index.py
python tools/build_coverage_legacy.py
python -m unittest discover -s tests -v
```

Тесты проверяют также локальные inline-ссылки на Markdown-файлы и найденные фрагменты заголовков в `docs/`. Эта ограниченная проверка не охватывает все формы Markdown, внешние ссылки или поведение в игре.

Генератор читает архивы как ZIP и переписывает только сгенерированные файлы `docs/inventory-*.md`, `docs/items-*.md`, `docs/version-diff.md`, `docs/mechanics-*.md`, `docs/entity-ledger-*.md` и `docs/world-ledger-*.md`, `docs/structures-{2.8.8,2.8.14}.md`, `docs/assets-*.md`, `docs/version-lines-*.md`, `docs/literal-references-*.md`, `docs/animation-ledger-*.md` и `docs/chain-index-1.6.md`, `docs/resource-graph-*.md`, `docs/client-animation-index.md`, `docs/client-geometry-index.md`, `docs/client-effects-ledger.md` и `docs/acquisition-index-*.md`, `docs/quick-reference.md`, `docs/randomize-index.md`, `docs/loot-context.md`, `docs/loot-selection-model.md`, `docs/player-groups-*.md`, `docs/player-sensor-index.md`, `docs/screenshot-stat-comparison.md`, `docs/sound-index-*.md`, `docs/target-matrix-1.6.md`, `docs/wolf-condition-samples-2.8.md`, `docs/digger-index.md`, `docs/definition-audit.md`, `docs/icon-comparison.md`, `docs/item-version-matrix.md`, `docs/item-repair-index.md`, `docs/item-visual-index.md`, `docs/ui-localization-index.md`, `docs/ui-stat-comparison.md`, `docs/localization-source-index.md`, `docs/ice-geometry-index.md`, `docs/ice-target-matrix-1.6.md`, `docs/lightning-patterns.md`, `docs/fire-web-targets-1.6.md`, `docs/jungle-vine-index.md`, `docs/grass-selector-samples.md`, `docs/weapon-event-index.md`, `docs/on-use-index.md`, `docs/coverage-1.6.md`, `docs/entity-groups-1.6.md`, `docs/entity-groups-2.x.md`, `docs/entity-combat-index-{1.6,2.x}.md`, `docs/entity-trigger-index-{1.6,2.x}.md`, `docs/entity-event-fields-1.6.md`, `docs/entity-event-fields-2.x.md`, `docs/spawn-shoot-index-1.6.md`, `docs/spawn-shoot-index-2.x.md`, `docs/projectile-component-index.md`, `docs/command-risk-index-{1.6,2.8.8,2.8.14}.md`, `docs/effect-index-{1.6,2.x}.md`, `docs/scoreboard-index-{1.6,2.x}.md`, `docs/command-entity-calls-{1.6,2.x}.md`, `docs/function-ledger-{1.6,2.x}.md`, `docs/world-command-index-{1.6,2.8.8,2.8.14}.md`. Исходные вручную сверенные цифры скриншотов хранятся в `data/screenshot-stat-evidence.json` и генератором не меняются. [Проверка отдельных условий случайного выбора](docs/manual-randomize-conditions.md) редактируется вручную. Контрольный список `docs/coverage-2.8.14.md` обновляется вручную по мере анализа.

[Сопоставление характеристик с кодом](docs/screenshot-stat-comparison.md) и [выбранные визуально проверенные утверждения скриншотов](docs/screenshot-visual-review.md) и их противоречия с кодом вынесены отдельно. Индекс [OCR скриншотов](docs/screenshot-ocr.md) сгенерирован отдельно: `python -m pip install rapidocr-onnxruntime==1.4.4 opencv-python-headless==5.0.0.93` и `python tools/transcribe_screenshots.py <папка_скриншотов>`. Оригинальные JPEG должны быть скачаны из указанной в статусе папки Google Диска; OCR не заменяет визуальную проверку.

Тест оригинального скрипта Cursed Pumpkin на имитациях использует Node.js; при его отсутствии тест пропускается. Он не запускает Minecraft.
