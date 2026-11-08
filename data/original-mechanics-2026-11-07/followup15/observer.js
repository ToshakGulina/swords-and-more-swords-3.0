import {world,system} from '@minecraft/server';
let start=0, interval;
world.afterEvents.entitySpawn.subscribe(e=>{try{if(e.entity.typeId==='minecraft:ender_crystal')console.warn('SPEC_SPAWN '+JSON.stringify({tick:system.currentTick,id:e.entity.id,pos:e.entity.location,dim:e.entity.dimension.id}));}catch(err){console.warn('SPEC_SPAWN_ERR '+String(err))}});
function player(){return world.getAllPlayers().find(x=>['ArenaSpectralProbe','ArenaSpecSurvival'].includes(x.name))}
function snap(label){
 try{
  const p=player();if(!p){console.warn('SPEC_NO_PLAYER '+label);return}
  const pos=p.location, dim=p.dimension;
  const e=dim.getEntities({type:'minecraft:ender_crystal',location:pos,maxDistance:32});
  const crystals=e.map(c=>{let riding=null,families={};try{riding=c.getComponent('minecraft:riding')?.entityRidingOn?.typeId??null}catch(_){}
    try{let f=c.getComponent('minecraft:type_family');for(const name of ['spectral_sword','ender_crystal_default','ender_crystal_scale'])families[name]=f?.hasTypeFamily(name)??null}catch(_){}
    return {id:c.id,pos:c.location,riding,families};});
  let item=null;try{item=p.getComponent('minecraft:inventory').container.getItem(p.selectedSlot)?.typeId??null}catch(_){}
  console.warn('SPEC_SAMPLE '+JSON.stringify({label,tick:system.currentTick,delta:system.currentTick-start,dimension:dim.id,player:pos,item,crystals}));
 }catch(err){console.warn('SPEC_ERROR '+String(err))}
}
system.afterEvents.scriptEventReceive.subscribe(e=>{
 if(e.id!=='arena:spectral_probe')return;
 try{
   if(e.message==='start'){start=system.currentTick;if(interval)system.clearRun(interval);interval=system.runInterval(()=>snap('periodic'),20);snap('start')}
   else if(e.message==='end'){system.clearRun(interval);snap('end')}
   else if(e.message==='to_end'){
    const p=player();p.teleport({x:0.5,y:100,z:0.5},{dimension:world.getDimension('the_end')});console.warn('SPEC_TELEPORT_END '+system.currentTick)
   }else snap(e.message)
 }catch(err){console.warn('SPEC_COMMAND_ERROR '+String(err))}
});
