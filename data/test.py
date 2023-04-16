#!/usr/bin/env python3

import yaml

yy = None
with open("/Users/kaktusz/repo/km100.dok/data/example_fortely.yaml", "r") as stream:
    try:
        yy = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

for kovetelmeny in yy['fokok'][1]['követelmények']:
    print(kovetelmeny['név'], ":", kovetelmeny['érték'])

# for key, value in yy.items():
#     print(key, ":", value, "\n")
