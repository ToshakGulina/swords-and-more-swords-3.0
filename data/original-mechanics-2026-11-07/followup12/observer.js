// Read-only movement sampling for the unmodified boss and two isolated comparison entities.
import { world, system } from '@minecraft/server';
let handle;
system.afterEvents.scriptEventReceive.subscribe(event => {
  if (event.id !== 'arena:slime_jump' || event.message !== 'start') return;
  try {
    const dim = world.getDimension('overworld');
    const definitions = [
      ['original', 'entity:slime_king', 50],
      ['slow_control', 'arena:slime_king_slow', 60],
      ['fast_control', 'arena:slime_king_fast', 70],
    ];
    const entities = definitions.map(([name, type, x]) => {
      const entity = dim.spawnEntity(type, {x, y: 100, z: 50});
      entity.addTag('arena_jump_probe');
      return {name, entity};
    });
    const start = system.currentTick;
    console.warn('JUMP_START ' + JSON.stringify({tick: start, entities: definitions}));
    handle = system.runInterval(() => {
      try {
        const tick = system.currentTick - start;
        for (const {name, entity} of entities) {
          const pos = entity.location;
          let velocity = null;
          try { velocity = entity.getVelocity(); } catch (_) {}
          let ground = null;
          try { ground = entity.isOnGround; } catch (_) {}
          console.warn('JUMP_SAMPLE ' + JSON.stringify({name, tick, x:pos.x, y:pos.y, z:pos.z, vy:velocity?.y, ground}));
        }
        if (tick >= 1000) {
          console.warn('JUMP_FINISHED ' + tick);
          system.clearRun(handle);
        }
      } catch (error) {
        console.warn('JUMP_ERR ' + String(error));
        system.clearRun(handle);
      }
    }, 1);
  } catch (error) { console.warn('JUMP_PREP_ERR ' + String(error)); }
});
