def update_md():
    with open("adj_view.tsv", "r") as f:
        lines = f.readlines()
        
    table_lines = []
    table_lines.append("| Ring | Address | Origin District | Adjacent Ring | Adjacent Address | Adjacent District | Allow Ingress | Allow Egress |")
    table_lines.append("|------|---------|----------------|--------------|-----------------|-------------------|--------------|-------------|")
    
    for row in lines[1:]: # skip header
        parts = row.strip('\n').split('\t')
        if len(parts) >= 8:
            ing = "TRUE" if parts[6] == '1' else "FALSE"
            egr = "TRUE" if parts[7] == '1' else "FALSE"
            table_lines.append(f"| {parts[0]} | {parts[1]} | {parts[2]} | {parts[3]} | {parts[4]} | {parts[5]} | {ing} | {egr} |")

    table_text = "\n".join(table_lines) + "\n\n"
    
    md_file = "/home/abosch/Projects/TheSignal/V1/01___Game_Board_New_Meridian.md"
    with open(md_file, "r") as f:
        lines = f.readlines()

    # Find the start of the table
    start_idx = -1
    for i, line in enumerate(lines):
        if line.startswith("| District ID (`district_id`)"):
            start_idx = i
            break
            
    if start_idx != -1:
        # Find the end of the table
        end_idx = start_idx
        while end_idx < len(lines) and lines[end_idx].startswith("|"):
            end_idx += 1
            
        new_lines = lines[:start_idx] + [table_text] + lines[end_idx:]
        
        with open(md_file, "w") as f:
            f.writelines(new_lines)
        print("Markdown table updated back to human readable view successfully.")
    else:
        print("Could not find start marker.")

if __name__ == "__main__":
    update_md()
