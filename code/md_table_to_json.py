#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://stackoverflow.com/questions/66185838/convert-markdown-table-to-json-with-python

from pathlib import Path
import json
import sys
import os
import re

class MdToJsonConverter:

    def __init__(self, path_md, path_json):
        self.path_md = path_md
        self.path_json = path_json
        self.raw_md = None
        self.raw_json = []

        self.tag_start = '<!-- tag: md_table_start -->'
        self.tag_end = '<!-- tag: md_table_end -->'
        self.filter_out_chars = ['**', '`']

        self.read_md()
        self.filter_raw_md()
        self.get_table_sections_from_raw_md()
        self.convert_md_to_json()
        # self.order_json_by_fegyver_name()         # TODO: kell ez?

    def read_md(self):
        with open(path_md, 'r') as fh:
            self.raw_md = fh.read()

    def filter_raw_md(self):
        """
        Filter unnecessary strings from raw markdown data
        """
        for ch in self.filter_out_chars:
            self.raw_md = self.raw_md.replace(ch, '')

    def get_table_sections_from_raw_md(self):
        """
        Filter markdown table code from raw markdown data
        """
        ## BUG: bad code here

        blocks = re.split(rf'{self.tag_start}|{self.tag_end}', self.raw_md)
        # print(f"BATMAN-1: {blocks}")
        blocks = [block.strip() for block in blocks if block.strip()]
        # print(f"BATMAN-2: {blocks}")
        blocks = [block for block in blocks if block != self.tag_start]
        print(f"BATMAN-3: {blocks}")
        self.raw_md = '\n'.join(blocks)
        # print(json.dumps(self.raw_md))      # DEBUG

        # TODO: handle multiple sections


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

    def order_json_by_fegyver_name(self):
        """"
        Order json by fegyver nev
        """
        pass
        # TODO: kell ez?? Lehet, hogy jó a meglevő sorrend

    def write_json(self, path_json=None):
        if not path_json:
            path_json = self.path_json
        with open(path_json, 'w', encoding="utf-8") as fj:
            json.dump(self.raw_json, fj, ensure_ascii=False, indent=4)

    def get_json_data(self):
        return self.raw_json


def write_out_to_json(path_json, raw_json):
    with open(path_json, 'w', encoding="utf-8") as fj:
        fj.seek(0)
        fj.truncate()
        json.dump(raw_json, fj, ensure_ascii=False, indent=4)



if __name__ == "__main__":

    dir_code = os.path.dirname(os.path.abspath(__file__))
    dir_data_root = os.path.join(Path(dir_code).parent, 'data')
    dir_md_root = os.path.join(Path(dir_code).parent, 'md')


    fegyver_raw_md_files = [f for f in os.listdir(dir_md_root) if f.endswith('_fegyverek.md')]

    # print(fegyver_raw_md_files)                                                                 # DEBUG

    full_json = []
    for fegyver_file in fegyver_raw_md_files:
        path_md = os.path.join(dir_md_root, fegyver_file)
        mjc = MdToJsonConverter(path_md, None)
        # print(mjc.get_json_data())                                                               # DEBUG
        # full_json.append(mjc.get_json_data())

    # print(full_json)                                                                            # DEBUG

    path_json=os.path.join(dir_data_root, "fegyverek.json")
    write_out_to_json(path_json, full_json)
