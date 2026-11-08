#!/usr/bin/env python3
"""Index literal effect-command candidates plus selected effect-bearing components."""
from pathlib import Path
from zipfile import ZipFile
from collections import Counter
import json,json5,re
from build_entity_group_index import VERSIONS
ROOT=Path(__file__).resolve().parents[1]
CANDIDATE=re.compile(r'(?<![\w:])effect\s+@')
EXTRACT=re.compile(r'(?<![\w:])effect\s+(@\w+(?:\[[^\]]*\])?)\s+([\w:]+)(?=\s|[",])')

def extract(filename,pack):
    lines=[];objects=[];errors=[];dups=[];unparsed=[]
    with ZipFile(ROOT/'sources'/filename) as z:
        for p in sorted(z.namelist()):
            if not p.startswith(pack+'/') or not p.endswith(('.json','.mcfunction','.js')):continue
            try:source=z.read(p).decode('utf-8-sig')
            except UnicodeDecodeError as err:errors.append((p,str(err)));continue
            for number,line in enumerate(source.splitlines(),1):
                occurrences=list(CANDIDATE.finditer(line))
                if not occurrences:continue
                matches=[EXTRACT.match(line,m.start()) for m in occurrences]
                if not all(matches):unparsed.append((p,number))
                names=tuple(m.group(2) for m in matches if m)
                lines.append((p,number,line,names))
            if not p.endswith('.json'):continue
            repeated=[]
            def pairs(seq):
                obj={}
                for k,v in seq:
                    if k in obj:repeated.append(k)
                    obj[k]=v
                return obj
            try:data=json5.loads(source,object_pairs_hook=pairs)
            except ValueError as err:errors.append((p,str(err).splitlines()[0]));continue
            if repeated:dups.append((p,tuple(repeated)))
            def walk(node,path):
                if isinstance(node,dict):
                    for key,v in node.items():
                        selected=(key in ('minecraft:spell_effects','mob_effect','arrow_effect') or
                                  key=='minecraft:attack' and isinstance(v,dict) and ('effect_name' in v or 'effect_duration' in v) or
                                  key=='minecraft:healable' and isinstance(v,dict) and isinstance(v.get('items'),list) and any(isinstance(item,dict) and 'effects' in item for item in v['items']))
                        if selected:objects.append((p,path+'.'+key,key,v))
                        walk(v,path+'.'+key)
                elif isinstance(node,list):
                    for i,x in enumerate(node):walk(x,path+f'[{i}]')
            walk(data,'$')
    return lines,objects,errors,dups,unparsed

def code(value):return '`'+json.dumps(value,ensure_ascii=False,separators=(',',':')).replace('|','\\|').replace('`','\\u0060')+'`'
def render(title,ver,data):
    lines,objects,errors,dups,unparsed=data;counts=Counter(name for _,_,_,names in lines for name in names);kinds=Counter(row[2] for row in objects)
    out=[f'# Эффекты: команды и выбранные компоненты — {title}', '',
         f'Лексический поиск во всех текстовых `.json`, `.mcfunction`, `.js` behavior pack: {len(lines)} исходных строк с буквальным `effect` и selector `@…`, {sum(counts.values())} распознанных вхождений. Исходные строки сохранены целиком с номерами, даже если один JSON-ряд содержит несколько команд; сохраняются повторы разных состояний. Строка может быть комментарием или недостижимой ветвью. Это не парсер команд и не подтверждение исполнения. Выборка не включает команды с другим синтаксисом, динамически составленные строки, ресурсы извне, ванильные функции или эффекты, приходящие по косвенным цепям.', '',
         'Селекторы, фильтры, нули, порядок и числовые аргументы приведены буквально. Не переводить duration/amplifier в секунды или уровни без учёта конкретной формы и версии; `0` не приравнивается автоматически к одному и тому же действию во всех контекстах. Необъявленный target не следует считать self. Имена ниже — лишь разбор подстроки, не гарантированный effect ID или цель.', '',
         'Вхождения имён после selector: '+', '.join(f'`{name}` — {count}' for name,count in sorted(counts.items()))+'.', '',
         f'Отдельно среди разобранных JSON извлечены **{len(objects)}** структурных объектов: '+', '.join(f'`{k}` — {v}' for k,v in sorted(kinds.items()))+'. Включены `minecraft:spell_effects`, `minecraft:attack` с `effect_name`/`effect_duration`, `minecraft:healable` с `items[].effects`, а также `mob_effect` и `arrow_effect`. Пустой `arrow_effect` не означает отсутствие стрелочных эффектов: обработка остаётся за движком. Списки, значения и вложенные фильтры сохранены целиком.', '',
         '- Неразобранные JSON: '+('; '.join(f'`{p}` ({e})' for p,e in errors) if errors else 'нет')+'. Исходные строки с командами ищутся и в них, но структурные объекты этих файлов исключены.',
         '- Повторные ключи в разобранных файлах: '+('; '.join(f'`{p}`: '+', '.join('`'+k+'`' for k in keys) for p,keys in dups) if dups else 'нет')+'. JSON5 сохраняет последнее значение; подлинник остаётся эталоном.',
         '- Вхождения не соответствующие ограниченному шаблону извлечения имени: '+('; '.join(f'`{p}:{n}`' for p,n in unparsed) if unparsed else 'нет')+'.','']
    if ver=='2.x':out += ['В выбранных строках команд и структурных объектах обеих 2.x совпадают пути, номера строк и значения; это не сравнение всех остальных частей файлов.', '']
    out += ['## Исходные строки с командами', '', '| Файл и строка | Распознанные имена | Исходная строка целиком |', '|---|---|---|']
    for path,line,text,names in lines:out.append(f'| `{path}:{line}` | '+(', '.join('`'+x+'`' for x in names) if names else 'не извлечено')+f' | {code(text)} |')
    out += ['', '## Структурные поля (все выбранные разобранные объекты)', '', '| Файл / путь | Поле | Полный разобранный объект |', '|---|---|---|']
    for path,where,key,value in objects:out.append(f'| `{path}`<br>`{where}` | `{key}` | {code(value)} |')
    out += ['',f'Контекст событий, включение групп и полные списки команд: [реестр сущностей](entity-ledger-{ver if ver!="2.x" else "2.8.14"}.md), [projectile](projectile-component-index.md), [weapon-хуки](weapon-event-index.md), [команды](command-risk-index-{ver if ver!="2.x" else "2.8.14"}.md).', '']
    return '\n'.join(out)

def build_all():
    d={v:extract(f,p) for v,f,p in VERSIONS}
    if d['2.8.8']!=d['2.8.14']:raise ValueError('2.x effect index inputs differ')
    return {'1.6':render('1.6','1.6',d['1.6']),'2.x':render('2.8.8 и 2.8.14','2.x',d['2.8.14'])}

def main():
    for ver,text in build_all().items():
        (ROOT/f'docs/effect-index-{ver}.md').write_text(text,encoding='utf8');print(ver,len(text.splitlines()),'lines')
if __name__=='__main__':main()
