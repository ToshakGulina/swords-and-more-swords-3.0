#!/usr/bin/env python3
"""Create auditable indexes of behavior-pack entities in each supplied archive.
JSON5 interpretation is not a replacement for the original bytes or runtime tests.
"""
import json, zipfile
from pathlib import Path
import json5
from build_mechanics import event_tree, compact, line_numbers

ROOT=Path(__file__).resolve().parents[1]
VERSIONS=[('1.6','SwordsAndMoreSwords.1.6.mcaddon','Sword_B'), ('2.8.8','swordsandmoreswords_2_8_8.mcaddon','Swords_B'), ('2.8.14','swordsandmoreswords-2-8-14.mcaddon','Swords_B')]

def parse_with_duplicates(s):
    duplicates=[]
    def hook(pairs):
        out={}
        for key,val in pairs:
            if key in out: duplicates.append(key)
            out[key]=val
        return out
    return json5.loads(s,object_pairs_hook=hook),duplicates

def lines(text,key):
    return ','.join(line_numbers(text,'"'+key+'"')) or '?'

def run(version, filename, pack):
    with zipfile.ZipFile(ROOT/'sources'/filename) as z:
        files={name:z.read(name) for name in z.namelist() if name.startswith(pack+'/entities/') and name.endswith('.json')}
    out=[f'# Реестр поведения сущностей — архив {version}', '',
      f'Автоматический структурный разбор каждого JSON в `{pack}/entities/`: описание, все компоненты и группы в исходных значениях, все события как деревья шагов/условных ветвей. Номера строк — все текстовые вхождения ключа; это ориентир, не точная граница блока. Набор не доказывает связи конкретного объекта с конкретным предметом и не является ручной верификацией.', '',
      'Соседние поля одного объекта не упорядочены этим отчётом. Веса в randomize — только относительные доли данного выбора при всех явных неотрицательных целых весах; успех действия, фильтры, вложенные вероятности и запуск события отдельно. Для повторяющихся ключей и неразобранного JSON см. оригинал: информация JSON5-парсера может теряться.', '']
    for path,raw in sorted(files.items()):
        text=raw.decode('utf-8-sig')
        try: obj,duplicates=parse_with_duplicates(text)
        except Exception as exc:
            out += [f'## `{path}`', '', f'**Не разобран JSON5:** `{str(exc).splitlines()[0]}`. Исходник не изменять и изучать вручную.', '']; continue
        entity=obj.get('minecraft:entity',{})
        desc=entity.get('description',{})
        out += [f'## `{desc.get("identifier",path)}`', '',f'- Путь `{path}`; format_version `{compact(obj.get("format_version"))}`.',
                f'- description: `{compact(desc)}`.']
        if duplicates: out += [f'- **Повторяющиеся ключи: `{compact(duplicates)}`; следующие выписки могут потерять ранее встреченные значения. Обязательно читать исходник.**']
        out += ['', '### Постоянные компоненты', '']
        for name,val in entity.get('components',{}).items():
            out.append(f'- `{name}` (строки {lines(text,name)}): `{compact(val)}`')
        out += ['', '### Группы компонентов', '']
        for name,val in entity.get('component_groups',{}).items():
            out.append(f'- `{name}` (строки {lines(text,name)}): `{compact(val)}`')
        out += ['', '### События', '']
        for name,val in entity.get('events',{}).items():
            out += [f'**`{name}`** (строки {lines(text,name)}):','']
            event_tree(val,out); out.append('')
        for k,v in entity.items():
            if k not in ('description','components','component_groups','events'):
                out += [f'Другое поле `{k}`: `{compact(v)}`.', '']
    (ROOT/'docs'/f'entity-ledger-{version}.md').write_text('\n'.join(out)+'\n',encoding='utf-8')
    return len(files)

if __name__=='__main__':
    for args in VERSIONS: print(args[0], 'entity JSON:', run(*args))
