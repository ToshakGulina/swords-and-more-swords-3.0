"""Original 2.8.8 fatal damage overlap, no modifications to original packs."""
import os,subprocess,threading,time
from pathlib import Path
here=Path(__file__).resolve().parent
s=subprocess.Popen(['./bedrock_server'],cwd='/tmp/swords-run/server',env={**os.environ,'LD_LIBRARY_PATH':'.'},stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1,errors='replace');ready=threading.Event();spawn=threading.Event();bot=None
def out(p,event,needle,prefix):
 for line in p.stdout:
  if 'Session ID:' not in line: print(f'{time.monotonic():.3f}',prefix,line.split('pfid:')[0].rstrip(),flush=True)
  if needle in line:event.set()
threading.Thread(target=out,args=(s,ready,'Server started.','SERVER'),daemon=True).start()
def cmd(c,t=0.8):print('COMMAND',c,flush=True);s.stdin.write(c+'\n');s.stdin.flush();time.sleep(t)
try:
 if not ready.wait(50):raise RuntimeError('server startup failed')
 bot=subprocess.Popen(['node',str(here/'bot_centella.js')],env={**os.environ,'BOT_NAME':'ArenaCentella'},stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1,errors='replace');threading.Thread(target=out,args=(bot,spawn,'BOT SPAWN','BOT'),daemon=True).start()
 if not spawn.wait(55):raise RuntimeError('bot did not spawn')
 cmd('gamemode creative ArenaCentella');cmd('tp ArenaCentella 50 100 50',4);cmd('gamerule doMobSpawning false');cmd('weather clear 200');cmd('fill 45 99 45 60 99 55 stone');cmd('fill 45 100 45 60 105 55 air')
 for i in range(5):
  print('MARK TRIAL',i,flush=True);cmd('kill @e[type=entity:centella]',1);cmd('summon entity:centella 55 100 50',1.5);cmd('testfor @e[type=entity:centella]',0.6);cmd('damage @e[type=entity:centella,c=1] 250 magic',3)
finally:
 if bot and bot.poll() is None:bot.terminate();bot.wait(5)
 if s.poll() is None:s.stdin.write('stop\n');s.stdin.flush();s.wait(20)
 print('DONE',flush=True)
