#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import jinjaHandler
import sys

template_dir =  sys.argv[1]
template_path =  sys.argv[2]
context = sys.argv[3]
outputfile = sys.argv[4]

jh = jinjaHandler.JinjaHandler(template_dir=template_dir, template_path=template_path, context=context)

jh.render_write(outputfile=outputfile)
