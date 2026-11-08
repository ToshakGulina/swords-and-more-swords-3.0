#!/usr/bin/env python3
"""Compare literal behavior/resource item icon keys and render offsets."""
from pathlib import Path
from zipfile import ZipFile
import json,json5
from build_quick_reference import read_items,slug
ROOT=Path(__file__).resolve().parents[1]
VERSIONS=(('1.6','SwordsAndMoreSwords.1.6.mcaddon','Sword_B','Sword_R'),('2.8.8','swordsandmoreswords_2_8_8.mcaddon','Swords_B','Swords_R'),('2.8.14','swordsandmoreswords-2-8-14.mcaddon','Swords_B','Swords_R'))

def collect(filename,bp,rp):
    items=read_items(filename,bp);resource_items={}
    with ZipFile(ROOT/'sources'/filename) as z:
        paths=set(z.namelist());atlas_raw=z.read(rp+'/textures/item_texture.json');atlas=json5.loads(atlas_raw.decode('utf-8-sig'))
        for path in sorted(paths):
            if not path.startswith(rp+'/items/') or not path.endswith('.json'):continue
            obj=json5.loads(z.read(path).decode('utf-8-sig'));item=obj['minecraft:item'];ident=item['description']['identifier']
            if ident in resource_items:raise ValueError('duplicate resource item id '+ident)
            resource_items[ident]=(path,obj)
        return items,resource_items,atlas,atlas_raw,paths

def icon_key(comp):
    icon=comp.get('minecraft:icon')
    if isinstance(icon,str):return icon
    if isinstance(icon,dict) and isinstance(icon.get('texture'),str):return icon['texture']
    return None

def val(comp,key):
    if key not in comp:return '—'
    return '`'+json.dumps(comp[key],ensure_ascii=False,separators=(',',':')).replace('|','\\|')+'`'

def atlas_entry(atlas,key):
    data=atlas.get('texture_data',{})
    if key is None:return 'нет подходящего ключа icon'
    if key not in data:return '**ключ не найден точно**'
    return '`'+json.dumps(data[key],ensure_ascii=False,separators=(',',':'))+'`'

def png_ref(data,key,rp):
    _,_,atlas,_,paths=data
    e=atlas.get('texture_data',{}).get(key);texture=e.get('textures') if isinstance(e,dict) else None
    if not isinstance(texture,str):return 'нет простого текстового пути'
    matches=[rp+'/'+texture+ext for ext in ('.png','.tga','.jpg','.jpeg') if rp+'/'+texture+ext in paths]
    return '<br>'.join('`'+p+'`' for p in matches) if matches else 'не найден локальный файл по простому пути'

def build():
    d={v:collect(f,b,r) for v,f,b,r in VERSIONS};old,a,b=d['1.6'],d['2.8.8'],d['2.8.14']
    if set(old[0])!=set(old[1]):raise ValueError('legacy behavior/resource item ids differ')
    if any(x[1]['minecraft:item']['components'].get('minecraft:render_offsets')!='miscellaneous' for x in old[1].values()):raise ValueError('unexpected 1.6 resource item offset')
    old_time=old[0]['effect:sword_of_time'][1]['components'];client_time=old[1]['effect:sword_of_time'][1]['minecraft:item']['components'];atlas=old[2]['texture_data']
    if icon_key(old_time)!='sword_of_time' or icon_key(client_time)!='Sword_of_Time' or 'Sword_of_Time' in atlas or atlas.get('sword_of_time')!={'textures':'textures/items/Sword_of_Time'} or 'Sword_R/textures/items/Sword_of_Time.png' not in old[4]:raise ValueError('unexpected 1.6 Sword of Time icon data')
    if a[1] or b[1]:raise ValueError('unexpected 2.x resource item files')
    if set(a[0])!=set(b[0]) or any(a[0][id][1]['components']!=b[0][id][1]['components'] for id in a[0]) or a[3]!=b[3]:raise ValueError('2.x components or atlas bytes differ')
    count16=sum('minecraft:render_offsets' in item['components'] for _,item in old[0].values());count2=sum('minecraft:render_offsets' in item['components'] for _,item in b[0].values())
    out=['# Значки и render_offsets предметов: буквальные источники', '',
         'В 1.6 сопоставлены behavior `Sword_B/items/` и отдельные client `Sword_R/items/` по точному `description.identifier`. В 2.x используются item-компоненты behavior; одноимённых файлов `Swords_R/items/` в архивах нет. Колонки сохраняют **исходный тип** icon и полные render_offsets; `—` означает отсутствие поля, не нулевое смещение и не отсутствие стандартного отображения.', '',
         f'В 1.6 для {len(old[0])} ID найдены одноимённые client-файлы, behavior render_offsets задан у {count16}; в client каждый предмет объявляет `"miscellaneous"`. В 2.x у {count2} из {len(b[0])} item объявлены render_offsets; компонентные объекты и исходный item_texture.json в 2.8.8/2.8.14 совпадают. Другие файлы, включая Ice events, могут различаться.', '',
         'Поиск в `texture_data` — **строгое совпадение регистра** извлечённого icon-ключа; записи atlas приведены буквально. Простая проверка файла делает только прямую проверку пути `textures` с расширениями png/tga/jpg/jpeg. Отсутствие точного ключа или локального файла — наблюдение о данных, не вывод о том, как движок разрешает источники. Хэши и размеры изображений — в [реестре 1.6](assets-1.6.md) и [2.8.14](assets-2.8.14.md).', '',
         'В частности, 1.6 `effect:sword_of_time`: behavior icon `{ "texture":"sword_of_time" }` находит этот ключ atlas, но client icon — строка `Sword_of_Time`, и такого **точного ключа** в atlas нет. При этом значение найденного atlas-поля ссылается на `textures/items/Sword_of_Time`, а соответствующий PNG существует. Это три разные строки в разных местах; их нельзя молча слить или менять регистр в источнике.', '',
         '## 1.6: behavior и resource item', '', '| Точный ID | Behavior icon / atlas | Client icon / atlas | Client render_offsets | PNG по behavior atlas |', '|---|---|---|---|---|']
    for id,(_,it) in sorted(old[0].items()):
        bc=it['components'];rc=old[1][id][1]['minecraft:item']['components'];bk=icon_key(bc);rk=icon_key(rc)
        out.append(f'| [`{id}`](items-1.6.md#{slug(id)}) | {val(bc,"minecraft:icon")}<br>{atlas_entry(old[2],bk)} | {val(rc,"minecraft:icon")}<br>{atlas_entry(old[2],rk)} | {val(rc,"minecraft:render_offsets")} | {png_ref(old,bk,"Sword_R")} |')
    out += ['', '## 2.8.8 и 2.8.14: behavior item', '', '| Точный ID | icon / atlas | render_offsets целиком | PNG по atlas |', '|---|---|---|---|']
    for id,(_,it) in sorted(b[0].items()):
        c=it['components'];key=icon_key(c)
        out.append(f'| [`{id}`](items-2.8.14.md#{slug(id)}) | {val(c,"minecraft:icon")}<br>{atlas_entry(b[2],key)} | {val(c,"minecraft:render_offsets")} | {png_ref(b,key,"Swords_R")} |')
    out += ['', 'Это статическое сопоставление только прямо указанных atlas-ключей и offsets, без вычисления transform или косвенных client-моделей. См. [сравнение значков](icon-comparison.md), [клиентские модели](client-geometry-index.md) и [полные item-определения](quick-reference.md).', '']
    return '\n'.join(out)

def main():
    (ROOT/'docs/item-visual-index.md').write_text(build(),encoding='utf-8');print('item visual index written')
if __name__=='__main__':main()
