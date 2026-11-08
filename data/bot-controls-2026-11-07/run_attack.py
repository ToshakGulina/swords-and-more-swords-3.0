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
bot=subprocess.Popen(['node','/home/user/swords-analysis/bot-runtime/bot_attack.js'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)
def botout():
 for line in bot.stdout:
  print(line,end='',flush=True)
  if 'BOT SPAWN' in line:spawn.set()
  if 'BOT ENTITY' in line and 'minecraft:pig' in line:pig.set()
threading.Thread(target=botout,daemon=True).start()
def cmd(c,delay=1):
 print('COMMAND',c,flush=True);p.stdin.write(c+'\n');p.stdin.flush();time.sleep(delay)
if spawn.wait(45):
 cmd('tp ArenaBot 10 100 10',8)
 cmd('fill 8 99 8 20 99 12 stone')
 cmd('fill 11 100 9 13 102 11 glass')
 cmd('fill 12 100 10 12 101 10 air')
 cmd('gamemode survival ArenaBot')
 cmd('clear ArenaBot')
 cmd('kill @e[type=pig]')
 cmd('summon pig 12 100 10',2)
 cmd('effect @e[type=pig] slowness 30 255 true')
 cmd('fill 11 100 10 11 101 10 air')
 cmd('testfor @e[type=pig,x=12,y=100,z=10,r=5]')
 print('HARNESS instruct ATTACK target_known=',pig.is_set(),flush=True);bot.stdin.write('attack\n');bot.stdin.flush();time.sleep(9)
 cmd('testfor @e[type=pig,x=12,y=100,z=10,r=5]')
else:print('NO SPAWN',flush=True)
bot.terminate();bot.wait(5);p.stdin.write('stop\n');p.stdin.flush();rc=p.wait(20)
print('HARNESS RESULT',spawn.is_set(),rc,flush=True)
