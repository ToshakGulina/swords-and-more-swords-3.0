import subprocess,threading,time,sys
from pathlib import Path
root=Path('/home/user/swords-analysis/bot-runtime/server')
env={'PATH':'/usr/bin:/bin','HOME':str(root),'LD_LIBRARY_PATH':'.','LANG':'C.UTF-8'}
p=subprocess.Popen(['./bedrock_server'],cwd=root,env=env,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1,errors='replace')
ready=threading.Event();spawn=threading.Event();pig=threading.Event()
def serverout():
 for line in p.stdout:
  if 'Session ID:' not in line:print('SERVER',line.split('pfid:')[0],end='',flush=True)
  if 'Server started.' in line:ready.set()
threading.Thread(target=serverout,daemon=True).start()
if not ready.wait(60):p.terminate();sys.exit(1)
bot=subprocess.Popen(['node','/home/user/swords-analysis/bot-runtime/bot_collision.js'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)
def botout():
 for line in bot.stdout:
  print(line,end='',flush=True)
  if 'BOT SPAWN' in line:spawn.set()
  if 'BOT ENTITY' in line and 'minecraft:pig' in line:pig.set()
threading.Thread(target=botout,daemon=True).start()
def cmd(c,delay=1):
 print('COMMAND',c,flush=True);p.stdin.write(c+'\n');p.stdin.flush();time.sleep(delay)
if spawn.wait(45):
 cmd('gamemode creative ArenaCollision')
 cmd('tp ArenaCollision 50 100 50',8)
 cmd('fill 47 99 47 53 99 53 stone')
 cmd('fill 59 95 47 65 95 53 stone')
 cmd('fill 59 96 47 65 105 53 air')
 cmd('summon pig 62 103 50')
 cmd('tag @e[type=pig,x=62,y=103,z=50,r=10,c=1] add probe')
 cmd('effect @e[type=pig,tag=probe] slowness 120 255 true')
 cmd('effect @e[type=pig,tag=probe] resistance 120 255 true')
 for block in ['stone','air','effect99:spectral_block']:
  print('HARNESS COLLISION',block,flush=True)
  cmd(f'fill 60 99 48 64 99 52 {block}')
  cmd(f'testforblock 62 99 50 {block}')
  cmd('tp @e[type=pig,tag=probe] 62.5 103 50.5',5)
  cmd('querytarget @e[type=pig,tag=probe]')
  cmd(f'testforblock 62 99 50 {block}')

else:print('NO SPAWN',flush=True)
bot.terminate();bot.wait(5);p.stdin.write('stop\n');p.stdin.flush();rc=p.wait(20)
print('HARNESS RESULT',spawn.is_set(),rc,flush=True)
