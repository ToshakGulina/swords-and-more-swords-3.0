#!/usr/bin/env python3
"""Compare manually reviewed screenshot declarations to literal item components."""
import json
import re
import zipfile
from pathlib import Path
import json5

ROOT=Path(__file__).resolve().parents[1]
VERSIONS=[('2.8.8','swordsandmoreswords_2_8_8.mcaddon'),('2.8.14','swordsandmoreswords-2-8-14.mcaddon')]

def items(filename):
    result={}
    with zipfile.ZipFile(ROOT/'sources'/filename) as z:
        for name in z.namelist():
            if not name.startswith('Swords_B/items/') or not name.endswith('.json'):continue
            obj=json5.loads(z.read(name).decode('utf-8-sig'))['minecraft:item']
            ident=obj['description']['identifier']
            if ident in result:raise ValueError('duplicate '+ident)
            c=obj['components'];dur=c.get('minecraft:durability')
            result[ident]={'damage':c.get('minecraft:damage'),'durability':dur.get('max_durability') if isinstance(dur,dict) else None,
                           'enchantable':'minecraft:enchantable' in c,'repairable':'minecraft:repairable' in c}
    return result

def evidence():
    data=json.loads((ROOT/'data/screenshot-stat-evidence.json').read_text(encoding='utf-8'))
    ids=[x['id'] for x in data]
    if len(set(ids))!=len(ids):raise ValueError('duplicate evidence ID')
    if any(not isinstance(row['screenshots'],list) or not row['screenshots'] for row in data):raise ValueError('missing image evidence')
    return data

def generate():
    versions={label:items(filename) for label,filename in VERSIONS}
    images=dict(re.findall(r'\[Screenshot_20261104_(\d{6})_com_kayenworks_mcpeaddons_AddonDetailActivity\.jpg\]\((https://drive\.google\.com/file/d/[A-Za-z0-9_-]+/view)\)',(ROOT/'docs/screenshot-visual-review.md').read_text(encoding='utf-8')))
    rows=evidence(); identifiers=set(versions['2.8.14']);unknown={r['id'] for r in rows}-identifiers
    if unknown:raise ValueError('unknown evidence ID '+str(unknown))
    def printable(v):
        if v is None:return '—'
        if isinstance(v,bool):return 'true' if v else 'false'
        return str(v)
    def components(c):
        return f"{printable(c['damage'])} / {printable(c['durability'])} / "+('задан' if c['enchantable'] else 'нет')+' / '+('задан' if c['repairable'] else 'нет')
    def comparison(row,item):
        matches=[];diff=[];uncomparable=[]
        for key in ('damage','durability'):
            a,b=row[key],item[key]
            if a is None:continue
            if isinstance(a,(int,float)) and not isinstance(a,bool) and isinstance(b,(int,float)) and not isinstance(b,bool):
                (matches if a==b else diff).append(key)
            else:uncomparable.append(key)
        flags=[]
        for key in ('enchantable','repairable'):
            if row[key] is False and item[key]:flags.append(key+': false при заданном компоненте')
            elif row[key] is True and not item[key]:flags.append(key+': true, компонент отсутствует')
        labels=[]
        if diff:labels.append('числа различаются: '+', '.join(diff))
        elif matches:labels.append('числа совпадают: '+', '.join(matches))
        if uncomparable:labels.append('не сопоставимо напрямую: '+', '.join(uncomparable))
        labels+=flags
        return '; '.join(labels) if labels else 'не сопоставлено'
    lines=['# Сопоставление чисел из скриншотов и item JSON 2.x','',
           'Числа и true/false слева вручную считаны с изображений и сохранены в `data/screenshot-stat-evidence.json`. Названия screen → ID сопоставлены вручную; обрезанные поля не угадываются. Данные страницы не имеют подтверждённой версии и являются утверждениями, не измерениями игры. Ссылки ведут на оригинальные JPEG из пользовательской папки; [выборочная визуальная сверка](screenshot-visual-review.md).','',
           'Справа: **буквальные поля** `minecraft:damage`, `minecraft:durability.max_durability`, наличие `minecraft:enchantable`, наличие `minecraft:repairable` в каждом item JSON. Если поля обеих версий равны, показаны вместе; иначе отдельно. `—` = не прочитано на скрине или отсутствует поле в архиве (смотреть столбец), не значение по умолчанию. `Infinite`/`Unbreakable` — слова описания, отсутствие компонента не доказывает бесконечной прочности.','',
           'Совпадение числа не подтверждает реальный урон, формулу прочности или остальное поведение. `true/false` страницы **не эквивалентны** наличию/отсутствию компонента в JSON: флаги указывают на необходимость проверить игру, а не на доказанный баг. Некоторые цифры приводятся с пояснениями о динамических эффектах; ниже сохранена лишь базовая цифра, не эти эффекты.','',
           '| ID | Скриншот | Скрин: damage / durability / enchantable / repairable | 2.x JSON: damage / durability / enchantable / repairable | Сопоставление |','|---|---|---|---|---|']
    for row in rows:
        ident=row['id']; screenshot=' · '.join(f'[{stamp}]({images[stamp]})' for stamp in row['screenshots'])
        seen=' / '.join(printable(row[k]) for k in ('damage','durability','enchantable','repairable'))
        a=versions['2.8.8'][ident];b=versions['2.8.14'][ident]
        value=components(b) if a==b else '2.8.8: '+components(a)+'<br>2.8.14: '+components(b)
        status=comparison(row,b) if a==b else '2.8.8: '+comparison(row,a)+'<br>2.8.14: '+comparison(row,b)
        lines.append(f'| [`{ident}`](items-2.8.14.md#{ident.replace(":", "")}) | {screenshot} | {seen} | {value} | {status} |')
    missing=sorted(identifiers-{r['id'] for r in rows})
    lines += ['',f'Выборка: {len(rows)} ID из {len(identifiers)}; без сопоставленной строки чисел: '+', '.join('`'+m+'`' for m in missing)+'. Наличие названия/ингредиента на другом фрагменте не означает наличия проверенной карточки характеристик.','']
    return '\n'.join(lines)

def main():
    text=generate();(ROOT/'docs/screenshot-stat-comparison.md').write_text(text,encoding='utf-8');print(len(evidence()),'rows')

if __name__=='__main__':main()
