import re
import subprocess

MD_FILE = "/home/abosch/Projects/TheSignal/V1/04___Card_System.md"
DB_NAME = "the_signal_db"

def run_sql(query):
    subprocess.run(["mysql", DB_NAME, "-e", query], check=True)

with open(MD_FILE, "r") as f:
    content = f.read()

# We need to find the blocks for:
# 1. All ModReact cards (id contains .MOD.)
# 2. GUI.CA.4, GUI.PA.1, GUI.CA.7, GUI.PA.3, GUI.PA.4, GUI.PA.5

target_ids = ["GUI.CA.4", "GUI.PA.1", "GUI.CA.7", "GUI.CA.8", "GUI.PA.3", "GUI.PA.4", "GUI.PA.5", "GUI.PA.6", "GUI.PA.7", "GUI.PA.8", "GHO.CA.13", "GHO.CA.14", "GHO.MOD.9", "GHO.MOD.10", "DIR.PA.7", "DIR.PA.8", "NET.PA.4", "NET.PA.5", "NET.PA.6", "NET.MOD.11", "SYN.PA.4", "SYN.PA.5", "GHO.CA.15", "GHO.MOD.11", "NET.MOD.12"]
card_blocks = content.split("Card(")[1:]

def parse_cost(cost_str, faction_name):
    cost_str = cost_str.strip().strip(",")
    if not cost_str or cost_str == "None":
        return "'free'", 0, 0
    
    # Example: resource.faction(Guild).capacity * 2 + resource.faction(Guild).findings * 1
    # Example: resource.faction(acting).capacity * 2 + resource.faction(acting).findings * 1
    parts = cost_str.split("+")
    is_cross = len(parts) > 1
    
    primary_amount = "NULL"
    native_count = len(parts)
    
    # Try to extract the first multiplier as primary amount
    match = re.search(r'\*\s*(\d+)', parts[0])
    if match:
        primary_amount = match.group(1)
        
    cost_type = "'cross'" if is_cross else "'mono'"
    
    return cost_type, primary_amount, native_count

def escape(val):
    if not val:
        return "NULL"
    return "'" + val.replace("'", "''") + "'"

for block in card_blocks:
    id_match = re.search(r'id\s*=\s*[\"\']?([A-Z]{3}\.(CA|PA|MOD)\.\d+)[\"\']?', block)
    if not id_match:
        # maybe int id? skip for now, we only care about named IDs
        continue
        
    card_id = id_match.group(1)
    is_mod = ".MOD." in card_id
    is_target = card_id in target_ids
    
    if not (is_mod or is_target):
        continue
        
    # Extract faction
    faction = "Standard"
    fac_match = re.search(r'faction\s*=\s*([A-Za-z]+)', block)
    if fac_match:
        faction = fac_match.group(1)
        if faction == "acting":
            faction = "Standard"
            
    # Extract card_type
    card_type = "MOD" if ".MOD." in card_id else ("CA" if ".CA." in card_id else "PA")
    
    # Extract name
    name_match = re.search(r'name\s*=\s*\"(.*?)\"', block)
    name = name_match.group(1) if name_match else card_id
    
    # Extract taxonomy
    layer_match = re.search(r'layer\s*=\s*([A-Za-z]+)', block)
    func_match = re.search(r'function\s*=\s*([A-Za-z]+)', block)
    subj_match = re.search(r'subject\s*=\s*([A-Za-z]+)', block)
    beat_match = re.search(r'beat\s*=\s*(\d+)', block)
    
    layer = layer_match.group(1) if layer_match else None
    func = func_match.group(1) if func_match else None
    subj = subj_match.group(1) if subj_match else None
    beat = beat_match.group(1) if beat_match else "NULL"
    
    # Extract cost
    cost_match = re.search(r'cost\s*=\s*(.*?)\n', block)
    if cost_match:
        cost_str = cost_match.group(1)
        cost_type, cost_primary, cost_native_count = parse_cost(cost_str, faction)
    else:
        cost_type, cost_primary, cost_native_count = "'free'", "NULL", 0
        
    # Check if uses_intel_token
    uses_intel = 1 if "IntelToken" in block and "cost" in block else 0

    sql = f"""
    INSERT INTO card_status (
        card_id, name, faction, card_type, 
        layer, function, subject, beat,
        cost_type, cost_primary_amount, cost_native_count, uses_intel_token, blocked
    ) VALUES (
        '{card_id}', {escape(name)}, '{faction}', '{card_type}',
        {escape(layer)}, {escape(func)}, {escape(subj)}, {beat},
        {cost_type}, {cost_primary}, {cost_native_count}, {uses_intel}, 0
    ) ON DUPLICATE KEY UPDATE 
        name=VALUES(name), faction=VALUES(faction), card_type=VALUES(card_type),
        layer=VALUES(layer), function=VALUES(function), subject=VALUES(subject), beat=VALUES(beat),
        cost_type=VALUES(cost_type), cost_primary_amount=VALUES(cost_primary_amount), 
        cost_native_count=VALUES(cost_native_count), uses_intel_token=VALUES(uses_intel_token);
    """
    
    # Wait, card_id is NOT a primary key or unique key in card_status!
    # The primary key is `id` INT AUTO_INCREMENT. 
    # I should use UPDATE if exists, else INSERT.
    
    check_sql = f"SELECT id FROM card_status WHERE card_id = '{card_id}';"
    res = subprocess.run(["mysql", DB_NAME, "-s", "-N", "-e", check_sql], capture_output=True, text=True)
    existing_id = res.stdout.strip()
    
    if existing_id:
        update_sql = f"""
        UPDATE card_status SET
            name={escape(name)}, faction='{faction}', card_type='{card_type}',
            layer={escape(layer)}, function={escape(func)}, subject={escape(subj)}, beat={beat},
            cost_type={cost_type}, cost_primary_amount={cost_primary}, 
            cost_native_count={cost_native_count}, uses_intel_token={uses_intel}
        WHERE id = {existing_id};
        """
        run_sql(update_sql)
        print(f"Updated {card_id}")
    else:
        insert_sql = f"""
        INSERT INTO card_status (
            card_id, name, faction, card_type, 
            layer, function, subject, beat,
            cost_type, cost_primary_amount, cost_native_count, uses_intel_token, blocked
        ) VALUES (
            '{card_id}', {escape(name)}, '{faction}', '{card_type}',
            {escape(layer)}, {escape(func)}, {escape(subj)}, {beat},
            {cost_type}, {cost_primary}, {cost_native_count}, {uses_intel}, 0
        );
        """
        run_sql(insert_sql)
        print(f"Inserted {card_id}")
