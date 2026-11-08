import os,sys,time,threading,subprocess,json
from pathlib import Path
server=Path('/home/user/swords-analysis/bedrock-run/server')
label=sys.argv[1] if len(sys.argv)>1 else 'baseline'
commands=json.loads(Path(sys.argv[2]).read_text()) if len(sys.argv)>2 else [['list',0.4]]
ready=threading.Event();lines=[]
env={'PATH':'/usr/bin:/bin','HOME':str(server),'LD_LIBRARY_PATH':'.','LANG':'C.UTF-8'}
p=subprocess.Popen(['unshare','-Urn','sh','-c','ip link set lo up && exec ./bedrock_server'],cwd=server,env=env,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,bufsize=1,text=True,errors='replace')
def reader():
 for line in p.stdout:
  print(line,end='',flush=True);lines.append(line)
  if 'Server started' in line:ready.set()
t=threading.Thread(target=reader,daemon=True);t.start()
deadline=time.monotonic()+90
while not ready.is_set() and p.poll() is None and time.monotonic()<deadline:ready.wait(0.5)
if not ready.is_set():
 print('HARNESS: server not ready; process exit',p.poll(),flush=True)
 if p.poll() is None:p.terminate()
 try:p.wait(10)
 except subprocess.TimeoutExpired:p.kill();p.wait()
 sys.exit(1)
print('HARNESS: server ready, send commands',flush=True)
for cmd,delay in commands:
 if p.poll() is not None:print('HARNESS: server exited early',p.returncode,flush=True);sys.exit(1)
 print('HARNESS COMMAND: '+cmd,flush=True);p.stdin.write(cmd+'\n');p.stdin.flush();time.sleep(delay)
time.sleep(1)
print('HARNESS COMMAND: stop',flush=True);p.stdin.write('stop\n');p.stdin.flush()
try:rc=p.wait(timeout=35)
except subprocess.TimeoutExpired:p.terminate();rc=p.wait(timeout=5)
t.join(2);print('HARNESS: exit',rc,flush=True);sys.exit(rc)
