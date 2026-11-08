const bedrock = require('/home/user/swords-analysis/bot/node_modules/bedrock-protocol')
const readline=require('readline')
const client = bedrock.createClient({host:'127.0.0.1',port:19132,version:'1.20.50',username:'ArenaBot',offline:true,skipPing:true,raknetBackend:'jsp-raknet',useRaknetWorkers:false})
let last=null
client.on('error', e=>console.log('BOT ERROR', e?.stack||String(e)))
client.on('kick',p=>console.log('BOT KICK',JSON.stringify(p)))
client.on('close',()=>{console.log('BOT CLOSE');process.exit(0)})
client.on('start_game',p=>console.log('BOT START_GAME',JSON.stringify({runtime_id:String(p.runtime_entity_id),position:p.player_position})))
client.on('move_player',p=>{if(String(p.runtime_id)===String(client.entityId)){last=p.position;console.log('BOT TELEPORT',JSON.stringify(last))}})
client.on('spawn',()=>console.log('BOT SPAWN'))
readline.createInterface({input:process.stdin}).on('line',cmd=>{
 if(cmd==='walk') {
  console.log('BOT WALK BEGIN position='+JSON.stringify(last)); client.queue('text',{type:'chat',needs_translation:false,source_name:'ArenaBot',message:'arena_control_test',xuid:'',platform_chat_id:''})
  if (!last) {console.log('BOT NO POSITION');return}
  let origin={...last};let i=0;let baseTick=client.tick||0n
  const t=setInterval(()=>{
   i++
   try {client.queue('player_auth_input',{position:{x:origin.x+i/6,y:origin.y,z:origin.z},pitch:0,yaw:-90,head_yaw:-90,move_vector:{x:0,y:1},analogue_move_vector:{x:0,y:1},input_data:{up:true,handled_teleport:i===1},input_mode:'mouse',play_mode:'normal',interaction_model:'crosshair',tick:baseTick+BigInt(i),delta:{x:1/6,y:0,z:0}})}
   catch(e){console.log('BOT WRITE ERROR '+e.stack);clearInterval(t)}
   if(i===30){clearInterval(t);console.log('BOT WALK SENT')}
  },50)
 }
})
setTimeout(()=>{console.log('BOT DONE');client.close()},60000)
