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
bot=subprocess.Popen(['node','/home/user/swords-analysis/bot-runtime/bot_clock.js'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)
def botout():
 for line in bot.stdout:
  print(line,end='',flush=True)
  if 'BOT SPAWN' in line:spawn.set()
  if 'BOT ENTITY' in line and 'minecraft:pig' in line:pig.set()
threading.Thread(target=botout,daemon=True).start()
def cmd(c,delay=1):
 print('COMMAND',c,flush=True);p.stdin.write(c+'\n');p.stdin.flush();time.sleep(delay)
if spawn.wait(45):
 cmd('tp ArenaClock 60 100 60',8)
 cmd('fill 57 99 57 63 99 63 stone')
 cmd('fill 57 100 57 63 104 63 air')
 cmd('gamemode survival ArenaClock')
 cmd('clear ArenaClock')
 cmd('gamerule dodaylightcycle false')
 cmd('gamerule randomtickspeed 7')
 cmd('time set 1000')
 cmd('replaceitem entity ArenaClock slot.weapon.mainhand 0 effect:clock_sword 1',5)
 cmd('testfor @a[name=ArenaClock,hasitem={item=effect:clock_sword,location=slot.weapon.mainhand}]')
 cmd('testfor @a[name=ArenaClock,family=clock_sword]')
 cmd('testfor @a[name=ArenaClock,family=clock_sword_skill]')
 cmd('gamerule randomtickspeed')
 cmd('time query daytime')
 print('HARNESS USE CLOCK',flush=True);bot.stdin.write('use\n');bot.stdin.flush();time.sleep(1)
 cmd('testfor @a[name=ArenaClock,family=clock_sword_skill]',0.5)
 cmd('gamerule randomtickspeed',0.5)
 cmd('time query daytime',7)
 cmd('testfor @a[name=ArenaClock,family=clock_sword_skill]')
 cmd('testfor @a[name=ArenaClock,hasitem={item=effect:clock_sword,location=slot.weapon.mainhand}]')
 cmd('gamerule randomtickspeed')
 cmd('time query daytime',3)
 cmd('time query daytime')
 cmd('replaceitem entity ArenaClock slot.weapon.mainhand 0 air',3)
 cmd('gamerule randomtickspeed')

else:print('NO SPAWN',flush=True)
bot.terminate();bot.wait(5);p.stdin.write('stop\n');p.stdin.flush();rc=p.wait(20)
print('HARNESS RESULT',spawn.is_set(),rc,flush=True)
