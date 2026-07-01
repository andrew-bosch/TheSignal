import re

def reformat_districts():
    md_file = "/home/abosch/Projects/TheSignal/V1/01___Game_Board_New_Meridian.md"
    with open(md_file, "r") as f:
        content = f.read()

    start_str = "### 6.4 Detailed District Specifications"
    end_str = "### 6.5 District Adjacency Map"
    
    start_idx = content.find(start_str)
    end_idx = content.find(end_str)
    
    if start_idx == -1 or end_idx == -1:
        print("Could not find section boundaries")
        return
        
    section = content[start_idx + len(start_str):end_idx]
    
    districts = []
    current = {}
    lines = section.strip().split('\n')
    
    for line in lines:
        if line.startswith('##### '):
            if current:
                districts.append(current)
            current = {
                'description': ''
            }
        elif '| `db_id` |' in line:
            current['db_id'] = line.split('|')[2].strip()
        elif '| `district_name` |' in line:
            current['name'] = line.split('|')[2].strip()
        elif '| `ring` |' in line:
            current['ring'] = line.split('|')[2].strip()
        elif '| `resource_type` |' in line:
            current['resource'] = line.split('|')[2].strip()
        elif '| `base_generation_value` |' in line:
            current['gen'] = line.split('|')[2].strip()
        elif '| `hex_color` |' in line:
            current['hex'] = line.split('|')[2].strip()
        elif line.startswith('* **Narrative Description:**'):
            current['description'] = line.replace('* **Narrative Description:**', '').strip()
    
    if current:
        districts.append(current)
        
    # Build the table
    table_lines = [
        "| District Name | DB ID | Ring | Resource Type | Base Gen | Hex Color | Description |",
        "|---------------|-------|------|---------------|----------|-----------|-------------|"
    ]
    
    for d in districts:
        desc = d.get('description', '')
        table_lines.append(f"| {d.get('name', '')} | {d.get('db_id', '')} | {d.get('ring', '')} | {d.get('resource', '')} | {d.get('gen', '')} | {d.get('hex', '')} | {desc} |")
        
    table_text = "\n\nAll 21 districts of New Meridian function as child zones of their respective rings.\n\n" + "\n".join(table_lines) + "\n\n"
    
    new_content = content[:start_idx + len(start_str)] + table_text + content[end_idx:]
    
    with open(md_file, "w") as f:
        f.write(new_content)
    print("Districts table reformatted.")

if __name__ == "__main__":
    reformat_districts()
