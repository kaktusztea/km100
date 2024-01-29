#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re
import os

def encode_anchor(match):
    anchor = match.group(1)
    encoded_anchor = re.sub(r'([^a-zA-Z0-9])', lambda x: f'&#{ord(x.group(1))};', anchor)
    return f'({encoded_anchor})'

def encode_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

#    pattern = r'\(([^)]+)\)'
    pattern = r'\w+\#([a-z].+)\).+'
    encoded_content = re.sub(pattern, encode_anchor, content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(encoded_content)

if __name__ == "__main__":

    encode_md_file('/repo/github/km100.code/code/test.md')

    sys.exit(0)

    dirpath = '/repo/github/km100.code/md'
    list_of_files = {}
    for (dirpath, dirnames, filenames) in os.walk(dirpath):
        for filename in filenames:
            if filename.endswith('.md'): 
#               list_of_files[filename] = os.sep.join([dirpath, filename])
                encode_md_file(os.sep.join([dirpath, filename]))

#    encode_md_file(md_file_path)
