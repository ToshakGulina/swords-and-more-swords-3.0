#!/usr/bin/env python3
"""Lexical raw-source ledger of world-changing command candidates."""
from pathlib import Path
from zipfile import ZipFile
from collections import Counter
import json,re
from build_entity_group_index import VERSIONS
ROOT=Path(__file__).resolve().parents[1]
WORDS={'fill':r'(?<![\w:])fill\b','setblock':r'(?<![\w:])setblock\b','clone':r'(?<![\w:])clone\b','structure load':r'(?<![\w:])structure\s+load\b','loot spawn':r'(?<![\w:])loot\s+spawn\b'}
PATS={k:re.compile(v) for k,v in WORDS.items()}

def extract(filename,pack):
    rows=[]
    with ZipFile(ROOT/'sources'/filename) as z:
        for path in sorted(z.namelist()):
            if not path.startswith(pack+'/') or not path.endswith(('.json','.mcfunction','.js')):continue
            for line,text in enumerate(z.read(path).decode('utf-8-sig').splitlines(),1):
                labels=tuple(k for k,p in PATS.items() if p.search(text))
                if labels:rows.append((path,line,text,labels))
    return rows

def code(v):return '`'+json.dumps(v,ensure_ascii=False,separators=(',',':')).replace('|','\\|').replace('`','\\u0060')+'`'

def render(version,rows):
    counts=Counter(label for row in rows for label in row[3]);out=[f'# Команды изменения мира и создания loot: исходные строки — {version}', '',
         f'Лексический поиск по всем `.json`, `.mcfunction`, `.js` behavior pack: **{len(rows)} исходных строк**, содержащих `fill`, `setblock`, `clone`, `structure load` или `loot spawn`. Сохранены точные строки, отступы, номера, порядок файла и повторы; строка может содержать несколько команд и несколько меток. Отсортировано по пути и номеру, а не по времени исполнения.', '',
         'Это **кандидаты по тексту**, не Bedrock-парсер или доказательство вызова, применимости синтаксиса и изменений мира. Комментарии, неразобранные JSON, строковые данные и шаблоны JS включены; координаты, selector, detect, replace, порядок в sequence, случайные фильтры и исполнитель сохраняются в исходном тексте, но здесь не вычисляются. Вне области: другие команды, функции из других пакетов, block components, взрывы, вызовы `summon`/`event entity`, автоматические механизмы и косвенные эффекты. Показан только найденный текст, а не число затронутых блоков.', '',
         'Метки по числу строк (не вхождений и не исполнений): '+', '.join(f'`{k}` — {counts[k]}' for k in WORDS)+'. Сумма может превышать количество строк. Для структур см. [NBT 2.8.8](structures-2.8.8.md) / [2.8.14](structures-2.8.14.md), для loot — [условия](loot-context.md), для льда — [геометрию](manual-ice-geometry-2.8.md), для Jungle — [лианы](jungle-vine-index.md).', '']
    if version in ('2.8.8','2.8.14'):
        out += ['Сравнение 2.x в этой выборке: 50 общих строк отличаются заменой `effect99:fake_ice` на `frosted_ice` (40 в Ice item, 10 в player); дополнительно только 2.8.8 содержит строку `setblock ~ ~ ~ air 0 destroy` в `blocks/fake_ice.json`. Исходные точки с иными командами и 11-е вхождение замены в `player.json` могут находиться вне данной выборки. Из замены нельзя вывести эквивалентность блоков.', '']
    out += ['| Файл / строка | Метки | Исходная строка целиком |', '|---|---|---|']
    for path,line,text,labels in rows:out.append(f'| `{path}:{line}` | '+', '.join('`'+k+'`' for k in labels)+f' | {code(text)} |')
    out += ['', 'Условия и полные определения: [реестр мира](world-ledger-'+version+'.md), [реестр сущностей](entity-ledger-'+version+'.md), [предметы](items-'+version+'.md).', '']
    return '\n'.join(out)

def build_all():
    d={v:extract(f,p) for v,f,p in VERSIONS};a={(p,n):(t,l) for p,n,t,l in d['2.8.8']};b={(p,n):(t,l) for p,n,t,l in d['2.8.14']};only=set(a)-set(b)
    if only!={('Swords_B/blocks/fake_ice.json',107)} or set(b)-set(a):raise ValueError('unexpected 2.x paths/lines')
    changed=[key for key in a.keys()&b.keys() if a[key]!=b[key]]
    if len(changed)!=50 or Counter(key[0] for key in changed)!={'Swords_B/items/ice_sword.json':40,'Swords_B/entities/player.json':10} or any(a[key][0].replace('effect99:fake_ice','frosted_ice')!=b[key][0] or a[key][1]!=b[key][1] for key in changed):raise ValueError('unexpected 2.x world command changes')
    return {ver:render(ver,rows) for ver,rows in d.items()}

def main():
    for ver,text in build_all().items():
        (ROOT/f'docs/world-command-index-{ver}.md').write_text(text,encoding='utf8');print(ver,len(text.splitlines()),'lines')
if __name__=='__main__':main()
