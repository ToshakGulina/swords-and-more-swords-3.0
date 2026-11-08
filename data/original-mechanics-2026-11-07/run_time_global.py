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
bot=subprocess.Popen(['node','/home/user/swords-analysis/bot-runtime/bot_time.js'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)
def botout():
 for line in bot.stdout:
  print(line,end='',flush=True)
  if 'BOT SPAWN' in line:spawn.set()
  if 'BOT ENTITY' in line and 'minecraft:pig' in line:pig.set()
threading.Thread(target=botout,daemon=True).start()
def cmd(c,delay=1):
 print('COMMAND',c,flush=True);p.stdin.write(c+'\n');p.stdin.flush();time.sleep(delay)
if spawn.wait(45):
 cmd('tp ArenaTime 50 100 50',8)
 cmd('fill 47 99 47 53 99 53 stone')
 cmd('fill 47 100 47 53 104 53 air')
 cmd('gamemode survival ArenaTime')
 cmd('clear ArenaTime')
 cmd('gamerule dodaylightcycle false')
 cmd('gamerule randomtickspeed 7')
 cmd('time set 1000')
 cmd('gamerule randomtickspeed')
 cmd('time query daytime',4)
 cmd('time query daytime')
 cmd('replaceitem entity ArenaTime slot.weapon.mainhand 0 effect:time_sword 1',5)
 cmd('testfor @a[name=ArenaTime,hasitem={item=effect:time_sword,location=slot.weapon.mainhand}]')
 cmd('testfor @a[name=ArenaTime,family=time_sword]')
 cmd('gamerule randomtickspeed')
 cmd('time query daytime',4)
 cmd('time query daytime')
 cmd('replaceitem entity ArenaTime slot.weapon.mainhand 0 air',4)
 cmd('testfor @a[name=ArenaTime,family=time_sword]')
 cmd('gamerule randomtickspeed')
 cmd('time query daytime',4)
 cmd('time query daytime')

else:print('NO SPAWN',flush=True)
bot.terminate();bot.wait(5);p.stdin.write('stop\n');p.stdin.flush();rc=p.wait(20)
print('HARNESS RESULT',spawn.is_set(),rc,flush=True)
