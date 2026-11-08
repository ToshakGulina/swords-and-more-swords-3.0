import { system, world } from "@minecraft/server";
system.beforeEvents.startup.subscribe(({itemComponentRegistry}) => {
 itemComponentRegistry.registerCustomComponent("arena_probe:test_effect", {
  onUse() { console.warn("ARENA_PROBE_ON_USE"); },
  onHitEntity() { console.warn("ARENA_PROBE_ON_HIT"); }
 });
 console.warn("ARENA_PROBE_COMPONENT_REGISTERED");
});
system.run(() => console.warn("ARENA_PROBE_SCRIPT_READY"));
