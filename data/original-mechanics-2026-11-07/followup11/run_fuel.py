"""Observe unmodified original Coal Sword fuel alongside coal and stick controls."""
import os,subprocess,threading,time
from pathlib import Path
here=Path(__file__).resolve().parent
server=subprocess.Popen(['./bedrock_server'],cwd='/tmp/swords-run/server',env={**os.environ,'LD_LIBRARY_PATH':'.'},stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1,errors='replace');ready=threading.Event();done=threading.Event();spawn=threading.Event();bot=None
def read(p,prefix,event=None,needle=None):
 for l in p.stdout:
  if 'Session ID:' not in l and (prefix=='SERVER' or any(x in l for x in ('BOT SPAWN','BOT ERROR','BOT START','BOT CUSTOM','BOT POSITION'))):print(f'{time.monotonic():.3f}',prefix,l.split('pfid:')[0].rstrip(),flush=True)
  if event and needle in l:event.set()
  if 'FUEL_FINISHED' in l or 'FUEL_PREP_ERR' in l or 'FUEL_ERR' in l:done.set()
threading.Thread(target=read,args=(server,'SERVER',ready,'Server started.'),daemon=True).start()
def cmd(c,t=.7):print('COMMAND',c,flush=True);server.stdin.write(c+'\n');server.stdin.flush();time.sleep(t)
try:
 if not ready.wait(60):raise RuntimeError('server did not start')
 bot=subprocess.Popen(['node',str(here/'bot_fuel.js')],env={**os.environ,'BOT_NAME':'ArenaFuel'},stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1,errors='replace');threading.Thread(target=read,args=(bot,'BOT',spawn,'BOT SPAWN'),daemon=True).start()
 if not spawn.wait(50):raise RuntimeError('bot did not spawn')
 cmd('gamemode creative ArenaFuel');cmd('tp ArenaFuel 50 100 50',4);cmd('gamerule doMobSpawning false');cmd('fill 47 99 47 60 99 53 stone');cmd('setblock 53 100 50 furnace');cmd('setblock 55 100 50 furnace');cmd('setblock 57 100 50 furnace');cmd('scriptevent arena:fuel start',1)
 if not done.wait(460):print('FUEL_TIMEOUT',flush=True)
finally:
 if bot and bot.poll() is None:bot.terminate();bot.wait(5)
 if server.poll() is None:server.stdin.write('stop\n');server.stdin.flush();server.wait(30)
 print('DONE',flush=True)
