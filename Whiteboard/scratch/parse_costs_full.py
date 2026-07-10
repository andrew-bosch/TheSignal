import re
import sys

def parse_cost_details(cost_line):
    if not cost_line or cost_line.strip() == "None" or cost_line.strip() == "0":
        return {"type": "free", "primary_amount": "NULL", "native_count": 0, "intel": 0, "variable": 0}
        
    intel = 1 if "IntelToken" in cost_line or "intel_token" in cost_line else 0
    variable = 1 if "count(" in cost_line or "+" in cost_line and " * " not in cost_line.split("+")[0] else 0  # naive but maybe works
    
    parts = [p.strip() for p in cost_line.split("+")]
    
    primary_amount = "NULL"
    native_count = 0
    is_cross = False
    
    for part in parts:
        # Extract multiplier e.g., '* 2' or '* 1'
        amt = 1
        m = re.search(r'\*\s*(\d+)', part)
        if m:
            amt = int(m.group(1))
            
        if "intel_token" in part.lower():
            intel = 1
            is_cross = True
            continue
            
        if "district" in part.lower() and "native" in part.lower():
            native_count += amt
            is_cross = True
            continue
            
        if "opponent" in part.lower() or "target_faction" in part.lower():
            is_cross = True
            
        # Check if this looks like a primary faction cost
        if "resource.faction" in part or "Resource(" in part or part.startswith("Capital") or part.startswith("Capacity") or part.startswith("Findings") or part.startswith("Exposure") or part.startswith("Mandate"):
            if primary_amount == "NULL":
                primary_amount = amt
            else:
                is_cross = True # multiple distinct faction resources
                
    if len(parts) > 1:
        is_cross = True
        
    cost_type = "cross" if is_cross else "mono"
    if "any_resource" in cost_line.lower() or "any" in cost_line.lower():
        cost_type = "cross"
        
    return {
        "type": cost_type,
        "primary_amount": primary_amount,
        "native_count": native_count,
        "intel": intel,
        "variable": 1 if variable or "X" in cost_line else 0
    }

with open("/home/abosch/Projects/TheSignal/V1/04___Card_System.md", "r") as f:
    text = f.read()

matches = re.findall(r'```python\n(.*?)\n```', text, re.DOTALL)
updates = []
for m in matches:
    id_match = re.search(r'(?:id|card_id)\s*=\s*"([^"]+)"', m)
    if not id_match:
        continue
    card_id = id_match.group(1)
    
    cost_match = re.search(r'cost\s*=\s*(.+?)(?:,\n|,\r\n|\n)', m)
    if not cost_match:
        continue
    
    cost_val = cost_match.group(1).strip()
    details = parse_cost_details(cost_val)
    
    updates.append(f"UPDATE card_status SET cost_type = '{details['type']}', cost_variable = {details['variable']}, cost_primary_amount = {details['primary_amount']}, cost_native_count = {details['native_count']}, uses_intel_token = {details['intel']} WHERE card_ID = '{card_id}';")

with open("update_costs_full.sql", "w") as f:
    f.write("\n".join(updates))
    
print(f"Generated {len(updates)} full update statements.")
