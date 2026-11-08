import {world, system, ItemStack} from '@minecraft/server';
console.warn('ARENA_OBSERVER_READY');
system.runInterval(()=>{
 try {
  const d=world.getDimension('overworld');
  for(const e of d.getEntities({type:'minecraft:pig',tags:['probe']})){
   const h=e.getComponent('minecraft:health');
   console.warn('ARENA_HEALTH '+JSON.stringify({health:h.currentValue,max:h.effectiveMax}));
  }
  for(const e of d.getEntities({type:'minecraft:item',location:{x:20,y:100,z:20},maxDistance:10})){
   const i=e.getComponent('minecraft:item')?.itemStack;
   const p=e.location;
   console.warn('ARENA_ITEM '+JSON.stringify({type:i?.typeId,amount:i?.amount,stackName:i?.nameTag,actorName:e.nameTag,tags:e.getTags(),position:{x:p.x,y:p.y,z:p.z}}));
  }
 } catch(e){console.warn('ARENA_OBSERVER_ERROR '+String(e));}
},20);

system.afterEvents.scriptEventReceive.subscribe(ev=>{
 if(ev.id!=='arena:spawn') return;
 try{
  const kinds={plain:'effect:quartz_diamond',named:'effect:quartz_diamond',other:'minecraft:diamond'};
  const id=kinds[ev.message]; if(!id) throw new Error('unknown case');
  const item=new ItemStack(id,1);if(ev.message!=='plain')item.nameTag='Quartz Diamond';
  const entity=world.getDimension('overworld').spawnItem(item,{x:20.5,y:100,z:20.5});
  console.warn('ARENA_SPAWN '+JSON.stringify({kind:ev.message,type:id,name:item.nameTag,actorName:entity.nameTag}));
 }catch(e){console.warn('ARENA_SPAWN_ERROR '+String(e));}
});
system.afterEvents.scriptEventReceive.subscribe(ev=>{
 if(ev.id!=='arena:trials')return;
 const kind=ev.message;
 const itemID=kind==='wish_3'?'effect:clock_sword':kind==='wish_2'?'effect99:quartz_diamond_block':'effect:quartz_diamond';
 const reward=kind==='wish_3'?'effect:time_sword':'effect:ultra_instinct_sword';
 if(!['wish_1','wish_2','wish_3'].includes(kind)) return;
 let attempted=0; const d=world.getDimension('overworld');
 console.warn('ARENA_TRIALS_START '+JSON.stringify({kind,itemID,reward,limit:500}));
 let handle=system.runInterval(()=>{
  try{
   const rewards=d.getEntities({type:'minecraft:item',location:{x:40,y:101,z:40},maxDistance:12}).filter(e=>e.getComponent('minecraft:item')?.itemStack.typeId===reward);
   if(rewards.length){console.warn('ARENA_TRIALS_REWARD '+JSON.stringify({kind,attempted,type:reward,entities:rewards.length,amount:rewards[0].getComponent('minecraft:item').itemStack.amount}));system.clearRun(handle);return;}
   if(attempted>=500){console.warn('ARENA_TRIALS_NO_REWARD '+JSON.stringify({kind,attempted}));system.clearRun(handle);return;}
   for(let i=0;i<5 && attempted<500;i++){
    const entity=d.spawnItem(new ItemStack(itemID,1),{x:40.5,y:101,z:40.5});
    entity.triggerEvent(kind);attempted++;
   }
  }catch(e){console.warn('ARENA_TRIALS_ERROR '+JSON.stringify({kind,attempted,error:String(e)}));system.clearRun(handle);}
 },1);
});
system.runInterval(()=>{try{for(const p of world.getAllPlayers()){
 const h=p.getComponent('minecraft:health');
 console.warn('ARENA_PLAYER_HEALTH '+JSON.stringify({name:p.name,health:h.currentValue,max:h.effectiveMax}));
}}catch(e){console.warn('ARENA_PLAYER_HEALTH_ERROR '+String(e))}},20);
let iceTicks=0;
system.afterEvents.scriptEventReceive.subscribe(ev=>{
 if(ev.id!=='arena:observe_ice')return;
 iceTicks=0;const d=world.getDimension('overworld');
 let handle=system.runInterval(()=>{
  iceTicks+=5;
  try{
   const states={};let count=0;
   for(let x=32;x<=34;x++)for(let y=100;y<=101;y++)for(let z=29;z<=31;z++){
    const b=d.getBlock({x,y,z});
    if(b.typeId==='effect99:fake_ice'){count++;const state=String(b.permutation.getState('fake_ice:model'));states[state]=(states[state]||0)+1;}
   }
   console.warn('ARENA_ICE '+JSON.stringify({ticks:iceTicks,count,states}));
   if(iceTicks>=400)system.clearRun(handle);
  }catch(e){console.warn('ARENA_ICE_ERROR '+String(e));system.clearRun(handle)}
 },5);
});
system.runInterval(()=>{
 try{
  const d=world.getDimension('overworld');
  for(const p of world.getAllPlayers()){
   const v=p.getComponent('minecraft:movement');const e=p.getEffect('speed');
   console.warn('ARENA_SPEED '+JSON.stringify({entity:'player',name:p.name,current:v?.currentValue,base:v?.defaultValue,effect:e?{amplifier:e.amplifier,duration:e.duration}:null}));
  }
  for(const e of d.getEntities({type:'minecraft:pig',tags:['probe']})){
   const v=e.getComponent('minecraft:movement');const x=e.getEffect('speed');
   console.warn('ARENA_SPEED '+JSON.stringify({entity:'pig',location:e.location,current:v?.currentValue,base:v?.defaultValue,effect:x?{amplifier:x.amplifier,duration:x.duration}:null}));
  }
 }catch(e){console.warn('ARENA_SPEED_ERROR '+String(e))}
},20);
