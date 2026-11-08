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
 for name in ('ArenaSpongeTest','ArenaDummy'):
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
 for n in ('ArenaSpongeTest','ArenaDummy'):
  cmd('gamemode creative '+n);cmd('clear '+n);cmd('tp '+n+' 50 100 50',2)
 cmd('fill 47 99 47 53 99 53 stone');cmd('fill 47 100 47 53 115 53 air')
 cmd('weather rain 120');cmd('replaceitem entity ArenaSpongeTest slot.weapon.mainhand 0 effect:sponge_sword 1',2)
 for step in range(9):
  print('MARKER SAMPLE',step, 'monotonic',time.monotonic(),flush=True)
  cmd('scoreboard players list ArenaSpongeTest',0.3)
  cmd('testfor @a[name=ArenaSpongeTest,hasitem={item=effect:wet_sponge_sword,location=slot.weapon.mainhand}]',2)
 cmd('weather clear 5')
finally:
 for b in bots:
  if b.poll() is None:b.terminate()
 try:
  if server.poll() is None:server.stdin.write('stop\n');server.stdin.flush();server.wait(20)
 except Exception:server.kill()
 print('DONE',flush=True)
