import {world,system,ItemStack} from '@minecraft/server';
const cases=[{name:'coal_sword',x:53,fuel:'effect:coal_sword'},{name:'coal',x:55,fuel:'minecraft:coal'},{name:'stick',x:57,fuel:'minecraft:stick'}];
let start=0, handle=0, last={};
function slot(item){return item?{id:item.typeId,amount:item.amount}:null}
system.afterEvents.scriptEventReceive.subscribe(e=>{
 if(e.id!=='arena:fuel'||e.message!=='start')return;
 try{
  const d=world.getDimension('overworld');
  for(const c of cases){const b=d.getBlock({x:c.x,y:100,z:50});const inv=b.getComponent('inventory').container;inv.setItem(0,new ItemStack('minecraft:iron_ore',64));inv.setItem(1,new ItemStack(c.fuel,1));console.warn('FUEL_PREP '+JSON.stringify({name:c.name,input:slot(inv.getItem(0)),fuel:slot(inv.getItem(1))}));}
  start=system.currentTick;
  handle=system.runInterval(()=>{try{
   for(const c of cases){const b=d.getBlock({x:c.x,y:100,z:50});const inv=b.getComponent('inventory').container;const status={name:c.name,ticks:system.currentTick-start,block:b.typeId,input:slot(inv.getItem(0)),fuel:slot(inv.getItem(1)),output:slot(inv.getItem(2))};const sig=JSON.stringify([status.block,status.input,status.fuel,status.output]);if(last[c.name]!==sig){last[c.name]=sig;console.warn('FUEL_STATE '+JSON.stringify(status));}}
   if(system.currentTick-start>=8400){console.warn('FUEL_FINISHED ticks='+String(system.currentTick-start));system.clearRun(handle)}
  }catch(err){console.warn('FUEL_ERR '+String(err));system.clearRun(handle)}},10);
 }catch(err){console.warn('FUEL_PREP_ERR '+String(err))}
});
