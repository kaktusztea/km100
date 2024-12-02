import os.path
# https://stackoverflow.com/questions/66185838/convert-markdown-table-to-json-with-python

md_table = """
| Some Title | Some Description             | Some Number |
|------------|------------------------------|-------------|
| Dark Souls | This is a fun game           | 5           |
| Bloodborne | This one is even better      | 2           |
| Sekiro     | This one is also pretty good | 110101      |
"""


path='c:\data\km100.code\data\fegyverek.md'
md_table = None
data = {}

with open(path, 'r') as fh:
    md_table = fh.read()

result = []

for n, line in enumerate(md_table[1:-1].split('\n')):

    if n == 0:
        header = [t.strip() for t in line.split('|')[1:-1]]
    if n > 1:
        values = [t.strip() for t in line.split('|')[1:-1]]
        for col, value in zip(header, values):
            data[col] = value
        result.append(data)

print(data)
