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
bot=subprocess.Popen(['node','/home/user/swords-analysis/bot-runtime/bot_wall.js'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)
def botout():
 for line in bot.stdout:
  print(line,end='',flush=True)
  if 'BOT SPAWN' in line:spawn.set()
  if 'BOT ENTITY' in line and 'minecraft:pig' in line:pig.set()
threading.Thread(target=botout,daemon=True).start()
def cmd(c,delay=1):
 print('COMMAND',c,flush=True);p.stdin.write(c+'\n');p.stdin.flush();time.sleep(delay)
if spawn.wait(45):
 cmd('gamemode survival ArenaWall')
 cmd('tp ArenaWall 200 100 200',7)
 cmd('fill 194 99 194 206 99 215 stone')
 cmd('fill 194 100 194 206 106 215 air')
 cmd('clear ArenaWall')
 cmd('replaceitem entity ArenaWall slot.weapon.mainhand 0 effect:ghost_sword 1',4)
 cmd('testfor @a[name=ArenaWall,family=ghost_sword]')
 for z in [202,204,206]:
  print('HARNESS WALL Z',z,flush=True)
  cmd('tp ArenaWall 200 100 200',4)
  cmd('fill 197 100 201 203 105 209 air')
  cmd(f'fill 197 100 {z} 203 105 {z} stone')
  cmd(f'testforblock 200 101 {z} stone')
  cmd('querytarget @a[name=ArenaWall]')
  print('HARNESS GHOST USE',flush=True);bot.stdin.write('use\n');bot.stdin.flush();time.sleep(4)
  cmd('querytarget @a[name=ArenaWall]')
  cmd(f'testforblock 200 101 {z} stone')

else:print('NO SPAWN',flush=True)
bot.terminate();bot.wait(5);p.stdin.write('stop\n');p.stdin.flush();rc=p.wait(20)
print('HARNESS RESULT',spawn.is_set(),rc,flush=True)
