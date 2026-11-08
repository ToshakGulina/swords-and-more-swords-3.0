#!/usr/bin/env python3
"""Check selected declaration IDs within each pack and summarize manifest IDs."""
from collections import Counter,defaultdict
from pathlib import Path
from zipfile import ZipFile
import json
import json5

ROOT=Path(__file__).resolve().parents[1]
VERSIONS=(('1.6','SwordsAndMoreSwords.1.6.mcaddon'),('2.8.8','swordsandmoreswords_2_8_8.mcaddon'),('2.8.14','swordsandmoreswords-2-8-14.mcaddon'))
def compact(x):return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'))

def collect(filename):
    records=[];errors=[];duplicates=[];manifests=[]
    with ZipFile(ROOT/'sources'/filename) as z:
        for path in sorted(z.namelist()):
            if not path.endswith('.json'):continue
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
            if path.endswith('/manifest.json'):manifests.append((path,obj))
            if not isinstance(obj,dict):continue
            for root,value in obj.items():
                if not isinstance(value,dict) or not isinstance(value.get('description'),dict):continue
                ident=value['description'].get('identifier')
                if not isinstance(ident,str):continue
                # Cross-check recipe types together: the actual registry namespace is not assumed.
                kind='minecraft:recipe_*' if root.startswith('minecraft:recipe_') else root
                records.append((path.split('/')[0],kind,ident,root,path))
    return records,errors,duplicates,manifests

def build():
    out=['# Локальные объявления ID и манифесты трёх архивов','',
         'Механический поиск `description.identifier` в корневых объектах разбираемых JSON каждого пакета отдельно. Рецепты разных видов объединены для дополнительной проверки, но реальный namespace регистрации определяется движком. **Совпадающий ID не доказывает ошибку**, победителя или запуск: версии client entity могут быть намеренными вариантами. Behavior и resource пакеты не смешаны. Не охвачены ресурсы без `description.identifier`, наборы geometry/animation/controllers, ванильные пакеты, неизвестные форматы, динамические объявления и неразобранные файлы. Повторные ключи JSON5 сохраняют последнее значение. Таблица не является доказательством загрузки.', '']
    for version,filename in VERSIONS:
        records,errors,dups,manifests=collect(filename)
        groups=defaultdict(list)
        for pack,kind,ident,root,path in records:groups[(pack,kind,ident)].append((root,path))
        collisions={key:vals for key,vals in groups.items() if len(vals)>1}
        out += [f'## {version}', '', f'Разобрано объявлений: {len(records)}; отдельных групп pack/вид/ID: {len(groups)}; групп с повтором: {len(collisions)}.', '',
                '- Неразобранные JSON: '+(', '.join('`'+p+'`' for p,_ in errors) if errors else 'нет')+'.',
                '- Повторные ключи JSON: '+(', '.join('`'+p+'`: `'+compact(keys)+'`' for p,keys in dups) if dups else 'нет')+'.', '',
                '### Пакеты и типы', '', '| Пакет | Категория объявления | Количество |','|---|---|---:|']
        for (pack,kind),count in sorted(Counter((r[0],r[1]) for r in records).items()):out.append(f'| `{pack}` | `{kind}` | {count} |')
        out += ['', '### Повторённые ID внутри одного пакета', '']
        if not collisions:out.append('Не обнаружено в указанном ограниченном поиске.')
        else:
            for (pack,kind,ident),paths in sorted(collisions.items()):
                out += [f'- `{pack}` · `{kind}` · `{ident}`: '+', '.join(f'`{path}` ({root})' for root,path in paths)+'.']
        out += ['', '### Манифесты', '']
        for path,m in manifests:
            header=m.get('header',{});modules=m.get('modules',[]);deps=m.get('dependencies',[])
            min_engine=compact(header['min_engine_version']) if 'min_engine_version' in header else 'не задан'
            module_fields=[{k:x.get(k) for k in ('type','uuid','version','entry') if k in x} for x in modules]
            out += [f'- `{path}`: header UUID `{header.get("uuid")}`, version `{compact(header.get("version"))}`, min_engine_version `{min_engine}`.',
                    f'  - modules: `{compact(module_fields)}`.',
                    f'  - dependencies: `{compact(deps)}`.']
        out.append('')
    return '\n'.join(out)+'\n'

def main():
    (ROOT/'docs/definition-audit.md').write_text(build(),encoding='utf-8')
    print('definition audit written')

if __name__=='__main__':main()
