import json
from pathlib import Path
server=Path('/tmp/swords-run/server')
p=server/'behavior_packs'/'ArenaGiveProbe'; (p/'scripts').mkdir(parents=True,exist_ok=True)
manifest={'format_version':2,'header':{'name':'Arena Give Observer','description':'temporary read-only inventory observer','uuid':'6968ebd5-33bc-45b4-a15e-c79f5d34a039','version':[1,0,0],'min_engine_version':[1,20,50]},'modules':[{'type':'data','uuid':'f17abacb-8b82-4f2b-8fbf-0a131d668ce9','version':[1,0,0]},{'type':'script','language':'javascript','entry':'scripts/main.js','uuid':'9dc1a051-111b-4390-971d-064a7f7e385b','version':[1,0,0]}],'dependencies':[{'module_name':'@minecraft/server','version':'1.8.0-beta'}]}
(p/'manifest.json').write_text(json.dumps(manifest)); (p/'scripts/main.js').write_text((Path(__file__).parent/'observer.js').read_text())
w=server/'worlds'/'ArenaSlime'/'world_behavior_packs.json'; packs=json.loads(w.read_text()); packs=[x for x in packs if x['pack_id'] not in ('4d6c4cbb-9dee-48f6-a338-a74eea5aad88','6968ebd5-33bc-45b4-a15e-c79f5d34a039')]; packs.insert(0,{'pack_id':manifest['header']['uuid'],'version':[1,0,0]}); w.write_text(json.dumps(packs)); print('packs',packs)
