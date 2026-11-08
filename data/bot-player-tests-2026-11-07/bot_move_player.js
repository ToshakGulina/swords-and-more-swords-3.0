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
  console.log('BOT WALK BEGIN position='+JSON.stringify(last))
  if (!last) {console.log('BOT NO POSITION');return}
  let origin={...last};let i=0
  const t=setInterval(()=>{
   i++
   try {client.queue('move_player',{runtime_id:Number(client.entityId),position:{x:origin.x+i/6,y:origin.y,z:origin.z},pitch:0,yaw:90,head_yaw:90,mode:'normal',on_ground:true,ridden_runtime_id:0,tick:BigInt(i)})}
   catch(e){console.log('BOT WRITE ERROR '+e.stack);clearInterval(t)}
   if(i===30){clearInterval(t);console.log('BOT WALK SENT')}
  },50)
 }
})
setTimeout(()=>{console.log('BOT DONE');client.close()},60000)
