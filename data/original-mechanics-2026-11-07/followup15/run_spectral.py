"""Observe the unchanged 2.8.8 crystal chain; deliberately trigger its weapon explosion event."""
import os, subprocess, threading, time
from pathlib import Path
here=Path(__file__).resolve().parent; log=open(here/'spectral_crystal_assisted.log','w',buffering=1)
def out(s):print(s,flush=True);print(s,file=log,flush=True)
server=subprocess.Popen(['./bedrock_server'],cwd='/tmp/swords-run/server',env={**os.environ,'LD_LIBRARY_PATH':'.'},stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1,errors='replace')
ready=threading.Event();spawned=threading.Event();bot=None
def read(p,prefix):
 for line in p.stdout:
  if 'Session ID:' not in line and (prefix=='SERVER' or any(x in line for x in ('BOT SPAWN','BOT ERROR'))):out(f'{time.monotonic():.3f} {prefix} {line.split("pfid:")[0].rstrip()}')
  if 'Server started.' in line:ready.set()
  if 'BOT SPAWN' in line:spawned.set()
threading.Thread(target=read,args=(server,'SERVER'),daemon=True).start()
def cmd(text,delay=.5):
 out('COMMAND '+text);server.stdin.write(text+'\n');server.stdin.flush();time.sleep(delay)
try:
 if not ready.wait(70):raise RuntimeError('server did not start')
 bot=subprocess.Popen(['node',str(here.parent/'followup9'/'bot_wolf.js')],env={**os.environ,'BOT_NAME':'ArenaSpectralProbe'},stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1,errors='replace');threading.Thread(target=read,args=(bot,'BOT'),daemon=True).start()
 if not spawned.wait(60):raise RuntimeError('bot did not spawn')
 cmd('gamerule doMobSpawning false');cmd('gamerule mobgriefing false');cmd('gamemode creative ArenaSpectralProbe');cmd('tp ArenaSpectralProbe 50 110 50',3)
 cmd('fill 40 99 40 60 99 60 stone');cmd('fill 40 100 40 60 110 60 air');cmd('tp ArenaSpectralProbe 50 100 50',2)
 cmd('clear ArenaSpectralProbe');cmd('execute as ArenaSpectralProbe at @s run kill @e[type=ender_crystal,r=32]');cmd('scriptevent arena:spectral_probe start');cmd('replaceitem entity ArenaSpectralProbe slot.weapon.mainhand 0 effect:spectral_sword 1',5)
 cmd('testfor @a[name=ArenaSpectralProbe,family=spectral_sword]',1);cmd('scriptevent arena:spectral_probe before_explode',1)
 cmd('execute as ArenaSpectralProbe at @s run event entity @s spectral_sword_skills',3);cmd('scriptevent arena:spectral_probe direct_skill',1)
 cmd('execute as ArenaSpectralProbe at @s run summon ender_crystal ~ ~1.8 ~ 0 0 minecraft:detect_player',4);cmd('scriptevent arena:spectral_probe assisted_summon',1)
 cmd('execute as ArenaSpectralProbe at @s run event entity @e[type=ender_crystal,c=1,r=5] minecraft:crystal_explode',1)
 cmd('scriptevent arena:spectral_probe after_explode',10)
 cmd('replaceitem entity ArenaSpectralProbe slot.weapon.mainhand 0 air',3);cmd('replaceitem entity ArenaSpectralProbe slot.weapon.mainhand 0 effect:spectral_sword 1',5);cmd('scriptevent arena:spectral_probe reequipped',1);cmd('execute as ArenaSpectralProbe at @s run event entity @s spectral_sword_skills',3);cmd('scriptevent arena:spectral_probe reequipped_direct',1)
 cmd('replaceitem entity ArenaSpectralProbe slot.weapon.mainhand 0 air',3);cmd('scriptevent arena:spectral_probe to_end',8)
 cmd('execute as ArenaSpectralProbe at @s run fill ~-4 ~-1 ~-4 ~4 ~-1 ~4 bedrock',1)
 cmd('replaceitem entity ArenaSpectralProbe slot.weapon.mainhand 0 effect:spectral_sword 1',5);cmd('testfor @a[name=ArenaSpectralProbe,family=spectral_sword]',1);cmd('execute as ArenaSpectralProbe at @s run event entity @s spectral_sword_skills',3);cmd('scriptevent arena:spectral_probe end_equipped',2);cmd('scriptevent arena:spectral_probe end',1)
finally:
 if bot and bot.poll() is None:bot.terminate();bot.wait(5)
 if server.poll() is None:server.stdin.write('stop\n');server.stdin.flush();server.wait(30)
 out('DONE');log.close()
