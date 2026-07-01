def update_md_table():
    with open("adj.tsv", "r") as f:
        lines = f.readlines()
        
    table_lines = []
    table_lines.append("| District ID (`district_id`) | Adjacent District ID (`adjacent_district_id`) | Allow Ingress (`allow_ingress`) | Allow Egress (`allow_egress`) |")
    table_lines.append("|-----------------------------|-----------------------------------------------|---------------------------------|-------------------------------|")
    
    for row in lines[1:]: # skip header
        parts = row.strip().split('\t')
        if len(parts) >= 4:
            ing = "TRUE" if parts[2] == '1' else "FALSE"
            egr = "TRUE" if parts[3] == '1' else "FALSE"
            table_lines.append(f"| {parts[0]} | {parts[1]} | {ing} | {egr} |")

    table_text = "\n".join(table_lines)
    
    md_file = "/home/abosch/Projects/TheSignal/V1/01___Game_Board_New_Meridian.md"
    with open(md_file, "r") as f:
        content = f.read()

    start_marker = "| Ring | Address | Origin District | Adjacent Ring | Adjacent Address | Adjacent District | Allow Ingress | Allow Egress |"
    if start_marker in content:
        start_idx = content.find(start_marker)
        end_idx = content.find("\n\n", start_idx)
        
        new_content = content[:start_idx] + table_text + content[end_idx:]
        
        with open(md_file, "w") as f:
            f.write(new_content)
        print("Markdown table updated.")
    else:
        print("Could not find start marker.")

if __name__ == "__main__":
    update_md_table()
