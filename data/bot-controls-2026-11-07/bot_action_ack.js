const bedrock = require('/home/user/swords-analysis/bot/node_modules/bedrock-protocol')
const readline = require('readline')
const client = bedrock.createClient({host:'127.0.0.1',port:19132,version:'1.20.50',username:'ArenaBot',offline:true,skipPing:true,raknetBackend:'jsp-raknet',useRaknetWorkers:false,viewDistance:4})
let position = null, pendingTeleport = 0, walking = 0, tick = 0n, lastLog = 0, ready = false
client.on('error', e => console.log('BOT ERROR',e?.stack||String(e)))
client.on('close',()=>{console.log('BOT CLOSE');process.exit(0)})
client.on('start_game',p=>{position=p.player_position; tick=BigInt(p.current_tick); console.log('BOT START',JSON.stringify({position,movement:p.movement_authority,tick:String(tick)}))})
client.on('respawn',p=>{ console.log('BOT RESPAWN',JSON.stringify(p,(_,v)=>typeof v==='bigint'?String(v):v)); if(p.state===1){client.queue('respawn',{position:p.position,state:2,runtime_entity_id:p.runtime_entity_id}); console.log('BOT RESPAWN READY')} })
client.on('spawn',()=>{ console.log('BOT SPAWN'); setInterval(()=>{
 if(!position || position.y>1000 || !ready)return
 tick++
 const dx=walking>0?0.08:0
 if(walking>0)walking--
 position={...position,x:position.x+dx}
 try {client.queue('player_auth_input',{position,pitch:0,yaw:-90,head_yaw:-90,move_vector:{x:0,y:dx?1:0},analogue_move_vector:{x:0,y:dx?1:0},input_data:{up:!!dx,handled_teleport:pendingTeleport>0},input_mode:'mouse',play_mode:'normal',interaction_model:'crosshair',tick,delta:{x:dx,y:0,z:0}});pendingTeleport=Math.max(0,pendingTeleport-1)} catch(e){console.log('BOT SEND ERROR',e.stack)}
 if(walking>0 && Date.now()-lastLog>1000){lastLog=Date.now();console.log('BOT HEARTBEAT',JSON.stringify({position,tick:String(tick),remaining:walking,serverTick:String(client.tick)}))}
 },50)})
client.on('move_player',p=>{if(String(p.runtime_id)===String(client.entityId)){position=p.position; pendingTeleport=10; ready=false; client.queue('player_action',{runtime_entity_id:client.entityId,action:'handled_teleport',position:{x:Math.floor(position.x),y:Math.floor(position.y-1.62),z:Math.floor(position.z)},result_position:{x:0,y:0,z:0},face:0}); console.log('BOT TELEPORT ACTION'); console.log('BOT SERVER MOVE',JSON.stringify({position,mode:p.mode,tick:String(p.tick)}))}})
client.on('correct_player_move_prediction',p=>{position=p.position; console.log('BOT CORRECTION',JSON.stringify(p,(_,v)=>typeof v==='bigint'?String(v):v))})
client.on('tick_sync',p=>{ if(BigInt(p.response_time)>tick) tick=BigInt(p.response_time); ready=true; console.log('BOT SYNC',String(p.request_time),String(p.response_time)) })
client.on('text',p=>console.log('BOT RECEIVED TEXT',JSON.stringify(p)))
readline.createInterface({input:process.stdin}).on('line',cmd=>{
 if(cmd==='walk'){console.log('BOT BEGIN WALK',JSON.stringify(position));walking=60; client.queue('text',{type:'chat',needs_translation:false,source_name:'ArenaBot',message:'arena_control_test',xuid:'',platform_chat_id:''})}
})
setTimeout(()=>client.close(),80000)
