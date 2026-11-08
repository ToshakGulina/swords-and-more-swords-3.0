#!/usr/bin/env python3
"""Compare directly bound 2.8.8 help lines with the unmodified user text.

Usage: python tools/compare_ui_to_description.py
Whitespace and case are normalized; non-matches still require human review.
"""
from pathlib import Path
import re
import zipfile

root = Path(__file__).resolve().parents[1]
with zipfile.ZipFile(root / 'sources/swordsandmoreswords_2_8_8.mcaddon') as archive:
    ui = archive.read('Swords_R/ui/how_to_play_screen.json').decode('utf-8')
    lang = archive.read('Swords_R/texts/en_US.lang').decode('utf-8')
keys = list(dict.fromkeys(re.findall(r'\$text"\s*:\s*"(effect\.[^" ]+\.text\.\d+)"', ui)))
values = dict(line.split('=', 1) for line in lang.splitlines() if '=' in line)
normalize = lambda s: re.sub(r'\s+', ' ', s.strip()).casefold()
user_lines = {normalize(line) for line in (root / 'docs/user-provided-original-description.txt').read_text().splitlines() if line.strip()}
missing = [key for key in keys if key not in values]
empty = [key for key in keys if key in values and not normalize(values[key])]
matched = [key for key in keys if key in values and normalize(values[key]) in user_lines]
other = [key for key in keys if key in values and normalize(values[key]) and key not in matched]
print(f'Directly bound keys: {len(keys)}; missing localization: {len(missing)}; empty: {len(empty)}; exact lines after whitespace/case normalization: {len(matched)}; non-exact: {len(other)}')
for key in missing:
    print('MISSING', key)
for key in empty:
    print('EMPTY', key)
for key in other:
    print('NON-EXACT', key, repr(values[key]))
