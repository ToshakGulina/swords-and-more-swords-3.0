"""Original Sea Sword, server client-authoritative: air -> water -> air -> no sword."""
import os, subprocess, threading, time
from pathlib import Path
here=Path(__file__).resolve().parent
s=subprocess.Popen(['./bedrock_server'],cwd='/tmp/swords-run/server',env={**os.environ,'LD_LIBRARY_PATH':'.'},stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1,errors='replace')
ready=threading.Event();spawn=threading.Event();bot=None
def out(proc,event,needle,prefix):
 for line in proc.stdout:
  if 'Session ID:' not in line:print(f'{time.monotonic():.3f}',prefix,line.split('pfid:')[0].rstrip(),flush=True)
  if needle in line:event.set()
threading.Thread(target=out,args=(s,ready,'Server started.','SERVER'),daemon=True).start()
try:
 if not ready.wait(50):raise RuntimeError('server failed to start')
 bot=subprocess.Popen(['node',str(here/'bot_lapis.js')],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1,errors='replace')
 threading.Thread(target=out,args=(bot,spawn,'BOT SPAWN','BOT'),daemon=True).start()
 if not spawn.wait(55):raise RuntimeError('bot did not spawn')
 def cmd(c,t=0.8):
  print('COMMAND',c,flush=True);s.stdin.write(c+'\n');s.stdin.flush();time.sleep(t)
 cmd('gamemode creative ArenaLapis');cmd('tp ArenaLapis 50 100 50',3);cmd('fill 45 99 45 55 99 55 stone');cmd('fill 45 100 45 55 105 55 air');cmd('clear ArenaLapis');cmd('xp -100L ArenaLapis')
 print('MARK HOLD',flush=True);cmd('replaceitem entity ArenaLapis slot.weapon.mainhand 0 effect:lapis_sword 1',3);cmd('testfor @a[name=ArenaLapis,family=lapis_sword]');time.sleep(20)
 print('MARK REMOVE',flush=True);cmd('replaceitem entity ArenaLapis slot.weapon.mainhand 0 air',3);cmd('testfor @a[name=ArenaLapis,family=lapis_sword]');time.sleep(10)
finally:
 if bot and bot.poll() is None:bot.terminate();bot.wait(5)
 if s.poll() is None:s.stdin.write('stop\n');s.stdin.flush();s.wait(20)
 print('DONE',flush=True)
