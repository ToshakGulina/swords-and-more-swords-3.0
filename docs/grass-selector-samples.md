# Grass Sword: условное пересечение селекторов 2.x

Это таблица **только текстовых type/family/tag-фильтров**, не эмуляция Bedrock и не доказательство действия на сущность. Для P/W/T предполагается отсутствие тега `grass`, для C/R/Q — его наличие; S от тега не зависит. Каждая колонка рассматривается отдельно при удовлетворении своего радиуса, а для P/W/C ещё и двух detect. `c=1` и выбор одной цели не моделируются: «да» означает возможность пройти только показанные тип/family/tag, не гарантию выбора, спавна, телепорта или эффекта. Имена type и соответствие runtime/vanilla нужно испытать в игре. Семейства строк ниже — гипотетические состояния; одновременное существование групп и смена состояний не установлены. [Пошаговый разбор](manual-grass-sword.md).

| Стадия | Исходный selector | Проверяемый тег |
|---|---|---|
| P: поиск игрока | `@e[type=!player,type=!item,type=!entity:grass,type=!xp_orb,type=!arrow,r=8,tag=!grass]` | нет |
| W: поиск ведьмы | `@e[family=!grass_witch,type=!item,type=!entity:grass,type=!xp_orb,type=!arrow,r=8,tag=!grass,family=!shulker_sword]` | нет |
| T: назначение тега | `@e[family=!grass_witch,type=!entity:grass,type=!xp_orb,type=!arrow,r=1,tag=!grass]` | нет |
| S: slowness | `@e[type=!entity:grass,r=1]` | без ограничения |
| C: выбор с tag | `@e[type=!entity:grass,c=1,r=1,tag=grass]` | есть |
| R: снять r=2 | `@e[tag=grass,r=2]` | есть |
| Q: снять rm=9/r=10 | `@e[tag=grass,rm=9,r=10]` | есть |

| Пример: type и предполагаемые families | P | W | T | S | C | R | Q |
|---|---|---|---|---|---|---|---|
| Обычный игрок: `player`, families `player,default_player` | нет | да | да | да | да | да | да |
| Игрок в полной Wolf-группе: `player`, families `wolf,wolf_sword,complete_wolf_transformation,monster` | нет | да | да | да | да | да | да |
| Shulker shield: `entity:shulker_shield`, families `effect99_entities,player,shulker_sword` | да | нет | да | да | да | да | да |
| Grass Witch: `witch`, families `witch,monster,mob,grass_witch` | да | нет | нет | да | да | да | да |
| Зомби: пример без спецсемей: `zombie`, families `monster` | да | да | да | да | да | да | да |
| Предмет: пример без спецсемей: `item`, без специальных families | нет | нет | да | да | да | да | да |
| Стрела: пример без спецсемей: `arrow`, без специальных families | нет | нет | нет | да | да | да | да |
| Grass helper: `entity:grass`, families `effect99_entities` | нет | нет | нет | нет | нет | да | да |
