import re
import sys

def parse_cost_line(cost_line):
    if not cost_line or cost_line.strip() == "None":
        return "free"
    if "+" in cost_line or "district_native" in cost_line or "IntelToken" in cost_line or "intel_token" in cost_line or "opponent" in cost_line or "target_faction" in cost_line:
        return "cross"
    return "mono"

with open("/home/abosch/Projects/TheSignal/V1/04___Card_System.md", "r") as f:
    text = f.read()

matches = re.findall(r'```python\n(.*?)\n```', text, re.DOTALL)
updates = []
for m in matches:
    id_match = re.search(r'(?:id|card_id)\s*=\s*"([^"]+)"', m)
    if not id_match:
        continue
    card_id = id_match.group(1)
    
    # Try to find cost
    cost_match = re.search(r'cost\s*=\s*(.+?)(?:,|\n)', m)
    if not cost_match:
        continue
    
    cost_val = cost_match.group(1).strip()
    cost_type = parse_cost_line(cost_val)
    
    updates.append(f"UPDATE card_status SET cost_type = '{cost_type}' WHERE card_ID = '{card_id}';")

with open("update_costs.sql", "w") as f:
    f.write("\n".join(updates))
    
print(f"Generated {len(updates)} update statements.")
