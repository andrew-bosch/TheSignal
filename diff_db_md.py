import re
import subprocess

with open("/home/abosch/Projects/TheSignal/V1/04___Card_System.md", "r") as f:
    text = f.read()

matches = re.findall(r'```python\n(.*?)\n```', text, re.DOTALL)
md_ids = set()
for m in matches:
    id_match = re.search(r'\s+id\s*=\s*"([^"]+)"', m)
    if id_match:
        md_ids.add(id_match.group(1))

# Get db ids
result = subprocess.run(['mysql', 'the_signal_db', '-e', 'SELECT card_ID FROM card_status;'], capture_output=True, text=True)
db_ids = set(result.stdout.split()[1:])

print(f"In DB but not in MD ({len(db_ids - md_ids)}):")
for i in sorted(db_ids - md_ids):
    print(i)

print(f"In MD but not in DB ({len(md_ids - db_ids)}):")
for i in sorted(md_ids - db_ids):
    print(i)
