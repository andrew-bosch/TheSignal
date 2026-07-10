import re

with open("/home/abosch/Projects/TheSignal/V1/04___Card_System.md", "r") as f:
    text = f.read()

matches = re.findall(r'class \w+\((?:ActionCard|ModifierCard|PublicActionCard|Card)\):', text)
print(f"Total card classes: {len(matches)}")
