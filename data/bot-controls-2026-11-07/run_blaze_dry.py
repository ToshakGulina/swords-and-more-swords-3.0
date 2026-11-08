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
bot=subprocess.Popen(['node','/home/user/swords-analysis/bot-runtime/bot_blaze_dry.js'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)
def botout():
 for line in bot.stdout:
  print(line,end='',flush=True)
  if 'BOT SPAWN' in line:spawn.set()
  if 'BOT ENTITY' in line and 'minecraft:pig' in line:pig.set()
threading.Thread(target=botout,daemon=True).start()
def cmd(c,delay=1):
 print('COMMAND',c,flush=True);p.stdin.write(c+'\n');p.stdin.flush();time.sleep(delay)
if spawn.wait(45):
 cmd('tp ArenaBlaze 30 100 30',8)
 cmd('fill 27 99 27 33 99 33 stone')
 cmd('fill 27 100 27 33 105 33 air')
 cmd('gamemode survival ArenaBlaze')
 cmd('clear ArenaBlaze')
 cmd('effect ArenaBlaze clear')
 cmd('replaceitem entity ArenaBlaze slot.weapon.mainhand 0 effect:blaze_sword 1',5)
 cmd('testfor @a[name=ArenaBlaze,hasitem={item=effect:blaze_sword,location=slot.weapon.mainhand}]')
 cmd('testfor @a[name=ArenaBlaze,family=blaze_sword]')
 cmd('testfor @a[name=ArenaBlaze,family=blaze_sword_skill]')
 print('HARNESS USE FIRST',flush=True);bot.stdin.write('use\n');bot.stdin.flush();time.sleep(2)
 cmd('testfor @a[name=ArenaBlaze,family=blaze_sword_skill]')
 print('HARNESS USE EARLY',flush=True);bot.stdin.write('use\n');bot.stdin.flush();time.sleep(2)
 cmd('testfor @a[name=ArenaBlaze,family=blaze_sword_skill]',10)
 cmd('testfor @a[name=ArenaBlaze,family=blaze_sword_skill]',10)
 print('HARNESS USE LATE',flush=True);bot.stdin.write('use\n');bot.stdin.flush();time.sleep(3)
 cmd('testfor @a[name=ArenaBlaze,family=blaze_sword_skill]')

else:print('NO SPAWN',flush=True)
bot.terminate();bot.wait(5);p.stdin.write('stop\n');p.stdin.flush();rc=p.wait(20)
print('HARNESS RESULT',spawn.is_set(),rc,flush=True)
