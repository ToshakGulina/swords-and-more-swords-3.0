#!/usr/bin/env python3
"""Rebuild a source inventory and literal item dossiers from supplied mcaddon ZIPs.
Requires json5: python -m pip install json5
"""
import hashlib, json, re, zipfile, collections
from pathlib import Path
import json5

ROOT = Path(__file__).resolve().parents[1]
VERSIONS = [('1.6','SwordsAndMoreSwords.1.6.mcaddon'), ('2.8.8','swordsandmoreswords_2_8_8.mcaddon'), ('2.8.14','swordsandmoreswords-2-8-14.mcaddon')]
OUT = ROOT/'docs'
OUT.mkdir(exist_ok=True)
def md5(b): return hashlib.md5(b).hexdigest()
def show(x): return json.dumps(x,ensure_ascii=False,indent=2)
def compact(x): return json.dumps(x,ensure_ascii=False,separators=(",", ":"))
def parse(raw): return json5.loads(raw.decode('utf-8-sig'))
def duplicate_keys(raw):
    duplicates = []
    def pairs(items):
        out = {}
        for k,v in items:
            if k in out: duplicates.append(k)
            out[k] = v
        return out
    json5.loads(raw.decode('utf-8-sig'), object_pairs_hook=pairs)
    return duplicates

data={}
for version, filename in VERSIONS:
    archive=ROOT/'sources'/filename
    with zipfile.ZipFile(archive) as z:
        bad=z.testzip()
        if bad: raise RuntimeError(f'CRC failure: {filename} {bad}')
        files={i.filename:z.read(i) for i in z.infolist() if not i.is_dir()}
    data[version]=files
    counts=collections.Counter(p.split('/')[1] if '/' in p else '(root)' for p in files)
    invalid=[]; duplicates=[]
    for p,b in files.items():
        if p.lower().endswith('.json'):
            try:
                ds=duplicate_keys(b)
                if ds: duplicates.append((p,ds))
            except Exception as e: invalid.append((p,str(e).splitlines()[0]))
    inventory=[f'# Инвентаризация {version}', '', f'Архив: `sources/{filename}`; MD5 `{md5(archive.read_bytes())}`.', f'Проверка ZIP CRC: успешно; файлов: {len(files)}.', '', '## Состав по каталогам', '']
    inventory += [f'- `{k}`: {n}' for k,n in sorted(counts.items())]
    inventory += ['', '## JSON с ошибками разбора JSON5', '']
    inventory += [f'- `{p}`: {e}' for p,e in invalid] or ['- Не обнаружены.']
    inventory += ['', '## Повторяющиеся ключи JSON (сохранять порядок исходника)', '']
    inventory += [f'- `{p}`: {", ".join(ds)}' for p,ds in duplicates] or ['- Не обнаружены.']
    inventory += ['', '## Каждый файл архива', '', '| Путь в архиве | Байты | MD5 |', '|---|---:|---|']
    inventory += [f'| `{p}` | {len(b)} | `{md5(b)}` |' for p,b in sorted(files.items())]
    (OUT/f'inventory-{version}.md').write_text('\n'.join(inventory)+'\n',encoding='utf-8')
    # Decode as text only: binary file metadata is covered by the inventory.
    texts={}
    for p,b in files.items():
        if p.lower().endswith(('.json','.js','.mcfunction','.lang','.material')):
            try: texts[p]=b.decode('utf-8-sig')
            except UnicodeDecodeError: pass
    lang={}
    for p,t in texts.items():
        if p.endswith('/texts/en_US.lang'):
            for line in t.splitlines():
                if '=' in line:
                    k,v=line.split('=',1); lang[k.strip()]=v.strip()
    itempaths=sorted(p for p in files if re.search(r'/(?:items)/[^/]+\.json$',p) and ('_B/' in p))
    out=[f'# Исходные карточки предметов — архив {version}', '', 'Эта машинная выписка — точная отправная точка, не законченный семантический аудит. JSON ниже получен из JSON5, комментарии и оформление опущены; при повторяющихся ключах читать исходный файл. События и команды приведены без пересчёта вероятностей: веса являются относительными внутри конкретного `randomize`. Движковые значения по умолчанию и недокументированное поведение не угадываются.', '', 'Ссылки указывают путь и номера строк **внутри указанного архива**. Поиск упоминаний текстовый и не является полным графом вызовов: косвенные события, группы компонентов, снаряды, таблицы добычи, функции и модели необходимо проверить вручную.', '']
    for path in itempaths:
        try: item=parse(files[path])['minecraft:item']
        except Exception as e:
            out += [f'## {path}',f'Ошибка чтения: `{e}`','']; continue
        desc=item.get('description',{}); ident=desc.get('identifier',''); stem=ident.split(':')[-1] or Path(path).stem
        aliases={stem,Path(path).stem}; aliases={x for x in aliases if len(x)>=5}
        pattern=re.compile(r'(?<![\w])(?:'+ '|'.join(map(re.escape,sorted(aliases,key=len,reverse=True)))+r')(?![\w])',re.I)
        # Some keys append _event/_skill, so also allow suffix underscores.
        pattern=re.compile(r'(?<![A-Za-z0-9])(?:'+ '|'.join(map(re.escape,sorted(aliases,key=len,reverse=True)))+r')(?![A-Za-z0-9])',re.I)
        name=lang.get('item.'+ident,lang.get('item.'+ident+'.name','(нет записи)'))
        comps=item.get('components',{}); ev=item.get('events',{})
        out += [f'## {ident}', '', f'- Название в en_US: `{name}`', f'- Определение: `{path}`', f'- Урон (`minecraft:damage`): `{compact(comps.get("minecraft:damage", "не указан"))}`', f'- Прочность (`minecraft:durability`): `{compact(comps.get("minecraft:durability", "не указана"))}`', f'- Кулдаун (`minecraft:cooldown`): `{compact(comps.get("minecraft:cooldown", "не указан"))}`', '', '### Полное определение предмета', '', '```json',show(item),'```','', '### Прямые текстовые упоминания', '']
        refs=[]
        for p,t in sorted(texts.items()):
            if p==path: continue
            lines=[str(n) for n,line in enumerate(t.splitlines(),1) if pattern.search(line)]
            if lines: refs.append(f'- `{p}`: строки {", ".join(lines)}')
        out += refs or ['- По названию не найдены; это не доказательство отсутствия косвенных связей.']
        # Include full recipes and loot tables mentioning the exact identifier, whether
        # they give the item or consume it. Other indirect sources remain possible.
        related = [(p,t) for p,t in sorted(texts.items()) if ('/recipes/' in p or '/loot_tables/' in p) and ident and ident in t]
        if related:
            out += ['', '### Рецепты и таблицы добычи с точным ID', '']
            for p,t in related:
                out += [f'`{p}`:', '', '```json',t.rstrip(),'```','']
        # Full player entity groups and events, only when the key is recognizably related.
        for pp, raw in files.items():
            if not pp.endswith('/entities/player.json'): continue
            try: player=parse(raw).get('minecraft:entity',{})
            except Exception: continue
            groups={section:{k:v for k,v in player.get(section,{}).items() if pattern.search(k)} for section in ('component_groups','events')}
            groups={k:v for k,v in groups.items() if v}
            if groups: out += ['',f'### Одноимённые группы и события игрока (`{pp}`)', '', '```json',show(groups),'```']
        out += ['']
    (OUT/f'items-{version}.md').write_text('\n'.join(out)+'\n',encoding='utf-8')
# Full comparison uses file bytes, not timestamps or archive names.
a,b=data['2.8.8'],data['2.8.14']
out=['# Сравнение архивов 2.8.8 и 2.8.14', '', 'Сравнение полных путей и содержимого в распакованных архивах; имена архивов не подтверждают действительную внутреннюю версию.','', '| Статус | Путь |', '|---|---|']
for p in sorted(a.keys()|b.keys()):
    status='только 2.8.14' if p not in a else ('только 2.8.8' if p not in b else ('изменён' if a[p]!=b[p] else ''))
    if status: out.append(f'| {status} | `{p}` |')
out += ['',f'Идентичны по байтам: {sum(a[p]==b[p] for p in a.keys() & b.keys())}.','']
(OUT/'version-diff.md').write_text('\n'.join(out),encoding='utf-8')
