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
bot=subprocess.Popen(['node','/home/user/swords-analysis/bot-runtime/bot_spectral.js'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)
def botout():
 for line in bot.stdout:
  print(line,end='',flush=True)
  if 'BOT SPAWN' in line:spawn.set()
  if 'BOT ENTITY' in line and 'minecraft:pig' in line:pig.set()
threading.Thread(target=botout,daemon=True).start()
def cmd(c,delay=1):
 print('COMMAND',c,flush=True);p.stdin.write(c+'\n');p.stdin.flush();time.sleep(delay)
if spawn.wait(45):
 cmd('tp ArenaSpectral 50 100 50',8)
 cmd('fill 45 99 45 58 99 55 stone')
 cmd('fill 45 100 45 58 105 55 air')
 cmd('gamemode survival ArenaSpectral')
 cmd('clear ArenaSpectral')
 cmd('setblock 53 100 50 stone')
 cmd('setblock 54 100 50 stone ["stone_type"="granite"]')
 cmd('setblock 55 100 50 gold_block')
 cmd('testforblock 53 100 50 stone')
 cmd('testforblock 54 100 50 stone ["stone_type"="granite"]')
 cmd('testforblock 55 100 50 gold_block')
 cmd('setblock 52 101 50 effect99:spectral_block',4)
 cmd('testforblock 52 101 50 effect99:spectral_block')
 cmd('testforblock 52 101 50 stone')
 cmd('replaceitem entity ArenaSpectral slot.weapon.mainhand 0 effect:spectral_sword 1',5)
 cmd('testfor @a[name=ArenaSpectral,family=spectral_sword]')
 cmd('testforblock 53 100 50 effect99:spectral_block')
 cmd('testforblock 54 100 50 effect99:spectral_block')
 cmd('testforblock 55 100 50 gold_block')
 cmd('replaceitem entity ArenaSpectral slot.weapon.mainhand 0 air',5)
 cmd('testfor @a[name=ArenaSpectral,family=spectral_sword]')
 cmd('testforblock 53 100 50 stone ["stone_type"="stone"]')
 cmd('testforblock 54 100 50 stone ["stone_type"="granite"]')
 cmd('testforblock 54 100 50 stone ["stone_type"="stone"]')
 cmd('testforblock 55 100 50 gold_block')

else:print('NO SPAWN',flush=True)
bot.terminate();bot.wait(5);p.stdin.write('stop\n');p.stdin.flush();rc=p.wait(20)
print('HARNESS RESULT',spawn.is_set(),rc,flush=True)
