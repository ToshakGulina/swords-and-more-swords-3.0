import subprocess,threading,time,sys
from pathlib import Path
root=Path('/home/user/swords-analysis/bot-runtime/server');env={'PATH':'/usr/bin:/bin','HOME':str(root),'LD_LIBRARY_PATH':'.','LANG':'C.UTF-8'}
p=subprocess.Popen(['./bedrock_server'],cwd=root,env=env,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1,errors='replace')
ready=threading.Event();spawn=threading.Event()
def serverout():
 for line in p.stdout:
  if 'Session ID:' not in line: print('SERVER',line.split('pfid:')[0],end='',flush=True)
  if 'Server started.' in line:ready.set()
threading.Thread(target=serverout,daemon=True).start()
if not ready.wait(60):p.terminate();sys.exit(1)
b=subprocess.Popen(['node','/home/user/swords-analysis/bot-runtime/bot_drop_addon.js'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)
def botout():
 for line in b.stdout:
  print(line,end='',flush=True)
  if 'BOT SPAWN' in line:spawn.set()
threading.Thread(target=botout,daemon=True).start()
def cmd(c,delay=1):
 print('COMMAND',c,flush=True);p.stdin.write(c+'\n');p.stdin.flush();time.sleep(delay)
def bot(c):print('HARNESS',c,flush=True);b.stdin.write(c+'\n');b.stdin.flush();time.sleep(1)
if spawn.wait(45):
 cmd('tp ArenaDrop 10 100 10',8)
 cmd('fill 7 99 7 16 99 17 stone')
 cmd('fill 7 100 7 16 103 17 air')
 cmd('gamemode survival ArenaDrop');cmd('clear ArenaDrop');cmd('kill @e[type=item]')
 cmd('fill 8 100 8 15 102 16 water')
 cmd('replaceitem entity ArenaDrop slot.weapon.mainhand 0 effect:fire_sword 1',2)
 cmd('testfor @a[name=ArenaDrop,hasitem={item=effect:fire_sword,location=slot.weapon.mainhand}]')
 bot('hotbar')
 cmd('testfor @a[name=ArenaDrop,hasitem={item=effect:fire_sword,location=slot.weapon.mainhand}]')
 cmd('testfor @e[type=item,x=10,y=101,z=11,r=10]')
 cmd('testfor @e[type=item,tag=fire_sword,x=10,y=101,z=11,r=10]',8)
 cmd('testfor @e[type=item,x=10,y=101,z=11,r=10]')
 cmd('testfor @e[type=item,tag=fire_sword,x=10,y=101,z=11,r=10]',4)
 cmd('testfor @e[type=item,x=10,y=101,z=11,r=10]')

else:print('HARNESS NO SPAWN',flush=True)
b.terminate();b.wait(5);p.stdin.write('stop\n');p.stdin.flush();rc=p.wait(20);print('HARNESS RESULT',spawn.is_set(),rc,flush=True)
