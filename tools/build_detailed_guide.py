#!/usr/bin/env python3
"""Assemble an offline, item-by-item Russian guide from audited sources and literal item data.

The generated guide combines static analysis with explicitly labeled selected tests. It preserves all
item components/events and selected detailed cross-file reviews, not all bytes in the packs.
"""
from collections import defaultdict
import argparse
import json
import re
from pathlib import Path
from zipfile import ZipFile
import json5
from build_quick_reference import VERSIONS,read_items,manual_links,legacy_manual_anchor,slug

ROOT=Path(__file__).resolve().parents[1]
DOCS=ROOT/'docs'

# A second, focused analysis, alongside the original 2.x trace for each ID.
# Whole single-subject reviews are retained where the details are distributed across sections.
DEEP={
 'bee_sword':('manual-bee-sword.md',None),
 'ice_sword':('manual-ice-geometry-2.8.md',None),
 'jungle_sword':('manual-jungle-vines.md',None),
 'sea_sword':('manual-sea-sword.md',None),
 'grass_sword':('manual-grass-sword.md',None),
 'creeper_sword':('manual-creeper-sword.md',None),
 'lightning_sword':('manual-lightning-1.6.md',None),
 'cursed_pumpkin_sword':('manual-pumpkin-script-2.8.md',None),
 'wolf_sword':('manual-wolf-conditions-2.8.md',None),
 'silver_ingot':('manual-silver-wolf-path.md','Руда, слиток и меч'),
 'silver_sword':('manual-silver-wolf-path.md','Alpha Wolf и получение Wolf Sword'),
 'slime_sword':('manual-ender-wither-tnt-slime.md','Slime Sword'),
 'sponge_sword':('manual-fire-spider-sponge.md','Sponge Sword и Wet Sponge Sword'),
 'wet_sponge_sword':('manual-fire-spider-sponge.md','Sponge Sword и Wet Sponge Sword'),
 'fire_sword':('manual-fire-spider-sponge.md','Fire Sword'),
 'spider_sword':('manual-fire-spider-sponge.md','Spider Sword'),
 'ender_sword':('manual-ender-wither-tnt-slime.md','Ender Sword'),
 'wither_sword':('manual-ender-wither-tnt-slime.md','Wither Sword'),
 'tnt_sword':('manual-ender-wither-tnt-slime.md','TNT Sword'),
 'blaze_sword':('manual-companion-projectile-swords.md','Blaze Sword'),
 'bone_sword':('manual-companion-projectile-swords.md','Bone Sword'),
 'shulker_sword':('manual-companion-projectile-swords.md','Shulker Sword'),
 'coal_sword':('manual-basic-swords.md','Coal Sword'),
 'cactus_sword':('manual-basic-swords.md','Cactus Sword'),
 'emerald_sword':('manual-basic-swords.md','Emerald Sword'),
 'lapis_sword':('manual-basic-swords.md','Lapis Sword'),
 'glass_sword':('manual-basic-swords.md','Glass Sword'),
 'obsidian_sword':('manual-heat-light-swords.md','Obsidian Sword'),
 'magma_sword':('manual-heat-light-swords.md','Magma Sword'),
 'glowstone_sword':('manual-heat-light-swords.md','Glowstone Sword'),
 'wither_skeleton_sword':('manual-heat-light-swords.md','Wither Skeleton Sword'),
 'bedrock_stick':('manual-quartz-bedrock-progression.md','Bedrock Stick и Bedrock Sword'),
 'bedrock_sword':('manual-quartz-bedrock-progression.md','Bedrock Stick и Bedrock Sword'),
 'quartz_diamond':('manual-quartz-bedrock-progression.md','Граф крафта 2.x: Quartz Diamond'),
 'quartz_diamond_stick':('manual-quartz-bedrock-progression.md','Граф крафта 2.x: Quartz Diamond'),
 'quartz_sword':('manual-quartz-bedrock-progression.md','Quartz Sword:'),
 'ghost_sword':('manual-ghost-nether-ultra.md','Ghost Sword'),
 'nether_star_sword':('manual-ghost-nether-ultra.md','Nether Star Sword'),
 'ultra_instinct_sword':('manual-ghost-nether-ultra.md','Ultra Instinct Sword'),
 'spectral_sword':('manual-spectral-time-comparison.md','Spectral Sword'),
 'time_sword':('manual-spectral-time-comparison.md','Clock Sword и Time Sword 2.x'),
 'clock_sword':('manual-spectral-time-comparison.md','Clock Sword и Time Sword 2.x'),
 'sword_of_time':('manual-spectral-time-comparison.md','Sword of Time 1.6'),
}
LEGACY_EXTRA={'ice_sword':'manual-ice-1.6.md','lightning_sword':'manual-lightning-1.6.md',
              'fire_sword':'manual-fire-magma-spider-1.6.md', 'magma_sword':'manual-fire-magma-spider-1.6.md',
              'spider_sword':'manual-fire-magma-spider-1.6.md'}
ADDITIONAL={'ultra_instinct_sword':'manual-fountain-2.8.md',
            'spectral_sword':'manual-spectral-world-2.8.md',
            'clock_sword':'manual-time-interactions-2.8.md',
            'time_sword':'manual-time-interactions-2.8.md'}


def read_doc(name):return (DOCS/name).read_text(encoding='utf-8')
def section_by_anchor(filename,anchor):
    text=read_doc(filename)
    sections=re.split(r'(?=^## )',text,flags=re.M)
    matches=[x for x in sections[1:] if slug(x.splitlines()[0][3:])==anchor]
    if len(matches)!=1:raise ValueError(f'{filename}: cannot resolve unique {anchor!r}')
    return matches[0].strip()
def section_by_prefix(filename,prefix):
    text=read_doc(filename)
    sections=re.split(r'(?=^## )',text,flags=re.M)
    matches=[x for x in sections[1:] if x.splitlines()[0][3:].startswith(prefix)]
    if len(matches)!=1:raise ValueError(f'{filename}: cannot resolve unique {prefix!r}')
    return matches[0].strip()
def demote(text):
    return re.sub(r'^(#{1,5}) ',lambda m:'#'*(min(6,len(m.group(1))+2))+' ',text.strip(),flags=re.M)
def whole_doc(filename):return demote(read_doc(filename))
def packed(value):return json.dumps(value,ensure_ascii=False,separators=(',',':'))
def field(c,key):return packed(c[key]) if key in c else 'не указан'
def output_items(v):
    if isinstance(v,str):return [v]
    if isinstance(v,list):return [i for x in v for i in output_items(x)]
    if isinstance(v,dict):return [v['item']] if isinstance(v.get('item'),str) else []
    return []

def recipe_data(filename,pack):
    result=defaultdict(list)
    with ZipFile(ROOT/'sources'/filename) as z:
        for path in sorted(z.namelist()):
            if not path.startswith(pack+'/recipes/') or not path.endswith('.json'):continue
            obj=json5.loads(z.read(path).decode('utf-8-sig'))
            for typ,recipe in obj.items():
                if not typ.startswith('minecraft:recipe_') or not isinstance(recipe,dict):continue
                for ident in output_items(recipe.get('result',recipe.get('output'))):result[ident].append((path,typ,recipe))
    return result

def recipe_lines(results,ident):
    matches=results.get(ident,[])
    if not matches:return ['- Рецептов с этим точным результатом локально не найдено. Это не исключает других путей.']
    lines=[]
    for path,typ,r in matches:
        lines.append(f'- Рецепт `{path}`; тип `{typ}`.')
        if 'pattern' in r:
            lines.append('  - Схема сверху вниз: '+ ' / '.join('`'+x+'`' for x in r['pattern'])+'.')
            lines.append('  - Обозначения: `'+packed(r.get('key',{}))+'`.')
            if isinstance(r.get('key'),dict) and all(isinstance(x,str) for x in r['pattern']):
                missing=sorted(set(''.join(r['pattern']))-{' '}-set(r['key']))
                if missing:lines.append('  - **В схеме есть символы без определения key: `'+packed(missing)+'`.** Их смысл и принятие рецепта движком не установлены.')
        if 'ingredients' in r:lines.append('  - Ингредиенты: `'+packed(r['ingredients'])+'`.')
        if 'input' in r:lines.append('  - Вход: `'+packed(r['input'])+'`.')
        lines.append('  - Результат: `'+packed(r.get('result',r.get('output')))+'`; рабочие станции/tags: `'+packed(r.get('tags'))+'`.')
    return lines

def acquisition_sections(version):
    text=read_doc(f'acquisition-index-{version}.md').split('## По предметам\n',1)[1]
    chunks=re.split(r'^### `(effect:[^`]+)`\s*$',text,flags=re.M)
    return {chunks[i]:chunks[i+1].strip() for i in range(1,len(chunks),2)}

def describe_item(version,entry):
    path,item=entry;c=item.get('components',{});lines=[f'**{version}** — определение `{path}`.']
    vals=[('урон','minecraft:damage'),('максимальная прочность','minecraft:durability'),('зачарование','minecraft:enchantable'),('перезарядка','minecraft:cooldown'),('левая рука','minecraft:allow_off_hand'),('размер стопки','minecraft:max_stack_size'),('свечение','minecraft:foil'),('предмет исчезает','minecraft:should_despawn')]
    lines.append('- '+'; '.join(label+': `'+field(c,k)+'`' if k in c else label+': не указан' for label,k in vals)+'.')
    r=c.get('minecraft:repairable')
    if r is None:lines.append('- Ремонт: компонент не указан; это не доказывает невозможности ремонта.')
    elif isinstance(r,dict):
        lines.append('- Ремонт (буквальные материалы и значения repair_amount): '+'; '.join('`'+packed(x.get('items'))+'` → `'+packed(x.get('repair_amount'))+'`' for x in r.get('repair_items',[]))+'.')
        if set(r)-{'repair_items'}:lines.append('  - Остальные поля компонента: `'+packed({k:v for k,v in r.items() if k!='repair_items'})+'`.')
    else:lines.append('- Ремонт: `'+packed(r)+'`.')
    w=c.get('minecraft:weapon');
    if isinstance(w,dict):
        labels={'on_hurt_entity':'нанесение урона существу','on_not_hurt_entity':'событие без нанесения урона существу','on_hit_block':'удар по блоку'}
        lines.append('- Оружейные хуки: '+('; '.join(labels.get(k,k)+' → `'+packed(v)+'`' for k,v in w.items()) if w else 'компонент пустой')+'.')
    else:lines.append('- Оружейный компонент не указан.')
    if 'minecraft:on_use' in c:lines.append('- При использовании предмета указано: `'+packed(c['minecraft:on_use'])+'`.')
    if 'minecraft:digger' in c:
        dig=c['minecraft:digger'];speeds=dig.get('destroy_speeds',[]) if isinstance(dig,dict) else []
        if len(speeds)>8:
            lines.append(f'- Правила добычи: {len(speeds)} записей; точные блоки, скорости и события приведены в полном определении в приложении В.')
        else:lines.append('- Скорости добычи и события digger: `'+packed(dig)+'`.')
    return '\n'.join(lines)

def screenshot_line(ident,evidence,files):
    e=evidence.get(ident)
    if not e:return 'Сопоставленной карточки чисел на скриншотах нет; это не значит, что предмет нигде на изображениях не упомянут.'
    lines=['На изображении вручную считаны: '+ '; '.join(k+' = `'+packed(e[k])+'`' for k in ('damage','durability','enchantable','repairable') if e.get(k) is not None)+'.']
    for shot in e['screenshots']:
        matches=[x for x in files if '20261104_'+shot+'_' in x['name']]
        if len(matches)!=1:raise ValueError('Screenshot ID unresolved: '+shot)
        lines.append('Оригинал: [скриншот '+shot+'](https://drive.google.com/file/d/'+matches[0]['id']+'/view).')
    return ' '.join(lines)

def old_summary(ident):
    name=ident.split(':')[1];anchor=legacy_manual_anchor(ident);text=section_by_anchor('manual-traces-1.6.md',anchor)
    if anchor==slug('Остальные предметы 1.6: первичные прямые цепочки'):
        label=name.removesuffix('_sword').replace('_',' ').title()
        m=re.search(r'^- \*\*'+re.escape(label)+r'\*\*[^\n]*',text,re.M)
        if not m:raise ValueError('Missing 1.6 bullet: '+ident+' label '+label)
        return m.group(0)
    return demote(text)

def build():
    versions={v:read_items(filename,pack) for v,filename,pack in VERSIONS}
    recipes={v:recipe_data(filename,pack) for v,filename,pack in VERSIONS}
    acquisition={v:acquisition_sections(v) for v,_,_ in VERSIONS}
    evidence={x['id']:x for x in json.loads((ROOT/'data/screenshot-stat-evidence.json').read_text(encoding='utf8'))}
    drive=json.loads((ROOT/'data/folder-listing-snapshot.json').read_text(encoding='utf8'))['files']
    manuals=manual_links();all_ids=sorted(set().union(*(set(v) for v in versions.values())))
    loot_models=defaultdict(list)
    for line in read_doc('loot-selection-model.md').splitlines():
        if not line.startswith('| `') or ' | `effect' not in line:continue
        cells=[c.strip() for c in line.strip('|').split(' | ')]
        if len(cells)!=7:raise ValueError('Unexpected loot model row: '+line)
        ident=cells[1].strip('`')
        loot_models[ident].append(cells)
    summary={}
    for line in read_doc('guide-ru.md').splitlines():
        if line.startswith('| [') and '<br>`effect:' in line:
            cells=[c.strip() for c in line.strip('|').split('|')]
            ident=re.search(r'`(effect:[^`]+)`',cells[0]).group(1)
            summary[ident]=cells[3]
    if set(summary)!=set(all_ids):raise ValueError('Overview coverage changed')
    raw_appendix=[]
    if len(all_ids)!=43 or set(DEEP)!={i.split(':')[1] for i in all_ids}:raise ValueError('Item/deep review coverage changed')
    out=['''# Swords and More Swords — подробная памятка по каждому предмету

## Как пользоваться документом

Это развернутый единый документ для проверки собранного материала. В нём **43 карточки точных ID**: 42 предмета 2.x и ещё Sword of Time 1.6. Некоторые из них — материалы, а не мечи. В структуре Google Документа выберите название нужного предмета: внутри указаны характеристики по версиям, материалы ремонта, объявленные рецепты и добыча, описание эффектов, условия, вероятности, отличия старой версии и то, что осталось неясным. В приложении В — полные машинно разобранные определения предметов, чтобы не потерять точные числа и события. Это техническая часть, её можно пропустить при первом чтении.

**Границы:** это преимущественно статический разбор исходных файлов; отдельные серверные испытания обозначены отдельно и не подтверждают остальные механики. Наличие команды, рецепта или условия не доказывает, что конкретная версия Bedrock их примет и выполнит. Условные доли randomize относятся к выбору после выполнения условий, а не автоматически к каждому удару, мобу или сундуку. Веса loot не равны процентам без суммы весов, rolls и других условий. Если поле не указано — не подставляйте ноль, false или бесконечность. Версия текстов скриншотов не установлена; OCR может ошибаться. Все 21 распознанных текста приведены в приложении.

В 1.6 три JSON сущностей не разбираются, в обеих 2.x не разбирается creeper.json; есть повторные ключи. Поэтому гипотетически исправленный в памяти файл и декларацию нельзя принимать за подтверждённую работу. Архивы не менялись. Отдельные проверки оригинала на сервере и личное наблюдение игрока документированы; ремейк не начат.

**Исходники:** 1.6 — 26 определений, 2.8.8 и 2.8.14 — по 42. У одноимённых ID 2.x все item-компоненты структурно совпадают; Ice отличается в событиях и окружении. Другие различия 2.x включают генерацию руд и торговлю. Названия версий взяты из имён архивов.

В повторяющихся подробных разделах сохранены исходные технические термины и уточнения из исследования; они намеренно не заменены выдуманными игровыми результатами. Ссылки на оригинальные скриншоты ведут на Google Диск.
''']
    for index,ident in enumerate(all_ids,1):
        short=ident.split(':')[1];display=short.replace('_',' ').title();out += [f'## {index:02d}. {display} — `{ident}`','', '**Кратко:** '+summary[ident]+' Описана версия 2.x, кроме Sword of Time 1.6.','', '### Основные данные и ремонт','']
        if ident in versions['1.6']:out += [describe_item('1.6',versions['1.6'][ident]),'']
        else:out += ['- В 1.6 предмет с этим точным ID не найден.','']
        if ident in versions['2.8.14']:
            out += [describe_item('2.8.8 / 2.8.14',versions['2.8.14'][ident]),'']
            if versions['2.8.8'][ident][1].get('components')!=versions['2.8.14'][ident][1].get('components'):raise ValueError('Unexpected component version diff '+ident)
        else:out += ['- В 2.x предмет с этим точным ID не найден.','']
        out += ['### Рецепты и пути получения','', 'При отсутствии точного локального рецепта другие источники всё ещё возможны. Прямые loot-записи, торговля и структуры ниже — индексы деклараций: структура может хранить предмет на стойке, а не выдавать дроп.','']
        for ver in ('1.6','2.8.14'):
            if ident not in versions[ver]:continue
            out += [f'**Архив {ver}:**','']+recipe_lines(recipes[ver],ident)+['',acquisition[ver][ident],'']
        if ident in versions['2.8.8']:
            if acquisition['2.8.8'][ident]!=acquisition['2.8.14'][ident] or recipes['2.8.8'].get(ident,[])!=recipes['2.8.14'].get(ident,[]):
                out += ['**Отличающиеся записи архива 2.8.8:**','']+recipe_lines(recipes['2.8.8'],ident)+['',acquisition['2.8.8'][ident],'']
            else:out += ['Записи прямых рецептов, loot, торговли и структур в индексе 2.8.8 совпадают с приведёнными для 2.8.14; это не гарантия одинаковой регистрации.','']
        if loot_models.get(ident):
            out += ['**Условная математическая модель выбора loot в 2.x:**','',
                    'Числа ниже — вероятность выбрать хотя бы одну запись предмета внутри уже активированного пула, а не шанс реальной добычи. Допущения: все записи доступны; отсутствующий вес принят за 1; quality и условия записей игнорируются; выборы независимы с возвращением; число rolls равномерно в указанном диапазоне. Условия пула считаются уже выполненными. Загрузка таблицы, дополнительный отбор, количество предметов и функции не эмулируются.','']
            for cells in loot_models[ident]:
                table,_,entry_indices,rolls,weights,chance,risk=cells
                out.append(f'- Таблица/пул: {table}; entries: {entry_indices}; rolls: {rolls}; вес ID/сумма: {weights}; выбор хотя бы одной записи по модели: **{chance}**. Условия и оговорки: {risk}.')
            out.append('')
        out += ['### Способности, условия и вероятности по файлам','']
        if ident in manuals:
            anchor=manuals[ident].split('#',1)[1]
            out += ['**Основная цепочка 2.8.14** (источник внутри проекта: `docs/manual-traces-2.8.14.md`):','',demote(section_by_anchor('manual-traces-2.8.14.md',anchor)),'']
        if ident in versions['1.6']:
            out += ['**Старая версия 1.6** (источник: `docs/manual-traces-1.6.md`):','',old_summary(ident),'']
        f,sel=DEEP[short]
        out += [f'**Дополнительный подробный разбор** (источник: `docs/{f}`):','',demote(section_by_prefix(f,sel)) if sel else whole_doc(f),'']
        if short in LEGACY_EXTRA and LEGACY_EXTRA[short]!=f:
            file=LEGACY_EXTRA[short];out += [f'**Дополнительные детали 1.6** (источник: `docs/{file}`):','',whole_doc(file),'']
        if short in ADDITIONAL:
            file=ADDITIONAL[short];out += [f'**Связанный подробный механизм** (источник: `docs/{file}`):','',whole_doc(file),'']
        out += ['### Что написано на скриншотах','',screenshot_line(ident,evidence,drive),'',
                'Описание на странице — заявление автора, не подтверждённая работа исходника. Данные OCR всех снимков приведены в приложении Б. Полное определение предмета — в приложении В.','']
        raw_appendix += [f'### {index:02d}. {display} — `{ident}`','']
        for ver in ('1.6','2.8.14'):
            if ident in versions[ver]:
                raw_appendix += [f'**Архив {ver}:**','', '```json',json.dumps(versions[ver][ident][1],ensure_ascii=False,indent=2),'```','']
        if ident=='effect:ice_sword':
            raw_appendix += ['**Архив 2.8.8: отдельное определение Ice из-за отличий событий:**','', '```json',json.dumps(versions['2.8.8'][ident][1],ensure_ascii=False,indent=2),'```','']
    out += ['## Приложение А. Общие различия версий и риски','',whole_doc('manual-version-2.8.8.md'),'',
            '### Общая архитектура и сбросы 1.6','',demote(section_by_prefix('manual-traces-1.6.md','Общая архитектура игрока')),'',
            '### Пересечения разных эффектов','',whole_doc('manual-family-cross-effects-2.8.md'),'',
            '### Отмеченные расхождения со скриншотами','',whole_doc('screenshot-visual-review.md'),'',
            '## Приложение Б. Распознанный текст всех 21 скриншотов','',
            'Ниже дословно приведён сохранённый OCR. Число в начале строки — оценка распознавания, а не часть описания. Возможны неверные слова, буквы, числа и пропуски; это **не** полностью вручную выверенная транскрипция.','',whole_doc('screenshot-ocr.md'),'',
            '## Приложение В. Точные компоненты и события предметов','',
            'Полное содержимое каждого `minecraft:item` после JSON5-разбора. Это машинная выписка, а не все косвенные файлы или доказательство выполнения.',''] + raw_appendix
    return '\n'.join(out)

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,default=DOCS/'detailed-item-guide-ru.md');args=p.parse_args();result=build();args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(result,encoding='utf8');print('Written:',args.output,'characters:',len(result),'item cards:',len(re.findall(r'^## \d{2}\. ',result,re.M)))
if __name__=='__main__':main()
