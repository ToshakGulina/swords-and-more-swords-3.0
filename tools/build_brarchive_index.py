#!/usr/bin/env python3
"""Inspect observed Bedrock server brarchive layout, without executing or extracting files.

The format interpretation is inferred from this one archive, not an official specification.
Zero-length indexed names are matched by path to ZIP entries as a hypothesis, not engine semantics.
"""
import argparse
from collections import Counter
from functools import lru_cache
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import struct
from zipfile import ZipFile

import json5
from PIL import Image
from build_server_file_index import MD5, SHA

ROOT=Path(__file__).resolve().parents[1]
MAGIC=bytes.fromhex('7d2725b1a0527026')

@lru_cache(maxsize=10000)
def validate(raw,ext):
    if ext=='.json':
        if raw.startswith(b'\x7fMCB'):
            return {'check':'mcb_binary_magic_only','status':'mcb_not_decoded'}
        duplicate=[]
        def pairs(items):
            out={}
            for k,v in items:
                if k in out:duplicate.append(k)
                out[k]=v
            return out
        text=raw.decode('utf-8-sig')
        try:
            json.loads(text,object_pairs_hook=pairs)
            return {'check':'json','status':'duplicate_keys' if duplicate else 'ok','duplicate_keys':sorted(set(duplicate))}
        except ValueError:
            try:json5.loads(text,allow_duplicate_keys=False)
            except ValueError as exc:return {'check':'json5','status':'invalid','error':str(exc).replace('\n',' ')[:180]}
            return {'check':'json5','status':'ok'}
    if ext=='.png':
        with Image.open(io.BytesIO(raw)) as im:im.verify()
        with Image.open(io.BytesIO(raw)) as im:im.load();return {'check':'image_verify_and_decode','status':'ok','size':list(im.size)}
    if ext=='.js':return {'check':'utf8_decode_only','status':'ok','lines':len(raw.decode('utf-8-sig').splitlines())}
    return {'check':'byte_fingerprint_only','status':'unclassified'}


def parse_archive(raw):
    if len(raw)<16 or raw[:8]!=MAGIC:raise ValueError('Unrecognised magic/header')
    count,version=struct.unpack_from('<II',raw,8)
    if version!=1:raise ValueError('Unexpected brarchive layout version')
    base=16+count*256
    if base>len(raw):raise ValueError('Truncated entry table')
    rows=[];spans=[];names=set()
    for i in range(count):
        p=16+i*256;length=raw[p]
        if length>247:raise ValueError('Entry name too long')
        name=raw[p+1:p+1+length].decode('utf-8')
        if not name or name.startswith('/') or '..' in PurePosixPath(name).parts:raise ValueError('Invalid entry name')
        if name in names:raise ValueError('Duplicate brarchive name')
        names.add(name)
        offset,size=struct.unpack_from('<II',raw,p+248)
        if base+offset+size>len(raw):raise ValueError('Entry extends past end')
        if size:spans.append((offset,offset+size))
        rows.append((name,offset,size,raw[base+offset:base+offset+size]))
    prev=0
    for start,end in sorted(spans):
        if start!=prev:raise ValueError('Gap or overlap in nonempty data spans')
        prev=end
    if prev!=len(raw)-base:raise ValueError('Unaccounted payload bytes')
    return rows


def build(path):
    md5=hashlib.md5();sha=hashlib.sha256()
    with path.open('rb') as f:
        while chunk:=f.read(1024*1024):md5.update(chunk);sha.update(chunk)
    if (md5.hexdigest(),sha.hexdigest())!=(MD5,SHA):raise ValueError('Server ZIP checksum mismatch')
    all_entries=[];archives=[]
    with ZipFile(path) as z:
        zip_names={i.filename for i in z.infolist() if not i.is_dir()}
        for info in z.infolist():
            if not info.filename.endswith('.brarchive'):continue
            raw=z.read(info);parsed=parse_archive(raw)
            if '/__brarchive/' not in info.filename:raise ValueError('Unexpected brarchive path: '+info.filename)
            pack,rel=info.filename.split('/__brarchive/',1);candidate_prefix=pack+'/'+rel[:-len('.brarchive')]+'/'
            archives.append({'path':info.filename,'sha256':hashlib.sha256(raw).hexdigest(),'count':len(parsed)})
            for name,offset,size,payload in parsed:
                row={'container':info.filename,'name':name,'offset':offset,'bytes':size}
                if size:
                    row['storage']='embedded';row['sha256']=hashlib.sha256(payload).hexdigest()
                    try:row['validation']=validate(payload,PurePosixPath(name).suffix.lower())
                    except Exception as exc:row['validation']={'check':'validator_error','status':'error','error':str(exc).replace('\n',' ')[:180]}
                else:
                    candidate=candidate_prefix+name
                    row['storage']='zero_length_index';row['path_candidate']=candidate;row['candidate_exists_in_zip']=candidate in zip_names
                all_entries.append(row)
    return {'method':'inferred 8-byte magic, version 1 header and 256-byte records; bounds and contiguous embedded spans checked; zero-length candidate path match does not prove engine resolution',
            'server_zip_md5':MD5,'server_zip_sha256':SHA,'containers':archives,'entries':all_entries}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--server-zip',type=Path,required=True);p.add_argument('--output',type=Path,default=ROOT/'data/server-brarchive-index.json');args=p.parse_args();out=build(args.server_zip);args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8');print('containers',len(out['containers']),'records',len(out['entries']));print('storage',dict(Counter(e['storage'] for e in out['entries'])));print('embedded validation',dict(Counter(e['validation']['status'] for e in out['entries'] if e['storage']=='embedded')));print('missing candidate',sum(not e['candidate_exists_in_zip'] for e in out['entries'] if e['storage']=='zero_length_index'))

if __name__=='__main__':main()
