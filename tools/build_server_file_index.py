#!/usr/bin/env python3
"""Read an optional server ZIP without execution/extraction, fingerprint and classify entries."""
import argparse
from collections import Counter
import gzip
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
from zipfile import ZipFile

import json5
import nbtlib
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
MD5='4a23794a882b008d3f0a5fde8b338f55'
SHA='50cdb466cddef99066b888e2198479a9b352ea1535f00820b0204e92baa1ab0a'
MAX_UNPACKED=25*1024*1024


def check_bytes(raw,suffix):
    if suffix=='.json':
        text=raw.decode('utf-8-sig')
        duplicate=[]
        def pairs(items):
            out={}
            for k,v in items:
                if k in out:duplicate.append(k)
                out[k]=v
            return out
        try:
            json.loads(text,object_pairs_hook=pairs)
            return {'check':'json_parse','status':'duplicate_keys' if duplicate else 'ok','duplicate_keys':sorted(set(duplicate))}
        except ValueError:
            try:json5.loads(text,allow_duplicate_keys=False)
            except ValueError as exc:return {'check':'json5','status':'invalid','error':str(exc).replace('\n',' ')[:250]}
            return {'check':'json5','status':'ok'}
    if suffix=='.nbt':
        # Do not attempt a schema/byte-order parse: bounded gzip decompression only.
        with gzip.GzipFile(fileobj=io.BytesIO(raw)) as f:unpacked=f.read(MAX_UNPACKED+1)
        if len(unpacked)>MAX_UNPACKED:return {'check':'gzip_only','status':'uncompressed_size_limit'}
        return {'check':'gzip_only','status':'ok','uncompressed_bytes':len(unpacked),'first_tag':unpacked[:1].hex()}
    if suffix=='.mcstructure':
        stream=io.BytesIO(raw);obj=nbtlib.File.parse(stream,byteorder='little')
        if stream.tell()!=len(raw):raise ValueError('trailing NBT bytes')
        return {'check':'little_endian_nbt_parse','status':'ok','root_keys':list(obj.keys())}
    if suffix=='.png':
        with Image.open(io.BytesIO(raw)) as im:im.verify()
        with Image.open(io.BytesIO(raw)) as im:im.load();return {'check':'image_verify_and_decode','status':'ok','size':list(im.size)}
    if suffix in ('.lang','.txt','.html','.properties','.wlist'):
        text=raw.decode('utf-8-sig');return {'check':'utf8_decode_only','status':'ok','lines':len(text.splitlines())}
    if suffix=='.brarchive':return {'check':'byte_fingerprint_only','status':'brarchive_not_decoded'}
    return {'check':'byte_fingerprint_only','status':'binary_not_decoded'}


def build(path):
    h1=hashlib.md5();h2=hashlib.sha256()
    with path.open('rb') as f:
        while chunk:=f.read(1024*1024):h1.update(chunk);h2.update(chunk)
    if h1.hexdigest()!=MD5 or h2.hexdigest()!=SHA:raise ValueError('Server archive checksum mismatch')
    rows=[];ext=Counter();dirs=0
    with ZipFile(path) as z:
        for info in z.infolist():
            if info.is_dir():dirs+=1;continue
            name=info.filename
            if name.startswith('/') or '..' in PurePosixPath(name).parts:raise ValueError('Unsafe ZIP path: '+name)
            suffix=PurePosixPath(name).suffix.lower();digest=hashlib.sha256();size=0;head=b'';collect=suffix in ('.json','.nbt','.mcstructure','.png','.lang','.txt','.html','.properties','.wlist');buf=bytearray()
            with z.open(info) as stream:
                while chunk:=stream.read(1024*1024):
                    if not head:head=chunk[:16]
                    digest.update(chunk);size+=len(chunk)
                    if collect:
                        if len(buf)+len(chunk)>MAX_UNPACKED:raise ValueError('Compressed member exceeds validation size cap: '+name)
                        buf.extend(chunk)
            if size!=info.file_size:raise ValueError('Length mismatch: '+name)
            try:validation=check_bytes(bytes(buf),suffix) if collect else check_bytes(b'',suffix)
            except Exception as exc:validation={'check':'validator_error','status':'error','error':str(exc).replace('\n',' ')[:250]}
            ext[suffix or '<no extension>']+=1
            rows.append({'path':name,'bytes':size,'compressed_bytes':info.compress_size,'crc32':f'{info.CRC:08x}','sha256':digest.hexdigest(),'first_bytes_hex':head.hex(),'validation':validation})
    if len({r['path'] for r in rows})!=len(rows):raise ValueError('Duplicate server ZIP paths')
    return {'source':'bedrock-server-1.26.62.1.zip; bytes read and CRC checked; no executables run or extracted','md5':MD5,'sha256':SHA,'files':len(rows),'directories':dirs,'bytes_total':sum(r['bytes'] for r in rows),'extensions':dict(ext.most_common()),'entries':rows}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--server-zip',type=Path,required=True);p.add_argument('--output',type=Path,default=ROOT/'data/server-file-index.json');args=p.parse_args();data=build(args.server_zip);args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8');print('Checked:',data['files'],'files; statuses:',dict(Counter(r['validation']['status'] for r in data['entries'])))

if __name__=='__main__':main()
