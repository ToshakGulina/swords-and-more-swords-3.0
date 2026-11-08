#!/usr/bin/env python3
"""Preserve the parsed contents of local render/animation controllers, particles and materials."""
from collections import Counter
from hashlib import sha256
from pathlib import Path
from zipfile import ZipFile
import json,json5
ROOT=Path(__file__).resolve().parents[1]
VERSIONS=(('1.6','SwordsAndMoreSwords.1.6.mcaddon','Sword_R'),('2.8.8','swordsandmoreswords_2_8_8.mcaddon','Swords_R'),('2.8.14','swordsandmoreswords-2-8-14.mcaddon','Swords_R'))
FOLDERS=('animation_controllers','render_controllers','particles','materials')

def collect(filename,pack):
    files=[];errors=[];dups=[]
    with ZipFile(ROOT/'sources'/filename) as z:
        for path in sorted(z.namelist()):
            if not any(path.startswith(pack+'/'+folder+'/') for folder in FOLDERS) or not path.endswith(('.json','.material')):continue
            repeated=[]
            def pairs(seq):
                out={}
                for k,v in seq:
                    if k in out:repeated.append(k)
                    out[k]=v
                return out
            raw=z.read(path)
            try:obj=json5.loads(raw.decode('utf-8-sig'),object_pairs_hook=pairs)
            except (ValueError,UnicodeDecodeError) as ex:errors.append((path,str(ex).splitlines()[0]));continue
            if repeated:dups.append((path,repeated))
            folder=path.split('/')[1];ids=[]
            if folder in ('animation_controllers','render_controllers'):
                section=obj.get(folder,{})
                if not isinstance(section,dict):raise ValueError('unexpected controller section: '+path)
                ids=list(section)
            elif folder=='particles':
                ident=obj.get('particle_effect',{}).get('description',{}).get('identifier')
                if isinstance(ident,str):ids=[ident]
            else:
                section=obj.get('materials',{})
                if isinstance(section,dict):ids=list(section)
            files.append({'path':path,'folder':folder,'sha256':sha256(raw).hexdigest(),'object':obj,'ids':ids})
    return files,errors,dups

def build():
    data={v:collect(f,p) for v,f,p in VERSIONS};old=data['1.6'];a=data['2.8.8'];b=data['2.8.14']
    if a!=b:raise ValueError('2.x client effects files differ')
    if old[0]:raise ValueError('unexpected 1.6 effects files')
    files,errors,dups=b;c=Counter(x['folder'] for x in files)
    out=['# Клиентские контроллеры, частицы и материалы: полные исходные объекты', '',
         'Это справочный архив для описаний из resource pack. Проверены только локальные JSON и `.material` в папках `animation_controllers`, `render_controllers`, `particles`, `materials`. В 1.6 таких файлов по указанным путям нет; это не означает, что ванильные или внешние ресурсы не используются. Все перечисленные файлы 2.8.8 и 2.8.14 побайтово совпадают по SHA-256 и дают одинаковые разобранные объекты.', '',
         'Порядок массивов, численные значения, поля контроллеров, условия, частицы и Molang ниже сохранены; исходные комментарии и форматирование JSON5 не сохраняются. В случае повторных ключей JSON5 оставляет последнее значение; архивы — эталон. Таблица ключей материалов — буквальные имена внутри `materials`, включая возможные метаданные, не утверждение о регистрации каждого ключа как отдельного материала.', '',
         'Сводка файлов: '+', '.join(f'`{k}` — {c[k]}' for k in FOLDERS)+f'; всего {len(files)}.', '',
         '- Ошибки разбора: '+('; '.join(f'`{p}` ({e})' for p,e in errors) if errors else 'нет')+'.',
         '- Повторные ключи: '+('; '.join(f'`{p}`: '+', '.join('`'+k+'`' for k in names) for p,names in dups) if dups else 'нет')+'.', '',
         '| Категория | Исходный файл | Объявленные имена / ключи |', '|---|---|---|']
    for f in files:out.append(f'| `{f["folder"]}` | `{f["path"]}` | '+(', '.join('`'+x+'`' for x in f['ids']) if f['ids'] else '—')+' |')
    out += ['', '## Полные файлы', '']
    for f in files:
        out += [f'### `{f["path"]}`','',f'- SHA-256 исходного файла: `{f["sha256"]}`.','', '```json',json.dumps(f['object'],ensure_ascii=False,indent=2),'```','']
    out += ['Связи client entity, местные/ванильные определения — [граф ресурсов](resource-graph-2.8.14.md). Сами модели — [реестр геометрии](client-geometry-index.md); keyframes — [реестр анимаций](client-animation-index.md); аудио и изображения — [реестр ассетов](assets-2.8.14.md).','']
    return '\n'.join(out)

def main():
    (ROOT/'docs/client-effects-ledger.md').write_text(build(),encoding='utf-8');print('client effects ledger written')
if __name__=='__main__':main()
