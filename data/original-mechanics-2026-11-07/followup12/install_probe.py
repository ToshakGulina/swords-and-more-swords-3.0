"""Install a temporary observer and two *separate* control mobs; never edit original BP."""
import hashlib
import json
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
SERVER = Path('/tmp/swords-run/server')
probe = SERVER / 'behavior_packs' / 'ArenaJumpProbe'
(probe / 'entities').mkdir(parents=True, exist_ok=True)
(probe / 'scripts').mkdir(parents=True, exist_ok=True)
manifest = {
    'format_version': 2,
    'header': {'name':'Arena jump probe', 'description':'temporary observation and controls',
               'uuid':'4d6c4cbb-9dee-48f6-a338-a74eea5aad88', 'version':[1,0,0], 'min_engine_version':[1,20,50]},
    'modules': [
        {'type':'data','uuid':'de68b793-7a2d-4bac-8308-108585343484','version':[1,0,0]},
        {'type':'script','language':'javascript','entry':'scripts/main.js',
         'uuid':'de294ba5-b94d-4ab1-a67e-e8bdd7c9a7e3','version':[1,0,0]}],
    'dependencies':[{'module_name':'@minecraft/server','version':'1.8.0-beta'}],
}
(probe / 'manifest.json').write_text(json.dumps(manifest), encoding='utf8')
(probe / 'scripts' / 'main.js').write_text((HERE / 'observer.js').read_text(encoding='utf8'), encoding='utf8')
with ZipFile(ROOT / 'sources' / 'swordsandmoreswords_2_8_8.mcaddon') as z:
    original_bytes = z.read('Swords_B/entities/slime_king.json')
original_installed = (SERVER / 'behavior_packs' / 'Swords_B' / 'entities' / 'slime_king.json').read_bytes()
assert original_bytes == original_installed, 'Original boss file must remain unchanged'
source = original_bytes.decode('utf-8-sig').replace('\r\n', '\n')
first = '      "minecraft:movement.jump": {\n        "jump_delay": [ 0.5, 1.5 ]\n      },\n'
second = '      "minecraft:movement.jump": {\n        "jump_delay": [ 0.16,  0.4 ]\n      },\n'
assert source.count(first) == source.count(second) == 1
for name, remove in [('slow', second), ('fast', first)]:
    control = source.replace('"identifier": "entity:slime_king"', f'"identifier": "arena:slime_king_{name}"').replace(remove, '')
    (probe / 'entities' / f'slime_king_{name}.json').write_text(control, encoding='utf8')
    print(name, 'sha256', hashlib.sha256(control.encode()).hexdigest())
print('original sha256', hashlib.sha256(original_bytes).hexdigest())
