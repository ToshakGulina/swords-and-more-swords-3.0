// Executes the original JavaScript handler in Node with mocked Bedrock interfaces.
// This tests JavaScript control flow, not Minecraft API/commands or game behavior.
'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
let script = fs.readFileSync(0, 'utf8');
const originalImport = 'import { world } from "@minecraft/server"';
assert.equal(script.split(originalImport).length, 2, 'expected exactly one original import');
script = script.replace(originalImport, ''); // Inject mock world into the context instead.
let listener;
const world = {afterEvents:{playerBreakBlock:{subscribe(fn){assert.equal(listener,undefined);listener=fn;}}}};
let r = 0;
let steps = [];
const mockedMath = Object.create(Math);
mockedMath.random = () => {steps.push('random');return r;};
vm.runInNewContext(script, {world, Math:mockedMath}, {timeout:1000});
assert.equal(typeof listener,'function');
function makePlayer(initial=[], fail=false) {
  const tags = new Set(initial); const commands=[];
  return {tags,commands,hasTag(tag){steps.push('hasTag:'+tag);return tags.has(tag);},
    addTag(tag){steps.push('addTag:'+tag);tags.add(tag);return true;},
    runCommand(cmd){steps.push('runCommand');commands.push(cmd);if(fail)throw new Error('mock command failure');return {};}};
}
function event(id,player){return {brokenBlockPermutation:{type:{id}},block:{location:{x:-7,y:64,z:9}},player};}
let player=makePlayer(); r=0.004999; steps=[];
listener(event('test:glowing_pumpkin',player));
assert.deepEqual(steps,['random','hasTag:pumpkin_sword','addTag:pumpkin_sword','runCommand']);
assert.deepEqual([...player.tags],['pumpkin_sword']);
assert.deepEqual(player.commands,['execute @s ~ ~ ~ loot spawn -7 64 9 loot pumpkin_sword']);
player=makePlayer(); r=0.005; steps=[];
listener(event('minecraft:pumpkin',player));
assert.deepEqual(steps,['random']);assert.equal(player.tags.size,0);assert.equal(player.commands.length,0);
player=makePlayer(); r=0; steps=[];
listener(event('test:pumpkin_stem',player));
listener(event('minecraft:melon_block',player));
assert.deepEqual(steps,[]);assert.equal(player.tags.size,0);
player=makePlayer(['pumpkin_sword']); r=0; steps=[];
listener(event('minecraft:carved_pumpkin',player));
assert.deepEqual(steps,['random','hasTag:pumpkin_sword']);assert.equal(player.commands.length,0);
player=makePlayer([],true); r=0; steps=[];
assert.throws(()=>listener(event('minecraft:pumpkin',player)),/mock command failure/);
assert.deepEqual(steps,['random','hasTag:pumpkin_sword','addTag:pumpkin_sword','runCommand']);
assert(player.tags.has('pumpkin_sword')); assert.equal(player.commands.length,1);
steps=[];listener(event('minecraft:pumpkin',player));
assert.deepEqual(steps,['random','hasTag:pumpkin_sword']);assert.equal(player.commands.length,1);
console.log('Mocked original script: all control-flow cases passed');
