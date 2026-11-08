#!/usr/bin/env python3
"""Navigational coverage list, not a claim of complete manual analysis."""
from pathlib import Path
from build_quick_reference import read_items,legacy_manual_anchor,slug
ROOT=Path(__file__).resolve().parents[1]
EXTRAS={
 'ice_sword':[('Ice: геометрия','manual-ice-1.6.md')],
 'lightning_sword':[('Lightning: цели','manual-lightning-1.6.md')],
 'sea_sword':[('Sea: группы','manual-sea-sword.md')],
 'jungle_sword':[('Jungle: лоза','manual-jungle-vines.md')],
 'grass_sword':[('Grass: теги','manual-grass-sword.md')],
 'fire_sword':[('Fire/Magma/Spider','manual-fire-magma-spider-1.6.md')],
 'magma_sword':[('Fire/Magma/Spider','manual-fire-magma-spider-1.6.md')],
 'spider_sword':[('Fire/Magma/Spider','manual-fire-magma-spider-1.6.md')],
 'spectral_sword':[('помощники и мир','manual-world-helpers-1.6.md')],
 'glowstone_sword':[('помощники и мир','manual-world-helpers-1.6.md')],
 'sponge_sword':[('помощники и мир','manual-world-helpers-1.6.md')],
 'obsidian_sword':[('помощники и мир','manual-world-helpers-1.6.md')],
 'coal_sword':[('помощники и мир','manual-world-helpers-1.6.md')],
 'blaze_sword':[('счётчики и помощники','manual-counter-helpers-1.6.md')],
 'bone_sword':[('счётчики и помощники','manual-counter-helpers-1.6.md')],
 'shulker_sword':[('счётчики и помощники','manual-counter-helpers-1.6.md')],
 'slime_sword':[('счётчики и помощники','manual-counter-helpers-1.6.md')],
 'lapis_sword':[('счётчики и помощники','manual-counter-helpers-1.6.md')],
 'ender_sword':[('селекторы и взрывы','manual-area-targets-1.6.md')],
 'wither_sword':[('селекторы и взрывы','manual-area-targets-1.6.md')],
 'creeper_sword':[('селекторы и взрывы','manual-area-targets-1.6.md'),('сравнение с 2.x','manual-creeper-sword.md')],
 'tnt_sword':[('селекторы и взрывы','manual-area-targets-1.6.md')],
 'sword_of_time':[('глобальные сбросы','manual-global-state-1.6.md')],
}

# Дополнительные сравнительные карточки: ссылки дополняют исходные трассы.
for keys, path in [
    (('coal','cactus','emerald','lapis'), 'manual-basic-swords.md'),
    (('obsidian','magma','glowstone'), 'manual-heat-light-swords.md'),
    (('blaze','bone','shulker'), 'manual-companion-projectile-swords.md'),
    (('ender','wither','tnt','slime'), 'manual-ender-wither-tnt-slime.md'),
    (('fire','spider'), 'manual-fire-spider-sponge.md'),
]:
    for name in keys:
        EXTRAS.setdefault(name+'_sword', []).append(('сравнение 1.6/2.x', path+'#'+slug(name.title()+' Sword')))

EXTRAS.setdefault('sponge_sword', []).append(('сравнение 1.6/2.x', 'manual-fire-spider-sponge.md#'+slug('Sponge Sword и Wet Sponge Sword')))
EXTRAS.setdefault('spectral_sword', []).append(('сравнение 1.6/2.x', 'manual-spectral-time-comparison.md#spectral-sword'))
EXTRAS.setdefault('sword_of_time', []).append(('мечи времени', 'manual-spectral-time-comparison.md#sword-of-time-16'))
EXTRAS.setdefault('quartz_sword', []).append(('Quartz 1.6/2.x', 'manual-quartz-bedrock-progression.md#'+slug('Quartz Sword: одинаковый ID, разные рецепты и побочные эффекты')))

def build():
    items=read_items('SwordsAndMoreSwords.1.6.mcaddon','Sword_B')
    if len(items)!=26:raise ValueError('unexpected 1.6 item count')
    out=['# Покрытие предметов 1.6: указатель частичных цепочек', '',
         'Все 26 точных item ID из `Sword_B/items/` имеют первичную ручную цепочку, но **ни один не считается завершённым**: компоновка, неявные/ванильные ресурсы и поведение в игре не проверены. Более подробная отдельная ссылка указывает лишь направление дальнейшего анализа, а не сертификат полного покрытия. Для 2.8.14 — [отдельная таблица](coverage-2.8.14.md).', '',
         '«Цепочка» — машинно обнаруженные прямые sensor/spawn/animation-связи; не гарантирует отсутствие косвенных связей. «Данные» и «получение» — буквальные выписки. Версии и имена не отождествляются автоматически, особенно `effect:sword_of_time` и `effect:time_sword`.', '',
         '| Точный ID | Ручное чтение | Дополнительные тематические документы | Цепочка / получение / данные |', '|---|---|---|---|']
    for ident in sorted(items):
        key=ident.split(':',1)[1];anchor=legacy_manual_anchor(ident);suffix=slug(ident)
        extras=' · '.join(f'[{label}]({path})' for label,path in EXTRAS.get(key,[])) or '—'
        for _,path in EXTRAS.get(key,[]):
            if not (ROOT/'docs'/path.split('#',1)[0]).is_file():raise ValueError('missing document '+path)
        out.append(f'| `{ident}` | [частично](manual-traces-1.6.md#{anchor}) | {extras} | [цепочка](chain-index-1.6.md#{suffix}) · [получение](acquisition-index-1.6.md#{suffix}) · [данные](items-1.6.md#{suffix}) |')
    return '\n'.join(out)+'\n'

def main():
    (ROOT/'docs/coverage-1.6.md').write_text(build(),encoding='utf-8');print('legacy coverage navigation written')
if __name__=='__main__':main()
