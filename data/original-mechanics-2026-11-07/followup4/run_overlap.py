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
 for name in ('ArenaOverlapClock','ArenaOverlapTime'):
  e=threading.Event(); spawned.append(e)
  b=subprocess.Popen(['node',str(here/'bot_overlap.js')],env={**os.environ,'BOT_NAME':name},stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1,errors='replace');bots.append(b)
  def read_bot(bot=b,n=name,ev=e):
   for line in bot.stdout:
    if any(word in line for word in ('BOT SPAWN','BOT ERROR','BOT USE','BOT HELD','BOT POSITION')): print(n,line.rstrip(),flush=True)
    if 'BOT SPAWN' in line:ev.set()
  threading.Thread(target=read_bot,daemon=True).start()
 if not all(x.wait(40) for x in spawned):raise RuntimeError('bots not spawned')
 def cmd(c,delay=0.7):
  print('COMMAND',c,flush=True);server.stdin.write(c+'\n');server.stdin.flush();time.sleep(delay)
 for n in ('ArenaOverlapClock','ArenaOverlapTime'):
  cmd('gamemode creative '+n);cmd('clear '+n);cmd('tp '+n+' 50 100 50',2)
 cmd('gamerule dodaylightcycle false');cmd('gamerule randomtickspeed 7');cmd('time set 1000')
 cmd('replaceitem entity ArenaOverlapClock slot.weapon.mainhand 0 effect:clock_sword 1',3)
 cmd('replaceitem entity ArenaOverlapTime slot.weapon.mainhand 0 effect:time_sword 1',3)
 cmd('testfor @a[name=ArenaOverlapTime,family=time_sword]');cmd('gamerule randomtickspeed');cmd('time query daytime')
 print('MARKER CLOCK ACTIVATE WHILE TIME ACTIVE',flush=True);bots[0].stdin.write('use\n');bots[0].stdin.flush();time.sleep(1)
 cmd('testfor @a[name=ArenaOverlapClock,family=clock_sword_skill]');cmd('gamerule randomtickspeed');cmd('time query daytime',1);cmd('gamerule randomtickspeed');cmd('time query daytime',1);cmd('gamerule randomtickspeed');cmd('time query daytime',3)
 print('MARKER CLOCK ENDED WHILE TIME ACTIVE',flush=True);cmd('gamerule randomtickspeed');cmd('time query daytime',1)
 cmd('replaceitem entity ArenaOverlapTime slot.weapon.mainhand 0 air',3);cmd('gamerule randomtickspeed');cmd('time query daytime')
finally:
 for b in bots:
  if b.poll() is None:b.terminate()
 try:
  if server.poll() is None:server.stdin.write('stop\n');server.stdin.flush();server.wait(20)
 except Exception:server.kill()
 print('DONE',flush=True)
