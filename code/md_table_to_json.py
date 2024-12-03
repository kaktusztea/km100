#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import json
import os

class MdToJsonConverter:

    def __init__(self, path_md, path_json, filepattern, table_pattern, skip_columns):
        self.path_md = path_md
        self.path_json = path_json

        self.raw_md = None
        self.raw_json = []
        self.filepattern = filepattern

        self.tag_start = f"<!-- tag: md_table_{table_pattern}_start -->"
        self.tag_end = f"<!-- tag: md_table_{table_pattern}_end -->"
        self.filter_out_chars = ['**', '`', '⭕TODO⭕', '⭕TODO', '⭕']
        self.skip_columns = skip_columns

        self.read_md()
        self.filter_raw_md()
        self.get_table_sections_from_raw_md()
        self.convert_md_to_json()
        # self.order_json_by_fegyver_name()

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
        extracted_lines = []
        is_between_markers = False

        for line in self.raw_md.split("\n"):
            if self.tag_start in line:
                is_between_markers = True
                continue
            if self.tag_end in line:
                is_between_markers = False
                break
            if is_between_markers:
                extracted_lines.append(line.strip())
        self.raw_md = "\n".join(extracted_lines)

    def convert_md_to_json(self):
        for n, line in enumerate(self.raw_md[1:-1].split('\n')):
            data = {}
            if n == 0:
                header = [t.strip() for t in line.split('|')[1:-1]]
            if n > 1:
                values = [t.strip() for t in line.split('|')[1:-1]]
                for col, value in zip(header, values):
                    if col not in self.skip_columns:
                        data[col] = value
                self.raw_json.append(data)
            n += 1

    def order_json_by_fegyver_name(self):
        """"
        Order json by fegyver nev
        """
        pass

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
    dir_data = os.path.join(Path(dir_code).parent, 'data')
    dir_md = os.path.join(Path(dir_code).parent, 'md')

    data = [
       {
        'id':'fegyverek',
        'output':'fegyverek.json',
        'file_pattern': 'fegyverek.md',
        'table_pattern': 'fegyver',
        'skip_columns': []
       },
       {
        'id':'kepzettseg_kp',
        'output':'kepzettseg_kp.json',
        'file_pattern': 'kepzettsegszintek_kp_igenye.md',
        'table_pattern': 'kepzettsegkp',
        'skip_columns': ['Fokozat']
       },
    ]

    for d in data:
        path_json = os.path.join(dir_data, d['output'])
        full_json = []
        for fname in os.listdir(dir_md):
            if (d['file_pattern']) in fname:
                path_md = os.path.join(dir_md, fname)
                mjc = MdToJsonConverter(path_md, None, d['file_pattern'], d['table_pattern'], d['skip_columns'])
                full_json.extend(mjc.get_json_data())
        path_json=os.path.join(dir_data, d['output'])
        write_out_to_json(path_json, full_json)
