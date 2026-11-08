"""Observe original Slime King and two single-jump-setting controls on BDS 1.20.50."""
import os
import subprocess
import threading
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
SERVER = Path('/tmp/swords-run/server')
BOT = HERE.parent / 'followup9' / 'bot_wolf.js'
ready, spawned, finished = threading.Event(), threading.Event(), threading.Event()
server = subprocess.Popen(['./bedrock_server'], cwd=SERVER, env={**os.environ, 'LD_LIBRARY_PATH':'.'},
                          stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                          text=True, bufsize=1, errors='replace')
bot = None

def reader(proc, prefix):
    for line in proc.stdout:
        if 'Session ID:' not in line:
            if prefix == 'SERVER' or any(x in line for x in ('BOT SPAWN','BOT ERROR','BOT START','BOT POSITION')):
                print(f'{time.monotonic():.3f} {prefix} {line.split("pfid:")[0].rstrip()}', flush=True)
        if 'Server started.' in line: ready.set()
        if 'BOT SPAWN' in line: spawned.set()
        if any(x in line for x in ('JUMP_FINISHED', 'JUMP_ERR', 'JUMP_PREP_ERR')): finished.set()

threading.Thread(target=reader, args=(server, 'SERVER'), daemon=True).start()

def command(text, delay=0.6):
    print('COMMAND', text, flush=True)
    server.stdin.write(text + '\n')
    server.stdin.flush()
    time.sleep(delay)

try:
    if not ready.wait(60): raise RuntimeError('server startup failed')
    bot = subprocess.Popen(['node', str(BOT)], env={**os.environ,'BOT_NAME':'ArenaJump'},
                           stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                           text=True, bufsize=1, errors='replace')
    threading.Thread(target=reader, args=(bot, 'BOT'), daemon=True).start()
    if not spawned.wait(60): raise RuntimeError('bot spawn failed')
    command('gamemode creative ArenaJump')
    command('gamerule doMobSpawning false')
    command('gamerule doDaylightCycle false')
    command('time set 18000')
    command('tp ArenaJump 60 112 60', 3)
    command('fill 44 99 44 76 99 56 stone')
    command('fill 44 100 44 76 106 56 air')
    # Matching identical 9x9 enclosures prevent control mobs from leaving loaded chunks.
    for x in (50, 60, 70):
        command(f'fill {x-4} 100 46 {x+4} 104 46 stone', .3)
        command(f'fill {x-4} 100 54 {x+4} 104 54 stone', .3)
        command(f'fill {x-4} 100 46 {x-4} 104 54 stone', .3)
        command(f'fill {x+4} 100 46 {x+4} 104 54 stone', .3)
    command('scriptevent arena:slime_jump start', .3)
    if not finished.wait(100): print('JUMP_TIMEOUT', flush=True)
finally:
    if bot and bot.poll() is None:
        bot.terminate()
        bot.wait(5)
    if server.poll() is None:
        server.stdin.write('stop\n')
        server.stdin.flush()
        server.wait(30)
    print('DONE', flush=True)
