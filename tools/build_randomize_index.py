#!/usr/bin/env python3
"""Index literal behavior-pack randomize lists, without interpreting Bedrock filters."""
import json
import zipfile
from pathlib import Path
import json5

ROOT=Path(__file__).resolve().parents[1]
VERSIONS=[('1.6','SwordsAndMoreSwords.1.6.mcaddon','Sword_B'),('2.8.8','swordsandmoreswords_2_8_8.mcaddon','Swords_B'),('2.8.14','swordsandmoreswords-2-8-14.mcaddon','Swords_B')]

def compact(x):
    return json.dumps(x,ensure_ascii=False,separators=(',',':'))

def collect(obj,path='$'):
    if isinstance(obj,dict):
        if 'randomize' in obj:
            yield path+'.randomize',obj['randomize']
        for key,value in obj.items():
            yield from collect(value,path+'.'+key)
    elif isinstance(obj,list):
        for i,value in enumerate(obj):
            yield from collect(value,f'{path}[{i}]')

def extract(filename,pack):
    found={};errors=[];duplicates=[]
    with zipfile.ZipFile(ROOT/'sources'/filename) as z:
        for path in sorted(z.namelist()):
            if not path.startswith(pack+'/') or not path.endswith('.json'):continue
            repeated=[]
            def pairs(items):
                out={}
                for key,value in items:
                    if key in out:repeated.append(key)
                    out[key]=value
                return out
            try:
                obj=json5.loads(z.read(path).decode('utf-8-sig'),object_pairs_hook=pairs)
            except (ValueError,UnicodeDecodeError) as exc:
                errors.append((path,str(exc).splitlines()[0]));continue
            if repeated:duplicates.append((path,repeated))
            for loc,branches in collect(obj):found[(path,loc)]=branches
    return found,errors,duplicates

def table(out,version,records):
    out += [f'## {version}', '', f'Найдено списков: {len(records)}.', '',
            '| Исходный файл | Путь к `randomize` | Веса → сумма | Поля веток в исходном порядке |',
            '|---|---|---|---|']
    for (source,path),branches in sorted(records.items()):
        if not isinstance(branches,list):
            out.append(f'| `{source}` | `{path}` | не список | `{compact(branches)}` |');continue
        weights=[b.get('weight') if isinstance(b,dict) else None for b in branches]
        valid=bool(weights) and all(isinstance(w,int) and not isinstance(w,bool) and w>=0 for w in weights) and sum(weights)>0
        shapes=[]
        for b in branches:
            if not isinstance(b,dict):shapes.append(compact(b));continue
            parts=[k for k in b if k not in ('weight','filters')]
            desc='+'.join(parts) if parts else 'пусто'
            if 'filters' in b:desc+='; filters='+compact(b['filters'])
            shapes.append(desc)
        out.append(f'| `{source}` | `{path}` | `{compact(weights)}` → '+(str(sum(weights)) if valid else 'не вычислена')+' | '+ '; '.join(f'`{x}`' for x in shapes)+' |')
    out.append('')

def main():
    data={}
    for version,filename,pack in VERSIONS:data[version]=extract(filename,pack)
    out=['# Где в исходниках используется randomize','',
         'Автоматический указатель по разобранным JSON behavior pack. Порядок и вес каждой ветви, сумма только явно заданных целых неотрицательных весов и названия полей ветки приведены без вывода о фактическом исполнении. Сумма и отношение weight/сумма — только сырой относительный вес; фильтры, внешние события, выбор сущностей, вложенные randomize и их порядок могут изменить результат. Соседние поля не считаются последовательностью. Подробности — в исходном архиве и ручных карточках.', '',
         'Это НЕ реестр всех источников случайности: loot `random_chance_with_looting`, веса пулов, timers, spawn weights, JS `Math.random`, команды и дефолты движка рассматриваются отдельно. Не разбирающиеся файлы и повторные ключи требуют чтения оригинала: JSON5 сохраняет последний ключ. В неразобранном creeper 2.x отдельно присутствует ветвь 95/5, см. [диагностическую трассу](manual-creeper-sword.md).', '', '## Диагностика разбора', '']
    for version in data:
        records,errors,dups=data[version]
        out.append(f'- {version}: {len(records)} списков; не разобраны '+(', '.join(f'`{p}`' for p,_ in errors) if errors else 'нет')+'; повторные ключи '+(', '.join(f'`{p}` ({compact(v)})' for p,v in dups) if dups else 'нет')+'.')
    out += ['', 'Сопоставление 2.8.x: '+('все распознанные пути и сами массивы ветвей равны структурно; окружающий код и фактические триггеры отдельно не сравниваются.' if data['2.8.8'][0]==data['2.8.14'][0] else 'найдены различия в путях или массивах — обе таблицы приведены ниже.') ,'']
    table(out,'1.6',data['1.6'][0])
    if data['2.8.8'][0]==data['2.8.14'][0]:table(out,'2.8.8 и 2.8.14',data['2.8.14'][0])
    else:
        table(out,'2.8.8',data['2.8.8'][0]);table(out,'2.8.14',data['2.8.14'][0])
    (ROOT/'docs/randomize-index.md').write_text('\n'.join(out)+'\n',encoding='utf-8')
    print(', '.join(f'{version}: {len(data[version][0])}' for version in data))

if __name__=='__main__':main()
