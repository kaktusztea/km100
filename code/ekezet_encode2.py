#!/usr/bin/env python3

import os
import re
import urllib.parse

# iterate over all files in current directory and subdirectories
for dirpath, dirnames, filenames in os.walk('.'):
    for filename in filenames:
        if filename.endswith('.md'):
            filepath = os.path.join(dirpath, filename)

            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # find URLs using a regex and replace them with their encoded versions
            content_new = re.sub(
                r'\(\s*([^)\s]+\.[^)\s]+)\s*\)',  # capture the URL in parentheses
                lambda m: '(' + urllib.parse.quote(m.group(1), safe="/:#@[]!$&'()*+,;=%") + ')',  # replace with encoded URL
                content
            )

            # write the modified content back to the file
            if content != content_new:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content_new)
