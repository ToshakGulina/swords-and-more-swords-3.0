import json
from pathlib import Path
server=Path('/tmp/swords-run/server');p=server/'behavior_packs'/'ArenaSpectralProbe';(p/'scripts').mkdir(parents=True,exist_ok=True)
manifest={'format_version':2,'header':{'name':'Arena spectral crystal observer','description':'Temporary test of original spectral crystal behavior','uuid':'256743ab-f5fb-41f4-9d99-76898dcff498','version':[1,0,0],'min_engine_version':[1,20,50]},'modules':[{'type':'data','uuid':'243c16c9-ce6a-4591-b868-3ca8a97f4b15','version':[1,0,0]},{'type':'script','language':'javascript','entry':'scripts/main.js','uuid':'7d15ab69-0b98-4af8-90fd-aa504c871ad2','version':[1,0,0]}],'dependencies':[{'module_name':'@minecraft/server','version':'1.8.0-beta'}]}
(p/'manifest.json').write_text(json.dumps(manifest));(p/'scripts/main.js').write_text((Path(__file__).parent/'observer.js').read_text())
w=server/'worlds'/'ArenaSlime'/'world_behavior_packs.json';packs=json.loads(w.read_text());packs=[x for x in packs if x['pack_id']!=manifest['header']['uuid']];packs.insert(0,{'pack_id':manifest['header']['uuid'],'version':[1,0,0]});w.write_text(json.dumps(packs));print('packs',packs)
