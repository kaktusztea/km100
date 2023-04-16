#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://pythonhosted.org/Frozen-Flask/

import yaml
from flask import Flask, render_template, url_for, request, redirect
from markupsafe import escape

yy = None
with open("/Users/kaktusz/repo/km100.dok/data/example_fortely1.yaml", "r") as stream:
    try:
        yy = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

for kovetelmeny in yy['fokok'][1]['követelmények']:
    print(kovetelmeny['név'], ":", kovetelmeny['érték'])

kov1nev = yy['fokok'][1]['követelmények'][0]['név']
kov1ert = yy['fokok'][1]['követelmények'][0]['érték']


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', kov1nev=kov1nev, kov1ert=kov1ert)

if __name__ == "__main__":
    app.run(debug=True)
