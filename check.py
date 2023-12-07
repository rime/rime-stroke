import re

with open('stroke.dict.yaml') as file:
    lines = file.readlines()

item2line: dict[tuple[str, str], int] = {}

start = lines.index('...\n') + 1

for i, line in enumerate(lines[start:], start=start+1):
    line = line.rstrip()
    if not line or line.startswith('#'):
        continue
    match = re.match(r'(\S+)\t(\S+)', line)
    if not match:
        print(f'Syntax error at line {i}')
        exit(1)
    key = (match.group(1), match.group(2))
    n = item2line.get(key)
    if n:
        print(f'Duplicated definition at line {n} and {i}: {line}')
        exit(1)
    item2line[key] = i
