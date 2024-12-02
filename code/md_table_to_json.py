#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://stackoverflow.com/questions/66185838/convert-markdown-table-to-json-with-python

import json
import os

class MdToJsonConverter:

    def __init__(self, path_md, path_json):
        self.path_md = path_md
        self.path_json = path_json
        self.raw_md = None
        self.raw_json = []

        self.read_md()
        self.convert_md_to_json()

    def read_md(self):
        with open(path_md, 'r') as fh:
            self.raw_md = fh.read()

    def convert_md_to_json(self):
        for n, line in enumerate(self.raw_md[1:-1].split('\n')):
            data = {}
            if n == 0:
                header = [t.strip() for t in line.split('|')[1:-1]]
            if n > 1:
                values = [t.strip() for t in line.split('|')[1:-1]]
                for col, value in zip(header, values):
                    data[col] = value
                self.raw_json.append(data)
            n += 1

    def write_json(self, path_json=None):
        if not path_json:
            path_json = self.path_json
        with open(path_json, 'w', encoding="utf-8") as fj:
            json.dump(self.raw_json, fj, ensure_ascii=False, indent=4)

    def get_json_data(self):
        return self.raw_json


def write_json(path_json, raw_json):
    with open(path_json, 'w', encoding="utf-8") as fj:
        fj.seek(0)
        json.dump(raw_json, fj, ensure_ascii=False, indent=4)


dir_code = os.path.dirname(os.path.abspath(__file__))
dir_md_root = os.path.join(dir_code, '../md')

fegyver_files = ['068_02_kozelharci_fegyverek.md',
                 '068_03_kardvivo_fegyverek.md',
                 '068_04_zuzo_fegyverek.md',
                 '068_05_landzsavivo_fegyverek.md']


raw_full_json = []
for fegyver_file in fegyver_files:
    path_md = os.path.join(dir_md_root, fegyver_file)
    mjc = MdToJsonConverter(path_md)
    raw_full_json.append(mjc.get_json_data())


path_json="/repo/github/km100.code/data/fegyverek.json"
write_json(path_json, raw_full_json)


# mjc = MdToJsonConverter(path_md, path_json)
# mjc.write_json()

