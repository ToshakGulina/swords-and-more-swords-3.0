import os,subprocess,threading,time,sys
from pathlib import Path
root=Path('/home/user/swords-analysis/bot-runtime/server')
env={'PATH':'/usr/bin:/bin','HOME':str(root),'LD_LIBRARY_PATH':'.','LANG':'C.UTF-8'}
p=subprocess.Popen(['./bedrock_server'],cwd=root,env=env,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1,errors='replace')
ready=threading.Event();spawn=threading.Event()
def serverout():
 for line in p.stdout:
  if 'Session ID:' not in line and 'pfid:' not in line:print('SERVER',line,end='',flush=True)
  if 'Server started.' in line:ready.set()
threading.Thread(target=serverout,daemon=True).start()
if not ready.wait(60):p.terminate();sys.exit(1)
bot=subprocess.Popen(['node','/home/user/swords-analysis/bot-runtime/bot_move.js'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)
def botout():
 for line in bot.stdout:
  print(line,end='',flush=True)
  if 'BOT SPAWN' in line:spawn.set()
threading.Thread(target=botout,daemon=True).start()
def command(cmd,delay=1):
 print('COMMAND',cmd,flush=True);p.stdin.write(cmd+'\n');p.stdin.flush();time.sleep(delay)
if spawn.wait(45):
 command('weather clear 6000',.5)
 command('tp ArenaBot 37 260 17',3)
 command('fill 33 259 13 43 259 21 stone',.5)
 command('fill 33 260 13 43 319 21 air',.5)
 command('kill @e[type=item]',.5)
 command('structure load fire_sword 35 260 17',1)
 command('testfor @e[type=item,tag=fire_sword]',3)
 command('testfor @e[type=item,tag=fire_sword]',.5)
 command('weather rain 60',25)
 command('testfor @e[type=item]',.5)
 command('testfor @e[type=item,tag=fire_sword]',.5)
 command('weather clear 6000',.5)
else:print('HARNESS CLIENT DID NOT SPAWN',flush=True)
bot.terminate()
try:bot.wait(5)
except subprocess.TimeoutExpired:bot.kill();bot.wait()
p.stdin.write('stop\n');p.stdin.flush()
try:rc=p.wait(20)
except subprocess.TimeoutExpired:p.kill();p.wait();rc=1
print('HARNESS RESULT player_spawned=',spawn.is_set(),'server_exit=',rc,flush=True)
sys.exit(0 if spawn.is_set() and rc==0 else 1)
