#!/usr/bin/env python3
"""Inventory literal 'event' properties in behavior entities, not a runtime call graph."""
from collections import Counter,defaultdict
from pathlib import Path
from zipfile import ZipFile
import json5
from build_entity_group_index import VERSIONS
ROOT=Path(__file__).resolve().parents[1]

def extract(filename,pack):
    result={};errors=[];dups=[]
    with ZipFile(ROOT/'sources'/filename) as z:
        for path in sorted(z.namelist()):
            if not path.startswith(pack+'/entities/') or not path.endswith('.json'):continue
            repeated=[]
            def pairs(seq):
                out={}
                for k,v in seq:
                    if k in out:repeated.append(k)
                    out[k]=v
                return out
            try:ent=json5.loads(z.read(path).decode('utf-8-sig'),object_pairs_hook=pairs)['minecraft:entity']
            except (ValueError,UnicodeDecodeError) as ex:errors.append((path,str(ex).splitlines()[0]));continue
            if repeated:dups.append((path,repeated))
            identifier=ent['description']['identifier'];events=ent.get('events',{});refs=[]
            def walk(node,where):
                if isinstance(node,dict):
                    if 'event' in node:
                        if not isinstance(node['event'],str):raise ValueError('non-string event: '+path+' '+where)
                        if 'target' in node and not isinstance(node['target'],str):raise ValueError('non-string target: '+path+' '+where)
                        refs.append((where+'.event',node['event'],node.get('target')))
                    for k,v in node.items():walk(v,where+'.'+k)
                elif isinstance(node,list):
                    for i,v in enumerate(node):walk(v,where+f'[{i}]')
            walk(ent,'$');result[path]={'id':identifier,'events':set(events),'refs':refs}
    return result,errors,dups

def summary(records):
    targets=Counter();absent=Counter();total=0
    for rec in records.values():
        for path,event,target in rec['refs']:
            total+=1;targets[target]+=1
            if event not in rec['events']:absent[target]+=1
    return total,targets,absent

def render(title,version,data):
    records,errors,dups=data;total,targets,absent=summary(records)
    show=lambda x: 'не указан' if x is None else '`'+x+'`'
    out=[f'# Буквальные поля event в behavior-сущностях — {title}', '',
         f'Поиск значений свойства `event`, являющихся строкой, во всём объекте `minecraft:entity`: разобранных файлов {len(records)}, вхождений {total}. Это **не полный граф вызовов**: `spawn_event`, строковые команды `event entity`, анимационные контроллеры, внешние вызовы, ванильные правила и динамическое разрешение не входят в этот поиск.', '',
         'Колонка локального объявления только проверяет наличие имени среди `events` **того же файла**, независимо от `target`. Она не определяет объект-адресат, фактическое исполнение или отсутствие события в игре: в частности, target `block` и `baby` не следует автоматически проверять как self. Если target не задан, его дефолт здесь не предположен. Само имя `self` не гарантирует, какой объект движок выберет в каждом контексте. Повторные ключи JSON5 сводит к последнему значению; неразобранные файлы исключены.', '',
         'Вхождения по буквально записанному target: '+', '.join(f'{show(k)} — {targets[k]}' for k in sorted(targets,key=lambda x:(x is not None,x or '')))+'.',
         'Из них вхождений с именем, отсутствующим в локальном `events`: '+(', '.join(f'{show(k)} — {absent[k]}' for k in sorted(absent,key=lambda x:(x is not None,x or ''))) if absent else 'нет')+'. Эти числа не являются количеством ошибок.', '',
         '- Неразобранные файлы: '+('; '.join(f'`{p}` ({err})' for p,err in errors) if errors else 'нет')+'.',
         '- Повторные ключи: '+('; '.join(f'`{p}`: '+', '.join('`'+k+'`' for k in ks) for p,ks in dups) if dups else 'нет')+'.', '']
    if version=='2.8.14':out+=['Сопоставление 2.8.x: имена локальных событий и все найденные поля `event`, их пути и target совпадают. Сами тела событий и другие части сущностей полностью не сравнивались.', '']
    out += ['| Файл / ID | Значение event | target | Локально объявлено имя | Буквальные пути |', '|---|---|---|---|---|']
    for path,rec in records.items():
        grouped=defaultdict(list)
        for loc,event,target in rec['refs']:grouped[(event,target)].append(loc)
        for (event,target),paths in sorted(grouped.items(),key=lambda x:(x[0][0],x[0][1] or '')):
            out.append(f'| `{path}`<br>`{rec["id"]}` | `{event}` | {show(target)} | {"да" if event in rec["events"] else "нет"} | '+ '<br>'.join('`'+p+'`' for p in paths)+' |')
    out += ['', f'Полные объявления и условия: [реестр сущностей {version}](entity-ledger-{version}.md); отдельный [индекс групп](entity-groups-{("1.6" if version=="1.6" else "2.x")}.md).', '']
    return '\n'.join(out)

def build_all():
    d={v:extract(f,p) for v,f,p in VERSIONS}
    if d['2.8.8']!=d['2.8.14']:raise ValueError('2.x literal event references differ')
    return {'1.6':render('1.6','1.6',d['1.6']),'2.x':render('2.8.8 и 2.8.14','2.8.14',d['2.8.14'])}

def main():
    for version,text in build_all().items():
        (ROOT/f'docs/entity-event-fields-{version}.md').write_text(text,encoding='utf-8');print(version,len(text.splitlines()),'lines')
if __name__=='__main__':main()
