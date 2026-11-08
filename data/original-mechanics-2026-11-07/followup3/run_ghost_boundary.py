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
bot=subprocess.Popen(['node','/home/user/swords-analysis/bot-runtime/bot_range2.js'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)
def botout():
 for line in bot.stdout:
  print(line,end='',flush=True)
  if 'BOT SPAWN' in line:spawn.set()
  if 'BOT ENTITY' in line and 'minecraft:pig' in line:pig.set()
threading.Thread(target=botout,daemon=True).start()
def cmd(c,delay=1):
 print('COMMAND',c,flush=True);p.stdin.write(c+'\n');p.stdin.flush();time.sleep(delay)
if spawn.wait(45):
 cmd('gamemode creative ArenaRange')
 cmd('tp ArenaRange 200 100 200 0 0',8)
 cmd('tickingarea remove GhostLong')
 cmd('tickingarea add 192 90 192 207 110 470 GhostBoundary',15)
 cmd('fill 197 99 197 203 99 205 stone')
 cmd('replaceitem entity ArenaRange slot.weapon.mainhand 0 effect:ghost_sword 1',4)
 for z in [450,451]:
  print('HARNESS WALL '+str(z),flush=True)
  cmd('kill @e[type=entity:ghost_projectile]')
  cmd('tp ArenaRange 200 100 200 0 0',3)
  cmd('fill 197 100 201 203 108 465 air',3)
  cmd('fill 197 100 %d 203 108 %d stone'%(z,z),2)
  cmd('testforblock 200 101 %d stone'%z)
  if z==451:cmd('testforblock 200 101 450 air')
  print('HARNESS GHOST USE',flush=True);bot.stdin.write('use\n');bot.stdin.flush();time.sleep(55)
  cmd('querytarget @a[name=ArenaRange]',2)
  cmd('querytarget @e[type=entity:ghost_projectile]',2)
  if z==451:
   time.sleep(40)
   print('HARNESS AFTER 95S',flush=True)
   cmd('querytarget @a[name=ArenaRange]',2)
   cmd('querytarget @e[type=entity:ghost_projectile]',2)

else:print('NO SPAWN',flush=True)
bot.terminate();bot.wait(5);p.stdin.write('stop\n');p.stdin.flush();rc=p.wait(20)
print('HARNESS RESULT',spawn.is_set(),rc,flush=True)
