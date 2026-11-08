#!/usr/bin/env python3
"""Reproducible path-normalized, line-by-line diffs of original ZIPs."""
from pathlib import Path
import difflib
import hashlib
import zipfile
import json5

ROOT = Path(__file__).resolve().parents[1]
VERSIONS = {'1.6': 'SwordsAndMoreSwords.1.6.mcaddon', '2.8.8': 'swordsandmoreswords_2_8_8.mcaddon', '2.8.14': 'swordsandmoreswords-2-8-14.mcaddon'}
TEXT = {'.json', '.js', '.mcfunction', '.lang', '.material', '.txt', '.md'}


def read(version):
    with zipfile.ZipFile(ROOT/'sources'/VERSIONS[version]) as z:
        result = {}
        for name in z.namelist():
            if name.endswith('/'):
                continue
            normalized = name.replace('Sword_B/', 'Swords_B/', 1).replace('Sword_R/', 'Swords_R/', 1)
            if normalized in result:
                raise ValueError(f'Path collision: {normalized}')
            result[normalized] = (name, z.read(name))
        return result


def ids(files):
    out = {}
    for path, (original, data) in files.items():
        if '/items/' not in path or not path.startswith('Swords_B/') or not path.endswith('.json'):
            continue
        try:
            ident = json5.loads(data.decode('utf-8-sig'))['minecraft:item']['description']['identifier']
            if ident in out:
                raise ValueError(f'duplicate ID {ident}')
            out[ident] = original
        except (KeyError, UnicodeDecodeError):
            continue
    return out


def main():
    all_data = {v: read(v) for v in VERSIONS}
    for old,new in [('1.6','2.8.14'), ('2.8.8','2.8.14')]:
        a,b = all_data[old], all_data[new]
        out = [f'# Построчное сравнение архивов {old} → {new}', '',
               'Имена корневых папок `Sword_B`/`Sword_R` в 1.6 нормализованы к `Swords_B`/`Swords_R` исключительно для сопоставления. Остальные пути сопоставляются буквально. Переименования файлов и смысловые эквиваленты автоматически не обнаруживаются; совпадение ID не гарантирует одинаковой механики. Двоичные файлы сравниваются по байтам без визуальной оценки. Для текстовых diff перенесены строки без различия CRLF/LF; изменение только окончания строк отражено в таблице как изменённый файл, но diff может быть пустым. Исходные архивы и их инвентаризации остаются эталоном.', '', '## Сопоставление ID предметов', '', '| ID | Старый путь | Новый путь |', '|---|---|---|']
        x,y=ids(a),ids(b)
        for k in sorted(x.keys()|y.keys()):
            out.append(f'| `{k}` | `{x[k]}` | `{y[k]}` |' if k in x and k in y else f'| `{k}` | '+(f'`{x[k]}`' if k in x else '—')+' | '+(f'`{y[k]}`' if k in y else '—')+' |')
        out += ['', '## Все несовпадающие пути', '', '| Статус | Нормализованный путь | SHA-256 старый | SHA-256 новый |', '|---|---|---|---|']
        changed=[]
        for k in sorted(a.keys()|b.keys()):
            left=a[k][1] if k in a else None; right=b[k][1] if k in b else None
            if left==right: continue
            status='изменён' if left is not None and right is not None else ('только '+old if right is None else 'только '+new)
            sha=lambda v: hashlib.sha256(v).hexdigest() if v is not None else '—'
            out.append(f'| {status} | `{k}` | `{sha(left)}` | `{sha(right)}` |')
            if left is not None and right is not None and Path(k).suffix.lower() in TEXT:
                changed.append((k,left,right))
        out += ['',f'Совпадают по нормализованному пути и байтам: {sum(a[k][1]==b[k][1] for k in a.keys() & b.keys())}.','', '## Построчные изменения совпадающих текстовых путей', '']
        for k,left,right in changed:
            try:
                l=left.decode('utf-8-sig').splitlines(); r=right.decode('utf-8-sig').splitlines()
            except UnicodeDecodeError:
                out += [f'### `{k}`', '', 'Не удалось декодировать как UTF-8; сравнивайте байты.', '']; continue
            diff=list(difflib.unified_diff(l,r,fromfile=f'{old}/{a[k][0]}',tofile=f'{new}/{b[k][0]}',lineterm='',n=3))
            out += [f'### `{k}`', '', '```diff', *(diff or ['(Только формат байтов, окончания строк или BOM.)']), '```', '']
        (ROOT/'docs'/f'version-lines-{old}-to-{new}.md').write_text('\n'.join(out),encoding='utf-8')
        print(old,new, 'changed text files',len(changed),'lines',len(out))

if __name__ == '__main__':
    main()
