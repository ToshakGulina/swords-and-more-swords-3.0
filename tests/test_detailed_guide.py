"""Regression checks for the standalone item-by-item research guide."""
import json
from pathlib import Path
import re
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
from build_detailed_guide import build,acquisition_sections,recipe_data,screenshot_line
from build_quick_reference import VERSIONS,read_items

class DetailedGuideTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text=(ROOT/'docs/detailed-item-guide-ru.md').read_text(encoding='utf8')
        cls.versions={v:read_items(filename,pack) for v,filename,pack in VERSIONS}
    def test_reproducible_and_complete_card_coverage(self):
        self.assertEqual(self.text,build())
        cards=re.findall(r'^## (\d{2})\. .*? — `(effect:[^`]+)`$',self.text,re.M)
        all_ids=set().union(*(set(items) for items in self.versions.values()))
        self.assertEqual(len(cards),43);self.assertEqual([int(i) for i,_ in cards],list(range(1,44)))
        self.assertEqual({i for _,i in cards},all_ids)
        for i,ident in cards:
            match=re.search(r'^## '+i+r'\. .*?(?=^## \d{2}\. |^## Приложение А\.|\Z)',self.text,re.S|re.M)
            card=match.group();self.assertIn('### Основные данные и ремонт',card);self.assertIn('### Рецепты и пути получения',card);self.assertIn('### Способности, условия и вероятности по файлам',card);self.assertIn('### Что написано на скриншотах',card)
            if ident in self.versions['2.8.14']:self.assertIn('Основная цепочка 2.8.14',card)
            if ident in self.versions['1.6']:self.assertIn('Старая версия 1.6',card)
    def test_all_raw_item_definitions_round_trip(self):
        appendix=self.text.split('## Приложение В. Точные компоненты и события предметов\n',1)[1]
        chunks=re.split(r'^### \d{2}\. .*? — `(effect:[^`]+)`\s*$',appendix,flags=re.M)
        self.assertEqual((len(chunks)-1)//2,43)
        for n in range(1,len(chunks),2):
            ident,section=chunks[n],chunks[n+1]
            blocks=re.findall(r'\*\*Архив ([^*]+):\*\*\s*\n\s*```json\n(.*?)\n```',section,re.S)
            for ver,raw in blocks:
                version='2.8.8' if ver.startswith('2.8.8') else ver
                self.assertEqual(json.loads(raw),self.versions[version][ident][1],(ident,version))
            expected=sum(ident in self.versions[v] for v in ('1.6','2.8.14'))+(ident=='effect:ice_sword')
            self.assertEqual(len(blocks),expected,ident)
    def test_ocr_and_loot_limitations(self):
        appendix=self.text.split('## Приложение Б. Распознанный текст всех 21 скриншотов',1)[1].split('## Приложение В.',1)[0]
        names=re.findall(r'^#### (Screenshot_[^\n]+\.jpg)\s*$',appendix,re.M)
        self.assertEqual(len(names),21);self.assertEqual(len(set(names)),21)
        self.assertIn('не полностью вручную выверенная транскрипция',appendix.replace('**',''))
        self.assertIn('а не шанс реальной добычи',self.text)
        self.assertIn('loot spawn',self.text);self.assertIn('5/41',self.text);self.assertIn('13.1758%',self.text)
        screenshots=json.loads((ROOT/'data/screenshot-stat-evidence.json').read_text())
        folder=json.loads((ROOT/'data/folder-listing-snapshot.json').read_text())['files']
        for entry in screenshots:
            self.assertIn(screenshot_line(entry['id'],{entry['id']:entry},folder),self.text)

if __name__=='__main__':unittest.main()
