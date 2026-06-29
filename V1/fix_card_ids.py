import re
import subprocess

DB_NAME = "the_signal_db"
MD_FILE = "/home/abosch/Projects/TheSignal/V1/04___Card_System.md"

# Get mapping of name -> card_id from DB
res = subprocess.run(["mysql", DB_NAME, "-s", "-N", "-e", "SELECT name, card_id FROM card_status;"], capture_output=True, text=True)
db_map = {}
for line in res.stdout.strip().split('\n'):
    if not line: continue
    parts = line.split('\t')
    if len(parts) == 2:
        name, card_id = parts
        db_map[name.strip()] = card_id.strip()

with open(MD_FILE, "r") as f:
    content = f.read()

# Fix integer IDs using the variable name.
# Pattern: VAR_NAME = Card(\n    id      = INT,
# Example: STD.CA.1 = Card(\n    id      = 1,
def replace_int_id(match):
    var_name = match.group(1)
    # The original id line including spacing
    id_line = match.group(2)
    # Extract the int
    int_val = match.group(3)
    
    # We want to replace just the int with "VAR_NAME"
    new_id_line = id_line.replace(f"id      = {int_val}", f"id      = \"{var_name}\"")
    # Some might just have `id = 1`
    new_id_line = re.sub(r'id(\s*)=(\s*)' + str(int_val) + r',', r'id\1=\2"' + var_name + '",', id_line)
    
    return f"{var_name} = Card({new_id_line}"

content = re.sub(r'([A-Z]{3}\.(?:CA|PA|MOD)\.\d+)\s*=\s*Card\(([^)]*?id\s*=\s*(\d+)\s*,)', replace_int_id, content, flags=re.DOTALL)


# Fix placeholder IDs using the name field
# We will iterate through all blocks, extract name, check db_map, and if id is not matching, replace it.
card_blocks = content.split(" = Card(")
new_content = card_blocks[0]

for block in card_blocks[1:]:
    # block is everything after " = Card(" up to the next one.
    name_match = re.search(r'name\s*=\s*"([^"]+)"', block)
    if name_match:
        name = name_match.group(1)
        if name in db_map:
            correct_id = db_map[name]
            # Replace id field if it exists
            # We look for id = "...", id = TBD, id = —
            # Note: need to handle various spacing and quotes
            block = re.sub(r'id\s*=\s*(?:"[^"]*"|TBD|—|[A-Za-z0-9_-]+)\s*,', f'id      = "{correct_id}",', block, count=1)
            
    new_content += " = Card(" + block

with open(MD_FILE, "w") as f:
    f.write(new_content)

print("Cleanup complete.")
