const bedrock = require('/home/user/swords-analysis/bot/node_modules/bedrock-protocol')
const readline=require('readline')
const client=bedrock.createClient({host:'127.0.0.1',port:19132,version:'1.20.50',username:'ArenaSelect',offline:true,skipPing:true,raknetBackend:'jsp-raknet',useRaknetWorkers:false})
let slots=[]
const out=x=>JSON.stringify(x,(_,v)=>typeof v==='bigint'?String(v):v)
client.on('error',e=>console.log('BOT ERROR',e?.stack||String(e)))
client.on('start_game',p=>console.log('BOT CUSTOM ITEMS',out(p.itemstates.filter(i=>['effect:fire_sword','effect:lapis_sword'].includes(i.name)))))
client.on('spawn',()=>console.log('BOT SPAWN'))
client.on('inventory_content',p=>{if(p.window_id==='inventory'){slots=p.input; console.log('BOT HOTBAR',out(slots.slice(0,2)))}})
client.on('inventory_slot',p=>{if(p.window_id==='inventory'){slots[p.slot]=p.item;console.log('BOT SLOT',p.slot,out(p.item))}})
readline.createInterface({input:process.stdin}).on('line',cmd=>{
 const i=Number(cmd);console.log('BOT SELECT',i,out(slots[i]));if(!Number.isInteger(i)||i<0||i>8||!slots[i])return
 try{client.queue('mob_equipment',{runtime_entity_id:client.entityId,item:slots[i],slot:i,selected_slot:i,window_id:'inventory'});console.log('BOT SELECT SENT')}catch(e){console.log('BOT ERROR SEND',e.stack)}
})
setTimeout(()=>client.close(),80000)
