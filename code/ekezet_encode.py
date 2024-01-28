#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def encode_anchor(match):
    anchor = match.group(1)
    encoded_anchor = re.sub(r'([^a-zA-Z0-9])', lambda x: f'&#{ord(x.group(1))};', anchor)
    return f'({encoded_anchor})'

def encode_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

#    pattern = r'\(([^)]+)\)'
    pattern = r'\(\#([^)]+)\)'
    encoded_content = re.sub(pattern, encode_anchor, content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(encoded_content)

if __name__ == "__main__":
    md_file_path = '../md/010_karakteralkotas.md'
    encode_md_file(md_file_path)

