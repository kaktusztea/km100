#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://stackoverflow.com/questions/66185838/convert-markdown-table-to-json-with-python

import json

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


## TODO: process all types of weapons. Retrieve it from  live .md files
path_md="/repo/github/km100.code/data/fegyverek.md"
path_json="/repo/github/km100.code/data/fegyverek.json"

mjc = MdToJsonConverter(path_md, path_json)
mjc.write_json()