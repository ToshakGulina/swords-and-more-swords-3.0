const bedrock = require('/home/user/swords-analysis/bot/node_modules/bedrock-protocol')
const readline = require('readline')
const client = bedrock.createClient({host:'127.0.0.1',port:19132,version:'1.20.50',username:'ArenaWall',offline:true,skipPing:true,raknetBackend:'jsp-raknet',useRaknetWorkers:false})
let pos=null, pig=null, held={network_id:0}
client.on('error', e=>console.log('BOT ERROR',e?.stack||String(e)))
client.on('start_game',p=>console.log('BOT START_GAME',JSON.stringify({runtime_id:String(p.runtime_id),movement:p.movement_authority})))
client.on('spawn',()=>console.log('BOT SPAWN'))
client.on('move_player',p=>{if(String(p.runtime_id)===String(client.entityId)){pos=p.position;console.log('BOT POSITION',JSON.stringify(pos))}})
client.on('add_entity',p=>{console.log('BOT ENTITY',JSON.stringify({type:p.entity_type,runtime:String(p.runtime_id),position:p.position})); if(p.entity_type==='minecraft:pig')pig=p.runtime_id})
client.on('inventory_slot',p=>{if(p.window_id==='inventory' && p.slot===0){held=p.item;console.log('BOT HELD',JSON.stringify(held,(_,v)=>typeof v==='bigint'?String(v):v))}})
client.on('inventory_content',p=>{if(p.window_id==='inventory' && p.input?.length){held=p.input[0]; console.log('BOT HELD CONTENT',JSON.stringify(held,(_,v)=>typeof v==='bigint'?String(v):v))}})
client.on('entity_event',p=>console.log('BOT ENTITY EVENT',JSON.stringify(p,(_,v)=>typeof v==='bigint'?String(v):v)))
client.on('text',p=>console.log('BOT TEXT',JSON.stringify(p)))
readline.createInterface({input:process.stdin}).on('line',cmd=>{
 if(cmd==='use'){
  console.log('BOT USE BEGIN',JSON.stringify({pos,network_id:held.network_id}));
  if(!pos||!held.network_id)return;
  try {client.queue('inventory_transaction',{transaction:{legacy:{legacy_request_id:0},transaction_type:'item_use',actions:[],transaction_data:{action_type:'click_air',block_position:{x:0,y:0,z:0},face:-1,hotbar_slot:0,held_item:held,player_pos:pos,click_pos:{x:0,y:0,z:0},block_runtime_id:0}}});console.log('BOT USE SENT')}catch(e){console.log('BOT USE ERROR',e.stack)}
 }
 if(cmd==='attack'){
   console.log('BOT ATTACK BEGIN',String(pig),JSON.stringify(pos));if(!pig||!pos)return
   let n=0;const t=setInterval(()=>{try{client.queue('inventory_transaction',{transaction:{legacy:{legacy_request_id:0},transaction_type:'item_use_on_entity',actions:[],transaction_data:{entity_runtime_id:pig,action_type:'attack',hotbar_slot:0,held_item:held,player_pos:pos,click_pos:{x:0,y:0,z:0}}}});console.log('BOT ATTACK SENT',++n)}catch(e){console.log('BOT SEND ERROR',e.stack);clearInterval(t)}if(n>=12)clearInterval(t)},600)
 }
})
setTimeout(()=>client.close(),180000)
