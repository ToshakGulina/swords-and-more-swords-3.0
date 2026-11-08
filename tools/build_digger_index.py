#!/usr/bin/env python3
"""Group exact item digger components and retain ordered destroy_speeds."""
from collections import defaultdict
from pathlib import Path
from zipfile import ZipFile
import json
import json5

ROOT=Path(__file__).resolve().parents[1]
VERSIONS=(('1.6','SwordsAndMoreSwords.1.6.mcaddon'),('2.8.8','swordsandmoreswords_2_8_8.mcaddon'),('2.8.14','swordsandmoreswords-2-8-14.mcaddon'))
ABSENT='<component absent>'
def compact(obj):return json.dumps(obj,ensure_ascii=False,sort_keys=True,separators=(',',':'))
def escape(s):return str(s).replace('|','\\|').replace('`','\\`').replace('\n',' ')

def collect():
    profiles={};members=defaultdict(lambda:defaultdict(list));diagnostics=[]
    for version,archive in VERSIONS:
        with ZipFile(ROOT/'sources'/archive) as z:
            for path in sorted(z.namelist()):
                if '_B/items/' not in path or not path.endswith('.json'):continue
                duplicate=[]
                def pairs(seq):
                    obj={}
                    for key,value in seq:
                        if key in obj:duplicate.append(key)
                        obj[key]=value
                    return obj
                try:raw=json5.loads(z.read(path).decode('utf-8-sig'),object_pairs_hook=pairs)['minecraft:item']
                except (ValueError,UnicodeDecodeError,KeyError) as e:
                    diagnostics.append((version,path,type(e).__name__));continue
                if duplicate:diagnostics.append((version,path,'duplicate keys: '+compact(duplicate)))
                components=raw.get('components',{});value=components['minecraft:digger'] if 'minecraft:digger' in components else ABSENT
                key=compact(value);profiles[key]=value
                members[key][version].append(raw.get('description',{}).get('identifier',path))
    return profiles,members,diagnostics

def build():
    profiles,members,diagnostics=collect()
    # Stable sequence by first appearance in archive-version ordering, then canonical JSON.
    keys=sorted(profiles,key=lambda k:(next((i for i,(v,_) in enumerate(VERSIONS) if members[k].get(v)),len(VERSIONS)),k))
    out=['# Правила добычи предметов: три исходные версии','',
         'Группировка буквальных `minecraft:digger` предметов из behavior pack. Профили равны только при одинаковой разобранной структуре компонента, включая порядок массива `destroy_speeds`; остальные свойства предметов могут различаться. Список правил Bedrock Sword сохранён в исходном порядке с повторами. Отсутствие компонента **не** означает скорость 0, запрет добычи или отсутствие ванильных значений. Механика блоков, приоритет пересекающихся правил, чары и `on_dig` требуют испытаний.', '',
         'Диагностика JSON5: '+('; '.join(f'{v} `{p}`: {e}' for v,p,e in diagnostics) if diagnostics else 'ошибки и повторные ключи не обнаружены')+'.', '',
         '| Профиль | 1.6 предметов | 2.8.8 предметов | 2.8.14 предметов |','|---|---:|---:|---:|']
    for i,k in enumerate(keys,1):out.append(f'| P{i:02d} | '+ ' | '.join(str(len(members[k].get(v,[]))) for v,_ in VERSIONS)+' |')
    for i,k in enumerate(keys,1):
        value=profiles[k];out += ['',f'## P{i:02d}','']
        for version,_ in VERSIONS:
            ids=sorted(members[k].get(version,[]))
            if ids:out.append(f'- **{version} ({len(ids)})**: '+', '.join('`'+escape(x)+'`' for x in ids)+'.')
        if value==ABSENT:
            out += ['', 'Компонент `minecraft:digger` не задан.'];continue
        if not isinstance(value,dict):
            out += ['',f'Буквальное значение: `{escape(compact(value))}`.'];continue
        other={key:val for key,val in value.items() if key!='destroy_speeds'}
        out += ['',f'Другие поля компонента: `{escape(compact(other))}`.', '', '| № | Блок / условие | Остальные поля правила |','|---:|---|---|']
        for j,rule in enumerate(value.get('destroy_speeds',[]),1):
            if isinstance(rule,dict):
                block=rule.get('block','<нет block>');other={key:val for key,val in rule.items() if key!='block'}
            else:block='<не объект>';other=rule
            out.append(f'| {j} | `{escape(compact(block))}` | `{escape(compact(other))}` |')
    return '\n'.join(out)+'\n'

def main():
    (ROOT/'docs/digger-index.md').write_text(build(),encoding='utf-8')
    print('digger index written')

if __name__=='__main__':main()
