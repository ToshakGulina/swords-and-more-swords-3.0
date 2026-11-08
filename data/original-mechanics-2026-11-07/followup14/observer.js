import {world,system,EntityDamageCause} from '@minecraft/server';
let bee, skeleton, handle;
world.afterEvents.entityHurt.subscribe(e=>{
 if(!bee || !skeleton) return;
 try {
  if(e.hurtEntity.id===bee.id||e.hurtEntity.id===skeleton.id) console.warn('BEE_HURT '+JSON.stringify({tick:system.currentTick,victim:e.hurtEntity.typeId,source:e.damageSource?.damagingEntity?.typeId,cause:e.damageSource?.cause,damage:e.damage}));
 }catch(err){console.warn('BEE_HURT_ERR '+String(err))}
});
system.afterEvents.scriptEventReceive.subscribe(e=>{
 if(e.id!=='arena:beevictim')return;
 try {
  const dim=world.getDimension('overworld');
  skeleton=dim.spawnEntity('minecraft:skeleton',{x:54.5,y:100,z:50.5}); skeleton.addTag('arena_bee_victim');
  skeleton.addEffect('fire_resistance',800,{showParticles:false});skeleton.addEffect('slowness',800,{amplifier:255,showParticles:false});
  bee=dim.spawnEntity('minecraft:bee',{x:50.5,y:100,z:50.5});bee.addTag('arena_bee_attacker');
  const begin=system.currentTick;
  console.warn('BEE_SETUP '+JSON.stringify({tick:begin,bee:bee.typeId,skeleton:skeleton.typeId}));
  system.runTimeout(()=>{try{bee.applyDamage(1,{cause:EntityDamageCause.entityAttack,damagingEntity:skeleton});console.warn('BEE_PROVOKE '+system.currentTick)}catch(err){console.warn('BEE_ERROR '+String(err))}},40);
  handle=system.runInterval(()=>{try{
   console.warn('BEE_SAMPLE '+JSON.stringify({tick:system.currentTick-begin,bee:bee.location,skeleton:skeleton.location,mark:bee.getComponent('minecraft:mark_variant')?.value}));
   if(system.currentTick-begin>=500){console.warn('BEE_FINISHED');system.clearRun(handle)}
  }catch(err){console.warn('BEE_END '+String(err));system.clearRun(handle)}},20);
 }catch(err){console.warn('BEE_ERROR '+String(err))}
});
