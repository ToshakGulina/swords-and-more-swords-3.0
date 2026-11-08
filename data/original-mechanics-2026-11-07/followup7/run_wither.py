"""Wither Skeleton Sword: attempt player-targeted effect via original projectile."""
import os,subprocess,threading,time
from pathlib import Path
here=Path(__file__).resolve().parent
s=subprocess.Popen(['./bedrock_server'],cwd='/tmp/swords-run/server',env={**os.environ,'LD_LIBRARY_PATH':'.'},stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1,errors='replace'); ready=threading.Event();bots=[]
def out(p,event,needle,prefix):
 for line in p.stdout:
  if 'Session ID:' not in line: print(f'{time.monotonic():.3f}',prefix,line.split('pfid:')[0].rstrip(),flush=True)
  if needle in line:event.set()
threading.Thread(target=out,args=(s,ready,'Server started.','SERVER'),daemon=True).start()
def cmd(c,t=0.8):print('COMMAND',c,flush=True);s.stdin.write(c+'\n');s.stdin.flush();time.sleep(t)
try:
 if not ready.wait(50):raise RuntimeError('server startup failed')
 events=[]
 for n in ('ArenaWAttacker','ArenaWTarget'):
  e=threading.Event();b=subprocess.Popen(['node',str(here/'bot_wither.js')],env={**os.environ,'BOT_NAME':n},stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1,errors='replace');bots.append(b);events.append(e);threading.Thread(target=out,args=(b,e,'BOT SPAWN',n),daemon=True).start()
 if not all(e.wait(55) for e in events):raise RuntimeError('bot did not spawn')
 for n in ('ArenaWAttacker','ArenaWTarget'):cmd('gamemode creative '+n);cmd('clear '+n);cmd('effect '+n+' clear')
 cmd('difficulty '+os.environ.get('PROBE_DIFFICULTY','easy'));cmd('gamerule doMobSpawning false');cmd('weather clear 200');cmd('tp ArenaWAttacker 50 100 50 0 0',4);cmd('fill 45 99 45 55 99 55 stone');cmd('fill 45 100 45 55 105 55 air');cmd('tp ArenaWTarget 50 100 51 0 0',3);cmd('kill @e[type=pig]');cmd('summon pig 50 100 53',2);cmd('replaceitem entity ArenaWAttacker slot.weapon.mainhand 0 effect:wither_skeleton_sword 1',5)
 print('MARK ATTACK',flush=True);bots[0].stdin.write('attack\n');bots[0].stdin.flush();time.sleep(14)
finally:
 for b in bots:
  if b.poll() is None:b.terminate();b.wait(5)
 if s.poll() is None:s.stdin.write('stop\n');s.stdin.flush();s.wait(20)
 print('DONE',flush=True)
