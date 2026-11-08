"""Check manually applied pumpkin_sword tag through respawn, logout and reconnect."""
import os,subprocess,threading,time
from pathlib import Path
here=Path(__file__).resolve().parent;s=subprocess.Popen(['./bedrock_server'],cwd='/tmp/swords-run/server',env={**os.environ,'LD_LIBRARY_PATH':'.'},stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1,errors='replace');ready=threading.Event();bot=None
def out(p,event,needle,prefix):
 for l in p.stdout:
  if 'Session ID:' not in l:print(prefix,l.split('pfid:')[0].rstrip(),flush=True)
  if needle in l:event.set()
threading.Thread(target=out,args=(s,ready,'Server started.','SERVER'),daemon=True).start()
def connect():
 e=threading.Event();p=subprocess.Popen(['node',str(here/'bot_tag.js')],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1,errors='replace');threading.Thread(target=out,args=(p,e,'BOT SPAWN','BOT'),daemon=True).start()
 if not e.wait(50):raise RuntimeError('bot did not spawn')
 return p
def cmd(c,t=1):print('COMMAND',c,flush=True);s.stdin.write(c+'\n');s.stdin.flush();time.sleep(t)
try:
 if not ready.wait(50):raise RuntimeError('server did not start')
 bot=connect();cmd('gamemode survival ArenaTag');cmd('tag ArenaTag add pumpkin_sword');cmd('testfor @a[name=ArenaTag,tag=pumpkin_sword]');cmd('kill ArenaTag',7);cmd('testfor @a[name=ArenaTag,tag=pumpkin_sword]');cmd('tag ArenaTag list');print('MARK LOGOUT',flush=True);bot.terminate();bot.wait(10);time.sleep(4);print('MARK RECONNECT',flush=True);bot=connect();cmd('testfor @a[name=ArenaTag,tag=pumpkin_sword]');cmd('tag ArenaTag list')
finally:
 if bot and bot.poll() is None:bot.terminate();bot.wait(5)
 if s.poll() is None:s.stdin.write('stop\n');s.stdin.flush();s.wait(20)
 print('DONE',flush=True)
