#!/usr/bin/env python3
"""Find selected literal file references without inferring runtime resolution."""
import collections
import re
import zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
VERSIONS={'1.6':'SwordsAndMoreSwords.1.6.mcaddon','2.8.8':'swordsandmoreswords_2_8_8.mcaddon','2.8.14':'swordsandmoreswords-2-8-14.mcaddon'}
PATTERNS=[('loot',re.compile(r'\b(loot_tables/[\w./-]+\.json)')),('structure',re.compile(r'\bstructure\s+load\s+([\w./:-]+)')),('function',re.compile(r'\bfunction\s+([\w./:-]+)'))]
SUFFIXES={'.json','.mcfunction','.js','.lang','.material'}


def main():
 for version,filename in VERSIONS.items():
  with zipfile.ZipFile(ROOT/'sources'/filename) as z:
   data={n:z.read(n) for n in z.namelist() if not n.endswith('/')}
  found=collections.defaultdict(list)
  for name,raw in sorted(data.items()):
   if Path(name).suffix.lower() not in SUFFIXES or '/' not in name: continue
   try: lines=raw.decode('utf-8-sig').splitlines()
   except UnicodeDecodeError:continue
   pack=name.split('/')[0]
   for number,line in enumerate(lines,1):
    for kind,pattern in PATTERNS:
     for match in pattern.finditer(line):
      ref=match.group(1)
      if kind=='loot': expected=f'{pack}/{ref}'
      elif kind=='structure': expected=f'{pack}/structures/{ref}.mcstructure'
      else: expected=f'{pack}/functions/{ref}.mcfunction'
      found[(kind,ref,expected,expected in data)].append((name,number))
  out=[f'# Буквальные ссылки на файлы — архив {version}', '', 'Механический поиск в UTF-8 текстах архива: `loot_tables/*.json`, команды `structure load` и `function`. Сравниваются только буквальные пути внутри того же корневого пакета. Список не является полным графом: пропускает динамические имена, встроенные ссылки и другие виды ресурсов; может захватить комментарии или некомандный текст. **«Не найден в пакете» не означает ошибка:** путь может быть ванильным, разрешаться из другого пакета или по правилам движка; поведение нужно проверять. Обратная ситуация тоже не доказывает доступность в игре.', '']
  for available in (False,True):
   out += ['## '+('Не найдены по буквальному пути в том же пакете' if not available else 'Найдены по буквальному пути в том же пакете'), '', '| Тип | Буквальная ссылка | Проверенный путь | Источники: строки |', '|---|---|---|---|']
   for (kind,ref,expected,ok),locations in sorted(found.items()):
    if ok!=available:continue
    loc=collections.defaultdict(list)
    for name,number in locations:loc[name].append(number)
    citations='; '.join('`'+p+'`: '+', '.join(map(str,ns)) for p,ns in sorted(loc.items()))
    out.append(f'| {kind} | `{ref}` | `{expected}` | {citations} |')
   out.append('')
  (ROOT/'docs'/f'literal-references-{version}.md').write_text('\n'.join(out),encoding='utf-8')
  print(version,'targets',len(found),'missing',sum(not k[3] for k in found))

if __name__=='__main__':main()
