#!/usr/bin/env python3
"""Lexical summon/event entity cross-reference, preserving exact source lines."""
from pathlib import Path
from zipfile import ZipFile
from collections import defaultdict,Counter
import re,json,json5
from build_entity_group_index import VERSIONS
ROOT=Path(__file__).resolve().parents[1]
SUMSCAN=re.compile(r'(?<![\w:])summon\s+')
EVSCAN=re.compile(r'\bevent\s+entity\s+')
SUM=re.compile(r'(?<![\w:])summon\s+([\w:.-]+)')
EVENT=re.compile(r'\bevent\s+entity\s+(@\w+(?:\[[^\]]*\])?|\S+)\s+([\w:.-]+)')

def extract(filename,pack):
    calls=[];errors=[];duplicates=[];defs=defaultdict(list);ids=defaultdict(list);unknown=[]
    with ZipFile(ROOT/'sources'/filename) as z:
        for path in sorted(z.namelist()):
            if not path.startswith(pack+'/') or not path.endswith(('.json','.mcfunction','.js')):continue
            source=z.read(path).decode('utf-8-sig')
            for n,line in enumerate(source.splitlines(),1):
                sms=list(SUMSCAN.finditer(line));evs=list(EVSCAN.finditer(line))
                if not sms and not evs:continue
                summatches=[SUM.match(line,m.start()) for m in sms];evmatches=[EVENT.match(line,m.start()) for m in evs]
                if any(x is None for x in summatches+evmatches):unknown.append((path,n))
                summons=tuple(x.group(1) for x in summatches if x);events=tuple((x.group(1),x.group(2)) for x in evmatches if x)
                calls.append((path,n,line,summons,events))
            if not (path.startswith(pack+'/entities/') and path.endswith('.json')):continue
            rep=[]
            def pairs(seq):
                obj={}
                for k,v in seq:
                    if k in obj:rep.append(k)
                    obj[k]=v
                return obj
            try:e=json5.loads(source,object_pairs_hook=pairs)['minecraft:entity']
            except (ValueError,KeyError) as err:errors.append((path,str(err).splitlines()[0]));continue
            if rep:duplicates.append((path,tuple(rep)))
            ident=e['description']['identifier'];ids[ident].append(path)
            for event in e.get('events',{}):defs[event].append((ident,path))
    return calls,errors,duplicates,dict(ids),dict(defs),unknown

def code(value):return '`'+json.dumps(value,ensure_ascii=False,separators=(',',':')).replace('|','\\|').replace('`','\\u0060')+'`'
def render(title,ver,data):
    calls,errors,dups,ids,defs,unknown=data;sm=Counter(id for _,_,_,summons,events in calls for id in summons);ev=Counter(event for _,_,_,summons,events in calls for selector,event in events)
    out=[f'# Командные summon и event entity — {title}', '',
         f'Лексический поиск во всех `.json`, `.mcfunction`, `.js` behavior pack: **{len(calls)} исходных строк**, {sum(sm.values())} подстрок `summon <ID>` и {sum(ev.values())} подстрок `event entity <цель> <имя>`. На одной исходной строке могут находиться несколько команд; показаны исходные строки и номера, повторы сохранены. Здесь отдельно от [component spawn/shoot](spawn-shoot-index-{ver}.md) показаны только указанные командные формы.', '',
         'Это не парсер Bedrock: строки могут быть комментариями, данными или недостижимыми ветвями, а синтаксис и выполнение не проверены. Не интерпретируются `execute`, координаты, target/holder, условия, область действия, событие после summon, косвенные функции или приоритеты. Приведены **кандидаты по точному имени**, а не определённые получатели: selectors могут выбирать другую сущность; `@s` не всегда равен субъекту файла. Локально ненайденный ID может относиться к vanilla, другому пакету или неразобранному файлу; namespace автоматически не добавляется.', '',
         'По exact ID для `summon`: '+(', '.join(f'`{k}` — {v}' for k,v in sorted(sm.items())) if sm else 'нет')+'.',
         'По имени для `event entity`: '+(', '.join(f'`{k}` — {v}' for k,v in sorted(ev.items())) if ev else 'нет')+'.', '',
         '- Не разобраны entity JSON: '+('; '.join(f'`{p}` ({e})' for p,e in errors) if errors else 'нет')+'. Сканирование исходных строк их всё равно включает, но определения и события из них не входят в кандидаты.',
         '- Повторные ключи: '+('; '.join(f'`{p}`: '+', '.join('`'+k+'`' for k in keys) for p,keys in dups) if dups else 'нет')+'. JSON5 оставляет последнее значение.',
         '- Подстроки не соответствующие ограниченным шаблонам: '+('; '.join(f'`{p}:{n}`' for p,n in unknown) if unknown else 'нет')+'.','']
    if ver=='2.x':out += ['Обе версии 2.x совпадают по выбранным исходным строкам, локальным именам/ID и списку ошибок, но не обязательно по содержимому самих событий или по другим командам. Например, `despawn` встречается в нескольких определениях; совпадение имени не означает одинакового действия.', '']
    out += ['| Файл / строка | Подстроки | Кандидаты в разобранных entity | Исходная строка |','|---|---|---|---|']
    for path,n,line,summons,events in calls:
        labels=[];candidates=[]
        for ident in summons:
            labels.append('summon '+ident);v=ids.get(ident,[]);candidates.append('summon '+ident+': '+(', '.join(v) if v else 'точное ID локально не найдено'))
        for sel,event in events:
            labels.append('event entity '+sel+' '+event);v=defs.get(event,[]);candidates.append('event '+event+': '+(', '.join(ident+' '+p for ident,p in v) if v else 'точное имя локально не найдено'))
        out.append(f'| `{path}:{n}` | '+'<br>'.join(code(x) for x in labels)+' | '+'<br>'.join(code(x) for x in candidates)+f' | {code(line)} |')
    out += ['',f'Полные события и фильтры: [реестр сущностей](entity-ledger-{ver if ver!="2.x" else "2.8.14"}.md); структурные ссылки событий — [event-поля](entity-event-fields-{ver}.md).', '']
    return '\n'.join(out)

def build_all():
    d={v:extract(f,p) for v,f,p in VERSIONS}
    if d['2.8.8']!=d['2.8.14']:raise ValueError('2.x command calls or exact-name entity candidates differ')
    return {'1.6':render('1.6','1.6',d['1.6']),'2.x':render('2.8.8 и 2.8.14','2.x',d['2.8.14'])}

def main():
    for ver,text in build_all().items():
        (ROOT/f'docs/command-entity-calls-{ver}.md').write_text(text,encoding='utf8');print(ver,len(text.splitlines()),'lines')
if __name__=='__main__':main()
