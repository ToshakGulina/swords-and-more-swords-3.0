#!/usr/bin/env python3
"""Literal candidate strings for selected command keywords; not a Bedrock parser."""
from collections import Counter
from pathlib import Path
from zipfile import ZipFile
import re,json5
from build_entity_group_index import VERSIONS
ROOT=Path(__file__).resolve().parents[1]
WORDS=('gamerule','scoreboard','time','weather','kill','damage','tp','teleport','ride','replaceitem','clear','tickingarea')
PATTERNS={word:re.compile(r'(?<![\w:])'+re.escape(word)+r'\b',re.I) for word in WORDS}

def marks(text):return tuple(word for word in WORDS if PATTERNS[word].search(text))

def extract(filename,pack):
    records=[];errors=[];duplicates=[];total=0
    def record(path,location,kind,text,target=None):
        nonlocal total
        total+=1;labels=marks(text)
        if labels:records.append((path,location,kind,target,text,labels))
    with ZipFile(ROOT/'sources'/filename) as z:
        for path in sorted(z.namelist()):
            if not path.startswith(pack+'/'):continue
            if path.endswith('.mcfunction'):
                try:text=z.read(path).decode('utf-8-sig')
                except UnicodeDecodeError as ex:errors.append((path,str(ex).splitlines()[0]));continue
                for line,value in enumerate(text.splitlines(),1):
                    v=value.strip()
                    if v and not v.startswith('#'):record(path,f'line:{line}','mcfunction',v)
            elif path.endswith('.json'):
                repeated=[]
                def pairs(seq):
                    out={}
                    for key,value in seq:
                        if key in out:repeated.append(key)
                        out[key]=value
                    return out
                try:obj=json5.loads(z.read(path).decode('utf-8-sig'),object_pairs_hook=pairs)
                except (ValueError,UnicodeDecodeError) as ex:errors.append((path,str(ex).splitlines()[0]));continue
                if repeated:duplicates.append((path,repeated))
                def strings(v,path0,kind,target=None):
                    if isinstance(v,str):record(path,path0,kind,v,target)
                    elif isinstance(v,list):
                        for i,x in enumerate(v):
                            if isinstance(x,str):record(path,f'{path0}[{i}]',kind,x,target)
                            else:raise ValueError('unsupported candidate list entry: '+path+path0)
                    else:raise ValueError('unsupported candidate string collection: '+path+path0)
                def walk(v,loc):
                    if isinstance(v,dict):
                        run=v.get('run_command')
                        if isinstance(run,dict) and 'command' in run:strings(run['command'],loc+'.run_command.command','run_command',run.get('target'))
                        for key,value in v.items():
                            if key in ('on_entry','on_exit'):strings(value,loc+'.'+key,key)
                            walk(value,loc+'.'+key)
                    elif isinstance(v,list):
                        for i,x in enumerate(v):walk(x,loc+f'[{i}]')
                walk(obj,'$')
    return records,errors,duplicates,total

def render(title,version,data):
    records,errors,duplicates,total=data;counts=Counter(label for row in records for label in row[-1])
    out=[f'# Выбранные побочные команды: буквальные кандидаты — {title}', '',
         f'Из {total} строк следующих источников выделено **{len(records)}** строк, содержащих одно или более ключевых слов: `{", ".join(WORDS)}`. Область поиска: `run_command.command`, строковые `on_entry`/`on_exit` в разобранных behavior JSON и непустые, не начинающиеся с `#` строки behavior mcfunction. Дубли из разных состояний и повторённые строки сохранены; номера/пути позволяют видеть порядок в конкретном списке.', '',
         'Это **лексический поиск**, не парсер команд и не подтверждение действия. Совпадение слова может находиться в аргументе или вложенном execute, а условие, адресат, область и разрешение `@s` зависят от контекста. `target` показан только явно записанный рядом с `run_command`; отсутствие не превращается в self. Состояния `on_entry`/`on_exit` могут содержать не только команды. Отдельные метки могут пересекаться, поэтому их количества нельзя складывать как число строк.', '',
         'Вне поиска: JS, строки команд в других полях, неразобранные JSON, внешние/ванильные вызовы, интерпретация `/function`, `fill`, `setblock`, `summon`, структуры и действия компонентов. Например, изменение мира может происходить и без команд из этого списка. Для обычных вызовов и полных условий сверять [реестр сущностей](entity-ledger-'+version+'.md), [контроллеры](animation-ledger-'+version+'.md), [предметы](items-'+version+'.md) и исходный архив.', '',
         'Метки по числу **строк**, а не исполнений: '+', '.join(f'`{w}` — {counts[w]}' for w in WORDS)+'.', '',
         '- Неразобранные JSON: '+('; '.join(f'`{p}` ({err})' for p,err in errors) if errors else 'нет')+'.',
         '- Повторные ключи: '+('; '.join(f'`{p}`: '+', '.join('`'+k+'`' for k in names) for p,names in duplicates) if duplicates else 'нет')+'. JSON5 сохраняет последнее значение.', '']
    if version in ('2.8.8','2.8.14'):
        other='2.8.14' if version=='2.8.8' else '2.8.8'
        out += [f'Сопоставление выбранных строк с [{other}](command-risk-index-{other}.md): один путь содержит различающийся аргумент блока в Ice teleport (`effect99:fake_ice` / `frosted_ice`); остальные найденные кандидаты совпадают. Это не сравнение остальных команд и файлов.', '']
    out += ['| Файл / путь | Источник / target | Метки | Исходная строка |','|---|---|---|---|']
    for path,loc,kind,target,text,labels in records:
        escaped=text.replace('`','\\`').replace('|','\\|').replace('\n','<br>')
        targ='; target `'+str(target)+'`' if target is not None else ('; target не указан' if kind=='run_command' else '')
        out.append(f'| `{path}`<br>`{loc}` | {kind}{targ} | '+', '.join('`'+x+'`' for x in labels)+f' | `{escaped}` |')
    return '\n'.join(out)+'\n'

def build_all():
    d={v:extract(f,p) for v,f,p in VERSIONS}
    a,b=d['2.8.8'],d['2.8.14'];only_a=set(a[0])-set(b[0]);only_b=set(b[0])-set(a[0])
    if a[1:3]!=b[1:3] or len(only_a)!=1 or len(only_b)!=1:raise ValueError('unexpected 2.x candidate differences')
    x,y=next(iter(only_a)),next(iter(only_b))
    if x[:4]!=y[:4] or x[4].replace('effect99:fake_ice','frosted_ice')!=y[4] or x[5]!=y[5]:raise ValueError('unexpected 2.x Ice candidate')
    return {v:render(v,v,d[v]) for v,_,_ in VERSIONS}

def main():
    for ver,text in build_all().items():
        (ROOT/f'docs/command-risk-index-{ver}.md').write_text(text,encoding='utf-8');print(ver,len(text.splitlines()),'lines')
if __name__=='__main__':main()
