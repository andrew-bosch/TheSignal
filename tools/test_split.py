import re
line = r"| Balance | ✓ | Some note with \| pipe | Art 05 |"
line = line.strip()
if line.startswith('|'): line = line[1:]
if line.endswith('|'): line = line[:-1]
parts = re.split(r'(?<!\\)\|', line)
parts = [p.strip().replace('\\|', '|') for p in parts]
print(parts)
