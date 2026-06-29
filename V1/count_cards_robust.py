import re

with open("/home/abosch/Projects/TheSignal/V1/04___Card_System.md", "r") as f:
    content = f.read()

# Find all occurrences of Card(
# We'll look for `id = "XXX.YY.Z"` or `id="XXX.YY.Z"` or `id = 5`
card_blocks = content.split("Card(")[1:]

counts = {"STD": 0, "GUI": 0, "GHO": 0, "DIR": 0, "NET": 0, "SYN": 0, "UNKNOWN": 0}
all_ids = []

for block in card_blocks:
    # Look for the id parameter
    match = re.search(r'id\s*=\s*(.*?)[,\n]', block)
    if match:
        raw_id = match.group(1).strip('"\'')
        all_ids.append(raw_id)
        
        # Determine prefix
        prefix = raw_id.split('.')[0] if '.' in raw_id else None
        
        if prefix in counts:
            counts[prefix] += 1
        elif isinstance(raw_id, str) and raw_id.isdigit():
            # some early STD cards might just have integer IDs like id = 5
            counts["STD"] += 1
        else:
            # Let's check if the block has faction = Standard
            if re.search(r'faction\s*=\s*(All|Standard)', block):
                counts["STD"] += 1
            elif re.search(r'faction\s*=\s*Guild', block):
                counts["GUI"] += 1
            elif re.search(r'faction\s*=\s*Ghost', block):
                counts["GHO"] += 1
            elif re.search(r'faction\s*=\s*Directorate', block):
                counts["DIR"] += 1
            elif re.search(r'faction\s*=\s*Network', block):
                counts["NET"] += 1
            elif re.search(r'faction\s*=\s*Syndicate', block):
                counts["SYN"] += 1
            else:
                counts["UNKNOWN"] += 1
    else:
        counts["UNKNOWN"] += 1

print("Card counts by identified faction:")
for k, v in counts.items():
    print(f"{k}: {v}")
    
std_count = counts.get('STD', 0)
for k, v in counts.items():
    if k not in ('STD', 'UNKNOWN'):
        print(f"Total playable palette for {k}: {std_count + v}")

# Let's also print all STD cards to see why we counted 20 or 24
print("\nSTD Cards found:")
for cid in all_ids:
    if isinstance(cid, str) and cid.startswith("STD."):
        print(cid)
    elif str(cid).isdigit():
        print(f"STD card with int ID: {cid}")
