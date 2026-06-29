import re

with open("/home/abosch/Projects/TheSignal/V1/04___Card_System.md", "r") as f:
    content = f.read()

card_blocks = content.split("Card(")[1:]
for i, block in enumerate(card_blocks):
    id_match = re.search(r'id\s*=\s*"([^"]+)"', block)
    if id_match:
        card_id = id_match.group(1)
        if not re.match(r'^[A-Z]{3}\.(CA|PA|MOD)\.[0-9]+$', card_id):
            name_match = re.search(r'name\s*=\s*"([^"]+)"', block)
            name = name_match.group(1) if name_match else "UNKNOWN NAME"
            print(f"Untracked/Bad ID: {card_id} | Name: {name}")
    else:
        id_match2 = re.search(r'id\s*=\s*([A-Za-z0-9_-]+)', block)
        if id_match2:
             card_id = id_match2.group(1)
             if not re.match(r'^[A-Z]{3}\.(CA|PA|MOD)\.[0-9]+$', card_id):
                name_match = re.search(r'name\s*=\s*"([^"]+)"', block)
                name = name_match.group(1) if name_match else "UNKNOWN NAME"
                print(f"Untracked/Bad ID: {card_id} | Name: {name}")

