"""Observe 2.8.8 Clock/Time overlap with two protocol clients; no remake code."""
import subprocess, threading, time, os, sys
from pathlib import Path
here=Path(__file__).resolve().parent
root=Path('/home/user/swords-analysis/bot-runtime/server')
env={**os.environ,'LD_LIBRARY_PATH':'.'}
server=subprocess.Popen(['./bedrock_server'],cwd=root,env=env,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1,errors='replace')
ready=threading.Event()
def read_server():
 for line in server.stdout:
  if 'Session ID:' not in line: print('SERVER',line.rstrip(),flush=True)
  if 'Server started.' in line: ready.set()
threading.Thread(target=read_server,daemon=True).start()
bots=[]
try:
 if not ready.wait(60): raise RuntimeError('server not ready')
 spawned=[]
 for name in ('ArenaWolfProbe','ArenaWolfObserver'):
  e=threading.Event(); spawned.append(e)
  b=subprocess.Popen(['node',str(here/'bot_wolf.js')],env={**os.environ,'BOT_NAME':name},stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1,errors='replace');bots.append(b)
  def read_bot(bot=b,n=name,ev=e):
   for line in bot.stdout:
    if any(word in line for word in ('BOT SPAWN','BOT ERROR','BOT USE','BOT HELD','BOT POSITION')): print(n,line.rstrip(),flush=True)
    if 'BOT SPAWN' in line:ev.set()
  threading.Thread(target=read_bot,daemon=True).start()
 if not all(x.wait(40) for x in spawned):raise RuntimeError('bots not spawned')
 def cmd(c,delay=0.7):
  print('COMMAND',c,flush=True);server.stdin.write(c+'\n');server.stdin.flush();time.sleep(delay)
 for n in ('ArenaWolfProbe','ArenaWolfObserver'):
  cmd('gamemode creative '+n);cmd('clear '+n);cmd('tp '+n+' 50 100 50',2)
 cmd('fill 47 99 47 55 99 55 stone');cmd('fill 47 100 47 55 105 55 air')
 cmd('gamerule dodaylightcycle false');cmd('time set 18000');cmd('kill @e[type=pig]')
 cmd('summon pig 51 100 50');cmd('tag @e[type=pig,x=51,y=100,z=50,r=5,c=1] add probe')
 cmd('replaceitem entity ArenaWolfProbe slot.weapon.mainhand 0 effect:wolf_sword 1',2)
 cmd('testfor @a[name=ArenaWolfProbe,family=complete_wolf_transformation]',0.3)
 cmd('event entity ArenaWolfProbe wolf_transformation',0.4)
 cmd('testfor @a[name=ArenaWolfProbe,family=complete_wolf_transformation]',0.4)
 print('MARKER WOLF ATTACK',flush=True);bots[0].stdin.write('attack\n');bots[0].stdin.flush();time.sleep(3)
 cmd('testfor @e[type=pig,tag=probe]')
finally:
 for b in bots:
  if b.poll() is None:b.terminate()
 try:
  if server.poll() is None:server.stdin.write('stop\n');server.stdin.flush();server.wait(20)
 except Exception:server.kill()
 print('DONE',flush=True)
