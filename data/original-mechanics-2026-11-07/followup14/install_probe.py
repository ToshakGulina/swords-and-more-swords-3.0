import json
from pathlib import Path
server=Path('/tmp/swords-run/server');p=server/'behavior_packs'/'ArenaBeeVictimProbe';(p/'scripts').mkdir(parents=True,exist_ok=True)
manifest={'format_version':2,'header':{'name':'Arena bee victim observer','description':'temporary bee targeting test','uuid':'9389ab3e-e067-4183-a311-f1bd8ae9c624','version':[1,0,0],'min_engine_version':[1,20,50]},'modules':[{'type':'data','uuid':'0d81b284-c9a9-44fb-a467-3c0fa3996f53','version':[1,0,0]},{'type':'script','language':'javascript','entry':'scripts/main.js','uuid':'98fb0e8c-6f1a-4444-84d1-531e8248dba5','version':[1,0,0]}],'dependencies':[{'module_name':'@minecraft/server','version':'1.8.0-beta'}]}
(p/'manifest.json').write_text(json.dumps(manifest));(p/'scripts/main.js').write_text((Path(__file__).parent/'observer.js').read_text())
w=server/'worlds'/'ArenaSlime'/'world_behavior_packs.json';packs=json.loads(w.read_text());packs=[x for x in packs if x['pack_id']!='9389ab3e-e067-4183-a311-f1bd8ae9c624'];packs.insert(0,{'pack_id':manifest['header']['uuid'],'version':[1,0,0]});w.write_text(json.dumps(packs));print('packs',packs)
