from pathlib import Path
import sys,io,shutil,json,struct,zipfile
sys.path.insert(0,'/home/user/swords-analysis/deps')
import nbtlib
root=Path('/home/user/swords-analysis/bot-runtime/server')
archive=Path('/home/user/swords-and-more-swords-3.0/sources/swordsandmoreswords_2_8_8.mcaddon')
with zipfile.ZipFile(archive) as z:
 for n in z.namelist():
  q=Path(n)
  if q.is_absolute() or '..' in q.parts: raise ValueError(n)
 for kind,dest in [('Swords_B','behavior_packs/Swords_B'),('Swords_R','resource_packs/Swords_R')]:
  d=root/dest; d.mkdir(parents=True,exist_ok=True)
  for n in z.namelist():
   if not n.startswith(kind+'/') or n.endswith('/'):continue
   output=d/n[len(kind)+1:];output.parent.mkdir(parents=True,exist_ok=True)
   with z.open(n) as f,output.open('wb') as o:shutil.copyfileobj(f,o)
source=root/'worlds/Bot movement';target=root/'worlds/Bot original attack';shutil.copytree(source,target,dirs_exist_ok=True)
p=target/'level.dat';data=p.read_bytes();f=nbtlib.File.parse(io.BytesIO(data[8:]),byteorder='little')
f['experiments']=nbtlib.Compound({k:nbtlib.Byte(1) for k in ['experiments_ever_used','saved_with_toggled_experiments','data_driven_items','upcoming_creator_features','gametest','experimental_molang_features']})
f['LevelName']=nbtlib.String('Bot original attack'); out=io.BytesIO();f.write(out,byteorder='little');payload=out.getvalue();p.write_bytes(data[:4]+struct.pack('<I',len(payload))+payload)
for file,uuid in [('world_behavior_packs.json','1acf4d4b-3a3c-1be3-bc21-9512946109b1'),('world_resource_packs.json','3f15ae41-a1c1-4111-aa1e-855a98a06316')]:
 (target/file).write_text(json.dumps([{'pack_id':uuid,'version':[1,0,0]}]))
p=root/'server.properties';p.write_text(p.read_text().replace('level-name=Bot movement','level-name=Bot original attack'))
