import os,subprocess,threading,time,sys
from pathlib import Path
root=Path('/home/user/swords-analysis/bot-runtime/server')
env={'PATH':'/usr/bin:/bin','HOME':str(root),'LD_LIBRARY_PATH':'.','LANG':'C.UTF-8'}
p=subprocess.Popen(['./bedrock_server'],cwd=root,env=env,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1,errors='replace')
ready=threading.Event();spawn=threading.Event()
def serverout():
 for line in p.stdout:
  if 'Session ID:' not in line: print('SERVER',line.split('pfid:')[0],flush=True)
  if 'Server started.' in line:ready.set()
threading.Thread(target=serverout,daemon=True).start()
if not ready.wait(60):p.terminate();sys.exit(1)
bot=subprocess.Popen(['node','/home/user/swords-analysis/bot-runtime/bot_heartbeat_clientauth.js'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)
def botout():
 for line in bot.stdout:
  print(line,end='',flush=True)
  if 'BOT SPAWN' in line:spawn.set()
threading.Thread(target=botout,daemon=True).start()
def command(cmd,delay=1):
 print('COMMAND',cmd,flush=True);p.stdin.write(cmd+'\n');p.stdin.flush();time.sleep(delay)
if spawn.wait(45):
 command('tp ArenaBot 10 100 10',8)
 command('fill 8 99 8 20 99 12 stone',1)
 command('fill 8 100 8 20 103 12 air',1)
 command('testfor @a[name=ArenaBot,x=15,y=100,z=10,r=1]',1)
 print('HARNESS instruct bot WALK',flush=True);bot.stdin.write('walk\n');bot.stdin.flush();time.sleep(7)
 command('testfor @a[name=ArenaBot,x=15,y=100,z=10,r=2]',1)
 command('testfor @a[name=ArenaBot,x=10,y=100,z=10,r=1]',1)
 command('execute as ArenaBot at @s run tp @s ~ ~ ~',1)
else:print('HARNESS CLIENT DID NOT SPAWN',flush=True)
bot.terminate()
try:bot.wait(5)
except subprocess.TimeoutExpired:bot.kill();bot.wait()
p.stdin.write('stop\n');p.stdin.flush()
try:rc=p.wait(20)
except subprocess.TimeoutExpired:p.kill();p.wait();rc=1
print('HARNESS RESULT player_spawned=',spawn.is_set(),'server_exit=',rc,flush=True)
sys.exit(0 if spawn.is_set() and rc==0 else 1)
