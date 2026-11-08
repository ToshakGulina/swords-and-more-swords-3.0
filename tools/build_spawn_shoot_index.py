#!/usr/bin/env python3
"""Index declared spawn_entity and shoot targets, not commands or runtime effects."""
from collections import Counter,defaultdict
from pathlib import Path
from zipfile import ZipFile
import json,json5
from build_entity_group_index import VERSIONS
ROOT=Path(__file__).resolve().parents[1]

def compact(x):return json.dumps(x,ensure_ascii=False,separators=(',',':'))

def extract(filename,pack):
    entities=defaultdict(list);actions=[];errors=[];duplicates=[]
    with ZipFile(ROOT/'sources'/filename) as z:
        for path in sorted(z.namelist()):
            if not path.startswith(pack+'/') or not path.endswith('.json'):continue
            repeated=[]
            def pairs(seq):
                obj={}
                for k,v in seq:
                    if k in obj:repeated.append(k)
                    obj[k]=v
                return obj
            try:obj=json5.loads(z.read(path).decode('utf-8-sig'),object_pairs_hook=pairs)
            except (ValueError,UnicodeDecodeError) as ex:errors.append((path,str(ex).splitlines()[0]));continue
            if repeated:duplicates.append((path,repeated))
            if path.startswith(pack+'/entities/') and isinstance(obj.get('minecraft:entity'),dict):
                e=obj['minecraft:entity'];desc=e.get('description',{});ident=desc.get('identifier');groups=e.get('component_groups',{});base=e.get('components',{})
                if not isinstance(ident,str):raise ValueError('entity without id: '+path)
                projectiles=[]
                if 'minecraft:projectile' in base:projectiles.append('components')
                projectiles.extend('component_groups.'+k for k,v in groups.items() if 'minecraft:projectile' in v)
                entities[ident].append({'path':path,'description':desc,'projectiles':projectiles,'events':set(e.get('events',{}))})
            def walk(v,loc):
                if isinstance(v,dict):
                    if 'minecraft:spawn_entity' in v:
                        val=v['minecraft:spawn_entity'];array=val if isinstance(val,list) else [val]
                        for i,entry in enumerate(array):
                            if not isinstance(entry,dict) or not isinstance(entry.get('spawn_entity'),str):raise ValueError('unexpected spawn_entity at '+path+loc)
                            actions.append({'path':path,'location':loc+'.minecraft:spawn_entity'+(f'[{i}]' if isinstance(val,list) else ''),'kind':'spawn_entity','id':entry['spawn_entity'],'value':entry,'weight':None})
                    if 'shoot' in v:
                        val=v['shoot']
                        if not isinstance(val,dict) or not isinstance(val.get('projectile'),str):raise ValueError('unexpected shoot at '+path+loc)
                        actions.append({'path':path,'location':loc+'.shoot','kind':'shoot','id':val['projectile'],'value':val,'weight':v.get('weight')})
                    for key,x in v.items():walk(x,loc+'.'+key)
                elif isinstance(v,list):
                    for i,x in enumerate(v):walk(x,loc+f'[{i}]')
            walk(obj,'$')
    return dict(entities),actions,errors,duplicates

def local(entities,ident,spawn_event=None):
    defs=entities.get(ident,[])
    if not defs:return 'не найдено в разобранных файлах'
    parts=[]
    for d in defs:
        desc=d['description'];flags={k:desc[k] for k in ('runtime_identifier','is_spawnable','is_summonable','is_experimental') if k in desc}
        projectile=', '.join('`'+p+'`' for p in d['projectiles']) if d['projectiles'] else 'не объявлен в base/groups'
        event_note='' if spawn_event is None else '<br>spawn_event в локальном events: '+('да' if spawn_event in d['events'] else 'нет')
        parts.append('`'+d['path']+'`<br>`'+compact(flags)+'`<br>projectile: '+projectile+event_note)
    return '<br>'.join(parts)

def render(title,version,data):
    entities,actions,errors,dups=data;types=Counter(x['kind'] for x in actions)
    out=[f'# Прямые spawn_entity и item shoot — {title}', '',
         f'Машинная выписка разобранных JSON behavior pack: {types["spawn_entity"]} элементов компонента `minecraft:spawn_entity` и {types["shoot"]} объектов `shoot`. В строке сохранён объект целиком, а при `shoot` — вес непосредственно содержащего его объекта, если он задан. Родительские randomize/filters и условия включения группы указаны только через путь, **не вычисляются**. Нельзя считать вес общей вероятностью создания или попадания.', '',
         'Локальное определение ищется только по точному `description.identifier` в разобранных behavior `entities/*.json`. Его отсутствие не доказывает ошибки: сущность может быть ванильной, внешней или находиться в неразобранном файле. Команды `summon`, `ride`, projectile компоненты других видов, структуры, скрипты и события, создающие сущности косвенно, **не охвачены**. Например, `minecraft:creeper` 2.x описан в повреждённом файле; см. [диагностику](manual-creeper-sword.md).', '',
         'Projectile в колонке — только наличие компонента в base или именованной component_group, а не доказательство, что группа активна или что spawn/shoot возможен; `is_summonable`/`is_spawnable` тоже сохраняются как буквальные объявления, без разрешения движка. `spawn_event`, если присутствует, сопоставлен с локальными именами events записанной цели; это сравнение имён, а не доказательство адресата и успешного вызова.', '',
         '- Неразобранные файлы: '+('; '.join(f'`{p}` ({err})' for p,err in errors) if errors else 'нет')+'.',
         '- Повторные ключи разобранных JSON: '+('; '.join(f'`{p}`: '+', '.join('`'+x+'`' for x in names) for p,names in dups) if dups else 'нет')+'. JSON5 оставляет последнее значение.', '']
    if version=='2.8.14':out+=['В 2.8.8 и 2.8.14 записи этих двух видов и локальные сведения об их целях структурно совпадают. Другие действия и содержание файлов могут различаться.', '']
    out += ['| Источник и путь | Вид / цель | Буквальный объект; вес ближайшей ветви | Локальное определение цели |', '|---|---|---|---|']
    for a in actions:
        weight='; вес `'+compact(a['weight'])+'`' if a['weight'] is not None else '; вес не указан непосредственно рядом'
        out.append(f'| `{a["path"]}`<br>`{a["location"]}` | `{a["kind"]}`<br>`{a["id"]}` | `{compact(a["value"])}`'+(weight if a['kind']=='shoot' else '')+' | '+local(entities,a['id'],a['value'].get('spawn_event'))+' |')
    out += ['', f'Подробные исходные компоненты: [сущности {version}](entity-ledger-{version}.md), [предметы {version}](items-{version}.md), [weapon-хуки](weapon-event-index.md).', '']
    return '\n'.join(out)

def build_all():
    d={v:extract(f,p) for v,f,p in VERSIONS};a,b=d['2.8.8'],d['2.8.14']
    # Compare actions and only the referenced local target data, not unrelated entity declarations.
    if a[1:]!=b[1:] or any(a[0].get(x['id'])!=b[0].get(x['id']) for x in b[1]):raise ValueError('2.x direct spawn/shoot data differs')
    return {'1.6':render('1.6','1.6',d['1.6']),'2.x':render('2.8.8 и 2.8.14','2.8.14',d['2.8.14'])}

def main():
    for version,text in build_all().items():
        (ROOT/f'docs/spawn-shoot-index-{version}.md').write_text(text,encoding='utf-8');print(version,len(text.splitlines()),'lines')
if __name__=='__main__':main()
