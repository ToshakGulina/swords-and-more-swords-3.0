#!/usr/bin/env python3
"""Extract literal projectile component objects from parsed behavior entities."""
from pathlib import Path
from zipfile import ZipFile
import json,json5
from build_entity_group_index import VERSIONS
ROOT=Path(__file__).resolve().parents[1]

def extract(filename,pack):
    records=[];errors=[];duplicates=[];entities=0
    with ZipFile(ROOT/'sources'/filename) as z:
        for path in sorted(z.namelist()):
            if not path.startswith(pack+'/entities/') or not path.endswith('.json'):continue
            dup=[]
            def pairs(values):
                result={}
                for k,v in values:
                    if k in result:dup.append(k)
                    result[k]=v
                return result
            try:e=json5.loads(z.read(path).decode('utf-8-sig'),object_pairs_hook=pairs)['minecraft:entity']
            except (ValueError,UnicodeDecodeError) as ex:errors.append((path,str(ex).splitlines()[0]));continue
            entities+=1
            if dup:duplicates.append((path,dup))
            ident=e['description']['identifier'];c=e.get('components',{});groups=e.get('component_groups',{})
            if 'minecraft:projectile' in c:records.append((path,ident,'components',c['minecraft:projectile']))
            for name,group in groups.items():
                if 'minecraft:projectile' in group:records.append((path,ident,'component_groups.'+name,group['minecraft:projectile']))
    return records,errors,duplicates,entities

def build_all():
    d={v:extract(f,p) for v,f,p in VERSIONS}
    if d['2.8.8']!=d['2.8.14']:raise ValueError('2.x projectile component data differs')
    out=['# Компоненты projectile: полные буквальные параметры 1.6 и 2.x', '',
         'Из разобранных behavior `entities/*.json` извлечены только объекты `minecraft:projectile` в базовых `components` и непосредственных `component_groups`; полное содержимое каждого объекта сохранено в таблице, включая `on_hit`. Это не реестр всех снарядов движка: shooter, item shoot, spawn_entity, команды summon, runtime- и ванильные сущности рассматриваются отдельно. [Прямые цели spawn/shoot 1.6](spawn-shoot-index-1.6.md) · [2.x](spawn-shoot-index-2.x.md).', '',
         f'1.6: разобрано {d["1.6"][3]} файлов, projectile-объектов {len(d["1.6"][0])}; это не означает отсутствия стрел и shooter, а три неразобранных helper-файла исключены. 2.x: разобран {d["2.8.14"][3]} файл, {len(d["2.8.14"][0])} объектов в {len(set(x[0] for x in d["2.8.14"][0]))} файлах. Эти объекты и их расположение совпадают в 2.8.8 и 2.8.14; прочие части файлов и события отдельно не сравнивались.', '',
         'Отсутствующий ключ не равен нулю/false: действующие дефолты зависят от движка. Несколько `on_hit` полей — соседние поля одного объекта, их последовательность и фактическое исполнение не установлены. Базовая и групповая записи показаны отдельно; какая запись активна, как разрешаются конфликты и как item `launch_power` взаимодействует с projectile `power`, нужно испытать. Здесь не подставляются отсутствующие компоненты, диапазоны или единицы.', '',
         '- Неразобранные файлы 1.6: '+', '.join(f'`{p}`' for p,_ in d['1.6'][1])+'.',
         '- Неразобранный файл 2.x: '+', '.join(f'`{p}`' for p,_ in d['2.8.14'][1])+'. Там есть текст mini-creeper projectile, дополнительно см. [диагностическую трассу](manual-creeper-sword.md); в таблицу гипотетически исправленный файл **не включён**.',
         '- Повторные ключи 2.x: '+('; '.join(f'`{p}`: '+', '.join('`'+k+'`' for k in ks) for p,ks in d['2.8.14'][2]))+'. JSON5 сохраняет последнее значение.', '',
         '| Файл / ID | Расположение | Исходный projectile-объект |', '|---|---|---|']
    for path,ident,where,value in d['2.8.14'][0]:
        obj=json.dumps(value,ensure_ascii=False,separators=(',',':')).replace('|','\\|').replace('`','\\`')
        out.append(f'| `{path}`<br>`{ident}` | `{where}` | `{obj}` |')
    out += ['', 'Дополнительные компоненты сущностей, фильтры событий и поведение при выборе группы: [реестр 2.8.14](entity-ledger-2.8.14.md), [группы 2.x](entity-groups-2.x.md), [поля event](entity-event-fields-2.x.md).', '']
    return '\n'.join(out)

def main():
    text=build_all();(ROOT/'docs/projectile-component-index.md').write_text(text,encoding='utf-8');print('projectile component index written')
if __name__=='__main__':main()
