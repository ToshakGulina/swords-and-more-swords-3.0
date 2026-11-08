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
bot=subprocess.Popen(['node','/home/user/swords-analysis/bot-runtime/bot_ice.js'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)
def botout():
 for line in bot.stdout:
  print(line,end='',flush=True)
  if 'BOT SPAWN' in line:spawn.set()
  if 'BOT ENTITY' in line and 'minecraft:pig' in line:pig.set()
threading.Thread(target=botout,daemon=True).start()
def cmd(c,delay=1):
 print('COMMAND',c,flush=True);p.stdin.write(c+'\n');p.stdin.flush();time.sleep(delay)
if spawn.wait(45):
 cmd('tp ArenaIce 30 100 30',8)
 cmd('fill 26 99 26 39 99 34 stone')
 cmd('fill 26 100 26 39 105 34 air')
 cmd('gamemode survival ArenaIce')
 cmd('clear ArenaIce')
 cmd('kill @e[type=pig]')
 cmd('summon pig 33 100 30',1)
 cmd('tag @e[type=pig,x=33,y=100,z=30,r=5,c=1] add probe')
 cmd('effect @e[type=pig,tag=probe] slowness 90 255 true')
 cmd('effect @e[type=pig,tag=probe] resistance 90 255 true')
 cmd('tp @e[type=pig,tag=probe] 33.5 100 30.5')
 cmd('setblock 34 101 30 stone')
 cmd('testforblock 34 101 30 stone')
 cmd('replaceitem entity ArenaIce slot.weapon.mainhand 0 effect:ice_sword 1',4)
 cmd('testfor @a[name=ArenaIce,hasitem={item=effect:ice_sword,location=slot.weapon.mainhand}]')
 cmd('scriptevent arena:observe_ice start',0.3)
 print('HARNESS ICE USE',flush=True);bot.stdin.write('use\n');bot.stdin.flush();time.sleep(0.4)
 cmd('testforblock 33 100 30 effect99:fake_ice')
 cmd('testforblock 34 101 30 stone',12)
 cmd('testforblock 33 100 30 air')
 cmd('testfor @e[type=pig,tag=probe]')

else:print('NO SPAWN',flush=True)
bot.terminate();bot.wait(5);p.stdin.write('stop\n');p.stdin.flush();rc=p.wait(20)
print('HARNESS RESULT',spawn.is_set(),rc,flush=True)
