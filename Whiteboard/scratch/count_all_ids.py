import re

with open("/home/abosch/Projects/TheSignal/V1/04___Card_System.md", "r") as f:
    text = f.read()

matches = re.findall(r'```python\n(.*?)\n```', text, re.DOTALL)
ids = set()
for m in matches:
    # Match id = "XXX" or card_id = "XXX"
    id_match = re.search(r'(?:id|card_id)\s*=\s*"([^"]+)"', m)
    if id_match:
        ids.add(id_match.group(1))

print(f"Total Unique IDs in MD python blocks: {len(ids)}")
