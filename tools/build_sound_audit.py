#!/usr/bin/env python3
"""Index explicit sound command strings and local sound definitions, not playback."""
from collections import defaultdict
from io import BytesIO
import hashlib
import json
import re
import zipfile
from pathlib import Path
import json5
from mutagen import File as AudioFile

ROOT=Path(__file__).resolve().parents[1]
VERSIONS=[('1.6','SwordsAndMoreSwords.1.6.mcaddon','Sword_R'),('2.8.8','swordsandmoreswords_2_8_8.mcaddon','Swords_R'),('2.8.14','swordsandmoreswords-2-8-14.mcaddon','Swords_R')]
COMMAND=re.compile(r'\b(playsound|stopsound)\s+([^\s]+)(?:\s+([^\s]+))?')

def collect(filename,resource):
    records=[];errors=[];duplicates=[]
    with zipfile.ZipFile(ROOT/'sources'/filename) as z:
        files={n:z.read(n) for n in z.namelist() if not n.endswith('/')}
    def record(source,loc,text):
        for match in COMMAND.finditer(text):
            op,first,second=match.groups()
            sound=first if op=='playsound' else (second or '<all>')
            records.append((source,loc,op,sound,text))
    def walk(source,node,loc):
        if isinstance(node,str):record(source,loc,node)
        elif isinstance(node,dict):
            for key,val in node.items():walk(source,val,loc+'.'+key)
        elif isinstance(node,list):
            for i,val in enumerate(node):walk(source,val,f'{loc}[{i}]')
    for source,raw in sorted(files.items()):
        if not source.endswith(('.json','.mcfunction','.js')):continue
        try:text=raw.decode('utf-8-sig')
        except UnicodeDecodeError as exc:errors.append((source,str(exc).splitlines()[0]));continue
        if source.endswith('.json'):
            duplicate=[]
            def pairs(values):
                out={}
                for key,val in values:
                    if key in out:duplicate.append(key)
                    out[key]=val
                return out
            try:obj=json5.loads(text,object_pairs_hook=pairs)
            except ValueError as exc:errors.append((source,str(exc).splitlines()[0]));continue
            if duplicate:duplicates.append((source,duplicate))
            walk(source,obj,'$')
        else:
            # This is a textual scan, not a JavaScript parser. Comments/strings can match.
            for i,line in enumerate(text.splitlines(),1):
                if not line.lstrip().startswith(('#','//')):record(source,f'line:{i}',line.strip())
    definitions={}
    path=resource+'/sounds/sound_definitions.json'
    if path in files:
        try:definitions=json5.loads(files[path].decode('utf-8-sig')).get('sound_definitions',{})
        except (ValueError,UnicodeDecodeError):pass
    return files,definitions,records,errors,duplicates

def compact(x):return json.dumps(x,ensure_ascii=False,separators=(',',':'))

def build(version,filename,resource):
    files,defs,records,errors,duplicates=collect(filename,resource)
    grouped=defaultdict(list)
    for source,loc,op,sound,text in records:grouped[(op,sound)].append((source,loc,text))
    out=[f'# Звуковые команды и локальные звуки — {version}', '',
         'Автоматический указатель строк `playsound`/`stopsound` в JSON-значениях и в текстовых строках mcfunction/JS; приведён весь исходный командный текст и путь внутри разобранного JSON. Это не полный граф звука: `sounds.json`, animation sound_effects, ванильные события, динамические команды и другие пакеты могут вызывать звуки без этих строк. Текстовый просмотр JS/mcfunction может включать неисполняемые строки; валидность, условия события, громкость/единицы и воспроизведение не проверены.', '',
         'Определение отсутствует локально ≠ ошибка: имя может быть ванильным или предоставлено другим пакетом. `stopsound` разбирается в порядке команда → цель → имя, отсутствие имени отмечено `<all>`. JSON5 пропускает повторённые ключи кроме последнего, а некорректные файлы исключены; полная диагностика ниже. Связи `sounds.json` — в [реестре ресурсов](resource-graph-'+version+'.md), медиа — в [реестре ассетов](assets-'+version+'.md).','',
         f'Объявлено локальных sound ID: {len(defs)}; командных строк: {len(records)}; разных пар команда/звук: {len(grouped)}.', '', '## Диагностика', '',
         '- Не разобраны: '+(', '.join(f'`{p}`' for p,_ in errors) if errors else 'нет')+'.',
         '- Повторные ключи при разборе: '+(', '.join(f'`{p}`: `{compact(keys)}`' for p,keys in duplicates) if duplicates else 'нет')+'.', '', '## Локальные определения и файлы', '']
    for name,definition in sorted(defs.items()):
        out += [f'### `{name}`','',f'- Исходное определение: `{compact(definition)}`']
        for sound in definition.get('sounds',[]):
            val=sound if isinstance(sound,str) else sound.get('name') if isinstance(sound,dict) else None
            if not isinstance(val,str):out.append(f'- Неподдерживаемая форма sound: `{compact(sound)}`');continue
            if isinstance(sound,dict) and sound.get('type')=='event':
                out.append(f'- `{val}` указан как event, не путь к файлу.');continue
            candidates=[resource+'/'+val+suffix for suffix in ('','.ogg','.wav','.mp3','.flac')]
            found=[p for p in candidates if p in files]
            if not found:out.append(f'- `{val}`: аудиофайл по прямому пути не найден локально.');continue
            for path in found:
                raw=files[path]
                try:
                    info=AudioFile(BytesIO(raw)).info
                    desc=f'{info.length:.6f} с; {getattr(info,"sample_rate","—")} Гц; {getattr(info,"channels","—")} канал(ов)'
                except Exception as exc:desc='ошибка чтения метаданных '+type(exc).__name__
                out.append(f'- `{path}` — {desc}; SHA-256 `{hashlib.sha256(raw).hexdigest()}`.')
        out.append('')
    out += ['## Все обнаруженные строки команд','']
    for (op,sound),calls in sorted(grouped.items()):
        out += [f'### `{op} {sound}`', '',f'Локальное sound definition: {"да" if sound in defs else "не найдено"}; упоминаний: {len(calls)}.', '']
        for source,loc,cmd in calls:
            # JSON strings do not include markdown quoting; preserve characters literally.
            escaped=cmd.replace('`','\\`')
            out.append(f'- `{source}` · `{loc}` · `{escaped}`')
        out.append('')
    return '\n'.join(out)

def main():
    for v,f,r in VERSIONS:
        text=build(v,f,r)
        (ROOT/f'docs/sound-index-{v}.md').write_text(text,encoding='utf-8')
        print(v,len(text.splitlines()),'lines')

if __name__=='__main__':main()
