"""Actual dropped Lightning Sword, tags isolated; original 2.8.8 / Bedrock 1.20.50."""
import os,subprocess,threading,time
from pathlib import Path
here=Path(__file__).resolve().parent
server=subprocess.Popen(['./bedrock_server'],cwd='/tmp/swords-run/server',env={**os.environ,'LD_LIBRARY_PATH':'.'},stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1,errors='replace');ready=threading.Event();spawn=threading.Event();bot=None
def read(p,e,needle,prefix):
 for l in p.stdout:
  if 'Session ID:' not in l:print(f'{time.monotonic():.3f}',prefix,l.split('pfid:')[0].rstrip(),flush=True)
  if needle in l:e.set()
threading.Thread(target=read,args=(server,ready,'Server started.','SERVER'),daemon=True).start()
def cmd(x,t=.7):print('COMMAND',x,flush=True);server.stdin.write(x+'\n');server.stdin.flush();time.sleep(t)
def throw():print('BOT COMMAND drop',flush=True);bot.stdin.write('hotbar\n');bot.stdin.flush();time.sleep(1)
try:
 if not ready.wait(50):raise RuntimeError('server unavailable')
 bot=subprocess.Popen(['node',str(here/'bot_drop_lightning.js')],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1,errors='replace');threading.Thread(target=read,args=(bot,spawn,'BOT SPAWN','BOT'),daemon=True).start()
 if not spawn.wait(50):raise RuntimeError('bot unavailable')
 cmd('gamerule doMobSpawning false');cmd('gamerule dofiretick false');cmd('weather clear 1000');cmd('gamemode creative ArenaDropLight');cmd('tp ArenaDropLight 50 100 50',3);cmd('fill 45 99 45 65 99 65 stone');cmd('fill 45 100 45 65 105 65 air');cmd('kill @e[type=item]')
 for test,item in [('tagged_1','effect:lightning_sword'),('untagged_1','effect:lightning_sword'),('tagged_2','effect:lightning_sword'),('tagged_3','effect:lightning_sword'),('untagged_2','effect:lightning_sword')]:
  print('MARK START '+test,flush=True);cmd('fill 45 100 45 65 105 65 air',.4);cmd('kill @e[type=item]',.4);cmd('tp ArenaDropLight 50 100 50',2);cmd('replaceitem entity ArenaDropLight slot.weapon.mainhand 0 '+item+' 1',1.5);throw();cmd('tp ArenaDropLight 48 105 48',.8);cmd('testfor @e[type=item]',.4);cmd('testfor @e[type=item,tag=lightning_sword]',.4)
  if test.startswith('tagged'):cmd('tag @e[type=item] add lightning_sword',.4)
  cmd('execute as @e[type=item] at @s run setblock ~ ~ ~ fire',.4);cmd('execute as @e[type=item] at @s run testforblock ~ ~ ~ fire',.4);cmd('testfor @e[type=item]',1);cmd('testfor @e[type=item]',0.5);print('MARK END '+test,flush=True)
finally:
 if bot and bot.poll() is None:bot.terminate();bot.wait(5)
 if server.poll() is None:server.stdin.write('stop\n');server.stdin.flush();server.wait(20)
 print('DONE',flush=True)
