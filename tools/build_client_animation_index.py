#!/usr/bin/env python3
"""Index complete local client animations and literal client-entity aliases."""
from collections import defaultdict
from hashlib import sha256
from pathlib import Path
from zipfile import ZipFile
import json,json5
from build_quick_reference import slug
ROOT=Path(__file__).resolve().parents[1]
VERSIONS=(('1.6','SwordsAndMoreSwords.1.6.mcaddon','Sword_R'),('2.8.8','swordsandmoreswords_2_8_8.mcaddon','Swords_R'),('2.8.14','swordsandmoreswords-2-8-14.mcaddon','Swords_R'))

def collect(filename,pack):
    animations=[];aliases=defaultdict(list);errors=[];dups=[]
    with ZipFile(ROOT/'sources'/filename) as z:
        paths=[p for p in sorted(z.namelist()) if (p.startswith(pack+'/animations/') or p.startswith(pack+'/entity/')) and p.endswith('.json')]
        for path in paths:
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
            if path.startswith(pack+'/animations/'):
                definitions=obj.get('animations',{})
                if not isinstance(definitions,dict):raise ValueError('unexpected animation section: '+path)
                for ident,data in definitions.items():
                    if not isinstance(data,dict):raise ValueError('unexpected animation definition: '+path)
                    animations.append({'path':path,'id':ident,'format_version':obj.get('format_version'),'sha256':sha256(raw).hexdigest(),'definition':data})
            else:
                desc=obj.get('minecraft:client_entity',{}).get('description',{});entries=desc.get('animations',{})
                if not isinstance(entries,dict):raise ValueError('unexpected animation aliases: '+path)
                for name,target in entries.items():
                    if isinstance(target,str):aliases[target].append((path,desc.get('identifier'),name))
    return animations,dict(aliases),errors,dups

def literal(obj,key):
    return '`'+json.dumps(obj[key],ensure_ascii=False,separators=(',',':'))+'`' if key in obj else '—'

def build():
    all_data={v:collect(f,p) for v,f,p in VERSIONS};old=all_data['1.6'];a=all_data['2.8.8'];b=all_data['2.8.14']
    if a!=b:raise ValueError('2.x client animations, source bytes or aliases differ')
    if old[0]:raise ValueError('unexpected 1.6 animation files')
    anims,aliases,errors,dups=b;ids=[x['id'] for x in anims]
    if len(ids)!=len(set(ids)):raise ValueError('duplicate animation ids require disambiguated anchors')
    files={x['path'] for x in anims}
    out=['# Клиентские анимации: определения и прямые aliases', '',
         f'В `Sword_R/animations/` 1.6 не обнаружено локальных JSON-анимаций; это не означает отсутствия ванильной анимации или ресурсов за пределами этого пути. В 2.x найдено **{len(anims)}** определений в **{len(files)}** JSON-файлах. Сравнение исходных SHA-256 файлов анимаций и структурное сравнение извлечённых aliases показывает совпадение двух архивов 2.x; остальной resource pack может отличаться.', '',
         'Таблица сохраняет буквальные `loop`, `animation_length`, `override_previous_animation` и список bones; `—` означает отсутствие поля, не false и не ноль. Имена references ищутся только в `description.animations` разобранных client entity JSON и обозначают объявленный alias, а не установленное применение. Отсутствие alias **не** означает неиспользуемость: например, `animation.player.explode` прямо назван в `playanimation` у Creeper Sword. Контроллеры, `scripts.animate`, команды и Molang не интерпретируются.', '',
         'Ниже каждый animation-объект приведён целиком, в том числе все временные ключи, значения, Molang-выражения, пустые объекты и порядок списков; JSON5-комментарии и форматирование не сохраняются. Если ключи повторяются, JSON5 оставляет последнее значение; исходный архив остаётся эталоном. Время/единицы и поведение interpolation не выводятся из этого индекса.', '',
         '- Ошибки разбора: '+('; '.join(f'`{p}` ({err})' for p,err in errors) if errors else 'нет')+'.',
         '- Повторные ключи: '+('; '.join(f'`{p}`: '+', '.join('`'+k+'`' for k in names) for p,names in dups) if dups else 'нет')+'.', '',
         '| Animation ID | loop | animation_length | override_previous_animation | bones | Локальные client aliases |','|---|---|---|---|---|---|']
    for x in anims:
        data=x['definition'];bone=data.get('bones',{})
        if not isinstance(bone,dict):raise ValueError('non-object bones '+x['id'])
        bs=('не задано' if 'bones' not in data else (', '.join('`'+name+'`' for name in bone) or 'пустой объект'))
        ref='<br>'.join(f'`{p}` · `{ident}` · `{name}`' for p,ident,name in aliases.get(x['id'],[])) or 'не найдено в client entity'
        out.append(f'| [`{x["id"]}`](#{slug(x["id"])}) | {literal(data,"loop")} | {literal(data,"animation_length")} | {literal(data,"override_previous_animation")} | {bs} | {ref} |')
    out += ['', '## Полные объекты анимаций', '']
    for x in anims:
        out += [f'### `{x["id"]}`', '',f'- `{x["path"]}`; исходный SHA-256 `{x["sha256"]}`; format_version `{x["format_version"]}`.', '', '```json',json.dumps(x['definition'],ensure_ascii=False,indent=2),'```','']
    out += ['Сопоставление прочих моделей, геометрии и render controllers — в [графе ресурсов](resource-graph-2.8.14.md); оригинальные аудиофайлы и изображения — в [реестре ассетов](assets-2.8.14.md).','']
    return '\n'.join(out)

def main():
    (ROOT/'docs/client-animation-index.md').write_text(build(),encoding='utf-8');print('client animation index written')
if __name__=='__main__':main()
