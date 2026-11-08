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
 cmd('tp ArenaGhost 20 106 12',8)
 cmd('gamemode creative ArenaGhost')
 cmd('fill 16 98 16 27 105 25 air')
 cmd('fill 18 99 18 22 101 22 stone')
 cmd('fill 19 99 19 21 99 21 sandstone')
 cmd('fill 19 100 19 21 101 21 air')
 cmd('fill 19 100 19 21 100 21 water')
 cmd('setblock 19 102 19 sandstone')
 cmd('setblock 21 102 19 sandstone')
 cmd('setblock 19 102 21 sandstone')
 cmd('setblock 21 102 21 sandstone')
 cmd('setblock 20 104 20 air')
 cmd('kill @e[type=item]')
 cmd('scriptevent arena:spawn plain',8)
 cmd('testfor @e[type=item,tag=wish_1,x=20,y=100,z=20,r=6]')
 cmd('kill @e[type=item]')
 cmd('scriptevent arena:spawn named',8)
 cmd('testfor @e[type=item,tag=wish_1,x=20,y=100,z=20,r=6]')
 cmd('testfor @e[type=item,name="Quartz Diamond",x=20,y=100,z=20,r=6]')
 cmd('kill @e[type=item]')
 cmd('scriptevent arena:spawn other',8)
 cmd('testfor @e[type=item,tag=wish_1,x=20,y=100,z=20,r=6]')
 cmd('testfor @e[type=item,name="Quartz Diamond",x=20,y=100,z=20,r=6]')

else:print('NO SPAWN',flush=True)
bot.terminate();bot.wait(5);p.stdin.write('stop\n');p.stdin.flush();rc=p.wait(20)
print('HARNESS RESULT',spawn.is_set(),rc,flush=True)
