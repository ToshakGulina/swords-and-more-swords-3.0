"""BDS 1.20.50: /give overflow and original 2.8.8 function; read-only observer."""
import os, subprocess, threading, time
from pathlib import Path
here=Path(__file__).resolve().parent
server=subprocess.Popen(['./bedrock_server'],cwd='/tmp/swords-run/server',env={**os.environ,'LD_LIBRARY_PATH':'.'},stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1,errors='replace')
ready=threading.Event();spawned=threading.Event();bot=None
def read(p,prefix):
 for line in p.stdout:
  if 'Session ID:' not in line and (prefix=='SERVER' or any(x in line for x in ('BOT SPAWN','BOT ERROR'))): print(f'{time.monotonic():.3f} {prefix} {line.split("pfid:")[0].rstrip()}',flush=True)
  if 'Server started.' in line:ready.set()
  if 'BOT SPAWN' in line:spawned.set()
threading.Thread(target=read,args=(server,'SERVER'),daemon=True).start()
def cmd(text,delay=.35):
 print('COMMAND',text,flush=True);server.stdin.write(text+'\n');server.stdin.flush();time.sleep(delay)
def snap(name):cmd('scriptevent arena:giveprobe '+name,1)
def reset():cmd('clear ArenaGiveTwo');cmd('execute as ArenaGiveTwo at @s run kill @e[type=item,r=20]')
try:
 if not ready.wait(60):raise RuntimeError('server did not start')
 bot=subprocess.Popen(['node',str(here.parent/'followup9'/'bot_wolf.js')],env={**os.environ,'BOT_NAME':'ArenaGiveTwo'},stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1,errors='replace');threading.Thread(target=read,args=(bot,'BOT'),daemon=True).start()
 if not spawned.wait(60):raise RuntimeError('bot did not spawn')
 cmd('gamerule doMobSpawning false');cmd('gamemode creative ArenaGiveTwo');cmd('tp ArenaGiveTwo 50 110 50',3);cmd('fill 40 99 40 60 99 60 stone');cmd('fill 40 100 40 60 106 60 air');cmd('tp ArenaGiveTwo 50 100 50',2)
 for mode in ('survival','creative'):
  cmd('gamemode '+mode+' ArenaGiveTwo');reset();cmd('give ArenaGiveTwo diamond 2304');snap(mode+'_full_before');cmd('give ArenaGiveTwo iron_sword 1');snap(mode+'_full_after');time.sleep(3);snap(mode+'_full_wait')
 cmd('gamemode survival ArenaGiveTwo');reset()
 for i in range(38):cmd('give ArenaGiveTwo iron_sword 1',.08)
 snap('survival_38_separate');time.sleep(3);snap('survival_38_wait')
 reset();cmd('give ArenaGiveTwo diamond 128');snap('function_before');cmd('execute as ArenaGiveTwo at @s run function give',2);snap('function_after');time.sleep(3);snap('function_wait')
finally:
 if bot and bot.poll() is None:bot.terminate();bot.wait(5)
 if server.poll() is None:server.stdin.write('stop\n');server.stdin.flush();server.wait(30)
 print('DONE',flush=True)
