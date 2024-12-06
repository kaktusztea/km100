#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

def order_list_of_dicts_by_key(list_dicts, sortkey):
    """"
    Order list of dicts  by key
    """
    return sorted(list_dicts, key=lambda x: x[sortkey].lower())


def write_list_of_dicts_to_jsonfile(path_json, list_dicts):
    with open(path_json, 'w', encoding="utf-8") as fj:
        fj.seek(0)
        fj.truncate()
        json.dump(list_dicts, fj, ensure_ascii=False, indent=4)
