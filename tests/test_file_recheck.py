"""Offline regression checks for the repeated file and container inventories."""
import hashlib
import io
import json
from collections import Counter
from pathlib import Path
import struct
import sys
import unittest
from zipfile import ZipFile

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
import nbtlib
from build_brarchive_index import MAGIC,parse_archive,validate as validate_embedded
from build_file_completeness_audit import ARCHIVES,render,validate
from build_server_player_comparison import render as render_player


def data(name):return json.loads((ROOT/'data'/name).read_text(encoding='utf-8'))


def sample_archive():
    files=[('test.json',b'{"ok":true}'),('external.nbt',b'')]
    entries=[];offset=0;payload=b''
    for name,content in files:
        b=name.encode();record=bytearray(256);record[0]=len(b);record[1:1+len(b)]=b
        struct.pack_into('<II',record,248,offset,len(content));entries.append(record);payload+=content;offset+=len(content)
    return MAGIC+struct.pack('<II',len(files),1)+b''.join(entries)+payload


class FileRecheckTests(unittest.TestCase):
    def test_addon_files_against_inventory(self):
        saved=data('file-validation.json')['archives']
        for version,(filename,md5) in ARCHIVES.items():
            raw=(ROOT/'sources'/filename).read_bytes();self.assertEqual(hashlib.md5(raw).hexdigest(),md5)
            with ZipFile(io.BytesIO(raw)) as z:
                rows={r['path']:r for r in saved[version]['files']};infos=[i for i in z.infolist() if not i.is_dir()]
                self.assertEqual(len(rows),len(infos));self.assertEqual(saved[version]['count'],len(infos))
                for info in infos:
                    content=z.read(info);r=rows[info.filename]
                    self.assertEqual(r['bytes'],len(content));self.assertEqual(r['sha256'],hashlib.sha256(content).hexdigest());self.assertEqual(r['crc32'],f'{info.CRC:08x}')
    def test_addon_validation_and_render(self):
        self.assertEqual(validate(b'{one:1}', '.json')['status'],'ok')
        self.assertEqual(validate(b'{x:1,x:2}', '.json')['status'],'duplicate_keys')
        self.assertEqual(validate(b'{x:1}}', '.json')['status'],'invalid')
        self.assertEqual(validate(b'a=1\na=2\n', '.lang')['duplicate_keys'],{'a':2})
        obj=nbtlib.File({'number':nbtlib.Int(3)},root_name='');buf=io.BytesIO();obj.write(buf,byteorder='little')
        self.assertEqual(validate(buf.getvalue(),'.mcstructure')['status'],'ok')
        saved=data('file-validation.json');self.assertEqual(render(saved),(ROOT/'docs/file-review-status.md').read_text(encoding='utf8'))
    def test_drive_and_screenshot_snapshot(self):
        listing=data('folder-listing-snapshot.json')['files'];screens=data('folder-screenshot-recheck.json')['files'];self.assertEqual(len(listing),25);self.assertEqual(len(screens),21)
        byid={r['id']:r for r in listing};self.assertEqual(len(byid),25);ocr=(ROOT/'docs/screenshot-ocr.md').read_text(encoding='utf8')
        for r in screens:
            original=byid[r['drive_id']];self.assertEqual(original['md5'],r['drive_md5']);self.assertEqual(original['size'],r['bytes']);self.assertTrue(r['sha256_matches_ocr_index']);self.assertIn(r['sha256'],ocr);self.assertIn(r['name'],ocr)
    def test_inferred_brarchive_layout(self):
        raw=sample_archive();rows=parse_archive(raw);self.assertEqual(rows[0],('test.json',0,11,b'{"ok":true}'));self.assertEqual(rows[1],('external.nbt',11,0,b''))
        for bad in (b'bad', b'X'+raw[1:],raw[:-1]):
            with self.assertRaises(ValueError):parse_archive(bad)
        overlap=bytearray(raw);struct.pack_into('<II',overlap,16+256+248,0,1)
        with self.assertRaises(ValueError):parse_archive(overlap)
        self.assertEqual(validate_embedded(b'{"x":1}', '.json')['status'],'ok')
        self.assertEqual(validate_embedded(b'{"x":1,"x":2}', '.json')['status'],'duplicate_keys')
        self.assertEqual(validate_embedded(b'\x7fMCB\x01\x00', '.json')['status'],'mcb_not_decoded')
    def test_server_indexes_are_consistent(self):
        top=data('server-file-index.json');nested=data('server-brarchive-index.json');entries=top['entries'];by_path={r['path']:r for r in entries}
        self.assertEqual(len(entries),3384);self.assertEqual(len(by_path),3384);self.assertEqual(top['sha256'],nested['server_zip_sha256'])
        containers=nested['containers'];self.assertEqual(len(containers),658);self.assertEqual(len(nested['entries']),9543)
        self.assertEqual(sum(r['count'] for r in containers),9543)
        for c in containers:self.assertEqual(c['sha256'],by_path[c['path']]['sha256'])
        counts=Counter(r['storage'] for r in nested['entries']);self.assertEqual(counts,{'embedded':7801,'zero_length_index':1742})
        checks=Counter(r['validation']['check'] for r in nested['entries'] if r['storage']=='embedded');self.assertEqual(checks,{'json':7236,'mcb_binary_magic_only':312,'image_verify_and_decode':238,'utf8_decode_only':15})
        for r in nested['entries']:
            if r['storage']=='zero_length_index':self.assertTrue(r['candidate_exists_in_zip']);self.assertIn(r['path_candidate'],by_path)
    def test_server_player_sources_and_render(self):
        saved=data('server-player-reference.json');nested=data('server-brarchive-index.json');refs={(r['container'],r['name']):r for r in nested['entries']}
        self.assertEqual(len(saved['references']),12)
        for r in saved['references']:self.assertEqual(r['sha256'],refs[(r['container'],r['entry'])]['sha256'])
        base=next(r for r in saved['references'] if r['container']=='behavior_packs/vanilla/__brarchive/entities.brarchive')
        for v in saved['addons'].values():
            for k in ('minecraft:player.exhaustion','minecraft:player.saturation'):self.assertEqual(v['components'][k],base['components'][k])
        self.assertTrue(base['components']['minecraft:exhaustion_values']['present']);self.assertEqual(base['components']['minecraft:exhaustion_values']['value'],'')
        self.assertEqual(render_player(saved),(ROOT/'docs/server-player-comparison.md').read_text(encoding='utf8'))

if __name__=='__main__':unittest.main()
