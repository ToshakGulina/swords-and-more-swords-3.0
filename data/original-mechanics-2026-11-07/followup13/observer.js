// Read-only snapshots of the server inventory and dropped item entities.
import { world, system } from '@minecraft/server';
system.afterEvents.scriptEventReceive.subscribe(e => {
 if (e.id !== 'arena:giveprobe') return;
 try {
  const p=world.getPlayers().find(p=>p.name==='ArenaGiveTwo');
  if (!p) throw new Error('player missing');
  const c=p.getComponent('minecraft:inventory').container;
  let slots=[];
  for(let i=0;i<c.size;i++) { const item=c.getItem(i); if(item)slots.push({slot:i,id:item.typeId,count:item.amount}); }
  const drops=p.dimension.getEntities({type:'minecraft:item',location:p.location,maxDistance:20}).map(x=>{const it=x.getComponent('minecraft:item').itemStack;return {id:it.typeId,count:it.amount,loc:x.location};});
  console.warn('GIVE_SNAPSHOT '+JSON.stringify({label:e.message,tick:system.currentTick,playerLocation:p.location,slots,empty:c.emptySlotsCount,drops}));
 } catch(ex) {console.warn('GIVE_ERROR '+String(ex));}
});
system.afterEvents.scriptEventReceive.subscribe(e=>{
 if(e.id!=='arena:givewatch')return;
 let n=0;const p=world.getPlayers().find(p=>p.name==='ArenaGiveTwo');
 const handle=system.runInterval(()=>{try{
  const items=p.dimension.getEntities({type:'minecraft:item',location:p.location,maxDistance:20}).map(x=>{let i=x.getComponent('minecraft:item').itemStack;return i.typeId+':'+i.amount});
  console.warn('GIVE_WATCH '+JSON.stringify({label:e.message,tick:system.currentTick,n,items}));
  if(++n>=80)system.clearRun(handle);
 }catch(err){console.warn('GIVE_WATCH_ERROR '+String(err));system.clearRun(handle)}},1);
});
