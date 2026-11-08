const bedrock=require('/home/user/swords-analysis/bot/node_modules/bedrock-protocol');const readline=require('readline');
const c=bedrock.createClient({host:'127.0.0.1',port:19132,version:'1.20.50',username:'ArenaAnvil',offline:true,skipPing:true,raknetBackend:'jsp-raknet',useRaknetWorkers:false});
const out=x=>JSON.stringify(x,(_,v)=>typeof v==='bigint'?String(v):v);let pos=null,slots={},anvil=null,win=null,seq=-1;
c.on('error',e=>console.log('BOT ERROR',e?.stack||String(e)));c.on('spawn',()=>console.log('BOT SPAWN'));
c.on('move_player',p=>{if(String(p.runtime_id)===String(c.entityId)){pos=p.position;console.log('BOT POS',out(pos));}});
c.on('inventory_slot',p=>{if(p.window_id==='inventory')slots[p.slot]=p.item;console.log('BOT SLOT',out(p));});
c.on('inventory_content',p=>{if(p.window_id==='inventory'){p.input.forEach((v,i)=>slots[i]=v)}console.log('BOT CONTENT',out({window_id:p.window_id,input:p.input.filter(i=>i.network_id)}));});
c.on('update_block',p=>{if(p.position.x===300&&p.position.y===100&&p.position.z===302){anvil=p.block_runtime_id;console.log('BOT BLOCK',out(p));}});
c.on('container_open',p=>{win=p;console.log('BOT OPEN',out(p));});c.on('container_close',p=>console.log('BOT CLOSE',out(p)));c.on('container_set_data',p=>console.log('BOT DATA',out(p)));c.on('item_stack_response',p=>console.log('BOT RESPONSE',out(p)));
function req(action){c.queue('item_stack_request',{requests:[{request_id:seq,actions:[action],custom_names:[],cause:'chat_public'}]});console.log('BOT REQUEST',seq,out(action));seq-=2}
readline.createInterface({input:process.stdin}).on('line',cmd=>{try{
 if(cmd==='open'&&!win){console.log('BOT OPEN TRY',out({pos,anvil,held:slots[0]}));c.queue('inventory_transaction',{transaction:{legacy:{legacy_request_id:0},transaction_type:'item_use',actions:[],transaction_data:{action_type:'click_block',block_position:{x:300,y:100,z:302},face:1,hotbar_slot:0,held_item:slots[0]||{network_id:0},player_pos:pos,click_pos:{x:.5,y:1,z:.5},block_runtime_id:anvil}}});}
 if(cmd==='input'||cmd==='material') {let source=cmd==='input'?0:1;req({type_id:'place',count:1,source:{slot_type:'hotbar',slot:source,stack_id:slots[source]?.stack_id||0},destination:{slot_type:cmd==='input'?'anvil_input':'anvil_material',slot:cmd==='input'?1:2,stack_id:0}})}
 if(cmd==='close'&&win){c.queue('container_close',{window_id:win.window_id,server:false});win=null}
 }catch(e){console.log('BOT SEND ERROR',e.stack)}});setTimeout(()=>c.close(),220000);
