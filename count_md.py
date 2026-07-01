import re

with open("/home/abosch/Projects/TheSignal/V1/04___Card_System.md", "r") as f:
    text = f.read()

# Find all blocks of python code for cards
matches = re.findall(r'```python\n(.*?)\n```', text, re.DOTALL)
count = 0
ids = []
for m in matches:
    if "Card" in m or "ActionCard" in m or "ModifierCard" in m or "PublicActionCard" in m:
        id_match = re.search(r'\s+id\s*=\s*"([^"]+)"', m)
        if id_match:
            ids.append(id_match.group(1))
            count += 1
print(f"Total cards found in Markdown: {count}")
print(f"Unique IDs: {len(set(ids))}")
