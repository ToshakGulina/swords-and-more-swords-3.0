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
b=subprocess.Popen(['node','/home/user/swords-analysis/bot-runtime/bot_drop.js'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)
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
 cmd('fill 8 99 8 15 99 15 stone');cmd('gamemode survival ArenaDrop');cmd('clear ArenaDrop');cmd('kill @e[type=item]')
 for mode in ['stack','hotbar','legacy']:
  cmd('replaceitem entity ArenaDrop slot.weapon.mainhand 0 diamond 1',2)
  cmd('testfor @a[name=ArenaDrop,hasitem={item=diamond,location=slot.weapon.mainhand}]')
  bot(mode)
  cmd('testfor @a[name=ArenaDrop,hasitem={item=diamond,location=slot.weapon.mainhand}]')
  cmd('testfor @e[type=item,x=10,y=100,z=10,r=10]')
  cmd('kill @e[type=item]')
else:print('HARNESS NO SPAWN',flush=True)
b.terminate();b.wait(5);p.stdin.write('stop\n');p.stdin.flush();rc=p.wait(20);print('HARNESS RESULT',spawn.is_set(),rc,flush=True)
