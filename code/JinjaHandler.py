#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import jinja2

import yaml

class JinjaHandler:
    def __init__(self, template_dir, template_path, context,
                 variable_start_string='{{', variable_end_string='}}',
                 block_start_string='{%', block_end_string='%}'):
        self.env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                                      variable_start_string=variable_start_string,
                                      variable_end_string=variable_end_string,
                                      block_start_string=block_start_string,
                                      block_end_string=block_end_string,
                                      trim_blocks=False,
                                      keep_trailing_newline=True)
        self.template_path = template_path
        self.name_template = os.path.basename(self.template_path)
        self.template = self.env.get_template(self.name_template)
        self.context = context

    def render(self):
        if isinstance(self.context, dict):
            ydata = yaml.safe_load(yaml.dump(self.context))
        else:
            ydata = yaml.safe_load(open(self.context, encoding="UTF-8"))
        return self.template.render(ydata)

    def render_write(self, outputfile=None):
        of = outputfile if outputfile else self.template_path
        print(f"[INFO] Rendering template: {self.template.name}")
        rendered_content = self.render()

        if not rendered_content:
            print(f"[WARNING] There was nothing to render, skipping: {of}")
            return
        try:
            mode = "wb" if of else "a+"
            with open(of, mode) as fh:
                fh.seek(0)
                fh.truncate()
                fh.write(rendered_content.encode('utf-8').strip())
        except (IOError, TypeError) as ioerr:
            raise Exception(f"[ERROR] Could not write context to {of}\n{ioerr}")
        print(f"[INFO] Applied context on {of}")
