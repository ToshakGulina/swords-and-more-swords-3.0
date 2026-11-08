"""Original 2.8.8 in 1.20.50: control cast, then cast and switch before shots."""
import os,sys,subprocess,threading,time
from pathlib import Path
here=Path(__file__).resolve().parent; root=Path('/tmp/swords-run/server')
s=subprocess.Popen(['./bedrock_server'],cwd=root,env={**os.environ,'LD_LIBRARY_PATH':'.'},stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1,errors='replace')
ready=threading.Event();spawn=threading.Event();bot=None
def sr():
 for line in s.stdout:
  if 'Session ID:' not in line:print('SERVER',line.split('pfid:')[0].rstrip(),flush=True)
  if 'Server started.' in line:ready.set()
threading.Thread(target=sr,daemon=True).start()
try:
 if not ready.wait(50):raise RuntimeError('server did not start')
 bot=subprocess.Popen(['node',str(here/'bot_blaze.js')],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1,errors='replace')
 def br():
  for line in bot.stdout:
   print(line.rstrip(),flush=True)
   if 'BOT SPAWN' in line:spawn.set()
 threading.Thread(target=br,daemon=True).start()
 if not spawn.wait(55):raise RuntimeError('bot did not spawn')
 def cmd(c,delay=0.6):
  print('COMMAND',c,flush=True);s.stdin.write(c+'\n');s.stdin.flush();time.sleep(delay)
 cmd('gamemode creative ArenaBlaze');cmd('tp ArenaBlaze 50 100 50',3)
 cmd('fill 45 99 45 55 99 55 stone');cmd('fill 45 100 45 55 115 55 air');cmd('weather clear 120');cmd('clear ArenaBlaze')
 cmd('replaceitem entity ArenaBlaze slot.weapon.mainhand 0 effect:blaze_sword 1',6)
 cmd('testfor @a[name=ArenaBlaze,hasitem={item=effect:blaze_sword,location=slot.weapon.mainhand}]');cmd('testfor @a[name=ArenaBlaze,family=blaze_sword]');print('MARK CONTROL use; keep sword',flush=True);bot.stdin.write('use\n');bot.stdin.flush();time.sleep(1)
 cmd('testfor @a[name=ArenaBlaze,family=blaze_sword_skill]',0.3);time.sleep(10)
 print('MARK CONTROL END',flush=True);time.sleep(12)
 print('MARK SWITCH use',flush=True);bot.stdin.write('use\n');bot.stdin.flush();time.sleep(1)
 cmd('testfor @a[name=ArenaBlaze,family=blaze_sword_skill]',0.2)
 cmd('replaceitem entity ArenaBlaze slot.weapon.mainhand 0 air',0.6);cmd('testfor @a[name=ArenaBlaze,hasitem={item=effect:blaze_sword,location=slot.weapon.mainhand}]')
 cmd('testfor @a[name=ArenaBlaze,family=blaze_sword_skill]',0.5)
 time.sleep(9);print('MARK SWITCH END',flush=True)
finally:
 if bot and bot.poll() is None:bot.terminate()
 if s.poll() is None:
  try:s.stdin.write('stop\n');s.stdin.flush();s.wait(20)
  except Exception:s.kill()
 print('DONE',flush=True)
