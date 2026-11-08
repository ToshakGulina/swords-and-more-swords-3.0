#!/usr/bin/env python3
"""Re-read every add-on ZIP member and record bounded, type-specific validation.

This is not proof that every file's semantics or game execution were understood.
"""
from collections import Counter
from functools import lru_cache
import hashlib
import io
import json
from pathlib import Path
from zipfile import ZipFile

import json5
import nbtlib
from PIL import Image
from mutagen.oggvorbis import OggVorbis

ROOT=Path(__file__).resolve().parents[1]
ARCHIVES={
 '1.6':('SwordsAndMoreSwords.1.6.mcaddon','4311b5625bc01a943fc3e36a3d6b8661'),
 '2.8.8':('swordsandmoreswords_2_8_8.mcaddon','adabcff0e37cf3ff567d3dcbbb3bc34e'),
 '2.8.14':('swordsandmoreswords-2-8-14.mcaddon','08b436f90465fd76a9b366dddbf321a2'),
}


def err(exc):return str(exc).replace('\n',' ')[:500]

@lru_cache(maxsize=1200)
def validate(raw, suffix):
    if suffix in ('.json','.material'):
        text=raw.decode('utf-8-sig')
        try:
            json5.loads(text,allow_duplicate_keys=False)
            return {'check':'json5_strict_no_duplicates','status':'ok'}
        except ValueError as strict_error:
            try:json5.loads(text,allow_duplicate_keys=True)
            except ValueError as permissive_error:
                return {'check':'json5','status':'invalid','error':err(permissive_error)}
            return {'check':'json5','status':'duplicate_keys','error':err(strict_error)}
    if suffix in ('.png','.jpeg','.jpg','.tga'):
        with Image.open(io.BytesIO(raw)) as im:im.verify()
        with Image.open(io.BytesIO(raw)) as im:
            im.load()
            return {'check':'image_verify_and_decode','status':'ok','format':im.format,'size':list(im.size),'mode':im.mode}
    if suffix=='.mcstructure':
        stream=io.BytesIO(raw);nbt=nbtlib.File.parse(stream,byteorder='little')
        if stream.tell()!=len(raw):raise ValueError('NBT has unread trailing bytes')
        rebuilt=nbtlib.File(nbtlib.parse_nbt(nbt.snbt(indent=2)),root_name=nbt.root_name)
        buffer=io.BytesIO();rebuilt.write(buffer,byteorder='little')
        if buffer.getvalue()!=raw:raise ValueError('NBT/SNBT round trip mismatch')
        return {'check':'little_endian_nbt_snbt_byte_roundtrip','status':'ok'}
    if suffix=='.ogg':
        audio=OggVorbis(io.BytesIO(raw))
        return {'check':'ogg_vorbis_metadata','status':'ok','channels':audio.info.channels,'sample_rate':audio.info.sample_rate,'duration_seconds':round(audio.info.length,6)}
    if suffix in ('.lang','.mcfunction','.js'):
        text=raw.decode('utf-8-sig')
        details={'check':'utf8_decode_only','status':'ok','lines':len(text.splitlines())}
        if suffix=='.lang':
            keys=Counter(line.split('=',1)[0] for line in text.splitlines() if line.strip() and not line.lstrip().startswith('#') and '=' in line)
            details['duplicate_keys']={k:v for k,v in sorted(keys.items()) if v>1}
        return details
    return {'check':'unsupported_file_type','status':'not_validated'}


def build():
    docs='\n'.join(p.read_text(encoding='utf-8') for p in (ROOT/'docs').glob('*.md') if not p.name.startswith('inventory-') and p.name!='file-review-status.md')
    result={'method':'all zip files read with CRC, sha256, type-specific structural validation; literal documentation mention is not semantic review', 'archives':{}}
    for version,(name,expected_md5) in ARCHIVES.items():
        path=ROOT/'sources'/name;raw=path.read_bytes();digest=hashlib.md5(raw).hexdigest()
        if digest!=expected_md5:raise ValueError(f'{name}: MD5 mismatch')
        with ZipFile(io.BytesIO(raw)) as z:
            infos=[i for i in z.infolist() if not i.is_dir()]
            if len({i.filename for i in infos})!=len(infos):raise ValueError('duplicate paths: '+name)
            rows=[]
            for info in infos:
                content=z.read(info) # Python verifies ZIP CRC during read.
                suffix=Path(info.filename).suffix.lower()
                try:detail=validate(content,suffix)
                except Exception as exc:detail={'check':'validator_exception','status':'error','error':err(exc)}
                rows.append({'path':info.filename,'bytes':len(content),'sha256':hashlib.sha256(content).hexdigest(),
                             'crc32':f'{info.CRC:08x}','literal_path_in_non_inventory_docs':info.filename in docs,'validation':detail})
        result['archives'][version]={'file':name,'md5':digest,'sha256':hashlib.sha256(raw).hexdigest(),'count':len(rows),'files':rows}
    return result


def render(data):
    lines=['# Повторная пофайловая проверка исходных архивов','',
           'Все записи файлов в трёх архивах перечитаны из ZIP с проверкой CRC, SHA-256 и ограниченной проверкой по типу. Это **не** подтверждение полного ручного понимания каждого файла, совместимости, воспроизведения игры или поведения Bedrock. Локальные исходники не изменялись. [Полный машиночитаемый список по каждому пути](../data/file-validation.json) · [сводка аудита](static-audit-summary.md).','',
           'JSON/material: JSON5 с проверкой дублирующихся ключей; при ошибке строгого разбора отдельно пробуется обычный JSON5 и сохраняется ошибка. Изображения: Pillow verify и полное декодирование пикселей, не оценка сходства. `.mcstructure`: little-endian NBT → SNBT → NBT, побайтовая обратная проверка. Ogg: только метаданные контейнера/кодека, **не** полное декодирование и прослушивание. JS, mcfunction и lang: UTF-8, а не полная семантика. Повторные ключи lang указаны отдельно. Отсутствие ошибки парсера не подтверждает валидность схемы или работу Bedrock.','',
           'Наличие точного пути в каком-либо другом Markdown-документе (без инвентаризаций и этого документа) отмечается только как **буквальное упоминание**. Оно не означает, что каждый байт или все косвенные связи вручную изучены.','',
           '| Архив | Файлы | JSON5 без дублей | JSON с повтором | JSON не разобран | Прочие ошибки/неподдержанные | Путь буквально встречается вне инвентаризации |', '|---|---:|---:|---:|---:|---:|---:|']
    for version in ARCHIVES:
        a=data['archives'][version]
        vals=[r['validation'] for r in a['files']];strict=sum(v['check']=='json5_strict_no_duplicates' for v in vals);dup=sum(v['status']=='duplicate_keys' for v in vals);invalid=sum(v['status']=='invalid' for v in vals);errors=sum(v['status'] in ('error','not_validated') for v in vals);mentions=sum(r['literal_path_in_non_inventory_docs'] for r in a['files'])
        lines.append(f'| {version} | {a["count"]} | {strict} | {dup} | {invalid} | {errors} | {mentions} |')
    lines+=['','## Исключения и неоднозначности','']
    for version in ARCHIVES:
        a=data['archives'][version]
        for row in a['files']:
            v=row['validation']
            if v['status']!='ok':
                detail=v.get('error',v['check']).replace('`',"'")
                lines.append(f'- {version} `{row["path"]}` — `{v["status"]}`: `{detail}`.')
            for key,count in v.get('duplicate_keys',{}).items():lines.append(f'- {version} `{row["path"]}` — повторный ключ lang `{key}`: {count} строк; приоритет не установлен.')
    lines+=['','## Состав исходной папки и границы проверки','',
            'В повторном списке Google Диска 25 файлов: 3 исходных mcaddon, 21 JPEG, один серверный ZIP. Три mcaddon здесь перечитаны; MD5 сравнивались с метаданными Диска. Все 21 JPEG повторно загружены: MD5 совпал с метаданными Диска, SHA-256 — с прежним OCR-индексом, изображения успешно декодированы. Ранее 20 описаний и браузерный снимок просмотрены визуально; **полной вручную выверенной транскрипции 21 изображения нет** ([OCR](screenshot-ocr.md), [выборочная визуальная сверка](screenshot-visual-review.md)). Серверный ZIP повторно проверен по MD5/SHA-256, CRC и хэшам **3384** файлов, без запуска; в 658 `.brarchive` найдены 9543 записи, из которых 312 с сигнатурой MCB не декодированы; четыре других двоичных файла тоже не декодированы, а 1608 `.nbt` проверены только как gzip, не как полностью разобранные NBT. Это не полная семантическая проверка серверного бинарника и ванильных данных ([сервер](server-archive.md)).','',
            'Имеются неразобранные JSON, повторные ключи, а также неизвестные приоритеты, внешние зависимости, порядок событий и поведение движка. Поэтому ответ «каждый файл полностью понят и проверен» не подтверждён. Можно опираться на буквальные выписки и тематические цепочки, но перенос поведения без последующей отдельной проверки остаётся с риском.','']
    return '\n'.join(lines)


def main():
    data=build();(ROOT/'data/file-validation.json').write_text(json.dumps(data,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf-8');(ROOT/'docs/file-review-status.md').write_text(render(data),encoding='utf-8');print('File-level audit completed')

if __name__=='__main__':main()
