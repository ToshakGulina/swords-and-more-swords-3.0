"""Silver Sword vs Alpha Wolf, using temporary read-only health probe (Bedrock 1.20.50)."""
import os,subprocess,threading,time
from pathlib import Path
here=Path(__file__).resolve().parent
s=subprocess.Popen(['./bedrock_server'],cwd='/tmp/swords-run/server',env={**os.environ,'LD_LIBRARY_PATH':'.'},stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1,errors='replace');ready=threading.Event();spawn=threading.Event();bot=None
def out(p,event,needle,prefix):
 for line in p.stdout:
  if 'Session ID:' not in line and any(x in line for x in ('ARENA_', 'ERROR','WARN','INFO','BOT SPAWN','BOT ATTACK','BOT ENTITY','BOT HELD','BOT POSITION','BOT START','BOT ERROR','BOT MOB')):print(f'{time.monotonic():.3f}',prefix,line.split('pfid:')[0].rstrip(),flush=True)
  if needle in line:event.set()
threading.Thread(target=out,args=(s,ready,'Server started.','SERVER'),daemon=True).start()
def cmd(c,t=0.8):print('COMMAND',c,flush=True);s.stdin.write(c+'\n');s.stdin.flush();time.sleep(t)
def attack():bot.stdin.write('attack\n');bot.stdin.flush();time.sleep(2)
try:
 if not ready.wait(50):raise RuntimeError('server startup failed')
 bot=subprocess.Popen(['node',str(here/'bot_wolf.js')],env={**os.environ,'BOT_NAME':'ArenaSilver'},stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1,errors='replace');threading.Thread(target=out,args=(bot,spawn,'BOT SPAWN','BOT'),daemon=True).start()
 if not spawn.wait(55):raise RuntimeError('bot did not spawn')
 cmd('gamemode creative ArenaSilver');cmd('gamerule doMobSpawning false');cmd('gamerule dodaylightcycle false');cmd('time set 18000');cmd('weather clear 200');cmd('tp ArenaSilver 50 100 50',3);cmd('fill 46 99 46 56 99 56 stone');cmd('fill 46 100 46 56 105 56 air');cmd('kill @e[type=entity:alpha_wolf]',0.4)
 for tick in (0,1,4799,4800,18500,19200,23999,24000,42000,191999,192000,210000):
  print('MARK TIME '+str(tick),flush=True);cmd('time set '+str(tick),0.3);cmd('time query day',0.3);cmd('time query daytime',0.3);cmd('summon entity:alpha_wolf 51 100 50',0.25);cmd('tag @e[type=entity:alpha_wolf,c=1] add probe',0.3);cmd('testfor @e[type=entity:alpha_wolf,tag=probe]',1.5);cmd('testfor @e[type=entity:alpha_wolf,tag=probe]',0.3);cmd('kill @e[type=entity:alpha_wolf]',0.3)

finally:
 if bot and bot.poll() is None:bot.terminate();bot.wait(5)
 if s.poll() is None:s.stdin.write('stop\n');s.stdin.flush();s.wait(20)
 print('DONE',flush=True)
