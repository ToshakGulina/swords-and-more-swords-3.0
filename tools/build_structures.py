#!/usr/bin/env python3
"""Decode supplied Bedrock structure NBT and cross-reference literal load commands.
Requires nbtlib==2.0.4. Original bytes in sources/ remain authoritative.
"""
import hashlib, io, re, zipfile
from pathlib import Path
import nbtlib
from nbtlib.tag import Compound, List, String

ROOT=Path(__file__).resolve().parents[1]
VERSIONS=[('2.8.8','swordsandmoreswords_2_8_8.mcaddon'),('2.8.14','swordsandmoreswords-2-8-14.mcaddon')]

def item_paths(node,path='$'):
    result=[]
    if isinstance(node,Compound):
        value=node.get('Name')
        if isinstance(value,String) and str(value).startswith(('effect:', 'effect99:')):
            result.append((path+'.Name',str(value)))
        for key,value in node.items():
            result.extend(item_paths(value,f'{path}.{key}'))
    elif isinstance(node,List):
        for i,value in enumerate(node): result.extend(item_paths(value,f'{path}[{i}]'))
    return result

def main():
    for version,archive in VERSIONS:
        with zipfile.ZipFile(ROOT/'sources'/archive) as z:
            files={p:z.read(p) for p in z.namelist() if not p.endswith('/')}
        refs={}
        for p,raw in files.items():
            if not p.endswith(('.json','.mcfunction','.js')): continue
            try: text=raw.decode('utf-8-sig')
            except UnicodeDecodeError: continue
            for i,line in enumerate(text.splitlines(),1):
                for m in re.finditer(r'\bstructure\s+load\s+([A-Za-z0-9_./:-]+)',line):
                    refs.setdefault(m.group(1),[]).append((p,i,line.strip()))
        structures={p.split('/structures/',1)[1][:-len('.mcstructure')]:p for p in files if '/structures/' in p and p.endswith('.mcstructure')}
        out=[f'# Двоичные структуры — архив {version}', '',
          f'Источник: `{archive}`. Каждая структура ниже прочитана как little-endian NBT и выведена в типизированном SNBT. Преобразование SNBT → NBT проверено побайтово для каждого файла; оригинал архива остаётся основным источником.', '',
          'Список вызовов ищется только по буквальному тексту `structure load` в JSON, JS и mcfunction. Синтаксис и успешность команд, динамические имена, другие пакеты и структуры из мира не проверяются. Пустой список вызовов не доказывает, что структура не используется.', '',
          '## Буквальные ссылки без одноимённого файла в архиве', '']
        missing=sorted(set(refs)-set(structures))
        if not missing: out += ['- Не обнаружено буквальных ссылок без файла.','']
        for name in missing:
            out += [f'- `{name}`: в архиве нет `*/structures/{name}.mcstructure`; возможна внешняя структура или другой способ разрешения имени.']
            out += [f'  - `{p}:{n}` — `{line}`' for p,n,line in refs[name]]
        out.append('')
        for name,p in sorted(structures.items()):
            raw=files[p]; nbt=nbtlib.File.parse(io.BytesIO(raw),byteorder='little')
            snbt=nbt.snbt(indent=2)
            rebuilt=nbtlib.File(nbtlib.parse_nbt(snbt),root_name=nbt.root_name)
            roundtrip=io.BytesIO(); rebuilt.write(roundtrip,byteorder='little')
            if roundtrip.getvalue()!=raw: raise ValueError(f'NBT round trip mismatch: {archive}:{p}')
            structure=nbt['structure']; entities=structure.get('entities',[])
            items=item_paths(structure)
            size=nbt.get('size'); origin=nbt.get('structure_world_origin')
            out += [f'## `{name}`', '', f'- Путь `{p}`; MD5 `{hashlib.md5(raw).hexdigest()}`; NBT round-trip: побайтово совпал.',
                    f'- Размер `{size.snbt() if size else "не задан"}`; structure_world_origin `{origin.snbt() if origin else "не задан"}`; сущностей {len(entities)}.',
                    '- Сущности: '+(', '.join(f'`{str(e.get("identifier","(не указан)"))}`' for e in entities) if entities else 'нет')+'.',
                    '- Предметы с `Name` в пространствах `effect:` / `effect99:`:']
            out += [f'  - `{path}`: `{item}`' for path,item in items] or ['  - Не найдены.']
            out += ['- Буквальные вызовы:']
            out += [f'  - `{source}:{line}` — `{cmd}`' for source,line,cmd in refs.get(name,[])] or ['  - Не найдены.']
            out += ['', '### Полный типизированный SNBT', '', '```snbt',snbt,'```','']
        (ROOT/'docs'/f'structures-{version}.md').write_text('\n'.join(out)+'\n',encoding='utf-8')
        print(version, 'структур:',len(structures),'буквально упомянутых имён без файла:',missing)

if __name__=='__main__': main()
