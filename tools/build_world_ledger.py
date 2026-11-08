#!/usr/bin/env python3
"""Index all supplied behavior-pack loot, recipes, blocks, spawn, features and trades."""
import json,zipfile
from fractions import Fraction
from pathlib import Path
import json5
ROOT=Path(__file__).resolve().parents[1]
VERSIONS=[('1.6','SwordsAndMoreSwords.1.6.mcaddon','Sword_B'), ('2.8.8','swordsandmoreswords_2_8_8.mcaddon','Swords_B'), ('2.8.14','swordsandmoreswords-2-8-14.mcaddon','Swords_B')]
CATEGORIES=('loot_tables','blocks','recipes','spawn_rules','features','feature_rules','trading')

def compact(x): return json.dumps(x,ensure_ascii=False,separators=(',',':'))

def run(version, filename, pack):
    with zipfile.ZipFile(ROOT/'sources'/filename) as z:
        files={n:z.read(n) for n in z.namelist() if n.endswith('.json') and any(n.startswith(pack+'/'+x+'/') for x in CATEGORIES)}
    out=[f'# Блоки, рецепты, генерация, торговля и таблицы добычи — архив {version}','',
         'Структурная выписка JSON файлов каталогов loot_tables, blocks, recipes, spawn_rules, features, feature_rules и trading behavior pack. Числа, условия, функции, веса, число бросков и порядок массивов приводятся как в JSON5. Это не ручное доказательство того, что файл загружен/вызывается, и не включает полный анализ структур и исполнения в игре.', '',
         'Для loot приводятся **сырые относительные доли** по явно указанным целым weight только если у всех записей пула они есть и сумма > 0. Число бросков, условия пула/записи, типы записей, функции, удача и семантика движка могут изменить результат: доли не являются вероятностью получить предмет. При пропущенном весе доля не вычисляется. Все данные самого пула приведены целиком.', '']
    for p,raw in sorted(files.items()):
        s=raw.decode('utf-8-sig')
        dups=[]
        def pairs(pairs):
            v={}
            for k,x in pairs:
                if k in v: dups.append(k)
                v[k]=x
            return v
        out += [f'## `{p}`', '']
        try: obj=json5.loads(s,object_pairs_hook=pairs)
        except Exception as e:
            out += [f'Ошибка JSON5: `{str(e).splitlines()[0]}`; читать оригинал.', '']; continue
        if dups: out += [f'Повторяющиеся ключи {compact(dups)}; выписка может терять значения; читать оригинал.', '']
        if '/loot_tables/' in p and isinstance(obj,dict):
            for i,pool in enumerate(obj.get('pools',[])):
                if not isinstance(pool,dict): continue
                entries=pool.get('entries',[])
                if not isinstance(entries,list): continue
                weights=[e.get('weight') if isinstance(e,dict) else None for e in entries]
                can=bool(weights) and all(isinstance(w,int) and not isinstance(w,bool) and w>=0 for w in weights) and sum(weights)>0
                out.append(f'- Пул {i}, rolls `{compact(pool.get("rolls","не указан"))}`, weights `{compact(weights)}`' + (f', сумма {sum(weights)}.' if can else '; доли не вычислены.'))
                if can:
                    for j,e in enumerate(entries):
                        f=Fraction(weights[j],sum(weights));out.append(f'  - Запись {j}: `{compact(e.get("name",e.get("type","нет имени")))}` — {f.numerator}/{f.denominator} ({float(f)*100:.6g}%) от суммы явно указанных весов, до учёта условий и функций.')
            out.append('')
        out += ['```json',json.dumps(obj,ensure_ascii=False,indent=2),'```','']
    (ROOT/'docs'/f'world-ledger-{version}.md').write_text('\n'.join(out)+'\n',encoding='utf-8')
    return len(files)
if __name__=='__main__':
    for args in VERSIONS: print(args[0], 'world JSON:', run(*args))
