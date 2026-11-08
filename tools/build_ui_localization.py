#!/usr/bin/env python3
"""Preserve language lines and trace every direct UI $text reference."""
from pathlib import Path
from zipfile import ZipFile
from collections import defaultdict
import json,json5
from build_quick_reference import read_items,slug
ROOT=Path(__file__).resolve().parents[1]
VERSIONS=(('1.6','SwordsAndMoreSwords.1.6.mcaddon','Sword_R'),('2.8.8','swordsandmoreswords_2_8_8.mcaddon','Swords_R'),('2.8.14','swordsandmoreswords-2-8-14.mcaddon','Swords_R'))
UI='Swords_R/ui/how_to_play_screen.json'

def load():
    versions={}
    for version,archive,rp in VERSIONS:
        with ZipFile(ROOT/'sources'/archive) as z:
            raw=z.read(rp+'/texts/en_US.lang').decode('utf-8-sig');lines=raw.splitlines();entries=defaultdict(list)
            for no,line in enumerate(lines,1):
                if not line.strip() or line.lstrip().startswith('#'):continue
                if '=' not in line:raise ValueError(f'unknown lang syntax {version} line {no}')
                key,value=line.split('=',1);entries[key].append((no,value))
            ui_raw=z.read(UI) if UI in z.namelist() else None
            versions[version]={'lines':lines,'entries':entries,'ui_raw':ui_raw,'ui':json5.loads(ui_raw.decode('utf-8-sig')) if ui_raw else None}
    return versions

def textrefs(obj,path):
    if isinstance(obj,dict):
        for key,v in obj.items():
            nextpath=path+'.'+key
            if key=='$text' and isinstance(v,str):yield nextpath,v
            yield from textrefs(v,nextpath)
    elif isinstance(obj,list):
        for i,v in enumerate(obj):yield from textrefs(v,path+f'[{i}]')

def code(v):return '`'+json.dumps(v,ensure_ascii=False).replace('|','\\|').replace('`','\\u0060')+'`'

def value(entries,key):
    vals=entries.get(key,[])
    if not vals:return '**нет точного ключа**'
    return '<br>'.join(f'стр. {no}: {code(s)}' for no,s in vals)

def build_ui(data):
    a,b=data['2.8.8'],data['2.8.14'];ui=b['ui']
    if data['1.6']['ui'] is not None or a['ui_raw']!=b['ui_raw']:raise ValueError('unexpected UI file differences')
    refs=list(textrefs(ui,'$'));missing=[(p,k) for p,k in refs if k not in b['entries']];items=read_items('swordsandmoreswords-2-8-14.mcaddon','Swords_B');sections=[key for key in ui if key.endswith('_section@how_to_play_common.main_sections')];mapped={key.split('@')[0][:-8] for key in sections if 'effect:'+key.split('@')[0][:-8] in items};unmapped=sorted(set(items)-{'effect:'+x for x in mapped})
    out=['# Встроенная справка 2.x: поля текста и локализация', '',
         'Источник UI: `Swords_R/ui/how_to_play_screen.json` (файл побайтово одинаков в 2.8.8 и 2.8.14); источник строк — `Swords_R/texts/en_US.lang` каждого архива. В 1.6 такого локального UI-файла нет. Разбор следует порядку полей JSON и списков, а не предполагаемому порядку отрисовки. Здесь сохранены все прямые строковые поля `$text`, без вычисления наследования, видимости, управления или шаблонов Bedrock.', '',
         f'Всего {len(refs)} полей `$text`, {len(set(k for _,k in refs))} различных ссылок, {len(missing)} ссылок без точного ключа в локальном en_US 2.8.14. Из {len(sections)} секций {len(mapped)} точно соответствуют ID предмета по имени; локального одноимённого раздела для остальных {len(unmapped)} ID нет: '+', '.join('`'+id+'`' for id in unmapped)+'. Отсутствие раздела или строки в пакете не доказывает отсутствия fallback, фактической видимости либо иной локализации.', '',
         'Значения приведены без изменения как JSON-строки: пробелы внутри кавычек, коды `§` и английский текст сохранены. Числа и обещания справки — заявления автора, а не подтверждение кода или поведения. Если ключ повторяется, перечислены все исходные строки; приоритет повторов и fallback не определяются. [Полные исходные строки en_US всех версий](localization-source-index.md); [сверка чисел UI с компонентами](ui-stat-comparison.md) · [сравнение скриншотов с компонентами](screenshot-stat-comparison.md).', '',
         'Пять ID без одноимённой секции всё же названы во вложенных заголовках: Wet Sponge Sword — в `sponge_sword_section`, четыре материала — в `blocks_and_items_section`. В секции Sponge под заголовком Wet Sponge заявлены прочность 64 и damage 3; локализованные строки `effect.sponge_sword.text.14` и `.15` присутствуют в en_US, но ни одно прямое `$text` поля UI не ссылается на них.', '',
         'Справка сама даёт два разных описания глубины серебряной руды: `effect.blocks_and_items.text_2` — ниже 35, `effect.silver_sword.text.7` — ниже 15. В 2.8.8 декларирован gaussian extent `[10,35]`, а в 2.8.14 локальных правил генерации этих руд нет; см. [анализ генерации](manual-version-2.8.8.md). Это разные типы данных, и утверждения UI не доказывают границы реальной генерации.', '',
         '## Локально отсутствующие ключи en_US', '', '| Путь поля UI | Ключ |', '|---|---|']
    for p,k in missing:out.append(f'| {code(p)} | {code(k)} |')
    out += ['','## Полный порядок прямых полей $text','']
    for name,obj in ui.items():
        records=list(textrefs(obj,'$.'+name))
        if not records:continue
        out += [f'### {name}', '', '| Путь поля | Ключ | Значение в 2.8.8 / 2.8.14 |', '|---|---|---|']
        for p,key in records:
            av=value(a['entries'],key);bv=value(b['entries'],key)
            # Locations are included, so avoid assuming same line numbers when only values match.
            rendered=av if av==bv else f'2.8.8: {av}<br>2.8.14: {bv}'
            out.append(f'| {code(p)} | {code(key)} | {rendered} |')
        out.append('')
    return '\n'.join(out)

def build_lang(data):
    out=['# Полный построчный реестр локализации en_US', '',
         'Исходные строки `texts/en_US.lang` представлены по порядку, включая пустые и повторяющиеся. Строка показана как JSON-строка, чтобы конечные и начальные пробелы оставались явными внутри кавычек; форматирование архивного файла и байтовый порядок следует брать из `sources/`. Это не интерпретация правил разбора движком. Прямые ссылки `$text` из UI — в [отдельном индексе](ui-localization-index.md).', '']
    for version,archive,rp in VERSIONS:
        v=data[version];dupes={k:values for k,values in v['entries'].items() if len(values)>1}
        out += [f'## {version}', '',f'Архив `{archive}`, путь `{rp}/texts/en_US.lang`; строк: {len(v["lines"])}; различных ключей: {len(v["entries"])}. Повторяющиеся ключи: '+(', '.join('`'+k+'` (строки '+', '.join(str(no) for no,_ in vals)+')' for k,vals in dupes.items()) if dupes else 'нет')+'.', '', '| № | Исходная строка |','|---:|---|']
        out += [f'| {i} | {code(line)} |' for i,line in enumerate(v['lines'],1)]
        out.append('')
    return '\n'.join(out)

def main():
    data=load();(ROOT/'docs/ui-localization-index.md').write_text(build_ui(data),encoding='utf-8');(ROOT/'docs/localization-source-index.md').write_text(build_lang(data),encoding='utf-8');print('UI and localization indexes written')
if __name__=='__main__':main()
