const bedrock = require('/home/user/swords-analysis/bot/node_modules/bedrock-protocol')
const readline = require('readline')
const client = bedrock.createClient({host:'127.0.0.1',port:19132,version:'1.20.50',username:'ArenaDrop',offline:true,skipPing:true,raknetBackend:'jsp-raknet',useRaknetWorkers:false})
let held={network_id:0};let seq=-1
const out=x=>JSON.stringify(x,(_,v)=>typeof v==='bigint'?String(v):v)
client.on('error',e=>console.log('BOT ERROR',e?.stack||String(e)))
client.on('start_game',p=>console.log('BOT CUSTOM ITEMS',out(p.itemstates.filter(i=>['effect:fire_sword','effect:glass_sword','effect:obsidian_sword','effect:sponge_sword','effect:wet_sponge_sword'].includes(i.name)))))
client.on('spawn',()=>console.log('BOT SPAWN'))
client.on('inventory_content',p=>{if(p.window_id==='inventory'&&p.input?.length){held=p.input[0];console.log('BOT HELD',out(held))}})
client.on('inventory_slot',p=>{if(p.window_id==='inventory'&&p.slot===0){held=p.item;console.log('BOT HELD',out(held))}})
client.on('add_item_entity',p=>console.log('BOT DROP ENTITY',out({item:p.item,position:p.position,velocity:p.velocity})))
client.on('remove_entity',p=>console.log('BOT REMOVE ENTITY',out(p)))
client.on('item_stack_response',p=>console.log('BOT STACK RESPONSE',out(p)))
readline.createInterface({input:process.stdin}).on('line',cmd=>{
 console.log('BOT COMMAND',cmd,'HELD',out(held)); if(!held.network_id)return
 try {
  if(cmd==='stack' || cmd==='hotbar'){
   client.queue('item_stack_request',{requests:[{request_id:seq,actions:[{type_id:'drop',count:1,source:{slot_type:cmd==='hotbar'?'hotbar':'hotbar_and_inventory',slot:0,stack_id:held.stack_id},randomly:false}],custom_names:[],cause:'chat_public'}]});seq-=2
  } else if(cmd==='legacy') {
   client.queue('inventory_transaction',{transaction:{legacy:{legacy_request_id:0},transaction_type:'normal',actions:[{source_type:'container',inventory_id:'inventory',slot:0,old_item:held,new_item:{network_id:0}},{source_type:'world_interaction',flags:0,slot:0,old_item:{network_id:0},new_item:held}]}})
  }
  console.log('BOT REQUEST SENT')
 }catch(e){console.log('BOT ERROR SEND',e.stack)}
})
setTimeout(()=>client.close(),80000)
