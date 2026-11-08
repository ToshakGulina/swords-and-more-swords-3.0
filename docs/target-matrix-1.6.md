# Целевые типы четырёх контроллеров 1.6

Воспроизводимое буквальное сравнение команд из Wither (`wither` state), Creeper (`default`), Ender (`default`) и TNT (`default`). Цифра — позиция команды в списке `on_entry`, начиная с 1; «—» означает отсутствие среди команд именно этого вида, а не полную неуязвимость типа или отсутствие других эффектов. Условия/radius/центры отличаются; таблица не доказывает работу селекторов, совместимость ID или фактическое исполнение.

- Wither: `@e[scores={w=100},r=16,type=…]` → `summon entity:explode`; default содержит только `/Effect99`.
- Creeper: `@e[scores={c=100},r=16,type=…]` → `summon entity:explode`.
- Ender: `execute @p` → `spreadplayers ~ ~ 8 16 @e[r=10,rm=5,type=…]`; у этих 27 команд нет score-фильтра.
- TNT: `@e[r=15,rm=10,type=…]` → `summon entity:explode`, без score-фильтра.

Число отдельных команд/типов: Wither 28, Creeper 27, Ender 27, TNT 26. Позиции и порядок — по исходному JSON; полные команды и другие состояния: [реестр контроллеров](animation-ledger-1.6.md), [ручной разбор](manual-area-targets-1.6.md).

| Буквальный type | Wither | Creeper | Ender | TNT |
|---|---:|---:|---:|---:|
| `zombie` | 17 | 4 | 13 | 1 |
| `husk` | 18 | 5 | 14 | 2 |
| `drowned` | 19 | 6 | 15 | 3 |
| `creeper` | 20 | — | 16 | 4 |
| `enderman` | 21 | 7 | 17 | 5 |
| `slime` | 22 | 8 | 18 | 6 |
| `skeleton` | 23 | 9 | 19 | 7 |
| `stray` | 24 | 10 | 20 | 8 |
| `blaze` | 25 | 11 | 21 | 9 |
| `wither_skeleton` | 26 | 12 | 22 | 10 |
| `witch` | 27 | 13 | 23 | 11 |
| `magma_cube` | 28 | 14 | 24 | 12 |
| `ghast` | 29 | 15 | 25 | 13 |
| `zombie_pigman` | 30 | 16 | 26 | 14 |
| `spider` | 31 | 17 | 27 | 15 |
| `cave_spider` | 32 | 18 | 28 | 16 |
| `silverfish` | 33 | 19 | 29 | 17 |
| `evocation_fang` | 34 | 20 | 30 | 18 |
| `evocation_illager` | 35 | 21 | 31 | 19 |
| `vex` | 36 | 22 | 32 | 20 |
| `ravager` | 37 | 23 | 33 | 21 |
| `endermite` | 38 | 24 | 34 | 22 |
| `guardian` | 39 | 25 | 35 | 23 |
| `vindicator` | 40 | 26 | 36 | 24 |
| `phantom` | 41 | 27 | 37 | 25 |
| `tnt` | 42 | 28 | 38 | — |
| `zombie_villager` | 43 | 29 | 39 | 26 |
| `wither` | 44 | 30 | — | — |
