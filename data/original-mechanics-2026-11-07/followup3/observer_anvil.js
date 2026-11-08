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
system.afterEvents.scriptEventReceive.subscribe(ev=>{
 if(ev.id!=='arena:anvil')return;
 try{const p=world.getAllPlayers().find(p=>p.name==='ArenaTest');const inv=p.getComponent('minecraft:inventory').container;
 if(ev.message==='glass_damage'||ev.message==='glass_fresh'||ev.message==='iron_damage'){
  const item=new ItemStack(ev.message==='iron_damage'?'minecraft:iron_sword':'effect:glass_sword',1);
  if(ev.message!=='glass_fresh'){let d=item.getComponent('minecraft:durability');d.damage=ev.message==='iron_damage'?50:1;}
  inv.setItem(0,item);inv.setItem(1,new ItemStack(ev.message==='iron_damage'?'minecraft:iron_ingot':'minecraft:glass',1));
 }
 for(let j=0;j<2;j++){const i=inv.getItem(j),d=i?.getComponent('minecraft:durability');console.warn('ANVIL_INV '+JSON.stringify({case:ev.message,slot:j,id:i?.typeId??null,damage:d?.damage??null,max:d?.maxDurability??null}));}
 }catch(e){console.warn('ANVIL_ERR '+String(e))}
});
