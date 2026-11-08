#!/usr/bin/env python3
"""Index literal entity component-group declarations and event add/remove references."""
from collections import defaultdict
from pathlib import Path
from zipfile import ZipFile
import json5

ROOT=Path(__file__).resolve().parents[1]
VERSIONS=(('1.6','SwordsAndMoreSwords.1.6.mcaddon','Sword_B'),('2.8.8','swordsandmoreswords_2_8_8.mcaddon','Swords_B'),('2.8.14','swordsandmoreswords-2-8-14.mcaddon','Swords_B'))

def extract(filename,pack):
    records={};errors=[];duplicates=[]
    with ZipFile(ROOT/'sources'/filename) as z:
        for path in sorted(z.namelist()):
            if not path.startswith(pack+'/entities/') or not path.endswith('.json'):continue
            dup=[]
            def pairs(pairs):
                out={}
                for k,v in pairs:
                    if k in out:dup.append(k)
                    out[k]=v
                return out
            try:obj=json5.loads(z.read(path).decode('utf-8-sig'),object_pairs_hook=pairs)
            except (ValueError,UnicodeDecodeError) as ex:
                errors.append((path,str(ex).splitlines()[0]));continue
            if dup:duplicates.append((path,dup))
            entity=obj.get('minecraft:entity')
            if not isinstance(entity,dict):raise ValueError('not a minecraft:entity: '+path)
            groups=entity.get('component_groups',{});events=entity.get('events',{});ident=entity.get('description',{}).get('identifier')
            if not isinstance(groups,dict) or not isinstance(events,dict) or not isinstance(ident,str):raise ValueError('unexpected entity shape: '+path)
            refs=defaultdict(lambda:{'add':[],'remove':[]})
            def walk(node,where):
                if isinstance(node,dict):
                    for action in ('add','remove'):
                        value=node.get(action)
                        if not isinstance(value,dict) or 'component_groups' not in value:continue
                        names=value['component_groups']
                        if not isinstance(names,list) or any(not isinstance(x,str) for x in names):raise ValueError('unexpected group reference: '+path+' '+where)
                        if set(value)!={'component_groups'}:raise ValueError('unsupported group action fields: '+path+' '+where)
                        for i,name in enumerate(names):refs[name][action].append(where+'.'+action+f'.component_groups[{i}]')
                    for key,value in node.items():walk(value,where+'.'+key)
                elif isinstance(node,list):
                    for i,value in enumerate(node):walk(value,where+f'[{i}]')
            for event,value in events.items():walk(value,'$.events.'+event)
            records[path]={'id':ident,'groups':groups,'events_count':len(events),'refs':dict(refs)}
    return records,errors,duplicates

def counts(records):
    out={'entities':len(records),'events':0,'declared':0,'add_only':0,'remove_only':0,'neither':0,'unknown':0,'add_refs':0,'remove_refs':0}
    for rec in records.values():
        groups,refs=rec['groups'],rec['refs'];out['events']+=rec['events_count'];out['declared']+=len(groups)
        out['unknown']+=len(set(refs)-set(groups))
        for value in refs.values():out['add_refs']+=len(value['add']);out['remove_refs']+=len(value['remove'])
        for group in groups:
            value=refs.get(group,{'add':[],'remove':[]});a=bool(value['add']);r=bool(value['remove'])
            out['add_only']+=a and not r;out['remove_only']+=r and not a;out['neither']+=not a and not r
    return out

def render(title,version,data):
    records,errors,dups=data;c=counts(records)
    out=[f'# Группы всех разбираемых behavior-сущностей — {title}', '',
         f'Включены все файлы `entities/*.json` behavior pack, в том числе `minecraft:player`: разобранных файлов: **{c["entities"]}**, локальных групп: **{c["declared"]}**, объявлений событий: **{c["events"]}**; неразобранные файлы перечислены ниже. Для каждого файла извлечены объявления и буквальные операции `add.component_groups` / `remove.component_groups` внутри его `events`, включая вложенные sequence/randomize. Путь содержит индекс элемента массива и не доказывает, что событие вызвано или ветвь прошла фильтры.', '',
         'Это не полный граф событий: команды `event entity`, внешние вызовы, vanilla/runtime, загрузка сохранённых состояний, отсутствующие файлы, наследование и другие способы включения групп не интерпретируются. Поэтому отсутствие локальных add/remove **не означает** неиспользуемость или постоянное действие; порядок выполнения и разрешение конфликтов компонентов не устанавливаются. Ссылки на необъявленные группы — диагностические наблюдения, а не доказанные ошибки Bedrock. Названия компонентов в таблице приведены только для ориентации; значения — в оригинале и реестре сущностей.', '',
         f'Объявленные локальные группы: только add — {c["add_only"]}; только remove — {c["remove_only"]}; ни add ни remove — {c["neither"]}. Имена групп, упомянутые в событиях, но не объявленные в том же файле: {c["unknown"]}. Это количество **имён на файл**, не отдельных вызовов; всего элементов ссылок add {c["add_refs"]}, remove {c["remove_refs"]}.', '',
         '- Неразобранные файлы: '+('; '.join(f'`{p}` ({err})' for p,err in errors) if errors else 'нет')+'.',
         '- Повторяющиеся ключи в разобранных файлах: '+('; '.join(f'`{p}`: '+', '.join('`'+k+'`' for k in keys) for p,keys in dups) if dups else 'нет')+'. JSON5 в таких объектах оставляет последнее значение; оригинал необходимо читать отдельно.', '']
    if version=='2.8.14':out += ['Сравнение 2.8.8/2.8.14: локальные объявления групп (включая их разобранные значения), количество событий и пути add/remove совпадают для всех разобранных файлов. Это **не** сравнение полных событий или прочих полей сущностей; например, `player.json` различается.', '']
    out += ['| Файл и локальный ID | Группа | Компоненты группы | add: пути внутри события | remove: пути внутри события |', '|---|---|---|---|---|']
    fmt=lambda v: '<br>'.join('`'+x+'`' for x in v) if v else '—'
    for path,rec in records.items():
        groups,refs=rec['groups'],rec['refs']
        for name in sorted(set(groups)|set(refs)):
            obj=groups.get(name);r=refs.get(name,{'add':[],'remove':[]})
            if name not in groups:components='**не объявлена локально**'
            elif isinstance(obj,dict):components=fmt(list(obj))
            else:raise ValueError('unexpected group definition '+path+' '+name)
            out.append(f'| `{path}`<br>`{rec["id"]}` | `{name}` | {components} | {fmt(r["add"])} | {fmt(r["remove"])} |')
    out += ['', f'Полные объекты и буквальные события: [реестр сущностей {version}](entity-ledger-{version}.md); для player отдельно — [индекс групп](player-groups-{version}.md).', '']
    return '\n'.join(out)

def build_all():
    data={v:extract(f,p) for v,f,p in VERSIONS}
    # Error text names the same file paths; pair list ordering is deterministic.
    if data['2.8.8']!=data['2.8.14']:raise ValueError('2.x group inventory differs: render separate indexes rather than asserting equality')
    return {'1.6':render('1.6','1.6',data['1.6']),'2.x':render('2.8.8 и 2.8.14','2.8.14',data['2.8.14'])}

def main():
    for version,text in build_all().items():
        (ROOT/f'docs/entity-groups-{version}.md').write_text(text,encoding='utf-8');print(version,len(text.splitlines()),'lines')
if __name__=='__main__':main()
