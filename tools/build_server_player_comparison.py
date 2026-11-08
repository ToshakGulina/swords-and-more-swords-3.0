#!/usr/bin/env python3
"""Extract selected player values from all matching vanilla brarchives in the supplied server ZIP."""
import argparse
import hashlib
import json
from pathlib import Path
from zipfile import ZipFile
import json5
from build_brarchive_index import parse_archive
from build_file_completeness_audit import ARCHIVES
from build_server_file_index import MD5,SHA

ROOT=Path(__file__).resolve().parents[1]
KEYS=('minecraft:player.exhaustion','minecraft:player.saturation','minecraft:exhaustion_values','minecraft:block_climber','minecraft:scaffolding_climber','minecraft:type_family')

def selected(raw):
    obj=json5.loads(raw.decode('utf-8-sig'),allow_duplicate_keys=False)
    ent=obj['minecraft:entity'];assert ent['description']['identifier']=='minecraft:player'
    comp=ent['components']
    return {'sha256':hashlib.sha256(raw).hexdigest(),'format_version':obj.get('format_version'),
            'components':{k:({'present':True,'value':comp[k]} if k in comp else {'present':False}) for k in KEYS}}

def build(path):
    m=hashlib.md5();s=hashlib.sha256()
    with path.open('rb') as f:
        while chunk:=f.read(1024*1024):m.update(chunk);s.update(chunk)
    if m.hexdigest()!=MD5 or s.hexdigest()!=SHA:raise ValueError('Server ZIP checksum mismatch')
    refs=[]
    with ZipFile(path) as z:
        for container in sorted(z.namelist()):
            if not container.startswith('behavior_packs/vanilla') or not container.endswith('/__brarchive/entities.brarchive'):continue
            for name,offset,size,content in parse_archive(z.read(container)):
                if name=='player.json':
                    if not size:raise ValueError('player.json unexpectedly zero-length')
                    refs.append({'container':container,'entry':name,**selected(content)})
    addons={}
    for ver,(filename,_) in ARCHIVES.items():
        prefix='Sword_B' if ver=='1.6' else 'Swords_B'
        with ZipFile(ROOT/'sources'/filename) as z:addons[ver]=selected(z.read(f'{prefix}/entities/player.json'))
    return {'method':'literal player component values from all named vanilla entities.brarchive containing player.json; no conclusion about active pack stack','server_zip_md5':MD5,'server_zip_sha256':SHA,'references':refs,'addons':addons}

def display(item,key):
    value=item['components'][key]
    return '`'+json.dumps(value['value'],ensure_ascii=False,sort_keys=True,separators=(',',':'))+'`' if value['present'] else 'отсутствует'

def render(data):
    lines=['# Поля player: аддон и определения внутри серверного ZIP','',
      'Это статическое чтение пользовательского серверного ZIP с фиксированным SHA-256, без запуска. Названия vanilla_1.x — названия внутренних пакетов, **не доказательство того, какой definition будет активен** на сервере или в версии автора. `format_version` — поле JSON, не версия сервера. В них обнаружены разные значения, поэтому отличия с образцами 1.19/1.20 нельзя автоматически считать изменениями, вызванными аддоном. Индекс всего ZIP и метод brarchive — в [проверке сервера](server-archive.md).','',
      '| Источник | format_version | exhaustion | saturation | exhaustion_values | block_climber | scaffolding_climber |','|---|---|---|---|---|---|---|']
    for ver in ARCHIVES:
        obj=data['addons'][ver]
        vals=[display(obj,k) for k in KEYS[:-1]];lines.append('| Аддон '+ver+' | `'+str(obj['format_version'])+'` | '+' | '.join(vals)+' |')
    for obj in data['references']:
        label=obj['container'].split('/')[1];vals=[display(obj,k) for k in KEYS[:-1]];lines.append('| ZIP `'+label+'` | `'+str(obj['format_version'])+'` | '+' | '.join(vals)+' |')
    lines+=['','В таблице `отсутствует` — нет точного ключа, а `""` — **присутствующая пустая строка**. Точные SHA-256 каждого JSON и type_family записаны в [данных](../data/server-player-reference.json). В базовом `vanilla` и четырёх папках 1.16–1.18.10 выбранные exhaustion/saturation совпадают с аддоном, тогда как ряд других папок и два внешних образца имеют max 20 / saturation 5. Нельзя заключить, какие компоненты реально действуют после загрузки и почему исходные файлы отличаются.','',
      'Для повтора: `python tools/build_server_player_comparison.py --server-zip /путь/bedrock-server-1.26.62.1.zip`. Исходники не изменяются.','']
    return '\n'.join(lines)

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--server-zip',type=Path,required=True);p.add_argument('--output',type=Path,default=ROOT/'data/server-player-reference.json');p.add_argument('--markdown-output',type=Path,default=ROOT/'docs/server-player-comparison.md');args=p.parse_args();data=build(args.server_zip);args.output.parent.mkdir(parents=True,exist_ok=True);args.markdown_output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(data,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf-8');args.markdown_output.write_text(render(data),encoding='utf-8');print('Player JSON found:',len(data['references']))

if __name__=='__main__':main()
