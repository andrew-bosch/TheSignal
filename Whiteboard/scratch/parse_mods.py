import re

with open("V1/04___Card_System.md") as f:
    text = f.read()

# Find all blocks looking like [FAC].MOD.[num] = Card( ... name = "..."
matches = re.finditer(r'([A-Z]{3}\.MOD\.\d+)\s*=\s*Card\([^)]*name\s*=\s*"([^"]+)"', text, re.DOTALL)

for match in matches:
    print(f"{match.group(1)} - {match.group(2)}")
