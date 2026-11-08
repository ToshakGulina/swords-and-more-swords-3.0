#!/usr/bin/env python3
"""Complete literal combat/vital component objects from valid entity definitions."""
from pathlib import Path
from zipfile import ZipFile
from collections import Counter
import json,json5
from build_entity_group_index import VERSIONS
ROOT=Path(__file__).resolve().parents[1]
KEYS=('minecraft:damage_sensor','minecraft:health','minecraft:attack','minecraft:attack_damage','minecraft:explode','minecraft:fire_immune','minecraft:breathable','minecraft:knockback_resistance','minecraft:hurt_on_condition','minecraft:on_death','minecraft:on_hurt')

def extract(filename,pack,keys=KEYS):
    rows=[];errors=[];duplicates=[];entity_count=0
    with ZipFile(ROOT/'sources'/filename) as z:
        for path in sorted(z.namelist()):
            if not path.startswith(pack+'/entities/') or not path.endswith('.json'):continue
            repeated=[]
            def pairs(seq):
                obj={}
                for k,v in seq:
                    if k in obj:repeated.append(k)
                    obj[k]=v
                return obj
            try:e=json5.loads(z.read(path).decode('utf-8-sig'),object_pairs_hook=pairs)['minecraft:entity']
            except (ValueError,KeyError) as err:errors.append((path,str(err).splitlines()[0]));continue
            entity_count+=1
            if repeated:duplicates.append((path,tuple(repeated)))
            ident=e['description']['identifier'];groups=e.get('component_groups',{});components=e.get('components',{})
            if not isinstance(components,dict) or not isinstance(groups,dict):raise ValueError('unexpected entity components '+path)
            for loc,obj in [('$.minecraft:entity.components',components)]+[('$.minecraft:entity.component_groups.'+k,v) for k,v in groups.items()]:
                if not isinstance(obj,dict):raise ValueError('unexpected component group '+path+' '+loc)
                for key,value in obj.items():
                    if key in keys:rows.append((path,ident,loc+'.'+key,key,value))
    return rows,errors,duplicates,entity_count

def code(value):return '`'+json.dumps(value,ensure_ascii=False,separators=(',',':')).replace('|','\\|').replace('`','\\u0060')+'`'

def render(title,ver,data):
    rows,errors,duplicates,files=data;counts=Counter(x[3] for x in rows);touched=len({r[0] for r in rows})
    out=[f'# Компоненты боя и уязвимости сущностей — {title}', '',
         f'Из **{files}** разобранных behavior entity файлов выбраны все значения {len(KEYS)} точных ключей только в базовом `components` и объявленных `component_groups`: **{len(rows)} объектов/значений**, файлов с выбранным ключом — {touched}. Сохранены целые объекты, вложенные triggers и filters, списки и порядок. Близко называющиеся события `minecraft:explode` не принимаются за одноимённый компонент.', '',
         'Это индекс **деклараций**, не итоговые характеристики: группа может быть неактивна, несколько групп могут задавать конфликтующие компоненты, события могут не вызываться, target и контекст определяются отдельно. `damage_sensor`, `hurt_on_condition` и `on_death` не дают полного графа последствий. Значения health относятся к сущностям, а не к прочности предмета. Отсутствующее поле не означает false, ноль, иммунитет либо непробиваемость. Источники ошибок/повторов ниже; поведение движка, vanilla/runtime и внешние пакеты не устанавливаются.', '',
         'Число вхождений выбранных ключей: '+', '.join(f'`{k}` — {counts[k]}' for k in KEYS)+'.', '',
         '- Исключены неразобранные файлы: '+('; '.join(f'`{p}` ({e})' for p,e in errors) if errors else 'нет')+'. '+('Для Creeper 2.x есть отдельная [диагностика](manual-creeper-sword.md); безусловно считать его отсутствующим нельзя.' if ver=='2.x' else 'Для трёх helper-файлов есть [отдельная диагностика](manual-traces-1.6.md#что-написано-в-повреждённых-helper-файлах).'),
         '- Дублирующиеся ключи: '+('; '.join(f'`{p}`: '+', '.join('`'+k+'`' for k in names) for p,names in duplicates) if duplicates else 'нет')+'. JSON5 сохраняет последнее значение, поэтому оригинал обязателен для спорных мест.','']
    if ver=='2.x':out += ['Выбранные объекты, имена, пути и список ошибок в 2.8.8/2.8.14 совпадают; это не сравнение всех остальных компонентов или событий.', '']
    out += ['| Файл / ID | Область и ключ | Полное разобранное значение |', '|---|---|---|']
    for path,ident,loc,key,value in rows:out.append(f'| `{path}`<br>`{ident}` | `{loc}` | {code(value)} |')
    out += ['',f'Дополнительный контекст: [полные сущности](entity-ledger-{ver if ver!="2.x" else "2.8.14"}.md), [группы](entity-groups-{ver}.md), [снаряды](projectile-component-index.md), [эффекты](effect-index-{ver}.md), [события](entity-event-fields-{ver}.md).', '']
    return '\n'.join(out)

def build_all():
    d={v:extract(f,p) for v,f,p in VERSIONS}
    if d['2.8.8']!=d['2.8.14']:raise ValueError('2.x combat component definitions differ')
    return {'1.6':render('1.6','1.6',d['1.6']),'2.x':render('2.8.8 и 2.8.14','2.x',d['2.8.14'])}

def main():
    for ver,text in build_all().items():
        (ROOT/f'docs/entity-combat-index-{ver}.md').write_text(text,encoding='utf8');print(ver,len(text.splitlines()),'lines')
if __name__=='__main__':main()
