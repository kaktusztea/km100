#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

class MdToJsonConverter:

    def __init__(self, path_md, path_json, params):
        self.path_md = path_md
        self.path_json = path_json

        if not isinstance(params, dict):
            raise Exception("MdToJsonConverter.init(): params is not dict")

        self.md = None
        self.list_dicts = []
        self.filepattern = params['file_pattern']
        self.table_pattern = params['table_pattern']
        self.sortkey = params['sortkey']

        self.tag_start = f"<!-- tag: md_table_{self.table_pattern}_start -->"
        self.tag_end = f"<!-- tag: md_table_{self.table_pattern}_end -->"
        self.filter_out_chars = ['**', '`', '⭕TODO⭕', '⭕TODO', '⭕']
        self.skip_columns = params['skip_columns']

        # execute processing
        self.read_md()
        self.filter_raw_md()
        self.get_table_sections_from_raw_md()
        self.convert_md_to_json()
        self.order_json_by_key()

    def read_md(self):
        with open(self.path_md, 'r') as fh:
            self.md = fh.read()

    def filter_raw_md(self):
        """
        Filter unnecessary strings from raw markdown data
        """
        for ch in self.filter_out_chars:
            self.md = self.md.replace(ch, '')

    def get_table_sections_from_raw_md(self):
        """
        Filter markdown table code from raw markdown data
        """
        extracted_lines = []
        is_between_markers = False

        for line in self.md.split("\n"):
            if self.tag_start in line:
                is_between_markers = True
                continue
            if self.tag_end in line:
                is_between_markers = False
                break
            if is_between_markers:
                extracted_lines.append(line.strip())
        self.md = "\n".join(extracted_lines)

    def convert_md_to_json(self):
        for n, line in enumerate(self.md[1:-1].split('\n')):
            data = {}
            if n == 0:
                header = [t.strip() for t in line.split('|')[1:-1]]
            if n > 1:
                values = [t.strip() for t in line.split('|')[1:-1]]
                for col, value in zip(header, values):
                    if col not in self.skip_columns:
                        data[col] = value
                self.list_dicts.append(data)
            n += 1

    def order_json_by_key(self):
        """"
        Order json by sortkey value
        """
        if self.sortkey:
            self.list_dicts = sorted(self.list_dicts, key=lambda x: x[self.sortkey].lower())

    def write_json(self, path_json=None):
        if not path_json:
            path_json = self.path_json
        with open(path_json, 'w', encoding="utf-8") as fj:
            json.dump(self.list_dicts, fj, ensure_ascii=False, indent=4)

    def get_json_data(self):
        return self.list_dicts