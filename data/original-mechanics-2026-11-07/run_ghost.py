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
bot=subprocess.Popen(['node','/home/user/swords-analysis/bot-runtime/bot_ghost.js'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)
def botout():
 for line in bot.stdout:
  print(line,end='',flush=True)
  if 'BOT SPAWN' in line:spawn.set()
  if 'BOT ENTITY' in line and 'minecraft:pig' in line:pig.set()
threading.Thread(target=botout,daemon=True).start()
def cmd(c,delay=1):
 print('COMMAND',c,flush=True);p.stdin.write(c+'\n');p.stdin.flush();time.sleep(delay)
if spawn.wait(45):
 cmd('tp ArenaGhost 30 100 30',8)
 cmd('fill 27 99 27 35 99 33 stone')
 cmd('fill 27 100 27 35 104 33 air')
 cmd('gamemode survival ArenaGhost')
 cmd('clear ArenaGhost')
 cmd('kill @e[type=pig]')
 cmd('summon pig 32 100 30',2)
 cmd('tag @e[type=pig,x=32,y=100,z=30,r=3,c=1] add probe')
 cmd('effect @e[type=pig,tag=probe] slowness 90 255 true')
 cmd('damage @e[type=pig,tag=probe] 4',3)
 cmd('replaceitem entity ArenaGhost slot.weapon.mainhand 0 effect:ghost_sword 1',5)
 cmd('testfor @a[name=ArenaGhost,hasitem={item=effect:ghost_sword,location=slot.weapon.mainhand}]')
 cmd('testfor @e[type=pig,tag=probe]')
 print('HARNESS GHOST ATTACK',flush=True);bot.stdin.write('attack\n');bot.stdin.flush();time.sleep(4)
 cmd('testfor @e[type=pig,tag=probe]')
 print('HARNESS GHOST ATTACK SECOND',flush=True);bot.stdin.write('attack\n');bot.stdin.flush();time.sleep(4)
 cmd('testfor @e[type=pig,tag=probe]')
 cmd('replaceitem entity ArenaGhost slot.weapon.mainhand 0 air',3)
 print('HARNESS EMPTY HAND CONTROL',flush=True);bot.stdin.write('attack\n');bot.stdin.flush();time.sleep(4)
 cmd('testfor @e[type=pig,tag=probe]')

else:print('NO SPAWN',flush=True)
bot.terminate();bot.wait(5);p.stdin.write('stop\n');p.stdin.flush();rc=p.wait(20)
print('HARNESS RESULT',spawn.is_set(),rc,flush=True)
