"""Ensure the reader-facing guide includes every ID and matches source index values."""
from pathlib import Path
import re
import unittest

ROOT=Path(__file__).resolve().parents[1]

def indexes(version):
    s=(ROOT/'docs/quick-reference.md').read_text(encoding='utf-8')
    part=re.split(r'^## '+re.escape(version)+r'\s*$',s,flags=re.M)[1].split('\n## ')[0]
    result={}
    for line in part.splitlines():
        if line.startswith('| `effect:'):
            cells=[x.strip() for x in line.strip('|').split('|')]
            result[cells[0].strip('`')]=[cells[1].strip('`'),cells[2].strip('`')]
    return result

class GuideTests(unittest.TestCase):
    def test_coverage_and_values_for_all_versions(self):
        versions={v:indexes(v) for v in ('1.6','2.8.8','2.8.14')}
        guide=(ROOT/'docs/guide-ru.md').read_text(encoding='utf-8');seen={}
        for line in guide.splitlines():
            m=re.search(r'`(effect:[^`]+)`',line)
            if line.startswith('| [') and m:
                cells=[x.strip() for x in line.strip('|').split('|')]
                self.assertNotIn(m.group(1),seen);seen[m.group(1)]=cells
        self.assertEqual(set(seen),set().union(*[set(x) for x in versions.values()]))
        self.assertEqual(len(seen),43)
        def normalized(item):return ' / '.join('не указано' if x=='—' else x for x in item)
        for id,cells in seen.items():
            self.assertEqual(cells[1],normalized(versions['1.6'][id]) if id in versions['1.6'] else 'нет ID')
            if id in versions['2.8.14']:
                self.assertEqual(versions['2.8.8'][id],versions['2.8.14'][id]);self.assertEqual(cells[2],normalized(versions['2.8.14'][id]))
            else:self.assertEqual(cells[2],'нет ID')
    def test_relative_links_and_scope_warning(self):
        p=ROOT/'docs/guide-ru.md';text=p.read_text(encoding='utf-8')
        self.assertIn('не дословная копия каждого файла',text)
        self.assertIn('не полная транскрипция всех скриншотов',text)
        for link in re.findall(r'\]\(([^)]+)\)',text):
            if '://' not in link:
                self.assertTrue((p.parent/link.split('#')[0]).is_file(),link)

if __name__=='__main__':unittest.main()
