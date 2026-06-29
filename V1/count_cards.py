import re

with open("/home/abosch/Projects/TheSignal/V1/04___Card_System.md", "r") as f:
    content = f.read()

# Find all cards like ID = Card(...)
matches = re.findall(r'^([A-Z]{3})\.(CA|PA|MOD)\.[0-9]+\s*=\s*Card\(', content, re.MULTILINE)

counts = {}
for prefix, _ in matches:
    counts[prefix] = counts.get(prefix, 0) + 1

print("Card counts by prefix:")
for k, v in counts.items():
    print(f"{k}: {v}")
    
std_count = counts.get('STD', 0)
for k, v in counts.items():
    if k != 'STD':
        print(f"Total playable palette for {k}: {std_count + v}")
