import re

def reformat_zones():
    md_file = "/home/abosch/Projects/TheSignal/V1/01___Game_Board_New_Meridian.md"
    with open(md_file, "r") as f:
        content = f.read()

    # Find boundaries for 6.3 Detailed Zone Specifications
    start_str = "### 6.3 Detailed Zone Specifications"
    end_str = "### 6.4 Detailed District Specifications"
    
    start_idx = content.find(start_str)
    end_idx = content.find(end_str)
    
    if start_idx == -1 or end_idx == -1:
        print("Could not find section boundaries")
        return
        
    section = content[start_idx + len(start_str):end_idx]
    
    # Parse the section
    zones = []
    current_zone = {}
    lines = section.strip().split('\n')
    
    for line in lines:
        if line.startswith('#### '):
            if current_zone:
                zones.append(current_zone)
            current_zone = {
                'description': ''
            }
        elif '| `db_id` |' in line:
            current_zone['db_id'] = line.split('|')[2].strip()
        elif '| `zone_id` |' in line:
            current_zone['zone_id'] = line.split('|')[2].strip()
        elif '| `zone_name` |' in line:
            current_zone['zone_name'] = line.split('|')[2].strip()
        elif '| `parent_zone_id` |' in line:
            current_zone['parent_zone_id'] = line.split('|')[2].strip()
        elif '| `visibility` |' in line:
            current_zone['visibility'] = line.split('|')[2].strip()
        elif line.startswith('* **Description:**'):
            current_zone['description'] = line.replace('* **Description:**', '').strip()
    
    if current_zone:
        zones.append(current_zone)
        
    # Build the table
    table_lines = [
        "| Zone Name | DB ID | Zone ID | Parent Zone ID | Visibility | Description |",
        "|-----------|-------|---------|----------------|------------|-------------|"
    ]
    
    for z in zones:
        desc = z.get('description', '')
        # Handle cases where description was missing
        table_lines.append(f"| {z.get('zone_name', '')} | {z.get('db_id', '')} | {z.get('zone_id', '')} | {z.get('parent_zone_id', '')} | {z.get('visibility', '')} | {desc} |")
        
    table_text = "\n\n" + "\n".join(table_lines) + "\n\n"
    
    new_content = content[:start_idx + len(start_str)] + table_text + content[end_idx:]
    
    with open(md_file, "w") as f:
        f.write(new_content)
    print("Zones table reformatted.")

if __name__ == "__main__":
    reformat_zones()
