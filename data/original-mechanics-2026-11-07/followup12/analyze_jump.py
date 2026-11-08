"""Summarize contiguous on-ground runs after an observed airborne landing."""
import json
import statistics
from pathlib import Path

log = Path(__file__).resolve().parent / 'jump.log'
samples = {}
for line in log.read_text(encoding='utf-8').splitlines():
    if 'JUMP_SAMPLE ' not in line:
        continue
    sample = json.loads(line.split('JUMP_SAMPLE ', 1)[1])
    samples.setdefault(sample['name'], []).append(sample)

for name, values in sorted(samples.items()):
    assert [v['tick'] for v in values] == list(range(1, 1001)), name
    assert all(isinstance(v['ground'], bool) for v in values), name
    ground_runs = []
    airborne_runs = []
    previous = values[0]['ground']
    start = values[0]['tick']
    initial = True
    for sample in values[1:]:
        current = sample['ground']
        if current != previous:
            length = sample['tick'] - start
            if not initial:
                (ground_runs if previous else airborne_runs).append(length)
            start, previous, initial = sample['tick'], current, False
    assert ground_runs and airborne_runs
    print(json.dumps({'name': name, 'samples': len(values),
                      'complete_ground_runs': len(ground_runs),
                      'ground_ticks_min': min(ground_runs), 'ground_ticks_median': statistics.median(ground_runs),
                      'ground_ticks_max': max(ground_runs),
                      'complete_airborne_runs': len(airborne_runs),
                      'airborne_ticks_min': min(airborne_runs), 'airborne_ticks_max': max(airborne_runs)},
                     ensure_ascii=False))
