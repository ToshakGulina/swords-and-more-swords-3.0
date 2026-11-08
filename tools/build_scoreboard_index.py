#!/usr/bin/env python3
"""Raw scoreboard objective candidates and selector references, with provenance."""
from pathlib import Path
from zipfile import ZipFile
from collections import defaultdict,Counter
import json,re
from build_entity_group_index import VERSIONS
ROOT=Path(__file__).resolve().parents[1]
OBJS=re.compile(r'\bscoreboard\s+objectives\s+(add|remove)\s+([\w.-]+)')
PLAYERS=re.compile(r'\bscoreboard\s+players\s+(set|add|remove)\s+(@\w+(?:\[[^\]]*\])?|\S+)\s+([\w.-]+)\s+([+-]?\d+)')
SCORES=re.compile(r'\bscores\s*=\s*\{([^}]*)\}')
LEGACY=re.compile(r'\bscore_[a-zA-Z0-9_.-]+')
SCAN=re.compile(r'\bscoreboard\b|\bscores\s*=|\bscore_[a-zA-Z0-9_.-]+')

def extract(filename,pack):
    records=[];unknown=[]
    with ZipFile(ROOT/'sources'/filename) as z:
        for path in sorted(z.namelist()):
            if not path.startswith(pack+'/') or not path.endswith(('.json','.mcfunction','.js')):continue
            source=z.read(path).decode('utf-8-sig')
            for line,text in enumerate(source.splitlines(),1):
                if not SCAN.search(text):continue
                refs=defaultdict(list);starts=set()
                for m in OBJS.finditer(text):refs[m[2]].append('objectives '+m[1]);starts.add(m.start())
                for m in PLAYERS.finditer(text):refs[m[3]].append('players '+m[1]+' '+m[2]+' '+m[4]);starts.add(m.start())
                for m in SCORES.finditer(text):
                    starts.add(m.start())
                    for pair in m[1].split(','):
                        if '=' not in pair or not pair.split('=',1)[0].strip():unknown.append((path,line,'scores element',pair));continue
                        k,v=pair.split('=',1);refs[k.strip()].append('selector '+k.strip()+'='+v.strip())
                for m in SCAN.finditer(text):
                    if m.start() not in starts:unknown.append((path,line,'unclassified',m.group()))
                for m in LEGACY.finditer(text):unknown.append((path,line,'legacy selector key',m.group()))
                records.append((path,line,text,tuple((k,tuple(v)) for k,v in sorted(refs.items()))))
    return records,unknown

def fmt(value):return '`'+json.dumps(value,ensure_ascii=False,separators=(',',':')).replace('|','\\|').replace('`','\\u0060')+'`'

def render(title,ver,data):
    records,unknown=data;by=defaultdict(list)
    for path,n,text,refs in records:
        for name,labels in refs:by[name].append((path,n,text,labels))
    out=[f'# Scoreboard: буквальные операции и selectors — {title}', '',
         f'Лексический поиск `scoreboard`, `scores=` и старых ключей `score_*` во всех `.json`, `.mcfunction`, `.js` behavior pack даёт **{len(records)} исходных строк**. Сканируются и строки JSON с ошибками, комментарии, JS и возможные строковые данные; запись сама по себе не доказывает выполнение команды. Имена objectives извлекаются только из буквальных `objectives add/remove`, `players add/set/remove` с числовым аргументом и `scores={{...}}`; иные формы перечислены как нераспознанные, если встретились.', '',
         'Числа — **значения score**, не секунды или тики. Операция objective и конкретная запись игрока/сущности различны; селектор, `@s`, ближайший `@p`, контекст execute, наличие objective, прерывание последовательности и конкуренцию игроков нельзя игнорировать. Здесь группировка по имени облегчает поиск, но не заменяет исходный порядок внутри события, условий и вызовов. Один и тот же ряд может попасть в несколько групп; повторы сохраняются.', '',
         'Распознанные objectives: '+', '.join(f'`{k}` ({len(rows)} строк)' for k,rows in sorted(by.items()))+'.', '',
         '- Нераспознанные кандидаты: '+('; '.join(f'`{p}:{n}` {what} {fmt(detail)}' for p,n,what,detail in unknown) if unknown else 'нет в ограниченной области сканирования')+'.','']
    if ver=='1.6':out += ['Важно: `normal.mcfunction` выполняет через ближайшего подходящего игрока `scoreboard objectives remove b/bn/sh/s`; это операции над именами objective, не команда удаления только его отдельного счёта. `normalft.mcfunction` работает с `@a` и `swords`, а многие контроллеры записывают `@a swords 2`. [Ручная схема глобального состояния](manual-global-state-1.6.md) · [спутники и счётчики](manual-counter-helpers-1.6.md).','']
    else:out += ['В 2.x команды `sponge_sword` находятся в `player.json` и указывают `@s`; `slime_despawn` в одних командах сбрасывается по selector ближайшего слизня, а в других увеличивается для `@s` в событии слизня. Проверки и сбросы в разных событиях не гарантируют фиксированную длительность. [Подробный Slime](manual-traces-2.8.14.md#slime-sword-effectslime_sword-и-slime-king) · [Sponge](manual-traces-2.8.14.md#sponge-sword-и-wet-sponge-sword-effectsponge_sword-effectwet_sponge_sword). В выбранных строках 2.8.8/2.8.14 совпадают пути, номера и текст; другие части файлов могут различаться.', '']
    out += ['## Все строки по имени objective','']
    for name,rows in sorted(by.items()):
        out += [f'### {name}', '', '| Файл и строка | Найденные формы | Исходная строка целиком |', '|---|---|---|']
        for path,n,text,labels in rows:out.append(f'| `{path}:{n}` | '+', '.join(fmt(x) for x in labels)+f' | {fmt(text)} |')
        out.append('')
    return '\n'.join(out)

def build_all():
    data={v:extract(f,p) for v,f,p in VERSIONS}
    if data['2.8.8']!=data['2.8.14']:raise ValueError('2.x score references differ')
    return {'1.6':render('1.6','1.6',data['1.6']),'2.x':render('2.8.8 и 2.8.14','2.x',data['2.8.14'])}

def main():
    for ver,text in build_all().items():
        (ROOT/f'docs/scoreboard-index-{ver}.md').write_text(text,encoding='utf8');print(ver,len(text.splitlines()),'lines')
if __name__=='__main__':main()
