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
bot=subprocess.Popen(['node','/home/user/swords-analysis/bot-runtime/bot_spectral_height.js'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)
def botout():
 for line in bot.stdout:
  print(line,end='',flush=True)
  if 'BOT SPAWN' in line:spawn.set()
  if 'BOT ENTITY' in line and 'minecraft:pig' in line:pig.set()
threading.Thread(target=botout,daemon=True).start()
def cmd(c,delay=1):
 print('COMMAND',c,flush=True);p.stdin.write(c+'\n');p.stdin.flush();time.sleep(delay)
if spawn.wait(45):
 cmd('gamemode creative ArenaHeight')
 cmd('clear ArenaHeight')
 for x,y in [(80,-10),(110,7),(140,8),(170,260)]:
  print('HARNESS HEIGHT',y,flush=True)
  cmd(f'tp ArenaHeight {x} {y} 80',6)
  cmd(f'fill {x-2} {y-1} 78 {x+5} {y-1} 82 stone')
  cmd(f'fill {x-2} {y} 78 {x+5} {y+4} 82 air')
  cmd(f'setblock {x+3} {y} 80 stone')
  cmd(f'testforblock {x+3} {y} 80 stone')
  cmd('querytarget @a[name=ArenaHeight]')
  cmd('replaceitem entity ArenaHeight slot.weapon.mainhand 0 effect:spectral_sword 1',4)
  cmd('testfor @a[name=ArenaHeight,family=spectral_sword]')
  cmd(f'testforblock {x+3} {y} 80 effect99:spectral_block')
  cmd(f'testforblock {x+3} {y} 80 stone')
  cmd('replaceitem entity ArenaHeight slot.weapon.mainhand 0 air',3)

else:print('NO SPAWN',flush=True)
bot.terminate();bot.wait(5);p.stdin.write('stop\n');p.stdin.flush();rc=p.wait(20)
print('HARNESS RESULT',spawn.is_set(),rc,flush=True)
