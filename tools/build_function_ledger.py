#!/usr/bin/env python3
"""Full mcfunction line ledger plus lexical direct callers for each archive."""
from pathlib import Path
from zipfile import ZipFile
from collections import defaultdict,Counter
import hashlib,json,re
from build_entity_group_index import VERSIONS
ROOT=Path(__file__).resolve().parents[1]
SCAN=re.compile(r'(?<![\w:])function\s+')
CALL=re.compile(r'(?<![\w:])function\s+([\w/.:_-]+)')

def extract(filename,pack):
    functions={};calls=[];unrecognized=[]
    with ZipFile(ROOT/'sources'/filename) as z:
        paths=sorted(z.namelist())
        for p in paths:
            if not p.startswith(pack+'/functions/') or not p.endswith('.mcfunction'):continue
            name=p[len(pack+'/functions/'):-len('.mcfunction')];raw=z.read(p);functions[name]={'path':p,'sha256':hashlib.sha256(raw).hexdigest(),'lines':raw.decode('utf-8-sig').splitlines()}
        for p in paths:
            if not p.startswith(pack+'/') or not p.endswith(('.json','.mcfunction','.js')):continue
            for n,line in enumerate(z.read(p).decode('utf-8-sig').splitlines(),1):
                for m in SCAN.finditer(line):
                    match=CALL.match(line,m.start())
                    if match is None:unrecognized.append((p,n,line));continue
                    calls.append((p,n,line,match.group(1)))
    return functions,calls,unrecognized

def code(v):return '`'+json.dumps(v,ensure_ascii=False,separators=(',',':')).replace('|','\\|').replace('`','\\u0060')+'`'

def render(title,ver,data):
    functions,calls,unknown=data;total=sum(len(f['lines']) for f in functions.values());by=defaultdict(list)
    for p,n,line,name in calls:by[name].append((p,n,line))
    notfound=sorted(set(by)-set(functions))
    out=[f'# Функции: все исходные строки и буквальные вызовы — {title}', '',
         f'Все **{len(functions)}** `.mcfunction` behavior pack, всего **{total} строк** с пустыми строками, по порядку. Строки представлены JSON-строками: кавычки, пробелы и специальные символы внутри значения не теряются; архив остаётся эталоном исходных байтов, в том числе окончаний строк. SHA-256 вычислен по исходным байтам. Путь function — относительный путь после `functions/` без `.mcfunction`.', '',
         f'Найдено {len(calls)} буквальных вхождений `function <путь>` при поиске во всех `.json`, `.mcfunction`, `.js` behavior pack, включая возможные комментарии или неразобранные JSON. Это только лексические кандидаты вызова, не парсер, доказательство запуска или исчерпывающий граф. Неточные или динамические пути, внешние пакеты и вызов игроком/консолью не интерпретируются. Нулевое число локальных вхождений не означает недоступность функции.', '',
         '- Точные пути вызова без одноимённого локального файла: '+(', '.join('`'+x+'`' for x in notfound) if notfound else 'нет в области поиска')+'.',
         '- Вхождения не соответствующие шаблону: '+('; '.join(f'`{p}:{n}`' for p,n,_ in unknown) if unknown else 'нет')+'.','']
    if ver=='2.x':out += ['Все четыре `.mcfunction` и выбранные строки вызова в двух архивах 2.x совпадают побайтово/буквально соответственно; это не равенство всех других файлов или фактической работы функций.', '']
    out += ['## Буквальные источники вызовов','', '| Файл:строка | Путь function | Локальный файл по точному пути | Полная строка |','|---|---|---|---|']
    for p,n,line,name in calls:
        target=functions.get(name);out.append(f'| `{p}:{n}` | {code(name)} | '+('`'+target['path']+'`' if target else 'не найден точно')+f' | {code(line)} |')
    out += ['', '## Полные файлы', '']
    for name,f in sorted(functions.items()):
        refs=by[name];out += [f'### {name}', '',f'Архивный путь: `{f["path"]}`; SHA-256 `{f["sha256"]}`; буквальных кандидатов вызова: {len(refs)}.', '', '| № | Исходная строка |', '|---:|---|']
        out += [f'| {i} | {code(line)} |' for i,line in enumerate(f['lines'],1)];out.append('')
    out += ['См. также [назначение тегов и проблемы получения](manual-acquisition-issues.md), [лианы Jungle](jungle-vine-index.md), [ручной разбор Wolf](manual-wolf-conditions-2.8.md) и [общий scoreboard 1.6](manual-global-state-1.6.md).', '']
    return '\n'.join(out)

def build_all():
    d={v:extract(f,p) for v,f,p in VERSIONS}
    if d['2.8.8']!=d['2.8.14']:raise ValueError('2.x function source bytes or lexical callers differ')
    return {'1.6':render('1.6','1.6',d['1.6']),'2.x':render('2.8.8 и 2.8.14','2.x',d['2.8.14'])}

def main():
    for version,text in build_all().items():
        (ROOT/f'docs/function-ledger-{version}.md').write_text(text,encoding='utf8');print(version,len(text.splitlines()),'lines')
if __name__=='__main__':main()
