#!/usr/bin/env python3
"""Index direct item event trees, conditional branch weights and static entity links.
This is an audit aid, not a Bedrock interpreter. Requires json5==0.17.3.
"""
import json, re, zipfile
from fractions import Fraction
from pathlib import Path
import json5

ROOT = Path(__file__).resolve().parents[1]
VERSIONS = [('1.6','SwordsAndMoreSwords.1.6.mcaddon'),('2.8.8','swordsandmoreswords_2_8_8.mcaddon'),('2.8.14','swordsandmoreswords-2-8-14.mcaddon')]

def compact(x):
    return json.dumps(x, ensure_ascii=False, separators=(',', ':'))

def event_tree(value, out, path='$', depth=0):
    """Do not infer event order except for explicit sequence arrays."""
    indent='  '*depth
    if not isinstance(value,dict):
        out.append(f'{indent}- `{path}`: `{compact(value)}`')
        return
    ordinary={k:v for k,v in value.items() if k not in ('sequence','randomize','weight')}
    if ordinary:
        # One object: ordering between sibling actions is not specified by this report.
        out.append(f'{indent}- `{path}` — поля действия: `{compact(ordinary)}`')
    if 'sequence' in value:
        seq=value['sequence']
        if not isinstance(seq,list):
            out.append(f'{indent}- `{path}.sequence` необычная структура: `{compact(seq)}`')
        else:
            out.append(f'{indent}- `{path}.sequence`: {len(seq)} шаг(ов), порядок как в исходнике:')
            for i, step in enumerate(seq): event_tree(step,out,f'{path}.sequence[{i}]',depth+1)
    if 'randomize' in value:
        branches=value['randomize']
        if not isinstance(branches,list):
            out.append(f'{indent}- `{path}.randomize` необычная структура: `{compact(branches)}`'); return
        weights=[b.get('weight') if isinstance(b,dict) else None for b in branches]
        can_compute=all(isinstance(w,int) and not isinstance(w,bool) and w>=0 for w in weights) and sum(weights)>0
        out.append(f'{indent}- `{path}.randomize`: альтернативы, веса `{compact(weights)}`'+ (f', сумма {sum(weights)}' if can_compute else ', сумму/вероятности не вычисляем')+':')
        for i, branch in enumerate(branches):
            probability=''
            if can_compute:
                p=Fraction(weights[i],sum(weights)); probability=f'; условная доля {p.numerator}/{p.denominator} ({float(p)*100:.6g}%)'
            out.append(f'{indent}  - ветвь {i}, weight `{compact(weights[i])}`{probability}:')
            # Weight is represented above; filters remain on the branch itself.
            if isinstance(branch,dict) and not any(k!='weight' for k in branch):
                out.append(f'{indent}    - пустое действие')
            else: event_tree(branch,out,f'{path}.randomize[{i}]',depth+2)

def values(obj):
    if isinstance(obj,dict):
        for v in obj.values(): yield from values(v)
    elif isinstance(obj,list):
        for v in obj: yield from values(v)
    elif isinstance(obj,str): yield obj

def line_numbers(text, needle):
    return [str(i) for i,s in enumerate(text.splitlines(),1) if needle in s]

def run(version,filename):
    with zipfile.ZipFile(ROOT/'sources'/filename) as z:
        files={p:z.read(p) for p in z.namelist() if not p.endswith('/')}
    texts={}
    for p,b in files.items():
        if p.endswith(('.json','.js','.mcfunction','.lang')):
            try: texts[p]=b.decode('utf-8-sig')
            except UnicodeDecodeError: pass
    objects={}
    for p,t in texts.items():
        if p.endswith('.json'):
            try: objects[p]=json5.loads(t)
            except Exception: pass
    entities={}
    for p,obj in objects.items():
        if '/entities/' not in p: continue
        entity=obj.get('minecraft:entity',{})
        ident=entity.get('description',{}).get('identifier')
        if ident: entities.setdefault(ident,[]).append(p)
    inventory=[]
    for p,obj in sorted(objects.items()):
        if not re.search(r'_B/items/[^/]+\.json$',p) or 'minecraft:item' not in obj: continue
        item=obj['minecraft:item']; desc=item.get('description',{}); comps=item.get('components',{}); events=item.get('events',{}); ident=desc.get('identifier','')
        inventory.append((ident,p,item,comps,events))
    out=[f'# Сводка прямых механик предметов — архив {version}', '',
      'Машинный индекс непосредственно объявленных данных предметов. Это **не** полное описание поведения: эффекты игрока, сущности, скрытые цепочки и поведение движка разбираются отдельно. Путь исходника и номера строк относятся к архиву из `sources/`.', '',
      'Доли randomize рассчитаны как weight / сумма явно заданных неотрицательных целых весов в том же массиве. Это условная доля при выборе ветви, не вероятность успешного результата; фильтры, вложенность и триггер влияют на итог. При отсутствующем весе доли не вычисляются. Соседние поля объекта показаны вместе без предположений об их порядке.', '',
      '## Общая таблица', '', '| ID | Урон | Прочность max | Cooldown (category, duration) | Крюки |', '|---|---:|---:|---|---|']
    for ident,p,item,c,e in inventory:
        dur=c.get('minecraft:durability',{}); dur=dur.get('max_durability','—') if isinstance(dur,dict) else compact(dur)
        hooks=[]
        for k in ('minecraft:on_use','minecraft:on_use_on','minecraft:weapon','minecraft:food'):
            if k in c: hooks.append(k.split(':')[1])
        out.append(f'| `{ident}` | `{compact(c.get("minecraft:damage","—"))}` | `{compact(dur)}` | `{compact(c.get("minecraft:cooldown","—"))}` | {", ".join(hooks) or "—"} |')
    out += ['','## Карточки', '']
    for ident,p,item,c,events in inventory:
        out += [f'### {ident}', '', f'- Файл `{p}`; format_version `{compact(objects[p].get("format_version"))}`.',
                f'- Урон `{compact(c.get("minecraft:damage","не задан"))}`; прочность `{compact(c.get("minecraft:durability","не задана"))}`; стак `{compact(c.get("minecraft:max_stack_size","не задан"))}`; перезарядка `{compact(c.get("minecraft:cooldown","не задана"))}`.',
                f'- Зачарование `{compact(c.get("minecraft:enchantable","не задано"))}`; ремонт `{compact(c.get("minecraft:repairable","не задан"))}`.',
                f'- Оффхенд `{compact(c.get("minecraft:allow_off_hand","не задан"))}`; hand_equipped `{compact(c.get("minecraft:hand_equipped","не задан"))}`; foil `{compact(c.get("minecraft:foil","не задан"))}`; icon `{compact(c.get("minecraft:icon","не задан"))}`.',
                f'- Скорости добычи `{compact(c.get("minecraft:digger","не заданы"))}`.', '']
        relevant={k:v for k,v in c.items() if k in ('minecraft:on_use','minecraft:on_use_on','minecraft:weapon','minecraft:food','minecraft:projectile','minecraft:shooter','minecraft:throwable')}
        out += [f'**Привязки триггеров:** `{compact(relevant)}`.', '']
        if not events: out += ['Прямых item events в файле нет; это не исключает пассивные и косвенные механики.', '']
        for name,event in events.items():
            lines=line_numbers(texts[p], '"'+name+'"')
            out += [f'**Событие `{name}`** (упоминания в исходнике: строки {", ".join(lines) or "не найдены"}):', '']
            event_tree(event,out); out.append('')
        # Only exact custom/vanilla entity IDs occurring in item fields; no claim of completeness.
        seen=set()
        for s in values(item): seen.update(re.findall(r'\b(?:entity|minecraft):[a-z0-9_]+\b',s))
        linked={id:entities[id] for id in sorted(seen) if id in entities}
        if linked:
            out += ['**Прямые ссылки на сущности из текстовых значений item** (распознавание идентификаторов; не все они обязательно вызываются):']
            for id,paths in linked.items(): out.append(f'- `{id}` → '+', '.join(f'`{q}`' for q in paths))
            out.append('')
        # Loot reference including its caller, even where table path differs from item id.
        loot=[q for q,t in texts.items() if '/loot_tables/' in q and ident and ident in t]
        if loot:
            out += ['**Таблицы добычи с буквальным ID и прямые упоминания этих таблиц:**']
            for q in sorted(loot):
                rel=q.split('/loot_tables/',1)[1][:-5]
                lookups={'loot_tables/'+rel+'.json','loot '+rel}
                callers=[]
                for f,t in texts.items():
                    if f==q: continue
                    lines=sorted({int(n) for s in lookups for n in line_numbers(t,s)})
                    if lines: callers.append(f'`{f}`:{",".join(map(str,lines))}')
                out.append(f'- `{q}` → '+('; '.join(callers) if callers else 'прямых текстовых ссылок не найдено; возможна регистрация движком/косвенная ссылка'))
            out.append('')
    (ROOT/'docs'/f'mechanics-{version}.md').write_text('\n'.join(out)+'\n',encoding='utf-8')
    return len(inventory)

if __name__=='__main__':
    for v,f in VERSIONS: print(v,run(v,f))
