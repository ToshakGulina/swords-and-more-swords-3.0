"""Original Sea Sword, server client-authoritative: air -> water -> air -> no sword."""
import os, subprocess, threading, time
from pathlib import Path
here=Path(__file__).resolve().parent
s=subprocess.Popen(['./bedrock_server'],cwd='/tmp/swords-run/server',env={**os.environ,'LD_LIBRARY_PATH':'.'},stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1,errors='replace')
ready=threading.Event();spawn=threading.Event();bot=None
def out(proc,event,needle,prefix):
 for line in proc.stdout:
  if 'Session ID:' not in line:print(prefix,line.split('pfid:')[0].rstrip(),flush=True)
  if needle in line:event.set()
threading.Thread(target=out,args=(s,ready,'Server started.','SERVER'),daemon=True).start()
try:
 if not ready.wait(50):raise RuntimeError('server failed to start')
 bot=subprocess.Popen(['node',str(here/'bot_sea.js')],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1,errors='replace')
 threading.Thread(target=out,args=(bot,spawn,'BOT SPAWN','BOT'),daemon=True).start()
 if not spawn.wait(55):raise RuntimeError('bot did not spawn')
 def cmd(c,t=0.8):
  print('COMMAND',c,flush=True);s.stdin.write(c+'\n');s.stdin.flush();time.sleep(t)
 cmd('gamemode creative ArenaSea');cmd('tp ArenaSea 50 100 50',3)
 cmd('fill 45 99 45 65 99 55 stone');cmd('fill 45 100 45 65 106 55 air')
 cmd('fill 59 100 48 63 104 52 water');cmd('clear ArenaSea');cmd('effect ArenaSea clear')
 print('MARK AIR',flush=True);cmd('replaceitem entity ArenaSea slot.weapon.mainhand 0 effect:sea_sword 1',5)
 cmd('testfor @a[name=ArenaSea,family=sea_sword]');cmd('testfor @a[name=ArenaSea,hasitem={item=effect:sea_sword,location=slot.weapon.mainhand}]');time.sleep(3)
 print('MARK WATER',flush=True);cmd('tp ArenaSea 61 101 50',2);cmd('execute as ArenaSea at @s if block ~ ~ ~ water run say IN_WATER_BLOCK',1);time.sleep(4)
 print('MARK AIR AGAIN',flush=True);cmd('tp ArenaSea 50 100 50',2);cmd('execute as ArenaSea at @s if block ~ ~ ~ air run say IN_AIR_BLOCK',1);time.sleep(4)
 print('MARK REMOVE',flush=True);cmd('replaceitem entity ArenaSea slot.weapon.mainhand 0 air',4);cmd('testfor @a[name=ArenaSea,family=sea_sword]');time.sleep(2)
finally:
 if bot and bot.poll() is None:bot.terminate();bot.wait(5)
 if s.poll() is None:s.stdin.write('stop\n');s.stdin.flush();s.wait(20)
 print('DONE',flush=True)
